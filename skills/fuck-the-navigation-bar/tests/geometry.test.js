const assert=require('node:assert/strict');const fs=require('node:fs');const {solve}=require('../geometry');
let total=0,orbit=0,list=0;const bySize={};
function check(input){const out=solve(input);total++;const k=`${input.bounds.right-input.bounds.left}x${input.bounds.bottom-input.bounds.top}`;bySize[k]??={orbit:0,list:0};bySize[k][out.mode]++;if(out.mode==='list'){list++;assert.equal(out.items.length,0);return;}orbit++;
 const {bounds:b,anchor:a,count:n,reserved=[],hand,pointer}=input;
 assert.equal(out.items.length,n);assert.equal(new Set(out.items.map(p=>p.id)).size,n);
 assert.ok(out.target>=44);for(const p of out.items){assert.ok([p.x,p.y].every(Number.isFinite));assert.ok(p.x-p.w/2>=b.left+8-1e-6&&p.x+p.w/2<=b.right-8+1e-6&&p.y-p.h/2>=b.top+8-1e-6&&p.y+p.h/2<=b.bottom-8+1e-6);assert.ok(Math.hypot(p.x-a.x,p.y-a.y)>=out.neutral+p.w/Math.SQRT2-1e-6);
 const avoid=[...reserved];if(pointer==='touch'&&['left','right'].includes(hand))avoid.push({x:a.x+(hand==='left'?-37:37),y:a.y+47,w:58,h:76,hand:true});
 for(const q of [...out.items.filter(q=>q.id!==p.id),...avoid]){const g=q.hand?0:8;assert.ok(Math.abs(p.x-q.x)>= (p.w+q.w)/2+g-1e-6||Math.abs(p.y-q.y)>=(p.h+q.h)/2+g-1e-6);}}
 assert.deepEqual(out,solve(input));}
for(const [w,h] of [[240,320],[320,568],[360,640],[390,844],[768,500],[1280,720],[844,390]])for(const x of [0,.08,.5,.92,1])for(const y of [0,.08,.5,.92,1])for(const n of [1,4,7])for(const [pointer,hand] of [['touch','auto'],['touch','left'],['touch','right'],['mouse','auto']])check({bounds:{left:5,top:13,right:w-5,bottom:h-19},anchor:{x:5+x*(w-10),y:13+y*(h-32)},count:n,pointer,hand});
for(let i=0;i<80;i++){const w=320+i%5*20,h=500+i%7*35;check({bounds:{left:0,top:0,right:w,bottom:h},anchor:{x:w*(i%11)/10,y:h*(i%9)/8},count:7,pointer:'touch',reserved:[{x:w/2,y:h/2,w:100,h:85}]});}
const tiny={bounds:{left:0,top:0,right:70,bottom:70},anchor:{x:35,y:35},count:7};check(tiny);assert.equal(solve(tiny).mode,'list');assert.throws(()=>solve({...tiny,count:8}),RangeError);assert.throws(()=>solve({...tiny,anchor:{x:NaN,y:0}}),RangeError);assert.throws(()=>solve({...tiny,reserved:[{x:0,y:0,w:-1,h:2}]}),RangeError);
const report={layoutCases:total,orbit,list,invalidInputs:3,forcedFallback:1,bySize};fs.writeFileSync(__dirname+'/geometry-results.json',JSON.stringify(report,null,2));console.log(report);
