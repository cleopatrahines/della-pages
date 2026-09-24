# Product card imagery

Eight original product photographs are preserved in `assets/product-original-01.webp` through `product-original-08.webp`. The cards use their corresponding transparent PNG derivatives in `assets/products-cutout/`.

Owner-approved programmatic processing follows the supplied DELLA comparison page: estimate the outer neutral backdrop color, remove edge-connected matching pixels at RGB tolerance 4, feather alpha by 0.35px, crop external transparent space, and add 2.5% transparent padding. Product shape, markings, grille, remotes, pipes and accessories retain their source RGB pixels. No generated equipment images are used in these cards.

Each output was decoded and compared against the cropped source: every RGB pixel is unchanged. Source SHA256 hashes confirm originals are unchanged. The alpha channels contain real transparency. White and dark contact sheets were visually reviewed for product completeness and accidental holes. Original contact shadows and ambiguous enclosed spaces within pipe coils are conservatively retained, as in the reference workflow.

The image containers use a pure-white square surface, `object-fit: contain`, and the reference page's desktop inset. The mobile product card structure is retained with a white square thumbnail. Product text, prices, destinations, tabs, hero, and category feature illustrations retain their existing values.

Source comparison page: https://cleopatrahines.github.io/della-pages/Mini%20Split%20vs%20Window%20AC%20vs%20Portable%20AC/mini-split-vs-window-ac-vs-portable-ac.html

Processing code, source/output hashes, original HTML backup, and visual evidence: `C:/Users/18041/Documents/Playground/della-product-cutouts-20260923/`.
