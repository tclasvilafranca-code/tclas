# -*- coding: utf-8 -*-
"""EL LLIBRE DE PEKES — muntatge.

   Portada i index amb l'aspecte dels albums; cada tema amb les seves fulles
   de teoria, d'al piano i de fitxa, dibuixades per `pekes_hojas.py`; i al
   final de cada capitol, la pagina de repas amb la medalla.

   Tres comprovacions, i cap es pot saltar:
   - si una fulla no hi cap, s'atura i diu quant sobra;
   - si una fulla acaba massa amunt (y final > 132), avisa: sobra paper;
   - la norma de varietat: dos temes seguits no poden portar les mateixes
     fitxes (cada tema n'ha de portar almenys DOS tipus que l'anterior no
     tenia) i cap tipus pot sortir a mes del 60 % dels temes.

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
from pekes_libro_datos import (CAPITOLS, TEMES, REPASSOS,                 # noqa: E402
                               paginacio, capitol_de)

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

    pags = paginacio()
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
        c.setFont('DejaVuSans-Bold', 9)
        c.setFillColor(ACCENT)
        c.drawRightString(W - MARGIN, y, 'repàs i medalla · %d' % pags[('repas', i)])
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
            pag = str(pags[('tema', num)])
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
    pag = paginacio()[('tema', num)]
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
            y, num_ex = _fulla(c, cfg, blocs, pag, num_ex)
            finals.append((esq, y))
            pag += 1
    return finals


NO_HI_CAP = []


def _fulla(c, cfg, blocs, pag, num_ex):
    """Com `ph.fulla`, pero si no hi cap ho apunta i continua: aixi una sola
       passada diu TOTES les fulles que s'han de retallar, no nomes la primera."""
    try:
        return ph.fulla(c, cfg, blocs, pag, primer_num=num_ex)
    except ph.NoHiCap as e:
        NO_HI_CAP.append(str(e))
        c.showPage()
        return 0.0, num_ex + 9


def _repas(c, cap_n):
    nom = CAPITOLS[cap_n - 1][0]
    r = REPASSOS[cap_n]
    cfg = dict(kicker='Pekes · capítol %d · %s' % (cap_n, nom), titol='Repàs i medalla',
               esquina='Capítol %d · repàs' % cap_n, intro=r['intro'], nom_data=True)
    y, _n = _fulla(c, cfg, r['blocs'], paginacio()[('repas', cap_n)], 1)
    return [(cfg['esquina'], y)]


def revisar_varietat():
    """La norma de varietat del projecte, aplicada a les fitxes dels temes."""
    errors = []
    tipus = {}
    for n in sorted(TEMES):
        tipus[n] = {b['tipus'] for f in TEMES[n]['fitxa']['fulles'] for b in f
                    if b['tipus'] in ph.FITXA}
    nums = sorted(tipus)
    for a, b in zip(nums, nums[1:]):
        nous = tipus[b] - tipus[a]
        if len(nous) < 2:
            errors.append('tema %d: nomes %d tipus de fitxa nous respecte al %d (%s)'
                          % (b, len(nous), a, ', '.join(sorted(tipus[b]))))
    compte = {}
    for n in nums:
        for t in tipus[n]:
            compte[t] = compte.get(t, 0) + 1
    for t, k in sorted(compte.items()):
        if k > 0.6 * len(nums):
            errors.append('el tipus %s surt a %d temes de %d' % (t, k, len(nums)))
    return errors, compte


def reequilibrar():
    """Abans de res: cap fulla pot desbordar. Si una no hi cap, l'ultim bloc passa
       al principi de la seguent fulla de la mateixa seccio (o en neix una de
       nova). Es fa sobre les DADES, abans de calcular la paginacio, perque el
       numero de pagina de l'index depen de quantes fulles te cada tema."""
    moguts = []
    for num in sorted(TEMES):
        cap_n, cap = capitol_de(num)
        base = dict(kicker='Pekes · capítol %d · %s' % (cap_n, cap),
                    titol=TEMES[num]['titol'])
        for clau, nom in (('teoria', 'teoria'), ('piano', 'al piano'), ('fitxa', 'fitxa')):
            sec = TEMES[num][clau]
            fulles = sec['fulles']
            k = 0
            while k < len(fulles):
                cfg = dict(base, esquina='Tema %d · %s' % (num, nom),
                           intro=sec.get('intro') if k == 0 else None,
                           regles=sec.get('regles') if k == 0 else None,
                           nom_data=(clau == 'fitxa'))
                while len(fulles[k]) > 1 and ph.altura(cfg, fulles[k]) < ph.SUELO:
                    sobra = [i for i, b in enumerate(fulles[k]) if b['tipus'] in ph.CREIXEN]
                    if sobra and sobra[-1] > 0:
                        # un bloc que creix es pot perdre sense perdre material
                        bl = fulles[k].pop(sobra[-1])
                        moguts.append('tema %d · %s: es treu un bloc "%s" que sobrava'
                                      % (num, nom, bl['tipus']))
                        continue
                    bl = fulles[k].pop()
                    if bl['tipus'] == 'estrelles' and k + 1 == len(fulles):
                        # unes estrelles soles no justifiquen una fulla nova
                        moguts.append('tema %d · %s: es treuen les estrelles, que no hi caben'
                                      % (num, nom))
                        continue
                    if k + 1 == len(fulles):
                        fulles.append([bl])
                    else:
                        fulles[k + 1].insert(0, bl)
                    moguts.append('tema %d · %s: un bloc "%s" passa a la fulla %d'
                                  % (num, nom, bl['tipus'], k + 2))
                k += 1
    return moguts


def construir(nom='Llibre_Pekes.pdf'):
    os.makedirs(SORTIDA, exist_ok=True)
    ruta = os.path.join(SORTIDA, nom)
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('El Quadern del Pianista · Pekes')
    del portada.NO_CABEN[:]
    del NO_HI_CAP[:]
    for m in reequilibrar():
        print('  reequilibri:', m)
    _portada(c)
    _index(c)
    finals = []
    for i, (_nom, _sub, temes) in enumerate(CAPITOLS, 1):
        for num, _t in temes:
            finals += _fulles_tema(c, num)
        finals += _repas(c, i)
    c.save()
    return ruta, finals


def main(argv):
    try:
        ruta, finals = construir()
    except ph.NoHiCap as e:
        print('NO HI CAP:', e)
        return 1
    print('Llibre Pekes · %s · %d pagines' % (os.path.basename(ruta), len(finals) + 2))
    mal = 0
    for etq, y in finals:
        avis = ''
        if y > 132:
            avis = '  <-- SOBRA PAPER'
            mal += 1
        elif y < 44:
            avis = '  <-- TREPITJA EL PEU'
            mal += 1
        print('  %-30s y final = %6.1f%s' % (etq, y, avis))
    errors, compte = revisar_varietat()
    print('Tipus de fitxa:', ', '.join('%s %d' % kv for kv in sorted(compte.items())))
    for e in errors:
        print('VARIETAT:', e)
    for e in NO_HI_CAP:
        print('NO HI CAP:', e)
    if portada.NO_CABEN:
        print('NO CABEN:', portada.NO_CABEN)
        return 1
    if NO_HI_CAP or mal or errors:
        return 1
    print('TOT OK')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
