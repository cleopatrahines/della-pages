"""Owner-authorized alpha-only cutouts, following the Whole House workflow.

Reads originals in the comparison project. Writes derivatives and QA evidence
beside this script. Does not edit the HTML or overwrite original photos.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import hashlib
import json
import shutil
import numpy as np

PROJECT = Path(r'C:\Users\18041\Desktop\della-pages\Mini Split vs Window AC vs Portable AC')
STAGE = Path(__file__).resolve().parent
OUT = STAGE / 'assets' / 'products-cutout'
QA = STAGE / 'qa' / 'image-refinement-20260917'
OUT.mkdir(parents=True, exist_ok=True)
QA.mkdir(parents=True, exist_ok=True)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def process(source, target):
    original = Image.open(source).convert('RGB')
    rgb = np.asarray(original).astype(np.int16)
    border = np.concatenate([rgb[:5].reshape(-1, 3), rgb[-5:].reshape(-1, 3),
                             rgb[:, :5].reshape(-1, 3), rgb[:, -5:].reshape(-1, 3)])
    key = np.median(border, axis=0)
    candidate = np.max(np.abs(rgb - key), axis=2) <= 4
    # Inspected Serena front-panel reflection matches the backdrop color.
    # Protect this interior surface; no source RGB is changed.
    protected = []
    if source.name in ('p02.jpg', 'p03.jpg'):
        candidate[400:645, 183:1894] = False
        protected.append([183, 400, 1894, 645])
    flood = Image.fromarray((candidate * 255).astype('uint8')).copy()
    for point in [(0, 0), (original.width - 1, 0),
                  (0, original.height - 1), (original.width - 1, original.height - 1)]:
        if flood.getpixel(point) == 255:
            ImageDraw.floodfill(flood, point, 128, thresh=0)
    background = np.asarray(flood) == 128
    # Window exports have a bright bottom scanline and JPEG ringing in 8 rows.
    # These near-uniform export borders are outside all equipment.
    cleared_border = False
    if source.name in ('p05.jpg', 'p06.jpg', 'p07.jpg', 'p08.jpg'):
        assert np.max(np.ptp(rgb[-8:], axis=1)) <= 4
        background[-8:] = True
        cleared_border = True
    fraction = float(background.mean())
    if not .05 < fraction < .90:
        raise ValueError(f'Unexpected removed area {source.name}: {fraction}')
    alpha = Image.fromarray(np.where(background, 0, 255).astype('uint8'))
    alpha = alpha.filter(ImageFilter.GaussianBlur(.35))
    bounds = alpha.getbbox()
    if bounds is None:
        raise ValueError(f'Empty foreground: {source}')
    rgba = original.convert('RGBA')
    rgba.putalpha(alpha)
    crop = rgba.crop(bounds)
    pad = max(8, round(max(crop.size) * .025))
    result = Image.new('RGBA', (crop.width + pad * 2, crop.height + pad * 2), (255, 255, 255, 0))
    result.paste(crop, (pad, pad))
    result.save(target, optimize=True)
    # Confirm PNG round-trip retains every cropped RGB value, not only opaque pixels.
    decoded = np.asarray(Image.open(target).convert('RGBA'))
    cropped_source = rgb[bounds[1]:bounds[3], bounds[0]:bounds[2]].astype(np.uint8)
    recovered = decoded[pad:pad+crop.height, pad:pad+crop.width, :3]
    assert np.array_equal(cropped_source, recovered), 'RGB changed'
    assert decoded[:, :, 3].min() == 0 and decoded[:, :, 3].max() == 255
    return {'sourceSize': list(original.size), 'outputSize': list(result.size),
            'sourceCropBox': list(bounds), 'padding': pad, 'backgroundRGB': key.tolist(),
            'removedFraction': round(fraction, 5), 'tolerance': 4, 'alphaFeatherPx': .35,
            'sourceRGBPreserved': True, 'trueAlpha': True,
            'protectedInteriorBoxes': protected, 'bottomExportBorderRowsRemoved': 8 if cleared_border else 0}

manifest = json.loads((STAGE / 'products.json').read_text(encoding='utf-8-sig'))
cache = {}
records = []
for product in manifest['products']:
    relative = product.get('originalLocalImage', product['localImage'])
    source = PROJECT / relative
    source_hash = sha(source)
    target = OUT / (product['id'] + '.png')
    if source_hash in cache:
        first, info = cache[source_hash]
        shutil.copyfile(first, target)
        info = dict(info, reusedFrom=first.name)
    else:
        info = process(source, target)
        cache[source_hash] = (target, info)
    assert sha(source) == source_hash, 'Original modified'
    product['originalLocalImage'] = relative
    product['localImage'] = 'assets/products-cutout/' + target.name
    product['imageWidth'], product['imageHeight'] = info['outputSize']
    records.append(dict(id=product['id'], original=relative, output=product['localImage'],
                        sourceSHA256=source_hash, outputSHA256=sha(target), **info))
    print(json.dumps({'id': product['id'], 'size': info['outputSize'],
                      'removed': info['removedFraction'], 'reused': info.get('reusedFrom')}, ensure_ascii=False), flush=True)

manifest['imageProcessing'] = {'date': '2026-09-17', 'method': 'Owner-approved edge-connected alpha-only removal',
                               'originalsPreserved': True, 'uniqueOriginals': len(cache)}
(STAGE / 'products.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
(QA / 'cutout-report.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')

unique_records = []
seen = set()
for record in records:
    if record['sourceSHA256'] not in seen:
        seen.add(record['sourceSHA256'])
        unique_records.append(record)

for theme, background in [('white', (255,255,255,255)), ('dark', (35,43,60,255))]:
    sheet = Image.new('RGBA', (1400, 920), background)
    draw = ImageDraw.Draw(sheet)
    color = 'black' if theme == 'white' else 'white'
    for index, record in enumerate(unique_records):
        x, y = (index % 4) * 350, (index // 4) * 460
        thumb = Image.open(STAGE / record['output']).convert('RGBA')
        thumb.thumbnail((318, 408), Image.Resampling.LANCZOS)
        sheet.alpha_composite(thumb, (x + (350-thumb.width)//2, y + 28 + (408-thumb.height)//2))
        draw.text((x+16, y+8), record['id'] + ' / alpha-only / original RGB', fill=color)
    sheet.convert('RGB').save(QA / ('cutouts-' + theme + '.png'))
print(json.dumps({'complete': True, 'products': len(records), 'uniqueSources': len(cache)}), flush=True)
