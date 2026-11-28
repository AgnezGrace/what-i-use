from pathlib import Path
root=Path(__file__).resolve().parent
(root/'preview.html').write_text((root/'preview-template.html').read_text().replace('/* GEOMETRY */',(root/'geometry.js').read_text()))
