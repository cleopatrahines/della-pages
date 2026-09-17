# Asset provenance and use

Date: 2026-09-16. Project assets are local to this folder; source originals are retained.

## Owner-supplied visual identity

- `assets/source/owner-mini-split-pair-blue-1.png`: original attachment `codex-clipboard-d5e56205-1ce2-4a9f-9b81-798eb6ccdcd3.png`.
- `assets/source/owner-mini-split-pair-blue-2.png`: original attachment `codex-clipboard-601a0442-75a5-4595-a2bb-a11d5c89d74a.png`.
- `assets/source/owner-mini-split-indoor.png`: original attachment `codex-clipboard-c4941604-b2c0-45fb-9953-a21d76f4a37e.png`.

The owner explicitly requested these indoor/outdoor machine appearances for scene imagery. Preserve the original attachments. No model number, voltage, capacity or certification is inferred from these reference photos.

Additional owner-supplied equipment references:

- `assets/source/owner-portable-studio.png`: `codex-clipboard-1d0a7861-bcd1-4b61-b4ac-65937b781f4f.png`; selected portable casing/top-outlet reference.
- `assets/source/owner-portable-dual-hose-install.png`: `codex-clipboard-65747936-cf35-444a-9e22-6cf2d457d745.png`; selected two-hose window-panel arrangement.
- `assets/source/owner-portable-blue-alternative.png`: `codex-clipboard-230a82eb-e335-45bb-8b42-12db84cba396.png`; alternate supplied casing, retained for reference rather than mixed with the selected smooth-front machine.
- `assets/source/owner-window-lifestyle.png`: `codex-clipboard-7ed5d371-4c39-4152-ae0e-46c7aac290bf.png`; alternative lifestyle reference. Its promotional text and percentages are not page copy.
- `assets/source/owner-window-studio.png`: `codex-clipboard-918bf013-d44f-45bf-b150-3c3f01aefbfa.png`; selected window AC appearance with finely perforated grille and upper-left controls.

## Generated assets

- `assets/hero-desktop.png`: wide desktop scene, clean left copy area, owner-reference mini-split pair fully visible, window AC and portable alternatives with natural architecture.
- `assets/hero-mobile.png`: separately composed mobile scene with all three types, including both mini-split units, visible below the HTML heading.
- `assets/installation-comparison.png`: explanatory architectural illustration, with condenser outdoors, wall head inside, window AC in window and portable exhaust outdoors.
- `design/final-mockup-v6.png`: full-page layout reference, updated to use the final scene direction and all three owner-specified equipment types.

These are image-tool outputs edited/generated with the supplied references, not mechanically exact product photographs or engineered installation plans. They convey category/setup relationships. Real text/labels/controls are implemented in HTML. Product cards use the official corresponding product images below.

Final original image-tool file locations and checksums are recorded in `evidence/delivery-manifest.json`. Prior generated assets are retained in `design/archive/` as appropriate and are not active implementation inputs.

## Official commerce images

`assets/products/p01.jpg` to `p11.jpg` are downloaded from the source `imageUrl` associated with each product/selected variant in products.json. Images are copied as delivered by Shopify and not edited. Product images may be shared by the brand across capacities; the file's name is not a product-specification source.

Prices/identity/variant links are in products.json. Date and source details are in PRODUCTS.md and evidence/catalog-handoff-snapshot.json. Source media may include brand marks or badges; do not extend those marks into unsupported claims elsewhere on the page.

## Fonts

Local WOFF2 files copied from the existing DELLA `single-zone-vs-multi-zone-mini-split` project:

- Spectral-Regular.woff2
- Spectral-Bold.woff2
- Poppins-400.woff2
- Poppins-600.woff2

Use for headings/prices/body per DESIGN.md. Reuse the existing project assets; no new external font dependency.

## Icon and label treatment

Service icons use the original embedded artwork from the Central Air reference. Hero and installation imagery display without overlay labels. Do not crop either mini-split unit, add heavy white divider bars, or obscure the portable hose with a label.


## 2026-09-17 visual refresh

The three scene assets and all product images are unchanged. design/final-mockup-v6.png updates layout and content density; design/portable-panel-v6.png specifies three full-row equal cards. Raster text, prices and radii defer to current DESIGN / LOCKED-COPY / products.json. Original generator locations and hashes are in evidence/visual-refresh-20260917/manifest.json.

Spectral-PageFly-Medium.woff2 is additionally copied from the Whole House assets/fonts directory for the source's 500-weight headings and product names. Existing font and image originals remain preserved.


## Active product derivatives — 2026-09-17

Use assets/products-cutout/p01.png through p11.png for comparison and commerce media. Owner authorized alpha-only programmatic processing modeled on Whole House. Original RGB pixels and original JPEG files are retained. The manifest localImage field points to the derivative; originalLocalImage retains its source. ImageWidth/imageHeight record the new canvas dimensions. Method, bounds, hashes and white/dark inspection sheets: PRODUCT-IMAGE-PROCESSING.md and qa/image-refinement-20260917. Scene assets remain unchanged.
