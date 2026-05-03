# Open Decisions Status — Yankee Handyman

Walks the 8 pending-walkthrough decisions from the README open-decisions table. For each: did the build use the documented fall-through? Is the marker findable for swap-out at walkthrough?

---

| # | Decision | Build status | Marker findability |
|---|---|---|---|
| 1 | **Confirm $125 flat service-call fee is current** | **Shipped as-is per Ron's exception ("preview only — flag for walkthrough confirmation").** The fee appears in 3 spots, all wrapped with HTML comments. | **3 markers in HTML.** Grep `pending-walkthrough` finds them at: trust marquee 4th item; plumbing service-card evidence quote; FAQ #1 answer. |
| 2 | Anthony's email | Fall-through used. Static Forms accessKey `sf_e0e200934d4f36c17a10d00c` currently routes to ron@getrootedmedia.com (GRM mirror). | Not in HTML — config lives in Static Forms dashboard. Walkthrough action: get Anthony's email, update the key destination in dashboard. |
| 3 | License/insurance verification | Fall-through used. **FAQ #5 omitted entirely** per content-inventory build instruction. Trust marquee credential line absent (was never added — content-inventory's trust marquee item 4 went to the $125 fee instead). | 1 marker in HTML — the FAQ list contains an `<!-- License Q omitted per content-inventory build instruction (pending-walkthrough) -->` comment where FAQ #5 would be. Grep `License Q omitted` finds it. |
| 4 | Phone-answering pattern | Fall-through used. Shipped contact subhead per content-inventory: "Phone is fastest. He answers most calls during business hours and returns voicemails the same day." | Not marked in HTML — copy is shipped as final unless Anthony's actual pattern differs at walkthrough. The subhead text itself is the swap target. |
| 5 | Instagram handle verification | Fall-through used. Footer IG link **omitted** per content-inventory build instruction. | Not marked in HTML — IG col is just absent. Walkthrough action: verify the `@the.yankee.handyman.llc` handle the web search surfaced; if real, add an `<li>` to footer "Find Him Online" col. |
| 6 | Photo selections (10-photo library) | **Per Ron's preview rule (not the README fall-through):** customer photos primary placement (09 pool, 10 porch); owner photos in filename order for hero + grid backfill. The README fall-through ("hero falls back to ink-solid background, proof grid contracts to 4") was NOT used because Ron explicitly overrode it for preview build. | 1 marker in HTML — the photo-grid intro carries `<!-- Photo grid: customer-attributed photos first, then owner photos. Subjects/captions pending walkthrough — re-author per actual photo content. -->`. Grep `pending walkthrough` (no hyphen) finds it. **Photo-selection swap is the highest-priority Design action per [photo-audit.md](photo-audit.md).** |
| 7 | Pool deck Diane Bennett quote (paraphrase vs verbatim) | Fall-through used. Shipped paraphrase from intake §Voice — Review 6: "He sanded all the edges and cut a curve around the pool. The price was fair. I had three other quotes." | Not marked in HTML — copy ships as final. Swap target is the visible quote text. Walkthrough action: ask Anthony if he has Diane's actual review text (or screenshot) to confirm/replace the paraphrase. |
| 8 | Owner/team identification ("two men, one truck") | Fall-through used. About section + footer ship "him and one other guy" / "Anthony Porett and one other guy" without naming the second person. | Not marked in HTML — copy ships as final. Swap target is the visible "one other guy" phrasing. Walkthrough action: ask Anthony for his teammate's first name; swap "one other guy" for the name (e.g. "Anthony and Jake"). |

---

## Summary

**8 of 8 decisions handled.** No decision was left ambiguous. 5 markers exist in HTML for items where future swap requires a code change (3 fee, 1 license-omission breadcrumb, 1 photo-grid intro).

**Walkthrough blockers for prod (not preview):**
- **#1 (the $125 fee)** is the README's gating decision before prod. Markers are in place; preview ships the current value with HTML breadcrumbs. **Confirm with Anthony before flipping `vercel deploy --prod`.**

**Walkthrough actions for sign-off (no code change required):**
- #2 — get Anthony's email, update Static Forms dashboard
- #4 — confirm phone-answering subhead is accurate (or revise)
- #5 — verify IG handle, add link if real
- #7 — get Diane's verbatim quote if available
- #8 — get teammate name

**Walkthrough actions that do require code change:**
- #1 — fee value if changed
- #3 — FAQ #5 license answer if Anthony confirms
- #6 — photo selections (per Design's [photo-audit.md](photo-audit.md) recommendations)

---

## Marker grep cheat sheet

```bash
# Find all pending-walkthrough HTML comments in the build
grep -nE 'pending-walkthrough|pending walkthrough|License Q omitted' build/index.html
```

Returns 5 lines as of audit time:
- Line ~ trust marquee 4th item — fee marker
- Line ~ plumbing service-card evidence quote — fee marker
- Line ~ FAQ #1 answer — fee marker
- Line ~ FAQ list — license-Q omission breadcrumb
- Line ~ photo-grid intro — photo selection note
