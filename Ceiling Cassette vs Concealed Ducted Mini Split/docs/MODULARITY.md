# Modularity

## Current Review

- Shared implementation code now consists of one 341-line namespaced CSS asset and one 97-line JavaScript asset; the static preview HTML is 357 lines.
- CSS stays below the 500-line review threshold and contains no unscoped page or element selectors.
- JavaScript functions stay below 50 lines and are limited to product tabs, keyboard handling, progressive enhancement, and Shopify section reloads.
- Flat runtime font, service-icon, and approved project-scene assets avoid path differences between static preview and Shopify.
- Step 1 nested asset folders remain as source archives; runtime code references only the flat assets.

## Implementation Constraints

- Keep page CSS in one namespaced asset unless it exceeds 500 lines or mixes unrelated responsibilities.
- Keep JavaScript limited to product tabs and approved measurement helpers; functions should remain under 50 lines.
- Keep the Liquid section focused on semantic markup, product resolution, and section settings. Do not embed the full CSS or duplicate JavaScript.
- If repeated product-card Liquid makes the section exceed 500 lines, introduce one cohesive product-card snippet rather than duplicating markup.
- Keep preview and Shopify behavior equivalent through shared CSS/JavaScript, but do not invent a build system solely to eliminate static/Liquid markup differences.
- Do not create generic component abstractions that are used only once.

## Review Triggers

- Any code file over 500 lines.
- Any function over 50 lines.
- Selector leakage outside the page namespace.
- Duplicate tab or FAQ logic.
- Product data repeated in more than the two required delivery forms without a documented reason.
- Temporary or unused assets remaining after a step.

## Next Review

The user-requested final image integration removes obsolete Hero, comparison, planning, and placeholder markup. The standalone-preview benefit strip is intentionally absent. Rerun this review after browser acceptance passes or after Step 6 creates the Liquid section.
