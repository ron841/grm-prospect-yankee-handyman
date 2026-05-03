# Photo Audit — Yankee Handyman

## GBP photos in use

10 photos pulled via Places Photo API at native resolution (3024–4800px on long edge), web-optimized to max 1920px for the build. See [`../images/README.md`](../images/README.md) for the full catalogue.

| # | File | Slot in build | Verdict | Notes |
|---|---|---|---|---|
| 01 | `01-gbp-owner-…llc.jpg` | **Hero** | **Weak** | Anthony mid-job installing Brand DuRock cement board. Authentic but composition fights the text overlay (Anthony's body sits where the headline lands). Window cuts the frame awkwardly. Not a "wow" hero. |
| 02 | `02-gbp-owner-…llc.jpg` | Photo grid #3 | OK | Bathroom shower install — clean, tight, finish-work shot. White surround on beige wall, towel bar visible. Decent proof tile. |
| 03 | `03-gbp-owner-…llc.jpg` | Photo grid #4 | Weak | Wooden boardwalk with "BEFORE / Don't Yo… Famil…" warning signage in background, vehicle on pavement. Industrial / commercial context that doesn't match the residential-handyman pitch. |
| 04 | `04-gbp-owner-…llc.jpg` | Photo grid #5 | Weak | Empty room with white-painted block walls and tile floor. Sterile, no styling, no human scale. Reads as "in-progress" rather than "completed work." |
| 05 | `05-gbp-owner-…llc.jpg` | Photo grid #6 | **Strong** | Front porch with white columns and lattice railings, yellow siding, lawn in foreground. Looks like a legitimate completed-work beauty shot. Could be a hero candidate (better than 01 in any case). |
| 06 | `06-gbp-owner-…llc.jpg` | Not used in current build | Unknown | Pulled but not slotted — fewer than 6 grid spots after counting; would be a backup. Owner-uploaded; dimension only. |
| 07 | `07-gbp-owner-…llc.jpg` | Not used | Unknown | Same — backup pool. |
| 08 | `08-gbp-owner-…llc.jpg` | Not used | Unknown | Same. |
| 09 | `09-gbp-customer-diane-bennett.jpg` | **Pool section + Photo grid #1** | **BROKEN PROMISE** | The "Pool decks built like furniture" section copy talks about Anthony sanding edges and cutting a curve to match the coping. The photo shows mid-construction wood framing — a stair/ramp structure, raw lumber, blue pool liner barely visible at edge. **Photo does NOT match the finished-carpentry promise.** |
| 10 | `10-gbp-customer-cole-spires.jpg` | Photo grid #2 | Weak | Porch interior with clutter — cardboard boxes, what looks like a child's wooden ramp/toy, ceiling fan, white walls. Construction-in-progress vibe rather than "finished porch enclosure." |

**Summary:** 1 strong, 1 OK, 5 weak (or wrong stage), 3 unused. **Net: the photo library cannot carry the site without help.** The pool-deck mismatch is the most serious because the copy explicitly sells what the photo doesn't show.

---

## Additional candidates from FB

Pulled via Playwright DOM extraction from the public FB page. The login wall blocked direct downloads of the largest variants for most photos, but the cover photo was retrievable at 960×720 and the other 8 thumbnails came down at 414×414. Saved to [`../audit/fb-photos/`](fb-photos/).

| # | File | Subject (from view + alt text) | Hero candidate? | Notes |
|---|---|---|---|---|
| 1 | [`fb-01-cover-photo-pergola.jpg`](fb-photos/fb-01-cover-photo-pergola.jpg) | **Finished pergola attached to Florida ranch home — full sun, blue sky, mature trees, grass lawn** | **YES — strongest single photo** | 960×720, full FB cover res. Finished outdoor structure. Could re-anchor the entire site's visual story. Recommend requesting larger-res original from Anthony. |
| 2 | `fb-02-photo-3-no-desc.jpg` | Wooden stairs/ramp leading up to above-ground pool, blue pool visible | No | 414×414. Mid-construction. Same job as GBP #9. |
| 3 | `fb-03-photo-4-no-desc.jpg` | Different angle, similar wood ramp/stair work | No | 414×414. Same series. |
| 4 | `fb-04-photo-5-rabbit-hutch.jpg` | Wooden frame structure on top of above-ground pool — looks like deck-in-progress | No | 414×414. FB's auto-alt called this a "rabbit hutch" — wrong; it's deck framing. |
| 5 | `fb-05-photo-6-no-desc.jpg` | Construction site with pool framing | No | 414×414. |
| 6 | `fb-06-photo-7-no-desc.jpg` | Construction site continued | No | 414×414. |
| 7 | `fb-07-photo-8-trampoline-grass.jpg` | Wider shot: pool, lawnmower, dirt patches, fence. FB auto-tagged "trampoline" — wrong; that's the pool. | No | 414×414. Documentary work-site shot. |
| 8 | `fb-08-photo-9-no-desc.jpg` | Construction context | No | 414×414. |
| 9 | `fb-09-photo-10-no-desc.jpg` | Construction context | No | 414×414. |

**FB findings summary:**
- **1 strong hero candidate** (the cover photo — the pergola)
- **0 finished-pool-deck photos** — Anthony does not appear to have one publicly visible
- The 8 thumbnails are all the same pool/deck construction series at different angles — they'd add nothing to the build that GBP doesn't already cover
- FB auto-alt-text was unreliable (called a pool a trampoline, deck framing a rabbit hutch) — don't trust it as content authority

---

## Recommendations

1. **Hero swap → fb-01 (pergola).** Best photo we have. Re-author hero alt to match.
2. **Pool deck photo: ask Anthony for a finished-deck shot.** None exists in the public photo set we can access. If he can't provide one, re-author the pool section to feature the pergola/finish-carpentry instead of pool decks specifically.
3. **Tag photo-grid captions** with real subjects:
   - Tile #3 (`02-gbp-owner-…`): "Bathroom shower install"
   - Tile #4 (`03-gbp-owner-…`): drop or replace
   - Tile #5 (`04-gbp-owner-…`): drop or replace
   - Tile #6 (`05-gbp-owner-…`): "Front porch" or similar
4. **If grid contracts to 4 tiles:** keep #1 (pool deck — mid-build, but flag to Anthony for replacement), #2 (Cole Spires porch — weak but the only "customer-uploaded" content we have besides Diane), #3 (bathroom), #6 (front porch).
5. **Request from Anthony at walkthrough:**
   - High-res pergola photo (the FB cover — original source)
   - Finished-pool-deck photo (per the copy promise)
   - Any additional finished interior or exterior beauty shots he hasn't posted
   - Any photos that include him + his team for an "About" portrait
