# Synthesis — Yankee Handyman LLC

> Output of the synthesis layer for prospect Yankee Handyman LLC (Ocala, FL). Consumed by CONTENT-INVENTORY directly.
>
> **Note on contract conformance:** captured `intake.md` predates the v2.0 intake template. This synthesis runs against what was captured (Path C), with every v2.0-contract block documented inline as `[v2.0-delta]` so the script-design session has a clean diff between captured-intake-shape and contract-required-intake-shape. None of the deltas blocked synthesis here, but several would have under strict v2.0 reading. Listed in §0.

## 0. Provenance

- Intake spec captured against: pre-v2.0 ("legacy") shape
- Intake capture date: 2026-05-03
- Synthesis date: 2026-05-03
- Synthesized by: Design (Claude)
- Stakeholder soft-passes acknowledged: photo-shortfall (10 photos total, library fixed); email; license/insurance verification; FB post cadence
- v2.0 contract deltas (synthesized through, flagged for script):
  - **CTA recommendation** — strict v2.0 blocks pending §7 phone-answering capture. Soft-pass: synthesized as `call-primary` based on review evidence ("the same day I called," "extremely reasonable price") and operator pattern (no website, FB Messenger likely). Confidence: high. Risk if wrong: medium.
  - **Service-area copy** — strict v2.0 blocks pending structured city/county/zip/radius. Soft-pass: synthesized from intake's inferred "Marion County / Ocala / Bellechase" with no zip enumeration. Confidence: medium. Risk if wrong: low (operator can correct in walkthrough).
  - **Differentiator paragraph** — strict v2.0 blocks pending §12 competitor set (≥2 captured). Soft-pass: synthesized differentiators against an *implicit* category baseline ("contractors who don't clean up; plumbers charging $350-$500"), citing review evidence. Confidence: medium-high — review language explicitly invokes competitor comparisons, which is unusually strong for an implicit baseline. Risk if wrong: low — claims are review-cited not Design-invented.
  - **Job-noun frequency counts** — captured intake gives flat list, not `[noun, count]` pairs. Synthesized §3 services list orders by *cited review count* I can derive (1 review = 1 count) which is a weak proxy. Counts noted inline.
  - **Photo subject/usability tags** — Ron explicitly deferred to Design. Tagged in §10 below; tags are Design's call, marked `[design-tagged]` so they're distinguishable from operator-confirmed.
  - **Owner-reply register shifts** — captured intake confirms the absence of replies across all 10 captured reviews. This is signal, not gap; treated as a voice-guide input in §2.
  - **Vernacular color evidence** — not separately captured; I'll extract from logo + photos in §7 below.

## 1. Tagline (committed)

- **Tagline:** **Creating Beautiful Spaces and Smiling Faces.**
- **Cites:** intake §Voice — Bio (FB tagline, verbatim — operator's own line); intake §Differentiator 3 (cleans up after the job — supports the "Beautiful Spaces" half); intake §Voice — Reviews customer language clusters around "above and beyond," "honest & reliable" (supports the "Smiling Faces" half).
- **Reasoning:** The operator already wrote a strong tagline. Per `synthesis.md` §4 ("synthesis does not invent evidence"), the right move is commit the operator's line and reject the temptation to "improve" it. Two of the three FB-tagline candidate lines are kept ("Creating Beautiful Spaces and Smiling Faces" as the primary; "No job too big or small" demoted to a sub-line in §8 hero stack). The middle line ("It's our pleasure to work for you") is rejected.
- **Rejected alternates:**
  - *"It's our pleasure to work for you."* — Too service-script-y for a tagline; lands with weight only after a transaction. Better as a closing line elsewhere or cut entirely.
  - *"No job too big or small."* — Operationally true (the multi-trade evidence supports it) but it's a category cliché. Demoted from tagline to hero supporting line.
  - *Synthesized alternates from review language* (e.g. "Honest, Reliable, Reasonable") — rejected because the operator's own line outperforms invented copy on register and ownership.

## 2. Voice guide

- **Sentence-level register:** Warm, plainspoken, hospitality-leaning. The owner's own register (FB tagline) is more service-warm than craft-proud; the customer review register is the inverse, leaning into competence and value. The site speaks in the **owner's voice** but inherits *evidence* from customers — meaning the site says "we clean up after ourselves" warmly, and lets a customer quote say "that's not usually the case with contractors" pointedly. Do not collapse these into one register.
- **Words to use:**
  - From operator (FB): *pleasure, beautiful, smiling, no job too big or small*
  - From customers (intake §Voice — Reviews, verbatim): *fair price, above and beyond, honest & reliable, same day, dynamic duo, cleaned up after himself, took pity on me, squeezed me in, recommend him 100%, did not disappoint, extremely reasonable, will use again, won't be disappointed, finished, really cares*
- **Words to avoid:**
  - *Premium, luxury, bespoke, craftsman* — operator's price positioning ($125 service-call) makes these dishonest.
  - *Family-owned, veteran-owned, since [year]* — none evidenced; intake explicitly null on these.
  - *Emergency, 24/7, on-call* — same-day flexibility is documented; 24/7 is not.
  - *General contractor* — GBP category but reviews never use it; *handyman* is the customer-word.
  - *Trusted, professional, reliable* (alone) — generic; the site has stronger evidence-grounded language available, use that instead.
- **Register shifts the site must perform:**
  - **No reply-register evidence.** The owner does not reply to Google reviews (intake §Voice — Owner Replies). This is a real signal: the site cannot lean on conversational owner-voice the way it could for an operator who replies to every review. **Implication:** the site's owner-voice surface is small (tagline, About, contact framing). Customer voice surfaces (review excerpts, captioned proof) carry more weight than they would otherwise.
  - **One register shift required:** when copy describes pricing, the register firms up. The $125 flat fee is *the* hook; it should be stated plainly with no softening adjectives, in the operator's voice. Elsewhere copy can stay warm.
- **Reading level target:** Grade 7. Customer reviews average ~grade 6-8; operator's tagline is grade 5; site copy should sit in the band.

## 3. Services (committed)

> Order = approximate frequency in captured reviews (1 review = 1 count). Real `[noun, count]` pairs require re-mining once 40 uncaptured reviews are captured; this list will likely re-order at that pass.

- **Primary services list:**
  1. **General handyman work** — multi-trade, all sizes (review 4: "20+ projects" / review 5: "several years")
  2. **Plumbing** — garbage disposal install, fixture work (review 1)
  3. **Electrical** — new circuit installation, lighting / chandelier hanging (review 3)
  4. **Carpentry & framing** — porch enclosures, interior walls, finish carpentry (reviews 2, 6)
  5. **Tile** — re-tiling rooms (review 2)
  6. **Pool deck construction** — finish-carpentry-grade (review 6)
  7. **Interior painting** — (review 7)
- **Demoted from GBP categories:**
  - *General Contractor* (GBP primary) — kept as evidence in trust block but not used as a service label; "handyman" is the customer-word and the brand-word.
  - *Service / point_of_interest / establishment* (GBP secondary) — Google catch-alls, no signal.
- **Promoted despite low evidence:** none. Every service above has at least one cited review.
- **Risk note:** the services list will look thin compared to the multi-trade reality. The "General handyman work" lead is doing real work — it's the umbrella that covers the long tail. Resist the temptation to expand to a 15-line itemized services list; the umbrella + 6 named depths is the right shape.

## 4. Trust block

- **Headline number:** **50 reviews · 4.9 stars on Google**
- **Years in business:** *Omitted.* LLC formed 2022 (~3 years), below the ≥10-year threshold per intake spec §1. Reviews note "several years" with one customer; that's evidence enough that the operator predates the LLC, but a "since 2022" or "since 20XX" line on the site under-sells reality without strengthening it. Cut.
- **Licensing line:** **`[gap: blocking-on-walkthrough]`** — site cannot make a licensing claim without verification at myfloridalicense.com. Two acceptable site treatments: (a) say nothing about licensing; (b) say "Licensed and insured" only after operator confirms in walkthrough. Default to (a) at first build; flip to (b) if walkthrough confirms.
- **Social-proof excerpts:** three short quotes, chosen for variety of job type. Cite review numbers.
  1. **"He took pity on me and squeezed me in at the end of his day. He did a great job and his price was phenomenal."** — Cheryl Mulhern (review 1, plumbing)
  2. **"Anthony is amazing. He goes above and beyond in every job he does, he has done probably over 20 projects for me."** — Andrew Abad (review 4, repeat customer)
  3. **"High quality work, professional, showed up on time, and him and his team worked together as a dynamic duo."** — Molly Groves (review 3, electrical)
- **Bellechase HOA vouching:** treated as a *secondary* trust signal — strong but not for the headline. One sentence in the trust block: *"Recommended by the Bellechase homeowners group."* (cites review 1 verbatim phrasing).

## 5. CTA commitment

- **Primary CTA:** **call**
- **Phone treatment:** **prominent** (top-right header, bottom of every section, sticky on mobile)
- **Form treatment:** **secondary** (a short "Send a message" form on Contact section only; pre-filled subject "Quote request"; honest about response time being phone-faster)
- **Reasoning:** Intake §Location & Contact confirms phone is the booking method ("the same day I called"). No website, no booking flow exists. Customer reviews repeatedly mention same-day phone response. Form is included as a secondary option for users who genuinely prefer text-first contact, but the site's UX gravity points to the phone number. Email is `[gap]` at intake; not surfaced as a contact method until captured.
- **`[v2.0-delta]`:** Strict v2.0 blocks here pending §7 phone-answering capture. Soft-pass justified by review-evidence weight; flag for walkthrough validation.

## 6. Service-area copy

- **Primary phrasing:** **"Serving Ocala and Marion County."**
- **Cities-listed treatment:** **county-only** (no enumerated cities; the only neighborhood explicitly named in evidence is Bellechase, which is a community within Ocala, not a separate city)
- **Out-of-scope handling:** No on-site copy needed. The site's call-CTA model means out-of-area inquiries get filtered at phone-answer time, not at form-submit time. If a form is added to Contact, no service-area validation field — keep the form open.
- **`[v2.0-delta]`:** Strict v2.0 blocks pending structured cities/zips/radius. Soft-pass justified — county-only phrasing is honest about evidence we have. Flag for walkthrough confirmation; if Anthony confirms a wider radius (e.g. into Sumter or Lake counties), copy expands.

## 7. Visual identity commitment

> **Branch:** A (logo present, raster) → palette extracted from logo + photos.

- **Logo:** Use `logo/logo.jpg` from intake (FB profile picture, 35,021 bytes JPEG). Quality: raster — usable at small/medium sizes (header, footer, favicon). For hero placement or print, a vectorization pass is needed; flag in walkthrough.
- **Vernacular color evidence (extracted at synthesis time, since not captured separately):**
  - **From logo:** [pending visual extraction — Design will run k-means on the saved logo file in CONTENT-INVENTORY layer; this synthesis commits to "use logo as palette source" without inventing hex values.]
  - **From photos:** any branded vehicle, uniform, or signage in the 10 GBP photos contributes a constraint. Flagged for visual review at next pass.
  - **Constraint summary (provisional):** the brand name "Yankee Handyman" carries red/white/blue connotation in American visual vernacular; if the logo confirms that direction, the palette commits to it. If the logo goes a different direction, the logo wins — do not let the brand name override the operator's actual visual identity.
- **Typography commitment:** deferred to CONTENT-INVENTORY. This synthesis commits only to "warm/hospitality" register supporting voice §2 — meaning a humanist sans for body, with a slightly hand-warm display option if the logo supports it. No typography hex commitments here.

## 8. Hero composition

- **Hero photo:** **TBD from 10-photo library** — `[design-tagged]` after photo review (next sub-step). Strong hero candidates given subject hints from intake: `09-gbp-customer-diane-bennett.jpg` (pool deck — finish carpentry visible, customer-uploaded) or `10-gbp-customer-cole-spires.jpg` (porch enclosure / interior wall). The customer-uploaded photos likely outperform owner-uploaded for hero use because: (a) customer photos cross-reference review text directly, and (b) owner-uploaded contractor photos tend toward project-mid-progress shots that need explanation.
- **Hero copy stack:**
  1. **Tagline (committed):** "Creating Beautiful Spaces and Smiling Faces."
  2. **Supporting line:** "No job too big or small." (demoted from tagline candidates per §1)
  3. **Trust line:** "50 reviews · 4.9 stars on Google" (from §4)
  4. **CTA:** large phone number with click-to-call, per §5.
- **Cites:** intake §Voice — Bio (FB tagline), §Photos (10-photo library), §Trust Signals.

## 9. Section sequence

> **Photo-shortfall acknowledged.** 10 photos total, untagged. Stakeholder ack: "Library is what it is." Section count reduced to fit; some sections may go imageless or use customer-quote tiles instead of photos.

Provisional section sequence (subject to photo-tagging confirmation):

1. **Hero** — see §8.
2. **Trades / Services** — list-led; the seven services from §3 with one-line plain descriptions. Photo: optional tile of in-progress work if any of the 8 owner-uploaded photos depicts active multi-trade scope. If not, no image — list density is fine.
3. **Proof — what customers say** — three review excerpts from §4 + one short paragraph naming the Bellechase HOA vouching. Photo: customer-uploaded photo (one of `09-` or `10-`) used as supporting tile.
4. **Pool decks & carpentry** — one focused section for the finish-carpentry hook (Diane Bennett's pool deck is the clearest "this is more than handyman" evidence). Photo: `09-gbp-customer-diane-bennett.jpg`. Body: short paragraph + Diane's review excerpt. This section earns its own slot because the pool-deck evidence is the operator's strongest portfolio claim and gets buried inside a generic services list otherwise.
5. **About Anthony** — short. Operator's voice. Two paragraphs at most. Mention the team-of-two ("dynamic duo" from review 3) without naming the second person (no evidence base). Mention years in Ocala obliquely ("years working in and around Ocala") without committing to a number. Photo: an owner-uploaded photo if any depict Anthony directly, else no photo (cropped tool/job detail tile is acceptable; do not invent an "Anthony portrait").
6. **Contact** — phone-prominent per §5. Address (6726 Cherry Rd, Ocala). Hours table from intake. Form secondary.

**Sections explicitly cut:**
- "Why choose us" / generic value-prop section — replaced by Trades + Proof working together.
- "Service area map" — county-only phrasing per §6 doesn't earn a map.
- "Areas we serve" enumerated list — same reason.
- "Awards / certifications" — none evidenced.
- Blog / news / project journal — out of scope; no content base.

## 10. Proof grid

- **Photo count committed:** **6** (subject to tagging — see below)
- **Photos:** ordered selection from the 10-photo library after `[design-tagged]` pass. Provisional ordering by intake filename hint: `09-gbp-customer-diane-bennett.jpg`, `10-gbp-customer-cole-spires.jpg`, then four of the 8 owner-uploaded based on subject quality.
- **Caption strategy:** **quoted-from-review** for the two customer-uploaded photos (pair each with its source reviewer's quote — Diane → review 6 excerpt; Cole → review 2 excerpt). For the four owner-uploaded photos, captions are short job-noun labels (e.g. "Interior tile," "New circuit + chandelier," "Porch enclosure") — not quotes, because the photos can't be cross-referenced to a specific reviewer's words.
- **Photo-tagging note (`[design-tagged]`):** tagging deferred to image-review sub-step inside CONTENT-INVENTORY. If fewer than 6 photos pass the `proof-grid` usability bar, grid contracts to 4 with no apology — better fewer good photos than a padded grid.

## 11. Differentiator paragraph

> ≤80 words. Cites §13 evidence bullets and *implicit* §12 competitor baseline (per `[v2.0-delta]` soft-pass).

**Committed copy:**

*"Anthony Porett runs a small operation out of Ocala — usually him and one other. He'll quote a small job for what other contractors charge for the estimate alone, finish it the same day if he can, and clean up before he leaves. Fifty Marion County customers have rated him 4.9 stars across plumbing, electrical, carpentry, tile, and pool deck work. The Bellechase homeowners group, which only adds the contractors they trust, recommends him."*

- **Word count:** 76.
- **Cites:** intake §Identity (Anthony Porett, Ocala, team-of-two from review 3); intake §Differentiator 1 ($125 vs $350-$500); intake §Differentiator 4 (same-day); intake §Differentiator 3 (cleans up); intake §Trust Signals (50 reviews, 4.9); intake §Categories & Services; intake §Voice — Reviews (review 1 Bellechase verbatim).
- **Implicit competitor baseline:** *"other contractors who charge for the estimate"* / *"plumbers quoting $350-$500"* — both review-evidenced, not Design-invented. Strict v2.0 would still block on §12 capture; documented.

## 12. Seasonality hook

- **Decision:** **absent**
- **Reasoning:** Captured review dates span July 2025 through May 2026 — 10 months. The set is too small to derive seasonality (10 reviews ≠ 10 monthly buckets), and the spread doesn't cluster suggestively. Intake §8-equivalent seasonality field not separately captured. **Soft-pass:** decline to commit a seasonality hook on first build; revisit at next intake pass when 40 more reviews are captured.

## 13. Open commitments index

> Flat list of every committed copy line in this synthesis, with intake citation. CONTENT-INVENTORY diffs against this index.

| # | Section | Copy committed | Intake citation |
|---|---|---|---|
| 1 | Tagline | "Creating Beautiful Spaces and Smiling Faces." | §Voice — Bio (FB tagline) |
| 2 | Hero supporting line | "No job too big or small." | §Voice — Bio (FB tagline) |
| 3 | Hero trust line | "50 reviews · 4.9 stars on Google" | §Trust Signals |
| 4 | Services list | General handyman; Plumbing; Electrical; Carpentry & framing; Tile; Pool deck construction; Interior painting | §Categories & Services (review-mined) |
| 5 | Trust headline | "50 reviews · 4.9 stars on Google" | §Trust Signals |
| 6 | Trust quote 1 | Cheryl Mulhern excerpt (plumbing) | §Voice — Review 1 |
| 7 | Trust quote 2 | Andrew Abad excerpt (repeat customer) | §Voice — Review 4 |
| 8 | Trust quote 3 | Molly Groves excerpt (electrical) | §Voice — Review 3 |
| 9 | Trust secondary | "Recommended by the Bellechase homeowners group." | §Voice — Review 1 verbatim |
| 10 | Service area | "Serving Ocala and Marion County." | §Location & Contact |
| 11 | Differentiator paragraph | (see §11 above) | composite — see §11 cites |
| 12 | Pool-deck section caption | Diane Bennett review 6 excerpt | §Voice — Review 6 |
| 13 | Porch/tile section caption | Cole Spires review 2 excerpt | §Voice — Review 2 |
| 14 | Hours table | M-F 8-5, Sat 9-5, Sun closed | §Hours & Availability |
| 15 | Address | 6726 Cherry Rd, Ocala, FL 34472 | §Location & Contact |
| 16 | Phone | (239) 867-8447 | §Location & Contact |

**Items NOT committed (deferred to CONTENT-INVENTORY or walkthrough):**
- Final hero photo selection (depends on photo subject/usability tagging)
- Final 6 proof-grid photos
- Logo color extraction → palette hex values
- Typography commitments
- License/insurance line (gap pending verification)
- Email (gap)
- IG link (handle unverified)
- "About Anthony" body copy (committed approach in §9 step 5; final words written in CONTENT-INVENTORY)

## Appendix — what this synthesis revealed about the v2.0 contract

> Notes for tonight's audit-script design session.

1. **No-reply operators are common enough to need first-class handling.** Anthony doesn't reply to Google reviews. Per the v2.0 contract, this looked like a `[gap]` in §4a *Owner language* and `[gap]` in §4a *Tone markers — owner*. Strict reading would have blocked synthesis on voice guide. But the *absence of replies is itself the signal* — and the v2.0 contract has no field for it. **Recommended addition to v2.0:** a §4a sub-field `Owner reply behavior: replies-to-all | replies-selectively | does-not-reply | unknown`, with the latter three each carrying voice-guide implications. Without this field, every no-reply operator generates a phantom block.

2. **Customer-uploaded photos deserve their own tag.** Intake distinguished owner-uploaded vs customer-uploaded; v2.0 §10 didn't promote this to a tag. Customer-uploaded photos cross-reference reviews directly and are dramatically more useful for hero/proof use than owner-uploaded contractor mid-progress shots. **Recommended addition to v2.0 §10:** a third axis `provenance: owner-uploaded | customer-uploaded | both-attribution-known`, alongside subject and usability.

3. **The "soft-pass on phone-answering" is going to recur.** Calling a prospect to test phone-answering is friction the manual capture pass tends to skip, and synthesis will repeatedly hit `[gap: blocking]` here. Two options: (a) make the phone-test the first manual step (cheap, 30 seconds, anchors everything else); (b) make it script-driven during the audit run (script reminds the human to call, captures the result inline). Both work; (b) is more reliable. Tonight's script should bake this in.

4. **Implicit competitor baseline is sometimes review-evidenced.** Review 1 says "I had contacted a few plumbers who quoted me $350-$500." That's a *customer-volunteered* competitor reference, which is stronger evidence than any §12 competitor capture would yield. The v2.0 contract treats §12 as a synthesis prerequisite; in practice, reviews sometimes do that work for free. **Recommended refinement to v2.0:** synthesis §11 differentiator-paragraph block can be lifted if customer-review language explicitly invokes a competitor comparison ≥2 times. Audit script should detect and flag these.

5. **The captured-intake → contract delta is the real artifact for the script.** This synthesis flagged 5 v2.0-deltas inline. Tonight's script-design session should walk those deltas as the test set: for each delta, decide whether v2.0 is wrong (the intake correctly captured something v2.0 doesn't model) or whether the capture is wrong (the intake skipped something v2.0 needs). My read: 1 and 2 above are v2.0-wrong; 3 is capture-wrong (need to add the prompt); 4 is a refinement, not a fix; 5 is the meta-pattern.
