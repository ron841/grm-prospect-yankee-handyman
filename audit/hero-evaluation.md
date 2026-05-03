# Hero Opener Evaluation — Yankee Handyman

Three options evaluated against the synthesis-committed hero stack (eyebrow / headline / supporting line / trust line / CTAs).

---

## Option A — Keep current GBP hero

**Photo:** [`build/images/01-gbp-owner-the-yankee-handyman-llc.jpg`](../build/images/01-gbp-owner-the-yankee-handyman-llc.jpg) — Anthony installing Brand DuRock cement board.

**As rendered:** [screenshots/01-hero-desktop.png](screenshots/01-hero-desktop.png)

**Pros:**
- Authentic — Anthony in his own t-shirt, in the act of working
- Free, already in the library, already wired in
- Reinforces the "real working contractor, no marketing fluff" pitch the site is going for

**Cons:**
- Composition fights the text overlay — Anthony's body sits right where the headline lands; the dark gradient covers him to make text readable, defeating the purpose of having him in the shot
- Subject is mid-process drywall/cement-board work, not aspirational
- Window in the frame creates a bright distraction
- Background is dim/cluttered (OSB, dust on floor)

**Verdict:** Below threshold for a $500-conversion preview. The site is supposed to make Anthony look hireable on first glance; this hero makes him look like every generic handyman.

---

## Option B — Swap to FB cover photo (pergola)

**Photo:** [`fb-photos/fb-01-cover-photo-pergola.jpg`](fb-photos/fb-01-cover-photo-pergola.jpg) — finished pergola/covered patio attached to a Florida ranch home.

**Source resolution:** 960×720 (FB cover photo standard size)

**Pros:**
- **Finished work, not in-progress.** The whole point of a portfolio hero — show what you can build, not what you're building.
- **Outdoor / blue-sky setting** — much more aspirational than an interior cement-board install. Florida sun + structure + grass is a sale-ready scene.
- **Visible craft:** the pergola beams + lattice show finish carpentry — directly supports the "Pool decks built like furniture" / finish-carpentry positioning that's already committed in copy
- **Open composition** — the pergola sits center-frame with sky above and grass below, leaving plenty of dark-overlay real estate for the headline copy without obscuring the subject

**Cons:**
- **Resolution is borderline for hero use.** 960×720 is enough for mobile and tablet at 1× density, but desktop hero at 88vh on 1280px viewport will need to upscale ~30%. On retina displays it'll look soft. Mitigation: request original from Anthony (he uploaded it to FB at some larger source size). If unavailable, the upscale is acceptable for a $500-preview.
- It's a pergola, not a job that's currently mentioned in the services list. Either accept that as "additional work he does" implicit signal, or explicitly add "Outdoor structures / pergolas" to the services list.

**Verdict:** **STRONG RECOMMEND.** Best single asset we have for Yankee Handyman. The 960×720 resolution caveat is real but solvable (request original from Anthony at walkthrough).

---

## Option C — Drop hero photo, ink-solid background

**Treatment:** No background image. `--c-ink` solid (or `--c-brand` brown solid) fills the hero. Headline goes large per slots.md fallback (`--t-display` 72px).

**Pros:**
- Removes the photo-quality dependency entirely — no risk of the photo undermining the message
- Clean, modern, type-forward — works for the Quiet confidence persona bias
- Lets the synthesis-committed tagline ("Creating Beautiful Spaces and Smiling Faces") carry the visual weight
- Slots.md §3 already specifies this fallback explicitly: "If no photo passes review at walkthrough: fall back to ink solid background, drop image, increase headline weight presence with `--t-display` (72px)"

**Cons:**
- Loses an evidence anchor — site has 50 reviews and a real story; a photo-less hero feels conservative for a portfolio-style trade business
- Front Porch persona expects scene-grounded sensory detail; type-only feels Closing Table-pure (the bias the build doesn't carry)

**Verdict:** Acceptable fallback. Use only if Option B's 960×720 fails Design's quality bar OR if Anthony's source is unavailable.

---

## Recommendation

**Ship Option B (pergola hero) at the next iteration.**

Implementation:
1. Replace `images/01-gbp-owner-…llc.jpg` reference in build with `fb-photos/fb-01-cover-photo-pergola.jpg` (or a new owner-uploaded original if Anthony provides one)
2. Re-author hero alt text: "Finished pergola Anthony built in Ocala, attached to a single-story home with screen porch behind."
3. Regenerate OG image from new hero (the build script's OG-generator step automatically picks up whatever the hero is)
4. Verify the two-axis dark gradient still pushes the headline to the dark quadrant — pergola sits center-frame so a center-darken or top-darken should work; current left-darken may pull focus oddly

If Design pushes back on 960×720: fallback to Option C (ink-solid) for preview, request original from Anthony at walkthrough, then upgrade to Option B post-walkthrough.

If Anthony provides a finished-pool-deck photo at walkthrough that's better than the pergola: re-evaluate. The pergola is the best of what we currently have, not necessarily the best he could provide.
