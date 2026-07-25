---
status: accepted
---

# Use an Online Store 2.0 section and JSON page template

The page uses PageFly references for Della visual language, but production will use a dedicated Online Store 2.0 Liquid section plus a dedicated JSON page template. This keeps eight product prices dynamic through Shopify product data, makes the page version-controlled, and avoids coupling product rendering and interactions to PageFly components; the local/GitHub HTML remains a static visual-review build with dated price snapshots.

## Considered Options

- PageFly Product Elements or Custom Code were rejected because product binding, interaction control, and long-term versioned maintenance would be less predictable for this custom comparison flow.
- A static Shopify HTML page was rejected because displayed prices could drift from the corresponding PDPs.

## Consequences

- The project has separate preview HTML and Shopify production artifacts.
- Theme integration, header/footer behavior, and product settings must be verified against the active Della theme before deployment.
