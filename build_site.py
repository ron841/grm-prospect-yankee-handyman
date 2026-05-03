"""Build the Yankee Handyman preview site into ./build/.

- Copies images from ../images/ → build/images/ (rescaled for web)
- Generates favicon and OG image
- Renders build/index.html from Home.html with:
  · Extracted brown palette (replaces provisional navy/red)
  · Real <img> tags swapped in for gradient placeholders
  · Static Forms backend (replaces Netlify Forms)
  · LocalBusiness + AggregateRating JSON-LD
  · Open Graph + Twitter Card meta tags
  · Favicon link
  · pending-walkthrough HTML comments at every $125 fee reference
  · comp-note overlay removed
- Outputs vercel.json for static-site deploy
"""

import os, re, shutil, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.expanduser('~/grm-sites-prospects/yankee-handyman')
BUILD = os.path.join(ROOT, 'build')
SRC_HTML = os.path.join(ROOT, 'design-pack/yankee-handyman/Home.html')
SRC_IMAGES = os.path.join(ROOT, 'images')
SRC_LOGO = os.path.join(ROOT, 'logo/logo.jpg')

os.makedirs(os.path.join(BUILD, 'images'), exist_ok=True)

# ---- Extracted palette (k-means on logo/logo.jpg) ----
BRAND       = '#5f463b'   # warm dark brown — main brand
BRAND_SOFT  = 'rgba(95,70,59,0.12)'
ACCENT      = '#9c6955'   # terracotta — accent, CTAs
INK         = '#1a1a1a'
INK_SOFT    = '#4a4a4a'
PAPER       = '#fafaf7'
PAPER_2     = '#f0ede4'
LINE        = '#e0dccf'

# ---- Web-optimize source images ----
def web_resize(src, dst, max_w=1920, q=82):
    img = Image.open(src).convert('RGB')
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(img.height * ratio)), Image.LANCZOS)
    img.save(dst, 'JPEG', quality=q, optimize=True, progressive=True)
    return os.path.getsize(dst)

photos = sorted(f for f in os.listdir(SRC_IMAGES) if f.endswith('.jpg'))
print(f"Web-optimizing {len(photos)} photos...")
for f in photos:
    src = os.path.join(SRC_IMAGES, f)
    dst = os.path.join(BUILD, 'images', f)
    sz_before = os.path.getsize(src)
    sz_after = web_resize(src, dst, max_w=1920, q=82)
    print(f"  {f}  {sz_before:>9,}B → {sz_after:>9,}B")

# Copy logo for in-page use
shutil.copy2(SRC_LOGO, os.path.join(BUILD, 'logo.jpg'))

# ---- Favicon (64×64 PNG cropped from center of logo) ----
fav_src = Image.open(SRC_LOGO).convert('RGB')
side = min(fav_src.size)
left = (fav_src.width - side) // 2
top = (fav_src.height - side) // 2
fav = fav_src.crop((left, top, left + side, top + side)).resize((64, 64), Image.LANCZOS)
fav.save(os.path.join(BUILD, 'favicon.png'), 'PNG')
# Also a 32×32 ICO-equivalent
fav.resize((32, 32), Image.LANCZOS).save(os.path.join(BUILD, 'favicon-32.png'), 'PNG')
print(f"\nfavicon.png + favicon-32.png written")

# ---- OG image (1200×630 from hero photo with gradient overlay + tagline) ----
hero_photo = os.path.join(BUILD, 'images', '01-gbp-owner-the-yankee-handyman-llc.jpg')
hero_img = Image.open(hero_photo).convert('RGB')
# Crop/cover to 1200×630
target_w, target_h = 1200, 630
ratio = max(target_w / hero_img.width, target_h / hero_img.height)
new_w, new_h = int(hero_img.width * ratio), int(hero_img.height * ratio)
hero_img = hero_img.resize((new_w, new_h), Image.LANCZOS)
left = (new_w - target_w) // 2
top = (new_h - target_h) // 2
hero_img = hero_img.crop((left, top, left + target_w, top + target_h))

# Two-axis gradient overlay (top→bottom + left→right black gradients)
overlay = Image.new('RGBA', (target_w, target_h), (0,0,0,0))
od = ImageDraw.Draw(overlay)
for y in range(target_h):
    a_v = int(80 + (180 - 80) * (y / target_h))  # 80 → 180 alpha top→bottom
    od.line([(0, y), (target_w, y)], fill=(0, 0, 0, a_v))
# left→right horizontal gradient (140 → 25 alpha) — biases dark to left
for x in range(target_w):
    a_h = int(140 - (140 - 25) * (x / target_w))
    for y in range(target_h):
        r, g, b, a = overlay.getpixel((x, y))
        a = min(255, a + a_h // 3)  # additive but tempered
        overlay.putpixel((x, y), (0, 0, 0, a))

hero_with_overlay = Image.alpha_composite(hero_img.convert('RGBA'), overlay)

# Add tagline text overlay
draw = ImageDraw.Draw(hero_with_overlay)
# Try to load a serif system font; fall back to default
font_paths = [
    '/Library/Fonts/Georgia.ttf',
    '/System/Library/Fonts/Supplemental/Georgia.ttf',
    '/System/Library/Fonts/Times.ttc',
    '/System/Library/Fonts/Helvetica.ttc',
]
font_lg = font_sm = None
for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_lg = ImageFont.truetype(fp, 48)
            font_sm = ImageFont.truetype(fp, 24)
            break
        except Exception: pass
if font_lg is None:
    font_lg = ImageFont.load_default()
    font_sm = ImageFont.load_default()
# Tagline (the synthesis-committed line)
draw.text((60, 220), "Creating Beautiful Spaces", fill=(255,255,255,255), font=font_lg)
draw.text((60, 280), "and Smiling Faces.", fill=(255,255,255,255), font=font_lg)
draw.text((60, 360), "Yankee Handyman · Ocala", fill=(235,222,205,230), font=font_sm)
draw.text((60, 400), "(239) 867-8447", fill=(235,222,205,230), font=font_sm)

og_path = os.path.join(BUILD, 'og-image.jpg')
hero_with_overlay.convert('RGB').save(og_path, 'JPEG', quality=85, optimize=True)
print(f"og-image.jpg written ({os.path.getsize(og_path):,}B)")

# ---- Read source HTML ----
with open(SRC_HTML) as f:
    html = f.read()

# ---- Color palette swap (provisional → extracted) ----
html = html.replace('--c-brand: #1a3a5c;', f'--c-brand: {BRAND};')
html = html.replace('--c-brand-soft: rgba(26,58,92,0.12);', f'--c-brand-soft: {BRAND_SOFT};')
html = html.replace('--c-accent: #b8392a;', f'--c-accent: {ACCENT};')
# Hover-darken values for the new palette
html = html.replace('background: #cc4030;', 'background: #b07a64;')   # accent hover (lighter terracotta)
html = html.replace('background: #122d49;', 'background: #4a3528;')   # brand hover (darker brown)

# ---- Replace gradient-placeholder hero with real <picture> background ----
hero_placeholder_css = """.hero::before {
  /* Photo placeholder — dotted pattern suggesting unselected photo */
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    radial-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
    linear-gradient(135deg, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.3) 50%, rgba(0,0,0,0.1) 100%);
  background-size: 24px 24px, cover;
  background-position: 0 0, center;
}"""
hero_real_css = """.hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(180deg, rgba(0,0,0,0.40) 0%, rgba(0,0,0,0.65) 100%),
    linear-gradient(90deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.10) 65%),
    url('images/01-gbp-owner-the-yankee-handyman-llc.jpg');
  background-size: cover, cover, cover;
  background-position: center, center, 70% center;
}"""
html = html.replace(hero_placeholder_css, hero_real_css)
# Strip the [hero photo pending image review] flag overlay
html = re.sub(r'\.hero::after \{[^}]*"\[ hero photo pending image review \]"[^}]*\}', '', html, count=0, flags=re.DOTALL)
# Above regex won't easily catch it because of multiline rules; simpler — just remove the rule between two known anchors
html = re.sub(
    r'\.hero::after\s*\{[^}]*\}',
    '',
    html, count=1, flags=re.DOTALL
)

# ---- Pool image: real <img> background ----
pool_placeholder_css = """.pool-image {
  aspect-ratio: 4 / 3;
  border-radius: var(--r-lg);
  background:
    linear-gradient(135deg, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0.1) 100%),
    radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px),
    linear-gradient(180deg, #4a6e8c 0%, #2a4d6e 100%);
  background-size: cover, 24px 24px, cover;
  position: relative;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding: var(--s-5);
  color: rgba(255,255,255,0.6);
  font-family: var(--font-eyebrow);
  font-size: 11px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}"""
pool_real_css = """.pool-image {
  aspect-ratio: 4 / 3;
  border-radius: var(--r-lg);
  background-image: url('images/09-gbp-customer-diane-bennett.jpg');
  background-size: cover;
  background-position: center;
  position: relative;
}"""
html = html.replace(pool_placeholder_css, pool_real_css)
# Strip the [pool deck — Diane Bennett] flag overlay
html = re.sub(
    r"\.pool-image::after\s*\{[^}]*\}",
    "",
    html, count=1, flags=re.DOTALL
)

# ---- Photo-grid tiles: replace placeholder gradients with real images ----
photo_grid_css = """.photo-tile {
  aspect-ratio: 1;
  border-radius: var(--r-md);
  overflow: hidden;
  position: relative;
  background:
    radial-gradient(rgba(255,255,255,0.06) 1px, transparent 1px),
    linear-gradient(180deg, #6e7a8a 0%, #3d4654 100%);
  background-size: 16px 16px, cover;
  display: flex;
  align-items: flex-end;
}
.photo-tile.alt-1 { background: linear-gradient(180deg, #8c6f4e 0%, #5e4530 100%); }
.photo-tile.alt-2 { background: linear-gradient(180deg, #4f6650 0%, #2f4032 100%); }
.photo-tile.alt-3 { background: linear-gradient(180deg, #6b5b3e 0%, #423520 100%); }
.photo-tile.alt-4 { background: linear-gradient(180deg, #5a6b7a 0%, #354150 100%); }
.photo-tile.alt-5 { background: linear-gradient(180deg, #7a5a4a 0%, #4a3528 100%); }"""
photo_grid_real_css = """.photo-tile {
  aspect-ratio: 1;
  border-radius: var(--r-md);
  overflow: hidden;
  position: relative;
  background: var(--c-paper-2);
  display: flex;
  align-items: flex-end;
}
.photo-tile img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.photo-tile .photo-caption { position: relative; z-index: 1; }"""
html = html.replace(photo_grid_css, photo_grid_real_css)

# Replace photo-grid markup with real <img> tags
photo_grid_markup_old = """      <div class="photo-grid">
        <div class="photo-tile">
          <div class="photo-caption">Pool deck. Diane Bennett, 2026.</div>
        </div>
        <div class="photo-tile alt-1">
          <div class="photo-caption">Porch enclosure. Cole Spires, 2025.</div>
        </div>
        <div class="photo-tile alt-2">
          <div class="photo-caption">Interior tile</div>
        </div>
        <div class="photo-tile alt-3">
          <div class="photo-caption">Chandelier circuit</div>
        </div>
        <div class="photo-tile alt-4">
          <div class="photo-caption">Framing detail</div>
        </div>
        <div class="photo-tile alt-5">
          <div class="photo-caption">Interior paint</div>
        </div>
      </div>"""
# Use the customer photos first (per Ron's brief), then owner photos in filename order
photo_grid_markup_new = """      <!-- Photo grid: customer-attributed photos first, then owner photos. Subjects/captions pending walkthrough — re-author per actual photo content. -->
      <div class="photo-grid">
        <div class="photo-tile">
          <img src="images/09-gbp-customer-diane-bennett.jpg" loading="lazy" alt="Pool deck Anthony built for Diane Bennett in Ocala. Sanded edges and a curved cut around the pool.">
          <div class="photo-caption">Pool deck. Diane Bennett, 2026.</div>
        </div>
        <div class="photo-tile">
          <img src="images/10-gbp-customer-cole-spires.jpg" loading="lazy" alt="Porch enclosure and re-tile work Anthony finished for Cole Spires in Ocala, 2025.">
          <div class="photo-caption">Porch enclosure and re-tile. Cole Spires, 2025.</div>
        </div>
        <div class="photo-tile">
          <img src="images/02-gbp-owner-the-yankee-handyman-llc.jpg" loading="lazy" alt="Completed work in Ocala by Anthony Porett.">
          <div class="photo-caption">Completed work, 2025.</div>
        </div>
        <div class="photo-tile">
          <img src="images/03-gbp-owner-the-yankee-handyman-llc.jpg" loading="lazy" alt="Completed work in Ocala by Anthony Porett.">
          <div class="photo-caption">Completed work, 2025.</div>
        </div>
        <div class="photo-tile">
          <img src="images/04-gbp-owner-the-yankee-handyman-llc.jpg" loading="lazy" alt="Completed work in Ocala by Anthony Porett.">
          <div class="photo-caption">Completed work, 2025.</div>
        </div>
        <div class="photo-tile">
          <img src="images/05-gbp-owner-the-yankee-handyman-llc.jpg" loading="lazy" alt="Completed work in Ocala by Anthony Porett.">
          <div class="photo-caption">Completed work, 2025.</div>
        </div>
      </div>"""
html = html.replace(photo_grid_markup_old, photo_grid_markup_new)

# ---- Add pending-walkthrough comments at every $125 fee reference ----
walkthrough_comment = "<!-- pending-walkthrough: $125 fee — confirm current with Anthony before prod -->"

html = html.replace(
    '<span>$125 flat service-call fee</span>',
    f'{walkthrough_comment}\n          <span>$125 flat service-call fee</span>'
)
html = html.replace(
    '<p class="service-quote">"I had contacted a few plumbers who quoted me $350–$500. I only paid $125, his standard service fee."</p>',
    f'{walkthrough_comment}\n            <p class="service-quote">"I had contacted a few plumbers who quoted me $350–$500. I only paid $125, his standard service fee."</p>'
)
html = html.replace(
    '<p class="faq-a">$125 flat. That covers the visit and most small jobs in full. Bigger jobs get an estimate before any work starts.</p>',
    f'{walkthrough_comment}\n            <p class="faq-a">$125 flat. That covers the visit and most small jobs in full. Bigger jobs get an estimate before any work starts.</p>'
)

# ---- Replace Netlify form with Static Forms ----
# Static Forms takes POST to https://api.staticforms.xyz/submit with hidden accessKey field
# and routes the submission to the email associated with the access key.
old_form_open = '<form class="contact-form" name="contact" method="POST" data-netlify="true">'
new_form_open = '''<form class="contact-form" action="https://api.staticforms.xyz/submit" method="POST" id="contact-form">
          <input type="hidden" name="accessKey" value="sf_e0e200934d4f36c17a10d00c">
          <input type="hidden" name="subject" value="Yankee Handyman — new contact form submission">
          <input type="hidden" name="redirectTo" value="https://yankeehandyman.example/?submitted=1">
          <input type="text" name="honeypot" style="display:none" tabindex="-1" autocomplete="off">'''
html = html.replace(old_form_open, new_form_open)

# ---- Wire form to inline submit handler so we keep success/error UX ----
# Find existing submit button, replace with inline-handler version
html = html.replace(
    '<button class="form-submit" type="submit">Send to Anthony</button>',
    '''<button class="form-submit" type="submit">Send to Anthony</button>
          <div class="form-status" id="form-status" hidden></div>'''
)

# Inline JS for form handling + nav scroll behavior
inline_js = """
<script>
(function () {
  // Nav background on scroll
  var nav = document.querySelector('.nav');
  function onScroll() {
    if (window.scrollY > 80) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Form handling — POST to Static Forms via fetch, show inline success/error
  var form = document.getElementById('contact-form');
  var status = document.getElementById('form-status');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.hidden = false;
      status.className = 'form-status';
      status.textContent = 'Sending...';
      var data = new FormData(form);
      var json = {};
      data.forEach(function (v, k) { json[k] = v; });
      fetch('https://api.staticforms.xyz/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(json)
      }).then(function (r) { return r.json(); })
        .then(function (resp) {
          if (resp && resp.success) {
            status.className = 'form-status success';
            status.textContent = 'Got it. He\\'ll call back the same day if it comes in during business hours.';
            form.reset();
          } else {
            status.className = 'form-status error';
            status.textContent = "Something didn't go through. Try again, or call (239) 867-8447.";
          }
        }).catch(function () {
          status.className = 'form-status error';
          status.textContent = "Something didn't go through. Try again, or call (239) 867-8447.";
        });
    });
  }
})();
</script>
"""

# Status message styles (insert into stylesheet just before closing </style>)
status_css = """
.form-status { margin-top: var(--s-4); padding: var(--s-3) var(--s-4); border-radius: var(--r-md); font-family: var(--font-body); font-size: var(--t-body-sm); }
.form-status.success { background: rgba(45,106,79,0.10); color: var(--c-success); border: 1px solid rgba(45,106,79,0.25); }
.form-status.error { background: rgba(155,44,44,0.10); color: var(--c-error); border: 1px solid rgba(155,44,44,0.25); }
"""
html = html.replace('</style>\n</head>', status_css + '</style>\n</head>')

# Insert inline JS before </body>
html = html.replace('</body>', inline_js + '\n</body>')

# ---- Open Graph + Twitter Card + favicon + canonical (head additions) ----
canonical_url = 'https://yankee-handyman.vercel.app/'   # placeholder; replaces post-deploy
head_additions = f"""<meta property="og:title" content="Yankee Handyman — Ocala">
<meta property="og:description" content="Creating Beautiful Spaces and Smiling Faces. Fifty Marion County customers, 4.9 stars on Google.">
<meta property="og:image" content="og-image.jpg">
<meta property="og:url" content="{canonical_url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Yankee Handyman — Ocala">
<meta name="twitter:description" content="Creating Beautiful Spaces and Smiling Faces.">
<meta name="twitter:image" content="og-image.jpg">
<link rel="canonical" href="{canonical_url}">
<link rel="icon" type="image/png" sizes="64x64" href="favicon.png">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="{BRAND}">
"""
# Insert just before <link href="https://fonts.googleapis.com/css2..."> or before </head>
html = html.replace(
    '<link href="https://fonts.googleapis.com/css2',
    head_additions + '<link href="https://fonts.googleapis.com/css2'
)

# ---- LocalBusiness + AggregateRating JSON-LD (insert before </head>) ----
schema = {
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": "Yankee Handyman LLC",
    "alternateName": "The Yankee Handyman",
    "telephone": "+1-239-867-8447",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "6726 Cherry Rd",
        "addressLocality": "Ocala",
        "addressRegion": "FL",
        "postalCode": "34472",
        "addressCountry": "US"
    },
    "areaServed": [
        {"@type": "City", "name": "Ocala"},
        {"@type": "AdministrativeArea", "name": "Marion County"}
    ],
    "openingHoursSpecification": [
        {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"17:00"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"09:00","closes":"17:00"}
    ],
    "priceRange": "$",
    "url": canonical_url,
    "image": canonical_url + "og-image.jpg",
    "logo": canonical_url + "logo.jpg",
    "founder": {"@type":"Person","name":"Anthony Porett"},
    "aggregateRating": {
        "@type":"AggregateRating","ratingValue":"4.9","reviewCount":"50",
        "bestRating":"5","worstRating":"1"
    },
    "sameAs": ["https://www.facebook.com/TheYankeeHandymanLLC/"]
}
schema_block = '<script type="application/ld+json">\n' + json.dumps(schema, indent=2) + '\n</script>\n'
html = html.replace('</head>', schema_block + '</head>')

# ---- Strip the visual-comp note overlay div ----
html = re.sub(
    r'<div class="comp-note">[^<]*</div>',
    '',
    html
)
# Strip its CSS too
html = re.sub(
    r'/\* placeholder marker style — visible only in comp \*/\n\.comp-note \{[^}]*\}',
    '',
    html, flags=re.DOTALL
)

# ---- Add nav.scrolled style (referenced by JS) ----
html = html.replace(
    '.nav-links a:hover { color: var(--c-ink); }',
    '.nav-links a:hover { color: var(--c-ink); }\n.nav.scrolled { box-shadow: 0 1px 0 var(--c-line); }'
)

# ---- Write index.html ----
out = os.path.join(BUILD, 'index.html')
with open(out, 'w') as f:
    f.write(html)
print(f"\nWritten {out}  ({len(html):,} bytes)")

# ---- vercel.json (static-site config) ----
vercel_cfg = {
    "version": 2,
    "headers": [
        {
            "source": "/(.*\\.(jpg|png|webp|woff2|ico))",
            "headers": [{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]
        },
        {
            "source": "/",
            "headers": [{"key":"Cache-Control","value":"public, max-age=300, must-revalidate"}]
        }
    ],
    "cleanUrls": True
}
with open(os.path.join(BUILD, 'vercel.json'), 'w') as f:
    json.dump(vercel_cfg, f, indent=2)
print(f"vercel.json written")

# ---- robots.txt + sitemap.xml ----
with open(os.path.join(BUILD, 'robots.txt'), 'w') as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {canonical_url}sitemap.xml\n")
with open(os.path.join(BUILD, 'sitemap.xml'), 'w') as f:
    f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{canonical_url}</loc>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
""")
print("robots.txt + sitemap.xml written")

# ---- Build summary ----
total_size = sum(os.path.getsize(os.path.join(dirpath, f))
                 for dirpath, _, files in os.walk(BUILD) for f in files)
print(f"\nBuild complete. Total bytes: {total_size:,}")
print(f"\nbuild/ contents:")
for dirpath, _, files in os.walk(BUILD):
    rel = os.path.relpath(dirpath, BUILD)
    for f in sorted(files):
        path = os.path.join(dirpath, f)
        sz = os.path.getsize(path)
        print(f"  {os.path.join(rel, f) if rel != '.' else f:55s}  {sz:>10,}B")
