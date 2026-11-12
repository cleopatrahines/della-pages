"""Generate DELLA landing-page photos with gpt-image-2.6 (edits endpoint + product reference).

Usage: python -I gen_della.py <jobs.json> <out_dir> [name ...]
jobs.json: {"name": {"prompt": "...", "size": "3072x2048", "quality": "high", "kind": "indoor|outdoor|plain", "ref": "optional path"}}
kind picks the shared style text and the default reference image:
  indoor  -> _refs/waiji.png (wall-mounted indoor unit)   [default]
  outdoor -> _refs/aq.png    (outdoor condenser on a wall)
  plain   -> style text only, no product description (pass your own ref, or none)
"raw": true sends the prompt alone (no style/unit text): use it to edit an existing image passed first in "ref".
Existing outputs are skipped; delete one to regenerate. GEN_WORKERS sets parallel calls (default 3).
"""
import base64, io, json, os, sys, urllib.request, uuid, concurrent.futures as cf
from PIL import Image

KEY = os.environ['OPENAI_API_KEY']
MODEL = 'gpt-image-2.6-sunburst'
REFS = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '_refs')

LOOK = (
    ' Style: Homary room-ideas catalog photography (modern minimalist / modern luxury): bright, airy, high-key '
    'daylight through large windows with sheer curtains; generous empty floor and wall space; a few sculptural statement '
    'furniture pieces are the heroes, styled minimally with at most two or three small objects and at most one plant; '
    'no clutter, no rows of lamps. Furniture, materials and palette exactly as described above and nothing borrowed '
    'from other rooms. The space must read instantly as the specific room type described. Eye-level, mostly frontal, '
    'balanced composition. True-to-life color, clean whites, high dynamic range, clean and '
    'crisp: nothing dirty, dusty, hazy, muddy or yellow-cast. Avoid pale blond wood furniture and avoid plain white '
    'bedding everywhere. Staged and uninhabited: absolutely no people, no hands, no body parts and no pets. Shot on a '
    'full-frame camera, 24-35mm lens, straight verticals, sharp detail, photorealistic, not CGI-looking. No text, '
    'captions, extra logos or watermark.'
)
UNIT = {
    'indoor': (
        ' The wall-mounted indoor mini split must match the reference photo exactly and keep its true proportions: a '
        'sleek white unit about three times as wide as it is tall (about 32 inches wide, 11 inches tall, 8 inches deep), '
        'flat glossy front panel with softly rounded corners, a small gray DELLA wordmark at the upper left, a small white '
        'digital "70" temperature display slightly right of center, and a slim horizontal louver along the bottom edge. '
        'Straight, rigid, perfectly level geometry: not stretched, bent, warped, melted or tilted. Mount it high on the '
        'wall, about 8 inches below the ceiling, fully visible with clear wall space on every side. No visible pipes, '
        'cables or brackets indoors.'
    ),
    'outdoor': (
        ' The outdoor condenser must match the reference photo exactly: a white rectangular cabinet with a large round fan '
        'grille on the left, a small blue DELLA badge at the top right, service valve cover on the right side, mounted on '
        'two white wall brackets. Line set runs inside a neat white line-set cover up the wall.'
    ),
    'plain': '',
}
# indoor + outdoor unit in one image (cutaways): both reference photos, both descriptions
UNIT['both'] = UNIT['indoor'] + ' Outside:' + UNIT['outdoor'].replace(' The outdoor', ' the outdoor', 1) +     ' The first reference photo is the indoor unit, the second is the outdoor condenser.'


def multipart(fields, files):
    b = uuid.uuid4().hex
    out = io.BytesIO()
    for k, v in fields.items():
        out.write(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    for k, (fn, data, ct) in files:
        out.write(f'--{b}\r\nContent-Disposition: form-data; name="{k}"; filename="{fn}"\r\nContent-Type: {ct}\r\n\r\n'.encode())
        out.write(data)
        out.write(b'\r\n')
    out.write(f'--{b}--\r\n'.encode())
    return out.getvalue(), f'multipart/form-data; boundary={b}'


def run(name, job, out_dir):
    dst = os.path.join(out_dir, f'{name}.webp')
    if os.path.exists(dst):
        return name, 'skip', None
    kind = job.get('kind', 'indoor')
    ref = job.get('ref') or {'indoor': os.path.join(REFS, 'waiji.png'), 'outdoor': os.path.join(REFS, 'aq.png'),
                             'both': [os.path.join(REFS, 'waiji.png'), os.path.join(REFS, 'aq.png')]}.get(kind)
    refs = ref if isinstance(ref, list) else [ref] if ref else []
    prompt = job['prompt'] if job.get('raw') else job['prompt'] + LOOK + UNIT[kind]
    fields = {'model': MODEL, 'prompt': prompt, 'size': job.get('size', '3072x2048'),
              'quality': job.get('quality', 'high'), 'n': '1'}
    if refs:
        def ct_of(r):
            return 'image/webp' if r.endswith('.webp') else 'image/jpeg' if r.endswith(('.jpg', '.jpeg')) else 'image/png'
        body, ct = multipart(fields, [('image[]', (os.path.basename(r), open(r, 'rb').read(), ct_of(r))) for r in refs])
        url = 'https://api.openai.com/v1/images/edits'
    else:
        body, ct = json.dumps(fields | {'n': 1}).encode(), 'application/json'
        url = 'https://api.openai.com/v1/images/generations'
    req = urllib.request.Request(url, data=body, headers={'Authorization': f'Bearer {KEY}', 'Content-Type': ct})
    for attempt in range(3):
        try:
            data = json.load(urllib.request.urlopen(req, timeout=600))
            break
        except urllib.error.HTTPError as e:
            return name, 'error', e.read().decode()[:400]
        except Exception as e:  # network hiccup: retry
            if attempt == 2:
                return name, 'error', str(e)[:200]
    im = Image.open(io.BytesIO(base64.b64decode(data['data'][0]['b64_json']))).convert('RGB')
    im.save(dst, 'WEBP', quality=84, method=6)
    # web-weight copy next to the 4K master: <name>-1920.webp (used in srcset)
    if im.width > 1920:
        im.resize((1920, round(im.height * 1920 / im.width)), Image.LANCZOS).save(dst[:-5] + '-1920.webp', 'WEBP', quality=84, method=6)
    u = data.get('usage', {})
    return name, f'ok {im.size}', f"in={u.get('input_tokens')} out={u.get('output_tokens')}"


if __name__ == '__main__':
    jobs = json.load(open(sys.argv[1], encoding='utf-8'))
    out_dir = sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    names = sys.argv[3:] or list(jobs)
    with cf.ThreadPoolExecutor(int(os.environ.get('GEN_WORKERS', '3'))) as ex:
        for name, status, extra in ex.map(lambda n: run(n, jobs[n], out_dir), names):
            print(name, status, extra if extra else '')
