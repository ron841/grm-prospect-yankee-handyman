"""Build /reviews page (build/reviews.html) per reviews-slots.md spec.
Also updates homepage: adds /reviews nav link + trust marquee item 2a.
Output: build/reviews.html + modified build/index.html.
"""

import json, os, re, html

ROOT = os.path.expanduser('~/grm-sites-prospects/yankee-handyman')
BUILD = os.path.join(ROOT, 'build')
INDEX = os.path.join(BUILD, 'index.html')
REVIEWS = os.path.join(BUILD, 'reviews.html')

# ---- 1) Load corpus ----
with open(os.path.join(ROOT, 'audit/gbp-reviews-v3-with-replies.json')) as f:
    corpus_wrap = json.load(f)
corpus = {r['name']: r for r in corpus_wrap['reviews'] if r.get('body')}
print(f"Corpus loaded: {len(corpus)} reviews")

# ---- 2) Slot lists per content-inventory ----
CURATED = [
    ('Judy',           'Multi-project relationship'),
    ('Cheryl Mulhern', 'Plumbing · Bellechase'),
    ('Diane Bennett',  'Pool deck'),
    ('Linda Weis',     'Deck rebuild'),
    ('Andrew Abad',    'Repeat customer · 20+ projects'),
]
OUTLIER_NAME = 'DM _'

GROUPS = [
    {
        'eyebrow': 'GROUP 1', 'headline': 'Carpentry and framing',
        'subhead': 'Six reviews mention carpentry, framing, or finish work.',
        'reviewers': [
            ('Cole Spires',      'Porch enclosure + interior wall + tile'),
            ('Barbara Roberts',  'Wall replacement + sliding glass door + windows'),
            ('William Stone',    'Door trim repair (termite damage)'),
            ('Edward Campea',    'Pavilion + trash can container'),
            ('Leanna Fitzgerald','Siding repair + screens + paint'),
            ('Ju B',             'Pergola'),
        ],
    },
    {
        'eyebrow': 'GROUP 2', 'headline': 'Tile and flooring',
        'subhead': 'Carpet pulled, tile laid, floors finished clean from one room to the next.',
        'reviewers': [
            ('Maudeline Henry',  'Carpet removal + tile + backsplash'),
            ('Zac Stone',        'Floor finishing'),
            ('Ashley Santiago',  'Floors'),
        ],
    },
    {
        'eyebrow': 'GROUP 3', 'headline': 'Porches, decks, outdoor builds',
        'subhead': 'Florida rooms, screened porches, walk-in showers, decks for the pool.',
        'reviewers': [
            ('David Bittman',    'Screened porch rebuild + rear deck'),
            ('Brendon Pointing', 'Bathroom remodel + walk-in shower'),
            ('Terri',            'Screen door + porch railing'),
        ],
    },
    {
        'eyebrow': 'GROUP 4', 'headline': 'Multi-trade and repeat customers',
        'subhead': 'Customers who hired Anthony once, then kept hiring him.',
        'reviewers': [
            ('JEAN JONES',       'Drywall + paint + flooring + plumbing + electrical + tile'),
            ('audrey bittman',   'Multi-year relationship'),
            ('Karen Cowan',      'Multi-job'),
        ],
    },
    {
        'eyebrow': 'GROUP 5', 'headline': 'Plumbing and electrical',
        'subhead': 'Disposals, leaks, new circuits, light fixtures.',
        'reviewers': [
            ('Megan Stone',      'Major kitchen leak'),
            ('Molly Groves',     'New circuit + chandelier'),
        ],
    },
    {
        'eyebrow': 'GROUP 6', 'headline': 'Painting',
        'subhead': 'Interior, exterior, trim.',
        'reviewers': [
            ('Jennifer LeMay',   'Interior paint'),
        ],
    },
    {
        'eyebrow': 'GROUP 7', 'headline': 'Quick jobs and short praise',
        'subhead': 'On-time, reasonable, done. Fourteen reviews in this category.',
        'two_col': True,
        'reviewers': [
            ('Zulma Velez',      ''), ('Robert Nedow',    ''), ('George Kim',     ''),
            ('Devin P',          ''), ('Bob Hart',        ''), ('Sam Perry',      ''),
            ('Dan Carter',       ''), ('Jon De Lucia',    ''), ('Griselle Martin',''),
            ('Jorge Aliaga',     ''), ('Ryan McBride',    ''), ('Brian Stamper',  ''),
            ('Jarron Remington', ''), ('Katheryn Foerste','')
        ],
    },
]

ARCHIVE = [
    'Wally Plumstead', 'Hi 5 Tobacco and vapor', 'tyisha epps',
    'Sherry Brickner', 'Patrice Stone', 'Ariana Vixen',
]

# ---- 3) Sanity check: every named reviewer is in the corpus ----
all_named = ([n for n, _ in CURATED] + [OUTLIER_NAME] +
             [n for g in GROUPS for n, _ in g['reviewers']] + ARCHIVE)
print(f"Named reviewers in spec: {len(all_named)}")
missing = [n for n in all_named if n not in corpus]
if missing:
    # Some reviewers may have slightly different names — try fuzzy
    print(f"  ! NOT in corpus by exact match: {missing}")
    for m in missing:
        cands = [k for k in corpus if m.lower().split()[0] in k.lower()]
        print(f"    candidates for '{m}': {cands[:3]}")
        if cands:
            corpus[m] = corpus[cands[0]]
            print(f"    → mapped {m!r} to {cands[0]!r}")

# Final missing check
still_missing = [n for n in all_named if n not in corpus]
if still_missing:
    print(f"  ! still missing after fuzzy: {still_missing}")
print(f"  Sum: 5 curated + 1 outlier + {sum(len(g['reviewers']) for g in GROUPS)} grouped + {len(ARCHIVE)} archive = {5+1+sum(len(g['reviewers']) for g in GROUPS)+len(ARCHIVE)}")

# ---- 4) Helpers ----
def esc(s):
    return html.escape(s or '', quote=True)

def review_paragraphs(body):
    """Split review body into <p> tags on blank-line breaks for proper rendering."""
    paras = re.split(r'\n\s*\n', (body or '').strip())
    return ''.join(f'<p>{esc(p.strip())}</p>' for p in paras if p.strip())

def render_pair_card(reviewer, job_tag, body, reply_text, reply_date, stars=5, compact=False, outlier=False):
    star_class = 'star-outlier' if outlier else 'star-curated'
    tag_html = f'<span class="job-tag">{esc(job_tag)}</span>' if job_tag else ''
    reply_block = ''
    if reply_text:
        reply_block = f'''
        <div class="reply-block">
          <div class="reply-attr"><span class="reply-arrow" aria-hidden="true">↳</span> Anthony{f', {esc(reply_date)}' if reply_date else ''}<span class="visually-hidden"> reply from Anthony Porett</span></div>
          <p class="reply-text">{esc(reply_text)}</p>
        </div>'''
    klass = 'review-pair-card' + (' compact' if compact else '') + (' outlier' if outlier else '')
    aria_id = 'r-' + re.sub(r'[^a-z0-9]', '-', reviewer.lower()).strip('-')
    return f'''<article class="{klass}" aria-labelledby="{aria_id}">
        <div class="card-header">
          <span class="stars {star_class}" aria-label="{stars} out of 5 stars">{'★' * stars}{'☆' * (5-stars)}</span>
          <h3 class="reviewer-name" id="{aria_id}">{esc(reviewer)}</h3>
          {tag_html}
        </div>
        <div class="review-body">{review_paragraphs(body)}</div>{reply_block}
      </article>'''

def render_archive_entry(reviewer):
    r = corpus.get(reviewer, {})
    body = (r.get('body') or '').strip()
    reply_text = (r.get('reply_text') or '').strip()
    reply_date = (r.get('reply_by') or '').strip()
    return f'''<div class="archive-entry">
        <div class="archive-meta"><span class="stars star-curated" aria-label="5 out of 5 stars">★★★★★</span> <span class="archive-name">{esc(reviewer)}</span>{f' · <span class="archive-date">{esc(reply_date)}</span>' if reply_date else ''}</div>
        <p class="archive-body">"{esc(body)}"</p>
        {f'<p class="archive-reply"><span class="reply-arrow" aria-hidden="true">↳</span> {esc(reply_text)}</p>' if reply_text else ''}
      </div>'''

# ---- 5) Render sections ----
curated_html = ''
for name, tag in CURATED:
    r = corpus[name]
    curated_html += render_pair_card(
        reviewer=name, job_tag=tag,
        body=r.get('body',''), reply_text=r.get('reply_text',''), reply_date=r.get('reply_by',''),
        stars=5
    ) + '\n'

outlier_r = corpus[OUTLIER_NAME]
outlier_html = render_pair_card(
    reviewer=OUTLIER_NAME, job_tag='April 2024',
    body=outlier_r.get('body',''), reply_text=outlier_r.get('reply_text',''), reply_date=outlier_r.get('reply_by',''),
    stars=1, outlier=True
)

groups_html = ''
for g in GROUPS:
    cards = ''
    for name, tag in g['reviewers']:
        r = corpus[name]
        cards += render_pair_card(
            reviewer=name, job_tag=tag,
            body=r.get('body',''), reply_text=r.get('reply_text',''), reply_date=r.get('reply_by',''),
            stars=5, compact=True
        ) + '\n'
    grid_class = ' two-col' if g.get('two_col') else ''
    groups_html += f'''<section class="group-section">
      <header class="group-header">
        <div class="section-eyebrow">{esc(g['eyebrow'])}</div>
        <h2 class="section-headline">{esc(g['headline'])}</h2>
        <p class="section-subhead">{esc(g['subhead'])}</p>
      </header>
      <div class="group-grid{grid_class}">
        {cards}
      </div>
    </section>
    '''

archive_html = ''
for name in ARCHIVE:
    archive_html += render_archive_entry(name) + '\n'

# ---- 6) JSON-LD: 44 Review entries ----
json_ld_reviews = []
all_for_schema = (
    [(name, 5) for name, _ in CURATED] +
    [(OUTLIER_NAME, 1)] +
    [(name, 5) for g in GROUPS for name, _ in g['reviewers']] +
    [(name, 5) for name in ARCHIVE]
)
for name, stars in all_for_schema:
    r = corpus.get(name, {})
    json_ld_reviews.append({
        "@context": "https://schema.org",
        "@type": "Review",
        "itemReviewed": {"@type": "LocalBusiness", "name": "The Yankee Handyman LLC"},
        "reviewRating": {"@type": "Rating", "ratingValue": str(stars), "bestRating": "5"},
        "author": {"@type": "Person", "name": name},
        "reviewBody": r.get('body','').strip(),
        "publisher": {"@type": "Organization", "name": "Google"}
    })
print(f"\nJSON-LD Review entries: {len(json_ld_reviews)}")

json_ld_block = json.dumps(json_ld_reviews, indent=2, ensure_ascii=False)

# ---- 7) GBP listing URL for "see all 50" CTA ----
GBP_REVIEWS_URL = "https://www.google.com/maps/place/?q=place_id:ChIJd58JVcXT54gRPqTCoeHtDXA"

# ---- 8) Build full /reviews HTML ----
reviews_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Reviews — Yankee Handyman, Ocala</title>
<meta name="description" content="Forty-four of Anthony Porett's fifty Google reviews. Plumbing, electrical, carpentry, tile, paint. Marion County, 4.9 stars.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@700&family=Merriweather:ital,wght@0,400;0,700;1,400&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
<meta property="og:title" content="What Marion County says about Yankee Handyman">
<meta property="og:description" content="Forty-four customer reviews. Forty-three replies from Anthony. One 1-star included.">
<meta property="og:url" content="https://yankee-handyman.example/reviews">
<meta property="og:type" content="website">
<meta property="og:image" content="og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="What Marion County says about Yankee Handyman">
<meta name="twitter:description" content="Forty-four customer reviews. Forty-three replies from Anthony.">
<meta name="twitter:image" content="og-image.jpg">
<link rel="canonical" href="/reviews">
<link rel="icon" type="image/png" sizes="64x64" href="favicon.png">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#6b4423">
<style>
:root {{
  --font-display: 'Merriweather', Georgia, serif;
  --font-eyebrow: 'Comfortaa', system-ui, sans-serif;
  --font-body:    'Nunito', system-ui, sans-serif;
  --t-eyebrow: 13px; --t-body-sm: 16px; --t-body: 18px; --t-body-lg: 20px;
  --t-h4: 22px; --t-h3: 28px; --t-h2: 40px; --t-h1: 56px;
  --c-ink: #1f1810; --c-ink-soft: #5a4a3a; --c-paper: #faf6ee;
  --c-paper-2: #ede4d2; --c-line: #d8ccb4;
  --c-brand: #6b4423; --c-brand-soft: rgba(107,68,35,0.12); --c-accent: #a8784a;
  --c-success: #5a6a3f; --c-error: #8b3a2a;
  --s-1: 4px;  --s-2: 8px;  --s-3: 12px; --s-4: 16px;
  --s-5: 24px; --s-6: 32px; --s-7: 48px; --s-8: 64px;
  --s-9: 96px; --s-10: 128px;
  --r-sm: 4px; --r-md: 8px; --r-lg: 16px;
  --line: 1px solid var(--c-line);
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: var(--font-body); font-size: var(--t-body); line-height: 1.6;
  color: var(--c-ink); background: var(--c-paper);
  -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility;
}}
a {{ color: inherit; text-decoration: none; }}
.visually-hidden {{ position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); border: 0; }}
.container {{ max-width: 800px; margin: 0 auto; padding: 0 var(--s-6); }}
.container-wide {{ max-width: 1200px; margin: 0 auto; padding: 0 var(--s-6); }}
/* Nav */
.nav {{ position: fixed; top: 0; left: 0; right: 0; height: 72px; background: rgba(250,246,238,0.92); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-bottom: var(--line); z-index: 100; display: flex; align-items: center; }}
.nav-inner {{ width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 var(--s-6); display: flex; align-items: center; justify-content: space-between; gap: var(--s-6); }}
.nav-brand {{ display: flex; align-items: center; gap: var(--s-3); font-family: var(--font-display); font-weight: 700; font-size: 18px; color: var(--c-ink); }}
.nav-logo {{ width: 32px; height: 32px; background: var(--c-brand); color: #fff; display: flex; align-items: center; justify-content: center; font-family: var(--font-display); font-weight: 700; font-size: 16px; border-radius: var(--r-sm); }}
.nav-links {{ display: flex; gap: var(--s-7); list-style: none; font-family: var(--font-body); font-weight: 600; font-size: 16px; }}
.nav-links a {{ color: var(--c-ink-soft); transition: color 0.2s; }}
.nav-links a:hover {{ color: var(--c-ink); }}
.nav-links a.active {{ color: var(--c-ink); border-bottom: 2px solid var(--c-brand); padding-bottom: 4px; }}
.nav-cta {{ background: var(--c-brand); color: #fff; padding: 10px 20px; border-radius: var(--r-md); font-family: var(--font-body); font-weight: 700; font-size: 15px; display: inline-flex; align-items: center; gap: var(--s-2); }}
main {{ padding-top: 72px; }}

/* Page header */
.page-header {{ padding: var(--s-9) 0 var(--s-7); }}
.page-eyebrow {{ font-family: var(--font-eyebrow); font-weight: 700; font-size: var(--t-eyebrow); letter-spacing: 0.20em; text-transform: uppercase; color: var(--c-brand); margin-bottom: var(--s-4); }}
.page-headline {{ font-family: var(--font-display); font-weight: 700; font-size: var(--t-h1); line-height: 1.15; color: var(--c-ink); margin-bottom: var(--s-5); text-wrap: balance; }}
.page-subhead {{ font-family: var(--font-body); font-size: var(--t-body-lg); color: var(--c-ink-soft); max-width: 60ch; margin-bottom: var(--s-6); line-height: 1.55; }}
.back-link {{ font-family: var(--font-body); font-size: var(--t-body-sm); color: var(--c-ink-soft); }}
.back-link:hover {{ text-decoration: underline; }}

/* Section bases */
.section-eyebrow {{ font-family: var(--font-eyebrow); font-weight: 700; font-size: var(--t-eyebrow); letter-spacing: 0.20em; text-transform: uppercase; color: var(--c-ink-soft); margin-bottom: var(--s-3); }}
.section-headline {{ font-family: var(--font-display); font-weight: 700; font-size: var(--t-h2); line-height: 1.2; color: var(--c-ink); margin-bottom: var(--s-4); text-wrap: balance; }}
.section-subhead {{ font-family: var(--font-body); font-size: var(--t-body-lg); color: var(--c-ink-soft); line-height: 1.55; margin-bottom: var(--s-7); }}

/* Curated leads */
.curated-section {{ padding: var(--s-7) 0; }}
.curated-stack > .review-pair-card + .review-pair-card {{ margin-top: var(--s-7); }}

/* Outlier section */
.outlier-section {{ padding: var(--s-9) 0 var(--s-7); }}

/* Group sections */
.group-section {{ padding: var(--s-9) 0 0; }}
.group-header {{ margin-bottom: var(--s-7); }}
.group-grid {{ display: flex; flex-direction: column; gap: var(--s-5); }}
.group-grid.two-col {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: var(--s-5); }}

/* Pair card */
.review-pair-card {{ background: var(--c-paper); border: var(--line); border-radius: var(--r-lg); padding: var(--s-7); }}
.review-pair-card.compact {{ padding: var(--s-5); }}
.review-pair-card.outlier {{ background: var(--c-paper-2); }}
.card-header {{ display: flex; align-items: baseline; gap: var(--s-4); flex-wrap: wrap; margin-bottom: var(--s-4); }}
.stars {{ font-size: var(--t-body-lg); letter-spacing: 0.05em; line-height: 1; }}
.star-curated {{ color: #d6a419; }}
.star-outlier {{ color: var(--c-error); }}
.reviewer-name {{ font-family: var(--font-display); font-weight: 700; font-size: var(--t-h4); color: var(--c-ink); flex: 1; }}
.job-tag {{ font-family: var(--font-body); font-style: italic; font-size: var(--t-body-sm); color: var(--c-ink-soft); margin-left: auto; }}
.review-body {{ font-family: var(--font-body); font-size: var(--t-body); color: var(--c-ink); line-height: 1.6; max-width: 70ch; }}
.review-body p + p {{ margin-top: var(--s-4); }}
.reply-block {{ margin-top: var(--s-5); margin-left: var(--s-5); padding: var(--s-5); background: var(--c-paper-2); border-radius: var(--r-md); }}
.review-pair-card.outlier .reply-block {{ background: rgba(255,255,255,0.55); }}
.reply-attr {{ font-family: var(--font-body); font-weight: 600; font-size: var(--t-body-sm); color: var(--c-ink-soft); margin-bottom: var(--s-3); }}
.reply-arrow {{ color: var(--c-brand); font-weight: 700; margin-right: var(--s-2); }}
.reply-text {{ font-family: var(--font-display); font-style: italic; font-size: var(--t-body); color: var(--c-ink); line-height: 1.55; }}

/* Archive */
.archive-section {{ padding: var(--s-10) 0 var(--s-9); }}
.archive-list {{ margin-top: var(--s-7); }}
.archive-entry {{ padding: var(--s-5) 0; border-bottom: var(--line); }}
.archive-entry:first-child {{ border-top: var(--line); }}
.archive-meta {{ font-family: var(--font-body); font-size: var(--t-body-sm); color: var(--c-ink-soft); margin-bottom: var(--s-3); }}
.archive-name {{ font-weight: 600; color: var(--c-ink); }}
.archive-body {{ font-family: var(--font-display); font-style: italic; font-size: var(--t-body); color: var(--c-ink); line-height: 1.55; max-width: 70ch; margin-bottom: var(--s-3); }}
.archive-reply {{ font-family: var(--font-body); font-size: var(--t-body-sm); color: var(--c-ink-soft); font-style: italic; max-width: 70ch; }}

/* CTA banner */
.cta-banner {{ background: var(--c-paper-2); padding: var(--s-10) 0; text-align: center; margin-top: var(--s-10); }}
.cta-banner h2 {{ font-family: var(--font-display); font-weight: 700; font-size: var(--t-h2); color: var(--c-ink); margin-bottom: var(--s-4); }}
.cta-banner p {{ font-family: var(--font-body); font-size: var(--t-body-lg); color: var(--c-ink-soft); max-width: 60ch; margin: 0 auto var(--s-7); }}
.cta-row {{ display: inline-flex; align-items: center; gap: var(--s-6); flex-wrap: wrap; justify-content: center; }}
.cta-phone {{ background: var(--c-brand); color: #fff; padding: 16px 28px; border-radius: var(--r-md); font-family: var(--font-body); font-weight: 700; font-size: var(--t-body); display: inline-flex; align-items: center; gap: var(--s-2); }}
.cta-phone:hover {{ background: #4a2f15; }}
.cta-link {{ font-family: var(--font-body); font-weight: 600; font-size: var(--t-body); color: var(--c-ink-soft); border-bottom: 1px solid currentColor; padding-bottom: 2px; }}
.cta-link:hover {{ color: var(--c-brand); }}

/* Footer */
.footer {{ background: var(--c-ink); color: var(--c-paper); padding: var(--s-9) 0 var(--s-6); margin-top: 0; }}
.footer-grid {{ display: grid; grid-template-columns: 1.5fr 1fr 1fr; gap: var(--s-7); margin-bottom: var(--s-8); }}
.footer-brand {{ font-family: var(--font-display); font-weight: 700; font-size: var(--t-h3); margin-bottom: var(--s-4); color: #fff; }}
.footer-tagline {{ font-family: var(--font-body); font-size: var(--t-body); color: rgba(255,255,255,0.75); max-width: 320px; line-height: 1.6; }}
.footer-label {{ font-family: var(--font-eyebrow); font-weight: 700; font-size: var(--t-eyebrow); letter-spacing: 0.20em; text-transform: uppercase; color: rgba(255,255,255,0.55); margin-bottom: var(--s-4); }}
.footer-list {{ list-style: none; display: flex; flex-direction: column; gap: var(--s-3); }}
.footer-list a, .footer-list span {{ font-family: var(--font-body); font-size: var(--t-body); color: rgba(255,255,255,0.85); transition: color 0.2s; }}
.footer-list a:hover {{ color: #fff; }}
.footer-bottom {{ border-top: 1px solid rgba(255,255,255,0.1); padding-top: var(--s-5); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: var(--s-3); }}
.footer-meta {{ font-family: var(--font-body); font-size: var(--t-body-sm); color: rgba(255,255,255,0.55); }}

/* Sticky mobile call bar */
.sticky-call {{ display: none; position: fixed; left: 0; right: 0; bottom: 0; background: var(--c-accent); color: #fff; padding: var(--s-4); font-family: var(--font-body); font-weight: 700; font-size: var(--t-body-lg); text-align: center; z-index: 90; box-shadow: 0 -4px 16px rgba(0,0,0,0.15); }}

/* Responsive */
@media (max-width: 1023px) {{
  .group-grid.two-col {{ grid-template-columns: 1fr; }}
  .footer-grid {{ grid-template-columns: 1fr 1fr; }}
}}
@media (max-width: 767px) {{
  :root {{ --t-h1: 36px; --t-h2: 32px; --t-h3: 24px; }}
  .nav-links {{ display: none; }}
  .nav-cta {{ padding: 8px 14px; font-size: 13px; }}
  .nav-brand span {{ display: none; }}
  .page-header {{ padding: var(--s-7) 0 var(--s-5); }}
  .group-section {{ padding: var(--s-8) 0 0; }}
  .review-pair-card {{ padding: var(--s-5); }}
  .review-pair-card.compact {{ padding: var(--s-4); }}
  .reply-block {{ margin-left: var(--s-3); padding: var(--s-4); }}
  .card-header {{ flex-direction: column; align-items: flex-start; gap: var(--s-2); }}
  .job-tag {{ margin-left: 0; }}
  .footer-grid {{ grid-template-columns: 1fr; }}
  .sticky-call {{ display: block; }}
  main {{ padding-bottom: 64px; }}
  .cta-row {{ flex-direction: column; gap: var(--s-4); align-items: stretch; }}
  .cta-phone {{ width: 100%; justify-content: center; }}
}}
</style>
<script type="application/ld+json">
{json_ld_block}
</script>
</head>
<body>

<header class="nav">
  <div class="nav-inner">
    <a class="nav-brand" href="/"><div class="nav-logo">YH</div><span>Yankee Handyman</span></a>
    <nav>
      <ul class="nav-links">
        <li><a href="/#services">Services</a></li>
        <li><a href="/#proof">Proof</a></li>
        <li><a class="active" href="/reviews">Reviews</a></li>
        <li><a href="/#about">About</a></li>
        <li><a href="/#contact">Contact</a></li>
      </ul>
    </nav>
    <a class="nav-cta" href="tel:+12398678447">📞 Call (239) 867-8447</a>
  </div>
</header>

<main id="main">

  <header class="page-header container">
    <div class="page-eyebrow">REVIEWS</div>
    <h1 class="page-headline">What Marion County says.</h1>
    <p class="page-subhead">Forty-four reviews on Google. Anthony has replied to forty-three of them. One 1-star is in here too.</p>
    <a class="back-link" href="/">← Yankee Handyman home</a>
  </header>

  <section class="curated-section container" aria-label="Curated lead reviews">
    <div class="curated-stack">
      {curated_html}
    </div>
  </section>

  <section class="outlier-section container" aria-label="One 1-star review">
    <header style="margin-bottom: var(--s-7);">
      <h2 class="section-headline">One 1-star review.</h2>
      <p class="section-subhead" style="margin-bottom: 0;">Anthony's reply is below it.</p>
    </header>
    {outlier_html}
  </section>

  <div class="container">
    {groups_html}

    <section class="archive-section">
      <header>
        <div class="section-eyebrow">ARCHIVE</div>
        <h2 class="section-headline">The shortest ones.</h2>
        <p class="section-subhead">Real reviews, just brief.</p>
      </header>
      <div class="archive-list">
        {archive_html}
      </div>
    </section>
  </div>

  <section class="cta-banner">
    <div class="container">
      <h2>Tell him about the job.</h2>
      <p>Phone is fastest. He answers most calls during business hours.</p>
      <div class="cta-row">
        <a class="cta-phone" href="tel:+12398678447">📞 Call (239) 867-8447</a>
        <a class="cta-link" href="{GBP_REVIEWS_URL}" target="_blank" rel="noopener">See all 50 reviews on Google →</a>
      </div>
    </div>
  </section>

</main>

<footer class="footer">
  <div class="container-wide">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">Yankee Handyman</div>
        <p class="footer-tagline">Anthony Porett and one other guy, working their way through Ocala one job at a time.</p>
      </div>
      <div>
        <div class="footer-label">Reach Anthony</div>
        <ul class="footer-list">
          <li><a href="tel:+12398678447">(239) 867-8447</a></li>
          <li><span>6726 Cherry Rd, Ocala, FL 34472</span></li>
          <li><span>Mon–Fri 8–5 · Sat 9–5 · Sun closed</span></li>
        </ul>
      </div>
      <div>
        <div class="footer-label">Find Him Online</div>
        <ul class="footer-list">
          <li><a href="https://www.facebook.com/TheYankeeHandymanLLC/" target="_blank" rel="noopener">Facebook</a></li>
          <li><a href="{GBP_REVIEWS_URL}" target="_blank" rel="noopener">Reviews on Google</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-meta">© 2026 The Yankee Handyman LLC · Ocala, Florida</div>
      <div class="footer-meta">A Get Rooted Media site.</div>
    </div>
  </div>
</footer>

<a class="sticky-call" href="tel:+12398678447">📞 Call (239) 867-8447</a>

</body>
</html>
'''

with open(REVIEWS, 'w') as f:
    f.write(reviews_html)
print(f"\nWritten {REVIEWS} ({len(reviews_html):,} bytes)")

# ---- 9) Update homepage: add /reviews nav link + trust marquee item 2a ----
with open(INDEX) as f:
    home = f.read()

# Insert "Reviews" link in nav between "Proof" and "About"
old_nav = '<li><a href="#proof">Proof</a></li>\n        <li><a href="#about">About</a></li>'
new_nav = '<li><a href="#proof">Proof</a></li>\n        <li><a href="/reviews">Reviews</a></li>\n        <li><a href="#about">About</a></li>'
if old_nav in home:
    home = home.replace(old_nav, new_nav)
    print("  homepage nav: added /reviews link")
else:
    print("  ! homepage nav anchor not found (already updated?)")

# Insert trust marquee item 2a between Bellechase and Same-day items
old_marquee = '''<div class="trust-item">
          <span class="trust-item-icon">✓</span>
          <span>Recommended by the Bellechase homeowners group</span>
        </div>
        <div class="trust-divider"></div>
        <div class="trust-item">
          <span class="trust-item-icon">⚡</span>
          <span>Same-day service when the schedule allows</span>
        </div>'''
new_marquee = '''<div class="trust-item">
          <span class="trust-item-icon">✓</span>
          <span>Recommended by the Bellechase homeowners group</span>
        </div>
        <div class="trust-divider"></div>
        <div class="trust-item">
          <span class="trust-item-icon">↩</span>
          <span>Replies personally to nearly every review</span>
        </div>
        <div class="trust-divider"></div>
        <div class="trust-item">
          <span class="trust-item-icon">⚡</span>
          <span>Same-day service when the schedule allows</span>
        </div>'''
if old_marquee in home:
    home = home.replace(old_marquee, new_marquee)
    print("  homepage trust marquee: added item 2a (Replies personally to nearly every review)")
else:
    print("  ! trust marquee anchor not found")

with open(INDEX, 'w') as f:
    f.write(home)
print(f"  Updated {INDEX}")
