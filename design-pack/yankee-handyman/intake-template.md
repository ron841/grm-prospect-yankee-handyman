# Intake — [Business Name]

> **Purpose:** This is the spec CONTENT-INVENTORY consumes and the audit script targets. Capture against the field shape exactly; do not invent sections.
>
> **Source tags** (every field carries one):
> - `[api]` — auto-fillable from Google Places API
> - `[scrape]` — fillable via Playwright scraping of FB/IG/photo URLs (brittle, expect failures)
> - `[human]` — manual capture or judgment that won't automate cleanly
> - `[derived]` — computed from other fields (script handles, do not hand-fill)
>
> **Gap tag:** append `[gap]` to any field that is blank or insufficient after best-effort capture. The audit script reports gaps; do not maintain a separate roll-up.

---

## 1. Identity

- **Legal name:** `[api]`
- **Display name:** `[api]` — what GBP shows; usually same as legal, sometimes shorter
- **Owner first name:** `[api]` — from GBP if listed, else `[human]`
- **Owner last name:** `[human]` — rarely in API; check FB page About, license records
- **Tagline:** `[human]` — one line, customer-facing. If none exists, write `[gap]` rather than invent one. Synthesis comes later, not here.
- **Founded year:** `[human]` — capture **only if ≥10 years ago**. Below threshold it's noise; leave blank, no gap tag.
- **License / insurance:** `[human]` — license number + state board if regulated trade. `[gap]` if claimed-but-unverified vs. `[gap: not applicable]` if trade doesn't license.
- **Primary GBP category:** `[api]`
- **Secondary GBP categories:** `[api]` — list, do not promote to a top-level Services section. Real services come from review-mining (§5).

---

## 2. Location & Contact

- **Street address:** `[api]`
- **City / state / zip:** `[api]`
- **Phone:** `[api]`
- **Email:** `[human]` — check FB About, IG bio, business card in photos
- **Website:** `[api]` — expected blank for this prospect class; that's the point
- **Service-area geography:** `[human]`
  - **Cities served:** structured list, e.g. `["Ocala", "Belleview", "Dunnellon"]`
  - **Counties served:** structured list, e.g. `["Marion"]`
  - **Zip codes (if owner specifies):** structured list
  - **Radius from base (miles, if owner specifies):** integer
  - Capture as the owner states it. If GBP says "Marion County" but reviews mention Sumter, flag with `[gap: scope unclear]`.
- **Emergency / after-hours:** `[human]` — boolean + note. "Yes, 24/7" vs. "Yes, with surcharge" vs. "No" all matter for copy.

---

## 3. Hours & Availability

- **Regular hours:** `[api]` — structured per day
- **Special hours / holiday closures:** `[api]`
- **Currently open flag:** `[derived]` — script computes from hours + capture timestamp
- **Response-time signal:** `[human]` — from review language ("called back same day," "showed up next morning"). One sentence. Distinct from emergency flag.

---

## 4. Voice

> Single consolidated section. Synthesized markers on top, raw evidence underneath. Do not split reviews from replies — the pairing is the signal.

### 4a. Synthesized markers `[human]`

- **Customer language — recurring phrases:** bullet list, verbatim short phrases that appear ≥2 times across reviews. Quote marks, no paraphrasing.
- **Owner language — recurring phrases:** same, from owner replies.
- **Recurring job nouns:** flat list of work types named in reviews — e.g. `["deck railing", "drywall patch", "ceiling fan install", "garbage disposal"]`. This is the **real** services list and feeds CONTENT-INVENTORY's services block.
- **Tone markers — customer:** 2–4 adjectives with one-line justification each. E.g. *"relieved — multiple reviews describe being stuck before he showed up."*
- **Tone markers — owner:** 2–4 adjectives. Note **register shifts** explicitly: how owner talks to a 5-star vs. a complaint vs. a repeat customer. Register shift is the single highest-value voice signal; do not flatten it.
- **Price signaling:** `[human]` — what reviews say about cost. Pick one of: `fair / reasonable / premium-but-worth-it / cheap / mixed / not-mentioned`. Add 1–2 quoted phrases as evidence.

### 4b. Raw evidence `[api]` for the first 5, `[human]` beyond

> Capture target: **top 12 by length + any review under 50 words that names a specific job.** Past ~15 you're at diminishing returns. Do not attempt all 45.

For each captured review:

```
### Review [N]
- Stars: [api]
- Date: [api]
- Author: [api]
- Length-bucket: short | medium | long [derived]
- Names-specific-job: yes | no [human]
- Text: |
    [api, full text]
- Owner reply:
    - Date: [api]
    - Text: |
        [api, full text]
    - Register: warm-standard | warm-extra | apologetic | corrective | none [human]
```

If no owner reply, write `Owner reply: none` — do not omit the field.

---

## 5. Services (derived, not captured)

- **Services list:** `[derived]` — promoted from §4a *Recurring job nouns*. Do not hand-write a services list; it always drifts from review evidence.
- **Service categories that appear in GBP but NOT in reviews:** `[derived]` — flag as `[gap: claimed-not-evidenced]`. These are the riskiest copy items.

---

## 6. Trust Signals

- **Review count:** `[api]`
- **Average rating:** `[api]`
- **Rating distribution (5/4/3/2/1):** `[api]`
- **Years in business:** `[derived]` from §1 founded year, **only if ≥10**
- **Licensing claims (verified):** `[human]` — see §1
- **Insurance claims (verified):** `[human]`
- **Awards / certifications visible in photos or replies:** `[human]`
- **BBB / industry-body membership:** `[human]` `[gap]` if absent

---

## 7. Phone-answering behavior `[human]`

> 30-second capture. Call once during stated hours, once outside.

- **Answers live during hours:** yes | voicemail | no-answer
- **Voicemail tone:** none | generic | personal-warm | personal-curt
- **Callback time (if left message):** integer hours, or `not-returned`
- **Implication for CTA:** push-call | push-form | mixed | needs-form-only

---

## 8. Seasonality `[derived]` + `[human]`

- **Review-date histogram by month:** `[derived]` from §4b
- **Owner-stated season patterns:** `[human]` if owner mentions in replies or FB posts
- **Implication:** one sentence — does the site need a "summer book early" or "winter availability" hook?

---

## 9. Social Presence

- **Facebook page URL:** `[human]` to find, `[scrape]` to mine
- **Facebook — last post date:** `[scrape]`
- **Facebook — post cadence (posts/month, last 6 months):** `[scrape]`
- **Facebook — top 3 post types:** `[scrape]` — e.g. job photos, holiday greetings, reviews-reposted
- **Instagram handle:** `[human]` to find, `[scrape]` to mine
- **Instagram — last post date:** `[scrape]`
- **Instagram — grid coherence:** `[human]` — judgment call: tight | loose | chaotic | empty
- **Active-presence verdict:** `[human]` — `active | dormant | absent`. Drives whether site links social at all.

---

## 10. Photos

> Tag each on two axes. Photo lives in `images/` with filename `[NN]-[subject]-[usability].jpg`.

**Subject tags** (pick one): `owner-on-site` | `crew` | `before` | `after` | `tool-or-truck` | `completed-detail` | `exterior-context` | `interior-context` | `other`

**Usability tags** (pick one): `hero-candidate` | `section-header` | `proof-grid` | `unusable`

**Minimum viable inventory:**
- ≥1 `hero-candidate`
- ≥3 `section-header`
- ≥6 `proof-grid`
- ≥1 `before` paired with ≥1 `after` (gold for handyman specifically — flag pairs explicitly)

If minimums not met after capture, flag `[gap: photo-shortfall]` at this section level. This is a **pre-build blocker**, not a build-time discovery.

```
### Photo [NN]
- Filename: [NN]-[subject]-[usability].jpg
- Source: gbp | facebook | instagram | owner-supplied
- Subject: [human]
- Usability: [human]
- Pair-id: [human, optional] — for before/after pairs, same id on both
- Notes: [human, optional] — one line if needed
```

---

## 11. Visual identity

### 11a. Logo

- **Logo file present:** boolean `[human]`
- **Source:** gbp-profile | facebook-profile | instagram-profile | photo-extract | owner-supplied | none
- **Quality:** vector | high-raster | low-raster | needs-recreation
- If `none`, flag `[gap: identity-from-scratch]` — this is a design step, not a capture step.

### 11b. Vernacular color evidence `[human]`

> Replaces "propose palette from uniforms." Capture evidence only; identity work is downstream.

- **Truck colors:** list of hex-approximations from photos, or `not-visible`
- **Uniform / shirt colors:** list, or `not-visible`
- **Yard sign / business card colors:** list, or `not-visible`
- **Existing logo colors (if logo present):** list
- **Constraint summary:** one sentence — what colors must the identity NOT contradict? E.g. *"truck is white with red lettering; navy/gold palette would contradict."*

---

## 12. Competitor set `[human]`

> 2–3 other operators in the same county/category with websites, even bad ones. Establishes local category baseline for CONTENT-INVENTORY.

For each:

```
### Competitor [N]
- Name:
- URL:
- Review count / rating: [api if available]
- Site quality: template | custom-cheap | custom-good | none
- Notable copy moves: 1–2 bullets
- Notable visual moves: 1–2 bullets
```

---

## 13. Differentiators — raw evidence `[human]`

> Bullet evidence only. Synthesis into prose happens in a separate `synthesis.md`, not here. If you find yourself writing sentences, stop.

- Bullet list of specific evidence from §4 (Voice) and §10 (Photos) that distinguishes this operator from §12 (Competitors).
- Each bullet ≤15 words.
- Tag each bullet with the source field, e.g. *"Owner replies to every review within 24h — see §4b register shifts."*

---

## Capture metadata

- **Captured by:** `[human]`
- **Capture date:** `[human]`
- **Places API pull date:** `[api]`
- **Last social scrape date:** `[scrape]`
- **Spec version:** 2.0
