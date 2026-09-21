# QA — selector editorial studio + compact comparison (2026-09-21)

Target: `ceiling-cassette-vs-wall-mount-mini-split.html`
Backup before this round: `backup-editorial-studio-20260921-100120.html`

Real browser: headless Chrome via CDP, local file.

## Interaction results

- Default: 0 radios checked, result `is-empty`, primary CTA hidden, `Compare both
  styles` visible, Reset hidden. No preselection. PASS
- priority=look + wall=no + ceiling=unknown → **"Check ceiling feasibility first"** PASS
- ceiling=yes + wall=yes + priority=look → **"Compare ceiling cassettes first"**,
  CTA "View cassette options →" → ceiling collection. PASS
- Reset: 0 checked, 0 `.is-selected`, result back to empty prompt, Reset hidden. PASS
- Info note: hidden by default; click opens (`aria-expanded=true`); Escape closes. PASS
- Touch targets: every `.checker-option` ≥ 44px (min measured 44); info button 44×44. PASS

## Layout / media

- Selector image: rendered ratio 1.778 vs natural 1.777 → not distorted; both units
  fully visible; 16:9 frame (no longer 4:3).
- Comparison media: desktop frame 120px (cassette max 180px, wall max 230px),
  mobile frame 96px; `object-fit: contain`. Header height reduced.
- No horizontal overflow: 1440, 1024, 768, 430, 390, 360 all `scrollWidth == clientWidth`.

## Preserved

- 5 FAQ items ↔ JSON-LD: decoded question lists identical. PASS
- `#products` (4 cards, 4 tabs) and `#services` (4 cards) present; region byte-identical
  to the pre-round backup.
- All 13 images load after scroll (0 failed). Console: no errors or warnings.

## Screenshots (absolute paths)

```
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\selector-1440.png
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\selector-390.png
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\selector-result-1440.png
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\selector-result-390.png
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\selector-info-open-390.png
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\comparison-1440.png
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\comparison-390.png
```

Screenshots are module clips (element bounds).
