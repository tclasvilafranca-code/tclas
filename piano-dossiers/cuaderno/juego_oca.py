# -*- coding: utf-8 -*-
"""OCA MUSICAL — el tablero de toda la vida, con las casillas vestidas de
   música.

   POR QUÉ ASÍ. Decisión del cliente: estos juegos son para el final de
   clase, para romper la dinámica y pasarlo bien — no para seguir en clase
   con otro disfraz. Así que aquí NO hay cartas de reto ni preguntas: es la
   Oca de siempre, con el mismo tablero de 63 casillas y las mismas siete
   casillas especiales de siempre, cada una vestida con un signo musical
   real. La diversión es la de la Oca — el azar, el "otra vez a la casilla
   1" — y la música es la piel, no una prueba.

   LAS CASILLAS, con su equivalencia clásica entre paréntesis:

     CORCHEA          (oca)       salta a la siguiente y tira otra vez
     LIGADURA          (puente)    te lleva a la otra ligadura
     CALDERÓN          (posada)    pierdes un turno — la nota se alarga
     SILENCIO           (pozo)      quieto hasta que otro caiga contigo
     BECUADRO           (laberinto) deshace lo andado, retrocedes
     SILENCIO DE REDONDA (cárcel)   el silencio más largo: dos turnos
     DA CAPO            (calavera)  vuelves derecho a la salida
     FINE               (meta)      hay que caer justo para ganar

   Silencio y becuadro son LOS MISMOS símbolos que en el UNO musical
   (`juegos_comun.simbolo`): un alumno que ha aprendido a leer una baraja
   lee el tablero sin que nadie le explique nada — es la norma de la
   colección.

   Tablero: cuadrícula de 9×7 (=63) recorrida en espiral desde la esquina
   superior izquierda hasta el centro, que es donde cae la casilla 63
   (FINE) — el mismo gesto visual de "el camino se enrosca hasta la meta"
   que tiene una Oca de verdad.

   Uso:  python3 juego_oca.py
"""
import os
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas as rl_canvas

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from juegos_comun import (W, H, NAVY, CREAM, INK, MUTED, ACCENT, RULE,        # noqa: E402
                          PALOS, COLOR_PALO, FORMA_PALO, forma, simbolo,
                          logo_tclas, portada_juego)
from portada import _wrap                                                    # noqa: E402
from notation import BLEED_SAFE                                              # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

# --------------------------------------------------------------------------
# El tablero clásico: 9x7 casillas, espiral hacia el centro
# --------------------------------------------------------------------------
COLS, ROWS = 9, 7
BOARD_W, BOARD_H = H, W          # A4 apaisada: 841.89 x 595.276

# Las posiciones son las de la Oca de toda la vida (13 ocas, cada 4-5
# casillas; puentes en 6 y 12; posada 19; pozo 31; laberinto 42; carcel 52;
# calavera 58; meta 63) — no las hemos inventado, para que quien conoce el
# juego real la reconozca de un vistazo.
CORCHEAS = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
LIGADURAS = {6: 12, 12: 6}
CALDERON = 19
SILENCIO = 31
BECUADRO = 42
BECUADRO_DESTINO = 30
CARCEL = 52          # silencio de redonda: 2 turnos
DACAPO = 58
FINE = 63

COLOR_TIPO = {
    'corchea':          HexColor('#4A6741'),
    'ligadura':         HexColor('#2C4C6B'),
    'calderon':         HexColor('#A9762F'),
    'silencio':         NAVY,
    'becuadro':         HexColor('#B4462F'),
    'redonda_espera':   NAVY,
    'dacapo':           HexColor('#6E2A1F'),
    'fine':             ACCENT,
}

NOMBRE_TIPO = {
    'corchea':        'CORCHEA',
    'ligadura':       'LIGADURA',
    'calderon':       'CALDERÓN',
    'silencio':       'SILENCIO',
    'becuadro':       'BECUADRO',
    'redonda_espera': 'SILENCIO DE REDONDA',
    'dacapo':         'DA CAPO',
    'fine':           'FINE',
}

DETALLE = {
    'corchea':        '(la "oca" de siempre) Saltas a la siguiente corchea '
                       'y tiras otra vez — "de corchea en corchea, y tiro '
                       'porque me toca".',
    'ligadura':       '(el "puente") Te lleva directo a la otra ligadura '
                       'del tablero, en cualquier sentido.',
    'calderon':       '(la "posada") La nota se alarga: pierdes un turno.',
    'silencio':       '(el "pozo") Te quedas callado ahí hasta que otro '
                       'jugador caiga en la misma casilla — entonces te '
                       'libera y se queda él.',
    'becuadro':       '(el "laberinto") Un becuadro deshace lo andado: '
                       'retrocedes hasta la casilla %d.' % BECUADRO_DESTINO,
    'redonda_espera': '(la "cárcel") El silencio más largo que hay: te '
                       'quedas DOS turnos completos sin moverte.',
    'dacapo':         '(la "calavera") Vuelves derecho a la salida, la '
                       'casilla 1 — se empieza de cero.',
    'fine':           '(la "meta") Hay que caer justo encima. Si el dado '
                       'te hace pasarte, rebotas hacia atrás lo que sobre.',
}


def _tipo_casilla(n):
    if n == FINE:
        return 'fine'
    if n == CALDERON:
        return 'calderon'
    if n == SILENCIO:
        return 'silencio'
    if n == BECUADRO:
        return 'becuadro'
    if n == CARCEL:
        return 'redonda_espera'
    if n == DACAPO:
        return 'dacapo'
    if n in LIGADURAS:
        return 'ligadura'
    if n in CORCHEAS:
        return 'corchea'
    return None


def _espiral(cols, rows):
    """Las posiciones (col, fila) de una cuadricula, en el orden en que las
       recorre una espiral que entra por la esquina superior izquierda y
       se enrosca hacia el centro — el mismo gesto que un tablero de Oca de
       verdad, donde el camino se enrosca hasta Roma."""
    grid = []
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    while top <= bottom and left <= right:
        for x in range(left, right + 1):
            grid.append((x, top))
        top += 1
        for y in range(top, bottom + 1):
            grid.append((right, y))
        right -= 1
        if top <= bottom:
            for x in range(right, left - 1, -1):
                grid.append((x, bottom))
            bottom -= 1
        if left <= right:
            for y in range(bottom, top - 1, -1):
                grid.append((left, y))
            left += 1
    return grid


# --------------------------------------------------------------------------
# La hoja del tablero
# --------------------------------------------------------------------------
def _dibujar_casilla(c, x, y, w, h, numero, alterna):
    tipo = _tipo_casilla(numero)
    if tipo is None:
        fondo = CREAM if alterna else white
        c.setFillColor(fondo)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.6)
        c.rect(x, y, w, h, fill=1, stroke=1)
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(NAVY)
        c.drawString(x + 4, y + h - 12, str(numero))
        if numero == 1:
            c.setFont('DejaVuSans-Bold', 6.0)
            c.setFillColor(HexColor('#4A6741'))
            c.drawCentredString(x + w / 2.0, y + 4, 'SALIDA')
        return
    color = COLOR_TIPO[tipo]
    c.setFillColor(color)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.6)
    c.rect(x, y, w, h, fill=1, stroke=1)
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(white)
    c.drawString(x + 4, y + h - 11, str(numero))
    r = min(w, h) * 0.245
    cy = y + h * 0.56
    simbolo(c, x + w / 2.0, cy, r, tipo, white)
    extra = None
    if tipo == 'ligadura':
        extra = '→%d' % LIGADURAS[numero]
    elif tipo == 'becuadro':
        extra = '→%d' % BECUADRO_DESTINO
    elif tipo == 'dacapo':
        extra = '→1'
    elif tipo == 'redonda_espera':
        extra = '2 turnos'
    if extra:
        c.setFont('DejaVuSans-Bold', 6.4)
        c.setFillColor(white)
        c.drawCentredString(x + w / 2.0, y + 4, extra)


def _hoja_tablero(c):
    c.setPageSize((BOARD_W, BOARD_H))
    c.setFillColor(CREAM)
    c.rect(0, 0, BOARD_W, BOARD_H, fill=1, stroke=0)

    band_h = 42
    c.setFillColor(NAVY)
    c.rect(BLEED_SAFE, BOARD_H - band_h - BLEED_SAFE, BOARD_W - 2 * BLEED_SAFE,
          band_h, fill=1, stroke=0)
    c.setFont('DejaVuSerif-Bold', 19)
    c.setFillColor(white)
    c.drawString(28, BOARD_H - 30, 'Oca musical')
    c.setFont('DejaVuSans', 8.6)
    c.setFillColor(HexColor('#C3CEDB'))
    c.drawString(28, BOARD_H - 30 - 13, 'de corchea en corchea, y tiro porque me toca')
    logo_tclas(c, BOARD_W - 40, BOARD_H - band_h / 2.0, 16)

    margin_x = max(26, BLEED_SAFE + 18)
    margin_top, margin_bottom = band_h + BLEED_SAFE + 14, 20
    gx0 = margin_x
    gy_top = BOARD_H - margin_top
    grid_w = BOARD_W - 2 * margin_x
    grid_h = gy_top - margin_bottom
    cell_w = grid_w / COLS
    cell_h = grid_h / ROWS

    orden = _espiral(COLS, ROWS)

    # el camino: una linea que pasa por el centro de cada casilla en el
    # orden en que se juega, para que la espiral se LEA como un camino y no
    # como una cuadricula suelta. Las casillas se dibujan con un hueco fino
    # entre ellas (ver GAP mas abajo) para que la linea asome por la juntura
    # y se vea de verdad, no solo quede debajo tapada.
    c.saveState()
    c.setStrokeColor(HexColor('#C7BCA6'))
    c.setLineWidth(3.4)
    pts = []
    for (gx, gy) in orden:
        cx = gx0 + (gx + 0.5) * cell_w
        cy = gy_top - (gy + 0.5) * cell_h
        pts.append((cx, cy))
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    c.drawPath(p, fill=0, stroke=1)
    c.restoreState()

    GAP = 1.6
    for idx, (gx, gy) in enumerate(orden):
        numero = idx + 1
        x = gx0 + gx * cell_w
        y = gy_top - (gy + 1) * cell_h
        _dibujar_casilla(c, x + GAP / 2.0, y + GAP / 2.0,
                         cell_w - GAP, cell_h - GAP, numero, (gx + gy) % 2 == 0)

    c.setFont('DejaVuSans', 6.8)
    c.setFillColor(MUTED)
    c.drawCentredString(BOARD_W / 2.0, 8, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()
    c.setPageSize((W, H))


# --------------------------------------------------------------------------
# La hoja de reglas
# --------------------------------------------------------------------------
def reglas():
    return [
        'Cada jugador pone su ficha en la SALIDA (casilla 1) y tira el '
        'dado por turnos.',
        'Avanzas tantas casillas como marque el dado. Si caes en una '
        'casilla normal, no pasa nada: turno del siguiente.',
        'CORCHEA: saltas a la siguiente corchea y tiras otra vez — "de '
        'corchea en corchea, y tiro porque me toca".',
        'LIGADURA: te lleva directo a la otra ligadura del tablero.',
        'CALDERÓN pierdes un turno; SILENCIO te quedas quieto hasta que '
        'otro jugador caiga contigo; el silencio de redonda son DOS '
        'turnos seguidos.',
        'BECUADRO deshace lo andado: retrocedes a la casilla que marca.',
        'DA CAPO te manda derecho a la SALIDA — se empieza de cero.',
        'Para llegar a FINE hay que caer justo encima: si te pasas, '
        'rebotas hacia atrás lo que sobre.',
        'Gana quien llegue primero a FINE.',
    ]


MATERIALES = [
    'El tablero (hoja siguiente), un dado normal y una ficha de color por '
    'jugador — recórtalas de la hoja de fichas.',
    'De 2 a 4 jugadores.',
]


def _hoja_reglas(c):
    return portada_juego(
        c, 'Oca musical', 'El tablero de toda la vida, con las casillas vestidas de música',
        None,
        'Es la Oca de siempre: se tira el dado, se avanza, y las casillas '
        'especiales cambian la partida. Aquí cada casilla especial es un '
        'signo musical real —un silencio, una ligadura, un calderón— pero '
        'la regla es exactamente la misma que ya conoces. Sin preguntas ni '
        'retos: esto es para desconectar, no para seguir en clase.',
        reglas(), MATERIALES)


def _explicar(c, x, y, tipo, ancho):
    _wrap(c, DETALLE[tipo], x, y, 'DejaVuSans', 8.6, ancho, 12.0, INK)


def _hoja_leyenda(c):
    """La chuleta de las ocho casillas especiales, a dos columnas — mismo
       patron que la del UNO musical, para que la coleccion se lea igual."""
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFont('DejaVuSerif-Bold', 22)
    c.setFillColor(NAVY)
    c.drawString(52, H - 78, 'Las casillas especiales')
    c.setFont('DejaVuSans', 10)
    c.setFillColor(MUTED)
    c.drawString(52, H - 98, 'Déjala al lado del tablero las primeras partidas. '
                             'A la tercera ya no hace falta.')
    orden = ['corchea', 'ligadura', 'calderon', 'silencio',
             'becuadro', 'redonda_espera', 'dacapo', 'fine']
    gutter = 22
    colw = (W - 104 - gutter) / 2.0
    filas = (len(orden) + 1) // 2
    alto, paso = 76, 84
    y0 = H - 150
    for i, tipo in enumerate(orden):
        col, fila = divmod(i, filas)
        x0 = 52 + col * (colw + gutter)
        y = y0 - fila * paso
        c.setFillColor(white)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.7)
        c.roundRect(x0, y - alto, colw, alto, 7, fill=1, stroke=1)
        color = COLOR_TIPO[tipo]
        cx, cy = x0 + 38, y - alto / 2.0
        c.setFillColor(color)
        c.circle(cx, cy, 24, fill=1, stroke=0)
        simbolo(c, cx, cy, 15, tipo, white)
        tx = x0 + 74
        c.setFont('DejaVuSans-Bold', 10.6)
        c.setFillColor(NAVY)
        c.drawString(tx, y - 24, NOMBRE_TIPO[tipo])
        c.setFont('DejaVuSans', 8.6)
        c.setFillColor(INK)
        _explicar(c, tx, y - 39, tipo, x0 + colw - tx - 10)

    y = y0 - filas * paso - 10
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2.0, 30, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()


# --------------------------------------------------------------------------
# Fichas y dado
# --------------------------------------------------------------------------
_PIPS = {
    1: [(0.5, 0.5)],
    2: [(0.26, 0.74), (0.74, 0.26)],
    3: [(0.26, 0.74), (0.5, 0.5), (0.74, 0.26)],
    4: [(0.26, 0.26), (0.26, 0.74), (0.74, 0.26), (0.74, 0.74)],
    5: [(0.26, 0.26), (0.26, 0.74), (0.5, 0.5), (0.74, 0.26), (0.74, 0.74)],
    6: [(0.26, 0.22), (0.26, 0.5), (0.26, 0.78),
        (0.74, 0.22), (0.74, 0.5), (0.74, 0.78)],
}


def _cara_dado(c, x, y, s, valor):
    c.setFillColor(white)
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.1)
    c.roundRect(x, y, s, s, 6, fill=1, stroke=1)
    c.setFillColor(NAVY)
    r = s * 0.075
    for (px, py) in _PIPS[valor]:
        c.circle(x + px * s, y + py * s, r, fill=1, stroke=0)


def _hoja_piezas(c):
    """Las cuatro fichas (mismos palos que el resto de la coleccion) y un
       dado de verdad para montar, por si en la mesa no hay uno a mano."""
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFont('DejaVuSerif-Bold', 22)
    c.setFillColor(NAVY)
    c.drawString(52, H - 78, 'Fichas y dado')
    c.setFont('DejaVuSans', 10)
    c.setFillColor(MUTED)
    c.drawString(52, H - 98, 'Recorta las cuatro fichas y, si hace falta, monta el dado.')

    c.setFont('DejaVuSans-Bold', 10.5)
    c.setFillColor(NAVY)
    c.drawString(52, H - 130, 'FICHAS')
    fy = H - 220
    fr = 26
    for i, (nombre, color, fm) in enumerate(PALOS):
        fx = 52 + 90 + i * 110
        c.setStrokeColor(RULE)
        c.setLineWidth(0.6)
        c.setDash(3, 3)
        c.circle(fx, fy, fr + 10, fill=0, stroke=1)
        c.setDash()
        forma(c, fx, fy, fr, fm, color)
        c.setFont('DejaVuSans', 8.4)
        c.setFillColor(INK)
        c.drawCentredString(fx, fy - fr - 26, nombre.capitalize())

    c.setFont('DejaVuSans-Bold', 10.5)
    c.setFillColor(NAVY)
    c.drawString(52, H - 330, 'DADO (opcional — solo si no tienes uno a mano)')
    c.setFont('DejaVuSans', 8.6)
    c.setFillColor(MUTED)
    _wrap(c, 'Recorta por el contorno, marca las líneas discontinuas con el '
             'canto de una regla para doblar bien, y pega las lengüetas '
             'grises por dentro.', 52, H - 344, 'DejaVuSans', 8.6, W - 104, 12, MUTED)

    s = 66
    ox, oy = 200, H - 430 - 3 * s
    layout = {
        (1, 2): 4, (0, 1): 2, (1, 1): 1, (2, 1): 5, (3, 1): 6, (1, 0): 3,
    }
    c.saveState()
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.setDash(4, 3)
    for (gx, gy), valor in layout.items():
        x = ox + gx * s
        y = oy + gy * s
        c.rect(x, y, s, s, fill=0, stroke=1)
    c.setDash()
    c.restoreState()
    for (gx, gy), valor in layout.items():
        x = ox + gx * s
        y = oy + gy * s
        _cara_dado(c, x, y, s, valor)
    # lengüetas de pegar, en los bordes libres del desarrollo
    c.saveState()
    c.setFillColor(HexColor('#E4E0D6'))
    c.setStrokeColor(RULE)
    c.setLineWidth(0.6)
    tabs = [
        (ox - s * 0.32, oy + s, s * 0.32, s),               # izq. de la cara 2
        (ox + 4 * s, oy + s, s * 0.32, s),                  # der. de la cara 6
        (ox + s, oy + 3 * s, s, s * 0.32),                  # arriba cara 4
        (ox + s, oy - s * 0.32, s, s * 0.32),                # abajo cara 3
    ]
    for (tx, ty, tw, th) in tabs:
        c.rect(tx, ty, tw, th, fill=1, stroke=1)
    c.restoreState()

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2.0, 30, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()


# --------------------------------------------------------------------------
def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'Oca_musical.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('Oca musical')

    _hoja_reglas(c)
    _hoja_leyenda(c)
    _hoja_tablero(c)
    _hoja_piezas(c)
    c.save()
    return ruta


def main(argv):
    ruta = construir()
    print('Oca musical · %s' % os.path.basename(ruta))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
