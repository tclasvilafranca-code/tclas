# -*- coding: utf-8 -*-
"""Dosier de Pedro (adult, nivell 1-4): índex de menys a més dificultat + una fitxa per partitura
   (i la partitura original a continuació, tret de les que porten «NO» al nom: d'aquestes només la fitxa).

   python3 pedro_libro.py            -> entrega/DOSIER_PEDRO_completo.pdf
   BN=1 python3 pedro_libro.py       -> entrega/DOSIER_PEDRO_completo_BN.pdf

   Les dades de cada peça (mesurades sobre el PDF) són a pedro_datos.py. Les partitures NO es versionen:
   students/pedro/source/ (veure .gitignore). Norma de les peces a quatre mans: la partitura comença en
   pàgina PARELLA (pàgines enfrontades) i, si cal, s'intercala un full de paper pautat."""
import io
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.setdefault('ALUMNA', 'alba')          # tema sobri d'adult (sense Mussol Misol), text fix en català
os.environ.setdefault('IDIOMA', 'ca')
from mayores_motor import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, INK, MUTED, PANEL, OCRE, AZUL, GRIS, COLORES_BLOQUE,
                           marco, titulo_pag, FICHA, build_ficha, build_pauta, _qr, _wrap)
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter, Transformation
import pymupdf
import pedro_datos as PD

BN = os.environ.get('BN') == '1'
SRC = os.path.join(HERE, '..', 'students', 'pedro', 'source')
SRC_BN = os.path.join(HERE, '..', 'students', 'pedro', 'source_bn')
OUT = os.path.join(HERE, 'entrega')
KICK = 'DOSIER DE PEDRO · REPERTORI'
TEMPOS_IT = ('Largo', 'Adagio', 'Allegro', 'Allegretto', 'Andantino', 'Moderato')


# ------------------------------------------------------------------ dificultat (criteri declarat i comprovable)
def puntuar(s):
    """Punts de dificultat a partir de dades MESURADES (vegeu pedro_datos.py)."""
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


# ------------------------------------------------------------------ fitxa
class _Lienzo(canvas.Canvas):
    """Retén el showPage de build_ficha per poder afegir, amb la y final que retorna, el quadre de notes de classe."""
    retener = False

    def showPage(self):
        if not self.retener:
            super().showPage()


def notas_clase(c, y):
    """Quadre per escriure a mà (digitació, passatges difícils, data de la classe): omple el que queda de full."""
    top = y - 18
    bot = 46
    if top - bot < 60:
        return
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, top, 'NOTES DE CLASSE')
    c.setFont('DejaVuSans', 7.2)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 82, top, 'digitació · passatges a repassar · què treballem la propera setmana')
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
    if tempo.startswith('No indicat («'):
        txt = tempo.split('«')[1].rstrip('»)')
        datos_t = ('Caràcter', txt)
    elif tempo == 'No indicat':
        datos_t = ('Tempo', 'No indicat')
    elif tempo.startswith('♩'):
        datos_t = ('Tempo', tempo)
    else:
        datos_t = ('Tempo' if tempo in TEMPOS_IT else 'Caràcter', tempo)
    ton = v['ton']
    ton_l = 'Tonalitat' if ('major' in ton or 'menor' in ton) else 'Armadura'
    ton = (ton.replace('Sense alteracions a l\'armadura', 'Sense armadura').replace('Sense alteracions', 'Sense armadura')
           .replace(' (acords impresos)', '').replace('Armadura de tres sostinguts (Fa♯ Do♯ Sol♯)', '3 sostinguts')
           .replace('Armadura d\'un sostingut (Sol major)', 'Sol major (1 ♯)').replace(' (un sostingut)', ' (1 ♯)'))
    total = v['compases']
    ncomp = '%d%s' % (total, ' + anacrusi' if v['ana'] else '')
    datos = [(ton_l, ton), ('Compàs', v['compas']), datos_t, ('Figura curta', PD.FIGS[v['fig']].capitalize()), ('Compassos', ncomp)]
    # mapa: seccions formals si la forma és clara; si no, un tram per sistema de la partitura (és el que s'ha mesurat)
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
        ideas_pie += ' · Mapa: %s de la teva partitura.' % ('cada tram és un sistema' if g == 1 else 'cada tram són dos sistemes')
    sp = FICHA(datos=datos, secciones=secs, total=total, ideas=v['ideas'], especial=v['especial'], reto=v['reto'],
               truco=v['truco'], sabias=v['sabias'], qr_texto='Escolta-la amb la partitura al davant.', ts=v['ts'],
               ideas_titulo='La peça en quatre idees', ideas_pie=ideas_pie,
               cuenta_titulo='Com es compta un compàs de %d/%d' % v['ts'],
               cuenta_pie='Un compàs de %d/%d en corxeres. Aquí només el ritme; les notes, a la teva partitura.' % v['ts'])
    qr = os.path.join(OUT, '_qr_pedro_%s.png' % v['slug'])
    _qr('https://www.youtube.com/results?search_query=' + v['yt'], qr)
    cfg = dict(sp)
    cfg.update(kicker='Pedro · peça %d · %s' % (v['num'], v['titulo']), page_num=num_pag, time_sig=v['ts'],
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
    build_pauta(c, dict(kicker='Pedro · ' + titol, page_num=num_pag, titulo_pauta='Per escriure', misol=None,
                        pie_pauta='espai per apuntar passos, digitació o els compassos que us costen · '
                                  'la partitura del duet s\'obre a la pàgina següent'))
    c.save()
    return ruta


# ------------------------------------------------------------------ pàgines de partitura
def pagines_partitura(v, num0, tmpdir):
    """Retorna [(ruta_pdf_d_una_pagina, num)]: cada pàgina de la partitura original, escalada a A4 i amb el peu T-Clas."""
    src = os.path.join(SRC_BN if BN and os.path.exists(os.path.join(SRC_BN, v['slug'] + '.pdf')) else SRC, v['slug'] + '.pdf')
    rd = PdfReader(src)
    out = []
    for k, pg in enumerate(rd.pages):
        n = num0 + k
        ruta = os.path.join(tmpdir, '_s_%s_%d.pdf' % (v['slug'], k))
        # base A4 blanca amb el peu
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


# ------------------------------------------------------------------ índex
def pag_index(c, llista, inicio):
    marco(c, KICK, 'El repertori de menys a més', 1)
    y = titulo_pag(c, 'El repertori, de menys a més',
                   '%d peces ordenades per dificultat. Les marcades «només fitxa» tenen la partitura impresa a part: '
                   'la fitxa és la guia per treballar-la.' % len(llista))
    y -= 8
    xs = [MARGIN, MARGIN + 26, MARGIN + 270, MARGIN + 392, MARGIN + 462]
    for x, t in zip(xs, ['Nº', 'PEÇA', 'QUÈ PORTA', 'NIVELL', 'PÀG.']):
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
        c.drawString(xs[2], y - (10 if v['duo'] else 13.5), 'Només fitxa' if v['no'] else 'Fitxa + partitura')
        if v['duo']:
            c.setFont('DejaVuSans', 6.2)
            c.setFillColor(MUTED)
            c.drawString(xs[2], y - 18, 'peça a quatre mans')
        for k in range(5):
            c.setFillColor(NAVY if k < v['nivel'] else GRIS)
            c.circle(xs[3] + 4 + k * 9.6, y - 12.5, 3.1, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 8.6)
        c.setFillColor(NAVY)
        c.drawString(xs[4], y - 13.5, str(inicio[v['slug']]))
        y -= h + 2.0
    y -= 10
    y = _wrap(c, 'Criteri: longitud (compassos), figura més curta, compàs, activitat de la mà esquerra, alteracions, canvis de '
                 'posició, matisos i indicacions, quatre mans, anacrusi i xifrats. Tot mesurat sobre la teva edició. '
                 'Les curiositats del «Sabies que…?» són culturals i no estan verificades sobre la partitura.',
              MARGIN, y, 'DejaVuSans', 7.2, CONTENT_W, 9.6, MUTED)
    c.showPage()
    return y


# ------------------------------------------------------------------ muntatge
def muntar(destino, llista):
    os.makedirs(OUT, exist_ok=True)
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        # pas 1: calcular les pàgines de cada peça (per fer l'índex amb números)
        inicio, pag, plan = {}, 2, []
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
        wr.add_metadata({'/Title': 'Dosier de Pedro · repertori', '/Author': 'T-Clas'})
        with open(destino, 'wb') as fh:
            wr.write(fh)
    return pag - 1, inicio


if __name__ == '__main__':
    llista = ordenar()
    dst = os.path.join(OUT, 'DOSIER_PEDRO_completo%s.pdf' % ('_BN' if BN else ''))
    n, inicio = muntar(dst, llista)
    print(n, 'pàgines ->', dst)
    for v in llista:
        print('%2d  %-34s pts=%4.1f nivel=%d  %s  p.%d' % (v['num'], v['titulo'][:34], v['pts'], v['nivel'],
                                                           'NO ' if v['no'] else 'sí ', inicio[v['slug']]))
