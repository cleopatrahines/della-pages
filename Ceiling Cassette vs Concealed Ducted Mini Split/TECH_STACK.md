# TECH STACK: Ceiling Cassette vs Concealed Ducted Mini Split

## Status

- Approved architecture: dedicated Shopify Online Store 2.0 section plus JSON page template.
- Current implementation state: complete static preview with shared namespaced CSS/JavaScript and final local visual assets. Shopify Liquid and JSON have not started.
- Current QA state: Step 5 acceptance run completed but remains blocked; no implementation code changed during the acceptance run.

## Delivery Forms

### Static Preview

- One semantic HTML file named `ceiling-cassette-vs-concealed-ducted-mini-split.html`.
- Shared local CSS and JavaScript assets, validated through a temporary local fixture.
- Dated static Preview Prices.
- No Header, navigation, or Footer.
- Suitable for local and GitHub Pages visual review.

### Shopify Production

- One dedicated Liquid section.
- One dedicated JSON page template containing the section once.
- Dynamic prices from the eight approved Shopify product objects.
- Active Della theme owns global Header, Footer, page metadata, canonical behavior, and money formatting context.
- No PageFly component dependency.

## Frontend

- Semantic HTML5.
- Namespaced CSS with Della PageFly/Memorial tokens.
- Minimal vanilla JavaScript for accessible product tabs and optional stable measurement hooks.
- Native `details` and `summary` for FAQ.
- Editable HTML/SVG conceptual planning diagrams.
- No framework, package manager, bundler, or runtime dependency is required for V1.

## Typography And Assets

- Spectral Regular, Medium, and Bold local WOFF2 files, exposed as flat runtime assets for Shopify compatibility.
- Poppins 400 and 600 local WOFF2 files, exposed as flat runtime assets for Shopify compatibility.
- Official Della CDN product images as approved in the PRD.
- Four localized official Della service icons.
- Open-Concept and Finished-Basement project scenes are approved and localized as flat runtime assets.
- Hero, Quick Answer, Project Fit, Key Differences, and Installation Requirements use the supplied final local WebP/PNG assets. Product cards retain their approved Della CDN identity images.

## Data Contracts

- Product identity: exact PRD handles and approved image URLs.
- Preview price: live Shopify `.js` snapshot with date and source record.
- Production price: Shopify product object with money filter; prefix `From` when `price_varies` is true.
- Product substitutions are never automatic.

## Validation

- Docs and data: path, hash, URL, availability, price, and source checks.
- PDF evidence: text extraction plus visual inspection of relevant official manual pages.
- Frontend later: browser screenshots, keyboard interaction, overflow, links, console, semantic structure, and price parity.
- Shopify later: theme syntax/preview, section reload behavior, product resolution, Header/Footer count, metadata, and schema.

## Current Environment Limits

- The normal web-access CDP prerequisite is unavailable because the system Node.js prerequisite is missing; official Shopify JSON and direct official-page reads were used for Step 1.
- Step 2 interaction and responsive checks were completed through the app browser against a temporary localhost fixture; no dependency installation was needed.
- No active Della theme export or theme preview environment exists in the project, so final Shopify integration cannot yet be accepted.
- No new dependency installation is authorized or required.
