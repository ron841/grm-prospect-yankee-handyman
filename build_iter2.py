"""Apply iteration-2 changes to build/index.html in place.

Workstream A:
- Palette swap (more saturated brown/sepia per iter-2 Home.html :root)
- Hero swap to pergola (audit/fb-photos/fb-01-cover-photo-pergola.jpg)
- Pool section → Finish Carpentry section (rename + re-author)
- Add pending-walkthrough HTML comments for new README items #9 and #10
- Regenerate OG image from new pergola hero
- Footer YH symbol: NOT applied (held for walkthrough)
"""

import os, re, shutil, json
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.expanduser('~/grm-sites-prospects/yankee-handyman')
BUILD = os.path.join(ROOT, 'build')
PERGOLA_SRC = os.path.join(ROOT, 'audit/fb-photos/fb-01-cover-photo-pergola.jpg')

# ---- 1) Move pergola into build/images and resize for web (max 1920px) ----
hero_dst = os.path.join(BUILD, 'images', 'hero-pergola.jpg')
img = Image.open(PERGOLA_SRC).convert('RGB')
print(f"Pergola source: {img.size}, {os.path.getsize(PERGOLA_SRC):,}B")
# Source is 960x720 — already <1920, no upscale needed; just re-encode at q=85
img.save(hero_dst, 'JPEG', quality=85, optimize=True, progressive=True)
print(f"Hero saved: {hero_dst}, {os.path.getsize(hero_dst):,}B, {img.size}")

# ---- 2) Read build/index.html ----
INDEX = os.path.join(BUILD, 'index.html')
with open(INDEX) as f:
    html = f.read()

# ---- 3) Palette swap (iter-1 → iter-2 sepia/brown) ----
PALETTE_SWAPS = [
    ('--c-ink: #1a1a1a;',                   '--c-ink: #1f1810;'),
    ('--c-ink-soft: #4a4a4a;',              '--c-ink-soft: #5a4a3a;'),
    ('--c-paper: #fafaf7;',                 '--c-paper: #faf6ee;'),
    ('--c-paper-2: #f0ede4;',               '--c-paper-2: #ede4d2;'),
    ('--c-line: #e0dccf;',                  '--c-line: #d8ccb4;'),
    ('--c-brand: #5f463b;',                 '--c-brand: #6b4423;'),
    ('--c-brand-soft: rgba(95,70,59,0.12);','--c-brand-soft: rgba(107,68,35,0.12);'),
    ('--c-accent: #9c6955;',                '--c-accent: #a8784a;'),
    # Hover-state shifts (computed for new palette)
    ('background: #b07a64;',                'background: #c08e5e;'),  # accent hover (lighter tan)
    ('background: #4a3528;',                'background: #4a2f15;'),  # brand hover (darker brown)
    # theme-color meta
    ('content="#5f463b">',                  'content="#6b4423">'),
]
for old, new in PALETTE_SWAPS:
    if old in html:
        html = html.replace(old, new)
        print(f"  swapped: {old} → {new}")
    else:
        print(f"  ! not found (ok if already-swapped): {old}")

# ---- 4) Hero photo + alt: pergola ----
old_hero_bg = "url('images/01-gbp-owner-the-yankee-handyman-llc.jpg')"
new_hero_bg = "url('images/hero-pergola.jpg')"
html = html.replace(old_hero_bg, new_hero_bg)
print(f"  hero background: → hero-pergola.jpg")

# Re-center the focal point — pergola subject is roughly center-frame, headline is in left-quadrant overlay
html = html.replace(
    "background-position: center, center, 70% center;",
    "background-position: center, center, 60% 65%;"
)

# ---- 5) Finish Carpentry section: rename headline + re-author body ----
# Old (pool-deck-led):
old_pool_heading = '<h2 class="section-headline">Pool decks built like furniture.</h2>'
new_finish_heading = '<h2 class="section-headline">Finish carpentry, not just framing.</h2>'
html = html.replace(old_pool_heading, new_finish_heading)
print("  section headline: → Finish carpentry, not just framing.")

old_pool_body = '<p class="pool-body">Most pool decks get framed, screwed down, and called done. Anthony sanded every edge. He cut the curve around the pool to match the coping. Diane Bennett got three other quotes before she called him; his came in fair and the work came in furniture-grade.</p>'
new_finish_body = '<p class="pool-body">Most handymen frame it, screw it down, call it done. Anthony sands the edges. He cuts curves to match the coping. He notches around what\'s already there instead of trimming around it. Diane Bennett\'s pool deck got three other quotes before she called him; the work is what made the difference. Cole Spires hired him for one porch and brought him back for the bedroom tile.</p>'
html = html.replace(old_pool_body, new_finish_body)
print("  section body: re-authored")

# Caption stays — it's still Diane Bennett's pool deck (the photo on screen)
# but the section is now finish-carpentry-general

# ---- 6) Pool service-card softened (no more "Sanded edges. Curve around the pool." spec claim) ----
old_pool_card = '<p class="service-blurb">Built and finished, with the carpentry-grade detail most pool guys skip. Sanded edges. Curve around the pool.</p>'
new_pool_card = '<p class="service-blurb">Built and finished, with the carpentry-grade detail most pool guys skip. Ask for the gallery.</p>'
html = html.replace(old_pool_card, new_pool_card)
print("  pool service card: softened (per content-inventory iter-2)")

# ---- 7) Open-decisions HTML comments for new items #9 and #10 ----
# #9 — brand color (anywhere --c-brand is rendered visually; safest spot: just before <style> closes
#       so it's findable but doesn't affect rendering)
od9 = '<!-- pending-walkthrough #9: brand color is sepia/brown per k-means logo extraction. Confirm with Anthony whether intentional brand DNA or JPEG-degraded artifact. If degraded, request original logo file. -->'
od10 = '<!-- pending-walkthrough #10: pool section re-authored as Finish Carpentry. No finished pool-deck photo public; section now leads with general finish-carpentry framing, Diane Bennett quote demoted to evidence row. Confirm Anthony is comfortable with reframe; restore pool-deck-led version if he surfaces a finished pool deck photo. -->'

# Insert #9 just before <style> opening (in head)
html = html.replace('<style>', f'{od9}\n<style>', 1)
# Insert #10 inside the finish-carpentry section just before its eyebrow
html = html.replace(
    '<div class="section-eyebrow">Finish Carpentry</div>',
    f'{od10}\n          <div class="section-eyebrow">Finish Carpentry</div>',
    1
)
print("  added pending-walkthrough HTML comments for README items #9 and #10")

# ---- 8) Regenerate OG image from new pergola hero ----
img_for_og = Image.open(hero_dst).convert('RGB')
target_w, target_h = 1200, 630
ratio = max(target_w / img_for_og.width, target_h / img_for_og.height)
new_w, new_h = int(img_for_og.width * ratio), int(img_for_og.height * ratio)
img_for_og = img_for_og.resize((new_w, new_h), Image.LANCZOS)
left = (new_w - target_w) // 2
top = (new_h - target_h) // 2
img_for_og = img_for_og.crop((left, top, left + target_w, top + target_h))

# Two-axis dark gradient overlay (top→bottom + left→right), then text
overlay = Image.new('RGBA', (target_w, target_h), (0,0,0,0))
od = ImageDraw.Draw(overlay)
for y in range(target_h):
    a_v = int(60 + (160 - 60) * (y / target_h))
    od.line([(0, y), (target_w, y)], fill=(0, 0, 0, a_v))
for x in range(target_w):
    a_h = int(150 - (150 - 30) * (x / target_w))
    for y in range(target_h):
        r, g, b, a = overlay.getpixel((x, y))
        a = min(255, a + a_h // 3)
        overlay.putpixel((x, y), (0, 0, 0, a))

og_img = Image.alpha_composite(img_for_og.convert('RGBA'), overlay)
draw = ImageDraw.Draw(og_img)
font_paths = ['/Library/Fonts/Georgia.ttf', '/System/Library/Fonts/Supplemental/Georgia.ttf']
font_lg = font_sm = None
for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_lg = ImageFont.truetype(fp, 48)
            font_sm = ImageFont.truetype(fp, 24)
            break
        except Exception: pass
if font_lg is None:
    font_lg = ImageFont.load_default(); font_sm = ImageFont.load_default()
draw.text((60, 220), "Creating Beautiful Spaces", fill=(255,255,255,255), font=font_lg)
draw.text((60, 280), "and Smiling Faces.", fill=(255,255,255,255), font=font_lg)
draw.text((60, 360), "Yankee Handyman · Ocala", fill=(237,228,210,235), font=font_sm)
draw.text((60, 400), "(239) 867-8447", fill=(237,228,210,235), font=font_sm)
og_img.convert('RGB').save(os.path.join(BUILD, 'og-image.jpg'), 'JPEG', quality=85, optimize=True)
print(f"  og-image.jpg regenerated from pergola hero")

# ---- 9) Update README open decisions count comment if present ----
# (If we'd added one. Skipping — the comments above carry the trail.)

# ---- 10) Write index.html ----
with open(INDEX, 'w') as f:
    f.write(html)
print(f"\nWritten {INDEX}  ({len(html):,} bytes)")
