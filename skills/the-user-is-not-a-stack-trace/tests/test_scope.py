"""Controlled CSS scope experiment; no LLM invocation."""
import json, os, pathlib, shutil, tempfile
from playwright.sync_api import sync_playwright
ROOT=pathlib.Path(__file__).resolve().parent
PAGES=('home','settings','library','profile')
BASE='''body{font:16px system-ui;background:#f5f6f8;color:#17212a;padding:32px}
.button{border:1px solid transparent;border-radius:8px;background:#285b91;color:white;min-height:44px;padding:0 16px;box-shadow:none}
.button:focus-visible{outline:3px solid #162b49;outline-offset:3px}
.button.accent{box-shadow:0 3px 8px rgba(0,0,0,.3)}
'''
BAD='.button.standard:focus{box-shadow:0 0 0 4px rgb(203,52,70)}\n'
OVERRIDE='.button.standard:focus{box-shadow:none}\n'
# Shared defect affects Settings and Library; Profile has healthy override.
CASES={
 'local': (False,['settings'],[],['settings.css']),
 'shared': (True,[],[],['shared.css']),
 'independent_example': (False,['settings','profile'],['profile'],['settings.css']),
 'independent_global': (False,['settings','profile'],[],['settings.css','profile.css']),
 'explicit_local_boundary_hold': (True,[],['settings','library'],[]),
}
STRATEGIES=('local_override','global_reset','evidence_based')
def build(folder,c):
    shared,local,_,_=c; folder.mkdir()
    (folder/'shared.css').write_text(BASE+(BAD if shared else ''))
    for p in PAGES:
        (folder/f'{p}.css').write_text((BAD if p in local else '')+(OVERRIDE if p=='profile' and shared else ''))
        variant='accent' if p=='home' else 'standard'
        (folder/f'{p}.html').write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><title>{p}</title><link rel="stylesheet" href="shared.css"><link rel="stylesheet" href="{p}.css"><main><h1>{p.title()}</h1><button class="button {variant}">Open</button></main></html>')
def snapshot(folder): return {p.name:p.read_text() for p in folder.glob('*.css')}
def apply(folder,c,strategy):
    # Predetermined repairs, not sampled agent output.
    if strategy=='local_override':
        p=folder/'settings.css'; p.write_text(p.read_text()+OVERRIDE)
    elif strategy=='global_reset':
        p=folder/'shared.css'; p.write_text(p.read_text()+'.button,.button:focus{box-shadow:none!important}\n')
    else:
        for name in c[3]:
            p=folder/name; p.write_text(p.read_text().replace(BAD,''))
def observe(page,folder,p):
    html=(folder/f'{p}.html').read_text()
    for name in ('shared.css',f'{p}.css'):
        html=html.replace(f'<link rel="stylesheet" href="{name}">','<style>'+(folder/name).read_text()+'</style>')
    page.set_content(html)
    b=page.get_by_role('button',name='Open')
    idle=b.evaluate('(e)=>getComputedStyle(e).boxShadow')
    b.click()
    clicked=b.evaluate('(e)=>getComputedStyle(e).boxShadow')
    outline=b.evaluate('(e)=>getComputedStyle(e).outlineStyle')
    page.set_content(html); page.keyboard.press('Tab')
    key=b.evaluate('(e)=>({focused:document.activeElement===e, outline:getComputedStyle(e).outlineStyle, width:parseFloat(getComputedStyle(e).outlineWidth)})')
    return dict(idle=idle,clicked=clicked,pointer_outline=outline,keyboard=key,artifact='rgb(203, 52, 70)' in clicked)
def policy(kind,intent,safe=False):
    if kind=='unknown': return 'investigate'
    if kind=='intentional': return 'preserve'
    if kind=='preference': return 'shared_preference' if intent=='global' else 'local'
    if kind=='local': return 'local'
    if kind=='shared': return ('local_variant' if safe else 'ask') if intent=='only_local' else 'shared'
    if kind=='multiple': return 'all_confirmed' if intent=='global' else 'reported_and_disclose'
    raise ValueError(kind)
POLICY=[('local','example',False,'local'),('shared','example',False,'shared'),('shared','only_local',False,'ask'),('shared','only_local',True,'local_variant'),('multiple','example',False,'reported_and_disclose'),('multiple','global',False,'all_confirmed'),('intentional','example',False,'preserve'),('unknown','example',False,'investigate'),('preference','example',False,'local'),('preference','global',False,'shared_preference')]
def run():
    results={'policy':[], 'experiments':[], 'summary':{}}
    for kind,intent,safe,expected in POLICY:
        actual=policy(kind,intent,safe)
        results['policy'].append(dict(kind=kind,intent=intent,safe_local=safe,expected=expected,actual=actual,passed=actual==expected))
    with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
        root=pathlib.Path(tmp); browser=pw.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH','/usr/bin/chromium'),headless=True,args=['--no-sandbox'])
        for width,height in [(360,780),(1280,800)]:
            page=browser.new_page(viewport={'width':width,'height':height})
            for name,c in CASES.items():
                baseline=root/f'{name}-{width}'; build(baseline,c)
                initial={p:observe(page,baseline,p) for p in PAGES}
                assert {p for p,o in initial.items() if o['artifact']}==set(c[1])|({'settings','library'} if c[0] else set()),initial
                assert initial['home']['idle']!='none'
                for strategy in STRATEGIES:
                    folder=root/f'{name}-{width}-{strategy}'; shutil.copytree(baseline,folder)
                    before=snapshot(folder); apply(folder,c,strategy); after=snapshot(folder)
                    edited=sorted(p for p in before if before[p]!=after[p])
                    observed={p:observe(page,folder,p) for p in PAGES}; checks={}
                    for p,o in observed.items():
                        checks[f'{p}:expected click shadow']=o['clicked']==(initial[p]['clicked'] if p in c[2] or p=='home' else 'none')
                        checks[f'{p}:idle preserved']=o['idle']==initial[p]['idle']
                        checks[f'{p}:pointer outline preserved']=o['pointer_outline']==initial[p]['pointer_outline']
                        checks[f'{p}:keyboard focus visible']=o['keyboard']['focused'] and o['keyboard']['outline']=='solid' and o['keyboard']['width']>=2
                    checks['exact reference edit']=edited==sorted(c[3])
                    results['experiments'].append(dict(case=name,viewport=width,strategy=strategy,baseline=initial,observed=observed,modified=edited,checks=checks,passed=sum(checks.values()),total=len(checks)))
            page.close()
        browser.close()
    for strategy in STRATEGIES:
        runs=[r for r in results['experiments'] if r['strategy']==strategy]
        results['summary'][strategy]=dict(passed=sum(r['passed'] for r in runs),total=sum(r['total'] for r in runs),all_pass_runs=sum(r['passed']==r['total'] for r in runs),runs=len(runs))
    results['summary']['policy']=dict(passed=sum(r['passed'] for r in results['policy']),total=len(POLICY))
    (ROOT/'results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results['summary'],indent=2))
    assert results['summary']['evidence_based']['passed']==results['summary']['evidence_based']['total']
    assert all(r['passed'] for r in results['policy'])
if __name__=='__main__': run()
