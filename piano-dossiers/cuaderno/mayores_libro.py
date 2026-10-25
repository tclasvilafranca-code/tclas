# -*- coding: utf-8 -*-
"""Libro completo del dosier de Eva (Sant Cugat, 30 min de clase): portada, como usarlo,
   calendario/indice, registro y las piezas de menos a mas dificultad, numeradas seguidas."""
import glob
import importlib
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
from mayores_motor import *                                        # noqa: F401,F403
from portada import build_cover, _wrap
import tema_ca

ASSETS = os.path.join(HERE, '..', 'assets')
FRONT = {'lola': 6, 'txell': 6, 'alba': 14}.get(ALUMNA, 4)                              # portada + 3 hojas (Lola: + colors i figures)
DIFIC = {1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3, 9: 3, 10: 3, 11: 4, 12: 4, 13: 4,
         14: 4, 15: 5}
if ALUMNA != 'eva':
    DIFIC = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2, 8: 3, 9: 3, 10: 3, 11: 3, 12: 4, 13: 4,
             14: 4, 15: 5}
if ALUMNA == 'abril':
    DIFIC = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2, 8: 3, 9: 3, 10: 3, 11: 3, 12: 4, 13: 4,
             14: 4, 15: 5}
AUTOR_CORTO = {}


def corta(t, n):
    if len(t) <= n:
        return t
    return t[:n].rsplit(' ', 1)[0].rstrip(' ·,') + '…'


def cargar():
    specs = []
    for f in sorted(glob.glob(os.path.join(HERE, {'eva': 'mp', 'sharifa': 'ms', 'abril': 'ab', 'lola': 'lo', 'alba': 'ba', 'txell': 'tx'}.get(ALUMNA, 'ms') + '_[0-9][0-9]_*.py'))):
        mod = importlib.import_module(os.path.basename(f)[:-3])
        if hasattr(mod, 'SPEC'):
            specs.append(mod.SPEC)
    specs.sort(key=lambda s: s['num'])
    return specs


def _marco(c, n, derecha):
    marco_pag(c, n, derecha)


def marco_pag(c, n, derecha):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(18, H - 24, W - 36, 6, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, H - 44, 'DOSIER DE ' + ALUMNA.upper() + ' · CURSO NOVIEMBRE - JULIO')
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, H - 44, derecha)
    c.setFont('DejaVuSans', 7.4)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(n))


def misol_pie(c, y, txt, pose='normal', alto_buho=62.0):
    if tema_ca.ACTIU and y - tema_ca.alto_caixa_misol(CONTENT_W, txt, alto_buho) > 44:
        tema_ca.caixa_misol(c, MARGIN, y, CONTENT_W, txt, pose, alto_buho)


def pag_como(c, n):
    marco_pag(c, n, 'Cómo usar el dosier')
    y = titulo_pag(c, 'Cómo usar este dosier',
                   'Pensado para clases de media hora: una pieza cada dos semanas, de la más '
                   'fácil a la más difícil.' if ALUMNA != 'alba' else
                   "Pensat per a classes de mitja hora. Abans de les peces hi ha una secció d'exercicis de base "
                   "(pàgines 5 a 14): postura, notes, escales, acords i ritme. Fes-los entre peça i peça.")
    y -= 16
    # esquema de cada pieza
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'LAS HOJAS DE CADA PIEZA')
    y -= 12
    items = [('1', 'Ficha de la partitura', 'Los datos medidos (tonalidad, compás, tempo), el mapa de la '
                                             'pieza, el reto, el truco y un QR para escucharla.'),
             ('2', 'Manos', 'Cuatro pasos para la mano izquierda y cuatro para la derecha, y la '
                            'técnica en tres frases.'),
             ('3', 'Guía por bloques', 'La pieza partida en bloques: qué tocar, en qué orden y '
                                       'cómo juntar las manos.'),
             ('4', 'La partitura', 'Tu partitura con los bloques en color y burbujas que explican '
                                   'qué practicar en cada sitio.'),
             ('5', 'Papel pautado', 'Para copiar un compás, escribir la escala o inventar.')]
    if ALUMNA == 'lola':
        items = [('1', 'Fitxa de la partitura', 'Les dades de la peça, el seu mapa, el repte, un truc i un QR per escoltar-la.'),
                 ('2', 'Mans', 'Quatre passos per a la mà esquerra i quatre per a la dreta, i la tècnica en tres frases.'),
                 ('3', 'Guia per blocs', 'La cançó partida en trossos petits: què toca cada mà i com ajuntar-les.'),
                 ('4', 'La partitura', 'La teva partitura amb les notes pintades del seu color i bocadillos del Mussol.'),
                 ('5', 'Paper pautat', 'Per escriure notes i pintar-les, o inventar una cançó.')]
    if CONTINUA and ALUMNA != 'lola':
        items = list(items)
        items[3] = ('4', 'La partitura', 'La teva partitura sencera, tal com és: els trams, al marge esquerre, i les indicacions, al dret.')
    for k, t, d in items:
        c.setFillColor(PANEL)
        c.roundRect(MARGIN, y - 34, CONTENT_W, 34, 4, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.circle(MARGIN + 18, y - 17, 9, fill=1, stroke=0)
        c.setFillColor(BLANCO)
        c.setFont('DejaVuSerif-Bold', 10)
        c.drawCentredString(MARGIN + 18, y - 20.6, k)
        c.setFillColor(NAVY)
        c.setFont('DejaVuSerif-Bold', 10)
        c.drawString(MARGIN + 38, y - 14, t)
        _wrap(c, d, MARGIN + 38, y - 25, 'DejaVuSans', 8, CONTENT_W - 50, 10, INK)
        y -= 40
    y -= 8
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'UNA CLASE DE 30 MINUTOS')
    y -= 12
    partes = [('5′', 'Calentar', 'La mano izquierda del bloque de hoy, sola y despacio.', AZUL),
              ('10′', 'Bloque nuevo', 'Izquierda, derecha y juntas, siguiendo la guía de bloques.',
               OCRE),
              ('10′', 'Tocar lo ya sabido', 'Los bloques anteriores y, si se puede, la pieza entera.',
               VERDE),
              ('5′', 'Deberes', 'Una sola tarea para casa: la que marca la tarjeta del bloque.',
               ROJO)]
    x = MARGIN
    ancho = (CONTENT_W - 3 * 8) / 4
    for t, tit, txt, col in partes:
        c.setFillColor(PANEL)
        c.roundRect(x, y - 86, ancho, 86, 5, fill=1, stroke=0)
        c.setFillColor(col)
        c.rect(x, y - 86, ancho, 3, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 20)
        c.drawString(x + 10, y - 30, t)
        c.setFont('DejaVuSerif-Bold', 9.4)
        c.setFillColor(NAVY)
        c.drawString(x + 10, y - 46, tit)
        _wrap(c, txt, x + 10, y - 58, 'DejaVuSans', 7.6, ancho - 18, 9.6, INK)
        x += ancho + 8
    y -= 104
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'CÓMO LEER LA PARTITURA ANOTADA' if ALUMNA != 'lola' else 'COM LLEGIR LA PARTITURA')
    y -= 12
    h = 74
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 5, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    txt = ('El paréntesis de color del margen izquierdo y su número dicen en qué bloque estás. '
           'Las burbujas explican qué practicar: «mano izquierda» y «mano derecha» (color ocre y '
           'azul), «las dos», «ojo» (algo que no hay que pasar por alto) y, en los dúos, «Primo» y '
           '«Secondo». Los recuadros finos con número rodean lo importante: tachad el número con '
           'lápiz cuando lo tengáis. Los acordes se llaman como siempre (La menor, Sol mayor…); '
           'encima de algunas partituras vienen en cifrado americano (A = La, B = Si, C = Do, '
           'D = Re, E = Mi, F = Fa, G = Sol).')
    if ALUMNA == 'lola':
        txt = ("Les notes ja estan pintades: DO vermell, RE taronja, MI groc, FA verd, SOL blau, LA lila i SI gris. "
               "Al marge hi ha un parèntesi de color amb un número: és el bloc on ets. Els bocadillos expliquen "
               "què practicar: «mà esquerra» (ocre), «mà dreta» (blau), «les dues» i «ojo» (el Mussol et diu "
               "alguna cosa important). Quan tinguis un bloc ben après, marca'l amb un llapis!")
    if CONTINUA and ALUMNA != 'lola':
        txt = ("La partitura surt sencera, com la tens a Drive. El parèntesi de color del marge esquerre i el seu número diuen en quin tram "
               "ets. Les indicacions són al marge dret, cadascuna amb una lletra que es repeteix en un punt damunt de la partitura: "
               "«mà esquerra», «mà dreta», «les dues» i «ull» (alguna cosa que no s'ha de passar per alt)"
               + (" i, en els duets, «Primo» i «Secondo»" if ALUMNA != 'alba' else '') + ". Els acords es diuen com sempre (La menor, Sol major…); "
               "a sobre d'algunes partitures surten en xifrat americà (A = La, B = Si, C = Do, D = Re, E = Mi, F = Fa, G = Sol).")
    _wrap(c, txt, MARGIN + 14, y - 14, 'DejaVuSans', 8.2, CONTENT_W - 28, 11, INK)
    misol_pie(c, y - h - 22, "Hola! Soc en Mussol Misol i et faré companyia a cada peça. Si un "
              "consell em ve al cap, el trobaràs en aquest quadre. Fes cas a l'ocell!", 'normal')
    c.showPage()


def pag_calendario(c, n, specs, inicio):
    marco_pag(c, n, 'El curso de un vistazo')
    y = titulo_pag(c, 'El curso de un vistazo',
                   'Quince piezas de noviembre a julio, de menos a más dificultad. Una pieza cada '
                   'dos semanas; las más largas pueden llevar un poco más.')
    y -= 14
    xs = [MARGIN, MARGIN + 26, MARGIN + 215, MARGIN + 340, MARGIN + 438]
    for x, t in zip(xs, ['Nº', 'PIEZA', 'CUÁNDO', 'NIVEL', 'PÁG.']):
        c.setFont('DejaVuSans-Bold', 7)
        c.setFillColor(MUTED)
        c.drawString(x, y, t)
    y -= 8
    for s in specs:
        h = 33
        c.setFillColor(PANEL)
        c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
        col = COLORES_BLOQUE[(s['num'] - 1) % len(COLORES_BLOQUE)]
        c.setFillColor(col)
        c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 11)
        c.setFillColor(NAVY)
        c.drawString(xs[0] + 6, y - 20, str(s['num']))
        c.setFont('DejaVuSerif-Bold', 9.6)
        c.drawString(xs[1], y - 14, corta(s['titulo'], 34))
        c.setFont('DejaVuSans', 7)
        c.setFillColor(MUTED)
        c.drawString(xs[1], y - 25, corta(s['autor'], 38))
        c.setFont('DejaVuSans', 8)
        c.setFillColor(INK)
        c.drawString(xs[2], y - 20, s['mes'].split(' (')[0])
        d = DIFIC.get(s['num'], 3)
        for k in range(5):
            c.setFillColor(NAVY if k < d else GRIS)
            c.circle(xs[3] + 4 + k * 11, y - 18, 3.6, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 9)
        c.setFillColor(NAVY)
        c.drawString(xs[4], y - 20, str(inicio[s['num']]))
        y -= h + 4
    misol_pie(c, y - 6, "Cada peça és una petita aventura: una cada dues setmanes. Les més "
              "llargues poden portar una mica més, i no passa res. Poc a poc, i sense pressa!",
              'happy', 52.0)
    c.showPage()


def pag_registro(c, n, specs):
    marco_pag(c, n, 'Mi registro')
    y = titulo_pag(c, 'Mi registro',
                   'Marca cada pieza cuando la tengas: por bloques, entera y a tempo.')
    y -= 14
    xs = [MARGIN + 190, MARGIN + 250, MARGIN + 310, MARGIN + 370, MARGIN + 430]
    for x, t in zip(xs, ['Bloques', 'Entera', 'A tempo', 'Grabada', 'Fecha']):
        c.setFont('DejaVuSans-Bold', 6.6)
        c.setFillColor(MUTED)
        c.drawString(x, y, t)
    y -= 8
    for s in specs:
        h = 30
        c.setFillColor(PANEL)
        c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 9)
        c.setFillColor(NAVY)
        c.drawString(MARGIN + 10, y - 19, '%d · %s' % (s['num'], corta(s['titulo'], 31)))
        for x in xs[:4]:
            c.setStrokeColor(NAVY)
            c.setLineWidth(0.9)
            c.roundRect(x + 8, y - 21, 12, 12, 2, fill=0, stroke=1)
        c.setStrokeColor(GRIS)
        c.line(xs[4], y - 20, xs[4] + 52, y - 20)
        y -= h + 4
    misol_pie(c, y - 6, "Cada vegada que acabis una peça, marca-la aquí. Quan tinguis les quinze, "
              "farem una festa! (D'acord, una festa de música.)", 'happy', 52.0)
    c.showPage()


def construir(salida, solo=None):
    specs = cargar()
    if solo:
        specs = [s for s in specs if s['num'] in solo]
    partes, inicio, pag = [], {}, FRONT + 1
    for s in specs:
        wr, n = construir_pieza(s, pag)
        inicio[s['num']] = pag
        partes.append(wr)
        pag += n
        print('pieza', s['num'], s['slug'], n, 'páginas')
    f = os.path.join(OUT, '_front.pdf')
    c = canvas.Canvas(f, pagesize=(W, H))
    build_cover(c, os.path.join(ASSETS, 'asset_logo_tclas_v2.png'), ALUMNA.capitalize(),
                'Quince piezas · de menos a más · 30 minutos por clase',
                'Curso de noviembre a julio',
                extra=(lambda cc: tema_ca.caixa_misol(
                    cc, MARGIN + 30, 232, CONTENT_W - 60, "Hola, " + ALUMNA.capitalize() + "! Soc en Mussol Misol. Aquest "
                    "quadern té quinze peces, de les més fàcils a les més difícils. Jo seré al teu "
                    "costat, i de tant en tant et donaré algun truc.", 'happy', 84.0))
                if tema_ca.ACTIU else None)
    pag_como(c, 2)
    if ALUMNA in ('lola', 'txell'):
        import lo_front
        lo_front.pag_colors(c, 3, marco_pag, misol_pie, color=(ALUMNA == 'lola'))
        lo_front.pag_figures(c, 4, marco_pag, misol_pie)
        pag_calendario(c, 5, specs, inicio)
        pag_registro(c, 6, specs)
    elif ALUMNA == 'alba':
        import ba_front
        import lo_front
        pag_calendario(c, 3, specs, inicio)
        pag_registro(c, 4, specs)
        ba_front.pag_postura(c, 5, marco_pag)
        lo_front.pag_colors(c, 6, marco_pag, misol_pie, color=False)
        lo_front.pag_figures(c, 7, marco_pag, misol_pie)
        ba_front.pag_ex_dreta(c, 8, marco_pag)
        ba_front.pag_ex_esquerra(c, 9, marco_pag)
        ba_front.pag_ex_juntes(c, 10, marco_pag)
        ba_front.pag_escales(c, 11, marco_pag)
        ba_front.pag_acords(c, 12, marco_pag)
        ba_front.pag_ritme(c, 13, marco_pag)
        ba_front.pag_pla(c, 14, marco_pag)
    else:
        pag_calendario(c, 3, specs, inicio)
        pag_registro(c, 4, specs)
    c.save()
    wr = PdfWriter()
    for p in PdfReader(f).pages:
        wr.add_page(p)
    os.remove(f)
    for w in partes:
        for p in w.pages:
            wr.add_page(p)
    with open(salida, 'wb') as fh:
        wr.write(fh)
    return pag - 1


if __name__ == '__main__':
    solo = [int(x) for x in sys.argv[1:]] or None
    out = os.path.join(OUT, 'DOSIER_%s_completo%s.pdf' % (ALUMNA.upper(), '_BN' if os.environ.get('BN') == '1' else ''))
    print(construir(out, solo), 'paginas ->', out)
