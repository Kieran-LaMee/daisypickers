# Daisy Pickers

The website for the Daisy Pickers softball team, to be served at daisypickers.com. One static page: a field of hand-drawn daisies that react to the cursor, a Seasons view with every roster, and a Contact view.

## What's here

| Path | What it is |
|---|---|
| `index.html` | The built page. This is what gets deployed. Do not edit it by hand. |
| `CNAME` | Tells GitHub Pages the site lives at daisypickers.com. |
| `.nojekyll` | Stops GitHub Pages running Jekyll over the files. |
| `build.py` | Builds `index.html` from `src/`. Python standard library only. |
| `src/template.html` | The source: all the markup, styles, script and season data. Edit this. |
| `src/shapes.json` | The three daisy shapes (the pair and two singles) as SVG path data, plus their centres. |
| `src/fonts/` | Barlow Semi Condensed, Geist and Geist Mono (all SIL Open Font License). Inlined at build time. |
| `assets/logos/` | The traced daisies as SVG files in black, navy and white. One is used as the favicon. |
| `design-system/` | A copy of the brand book, tokens and logo notes. See "Out of date" below. |
| `reference/shirt.jpg` | The team shirt photo the daisies and lettering were traced and matched from. |

## Build and preview

```
python3 build.py
open index.html
```

Add `#controls` to the address (`index.html#controls`) to show the tuning panel for the daisy field. It is hidden otherwise.

`python3 build.py --artifact` also writes `dist/prototype.html`, the controls-on version used for the claude.ai prototype.

## Deploy: GitHub Pages with a Cloudflare domain

1. Create a public repository (for example `daisypickers`) and push this folder to `main`.
2. In the repository: Settings, Pages. Set the source to "Deploy from a branch", branch `main`, folder `/ (root)`.
3. Still under Pages, set the custom domain to `daisypickers.com`. The `CNAME` file here already says the same.
4. In Cloudflare, DNS for daisypickers.com, add:
   - four `A` records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - optionally four `AAAA` records for `@`: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
   - one `CNAME` record for `www` pointing to `kieran-lamee.github.io`
5. Set those records to "DNS only" (grey cloud) to begin with, so GitHub can issue its own certificate.
6. Back in Pages settings, tick "Enforce HTTPS" once it becomes available. GitHub says this and DNS changes can each take up to 24 hours.

The record values come from GitHub's custom domain documentation, checked on 3 October 2026.

One caveat for later: GitHub Pages' terms do not allow running an online shop from it. If merch goes ahead, either link out to a hosted checkout or move hosting to Cloudflare Pages, which can deploy from this same repository.

## Decisions so far

- **Look:** white page, black type, navy daisies, one yellow accent. Minimal, lots of empty space. "Stylish, not cute."
- **Daisies:** traced from a photo of the team shirt. The pair is the logo. The two singles were cut from it, each given its own normal-length petal where the two overlap on the shirt.
- **Field defaults:** spin movement, a mix of singles and pairs, about 123 daisies on a 1470 x 920 window, size 115%, navy, drift on, dots off.
- **Home page extras:** click a daisy to pick it; it flies to a small bouquet under the name (most recent 14) with a "Picked N" count that flashes yellow. Daisies near the cursor get yellow centres. A softball infield in very light navy lines sits in the bottom-right corner; daisies only grow in the outfield.
- **Opening:** the name appears large and centred, then shrinks to the top-left as the field fades in.
- **Seasons:** list on the left, selected season on the right, arrow keys move through them. Each shows a win record and a fun record; the fun record is always games played to nil.
- **Players:** first names only. Mimi and Zackary are shown as co-captains in every season where either was a captain.
- **Contact:** info@daisypickers.com, no Instagram for now.
- **Rejected:** a grass texture background (tried three ways), a tagline, dots between the daisies, a photo behind the seasons list.

## Still to do

- **Email:** info@daisypickers.com does not exist yet. It needs setting up before launch, for example with Cloudflare's email forwarding.
- **Spring 2026 and Fall 2025:** placeholders marked "[Details to come]". These were played in a different league; the details are still to be collected.
- **Spring 2025 roster:** one name was hidden in the source screenshot with only "Ph" visible. It is entered as Phil, which is a guess.
- **Rosters may be incomplete:** the screenshots for Summer 2023, Fall 2023, Spring 2024 and Spring 2025 ended at the bottom of the screen, so later names could be missing.
- **League size:** Summer 2023 ("10th") and Spring 2025 ("12th") have no "of how many" because the standings were cut off.
- **Fall 2026:** marked in progress at 0-4. Update the record when the season ends.
- **Logo artwork:** the daisies are traced from a small photo. Replace `src/shapes.json` and `assets/logos/` when the original file is available.
- **Shirt typeface:** Barlow Semi Condensed is the closest free match found, not a confirmed identification.
- **Season pages, photos, merch:** not started.
- **Phones:** the infield takes roughly the bottom 40% of a phone screen. It has been viewed in still screenshots only, not on a real device.

## Out of date

`design-system/brand-book.md` predates the last round of changes. It still says never to colour the daisy centres, describes a hover photo behind the seasons list, and does not mention picking, the bouquet, the diamond or the list-and-detail Seasons layout. Where it disagrees with `src/template.html`, the template is right.

## Where the prototype lives

- Prototype with controls: https://claude.ai/artifact/XybtE5vozr5buH3Zdx6Jkj
- Design system: https://claude.ai/artifact/JooXf3C2dybPuWdciwTBHu

Both are private to Kieran's Claude account.
