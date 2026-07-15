# Ceiling Cassette vs Concealed Ducted Decision Page

This context defines the project-specific language used to describe the two shopping paths and their curated product recommendations.

## Language

**System Type**:
One of the two compared indoor-unit paths: **Ceiling Cassette** or **Concealed Ducted**.
_Avoid_: Product type, setup type, mount choice

**Recommended Product Set**:
The four user-approved Della products belonging to one **System Type**.
_Avoid_: Supporting products, inventory grid, full collection

**Recommended Starting Point**:
The single product within a **Recommended Product Set** highlighted as the broadest initial comparison point, not a universal best choice.
_Avoid_: Best product, winner, default purchase

**Collection Path**:
The Della collection destination where a shopper can browse all available products for one **System Type**.
_Avoid_: Shop all products, category page

**Displayed Price**:
The current verified Shopify selling price presented on a recommended product card.
_Avoid_: Mockup price, reference-page price, estimated price

**Preview Price**:
A dated static snapshot of the **Displayed Price** used only in the local or GitHub HTML review build.
_Avoid_: Production price, permanent price

**Production Price**:
The **Displayed Price** rendered dynamically from Shopify product data on the live store.
_Avoid_: Hard-coded price, screenshot price

**Landing Page Body**:
The complete comparison content authored by this project, excluding the theme's global Header, navigation, and Footer.
_Avoid_: Landing page shell, full theme page

**Storefront Chrome**:
The active Della theme's global Header, navigation, and Footer surrounding the **Landing Page Body** in Shopify production.
_Avoid_: Landing page body, custom page navigation

**Conceptual Planning Diagram**:
A not-to-scale decision aid showing only verified project-planning relationships, never product-specific installation construction.
_Avoid_: Installation drawing, equipment cutaway, technical schematic

**Why Shop Della?**:
The fixed four-item trust set for this decision page: Free Shipping Sitewide, 24/7 Live Chat Support, Lifetime Coverage on Mini Splits, and Product Guidance Before You Buy.
_Avoid_: Trust cards, support grid, service benefits

## Relationships

- The page compares exactly two **System Types**.
- Each **System Type** has exactly one **Recommended Product Set** containing four products.
- Each **Recommended Product Set** has exactly one **Recommended Starting Point**.
- Each **System Type** routes to exactly one primary **Collection Path**.
- Every product in a **Recommended Product Set** has one **Displayed Price**.
- A **Preview Price** and its corresponding **Production Price** represent the same product's **Displayed Price** in different delivery environments.
- Preview renders the **Landing Page Body** alone.
- Shopify production renders the **Landing Page Body** once inside the normal **Storefront Chrome**.
- Each **System Type** has one **Conceptual Planning Diagram**.
- **Why Shop Della?** contains exactly four approved service labels and appears once after product recommendations.

## Example dialogue

> **Developer:** "Should both **Recommended Product Sets** be visible together?"
> **Domain expert:** "No. Show the set for the selected **System Type**, then provide its **Collection Path** for broader shopping."

## Flagged ambiguities

- "Two product groups" previously risked meaning two vertically stacked sections; resolved: they are two mutually exclusive system states.
- "Supporting products" implied that three products were secondary inventory; resolved: all four products in each set are recommended, with one compact **Recommended Starting Point** distinction.
- "Show price" could mean reusing prices visible in a reference screenshot; resolved: each **Displayed Price** must come from current Shopify data.
- "Static versus dynamic price" is environment-specific; resolved: previews use a dated **Preview Price**, while Shopify uses a dynamic **Production Price**.
- "No Header and Footer" applies only to the local/GitHub preview and to content authored inside the **Landing Page Body**; Shopify production keeps the normal **Storefront Chrome**.
- "Technical diagram" previously implied an installation drawing; resolved: the page uses a **Conceptual Planning Diagram** and defers exact installation facts to product documentation and qualified HVAC review.
- "Lifetime Coverage" means the exact short label inside **Why Shop Della?**; it does not authorize additional compressor, parts, labor, duration, or eligibility claims on this page.
