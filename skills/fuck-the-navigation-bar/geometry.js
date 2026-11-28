/* Ghost Orbit: deterministic, dependency-free layout in CSS pixels. */
(function(root){
'use strict';
const rad = x=>x*Math.PI/180;
const distance=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y);
function overlaps(a,b,gap=0){return Math.abs(a.x-b.x)<(a.w+b.w)/2+gap-1e-7 && Math.abs(a.y-b.y)<(a.h+b.h)/2+gap-1e-7;}
function fits(p,b,margin){return p.x-p.w/2>=b.left+margin-1e-7 && p.x+p.w/2<=b.right-margin+1e-7 && p.y-p.h/2>=b.top+margin-1e-7 && p.y+p.h/2<=b.bottom-margin+1e-7;}
function solve({bounds:b,anchor:a,count:n,hand='auto',pointer='touch',reserved=[]}){
 if(!b||!a||![b.left,b.top,b.right,b.bottom,a.x,a.y].every(Number.isFinite)||b.right<=b.left||b.bottom<=b.top||!Number.isInteger(n)||n<1||n>7||!['auto','left','right'].includes(hand)||!['touch','mouse','pen','keyboard'].includes(pointer)||!Array.isArray(reserved)||reserved.some(r=>![r.x,r.y,r.w,r.h].every(Number.isFinite)||r.w<0||r.h<0)) throw new RangeError('Invalid layout input');
 const target=pointer==='mouse'||pointer==='keyboard'?44:48, gap=8, margin=8, neutral=pointer==='touch'?30:18;
 const fallback={mode:'list',target,gap,margin,neutral,items:[]};
 if(a.x<b.left||a.x>b.right||a.y<b.top||a.y>b.bottom) return fallback;
 // Preference blends inward direction with an approximate hand avoidance vector.
 const dx=(b.left+b.right)/2-a.x,dy=(b.top+b.bottom)/2-a.y;
 let vx=dx/Math.max(1,(b.right-b.left)/2),vy=dy/Math.max(1,(b.bottom-b.top)/2);
 if(pointer==='touch'){vx+=hand==='left'?.48:hand==='right'?-.48:0;vy-=.38;}
 const preferred=Math.hypot(vx,vy)<.001?-Math.PI/2:Math.atan2(vy,vx);
 // Approximate exclusion only for a declared hand; automatic makes no claim about grip.
 const occlusion=pointer==='touch'&&hand!=='auto'?{x:a.x+(hand==='left'?-37:37),y:a.y+47,w:58,h:76}:null;
 const angles=[0,15,-15,30,-30,45,-45,60,-60,90,-90,120,-120,150,-150,180];
 const spreads=pointer==='touch'?[150,180,120,210,240,90,75,60,360]:[360,180,150,240,120,90,75,60];
 const maxRadius=Math.min(260,Math.hypot(b.right-b.left,b.bottom-b.top));
 let best=null;
 for(const spread of spreads){
  const step=n===1?0:rad(spread)/(spread===360?n:n-1);
  // Square hit regions need conservative diagonal clearance; exact AABB checks follow.
  const lower=Math.max(neutral+target/Math.SQRT2, n===1?0:(target+gap)/(2*Math.sin(step/2)));
  for(let r=Math.ceil(lower/4)*4;r<=maxRadius;r+=4){
   for(const offset of angles){
    const base=preferred+rad(offset)-(n===1?0:step*(n-1)/2);
    const items=[];
    for(let i=0;i<n;i++){
     const t=base+i*step,p={id:i,x:a.x+r*Math.cos(t),y:a.y+r*Math.sin(t),w:target,h:target};
     if(!fits(p,b,margin)||distance(p,a)<neutral+target/Math.SQRT2-1e-7||reserved.some(q=>overlaps(p,q,gap))||items.some(q=>overlaps(p,q,gap))||(occlusion&&overlaps(p,occlusion,0)))break;
     items.push(p);
    }
    if(items.length!==n)continue;
    const score=r+Math.abs(offset)*.30+(pointer==='touch'?Math.abs(spread-150)*.13:Math.abs(spread-360)*.06);
    if(!best||score<best.score-1e-7)best={mode:'orbit',target,gap,margin,neutral,items,radius:r,spread,angle:base,score};
   }
  }
 }
 return best||fallback;
}
const api={solve,overlaps,fits,distance};if(typeof module!=='undefined')module.exports=api;else root.GhostGeometry=api;
})(typeof globalThis!=='undefined'?globalThis:this);
