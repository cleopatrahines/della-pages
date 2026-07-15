# Project Agent Instructions

## Always Read Before Action

- Read `PRD.md`, `DESIGN.md`, `PLAN.md`, and `CONTEXT.md` before changing implementation behavior.
- Read `TECH_STACK.md`, `docs/ARCHITECTURE.md`, `docs/MODULARITY.md`, `docs/PROGRESS.md`, and `HANDOFF.md` before executing a planned step.
- Treat the latest explicit user instruction as higher priority than project documents; update the affected source-of-truth document before implementation when a decision changes.

## Workflow Gates

- Execute one `PLAN.md` step at a time by default.
- Define and run the stated verification harness before marking a step complete.
- Stop for user approval after each step unless the user explicitly authorizes multiple steps.
- Do not start shared CSS, preview HTML, Liquid, or JSON before its numbered step is approved.
- After repeated failure, stop patching, capture evidence, identify the likely cause, and update the plan or progress record.

## Project Scope

- Keep the exact nine-section order from `PRD.md`; the authored top Benefit Strip is intentionally omitted.
- Do not add modules, product substitutions, promotional claims, ratings, compare-at prices, or `Add to Cart` without an approved PRD change.
- Use exactly four products per System Type and show one active product tab at a time.
- Preview contains no Header or Footer. Shopify production inherits the active theme Header and Footer exactly once.
- Production uses a dedicated Online Store 2.0 section plus JSON page template, not PageFly components.

## Data And Claim Rules

- Product identity comes from the approved PRD table. Current price and availability come from live Shopify data at the relevant QA time.
- Never copy prices, policy text, technical details, or product data from the mockups or reference screenshots.
- Preview prices are dated snapshots. Production prices are dynamic Liquid output.
- If a product is unavailable, a price cannot be verified, or a live source materially conflicts with the PRD, stop for user review.
- Installation visuals remain conceptual and not to scale. Do not add exact dimensions, internal routing, DIY steps, or unreviewed technical claims.
- FAQ schema is disabled until visible FAQ answers are approved.

## Files And Modularity

- Keep every project artifact under `C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Concealed Ducted Mini Split`.
- Namespace frontend selectors and JavaScript to avoid theme leakage.
- Prefer shared external CSS and JavaScript over duplicated inline implementations.
- Keep code files under 500 lines and functions under 50 lines where practical; document an exception or split recommendation when a limit is exceeded.
- Remove temporary files, debug output, unused assets, dead paths, and placeholders before acceptance.

## Verification And External Actions

- Frontend acceptance requires browser checks at 1440, 1280, 768, 430, 390, and below 360 pixels as defined in `PLAN.md`.
- Verify keyboard tabs, FAQ controls, focus states, links, overflow, product data, prices, schema, and Shopify Header/Footer behavior.
- Do not commit, push, upload to a theme, assign a production template, or publish without explicit user approval and current QA evidence.
- Preserve unrelated user changes and inspect git status before any checkpoint action.

## Language

- Project documentation, code comments, and commit messages are in English.
- User-facing reports are in Chinese unless the user requests otherwise.
