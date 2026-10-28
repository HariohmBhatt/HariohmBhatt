"""Build the profile banners in dark and light variants.

Run from the repository root: python3 scripts/build_banners.py
"""
import base64
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

# Colours follow GitHub's own dark and light palettes so the banners sit naturally on the page.
DARK = dict(bg="#161b22", border="#30363d", text="#e6edf3", muted="#9198a1", accent="#3fb9a9")
LIGHT = dict(bg="#f6f8fa", border="#d0d7de", text="#1f2328", muted="#59636e", accent="#1a7f74")

FOCUS = [
    ("Medical &amp; scientific vision", "Segmentation · Structure · Measurement"),
    ("Learning with limited labels", "Semi-supervision · Uncertainty · Calibration"),
    ("ML systems engineering", "Data pipelines · Reproducibility · Inference"),
]


def header(t):
    photo = base64.b64encode((ASSETS / "portrait.jpg").read_bytes()).decode()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-labelledby="title description">
  <title id="title">Hariohm Bhatt</title>
  <desc id="description">Portrait of Hariohm Bhatt. Computer vision and scientific machine learning.</desc>
  <style>
    @media (max-width: 600px) {{
      .name {{ font-size: 84px; }}
      .tagline {{ font-size: 44px; }}
    }}
  </style>
  <defs><clipPath id="portrait"><circle cx="170" cy="150" r="96"/></clipPath></defs>
  <rect x=".5" y=".5" width="1199" height="299" rx="12" fill="{t['bg']}" stroke="{t['border']}"/>
  <image clip-path="url(#portrait)" x="74" y="54" width="192" height="192" xlink:href="data:image/jpeg;base64,{photo}"/>
  <circle cx="170" cy="150" r="96" fill="none" stroke="{t['border']}" stroke-width="2"/>
  <g font-family="{FONT}">
    <text class="name" x="318" y="160" fill="{t['text']}" font-size="72" font-weight="600" letter-spacing="-2">Hariohm Bhatt</text>
    <text class="tagline" x="320" y="214" fill="{t['muted']}" font-size="30">Computer vision · <tspan fill="{t['accent']}">Scientific ML</tspan></text>
  </g>
</svg>
'''


def focus(t):
    rows = []
    for i, (title, desc) in enumerate(FOCUS):
        y = 40 + i * 100
        if i:
            rows.append(f'  <path d="M48 {y}H1152" stroke="{t["border"]}"/>')
        rows.append(f'''  <circle class="dot" cx="58" cy="{y + 34}" r="5" fill="{t['accent']}"/>
  <text class="title" x="84" y="{y + 46}" fill="{t['text']}" font-size="34" font-weight="600">{title}</text>
  <text class="desc" x="84" y="{y + 80}" fill="{t['muted']}" font-size="24">{desc}</text>''')
    rows = "\n".join(rows)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="380" viewBox="0 0 1200 380" role="img" aria-labelledby="title description">
  <title id="title">Focus areas</title>
  <desc id="description">Medical and scientific vision: segmentation, structure, measurement. Learning with limited labels: semi-supervision, uncertainty, calibration. ML systems engineering: data pipelines, reproducibility, inference.</desc>
  <style>
    @media (max-width: 600px) {{
      .title {{ font-size: 56px; transform: translateY(20px); }}
      .dot {{ transform: translateY(16px); }}
      .desc {{ display: none; }}
    }}
  </style>
  <rect x=".5" y=".5" width="1199" height="379" rx="12" fill="{t['bg']}" stroke="{t['border']}"/>
  <g font-family="{FONT}">
{rows}
  </g>
</svg>
'''


def build():
    for suffix, t in (("", DARK), ("-light", LIGHT)):
        (ASSETS / f"profile-banner{suffix}.svg").write_text(header(t))
        (ASSETS / f"focus-banner{suffix}.svg").write_text(focus(t))


if __name__ == "__main__":
    build()
