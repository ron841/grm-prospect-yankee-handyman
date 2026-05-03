# Audit Bridge — Code's Audit ↔ This Pack

> Cross-reference document. Code ran a full audit pass on the live build (2026-05-03). This file maps every audit finding to the doc(s) in this pack that absorbed the resolution, plus what's still open.
>
> **Audit artifacts live in Code's repo:** `audit/` folder at github.com/ron841/grm-prospect-yankee-handyman, commit `da08050`. Includes 11 screenshots (3 breakpoints + 8 targeted), 9 FB-scraped photos, 5 audit docs, 1 footer-YH-symbol mockup. Not duplicated here — single source of truth lives in the repo.

---

## Findings → resolution map

### Critical (1)

| # | Finding | Where it lives in the audit | Resolution in this pack |
|---|---|---|---|
| 1 | $125 service-call fee may be stale | `audit/AUDIT.md` §Critical | Already README-gated as Open Decision #1. **No change** — pack already correctly flagged this as walkthrough-blocking before audit. Status: confirmed. |

### High (2 — block walkthrough sign-off)

| # | Finding | Where it lives in the audit | Resolution in this pack |
|---|---|---|---|
| 2 | Pool-deck section: copy/photo truth violation. Committed copy ("sanded every edge / curve around the pool") against mid-construction framing photo. | `audit/comp-diff.md`, `audit/photo-audit.md` | **Re-authored across three docs:** `synthesis.md §9` step 4 reframed from pool-deck-led to finish-carpentry-general; `content-inventory.md` `pool_section.*` → `finish_section.*` with new headline "Finish carpentry, not just framing"; `slots.md §6` re-titled. Diane Bennett's pool-deck quote demoted from headline to evidence row. `Home.html` updated. |
| 3 | Hero photo weakness. Cement-board install photo fights text overlay (Anthony's body sits where headline lands); process-not-product. | `audit/hero-evaluation.md` | **Hero swapped to FB cover-photo pergola** (`audit/fb-photos/fb-01-cover-photo-pergola.jpg`, 960×720, finished pergola). Updated in `synthesis.md §8`, `content-inventory.md hero.image`, `slots.md §16` build sequence. Resolution caveat: 960×720 will pixel up on widescreens — walkthrough action is to request high-res original from Anthony. |

### Important (4 — Design should review)

| # | Finding | Where it lives in the audit | Resolution in this pack |
|---|---|---|---|
| 4 | Palette validation: k-means against actual logo returned brown/sepia, zero blue clusters. Provisional navy was wrong direction. | `audit/AUDIT.md` §Palette | **Palette swapped to sepia/brown** in `Home.html` `:root` block. Updated `slots.md §16` build sequence with note that k-means extraction returns brown/sepia. Added Open Decision #9 to `README.md`: confirm with Anthony whether sepia is intentional brand DNA or JPEG-degraded. |
| 5 | Photo grid captions: 4 generic "Completed work, 2025" because subjects untagged | `audit/photo-audit.md` | **Acknowledged unresolved.** `content-inventory.md` proof-grid captions remain `pending-image-review` per original synthesis decision. The audit confirms what we already knew. Walkthrough action: tag subjects, re-author captions per actual content. |
| 6 | Weak grid photos: several owner-uploaded photos may not pass usability bar | `audit/photo-audit.md` | **Acknowledged.** `synthesis.md §10` and `slots.md §6` already documented "grid contracts to 4 if fewer photos pass usability bar" — audit confirms grid likely contracts. No doc change; behavior is already specced. |
| 7 | Footer YH symbol decision (mockup exists, not pushed) | `audit/mockups/footer-yh-mockup.html` + screenshot | **Deferred to Design call.** Mockup reads well visually (cream box, brown YH — clean bookend to nav). Recommendation: ship YH symbol in footer. Pack does not mandate either way; `slots.md §11` (footer) and `Home.html` footer remain symbol-less for now. Walkthrough decision. |

### Nice-to-have (4)

| # | Finding | Where it lives in the audit | Resolution in this pack |
|---|---|---|---|
| 8 | Footer background color review | `audit/AUDIT.md` §Nice-to-have | **No change.** Footer uses ink-on-paper-2 currently; readable, contrast passes. Optional polish at v2. |
| 9 | IG handle verification | Already README Open Decision #5 | **No change.** Already gated. |
| 10 | Email routing | Already README Open Decision #2 | **No change.** Already gated. |
| 11 | 768px breakpoint behavior (lands in mobile mode at the boundary) | `audit/comp-diff.md` | **Acknowledged.** CSS rule is `max-width: 768px` inclusive, which is correct per `slots.md §13` responsive spec. The breakpoint behavior is intentional, not a bug. No change. |

---

## What changed in the pack today (post-audit edits, 2026-05-03)

| Doc | Change |
|---|---|
| `synthesis.md` | §8 hero photo committed to pergola provisional. §9 step 4 reframed pool→finish-carpentry. §13 row 12 updated. |
| `content-inventory.md` | `hero.image` + `hero.image.alt` swapped to pergola. Pool section renamed Finish carpentry section, all `pool_section.*` slots renamed `finish_section.*` with new headline + body. |
| `slots.md` | §6 retitled. §16 build sequence updated for k-means brown/sepia + pergola hero. Open decisions table updated. |
| `Home.html` | Color tokens swapped to sepia/brown family. Hero/section photo placeholder labels updated. Pool section headline + body re-authored. Pool service card blurb softened (no more pool-specific "sanded edges" claim — replaced with "ask for the gallery"). |
| `README.md` | Open Decisions table grew from 8 to 10. Added items 9 (brand color confirmation) and 10 (pool reframe confirmation). Header note added flagging post-audit update. |
| `audit-script-implications.md` | Appended four post-audit findings: (1) FB photos lift to Playwright-required, (2) hero capture must be exhaustive across surfaces, (3) k-means logo extraction belongs in intake not build, (4) copy-photo truth violation check belongs in synthesis QA. |
| `audit-bridge.md` | (this file — new) |

---

## What did NOT change (and why)

- **Photo subject tagging** — still deferred to image-review at walkthrough. Audit confirmed the deferral was correct; vision-model auto-tagging at 70% accuracy is worse than useless per `audit-script-implications.md`.
- **Footer YH symbol** — mockup exists; design call. Pack stays neutral until walkthrough.
- **Service area structured geography** — still soft-passed per synthesis §0. Audit didn't surface new evidence.
- **Phone-answering pattern** — still pending walkthrough. Audit didn't test phone behavior; no new evidence.
- **Tagline** — committed line ("Creating Beautiful Spaces and Smiling Faces") survives audit unchanged. Audit had no objection.

---

## Recommendation to Code

1. **Pull the audit photos.** `audit/fb-photos/fb-01-cover-photo-pergola.jpg` is the new hero. The other 8 FB photos are the proof-grid candidate set; cherry-pick the 4 finish-carpentry-strongest after image review at walkthrough.
2. **Walkthrough action list expanded** — README Open Decisions now has 10 items. Items 1, 9, 10 are walkthrough-critical (block publish if unresolved).
3. **Re-deploy preview after walkthrough** — the pergola hero + sepia palette are visible enough changes that Anthony should see them before publish, not at publish.
