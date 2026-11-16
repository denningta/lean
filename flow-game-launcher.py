#!/usr/bin/env python3
"""A small window that starts and stops the LAN server (serve.py), so nobody has to
remember a terminal command.

    python3 flow-game-launcher.py             # open the window (the server starts right away)
    python3 flow-game-launcher.py --install   # add "Flow Game Server" to the Linux app launcher
"""
import argparse
import sys
import threading
import webbrowser
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import serve  # noqa: E402

APP_NAME = "Flow Game Server"


def install_desktop_entry():
    apps = Path.home() / ".local/share/applications"
    apps.mkdir(parents=True, exist_ok=True)
    entry = apps / "flow-game-server.desktop"
    entry.write_text(
        "[Desktop Entry]\n"
        "Type=Application\n"
        f"Name={APP_NAME}\n"
        "Comment=Host the Paper Airplane Flow Game so others can enter data from their phones\n"
        f"Exec={sys.executable} \"{Path(__file__).resolve()}\"\n"
        f"Path={HERE}\n"
        "Icon=network-server\n"
        "Terminal=false\n"
        "Categories=Education;\n"
    )
    print(f"Added {entry}")


class Launcher:
    def __init__(self, root, port):
        import tkinter as tk
        from tkinter import ttk

        self.tk, self.root = tk, root
        self.httpd = None
        root.title(APP_NAME)
        root.minsize(440, 0)
        root.resizable(False, False)
        try:  # a dialog-type window floats at its own size in tiling window managers (Hyprland, i3, sway)
            root.attributes("-type", "dialog")
        except tk.TclError:
            pass  # not X11 (macOS, Windows)
        style = ttk.Style(root)
        if "clam" in style.theme_names():
            style.theme_use("clam")
        bg = style.lookup("TFrame", "background")
        root.configure(bg=bg)
        style.configure("Title.TLabel", font=("TkDefaultFont", 14, "bold"))
        style.configure("Url.TLabel", font=("TkFixedFont", 12, "bold"))
        style.configure("Hint.TLabel", foreground="#5b6470")
        style.configure("Big.TButton", font=("TkDefaultFont", 11, "bold"), padding=(16, 8))

        f = ttk.Frame(root, padding=18)
        f.grid(sticky="nsew")
        root.columnconfigure(0, weight=1)
        f.columnconfigure(1, weight=1)

        ttk.Label(f, text="Paper Airplane Flow Game", style="Title.TLabel").grid(row=0, column=0, columnspan=3, sticky="w")
        self.status = tk.StringVar()
        self.status_label = tk.Label(f, textvariable=self.status, font=("TkDefaultFont", 11, "bold"), anchor="w", bg=bg)
        self.status_label.grid(row=1, column=0, columnspan=3, sticky="w", pady=(4, 12))

        ttk.Label(f, text="Port").grid(row=2, column=0, sticky="w")
        self.port = tk.StringVar(value=str(port))
        self.port_entry = ttk.Entry(f, textvariable=self.port, width=7)
        self.port_entry.grid(row=2, column=1, sticky="w", padx=(8, 0))
        self.toggle_btn = ttk.Button(f, text="Start", style="Big.TButton", command=self.toggle)
        self.toggle_btn.grid(row=2, column=2, sticky="e")

        ttk.Separator(f).grid(row=3, column=0, columnspan=3, sticky="ew", pady=14)

        ttk.Label(f, text="This laptop (facilitator)").grid(row=4, column=0, columnspan=2, sticky="w")
        self.local_url = tk.StringVar(value="—")
        ttk.Label(f, textvariable=self.local_url, style="Url.TLabel").grid(row=5, column=0, columnspan=2, sticky="w")
        self.open_btn = ttk.Button(f, text="Open game", command=self.open_game)
        self.open_btn.grid(row=5, column=2, sticky="e")

        ttk.Label(f, text="Phones on the same Wi-Fi").grid(row=6, column=0, columnspan=2, sticky="w", pady=(12, 0))
        self.join_url = tk.StringVar(value="—")
        ttk.Label(f, textvariable=self.join_url, style="Url.TLabel").grid(row=7, column=0, columnspan=2, sticky="w")
        self.copy_btn = ttk.Button(f, text="Copy link", command=self.copy_link)
        self.copy_btn.grid(row=7, column=2, sticky="e")

        self.clients = tk.StringVar()
        ttk.Label(f, textvariable=self.clients).grid(row=8, column=0, columnspan=3, sticky="w", pady=(14, 0))
        self.hint = tk.StringVar()
        ttk.Label(f, textvariable=self.hint, style="Hint.TLabel", wraplength=420, justify="left").grid(row=9, column=0, columnspan=3, sticky="w", pady=(6, 0))

        root.protocol("WM_DELETE_WINDOW", self.quit)
        self.refresh()
        self.start()
        self.tick()

    # --- server --------------------------------------------------------
    def start(self):
        try:
            port = int(self.port.get())
            if not 1 <= port <= 65535:
                raise ValueError
        except ValueError:
            self.hint.set("The port must be a number from 1 to 65535.")
            return
        try:
            self.httpd = serve.make_server(port)
        except OSError as e:
            self.httpd = None
            in_use = getattr(e, "errno", None) in (48, 98, 10048)
            self.hint.set(f"Port {port} is already in use. Is the server already running in a terminal? "
                          "Stop it there, or pick another port and press Start."
                          if in_use else f"Couldn't start the server: {e}")
            self.refresh()
            return
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()
        self.hint.set(f"If phones time out, allow port {port} through the firewall, "
                      "and check they're on the same Wi-Fi (not a guest network).")
        self.refresh()

    def stop(self):
        httpd, self.httpd = self.httpd, None
        if httpd:
            serve.stop_server(httpd)
        self.hint.set(f"Stopped. The last game was saved to {serve.BACKUP.name}; open it with \"Load session\".")
        self.refresh()

    def toggle(self):
        if self.httpd:
            self.stop()
        else:
            self.start()

    def quit(self):
        if self.httpd:
            serve.stop_server(self.httpd)
        self.root.destroy()

    # --- buttons ---------------------------------------------------------
    def open_game(self):
        if self.httpd:
            webbrowser.open(self.local_url.get())

    def copy_link(self):
        if self.httpd:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.httpd.join_url)
            self.copy_btn.config(text="Copied")
            self.root.after(1500, lambda: self.copy_btn.config(text="Copy link"))

    # --- display ---------------------------------------------------------
    def refresh(self):
        running = self.httpd is not None
        if running:
            port = self.httpd.server_address[1]
            self.local_url.set(f"http://localhost:{port}/")
            self.join_url.set(self.httpd.join_url)
            self.status.set("● Running")
            self.status_label.config(fg="#1d8a4b")
        else:
            self.local_url.set("—")
            self.join_url.set("—")
            self.clients.set("")
            self.status.set("● Stopped")
            self.status_label.config(fg="#d43a3a")
        self.toggle_btn.config(text="Stop" if running else "Start")
        state = "normal" if running else "disabled"
        self.open_btn.config(state=state)
        self.copy_btn.config(state=state)
        self.port_entry.config(state="disabled" if running else "normal")

    def tick(self):
        if self.httpd:
            host, phones = self.httpd.hub.counts()
            game = "Game tab: open" if host else "Game tab: not open yet (press Open game)"
            self.clients.set(f"{game}   ·   Phones connected: {phones}")
        self.root.after(1000, self.tick)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--install", action="store_true", help="add a desktop entry to the app launcher and exit")
    args = ap.parse_args()
    if args.install:
        install_desktop_entry()
        return
    import tkinter as tk
    root = tk.Tk(className="flow-game-server")
    Launcher(root, args.port)
    root.mainloop()


if __name__ == "__main__":
    main()
