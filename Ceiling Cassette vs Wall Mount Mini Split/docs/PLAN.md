# Implementation Plan

## Step 1: Project Memory And Scope

Goal: record the page objective, target URL, positioning, conversion paths, and acceptance criteria.

Spec summary:
- Inputs: user-approved scope, Della design references, existing comparison page.
- Outputs: docs and handoff notes.
- Boundaries: no Shopify Liquid implementation.

Files involved:
- `docs/PRD.md`
- `docs/DESIGN.md`
- `docs/TECH_STACK.md`
- `docs/PLAN.md`
- `docs/ARCHITECTURE.md`
- `docs/MODULARITY.md`
- `docs/PROGRESS.md`
- `HANDOFF.md`

Acceptance criteria:
- Docs reflect the confirmed decisions and redirect strategy.

Validation:
- Manual read-through.

Expected evidence:
- Files exist in the page directory.

Risk note:
- Keep docs concise so they guide the build without slowing future edits.

## Step 2: Standalone Page Build

Goal: create the local HTML demo and local assets.

Spec summary:
- Inputs: product URLs, image URLs, current PDP prices, brand tokens, existing product card pattern.
- Outputs: standalone HTML and local assets.
- Boundaries: no dynamic Shopify product data.

Files involved:
- `ceiling-cassette-vs-wall-mount-mini-split.html`
- `assets/*`

Acceptance criteria:
- Above-fold verdict and CTAs are visible.
- Product cards include image, title, tags, price, and `View Product`.
- Product cards are organized into two tabs by indoor unit type.
- Comparison sections match the revised 10-section structure.

Validation:
- Browser preview at desktop and mobile widths.
- Link check for primary collection and product URLs.

Expected evidence:
- Screenshot or browser inspection confirms layout is not broken.
- Static check confirms expected links and local assets.

Risk note:
- Product prices are static and must be checked before Shopify publish.

## Step 3: Verification And GitHub Publish

Goal: verify the page and publish scoped changes.

Spec summary:
- Inputs: completed page and docs.
- Outputs: Git commit and push to GitHub Pages repository.
- Boundaries: do not stage unrelated existing files.

Files involved:
- New page directory.
- Optional root `index.html` link.

Acceptance criteria:
- `git status` shows only intended files staged.
- Commit is created with a purposeful message.
- Push succeeds to `origin/master`.

Validation:
- `git diff --cached --name-only`
- local browser or static HTML checks
- `git status --short --branch`

Expected evidence:
- Commit hash and GitHub Pages path.

Risk note:
- Existing untracked PageFly exports must remain unstaged unless explicitly requested.
