# GitHub Pages release review — 2026-09-17

Status: reviewed and approved for the owner-authorized commit, push and GitHub Pages publication.

Reviewed HTML: mini-split-vs-window-ac-vs-portable-ac.html; 66,193 bytes.
SHA256: 11DF4D0CDF4191ACA2E378F49ACB59E4406A034F7A38A50171C87715AC8B6CC8

## Final verification

- Codex reran the targeted Chrome CDP suite: **44/44 passed, exit 0**, with seven fresh captures. Results: qa/codex-publish-review-20260917/qa-results.json. Reproduce via qa/copy-refinement-implementation-20260917/capture.mjs.
- All 12 approved copy replacements match. Reversing them reconstructs the exact recorded pre-edit HTML SHA256 682BA16593B961A9E8AE243B016986F715C17B9AF03E18481DC8426C1E4CB89C. CSS, JavaScript, attributes, links and product data are otherwise identical to that baseline.
- Inspected desktop painted-Hero, mobile and expanded-Evidence captures. New wording fits, images and text remain clear, Evidence answers are not clipped. Mobile Tabs stay on one row and purchase areas retain 16px spacing.
- Four FAQ items, four Evidence items, 11 cards, 19 initially closed disclosures; comparison routing, tabs, no page overflow, no console errors and no failed requests passed.
- DeepSeek's separately recorded full regression is **127/127**, including the previous image, typography, navigation and no-JS requirements. Codex did not relabel that result as a newly rerun full suite.

## Publication

Verified GitHub Pages configuration: legacy build, master branch, repository root. Before release origin/master was one commit behind HEAD, consisting only of this page's initial commit 1baf1c3. This release adds its copy refinement and one-row mobile Tab styling. Only this project is staged; unrelated local changes remain untouched.

Public destination: https://cleopatrahines.github.io/della-pages/Mini%20Split%20vs%20Window%20AC%20vs%20Portable%20AC/mini-split-vs-window-ac-vs-portable-ac.html

After push, verify the Pages build for the pushed commit and fetch the destination to check the current copy and assets. Remote completion is reported from those checks, not inferred from a successful push alone.

## Limits

Full-page headless captures can omit Hero pixels after scrolling; the separately inspected actual-painted clip contains the scene. This is not a formal full-page pixel diff. Physical touch devices, Safari/Firefox and Shopify embedding are not tested.

Commercial facts were unchanged and were not newly fetched by Codex. The same-day live product check is DeepSeek's recorded evidence. This GitHub Pages release remains a static preview; live Shopify product rendering and production theme integration are separate work.
