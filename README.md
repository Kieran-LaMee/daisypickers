# Daisy Pickers

Website for the Daisy Pickers softball team, live at https://daisypickers.com. One static page: a field of hand-drawn daisies, a Seasons view with every roster, and a Contact view.

## Files

- `src/template.html`: all markup, styles, script and the `SEASONS` data. Edit this.
- `build.py`: inlines fonts and shapes into `index.html` (Python standard library only). Never edit `index.html` by hand.
- `src/shapes.json`, `src/fonts/`, `assets/logos/`: traced daisies, fonts (SIL OFL), logo SVGs.
- `design-system/`: brand book and tokens. Partly out of date (see below).
- `reference/shirt.jpg`: the shirt photo the daisies and lettering were traced from.

## Build and publish

```
python3 build.py      # writes index.html; open it to preview, add #controls for the tuning panel
git commit -am "..." && git push   # GitHub Pages redeploys in about a minute
```

- **Hosting:** GitHub Pages from `main`, root folder. `CNAME` and `.nojekyll` are for Pages.
- **DNS:** Cloudflare, A/AAAA records to GitHub Pages and `www` CNAME to `kieran-lamee.github.io`. Keep them DNS only (grey cloud) so GitHub can renew its certificate.
- **Email:** Cloudflare Email Routing forwards info@daisypickers.com to daisypickersnyc@gmail.com, which forwards a copy to Zackary. Receive only.
- **Shop:** GitHub Pages doesn't allow one. For merch, link to a hosted checkout or move to Cloudflare Pages.

## Decisions

- **Look:** white, black type, navy daisies, one yellow accent, lots of space. "Stylish, not cute."
- **Home:** the name opens large and centred, then settles top-left. Click a daisy to pick it into a bouquet with a "Picked N" count. A faint infield (foul lines, base paths, arc, pitcher's circle) sits bottom-right.
- **Seasons:** list and detail, arrow keys move through them. The fun record is games played to nil. Seasons with an unknown record omit it.
- **Players:** first names only. Mimi and Zackary shown as co-captains wherever either captained.
- **Rejected:** grass texture, tagline, dots between daisies, photo behind the seasons list.

## To do

- Fall 2026: update the record (0–4 so far) when the season ends.
- Records for Fall 2025 and Spring 2026 (PS Social) are unknown; fun record set to 6–0.
- Spring 2025 "Phil" is a guess from a cut-off name. Rosters for Summer 2023 to Spring 2025 may be incomplete. Summer 2023 and Spring 2025 finishes lack league size.
- Replace traced logo with original artwork when available. Shirt typeface is a near match, not confirmed.
- Not started: season pages, photos, merch.

## Out of date

`design-system/brand-book.md` predates picking, the bouquet, the diamond, yellow centres and the Seasons layout. Where it disagrees with `src/template.html`, the template wins.

Prototype and design system on claude.ai (private): [prototype](https://claude.ai/artifact/XybtE5vozr5buH3Zdx6Jkj), [design system](https://claude.ai/artifact/JooXf3C2dybPuWdciwTBHu).
