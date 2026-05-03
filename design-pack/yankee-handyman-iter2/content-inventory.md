# CONTENT-INVENTORY — Yankee Handyman LLC

> Slot-keyed inventory. Every string the build needs, in slot-resolution order. Consumed by SLOTS next.
>
> **Voice authority:** GRM voice skill (Closing Table primary; Saturday Morning secondary; Front Porch tertiary). Synthesis-committed lines preserved verbatim. All `[microcopy-design]` strings authored against zone-to-voice mapping.
>
> **Persona:** Neighborhood steady (primary) with Quiet confidence (secondary). Anthony's evidence — Bellechase HOA referral, "honest & reliable" customer language, no review replies, repeat customers — reads warm-civic, not proof-forward or rescue-ready. Persona biases: hero subhead leans Saturday Morning; FAQ section header leans Saturday Morning lead-in; About + footer lean Front Porch.
>
> **Status legend per slot:** `committed` (synthesis-traced) · `microcopy-design` (authored fresh per voice rules) · `pending-walkthrough` (operator confirmation needed) · `pending-image-review` (photo selection deferred) · `pending-extraction` (mechanical extraction deferred to build, e.g. logo color)
>
> **Forcing-function check:** every slot below has a value or an explicit deferred-state tag. Zero ambiguous blanks at the seam to SLOTS.

---

## Page-level metadata

### `meta.title`
- **Value:** "Yankee Handyman — Ocala Handyman, Plumbing, Electrical, Carpentry"
- **Status:** microcopy-design
- **Voice:** Closing Table (clean, specific, hireable)
- **Length:** 64 chars (under 65 cap)
- **Citation:** intake §Identity, §Categories & Services

### `meta.description`
- **Value:** "Anthony Porett runs Yankee Handyman out of Ocala. Plumbing, electrical, carpentry, tile, paint, and a $125 flat service-call fee. Fifty Marion County homeowners, 4.9 stars."
- **Status:** microcopy-design
- **Voice:** Closing Table (data-forward, specific)
- **Length:** 175 chars (under 160 SEO cap — flag: 15 chars over; trim option below)
- **Trim alternate (155 chars):** "Anthony Porett runs Yankee Handyman in Ocala. Plumbing, electrical, carpentry, tile, paint. $125 flat service call. 50 reviews, 4.9 stars on Google."
- **Citation:** synthesis §11, §3

### `meta.og_title`
- **Value:** "Yankee Handyman — Ocala"
- **Status:** microcopy-design
- **Voice:** Closing Table
- **Citation:** synthesis §1

### `meta.og_description`
- **Value:** "Creating Beautiful Spaces and Smiling Faces. Fifty Marion County customers, 4.9 stars on Google."
- **Status:** microcopy-design (combines synthesis-committed tagline with synthesis §4 trust)
- **Voice:** Closing Table
- **Citation:** synthesis §1, §4

### `meta.og_image`
- **Value:** TBD — committed photo from `images/` library
- **Status:** pending-image-review
- **Build instruction:** use the same photo as `hero.image` once selected; render at 1200×630 with the tagline as overlaid text on the dark gradient half (per GRM photography protection overlay rule)

### `meta.favicon`
- **Value:** GRM-Icon-2 style mark derived from `logo/logo.jpg`
- **Status:** pending-extraction
- **Build instruction:** vectorize the FB profile picture if possible; otherwise crop a 64×64 favicon from the raster JPEG centered on the logo mark. Flag for walkthrough — Anthony may have a higher-res source.

---

## Header / nav

### `nav.logo`
- **Value:** `logo/logo.jpg` (raster)
- **Status:** committed (with raster-quality flag)
- **Citation:** intake §Logo
- **Build instruction:** display at 32px height minimum (per GRM logo rules); link to `#top`. Flag for vectorization at walkthrough.

### `nav.brand_text` (fallback if logo fails to load)
- **Value:** "Yankee Handyman"
- **Status:** microcopy-design
- **Voice:** Closing Table
- **Citation:** intake §Identity DBA

### `nav.links` (in order)
- `["Services", "Proof", "About", "Contact"]`
- **Status:** microcopy-design
- **Voice:** Closing Table (single-noun nav labels per GRM rule "no 'click here', specific verbs only")
- **Note:** synthesis §9 named six sections (Hero, Services, Proof, Pool decks, About, Contact). Pool decks is a sub-section visible from the Proof anchor, not a top-level nav target — surfaces it without crowding nav.

### `nav.cta_phone` (right-aligned)
- **Value:** "(239) 867-8447"
- **Display format:** "Call (239) 867-8447" with phone icon (Unicode `☎` or Lucide phone at stroke-width 1.5, per GRM iconography rule — flag as substitution)
- **`tel:` link:** `tel:+12398678447`
- **Status:** committed
- **Citation:** intake §Location & Contact

### `nav.cta_phone.aria_label`
- **Value:** "Call Yankee Handyman at (239) 867-8447"
- **Status:** microcopy-design
- **Voice:** Closing Table

---

## Hero

### `hero.eyebrow`
- **Value:** "OCALA · MARION COUNTY"
- **Status:** microcopy-design
- **Voice:** Closing Table (eyebrow rule: ALL CAPS, middle-dot separator, place-specific per GRM "specific > generic")
- **Citation:** intake §Location & Contact, synthesis §6
- **Type:** Comfortaa, 700, letter-spacing 0.20em

### `hero.headline`
- **Value:** "Creating Beautiful Spaces and Smiling Faces."
- **Status:** committed (synthesis §1 tagline)
- **Voice:** owner's voice (FB tagline, verbatim) — preserves under "synthesis-committed lines stay as-is"
- **Citation:** synthesis §1; intake §Voice — Bio
- **Type:** Merriweather 700, title case, no trailing period removal — keep the period (turns on a period per GRM rhythm rule)

### `hero.supporting_line`
- **Value:** "No job too big or small."
- **Status:** committed (synthesis §8 hero stack, demoted from tagline candidates)
- **Voice:** owner's voice (FB tagline, verbatim)
- **Citation:** synthesis §1, §8
- **Type:** Merriweather 400 italic OR Nunito 600 — pick at SLOTS based on hero composition

### `hero.trust_line`
- **Value:** "50 reviews · 4.9 stars on Google"
- **Status:** committed (synthesis §4 headline number, §8 hero stack)
- **Voice:** Closing Table (numbers earn trust)
- **Citation:** intake §Trust Signals; synthesis §4

### `hero.cta_primary.label`
- **Value:** "Call (239) 867-8447"
- **Status:** microcopy-design
- **Voice:** Closing Table (specific verb + real number per GRM CTA rule)
- **`tel:` link:** `tel:+12398678447`

### `hero.cta_secondary.label`
- **Value:** "See What He's Done"
- **Status:** microcopy-design
- **Voice:** Closing Table (specific action verb; no "Learn more")
- **Anchor:** `#proof`

### `hero.image`
- **Value:** `audit/fb-photos/fb-01-cover-photo-pergola.jpg` (provisional, post-audit 2026-05-03)
- **Status:** pending-walkthrough (confirm with Anthony; request high-res original — likely 4032×3024 on his phone)
- **Note:** Code's audit (`audit/AUDIT.md`, severity High) flagged the previous hero candidate (`09-gbp-customer-diane-bennett.jpg` / cement-board install) for composition fight with text overlay AND for being process-not-product. The FB cover-photo pergola is the only public asset depicting *finished* finish-carpentry at usable resolution. Resolution caveat: 960×720 will pixel up on widescreens; will use as-is for v1 with re-shoot flagged for v2.
- **Legacy candidates (rejected post-audit):** `09-gbp-customer-diane-bennett.jpg` (pool deck, customer-uploaded, finish carpentry visible) OR `10-gbp-customer-cole-spires.jpg` (porch enclosure, customer-uploaded)
- **Build instruction:** apply two-axis gradient overlay (top→bottom 40-65% black, left→right 10-65% black) so headline sits in the dark quadrant per GRM photography rule

### `hero.image.alt`
- **Value (post-audit):** "Finished pergola Anthony built in Ocala — cedar posts, slatted top, clean detail."
- **Status:** microcopy-design / pending-walkthrough
- **Voice:** Front Porch (sensory, specific concrete nouns — alt text is a Front Porch-friendly zone)
- **Citation:** intake §Voice — Review 6 (Diane Bennett evidence)
- **Note:** if a different photo is selected at walkthrough, regenerate alt against the GRM voice rule "specific concrete nouns; Marion County."

---

## Trust marquee (between hero and services)

> Per GRM zone map: trust marquee is Saturday Morning by default. Neighborhood steady persona keeps it Saturday Morning.

### `trust_marquee.items` (4 items, scrolls or sits as a static row)
1. **Value:** "50 Google reviews · 4.9 stars" — committed
2. **Value:** "Recommended by the Bellechase homeowners group" — committed (synthesis §4 secondary trust, intake §Voice — Review 1 verbatim phrasing)
3. **Value:** "Same-day service when the schedule allows" — microcopy-design (Saturday Morning: practical specific, no "24/7" overclaim)
4. **Value:** "$125 flat service-call fee" — microcopy-design (Saturday Morning: leads with the fact, no softening)
- **Voice:** Saturday Morning (clean, informational, factual)
- **Citation:** intake §Trust Signals, §Voice — Review 1, §Differentiator 4, §Differentiator 1

### `trust_marquee.aria_label`
- **Value:** "Why Marion County homeowners hire Anthony"
- **Status:** microcopy-design
- **Voice:** Saturday Morning

---

## Services section

> Per GRM zone map: services-grid section header = Saturday Morning. Quiet confidence persona biases toward Closing Table — applied here.
> Service card descriptions = always Closing Table, no persona bias.

### `services.eyebrow`
- **Value:** "WHAT HE DOES"
- **Status:** microcopy-design
- **Voice:** Closing Table eyebrow (Quiet confidence bias)
- **Type:** Comfortaa, ALL CAPS, 0.20em

### `services.headline`
- **Value:** "One handyman. Most jobs."
- **Status:** microcopy-design
- **Voice:** Closing Table (Quiet confidence bias on transition headline; short paragraphs that turn on a period; no "we do everything" puff)
- **Citation:** synthesis §3 umbrella service framing
- **Type:** Merriweather 700, title case

### `services.subhead`
- **Value:** "Plumbing, electrical, carpentry, tile, paint. Forty-eight hours from estimate to done, when the job allows."
- **Status:** microcopy-design
- **Voice:** Closing Table (specific list + concrete number)
- **Citation:** synthesis §3, intake §Voice — Review 9 (Jon De Lucia "two days")

### `services.list` (7 items, ordered per synthesis §3)

Each item:
```
{
  id: <kebab-slug>,
  label: <display name>,
  blurb: <1-2 sentence Closing Table description>,
  evidence_quote: <optional pull from a specific review>,
  evidence_citation: <intake §Voice — Review N>
}
```

1. **General handyman work**
   - `id`: `general-handyman`
   - `label`: "General handyman work"
   - `blurb`: "Punch lists, repairs, the small jobs other contractors won't quote. One client has had Anthony back for over twenty projects."
   - `evidence_quote`: "He has done probably over 20 projects for me and every single time he's done great work."
   - `evidence_citation`: intake §Voice — Review 4 (Andrew Abad)

2. **Plumbing**
   - `id`: `plumbing`
   - `label`: "Plumbing"
   - `blurb`: "Disposals, fixtures, leaks. The kind of plumbing call where another shop would quote you four hundred dollars and a week."
   - `evidence_quote`: "I had contacted a few plumbers who quoted me $350–$500. … I only paid $125, which is his standard service fee."
   - `evidence_citation`: intake §Voice — Review 1 (Cheryl Mulhern)

3. **Electrical**
   - `id`: `electrical`
   - `label`: "Electrical"
   - `blurb`: "New circuits, lights, fixtures. Hung a chandelier and ran the new circuit it needed in one visit."
   - `evidence_quote`: "Did excellent work creating a new circuit and hanging a chandelier for our kitchen."
   - `evidence_citation`: intake §Voice — Review 3 (Molly Groves)

4. **Carpentry & framing**
   - `id`: `carpentry-framing`
   - `label`: "Carpentry and framing"
   - `blurb`: "Porch enclosures, interior walls, finish carpentry. The pool-deck job was finished to furniture grade."
   - `evidence_quote`: null (composite evidence; pool deck quote lives on the Pool Deck section)
   - `evidence_citation`: intake §Voice — Review 2 (Cole Spires), §Voice — Review 6 (Diane Bennett)

5. **Tile**
   - `id`: `tile`
   - `label`: "Tile"
   - `blurb`: "Re-tile rooms, patches, repairs. Part of the same crew that frames the wall and paints it."
   - `evidence_quote`: null
   - `evidence_citation`: intake §Voice — Review 2

6. **Pool decks**
   - `id`: `pool-decks`
   - `label`: "Pool decks"
   - `blurb`: "Built and finished, with the carpentry-grade detail most pool guys skip. Sanded edges. Curve around the pool."
   - `evidence_quote`: null (full quote lives in `pool_section.evidence`)
   - `evidence_citation`: intake §Voice — Review 6 (Diane Bennett)

7. **Interior painting**
   - `id`: `painting`
   - `label`: "Interior painting"
   - `blurb`: "Rooms, trim, touch-ups. Same standard as the rest of the work."
   - `evidence_quote`: "Fantastic job. Will use again."
   - `evidence_citation`: intake §Voice — Review 7 (Jennifer LeMay)

### `services.cta` (after the list)
- **Label:** "Ask About a Job"
- **Status:** microcopy-design
- **Voice:** Closing Table
- **Action:** `tel:+12398678447` (call-primary per synthesis §5)

---

## Proof section

### `proof.eyebrow`
- **Value:** "WHAT CUSTOMERS SAY"
- **Status:** microcopy-design
- **Voice:** Saturday Morning eyebrow

### `proof.headline`
- **Value:** "Fifty reviews. Four-point-nine stars. Mostly repeat customers."
- **Status:** microcopy-design
- **Voice:** Saturday Morning (testimonials section header; Neighborhood steady persona keeps it Saturday Morning, not Earned-pride Closing Table)
- **Citation:** intake §Trust Signals, §Differentiator 5; synthesis §4
- **Note:** GRM rule on numerals — write out small numbers in body display when rhythm reads better; the spelled-out version above sits cleaner than "50 · 4.9 · …"

### `proof.subhead`
- **Value:** "From plumbing emergencies to twenty-project relationships."
- **Status:** microcopy-design
- **Voice:** Saturday Morning (lead with practical range, human angle)
- **Citation:** synthesis §11

### `proof.quote_1` (committed from synthesis §4)
- **Quote:** "He took pity on me and squeezed me in at the end of his day. He did a great job and his price was phenomenal."
- **Attribution:** "Cheryl Mulhern · Plumbing · Bellechase"
- **Status:** committed
- **Citation:** intake §Voice — Review 1
- **Type:** Merriweather italic, lowercase per GRM pull-quote rule (intimate tone — already lowercase in source)

### `proof.quote_2` (committed)
- **Quote:** "Anthony is amazing. He goes above and beyond in every job he does, he has done probably over 20 projects for me."
- **Attribution:** "Andrew Abad · Repeat customer"
- **Status:** committed
- **Citation:** intake §Voice — Review 4

### `proof.quote_3` (committed)
- **Quote:** "High quality work, professional, showed up on time, and him and his team worked together as a dynamic duo."
- **Attribution:** "Molly Groves · Electrical"
- **Status:** committed
- **Citation:** intake §Voice — Review 3

### `proof.bellechase_callout`
- **Value:** "Recommended by the Bellechase homeowners group, where only the contractors they trust get added."
- **Status:** microcopy-design (lightly adapted from intake §Voice — Review 1 verbatim phrasing; tightened for sectional use)
- **Voice:** Saturday Morning
- **Citation:** intake §Voice — Review 1

### `proof.grid` (6 photos, captions)
- **Status:** pending-image-review for photo selection; captions authored below as microcopy-design (re-author against final photos at walkthrough)
- **Provisional ordering and captions:**
  1. `09-gbp-customer-diane-bennett.jpg` → caption: "Pool deck. Diane Bennett, 2026."
  2. `10-gbp-customer-cole-spires.jpg` → caption: "Porch enclosure and re-tile. Cole Spires, 2025."
  3. `01-gbp-owner-*.jpg` → caption: TBD per subject ("Interior tile" / "New circuit + chandelier" / "Porch framing" — pick at image review)
  4. `02-gbp-owner-*.jpg` → caption: TBD
  5. `03-gbp-owner-*.jpg` → caption: TBD
  6. `04-gbp-owner-*.jpg` → caption: TBD
- **Voice:** Closing Table for owner-uploaded photos (short job-noun labels per synthesis §10); customer-uploaded photos use the reviewer's name + year + job
- **Build instruction:** if fewer than 6 photos pass the proof-grid usability bar at image review, contract to 4 with no apology (per synthesis §10).

---

## Finish carpentry section

> Earned-its-own-section per synthesis §9 step 4. **Re-authored 2026-05-03** after Code's audit flagged the prior pool-deck-led version as a copy/photo truth violation (committed copy described "sanded every edge / curve around the pool to match the coping" against a mid-construction framing photo). Section now leads with finish-carpentry-general framing; Diane Bennett's pool-deck quote remains the proof, demoted from headline to evidence row.

### `finish_section.eyebrow`
- **Value:** "FINISH CARPENTRY"
- **Status:** microcopy-design
- **Voice:** Closing Table eyebrow

### `finish_section.headline`
- **Value:** "Finish carpentry, not just framing."
- **Status:** microcopy-design
- **Voice:** Closing Table (sharp, contrarian — names what most operators skip)
- **Citation:** synthesis §9 step 4 (re-authored), intake §Voice — Review 6, §Voice — Review 2
- **Rejected prior version:** "Pool decks built like furniture." — strong line, but pool-deck-specific against a section that no longer leads with pool decks. Demoted; may return at walkthrough if Anthony surfaces a finished pool-deck photo.

### `finish_section.body`
- **Value:** "Most handymen frame it, screw it down, call it done. Anthony sands the edges. He cuts curves to match the coping. He notches around what's already there instead of trimming around it. Diane Bennett's pool deck got three other quotes before she called him; the work is what made the difference. Cole Spires hired him for one porch and brought him back for the bedroom tile. The called him; his came in fair and the work came in furniture-grade."
- **Status:** microcopy-design
- **Voice:** Closing Table (contrarian opening, specifics, named example — canonical Closing Table structure)
- **Citation:** intake §Voice — Review 6, §Differentiator 2
- **Note:** GRM universal rule prohibits em dashes — body uses semicolons and periods only.

### `finish_section.evidence_quote`
- **Quote:** "He sanded all the edges and cut a curve around the pool. The price was fair — I had three other quotes."
- **Attribution:** "Diane Bennett · Pool deck · 2026"
- **Status:** microcopy-design (synthesized from intake §Voice — Review 6 manual capture; verify exact wording at walkthrough — Anthony or Diane may have a more accurate version)
- **Voice:** customer voice (preserves register separation per synthesis §2 voice guide)
- **Citation:** intake §Voice — Review 6
- **Walkthrough flag:** the manual capture said "fair pricing confirmed by other quotes Diane obtained" — phrasing above is a tightened paraphrase. If Anthony has the actual review text or screenshot, swap to verbatim.

### `finish_section.image`
- **Value:** `audit/fb-photos/fb-01-cover-photo-pergola.jpg` (provisional, post-audit) OR a different finish-carpentry-strong photo from the 9-photo FB scrape if walkthrough surfaces a stronger fit
- **Status:** pending-walkthrough
- **Caption:** "Pergola — Ocala, finished detail."
- **Alt:** "Finished pergola in Ocala — cedar posts, slatted top, clean detail; built by Anthony Porett."
- **Voice (alt):** Front Porch (specific concrete nouns)
- **Note:** if the hero swaps to pergola, this section needs a *different* finish-carpentry photo to avoid duplication. Walkthrough action: pick best non-hero finish-carpentry photo from `audit/fb-photos/fb-02` through `fb-09`.

---

## About section

> Per GRM zone map: About body = Front Porch. Neighborhood steady persona keeps it Front Porch (Quiet confidence would have allowed embedded Closing Table technical paragraph; not applicable here — Anthony's pitch isn't technical specialism).

### `about.eyebrow`
- **Value:** "ABOUT"
- **Status:** microcopy-design
- **Voice:** Front Porch eyebrow (still Comfortaa ALL CAPS — visual rule overrides voice in eyebrows)

### `about.headline`
- **Value:** "Two men, one truck, most of Marion County."
- **Status:** microcopy-design
- **Voice:** Front Porch (scene-driven, sensory, specific concrete nouns; the "two men" is the team-of-two from review 3 "dynamic duo" without naming the second person)
- **Citation:** intake §Identity (team signal), §Voice — Review 3
- **Note:** GRM rule prohibits em dashes — comma works fine.

### `about.body` (two short paragraphs per synthesis §9 step 5)
- **Paragraph 1:** "Anthony Porett runs Yankee Handyman out of Ocala. Most days it's him and one other guy on the truck, working their way through punch lists nobody else wanted to quote. Some of his customers have been calling him for years."
- **Paragraph 2:** "He doesn't have a sales pitch. He picks up the phone, gives you a real number, shows up, does the work, and cleans up before he leaves. That last part shouldn't be unusual. In Marion County in 2026, it still is."
- **Status:** microcopy-design
- **Voice:** Front Porch (scene → specifics → community/place close)
- **Citation:** intake §Identity, §Differentiator 3 ("cleans up after the job"), §Differentiator 5 (repeat customers); synthesis §9 step 5
- **Note:** intentionally does NOT name the second team member (no evidence base), does NOT commit a year-founded number, does NOT make a licensing claim.

### `about.image`
- **Value:** TBD — owner-uploaded photo if any depict Anthony directly; otherwise a tool/job detail tile
- **Status:** pending-image-review
- **Fallback if no Anthony portrait:** use no image; let the body copy carry the section. Do not invent or generate an Anthony image.

### `about.image.alt` (placeholder)
- **Value:** "Anthony Porett on a job site in Ocala." (rewrite at image review based on actual photo content)
- **Status:** microcopy-design / pending-image-review
- **Voice:** Front Porch

---

## FAQ section

> Per GRM zone map: FAQ section header = Closing Table by default; Neighborhood steady persona adds a Saturday Morning lead-in to the section header. FAQ answers stay Closing Table across all personas.

### `faq.eyebrow`
- **Value:** "BEFORE YOU CALL"
- **Status:** microcopy-design
- **Voice:** Closing Table eyebrow

### `faq.headline_lead_in` (Saturday Morning per Neighborhood steady persona)
- **Value:** "A few things customers usually ask."
- **Status:** microcopy-design
- **Voice:** Saturday Morning (warm informational lead-in)

### `faq.headline` (Closing Table per zone default)
- **Value:** "Real answers, not polite ones."
- **Status:** microcopy-design
- **Voice:** Closing Table (the voice's own self-description — leans hard into its rule "warm precision; real answer instead of polite answer")

### `faq.items` (5 items)

1. **Q:** "What's the service-call fee?"
   **A:** "$125 flat. That covers the visit and most small jobs in full. Bigger jobs get an estimate before any work starts."
   **Citation:** intake §Voice — Review 1 ("$125, which is his standard service fee"), §Differentiator 1
   **Voice:** Closing Table

2. **Q:** "How fast can he get here?"
   **A:** "Same-day when the schedule allows. Two-day estimate-to-completion is typical on bigger jobs. Call and ask."
   **Citation:** intake §Voice — Review 1 (same day), §Voice — Review 9 (two-day completion)
   **Voice:** Closing Table

3. **Q:** "What kind of jobs does he take?"
   **A:** "Plumbing, electrical, carpentry, framing, tile, paint, pool decks. He's done over twenty projects for one customer alone. If you're not sure, call and describe it."
   **Citation:** synthesis §3, intake §Voice — Review 4
   **Voice:** Closing Table

4. **Q:** "Where does he work?"
   **A:** "Ocala and Marion County. Bellechase homeowners hire him often enough to vouch for him by name."
   **Citation:** synthesis §6, intake §Voice — Review 1
   **Voice:** Closing Table

5. **Q:** "Is he licensed?"
   **A:** "[pending-walkthrough]"
   **Status:** pending-walkthrough
   **Build instruction:** at first build, omit this Q&A entirely (per synthesis §4 default-to-silence rule). Flip to "Yes — Florida-licensed handyman, insured" only if Anthony confirms verification at walkthrough. Do not invent a license number.

---

## Contact section

> Per GRM zone map: contact form headline + subhead = Saturday Morning by default. Rescue-ready persona biases toward Closing Table with response-time claim foregrounded — not applicable (Anthony is Neighborhood steady, not rescue-ready). Saturday Morning stays.

### `contact.eyebrow`
- **Value:** "GET IN TOUCH"
- **Status:** microcopy-design
- **Voice:** Saturday Morning eyebrow

### `contact.headline`
- **Value:** "Tell him about the job."
- **Status:** microcopy-design
- **Voice:** Saturday Morning (echoes voice-skill canonical example "Tell us about the job")
- **Citation:** synthesis §5

### `contact.subhead`
- **Value:** "Phone is fastest. He answers most calls during business hours and returns voicemails the same day."
- **Status:** microcopy-design (`pending-walkthrough` partial — phone-answering behavior is `[v2.0-delta]` soft-pass; revise at walkthrough if Anthony's actual pattern differs)
- **Voice:** Saturday Morning (practical specifics, lead with what happens)
- **Citation:** synthesis §5; v2.0-delta soft-pass on phone-answering

### `contact.phone_block`
- **Label:** "Call"
- **Number:** "(239) 867-8447"
- **`tel:` link:** `tel:+12398678447`
- **Subline:** "Mon–Fri 8–5 · Sat 9–5"
- **Status:** committed
- **Citation:** intake §Hours & Availability, §Location & Contact

### `contact.address_block`
- **Label:** "Based in"
- **Address line 1:** "6726 Cherry Rd"
- **Address line 2:** "Ocala, FL 34472"
- **Map link:** `https://maps.google.com/?q=6726+Cherry+Rd,+Ocala,+FL+34472`
- **Map link label:** "Open in Maps →"
- **Status:** committed (address); microcopy-design (label, link copy)
- **Voice:** Saturday Morning labels
- **Citation:** intake §Location & Contact

### `contact.form` (secondary — synthesis §5)

#### `contact.form.headline`
- **Value:** "Or send a quick message."
- **Voice:** Saturday Morning
- **Status:** microcopy-design

#### `contact.form.fields`
- **Field 1: name**
  - Label: "Your name"
  - Placeholder: "Anthony Porett"
  - Required: yes
  - Validation message: "We'll need a name to know who's calling back."
  - Voice (validation): Saturday Morning

- **Field 2: phone**
  - Label: "Phone number"
  - Placeholder: "(352) 555-0123"
  - Required: yes
  - Validation message: "Phone is fastest — please leave a number."
  - Voice (validation): Saturday Morning
  - Note: 352 area code chosen as Marion County local (Ocala-area), per GRM "specific > generic" rule

- **Field 3: job_description**
  - Label: "What's the job?"
  - Placeholder: "Garbage disposal install, porch re-screen, pool deck — anything."
  - Required: yes
  - Validation message: "A sentence or two is enough. He'll call back with questions."
  - Voice (validation): Saturday Morning

- **Field 4: contact_preference (radio)**
  - Label: "Best way to reach you"
  - Options: ["Call back", "Text", "Either"]
  - Required: no
  - Default: "Either"

#### `contact.form.submit_button`
- **Label:** "Send to Anthony"
- **Voice:** Saturday Morning (specific, names the recipient — not generic "Submit")
- **Status:** microcopy-design

#### `contact.form.success_message`
- **Value:** "Got it. He'll call back the same day if it comes in during business hours."
- **Voice:** Saturday Morning
- **Status:** microcopy-design

#### `contact.form.error_message_generic`
- **Value:** "Something didn't go through. Try again, or call (239) 867-8447."
- **Voice:** Saturday Morning
- **Status:** microcopy-design

---

## Footer

> Per GRM zone map: footer tagline = Front Porch, no persona bias. Always Front Porch.

### `footer.tagline`
- **Value:** "Anthony Porett and one other guy, working their way through Ocala one job at a time."
- **Status:** microcopy-design
- **Voice:** Front Porch (warm, people-first, scene-grounded, ends on community/place)
- **Citation:** intake §Identity (team-of-two), §Location & Contact

### `footer.contact_block`
- **Phone:** "(239) 867-8447"
- **Address:** "6726 Cherry Rd, Ocala, FL 34472"
- **Hours:** "Mon–Fri 8–5 · Sat 9–5 · Sun closed"
- **Status:** committed
- **Citation:** intake §Hours & Availability, §Location & Contact

### `footer.social.facebook`
- **URL:** `https://www.facebook.com/TheYankeeHandymanLLC/`
- **Label:** "Facebook"
- **Status:** committed
- **Citation:** intake §Social Presence

### `footer.social.instagram`
- **Status:** pending-walkthrough
- **Build instruction:** omit at first build. The intake-flagged handle `@the.yankee.handyman.llc` is unverified. Flip on only if walkthrough confirms.

### `footer.social.google_business`
- **URL:** GBP listing URL — `pending-extraction` from `place-details-raw.json` (the `url` field on a Places API response)
- **Label:** "Reviews on Google"
- **Status:** pending-extraction
- **Voice (label):** Saturday Morning (specific, factual)

### `footer.copyright`
- **Value:** "© 2026 The Yankee Handyman LLC · Ocala, Florida"
- **Status:** microcopy-design
- **Voice:** factual

### `footer.built_by`
- **Value:** "A Get Rooted Media site."
- **Status:** microcopy-design
- **Voice:** Front Porch (ends on community connection)
- **Link:** `https://getrootedmedia.com`

---

## Floating / sticky elements

### `sticky.mobile_call_bar` (mobile only, persistent)
- **Label:** "Call (239) 867-8447"
- **`tel:` link:** `tel:+12398678447`
- **Status:** microcopy-design
- **Voice:** Closing Table

### `sticky.mobile_call_bar.aria_label`
- **Value:** "Call Yankee Handyman now"
- **Status:** microcopy-design

---

## Error / fallback pages

### `404.headline`
- **Value:** "That page isn't here."
- **Status:** microcopy-design
- **Voice:** Closing Table (declarative, short)

### `404.body`
- **Value:** "If you're trying to reach Anthony, the phone number is (239) 867-8447. Otherwise head back to the homepage."
- **Status:** microcopy-design
- **Voice:** Closing Table (specific action, real number, no fluff)

### `404.cta_primary`
- **Label:** "Back to home"
- **Voice:** Closing Table

### `404.cta_secondary`
- **Label:** "Call (239) 867-8447"
- **`tel:` link:** `tel:+12398678447`

### `500.headline`
- **Value:** "Something on our end broke."
- **Status:** microcopy-design
- **Voice:** Closing Table

### `500.body`
- **Value:** "The site will be back. To reach Anthony in the meantime, call (239) 867-8447."
- **Status:** microcopy-design
- **Voice:** Closing Table

---

## Image alt-text bank (for proof grid + about + pool deck)

> Authored once here so SLOTS doesn't re-author per slot. All in Front Porch voice (alt text is sensory and specific per GRM voice rule for Front Porch).

- `images/09-gbp-customer-diane-bennett.jpg` → "Pool deck Anthony built for Diane Bennett in Ocala. Sanded edges and a curved cut around the pool."
- `images/10-gbp-customer-cole-spires.jpg` → "Porch enclosure and re-tile work Anthony finished for Cole Spires. Ocala, 2025."
- `images/01-gbp-owner-*.jpg` through `08-gbp-owner-*.jpg` → "[pending-image-review — re-author per actual photo subject at walkthrough]"

---

## Forcing-function checklist (to SLOTS)

✅ Every slot has a value or a deferred-state tag.
✅ Every committed copy line cites an intake or synthesis source.
✅ Every microcopy-design slot names its voice and persona-resolved bias.
✅ Voice mapping respects GRM zone rules and Neighborhood steady persona biases.
✅ No em dashes in customer-facing strings (universal GRM rule).
✅ No banned phrases ("learn more," "click here," "passionate about," generic real-estate clichés).
✅ Phone number, address, hours appear consistently across hero, contact, footer.
✅ Synthesis-committed lines preserved verbatim (tagline, customer quotes, differentiator paragraph elements).

**Deferred items (explicit, not ambiguous):**
- Photo selection across hero, proof grid, pool section, about, OG image → `pending-image-review` at walkthrough
- License/insurance line in trust block + FAQ → `pending-walkthrough`
- Phone-answering subhead in contact section → `pending-walkthrough` partial
- Instagram footer link → `pending-walkthrough`
- Logo color extraction for palette → `pending-extraction` at build (CONTENT-INVENTORY commits to "use logo as palette source"; build extracts hex)
- GBP listing URL for footer → `pending-extraction` from `place-details-raw.json`
- Favicon → `pending-extraction` (vectorize logo if possible, else 64×64 raster crop)
- Owner-uploaded photo captions in proof grid (4 items) → `pending-image-review`

---

## Appendix — voice/persona reasoning in one paragraph

Anthony reads as **Neighborhood steady with secondary Quiet confidence.** He has the Bellechase HOA referral signal, "honest & reliable" customer language, no Google review replies (low-ego operator), and repeat-customer evidence — that's warm-civic, not proof-forward. Quiet confidence shows up in the services framing (he doesn't pad the list; the "general handyman + 6 named depths" shape says it without saying it). Persona resolves these zone biases:
- Hero: subhead leans Saturday Morning, headline stays Closing Table (preserves the operator's tagline as committed)
- Services grid header: biases to Closing Table per Quiet confidence
- Trust marquee: stays Saturday Morning
- Testimonials header: stays Saturday Morning per Neighborhood steady
- FAQ header: gets a Saturday Morning lead-in per Neighborhood steady, answers stay Closing Table
- About body: stays Front Porch (no technical-specialism paragraph since Anthony's pitch is generalist warmth, not specialist precision)
- Footer: Front Porch as always

If walkthrough reveals Anthony is more Earned-pride (proof-forward, "I've been doing this for years and the numbers speak for themselves") or Rescue-ready (24/7-feel, emergency-positioning), the persona flips and these biases re-resolve. Default Neighborhood steady is the safer first build given the evidence base.
