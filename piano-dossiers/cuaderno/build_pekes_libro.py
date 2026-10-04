# -*- coding: utf-8 -*-
"""EL LIBRO DE PEKES — version 2, de cero, en blanco y negro.

   Bloque de MUESTRA: construye solo el Tema 1 (3 hojas: teoria, al piano,
   ficha) para que el cliente vea el enfoque nuevo antes de escribir el
   resto del curso. Ver `pekes_libro_datos.py` para el porque del cambio
   de estructura.

   Uso:  python3 build_pekes_libro.py
"""
import os
import sys

from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from notation import BLEED_SAFE                                               # noqa: E402
from portada import W, H, MARGIN, CONTENT_W, RULE, _fit                       # noqa: E402
import pekes_libro_dibujos as pekes_dibujos                                   # noqa: E402
import pekes_mascota as mascota                                               # noqa: E402
from pekes_libro_datos import TEMAS                                           # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'pekes')

# El Musol Misol real, recortado del Canva original del cliente y pasado a
# gris (el cliente lo pidio explicito: "el musol misol lo puedes coger del
# canva y ponerlo directamente porque ya se veia bien" -- su dibujo vectorial
# desde cero no llegaba a ese nivel). Dos poses: normal (con birrete, para
# explicar) y happy (cantando, para portadas/celebraciones).
_ASSETS_OWL = os.path.join(HERE, '..', 'assets', 'pekes_owl')
from reportlab.lib.utils import ImageReader                                   # noqa: E402
_OWL_IMG = {
    'normal': ImageReader(os.path.join(_ASSETS_OWL, 'owl_normal.png')),
    'happy': ImageReader(os.path.join(_ASSETS_OWL, 'owl_happy.png')),
}


def _dibujar_owl(c, cx, cy_base, alto, pose='normal'):
    """Dibuja a Misol centrado en cx, con la base (las patas) en cy_base."""
    img = _OWL_IMG[pose]
    iw, ih = img.getSize()
    w = alto * iw / float(ih)
    c.drawImage(img, cx - w / 2.0, cy_base, w, alto, mask='auto')
    return w

INK = HexColor('#1A1A1A')
PAPER = white
TITLE_FONT = 'WorkSans-ExtraBold'
BODY_FONT = 'WorkSans-Regular'
BODY_BOLD = 'WorkSans-SemiBold'
_FONTS_DIR = os.path.join(HERE, '..', 'assets', 'fonts_juegos')
from reportlab.pdfbase.ttfonts import TTFont                                   # noqa: E402
from reportlab.pdfbase.pdfmetrics import registerFont                         # noqa: E402
for _n, _f in ((TITLE_FONT, 'WorkSans-ExtraBold.ttf'), (BODY_FONT, 'WorkSans-Regular.ttf'),
              (BODY_BOLD, 'WorkSans-SemiBold.ttf')):
    try:
        registerFont(TTFont(_n, os.path.join(_FONTS_DIR, _f)))
    except Exception:
        pass

PAGINA_W, PAGINA_H = 1, 1  # placeholder, no se usa


def _wrap(c, text, x, y, font, size, max_w, leading, color=INK):
    c.setFont(font, size)
    c.setFillColor(color)
    line = ''
    for word in text.split(' '):
        test = (line + ' ' + word).strip()
        if stringWidth(test, font, size) <= max_w:
            line = test
        else:
            c.drawString(x, y, line)
            y -= leading
            line = word
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def _fondo(c):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def _notita(c, cx, cy, s):
    """Una corchea pequena, el motivo decorativo que sustituye a la barra
       de color de los dosieres normales -- aqui todo es blanco y negro."""
    c.saveState()
    c.setFillColor(INK)
    c.circle(cx, cy, s * 0.5, fill=1, stroke=0)
    c.setStrokeColor(INK)
    c.setLineWidth(s * 0.22)
    c.line(cx + s * 0.46, cy, cx + s * 0.46, cy + s * 1.7)
    p = c.beginPath()
    p.moveTo(cx + s * 0.46, cy + s * 1.7)
    p.curveTo(cx + s * 1.3, cy + s * 1.5, cx + s * 1.25, cy + s * 0.9,
             cx + s * 0.55, cy + s * 1.0)
    c.setFillColor(INK)
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()


def _cabecera(c, tema, etiqueta):
    _fondo(c)
    y = H - MARGIN

    # fila decorativa de notitas, en vez de la barra de color de siempre
    paso = 26
    n = int(CONTENT_W // paso)
    x0 = MARGIN + (CONTENT_W - (n - 1) * paso) / 2.0
    for i in range(n):
        _notita(c, x0 + i * paso, y + 6, 3.1)

    y -= 26
    c.setFont(BODY_BOLD, 9.2)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, ('CAPÍTULO · ' + tema['capitulo']).upper())

    badge_w = stringWidth(etiqueta.upper(), TITLE_FONT, 10.5) + 28
    c.setFillColor(INK)
    c.roundRect(W - MARGIN - badge_w, y - 6, badge_w, 20, 10, fill=1, stroke=0)
    c.setFont(TITLE_FONT, 10.5)
    c.setFillColor(PAPER)
    c.drawCentredString(W - MARGIN - badge_w / 2.0, y - 0.5, etiqueta.upper())
    y -= 34

    size = _fit(tema['titulo'], TITLE_FONT, 29, CONTENT_W, floor=18)
    c.setFont(TITLE_FONT, size)
    c.setFillColor(INK)
    c.drawString(MARGIN, y - size * 0.75, tema['titulo'])
    y -= size * 0.75 + 16

    c.setStrokeColor(INK)
    c.setLineWidth(2.2)
    dash_w, gap_w, xx = 9, 7, MARGIN
    while xx < MARGIN + CONTENT_W:
        xend = min(xx + dash_w, MARGIN + CONTENT_W)
        c.line(xx, y, xend, y)
        xx += dash_w + gap_w
    y -= 26
    return y


def _bloque_misol(c, y, texto, titulo=None, alto=118, pose='normal'):
    """Misol a la izquierda, su globo a la derecha -- la fila que abre el
       contenido de cada una de las tres hojas."""
    owl_w = _dibujar_owl(c, MARGIN + alto * 0.42, y - alto, alto, pose=pose)
    bx = MARGIN + owl_w + 18
    bw = CONTENT_W - owl_w - 18
    mascota.globo_texto(c, bx, y - alto, bw, alto, texto,
                        cola_x=bx + 26, cola_abajo=False, titulo=titulo,
                        font=BODY_FONT, font_bold=BODY_BOLD, size=10.6, leading=14.2)
    return y - alto - 22


def _pie(c, num_pagina, etiqueta_pie=''):
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(MARGIN, 34, W - MARGIN, 34)
    c.setFont(BODY_FONT, 8.4)
    c.setFillColor(HexColor('#6B6B6B'))
    c.drawString(MARGIN, 20, etiqueta_pie or 'El Cuaderno del Pianista · T-Clas')
    c.drawRightString(W - MARGIN, 20, str(num_pagina))


# --------------------------------------------------------------------------
# HOJA 1 · TEORÍA
# --------------------------------------------------------------------------
def pagina_teoria(c, tema, num_pagina):
    t = tema['teoria']
    y = _cabecera(c, tema, 'Teoría')
    y = _bloque_misol(c, y, t['intro'], titulo='MUSOL MISOL DICE...')

    y = _wrap(c, t['explicacion'], MARGIN, y, BODY_FONT, 11.6, CONTENT_W, 16.4)
    y -= 18

    alto_dibujo = 300
    c.setStrokeColor(INK)
    c.setLineWidth(2.2)
    c.roundRect(MARGIN, y - alto_dibujo, CONTENT_W, alto_dibujo, 16, fill=0, stroke=1)
    clave, params = t['dibujo']
    pekes_dibujos.dibujar(c, clave, MARGIN + 16, y - alto_dibujo + 16,
                          CONTENT_W - 32, alto_dibujo - 32, params)
    y -= alto_dibujo + 20

    if t.get('dato'):
        c.setStrokeColor(INK)
        c.setLineWidth(1.6)
        c.setDash(2, 3)
        c.roundRect(MARGIN, y - 54, CONTENT_W, 54, 12, fill=0, stroke=1)
        c.setDash()
        c.setFont(BODY_BOLD, 9.6)
        c.setFillColor(INK)
        c.drawString(MARGIN + 16, y - 21, '¿SABÍAS QUÉ...?')
        _wrap(c, t['dato'], MARGIN + 16, y - 37, BODY_FONT, 9.8, CONTENT_W - 32, 13.2)

    _pie(c, num_pagina)
    c.showPage()


# --------------------------------------------------------------------------
# HOJA 2 · AL PIANO
# --------------------------------------------------------------------------
def pagina_piano(c, tema, num_pagina):
    p = tema['piano']
    y = _cabecera(c, tema, 'Al piano')
    y = _bloque_misol(c, y, p['intro'], titulo='MUSOL MISOL DICE...')

    pasos = p['pasos']
    n = len(pasos)
    alto_disponible = y - 150
    fila_h = min(alto_disponible / n, 78)
    for i, paso in enumerate(pasos):
        fy = y - i * fila_h
        r = 17
        c.setFillColor(INK)
        c.circle(MARGIN + r, fy - r, r, fill=1, stroke=0)
        c.setFont(TITLE_FONT, 15)
        c.setFillColor(PAPER)
        c.drawCentredString(MARGIN + r, fy - r - 5.2, str(i + 1))
        tx = MARGIN + r * 2 + 16
        _wrap(c, paso, tx, fy - 8, BODY_FONT, 11.2, CONTENT_W - r * 2 - 16, 15.2)
        if i < n - 1:
            c.setStrokeColor(RULE)
            c.setLineWidth(1.0)
            c.setDash(1, 3)
            c.line(MARGIN + r, fy - 2 * r - 4, MARGIN + r, fy - fila_h + 6)
            c.setDash()
    y -= n * fila_h + 14

    if p.get('consejo'):
        c.setFillColor(INK)
        c.roundRect(MARGIN, y - 56, CONTENT_W, 56, 14, fill=1, stroke=0)
        c.setFont(BODY_BOLD, 9.6)
        c.setFillColor(PAPER)
        c.drawString(MARGIN + 18, y - 23, 'CONSEJO DE MUSOL MISOL')
        _wrap(c, p['consejo'], MARGIN + 18, y - 39, BODY_FONT, 9.8, CONTENT_W - 36, 13.2, color=PAPER)

    _pie(c, num_pagina)
    c.showPage()


# --------------------------------------------------------------------------
# HOJA 3 · FICHA
# --------------------------------------------------------------------------
def pagina_ficha(c, tema, num_pagina):
    f = tema['ficha']
    y = _cabecera(c, tema, 'Ficha')

    c.setFont(BODY_BOLD, 8.6)
    c.setFillColor(INK)
    c.drawString(MARGIN, y, 'NOMBRE')
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(MARGIN + 44, y - 2, MARGIN + 230, y - 2)
    c.drawString(MARGIN + 250, y, 'FECHA')
    c.line(MARGIN + 288, y - 2, MARGIN + CONTENT_W, y - 2)
    y -= 26

    y = _bloque_misol(c, y, f['intro'], titulo='MUSOL MISOL DICE...', alto=96)

    alto_dibujo = 240
    c.setStrokeColor(INK)
    c.setLineWidth(2.2)
    c.roundRect(MARGIN, y - alto_dibujo, CONTENT_W, alto_dibujo, 16, fill=0, stroke=1)
    clave, params = f['dibujo']
    pekes_dibujos.dibujar(c, clave, MARGIN + 16, y - alto_dibujo + 16,
                          CONTENT_W - 32, alto_dibujo - 32, params)
    y -= alto_dibujo + 20

    items = f['items']
    cols = 2
    filas_n = (len(items) + cols - 1) // cols
    col_w = CONTENT_W / cols
    fila_h = 30
    for i, nombre in enumerate(items):
        col, fil = i % cols, i // cols
        fx = MARGIN + col * col_w
        fy = y - fil * fila_h
        c.setStrokeColor(INK)
        c.setLineWidth(1.4)
        c.rect(fx, fy - 20, 26, 20, fill=0, stroke=1)
        c.setFont(BODY_FONT, 10.4)
        c.setFillColor(INK)
        c.drawString(fx + 34, fy - 14.5, nombre)
    y -= filas_n * fila_h + 14

    if f.get('reto'):
        c.setFont(BODY_BOLD, 9.6)
        c.setFillColor(INK)
        _wrap(c, '★ ' + f['reto'], MARGIN, y, BODY_FONT, 9.8, CONTENT_W, 13.2)

    _pie(c, num_pagina)
    c.showPage()


def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'Libro_Pekes_muestra.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('El libro de Pekes · muestra')
    pag = 1
    for tema in TEMAS:
        pagina_teoria(c, tema, pag); pag += 1
        pagina_piano(c, tema, pag); pag += 1
        pagina_ficha(c, tema, pag); pag += 1
    c.save()
    return ruta, pag - 1


def main(argv):
    ruta, paginas = construir()
    print('Libro Pekes (muestra) · %s · %d páginas' % (os.path.basename(ruta), paginas))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
