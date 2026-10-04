# -*- coding: utf-8 -*-
"""EL LIBRO DE PEKES — con el motor y el aspecto de los albumes de alumno.

   Portada e indice como los de los albumes, y cada tema en tres hojas:

     teoria    `hoja_teoria.build_teoria`   (piezas de la ficha de partitura)
     al piano  `hoja_piano.build_piano`     (la misma hoja de "Como se aprende")
     ficha     `hoja_deberes.build_deberes` (la misma hoja de deberes)

   Musol Misol entra en las tres como un bloque mas (tipo 'misol').

   Uso:  python3 build_pekes_libro.py            -> solo los temas escritos
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
                     RULE, INK, MUTED, ACCENT, _fit, _wrap)
from hoja_teoria import build_teoria                                      # noqa: E402
from hoja_piano import build_piano                                        # noqa: E402
from hoja_deberes import build_deberes                                    # noqa: E402
from misol import dibujar_buho                                            # noqa: E402
from pekes_libro_datos import CAPITULOS, TEMAS, pagina_de, capitulo_de   # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'pekes')
LOGO = os.path.join(HERE, '..', 'assets', 'asset_logo_tclas_v2.png')


def _portada(c):
    """La portada de los albumes (marco fino, logo, titulo en serifa) con el
       buho debajo del titulo."""
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.rect(MARGIN * 0.62, MARGIN * 0.62, W - MARGIN * 1.24, H - MARGIN * 1.24, fill=0, stroke=1)

    logo = 150
    y = H - 120
    try:
        c.drawImage(LOGO, (W - logo) / 2, y - logo, logo, logo, mask='auto',
                    preserveAspectRatio=True)
    except Exception:
        pass
    y -= logo + 48

    c.setFont('DejaVuSerif-Bold', 30)
    c.setFillColor(NAVY)
    c.drawCentredString(W / 2, y, 'El Cuaderno')
    y -= 34
    c.drawCentredString(W / 2, y, 'del Pianista')
    y -= 30
    c.setStrokeColor(RULE)
    c.line(W / 2 - 62, y, W / 2 + 62, y)
    y -= 30
    c.setFont('DejaVuSans-Bold', 16)
    c.setFillColor(NAVY_SOFT)
    c.drawCentredString(W / 2, y, 'PEKES · NIVEL 1')
    y -= 20
    c.setFont('DejaVuSans', 10.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, 'Mi primer libro de piano, con Musol Misol')
    y -= 22

    alto = 150
    ancho = alto * 290 / 282.0
    dibujar_buho(c, (W - ancho) / 2, y - alto, alto, pose='happy')
    y -= alto + 40

    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(W / 2 - 110, y, 'NOMBRE')
    c.setStrokeColor(RULE)
    c.line(W / 2 - 64, y - 2, W / 2 + 110, y - 2)

    c.setFont('DejaVuSans', 8)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, MARGIN * 0.62 + 16, 'T-CLAS  ·  DESPIERTA TU SONIDO INTERIOR')
    c.showPage()


def _indice(c):
    """El indice de los albumes: capitulo con su linea, y debajo los temas con
       su numero en ocre y la pagina a la derecha."""
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(BLEED_SAFE, H - 6 - BLEED_SAFE, W - 2 * BLEED_SAFE, 6, fill=1, stroke=0)

    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, 'PEKES  ·  LA RUTA MUSICAL')
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, 'cada tema: teoría · al piano · ficha')
    y -= 28
    c.setFont('DejaVuSerif-Bold', 22)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, 'Índice del libro')
    y -= 16
    y = _wrap(c, 'Siete capítulos, del primer día al primer concierto. Cada tema tiene tres '
                 'hojas: la teoría, lo que se toca al piano y una ficha para hacer en casa.',
              MARGIN, y, 'DejaVuSans', 8.8, CONTENT_W, 11.2, MUTED)
    y -= 8
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.line(MARGIN, y, W - MARGIN, y)
    y -= 26

    fila = 21.0
    for i, (nombre, sub, temas) in enumerate(CAPITULOS, 1):
        c.setFont('DejaVuSans-Bold', 9.6)
        c.setFillColor(NAVY)
        cab = 'CAPÍTULO %d · %s' % (i, nombre.upper())
        c.drawString(MARGIN, y, cab)
        tw = stringWidth(cab, 'DejaVuSans-Bold', 9.6)
        c.setFont('DejaVuSans', 8.4)
        c.setFillColor(MUTED)
        c.drawString(MARGIN + tw + 10, y, sub)
        y -= 6
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.4)
        c.line(MARGIN, y, MARGIN + 26, y)
        y -= 14
        for num, titulo in temas:
            c.setFont('DejaVuSerif-Bold', 11)
            c.setFillColor(ACCENT)
            c.drawRightString(MARGIN + 17, y - 8, str(num))
            c.setFont('DejaVuSans-Bold', 10.2)
            c.setFillColor(INK)
            c.drawString(MARGIN + 26, y - 8, titulo)
            pag = str(pagina_de(num))
            c.setFont('DejaVuSans', 9)
            c.setFillColor(MUTED)
            c.drawRightString(W - MARGIN, y - 8, pag)
            # la linea de puntos entre el titulo y el numero de pagina
            x0 = MARGIN + 26 + stringWidth(titulo, 'DejaVuSans-Bold', 10.2) + 8
            x1 = W - MARGIN - stringWidth(pag, 'DejaVuSans', 9) - 8
            c.setStrokeColor(RULE)
            c.setLineWidth(0.8)
            c.setDash(1, 3)
            c.line(x0, y - 8, x1, y - 8)
            c.setDash()
            y -= fila
        y -= 12

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, '2')
    c.showPage()


def _hojas_tema(num):
    tema = TEMAS[num]
    cap_n, cap = capitulo_de(num)
    kicker = 'Pekes · capítulo %d · %s' % (cap_n, cap)
    p0 = pagina_de(num)
    titulo = tema['titulo']

    teo = dict(tema['teoria'], kicker=kicker, titulo=titulo, page_num=p0,
               esquina='Tema %d · teoría' % num)
    pia = dict(tema['piano'], kicker=kicker, titulo=titulo, page_num=p0 + 1,
               esquina='Tema %d · al piano' % num, time_sig=(4, 4), key_sig=None,
               gap=tema['piano'].get('gap', 8.2))
    fic = dict(tema['ficha'], kicker=kicker, titulo=titulo, page_num=p0 + 2,
               esquina='Tema %d · ficha para casa' % num)
    return [('teoria', lambda c: build_teoria(c, teo)),
            ('piano', lambda c: build_piano(c, pia)),
            ('ficha', lambda c: build_deberes(c, fic))]


def construir(nombre='Libro_Pekes_muestra.pdf'):
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, nombre)
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('El Cuaderno del Pianista · Pekes')
    del portada.NO_CABEN[:]
    _portada(c)
    _indice(c)
    finales = []
    for num in sorted(TEMAS):
        for etq, fn in _hojas_tema(num):
            finales.append(('tema %d %s' % (num, etq), fn(c)))
    c.save()
    return ruta, finales


def main(argv):
    ruta, finales = construir()
    print('Libro Pekes · %s' % os.path.basename(ruta))
    for etq, y in finales:
        print('  %-18s y final = %s' % (etq, None if y is None else round(y, 1)))
    if portada.NO_CABEN:
        print('NO CABEN:', portada.NO_CABEN)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
