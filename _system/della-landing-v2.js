/* === DELLA SYSTEM v2 JS START ===
   Shared behaviour for every topic landing page. Edit ONLY in _system/della-landing-v2.js,
   then run `python _system/sync.py`. Page-specific code goes in a separate <script> after this one. */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const behavior = reduce ? 'auto' : 'smooth';
  window.dellaTrack = (event, data = {}) => { if (Array.isArray(window.dataLayer)) window.dataLayer.push({ event, ...data }); };
  window.dellaScrollTo = el => el && el.scrollIntoView({ behavior, block: 'start' });

  /* dellahome.com has a sticky site header: expose its height as --hdr so the sub-nav and anchor jumps sit below it */
  const root = document.documentElement;
  const hdrs = [...document.querySelectorAll('.shopify-section-group-header-group, sticky-header, .site-header')];
  const fitHdr = () => {
    let h = 0;
    hdrs.forEach(el => { const cs = getComputedStyle(el); if (cs.position === 'sticky' || cs.position === 'fixed') { const r = el.getBoundingClientRect(); if (r.top <= 1) h = Math.max(h, Math.round(r.bottom)); } });
    root.style.setProperty('--hdr', h + 'px');
  };
  if (hdrs.length) { fitHdr(); addEventListener('scroll', () => requestAnimationFrame(fitHdr), { passive: true }); addEventListener('resize', fitHdr); }
  const topOffset = () => (parseFloat(getComputedStyle(root).getPropertyValue('--hdr')) || 0) + (document.querySelector('.subnav')?.offsetHeight || 0);

  /* reveal on scroll */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  /* sticky sub-nav: stuck state + active section (and keep the active pill in view on phones) */
  const subnav = document.querySelector('.subnav');
  if (subnav) {
    const sentinel = document.createElement('div');
    subnav.before(sentinel);
    new IntersectionObserver(([e]) => subnav.classList.toggle('is-stuck', !e.isIntersecting)).observe(sentinel);
    const strip = subnav.querySelector('.subnav-links');
    const links = [...subnav.querySelectorAll('.subnav-links a[href^="#"]')];
    const spy = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return;
      links.forEach(a => {
        const on = a.getAttribute('href') === '#' + e.target.id;
        a.classList.toggle('is-active', on);
        if (on && strip.scrollWidth > strip.clientWidth) strip.scrollTo({ left: a.offsetLeft - 12, behavior });
      });
    }), { rootMargin: '-40% 0px -55% 0px' });
    links.forEach(a => { const s = document.querySelector(a.getAttribute('href')); if (s) spy.observe(s); });
  }

  /* segmented tabs: .seg[role=tablist][data-tabs=x] buttons[data-tab] -> [data-panel] inside [data-tab-scope=x] */
  document.querySelectorAll('.seg[role="tablist"]').forEach(seg => {
    const tabs = [...seg.querySelectorAll('[role="tab"]')];
    const scope = document.querySelector(`[data-tab-scope="${seg.dataset.tabs}"]`) || document;
    const panels = [...scope.querySelectorAll('[data-panel]')];
    const set = (key, source) => {
      const i = Math.max(0, tabs.findIndex(t => t.dataset.tab === key));
      tabs.forEach((t, j) => { t.setAttribute('aria-selected', j === i); t.tabIndex = j === i ? 0 : -1; });
      panels.forEach(p => { p.hidden = p.dataset.panel !== tabs[i].dataset.tab; });
      seg.style.setProperty('--seg-w', `calc((100% - 8px) / ${tabs.length})`);
      seg.style.setProperty('--seg-x', `${i * 100}%`);
      seg.dataset.active = tabs[i].dataset.tab;
      scope.querySelectorAll('[data-panel]:not([hidden]) .p-grid, [data-panel]:not([hidden]) .rail').forEach(r => { r.scrollLeft = 0; r.dispatchEvent(new Event('scroll')); });
      if (source) seg.dispatchEvent(new CustomEvent('della:tab', { bubbles: true, detail: { key: tabs[i].dataset.tab, source } }));
    };
    seg.dellaSet = set;
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => set(t.dataset.tab, 'tab'));
      t.addEventListener('keydown', e => {
        if (!['ArrowLeft', 'ArrowRight'].includes(e.key)) return;
        const n = tabs[(i + (e.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length];
        n.focus(); set(n.dataset.tab, 'tab_keyboard');
      });
    });
    set((tabs.find(t => t.getAttribute('aria-selected') === 'true') || tabs[0]).dataset.tab);
  });

  /* swipe rails (phones): dots under every .p-grid / .rail */
  document.querySelectorAll('.p-grid, .rail').forEach(rail => {
    const items = [...rail.children];
    if (items.length < 2) return;
    const dots = document.createElement('div');
    dots.className = 'rail-dots';
    dots.innerHTML = items.map((_, i) => `<button type="button" aria-label="Show item ${i + 1}"></button>`).join('');
    rail.after(dots);
    const btns = [...dots.children];
    const update = () => {
      const x = rail.scrollLeft, w = rail.scrollWidth - rail.clientWidth;
      const i = w <= 0 ? 0 : Math.round((x / w) * (items.length - 1));
      btns.forEach((b, j) => b.classList.toggle('is-active', j === i));
    };
    btns.forEach((b, i) => b.addEventListener('click', () => rail.scrollTo({ left: items[i].offsetLeft - parseFloat(getComputedStyle(rail).paddingLeft), behavior })));
    rail.addEventListener('scroll', () => requestAnimationFrame(update), { passive: true });
    update();
  });

  /* step accordions: ol.steps[data-media=id] > li[data-img] ; swaps images inside figure#id */
  document.querySelectorAll('ol.steps[data-media]').forEach(list => {
    const fig = document.getElementById(list.dataset.media);
    const imgs = fig ? [...fig.querySelectorAll('img')] : [];
    const cap = fig && fig.querySelector('figcaption');
    const items = [...list.children];
    const open = i => items.forEach((li, j) => {
      const on = j === i;
      li.classList.toggle('is-open', on);
      li.querySelector('.step-btn').setAttribute('aria-expanded', on);
      if (imgs[j]) imgs[j].classList.toggle('is-on', on);
      if (on && cap && li.dataset.caption) cap.innerHTML = `<b>${j + 1}</b>${li.dataset.caption}`;
    });
    items.forEach((li, i) => li.querySelector('.step-btn').addEventListener('click', () => {
      open(i);
      /* phones: the step above collapses (with its photo), so bring the opened step back into view */
      if (matchMedia('(max-width: 640px)').matches) setTimeout(() => {
        const y = li.getBoundingClientRect().top - topOffset() - 12;
        if (y < 0 || y > innerHeight * 0.5) scrollBy({ top: y, behavior });
      }, 480);
      window.dellaTrack('landing_step_open', { step: i + 1, section: list.dataset.media });
    }));
    open(0);
  });

  /* phones: floating buy bar after the hero, hidden over the final CTA */
  const bar = document.querySelector('.buybar');
  const hero = document.querySelector('.hero');
  const cta = document.querySelector('.cta');
  if (bar && hero) {
    let pastHero = false, atEnd = false;
    const sync = () => bar.classList.toggle('is-on', pastHero && !atEnd);
    new IntersectionObserver(([e]) => { pastHero = !e.isIntersecting && e.boundingClientRect.top < 0; sync(); }).observe(hero);
    if (cta) new IntersectionObserver(([e]) => { atEnd = e.isIntersecting || e.boundingClientRect.top < 0; sync(); }).observe(cta);
  }

  /* live price / stock on dellahome.com (static values stay if this fails) */
  if (/(^|\.)dellahome\.com$/.test(location.hostname)) {
    const fmt = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
    document.querySelectorAll('.p-card[data-product-handle]').forEach(async card => {
      try {
        const r = await fetch(`/products/${card.dataset.productHandle}.js`, { credentials: 'same-origin' });
        if (!r.ok) return;
        const p = await r.json();
        const live = p.variants.filter(v => v.available);
        const stock = card.querySelector('.p-stock');
        const full = card.querySelector('.p-full');
        if (full && p.title) full.textContent = p.title;
        if (!live.length) { if (stock) { stock.textContent = 'Currently unavailable'; stock.classList.add('is-out'); } return; }
        const prices = live.map(v => v.price), min = Math.min(...prices);
        const price = card.querySelector('.p-price');
        if (price) price.textContent = (min !== Math.max(...prices) ? 'From ' : '') + fmt.format(min / 100);
        if (stock) { stock.textContent = 'In stock'; stock.classList.remove('is-out'); }
      } catch (e) { /* keep static data */ }
    });
  }
})();
/* === DELLA SYSTEM v2 JS END === */
