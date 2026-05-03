# Yankee Handyman LLC — Build Pack

> Single-page brochure site for Anthony Porett's handyman business in Ocala, FL. This pack contains every artifact Code needs to build the site, plus the upstream synthesis trail Chat needs for client conversations.
>
> **If you are Code:** start with this README, then read `BUILD-DECISIONS.md`, then `slots.md`. Refer to `content-inventory.md` for any string. Refer to `Home.html` for visual target.
>
> **If you are Chat:** start here, then read `synthesis.md` for the strategic argument and `intake.md` for the raw evidence base.

---

## Reading order by role

### For Code (build engineer)

| Order | File | Why |
|---|---|---|
| 1 | `README.md` | This file. Pack overview, open decisions, build sequence. |
| 2 | `BUILD-DECISIONS.md` | Hosting, fonts, forms, analytics, schema.org. The technical contract. |
| 3 | `slots.md` | Section-by-section layout spec. Type, color, spacing tokens. The build manual. |
| 4 | `content-inventory.md` | Every string the build needs. Cite from this — never re-author. |
| 5 | `Home.html` | Visual reference comp. The look-and-feel target. |
| 6 | `synthesis.md` | Optional. Read if a SLOT decision feels arbitrary — the reasoning is here. |
| 7 | `intake.md` | Reference only. Raw evidence behind every committed line. |

### For Chat (account / client conversations)

| Order | File | Why |
|---|---|---|
| 1 | `README.md` | This file. |
| 2 | `synthesis.md` | The strategic argument: voice, persona, section sequence, taglines. Use this in walkthrough. |
| 3 | `intake.md` | Raw evidence by section. Cite review numbers, FB tagline, etc., back to client. |
| 4 | `intake-template.md` | The v2.0 contract spec. Reference for next prospect. |
| 5 | `audit-script-implications.md` | Internal note for the intake-script design session. Skip for client work. |

### Internal-only (not for Code, not for client)

- `audit-script-implications.md` — design notes for the audit script we're building separately

---

## Pack contents

```
yankee-handyman/
├── README.md                           ← you are here
├── BUILD-DECISIONS.md                  ← technical contract for Code
├── intake.md                           ← raw evidence, captured against v1.x shape
├── intake-template.md                  ← v2.0 spec (preserved for reference)
├── audit-script-implications.md        ← internal note (intake-script design)
├── synthesis.md                        ← strategic decisions: voice, persona, section sequence
├── content-inventory.md                ← every string the build needs
├── slots.md                            ← section-by-section layout spec
└── Home.html                           ← visual reference comp
```

---

## Open decisions (the client owes us before publish)

These are the slots tagged `pending-walkthrough` across the pack. Walk this list with Anthony before Code ships:

| # | Decision | Where it shows up | Default if unresolved |
|---|---|---|---|
| 1 | **Confirm $125 flat service-call fee is current** | Trust marquee, FAQ #1, differentiator paragraph | Stop the build. This is the strongest pricing hook on the page; if stale, multiple sections re-author. |
| 2 | Anthony's email address | Form backend destination, footer optional contact | Mailto fallback to a GRM-managed inbox; flip to Anthony's at walkthrough |
| 3 | License/insurance verification | FAQ #5, trust marquee optional line | Omit FAQ #5 entirely. Do not invent a license number. |
| 4 | Phone-answering pattern | Contact subhead | Ship "Phone is fastest. He answers most calls during business hours and returns voicemails the same day." Revise if Anthony's actual pattern differs. |
| 5 | Instagram handle verification | Footer social link | Omit the link. Don't link to an unverified handle. |
| 6 | Photo selections (10-photo library) | Hero, proof grid, pool section, about, OG image | Hero falls back to ink-solid background. Proof grid contracts to 4 if fewer photos pass usability bar. About goes image-less. |
| 7 | Pool deck Diane Bennett quote | Pool section evidence quote | Ship the paraphrase from intake §Voice — Review 6. Swap to verbatim if Anthony has the source. |
| 8 | Owner/team identification | About section ("two men, one truck") | Don't name the second team member. Keep "and one other guy" until Anthony confirms a name. |

---

## Build sequence (high level)

1. **Resolve open decisions** above with Anthony at walkthrough. Don't start the build until #1 (the $125 fee) is confirmed.
2. **Extract logo color** → `--c-brand` (per `slots.md §0`).
3. **Image review** → assign photos to slots, regenerate alt text per actual subject.
4. **Build per `slots.md §16`** — start with tokens, then sections in document order.
5. **Wire structured data** per `BUILD-DECISIONS.md` (LocalBusiness + aggregateRating).
6. **QA against `content-inventory.md`** — every committed line must appear verbatim. Every `pending-*` flag must either be resolved or fall through to its documented default.
7. **Lighthouse run** — target ≥95 mobile, ≥98 desktop per `slots.md §15`.
8. **Visual diff against `Home.html`** — if the build deviates significantly from the comp, flag back to design before ship.

---

## Authority chain (when something is ambiguous)

If two docs conflict, the later one wins:

```
intake → synthesis → content-inventory → slots → BUILD-DECISIONS → Home.html
```

- **Copy disputes:** `content-inventory.md` is canonical. Synthesis is the reasoning, inventory is the commitment.
- **Layout disputes:** `slots.md` is canonical. Home.html is a reference, not a contract.
- **Technical disputes:** `BUILD-DECISIONS.md` is canonical for hosting / forms / fonts / analytics / structured data.
- **Voice disputes:** `synthesis.md §2` (voice guide) is canonical. Inventory and slots inherit.

If a real conflict surfaces, kick it back to design before inventing a resolution.

---

## What's *not* in this pack (and why)

- **No CMS schema.** This is a static brochure site. Anthony does not maintain content; GRM updates the page when needed. If the client later wants to self-edit, that's a v2 conversation.
- **No multi-page routing.** Single-page scroll with section anchors. About, FAQ, Contact are sections, not pages.
- **No menu system, events module, or dynamic content.** Service contractor, not restaurant.
- **No Spanish translation.** Marion County demographic supports it but client hasn't asked. Flag for v2.
- **No blog / news.** No content engine; nothing to populate it. Flag for v2 if Anthony wants one.
- **No online booking or quote form integration.** Phone-primary site per synthesis §5. Form is secondary fallback only.

---

## Forcing-function check (this pack is shippable when…)

- ✅ Every doc is in this folder
- ✅ Every committed string in `content-inventory.md` traces to an `intake.md` source
- ✅ Every layout decision in `slots.md` has explicit responsive + a11y spec
- ✅ Every technical decision is documented in `BUILD-DECISIONS.md`
- ✅ A visual comp (`Home.html`) exists for design reference
- 🟡 Open decisions list above is walked with Anthony before publish

If all eight checkboxes pass, the pack is complete enough that two different Code engineers would build the same site.
