"""Reproducible checks for the restricted reference profile, not a general SVG sanitizer."""
from pathlib import Path
import sys, re, math, json, hashlib, subprocess, os, io
from xml.etree import ElementTree as ET
from collections import Counter
from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
import generate as g
results=[]
def check(group,label,ok):
    results.append(dict(group=group,check=label,passed=bool(ok)))
NS='{'+g.NS+'}'
ATTR={'svg':{'viewBox','fill','stroke','stroke-width','stroke-linecap','stroke-linejoin'},'path':{'d'},'circle':{'cx','cy','r','fill','stroke'},'rect':{'x','y','width','height','rx'},'polygon':{'points'},'ellipse':{'cx','cy','rx','ry','transform'}}
NUM=r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)'
def static_ok(s):
    if len(s)>8192 or re.search(r'<!|<\?',s): return False
    try: root=ET.fromstring(s)
    except ET.ParseError: return False
    if root.tag!=NS+'svg' or root.attrib!=dict(viewBox='0 0 24 24',fill='none',stroke='currentColor',**{'stroke-width':'1.75','stroke-linecap':'round','stroke-linejoin':'round'}): return False
    if not 1<=len(root)<=32: return False
    for e in root:
        if not e.tag.startswith(NS) or len(e) or (e.text and e.text.strip()) or (e.tail and e.tail.strip()): return False
        tag=e.tag[len(NS):]
        if tag not in ATTR or tag=='svg' or set(e.attrib)-ATTR[tag]: return False
        req={'path':{'d'},'circle':{'cx','cy','r'},'rect':{'x','y','width','height'},'polygon':{'points'},'ellipse':{'cx','cy','rx','ry'}}[tag]
        if not req<=set(e.attrib): return False
        for k,v in e.attrib.items():
            if k in ('fill','stroke'):
                if v not in ('currentColor','none'): return False
            elif k=='d':
                if not re.fullmatch(r'[MLHVQCAZmlhvqcaz0-9., +\-]+',v) or not v.startswith('M'): return False
            elif k=='points':
                if not re.fullmatch(r'[0-9., +\-]+',v): return False
                if len(re.findall(NUM,v))<6 or len(re.findall(NUM,v))%2: return False
            elif k=='transform':
                if not re.fullmatch(r'rotate\('+NUM+r' 12 12\)',v): return False
            elif not re.fullmatch(NUM,v): return False
            if k not in ('fill','stroke') and any(not math.isfinite(float(n)) or abs(float(n))>100 for n in re.findall(NUM,v)): return False
            if k in ('r','rx','ry','width','height') and float(v)<=0: return False
    return not (root.text and root.text.strip())
paths=sorted((ROOT/'icons').glob('*.svg')); reg=json.loads((ROOT/'registry.json').read_text())
check('static','registry matches assets',set(reg['icons'])=={p.stem for p in paths}==set(g.ICONS))
for p in paths:
    s=p.read_text(); check('static',p.stem+' profile',static_ok(s)); check('static',p.stem+' source matches',s==g.svg(reg['icons'][p.stem]['geometry'])+'\n')
check('static','unique SVG bodies',len({p.read_bytes() for p in paths})==len(paths))
base=g.svg(g.ICONS['search'])
for label,bad in {'script':base.replace('</svg>','<script>1</script></svg>'),'handler':base.replace('<circle ','<circle onclick="x()" '),'external':base.replace('</svg>','<image href="https://example.invalid/x"/></svg>'),'foreign':base.replace('</svg>','<foreignObject/></svg>'),'DTD':'<!DOCTYPE svg>'+base,'NaN':base.replace('r="6"','r="NaN"'),'paint':base.replace('stroke="currentColor"','stroke="url(https://example.invalid/x)"'),'namespace':base.replace(g.NS,'urn:other'),'oversize':base+' '*9000,'nested':base.replace('</svg>','<svg/></svg>')}.items(): check('negative',label,not static_ok(bad))
tracked=paths+[ROOT/'registry.json',ROOT/'catalog.html']; hashes=lambda:[hashlib.sha256(p.read_bytes()).hexdigest() for p in tracked]
before=hashes(); g.generate(); check('build','regeneration identical',before==hashes()); g.generate(); check('build','second regeneration identical',before==hashes())
for n in range(5,13):
    body=g.gear(n); root=ET.fromstring(g.svg(body)); pts=[tuple(map(float,p.split(','))) for p in root[0].attrib['points'].split()]
    check('math',f'gear {n} profile',static_ok(g.svg(body)))
    check('math',f'gear {n} vertex count',len(pts)==4*n)
    check('math',f'gear {n} root/tip radii',all(abs(math.hypot(x-12,y-12)-(9.2 if i%4 in (1,2) else 7.1))<.0001 for i,(x,y) in enumerate(pts)))
    check('math',f'gear {n} rotational center',all(abs(sum(p[k] for p in pts)/len(pts)-12)<.0001 for k in (0,1)))
for label,fn in [('too few teeth',lambda:g.gear(4)),('fractional teeth',lambda:g.gear(6.5)),('oversize gear',lambda:g.gear(8,7,12)),('hub clearance',lambda:g.gear(8,7,9,6)),('nonfinite radius',lambda:g.gear(8,float('nan'))),('zero arrow',lambda:g.arrow((1,1),(1,1))),('invalid head',lambda:g.arrow((1,1),(2,2),8))]:
    try: fn(); ok=False
    except ValueError: ok=True
    check('negative',label,ok)
# Test actual raster pixels from full-page screenshots. Compare each icon's area to its flat card surface.
def luminance(rgb):
    vals=[x/255 for x in rgb]; return sum(w*(v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4) for w,v in zip((.2126,.7152,.0722),vals))
def ratio(a,b):
    x,y=sorted((luminance(a),luminance(b))); return (y+.05)/(x+.05)
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path=os.environ.get('CHROMIUM','/usr/bin/chromium'),args=['--no-sandbox'])
    version=browser.version
    for width in (360,1280):
      for dpr in (1,2):
       for theme in ('light','dark'):
        tag=f'{width}-{dpr}x-{theme}'; ctx=browser.new_context(viewport={'width':width,'height':900},device_scale_factor=dpr,offline=True,color_scheme=theme)
        requests=[]; errors=[]; page=ctx.new_page(); page.on('request',lambda r:requests.append(r.url)); page.on('pageerror',lambda e:errors.append(str(e)))
        page.set_content((ROOT/'catalog.html').read_text()); page.evaluate("t=>document.documentElement.dataset.theme=t",theme)
        page.locator('#theme').evaluate('(e,t)=>{e.setAttribute("aria-pressed",String(t==="dark"));e.textContent=t==="dark"?"Light mode":"Dark mode"}',theme)
        boxes=page.locator('.sample').evaluate_all('es=>es.map(e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e.closest("article")),f=getComputedStyle(e.querySelector("svg"));return {name:e.closest("article").dataset.icon,size:+e.dataset.size,x:r.x,y:r.y,w:r.width,h:r.height,bg:s.backgroundColor,fg:f.color,stroke:f.stroke}})')
        check('browser',tag+' count',len(boxes)==len(paths)*5)
        check('browser',tag+' no horizontal overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
        imgbytes=page.screenshot(full_page=True,animations='disabled'); im=Image.open(io.BytesIO(imgbytes)).convert('RGB')
        if dpr==1: (ROOT/'tests'/f'preview-{width}-{theme}.png').write_bytes(imgbytes)
        fingerprints={}
        for b in boxes:
            rgb=lambda s:tuple(map(int,re.findall(r'\d+',s)[:3]))
            bg=rgb(b['bg']); fg=rgb(b['fg']); bounds=tuple(round(b[k]*dpr) for k in ('x','y'))+tuple(round((b[k]+b[s])*dpr) for k,s in [('x','w'),('y','h')]); crop=im.crop(bounds)
            diff=ImageChops.difference(crop,Image.new('RGB',crop.size,bg)).convert('L').point(lambda x:255 if x>18 else 0); bb=diff.getbbox(); key=f'{tag} {b["name"]} {b["size"]}px'
            check('render',key+' visible',bb is not None)
            check('render',key+' clear viewport edges',bb is not None and bb[0]>0 and bb[1]>0 and bb[2]<crop.width and bb[3]<crop.height)
            check('render',key+' currentColor and contrast',b['stroke']==b['fg'] and ratio(bg,fg)>=3)
            if b['size']==24: fingerprints[b['name']]=diff.tobytes()
        check('render',tag+' unique 24px silhouettes',len(set(fingerprints.values()))==len(paths))
        search=page.get_by_role('button',name='Focus icon search'); check('interaction',tag+' target >=44',search.bounding_box()['width']>=44 and search.bounding_box()['height']>=44)
        page.keyboard.press('Tab'); check('interaction',tag+' keyboard focus',search.evaluate('(e)=>e===document.activeElement&&getComputedStyle(e).outlineStyle!=="none"'))
        page.keyboard.press('Enter'); check('interaction',tag+' native keyboard activation',page.locator('#filter').evaluate('e=>e===document.activeElement'))
        page.locator('#filter').fill('search'); check('interaction',tag+' filter',page.locator('article:visible').count()==1)
        page.locator('#filter').fill(''); check('interaction',tag+' restore catalog',page.locator('article:visible').count()==len(paths))
        page.locator('#theme').click(); check('interaction',tag+' toggle state',page.locator('#theme').get_attribute('aria-pressed')==str(theme=='light').lower())
        for n in (5,12):
            page.locator('#teeth').fill(str(n)); check('interaction',tag+f' live gear {n}',page.locator('#gear polygon').get_attribute('points').count(' ')==4*n-1)
            actual=page.locator('#gear polygon').get_attribute('points'); expected=ET.fromstring(g.svg(g.gear(n)))[0].attrib['points']; check('math',tag+f' JS/Python parity {n}',all(abs(float(a)-float(b))<.00011 for a,b in zip(re.split('[ ,]',actual),re.split('[ ,]',expected))))
        check('browser',tag+' no external requests offline',not any(r.startswith(('http:','https:')) for r in requests))
        check('browser',tag+' no JS errors',not errors); ctx.close()
    browser.close()
counts={k:{'pass':sum(x['passed'] for x in results if x['group']==k),'total':sum(x['group']==k for x in results)} for k in sorted({x['group'] for x in results})}
summary={'browser':version,'counts':counts,'passed':sum(x['passed'] for x in results),'total':len(results),'failures':[x for x in results if not x['passed']],'checks':results}
(ROOT/'tests'/'results.json').write_text(json.dumps(summary,indent=2)+'\n'); print(json.dumps({k:v for k,v in summary.items() if k!='checks'},indent=2)); sys.exit(bool(summary['failures']))
