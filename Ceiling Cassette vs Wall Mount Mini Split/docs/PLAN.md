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
- Inputs: product URLs, image URLs, Della lifestyle assets, brand tokens, existing Single-Zone comparison page patterns.
- Outputs: standalone HTML and local assets.
- Boundaries: no dynamic Shopify product data.

Files involved:
- `ceiling-cassette-vs-wall-mount-mini-split.html`
- `assets/*`

Acceptance criteria:
- Above-fold full-bleed lifestyle hero, verdict, and two collection CTAs are visible.
- Overlay commerce nav includes only Ceiling Cassette, Wall Mount, Compare Fit, and Find Installer.
- Quick answer is two path cards.
- Decision checker asks five install-fit questions and updates the recommendation.
- Comparison section has 7-8 rows and becomes stacked cards on mobile.
- Product area starts with two collection path cards, then popular comparison picks; no static demo pricing notes remain.
- Installation feasibility and mixed-indoor-unit modules are present.

Validation:
- Browser preview at desktop and mobile widths.
- Link check for primary collection and product URLs.

Expected evidence:
- Screenshot or browser inspection confirms layout is not broken.
- Static check confirms expected links and local assets.

Risk note:
- PDP pricing should be dynamic in Shopify or handled through `See Current Price` links.

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
