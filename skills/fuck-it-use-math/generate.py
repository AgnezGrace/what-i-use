"""Deterministic, standard-library-only local icon generation."""
from math import sin, cos, pi, isfinite, hypot
from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parent
NS='http://www.w3.org/2000/svg'

def fmt(x):
    if not isfinite(x): raise ValueError('finite coordinates required')
    return f'{x:.4f}'.rstrip('0').rstrip('.') or '0'

def point(x,y): return f'{fmt(x)},{fmt(y)}'
def polar(r,a): return (12+r*cos(a),12+r*sin(a))
def gear(n=8, root=7.1, tip=9.2, hub=3.1):
    if type(n) is not int or not 5<=n<=12 or not all(isfinite(v) for v in (root,tip,hub)) or not (1<=hub and hub+2.5<=root<=tip-.8 and tip<=9.5):
        raise ValueError('invalid gear parameters')
    points=[point(*polar(tip if j in (1,2) else root,-pi/2+(i+(j-1.5)/4)*2*pi/n)) for i in range(n) for j in range(4)]
    return f'<polygon points="{" ".join(points)}"/><circle cx="12" cy="12" r="{fmt(hub)}"/>'
def arrow(a,b,L=4.5,W=4):
    x,y=a; X,Y=b; d=hypot(X-x,Y-y)
    if not all(isfinite(v) for v in (*a,*b,L,W,d)) or not (d>L>0 and W>0): raise ValueError('invalid arrow')
    u,v=(X-x)/d,(Y-y)/d
    p=(X-L*u-W*v,Y-L*v+W*u); q=(X-L*u+W*v,Y-L*v-W*u)
    return f'<path d="M{point(x,y)} L{point(X,Y)} M{point(*p)} L{point(X,Y)} L{point(*q)}"/>'
def path(d): return f'<path d="{d}"/>'
def circle(x,y,r): return f'<circle cx="{x}" cy="{y}" r="{r}"/>'
def rect(x,y,w,h,r=2): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>'
def svg(body,inline=False):
    extra=' aria-hidden="true" focusable="false"' if inline else ''
    return f'<svg xmlns="{NS}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"{extra}>{body}</svg>'
ICONS={
'home':path('M3 11 L12 3 L21 11 M5 10 V20 H10 V14 H14 V20 H19 V10'),
'back':arrow((20,12),(4,12)), 'forward':arrow((4,12),(20,12)),
'menu':path('M4 6 H20 M4 12 H20 M4 18 H20'),
'external':path('M13 4 H20 V11 M20 4 L11 13 M10 5 H5 Q4 5 4 6 V19 Q4 20 5 20 H18 Q19 20 19 19 V14'),
'search':circle(10,10,6)+path('M14.2426 14.2426 L20 20'),
'add':path('M12 4 V20 M4 12 H20'), 'close':path('M5 5 L19 19 M19 5 L5 19'),
'edit':path('M4 16 L16 4 Q17 3 18 4 L20 6 Q21 7 20 8 L8 20 H4 Z M14 6 L18 10'),
'save':path('M5 3 H17 L21 7 V19 Q21 21 19 21 H5 Q3 21 3 19 V5 Q3 3 5 3 Z M7 3 V9 H16 V3 M7 21 V14 H17 V21'),
'delete':path('M4 6 H20 M9 6 V3 H15 V6 M6 6 L7 20 Q7 21 8 21 H16 Q17 21 17 20 L18 6 M10 10 V17 M14 10 V17'),
'copy':rect(8,8,13,13)+path('M16 5 V4 Q16 3 15 3 H5 Q3 3 3 5 V15 Q3 16 5 16'),
'download':arrow((12,3),(12,15),4,4)+path('M4 15 V20 H20 V15'),
'upload':arrow((12,16),(12,4),4,4)+path('M4 15 V20 H20 V15'),
'document':path('M6 3 H14 L19 8 V20 Q19 21 18 21 H6 Q5 21 5 20 V4 Q5 3 6 3 Z M14 3 V8 H19 M8 12 H16 M8 16 H16'),
'folder':path('M3 7 Q3 5 5 5 H10 L12 8 H19 Q21 8 21 10 V18 Q21 20 19 20 H5 Q3 20 3 18 Z'),
'image':rect(3,4,18,16)+circle(8,9,1.5)+path('M4 18 L10 12 L14 16 L17 13 L20 16'),
'library':rect(3,4,5,16,1)+rect(9,4,5,16,1)+path('M16 5 L18 4.5 L21 19 L19 19.5 Z'),
'check':path('M4 12 L9 17 L20 6'),
'warning':path('M12 3 Q13 3 14 5 L21 18 Q22 20 19 20 H5 Q2 20 3 18 L10 5 Q11 3 12 3 Z M12 9 V13 M12 16 H12.01'),
'info':circle(12,12,9)+path('M12 11 V17 M12 7 H12.01'),
'lock':rect(5,10,14,11)+path('M8 10 V7 A4 4 0 0 1 16 7 V10 M12 14 V17'),
'eye':path('M3 12 Q12 -1 21 12 Q12 25 3 12 Z')+circle(12,12,3),
'settings':gear(),
'layers':path('M3 8 L12 3 L21 8 L12 13 Z M3 12 L12 17 L21 12 M3 16 L12 21 L21 16'),
'orbit':'<ellipse cx="12" cy="12" rx="9" ry="4" transform="rotate(40 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="4" transform="rotate(-40 12 12)"/><circle cx="12" cy="12" r="1.3" fill="currentColor" stroke="none"/>'
}

def generate():
    (ROOT/'icons').mkdir(exist_ok=True)
    for name,body in ICONS.items(): (ROOT/'icons'/f'{name}.svg').write_text(svg(body)+'\n')
    (ROOT/'registry.json').write_text(json.dumps({'viewBox':[0,0,24,24],'stroke':1.75,'icons':{n:{'label':n.replace('-',' ').capitalize(),'file':f'icons/{n}.svg','geometry':b} for n,b in ICONS.items()}},indent=2)+'\n')
    cards=''.join(f'<article data-icon="{n}"><div class="sizes">'+''.join(f'<span class="sample" style="--size:{s}px" data-size="{s}">{svg(b,True)}</span>' for s in (16,20,24,32,48))+f'</div><div class="name">{html.escape(n)}</div><button class="copy" type="button" aria-label="Copy {n} SVG" data-copy="{n}">Copy SVG</button></article>' for n,b in ICONS.items())
    data=json.dumps({n:svg(b) for n,b in ICONS.items()})
    template=(ROOT/'catalog-template.html').read_text()
    (ROOT/'catalog.html').write_text(template.replace('<!--CARDS-->',cards).replace('<!--DATA-->',data).replace('<!--SEARCH-->',svg(ICONS['search'],True)).replace('<!--SETTINGS-->',svg(ICONS['settings'],True)))
if __name__=='__main__': generate()
