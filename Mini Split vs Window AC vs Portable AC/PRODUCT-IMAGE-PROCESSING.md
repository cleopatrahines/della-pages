# Product image processing — 2026-09-17

Owner explicitly approved the Whole House programmatic background-removal workflow. Originals remain in assets/products. Eleven transparent PNG derivatives in assets/products-cutout correspond to eight unique source images; p02/p03, p06/p08 and p09/p10 share identical source/derivative bytes.

## Method

Pillow and NumPy, no generative repainting. Estimate the neutral background from the outer five-pixel border. Flood-fill only edge-connected pixels within four RGB levels of that color. Preserve the visually inspected Serena front-panel reflection with an interior protection box. Remove the near-uniform bottom eight-row export border from the window photos. Feather alpha by 0.35px, crop surrounding transparent area, and add 2.5% transparent safety padding.

RGB channels of every cropped source pixel are retained byte-for-byte, including behind transparent pixels. Only alpha, canvas bounds and padding change. Model shape, logo, display, fins, pipes, labels, phones and remotes are not redrawn. Original JPEG files are not overwritten.

This is a conservative white-page cutout: ambiguous enclosed areas inside pipe coils and original contact shadows remain. It is not a newly photographed or physically relit asset for arbitrary dark backgrounds.

## Verification

`qa/image-refinement-20260917/cutout-report.json` records original and derivative SHA256, crop bounds, output size, protection box, border handling, alpha and RGB equality checks for every ID. White and dark contact sheets were visually inspected for product completeness, accidental transparent holes and stray border artifacts. Source file hashes are checked before and after processing.

`products.json` maps localImage to the PNG, preserves originalLocalImage and includes intrinsic imageWidth/imageHeight. Commercial facts are unchanged. Compare uses p01/p07/p11; all 11 product cards use their own mapped PNG.

`prepare_cutouts.py` is the reproducible processing script. It expects the project directory containing this report, reads originalLocalImage when present, writes derivative assets and refreshes image metadata/evidence. Keep Pillow/NumPy available in the execution environment. The script does not edit HTML.

This report verifies assets and data, not the pending DeepSeek page implementation or a newly checked live price.
