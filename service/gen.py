import json,sys,html
tpl='''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} — {city}</title><meta name="description" content="{tagline}">
<style>body{{font:17px/1.6 system-ui,sans-serif;margin:0;color:#1b1b1b}}header{{background:{color};color:#fff;padding:56px 20px;text-align:center}}
h1{{margin:0 0 8px;font-size:2rem}}main{{max-width:720px;margin:0 auto;padding:20px}}.btn{{display:inline-block;background:#fff;color:{color};padding:14px 28px;border-radius:30px;text-decoration:none;font-weight:700;margin-top:16px}}
.row{{display:flex;justify-content:space-between;border-bottom:1px solid #eee;padding:10px 0}}.cta{{background:{color};color:#fff;text-align:center;padding:32px 20px;border-radius:12px;margin:28px 0}}</style></head><body>
<header><h1>{name}</h1><div>{tagline}</div><a class="btn" href="{link}">Записаться</a></header><main>
<h2>Услуги и цены</h2>{rows}<h2>Почему мы</h2><ul>{why}</ul>
<h2>Контакты</h2><p>{city}, {address}<br>{phone_html}{hours}</p>
<div class="cta"><b>Запишитесь сегодня</b><br><a class="btn" href="{link}">Написать</a></div></main></body></html>'''
c=json.load(open(sys.argv[1]));e=html.escape
c['rows']=''.join(f'<div class="row"><span>{e(a)}</span><b>{e(b)}</b></div>' for a,b in c['services'])
c['phone_html']=(f'Тел.: <a href="tel:{html.escape(c["phone"])}">{html.escape(c["phone"])}</a><br>' if c.get('phone') else '')
c['why']=''.join(f'<li>{e(x)}</li>' for x in c['why'])
for k in('name','city','tagline','address','hours'):c[k]=e(c[k])
open(sys.argv[2],'w').write(tpl.format(**c))
