# -*- coding: utf-8 -*-
"""CURSO PEKES — el dosier de iniciacion de 6-8 anos, reconstruido con el
   motor del proyecto a partir del "NIVEL PEKES" que el cliente ya tenia en
   Canva (ver `pekes_datos.py` para el porque y los bugs que se corrigen).

   Lo que pidio el cliente, literal: orden logico de aprendizaje, comprimir
   de 3 hojas por clase a 1, y "profesionalizarlo, llevarlo a un dosier de
   tclase". Esto es eso: UNA hoja A4 por semana (44 semanas), con sus tres
   bloques (Teoria / Ejercicio / Juego Musical) dentro de la misma hoja,
   agrupadas visualmente en 7 bloques tematicos con su propio color para que
   el peke vea el curso avanzar.

   Uso:  python3 build_pekes.py
"""
import os
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from notation import draw_staff, draw_clef, draw_barline, BLEED_SAFE          # noqa: E402
from portada import W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, RULE, \
                    INK, MUTED, ACCENT, _fit, _wrap, NO_CABEN                  # noqa: E402
from juegos_comun import figura_en_caja, simbolo                              # noqa: E402
from pekes_datos import CLASES, BLOQUES, bloque_de                           # noqa: E402
import pekes_dibujos                                                         # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'pekes')

# --------------------------------------------------------------------------
# presupuesto vertical, de arriba a abajo (ver cabecera del modulo para el
# porque de estos numeros concretos)
# --------------------------------------------------------------------------
Y_TOP = H - MARGIN
ALTO_DIAGRAMA_TEORIA = 148
ALTO_EJERCICIO = 232
ALTO_JUEGO = 104


def _tinte(color, frac):
    """Un color mezclado hacia blanco -- para fondos suaves de la banda de
       bloque, sin tocar `notation.py` ni inventar una paleta nueva."""
    r, g, b = color.red, color.green, color.blue
    return HexColor('#%02x%02x%02x' % (
        int(255 - (255 - r * 255) * frac),
        int(255 - (255 - g * 255) * frac),
        int(255 - (255 - b * 255) * frac)))


# --------------------------------------------------------------------------
# cabecera de cada hoja: banda de bloque, kicker, tira de avance, titulo
# --------------------------------------------------------------------------
def _cabecera(c, clase):
    bloque = bloque_de(clase['n'])
    color = bloque['color']

    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(color)
    c.rect(BLEED_SAFE, H - 6 - BLEED_SAFE, W - 2 * BLEED_SAFE, 6, fill=1, stroke=0)

    y = Y_TOP - 2
    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(color)
    c.drawString(MARGIN, y, ('BLOQUE %d · %s' % (bloque['n'], bloque['nombre'])).upper())
    c.setFont('DejaVuSans', 8.2)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, 'CURSO PEKES · SEMANA %d/44' % clase['n'])
    y -= 14

    _tira_avance(c, MARGIN, y, CONTENT_W, clase['n'])
    y -= 22

    c.setFont('DejaVuSerif-Bold', 20)
    c.setFillColor(NAVY)
    titulo = clase['teoria']['titulo']
    size = _fit(titulo, 'DejaVuSerif-Bold', 20, CONTENT_W, floor=14)
    c.setFont('DejaVuSerif-Bold', size)
    c.drawString(MARGIN, y - size * 0.78, titulo)
    y -= size * 0.78 + 22

    y = _wrap(c, clase['teoria']['texto'], MARGIN, y, 'DejaVuSans', 10, CONTENT_W, 13.2, INK)
    return y - 8


def _tira_avance(c, x, y, w, actual):
    n = 44
    paso = w / float(n)
    r = min(paso * 0.32, 3.1)
    for i in range(n):
        semana = i + 1
        cx = x + (i + 0.5) * paso
        col = bloque_de(semana)['color']
        if semana < actual:
            c.setFillColor(col)
            c.circle(cx, y, r, fill=1, stroke=0)
        elif semana == actual:
            c.setFillColor(col)
            c.circle(cx, y, r * 1.7, fill=1, stroke=0)
        else:
            c.setStrokeColor(RULE)
            c.setLineWidth(0.6)
            c.circle(cx, y, r, fill=0, stroke=1)


# --------------------------------------------------------------------------
# seccion TEORIA: ya la cabecera escribe titulo+texto; aqui solo el dibujo
# --------------------------------------------------------------------------
def _seccion_teoria(c, y, clase):
    dibujo = clase['teoria']['dibujo']
    if dibujo is None:
        return y
    clave, params = dibujo
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.roundRect(MARGIN, y - ALTO_DIAGRAMA_TEORIA, CONTENT_W, ALTO_DIAGRAMA_TEORIA, 8, fill=0, stroke=1)
    pekes_dibujos.dibujar(c, clave, MARGIN + 6, y - ALTO_DIAGRAMA_TEORIA + 6,
                          CONTENT_W - 12, ALTO_DIAGRAMA_TEORIA - 12, params)
    return y - ALTO_DIAGRAMA_TEORIA - 14


# --------------------------------------------------------------------------
# seccion EJERCICIO
# --------------------------------------------------------------------------
def _etiqueta_seccion(c, y, texto, color):
    c.setFont('DejaVuSans-Bold', 9.2)
    c.setFillColor(color)
    c.drawString(MARGIN, y, texto.upper())
    tw = stringWidth(texto.upper(), 'DejaVuSans-Bold', 9.2)
    c.setStrokeColor(color)
    c.setLineWidth(1.2)
    c.line(MARGIN, y - 4, MARGIN + tw, y - 4)
    return y - 17


def _seccion_ejercicio(c, y, clase, bloque_color):
    y = _etiqueta_seccion(c, y, 'Ejercicio', bloque_color)
    ej = clase['ejercicio']
    c.setFont('DejaVuSans-Bold', 11.3)
    c.setFillColor(NAVY)
    titulo = {'numera': 'Numera y escribe', 'colorea': 'Colorea', 'escribe_letra': 'Escribe',
             'rodea': 'Rodea', 'vf': 'Verdadero o falso', 'cuenta': 'Cuenta los tiempos',
             'crea': 'Crea', 'test': 'El gran test', 'diploma': 'La búsqueda'}.get(ej['tipo'], 'Ejercicio')
    c.drawString(MARGIN, y - 10, titulo)
    y -= 24
    y = _wrap(c, ej['instrucciones'], MARGIN, y, 'DejaVuSans', 9.3, CONTENT_W, 12.2, MUTED)
    y -= 10

    top = y
    bottom = top - ALTO_EJERCICIO
    c.setFillColor(_tinte(bloque_color, 0.06))
    c.roundRect(MARGIN, bottom, CONTENT_W, ALTO_EJERCICIO, 8, fill=1, stroke=0)
    _RENDER_EJERCICIO[ej['tipo']](c, MARGIN + 14, top - 10, CONTENT_W - 28, ALTO_EJERCICIO - 20, ej, bloque_color)
    return bottom - 16


def _render_numera(c, x, y_top, w, h, ej, color):
    items = ej['items']
    n = len(items)
    fila_h = min(h / float(n), 24)
    for i, nombre in enumerate(items):
        fy = y_top - i * fila_h - fila_h * 0.5
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(1.0)
        c.rect(x, fy - 7, 20, 14, fill=0, stroke=1)
        c.setFont('DejaVuSans', 9.6)
        c.setFillColor(INK)
        c.drawString(x + 30, fy - 3.3, nombre)


def _render_colorea(c, x, y_top, w, h, ej, color):
    if 'figuras' in ej:
        claves = ej['figuras']
        paso = w / float(len(claves))
        for i, clave in enumerate(claves):
            cx = x + (i + 0.5) * paso
            cy = y_top - h * 0.45
            lado = min(paso * 0.6, h * 0.7)
            figura_en_caja(c, cx, cy, lado * 0.6, lado, clave, None)
        c.setFont('DejaVuSans', 8.6)
        c.setFillColor(MUTED)
        c.drawCentredString(x + w / 2.0, y_top - h + 12,
                            'colorea cada figura y cuenta los tiempos dando palmas')
    else:
        nombre = ej.get('nombre', '')
        from pekes_datos import NOTAS_COLOR
        pitch, col = NOTAS_COLOR[nombre] if nombre in NOTAS_COLOR else (None, color)
        c.setFont('DejaVuSans', 9.4)
        c.setFillColor(MUTED)
        c.drawCentredString(x + w / 2.0, y_top - h * 0.5,
                            'colorea la tecla y la nota %s del color de arriba' % nombre.capitalize())


def _render_escribe_letra(c, x, y_top, w, h, ej, color):
    filas = ej['filas']
    n = len(filas)
    fila_h = min(h / float(n), 26)
    for i, texto in enumerate(filas):
        fy = y_top - i * fila_h - fila_h * 0.5
        c.setFont('DejaVuSans', 9.4)
        c.setFillColor(INK)
        c.drawString(x, fy - 3.3, texto)
        bx = x + w - 120
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(1.0)
        for k in range(4):
            c.rect(bx + k * 26, fy - 9, 20, 18, fill=0, stroke=1)


def _render_rodea(c, x, y_top, w, h, ej, color):
    items = ej['items']
    n = len(items)
    cols = min(n, 4)
    filas_n = (n + cols - 1) // cols
    cw = w / float(cols)
    ch = h / float(filas_n)
    for i, texto in enumerate(items):
        col, fil = i % cols, i // cols
        cx = x + col * cw + cw / 2.0
        cy = y_top - fil * ch - ch / 2.0
        c.setStrokeColor(color)
        c.setLineWidth(1.3)
        c.ellipse(cx - cw * 0.42, cy - ch * 0.30, cx + cw * 0.42, cy + ch * 0.30, fill=0, stroke=1)
        size = _fit(texto, 'DejaVuSans', 8.6, cw * 0.78, floor=6.5)
        c.setFont('DejaVuSans', size)
        c.setFillColor(INK)
        c.drawCentredString(cx, cy - 3, texto)


def _render_vf(c, x, y_top, w, h, ej, color):
    items = ej['items']
    n = len(items)
    fila_h = min(h / float(n), 26)
    for i, texto in enumerate(items):
        fy = y_top - i * fila_h
        c.setFont('DejaVuSans', 9.0)
        c.setFillColor(INK)
        yy = _wrap(c, texto, x, fy - 9, 'DejaVuSans', 9.0, w - 90, 11.5, INK)
        for k, letra in enumerate(('V', 'F')):
            bx = x + w - 70 + k * 34
            c.setStrokeColor(NAVY_SOFT)
            c.setLineWidth(1.0)
            c.rect(bx, fy - 11, 22, 16, fill=0, stroke=1)
            c.setFont('DejaVuSans-Bold', 8)
            c.setFillColor(MUTED)
            c.drawCentredString(bx + 11, fy - 20, letra)


def _render_cuenta(c, x, y_top, w, h, ej, color):
    claves = ej['figuras']
    paso = w / float(len(claves))
    for i, clave in enumerate(claves):
        cx = x + (i + 0.5) * paso
        cy = y_top - h * 0.5
        lado = min(paso * 0.55, h * 0.62)
        figura_en_caja(c, cx, cy, lado * 0.55, lado, clave, NAVY)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.rect(cx - lado * 0.28, y_top - h + 8, lado * 0.56, 16, fill=0, stroke=1)


def _render_crea(c, x, y_top, w, h, ej, color):
    n_compases = ej.get('compases', 0)
    if not n_compases:
        c.setFont('DejaVuSans', 9.4)
        c.setFillColor(MUTED)
        c.drawCentredString(x + w / 2.0, y_top - h * 0.5, 'completa la ficha de arriba')
        return
    gap = min(h * 0.26, 13.0)
    top_y = y_top - h * 0.25
    x0 = x + 6
    ys = draw_staff(c, x0, top_y, w - 12, gap=gap)
    draw_clef(c, x0 + gap * 0.3, ys[-1], gap, clef='treble')
    paso = (w - 12 - gap * 5) / float(n_compases)
    for i in range(n_compases + 1):
        bx = x0 + gap * 5 + i * paso
        draw_barline(c, bx, ys[0], ys[-1], final=(i == n_compases))


def _render_test(c, x, y_top, w, h, ej, color):
    partes = ej['partes']
    y = y_top
    alto_parte = h / float(len(partes))
    for parte in partes:
        c.setFont('DejaVuSans-Bold', 9.4)
        c.setFillColor(color)
        c.drawString(x, y - 10, parte['pregunta'])
        y -= 20
        items = parte['items']
        if parte['tipo'] == 'vf':
            fila_h = min((alto_parte - 20) / float(len(items)), 15)
            for texto in items:
                c.setFont('DejaVuSans', 8.4)
                c.setFillColor(INK)
                c.drawString(x + 8, y - 8, '· ' + texto)
                for k, letra in enumerate(('V', 'F')):
                    bx = x + w - 56 + k * 26
                    c.setStrokeColor(NAVY_SOFT)
                    c.rect(bx, y - 11, 18, 13, fill=0, stroke=1)
                y -= fila_h
        else:
            paso = w / float(len(items))
            for i, nombre in enumerate(items):
                cx = x + i * paso + paso / 2.0
                c.setFont('DejaVuSans', 8.4)
                c.setFillColor(INK)
                c.drawCentredString(cx, y - 8, nombre)
                c.setStrokeColor(RULE)
                c.rect(cx - paso * 0.3, y - 26, paso * 0.6, 14, fill=0, stroke=1)
            y -= alto_parte - 20
        y -= 4


def _render_diploma(c, x, y_top, w, h, ej, color):
    pruebas = ej['pruebas']
    fila_h = min(h / float(len(pruebas)), 20)
    for i, texto in enumerate(pruebas):
        fy = y_top - i * fila_h
        c.setStrokeColor(color)
        c.setLineWidth(1.2)
        c.rect(x, fy - 11, 14, 14, fill=0, stroke=1)
        c.setFont('DejaVuSans', 9.0)
        c.setFillColor(INK)
        c.drawString(x + 22, fy - 7, '%d. %s' % (i + 1, texto))


_RENDER_EJERCICIO = {
    'numera': _render_numera, 'colorea': _render_colorea,
    'escribe_letra': _render_escribe_letra, 'rodea': _render_rodea,
    'vf': _render_vf, 'cuenta': _render_cuenta, 'crea': _render_crea,
    'test': _render_test, 'diploma': _render_diploma,
}


# --------------------------------------------------------------------------
# seccion JUEGO MUSICAL
# --------------------------------------------------------------------------
def _seccion_juego(c, y, clase, bloque_color):
    j = clase['juego']
    top = y
    bottom = top - ALTO_JUEGO
    c.setFillColor(bloque_color)
    c.roundRect(MARGIN, bottom, CONTENT_W, ALTO_JUEGO, 8, fill=1, stroke=0)
    simbolo(c, MARGIN + 26, (top + bottom) / 2.0, 13, 'calderon', white)
    c.setFont('DejaVuSans-Bold', 9.4)
    c.setFillColor(white)
    c.drawString(MARGIN + 50, top - 18, 'JUEGO MUSICAL · ' + j['titulo'])
    _wrap(c, j['texto'], MARGIN + 50, top - 34, 'DejaVuSans', 9.0,
          CONTENT_W - 70, 12.0, HexColor('#E4E8EE'))
    return bottom - 20


# --------------------------------------------------------------------------
# pie de hoja
# --------------------------------------------------------------------------
def _pie(c, clase):
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, 30, 'NOMBRE')
    c.line(MARGIN + 40, 29, MARGIN + CONTENT_W * 0.55, 29)
    c.drawString(MARGIN + CONTENT_W * 0.60, 30, 'FECHA')
    c.line(MARGIN + CONTENT_W * 0.60 + 34, 29, W - MARGIN, 29)
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2.0, 16, 'El Cuaderno del Pianista · T-Clas')
    c.drawRightString(W - MARGIN, 16, 'Semana %d' % clase['n'])


def _hoja_semana(c, clase):
    bloque_color = bloque_de(clase['n'])['color']
    y = _cabecera(c, clase)
    y = _seccion_teoria(c, y, clase)
    y = _seccion_ejercicio(c, y, clase, bloque_color)
    _seccion_juego(c, y, clase, bloque_color)
    _pie(c, clase)
    c.showPage()


# --------------------------------------------------------------------------
# portada
# --------------------------------------------------------------------------
def _portada(c):
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('DejaVuSans-Bold', 9.5)
    c.drawCentredString(W / 2.0, H - 140, 'EL CUADERNO DEL PIANISTA · T-CLAS')
    simbolo(c, W / 2.0, H - 330, 70, 'clave_sol', white)
    c.setFont('DejaVuSerif-Bold', 40)
    c.drawCentredString(W / 2.0, H - 420, 'Curso Pekes')
    c.setFont('DejaVuSans', 13)
    c.setFillColor(HexColor('#C3CEDB'))
    c.drawCentredString(W / 2.0, H - 448, 'Primer año de piano · 6 a 8 años · 44 semanas')
    for i, b in enumerate(BLOQUES):
        yy = H - 520 - i * 24
        c.setFillColor(b['color'])
        c.circle(W / 2.0 - 150, yy, 5, fill=1, stroke=0)
        c.setFont('DejaVuSans', 10.5)
        c.setFillColor(white)
        c.drawString(W / 2.0 - 135, yy - 4, 'BLOQUE %d · %s (semanas %d-%d)' %
                    (b['n'], b['nombre'], b['desde'], b['hasta']))
    c.setStrokeColor(HexColor('#3C4A5E'))
    c.line(W / 2.0 - 90, 120, W / 2.0 + 90, 120)
    c.setFont('DejaVuSans', 9)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2.0, 100, 'NOMBRE DEL ALUMNO')
    c.showPage()


# --------------------------------------------------------------------------
def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'Curso_Pekes.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('Curso Pekes · El Cuaderno del Pianista')
    _portada(c)
    for clase in CLASES:
        _hoja_semana(c, clase)
    c.save()
    return ruta, len(CLASES) + 1


def main(argv):
    ruta, paginas = construir()
    print('Curso Pekes · %s · %d páginas' % (os.path.basename(ruta), paginas))
    if NO_CABEN:
        print('AVISO: %d textos no caben en su caja:' % len(NO_CABEN))
        for t in NO_CABEN:
            print('  ', t)
    return 1 if NO_CABEN else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
