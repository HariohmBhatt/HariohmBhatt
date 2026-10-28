"""Build the profile banners in dark and light variants.

Run from the repository root: python3 scripts/build_banners.py
Tool logos are from Simple Icons (CC0 1.0).
"""
import base64
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"

DARK = dict(
    hero_bg=("#101a30", "#080d19"), card_bg=("#111b2e", "#0a111e"), grid="#a8c7ef", grid_op=".065",
    text="#f4f7fc", sub="#b9c8df", desc="#b5c5db", ring="#80a8c8", bracket="#ffb178", border="#6b83a5",
    panel="#101a2c", cyan="#5de4dd", purple="#c2a5ff", orange="#ffb178", indigo="#7c87ff", glow_op=".14",
)
LIGHT = dict(
    hero_bg=("#ffffff", "#eaf1f8"), card_bg=("#ffffff", "#f0f5fa"), grid="#3a5a85", grid_op=".07",
    text="#0f1b2d", sub="#4a5b73", desc="#46566d", ring="#6a8db0", bracket="#c9661c", border="#6b83a5",
    panel="#ffffff", cyan="#0b8a84", purple="#6f52d4", orange="#c9661c", indigo="#5b67e8", glow_op=".10",
)

TOOLS = [
    ('Python', '#3776ab', 'M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z'),
    ('PyTorch', '#ee4c2c', 'M12.005 0L4.952 7.053a9.865 9.865 0 000 14.022 9.866 9.866 0 0014.022 0c3.984-3.9 3.986-10.205.085-14.023l-1.744 1.743c2.904 2.905 2.904 7.634 0 10.538s-7.634 2.904-10.538 0-2.904-7.634 0-10.538l4.647-4.646.582-.665zm3.568 3.899a1.327 1.327 0 00-1.327 1.327 1.327 1.327 0 001.327 1.328A1.327 1.327 0 0016.9 5.226 1.327 1.327 0 0015.573 3.9z'),
    ('OpenCV', '#5c3ee8', 'M11.8992.8525C8.735.8525 6.17 3.4175 6.17 6.5817c0 2.102 1.1321 3.9398 2.8198 4.9366l1.6412-2.7849c.0411-.0699.0176-.1593-.0495-.2048-.6233-.4227-1.0328-1.137-1.0328-1.947 0-1.298 1.0524-2.3504 2.3505-2.3504 1.2981 0 2.3505 1.0524 2.3505 2.3505 0 .8098-.4095 1.5242-1.0328 1.947-.0671.0454-.0907.1348-.0495.2047l1.6414 2.785c1.6878-.9969 2.8199-2.8346 2.8199-4.9367 0-3.1642-2.5653-5.7292-5.7295-5.7292zm-6.17 10.8366C2.565 11.6891 0 14.2541 0 17.4183c0 3.1642 2.565 5.7292 5.7292 5.7292 3.1798 0 5.8074-2.6995 5.7275-5.8762H8.2313c-.0847 0-.1513.0717-.1519.1564-.0082 1.266-1.0644 2.3411-2.3502 2.3411-1.2981 0-2.3505-1.0524-2.3505-2.3505 0-1.2982 1.0524-2.3505 2.3505-2.3505.34 0 .663.0724.9547.2022.0713.0318.1566.0077.1962-.0595l1.6464-2.7935c-.8273-.4636-1.7815-.7279-2.7973-.7279zm15.4424.7614l-1.6366 2.7878c-.041.07-.0172.1594.05.2048.624.4217 1.0348 1.1354 1.0363 1.9452.0022 1.298-1.0483 2.352-2.3465 2.3542-1.298.0023-2.3523-1.0482-2.3545-2.3462-.0015-.8098.4068-1.5248 1.0294-1.9486.067-.0457.0905-.1353.0492-.2051l-1.6464-2.7818c-1.6859.9998-2.8146 2.8394-2.811 4.9415.0056 3.1641 2.575 5.7248 5.7393 5.7192 3.1641-.0054 5.7246-2.575 5.7192-5.7392-.0037-2.1022-1.139-3.938-2.8284-4.9318z'),
    ('FastAPI', '#009688', 'M12 .0387C5.3729.0384.0003 5.3931 0 11.9988c-.001 6.6066 5.372 11.9628 12 11.9625 6.628.0003 12.001-5.3559 12-11.9625-.0003-6.6057-5.3729-11.9604-12-11.96m-.829 5.4153h7.55l-7.5805 5.3284h5.1828L5.279 18.5436q2.9466-6.5444 5.892-13.0896'),
    ('Docker', '#2496ed', 'M13.983 11.078h2.119a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185m-2.954-5.43h2.118a.186.186 0 00.186-.186V3.574a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.185.185.185m0 2.716h2.118a.187.187 0 00.186-.186V6.29a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.887c0 .102.082.185.185.186m-2.93 0h2.12a.186.186 0 00.184-.186V6.29a.185.185 0 00-.185-.185H8.1a.185.185 0 00-.185.185v1.887c0 .102.083.185.185.186m-2.964 0h2.119a.186.186 0 00.185-.186V6.29a.185.185 0 00-.185-.185H5.136a.186.186 0 00-.186.185v1.887c0 .102.084.185.186.186m5.893 2.715h2.118a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.185.185.185m-2.93 0h2.12a.185.185 0 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.185v1.888c0 .102.083.185.185.185m-2.964 0h2.119a.185.185 0 00.185-.185V9.006a.185.185 0 00-.184-.186h-2.12a.186.186 0 00-.186.186v1.887c0 .102.084.185.186.185m-2.92 0h2.12a.185.185 0 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.185v1.888c0 .102.082.185.185.185M23.763 9.89c-.065-.051-.672-.51-1.954-.51-.338.001-.676.03-1.01.087-.248-1.7-1.653-2.53-1.716-2.566l-.344-.199-.226.327c-.284.438-.49.922-.612 1.43-.23.97-.09 1.882.403 2.661-.595.332-1.55.413-1.744.42H.751a.751.751 0 00-.75.748 11.376 11.376 0 00.692 4.062c.545 1.428 1.355 2.48 2.41 3.124 1.18.723 3.1 1.137 5.275 1.137.983.003 1.963-.086 2.93-.266a12.248 12.248 0 003.823-1.389c.98-.567 1.86-1.288 2.61-2.136 1.252-1.418 1.998-2.997 2.553-4.4h.221c1.372 0 2.215-.549 2.68-1.009.309-.293.55-.65.707-1.046l.098-.288Z'),]

MOTION_OFF = "@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }"


def hero(t):
    photo = base64.b64encode((ASSETS / "portrait.jpg").read_bytes()).decode()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="440" viewBox="0 0 1200 440" role="img" aria-labelledby="title description">
  <title id="title">Hariohm Bhatt</title>
  <desc id="description">Portrait of Hariohm Bhatt. Computer vision and scientific machine learning.</desc>
  <style>
    .orbit {{ transform-box: fill-box; transform-origin: center; animation: orbit 90s linear infinite; }}
    .pulse {{ transform-box: fill-box; transform-origin: center; animation: pulse 3.2s ease-in-out infinite; }}
    @keyframes orbit {{ to {{ transform: rotate(360deg); }} }}
    @keyframes pulse {{ 50% {{ transform: scale(1.5); opacity: .5; }} }}
    @media (max-width: 600px) {{
      .eyebrow {{ font-size: 32px; }}
      .tagline {{ font-size: 44px; }}
      .tag {{ display: none; }}
    }}
    {MOTION_OFF}
  </style>
  <defs>
    <linearGradient id="bg" x2="1" y2="1"><stop stop-color="{t['hero_bg'][0]}"/><stop offset="1" stop-color="{t['hero_bg'][1]}"/></linearGradient>
    <radialGradient id="glow"><stop stop-color="{t['cyan']}" stop-opacity=".22"/><stop offset="1" stop-color="{t['cyan']}" stop-opacity="0"/></radialGradient>
    <linearGradient id="orbit"><stop stop-color="{t['cyan']}"/><stop offset="1" stop-color="{t['indigo']}"/></linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{t['grid']}" stroke-opacity="{t['grid_op']}"/></pattern>
    <clipPath id="frame"><rect width="1200" height="440" rx="24"/></clipPath>
    <clipPath id="portrait"><circle r="112"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="1200" height="440" fill="url(#bg)"/>
    <rect width="1200" height="440" fill="url(#grid)"/>
    <ellipse cx="985" cy="220" rx="360" ry="340" fill="url(#glow)"/>
    <path d="M0 438H1200" stroke="url(#orbit)" stroke-width="4"/>
    <g fill="none" transform="translate(985 220)">
      <circle r="182" stroke="{t['ring']}" stroke-opacity=".18" stroke-dasharray="3 10"/>
      <g class="orbit">
        <ellipse rx="196" ry="72" transform="rotate(-32)" stroke="url(#orbit)" stroke-width="2"/>
        <ellipse rx="196" ry="72" transform="rotate(32)" stroke="url(#orbit)" stroke-opacity=".4"/>
        <circle class="pulse" cx="166" cy="-104" r="7" fill="{t['orange']}"/>
        <circle cx="-166" cy="104" r="5" fill="{t['cyan']}"/>
      </g>
      <circle r="121" fill="{t['hero_bg'][1]}" stroke="url(#orbit)" stroke-width="3"/>
      <image clip-path="url(#portrait)" x="-112" y="-112" width="224" height="224" xlink:href="data:image/jpeg;base64,{photo}"/>
      <path d="M-148-118V-146H-120M120-146H148V-118M-148 118V146H-120M120 146H148V118" stroke="{t['bracket']}" stroke-width="2.5"/>
      <g class="tag" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="15">
        <rect x="-148" y="-174" width="118" height="24" rx="4" fill="{t['bracket']}"/>
        <text x="-140" y="-157" fill="{t['hero_bg'][1]}">person 0.99</text>
      </g>
    </g>
    <g font-family="{FONT}">
      <rect x="56" y="78" width="34" height="5" rx="2.5" fill="{t['orange']}"/>
      <text class="eyebrow" x="106" y="90" fill="{t['sub']}" font-size="22" letter-spacing="4">VISION / LEARNING / SYSTEMS</text>
      <text x="50" y="212" fill="{t['text']}" font-size="108" font-weight="750" letter-spacing="-5">Hariohm</text>
      <text x="50" y="316" fill="{t['text']}" font-size="108" font-weight="750" letter-spacing="-5">Bhatt<tspan fill="{t['orange']}">.</tspan></text>
      <text class="tagline" x="56" y="374" fill="{t['cyan']}" font-size="30">Computer vision · Scientific ML</text>
    </g>
  </g>
</svg>
'''


def focus(t, num, accent, title, desc, icon, css=""):
    c = t[accent]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="220" viewBox="0 0 1200 220" role="img" aria-labelledby="title description">
  <title id="title">{title}</title>
  <desc id="description">{desc}.</desc>
  <style>
    .flow {{ stroke-dasharray: 4 8; animation: flow 1.4s linear infinite; }}
    @keyframes flow {{ to {{ stroke-dashoffset: -12; }} }}{css}
    @media (max-width: 600px) {{
      .theme-title {{ font-size: 52px; transform: translateY(40px); }}
      .theme-number {{ font-size: 28px; transform: translateY(22px); }}
      .theme-description {{ display: none; }}
    }}
    {MOTION_OFF}
  </style>
  <defs>
    <linearGradient id="bg" x2="1" y2=".5"><stop stop-color="{t['card_bg'][0]}"/><stop offset="1" stop-color="{t['card_bg'][1]}"/></linearGradient>
    <radialGradient id="glow"><stop stop-color="{c}" stop-opacity="{t['glow_op']}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>
    <linearGradient id="accent" x2="0" y2="1"><stop stop-color="{c}" stop-opacity="0"/><stop offset=".5" stop-color="{c}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient>
    <linearGradient id="scanfade" x2="0" y2="1"><stop stop-color="{c}" stop-opacity="0"/><stop offset="1" stop-color="{c}" stop-opacity=".22"/></linearGradient>
    <clipPath id="frame"><rect x=".5" y=".5" width="1199" height="219" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="1200" height="220" fill="url(#bg)"/>
    <ellipse cx="1016" cy="110" rx="250" ry="200" fill="url(#glow)"/>
    <path d="M0 32V188" stroke="{c}" stroke-width="6"/>
    <path d="M832 25V195" stroke="url(#accent)" stroke-opacity=".3"/>
    <g transform="translate(1016 110)" color="{c}" fill="none">
{icon.replace("PANEL", t['panel'])}
    </g>
    <g font-family="{FONT}">
      <text class="theme-number" x="40" y="51" fill="{c}" font-size="21" letter-spacing="3">{num} / FOCUS</text>
      <text class="theme-title" x="38" y="116" fill="{t['text']}" font-size="44" font-weight="700" letter-spacing="-1">{title}</text>
      <text class="theme-description" x="40" y="169" fill="{t['desc']}" font-size="26">{desc}</text>
    </g>
  </g>
  <rect x=".5" y=".5" width="1199" height="219" rx="18" fill="none" stroke="{t['border']}" stroke-opacity=".22"/>
</svg>
'''


VISION = '''      <path d="M-79 34C-108-12-53-70-7-54S83-69 83-13 42 66-4 50-51 80-79 34Z" fill="currentColor" fill-opacity=".06" stroke="currentColor" stroke-width="2"/>
      <path d="M-56 21C-78-12-37-49-5-37S58-48 58-9 29 46-3 35-36 56-56 21Z" stroke="currentColor" stroke-opacity=".6" stroke-width="2"/>
      <path d="M-31 12C-43-7-21-28-3-21S33-27 33-5 16 26-2 20-20 32-31 12Z" stroke="currentColor" stroke-opacity=".4" stroke-width="2"/>
      <path d="M-98-72H-76M-98-72V-50M98 72H76M98 72V50M98-72H76M98-72V-50M-98 72H-76M-98 72V50" stroke="currentColor" stroke-opacity=".4" stroke-width="2"/>
      <path d="M-79 86H83M-79 81V91M83 81V91M2 83V89" stroke="currentColor" stroke-opacity=".45" stroke-width="1.5"/>
      <g class="scan"><rect x="-96" y="-1" width="192" height="2" fill="currentColor" fill-opacity=".8"/><rect x="-96" y="-15" width="192" height="14" fill="url(#scanfade)"/></g>
      <circle r="4" fill="currentColor"/>'''
VISION_CSS = '''
    .scan { animation: scan 4.5s ease-in-out infinite alternate; }
    @keyframes scan { from { transform: translateY(-62px); } to { transform: translateY(62px); } }'''

LEARNING = '''      <path d="M-66-40L-15-58 55-35 72 28 5 59-68 31ZM-66-40L5 59 55-35-68 31-15-58 72 28-66-40" stroke="currentColor" stroke-opacity=".25" stroke-width="2"/>
      <g fill="currentColor"><circle cx="-15" cy="-58" r="7"/><circle cx="72" cy="28" r="7"/><circle cx="-68" cy="31" r="7"/></g>
      <g stroke="currentColor" stroke-width="2" fill="currentColor"><circle class="label" cx="-66" cy="-40" r="8"/><circle class="label l2" cx="55" cy="-35" r="8"/><circle class="label l3" cx="5" cy="59" r="8"/></g>
      <circle class="ring" r="22" fill="currentColor" fill-opacity=".08" stroke="currentColor" stroke-dasharray="3 5"/>
      <circle r="5" fill="currentColor"/>'''
LEARNING_CSS = '''
    .label { fill-opacity: 0; animation: label 6s ease-in-out infinite; }
    .l2 { animation-delay: 2s; } .l3 { animation-delay: 4s; }
    @keyframes label { 15%, 35% { fill-opacity: .9; } 55% { fill-opacity: 0; } }
    .ring { transform-box: fill-box; transform-origin: center; animation: ring 24s linear infinite; }
    @keyframes ring { to { transform: rotate(360deg); } }'''

SYSTEMS = '''      <path class="flow" d="M-49 0H-28M28 0H49" stroke="currentColor" stroke-width="2"/>
      <path class="flow" d="M75 30C75 78-75 78-75 36" stroke="currentColor" stroke-opacity=".45" stroke-width="1.5"/>
      <path d="M-81 44L-75 34-69 44" stroke="currentColor" stroke-opacity=".6" stroke-width="1.5" stroke-linejoin="round"/>
      <g fill="PANEL" stroke="currentColor" stroke-width="2">
        <path d="M-99-26V26A24 8 0 0 0-51 26V-26"/>
        <ellipse cx="-75" cy="-26" rx="24" ry="8"/>
        <rect x="-26" y="-26" width="52" height="52" rx="10"/>
        <circle cx="75" r="24"/>
      </g>
      <path d="M-99 0A24 8 0 0 0-51 0M-12-11V11M0-15V15M12-11V11M65 1L72 8 86-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'''


def tools(t):
    chips = []
    for i, (name, color, d) in enumerate(TOOLS):
        x = 28 + i * 232
        chips.append(f'''    <g transform="translate({x} 22)">
      <rect width="216" height="76" rx="14" fill="{t['card_bg'][0]}" stroke="{t['border']}" stroke-opacity=".25"/>
      <path class="logo" d="{d}" fill="{color}" transform="translate(24 22) scale(1.33)"/>
      <path class="logo-large" d="{d}" fill="{color}" transform="translate(78 8) scale(2.5)"/>
      <text class="label" x="72" y="47" fill="{t['text']}" font-size="25" font-weight="600">{name}</text>
    </g>''')
    chips = "\n".join(chips)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="120" viewBox="0 0 1200 120" role="img" aria-labelledby="title">
  <title id="title">Tools: {", ".join(n for n, _, _ in TOOLS)}</title>
  <style>
    .logo-large {{ display: none; }}
    @media (max-width: 600px) {{
      .logo, .label {{ display: none; }}
      .logo-large {{ display: inline; }}
    }}
  </style>
  <g font-family="{FONT}">
{chips}
  </g>
</svg>
'''


def build():
    for suffix, t in (("", DARK), ("-light", LIGHT)):
        files = {
            "profile-banner": hero(t),
            "vision-banner": focus(t, "01", "cyan", "Medical &amp; scientific vision", "Segmentation · Structure · Measurement", VISION, VISION_CSS),
            "learning-banner": focus(t, "02", "purple", "Learning with limited labels", "Semi-supervision · Uncertainty · Calibration", LEARNING, LEARNING_CSS),
            "systems-banner": focus(t, "03", "orange", "ML systems engineering", "Data pipelines · Reproducibility · Inference", SYSTEMS),
            "tools-banner": tools(t),
        }
        for name, svg in files.items():
            (ASSETS / f"{name}{suffix}.svg").write_text(svg)


if __name__ == "__main__":
    build()
