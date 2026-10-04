# -*- coding: utf-8 -*-
"""EL LLIBRE DE PEKES — muntatge.

   Portada i index amb l'aspecte dels albums, i cada tema en quatre fulles
   (teoria · al piano · fitxa 1 · fitxa 2) dibuixades per `pekes_hojas.py`.
   Si alguna fulla no hi cap, s'atura i diu quant sobra.

   Us:  python3 build_pekes_libro.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from reportlab.pdfgen import canvas as rl_canvas                           # noqa: E402
from reportlab.pdfbase.pdfmetrics import stringWidth                      # noqa: E402

from notation import BLEED_SAFE                                           # noqa: E402
import portada                                                            # noqa: E402
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM,     # noqa: E402
                     RULE, INK, MUTED, ACCENT)
from misol import dibujar_buho                                            # noqa: E402
import pekes_hojas as ph                                                  # noqa: E402
from pekes_libro_datos import (CAPITOLS, TEMES, FULLES_PER_TEMA,          # noqa: E402
                               pagina_de, capitol_de)

SORTIDA = os.path.join(HERE, '..', 'output', 'pekes')
LOGO = os.path.join(HERE, '..', 'assets', 'asset_logo_tclas_v2.png')


def _portada(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.rect(MARGIN * 0.62, MARGIN * 0.62, W - MARGIN * 1.24, H - MARGIN * 1.24, fill=0, stroke=1)

    logo = 140
    y = H - 104
    try:
        c.drawImage(LOGO, (W - logo) / 2, y - logo, logo, logo, mask='auto',
                    preserveAspectRatio=True)
    except Exception:
        pass
    y -= logo + 52
    c.setFont('DejaVuSerif-Bold', 34)
    c.setFillColor(NAVY)
    c.drawCentredString(W / 2, y, 'El Quadern')
    y -= 40
    c.drawCentredString(W / 2, y, 'del Pianista')
    y -= 30
    c.setStrokeColor(RULE)
    c.line(W / 2 - 62, y, W / 2 + 62, y)
    y -= 34
    c.setFont('DejaVuSans-Bold', 19)
    c.setFillColor(NAVY_SOFT)
    c.drawCentredString(W / 2, y, 'PEKES · NIVELL 1')
    y -= 24
    c.setFont('DejaVuSans', 12.5)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, 'El meu primer llibre de piano, amb en Mussol Misol')
    y -= 22

    alt = 170
    ample = alt * 290 / 282.0
    dibujar_buho(c, (W - ample) / 2, y - alt, alt, pose='happy')
    y -= alt + 44

    c.setFont('DejaVuSans-Bold', 11)
    c.setFillColor(NAVY_SOFT)
    c.drawString(W / 2 - 130, y, 'NOM')
    c.setStrokeColor(RULE)
    c.line(W / 2 - 96, y - 2, W / 2 + 130, y - 2)

    c.setFont('DejaVuSans', 8.5)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, MARGIN * 0.62 + 16, 'T-CLAS  ·  DESPERTA EL TEU SO INTERIOR')
    c.showPage()


def _index(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(BLEED_SAFE, H - 6 - BLEED_SAFE, W - 2 * BLEED_SAFE, 6, fill=1, stroke=0)

    y = H - 46
    c.setFont('DejaVuSans-Bold', 9.5)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'PEKES  ·  LA RUTA MUSICAL')
    c.setFont('DejaVuSans', 9.5)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, 'cada tema: teoria · al piano · fitxes')
    y -= 34
    c.setFont('DejaVuSerif-Bold', 30)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, 'Índex del llibre')
    y -= 24
    y = ph._wrap(c, 'Set capítols, del primer dia al primer concert. Cada tema té la teoria, '
                    'el que es toca al piano i les fitxes per fer a casa, sempre amb en Mussol Misol.',
                 MARGIN, y, 'DejaVuSans', 12, CONTENT_W, 15.5, NAVY_SOFT)
    y -= 4
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.line(MARGIN, y, W - MARGIN, y)
    y -= 24

    fila = 20.5
    for i, (nom, sub, temes) in enumerate(CAPITOLS, 1):
        c.setFont('DejaVuSans-Bold', 10.5)
        c.setFillColor(NAVY)
        cap = 'CAPÍTOL %d · %s' % (i, nom.upper())
        c.drawString(MARGIN, y, cap)
        tw = stringWidth(cap, 'DejaVuSans-Bold', 10.5)
        c.setFont('DejaVuSans', 9.5)
        c.setFillColor(MUTED)
        c.drawString(MARGIN + tw + 10, y, sub)
        y -= 6
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.5)
        c.line(MARGIN, y, MARGIN + 26, y)
        y -= 13
        for num, titol in temes:
            c.setFont('DejaVuSerif-Bold', 12.5)
            c.setFillColor(ACCENT)
            c.drawRightString(MARGIN + 18, y - 8, str(num))
            c.setFont('DejaVuSans-Bold', 12)
            c.setFillColor(INK)
            c.drawString(MARGIN + 28, y - 8, titol)
            pag = str(pagina_de(num))
            c.setFont('DejaVuSans', 10.5)
            c.setFillColor(MUTED)
            c.drawRightString(W - MARGIN, y - 8, pag)
            x0 = MARGIN + 28 + stringWidth(titol, 'DejaVuSans-Bold', 12) + 8
            x1 = W - MARGIN - stringWidth(pag, 'DejaVuSans', 10.5) - 8
            c.setStrokeColor(RULE)
            c.setLineWidth(0.8)
            c.setDash(1, 3)
            c.line(x0, y - 8, x1, y - 8)
            c.setDash()
            y -= fila
        y -= 10
    ph.peu(c, 2)
    c.showPage()


def _fulles_tema(c, num):
    tema = TEMES[num]
    cap_n, cap = capitol_de(num)
    base = dict(kicker='Pekes · capítol %d · %s' % (cap_n, cap), titol=tema['titol'])
    pag = pagina_de(num)
    finals = []
    for clau, nom in (('teoria', 'teoria'), ('piano', 'al piano'), ('fitxa', 'fitxa')):
        sec = tema[clau]
        fulles = sec['fulles']
        num_ex = 1
        for k, blocs in enumerate(fulles):
            esq = 'Tema %d · %s' % (num, nom)
            if len(fulles) > 1:
                esq += ' %d de %d' % (k + 1, len(fulles))
            cfg = dict(base, esquina=esq, intro=sec.get('intro') if k == 0 else None,
                       regles=sec.get('regles') if k == 0 else None,
                       nom_data=(clau == 'fitxa'))
            y, num_ex = ph.fulla(c, cfg, blocs, pag, primer_num=num_ex)
            finals.append((esq, y))
            pag += 1
    if pag - pagina_de(num) != FULLES_PER_TEMA:
        raise ph.NoHiCap('el tema %d te %d fulles i l’index en compta %d'
                         % (num, pag - pagina_de(num), FULLES_PER_TEMA))
    return finals


def construir(nom='Llibre_Pekes_mostra.pdf'):
    os.makedirs(SORTIDA, exist_ok=True)
    ruta = os.path.join(SORTIDA, nom)
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('El Quadern del Pianista · Pekes')
    del portada.NO_CABEN[:]
    _portada(c)
    _index(c)
    finals = []
    for num in sorted(TEMES):
        finals += _fulles_tema(c, num)
    c.save()
    return ruta, finals


def main(argv):
    try:
        ruta, finals = construir()
    except ph.NoHiCap as e:
        print('NO HI CAP:', e)
        return 1
    print('Llibre Pekes · %s' % os.path.basename(ruta))
    for etq, y in finals:
        print('  %-26s y final = %.1f' % (etq, y))
    if portada.NO_CABEN:
        print('NO CABEN:', portada.NO_CABEN)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
