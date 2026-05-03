# SLOTS — Yankee Handyman LLC

> Build spec. Maps content-inventory slots to a single-page layout with explicit section composition, type/spacing/color tokens, component rules, and responsive behavior. Consumed by Code at build time.
>
> **Authority chain:** synthesis → content-inventory → SLOTS → build. SLOTS does not re-litigate copy or voice — both are locked upstream. SLOTS only resolves *layout, hierarchy, type, color, spacing, behavior*.
>
> **Persona inheritance:** Neighborhood steady (primary) + Quiet confidence (secondary). Drives layout density (medium), type-scale ratio (1.250 modular), and color saturation (low-mid).
>
> **Page model:** single-page scroll. No multi-page routing. Section anchors only: `#services`, `#proof`, `#about`, `#contact`. Pool decks reachable via `#proof` (it's a sub-section).

---

## §0 — Tokens

### Type

```
--font-display: 'Merriweather', Georgia, serif;
--font-eyebrow: 'Comfortaa', system-ui, sans-serif;
--font-body:    'Nunito', system-ui, sans-serif;
```

**Scale (1.250 modular, base 18px):**

| Token | Size | Line-height | Use |
|---|---|---|---|
| `--t-eyebrow` | 13px | 1.4 | section eyebrows, ALL CAPS, letter-spacing 0.20em |
| `--t-body-sm` | 16px | 1.5 | captions, footer, microcopy |
| `--t-body` | 18px | 1.6 | body paragraphs |
| `--t-body-lg` | 20px | 1.55 | hero supporting line, pool-section body |
| `--t-h4` | 22px | 1.4 | service-card labels, FAQ Q |
| `--t-h3` | 28px | 1.3 | trust marquee items, proof attribution |
| `--t-h2` | 40px | 1.2 | section headlines |
| `--t-h1` | 56px | 1.15 | hero headline (mobile: 36px) |
| `--t-display` | 72px | 1.1 | reserved, unused on this build |

**Weights:**
- Merriweather: 400 (italic body), 700 (display)
- Comfortaa: 700 (eyebrows only)
- Nunito: 400 (body), 600 (UI labels), 700 (CTAs)

**Universal rule:** no em dashes anywhere on page (per GRM). Use periods, commas, semicolons.

### Color

Palette derived from logo (`logo/logo.jpg`) — extraction at build time. Provisional values below; replace `--c-*` hexes with extracted values when logo color extraction completes.

```
--c-ink:        #1a1a1a;   /* primary text */
--c-ink-soft:   #4a4a4a;   /* secondary text */
--c-paper:      #fafaf7;   /* page bg, warm off-white */
--c-paper-2:    #f0ede4;   /* alt section bg */
--c-line:       #e0dccf;   /* hairlines, dividers */

--c-brand:      #pending;  /* extracted from logo — likely navy or deep red per "Yankee" framing */
--c-brand-soft: #pending;  /* 0.15 alpha overlay tint */
--c-accent:     #pending;  /* secondary logo color */

--c-success:    #2d6a4f;   /* form success */
--c-error:      #9b2c2c;   /* form error */
```

**Build instruction:** at logo extraction, the dominant non-neutral color becomes `--c-brand`. If the logo is monochrome or dark navy/black, set `--c-brand` to the darkest non-black hue; if no second color, leave `--c-accent` unset and use `--c-ink` for accent zones.

### Spacing

8px base grid. Section vertical rhythm:

```
--s-1: 4px;    --s-2: 8px;    --s-3: 12px;
--s-4: 16px;   --s-5: 24px;   --s-6: 32px;
--s-7: 48px;   --s-8: 64px;   --s-9: 96px;
--s-10: 128px;
```

Section padding: `--s-9` top/bottom desktop, `--s-7` mobile.
Container max-width: 1200px desktop, 92vw mobile, padded `--s-6` lateral.

### Radii / lines

```
--r-sm: 4px;     --r-md: 8px;     --r-lg: 16px;
--line: 1px solid var(--c-line);
```

No heavy shadows. At most a 0 1px 2px rgba(0,0,0,0.04) on form inputs and CTA buttons. Neighborhood steady persona forbids elevation theater.

---

## §1 — Page structure

```
<header.nav> (sticky, 72px)
<main>
  §1 Hero               (full-width, 88vh min, image right OR background)
  §2 Trust marquee      (full-width, --c-paper-2 bg, 96px tall)
  §3 Services           (container, 7 service cards in 2-col → 1-col grid)
  §4 Pool decks         (full-width feature, image-left + body-right)
  §5 Proof              (container, 3 quote cards + 6-photo grid below)
  §6 About              (container, 2 paragraphs centered, optional photo)
  §7 FAQ                (container, 5 Q&A in accordion or open list)
  §8 Contact            (container split: phone block left, form right)
</main>
<footer> (3-col desktop, stacked mobile)
<div.sticky-call-bar> (mobile only, fixed bottom)
```

Section order is locked per synthesis §9. **Do not reorder.** Pool decks lives between Services and Proof so the strongest portfolio claim immediately follows the umbrella service framing.

---

## §2 — Header / nav

### Layout

```
[ logo (32px) | brand-text (visible <md) ]    [ Services  Proof  About  Contact ]    [ ☎ Call (239) 867-8447 ]
```

- Height: 72px desktop, 56px mobile
- Background: `--c-paper` with 0.92 alpha + 12px backdrop-blur on scroll past 80px
- Border-bottom: `--line` (only after scroll trigger)
- Logo: 32px square, link to `#top`
- Nav links: Nunito 600, 16px, gap 32px desktop. Hide on mobile, show in disclosure menu.
- Phone CTA: Nunito 700, 15px, with phone glyph (Lucide `phone` at stroke 1.5px). On mobile, collapses to icon-only.

### Behavior

- Sticky from scroll position 0
- Active section indicator: 2px underline below nav link matching current `#anchor` via IntersectionObserver
- Disclosure menu (mobile): full-screen overlay with 4 nav links stacked + phone CTA at bottom

---

## §3 — Hero

### Layout option: image-background (default)

```
[full-width container, 88vh min height, 600px min]
  background: hero.image with 2-axis gradient overlay
    - top→bottom: rgba(0,0,0,0.35) → rgba(0,0,0,0.65)
    - left→right: rgba(0,0,0,0.55) → rgba(0,0,0,0.10)
  content sits in left half, vertically centered, max-width 640px

  [eyebrow]
  [h1 headline]
  [supporting-line]
  [trust-line]
  [cta-row: primary | secondary]
```

### Type & color

- Eyebrow: `--t-eyebrow`, Comfortaa 700, color `rgba(255,255,255,0.85)`, letter-spacing 0.20em, margin-bottom `--s-5`
- Headline: `--t-h1` (56px desktop, 36px mobile), Merriweather 700, color `#fff`, line-height 1.15, max-width 640px, margin-bottom `--s-4`
- Supporting line: `--t-body-lg` (20px), Merriweather 400 italic, color `rgba(255,255,255,0.92)`, margin-bottom `--s-5`
- Trust line: `--t-body` (18px), Nunito 600, color `rgba(255,255,255,0.85)`, margin-bottom `--s-7`
- CTA primary: filled `--c-brand`, Nunito 700, 16px, padding `--s-4 --s-6`, radius `--r-md`
- CTA secondary: ghost (border 1px solid `rgba(255,255,255,0.5)`, color `#fff`), same padding/radius

### Image instruction

- Source: `hero.image` from content-inventory (currently `pending-image-review` — Diane Bennett pool deck OR Cole Spires porch)
- Aspect: cover full container, focal-point 30% from left (so headline copy sits over the dark side, photo subject sits right)
- If no photo passes review at walkthrough: fall back to `--c-ink` solid background, drop image, increase headline weight presence with `--t-display` (72px)

### Mobile

- Image is full-bleed, 70vh
- Content shifts to bottom-aligned, padding `--s-7` lateral
- Headline drops to 36px
- CTAs stack vertically, full-width

---

## §4 — Trust marquee

### Layout

Full-width strip, `--c-paper-2` background, 96px tall, vertically centered content.

```
[ ★ 50 reviews · 4.9 stars ]   |   [ ✓ Bellechase homeowners ]   |   [ ⚡ Same-day when scheduled ]   |   [ $ $125 flat service call ]
```

- 4 items in single row desktop, separated by 1px vertical dividers (`--c-line`)
- Each item: Nunito 600, 16px, color `--c-ink-soft`, with small icon (12px, stroke 1.5) in `--c-brand`
- Mobile: horizontal scroll, snap-to-item, item width 70vw

### Behavior

- Static row desktop (no auto-scroll — Neighborhood steady persona forbids motion theater)
- Mobile: native horizontal scroll only, no auto-advance

---

## §5 — Services

### Layout

```
[container, padding-top --s-9]
  [eyebrow]
  [h2 headline]
  [subhead body-lg, max-width 640px]

  [grid, 2-col desktop, 1-col mobile, gap --s-6, margin-top --s-8]
    [service-card × 7]

  [cta button, centered, margin-top --s-8]
```

### Service card composition

```
[card, padding --s-6, background --c-paper, border --line, radius --r-lg]
  [label, t-h4, Merriweather 700]
  [blurb, t-body, Nunito 400, color --c-ink-soft, margin-top --s-3]
  [evidence-quote (if present), t-body-sm italic, color --c-ink-soft, margin-top --s-4, border-top --line, padding-top --s-4]
  [evidence-citation (if present), t-eyebrow, color --c-ink-soft, margin-top --s-2]
```

- No icons on cards (Neighborhood steady persona — forbids icon-soup, lets type and copy carry)
- Cards do not have hover lift; use 1px border darkening on hover only
- "General handyman work" card spans 2 cols on desktop (anchor card with strongest evidence)

### Type per element

- Card label: `--t-h4` (22px), Merriweather 700, color `--c-ink`
- Blurb: `--t-body` (18px), Nunito 400, color `--c-ink-soft`, line-height 1.6
- Evidence quote: `--t-body-sm` (16px), Merriweather 400 italic, color `--c-ink-soft`
- Citation: `--t-eyebrow` (13px), Comfortaa 700, color `--c-ink-soft`, letter-spacing 0.15em

### Mobile

- Single column, full container width
- Anchor card no longer spans 2 cols (single column anyway)

---

## §6 — Pool decks (feature section)

### Layout

Full-width section, `--c-paper-2` background, padding `--s-10` top/bottom desktop.

```
[container, 2-col grid, gap --s-8]
  [left col (image, 7/12 cols)]
    [pool_section.image, full-width, aspect 4/3, radius --r-lg]
    [caption, t-body-sm, color --c-ink-soft, margin-top --s-3]
  [right col (body, 5/12 cols)]
    [eyebrow]
    [h2 headline]
    [body, t-body-lg, max-width 480px]
    [evidence-quote block, margin-top --s-7]
      [quote, Merriweather italic, t-h3, lowercase per GRM rule]
      [attribution, t-eyebrow, margin-top --s-4]
```

### Type

- Headline: `--t-h2` (40px), Merriweather 700
- Body: `--t-body-lg` (20px), Nunito 400, line-height 1.55
- Quote: `--t-h3` (28px), Merriweather 400 italic, line-height 1.35, color `--c-ink`
- Attribution: `--t-eyebrow`, Comfortaa 700, color `--c-ink-soft`

### Mobile

- Stack vertically: image first, body below, gap `--s-6`
- Image aspect stays 4/3
- Quote stays at 28px (don't shrink — it's the moneyline)

---

## §7 — Proof

### Layout

```
[container, padding --s-9 top/bottom]
  [eyebrow]
  [h2 headline]
  [subhead]
  [bellechase-callout, padding --s-5, --c-paper-2 bg, border-left 3px solid --c-brand, radius --r-md, margin-top --s-6]

  [quote-grid, 3-col desktop, 1-col mobile, gap --s-6, margin-top --s-8]
    [quote-card × 3]

  [photo-grid, 3-col desktop, 2-col mobile, gap --s-4, margin-top --s-9]
    [photo-tile × 6]
```

### Quote card composition

```
[card, padding --s-6, background --c-paper, border --line, radius --r-lg]
  [quote, Merriweather 400 italic, t-body-lg, color --c-ink]
  [attribution-row, margin-top --s-5, border-top --line, padding-top --s-4]
    [name, Nunito 600, t-body]
    [role/job, t-eyebrow, color --c-ink-soft]
```

### Photo tile composition

```
[tile, aspect-1/1 desktop OR 4/3 mobile, radius --r-md, overflow hidden]
  [img, object-fit cover]
  [caption-strip, position absolute bottom, padding --s-3 --s-4, background gradient bottom→top rgba(0,0,0,0.7) → transparent]
    [caption, Nunito 600, t-body-sm, color #fff]
```

### Mobile

- Quote cards stack vertically
- Photo grid: 2 columns
- Bellechase callout stays full-width

---

## §8 — About

### Layout

```
[container, max-width 720px, centered, padding --s-9 top/bottom]
  [eyebrow, centered]
  [h2 headline, centered, t-h2]
  [body paragraphs, t-body-lg, max-width 640px, centered, margin-top --s-7]
    [paragraph 1]
    [gap --s-5]
    [paragraph 2]
  [optional image, centered, margin-top --s-8, max-width 480px, aspect 4/3 OR 1/1]
```

### Type

- Headline: `--t-h2` (40px), Merriweather 700, color `--c-ink`, text-align center
- Body: `--t-body-lg` (20px), Nunito 400, line-height 1.6, color `--c-ink`

### Mobile

- All centered
- Body line-length stays at 640px max (becomes 92vw on small screens)

### If no About image at walkthrough

- Drop the image slot entirely
- Body becomes the section's full visual weight
- Section padding stays `--s-9`

---

## §9 — FAQ

### Layout

```
[container, max-width 720px, padding --s-9 top/bottom]
  [eyebrow]
  [headline-lead-in, t-body-lg, color --c-ink-soft]
  [h2 headline, margin-top --s-3]

  [faq-list, margin-top --s-8]
    [faq-item × 5]
```

### FAQ item composition

Default to **open list** (not accordion) — Neighborhood steady persona reads cleaner with everything visible. Saturday Morning lead-in implies "tell me up front."

```
[item, padding --s-6 0, border-bottom --line]
  [Q, t-h4, Merriweather 700, color --c-ink]
  [A, t-body, Nunito 400, color --c-ink-soft, margin-top --s-3, line-height 1.7]
```

### Type

- Q: `--t-h4` (22px), Merriweather 700
- A: `--t-body` (18px), Nunito 400, line-height 1.7

### License Q (item 5) instruction

- At first build: **omit entirely** if `pending-walkthrough` unresolved (per content-inventory build instruction)
- After walkthrough: if confirmed, render as standard item; if Anthony declines to confirm, leave omitted

### Mobile

- Same layout, `--s-6` lateral padding
- Q stays 22px

---

## §10 — Contact

### Layout

```
[container, padding --s-9 top/bottom]
  [eyebrow]
  [h2 headline]
  [subhead, t-body-lg, max-width 540px]

  [grid, 2-col desktop (5/12 + 7/12), 1-col mobile, gap --s-8, margin-top --s-8]
    [left col]
      [phone-block]
        [label "Call", t-eyebrow]
        [number, t-h2 size, Merriweather 700, --tel: link]
        [subline hours, t-body, color --c-ink-soft]
      [address-block, margin-top --s-7]
        [label "Based in", t-eyebrow]
        [address line 1, t-body-lg]
        [address line 2, t-body-lg]
        [map link, t-body, color --c-brand, with → glyph]
    [right col]
      [form]
```

### Phone block emphasis

The phone number gets `--t-h2` (40px) treatment — matches sectional headlines. This is intentional: synthesis §5 made phone primary CTA, and the contact section foregrounds it visually rather than hiding it under form-equivalent weight.

### Form composition

```
[form, padding --s-6, background --c-paper-2, border --line, radius --r-lg]
  [headline, t-h4]
  [field-group, margin-top --s-5]
    [label, t-eyebrow style: Comfortaa 700, 13px, letter-spacing 0.10em, color --c-ink-soft]
    [input/textarea, padding --s-4, border --line, radius --r-md, font-body, t-body, focus state: border --c-brand]
    [validation message slot, t-body-sm, color --c-error, hidden until error]
  [field-group × 4]
  [submit button, full-width, --c-brand bg, color #fff, t-body Nunito 700, padding --s-4 --s-6, radius --r-md, margin-top --s-6]
  [success/error message, t-body, hidden until submit]
```

### Field-specific notes

- `name`: text input, autocomplete `name`
- `phone`: tel input, autocomplete `tel`, format mask `(###) ###-####`
- `job_description`: textarea, 4 rows minimum, autocomplete `off`
- `contact_preference`: 3-option segmented control (radio styled as button group), default "Either"

### Form submission behavior

Form posts to a build-time-configured endpoint (mailto fallback if no backend). Synthesis-committed contract:
- Success message shown inline, form clears
- Error message shown inline with phone fallback CTA

### Mobile

- Single column
- Phone block stacks above address, then form
- Submit button stays full-width

---

## §11 — Footer

### Layout

```
[full-width, --c-ink background, color --c-paper, padding --s-9 top, --s-6 bottom]
  [container, 3-col desktop, 1-col mobile, gap --s-7]
    [col 1: tagline]
      [logo white version, 32px]
      [tagline, t-body, max-width 320px, margin-top --s-5]
    [col 2: contact-block]
      [label "Reach Anthony", t-eyebrow, color rgba(255,255,255,0.6)]
      [phone, t-body-lg, --tel: link]
      [address, t-body, color rgba(255,255,255,0.8)]
      [hours, t-body, color rgba(255,255,255,0.8)]
    [col 3: social + reviews]
      [label "Find him online", t-eyebrow, color rgba(255,255,255,0.6)]
      [facebook link, t-body]
      [google reviews link, t-body]
      [instagram link, t-body — omit if pending]

  [bottom-bar, border-top rgba(255,255,255,0.1), padding-top --s-5, margin-top --s-8]
    [copyright, t-body-sm, color rgba(255,255,255,0.6)]
    [built-by, t-body-sm, color rgba(255,255,255,0.6), text-align right desktop]
```

### Mobile

- Stack 3 cols vertically
- Bottom bar stays at bottom, copyright + built-by stack with `--s-3` gap

---

## §12 — Sticky mobile call bar

### Layout

```
[fixed bottom 0, full-width, --c-brand bg, color #fff, padding --s-4]
  [centered: phone glyph + "Call (239) 867-8447", Nunito 700, t-body-lg]
```

- Visible only on viewport <768px
- Persistent — does not hide on scroll
- Adds 64px bottom padding to `<main>` to prevent content overlap
- Tap target: full bar, opens `tel:+12398678447`

---

## §13 — Responsive breakpoints

```
--bp-sm:  480px
--bp-md:  768px   /* mobile → tablet transition */
--bp-lg:  1024px  /* tablet → desktop */
--bp-xl:  1280px  /* desktop → wide */
```

- Below `--bp-md`: single-column everywhere, mobile sticky CTA on, nav collapses to disclosure
- `--bp-md` to `--bp-lg`: 2-col grids stay 2-col, hero gets reduced top padding, type-scale unchanged
- Above `--bp-lg`: full desktop layout
- Above `--bp-xl`: container max-width caps at 1200px, content does not stretch

---

## §14 — Accessibility

- Skip link at top: "Skip to main content" → `#main`
- Heading hierarchy: one `<h1>` (hero only), `<h2>` per section, `<h3>` reserved for sub-claims (pool quote, FAQ Q can be h3 or styled-only)
- All interactive elements: 44px minimum tap target on mobile (sticky bar = 56px tall)
- Focus state: 2px outline `--c-brand` with 2px offset on all interactive elements; never remove
- Color contrast: ink-on-paper ≥ 11:1, ink-soft-on-paper ≥ 7:1, white-on-brand ≥ 4.5:1 (verify at logo extraction — if `--c-brand` extracts too light, use `--c-ink` for high-contrast surfaces)
- Form labels: always present, never placeholder-only
- Reduced motion: honor `prefers-reduced-motion: reduce` — disables nav-active underline animation, scroll-linked effects (none currently used)

---

## §15 — Performance

- Hero image: `<picture>` with WebP + JPEG fallback, lazy=eager (above fold)
- All other images: `loading="lazy"`, WebP preferred
- Fonts: `font-display: swap` for Merriweather, Nunito, Comfortaa
- Subset Google Fonts to Latin only
- No JS framework needed for this build — vanilla JS for nav scroll, form validation, mobile disclosure
- CSS file target: <40kb min+gz
- Total page weight target: <500kb above fold (excluding hero image)

---

## §16 — Build-order checklist (for Code)

1. Resolve logo → extract `--c-brand` and `--c-accent`. If extraction fails or palette is monochrome, set `--c-brand` to `#1a3a5c` (provisional navy) and flag for walkthrough.
2. Resolve hero image. If no candidate passes review at walkthrough time, fall back to ink solid background (per §3 instructions).
3. Build §0 tokens as CSS custom properties in a single `:root` block.
4. Build sections §3 through §11 in document order.
5. Build §12 sticky bar (mobile) last.
6. Wire `tel:+12398678447` on every phone reference (hero CTA, nav CTA, contact phone, sticky bar, 404, 500).
7. Wire form submission endpoint (mailto fallback if no backend at build).
8. Verify §14 contrast ratios after color extraction.
9. Run §15 performance pass: Lighthouse target ≥ 95 mobile, ≥ 98 desktop.

---

## §17 — Deferred resolutions (carried from content-inventory)

| Slot | State | Resolution path |
|---|---|---|
| Photo selections (hero, proof grid 4 owner-uploaded, pool, about, OG) | pending-image-review | Walkthrough with image review |
| License/insurance line (trust marquee + FAQ #5) | pending-walkthrough | Confirm with Anthony; default to omit |
| Phone-answering subhead exact wording | pending-walkthrough partial | Confirm phone behavior; revise if needed |
| Instagram footer link | pending-walkthrough | Verify handle exists |
| Logo color extraction | pending-extraction | Build step before §3+ |
| GBP listing URL | pending-extraction | From `place-details-raw.json` |
| Favicon | pending-extraction | Vectorize logo OR raster crop |
| Pool deck Diane Bennett quote (paraphrase vs verbatim) | pending-walkthrough | Confirm wording with Anthony or source |
| Service-call fee currency ($125 flat) | walkthrough-critical | **Confirm number is current** before publish |

---

## §18 — Forcing-function check (to Code)

✅ Every section has explicit layout, type tokens, color tokens, spacing tokens.
✅ Every responsive breakpoint behavior is specified.
✅ Every interactive element has accessibility spec.
✅ Every deferred slot has explicit fallback behavior at build.
✅ No re-litigation of upstream commitments (copy, voice, persona, content-inventory citations all preserved).
✅ Build-order is explicit and check-able.
✅ Performance and a11y targets are numeric and testable.

**Five docs in `yankee-handyman/`:** `intake.md`, `intake-template.md`, `synthesis.md`, `content-inventory.md`, `slots.md`. Ready for Code.
