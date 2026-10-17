# -*- coding: utf-8 -*-
"""Convierte los JSON que devuelve la descarga de Drive (base64) en PDF dentro de
   students/eva_sc/source/ (gitignored). Uso: python3 mayores_bajar.py"""
import base64, glob, json, os, re, sys
TR = '/root/.claude/projects/-home-user-tclas/34206757-a690-5241-b1bf-4ebbff352a1e/tool-results'
DST = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'students', 'eva_sc', 'source')
os.makedirs(DST, exist_ok=True)
DESDE = int(sys.argv[1]) if len(sys.argv) > 1 else 0
for f in sorted(glob.glob(TR + '/mcp-Google_Drive-download_file_content-*.txt')):
    if int(re.findall(r'-(\d+)\.txt', f)[0]) < DESDE:
        continue
    try:
        d = json.load(open(f))
        c = d['content']
        if d.get('mimeType') != 'application/pdf':
            continue
        slug = re.sub(r'[^a-z0-9]+', '_', d['title'].lower()).strip('_')[:40]
        out = os.path.join(DST, slug + '.pdf')
        if not os.path.exists(out):
            open(out, 'wb').write(base64.b64decode(c))
            print('nuevo', slug)
    except Exception as e:
        pass
