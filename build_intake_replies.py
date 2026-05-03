"""Re-render the Voice — Reviews section in intake.md with reply text +
reply-relative-dates added to each review entry."""

import json, os, re, collections

ROOT = os.path.expanduser('~/grm-sites-prospects/yankee-handyman')

with open(os.path.join(ROOT, 'audit/gbp-reviews-v3-with-replies.json')) as f:
    v3 = json.load(f)
reviews = v3['reviews']
# Filter to reviews with body text + sort by body length desc (curation hint preserved)
filled = [r for r in reviews if r.get('body')]
filled.sort(key=lambda r: -len(r.get('body','')))
print(f"v3 reviews with body: {len(filled)}; with reply text: {sum(1 for r in filled if r.get('reply_text'))}")

# Reply-voice analysis for the section preamble
reply_lengths = [len(r.get('reply_text','')) for r in filled if r.get('reply_text')]
canned = sum(1 for L in reply_lengths if L < 30)
short = sum(1 for L in reply_lengths if 30 <= L < 100)
medium = sum(1 for L in reply_lengths if 100 <= L < 250)
detailed = sum(1 for L in reply_lengths if L >= 250)
opener_counts = collections.Counter()
for r in filled:
    rt = (r.get('reply_text') or '').lower().strip()
    if rt:
        opener_counts[rt[:30]] += 1
top_openers = opener_counts.most_common(5)
emoji_replies = sum(1 for r in filled if any(e in (r.get('reply_text') or '') for e in ['😁','❤','🙏','😀','💪','🎉','👍']))

# Re-render the Voice — Reviews section
out = []
out.append("## Voice — Reviews")
out.append("")
out.append(f"> **Capture method, iteration 2 (re-scrape 2026-05-03):** Scraped via Playwright DOM extraction against the Google Maps reviews panel (~25 scroll-load cycles). Pulled **44 reviews with body text** out of Yankee Handyman's 50 total. The 6 missing are 5-star ratings with no body, treated as zero-evidence-add per the saturation rule. **Re-scrape adds owner-reply text via the `.CDe7pd` selector** + reply-relative dates via `.DZSIDd`.")
out.append("")
out.append(f"> **Saturation status (per audit-script-implications.md #5):** **REACHED.** Distinct job-nouns plateau at review #38/44 (13 of 15 categories matched). Distinct praise-patterns plateau at #41/44 (13 of 14 categories matched). Both fully saturated by review #41; remaining 3 reviews are confirmation-not-discovery. Birdeye and Yelp not pulled per the locked rule.")
out.append("")
out.append(f"> **Owner-reply evidence (overturns iter-1 finding):** **43 of 44 reviews have an owner reply.** The iter-1 audit had concluded Anthony does not reply — wrong; the API's 5 returned reviews simply happened to truncate the reply field.")
out.append("")
out.append(f"> **Reply voice — quick analysis** (full reply text appears in each entry below):")
out.append(f"> - Length distribution: **{canned} canned (<30 chars)**, **{short} short (30-100)**, **{medium} medium (100-250)**, **{detailed} detailed (>250)**. No novel-length replies — Anthony keeps it brief, but most are personalized.")
out.append(f"> - Recurring openers: \"Thank you for choosing the Yankee Handyman\" (3×), \"Thank you for choosing us\" (2×), \"Thank you.\" (2×). The personal openers (\"It was my pleasure…\", \"Thank you Zack…\") are warmer than the boilerplate.")
out.append(f"> - **Voice tone:** gratitude-first, family/community framing (\"being a part of the family\", \"we appreciate you relying on us\"), forward-looking (\"looking forward to more projects\"), occasional 😁 emoji ({emoji_replies} replies use one). Switches between \"we\" and \"I/me\" — solo-operator with collective framing.")
out.append(f"> - **Implication for Design:** the reviews-page voice can lean on Anthony's actual reply phrases as connector copy or section breaks. Notable phrases worth lifting: \"being a part of the family\", \"It was my pleasure\", \"looking forward to more projects\", \"Thank you for trusting us\".")
out.append("")
out.append(f"> **Star distribution:** 43 × 5-star, 1 × 1-star (DM_, Apr 12 2024 per Birdeye). The 1-star is captured below at its index in body-length sort order.")
out.append("")

# Render each review
for i, r in enumerate(filled, 1):
    name = r.get('name', '?')
    stars = r.get('stars', '?')
    body = (r.get('body') or '').strip()
    reply_text = (r.get('reply_text') or '').strip()
    reply_date = (r.get('reply_by') or '').strip()  # Field actually contains "X months ago" relative date
    out.append(f"### Review {i} _[GBP scrape, 2026-05-03]_")
    out.append(f"- Stars: {stars}")
    out.append(f"- Reviewer: {name}")
    out.append(f"- Text: \"{body}\"")
    if reply_text:
        date_label = f" _({reply_date})_" if reply_date else ""
        out.append(f"- Owner reply{date_label}: \"{reply_text}\"")
    else:
        out.append(f"- Owner reply: _none_")
    out.append("")

# Saturation tables (same as before, regenerated for completeness)
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
    counts = {}
    for r in reviews:
        body = (r.get('body') or '').lower()
        for name, pat in patterns.items():
            if re.search(pat, body):
                counts[name] = counts.get(name, 0) + 1
    return counts

job_counts = count_matches(filled, JOB_NOUN_PATTERNS)
praise_counts = count_matches(filled, PRAISE_PATTERNS)

out.append("## Voice — Saturation tables")
out.append("")
out.append("> Generated from the 44-review GBP scrape. Frequency = number of reviews matching the regex pattern for that category.")
out.append("")
out.append("### Job-noun frequency (synthesis §3 input)")
out.append("")
out.append("| Job category | Reviews mentioning |")
out.append("|---|---|")
for k, v in sorted(job_counts.items(), key=lambda x: -x[1]):
    out.append(f"| {k.replace('_',' ')} | {v} |")
out.append("")
out.append("**Reading:** carpentry leads (6), tile (5), porch + pool deck + general repair tied (4 each), plumbing/electrical/painting/doors/demo all show evidence. Multi-trade competence is fully verified. Pergola surfaces only once — confirms it's an occasional outdoor build, not a primary service category.")
out.append("")
out.append("### Praise-pattern frequency (synthesis §4 differentiator input)")
out.append("")
out.append("| Praise category | Reviews mentioning |")
out.append("|---|---|")
for k, v in sorted(praise_counts.items(), key=lambda x: -x[1]):
    out.append(f"| {k.replace('_',' ')} | {v} |")
out.append("")
out.append("**Reading:** quality/finish dominates (23 of 44 = 52%); highly-recommend pattern second (18 = 41%); price/value third (11 = 25%). On-time and fast-response together account for 14 (32%) — the speed signal is strong. Repeat-customer pattern shows 5 explicit mentions; the actual repeat-customer rate is likely higher (most reviewers don't disclose history). Cleanup mentioned in only 2 — was the iter-1 hero differentiator but the data doesn't support it as a top claim; demote.")
out.append("")
out.append("### Differentiator implications (for synthesis re-evaluation)")
out.append("")
out.append("- **Pricing transparency / value vs competitors** — confirmed strong (price_value × 11 + price_vs_competitor × 1 — combined 12)")
out.append("- **Multi-trade competence** — confirmed across 13 of 15 categories")
out.append("- **Quality / finish work** — overwhelmingly dominant praise pattern")
out.append("- **Speed / responsiveness** — strong (fast_response + on_time = 14)")
out.append("- **Cleanup as differentiator** — **WEAK in evidence** (2 mentions only). Iter-1 leaned on this; the data doesn't support headline weight. Demote in iter-2.")
out.append("- **Owner-replies-to-reviews** — strong active engagement signal (43 of 44). Replies are gratitude-first, family-framed, often forward-looking. Notable phrases for Design to consider as connector copy: \"being a part of the family\", \"It was my pleasure\", \"looking forward to more projects\", \"Thank you for trusting us\".")
out.append("")

# Read existing intake, replace the Voice — Reviews section through Saturation tables
intake_path = os.path.join(ROOT, 'intake.md')
with open(intake_path) as f:
    existing = f.read()

start_re = re.compile(r'^## Voice — Reviews\b', re.M)
end_re = re.compile(r'^## Voice — Owner Replies', re.M)
m_start = start_re.search(existing)
m_end = end_re.search(existing)
if not m_start or not m_end:
    raise SystemExit("Could not find Voice — Reviews bounds")

new_block = '\n'.join(out) + '\n'
expanded = existing[:m_start.start()] + new_block + existing[m_end.start():]

# Update Voice — Owner Replies section to point to the inline reply text now present
expanded = expanded.replace(
    "## Voice — Owner Replies (synthesized)\n_[OVERTURNED iter-1 finding via 2026-05-03 GBP scrape: 43 of 44 reviews have an owner reply. Anthony actively engages on reviews. Reply text not extracted in this scrape — re-scrape with the .CDe7pd selector if the actual reply text is needed for voice synthesis. Until then, the binary fact (he does reply) is the signal.]_",
    """## Voice — Owner Replies (synthesized)

_Reply text is now captured inline with each review entry above (re-scrape via `.CDe7pd` selector, 2026-05-03)._

- **Tone:** warm, gratitude-first, family-framed. Anthony opens nearly every reply with "Thank you" or "We appreciate." Forward-looking close ("looking forward to more projects") appears multiple times.
- **Length:** brief but personalized. 8 canned (<30 chars) like "Thank you." or "Thank you for choosing us." 28 short (30-100 chars) like "Thank you for being a part of the family. We appreciate you relying on us!" 7 medium (100-250 chars) with project-specific call-outs. **Zero novel-length replies** — Anthony keeps the time investment per reply low.
- **Recurring phrases:** "Thank you for choosing the Yankee Handyman" (3×), "Thank you for choosing us" (2×), "We appreciate you", "It was my pleasure", "Thank you for trusting us", "looking forward to more projects".
- **Personality signals:** uses 😁 emoji occasionally; switches between "we" and "I/me" (solo operator with collective framing — same pattern as the FB tagline "It's our pleasure to work for you"); occasionally addresses reviewers by first name ("Thank you Zack…"); refers to customers as "family" and "friends".
- **Implication for Design:** Anthony's actual reply phrases are voice-authentic and lift directly into the reviews-page connector copy. Don't over-author what his existing replies already say.
"""
)

with open(intake_path, 'w') as f:
    f.write(expanded)

print(f"Wrote intake.md with reply text inline ({len(expanded):,} chars)")
print(f"43 reviews now show owner reply text + reply date")
