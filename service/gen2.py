import json,sys,html,urllib.parse
e=html.escape
c=json.load(open(sys.argv[1]))
col=c['color'];maps='https://www.google.com/maps/search/?api=1&query='+urllib.parse.quote(c['name']+' '+c['address'])
def card(s):
    n,p,ic=(s+['',''])[:3] if len(s)<3 else s
    price=f'<span class="pr">{e(p)}</span>' if p and p!='уточняйте' else '<span class="pr ask">по запросу</span>'
    return f'<div class="card"><div class="ic">{ic or "✦"}</div><b>{e(n)}</b>{price}</div>'
cards=''.join(card(s) for s in c['services'])
facts=''.join(f'<div class="f"><small>{e(a)}</small><b>{e(b)}</b></div>' for a,b in c['facts'])
why=''.join(f'<li>{e(x)}</li>' for x in c['why'])
ph=f'<a class="btn ghost" href="tel:{e(c["phone"])}">Позвонить</a>' if c.get('phone') else ''
open(sys.argv[2],'w').write(f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(c['name'])} — {e(c['city'])}</title><meta name="description" content="{e(c['tagline'])}"><meta name="robots" content="noindex">
<style>:root{{--c:{col}}}*{{box-sizing:border-box}}body{{margin:0;font:17px/1.55 system-ui,-apple-system,Segoe UI,sans-serif;color:#17181a;background:#faf9f7}}
.hero{{background:radial-gradient(circle at 20% 10%,color-mix(in srgb,var(--c) 70%,#fff) ,var(--c) 55%,#000 160%);color:#fff;padding:72px 20px 64px;text-align:center}}
.hero h1{{font-size:clamp(2.2rem,7vw,3.6rem);margin:0 0 12px;letter-spacing:-.02em}}.hero p{{max-width:560px;margin:0 auto 24px;opacity:.92;font-size:1.1rem}}
.btn{{display:inline-block;padding:14px 28px;border-radius:40px;background:#fff;color:var(--c);font-weight:700;text-decoration:none;margin:4px}}.btn.ghost{{background:transparent;color:#fff;border:2px solid #fff8}}
main{{max-width:900px;margin:0 auto;padding:0 16px 40px}}.facts{{display:flex;flex-wrap:wrap;gap:12px;margin:-32px 0 32px}}.f{{flex:1 1 200px;background:#fff;border-radius:14px;padding:16px 18px;box-shadow:0 6px 24px #0001}}.f small{{display:block;color:#777}}.f b{{font-size:1.05rem}}
h2{{font-size:1.6rem;margin:36px 0 16px}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}}.card{{background:#fff;border-radius:14px;padding:18px;box-shadow:0 2px 10px #0001;display:flex;flex-direction:column;gap:6px}}
.ic{{font-size:1.8rem}}.pr{{color:var(--c);font-weight:700}}.pr.ask{{color:#8a8a8a;font-weight:500}}
ul{{padding-left:20px}}li{{margin:6px 0}}.map{{display:block;background:#fff;border-radius:14px;padding:18px;text-decoration:none;color:inherit;box-shadow:0 2px 10px #0001}}.map b{{color:var(--c)}}
.cta{{background:var(--c);color:#fff;border-radius:18px;text-align:center;padding:36px 16px;margin-top:36px}}.cta h2{{margin:0 0 14px}}footer{{text-align:center;color:#999;font-size:13px;padding:24px 16px 90px}}
.bar{{position:fixed;left:0;right:0;bottom:0;background:var(--c);padding:10px;text-align:center;display:none}}@media(max-width:700px){{.bar{{display:block}}}}.bar a{{margin:0}}
</style></head><body>
<section class="hero"><h1>{e(c['name'])}</h1><p>{e(c['tagline'])}</p><a class="btn" href="{c['link']}">Записаться</a>{ph}</section>
<main><div class="facts">{facts}</div>
<h2>Услуги</h2><div class="grid">{cards}</div>
<h2>Почему выбирают нас</h2><ul>{why}</ul>
<h2>Как нас найти</h2><a class="map" href="{maps}" target="_blank" rel="noopener"><b>📍 {e(c['address'])}</b><br>{e(c['hours'])}<br><small>Открыть на карте →</small></a>
<div class="cta"><h2>Запишитесь сегодня</h2><a class="btn" href="{c['link']}">Написать в Instagram</a></div></main>
<footer>Демо-макет сайта. Не является официальным сайтом заведения.</footer>
<div class="bar"><a class="btn" href="{c['link']}">Записаться</a></div></body></html>''')
