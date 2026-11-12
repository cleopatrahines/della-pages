"""Copy the shared DELLA v2 blocks (CSS, JS, icons, trust) into every v2 page.

Usage: python _system/sync.py            # all pages listed in PAGES
       python _system/sync.py --check    # report pages that are out of date, change nothing
       python _system/sync.py --only <path or part of it>   # sync just the matching page(s)
A page joins the system once it contains the START/END markers; this script only replaces
what is between them.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYS = os.path.join(ROOT, '_system')

PAGES = [
    'Mini Split for Bedroom/mini-split-for-bedroom.html',
    'mini-split-for-basement.html',
    'Mini Split for Whole House/mini-split-for-whole-house.html',
    'mini-split-for-old-house.html',
    '12000 BTU vs 18000 BTU Mini Split/12000-btu-vs-18000-btu-mini-split.html',
    'DIY Mini Split Installation Guide/diy-mini-split-installation-guide.html',
    'Mini Split vs Window AC vs Portable AC/mini-split-vs-window-ac-vs-portable-ac.html',
    'mini-split-for-sunroom.html',
    'mini-split-for-attic.html',
    'Ceiling Cassette vs Wall Mount Mini Split/ceiling-cassette-vs-wall-mount-mini-split.html',
    'Ceiling Cassette vs Concealed Ducted Mini Split/ceiling-cassette-vs-concealed-ducted-mini-split.html',
    'mini-split-for-apartment.html',
    'mini-split-for-shed.html',
    '2-zone-vs-3-zone-mini-split/2-zone-vs-3-zone-mini-split.html',
    'Ductless Mini Split vs Central Air/ductless-mini-split-vs-central-air-nov.html',
]


def block(text, start, end):
    m = re.search(re.escape(start) + r'.*?' + re.escape(end), text, re.S)
    if not m:
        raise SystemExit(f'marker {start!r} missing in source')
    return m.group(0)


css = open(os.path.join(SYS, 'della-landing-v2.css'), encoding='utf-8').read()
js = open(os.path.join(SYS, 'della-landing-v2.js'), encoding='utf-8').read()
mods = open(os.path.join(SYS, 'modules.html'), encoding='utf-8').read()
BLOCKS = [
    ('/* === DELLA SYSTEM v2 START', 'DELLA SYSTEM v2 END === */', block(css, '/* === DELLA SYSTEM v2 START', 'DELLA SYSTEM v2 END === */')),
    ('/* === DELLA SYSTEM v2 JS START', 'DELLA SYSTEM v2 JS END === */', block(js, '/* === DELLA SYSTEM v2 JS START', 'DELLA SYSTEM v2 JS END === */')),
    ('<!-- DELLA ICONS START -->', '<!-- DELLA ICONS END -->', block(mods, '<!-- DELLA ICONS START -->', '<!-- DELLA ICONS END -->')),
    ('<!-- DELLA TRUST START -->', '<!-- DELLA TRUST END -->', block(mods, '<!-- DELLA TRUST START -->', '<!-- DELLA TRUST END -->')),
]

check = '--check' in sys.argv
only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None
for rel in PAGES:
    if only and only not in rel:
        continue
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        print('missing ', rel); continue
    text = open(path, encoding='utf-8').read()
    new = text
    found = 0
    for start, end, src in BLOCKS:
        pat = re.compile(re.escape(start) + r'.*?' + re.escape(end), re.S)
        if pat.search(new):
            found += 1
            new = pat.sub(lambda _: src, new, count=1)
    if not found:
        print('not v2  ', rel); continue
    if found < len(BLOCKS):
        print(f'partial  {rel} ({found}/{len(BLOCKS)} blocks)')
    if new == text:
        print('ok      ', rel)
    elif check:
        print('stale   ', rel)
    else:
        open(path, 'w', encoding='utf-8', newline='\n').write(new)
        print('synced  ', rel)
