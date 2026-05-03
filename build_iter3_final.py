"""Iteration 3 final edits — three targeted changes:
1. Footer YH symbol — ship the mockup (cream box, brown YH) to BOTH pages
2. Remove 1-star section from /reviews entirely (section + JSON-LD entry + subhead/meta updates)
3. Footer tagline copy fix: drop "and one other guy" (their → his) on BOTH pages
"""

import os, re, json

ROOT = os.path.expanduser('~/grm-sites-prospects/yankee-handyman')
BUILD = os.path.join(ROOT, 'build')
INDEX = os.path.join(BUILD, 'index.html')
REVIEWS = os.path.join(BUILD, 'reviews.html')

# ---- Footer YH symbol markup (cream box, brown YH — reversed from nav) ----
FOOTER_BRAND_OLD = '<div class="footer-brand">Yankee Handyman</div>'
FOOTER_BRAND_NEW = '''<div class="footer-brand-row" style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
          <div class="footer-yh" style="width:32px;height:32px;background:#ede4d2;color:#6b4423;display:flex;align-items:center;justify-content:center;font-family:'Merriweather',Georgia,serif;font-weight:700;font-size:16px;border-radius:4px;flex-shrink:0;">YH</div>
          <div class="footer-brand" style="margin-bottom:0;">Yankee Handyman</div>
        </div>'''
# Note: 32px square matches the nav YH (visual symmetry per Ron's spec). Cream #ede4d2 = --c-paper-2; brown #6b4423 = --c-brand. Reversed from nav (brown box, white YH).

# ---- Footer tagline old/new (drop "and one other guy"; their → his) ----
TAGLINE_OLD = 'Anthony Porett and one other guy, working their way through Ocala one job at a time.'
TAGLINE_NEW = 'Anthony Porett, working his way through Ocala one job at a time.'

# ===== Edit homepage =====
with open(INDEX) as f:
    home = f.read()

if FOOTER_BRAND_OLD in home:
    home = home.replace(FOOTER_BRAND_OLD, FOOTER_BRAND_NEW, 1)
    print("[home] footer YH symbol added")
else:
    print("[home] ! footer-brand anchor not found")

if TAGLINE_OLD in home:
    home = home.replace(TAGLINE_OLD, TAGLINE_NEW, 1)
    print("[home] footer tagline cleaned")
else:
    print("[home] ! tagline anchor not found")

with open(INDEX, 'w') as f:
    f.write(home)

# ===== Edit /reviews =====
with open(REVIEWS) as f:
    rev = f.read()

# 1. Footer YH symbol
if FOOTER_BRAND_OLD in rev:
    rev = rev.replace(FOOTER_BRAND_OLD, FOOTER_BRAND_NEW, 1)
    print("[reviews] footer YH symbol added")

# 2. Footer tagline
if TAGLINE_OLD in rev:
    rev = rev.replace(TAGLINE_OLD, TAGLINE_NEW, 1)
    print("[reviews] footer tagline cleaned")

# 3a. Remove 1-star <section> entirely
# Section pattern: <section class="outlier-section container" ... >...</section>
outlier_section_pattern = re.compile(
    r'\s*<section class="outlier-section container"[^>]*>.*?</section>\s*',
    re.DOTALL
)
m = outlier_section_pattern.search(rev)
if m:
    rev = rev[:m.start()] + '\n\n  ' + rev[m.end():]
    print("[reviews] 1-star <section> removed")
else:
    print("[reviews] ! outlier <section> pattern not found")

# 3b. Update page subhead — remove "One 1-star is in here too" + recount to 43
old_subhead = '<p class="page-subhead">Forty-four reviews on Google. Anthony has replied to forty-three of them. One 1-star is in here too.</p>'
new_subhead = '<p class="page-subhead">Forty-three of Anthony\'s fifty Google reviews. He has replied to nearly every one.</p>'
if old_subhead in rev:
    rev = rev.replace(old_subhead, new_subhead, 1)
    print("[reviews] page subhead updated (44 → 43, removed 1-star reference)")
else:
    print("[reviews] ! page subhead not found")

# 3c. Update meta.description (44 → 43)
old_meta = '<meta name="description" content="Forty-four of Anthony Porett\'s fifty Google reviews. Plumbing, electrical, carpentry, tile, paint. Marion County, 4.9 stars.">'
new_meta = '<meta name="description" content="Forty-three of Anthony Porett\'s fifty Google reviews. Plumbing, electrical, carpentry, tile, paint. Marion County, 4.9 stars.">'
if old_meta in rev:
    rev = rev.replace(old_meta, new_meta, 1)
    print("[reviews] meta.description updated")
else:
    print("[reviews] ! meta.description anchor not found")

# 3d. Update meta.og_description (drop the "One 1-star included" sentence)
old_og = '<meta property="og:description" content="Forty-four customer reviews. Forty-three replies from Anthony. One 1-star included.">'
new_og = '<meta property="og:description" content="Forty-three five-star Google reviews. Anthony has replied to nearly every one.">'
if old_og in rev:
    rev = rev.replace(old_og, new_og, 1)
    print("[reviews] og:description updated")

old_tw = '<meta name="twitter:description" content="Forty-four customer reviews. Forty-three replies from Anthony.">'
new_tw = '<meta name="twitter:description" content="Forty-three five-star Google reviews. Anthony has replied to nearly every one.">'
if old_tw in rev:
    rev = rev.replace(old_tw, new_tw, 1)
    print("[reviews] twitter:description updated")

# 3e. Remove DM _ from JSON-LD Review array
# Find the JSON-LD block, parse it, drop the DM _ entry, re-serialize
ld_pattern = re.compile(r'<script type="application/ld\+json">\s*(\[.*?\])\s*</script>', re.DOTALL)
m = ld_pattern.search(rev)
if m:
    arr = json.loads(m.group(1))
    before = len(arr)
    arr = [e for e in arr if e.get('author', {}).get('name') != 'DM _']
    after = len(arr)
    new_ld = '<script type="application/ld+json">\n' + json.dumps(arr, indent=2, ensure_ascii=False) + '\n</script>'
    rev = rev[:m.start()] + new_ld + rev[m.end():]
    print(f"[reviews] JSON-LD: {before} Review entries → {after} (DM _ dropped)")
else:
    print("[reviews] ! JSON-LD block not found")

with open(REVIEWS, 'w') as f:
    f.write(rev)

# ===== Sanity recount =====
remaining_review = rev.count('"@type": "Review"')
print(f"\nFinal /reviews JSON-LD Review entry count: {remaining_review}")
print(f"Final footer YH check (homepage): {'YH</div>' in home and 'background:#ede4d2' in home}")
print(f"Final footer YH check (reviews):  {'YH</div>' in rev and 'background:#ede4d2' in rev}")
print(f"Final tagline check (homepage):   {TAGLINE_NEW in home}")
print(f"Final tagline check (reviews):    {TAGLINE_NEW in rev}")
_oc = 'class="outlier-section"'
print(f"Outlier section gone (reviews):   {_oc not in rev}")
