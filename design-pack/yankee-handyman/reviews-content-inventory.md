# Reviews Page — CONTENT-INVENTORY

> Slot-keyed inventory for `/reviews`. Every string the build needs. Consumed by `reviews-slots.md` next.
>
> **Voice authority:** GRM voice skill. Customer review text is preserved verbatim (no edits, no trims unless flagged). Owner reply text preserved verbatim. All connector copy authored against synthesis §1 voice rule (≤100 chars, match Anthony's reply tempo).
>
> **Persona:** Neighborhood steady (primary) + Quiet confidence (secondary), inherited from homepage.
>
> **Status legend:** `committed-verbatim` (review/reply text from corpus, untouched) · `microcopy-design` (authored connector) · `pending-walkthrough` (operator confirmation needed)
>
> **Forcing-function check:** every review-slot below has a value or an explicit deferred-state tag. Zero ambiguous blanks at the seam to SLOTS.

---

## Page-level metadata

### `meta.title`
- **Value:** "Reviews — Yankee Handyman, Ocala"
- **Status:** microcopy-design
- **Voice:** Closing Table
- **Length:** 38 chars

### `meta.description`
- **Value:** "Forty-four of Anthony Porett's fifty Google reviews. Plumbing, electrical, carpentry, tile, paint. Marion County, 4.9 stars."
- **Status:** microcopy-design
- **Voice:** Closing Table (data-forward)
- **Length:** 132 chars
- **Citation:** synthesis §8

### `meta.og_title`
- **Value:** "What Marion County says about Yankee Handyman"
- **Status:** microcopy-design
- **Voice:** Saturday Morning

### `meta.og_description`
- **Value:** "Forty-four customer reviews. Forty-three replies from Anthony. One 1-star included."
- **Status:** microcopy-design
- **Voice:** Saturday Morning (specific, transparent — leads with the count, names the outlier)

### `meta.canonical`
- **Path:** `/reviews`

---

## Page header

### `page.eyebrow`
- **Value:** "REVIEWS"
- **Status:** microcopy-design
- **Voice:** Closing Table eyebrow

### `page.headline`
- **Value:** "What Marion County says."
- **Status:** microcopy-design
- **Voice:** Closing Table (declarative, place-specific)

### `page.subhead`
- **Value:** "Forty-four reviews on Google. Anthony has replied to forty-three of them. One 1-star is in here too."
- **Status:** microcopy-design
- **Voice:** Saturday Morning (lead with the count, name the outlier without drama)
- **Citation:** synthesis §0, §5
- **Length:** 99 chars (under the 100-char authoring cap per synthesis §1)

### `page.cta_back_to_home`
- **Label:** "← Yankee Handyman home"
- **Status:** microcopy-design
- **Voice:** Closing Table

---

## Section 1: Curated leads (5 review/reply pairs)

> Sequence-locked per reviews-synthesis §4. No section header — these read as the page lede after `page.subhead`.

Each item:
```
{
  id: <kebab-slug>,
  reviewer: <name>,
  star_rating: 5,
  date: <as captured>,
  review_text: <verbatim>,
  reply_text: <verbatim or null>,
  reply_date: <relative date as captured>,
  job_tag: <1-3 word service category for sub-label>
}
```

### `curated.judy`
- `reviewer`: "Judy"
- `date`: (corpus does not date-stamp; reply is "a year ago" → ~early 2025)
- `job_tag`: "Multi-project relationship"
- `review_text`:
  > "I called the Yankee Handyman after a friend of mine recommended him in Ocala. I called midday and Anthony came out that evening to give us an estimate. We had water damage on our living room wall from a bathroom that we wanted completely torn out and redone.
  >
  > He gave us a complete estimate, explaining all that he would do. He was reasonable and detailed in his explanations of what all had to be done.
  >
  > Anthony did absolutely beautiful work! He finished within the timeframe he had given us and within budget.
  >
  > A sidenote but important to us. He was doing the bathroom for a mentally challenged young man who had questions, many questions as he worked. Anthony took the time to explain to him each and every time he was questioned. That in itself was above and beyond!
  >
  > We have since had him back for many jobs. He has remodeled another bathroom completely. Tiled and painted a bedroom. Replaced the ceiling on our wrap around porch and installed fans on it. He repaired and replaced to porch railings. Then, built and installed wooden hurricane shutters for our windows. He redone the wiring for our pool pump and installed the new pump.
  >
  > Every job we have called him for, he has been reasonably priced and the work has been perfect. We keep him on speed dial."
- `reply_text`: "Thank you Judy again for choosing us."
- `reply_date`: "a year ago"
- **Status:** committed-verbatim
- **Citation:** corpus review #1

### `curated.cheryl-mulhern`
- `reviewer`: "Cheryl Mulhern"
- `date`: (reply is "2 months ago" → ~March 2026)
- `job_tag`: "Plumbing · Bellechase"
- `review_text`:
  > "I used Anthony (The Yankee Handyman) to install a garbage disposal for me. I wanted it done ASAP, and Anthony was able to work me into his schedule the same day I called.
  >
  > I had contacted a few plumbers who quoted me $350–$500! I was shocked and was never going to pay more for an installation than I paid for the actual disposal. Anthony was recommended by our Bellechase homeowners Facebook group, where we only allow the very best contractors to be added to the page, and he did not disappoint.
  >
  > He took pity on me and squeezed me in at the end of his day. He did a great job and his price was phenomenal—I only paid $125, which is his standard service fee. I recommend him 100%. He even cleaned up after himself and took the old disposal away. As we all know, that's not usually the case with contractors, as I've often been left with a mess after a job is done."
- `reply_text`: "Thank you for being a part of the family. We appreciate you relying on us!"
- `reply_date`: "2 months ago"
- **Status:** committed-verbatim
- **Citation:** corpus review #2

### `curated.diane-bennett`
- `reviewer`: "Diane Bennett"
- `date`: (reply is "5 days ago" → late April 2026)
- `job_tag`: "Pool deck"
- `review_text`:
  > "Anthony built a deck for my pool- I cannot be more pleased- he was so detailed right down to sanding all the edges and I do mean ALL. Excellent quality and a great price. I did ask around if the price was fair for my area and everyone either said yes or they would have charged almost $1000 more. I already have him quoting another project for me. Zoom in and checkout how he did the curve around the pool- holy awesome!!!"
- `reply_text`: "😁. Thank you. I really do appreciate my community. I hope you enjoy it. Thank you for choosing us!!!"
- `reply_date`: "5 days ago"
- **Status:** committed-verbatim
- **Citation:** corpus review #5

### `curated.linda-weis`
- `reviewer`: "Linda Weis"
- `date`: (reply is "a year ago" → ~early 2025)
- `job_tag`: "Deck rebuild"
- `review_text`:
  > "Tried to get a contractor to repair my wooden deck. Went through 10 contractors and no one showed up. That was until yankee Handyman responded and was there in 3 days. He took and impossible rehab of my deck and in two days he had rebuilt it with it looking new, He did what he said he would do on time and within budget. His team was great and left me with a smile on my face. Even neighbors commented how great it looked. Thank you Yankee Handyman to a job well done."
- `reply_text`: "Thank you we appreciate the opportunity. I'm happy that I put a smile on your face. That's what it's all about. Thanks for the 🎂."
- `reply_date`: "a year ago"
- **Status:** committed-verbatim
- **Citation:** corpus review #4

### `curated.andrew-abad`
- `reviewer`: "Andrew Abad"
- `date`: (reply is "2 months ago" → ~March 2026)
- `job_tag`: "Repeat customer · 20+ projects"
- `review_text`:
  > "Anthony is amazing! He goes above and beyond in every job he does, he has done probably over 20 projects for me and every single time he's done great work at an extremely reasonable price! Highly recommended!"
- `reply_text`: "Thank you for allowing me the opportunity to do a good job for you. I'm sure I will be seeing more of you in the future. 😁❤️"
- `reply_date`: "2 months ago"
- **Status:** committed-verbatim
- **Citation:** corpus review #14

---

## Section 2: One 1-star

> Plain header. No editorial wrapper. Reviews-synthesis §5.

### `outlier.header`
- **Value:** "One 1-star review."
- **Status:** microcopy-design
- **Voice:** Closing Table (declarative, no softening)
- **Length:** 18 chars

### `outlier.subhead`
- **Value:** "Anthony's reply is below it."
- **Status:** microcopy-design
- **Voice:** Saturday Morning (just naming what's there)
- **Length:** 27 chars

### `outlier.review`
- `reviewer`: "DM _"
- `star_rating`: 1
- `date`: "April 2024" (per Birdeye cross-reference noted in corpus)
- `review_text`:
  > "I would not recommend hiring this handyman for your projects/home repair needs.
  >
  > If you decide you want to give this person an opportunity for your work, here's some advice after hiring this handyman:
  >
  > 1. Get a written quote for the work you'd like to get done. He 'forgets' how much he said he'd charge you for things.
  > 2. Ensure the written quote has details/specifics about what he's actually going to do for each work item.
  > 3. I also suggest waiting at least 24/48 hours before making payment, depending on the type of project, to make sure what was done works correctly and trash/debris was removed.
  > 4. Lastly, if records are important for you or your business, make sure you get an invoice before making a payment. It's been about a month since my work was 'completed,' he received his payment, and there is still no invoice for me.
  >
  > Good luck."
- `reply_text`: "I'm sorry to hear we weren't on the same page. I take pride in the quality of my work and aim for 5-star service with every client. I appreciate your feedback. Best of luck with your future home projects."
- `reply_date`: "Edited 2 months ago"
- **Status:** committed-verbatim
- **Citation:** corpus review #3
- **Walkthrough flag:** confirm Anthony is comfortable surfacing this. Default = ship.

---

## Section 3: Grouped by service type

> Group order from synthesis §6 (job-noun frequency). Within group, sort by review length (longer first). Reviews already used in curated leads NOT repeated.

### `group.carpentry-framing`

#### Header
- `eyebrow`: "GROUP 1"
- `headline`: "Carpentry and framing"
- `subhead`: "Six reviews mention carpentry, framing, or finish work."
- **Voice:** Saturday Morning

#### Reviews (in order)

1. **Cole Spires** (corpus #9, ~7 months ago) · Porch enclosure + interior wall + tile
   > "We highly recommend Yankee Handyman, he recently finished enclosing our porch as well as adding an interior wall to another room. They did a great job and made a big difference in our home. Also re-tiled another room for us. Really cares about his work. Will use him again when needed. 5 star rated for a reason!"
   - Reply: "We appreciate your business, sir, and looking forward to more projects in the future. Thank you for choosing us. 😁"

2. **Barbara Roberts** (corpus #6, "a year ago") · Wall replacement + sliding glass door + windows
   > "Anthony and his co-worker are the hardest working guys I've ever seen. They did a fantastic job replacing a wall and installing a sliding glass door on our Florida room. They did such a good job on that, I hired them to also replace another wall and install 2 windows on the new wall. I can't wait to see my new room! Hard working and trustworthy. I recommend them to anyone."
   - Reply: "Thank you, Barbara. It was a pleasure."

3. **William Stone** (corpus #22, "a year ago") · Door trim repair (termite damage)
   > "He did a fantastic job replacing the wood around one of our doors which had termite damage. The door trim now looks just like all the others. So happy about it."
   - Reply: "It was yet our pleasure to Help. Thank you!!"

4. **Edward Campea** (corpus #29, "a year ago") · Pavilion + trash can container
   > "I highly recommend Anthony (Yankee Handyman) for any project you need done on your home. He did a pavillion and trash can container."
   - Reply: "Thank you Edd. It was my pleasure."

5. **Leanna Fitzgerald** (corpus #24, "3 years ago") · Siding repair + screens + paint
   > "Anthony did a great job repairing our siding, making new screens and painting our house! Will definitely call Anthony again for any future repairs/renovations."
   - Reply: "It was my pleasure. It turned out beautiful."

6. **Ju B** (corpus #43, no reply) · Pergola
   > "construction of a pergola."
   - Reply: *none*

**Status:** all committed-verbatim. Citation: corpus.

### `group.tile-flooring`

#### Header
- `eyebrow`: "GROUP 2"
- `headline`: "Tile and flooring"
- `subhead`: "Carpet pulled, tile laid, floors finished clean from one room to the next."
- **Voice:** Saturday Morning

#### Reviews

1. **Maudeline Henry** (corpus #12, "a year ago") · Carpet removal + tile install + backsplash
   > "He removed all the carpets in my two bedrooms, and removed the tiles in my kitchen, dining room. Also he got my backsplash done. After that he installed the new tiles. He was doing a great job and kept the place clean. The price was reasonable. Thank you"
   - Reply: "Thank you for the opportunity. We aim to please."

2. **Zac Stone** (corpus #15, "a year ago") · Floor finishing
   > "Fantastic work! Finished a day earlier than estimate. There was an issue with the previous work done on our floor and Anthony was able finish with a clean look from bedroom to bathroom. Highly recommend!!"
   - Reply: "Thank you Zack. It was a mess now it's a success!"

3. **Ashley Santiago** (corpus #30, "4 months ago") · Floors
   > "Anthony was absolutely great to work with. He came right away and solved all my problems and the floors looks wonderful."
   - Reply: "Thank you for choosing us. We appreciate your busy ad love the opportunity. Thank you."

**Status:** all committed-verbatim.

### `group.porches-decks-outdoor`

#### Header
- `eyebrow`: "GROUP 3"
- `headline`: "Porches, decks, outdoor builds"
- `subhead`: "Florida rooms, screened porches, walk-in showers, decks for the pool."
- **Voice:** Saturday Morning

#### Reviews

1. **David Bittman** (corpus #8, "7 months ago") · Screened porch rebuild + rear deck
   > "Anthony took over the construction of a screened in porch that the initial builder defaulted on and made poorly. Anthony rebuilt it from start to finish including the decking for screening and a roof. Then he built my rear deck. I highly recommend Yankee LLC. Fair pricing good quality and done in a timely fashion."
   - Reply: "Thank you David. I'm sure we will meet again."

2. **Brendon Pointing** (corpus #27, "a year ago") · Bathroom remodel + walk-in shower
   > "Anthony did a tear out and remodel of my bathroom. As I get older, I wanted a walk-in shower. He did great work and I am beyond satisfied!"
   - Reply: "Thank you."

3. **Terri** (corpus #25, "6 months ago") · Screen door + porch railing
   > "Super Great guy ,he put in our screen door and now added a railing on the back porch. Definitely be calling him again for my bucket list. Thank you, Anthony."
   - Reply: "Yes ma'am 😊😃 your very welcome."

**Status:** all committed-verbatim.

### `group.multi-trade-repeat`

#### Header
- `eyebrow`: "GROUP 4"
- `headline`: "Multi-trade and repeat customers"
- `subhead`: "Customers who hired Anthony once, then kept hiring him."
- **Voice:** Saturday Morning

#### Reviews

1. **JEAN JONES** (corpus #7, "3 years ago") · Drywall + paint + flooring + plumbing + electrical + tile + walk-in shower
   > "Anthony has done drywall repair, painting, flooring repair and replacement, and miscellaneous plumbing and electrical repair for me on several sites. He has replaced an entire walk-in shower, cabinets, toilets, etc., and does beautiful tile work. He's dependable and knowledgeable. I have recommended him to at least four other people and all of them were happy with his work."
   - Reply: "It's my Absolute pleasure to work with you Jean. Thank you kindly."

2. **audrey bittman** (corpus #20, "2 months ago") · Multi-year relationship
   > "We have been working with Anthony for several years and can not recommend him highly enough. He does excellent work, he is honest & reliable. You will not be disappointed!"
   - Reply: "I am thankful. I appreciate you guys having me on speed dial😁. I love my community and all the great people like you who relies on me. Thank you. It means a lot."

3. **Karen Cowan** (corpus #28, "a year ago") · Multi-job
   > "Great work, super patient, professional and respectful. He did everything exactly as I wanted. I would definitely hire Anthony again."
   - Reply: "Thank you for your support."

**Status:** all committed-verbatim.

### `group.plumbing-electrical`

#### Header
- `eyebrow`: "GROUP 5"
- `headline`: "Plumbing and electrical"
- `subhead`: "Disposals, leaks, new circuits, light fixtures."
- **Voice:** Saturday Morning

#### Reviews

1. **Megan Stone** (corpus #10, "a year ago") · Major kitchen leak
   > "I could not be happier with the service. Anthony is professional, does tip quality work, ands very reasonably priced. We had a major leak in our kitchen. He was knowledgeable, worked with our schedule, and got the job done better than I could have imagined. Highly recommend."
   - Reply: "Your very welcome."

2. **Molly Groves** (corpus #16, "3 months ago") · New circuit + chandelier
   > "Did excellent work creating a new circuit and hanging a chandelier for our kitchen. High quality work, professional, showed up on time, and him and his team worked together as a dynamic duo."
   - Reply: "😁 thank you. We appreciate you!!"

**Status:** all committed-verbatim.

### `group.painting`

#### Header
- `eyebrow`: "GROUP 6"
- `headline`: "Painting"
- `subhead`: "Interior, exterior, trim."
- **Voice:** Saturday Morning

#### Reviews

1. **Jennifer LeMay** (corpus #32, "6 days ago") · Interior paint
   > "We had Yankee Handyman paint the interior of our house and they did a fantastic job. Will definitely use them again."
   - Reply: "Thank you for choosing us. It's always a pleasure. We appreciate your business."

**Status:** committed-verbatim.

### `group.quick-jobs`

#### Header
- `eyebrow`: "GROUP 7"
- `headline`: "Quick jobs and short praise"
- `subhead`: "On-time, reasonable, done. Fourteen reviews in this category."
- **Voice:** Saturday Morning (honest about what these are — short reviews, real work)

#### Reviews (sorted by length, longer first)

1. **Zulma Velez** (corpus #11, "7 months ago")
   > "Exceptional service. We are very please with the finished product. Detail oriented, Time efficient, Friendly, Customer service oriented. 10/10 highly recommended, we will most certainly be repeat customers. If you are looking for handyman services, Anthony is your guy!"
   - Reply: "Thank you for choosing us. We appreciate our community. Thank you. 😊"

2. **Robert Nedow** (corpus #35, "a year ago")
   > "Very friendly and got the job done quickly and efficiently. Cleaned up after the work was done."
   - Reply: "The Yankee Handyman at your Service!!!! It was our pleasure. Creating beautiful spaces and smiling faces is what we really strive for. Thank you."

3. **George Kim** (corpus #13, "2 years ago")
   > "Really good guy to work with thats super knowlegeable. Will go above and beyond to get things done in a timely matter with quality work. In my opinion, he's a Jack of all trades and Master of all!! Thank you Mr. YANKEE!"
   - Reply: "Your very welcome George."

4. **Devin P** (corpus #17, "a year ago")
   > "Definitely recommend. Quick, efficient, friendly, good with dogs (ours kept sniffing at him while he worked 😂), and very affordable (charged us a quarter of what we were quoted elsewhere!)"
   - Reply: "Thank you."

5. **Bob Hart** (corpus #21, "2 weeks ago")
   > "Did a fantastic job for us. Will be calling on him again. He was prompt and courteous. He knew what he was doing. And we even gave him an extra job. Also very reasonable."
   - Reply: "We appreciate you choosing us. Thank you 😊."

6. **Sam Perry** (corpus #23, "a year ago")
   > "Excellent service. On time. He stayed until the project was done to completion! Really went above and beyond. Excellent pricing. Really knows what he's doing."
   - Reply: "We appreciate the opportunity and your kind words."

7. **Dan Carter** (corpus #26, "a year ago")
   > "Hired Anthony to help me with some jobs too tough for me. He was a very hard, knowledgable, worker! Got done what I wanted! We are Hurricane Ian survivors."
   - Reply: "Thank you Dan. It was my pleasure."

8. **Jon De Lucia** (corpus #18, "3 weeks ago")
   > "Anthony strives for and maintains 100% customer satisfaction, I was given a estimate, agreed upon & works was completed in two days. What more could I have ask for. Thanks Anthony."
   - Reply: "Thank you Jon. We appreciate your business."

9. **Griselle Martin** (corpus #19, "a year ago")
   > "I hired Anthony to do some work on my home. He showed up on time, was very professional, and did a great job. His price are reasonable. I will definitely be using him again"
   - Reply: "Thank you for choosing the Yankee handyman LLC. We appreciate your support."

10. **Jorge Aliaga** (corpus #33, "7 months ago")
    > "Great service! Easy to work with and always on time, if not early. One of the few I would recommend to anyone."
    - Reply: "It was my pleasure. Thank you for the opportunity."

11. **Ryan McBride** (corpus #34, "a year ago")
    > "On time, professional, solid job through. I will be using his services again for more work in my house."
    - Reply: "Thank you for choosing the Yankee Handyman LLC Ryan."

12. **Brian Stamper** (corpus #31, "a year ago")
    > "Yankee showed up when he said he would.. the work was done well.. price was ok ... would use again if needed.. touché"
    - Reply: "Thank you sir for the opportunity. we appreciate your feedback."

13. **Jarron Remington** (corpus #36, "a year ago")
    > "On time, did the job quickly. Very reasonable. Will hire again."
    - Reply: "Thank you. I appreciate you choosing The Yankee Handyman LLC."

14. **Katheryn Foerste** (corpus #37, "2 years ago")
    > "He was efficient and worked fast. Pleased with repair."
    - Reply: "It was my pleasure. Thank you."

**Status:** all committed-verbatim.

---

## Section 4: Archive

> Date-ordered remaining reviews. Lighter visual weight.

### `archive.header`
- `eyebrow`: "ARCHIVE"
- `headline`: "The shortest ones."
- `subhead`: "Real reviews, just brief."
- **Voice:** Saturday Morning

### Archive items

1. **Wally Plumstead** (corpus #38, "a year ago"): "Outstanding. Went above and beyond too. Professional." — Reply: "Thank you for choosing The Yankee Handyman, we appreciate your business. Thank you."

2. **Hi 5 Tobacco and vapor** (corpus #39, "a year ago"): "Great work, fast response and reasonably priced" — Reply: "It was a pleasure. Thank you for choosing The Yankee Handyman LLC."

3. **tyisha epps** (corpus #40, "a year ago"): "Highly recommended neighborhood handyman" — Reply: "We appreciate your business. Thank you."

4. **Sherry Brickner** (corpus #41, "a year ago"): "Awesome person and great job!" — Reply: "Thank you Ma'am."

5. **Patrice Stone** (corpus #42, "a year ago"): "We appreciate your support." — Reply: "We appreciate your support."

6. **Ariana Vixen** (corpus #44, "a year ago"): "Thank you for choosing us." — Reply: "Thank you for choosing us."

**Status:** all committed-verbatim.

---

## Page footer

### `cta.banner.headline`
- **Value:** "Tell him about the job."
- **Status:** microcopy-design
- **Voice:** Saturday Morning (matches homepage `contact.headline`)

### `cta.banner.subhead`
- **Value:** "Phone is fastest. He answers most calls during business hours."
- **Status:** microcopy-design
- **Voice:** Saturday Morning

### `cta.banner.phone_button`
- **Label:** "Call (239) 867-8447"
- **`tel:` link:** `tel:+12398678447`
- **Status:** committed

### `cta.banner.see_more`
- **Label:** "See all 50 reviews on Google"
- **URL:** GBP listing URL — `pending-extraction` from `place-details-raw.json`
- **Status:** pending-extraction

---

## JSON-LD Review schema

> Build instruction: emit one `Review` entry per surfaced review on this page (44 total). Homepage retains `aggregateRating` only (do not duplicate `Review` entries on homepage).

Per-review schema template:
```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "LocalBusiness",
    "name": "The Yankee Handyman LLC"
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "<5 or 1>",
    "bestRating": "5"
  },
  "author": {
    "@type": "Person",
    "name": "<reviewer name>"
  },
  "reviewBody": "<verbatim review text>",
  "publisher": {
    "@type": "Organization",
    "name": "Google"
  }
}
```

**Reply schema:** Anthony's replies attach as `Review.publisher.replyToUrl` is not standard schema. Best practice: include reply text as a `Comment` on the parent review, OR omit reply from schema (browsers don't surface it anyway). **Recommend omit** — schema purpose is rich-results SEO; replies are page-only artifacts.

---

## Forcing-function checklist (to SLOTS)

✅ Every review/reply pair appears verbatim, no edits.
✅ Every connector copy slot names voice + length.
✅ All 44 reviews from corpus accounted for: 5 curated + 1 outlier + 6 carpentry + 3 tile + 3 porches + 3 multi-trade + 2 plumbing-electrical + 1 painting + 14 quick + 6 archive = 44.
✅ Reply absence (Ju B / pergola) flagged inline, not papered over.
✅ 1-star handled with plain header, no editorial wrapper.
✅ Customer-voice forward, owner-voice supporting (synthesis §1).
✅ Phone number, CTA banner, JSON-LD schema specified.

**Deferred items (explicit):**
- GBP listing URL for "see all 50 on Google" CTA → `pending-extraction`
- Walkthrough confirmation that Anthony is comfortable surfacing the 1-star (default = ship)
