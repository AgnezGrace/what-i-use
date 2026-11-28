import os
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
ROOT=Path(__file__).resolve().parents[1]
results=[]
def check(name,value):
    assert value,name
    results.append(name)
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH','/usr/bin/chromium'),args=['--no-sandbox'])
    for w,h,touch in [(360,740,True),(1280,800,False),(320,568,True)]:
        ctx=browser.new_context(viewport={'width':w,'height':h},has_touch=touch,is_mobile=touch, reduced_motion='reduce' if w==320 else 'no-preference',offline=True)
        page=ctx.new_page();requests=[];page.on('request',lambda r:requests.append(r.url));page.set_content((ROOT/'preview.html').read_text());stage=page.locator('#stage');bb=stage.bounding_box();tag=str(w)
        snap=lambda:page.evaluate('lab.snapshot()')
        def pos(x,y):return (bb['x']+1+x*(bb['width']-2),bb['y']+1+y*(bb['height']-2))
        def touch_event(kind,x,y):
            session.send('Input.dispatchTouchEvent',{'type':kind,'touchPoints':[] if kind in ('touchEnd','touchCancel') else [{'x':x,'y':y}]})
        session=ctx.new_cdp_session(page)
        def start(x,y):
            if touch:touch_event('touchStart',x,y)
            else:page.mouse.move(x,y);page.mouse.down()
        def move(x,y):
            if touch:touch_event('touchMove',x,y)
            else:page.mouse.move(x,y)
        def end():
            if touch:touch_event('touchEnd',0,0)
            else:page.mouse.up()
        def esc():page.keyboard.press('Escape')
        check(tag+' initial hidden',page.locator('#menu').is_hidden())
        x,y=pos(.5,.6);start(x,y);end();check(tag+' short tap',snap()['state']=='idle' and snap()['commits']==0)
        start(x,y);move(x+30,y);page.wait_for_timeout(360);end();check(tag+' early move',snap()['state']=='idle' and snap()['commits']==0)
        start(x,y);page.wait_for_timeout(400);check(tag+' hold',snap()['state']=='held');end();page.wait_for_timeout(150);check(tag+' neutral release',snap()['state']=='tap')
        check(tag+' all actions',page.locator('#menu button').count()==7)
        page.locator('#menu button').first.click();check(tag+' tap select',snap()['commits']==1 and snap()['state']=='idle')
        page.locator('#count').select_option('4');start(x,y);page.wait_for_timeout(380);s=snap();check(tag+' four orbit',s['mode']=='orbit')
        q=s['layout']['items'][1];move(bb['x']+1+q['x'],bb['y']+1+q['y']);end();check(tag+' drag selection',snap()['commits']==2 and snap()['state']=='idle')
        start(x,y);page.wait_for_timeout(380);esc();end();check(tag+' escape cancels',snap()['commits']==2 and snap()['state']=='idle')
        if touch:
            start(x,y);page.wait_for_timeout(380);touch_event('touchCancel',0,0);check(tag+' real touchcancel',snap()['state']=='idle' and snap()['commits']==2)
        start(x,y);page.wait_for_timeout(380);s=snap();
        if s['mode']=='orbit':
            # Move out of the neutral zone to an empty part of the canvas.
            candidates=[pos(.06,.06),pos(.94,.06),pos(.06,.94),pos(.94,.94)]
            def free(v):
                lx,ly=v[0]-bb['x']-1,v[1]-bb['y']-1
                return all(abs(lx-q['x'])>q['w']/2+1 or abs(ly-q['y'])>q['h']/2+1 for q in s['layout']['items']) and ((lx-s['anchor']['x'])**2+(ly-s['anchor']['y'])**2)**.5>s['layout']['neutral']
            v=next(v for v in candidates if free(v));move(*v);end();check(tag+' release outside cancels',snap()['state']=='idle' and snap()['commits']==2)
        else:esc();end()
        page.locator('#count').select_option('7');page.locator('#trigger').focus();page.keyboard.press('Enter');check(tag+' keyboard list',snap()['mode']=='list' and page.locator('#menu button').count()==7)
        check(tag+' focus first',page.evaluate('document.activeElement.dataset.id')=='home');page.keyboard.press('Tab');check(tag+' tab',page.evaluate('document.activeElement.dataset.id')=='search');page.keyboard.press('Enter');check(tag+' keyboard select',snap()['commits']==3 and page.evaluate('document.activeElement.id')=='trigger')
        page.locator('#trigger').click();esc();check(tag+' restore',page.evaluate('document.activeElement.id')=='trigger')
        page.locator('#trigger').click();page.locator('#protected').click();page.locator('#protected').fill('native input');check(tag+' outside and native field',snap()['state']=='idle' and page.locator('#protected').input_value()=='native input')
        for hand in ['auto','left','right']:
            page.locator('#hand').select_option(hand)
            for ax,ay in [(0,0),(.03,.5),(.5,.5),(.97,.97),(1,1)]:
                page.evaluate('([x,y,p])=>lab.openAt(x,y,p)',[(bb['width']-2)*ax,(bb['height']-2)*ay,'touch' if touch else 'mouse']);s=snap();buttons=page.locator('#menu button');check(tag+f' {hand} {ax} {ay} count',buttons.count()==7)
                if s['mode']=='orbit':
                    rects=buttons.evaluate_all('(els)=>els.map(e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,h:r.height}})');ok=True
                    for i,a in enumerate(rects):
                        ok &= a['x']>=bb['x']+8 and a['y']>=bb['y']+8 and a['x']+a['w']<=bb['x']+bb['width']-8 and a['y']+a['h']<=bb['y']+bb['height']-8 and a['w']>=44 and a['h']>=44
                        for b in rects[i+1:]:ok &= a['x']+a['w']+7.9<=b['x'] or b['x']+b['w']+7.9<=a['x'] or a['y']+a['h']+7.9<=b['y'] or b['y']+b['h']+7.9<=a['y']
                    check(tag+f' {hand} {ax} {ay} DOM containment and gap',ok)
                else:
                    buttons.last.scroll_into_view_if_needed();check(tag+f' {hand} {ax} {ay} fallback last visible',buttons.last.is_visible() and buttons.last.bounding_box()['height']>=48)
                esc()
        page.locator('#hand').select_option('auto');page.evaluate('([x,y,p])=>lab.openAt(x,y,p)',[(bb['width']-2)*.5,(bb['height']-2)*.68,'touch' if touch else 'mouse']);page.screenshot(path=str(ROOT/'tests'/f'preview-{w}.png'),animations='disabled');esc()
        page.locator('#trigger').click();page.screenshot(path=str(ROOT/'tests'/f'fallback-{w}.png'),animations='disabled');page.set_viewport_size({'width':w,'height':h-20});page.wait_for_timeout(100);check(tag+' resize cancels',snap()['state']=='idle');check(tag+' offline no requests',not requests)
        if w==320:
            page.locator('#trigger').click();check(tag+' reduced motion',page.locator('#menu button').first.evaluate('(e)=>getComputedStyle(e).animationName')=='none');
            panel=page.locator('.list');pr=panel.bounding_box();panel.evaluate('(e)=>e.scrollTop=0');
            touch_event('touchStart',pr['x']+pr['width']/2,pr['y']+pr['height']-25);
            for i in range(1,9):
                touch_event('touchMove',pr['x']+pr['width']/2,pr['y']+pr['height']-25-i*20);page.wait_for_timeout(20)
            touch_event('touchEnd',0,0);page.wait_for_timeout(300);check(tag+' fallback native touch scroll',panel.evaluate('(e)=>e.scrollTop')>0 and snap()['state']=='tap');esc()
        if not touch:
            page.mouse.click(x,y,button='right');check(tag+' mouse context',snap()['state']=='tap');esc()
        ctx.close()
    browser.close()
(ROOT/'tests'/'browser-results.json').write_text(json.dumps({'passed':len(results),'checks':results},indent=2));print('Browser passed',len(results))
