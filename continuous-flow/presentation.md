---
theme: "tokyo-night"
font: "Adwaita Sans"
title: "Creating Continuous Flow"
color_accent: "#7aa2f7"
color_selection: "#292e42"
color_muted: "#414868"
color_background: "#1a1b26"
color_dark_background: "#13141c"
color_darker_background: "#0e0e14"
color_lighter_background: "#24283b"
color_foreground: "#a9b1d6"
color_dark_foreground: "#565f89"
color_light_foreground: "#b4bee6"
color_bright_foreground: "#c0caf5"
color_red: "#f7768e"
color_yellow: "#e0af68"
color_orange: "#eb927b"
color_green: "#9ece6a"
color_cyan: "#449dab"
color_blue: "#7aa2f7"
color_magenta: "#ad8ee6"
color_brown: "#75493d"
color_bright_red: "#ff7a93"
color_bright_yellow: "#ff9e64"
color_bright_green: "#b9f27c"
color_bright_cyan: "#0db9d7"
color_bright_blue: "#7da6ff"
color_bright_magenta: "#bb9af7"
---

![position=center size=100%](footer-01.svg)

# Creating Continuous Flow

Understand the work · Distribute the work · Arrange the cell

<!--
Welcome. This session is for everyone who touches the line: engineers who design it, planners who load it, technicians who run and maintain it.
By the end, the team should be able to take a real product family, calculate takt, break the work into elements, balance it across operators, and sketch a cell that flows.
Allow about 3 hours including the flow game and the workshop on our own line.
-->

---

![position=center size=100%](footer-02.svg)

# Why are we here?

- Piles of WIP between stations
- Lead times measured in days, work content measured in minutes
- One station drowning, the next one waiting
- Problems found hours after they were made

<!--
Ask the room: where have you seen each of these this week? Write their examples on the whiteboard; come back to them at the end.
The gap between lead time (days) and work content (minutes) is the opportunity. Almost all of lead time is waiting.
-->

---

# Batch & queue vs. one-piece flow

```svg
<svg viewBox="0 0 640 300">
  <text x="20" y="34" font-size="20" font-weight="bold">Batch &amp; queue</text>
  <g font-size="16" text-anchor="middle">
    <rect x="150" y="54" width="110" height="56" rx="8" fill="none" stroke="var(--foreground)" stroke-width="2"/>
    <text x="205" y="88">Step A</text>
    <rect x="340" y="54" width="110" height="56" rx="8" fill="none" stroke="var(--foreground)" stroke-width="2"/>
    <text x="395" y="88">Step B</text>
    <rect x="530" y="54" width="100" height="56" rx="8" fill="none" stroke="var(--foreground)" stroke-width="2"/>
    <text x="580" y="88">Step C</text>
  </g>
  <g fill="var(--red)">
    <rect x="30" y="60" width="18" height="18"/><rect x="52" y="60" width="18" height="18"/><rect x="74" y="60" width="18" height="18"/><rect x="96" y="60" width="18" height="18"/><rect x="118" y="60" width="18" height="18"/>
    <rect x="30" y="84" width="18" height="18"/><rect x="52" y="84" width="18" height="18"/><rect x="74" y="84" width="18" height="18"/><rect x="96" y="84" width="18" height="18"/><rect x="118" y="84" width="18" height="18"/>
    <rect x="270" y="72" width="18" height="18"/><rect x="292" y="72" width="18" height="18"/><rect x="314" y="72" width="18" height="18"/>
    <rect x="460" y="60" width="18" height="18"/><rect x="482" y="60" width="18" height="18"/><rect x="504" y="60" width="18" height="18"/>
    <rect x="460" y="84" width="18" height="18"/><rect x="482" y="84" width="18" height="18"/>
  </g>
  <line x1="20" y1="150" x2="620" y2="150" stroke="var(--dark-foreground)" stroke-dasharray="4 6"/>
  <text x="20" y="194" font-size="20" font-weight="bold">One-piece flow</text>
  <g font-size="16" text-anchor="middle">
    <rect x="150" y="214" width="110" height="56" rx="8" fill="none" stroke="var(--accent)" stroke-width="2"/>
    <text x="205" y="248">Step A</text>
    <rect x="340" y="214" width="110" height="56" rx="8" fill="none" stroke="var(--accent)" stroke-width="2"/>
    <text x="395" y="248">Step B</text>
    <rect x="530" y="214" width="100" height="56" rx="8" fill="none" stroke="var(--accent)" stroke-width="2"/>
    <text x="580" y="248">Step C</text>
  </g>
  <g fill="var(--accent)">
    <rect x="96" y="233" width="18" height="18"/>
    <rect x="286" y="233" width="18" height="18"/>
    <rect x="476" y="233" width="18" height="18"/>
  </g>
  <g stroke="var(--accent)" stroke-width="2">
    <line x1="118" y1="242" x2="146" y2="242"/><line x1="308" y1="242" x2="336" y2="242"/><line x1="498" y1="242" x2="526" y2="242"/>
  </g>
  <text id="slide-number" x="-49.8" y="301.0" font-size="9.8" fill="var(--foreground)">3</text>
  <g id="bae-logo" transform="translate(595.9,290.1) scale(0.1364)"><rect width="688" height="106" fill="#ED1A3B"/><path fill="#FFFFFF" fill-rule="evenodd" d="M263.8,25.8 270.5,25.8 270.5,26 272,26 272,26.2 274.2,26.2 276.2,27.2 277.5,27.2 278.2,28 279.5,28.2 280.5,28.8 280.8,29.2 281.8,29.5 282.8,30.8 283.2,30.8 285.2,32.8 285.2,33.2 286.2,34 286.8,35.5 287.2,35.8 288,37.2 288,38.8 287.2,39.2 285.2,39.5 283.5,40.5 282.2,40.5 282.2,40.8 280.5,41 280,41.5 278,41.8 276.2,42.8 274.8,42.8 274.2,42.2 274,41 271.8,38.8 270,38.2 270,38 268,37.8 268,37.5 265.5,37.5 265.5,37.8 263.5,38 261.8,39.8 261.5,41 261.8,41 262.2,42.8 263.5,43 265,44 269.2,44.5 269.2,44.8 271,45 271,45.2 274.2,45.5 275.2,46.2 277.5,46.5 278.8,47.2 279.8,47.2 281.5,48.5 282.8,48.8 284,50 284.5,50 287.8,53.5 287.8,54.2 288.5,55 288.8,56.8 289.5,58 289.8,65 289.5,65 288.8,68.2 287.5,70.8 286.8,71.2 286.8,71.8 283.8,74.8 282,75.5 281.2,76.5 280,76.8 278.2,77.8 277.2,77.8 275.5,78.8 274,78.8 274,79 272.8,79 271.8,79.5 263,79.8 263,79.5 260.8,79.5 260.8,79.2 258.8,79 258.8,78.8 257,78.8 255.5,77.8 253.8,77.5 253.5,77 251.5,76.2 251.2,75.8 249.2,74.8 246.5,72 246.5,71.5 245,70 245,69.2 244.2,68.5 243.5,66 243,65.5 243.2,63.2 246.5,63 246.5,62.8 248.2,62.5 248.2,62.2 250.8,62.2 250.8,62 252,62 252.5,61.5 254,61.5 254,61.2 255.5,61.2 255.5,61 257.8,61 259.2,64 260.5,65.2 261,65.2 261.2,65.8 263.2,66.8 269.8,67 269.8,66.8 271.5,66.5 273.2,64.8 273,63 270.5,60.8 268,60.5 266.5,59.8 263.2,59.5 262.5,59 258.2,58.2 257.5,57.5 255.8,57.2 253.8,56 253,56 252.5,55.2 251.2,55 247.5,51.2 247,49.8 246.2,49 246,47.2 245.5,46.5 245.2,40.8 245.5,40.8 245.5,39.5 246,39 246.2,36.8 247,36 247.5,34.2 250,31.8 250,31.2 250.8,31 251,30.2 251.5,30.2 252.2,29.2 253.2,29 254,28.2 255.8,27.8 256,27.2 258.2,27 259.8,26.2 263.8,26ZM380.2,25.8 388.8,26 388.8,26.2 390.2,26.2 391.8,27 393.8,27.2 395.2,28.2 396,28.2 396.2,28.8 396.8,28.8 397,29.2 399,30.2 400.5,32 401,32 401,32.5 402,33.2 402.5,34.5 403.2,35 404.2,37 404.2,37.8 404.5,37.8 404.2,38.8 403.5,39.2 402.5,39.2 402.5,39.5 401,39.8 399.8,40.5 398.5,40.5 396.5,41.5 394.2,41.8 392.5,42.8 391.2,42.8 390.5,42 389.8,40.2 388,38.8 386.2,38.2 386.2,38 384,37.8 384,37.5 382,37.5 381,38 379.8,38 378.2,39.2 377.8,40.2 377.8,41.2 378.5,42 378.5,42.5 379.8,43.2 380.5,43.2 381.2,44 385.5,44.5 385.5,44.8 387.2,45 387.2,45.2 389.5,45.2 391,46 394,46.5 395.8,47.5 396.8,47.5 397.5,48.2 399.5,49 401.2,50.8 401.8,50.8 402.5,51.5 402.5,52 403.5,52.8 405.8,57.2 405.8,59.8 406,59.8 406,61.2 406.2,61.2 405.8,66.5 405.5,66.5 405.5,67.2 403.5,71.2 402.5,72 402.5,72.5 401,74 400.5,74 399.8,75 398.2,75.5 397.8,76.2 396,76.8 395.2,77.5 393.8,77.8 392.8,78.5 389,79 388,79.5 386,79.5 386,79.8 377,79.5 377,79.2 376,79.2 375.2,78.8 372.8,78.5 372.2,78 370.8,77.8 367.8,76.2 367.5,75.8 366.2,75.2 365.8,74.5 365.2,74.5 363.2,72.5 363.2,72 362.2,71.2 362,70.2 361.2,69.8 360.8,68.2 360,67.5 360,66.2 359,64.5 359,63.8 359.5,63.2 361.8,63.2 363.2,62.5 368.2,62 368.2,61.8 369.2,61.8 370,61.2 373.8,61 374.2,61.2 375.2,63.5 377.2,65.5 378.2,65.8 378.8,66.5 379.5,66.5 379.5,66.8 386,67 386,66.8 387.2,66.8 389,65.5 389.2,64.2 389.5,64.2 389,62.2 387.5,61.5 387.2,61 384.5,60.5 384.5,60.2 382.8,60 382.8,59.8 381,59.8 380,59.2 378.5,59.2 377.8,58.8 374.8,58.2 374.2,57.8 372,57.2 370.5,56.2 369.2,56 368.8,55.2 367.2,54.8 364.8,52.5 364.8,52 363.5,50.8 363,49 362.2,48.2 362.2,47 362,47 362,45.8 361.8,45.8 361.8,40.5 362,40.5 362.2,37.5 363,36.8 363.2,35.5 364,34 364.5,33.8 364.5,33.2 365.8,32.2 365.8,31.8 367.2,30.2 367.8,30.2 368.2,29.5 369.2,29.2 369.5,28.8 371.5,28 371.8,27.5 373.8,27.2 375.8,26.2 378,26.2 378,26 380.2,26ZM627,25.8 634,25.8 634,26 635.5,26 635.5,26.2 637.8,26.2 639.8,27.2 641,27.2 642,28.2 643.5,28.5 643.8,29 645,29.5 645.5,30.2 646,30.2 646.5,31 647,31 648.2,32.2 648.2,32.8 649,33.2 649,33.8 650,34.5 650,35.2 650.8,35.8 651,37.2 651.5,37.8 651.5,38.8 650.8,39.2 649.2,39.2 648.2,40 644.8,40.8 643.5,41.5 641.2,41.8 639.5,42.8 638.2,42.8 637.5,41.2 637,41 637,40.5 635.5,39 635,39 634.2,38.2 632.5,38 632.5,37.8 628.8,37.5 628,38 627,38 626,38.5 625,40 625.2,42 626.2,43 627.5,43.2 628.2,44 631.2,44.2 631.2,44.5 632.5,44.5 632.5,44.8 633.5,44.8 634.5,45.2 637.5,45.5 639,46.2 641,46.5 642,47.2 643,47.2 643,47.5 643.8,47.5 645.8,48.5 646,49 647.2,49.5 648.2,50.8 648.8,50.8 649.2,51.8 649.8,51.8 649.8,52.2 650.5,52.8 650.5,53.2 652,55 652,56.2 652.8,57.5 653,60.2 653.2,60.2 653,65.2 652.8,65.2 652.8,66.2 652,67.8 652,68.8 651.2,69.5 650.8,71 649.8,71.8 649.8,72.2 649,73 648,73.5 648,74 647.5,74 646.8,75 646.2,75 644.5,76.5 643.2,76.8 642.2,77.5 640,78 639.8,78.5 639,78.5 639,78.8 637.2,78.8 637.2,79 636,79 635.2,79.5 626.5,79.8 626.5,79.5 624,79.5 623.5,79 620.5,78.8 619,77.8 617.8,77.8 617,77 615.2,76.5 615,76 613,75 609.8,71.8 609.8,71.2 609,70.8 608.2,69 607.8,68.8 607,66.2 606.2,65.2 606.5,63.2 609.8,63 609.8,62.8 610.8,62.8 611.5,62.2 614.2,62.2 614.2,62 615.2,62 616,61.5 617.5,61.5 617.5,61.2 619,61.2 619,61 621.2,61 622.8,64 624.2,65.5 626.8,66.8 633,67 633,66.8 634.8,66.5 636.2,65.2 636.5,63.2 634,60.8 631.5,60.5 630,59.8 626.8,59.5 626,59 621.8,58.2 620.5,57.2 619,57.2 618,56.8 617.8,56.2 617,56.2 616,55.8 615.8,55.2 614.8,55 610.8,51 609.5,48.5 609,46 608.8,46 608.8,43.8 608.5,43.8 608.8,40 609,40 609,39 609.8,37.8 609.8,36.8 611,34.2 612,33.2 612,32.8 615,29.8 615.5,29.8 615.8,29.2 616.8,29 617.5,28.2 618.8,28 619.5,27.2 620.8,27.2 620.8,27 621.5,27 623,26.2 625,26.2 625,26 627,26ZM39.5,26.5 69.5,26.5 70.2,27 73,27.2 74.5,28.2 75.2,28.2 77,30 77.5,30 78,31 79.2,32 79.2,32.5 79.8,32.8 80.8,34.8 80.8,35.5 81,35.5 81,36.2 81.8,37.8 81.8,42.8 81.5,42.8 81.2,44.2 79.5,47.8 76.8,50.5 75.2,50.8 74.8,51.8 76.2,52.5 76.5,53 77.8,53.2 78.5,54.2 79,54.2 80.8,56 81,57 81.8,57.5 82,59 82.8,59.8 83,65.5 82.8,65.5 82.8,68 81.8,70 81.8,71.2 80.8,72.2 79.8,74.2 78.5,75.5 78,75.5 77.5,76.2 76,76.8 75.2,77.5 74.2,77.5 74.2,77.8 72.8,78 72.2,78.5 71,78.5 71,78.8 39.5,78.8 39.2,78.5 39.2,27ZM113.8,26.5 130.2,26.5 131,27.2 131.2,29.2 132,30 132.2,32.2 133.5,34.8 133.5,36 133.8,36 133.8,36.8 134,36.8 134,37.5 134.8,39 135,40.8 135.8,42 136.2,44.8 136.8,45.2 137,47.5 137.8,48.2 138,50.8 138.8,51.8 139,53.8 140,55.5 140.2,57.8 141,59 141.5,61.8 142.5,63.8 142.5,65 143.5,66.8 143.5,67.8 143.8,67.8 143.8,68.8 144.8,70.8 145,72.8 145.8,73.8 146,76.2 147,77.8 146.8,78.8 130.5,78.8 129.5,76.8 129,73.8 128.2,72.8 127.8,69.5 126.8,68.8 114,68.8 113.2,69.5 113,71.8 112,73.8 112,75.2 111,76.8 111,78.2 110.5,78.8 97.8,78.8 97.5,78.5 97.5,77.5 98,77 98,75.2 98.5,75 98.8,73.8 99,73.8 99,72.2 100,70.5 100.2,68.2 101,67.2 101.2,65 102.2,63 102.5,60.8 103.2,59.8 103.5,58 104.2,56.5 104.2,55.5 104.5,55.5 104.5,54.8 104.8,54.8 104.8,54 105.5,52.5 105.5,51.5 106,50.8 106,49.8 106.8,48.5 107,46.5 108,44.8 108,43.2 109,41.5 109.2,39.2 110,38.2 110.2,36 111.2,34 111.2,32.8 112.2,30.8 112.5,28.8ZM164.2,26.5 202.8,26.5 203,26.8 203,27.8 203.2,27.8 203.2,37.8 202.5,38.8 180,38.8 179.5,39.8 179.5,45 180.2,46 198.2,46 198.8,47 198.8,57 198.2,58 197.8,58.2 181.2,58.2 181.2,58 180,58.2 179.5,59 179.5,65.2 179.8,65.8 180.2,66.2 202.8,66.2 203.2,67.2 203.2,68.5 203,68.5 203.2,69 203.2,75.5 203,75.5 203.2,78.2 202.8,78.8 164,78.8 163.8,78.5 163.8,27ZM301,26.5 317.8,26.5 318.2,26.8 319,27.5 319.5,29 320,29.2 320,30 320.5,31 321,31.2 321.8,33.2 322.2,33.5 322.8,35.2 323.8,36.2 323.8,37 324.5,37.8 325,39.5 326,40.5 326,41.2 326.5,41.5 326.5,42 327.2,42.5 328,42.2 328.5,40.2 329.2,39.8 329.5,38.5 330.2,37.8 331,35.5 331.8,35 332,33.5 332.5,33.2 333,31.5 334,30.5 334,29.5 334.8,28.8 335.8,26.8 336.2,26.5 349.5,26.5 349.8,26.8 349.5,28.5 348.5,29.2 348.5,30 347.8,31.5 347.2,31.8 346.8,33.2 346.2,33.5 346,34.8 345.2,35.5 344.8,37 344.2,37.2 343.5,39.2 343,39.5 342.8,40.8 341.8,42 341.8,42.8 340.8,43.8 340,45.8 339.2,46.5 339,47.8 338.5,48 338,49.5 337.5,49.8 336.8,51.8 336,52.5 335.8,53.8 335,54.2 335,55 334,56 334,56.8 333.8,56.8 333.8,78.8 318.2,78.8 317.8,78.2 317.8,56.5 317,55 316.5,54.8 315.8,52.8 315,52.2 314.8,51 314,50.5 313.5,49 313,48.8 312.8,47.8 311.5,46.2 309,41.2 308.2,40.8 308.2,40 307.8,39 307,38.5 306.8,37.2 306,36.8 305.5,35.2 305,35 303,31 302.5,30.8 302,29.2 301.5,29 300.8,27.5ZM420.8,26.5 456.8,26.5 457.5,27.5 457.5,38.5 457.2,39 456.8,39.2 447.5,39.2 446.8,39.8 446.8,78.2 446.2,78.8 431.5,78.8 431,78.2 431,76.5 431.2,76.5 431,76 431,40.8 431.2,40.5 431,40.5 431,39.8 430.2,39.2 420.8,39.2 420.2,38.8 420.2,27ZM475,26.5 513.5,26.5 514,27 514.2,27.5 514.2,38 513.5,38.8 491.2,38.8 490.5,39.5 490.5,45 491.5,46 509.2,46 509.8,46.8 509.8,57.2 509.5,57.8 508.8,58.2 491.2,58.2 490.5,59 490.5,65.2 490.8,65.8 491.8,66.2 513.8,66.2 514.2,67 514.2,78.2 513.8,78.8 474.8,78.8 474.5,78.2 474.5,27.5ZM533.8,26.5 554,26.5 554.5,26.8 555.2,28 555.2,29.2 555.5,29.2 555.5,30.2 556.2,31.8 556.8,35 557.5,36.2 557.8,38.5 558.5,39.8 559,43 559.8,44.2 560,47 560.8,48 560.8,49.2 561,49.2 561,51 561.8,51.8 562.8,51 562.8,50.2 563.2,49.5 564.2,44.2 564.8,43.8 565,41.5 565.8,40.2 566,37.2 566.8,36 567.2,32.8 568,31.5 568.2,28.5 569.5,26.5 589.8,26.5 590.2,27.2 590.2,78.2 590,78.8 575.5,78.8 575,78.2 575,51.2 575.2,51.2 575.2,48.5 575,48.5 574.8,47 573.8,47.8 573.5,49 573.2,49 573.2,50.5 573,50.5 573,51.5 572.2,53 572,55.8 571,57.8 571,59.5 570.8,59.5 570.8,60.5 570,62 570,63.8 569.8,63.8 569.8,64.8 569,66 568.8,68.5 568,70 567.8,72.5 567.5,72.5 567.5,73.5 566.8,75 566.2,78.2 565.8,78.8 555.5,78.8 555,78.2 554.2,74.2 553.5,72.8 553.5,71.2 553.2,71.2 553.2,70.5 553,70.5 553,69.8 552.2,68.2 552.2,66.8 552,66.8 552,65.8 551.2,64.2 551,61.8 550.2,60.8 550,58 549.2,56.8 548.8,53.5 548.2,53 547.8,49.5 547.5,49.5 547.5,48.8 547,48.2 547,47.5 546,45.5 545.5,46 545.5,47.2 545.8,47.2 545.8,78.2 545.2,78.8 533.5,78.8 533.2,78.5 533.2,27ZM54.5,37.5 53.8,38.2 53.8,46.2 54.2,46.8 62.8,46.8 62.8,46.5 64.8,46 65.8,45 66.2,44 66.2,40.2 65.2,38.8 63.8,38 60.5,37.8 60.5,37.5ZM120.5,42.8 120,43 119.8,45 119.5,45 119.5,45.8 119,46 118.8,48.2 118,49.8 117.5,53 117,53.5 116.8,55.2 116.5,55.2 116.5,56.8 117.5,57.2 122.2,57.2 122.2,57 124,57.2 124.5,57 124.8,55.8 123.8,53.8 123.8,52 122.8,50 122.5,47.8 121.5,46 121.2,43.2 121,42.8ZM54.8,57.2 54,57.5 53.8,58 53.8,66.8 54.2,67.2 63.2,67.2 63.2,67 65.5,66.5 67.2,64.5 67.5,61.2 67.2,61.2 67,60 65.5,58.5 62.8,57.8 62.8,57.5 57.8,57.5 57.8,57.2 55.5,57.5 55.5,57.2Z"/></g>
</svg>
```

<!--
Top: each step finishes the whole batch before passing it on. Inventory piles up in front of every step and hides problems.
Bottom: make one, check one, move one. Each step hands off a single piece, so a defect is seen on the very next piece.
-->

---

![position=center size=100%](footer-04.svg)

# Same work, different lead time

10 parts · 3 steps · 1 minute per part per step

| | Batch of 10 | One-piece flow |
| --- | :---: | :---: |
| First good part out | 21 min | **3 min** |
| All 10 parts done | 30 min | **12 min** |
| Parts waiting (WIP) | up to 10 | **3** |
| Time to find a defect | up to 10 parts later | **next part** |

<!--
Walk through the math on the whiteboard.
Batch: Step A finishes all 10 at minute 10, B at minute 20, the first part out of C at minute 21, the last at 30.
Flow: the first part is out at minute 3, then one every minute after that: 3 + 9 = 12.
Nobody worked faster. The work content is identical: 30 operator-minutes. Only the waiting changed.
-->

---

![position=center size=100%](footer-05.svg)

# Continuous flow is…

> Making and moving one piece at a time, at the rate the customer needs, with each step making only what the next step needs.

<!--
Three ideas packed into the definition:
1. One piece at a time (or the smallest practical batch).
2. At the customer's rate: that's takt time.
3. Each step makes just what the next step needs: no overproduction between stations.
-->

---

![position=center size=100%](footer-06.svg)

# Today's roadmap

1. **Understand the work:** takt time, work elements, time observation
2. **Distribute the work:** operator count, line balancing, yamazumi
3. **Arrange the cell:** layout, walk paths, material presentation
4. **Practice:** flow game + our own line

<!--
We'll use one running example throughout: a pump housing assembly line. The numbers are made up but realistic. In the workshop we'll swap in data from our own line.
-->

---

![position=center size=100%](footer-07.svg)

# Everyone owns a piece of flow

| Role | Brings | Owns |
| --- | --- | --- |
| Manufacturing engineers | Process knowledge, data | Work elements, balance, layout |
| Planners | Customer demand, mix | Takt time, schedule, staffing |
| Technicians | How the work *really* runs | Time studies, trials, standard work |

<!--
This is why the team is cross-functional. An engineer can design a beautiful balance against the wrong demand. A planner can schedule to a takt the line can't hit. Technicians know where the real time goes: the reaching, searching, and waiting that never shows up in a routing.
-->

---

![position=center size=100%](footer-08.svg)

# Part 1

## Understand the work

---

![position=center size=100%](footer-09.svg)

# Start with the customer

**Takt time** = available work time ÷ customer demand

<!--
Takt is German for beat or meter, as in a conductor's baton. It is the heartbeat the whole line plays to.
Available time is net: shift length minus breaks, meetings, and planned cleaning. Don't subtract downtime or changeovers here; we account for those later in planned cycle time.
-->

---

![position=center size=100%](footer-10.svg)

# Takt time: our example

| | |
| --- | ---: |
| Shifts per day | 2 |
| Net time per shift | 450 min |
| Available time | 900 min = **54,000 s** |
| Customer demand | **900 units / day** |
| **Takt time** | **60 s** |

<!--
8-hour shift = 480 min, minus two 10-minute breaks and a 10-minute start-up meeting = 450 min net.
54,000 s ÷ 900 units = 60 seconds. The customer needs one finished pump every minute.
Planners: this is your number. If demand changes, takt changes, and the line has to be rebalanced. We'll see that later.
-->

---

![position=center size=100%](footer-11.svg)

# Takt is a beat, not a race

- Faster than takt: **overproduction**: inventory, hidden problems
- Slower than takt: **overtime**: missed shipments, expediting
- At takt: just what the customer needs, when they need it

<!--
A common mistake is treating takt as a target to beat. Building ahead of takt just creates inventory, the most expensive way to hide a problem.
-->

---

![position=center size=100%](footer-12.svg)

# Go and see

Watch the real process at the real place.

- Stand where the work happens
- Watch several full cycles before writing anything
- Talk with the operators: they know where the time goes
- Note the variation, not just the average

<!--
Genchi genbutsu. Don't build a balance from the routing or the ERP standard times; they are almost always wrong, and usually wrong in a way that hides the waste.
Technicians: you lead here. Explain to operators that we are studying the process, not the person.
-->

---

![position=center size=100%](footer-13.svg)

# Break the work into elements

A **work element** is the smallest piece of work that could be given to another person.

- Starts and ends at a clear, observable point
- "Torque 6 bolts" ✔ not "pick up wrench" ✘
- Not so large it can't be moved: "Assemble pump" ✘

<!--
Too small and you have hundreds of elements that can't be separated anyway. Too large and you have no flexibility to balance.
A good test: could I hand this element to the next person in line without them needing tools or parts from my station? If yes, it's a movable element.
-->

---

![position=center size=100%](footer-14.svg)

# See the waste in every element

| Value-added | Necessary, non-value-added | Pure waste |
| --- | --- | --- |
| Changes form, fit, or function | Required today, adds no value | Remove it |
| Press, torque, assemble | Load fixture, scan, inspect | Walk, search, wait, rework |

<!--
Value-added is what the customer would pay for if they watched us. Usually less than 30% of what we see.
Necessary non-value-added: reduce it over time, e.g. a better fixture makes loading faster.
Pure waste: walking, waiting, searching, reaching, re-handling, rework, overprocessing. Every one of these is a kaizen target.
-->

---

![position=center size=100%](footer-15.svg)

# Time the elements

- Time each element separately, 10+ cycles
- Use the **lowest repeatable** time, not the average
- Separate **manual time** from **machine time**
- Record walk time between stations
- Write down anything abnormal: it's a clue

<!--
Why lowest repeatable? It represents the process when nothing goes wrong. The gap between it and the average is the waste caused by variation and problems; that's a separate list to attack.
Machine time matters because an operator should never stand and watch a machine cycle. Track manual and machine time in separate columns.
-->

---

![position=center size=100%](footer-16.svg)

# Pump housing: work elements (1 of 2)

| # | Element | Manual (s) | Machine (s) |
| :---: | --- | ---: | ---: |
| 1 | Get housing, load fixture | 12 | |
| 2 | Press bearing | 10 | 25 |
| 3 | Install seal | 14 | |
| 4 | Insert shaft and rotor | 18 | |
| 5 | Torque 6 bolts | 24 | |
| 6 | Install gasket | 11 | |

<!--
These are lowest repeatable manual times. Element 2 has a 25-second automatic press cycle; the operator loads, presses start, and walks away.
-->

---

![position=center size=100%](footer-17.svg)

# Pump housing: work elements (2 of 2)

| # | Element | Manual (s) | Machine (s) |
| :---: | --- | ---: | ---: |
| 7 | Fit cover and fasten | 20 | |
| 8 | Leak test | 12 | 40 |
| 9 | Connect wire harness | 22 | |
| 10 | Function test | 15 | |
| 11 | Label and scan | 12 | |
| 12 | Visual inspect and pack | 28 | |
| | **Total work content** | **198** | |

<!--
Total manual work content is 198 seconds. That's the number we balance. Machine time doesn't add operator load as long as the machine cycle is shorter than takt and the operator isn't waiting on it.
The leak test is 40 s of machine time, under the 60 s takt, so one tester is enough.
-->

---

# Current state: the yamazumi

```svg
<svg viewBox="0 0 640 340">
  <g font-size="15" fill="var(--dark-foreground)" text-anchor="end">
    <text x="50" y="305">0</text><text x="50" y="215">30</text><text x="50" y="125">60</text><text x="50" y="65">80</text>
  </g>
  <line x1="60" y1="300" x2="620" y2="300" stroke="var(--foreground)" stroke-width="2"/>
  <rect x="100" y="66" width="90" height="234" fill="var(--red)"/>
  <rect x="230" y="207" width="90" height="93" fill="var(--green)"/>
  <rect x="360" y="153" width="90" height="147" fill="var(--yellow)"/>
  <rect x="490" y="150" width="90" height="150" fill="var(--magenta)"/>
  <line x1="60" y1="120" x2="620" y2="120" stroke="var(--foreground)" stroke-width="3" stroke-dasharray="10 6"/>
  <text x="620" y="110" font-size="17" text-anchor="end" font-weight="bold">Takt 60 s</text>
  <g font-size="18" text-anchor="middle" font-weight="bold">
    <text x="145" y="56">78</text><text x="275" y="197">31</text><text x="405" y="143">49</text><text x="535" y="170">40</text>
  </g>
  <g font-size="16" text-anchor="middle">
    <g transform="translate(128,304) scale(0.07)" fill="var(--accent)"><path d="M12,250 9,232 6,224 3,208 1,192 1,176 2,160 4,144 8,128 14,112 21,96 31,80 43,64 58,48 77,32 105,16 126,8 150,2 182,0 233,8 254,16 270,24 282,32 293,40 305,44 429,33 472,28 483,32 485,50 474,56 452,64 407,80 362,96 350,104 355,112 365,128 380,152 396,176 411,200 426,224 433,234 426,240 407,248 389,256 370,264 366,272 368,280 371,296 373,312 373,328 371,344 367,360 359,376 347,392 338,400 325,408 321,410 315,400 304,384 292,370 303,360 311,352 321,336 327,320 331,304 332,288 331,264 328,248 326,232 348,224 356,216 349,208 335,192 321,176 307,160 293,144 285,134 244,152 130,200Z"/><circle cx="262" cy="196" r="31"/></g><g transform="translate(258,304) scale(0.07)" fill="var(--accent)"><path d="M12,250 9,232 6,224 3,208 1,192 1,176 2,160 4,144 8,128 14,112 21,96 31,80 43,64 58,48 77,32 105,16 126,8 150,2 182,0 233,8 254,16 270,24 282,32 293,40 305,44 429,33 472,28 483,32 485,50 474,56 452,64 407,80 362,96 350,104 355,112 365,128 380,152 396,176 411,200 426,224 433,234 426,240 407,248 389,256 370,264 366,272 368,280 371,296 373,312 373,328 371,344 367,360 359,376 347,392 338,400 325,408 321,410 315,400 304,384 292,370 303,360 311,352 321,336 327,320 331,304 332,288 331,264 328,248 326,232 348,224 356,216 349,208 335,192 321,176 307,160 293,144 285,134 244,152 130,200Z"/><circle cx="262" cy="196" r="31"/></g><g transform="translate(388,304) scale(0.07)" fill="var(--accent)"><path d="M12,250 9,232 6,224 3,208 1,192 1,176 2,160 4,144 8,128 14,112 21,96 31,80 43,64 58,48 77,32 105,16 126,8 150,2 182,0 233,8 254,16 270,24 282,32 293,40 305,44 429,33 472,28 483,32 485,50 474,56 452,64 407,80 362,96 350,104 355,112 365,128 380,152 396,176 411,200 426,224 433,234 426,240 407,248 389,256 370,264 366,272 368,280 371,296 373,312 373,328 371,344 367,360 359,376 347,392 338,400 325,408 321,410 315,400 304,384 292,370 303,360 311,352 321,336 327,320 331,304 332,288 331,264 328,248 326,232 348,224 356,216 349,208 335,192 321,176 307,160 293,144 285,134 244,152 130,200Z"/><circle cx="262" cy="196" r="31"/></g><g transform="translate(518,304) scale(0.07)" fill="var(--accent)"><path d="M12,250 9,232 6,224 3,208 1,192 1,176 2,160 4,144 8,128 14,112 21,96 31,80 43,64 58,48 77,32 105,16 126,8 150,2 182,0 233,8 254,16 270,24 282,32 293,40 305,44 429,33 472,28 483,32 485,50 474,56 452,64 407,80 362,96 350,104 355,112 365,128 380,152 396,176 411,200 426,224 433,234 426,240 407,248 389,256 370,264 366,272 368,280 371,296 373,312 373,328 371,344 367,360 359,376 347,392 338,400 325,408 321,410 315,400 304,384 292,370 303,360 311,352 321,336 327,320 331,304 332,288 331,264 328,248 326,232 348,224 356,216 349,208 335,192 321,176 307,160 293,144 285,134 244,152 130,200Z"/><circle cx="262" cy="196" r="31"/></g>
  </g>
  <text id="slide-number" x="-99.1" y="341.2" font-size="11.1" fill="var(--foreground)">18</text>
  <g id="bae-logo" transform="translate(632.7,328.8) scale(0.1546)"><rect width="688" height="106" fill="#ED1A3B"/><path fill="#FFFFFF" fill-rule="evenodd" d="M263.8,25.8 270.5,25.8 270.5,26 272,26 272,26.2 274.2,26.2 276.2,27.2 277.5,27.2 278.2,28 279.5,28.2 280.5,28.8 280.8,29.2 281.8,29.5 282.8,30.8 283.2,30.8 285.2,32.8 285.2,33.2 286.2,34 286.8,35.5 287.2,35.8 288,37.2 288,38.8 287.2,39.2 285.2,39.5 283.5,40.5 282.2,40.5 282.2,40.8 280.5,41 280,41.5 278,41.8 276.2,42.8 274.8,42.8 274.2,42.2 274,41 271.8,38.8 270,38.2 270,38 268,37.8 268,37.5 265.5,37.5 265.5,37.8 263.5,38 261.8,39.8 261.5,41 261.8,41 262.2,42.8 263.5,43 265,44 269.2,44.5 269.2,44.8 271,45 271,45.2 274.2,45.5 275.2,46.2 277.5,46.5 278.8,47.2 279.8,47.2 281.5,48.5 282.8,48.8 284,50 284.5,50 287.8,53.5 287.8,54.2 288.5,55 288.8,56.8 289.5,58 289.8,65 289.5,65 288.8,68.2 287.5,70.8 286.8,71.2 286.8,71.8 283.8,74.8 282,75.5 281.2,76.5 280,76.8 278.2,77.8 277.2,77.8 275.5,78.8 274,78.8 274,79 272.8,79 271.8,79.5 263,79.8 263,79.5 260.8,79.5 260.8,79.2 258.8,79 258.8,78.8 257,78.8 255.5,77.8 253.8,77.5 253.5,77 251.5,76.2 251.2,75.8 249.2,74.8 246.5,72 246.5,71.5 245,70 245,69.2 244.2,68.5 243.5,66 243,65.5 243.2,63.2 246.5,63 246.5,62.8 248.2,62.5 248.2,62.2 250.8,62.2 250.8,62 252,62 252.5,61.5 254,61.5 254,61.2 255.5,61.2 255.5,61 257.8,61 259.2,64 260.5,65.2 261,65.2 261.2,65.8 263.2,66.8 269.8,67 269.8,66.8 271.5,66.5 273.2,64.8 273,63 270.5,60.8 268,60.5 266.5,59.8 263.2,59.5 262.5,59 258.2,58.2 257.5,57.5 255.8,57.2 253.8,56 253,56 252.5,55.2 251.2,55 247.5,51.2 247,49.8 246.2,49 246,47.2 245.5,46.5 245.2,40.8 245.5,40.8 245.5,39.5 246,39 246.2,36.8 247,36 247.5,34.2 250,31.8 250,31.2 250.8,31 251,30.2 251.5,30.2 252.2,29.2 253.2,29 254,28.2 255.8,27.8 256,27.2 258.2,27 259.8,26.2 263.8,26ZM380.2,25.8 388.8,26 388.8,26.2 390.2,26.2 391.8,27 393.8,27.2 395.2,28.2 396,28.2 396.2,28.8 396.8,28.8 397,29.2 399,30.2 400.5,32 401,32 401,32.5 402,33.2 402.5,34.5 403.2,35 404.2,37 404.2,37.8 404.5,37.8 404.2,38.8 403.5,39.2 402.5,39.2 402.5,39.5 401,39.8 399.8,40.5 398.5,40.5 396.5,41.5 394.2,41.8 392.5,42.8 391.2,42.8 390.5,42 389.8,40.2 388,38.8 386.2,38.2 386.2,38 384,37.8 384,37.5 382,37.5 381,38 379.8,38 378.2,39.2 377.8,40.2 377.8,41.2 378.5,42 378.5,42.5 379.8,43.2 380.5,43.2 381.2,44 385.5,44.5 385.5,44.8 387.2,45 387.2,45.2 389.5,45.2 391,46 394,46.5 395.8,47.5 396.8,47.5 397.5,48.2 399.5,49 401.2,50.8 401.8,50.8 402.5,51.5 402.5,52 403.5,52.8 405.8,57.2 405.8,59.8 406,59.8 406,61.2 406.2,61.2 405.8,66.5 405.5,66.5 405.5,67.2 403.5,71.2 402.5,72 402.5,72.5 401,74 400.5,74 399.8,75 398.2,75.5 397.8,76.2 396,76.8 395.2,77.5 393.8,77.8 392.8,78.5 389,79 388,79.5 386,79.5 386,79.8 377,79.5 377,79.2 376,79.2 375.2,78.8 372.8,78.5 372.2,78 370.8,77.8 367.8,76.2 367.5,75.8 366.2,75.2 365.8,74.5 365.2,74.5 363.2,72.5 363.2,72 362.2,71.2 362,70.2 361.2,69.8 360.8,68.2 360,67.5 360,66.2 359,64.5 359,63.8 359.5,63.2 361.8,63.2 363.2,62.5 368.2,62 368.2,61.8 369.2,61.8 370,61.2 373.8,61 374.2,61.2 375.2,63.5 377.2,65.5 378.2,65.8 378.8,66.5 379.5,66.5 379.5,66.8 386,67 386,66.8 387.2,66.8 389,65.5 389.2,64.2 389.5,64.2 389,62.2 387.5,61.5 387.2,61 384.5,60.5 384.5,60.2 382.8,60 382.8,59.8 381,59.8 380,59.2 378.5,59.2 377.8,58.8 374.8,58.2 374.2,57.8 372,57.2 370.5,56.2 369.2,56 368.8,55.2 367.2,54.8 364.8,52.5 364.8,52 363.5,50.8 363,49 362.2,48.2 362.2,47 362,47 362,45.8 361.8,45.8 361.8,40.5 362,40.5 362.2,37.5 363,36.8 363.2,35.5 364,34 364.5,33.8 364.5,33.2 365.8,32.2 365.8,31.8 367.2,30.2 367.8,30.2 368.2,29.5 369.2,29.2 369.5,28.8 371.5,28 371.8,27.5 373.8,27.2 375.8,26.2 378,26.2 378,26 380.2,26ZM627,25.8 634,25.8 634,26 635.5,26 635.5,26.2 637.8,26.2 639.8,27.2 641,27.2 642,28.2 643.5,28.5 643.8,29 645,29.5 645.5,30.2 646,30.2 646.5,31 647,31 648.2,32.2 648.2,32.8 649,33.2 649,33.8 650,34.5 650,35.2 650.8,35.8 651,37.2 651.5,37.8 651.5,38.8 650.8,39.2 649.2,39.2 648.2,40 644.8,40.8 643.5,41.5 641.2,41.8 639.5,42.8 638.2,42.8 637.5,41.2 637,41 637,40.5 635.5,39 635,39 634.2,38.2 632.5,38 632.5,37.8 628.8,37.5 628,38 627,38 626,38.5 625,40 625.2,42 626.2,43 627.5,43.2 628.2,44 631.2,44.2 631.2,44.5 632.5,44.5 632.5,44.8 633.5,44.8 634.5,45.2 637.5,45.5 639,46.2 641,46.5 642,47.2 643,47.2 643,47.5 643.8,47.5 645.8,48.5 646,49 647.2,49.5 648.2,50.8 648.8,50.8 649.2,51.8 649.8,51.8 649.8,52.2 650.5,52.8 650.5,53.2 652,55 652,56.2 652.8,57.5 653,60.2 653.2,60.2 653,65.2 652.8,65.2 652.8,66.2 652,67.8 652,68.8 651.2,69.5 650.8,71 649.8,71.8 649.8,72.2 649,73 648,73.5 648,74 647.5,74 646.8,75 646.2,75 644.5,76.5 643.2,76.8 642.2,77.5 640,78 639.8,78.5 639,78.5 639,78.8 637.2,78.8 637.2,79 636,79 635.2,79.5 626.5,79.8 626.5,79.5 624,79.5 623.5,79 620.5,78.8 619,77.8 617.8,77.8 617,77 615.2,76.5 615,76 613,75 609.8,71.8 609.8,71.2 609,70.8 608.2,69 607.8,68.8 607,66.2 606.2,65.2 606.5,63.2 609.8,63 609.8,62.8 610.8,62.8 611.5,62.2 614.2,62.2 614.2,62 615.2,62 616,61.5 617.5,61.5 617.5,61.2 619,61.2 619,61 621.2,61 622.8,64 624.2,65.5 626.8,66.8 633,67 633,66.8 634.8,66.5 636.2,65.2 636.5,63.2 634,60.8 631.5,60.5 630,59.8 626.8,59.5 626,59 621.8,58.2 620.5,57.2 619,57.2 618,56.8 617.8,56.2 617,56.2 616,55.8 615.8,55.2 614.8,55 610.8,51 609.5,48.5 609,46 608.8,46 608.8,43.8 608.5,43.8 608.8,40 609,40 609,39 609.8,37.8 609.8,36.8 611,34.2 612,33.2 612,32.8 615,29.8 615.5,29.8 615.8,29.2 616.8,29 617.5,28.2 618.8,28 619.5,27.2 620.8,27.2 620.8,27 621.5,27 623,26.2 625,26.2 625,26 627,26ZM39.5,26.5 69.5,26.5 70.2,27 73,27.2 74.5,28.2 75.2,28.2 77,30 77.5,30 78,31 79.2,32 79.2,32.5 79.8,32.8 80.8,34.8 80.8,35.5 81,35.5 81,36.2 81.8,37.8 81.8,42.8 81.5,42.8 81.2,44.2 79.5,47.8 76.8,50.5 75.2,50.8 74.8,51.8 76.2,52.5 76.5,53 77.8,53.2 78.5,54.2 79,54.2 80.8,56 81,57 81.8,57.5 82,59 82.8,59.8 83,65.5 82.8,65.5 82.8,68 81.8,70 81.8,71.2 80.8,72.2 79.8,74.2 78.5,75.5 78,75.5 77.5,76.2 76,76.8 75.2,77.5 74.2,77.5 74.2,77.8 72.8,78 72.2,78.5 71,78.5 71,78.8 39.5,78.8 39.2,78.5 39.2,27ZM113.8,26.5 130.2,26.5 131,27.2 131.2,29.2 132,30 132.2,32.2 133.5,34.8 133.5,36 133.8,36 133.8,36.8 134,36.8 134,37.5 134.8,39 135,40.8 135.8,42 136.2,44.8 136.8,45.2 137,47.5 137.8,48.2 138,50.8 138.8,51.8 139,53.8 140,55.5 140.2,57.8 141,59 141.5,61.8 142.5,63.8 142.5,65 143.5,66.8 143.5,67.8 143.8,67.8 143.8,68.8 144.8,70.8 145,72.8 145.8,73.8 146,76.2 147,77.8 146.8,78.8 130.5,78.8 129.5,76.8 129,73.8 128.2,72.8 127.8,69.5 126.8,68.8 114,68.8 113.2,69.5 113,71.8 112,73.8 112,75.2 111,76.8 111,78.2 110.5,78.8 97.8,78.8 97.5,78.5 97.5,77.5 98,77 98,75.2 98.5,75 98.8,73.8 99,73.8 99,72.2 100,70.5 100.2,68.2 101,67.2 101.2,65 102.2,63 102.5,60.8 103.2,59.8 103.5,58 104.2,56.5 104.2,55.5 104.5,55.5 104.5,54.8 104.8,54.8 104.8,54 105.5,52.5 105.5,51.5 106,50.8 106,49.8 106.8,48.5 107,46.5 108,44.8 108,43.2 109,41.5 109.2,39.2 110,38.2 110.2,36 111.2,34 111.2,32.8 112.2,30.8 112.5,28.8ZM164.2,26.5 202.8,26.5 203,26.8 203,27.8 203.2,27.8 203.2,37.8 202.5,38.8 180,38.8 179.5,39.8 179.5,45 180.2,46 198.2,46 198.8,47 198.8,57 198.2,58 197.8,58.2 181.2,58.2 181.2,58 180,58.2 179.5,59 179.5,65.2 179.8,65.8 180.2,66.2 202.8,66.2 203.2,67.2 203.2,68.5 203,68.5 203.2,69 203.2,75.5 203,75.5 203.2,78.2 202.8,78.8 164,78.8 163.8,78.5 163.8,27ZM301,26.5 317.8,26.5 318.2,26.8 319,27.5 319.5,29 320,29.2 320,30 320.5,31 321,31.2 321.8,33.2 322.2,33.5 322.8,35.2 323.8,36.2 323.8,37 324.5,37.8 325,39.5 326,40.5 326,41.2 326.5,41.5 326.5,42 327.2,42.5 328,42.2 328.5,40.2 329.2,39.8 329.5,38.5 330.2,37.8 331,35.5 331.8,35 332,33.5 332.5,33.2 333,31.5 334,30.5 334,29.5 334.8,28.8 335.8,26.8 336.2,26.5 349.5,26.5 349.8,26.8 349.5,28.5 348.5,29.2 348.5,30 347.8,31.5 347.2,31.8 346.8,33.2 346.2,33.5 346,34.8 345.2,35.5 344.8,37 344.2,37.2 343.5,39.2 343,39.5 342.8,40.8 341.8,42 341.8,42.8 340.8,43.8 340,45.8 339.2,46.5 339,47.8 338.5,48 338,49.5 337.5,49.8 336.8,51.8 336,52.5 335.8,53.8 335,54.2 335,55 334,56 334,56.8 333.8,56.8 333.8,78.8 318.2,78.8 317.8,78.2 317.8,56.5 317,55 316.5,54.8 315.8,52.8 315,52.2 314.8,51 314,50.5 313.5,49 313,48.8 312.8,47.8 311.5,46.2 309,41.2 308.2,40.8 308.2,40 307.8,39 307,38.5 306.8,37.2 306,36.8 305.5,35.2 305,35 303,31 302.5,30.8 302,29.2 301.5,29 300.8,27.5ZM420.8,26.5 456.8,26.5 457.5,27.5 457.5,38.5 457.2,39 456.8,39.2 447.5,39.2 446.8,39.8 446.8,78.2 446.2,78.8 431.5,78.8 431,78.2 431,76.5 431.2,76.5 431,76 431,40.8 431.2,40.5 431,40.5 431,39.8 430.2,39.2 420.8,39.2 420.2,38.8 420.2,27ZM475,26.5 513.5,26.5 514,27 514.2,27.5 514.2,38 513.5,38.8 491.2,38.8 490.5,39.5 490.5,45 491.5,46 509.2,46 509.8,46.8 509.8,57.2 509.5,57.8 508.8,58.2 491.2,58.2 490.5,59 490.5,65.2 490.8,65.8 491.8,66.2 513.8,66.2 514.2,67 514.2,78.2 513.8,78.8 474.8,78.8 474.5,78.2 474.5,27.5ZM533.8,26.5 554,26.5 554.5,26.8 555.2,28 555.2,29.2 555.5,29.2 555.5,30.2 556.2,31.8 556.8,35 557.5,36.2 557.8,38.5 558.5,39.8 559,43 559.8,44.2 560,47 560.8,48 560.8,49.2 561,49.2 561,51 561.8,51.8 562.8,51 562.8,50.2 563.2,49.5 564.2,44.2 564.8,43.8 565,41.5 565.8,40.2 566,37.2 566.8,36 567.2,32.8 568,31.5 568.2,28.5 569.5,26.5 589.8,26.5 590.2,27.2 590.2,78.2 590,78.8 575.5,78.8 575,78.2 575,51.2 575.2,51.2 575.2,48.5 575,48.5 574.8,47 573.8,47.8 573.5,49 573.2,49 573.2,50.5 573,50.5 573,51.5 572.2,53 572,55.8 571,57.8 571,59.5 570.8,59.5 570.8,60.5 570,62 570,63.8 569.8,63.8 569.8,64.8 569,66 568.8,68.5 568,70 567.8,72.5 567.5,72.5 567.5,73.5 566.8,75 566.2,78.2 565.8,78.8 555.5,78.8 555,78.2 554.2,74.2 553.5,72.8 553.5,71.2 553.2,71.2 553.2,70.5 553,70.5 553,69.8 552.2,68.2 552.2,66.8 552,66.8 552,65.8 551.2,64.2 551,61.8 550.2,60.8 550,58 549.2,56.8 548.8,53.5 548.2,53 547.8,49.5 547.5,49.5 547.5,48.8 547,48.2 547,47.5 546,45.5 545.5,46 545.5,47.2 545.8,47.2 545.8,78.2 545.2,78.8 533.5,78.8 533.2,78.5 533.2,27ZM54.5,37.5 53.8,38.2 53.8,46.2 54.2,46.8 62.8,46.8 62.8,46.5 64.8,46 65.8,45 66.2,44 66.2,40.2 65.2,38.8 63.8,38 60.5,37.8 60.5,37.5ZM120.5,42.8 120,43 119.8,45 119.5,45 119.5,45.8 119,46 118.8,48.2 118,49.8 117.5,53 117,53.5 116.8,55.2 116.5,55.2 116.5,56.8 117.5,57.2 122.2,57.2 122.2,57 124,57.2 124.5,57 124.8,55.8 123.8,53.8 123.8,52 122.8,50 122.5,47.8 121.5,46 121.2,43.2 121,42.8ZM54.8,57.2 54,57.5 53.8,58 53.8,66.8 54.2,67.2 63.2,67.2 63.2,67 65.5,66.5 67.2,64.5 67.5,61.2 67.2,61.2 67,60 65.5,58.5 62.8,57.8 62.8,57.5 57.8,57.5 57.8,57.2 55.5,57.5 55.5,57.2Z"/></g>
</svg>
```

<!--
Yamazumi is Japanese for "stacked up." One bar per operator, height = the manual work assigned to them, with takt drawn across.
Today's assignment grew over time: Op A does elements 1 through 5 (78 s), Op B only 6 and 7 (31 s).
-->

---

![position=center size=100%](footer-19.svg)

# Read the chart

- Op A at 78 s is **over takt**: the line can only make one every 78 s
- 54,000 s ÷ 78 s = **692 units** vs. 900 demanded
- Ops B, C, D **wait** for A: 114 s of idle time every cycle
- Result: overtime every day, with four people who aren't busy

<!--
The bottleneck sets the pace for the whole line. Four operators × 78 s = 312 s of paid time per unit, for 198 s of work. That's 37% waste baked into the design, before any breakdown happens.
Ask the room: does this look familiar? What does the planner do when output is 692 and demand is 900? Overtime, Saturday shifts, expediting.
-->

---

![position=center size=100%](footer-20.svg)

# Part 2

## Distribute the work

---

![position=center size=100%](footer-21.svg)

# How many operators?

**Operators** = total work content ÷ takt time

198 s ÷ 60 s = **3.3 operators**

<!--
This is the theoretical minimum. You can't hire 0.3 of a person, so the question becomes: round up to 4, or kaizen the work content down until 3 is enough?
198 s of work at 3 operators would need 66 s per person, over takt. To run with 3 we'd need to remove at least 18 s of waste.
-->

---

![position=center size=100%](footer-22.svg)

# Plan for reality: planned cycle time

**Planned cycle time** = takt × planned uptime

60 s × 92% ≈ **55 s**

- Covers changeovers, small stops, quality checks
- Balance to 55 s, not 60 s
- Keep the margin honest: it's not a buffer for waste

<!--
If you balance exactly to takt, any hiccup puts you behind and you never catch up. Planned cycle time leaves room for known losses such as changeovers and planned checks.
Planners and engineers should agree on this number together, based on real uptime data.
198 ÷ 55 = 3.6, so we plan for 4 operators.
-->

---

![position=center size=100%](footer-23.svg)

# Rules for distributing the work

1. Follow the **sequence**: respect what must come first
2. **Fill** each operator to planned cycle time, in order
3. Never **split** an element between two people
4. Put the **remainder** on the last operator
5. Keep the operator **moving** while machines run

<!--
Rule 4 is the one people resist. The instinct is to share the work evenly. Don't.
Loading the remainder onto the last operator makes the leftover capacity visible in one place. That gap is the kaizen target: remove enough waste and you free a whole person for other work.
-->

---

![position=center size=100%](footer-24.svg)

# Even balance hides waste

| Operator | Share evenly | Fill to 55 s |
| --- | :---: | :---: |
| A | 49.5 s | 54 s |
| B | 49.5 s | 55 s |
| C | 49.5 s | 49 s |
| D | 49.5 s | **40 s** |
| Waste is… | spread out, invisible | in one place, visible |

<!--
With even sharing, every operator has 5 to 10 seconds of slack. People fill slack: they work slower, build ahead, or chat. Nobody sees it.
With fill-to-PCT, operator D has 40 s of work, about 15 s short. Everyone can see it, and it's one clear target. Remove 15 seconds of waste from the line and D's work can be absorbed.
-->

---

# Future state: the yamazumi

```svg
<svg viewBox="0 0 640 340">
  <g font-size="15" fill="var(--dark-foreground)" text-anchor="end">
    <text x="50" y="305">0</text><text x="50" y="215">30</text><text x="50" y="125">60</text><text x="50" y="65">80</text>
  </g>
  <line x1="60" y1="300" x2="620" y2="300" stroke="var(--foreground)" stroke-width="2"/>
  <rect x="100" y="138" width="90" height="162" fill="var(--accent)"/>
  <rect x="230" y="135" width="90" height="165" fill="var(--accent)"/>
  <rect x="360" y="153" width="90" height="147" fill="var(--accent)"/>
  <rect x="490" y="180" width="90" height="120" fill="var(--yellow)"/>
  <line x1="60" y1="120" x2="620" y2="120" stroke="var(--foreground)" stroke-width="3" stroke-dasharray="10 6"/>
  <text x="620" y="110" font-size="17" text-anchor="end" font-weight="bold">Takt 60 s</text>
  <line x1="60" y1="135" x2="620" y2="135" stroke="var(--green)" stroke-width="2" stroke-dasharray="3 4"/>
  <text x="620" y="156" font-size="15" text-anchor="end" fill="var(--green)" font-weight="bold">PCT 55 s</text>
  <g font-size="20" text-anchor="middle" font-weight="bold" fill="var(--background)">
    <text x="145" y="230">54</text><text x="275" y="230">55</text><text x="405" y="240">49</text><text x="535" y="250">40</text>
  </g>
  <g font-size="16" text-anchor="middle">
    <text x="145" y="325">Op A · 1–4</text><text x="275" y="325">Op B · 5–7</text><text x="405" y="325">Op C · 8–10</text><text x="535" y="325">Op D · 11–12</text>
  </g>
  <text id="slide-number" x="-99.1" y="341.2" font-size="11.1" fill="var(--foreground)">25</text>
  <g id="bae-logo" transform="translate(632.7,328.8) scale(0.1546)"><rect width="688" height="106" fill="#ED1A3B"/><path fill="#FFFFFF" fill-rule="evenodd" d="M263.8,25.8 270.5,25.8 270.5,26 272,26 272,26.2 274.2,26.2 276.2,27.2 277.5,27.2 278.2,28 279.5,28.2 280.5,28.8 280.8,29.2 281.8,29.5 282.8,30.8 283.2,30.8 285.2,32.8 285.2,33.2 286.2,34 286.8,35.5 287.2,35.8 288,37.2 288,38.8 287.2,39.2 285.2,39.5 283.5,40.5 282.2,40.5 282.2,40.8 280.5,41 280,41.5 278,41.8 276.2,42.8 274.8,42.8 274.2,42.2 274,41 271.8,38.8 270,38.2 270,38 268,37.8 268,37.5 265.5,37.5 265.5,37.8 263.5,38 261.8,39.8 261.5,41 261.8,41 262.2,42.8 263.5,43 265,44 269.2,44.5 269.2,44.8 271,45 271,45.2 274.2,45.5 275.2,46.2 277.5,46.5 278.8,47.2 279.8,47.2 281.5,48.5 282.8,48.8 284,50 284.5,50 287.8,53.5 287.8,54.2 288.5,55 288.8,56.8 289.5,58 289.8,65 289.5,65 288.8,68.2 287.5,70.8 286.8,71.2 286.8,71.8 283.8,74.8 282,75.5 281.2,76.5 280,76.8 278.2,77.8 277.2,77.8 275.5,78.8 274,78.8 274,79 272.8,79 271.8,79.5 263,79.8 263,79.5 260.8,79.5 260.8,79.2 258.8,79 258.8,78.8 257,78.8 255.5,77.8 253.8,77.5 253.5,77 251.5,76.2 251.2,75.8 249.2,74.8 246.5,72 246.5,71.5 245,70 245,69.2 244.2,68.5 243.5,66 243,65.5 243.2,63.2 246.5,63 246.5,62.8 248.2,62.5 248.2,62.2 250.8,62.2 250.8,62 252,62 252.5,61.5 254,61.5 254,61.2 255.5,61.2 255.5,61 257.8,61 259.2,64 260.5,65.2 261,65.2 261.2,65.8 263.2,66.8 269.8,67 269.8,66.8 271.5,66.5 273.2,64.8 273,63 270.5,60.8 268,60.5 266.5,59.8 263.2,59.5 262.5,59 258.2,58.2 257.5,57.5 255.8,57.2 253.8,56 253,56 252.5,55.2 251.2,55 247.5,51.2 247,49.8 246.2,49 246,47.2 245.5,46.5 245.2,40.8 245.5,40.8 245.5,39.5 246,39 246.2,36.8 247,36 247.5,34.2 250,31.8 250,31.2 250.8,31 251,30.2 251.5,30.2 252.2,29.2 253.2,29 254,28.2 255.8,27.8 256,27.2 258.2,27 259.8,26.2 263.8,26ZM380.2,25.8 388.8,26 388.8,26.2 390.2,26.2 391.8,27 393.8,27.2 395.2,28.2 396,28.2 396.2,28.8 396.8,28.8 397,29.2 399,30.2 400.5,32 401,32 401,32.5 402,33.2 402.5,34.5 403.2,35 404.2,37 404.2,37.8 404.5,37.8 404.2,38.8 403.5,39.2 402.5,39.2 402.5,39.5 401,39.8 399.8,40.5 398.5,40.5 396.5,41.5 394.2,41.8 392.5,42.8 391.2,42.8 390.5,42 389.8,40.2 388,38.8 386.2,38.2 386.2,38 384,37.8 384,37.5 382,37.5 381,38 379.8,38 378.2,39.2 377.8,40.2 377.8,41.2 378.5,42 378.5,42.5 379.8,43.2 380.5,43.2 381.2,44 385.5,44.5 385.5,44.8 387.2,45 387.2,45.2 389.5,45.2 391,46 394,46.5 395.8,47.5 396.8,47.5 397.5,48.2 399.5,49 401.2,50.8 401.8,50.8 402.5,51.5 402.5,52 403.5,52.8 405.8,57.2 405.8,59.8 406,59.8 406,61.2 406.2,61.2 405.8,66.5 405.5,66.5 405.5,67.2 403.5,71.2 402.5,72 402.5,72.5 401,74 400.5,74 399.8,75 398.2,75.5 397.8,76.2 396,76.8 395.2,77.5 393.8,77.8 392.8,78.5 389,79 388,79.5 386,79.5 386,79.8 377,79.5 377,79.2 376,79.2 375.2,78.8 372.8,78.5 372.2,78 370.8,77.8 367.8,76.2 367.5,75.8 366.2,75.2 365.8,74.5 365.2,74.5 363.2,72.5 363.2,72 362.2,71.2 362,70.2 361.2,69.8 360.8,68.2 360,67.5 360,66.2 359,64.5 359,63.8 359.5,63.2 361.8,63.2 363.2,62.5 368.2,62 368.2,61.8 369.2,61.8 370,61.2 373.8,61 374.2,61.2 375.2,63.5 377.2,65.5 378.2,65.8 378.8,66.5 379.5,66.5 379.5,66.8 386,67 386,66.8 387.2,66.8 389,65.5 389.2,64.2 389.5,64.2 389,62.2 387.5,61.5 387.2,61 384.5,60.5 384.5,60.2 382.8,60 382.8,59.8 381,59.8 380,59.2 378.5,59.2 377.8,58.8 374.8,58.2 374.2,57.8 372,57.2 370.5,56.2 369.2,56 368.8,55.2 367.2,54.8 364.8,52.5 364.8,52 363.5,50.8 363,49 362.2,48.2 362.2,47 362,47 362,45.8 361.8,45.8 361.8,40.5 362,40.5 362.2,37.5 363,36.8 363.2,35.5 364,34 364.5,33.8 364.5,33.2 365.8,32.2 365.8,31.8 367.2,30.2 367.8,30.2 368.2,29.5 369.2,29.2 369.5,28.8 371.5,28 371.8,27.5 373.8,27.2 375.8,26.2 378,26.2 378,26 380.2,26ZM627,25.8 634,25.8 634,26 635.5,26 635.5,26.2 637.8,26.2 639.8,27.2 641,27.2 642,28.2 643.5,28.5 643.8,29 645,29.5 645.5,30.2 646,30.2 646.5,31 647,31 648.2,32.2 648.2,32.8 649,33.2 649,33.8 650,34.5 650,35.2 650.8,35.8 651,37.2 651.5,37.8 651.5,38.8 650.8,39.2 649.2,39.2 648.2,40 644.8,40.8 643.5,41.5 641.2,41.8 639.5,42.8 638.2,42.8 637.5,41.2 637,41 637,40.5 635.5,39 635,39 634.2,38.2 632.5,38 632.5,37.8 628.8,37.5 628,38 627,38 626,38.5 625,40 625.2,42 626.2,43 627.5,43.2 628.2,44 631.2,44.2 631.2,44.5 632.5,44.5 632.5,44.8 633.5,44.8 634.5,45.2 637.5,45.5 639,46.2 641,46.5 642,47.2 643,47.2 643,47.5 643.8,47.5 645.8,48.5 646,49 647.2,49.5 648.2,50.8 648.8,50.8 649.2,51.8 649.8,51.8 649.8,52.2 650.5,52.8 650.5,53.2 652,55 652,56.2 652.8,57.5 653,60.2 653.2,60.2 653,65.2 652.8,65.2 652.8,66.2 652,67.8 652,68.8 651.2,69.5 650.8,71 649.8,71.8 649.8,72.2 649,73 648,73.5 648,74 647.5,74 646.8,75 646.2,75 644.5,76.5 643.2,76.8 642.2,77.5 640,78 639.8,78.5 639,78.5 639,78.8 637.2,78.8 637.2,79 636,79 635.2,79.5 626.5,79.8 626.5,79.5 624,79.5 623.5,79 620.5,78.8 619,77.8 617.8,77.8 617,77 615.2,76.5 615,76 613,75 609.8,71.8 609.8,71.2 609,70.8 608.2,69 607.8,68.8 607,66.2 606.2,65.2 606.5,63.2 609.8,63 609.8,62.8 610.8,62.8 611.5,62.2 614.2,62.2 614.2,62 615.2,62 616,61.5 617.5,61.5 617.5,61.2 619,61.2 619,61 621.2,61 622.8,64 624.2,65.5 626.8,66.8 633,67 633,66.8 634.8,66.5 636.2,65.2 636.5,63.2 634,60.8 631.5,60.5 630,59.8 626.8,59.5 626,59 621.8,58.2 620.5,57.2 619,57.2 618,56.8 617.8,56.2 617,56.2 616,55.8 615.8,55.2 614.8,55 610.8,51 609.5,48.5 609,46 608.8,46 608.8,43.8 608.5,43.8 608.8,40 609,40 609,39 609.8,37.8 609.8,36.8 611,34.2 612,33.2 612,32.8 615,29.8 615.5,29.8 615.8,29.2 616.8,29 617.5,28.2 618.8,28 619.5,27.2 620.8,27.2 620.8,27 621.5,27 623,26.2 625,26.2 625,26 627,26ZM39.5,26.5 69.5,26.5 70.2,27 73,27.2 74.5,28.2 75.2,28.2 77,30 77.5,30 78,31 79.2,32 79.2,32.5 79.8,32.8 80.8,34.8 80.8,35.5 81,35.5 81,36.2 81.8,37.8 81.8,42.8 81.5,42.8 81.2,44.2 79.5,47.8 76.8,50.5 75.2,50.8 74.8,51.8 76.2,52.5 76.5,53 77.8,53.2 78.5,54.2 79,54.2 80.8,56 81,57 81.8,57.5 82,59 82.8,59.8 83,65.5 82.8,65.5 82.8,68 81.8,70 81.8,71.2 80.8,72.2 79.8,74.2 78.5,75.5 78,75.5 77.5,76.2 76,76.8 75.2,77.5 74.2,77.5 74.2,77.8 72.8,78 72.2,78.5 71,78.5 71,78.8 39.5,78.8 39.2,78.5 39.2,27ZM113.8,26.5 130.2,26.5 131,27.2 131.2,29.2 132,30 132.2,32.2 133.5,34.8 133.5,36 133.8,36 133.8,36.8 134,36.8 134,37.5 134.8,39 135,40.8 135.8,42 136.2,44.8 136.8,45.2 137,47.5 137.8,48.2 138,50.8 138.8,51.8 139,53.8 140,55.5 140.2,57.8 141,59 141.5,61.8 142.5,63.8 142.5,65 143.5,66.8 143.5,67.8 143.8,67.8 143.8,68.8 144.8,70.8 145,72.8 145.8,73.8 146,76.2 147,77.8 146.8,78.8 130.5,78.8 129.5,76.8 129,73.8 128.2,72.8 127.8,69.5 126.8,68.8 114,68.8 113.2,69.5 113,71.8 112,73.8 112,75.2 111,76.8 111,78.2 110.5,78.8 97.8,78.8 97.5,78.5 97.5,77.5 98,77 98,75.2 98.5,75 98.8,73.8 99,73.8 99,72.2 100,70.5 100.2,68.2 101,67.2 101.2,65 102.2,63 102.5,60.8 103.2,59.8 103.5,58 104.2,56.5 104.2,55.5 104.5,55.5 104.5,54.8 104.8,54.8 104.8,54 105.5,52.5 105.5,51.5 106,50.8 106,49.8 106.8,48.5 107,46.5 108,44.8 108,43.2 109,41.5 109.2,39.2 110,38.2 110.2,36 111.2,34 111.2,32.8 112.2,30.8 112.5,28.8ZM164.2,26.5 202.8,26.5 203,26.8 203,27.8 203.2,27.8 203.2,37.8 202.5,38.8 180,38.8 179.5,39.8 179.5,45 180.2,46 198.2,46 198.8,47 198.8,57 198.2,58 197.8,58.2 181.2,58.2 181.2,58 180,58.2 179.5,59 179.5,65.2 179.8,65.8 180.2,66.2 202.8,66.2 203.2,67.2 203.2,68.5 203,68.5 203.2,69 203.2,75.5 203,75.5 203.2,78.2 202.8,78.8 164,78.8 163.8,78.5 163.8,27ZM301,26.5 317.8,26.5 318.2,26.8 319,27.5 319.5,29 320,29.2 320,30 320.5,31 321,31.2 321.8,33.2 322.2,33.5 322.8,35.2 323.8,36.2 323.8,37 324.5,37.8 325,39.5 326,40.5 326,41.2 326.5,41.5 326.5,42 327.2,42.5 328,42.2 328.5,40.2 329.2,39.8 329.5,38.5 330.2,37.8 331,35.5 331.8,35 332,33.5 332.5,33.2 333,31.5 334,30.5 334,29.5 334.8,28.8 335.8,26.8 336.2,26.5 349.5,26.5 349.8,26.8 349.5,28.5 348.5,29.2 348.5,30 347.8,31.5 347.2,31.8 346.8,33.2 346.2,33.5 346,34.8 345.2,35.5 344.8,37 344.2,37.2 343.5,39.2 343,39.5 342.8,40.8 341.8,42 341.8,42.8 340.8,43.8 340,45.8 339.2,46.5 339,47.8 338.5,48 338,49.5 337.5,49.8 336.8,51.8 336,52.5 335.8,53.8 335,54.2 335,55 334,56 334,56.8 333.8,56.8 333.8,78.8 318.2,78.8 317.8,78.2 317.8,56.5 317,55 316.5,54.8 315.8,52.8 315,52.2 314.8,51 314,50.5 313.5,49 313,48.8 312.8,47.8 311.5,46.2 309,41.2 308.2,40.8 308.2,40 307.8,39 307,38.5 306.8,37.2 306,36.8 305.5,35.2 305,35 303,31 302.5,30.8 302,29.2 301.5,29 300.8,27.5ZM420.8,26.5 456.8,26.5 457.5,27.5 457.5,38.5 457.2,39 456.8,39.2 447.5,39.2 446.8,39.8 446.8,78.2 446.2,78.8 431.5,78.8 431,78.2 431,76.5 431.2,76.5 431,76 431,40.8 431.2,40.5 431,40.5 431,39.8 430.2,39.2 420.8,39.2 420.2,38.8 420.2,27ZM475,26.5 513.5,26.5 514,27 514.2,27.5 514.2,38 513.5,38.8 491.2,38.8 490.5,39.5 490.5,45 491.5,46 509.2,46 509.8,46.8 509.8,57.2 509.5,57.8 508.8,58.2 491.2,58.2 490.5,59 490.5,65.2 490.8,65.8 491.8,66.2 513.8,66.2 514.2,67 514.2,78.2 513.8,78.8 474.8,78.8 474.5,78.2 474.5,27.5ZM533.8,26.5 554,26.5 554.5,26.8 555.2,28 555.2,29.2 555.5,29.2 555.5,30.2 556.2,31.8 556.8,35 557.5,36.2 557.8,38.5 558.5,39.8 559,43 559.8,44.2 560,47 560.8,48 560.8,49.2 561,49.2 561,51 561.8,51.8 562.8,51 562.8,50.2 563.2,49.5 564.2,44.2 564.8,43.8 565,41.5 565.8,40.2 566,37.2 566.8,36 567.2,32.8 568,31.5 568.2,28.5 569.5,26.5 589.8,26.5 590.2,27.2 590.2,78.2 590,78.8 575.5,78.8 575,78.2 575,51.2 575.2,51.2 575.2,48.5 575,48.5 574.8,47 573.8,47.8 573.5,49 573.2,49 573.2,50.5 573,50.5 573,51.5 572.2,53 572,55.8 571,57.8 571,59.5 570.8,59.5 570.8,60.5 570,62 570,63.8 569.8,63.8 569.8,64.8 569,66 568.8,68.5 568,70 567.8,72.5 567.5,72.5 567.5,73.5 566.8,75 566.2,78.2 565.8,78.8 555.5,78.8 555,78.2 554.2,74.2 553.5,72.8 553.5,71.2 553.2,71.2 553.2,70.5 553,70.5 553,69.8 552.2,68.2 552.2,66.8 552,66.8 552,65.8 551.2,64.2 551,61.8 550.2,60.8 550,58 549.2,56.8 548.8,53.5 548.2,53 547.8,49.5 547.5,49.5 547.5,48.8 547,48.2 547,47.5 546,45.5 545.5,46 545.5,47.2 545.8,47.2 545.8,78.2 545.2,78.8 533.5,78.8 533.2,78.5 533.2,27ZM54.5,37.5 53.8,38.2 53.8,46.2 54.2,46.8 62.8,46.8 62.8,46.5 64.8,46 65.8,45 66.2,44 66.2,40.2 65.2,38.8 63.8,38 60.5,37.8 60.5,37.5ZM120.5,42.8 120,43 119.8,45 119.5,45 119.5,45.8 119,46 118.8,48.2 118,49.8 117.5,53 117,53.5 116.8,55.2 116.5,55.2 116.5,56.8 117.5,57.2 122.2,57.2 122.2,57 124,57.2 124.5,57 124.8,55.8 123.8,53.8 123.8,52 122.8,50 122.5,47.8 121.5,46 121.2,43.2 121,42.8ZM54.8,57.2 54,57.5 53.8,58 53.8,66.8 54.2,67.2 63.2,67.2 63.2,67 65.5,66.5 67.2,64.5 67.5,61.2 67.2,61.2 67,60 65.5,58.5 62.8,57.8 62.8,57.5 57.8,57.5 57.8,57.2 55.5,57.5 55.5,57.2Z"/></g>
</svg>
```

<!--
Same 198 s of work, same 4 people, redistributed with the rules.
A: elements 1-4 = 54 s. B: 5-7 = 55 s. C: 8-10 = 49 s (adding element 11 would make 61, over PCT). D: 11-12 = 40 s.
No one is over takt, so the line can now make one every 55 s: 54,000 ÷ 55 = 981 units capacity vs. 900 demand. Overtime disappears.
Op D in yellow is the kaizen target.
-->

---

![position=center size=100%](footer-26.svg)

# Before and after

| | Current | Future |
| --- | :---: | :---: |
| Slowest operator | 78 s | **55 s** |
| Daily capacity | 692 | **981** |
| Meets demand of 900? | ✘ | ✔ |
| Operators | 4 | 4 |
| Capital spent | | **$0** |

<!--
We didn't buy a machine or hire anyone. We just understood the work and distributed it deliberately.
That's the point of this whole session: most capacity problems are distribution problems.
-->

---

![position=center size=100%](footer-27.svg)

# Don't let operators wait on machines

- Load, start, and **walk away**: the machine finishes on its own
- **Auto-eject** so the operator doesn't have to unload
- Machine stops itself on a defect (**jidoka**)
- Machine cycle must be **< takt**

<!--
In our example the press (25 s) and leak tester (40 s) both run while the operator does other elements. The operator loads part N, starts the cycle, then moves on. On the next lap they unload N and load N+1.
A Standard Work Combination Table shows manual, machine, and walk time on a timeline against takt. Use it any time a machine is in the loop.
-->

---

![position=center size=100%](footer-28.svg)

# When demand changes, rebalance

| Demand / day | Takt | 198 s ÷ takt | Operators |
| ---: | :---: | :---: | :---: |
| 600 | 90 s | 2.2 | 3 |
| 900 | 60 s | 3.3 | 4 |
| 1,200 | 45 s | 4.4 | 5 |

<!--
Flow cells flex with demand by changing the number of people, not by running faster or building ahead.
Planners: prepare standard work for each staffing level ahead of time, so a demand change becomes a planned switch, not a scramble.
This is also why we want cells where work can easily be shifted between operators. That leads us to layout.
-->

---

![position=center size=100%](footer-29.svg)

# Part 3

## Arrange the cell

---

![position=center size=100%](footer-30.svg)

# Principles of a flow cell

- Stations in **process sequence**, close together
- Flow **counterclockwise**: the right hand leads to the next station
- **Start and finish together**: in and out at the same point
- **No space for WIP** between stations
- Operators **inside**, materials fed from **outside**

<!--
Counterclockwise is a convention: most people are right-handed and it lets them pass parts with the right hand. Pick one direction and use it everywhere.
Starting and finishing in the same spot means the person loading raw material can also see finished output, and the last operator can step straight back to the first station.
If there's room for a pile, a pile will appear. Put stations close enough that there's only room for one part.
-->

---

# The U-shaped cell

```svg
<svg viewBox="0 0 640 360">
  <g stroke="var(--dark-foreground)" stroke-width="2" fill="none" stroke-dasharray="6 5">
    <polyline points="110,86 110,166 110,246 250,306 390,306 530,246 530,166 530,86"/>
  </g>
  <g fill="var(--background)" stroke="var(--foreground)" stroke-width="2">
    <rect x="40" y="60" width="140" height="52" rx="8"/>
    <rect x="40" y="140" width="140" height="52" rx="8"/>
    <rect x="40" y="220" width="140" height="52" rx="8"/>
    <rect x="180" y="280" width="140" height="52" rx="8"/>
    <rect x="320" y="280" width="140" height="52" rx="8"/>
    <rect x="460" y="220" width="140" height="52" rx="8"/>
    <rect x="460" y="140" width="140" height="52" rx="8"/>
    <rect x="460" y="60" width="140" height="52" rx="8"/>
  </g>
  <g font-size="15" text-anchor="middle">
    <text x="110" y="92">1 Load</text>
    <text x="110" y="172">2 Press</text>
    <text x="110" y="252">3–4 Seal, shaft</text>
    <text x="250" y="312">5 Torque</text>
    <text x="390" y="312">6–7 Cover</text>
    <text x="530" y="252">8 Leak test</text>
    <text x="530" y="172">9–10 Wire, test</text>
    <text x="530" y="92">11–12 Pack</text>
  </g>
  <g font-size="18" font-weight="bold" fill="var(--accent)">
    <text x="78" y="36">IN ↓</text>
    <text x="508" y="36">OUT ↑</text>
  </g>
  <g stroke="var(--accent)" stroke-width="2" stroke-dasharray="2 4">
    <line x1="230" y1="166" x2="180" y2="86"/><line x1="230" y1="166" x2="180" y2="166"/><line x1="230" y1="166" x2="180" y2="246"/>
    <line x1="320" y1="230" x2="250" y2="280"/><line x1="320" y1="230" x2="390" y2="280"/>
    <line x1="410" y1="196" x2="460" y2="246"/><line x1="410" y1="196" x2="460" y2="166"/>
    <line x1="410" y1="86" x2="460" y2="86"/>
  </g>
  <g fill="var(--accent)">
    <circle cx="230" cy="166" r="20"/><circle cx="320" cy="230" r="20"/><circle cx="410" cy="196" r="20"/><circle cx="410" cy="86" r="20"/>
  </g>
  <g font-size="18" font-weight="bold" text-anchor="middle" fill="var(--background)">
    <text x="230" y="172">A</text><text x="320" y="236">B</text><text x="410" y="202">C</text><text x="410" y="92">D</text>
  </g>
  <text id="slide-number" x="-123.7" y="361.2" font-size="11.8" fill="var(--foreground)">31</text>
  <g id="bae-logo" transform="translate(651.1,348.1) scale(0.1637)"><rect width="688" height="106" fill="#ED1A3B"/><path fill="#FFFFFF" fill-rule="evenodd" d="M263.8,25.8 270.5,25.8 270.5,26 272,26 272,26.2 274.2,26.2 276.2,27.2 277.5,27.2 278.2,28 279.5,28.2 280.5,28.8 280.8,29.2 281.8,29.5 282.8,30.8 283.2,30.8 285.2,32.8 285.2,33.2 286.2,34 286.8,35.5 287.2,35.8 288,37.2 288,38.8 287.2,39.2 285.2,39.5 283.5,40.5 282.2,40.5 282.2,40.8 280.5,41 280,41.5 278,41.8 276.2,42.8 274.8,42.8 274.2,42.2 274,41 271.8,38.8 270,38.2 270,38 268,37.8 268,37.5 265.5,37.5 265.5,37.8 263.5,38 261.8,39.8 261.5,41 261.8,41 262.2,42.8 263.5,43 265,44 269.2,44.5 269.2,44.8 271,45 271,45.2 274.2,45.5 275.2,46.2 277.5,46.5 278.8,47.2 279.8,47.2 281.5,48.5 282.8,48.8 284,50 284.5,50 287.8,53.5 287.8,54.2 288.5,55 288.8,56.8 289.5,58 289.8,65 289.5,65 288.8,68.2 287.5,70.8 286.8,71.2 286.8,71.8 283.8,74.8 282,75.5 281.2,76.5 280,76.8 278.2,77.8 277.2,77.8 275.5,78.8 274,78.8 274,79 272.8,79 271.8,79.5 263,79.8 263,79.5 260.8,79.5 260.8,79.2 258.8,79 258.8,78.8 257,78.8 255.5,77.8 253.8,77.5 253.5,77 251.5,76.2 251.2,75.8 249.2,74.8 246.5,72 246.5,71.5 245,70 245,69.2 244.2,68.5 243.5,66 243,65.5 243.2,63.2 246.5,63 246.5,62.8 248.2,62.5 248.2,62.2 250.8,62.2 250.8,62 252,62 252.5,61.5 254,61.5 254,61.2 255.5,61.2 255.5,61 257.8,61 259.2,64 260.5,65.2 261,65.2 261.2,65.8 263.2,66.8 269.8,67 269.8,66.8 271.5,66.5 273.2,64.8 273,63 270.5,60.8 268,60.5 266.5,59.8 263.2,59.5 262.5,59 258.2,58.2 257.5,57.5 255.8,57.2 253.8,56 253,56 252.5,55.2 251.2,55 247.5,51.2 247,49.8 246.2,49 246,47.2 245.5,46.5 245.2,40.8 245.5,40.8 245.5,39.5 246,39 246.2,36.8 247,36 247.5,34.2 250,31.8 250,31.2 250.8,31 251,30.2 251.5,30.2 252.2,29.2 253.2,29 254,28.2 255.8,27.8 256,27.2 258.2,27 259.8,26.2 263.8,26ZM380.2,25.8 388.8,26 388.8,26.2 390.2,26.2 391.8,27 393.8,27.2 395.2,28.2 396,28.2 396.2,28.8 396.8,28.8 397,29.2 399,30.2 400.5,32 401,32 401,32.5 402,33.2 402.5,34.5 403.2,35 404.2,37 404.2,37.8 404.5,37.8 404.2,38.8 403.5,39.2 402.5,39.2 402.5,39.5 401,39.8 399.8,40.5 398.5,40.5 396.5,41.5 394.2,41.8 392.5,42.8 391.2,42.8 390.5,42 389.8,40.2 388,38.8 386.2,38.2 386.2,38 384,37.8 384,37.5 382,37.5 381,38 379.8,38 378.2,39.2 377.8,40.2 377.8,41.2 378.5,42 378.5,42.5 379.8,43.2 380.5,43.2 381.2,44 385.5,44.5 385.5,44.8 387.2,45 387.2,45.2 389.5,45.2 391,46 394,46.5 395.8,47.5 396.8,47.5 397.5,48.2 399.5,49 401.2,50.8 401.8,50.8 402.5,51.5 402.5,52 403.5,52.8 405.8,57.2 405.8,59.8 406,59.8 406,61.2 406.2,61.2 405.8,66.5 405.5,66.5 405.5,67.2 403.5,71.2 402.5,72 402.5,72.5 401,74 400.5,74 399.8,75 398.2,75.5 397.8,76.2 396,76.8 395.2,77.5 393.8,77.8 392.8,78.5 389,79 388,79.5 386,79.5 386,79.8 377,79.5 377,79.2 376,79.2 375.2,78.8 372.8,78.5 372.2,78 370.8,77.8 367.8,76.2 367.5,75.8 366.2,75.2 365.8,74.5 365.2,74.5 363.2,72.5 363.2,72 362.2,71.2 362,70.2 361.2,69.8 360.8,68.2 360,67.5 360,66.2 359,64.5 359,63.8 359.5,63.2 361.8,63.2 363.2,62.5 368.2,62 368.2,61.8 369.2,61.8 370,61.2 373.8,61 374.2,61.2 375.2,63.5 377.2,65.5 378.2,65.8 378.8,66.5 379.5,66.5 379.5,66.8 386,67 386,66.8 387.2,66.8 389,65.5 389.2,64.2 389.5,64.2 389,62.2 387.5,61.5 387.2,61 384.5,60.5 384.5,60.2 382.8,60 382.8,59.8 381,59.8 380,59.2 378.5,59.2 377.8,58.8 374.8,58.2 374.2,57.8 372,57.2 370.5,56.2 369.2,56 368.8,55.2 367.2,54.8 364.8,52.5 364.8,52 363.5,50.8 363,49 362.2,48.2 362.2,47 362,47 362,45.8 361.8,45.8 361.8,40.5 362,40.5 362.2,37.5 363,36.8 363.2,35.5 364,34 364.5,33.8 364.5,33.2 365.8,32.2 365.8,31.8 367.2,30.2 367.8,30.2 368.2,29.5 369.2,29.2 369.5,28.8 371.5,28 371.8,27.5 373.8,27.2 375.8,26.2 378,26.2 378,26 380.2,26ZM627,25.8 634,25.8 634,26 635.5,26 635.5,26.2 637.8,26.2 639.8,27.2 641,27.2 642,28.2 643.5,28.5 643.8,29 645,29.5 645.5,30.2 646,30.2 646.5,31 647,31 648.2,32.2 648.2,32.8 649,33.2 649,33.8 650,34.5 650,35.2 650.8,35.8 651,37.2 651.5,37.8 651.5,38.8 650.8,39.2 649.2,39.2 648.2,40 644.8,40.8 643.5,41.5 641.2,41.8 639.5,42.8 638.2,42.8 637.5,41.2 637,41 637,40.5 635.5,39 635,39 634.2,38.2 632.5,38 632.5,37.8 628.8,37.5 628,38 627,38 626,38.5 625,40 625.2,42 626.2,43 627.5,43.2 628.2,44 631.2,44.2 631.2,44.5 632.5,44.5 632.5,44.8 633.5,44.8 634.5,45.2 637.5,45.5 639,46.2 641,46.5 642,47.2 643,47.2 643,47.5 643.8,47.5 645.8,48.5 646,49 647.2,49.5 648.2,50.8 648.8,50.8 649.2,51.8 649.8,51.8 649.8,52.2 650.5,52.8 650.5,53.2 652,55 652,56.2 652.8,57.5 653,60.2 653.2,60.2 653,65.2 652.8,65.2 652.8,66.2 652,67.8 652,68.8 651.2,69.5 650.8,71 649.8,71.8 649.8,72.2 649,73 648,73.5 648,74 647.5,74 646.8,75 646.2,75 644.5,76.5 643.2,76.8 642.2,77.5 640,78 639.8,78.5 639,78.5 639,78.8 637.2,78.8 637.2,79 636,79 635.2,79.5 626.5,79.8 626.5,79.5 624,79.5 623.5,79 620.5,78.8 619,77.8 617.8,77.8 617,77 615.2,76.5 615,76 613,75 609.8,71.8 609.8,71.2 609,70.8 608.2,69 607.8,68.8 607,66.2 606.2,65.2 606.5,63.2 609.8,63 609.8,62.8 610.8,62.8 611.5,62.2 614.2,62.2 614.2,62 615.2,62 616,61.5 617.5,61.5 617.5,61.2 619,61.2 619,61 621.2,61 622.8,64 624.2,65.5 626.8,66.8 633,67 633,66.8 634.8,66.5 636.2,65.2 636.5,63.2 634,60.8 631.5,60.5 630,59.8 626.8,59.5 626,59 621.8,58.2 620.5,57.2 619,57.2 618,56.8 617.8,56.2 617,56.2 616,55.8 615.8,55.2 614.8,55 610.8,51 609.5,48.5 609,46 608.8,46 608.8,43.8 608.5,43.8 608.8,40 609,40 609,39 609.8,37.8 609.8,36.8 611,34.2 612,33.2 612,32.8 615,29.8 615.5,29.8 615.8,29.2 616.8,29 617.5,28.2 618.8,28 619.5,27.2 620.8,27.2 620.8,27 621.5,27 623,26.2 625,26.2 625,26 627,26ZM39.5,26.5 69.5,26.5 70.2,27 73,27.2 74.5,28.2 75.2,28.2 77,30 77.5,30 78,31 79.2,32 79.2,32.5 79.8,32.8 80.8,34.8 80.8,35.5 81,35.5 81,36.2 81.8,37.8 81.8,42.8 81.5,42.8 81.2,44.2 79.5,47.8 76.8,50.5 75.2,50.8 74.8,51.8 76.2,52.5 76.5,53 77.8,53.2 78.5,54.2 79,54.2 80.8,56 81,57 81.8,57.5 82,59 82.8,59.8 83,65.5 82.8,65.5 82.8,68 81.8,70 81.8,71.2 80.8,72.2 79.8,74.2 78.5,75.5 78,75.5 77.5,76.2 76,76.8 75.2,77.5 74.2,77.5 74.2,77.8 72.8,78 72.2,78.5 71,78.5 71,78.8 39.5,78.8 39.2,78.5 39.2,27ZM113.8,26.5 130.2,26.5 131,27.2 131.2,29.2 132,30 132.2,32.2 133.5,34.8 133.5,36 133.8,36 133.8,36.8 134,36.8 134,37.5 134.8,39 135,40.8 135.8,42 136.2,44.8 136.8,45.2 137,47.5 137.8,48.2 138,50.8 138.8,51.8 139,53.8 140,55.5 140.2,57.8 141,59 141.5,61.8 142.5,63.8 142.5,65 143.5,66.8 143.5,67.8 143.8,67.8 143.8,68.8 144.8,70.8 145,72.8 145.8,73.8 146,76.2 147,77.8 146.8,78.8 130.5,78.8 129.5,76.8 129,73.8 128.2,72.8 127.8,69.5 126.8,68.8 114,68.8 113.2,69.5 113,71.8 112,73.8 112,75.2 111,76.8 111,78.2 110.5,78.8 97.8,78.8 97.5,78.5 97.5,77.5 98,77 98,75.2 98.5,75 98.8,73.8 99,73.8 99,72.2 100,70.5 100.2,68.2 101,67.2 101.2,65 102.2,63 102.5,60.8 103.2,59.8 103.5,58 104.2,56.5 104.2,55.5 104.5,55.5 104.5,54.8 104.8,54.8 104.8,54 105.5,52.5 105.5,51.5 106,50.8 106,49.8 106.8,48.5 107,46.5 108,44.8 108,43.2 109,41.5 109.2,39.2 110,38.2 110.2,36 111.2,34 111.2,32.8 112.2,30.8 112.5,28.8ZM164.2,26.5 202.8,26.5 203,26.8 203,27.8 203.2,27.8 203.2,37.8 202.5,38.8 180,38.8 179.5,39.8 179.5,45 180.2,46 198.2,46 198.8,47 198.8,57 198.2,58 197.8,58.2 181.2,58.2 181.2,58 180,58.2 179.5,59 179.5,65.2 179.8,65.8 180.2,66.2 202.8,66.2 203.2,67.2 203.2,68.5 203,68.5 203.2,69 203.2,75.5 203,75.5 203.2,78.2 202.8,78.8 164,78.8 163.8,78.5 163.8,27ZM301,26.5 317.8,26.5 318.2,26.8 319,27.5 319.5,29 320,29.2 320,30 320.5,31 321,31.2 321.8,33.2 322.2,33.5 322.8,35.2 323.8,36.2 323.8,37 324.5,37.8 325,39.5 326,40.5 326,41.2 326.5,41.5 326.5,42 327.2,42.5 328,42.2 328.5,40.2 329.2,39.8 329.5,38.5 330.2,37.8 331,35.5 331.8,35 332,33.5 332.5,33.2 333,31.5 334,30.5 334,29.5 334.8,28.8 335.8,26.8 336.2,26.5 349.5,26.5 349.8,26.8 349.5,28.5 348.5,29.2 348.5,30 347.8,31.5 347.2,31.8 346.8,33.2 346.2,33.5 346,34.8 345.2,35.5 344.8,37 344.2,37.2 343.5,39.2 343,39.5 342.8,40.8 341.8,42 341.8,42.8 340.8,43.8 340,45.8 339.2,46.5 339,47.8 338.5,48 338,49.5 337.5,49.8 336.8,51.8 336,52.5 335.8,53.8 335,54.2 335,55 334,56 334,56.8 333.8,56.8 333.8,78.8 318.2,78.8 317.8,78.2 317.8,56.5 317,55 316.5,54.8 315.8,52.8 315,52.2 314.8,51 314,50.5 313.5,49 313,48.8 312.8,47.8 311.5,46.2 309,41.2 308.2,40.8 308.2,40 307.8,39 307,38.5 306.8,37.2 306,36.8 305.5,35.2 305,35 303,31 302.5,30.8 302,29.2 301.5,29 300.8,27.5ZM420.8,26.5 456.8,26.5 457.5,27.5 457.5,38.5 457.2,39 456.8,39.2 447.5,39.2 446.8,39.8 446.8,78.2 446.2,78.8 431.5,78.8 431,78.2 431,76.5 431.2,76.5 431,76 431,40.8 431.2,40.5 431,40.5 431,39.8 430.2,39.2 420.8,39.2 420.2,38.8 420.2,27ZM475,26.5 513.5,26.5 514,27 514.2,27.5 514.2,38 513.5,38.8 491.2,38.8 490.5,39.5 490.5,45 491.5,46 509.2,46 509.8,46.8 509.8,57.2 509.5,57.8 508.8,58.2 491.2,58.2 490.5,59 490.5,65.2 490.8,65.8 491.8,66.2 513.8,66.2 514.2,67 514.2,78.2 513.8,78.8 474.8,78.8 474.5,78.2 474.5,27.5ZM533.8,26.5 554,26.5 554.5,26.8 555.2,28 555.2,29.2 555.5,29.2 555.5,30.2 556.2,31.8 556.8,35 557.5,36.2 557.8,38.5 558.5,39.8 559,43 559.8,44.2 560,47 560.8,48 560.8,49.2 561,49.2 561,51 561.8,51.8 562.8,51 562.8,50.2 563.2,49.5 564.2,44.2 564.8,43.8 565,41.5 565.8,40.2 566,37.2 566.8,36 567.2,32.8 568,31.5 568.2,28.5 569.5,26.5 589.8,26.5 590.2,27.2 590.2,78.2 590,78.8 575.5,78.8 575,78.2 575,51.2 575.2,51.2 575.2,48.5 575,48.5 574.8,47 573.8,47.8 573.5,49 573.2,49 573.2,50.5 573,50.5 573,51.5 572.2,53 572,55.8 571,57.8 571,59.5 570.8,59.5 570.8,60.5 570,62 570,63.8 569.8,63.8 569.8,64.8 569,66 568.8,68.5 568,70 567.8,72.5 567.5,72.5 567.5,73.5 566.8,75 566.2,78.2 565.8,78.8 555.5,78.8 555,78.2 554.2,74.2 553.5,72.8 553.5,71.2 553.2,71.2 553.2,70.5 553,70.5 553,69.8 552.2,68.2 552.2,66.8 552,66.8 552,65.8 551.2,64.2 551,61.8 550.2,60.8 550,58 549.2,56.8 548.8,53.5 548.2,53 547.8,49.5 547.5,49.5 547.5,48.8 547,48.2 547,47.5 546,45.5 545.5,46 545.5,47.2 545.8,47.2 545.8,78.2 545.2,78.8 533.5,78.8 533.2,78.5 533.2,27ZM54.5,37.5 53.8,38.2 53.8,46.2 54.2,46.8 62.8,46.8 62.8,46.5 64.8,46 65.8,45 66.2,44 66.2,40.2 65.2,38.8 63.8,38 60.5,37.8 60.5,37.5ZM120.5,42.8 120,43 119.8,45 119.5,45 119.5,45.8 119,46 118.8,48.2 118,49.8 117.5,53 117,53.5 116.8,55.2 116.5,55.2 116.5,56.8 117.5,57.2 122.2,57.2 122.2,57 124,57.2 124.5,57 124.8,55.8 123.8,53.8 123.8,52 122.8,50 122.5,47.8 121.5,46 121.2,43.2 121,42.8ZM54.8,57.2 54,57.5 53.8,58 53.8,66.8 54.2,67.2 63.2,67.2 63.2,67 65.5,66.5 67.2,64.5 67.5,61.2 67.2,61.2 67,60 65.5,58.5 62.8,57.8 62.8,57.5 57.8,57.5 57.8,57.2 55.5,57.5 55.5,57.2Z"/></g>
</svg>
```

<!--
Our pump line as a U. Material comes in at top left, flows counterclockwise down, across, and up, and leaves at top right, next to where it came in.
Operators A–D work inside the U, each serving the stations in their balanced assignment. Parts and supplies are replenished from outside the U, so material handlers never get in the operators' way.
Notice D stands near both the last station and the first. When we kaizen out enough waste, D's work can be split between A and C across the U.
-->

---

![position=center size=100%](footer-32.svg)

# Choosing a cell shape

| Shape | Strengths | Watch out for |
| --- | --- | --- |
| **U** | Short walks, flexible staffing, start and end together | Needs floor space in a block |
| **L** | Fits corners, supports a feeder line | Less sharing across the cell |
| **Straight** | Simple, easy material feed | Long walks back to the start |

<!--
The U is the default because it gives the most options for assigning work: an operator can take stations on both sides of the U.
Straight lines are fine for short, one-operator cells or where building constraints force it.
The shape matters less than the principles: sequence, proximity, no WIP space, start and end together.
-->

---

![position=center size=100%](footer-33.svg)

# Ways to staff a cell

| Pattern | How it works | Best when |
| --- | --- | --- |
| **Divided** | Each operator owns a segment | Stable demand, distinct skills |
| **Across the U** | One operator takes stations on both sides | Odd remainders, low demand |
| **Rabbit chase** | Each operator builds the whole unit, following one another | Short total cycle, cross-trained team |

<!--
Divided is what we drew for the pump line.
Across the U is what lets us absorb operator D's work once we've done some kaizen.
Rabbit chase: each operator walks the whole loop with one part. It balances automatically but needs every station free when you arrive, and every operator fully trained.
-->

---

![position=center size=100%](footer-34.svg)

# Present materials at the point of use

- Parts within **easy reach**: no bending, no walking
- **Flow racks** loaded from outside, picked from inside
- Tools on **balancers or shadow boards**, always in the same spot
- Two-bin or kanban **replenishment**, sized to a known interval

<!--
Every time an operator reaches, bends, turns, or searches, that's seconds added to every cycle. At 900 units a day, 3 seconds of reaching is 45 minutes of lost time.
Material handlers run a fixed route on a fixed interval (a water spider) so operators never leave the cell for parts.
-->

---

![position=center size=100%](footer-35.svg)

# Design for flexibility

- **Right-sized equipment:** small, simple, dedicated
- **Mobile stations:** casters, quick-connect utilities
- **Standard WIP:** the minimum parts needed for flow, marked on the bench
- **Visual status:** andon, hour-by-hour board at the cell exit

<!--
Big, shared, monument machines force batching. One small press per cell beats one big press for the whole plant.
Utilities from above (drops) rather than through the floor make it possible to rearrange a cell over a weekend.
Standard WIP includes parts inside machines (the part in the press, the part in the leak tester) plus any required between operations. Mark the spots with tape so it's obvious when there's too much or too little.
-->

---

![position=center size=100%](footer-36.svg)

# Cell design checklist

- ☐ Stations in sequence, flowing one direction
- ☐ Start and finish next to each other
- ☐ No room for WIP beyond the standard
- ☐ Every machine cycle under takt
- ☐ Parts and tools reachable without walking
- ☐ Material fed from outside the cell

<!--
Use this as a walk-through checklist with the team when reviewing any proposed layout. Do a cardboard mock-up before moving any real equipment: tape on the floor and cardboard boxes for stations. Let operators walk the layout and change it.
-->

---

![position=center size=100%](footer-37.svg)

# Lock it in with standard work

1. **Takt time**: the pace
2. **Work sequence**: the order of elements for each operator
3. **Standard WIP**: the parts needed to keep flowing

<!--
Standard work is not a binder on a shelf. It's the current best way to do the job, posted at the station, written with the operators.
It's the baseline: when we improve, we update the standard. When something goes wrong, we compare to the standard to see what changed.
-->

---

![position=center size=100%](footer-38.svg)

> Where there is no standard, there can be no kaizen.

— Taiichi Ohno

<!--
Improvement needs a baseline. Without one, a change is just a different way of doing it, and nobody can tell whether it's better.
-->

---

![position=center size=100%](footer-39.svg)

# Sustain the flow

- **Hour-by-hour board:** planned vs. actual every hour
- **Andon:** stop and signal at the first problem
- **Leader response:** someone arrives within one takt cycle
- **Daily review:** top misses become tomorrow's kaizen

<!--
Flow makes problems visible immediately; that's the point. But visible problems only help if someone responds.
The hour-by-hour board turns takt into a daily conversation: at 60 s takt, the plan is 60 per hour. If we made 52, the board says why.
-->

---

![position=center size=100%](footer-40.svg)

# Practice: the flow game

**Round 1:** batches of 10, each station works independently

**Round 2:** one-piece flow, balanced to takt, cell layout

Measure: lead time, WIP, output, quality

<!--
Run the Paper Airplane Flow Game (see the facilitator tool in the lean folder).
Round 1: each station folds a batch of 10 before passing. Round 2: the team calculates takt from a given demand, times the folding elements, balances them, rearranges the tables into a U, and runs one-piece flow.
Debrief: what changed in lead time and WIP? What did each role notice? Who was waiting?
-->

---

![position=center size=100%](footer-41.svg)

# Workshop: our own line

1. **Planners:** bring demand and available time; calculate takt
2. **Technicians:** time the work elements at the line
3. **Engineers:** build the current yamazumi
4. **Together:** rebalance, sketch the cell, mock it up

<!--
Pick one product family with stable demand for the first attempt.
Day 1: takt and element timing. Day 2: current and future yamazumi. Day 3: cardboard mock-up and trial. Day 4–5: run, adjust, write standard work.
Report out to leadership at the end of the week using before/after metrics: lead time, WIP, output per labor hour.
-->

---

![position=center size=100%](footer-42.svg)

# Remember

- **Understand the work:** takt first, then elements and real times
- **Distribute the work:** fill to planned cycle time, make waste visible
- **Arrange the cell:** sequence, proximity, start and end together

<!--
Return to the problems the room listed at the start and ask which of today's tools address each one.
-->

---

![position=center size=100%](footer-43.svg)

# Make one. Check one. Move one.

Questions?
