"""Deterministic package and authored-fixture checks; no model calls."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
checks = []
def check(group, name, condition):
    checks.append({'group': group, 'name': name, 'passed': bool(condition)})

skill = (ROOT/'SKILL.md').read_text()
front = re.match(r'^---\nname: ([a-z0-9]+(?:-[a-z0-9]+)*)\ndescription: ([^\n]+)\n---\n', skill)
check('structure', 'frontmatter format', front is not None)
check('structure', 'name matches folder', bool(front and front[1] == ROOT.name and len(front[1]) <= 64))
check('structure', 'description length', bool(front and 0 < len(front[2]) <= 1024))
for path in ['AGENTS.md','agent.md','the-second-human.md','README.md','adapters/SOUL.md','tests/evaluation-rubric.md']:
    check('structure', path, (ROOT/path).is_file())
refs = re.findall(r'`(references/[^`]+\.md)`', skill)
check('structure', 'ten unique references', len(set(refs)) == len(refs) == 10)
for ref in refs:
    check('structure', 'reference: '+ref, (ROOT/ref).is_file())
check('structure', 'every reference is routed', set(refs) == {p.relative_to(ROOT).as_posix() for p in (ROOT/'references').rglob('*.md')})
check('structure', 'no external URLs in instruction documents', all(not re.search(r'https?://',p.read_text()) for p in ROOT.rglob('*.md')))
rows = json.loads((ROOT/'tests/scenarios.json').read_text())
check('structure','unique scenario IDs', len({r['id'] for r in rows}) == len(rows) == 20)
def evaluate(row, text):
    text = text.casefold()
    return all(x.casefold() in text for x in row['required']) and all(x.casefold() not in text for x in row['forbidden'])
for row in rows:
    check('fixtures', row['id']+': candidate matches lexical assertions', evaluate(row,row['candidate']))
    check('fixtures', row['id']+': deliberately weak baseline rejected', not evaluate(row,row['baseline']))
    check('mutation', row['id']+': injected forbidden phrase detected', not evaluate(row,row['candidate']+' '+row['forbidden'][0]))
summary = {g: {'passed':sum(c['passed'] for c in checks if c['group']==g),'total':sum(c['group']==g for c in checks)} for g in sorted({c['group'] for c in checks})}
result = {'method':'Deterministic package and authored-fixture lexical checks; no live model experiment', 'summary':summary,'checks':checks}
(ROOT/'tests/results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(summary,indent=2))
for c in checks:
    if not c['passed']: print('FAIL',c['name'])
raise SystemExit(0 if all(c['passed'] for c in checks) else 1)
