# Audit-script implications of intake.md v2.0

Read this alongside the template. These are the fields where the naive read ("scrape it") will mislead you tonight.

## Fields that look easy but are hard to scrape

- **Facebook last-post date and cadence** — FB aggressively rate-limits and serves different DOM to logged-out crawlers. Playwright works for ~10 minutes per IP before throttling. **Implication:** budget a real auth session per scrape run, or accept ~30% silent failure rate and let the script flag `[scrape-failed]` rather than `[gap]`. Those are different signals.
- **Instagram grid coherence** — DOM-readable but the *judgment* is what matters. Script can pull last 12 posts; classifying them as `tight | loose | chaotic` is `[human]`. Don't try to automate the verdict; automate the *evidence collection* that feeds the verdict.
- **Email from FB About** — the field exists in the DOM but FB obfuscates it as an image for ~40% of business pages. Pulling it requires OCR. Not worth it for v1; tag `[human]` and move on.
- **Owner first/last name** — Places API gives "owner" only when the owner has explicitly claimed the listing AND made the name public. Don't assume the field is there; the script should fall back gracefully to `[gap]`.
- **Review count beyond 5** — Places API hard-caps at 5. Scraping the GBP panel for the rest is doable but the DOM changes monthly. **Implication:** the audit script should not promise "all 45 reviews" — it should promise "5 from API + best-effort scrape of the rest, with explicit count of what was retrieved." The §4b capture target (top 12 + specific-job shorts) means we don't need all 45 anyway, which is convenient.

## Fields where manual judgment is irreducible

Do not let the script try to automate these. Have it output a structured prompt for the human instead.

- **§1 Tagline** — synthesis, not extraction. Script should refuse to autofill.
- **§4a Tone markers** — pattern recognition across paired reviews+replies. LLM can draft, human must approve, and "draft + approve" is slower than "capture cold" if the draft is bad. **Implication:** for v1 audit script, generate a tone-marker draft only if confidence ≥ some threshold (e.g. ≥8 paired reviews available), else leave blank. A bad draft anchors the human worse than no draft.
- **§4a Register shifts** — requires reading replies *as a sequence*. LLM can do this but the failure mode is generic ("warm and professional") which is worse than nothing. Same threshold gate as tone markers.
- **§7 Phone-answering behavior** — fundamentally requires placing a call. No automation path. Build the field, build the prompt, accept the manual step.
- **§11b Vernacular color evidence** — color extraction from photos is a solved problem (k-means on pixels), but **which photos to extract from** is the judgment. Script should propose; human confirms.
- **§13 Differentiators** — by definition this is a comparison against §12 competitors. Script can surface candidate bullets but the "vs. what" is human.

## Fields where partial automation is worse than none

These are the traps. Better to leave blank with a clear `[human]` tag than to half-fill.

- **§2 Service-area geography** — pulling cities from review author locations gives you *where customers live*, not *where the operator works*. Those overlap but aren't the same. A script that fills "cities served" from review metadata will be confidently wrong. **Don't.** Leave `[human]`.
- **§3 Response-time signal** — keyword-matching reviews for "fast" / "quick" / "same day" gives you a count, not a signal. The signal is whether response-speed is a *recurring positive*. Script outputs the count as evidence; human writes the sentence. Do not have the script write the sentence.
- **§5 Services list** — *only* derive from §4a recurring job nouns. If the script falls back to "use GBP categories when reviews are sparse," it will produce a generic services list that contradicts the review-mining principle. Better to output a `[gap: insufficient review evidence for services]` flag and force the human to either capture more reviews or accept the gap.
- **§8 Seasonality** — review-date histogram is genuinely `[derived]` and safe. Owner-stated season patterns from FB posts is **not** safe — keyword matching "summer" or "season" in posts will misfire on holiday greetings. Keep these fields separate; do not collapse them.
- **§10 Photo subject/usability tags** — vision models can guess `owner-on-site` vs. `tool-or-truck` at maybe 70% accuracy. That's worse than useless because you'll trust the tags and skip review. Either run vision with a confidence threshold and output uncertain ones as `[human-confirm]`, or skip and leave fully `[human]`. Don't ship 70%-correct tags as if they're done.

## Recommended audit-script output shape

The script should emit a populated `intake.md` with three states per field, not two:

1. **Filled with value** — confident autofill from `[api]`, successful `[scrape]`, or safe `[derived]`.
2. **Filled with `[gap]`** — script attempted and the source genuinely lacks the data.
3. **Filled with `[scrape-failed]` or `[low-confidence]`** — script attempted, technical or semantic failure. Distinct from a real gap; the human should retry, not write copy around the absence.

Conflating 2 and 3 is the most common audit-script bug for this class of work. Don't.

## One forcing-function check

Before shipping the script: take the populated `intake.md` it produces and run it past CONTENT-INVENTORY *as if* it were the final captured spec. Every field CONTENT-INVENTORY reaches for should be either filled or explicitly gap-tagged. If CONTENT-INVENTORY has to ask "is this blank because nothing was captured, or because the script didn't try?" — the script's tagging is wrong, not CONTENT-INVENTORY.

---

## Post-audit findings (added 2026-05-03 from Code's audit pass)

Code ran a Playwright-based audit on the live build and surfaced three things that change the script design:

### 1. FB photos move from `[scrape-failed]` to `[scrape-Playwright]`

Original v2.0 spec tagged FB photos behind login modal as effectively human-only. Code's audit demonstrated that a real headless-Chromium session with DOM extraction past the login wall pulls 9 photos plus a 960×720 cover photo cleanly. **Lift this from "human-only / deferred" to "Playwright-required scrape."** Implication: the script should expect FB photo extraction to succeed, not fail. When it fails, that's a scrape failure not a gap.

### 2. Hero photo selection has a non-obvious dependency

The 10-photo GBP library is what intake captured. Code's audit revealed a stronger asset (FB cover photo, finished pergola) that exists publicly but lives on a different surface. **Implication for the script:** photo capture must hit *all* public photo surfaces (GBP + FB + IG), not just the GBP one we naively defaulted to. The strongest-asset judgment is downstream, but the *evidence collection* must be exhaustive.

### 3. Logo color extraction must run pre-build, not at-build

Provisional brand color set in Home.html during pack-build was navy. K-means against the actual logo at audit time returned brown/sepia, zero blue clusters. The provisional was wrong direction, not just wrong shade. **Implication:** k-means logo extraction is a script-level capture, not a build-level inference. Run it during intake; surface result + confidence to the human; let the synthesis layer reason from a known palette instead of guessing.

### 4. Copy-photo truth violations need a structured check

Code's audit caught the pool-deck section committing to specific evidence ("sanded every edge / curve around the pool") against a mid-construction framing photo. The copy was true to the review; the photo was true to the operator's library; together they told a lie. **Implication:** synthesis-layer or content-inventory-layer should run a copy-photo agreement check — every paragraph that commits to specific physical evidence (sanded, curved, finished, painted) should be checked against the *photo* in the same section, not just the review. Add this to the synthesis QA pass; flag mismatches as `[truth-violation]`.

### 5. Review capture is evidence-saturation, not count-target

The "8-13 reviews is enough" working rule was wrong in principle, not just for high-volume prospects. Anthony has 50 Google reviews at 4.9; the intake captured ~10. That's 20% of his single strongest asset class.

**Capture-side rule (locked):** capture until **evidence saturation** — defined as "marginal next review adds zero new job-nouns and zero new praise-patterns." For a 50-review prospect this is probably 30-40; for a 12-review prospect it's all 12. The number is downstream of evidence state, not upstream of it. The script can compute this live: track distinct job-nouns and distinct praise-pattern clusters as captures accumulate; stop when both plateau.

**Multi-source capture (locked):** Google Places API + Birdeye pagination + Yelp + GBP "all reviews" panel via Playwright + FB recommendations. **Deduplication required**: dedup by author-name + date + first 30 chars of review body. Duplicates across platforms are *confidence boosters* (same review surfacing in multiple places = stronger signal), not separate review entries.

**Architectural implication for high-volume prospects:** when reviews are the strongest asset class for a prospect (review count + rating + specificity all high), the brochure-site default of "3-5 testimonials inline" is wrong. The architectural decision is per-prospect: a dedicated `/reviews` page is warranted when reviews carry primary asset weight. Homepage proof section stays curated-3; the dedicated page surfaces 30+ with three-layer structure (curated leads → grouped by service-type → date-archive). Don't auto-flex for all high-volume prospects; flex when reviews are demonstrably the strongest asset.

**Curation logic for the dedicated reviews page (locked at iteration-2 close):**
- Top: 3-5 curated leads. Repeat-customer language first, named-project-specifics second, service-diversity reviews third.
- Middle: grouped by service type, group-order driven by job-noun frequency from synthesis §3, within-group sort by length.
- Bottom: date-ordered archive of remaining reviews.
- Two rules: (a) specific-job-naming beats generic praise — "fixed the disposal in twenty minutes" > "great service"; (b) reviews mentioning competitors implicitly carry differentiator weight on top of testimonial weight, surface prominently.

**SEO/schema.org weight unlocked:** dedicated reviews page with `Review` JSON-LD entries at volume is rich-results territory; current build's 3 Review entries leaves signal on the table.

**Sales asset unlocked:** "send your next prospect to yankeehandyman.com/reviews" is a tool Anthony can hand out; the page exists for browsing visitors, but doubles as a referral-pitch surface.
