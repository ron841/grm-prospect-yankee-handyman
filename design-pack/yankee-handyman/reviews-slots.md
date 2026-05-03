# Reviews Page — SLOTS

> Build spec for `/reviews`. Iter-3.
>
> **Authority chain:** reviews-synthesis → reviews-content-inventory → SLOTS → build.
> **Inherits from homepage SLOTS:** all tokens (type, color, spacing, radii) — see `slots.md §0`. This file specifies layout, hierarchy, behavior unique to the reviews page.

---

## §0 — Tokens (inherited from homepage)

Same `--font-*`, `--t-*`, `--c-*`, `--s-*`, `--r-*` tokens as `slots.md §0`. No new tokens.

**Universal rule (reaffirmed):** no em dashes. Use periods, commas, semicolons.

---

## §1 — Page structure

```
<header.nav>                 (sticky, 72px — same as homepage)
<main>
  §1 Page header             (container, eyebrow + headline + subhead)
  §2 Curated leads           (container, 5 review/reply pair cards stacked)
  §3 One 1-star              (container, full-width card, paper-2 bg)
  §4 Grouped sections        (container, 7 groups, each with header + review cards)
  §5 Archive                 (container, lighter weight, list rather than cards)
  §6 CTA banner              (full-width, --c-paper-2 bg)
</main>
<footer>                     (same as homepage)
<div.sticky-call-bar>        (mobile only, fixed bottom)
```

**No hero image on this page.** Reviews ARE the hero. Do not add a stock-photo header banner.

---

## §2 — Page header

### Layout

```
[ eyebrow ]
[ headline                            ]
[ subhead — 2 line max                ]
[ ← Yankee Handyman home              ]   <- text link, --t-body-sm, --c-ink-soft
```

- Container: 800px max-width, centered
- Padding: `--s-9` top, `--s-7` bottom desktop; `--s-7`/`--s-6` mobile
- Eyebrow: `--t-eyebrow`, Comfortaa 700, --c-brand
- Headline: `--t-h1` desktop / 36px mobile, Merriweather 700
- Subhead: `--t-body-lg`, Nunito 400, --c-ink-soft, max-width 60ch
- Back link: `--t-body-sm`, underline on hover only

---

## §3 — Curated leads (5 pair cards)

> Stacked vertically, full container width. Each card pairs review + reply inline; no disclosure/accordion.

### Card layout

```
┌─ review-pair-card ─────────────────────────────────┐
│  ★★★★★    Reviewer Name              Job tag       │
│                                       (12px gap)   │
│  "Review text. Verbatim. Multiple paragraphs       │
│   render with normal margins. No truncation."      │
│                                                    │
│  ┌─ reply-block ────────────────────────────────┐  │
│  │  ↳ Anthony, <reply_date>                     │  │
│  │  "Reply text. Verbatim."                     │  │
│  └──────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────┘
```

- Card: `--c-paper`, `--r-lg` (16px), 1px hairline `--c-line`, `--s-7` interior padding
- Stars: gold (#d6a419 or extracted brand-warm), `--t-body-lg` size
- Reviewer name: Merriweather 700, `--t-h4`
- Job tag: right-aligned on desktop; below name on mobile. `--t-body-sm`, `--c-ink-soft`, italic
- Review text: Nunito 400, `--t-body`, `--c-ink`, line-length capped at ~70ch
- Reply block: indented `--s-5` from left, `--c-paper-2` bg, `--r-md`, `--s-5` interior pad
- Reply attribution (`↳ Anthony, 5 days ago`): `--t-body-sm`, `--c-ink-soft`, Comfortaa or Nunito 600
- Reply text: Nunito 400 italic, `--t-body`, `--c-ink`

### Stacking

- Vertical gap between cards: `--s-7`
- No card numbering on the page (the order IS the curation)

### Mobile

- Same structure, reduced padding (`--s-5` interior)
- Job tag stacks below reviewer name

---

## §4 — One 1-star

### Section header

```
[ One 1-star review.                  ]   <- --t-h2, Merriweather 700
[ Anthony's reply is below it.        ]   <- --t-body-lg, --c-ink-soft
```

- Container: 800px max-width, centered, `--s-9` top margin, `--s-7` bottom margin
- **No editorial wrapper.** No "how Anthony handles tough feedback." No badge. No icon.

### Card

Same `review-pair-card` layout as curated leads. Single change: stars render in `--c-error` (or muted gray if --c-error reads too alarming) — one star filled, four outlined.

**Critical:** the visual weight of this card matches a curated-lead card. Do not visually de-emphasize. Do not visually emphasize. Equal weight is the trust signal.

---

## §5 — Grouped sections

> Seven groups. Each group is a sub-section with its own header.

### Group header

```
[ GROUP N         ]    <- eyebrow, --t-eyebrow
[ Group headline. ]    <- --t-h2, Merriweather 700
[ One-line subhead. ]  <- --t-body-lg, --c-ink-soft
```

- `--s-9` top margin between groups
- 800px max-width container

### Group body

Reviews render as **compact pair cards** — same structure as curated leads, but:
- `--s-5` interior padding (vs `--s-7`)
- `--t-body` review text (no size bump)
- Reviewer name `--t-h4` (no h3 promotion)
- `--s-5` vertical gap between cards within a group (vs `--s-7`)

Compact cards keep groups dense without crowding. Long reviews (Cole Spires, Barbara Roberts, JEAN JONES, audrey bittman, David Bittman, Maudeline Henry, Megan Stone, Zulma Velez) still breathe inside their cards.

### Group sequence (locked from content-inventory §3)

1. Carpentry and framing (6 reviews — Cole Spires, Barbara Roberts, William Stone, Edward Campea, Leanna Fitzgerald, Ju B)
2. Tile and flooring (3 — Maudeline Henry, Zac Stone, Ashley Santiago)
3. Porches, decks, outdoor builds (3 — David Bittman, Brendon Pointing, Terri)
4. Multi-trade and repeat customers (3 — JEAN JONES, audrey bittman, Karen Cowan)
5. Plumbing and electrical (2 — Megan Stone, Molly Groves)
6. Painting (1 — Jennifer LeMay)
7. Quick jobs and short praise (14 — Zulma Velez, Robert Nedow, George Kim, Devin P, Bob Hart, Sam Perry, Dan Carter, Jon De Lucia, Griselle Martin, Jorge Aliaga, Ryan McBride, Brian Stamper, Jarron Remington, Katheryn Foerste)

### Group 7 special case

The "Quick jobs" group has 14 entries — the most of any. Layout: **2-column grid on desktop** (≥1024px), 1-column below. The shorter reviews tile cleanly without padding-feel. Other groups stay 1-column always (long reviews need full width).

---

## §6 — Archive

### Section header

```
[ ARCHIVE              ]
[ The shortest ones.   ]
[ Real reviews, just brief. ]
```

- `--s-10` top margin (extra breathing room separating from groups)

### Archive list

Compact list, not cards. Each entry:

```
[★★★★★] Wally Plumstead · a year ago
        "Outstanding. Went above and beyond too. Professional."
        ↳ "Thank you for choosing The Yankee Handyman, we appreciate your business. Thank you."
```

- Single-line star/name/date row, `--t-body-sm`
- Review text inline, `--t-body`, italic
- Reply prefix `↳`, `--t-body-sm`, `--c-ink-soft`, italic
- `--s-5` vertical gap between entries
- No card chrome — flat list against page background
- Hairline divider between entries: `--line`

---

## §7 — CTA banner (page bottom)

### Layout

Full-width section, `--c-paper-2` bg, `--s-10` vertical padding.

```
[              Tell him about the job.                  ]   <- --t-h2 centered
[  Phone is fastest. He answers most calls during        ]
[             business hours.                            ]   <- --t-body-lg centered, max 60ch
[                                                        ]
[       [ Call (239) 867-8447 ]   See all 50 on Google → ]
```

- Phone button: primary CTA, `--c-brand` bg, white text, `--r-md`, `--s-5` interior pad
- "See all 50" link: secondary, text-only, `--c-ink-soft`, `→` icon

### Mobile

- Buttons stack: phone first, "see all" second
- Phone button full-width
- "See all" link centered below

---

## §8 — JSON-LD

Per content-inventory: emit one `Review` entry per surfaced review (44 total). Place in `<head>` as a single `<script type="application/ld+json">` block containing an array.

Homepage retains `aggregateRating` only — do not emit `Review` entries on homepage.

---

## §9 — Responsive breakpoints

Same as homepage SLOTS:
- ≥1024px: full desktop
- 768-1023px: tablet — single column, reduced section padding
- ≤767px: mobile — `--s-7`/`--s-6` section padding, `--t-h1` becomes 36px, sticky call bar visible

---

## §10 — Accessibility

- Each review pair card: `<article>` with `aria-labelledby` pointing to reviewer name
- Star ratings: `<span aria-label="5 out of 5 stars">★★★★★</span>` (visual stars are decorative; aria-label carries the meaning)
- Group headers: `<h2>`, sub-cards use `<h3>` for reviewer names within
- "↳ Anthony" reply marker: not just a glyph — wrap with `<span class="visually-hidden">Reply from Anthony Porett</span>` for screen readers
- 1-star section: same h2 weight as group headers, no aria-special-handling — equal weight matches the visual treatment

---

## §11 — Performance

- No images on this page (intentional — reviews are the content)
- No JS required for layout (pure CSS)
- Optional: progressive disclosure for the longest reviews (Judy, JEAN JONES) via CSS `details/summary` if total page weight feels heavy. **Default: render all in full.** Long reviews ARE the asset; truncation defeats the purpose.
- Lighthouse target: ≥98 mobile, ≥99 desktop (text-only page)

---

## §12 — Build sequence

1. Copy homepage tokens block — no edits needed
2. Build page header
3. Build curated lead card component (`.review-pair-card`)
4. Build compact variant for groups (`.review-pair-card.compact`)
5. Build archive list item (`.archive-entry`)
6. Render content-inventory data through these components in section order
7. Inject JSON-LD `Review[]` array
8. QA: every review/reply pair from content-inventory appears; no truncation; reply attribution shows date

---

## §13 — Forcing-function check

✅ All 44 corpus reviews accounted for in layout (5 curated + 1 outlier + 31 grouped + 6 archive + Ju B in group 1 = 44)
✅ 1-star handled with equal visual weight to curated leads
✅ Customer-voice forward (review text dominates), owner-voice supporting (reply indented, smaller weight)
✅ No editorial wrappers around the 1-star
✅ Mobile, accessibility, performance specs explicit
✅ Tokens inherited from homepage; no token drift
