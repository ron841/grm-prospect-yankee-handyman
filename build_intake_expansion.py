"""Replace the Voice — Reviews section in intake.md with the saturation-driven
expanded set. Preserve everything else."""

import json, os, re

ROOT = os.path.expanduser('~/grm-sites-prospects/yankee-handyman')

with open(os.path.join(ROOT, 'audit/reviews-deduped.json')) as f:
    reviews = json.load(f)
with open(os.path.join(ROOT, 'audit/saturation-summary.json')) as f:
    sat = json.load(f)

# Build the new "Voice — Reviews" section block
out = []
out.append("## Voice — Reviews")
out.append("")
out.append(f"> **Capture method, iteration 2:** Scraped via Playwright DOM extraction against the Google Maps reviews panel (~25 scroll-load cycles to fully load the side panel). Pulled **44 reviews with body text** out of 50 total — the 6 missing are 5-star ratings with no body, which the saturation rule treats as zero-evidence-add and skips.")
out.append("")
out.append(f"> **Saturation status (per audit-script-implications.md #5):** **REACHED.** Distinct job-nouns plateau at review #{sat['job_noun_saturation_at_review']}/{sat['unique_after_dedup']} ({sat['distinct_job_nouns']} of 15 categories matched). Distinct praise-patterns plateau at #{sat['praise_pattern_saturation_at_review']}/{sat['unique_after_dedup']} ({sat['distinct_praise_patterns']} of 14 categories matched). Both fully saturated by review #{sat['both_saturated_at_review']}; remaining 3 reviews are confirmation-not-discovery. **Birdeye and Yelp not pulled** per the locked rule — additional captures would not surface new job-nouns or new praise-patterns. Birdeye listing confirms the same 50 reviews with 4.9 rating, all sourced from Google.")
out.append("")
out.append(f"> **Owner-reply evidence (overturns iter-1 finding):** **43 of 44 reviews have an owner reply.** The iter-1 audit had concluded Anthony does not reply to reviews — that was wrong; the API's 5 returned reviews simply happened to truncate the reply field. Manual review of the scrape confirms Anthony replies to nearly every review.")
out.append("")
out.append(f"> **Star distribution:** {sat['star_distribution'].get('5','0')} × 5-star, {sat['star_distribution'].get('1','0')} × 1-star. The single 1-star is from author 'DM _' on Apr 12, 2024 (Birdeye reports this as the lowest-rated review). Captured below at its index.")
out.append("")

# Render each review
for i, r in enumerate(reviews, 1):
    name = r.get('name', '?')
    stars = r.get('stars', '?')
    body = (r.get('body') or '').strip()
    has_reply = r.get('has_reply', False)
    out.append(f"### Review {i} _[GBP scrape, 2026-05-03]_")
    out.append(f"- Stars: {stars}")
    out.append(f"- Date: _[gap — Google Maps date class returned whitespace; available via re-scrape if needed]_")
    out.append(f"- Reviewer: {name}")
    out.append(f"- Text: \"{body}\"")
    out.append(f"- Owner reply: {'present (text not extracted in this scrape)' if has_reply else 'none visible'}")
    out.append("")

# Append the saturation tables
out.append("## Voice — Saturation tables")
out.append("")
out.append("> Generated from the 44-review GBP scrape. Frequency = number of reviews matching the regex pattern for that category.")
out.append("")
out.append("### Job-noun frequency (synthesis §3 input)")
out.append("")
out.append("| Job category | Reviews mentioning |")
out.append("|---|---|")
for k, v in sat['job_noun_frequency'].items():
    out.append(f"| {k.replace('_',' ')} | {v} |")
out.append("")
out.append("**Reading:** carpentry leads (6), tile (5), porch + pool deck + general repair tied (4 each), plumbing/electrical/painting/doors/demo all show evidence. Multi-trade competence is fully verified. Pergola surfaces only once — confirms it's an occasional outdoor build, not a primary service category.")
out.append("")
out.append("### Praise-pattern frequency (synthesis §4 differentiator input)")
out.append("")
out.append("| Praise category | Reviews mentioning |")
out.append("|---|---|")
for k, v in sat['praise_pattern_frequency'].items():
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
out.append("- **Owner-replies-to-reviews** — strong active engagement signal (43 of 44). Adds trust pattern not surfaced in iter-1.")
out.append("")

# Read the existing intake.md
intake_path = os.path.join(ROOT, 'intake.md')
with open(intake_path) as f:
    existing = f.read()

# Find the Voice — Reviews section start and the next major section
start_re = re.compile(r'^## Voice — Reviews\b', re.M)
end_re = re.compile(r'^## Voice — Owner Replies', re.M)
m_start = start_re.search(existing)
m_end = end_re.search(existing)
if not m_start or not m_end:
    raise SystemExit(f"Could not locate Voice — Reviews section bounds (start={bool(m_start)} end={bool(m_end)})")

new_block = '\n'.join(out) + '\n'
expanded = existing[:m_start.start()] + new_block + existing[m_end.start():]

# Also update the trust-signal review count from 50 to 50 (no change) and tag it as confirmed
# Update Owner Replies section to reflect new evidence
expanded = expanded.replace(
    "## Voice — Owner Replies (synthesized)\n_[gap — API returned no owner replies for the 5 visible reviews. Either Anthony does not reply to reviews, or the API's relevance ranking happened to surface 5 unreplied ones. Manual capture of the other 45 needed to confirm whether Anthony replies to reviews at all. None of the recent-capture excerpts noted a reply either, but reply-presence wasn't explicitly checked.]_",
    "## Voice — Owner Replies (synthesized)\n_[OVERTURNED iter-1 finding via 2026-05-03 GBP scrape: 43 of 44 reviews have an owner reply. Anthony actively engages on reviews. Reply text not extracted in this scrape — re-scrape with the .CDe7pd selector if the actual reply text is needed for voice synthesis. Until then, the binary fact (he does reply) is the signal.]_"
)

with open(intake_path, 'w') as f:
    f.write(expanded)

print(f"Wrote expanded intake.md ({len(expanded):,} chars)")
print(f"Inserted {len(reviews)} reviews + saturation tables in place of the 5 API + 5 manual reviews from iter-1")
