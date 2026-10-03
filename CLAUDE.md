# Working on this project

Read `README.md` first. It has the structure, the decisions made so far and the open items.

- Edit `src/template.html`, then run `python3 build.py`. Never edit `index.html` directly; it is generated.
- The page is one self-contained file with no dependencies and no build tooling beyond Python's standard library. Keep it that way unless Kieran asks otherwise.
- Season data is the `SEASONS` array in `src/template.html`. Players are first names only: no surnames, no contact details.
- The look is deliberately spare: white, black, navy, one yellow accent, square corners, no shadows or gradients. Kieran has rejected "cute" more than once. Check `design-system/` before adding a colour, a typeface or a new kind of element.
- Preview the tuning panel with `index.html#controls`.
- After a change, say what you tested and what you could not.
