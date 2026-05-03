# BUILD-DECISIONS — Yankee Handyman LLC

> The technical contract. Hosting, forms, fonts, analytics, structured data, deployment. Read this immediately after `README.md` and before touching `slots.md`.
>
> **What this doc is not:** copy, layout, or visual decisions. Those live in `content-inventory.md` and `slots.md`. This doc is *only* the technical and infrastructure decisions Code needs to make those upstream specs buildable.

---

## §1 — Site type & deploy target

### Site type
- **Static single-page** brochure site
- No CMS, no auth, no user-generated content (form is fire-and-forget)
- Single HTML document at root, served as `index.html`

### Hosting
- **Standard: Vercel** (team scope `ron-7323s-projects`). Non-negotiable per existing GRM infrastructure — matches the Volthom, T&F Electric, and Grandview deployment pattern.
- Reasoning: GRM has standardized on Vercel for all sold-client and prospect-preview contractor sites. Vercel offers the same free-tier story as Netlify (HTTPS, CDN, instant rollback) and integrates with GRM's existing GitHub commit-verification gate.
- **Domain:** `yankeehandyman.com` if available; else subdomain under GRM-managed apex. Confirm at walkthrough. Preview deploys land at `*.vercel.app`.
- **HTTPS:** automatic via Vercel; HSTS preload eligible after 1 year of clean serving
- **WWW handling:** redirect `www.yankeehandyman.com` → `yankeehandyman.com` (or vice-versa — pick one, redirect the other) via Vercel domain config

### Build pipeline
- Source-controlled in a GRM GitHub repo (private until preview, public for Design walkthrough access — see Yankee Handyman intake repo as the pattern)
- Vercel auto-deploys preview on every commit; production deploy is a manual `vercel --prod` after walkthrough confirmation
- No build step required for hand-coded HTML/CSS sites; `vercel.json` at the deploy root configures static serving + cache headers

---

## §2 — Forms

### Form backend
- **Standard: Static Forms** (`api.staticforms.xyz`). Non-negotiable per existing GRM infrastructure — matches the Volthom contact-form pattern.
- Static Forms is host-agnostic (works on Vercel, Netlify, raw S3, anywhere); routes by access key, not host integration.
- Submissions route to the email associated with the access key. No host-coupled form integration.

### Form HTML contract
- POST to `https://api.staticforms.xyz/submit`
- Required fields: hidden `accessKey` (the GRM-issued key for this prospect), plus the visible form fields
- Optional fields: hidden `subject` (email subject line), hidden `redirectTo` (post-submit URL), hidden `honeypot` (spam trap; Static Forms convention is `name="honeypot"` + `display:none`)
- Frontend wires inline `fetch()` POST with JSON body for inline success/error UX (matches `content-inventory.md` `contact.form.success_message` / `error_message_generic`); a regular form POST also works as fallback

### Email destinations
- Static Forms key is provisioned per prospect by GRM ops. Submissions route to whatever email is registered against that key.
- **Yankee Handyman key:** `sf_e0e200934d4f36c17a10d00c` — currently routes to `ron@getrootedmedia.com` (GRM-managed inbox; GRM forwards to Anthony manually until walkthrough confirms his email, then key destination is updated in the Static Forms dashboard)
- **Fallback if Anthony's email is not provided by launch:** keep routing to the GRM mirror; flip after walkthrough

### Spam protection
- Hidden `honeypot` field per Static Forms convention
- No reCAPTCHA at v1 (adds friction; not warranted for expected volume)

---

## §3 — Fonts

### Choices
Per `slots.md §0`:
- Display: **Merriweather** (400 italic, 700)
- Eyebrows: **Comfortaa** (700)
- Body/UI: **Nunito** (400, 600, 700)

All three are SIL Open Font License — free for self-hosting and commercial use.

### Self-host (do not CDN at production)
- Subset to Latin only (drops ~70% of file size)
- Serve as WOFF2 with WOFF fallback
- Use `font-display: swap` on every face
- Preload only the hero-critical face: Merriweather 700 (used in hero headline)
- Total font weight target: <120kb for all 6 faces combined

### File layout
```
/fonts/
  merriweather-700.woff2
  merriweather-400-italic.woff2
  comfortaa-700.woff2
  nunito-400.woff2
  nunito-600.woff2
  nunito-700.woff2
```

### CSS contract
Define `@font-face` declarations in a single block at the top of the stylesheet. Use the family names exactly as `slots.md §0` specifies (`'Merriweather'`, `'Comfortaa'`, `'Nunito'`).

---

## §4 — Analytics & tracking

### Analytics platform
- **Recommended: Google Analytics 4** (GRM standard if applicable)
- GA4 measurement ID provisioned by GRM, dropped into the page head
- Cookie consent: not legally required in FL for GA4; skip the cookie banner unless GRM policy requires one

### Critical events to track
The whole site is phone-primary. The conversion model is **phone clicks**, not form submissions. Wire these GA4 events:

| Event name | Trigger | Payload |
|---|---|---|
| `phone_click` | Click on any `tel:` link | `{ location: 'hero' \| 'nav' \| 'contact' \| 'sticky' \| 'faq' \| '404' }` |
| `form_submit` | Successful form submission | `{ contact_preference: '...' }` |
| `form_error` | Form submission error | `{ error_type: '...' }` |
| `cta_click` | Click on hero secondary CTA ("See What He's Done") | `{}` |
| `service_card_view` | Service card scrolled into viewport | `{ service_id: '...' }` (optional, only if measuring engagement) |
| `outbound_facebook` | Click on Facebook footer link | `{}` |
| `outbound_google_reviews` | Click on GBP reviews link | `{}` |

### Call tracking (optional, recommend defer)
- A call-tracking number (CallRail, Twilio) lets GRM attribute phone calls back to the website specifically
- **Recommend defer to v2** — adds cost ($30+/month per number) and Anthony has used his real number for years; swapping it on the site only would split his call data
- If GRM standard practice is to install call tracking on launch, follow that standard. Otherwise skip.

---

## §5 — Structured data (schema.org JSON-LD)

Critical for a contractor whose pitch leans on review proof. Drop a single JSON-LD block at the bottom of `<head>`.

### LocalBusiness + aggregateRating
```json
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "name": "Yankee Handyman LLC",
  "alternateName": "The Yankee Handyman",
  "telephone": "+1-239-867-8447",
  "email": "[pending-walkthrough]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "6726 Cherry Rd",
    "addressLocality": "Ocala",
    "addressRegion": "FL",
    "postalCode": "34472",
    "addressCountry": "US"
  },
  "areaServed": [
    { "@type": "City", "name": "Ocala" },
    { "@type": "AdministrativeArea", "name": "Marion County" }
  ],
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "08:00",
      "closes": "17:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "09:00",
      "closes": "17:00"
    }
  ],
  "priceRange": "$",
  "url": "https://yankeehandyman.com",
  "image": "https://yankeehandyman.com/[hero-image-filename]",
  "logo": "https://yankeehandyman.com/logo.jpg",
  "founder": {
    "@type": "Person",
    "name": "Anthony Porett"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "50",
    "bestRating": "5",
    "worstRating": "1"
  },
  "sameAs": [
    "https://www.facebook.com/TheYankeeHandymanLLC/"
  ]
}
```

### Notes
- `@type` = `HomeAndConstructionBusiness` (most specific schema.org type that fits handyman)
- `priceRange` = `"$"` (single dollar — signals affordability per the $125 service-call fee story)
- `aggregateRating.ratingValue` and `reviewCount` must match what's displayed visually (per `synthesis.md §4`)
- `sameAs` adds Instagram and GBP URL once verified at walkthrough
- Update `aggregateRating` quarterly (at minimum) — Google rich-results penalize stale ratings

### Verification
- Test with [Google Rich Results Test](https://search.google.com/test/rich-results) before launch
- Submit to Google Search Console after deploy
- Submit a sitemap (`sitemap.xml`) — single URL is fine (`/`)

---

## §6 — Open Graph & Twitter Cards

### Open Graph (per `content-inventory.md` `meta.og_*`)
```html
<meta property="og:title" content="Yankee Handyman — Ocala">
<meta property="og:description" content="Creating Beautiful Spaces and Smiling Faces. Fifty Marion County customers, 4.9 stars on Google.">
<meta property="og:image" content="[hero-image-1200x630-with-overlay]">
<meta property="og:url" content="https://yankeehandyman.com">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
```

### Twitter Card
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Yankee Handyman — Ocala">
<meta name="twitter:description" content="Creating Beautiful Spaces and Smiling Faces.">
<meta name="twitter:image" content="[same as og:image]">
```

### OG image production
- Render at 1200×630
- Use the same hero photo as the page hero, with the dark gradient overlay AND the tagline overlaid as text (per `content-inventory.md` `meta.og_image` build instruction)
- Save as JPEG, target <200kb

---

## §7 — Performance budget

Per `slots.md §15`. Hard targets:

| Metric | Mobile target | Desktop target |
|---|---|---|
| Lighthouse Performance | ≥ 95 | ≥ 98 |
| Lighthouse Accessibility | 100 | 100 |
| Lighthouse Best Practices | 100 | 100 |
| Lighthouse SEO | 100 | 100 |
| First Contentful Paint | < 1.2s | < 0.8s |
| Largest Contentful Paint | < 2.0s | < 1.5s |
| Cumulative Layout Shift | < 0.05 | < 0.05 |
| Total page weight (above fold) | < 500kb | < 800kb |
| CSS file (min+gz) | < 40kb | < 40kb |
| JS file (min+gz) | < 20kb | < 20kb |

### Image optimization
- Hero: WebP + JPEG fallback, ~150kb max at 1920×1080
- All other images: WebP, ~80kb max each
- Run all photos through Squoosh or equivalent before commit
- `loading="lazy"` on all images except hero

### JS minimization
- No framework. Vanilla JS only.
- Three concerns total: nav scroll behavior, form validation, mobile disclosure menu
- Single bundled JS file, defer-loaded

---

## §8 — Accessibility compliance

Per `slots.md §14`. Hard targets:

- WCAG 2.2 AA compliance
- Color contrast ≥ 4.5:1 for body text, ≥ 3:1 for large text and UI elements
- All interactive elements keyboard-accessible (no mouse-only flows)
- Focus indicators always visible (never `outline: none` without replacement)
- Form labels always present (no placeholder-only labels)
- `<html lang="en">` set
- `prefers-reduced-motion: reduce` honored (disables any scroll-linked or animated effects)

### Verification
- axe DevTools scan must show zero violations before launch
- Keyboard-only walkthrough: tab through every interactive element start to finish without getting stuck

---

## §9 — SEO foundation

### On-page
- One `<h1>` per page (hero only)
- `<title>` and `<meta name="description">` per `content-inventory.md` `meta.*`
- Canonical URL: `<link rel="canonical" href="https://yankeehandyman.com/">`
- Robots: `<meta name="robots" content="index, follow">`

### Off-page
- Submit to Google Search Console
- Submit `sitemap.xml` (single-URL sitemap is fine)
- Verify Google Business Profile is linked to the site (Anthony likely already has GBP set up; confirm URL field points to new domain at launch)

### Local SEO
- LocalBusiness JSON-LD per §5 above
- Address consistent across site, GBP, Facebook page (NAP consistency)
- Embed Google Map on contact section (already specced in `slots.md §10`)

---

## §10 — Browser support

Target: last 2 major versions of:
- Chrome / Edge (Chromium)
- Safari (incl. iOS Safari)
- Firefox

Do NOT support:
- IE 11 (dead)
- Opera Mini (negligible traffic for a Marion County contractor)
- UC Browser (negligible traffic)

CSS features used freely:
- CSS Grid (full support)
- CSS Custom Properties (full support)
- `aspect-ratio` (full support since 2021)
- `gap` on flex (full support since 2021)

CSS features to avoid:
- `:has()` selector (use it only where progressive enhancement is fine — Safari < 15.4 lacks support but those users are vanishingly rare)
- Container queries (overkill for this build)

---

## §11 — Deployment & launch checklist

Before flipping DNS to the new site:

- [ ] Open decisions in `README.md` resolved with Anthony
- [ ] $125 service-call fee confirmed current
- [ ] Hero photo selected and image-reviewed
- [ ] Logo color extracted and `--c-brand` token set
- [ ] Form backend tested end-to-end (submit → arrives at Anthony's email + GRM mirror)
- [ ] Phone link tested on iOS + Android (taps `tel:` correctly)
- [ ] Lighthouse scores meet §7 targets
- [ ] axe DevTools shows zero violations
- [ ] Rich Results Test passes for LocalBusiness
- [ ] Google Search Console verified
- [ ] GA4 firing on `phone_click` and `form_submit` confirmed
- [ ] Facebook page link confirmed live
- [ ] GBP URL field updated to new domain
- [ ] Visual diff against `Home.html` comp reviewed by GRM design

### After DNS flip
- [ ] HTTPS active with valid cert
- [ ] HTTP → HTTPS redirect working
- [ ] WWW handling per §1 working
- [ ] 404 page renders per `content-inventory.md` `404.*`
- [ ] Phone clicks attributing in GA4

---

## §12 — Things this doc does *not* decide

These are real decisions that will surface during build but belong elsewhere:

| Decision | Owner | Where it gets resolved |
|---|---|---|
| Logo color extraction (which hex is `--c-brand`) | Code at build time | Mechanical — extract from `logo/logo.jpg` |
| Photo selection (which of 10 photos goes where) | GRM design + Anthony | Walkthrough |
| Whether to ship FAQ #5 (license question) | Anthony | Walkthrough |
| Pool deck quote: paraphrase or verbatim | Anthony | Walkthrough |
| Anthony's email | Anthony | Walkthrough |
| Instagram handle | Anthony | Walkthrough |
| ~~Specific Netlify or Vercel preference~~ | ~~GRM ops~~ | **Resolved: Vercel is GRM standard. See §1.** |
| GA4 measurement ID | GRM ops | Provisioned at deploy time |
| Domain ownership / DNS access | Anthony or GRM | Pre-launch |

---

## §13 — Forcing-function check

✅ Every technical concern Code might surface during build is decided here, OR explicitly punted to a named owner.
✅ No "figure it out at build" decisions remain.
✅ Performance, a11y, and SEO targets are numeric and testable.
✅ Deploy and launch flow is explicit, not implicit.

If a Code agent reads this doc and still has a "what do I do about X" question, that's a gap — flag it back to design.
