#!/usr/bin/env python3
"""Host flow-game.html on the local network so observers can enter data from their phones.

    python3 serve.py            # http://localhost:8000 for the facilitator
    python3 serve.py --port 9000

The facilitator opens the localhost URL on this laptop. Everyone else on the same Wi-Fi
opens the "Others" URL (or scans the QR code from the game's Share button), picks a role,
and taps in data. The facilitator's browser tab is the single writer: joiners send taps
here, this server relays them to the facilitator's tab, and the tab broadcasts the updated
game back through here. Standard library only.
"""
import argparse
import json
import os
import queue
import secrets
import socket
import socketserver
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HERE = Path(__file__).resolve().parent
GAME = HERE / "flow-game.html"
BACKUP = HERE / "flow-game-session.json"
PING_SECONDS = 5
MAX_BODY = 4 * 1024 * 1024


def now_ms():
    return int(time.time() * 1000)


def lan_ip():
    """The address of the interface that routes off this machine. Nothing is sent."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


class Client:
    def __init__(self, role, as_, cid):
        self.id = secrets.token_hex(6)
        self.cid = cid  # the browser tab's id, so a reconnect replaces its old stream at once
        self.role = role  # 'host' or 'join'
        self.as_ = as_  # joiner's chosen role key
        self.q = queue.Queue()
        self.token = secrets.token_urlsafe(16) if role == "host" else None

    def send(self, event, data):
        self.q.put((event, data))

    def close(self):
        self.q.put(None)


class Hub:
    def __init__(self, join_url):
        self.join_url = join_url
        self.lock = threading.Lock()
        self.clients = {}
        self.host = None
        self.state = None  # last game JSON from the host, as a compact string
        self.save_timer = None

    # --- connections ---------------------------------------------------
    def _drop_cid(self, cid):
        """Forget every stream from this tab. Call with the lock held. True if the host left."""
        host_left = False
        for old in [x for x in self.clients.values() if cid and x.cid == cid]:
            self.clients.pop(old.id, None)
            old.close()
            if self.host is old:
                self.host = None
                host_left = True
        return host_left

    def connect(self, role, as_, cid):
        c = Client(role, as_, cid)
        with self.lock:
            host_left = self._drop_cid(cid)
            self.clients[c.id] = c
            if role == "host":
                old, self.host = self.host, c
                if old:
                    self.clients.pop(old.id, None)
                    old.send("demoted", "{}")
                    old.close()
            host_online = self.host is not None
            hello = {"t": now_ms(), "joinUrl": self.join_url, "isHost": role == "host", "hostOnline": host_online}
            if c.token:
                hello["token"] = c.token
            c.send("hello", json.dumps(hello))
            if role == "join" and self.state:
                c.send("state", self._wrap(self.state))
        if role == "host":
            self.broadcast_join("host", json.dumps({"online": True}))
        elif host_left:
            self.broadcast_join("host", json.dumps({"online": False}))
        self.send_presence()
        return c

    def close_all(self):
        with self.lock:
            clients, self.clients, self.host = list(self.clients.values()), {}, None
        for c in clients:
            c.close()

    def counts(self):
        """(host connected, number of phones) for the launcher window."""
        with self.lock:
            return self.host is not None, sum(1 for c in self.clients.values() if c.role == "join")

    def bye(self, cid):
        with self.lock:
            host_left = self._drop_cid(cid)
        if host_left:
            self.broadcast_join("host", json.dumps({"online": False}))
        self.send_presence()

    def disconnect(self, c):
        was_host = False
        with self.lock:
            self.clients.pop(c.id, None)
            if self.host is c:
                self.host = None
                was_host = True
        if was_host:
            self.broadcast_join("host", json.dumps({"online": False}))
        self.send_presence()

    def joiners(self):
        with self.lock:
            return [c for c in self.clients.values() if c.role == "join"]

    def broadcast_join(self, event, data):
        for c in self.joiners():
            c.send(event, data)

    def send_presence(self):
        with self.lock:
            host = self.host
            roles = [c.as_ for c in self.clients.values() if c.role == "join"]
        if host:
            host.send("presence", json.dumps({"roles": roles}))

    # --- game state ----------------------------------------------------
    @staticmethod
    def _wrap(state):
        return '{"t":%d,"s":%s}' % (now_ms(), state)

    def put_state(self, token, body):
        with self.lock:
            if not self.host or token != self.host.token:
                return False
            self.state = body
        msg = self._wrap(body)
        for c in self.joiners():
            c.send("state", msg)
        self.schedule_save()
        return True

    def schedule_save(self):
        with self.lock:
            if self.save_timer:
                self.save_timer.cancel()
            self.save_timer = threading.Timer(1.0, self.save_now)
            self.save_timer.daemon = True
            self.save_timer.start()

    def save_now(self):
        with self.lock:
            body = self.state
        if not body:
            return
        try:
            shared = json.loads(body).get("shared")
            tmp = BACKUP.with_suffix(".tmp")
            tmp.write_text(json.dumps(shared, indent=1))
            os.replace(tmp, BACKUP)
        except (OSError, ValueError, AttributeError) as e:
            print("Could not write backup:", e)

    def relay(self, msg):
        with self.lock:
            host = self.host
        if not host:
            return False
        host.send("action", json.dumps(msg))
        return True


class Server(ThreadingHTTPServer):
    daemon_threads = True

    def server_bind(self):
        # HTTPServer.server_bind does a reverse-DNS lookup that can stall for seconds on
        # workshop Wi-Fi. Nothing here needs the hostname.
        socketserver.TCPServer.server_bind(self)
        self.server_name, self.server_port = self.server_address[:2]


class Handler(BaseHTTPRequestHandler):
    server_version = "FlowGame/1"
    hub: Hub = None

    def log_message(self, fmt, *args):  # keep the terminal quiet
        pass

    def _send(self, code, body=b"", ctype="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code, obj):
        self._send(code, json.dumps(obj).encode())

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n <= 0 or n > MAX_BODY:
            return None
        return self.rfile.read(n)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path in ("/", "/flow-game.html"):
            try:
                self._send(200, GAME.read_bytes(), "text/html; charset=utf-8")
            except OSError:
                self._send(500, b"flow-game.html not found next to serve.py", "text/plain")
        elif u.path == "/api/info":
            self._json(200, {"app": "flow-game", "joinUrl": self.hub.join_url})
        elif u.path == "/api/events":
            self.events(parse_qs(u.query))
        else:
            self._send(404, b"Not found", "text/plain")

    def do_POST(self):
        u = urlparse(self.path)
        body = self._body()
        if body is None:
            return self._json(400, {"error": "empty or oversized body"})
        if u.path == "/api/state":
            try:
                compact = json.dumps(json.loads(body), separators=(",", ":"))
            except ValueError:
                return self._json(400, {"error": "bad json"})
            ok = self.hub.put_state(self.headers.get("X-Host-Token"), compact)
            self._json(200 if ok else 403, {"ok": ok})
        elif u.path == "/api/action":
            try:
                msg = json.loads(body)
            except ValueError:
                return self._json(400, {"error": "bad json"})
            if not isinstance(msg, dict):
                return self._json(400, {"error": "bad message"})
            ok = self.hub.relay(msg)
            self._json(200 if ok else 503, {"ok": ok})
        elif u.path == "/api/bye":  # sendBeacon from a closing tab
            try:
                cid = str(json.loads(body).get("cid", ""))
            except (ValueError, AttributeError):
                cid = ""
            if cid:
                self.hub.bye(cid)
            self._json(200, {"ok": True})
        else:
            self._send(404, b"Not found", "text/plain")

    def events(self, qs):
        role = "host" if qs.get("role", [""])[0] == "host" else "join"
        as_ = qs.get("as", [""])[0][:24]
        cid = qs.get("cid", [""])[0][:40]
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Accel-Buffering", "no")
        self.end_headers()
        c = self.hub.connect(role, as_, cid)
        try:
            while True:
                try:
                    item = c.q.get(timeout=PING_SECONDS)
                except queue.Empty:
                    item = ("ping", '{"t":%d}' % now_ms())
                if item is None:
                    break
                event, data = item
                self.wfile.write(f"event: {event}\ndata: {data}\n\n".encode())
                self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError, OSError):
            pass
        finally:
            self.hub.disconnect(c)


def make_server(port=8000, bind="0.0.0.0"):
    """Build a ready-to-run server. Raises OSError if the port is taken.
    Run it with httpd.serve_forever(); stop it with stop_server(httpd)."""
    join_url = f"http://{lan_ip()}:{port}/"
    handler = type("BoundHandler", (Handler,), {"hub": Hub(join_url)})
    httpd = Server((bind, port), handler)
    httpd.hub, httpd.join_url = handler.hub, join_url
    return httpd


def stop_server(httpd):
    """Stop accepting requests, end open browser streams (so they show "Reconnecting"), save the backup."""
    httpd.shutdown()
    httpd.hub.close_all()
    httpd.hub.save_now()
    httpd.server_close()


def main():
    ap = argparse.ArgumentParser(description="Host the Paper Airplane Flow Game on your local network.")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--bind", default="0.0.0.0", help="address to listen on (default: all interfaces)")
    args = ap.parse_args()

    httpd = make_server(args.port, args.bind)
    join_url = httpd.join_url

    print("Paper Airplane Flow Game: LAN mode")
    print(f"  Facilitator (this laptop): http://localhost:{args.port}/")
    print(f"  Others on the same Wi-Fi:  {join_url}")
    print(f"If phones can't connect, allow TCP {args.port} through the firewall")
    print(f"  (for example: sudo ufw allow {args.port}/tcp).")
    print(f"A backup of the live game is written to {BACKUP.name}. Load it with \"Load session\".")
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping.")
    finally:
        httpd.hub.close_all()
        httpd.hub.save_now()
        httpd.server_close()


if __name__ == "__main__":
    main()
