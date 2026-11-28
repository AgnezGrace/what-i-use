"""Reference gate and synthetic transaction checks; no external services."""
import json
import sqlite3
import tempfile
from pathlib import Path

VERIFIED, FAILED, UNVERIFIED, BLOCKED, NA = 'VERIFIED', 'FAILED', 'UNVERIFIED', 'BLOCKED', 'NOT APPLICABLE'
GATES = ('technical', 'operational', 'regulatory', 'third_party')

def gate(stage, records, authorization=False):
    if stage not in ('sandbox', 'pilot', 'public'):
        return 'HOLD'
    # Each record: status, evidence, actual stage, justified N/A.
    if set(records) != set(GATES):
        return 'HOLD'
    for status, evidence, evidence_stage, reason in records.values():
        if status == NA and reason and evidence and evidence_stage == stage:
            continue
        if status != VERIFIED or not evidence or evidence_stage != stage:
            return 'HOLD'
    if stage == 'sandbox':
        return 'SANDBOX READY'
    return 'AUTHORIZED STAGE' if authorization else 'READY FOR AUTHORIZATION'

def good(stage):
    return {k:(VERIFIED, 'synthetic evidence',stage,'') for k in GATES}

def replace(stage, key, value):
    d=good(stage); d[key]=value; return d

results=[]
def check(name, actual, expected):
    results.append({'name':name,'pass':actual==expected,'actual':actual,'expected':expected})

for stage in ('sandbox','pilot','public'):
    check(stage+' all gates',gate(stage,good(stage)), 'SANDBOX READY' if stage=='sandbox' else 'READY FOR AUTHORIZATION')
    for g in GATES:
        for status in (FAILED,UNVERIFIED,BLOCKED):
            check(f'{stage} {g} {status}',gate(stage,replace(stage,g,(status,'',stage,''))), 'HOLD')
check('public authorized',gate('public',good('public'),True),'AUTHORIZED STAGE')
check('pilot authorized',gate('pilot',good('pilot'),True),'AUTHORIZED STAGE')
check('owner consent cannot waive regulatory gate',gate('public',replace('public','regulatory',(BLOCKED,'','public','')),True),'HOLD')
check('sandbox evidence is not live evidence',gate('public',good('sandbox'),True),'HOLD')
check('pilot evidence is not public evidence',gate('public',good('pilot'),True),'HOLD')
check('missing gate',gate('public',{'technical':good('public')['technical']}),'HOLD')
check('missing evidence',gate('public',replace('public','operational',(VERIFIED,'','public',''))),'HOLD')
check('unjustified N/A',gate('public',replace('public','regulatory',(NA,'scope checked','public',''))),'HOLD')
check('evidenced N/A for illustrative nonregulated function',gate('public',replace('public','regulatory',(NA,'scope checked','public','no additional domain-specific authorization in this synthetic case'))),'READY FOR AUTHORIZATION')
check('invalid stage',gate('production?',good('public')),'HOLD')

# Small reference transaction fixture, deliberately NOT a production ledger.
# Each transfer is an atomic pair of entries; account totals derive from entries.
class Ledger:
    def __init__(self,p):
        self.db=sqlite3.connect(p)
        self.db.executescript('''CREATE TABLE IF NOT EXISTS transfers(id TEXT PRIMARY KEY, src TEXT, dst TEXT, amount INTEGER);
        CREATE TABLE IF NOT EXISTS entries(id INTEGER PRIMARY KEY, ref TEXT, account TEXT, amount INTEGER);
        ''')
    def balance(self,a):
        return self.db.execute('SELECT COALESCE(SUM(amount),0) FROM entries WHERE account=?',(a,)).fetchone()[0]
    def seed(self):
        with self.db:
            self.db.executemany('INSERT INTO entries(ref,account,amount) VALUES(?,?,?)',[('seed','alice',1000),('seed','opening',-1000)])
    def transfer(self, ident, src, dst, amount, actor, fault=False):
        if actor!=src or src==dst or type(amount) is not int or amount<=0:
            return 'DENIED'
        try:
            self.db.execute('BEGIN IMMEDIATE')
            old=self.db.execute('SELECT src,dst,amount FROM transfers WHERE id=?',(ident,)).fetchone()
            if old:
                self.db.rollback(); return 'REPLAY' if old==(src,dst,amount) else 'CONFLICT'
            if self.balance(src)<amount:
                self.db.rollback(); return 'INSUFFICIENT'
            self.db.execute('INSERT INTO transfers VALUES(?,?,?,?)',(ident,src,dst,amount))
            self.db.execute('INSERT INTO entries(ref,account,amount) VALUES(?,?,?)',(ident,src,-amount))
            if fault: raise RuntimeError('simulated interruption')
            self.db.execute('INSERT INTO entries(ref,account,amount) VALUES(?,?,?)',(ident,dst,amount))
            self.db.commit(); return 'SETTLED_LOCAL'
        except Exception:
            self.db.rollback(); raise
    def totals(self): return (self.balance('alice'),self.balance('bob'))
    def reconcile(self, external):
        local={r[0]:r[1] for r in self.db.execute('SELECT id,amount FROM transfers')}
        return sorted(k for k in set(local)|set(external) if local.get(k)!=external.get(k))

with tempfile.TemporaryDirectory() as td:
    p=Path(td)/'test.db'; l=Ledger(p); l.seed()
    check('transfer local transaction',l.transfer('t1','alice','bob',250,'alice'),'SETTLED_LOCAL')
    check('balances',l.totals(),(750,250))
    check('repeat request',l.transfer('t1','alice','bob',250,'alice'),'REPLAY')
    check('repeat preserves balance',l.totals(),(750,250))
    check('conflicting replay',l.transfer('t1','alice','bob',300,'alice'),'CONFLICT')
    check('unauthorized transfer',l.transfer('t2','alice','bob',50,'bob'),'DENIED')
    check('negative amount',l.transfer('t2','alice','bob',-5,'alice'),'DENIED')
    check('noninteger amount',l.transfer('t2','alice','bob',1.5,'alice'),'DENIED')
    check('overspend',l.transfer('t2','alice','bob',751,'alice'),'INSUFFICIENT')
    try: l.transfer('t2','alice','bob',50,'alice',True)
    except RuntimeError: check('fault injected',True,True)
    else: check('fault injected',False,True)
    check('rollback preserves balances',l.totals(),(750,250))
    check('rollback preserves transfer record',l.db.execute('SELECT COUNT(*) FROM transfers WHERE id=?',('t2',)).fetchone()[0],0)
    check('retry after rollback',l.transfer('t2','alice','bob',50,'alice'),'SETTLED_LOCAL')
    check('double entry invariant',l.db.execute('SELECT SUM(amount) FROM entries').fetchone()[0],0)
    check('reconcile exact',l.reconcile({'t1':250,'t2':50}),[])
    check('reconcile mismatch',l.reconcile({'t1':249,'external':10}),['external','t1','t2'])
    l.db.close(); l=Ledger(p)
    check('reopen balances',l.totals(),(700,300)); l.db.close()

out={'total':len(results),'passed':sum(r['pass'] for r in results),'checks':results}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
print(f"{out['passed']}/{out['total']} passed")
assert out['passed']==out['total']
