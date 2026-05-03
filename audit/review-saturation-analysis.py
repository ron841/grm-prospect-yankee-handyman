"""Take the GBP scrape (44 reviews with bodies), dedup, run saturation analysis,
and emit a structured table for the intake.md update."""

import json, re, collections, os

ROOT = os.path.expanduser('~/grm-sites-prospects/yankee-handyman')

with open(os.path.join(ROOT, 'audit/gbp-reviews-v2.json')) as f:
    data = json.load(f)
gbp = data if isinstance(data, list) else data.get('result', [])
gbp_with_body = [r for r in gbp if r.get('body')]
print(f"GBP reviews scraped (with body): {len(gbp_with_body)}")

# Dedup helper: author + first 30 chars of body
def dedup_key(r):
    name = (r.get('name') or '').lower().strip()
    body = re.sub(r'\s+', ' ', (r.get('body') or '').lower())[:30]
    return f"{name}|{body}"

seen = {}
unique = []
for r in gbp_with_body:
    k = dedup_key(r)
    if k in seen:
        seen[k]['confidence_boost'] += 1
        continue
    r['confidence_boost'] = 1
    r['source'] = 'GBP (scrape via Google Maps)'
    seen[k] = r
    unique.append(r)
print(f"After dedup within GBP: {len(unique)}")

# Star distribution
stars = collections.Counter(r['stars'] for r in unique)
print(f"\nStar distribution: {dict(sorted(stars.items()))}")
print(f"Reviews with owner-reply present: {sum(1 for r in unique if r.get('has_reply'))} of {len(unique)}")

# === Job-noun saturation ===
JOB_NOUN_PATTERNS = {
    'plumbing':       r'\b(plumb|plumbing|disposal|sink|toilet|faucet|leak|drain|water heater|garbage disposal)\b',
    'electrical':     r'\b(electric|electrical|circuit|wiring|chandelier|fixture|outlet|switch|light|lighting|ceiling fan|fan)\b',
    'carpentry':      r'\b(carpentry|frame|framing|wall|stud|trim|finish|cabinet|shelves?|bookcas|built-in)\b',
    'porch':          r'\b(porch|enclos|screen|patio)\b',
    'pool_deck':      r'\b(pool deck|pool|deck|coping|edge|sand|sanded|sanding)\b',
    'tile':           r'\b(tile|tiling|re-?tile|grout|backsplash|shower|bathroom)\b',
    'painting':       r'\b(paint|painting|wall color|interior paint|exterior paint)\b',
    'pergola':        r'\b(pergola|arbor|gazebo|outdoor structure)\b',
    'door_window':    r'\b(door|window|hinge|lock|sash|frame.*window)\b',
    'roof_siding':    r'\b(roof|roofing|shingle|siding|gutter|fascia)\b',
    'flooring':       r'\b(floor|flooring|laminate|hardwood|vinyl|baseboard)\b',
    'demo_haul':      r'\b(demo|demolition|haul|haul off|removed|removal|tear out)\b',
    'pressure_wash':  r'\b(pressure wash|wash)\b',
    'fence_gate':     r'\b(fence|gate|fencing)\b',
    'general_repair': r'\b(repair|fix|fixed|fixing|patch)\b',
}

PRAISE_PATTERNS = {
    'price_value':         r'\b(reasonable|fair|great price|good price|affordable|fair price|cost|priced|cheap|affordab)\b',
    'price_vs_competitor': r'\b(other (quote|estimate|plumb|contractor)|cheaper than|less than|quoted me|three (other )?quote)\b',
    'fast_response':       r'\b(same day|quick|fast|prompt|immediately|right away|next day|within (a |the )?day)\b',
    'on_time':             r'\b(on time|punctual|when he said|showed up|arrived)\b',
    'cleanup':             r'\b(clean(ed)? up|left it clean|cleaned after|no mess|cleaned everything|tidy)\b',
    'quality_finish':      r'\b(excellent|quality|finish|finished|professional|exceptional|great work|amazing|perfect|beautif|wonderful|fantastic|outstanding|impressive)\b',
    'goes_above':          r'\b(above and beyond|extra mile|over and above)\b',
    'repeat_customer':     r'\b(several years|years of|use(d)? (him|them) (again|before|multiple)|second time|past projects|over (\d+|twenty|ten) projects?|many (jobs|projects)|use (him|them) again)\b',
    'honest_reliable':     r'\b(honest|reliable|trustworth|integrity|trust|dependab)\b',
    'highly_recommend':    r'\b(highly recommend|recommend|recommended|will (use|hire) again|would (use|hire) again|100%)\b',
    'multi_trade':         r'\b(many (different|kinds)|all kinds|jack of all|various|multiple (jobs|trades)|whatever)\b',
    'communication':       r'\b(communicat|kept (me )?inform|in touch|responsive|texted|called back|return(ed)? (the )?call)\b',
    'knowledgeable':       r'\b(knew what|knowledg|expert|skilled|talented|capable)\b',
    'courteous_polite':    r'\b(courteous|polite|friendly|kind|nice (man|guy|gentleman)|respectful|considerate)\b',
}

def count_matches(reviews, patterns):
    """For each pattern: count of reviews that matched it. Cumulative + per-review for plateau detection."""
    counts = {}
    cumulative = []  # list of dicts — distinct patterns hit after each review
    distinct = set()
    review_hits = []  # for each review: which patterns it hit
    for r in reviews:
        body = (r.get('body') or '').lower()
        hits = set()
        for name, pat in patterns.items():
            if re.search(pat, body):
                hits.add(name)
                counts[name] = counts.get(name, 0) + 1
        review_hits.append(hits)
        distinct.update(hits)
        cumulative.append({'distinct_count': len(distinct), 'distinct_set': set(distinct)})
    return counts, cumulative, review_hits

job_counts, job_cum, job_hits = count_matches(unique, JOB_NOUN_PATTERNS)
praise_counts, praise_cum, praise_hits = count_matches(unique, PRAISE_PATTERNS)

print(f"\n=== Job-noun frequency (cumulative) ===")
for name, n in sorted(job_counts.items(), key=lambda x: -x[1]):
    print(f"  {n:4d}  {name}")
print(f"\n=== Praise-pattern frequency ===")
for name, n in sorted(praise_counts.items(), key=lambda x: -x[1]):
    print(f"  {n:4d}  {name}")

# Saturation — when did each set plateau?
def plateau_review_n(cumulative):
    """Return the review index at which we hit the final distinct count (saturation)."""
    final = cumulative[-1]['distinct_count']
    for i, c in enumerate(cumulative):
        if c['distinct_count'] >= final:
            return i + 1
    return len(cumulative)

job_plateau = plateau_review_n(job_cum)
praise_plateau = plateau_review_n(praise_cum)
print(f"\n=== Saturation ===")
print(f"Distinct job-nouns plateau at review #{job_plateau} of {len(unique)} (final: {job_cum[-1]['distinct_count']} of {len(JOB_NOUN_PATTERNS)})")
print(f"Distinct praise-patterns plateau at review #{praise_plateau} of {len(unique)} (final: {praise_cum[-1]['distinct_count']} of {len(PRAISE_PATTERNS)})")
both_saturated = max(job_plateau, praise_plateau)
print(f"Both saturated by review #{both_saturated}; remaining {len(unique)-both_saturated} reviews are confirmation-not-discovery")

# Save the cleaned, deduped, sorted set (longest reviews first as a curation hint)
unique_sorted = sorted(unique, key=lambda r: -len(r.get('body','')))
out_path = os.path.join(ROOT, 'audit/reviews-deduped.json')
with open(out_path, 'w') as f:
    # Strip the set-typed fields for JSON
    json.dump([{k:v for k,v in r.items() if not isinstance(v, set)} for r in unique_sorted], f, indent=2)
print(f"\nSaved {len(unique_sorted)} deduped reviews → {out_path}")

# Save analysis as a tabular summary for the intake.md write
summary = {
    'gbp_scraped': len(gbp_with_body),
    'unique_after_dedup': len(unique),
    'star_distribution': dict(stars),
    'with_owner_reply': sum(1 for r in unique if r.get('has_reply')),
    'job_noun_frequency': dict(sorted(job_counts.items(), key=lambda x: -x[1])),
    'praise_pattern_frequency': dict(sorted(praise_counts.items(), key=lambda x: -x[1])),
    'job_noun_saturation_at_review': job_plateau,
    'praise_pattern_saturation_at_review': praise_plateau,
    'distinct_job_nouns': job_cum[-1]['distinct_count'],
    'distinct_praise_patterns': praise_cum[-1]['distinct_count'],
    'both_saturated_at_review': both_saturated,
}
with open(os.path.join(ROOT, 'audit/saturation-summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)
print(f"Saturation summary saved → audit/saturation-summary.json")
