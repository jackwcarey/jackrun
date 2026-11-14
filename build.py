"""Builds index.html for Jack's Cross-Country Run.

Layout copies the mmm.page original: a 520px-wide freeform stage, every
element absolutely positioned. Positions are in px on that stage and are
converted to cqw so the whole collage scales down on phones.
"""
from pathlib import Path

W = 520  # stage width in px (original canvas units)
H = 800


def u(px):
    return f"{px * 100 / W:.3f}cqw"


def box(x, y, w, h=None, extra=""):
    s = f"left:{u(x)};top:{u(y)};width:{u(w)};"
    if h is not None:
        s += f"height:{u(h)};"
    return s + extra


LINK_ICON = (
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" '
    'stroke-width="2.4" stroke-linecap="round" d="M10 14a4.5 4.5 0 0 0 6.4 0l3-3a4.5 4.5 0 0 0-6.4-6.4l-1 1'
    'M14 10a4.5 4.5 0 0 0-6.4 0l-3 3a4.5 4.5 0 0 0 6.4 6.4l1-1"/></svg>'
)

LINKS = {
    "fund": "https://liveoakcamp.app.neoncrm.com/np/clients/liveoakcamp/campaign.jsp?campaign=1&fundraiser=8&",
    "map": "https://ultrapacer.com/course/65fc83cb2aa36458e76710d8",
    "stories": "https://tripcast.co/i/KJHNECHG",
    "reflections": "https://docs.google.com/document/d/10gwhClT8ibdvLQiZjHEAGsQXn_U1pENk-9qWZXY-iEY/edit?tab=t.0#heading=h.60seo8i2831v",
}


def button(cls, href, label, x, y, w, h, extra=""):
    return (
        f'<a class="btn {cls}" href="{href}" target="_blank" rel="noopener" '
        f'style="{box(x, y, w, h, extra)}">{LINK_ICON}<span>{label}</span></a>'
    )


def img(src, alt, x, y, w, h, cls=""):
    return (
        f'<img class="{cls}" src="img/{src}" alt="{alt}" loading="lazy" '
        f'style="{box(x, y, w, h)}">'
    )


els = [
    # background shapes
    f'<svg class="shape" viewBox="0 0 512 512" style="{box(326, -55, 141, 141)}"><polygon points="256 0, 512 512, 0 512" fill="#bb8b41"/></svg>',
    f'<svg class="shape" viewBox="0 0 512 512" style="{box(4, 31, 80, 80)}"><rect width="512" height="512" fill="#b44b65"/></svg>',
    f'<svg class="shape" viewBox="0 0 512 512" style="{box(325, 188, 189, 189)}"><circle cx="256" cy="256" r="256" fill="#b44b65"/></svg>',
    # header photo + intro
    img("jack.png", "Jack running with a support stroller", 49, 8, 210, 211),
    f'<div class="intro" style="{box(266, 24, 156)}"><h1>hi, i&#8217;m jack.</h1>'
    "<p>in 2024 i ran 2,835 miles from LA &#8212;&gt;NYC, 50 mi/day for 57 days. "
    "check it out and join the adventure:</p></div>",
    button("b1", LINKS["fund"], "1) FUNDRAISING FOR LIVE OAK CAMP", 27, 223, 394, 47),
    img("map.png", "Map of the route from Los Angeles to New York", 82, 282, 283, 141),
    img("otter.gif", "", 93, 282, 121, 83, "otter"),
    button("b2", LINKS["map"], "2) Check out the map!", 134, 366, 222, 44, "transform:rotate(-5deg);"),
    button("b3", LINKS["stories"], "3) STORIES AND PICS HERE", 69, 432, 317, 51),
    button("b4", LINKS["reflections"], "4) POST-RUN REFLECTIONS", 37, 494, 374, 51),
    img("campfire.jpg", "Campers around a campfire", 26, 550, 193, 128),
    img("campers.jpg", "Campers and coaches covered in mud", 229, 550, 192, 128),
    f'<h2 class="thanks" style="{box(160, 722, 140, 24)}">A HUGE THANKS TO:</h2>',
    img("skratch.jpg", "Skratch Labs", 49, 718, 62, 32),
    img("topo.png", "Topo Athletic", 307, 724, 90, 32),
    img("masseys.png", "Massey's Professional Outfitters", 104, 756, 191, 30),
    img("ranger.png", "Ranger", 46, 759, 41, 33),
    img("stringking.png", "StringKing", 312, 767, 99, 22),
]

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jack's Cross-Country Run</title>
<meta name="description" content="In 2024 Jack ran 2,835 miles from LA to NYC, 50 miles a day for 57 days.">
<meta property="og:title" content="Jack's Cross-Country Run">
<meta property="og:description" content="2,835 miles from LA to NYC, 50 mi/day for 57 days.">
<meta property="og:image" content="img/jack.png">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='%23b44b65'/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Courier+Prime:wght@700&family=Special+Elite&display=swap" rel="stylesheet">
<style>
  :root {{ --bg: #ff6c2f; }}
  html, body {{ margin: 0; background: var(--bg); }}
  body {{ overflow-x: hidden; }}
  .wrap {{ width: min({W}px, calc(100vw - 32px)); margin: 0 auto; container-type: inline-size; }}
  .stage {{ position: relative; width: 100%; height: {u(H)}; overflow: hidden; }}
  .stage > * {{ position: absolute; margin: 0; box-sizing: border-box; }}
  .stage img {{ object-fit: cover; }}
  .intro {{ text-align: center; font-family: 'Courier Prime', monospace; color: #000; }}
  .intro h1 {{ font-size: {u(19)}; font-weight: 700; margin: 0 0 {u(8)}; }}
  .intro p {{ font-size: {u(12.5)}; line-height: 1.5; margin: 0; }}
  .btn {{ display: flex; align-items: center; justify-content: center; gap: {u(8)};
         border-radius: {u(8)}; text-decoration: none; font-family: 'Special Elite', monospace;
         font-size: {u(17)}; padding: 0 {u(14)} 0 {u(40)}; transition: transform .15s; }}
  .btn svg {{ position: absolute; left: {u(14)}; width: {u(17)}; height: {u(17)}; }}
  .btn:hover {{ filter: brightness(1.06); }}
  .b1 {{ background: #ffd222; color: #000; }}
  .b2 {{ background: #f91aa1; color: #fff; font-size: {u(14)}; }}
  .b3 {{ background: #a75154; color: #fff; }}
  .b4 {{ background: #407060; color: #fff; }}
  .b3 span, .b4 span {{ text-shadow: 0 1px 1px rgba(0,0,0,.35); }}
  .otter {{ object-fit: contain !important; z-index: 1; }}
  .b2 {{ z-index: 2; }}
  .thanks {{ font-family: 'Special Elite', monospace; font-weight: 400; color: #fff;
             font-size: {u(11)}; text-align: center; transform: rotate(-5deg); }}
  .stage img[alt*="Skratch"], .stage img[alt*="Topo"], .stage img[alt*="Massey"],
  .stage img[alt="Ranger"], .stage img[alt*="StringKing"] {{ object-fit: contain; }}
</style>
</head>
<body>
<main class="wrap"><div class="stage">
{chr(10).join(els)}
</div></main>
</body>
</html>
"""

Path(__file__).with_name("index.html").write_text(html)
print("wrote index.html")
