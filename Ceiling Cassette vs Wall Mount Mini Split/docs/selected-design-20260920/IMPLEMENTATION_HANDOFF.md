# Implementation handoff — SELECTED_DESIGN (2026-09-20, owner refinement)

## Status

Local implementation complete through the owner-refinement round. Stopped for
**Codex review**. Not committed, not pushed, not published.

## Current file

`ceiling-cassette-vs-wall-mount-mini-split.html` (project root)

## Backups (project root)

- `backup-owner-refinement-20260920-102803.html` — immediate pre-round backup
- `backup-visual-fix-20260920-095637.html`
- `backup-selected-design-20260920-093959.html` — products/services frozen baseline
- earlier round backups retained

## This round

1. Hero: removed the `Compare the styles` button (no replacement); copy block
   recentered; no reserved margin left behind.
2. Selector: reordered to priority → wall → ceiling with homeowner-facing wording
   (Keep walls clear / Limit ceiling work / No preference; Looks possible /
   No clear spot / Not sure; Can install / Cannot install / Not checked). Result
   copy no longer treats a homeowner wall observation as confirmed.
3. Fixed the state-consistency defect: state is now rebuilt from the checked
   radios (`readState` + `syncStyles` + `render`) on init, `change`, `reset`, and
   `pageshow`. Reproduced the "3 selected but says unanswered" case before the fix
   and verified it is gone after.
4. Scene image fills the media card at 4:3; the white caption bar is replaced by
   an `i` info button (44px hit area, keyboard + touch, Escape to close, above the
   note). Note text: "Two alternative locations are shown for comparison. This is
   not an installation drawing."
5. Comparison: cassette 205px / wall 255px, media height 160px, value columns
   centered under their type, attribute column and group labels left aligned.
6. FAQ H2 no longer capped at 760px (single line on wide screens).
7. Footer rebuilt as the reference closing-band: limited-width light-blue band,
   left title, right two equal outline buttons; mobile left-aligned stacked.
8. Removed a duplicated `</main>` (and previously a duplicated `</head>`).

## Preserved (frozen)

`#products`, `#services`, the five FAQ Q&A + JSON-LD, all product data, the four
project tabs and their image sync. `#products` + `#services` remain byte-identical
to the frozen baseline.

## Unresolved / for review

- Codex visual review of this round is not done.
- Product prices are the existing local snapshot; Services policy wording was not
  re-verified and was not modified.
- Functional results are from the implementation side; Codex has not independently
  re-run the 27-combination matrix.
