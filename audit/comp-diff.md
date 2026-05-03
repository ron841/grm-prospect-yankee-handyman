# Comp vs Build Diff — Yankee Handyman

Comparing [`design-pack/yankee-handyman/Home.html`](../design-pack/yankee-handyman/Home.html) (Design's reference comp) to the live preview at [yankee-handyman-preview-q49slana2-ron-7323s-projects.vercel.app](https://yankee-handyman-preview-q49slana2-ron-7323s-projects.vercel.app/).

The build was authored from Home.html (one-to-one starting point), so structure, copy, and typography match exactly. Material differences are explicit swaps with traceable reasons.

---

## Deviations ranked by severity

### HIGH severity

#### 1. Brand palette — provisional → extracted
**What's different:** Comp ships with provisional `--c-brand: #1a3a5c` (navy) + `--c-accent: #b8392a` (barn red). Build ships with extracted `--c-brand: #5f463b` (warm dark brown) + `--c-accent: #9c6955` (terracotta).
**Why:** k-means on `logo/logo.jpg` (5 clusters, 230k pixels) returned **zero blue clusters at all**. Logo is brown/sepia/tan — wood/craftsman aesthetic. Provisional palette was a guess based on the "Yankee" framing; extraction proved it wrong.
**Recommendation:** **Stay with build.** Slots.md §0 explicitly defers the palette to extraction at build time. Documented in commit `ea3c917` body. Walkthrough should validate against Anthony's truck/uniform/business cards — if his actual brand is something else (red+blue+white "Yankee" stars-and-stripes flavor), swap then.

#### 2. Hero photo — placeholder → real (but weak)
**What's different:** Comp ships with a CSS gradient placeholder + "[ hero photo pending image review ]" overlay text. Build ships with `01-gbp-owner-…llc.jpg` (Anthony installing cement board).
**Why:** Real photo required for ship. Per Ron's brief, hero falls back to owner photos in filename order until walkthrough swaps them.
**Recommendation:** **Replace per [hero-evaluation.md](hero-evaluation.md).** Current photo is below conversion-quality bar.

### MEDIUM severity

#### 3. Pool section photo — placeholder → real (broken promise)
**What's different:** Comp ships gradient placeholder + "[ pool deck — Diane Bennett, 2026 ]" overlay. Build ships `09-gbp-customer-diane-bennett.jpg`.
**Why:** Per Ron's brief: "use the customer-attributed photos (09-gbp-customer-diane-bennett.jpg for pool section)…"
**Problem:** The Diane Bennett photo shows mid-construction wood framing, not a finished pool deck. The committed copy ("Pool decks built like furniture. Most pool decks get framed, screwed down, and called done. Anthony sanded every edge…") expects a finished, finish-carpentry beauty shot. The photo undermines the copy.
**Recommendation:** **Replace.** Either request a real finished-pool-deck photo from Anthony, or re-author the section.

#### 4. Photo grid captions — generic
**What's different:** Comp grid uses placeholder labels ("Pool deck", "Porch enclosure", "Interior tile", "Chandelier circuit", etc.). Build ships with 4 generic "Completed work, 2025" captions on tiles 3–6.
**Why:** Per Ron's brief ("Don't tag subject/usability — that's a human judgment we'll do later"). Captioning was deferred to walkthrough.
**Recommendation:** Tag at walkthrough or after Design photo review. See [photo-audit.md](photo-audit.md) recommendations for per-tile guidance.

#### 5. Form backend — Netlify → Static Forms
**What's different:** Comp form has `data-netlify="true"` + Netlify-style hidden fields. Build form POSTs to `https://api.staticforms.xyz/submit` with hidden `accessKey` / `subject` / `redirectTo` / `honeypot` and inline `fetch()` handler.
**Why:** Per Ron's GRM-standard override. Static Forms is host-agnostic, matches Volthom pattern.
**Recommendation:** **Stay with build.** Documented in commit `68f2c6c`. BUILD-DECISIONS.md was updated in-place to inherit forward.

### LOW severity

#### 6. Visual-comp note overlay removed
**What's different:** Comp has a `.comp-note` div pinned to bottom-left ("VISUAL REFERENCE COMP — provisional brand colors…"). Build has it removed.
**Why:** Production cleanup.
**Recommendation:** Stay with build.

#### 7. `<head>` additions
**What's different:** Comp `<head>` has only title + meta description + font preconnects. Build `<head>` adds OG meta, Twitter Card, canonical, favicon links (64×64 + 32×32 PNG), robots meta, theme-color, and a LocalBusiness JSON-LD schema block.
**Why:** Production SEO + social-share + structured-data requirements not specified in the comp but specified in BUILD-DECISIONS §5–§9.
**Recommendation:** Stay with build.

#### 8. Pending-walkthrough HTML comments at $125 references
**What's different:** Comp has no markers. Build has `<!-- pending-walkthrough: $125 fee — confirm current with Anthony before prod -->` at all 3 fee mentions (trust marquee, plumbing service-card quote, FAQ #1).
**Why:** Per Ron's brief — "Add a clear pending-walkthrough comment in the HTML at every spot the fee appears so it's findable for swap-out later."
**Recommendation:** Stay with build.

#### 9. Generated assets
**What's different:** Comp ships only the HTML. Build ships HTML + `og-image.jpg` (1200×630, hero photo + tagline overlay) + `favicon.png` (64×64) + `favicon-32.png` + `logo.jpg` + `vercel.json` (cache headers + cleanUrls) + `robots.txt` + `sitemap.xml`.
**Why:** Production deploy requirements.
**Recommendation:** Stay with build. The OG image regenerates automatically when hero swaps.

---

## Responsive behavior

| Breakpoint | Comp expectation | Build observation |
|---|---|---|
| 1280px (desktop) | Full 2-col / 7-card / 6-tile layout per slots.md | ✓ matches |
| 1024px (tablet upper) | 2-col stays, contact stacks at 1024 per `--bp-lg` | ✓ matches |
| 768px (tablet lower) | Per slots.md §13: "`--bp-md` to `--bp-lg`: 2-col grids stay 2-col" | **DEVIATION** — at 768 exactly, the `@media (max-width: 768px)` rule fires (max-width is **inclusive**), so mobile mode activates. Tablet 2-col only shows at 769px and above. |
| 375px (mobile) | Single column, sticky call bar visible at bottom | ✓ matches |

**Recommendation on 768px deviation:** Mostly cosmetic — actual tablet devices in 2026 are typically 768+ (iPad mini is 768×1024 portrait, iPad standard is 810+). The edge case is iPhone Plus / Android wide phones at exactly 768. Either change the CSS to `max-width: 767px` (cleaner) or accept that 768 lands in mobile. Low priority.

---

## Things the comp got right that the build preserves

- Section order (Hero → Trust → Services → Pool → Proof → About → FAQ → Contact)
- Type tokens (Merriweather display, Comfortaa eyebrow, Nunito body)
- Type scale (1.250 modular, base 18px)
- Spacing tokens (8px grid)
- All copy verbatim from `content-inventory.md`
- All section IDs and anchor links
- Sticky mobile call bar with `tel:` link
- Service cards (anchor card spans 2 cols on desktop)
- Pool section 7/12 + 5/12 grid
- Proof section 3 quote cards + 6 photo tiles
- About section 720px max-width centered
- FAQ as open-list (not accordion) with 4 items (FAQ #5 license-Q omitted per default)
- Contact 5/12 + 7/12 grid with phone block left, form right
- Footer 3-col with brand / contact / social
- Photo grid 3-col desktop / 2-col mobile
