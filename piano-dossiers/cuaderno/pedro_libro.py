# -*- coding: utf-8 -*-
"""Dosier de Pedro (adulto, nivel 1-4): índice de menos a más dificultad + una ficha por partitura
   (y la partitura original a continuación, salvo las que llevan «NO» en el nombre: de esas solo la ficha).

   python3 pedro_libro.py            -> entrega/DOSIER_PEDRO_completo.pdf
   BN=1 python3 pedro_libro.py       -> entrega/DOSIER_PEDRO_completo_BN.pdf

   Los datos de cada pieza (medidos sobre el PDF) están en pedro_datos.py. Las partituras NO se versionan:
   students/pedro/source/ (ver .gitignore). Norma de las piezas a cuatro manos: la partitura empieza en
   página PAR (páginas enfrentadas) y, si hace falta, se intercala una hoja de papel pautado."""
import io
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.setdefault('ALUMNA', 'alba')          # tema sobrio de adulto (sin Mussol Misol), texto fijo en castellano
os.environ.setdefault('IDIOMA', 'es')
from mayores_motor import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, INK, MUTED, PANEL, OCRE, AZUL, GRIS, COLORES_BLOQUE,
                           marco, titulo_pag, FICHA, build_ficha, build_pauta, _qr, _wrap)
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter, Transformation
import pymupdf
import pedro_datos as PD

BN = os.environ.get('BN') == '1'
OFF = int(os.environ.get('PEDRO_OFFSET', '0'))        # paginas que van delante (p. ej. el cuaderno de teoria); debe ser PAR para que los duos sigan enfrentados
SRC = os.path.join(HERE, '..', 'students', 'pedro', 'source')
SRC_BN = os.path.join(HERE, '..', 'students', 'pedro', 'source_bn')
OUT = os.path.join(HERE, 'entrega')
KICK = 'DOSIER DE PEDRO · REPERTORIO'
TEMPOS_IT = ('Largo', 'Adagio', 'Allegro', 'Allegretto', 'Andantino', 'Moderato')


# ------------------------------------------------------------------ dificultad (criterio declarado y comprobable)
def puntuar(s):
    """Puntos de dificultad a partir de datos MEDIDOS (véase pedro_datos.py)."""
    c = sum(s['segs'])
    lon = 0 if c <= 16 else 1 if c <= 24 else 2 if c <= 34 else 3 if c <= 48 else 4
    comp = {(4, 4): 0, (2, 4): 0, (3, 4): 0.5, (2, 2): 1.0, (12, 8): 2.0}.get(s['ts'], 1.0)
    lh = {'long': 0, 'alterna': 0.5, 'acords': 1.0, 'dues': 1.5}[s['lh']]
    return (lon + s['fig'] + comp + lh + 0.75 * s['alt'] + s['shift'] + 0.5 * s['expr']
            + (1.0 if s['duo'] else 0) + (0.5 if s['ana'] else 0) + (0.5 if s.get('cifrado') else 0))


def ordenar():
    llista = [dict(v, pts=puntuar(v), compases=sum(v['segs'])) for v in PD.SCORES.values()]
    llista.sort(key=lambda v: (v['pts'], v['compases'], v['titulo']))
    for i, v in enumerate(llista):
        v['num'] = i + 1
        v['nivel'] = 1 + min(4, int(5 * i / len(llista)))
    return llista


# ------------------------------------------------------------------ ficha
class _Lienzo(canvas.Canvas):
    """Retiene el showPage de build_ficha para poder añadir, con la y final que devuelve, el cuadro de notas de clase."""
    retener = False

    def showPage(self):
        if not self.retener:
            super().showPage()


def notas_clase(c, y):
    """Cuadro para escribir a mano (digitación, pasajes difíciles, fecha de la clase): llena lo que queda de hoja."""
    top = y - 18
    bot = 46
    if top - bot < 60:
        return
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, top, 'NOTAS DE CLASE')
    c.setFont('DejaVuSans', 7.2)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 82, top, 'digitación · pasajes a repasar · qué trabajamos la próxima semana')
    c.setStrokeColor(GRIS)
    c.setLineWidth(0.8)
    yy = top - 20
    while yy > bot + 6:
        c.line(MARGIN, yy, MARGIN + CONTENT_W, yy)
        yy -= 20


def fitxa(v, num_pag, ruta):
    c = _Lienzo(ruta, pagesize=(W, H))
    c.retener = True
    tempo = v['tempo']
    if tempo.startswith('No indicado («'):
        txt = tempo.split('«')[1].rstrip('»)')
        datos_t = ('Carácter', txt)
    elif tempo == 'No indicado':
        datos_t = ('Tempo', 'No indicado')
    elif tempo.startswith('♩'):
        datos_t = ('Tempo', tempo)
    else:
        datos_t = ('Tempo' if tempo in TEMPOS_IT else 'Carácter', tempo)
    ton = v['ton']
    ton_l = 'Tonalidad' if ('mayor' in ton or 'menor' in ton) else 'Armadura'
    ton = (ton.replace('Sin alteraciones en la armadura', 'Sin armadura').replace('Sin alteraciones', 'Sin armadura')
           .replace(' (acordes impresos)', '').replace('Armadura de tres sostenidos (Fa♯ Do♯ Sol♯)', '3 sostenidos')
           .replace('Armadura de un sostenido (Sol mayor)', 'Sol mayor (1 ♯)').replace(' (un sostenido)', ' (1 ♯)'))
    total = v['compases']
    ncomp = '%d%s' % (total, ' + anacrusa' if v['ana'] else '')
    datos = [(ton_l, ton), ('Compás', v['compas']), datos_t, ('Figura corta', PD.FIGS[v['fig']].capitalize()), ('Compases', ncomp)]
    # mapa: secciones formales si la forma es clara; si no, un tramo por sistema de la partitura (es lo que se ha medido)
    segs, forma = v['segs'], v.get('forma')
    g = 1 if (forma or len(segs) <= 6) else 2
    grup = [sum(segs[i:i + g]) for i in range(0, len(segs), g)]
    secs, a = [], 1
    for i, n in enumerate(grup):
        b = a + n - 1
        etq = forma[i] if forma else 'T%d' % (i + 1)
        secs.append((etq, a, b, 'cc. %d-%d' % (a, b), COLORES_BLOQUE[i % len(COLORES_BLOQUE)]))
        a = b + 1
    ideas_pie = v['ideas_pie']
    if not forma:
        ideas_pie += ' · Mapa: %s de tu partitura.' % ('cada tramo es un sistema' if g == 1 else 'cada tramo son dos sistemas')
    sp = FICHA(datos=datos, secciones=secs, total=total, ideas=v['ideas'], especial=v['especial'], reto=v['reto'],
               truco=v['truco'], sabias=v['sabias'], qr_texto='Escúchala con la partitura delante.', ts=v['ts'],
               ideas_titulo='La pieza en cuatro ideas', ideas_pie=ideas_pie,
               cuenta_titulo='Cómo se cuenta un compás de %d/%d' % v['ts'],
               cuenta_pie='Un compás de %d/%d en corcheas. Aquí solo el ritmo; las notas, en tu partitura.' % v['ts'])
    qr = os.path.join(OUT, '_qr_pedro_%s.png' % v['slug'])
    _qr('https://www.youtube.com/results?search_query=' + v['yt'], qr)
    cfg = dict(sp)
    cfg.update(kicker='Pedro · pieza %d · %s' % (v['num'], v['titulo']), page_num=num_pag, time_sig=v['ts'],
               qr=dict(sp['qr'], png=qr), titulo=v['titulo'], autor=v['autor'], misol_buho=False)
    y = build_ficha(c, cfg)
    c.retener = False
    notas_clase(c, y)
    c.showPage()
    c.save()
    os.remove(qr)
    return ruta


def pauta(num_pag, ruta, titol):
    c = canvas.Canvas(ruta, pagesize=(W, H))
    build_pauta(c, dict(kicker='Pedro · ' + titol, page_num=num_pag, titulo_pauta='Para escribir', misol=None,
                        pie_pauta='espacio para apuntar pasos, digitación o los compases que os cuestan · '
                                  'la partitura del dúo se abre en la página siguiente'))
    c.save()
    return ruta


# ------------------------------------------------------------------ páginas de partitura
def pagines_partitura(v, num0, tmpdir):
    """Devuelve [(ruta_pdf_de_una_pagina, num)]: cada página de la partitura original, escalada a A4 y con el pie T-Clas."""
    src = os.path.join(SRC_BN if BN and os.path.exists(os.path.join(SRC_BN, v['slug'] + '.pdf')) else SRC, v['slug'] + '.pdf')
    rd = PdfReader(src)
    out = []
    for k, pg in enumerate(rd.pages):
        n = num0 + k
        ruta = os.path.join(tmpdir, '_s_%s_%d.pdf' % (v['slug'], k))
        # base A4 blanca con el pie
        buf = canvas.Canvas(ruta, pagesize=(W, H))
        buf.setFillColor(NAVY_SOFT)
        buf.setFont('DejaVuSans', 7.4)
        buf.drawCentredString(W / 2, 18, 'El Cuaderno del Pianista  ·  T-Clas  ·  %s' % v['titulo'])
        buf.drawRightString(W - MARGIN, 18, str(n))
        buf.save()
        base = PdfReader(ruta).pages[0]
        pw, ph = float(pg.mediabox.width), float(pg.mediabox.height)
        rot = pg.get('/Rotate', 0) or 0
        if rot in (90, 270):
            pw, ph = ph, pw
        s = min((W - 28) / pw, (H - 50) / ph)
        tx = (W - s * pw) / 2.0
        ty = H - 14 - s * ph
        base.merge_transformed_page(pg, Transformation().scale(s).translate(tx - float(pg.mediabox.left) * s,
                                                                             ty - float(pg.mediabox.bottom) * s))
        w = PdfWriter()
        w.add_page(base)
        with open(ruta, 'wb') as fh:
            w.write(fh)
        out.append((ruta, n))
    return out


# ------------------------------------------------------------------ índice
def pag_index(c, llista, inicio):
    marco(c, KICK, 'El repertorio de menos a más', 1 + OFF)
    y = titulo_pag(c, 'El repertorio, de menos a más',
                   '%d piezas ordenadas por dificultad. Las marcadas «solo ficha» tienen la partitura impresa aparte: '
                   'la ficha es la guía para trabajarla.' % len(llista))
    y -= 8
    xs = [MARGIN, MARGIN + 26, MARGIN + 270, MARGIN + 392, MARGIN + 462]
    for x, t in zip(xs, ['Nº', 'PIEZA', 'QUÉ INCLUYE', 'NIVEL', 'PÁG.']):
        c.setFont('DejaVuSans-Bold', 7)
        c.setFillColor(MUTED)
        c.drawString(x, y, t)
    y -= 6
    h = 21
    for v in llista:
        c.setFillColor(PANEL)
        c.roundRect(MARGIN, y - h, CONTENT_W, h, 3, fill=1, stroke=0)
        col = COLORES_BLOQUE[(v['num'] - 1) % len(COLORES_BLOQUE)]
        c.setFillColor(col)
        c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 10)
        c.setFillColor(NAVY)
        c.drawString(xs[0] + 7, y - 14.5, str(v['num']))
        c.setFont('DejaVuSerif-Bold', 8.8)
        c.drawString(xs[1], y - 9.5, v['titulo'][:46])
        c.setFont('DejaVuSans', 6.4)
        c.setFillColor(MUTED)
        c.drawString(xs[1], y - 18, v['autor'][:70])
        c.setFont('DejaVuSans', 7.2)
        c.setFillColor(OCRE if v['no'] else INK)
        c.drawString(xs[2], y - (10 if v['duo'] else 13.5), 'Solo ficha' if v['no'] else 'Ficha + partitura')
        if v['duo']:
            c.setFont('DejaVuSans', 6.2)
            c.setFillColor(MUTED)
            c.drawString(xs[2], y - 18, 'pieza a cuatro manos')
        for k in range(5):
            c.setFillColor(NAVY if k < v['nivel'] else GRIS)
            c.circle(xs[3] + 4 + k * 9.6, y - 12.5, 3.1, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 8.6)
        c.setFillColor(NAVY)
        c.drawString(xs[4], y - 13.5, str(inicio[v['slug']]))
        y -= h + 2.0
    y -= 10
    y = _wrap(c, 'Criterio: longitud (compases), figura más corta, compás, actividad de la mano izquierda, alteraciones, cambios de '
                 'posición, matices e indicaciones, cuatro manos, anacrusa y cifrados. Todo medido sobre tu edición. '
                 'Las curiosidades del «¿Sabías que…?» son culturales y no están verificadas sobre la partitura.',
              MARGIN, y, 'DejaVuSans', 7.2, CONTENT_W, 9.6, MUTED)
    c.showPage()
    return y


# ------------------------------------------------------------------ montaje
def muntar(destino, llista):
    os.makedirs(OUT, exist_ok=True)
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        # paso 1: calcular las páginas de cada pieza (para hacer el índice con números)
        inicio, pag, plan = {}, 2 + OFF, []
        for v in llista:
            inicio[v['slug']] = pag
            plan.append(('fitxa', v, pag))
            pag += 1
            if not v['no']:
                npag = len(PdfReader(os.path.join(SRC, v['slug'] + '.pdf')).pages)
                if v['duo'] and pag % 2 == 1:
                    plan.append(('pauta', v, pag))
                    pag += 1
                plan.append(('score', v, pag))
                pag += npag
        wr = PdfWriter()
        idx = os.path.join(tmp, '_idx.pdf')
        c = canvas.Canvas(idx, pagesize=(W, H))
        pag_index(c, llista, inicio)
        c.save()
        for p in PdfReader(idx).pages:
            wr.add_page(p)
        for tipo, v, n in plan:
            if tipo == 'fitxa':
                for p in PdfReader(fitxa(v, n, os.path.join(tmp, '_f_%s.pdf' % v['slug']))).pages:
                    wr.add_page(p)
            elif tipo == 'pauta':
                for p in PdfReader(pauta(n, os.path.join(tmp, '_p_%s.pdf' % v['slug']), v['titulo'])).pages:
                    wr.add_page(p)
            else:
                for ruta, k in pagines_partitura(v, n, tmp):
                    for p in PdfReader(ruta).pages:
                        wr.add_page(p)
        wr.add_metadata({'/Title': 'Dosier de Pedro · repertorio', '/Author': 'T-Clas'})
        with open(destino, 'wb') as fh:
            wr.write(fh)
    return pag - 1 - OFF, inicio


if __name__ == '__main__':
    llista = ordenar()
    dst = os.path.join(OUT, os.environ.get('PEDRO_OUT', 'DOSIER_PEDRO_completo') + '%s.pdf' % ('_BN' if BN else ''))
    n, inicio = muntar(dst, llista)
    print(n, 'páginas ->', dst)
    for v in llista:
        print('%2d  %-34s pts=%4.1f nivel=%d  %s  p.%d' % (v['num'], v['titulo'][:34], v['pts'], v['nivel'],
                                                           'NO ' if v['no'] else 'sí ', inicio[v['slug']]))
