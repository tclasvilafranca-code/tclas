# -*- coding: utf-8 -*-
"""Constructor generico de UN dosier de cancion: las 6 paginas de una vez.

   Cada cancion pasa a ser un unico archivo de datos (`dilan_NN_*.py`) con un
   diccionario CANCION; aqui esta todo el fontanero. Asi el trabajo por
   cancion es medir la partitura, verificar a zoom y escribir el contenido,
   que es lo unico que no se puede automatizar.

   Estructura fija (decidida con el cliente):
       1 partitura · 2 ficha · 3 calentamiento · 4 agudeza · 5-6 al piano

   La regla dura del proyecto: el calentamiento DERIVA (transporta, invierte,
   amplia) y las hojas al piano CITAN compases literales con su numero. Nada
   puede estar en las dos. Se comprueba con audit_duplicados().
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))

import segno
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader

from portada import W, H
from ficha_info import build_ficha
from hoja_calentamiento import build_calentamiento
from hoja_lectura import build_lectura
from hoja_piano import build_piano
from audit_suite import run_full_audit, audit_text_bounds, audit_duplicados

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')


def _hojas(cfg, qr_png):
    """Las cinco hojas del dosier, ya con el kicker y la numeracion puestos."""
    kicker = '%s · canción %d · %s' % (cfg['alumno'], cfg['num'], cfg['titulo_corto'])
    nivel = '%s · canción %d · nivel %s' % (cfg['alumno'], cfg['num'], cfg['nivel'])

    ficha = dict(cfg['ficha'])
    ficha.update(kicker=nivel, page_num=4, time_sig=cfg['time_sig'])
    ficha['qr'] = dict(ficha['qr']); ficha['qr']['png'] = qr_png

    cal = dict(cfg['calentamiento'])
    cal.update(kicker=kicker, page_num=5, time_sig=cfg['time_sig'],
               key_sig=cfg.get('key_sig'), gap=cal.get('gap', 7.0))

    lec = dict(cfg['agudeza'])
    lec.update(kicker=kicker, page_num=6, time_sig=cfg['time_sig'],
               key_sig=cfg.get('key_sig'))

    p1 = dict(cfg['piano1'])
    p1.update(kicker=kicker, page_num=7, time_sig=cfg['time_sig'],
              key_sig=cfg.get('key_sig'), gap=p1.get('gap', 7.0),
              esquina='Al piano · desmontar la pieza',
              titulo='Al piano · por partes')

    p2 = dict(cfg['piano2'])
    p2.update(kicker=kicker, page_num=8, time_sig=cfg['time_sig'],
              key_sig=cfg.get('key_sig'), gap=p2.get('gap', 7.0),
              esquina='Al piano · montar la pieza',
              titulo='Al piano · montarla')

    return [('ficha', lambda c: build_ficha(c, ficha)),
            ('calentamiento', lambda c: build_calentamiento(c, cal)),
            ('agudeza', lambda c: build_lectura(c, lec)),
            ('piano 1', lambda c: build_piano(c, p1)),
            ('piano 2', lambda c: build_piano(c, p2))]


def construir(cfg, verificar=True):
    """Genera el PDF de 6 paginas y devuelve su ruta."""
    os.makedirs(OUT_DIR, exist_ok=True)
    qr = os.path.join(OUT_DIR, '_qr_%s.png' % cfg['slug'])
    segno.make(cfg['yt'], error='m').save(qr, scale=10, border=2,
                                          dark='#1A2332', light='#F3F1EA')
    hojas = _hojas(cfg, qr)

    tmp = os.path.join(HERE, '_tmp_%s.pdf' % cfg['slug'])
    c = canvas.Canvas(tmp, pagesize=(W, H))
    for _, fn in hojas:
        fn(c)
    c.save()

    wr = PdfWriter()
    for p in PdfReader(cfg['partitura']).pages:
        wr.add_page(p)
    for p in PdfReader(tmp).pages:
        wr.add_page(p)
    out = os.path.join(OUT_DIR, '%s_%02d_%s_CUADERNO.pdf'
                       % (cfg['alumno'], cfg['num'], cfg['slug']))
    with open(out, 'wb') as f:
        wr.write(f)
    os.remove(tmp)
    os.remove(qr)

    if verificar:
        auditar(cfg)
    return out


def auditar(cfg):
    """Las cuatro comprobaciones obligatorias. Imprime lo que falle."""
    qr = os.path.join(OUT_DIR, '_qr_a_%s.png' % cfg['slug'])
    segno.make(cfg['yt'], error='m').save(qr, scale=10, border=2,
                                          dark='#1A2332', light='#F3F1EA')
    hojas = _hojas(cfg, qr)
    fallos = []
    for nombre, fn in hojas:
        ov = audit_text_bounds(fn, 595.276, 841.89, 549.28)
        if ov:
            fallos.append('%s: texto fuera del margen -> %s' % (nombre, ov[:2]))
        calls, probs = _music(fn)
        for p in probs:
            if 'not a whole number of bars' in p:
                fallos.append('%s: %s' % (nombre, p))
        y = _altura(fn)
        if y is not None and y < 44:
            fallos.append('%s: la pagina se pasa por abajo (y=%.1f)' % (nombre, y))
    ident, parc = audit_duplicados(hojas)
    if ident:
        fallos.append('material IDENTICO entre hojas: %s' % (ident[:2],))
    if parc:
        fallos.append('solape >=8 notas entre hojas: %s' % (parc[:3],))
    os.remove(qr)
    print(('  %s: OK' % cfg['slug']) if not fallos else
          ('  %s: %d FALLOS\n    %s' % (cfg['slug'], len(fallos),
                                        '\n    '.join(fallos))))
    return fallos


def _music(fn):
    from audit_suite import audit_music
    return audit_music(fn)


def _altura(fn):
    """La y en la que acaba la hoja: por debajo de ~44 pisa el pie de pagina.
       build_ficha no devuelve y (su layout es en dos columnas), asi que ahi
       la comprobacion la hace el chequeo de pixeles."""
    c = canvas.Canvas(os.devnull, pagesize=(W, H))
    return fn(c)
