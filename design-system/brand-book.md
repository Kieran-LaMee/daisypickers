DAISY PICKERS is a softball team. The site is an archive of its seasons and the people who played them. It should look like the team shirt: white, a black print, a navy collar. It is mostly empty space, small type and one hand-drawn mark.

## Principles

- Leave it out. A page is a list, a headline, or a photo. Rarely two of them.
- White carries the design. If a screen feels empty, it is probably right.
- The drawn daisies are the only loose thing. Everything around them is square, aligned and flat.
- Colour arrives with movement. At rest a page is black, white and navy.

## Voice

- Say less. Most screens are a list of years or names.
- State results plainly: "3–11". No slogans, no exclamation marks, no emoji.
- Show two records wherever a record appears: the win record as played, and the fun record, which is always games played to nil ("Win 2–5 · Fun 7–0"). Never explain it. It is the only joke in the interface.
- Use sentence case for prose. Use uppercase only in `wordmark`, `headline` and `label`.
- Name players by first name or nickname only. Never a surname, never contact details.
- Keep captions to a word or a number: "Roster", "Photos", "2023", "3–11".

## Colour

- Build every page on `paper`. Use `chalk` only for a missing photo and the footer.
- Set text in `ink`, and captions in `ink-soft`.
- `navy` is the collar. Use it for the daisy field, links, the focus ring and the one dark surface a page may have. Text on `navy` is `on-navy`.
- `daisy` is a flat highlight behind a hovered or selected line, with `ink` text on it. It never appears at rest, never as text on `paper`, never as a block of decoration, and never inside the logo.
- A selected item also gets a 1px `ink` underline, so the state does not depend on yellow.
- `line` is decoration. Give controls an `ink` border.
- Keyboard focus is a solid 2px `navy` ring, offset 2px. On a `navy` surface the ring is `daisy`.

## Type

- `wordmark` is the shirt lettering. Use it large once, on the home canvas. In the header, set the name in `label`.
- `headline` appears once per page.
- `list` sets the centred lists: one item per line, `space-2` apart, with an optional `caption` beneath.
- `label` sets navigation and buttons. `body` and `small` carry what little prose there is.
- Do not add a family, italics, or a weight the styles don't name.

## The logo

- The logo is the pair of daisies from the shirt, stored in Logos. Use it whole, at its own proportions.
- Use `daisies-ink` on `paper` and `chalk`, and `daisies-white` on `navy`.
- `daisy-a` and `daisy-b` are the two daisies on their own, cut from the pair. Use them in the field and as a small accent. In a lockup, always use the pair.
- Never redraw it, tidy its line, fill the petals, colour the centres, rotate it in a lockup, or add a shadow.
- In a lockup, centre it under the name set in `wordmark`, as on the shirt, with `space-3` between them and `space-3` clear around both.
- Do not show it smaller than 48px wide, where the line closes up.
- These files were traced from a photograph of the shirt. Replace them with the original artwork when it is available.
- There is no icon set. Label actions with words ("Next", "Back") and use type arrows (← →) where a direction is needed.

## The field

- The home page opens on `paper` with DAISY PICKERS in `wordmark`, centred, and nothing else for about half a second. Then the field fades in around it.
- The field mixes `daisy-a-navy`, `daisy-b-navy` and `daisies-navy`, about two singles to each pair, scattered at random rotation, with nothing between them. Draw the pair 46px, 64px or 92px wide and the singles at the same scale, so every flower is the same size. Aim for about 120 marks on a laptop screen and 30 on a phone. Keep it light: more white than line.
- Marks within about 140px of the cursor spin as it passes, faster for a faster cursor, and coast to a stop at a new angle. They shift slightly out of its way and settle back in place.
- On touch screens a finger does what the cursor does. With no input the field drifts slowly.
- When the visitor prefers reduced motion, show the field still and do not react to the cursor.
- The canvas is decoration. Keep the wordmark and navigation as real text above it, and hide the canvas from screen readers.

## Layout

- The header holds the name on the left and three or four links on the right, both in `label`, inset `space-2` from the edges. Nothing else.
- Centre the page content in one column. Separate sections by `space-4`.
- A list line on hover gets a `daisy` highlight and shows one photo from that season behind the list. The hovered line keeps its highlight so it stays readable over the image.
- Corners are square (`radius-none`). Use `radius-soft` on form inputs only.
- No shadows, no cards, no gradients, no rounded panels.

## Photos

- Use the team's own photos, in full colour, unfiltered, with square corners.
- Show one photo at a time. A grid of photos belongs only on a season's own page.
- Where a photo is missing, show a `chalk` block of the same size. Never use stock imagery.
