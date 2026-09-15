"""Build static Bedroom-style cards from the verified catalogue."""
import json
import pathlib
import re
from html import escape

ROOT = pathlib.Path(__file__).resolve().parent
FORMATS = {'Wall-Mounted': 'wall-mounted', 'Ceiling Cassette': 'ceiling-cassette', 'Concealed Ducted': 'concealed-ducted'}

def card(p):
    esc = lambda v: escape(str(v), quote=True)
    units = ' + '.join(f'{n / 1000:g}K' for n in p['indoor_btu'])
    ef = p['efficiency']
    status = 'Available' if p['available_at_verification'] else 'Check availability'
    return f'''<li class="product-card" data-key="{esc(p['key'])}" data-zones="{p['zones']}" data-format="{FORMATS[p['format']]}">
<span class="product-badge">{p['zones']}-Zone · {esc(p['format'])}</span>
<div class="product-image-wrap"><img class="product-image" src="{esc(p['image_file'])}" alt="{esc(p['full_title'])}" width="{p.get('image_width', 2000)}" height="{p.get('image_height', 2000)}" loading="lazy"></div>
<div class="product-card-body">
<h3 class="product-title">{esc(p['series'])}</h3>
<p class="product-capacity">{p['listed_system_btu']:,} BTU · {p['zones']}-Zone</p>
<dl class="product-meta"><div><dt>Indoor units</dt><dd>{units}</dd></div><div><dt>Efficiency</dt><dd>{ef['value']:g} {esc(ef['metric'])}</dd></div><div><dt>Voltage</dt><dd>{esc(p['voltage'])}</dd></div></dl>
<details class="product-identity"><summary>Full model name</summary><p class="product-full-name">{esc(p['full_title'])}</p></details>
<p class="product-price">${p['price']:,.2f}</p><p class="availability">{status}</p>
<a class="btn btn-product product-link" href="{esc(p['url'])}" target="_blank" rel="noopener" aria-label="View {esc(p['full_title'])}">View Product</a>
</div></li>'''

def main():
    data = json.loads((ROOT / 'products.json').read_text(encoding='utf-8'))
    lookup = {p['key']: p for p in data['products']}
    order = data['display_order']
    if len(set(order)) != len(order) or set(order) != set(lookup):
        raise ValueError('Invalid product order')
    fragment = '<!-- PRODUCT_CARDS:START -->\n<ul class="product-grid" id="productGrid">\n' + '\n'.join(card(lookup[k]) for k in order) + '\n</ul>\n<!-- PRODUCT_CARDS:END -->'
    (ROOT / 'product-cards.fragment.html').write_text(fragment, encoding='utf-8')
    file = ROOT / 'mini-split-for-whole-house.html'
    html, count = re.subn(r'<!-- PRODUCT_CARDS:START -->.*?<!-- PRODUCT_CARDS:END -->', lambda _: fragment, file.read_text(encoding='utf-8'), flags=re.S)
    if count != 1:
        raise ValueError('Expected one injection location')
    file.write_text(html, encoding='utf-8')
    print(f'Injected {len(order)} verified cards')

if __name__ == '__main__':
    main()
