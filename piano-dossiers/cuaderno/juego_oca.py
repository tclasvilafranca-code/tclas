# -*- coding: utf-8 -*-
"""OCA MUSICAL — el tablero de toda la vida, con las casillas vestidas de
   música.

   POR QUÉ ASÍ. Decisión del cliente: estos juegos son para el final de
   clase, para romper la dinámica y pasarlo bien — no para seguir en clase
   con otro disfraz. Así que aquí NO hay cartas de reto ni preguntas: es la
   Oca de siempre, con el mismo tablero de 63 casillas y las siete casillas
   especiales de siempre, cada una vestida con un signo musical real, más
   UNA nueva (CAMBIO) para que cueste más llegar al final — sigue siendo
   puro azar, nunca una pregunta. La diversión es la de la Oca — el azar, el
   "otra vez a la casilla 1" — y la música es la piel, no una prueba.

   LAS CASILLAS, con su equivalencia clásica entre paréntesis:

     CORCHEA          (oca)       salta a la siguiente y tira otra vez
     LIGADURA          (puente)    te lleva a la otra ligadura
     CALDERÓN          (posada)    pierdes un turno — la nota se alarga
     SILENCIO           (pozo)      quieto hasta que otro caiga contigo
     BECUADRO           (laberinto) deshace lo andado, retrocedes
     SILENCIO DE REDONDA (cárcel)   el silencio más largo: dos turnos
     DA CAPO            (calavera)  vuelves derecho a la salida
     CAMBIO             (nueva)     cambias de sitio con quien va primero
     FINE               (meta)      hay que caer justo para ganar

   Silencio y becuadro son LOS MISMOS símbolos que en el UNO musical
   (`juegos_comun.simbolo`): un alumno que ha aprendido a leer una baraja
   lee el tablero sin que nadie le explique nada — es la norma de la
   colección. Y cada casilla llana lleva un instrumento de verdad
   (`juegos_comun.instrumento`, catorce en total, cíclicos) en vez de
   quedarse en blanco con solo un número — el tablero se lee como un
   tablero de juego, no como una hoja de instrucciones.

   Tablero: cuadrícula de 9×7 (=63), CASILLAS CUADRADAS, recorrida en
   espiral desde la esquina superior izquierda hasta el centro, que es
   donde cae la casilla 63 (FINE) bajo un medallón dorado con el gramófono
   — el mismo gesto visual de "el camino se enrosca hasta el premio" que
   tiene una Oca de verdad. Las esquinas donde la espiral gira llevan una
   cuña de color, y no una cuadrícula lisa.

   Uso:  python3 juego_oca.py
"""
import math
import os
import sys

from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfgen import canvas as rl_canvas

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from juegos_comun import (W, H, NAVY, CREAM, INK, MUTED, ACCENT, RULE,        # noqa: E402
                          PALOS, COLOR_PALO, FORMA_PALO, forma, simbolo,
                          logo_tclas, portada_juego, instrumento, INSTRUMENTOS)
from portada import _wrap                                                    # noqa: E402
from notation import BLEED_SAFE                                              # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

# --------------------------------------------------------------------------
# El tablero clásico: 9x7 casillas, espiral hacia el centro
# --------------------------------------------------------------------------
COLS, ROWS = 9, 7
# A3 apaisada: 1190.55 x 841.89 — un A4 se quedaba corto para que el tablero
# respirase de verdad (casillas grandes, medallón central con presencia,
# marco decorativo) en vez de ir todo encajado al milímetro.
BOARD_W, BOARD_H = landscape(A3)

# Las posiciones son las de la Oca de toda la vida (13 ocas, cada 4-5
# casillas; puentes en 6 y 12; posada 19; pozo 31; laberinto 42; carcel 52;
# calavera 58; meta 63) — no las hemos inventado, para que quien conoce el
# juego real la reconozca de un vistazo. CAMBIO es la unica que no tiene
# equivalente clasico: se añade para que cueste mas llegar (y de paso, mas
# risas) — un jugador puede caer bien situado y de repente estar el ultimo.
CORCHEAS = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
LIGADURAS = {6: 12, 12: 6}
CALDERON = 19
SILENCIO = 31
BECUADRO = 42
BECUADRO_DESTINO = 30
CARCEL = 52          # silencio de redonda: 2 turnos
DACAPO = 58
FINE = 63
CAMBIOS = [16, 47]   # cambias de sitio con quien va primero
# la escalera: subes directa de la casilla de abajo a la de arriba (no al
# reves, y no es un intercambio como la ligadura — es pura ganancia). Dos
# tramos, saltos grandes a proposito, para que de verdad se note el subidon.
ESCALERAS = {8: 29, 22: 40}

PLAIN_BG = HexColor('#2E7391')       # azul petroleo, no azul cielo de app
MAGENTA = HexColor('#C13C74')        # cambio, y las cuñas de los giros
FINE_GOLD = HexColor('#C9962B')
ESCALERA_COLOR = HexColor('#3E8E7E')  # verde azulado, distinto de corchea y ligadura

COLOR_TIPO = {
    'corchea':          HexColor('#3F5A38'),
    'ligadura':         HexColor('#20364F'),
    'calderon':         HexColor('#8C6423'),
    'silencio':         NAVY,
    'becuadro':         HexColor('#96381F'),
    'redonda_espera':   NAVY,
    'dacapo':           HexColor('#5C2118'),
    'cambio':           MAGENTA,
    'escalera':         ESCALERA_COLOR,
    'fine':             FINE_GOLD,
}

NOMBRE_TIPO = {
    'corchea':        'CORCHEA',
    'ligadura':       'LIGADURA',
    'calderon':       'CALDERÓN',
    'silencio':       'SILENCIO',
    'becuadro':       'BECUADRO',
    'redonda_espera': 'SILENCIO DE REDONDA',
    'dacapo':         'DA CAPO',
    'cambio':         'CAMBIO',
    'escalera':       'ESCALERA',
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
    'cambio':         'Cambias de sitio con quien va primero — si vas último, '
                       'de un tirón te pones en cabeza; si vas primero, cuidado.',
    'escalera':       'Nueva. El pentagrama hace de escalera: subes directo a '
                       'la casilla de arriba. Solo hacia arriba — no es un '
                       'intercambio, es pura ganancia.',
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
    if n in CAMBIOS:
        return 'cambio'
    if n in LIGADURAS:
        return 'ligadura'
    if n in CORCHEAS:
        return 'corchea'
    if n in ESCALERAS:
        return 'escalera'
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


def _giros(orden):
    """Las casillas donde la espiral cambia de direccion, con la esquina
       (sx, sy) hacia la que apunta el giro — para pintar ahi la cuña de
       color de la referencia, en vez de una cuadricula lisa."""
    giros = {}
    for i in range(1, len(orden) - 1):
        dx1 = orden[i][0] - orden[i - 1][0]
        dy1 = orden[i][1] - orden[i - 1][1]
        dx2 = orden[i + 1][0] - orden[i][0]
        dy2 = orden[i + 1][1] - orden[i][1]
        if (dx1, dy1) != (dx2, dy2):
            sx = 1 if (dx1 > 0 or dx2 > 0) else (-1 if (dx1 < 0 or dx2 < 0) else 0)
            sy = 1 if (dy1 > 0 or dy2 > 0) else (-1 if (dy1 < 0 or dy2 < 0) else 0)
            giros[i] = (sx, sy)
    return giros


# --------------------------------------------------------------------------
# La hoja del tablero
# --------------------------------------------------------------------------
def _cuna(c, x, y, w, h, sx, sy, color, jit=0):
    """La cuña triangular de la esquina del giro, el detalle que hace que la
       espiral se lea como un camino que dobla y no como una cuadricula
       lisa — el mismo lenguaje que las cuñas de color de la referencia.
       `jit` varia el tamaño un poco entre giro y giro para que las ocho
       cuñas del tablero no salgan todas del mismo molde exacto."""
    if sx == 0 or sy == 0:
        return
    lado = min(w, h) * (0.42 + jit)
    cxo = x + w / 2.0 + sx * w / 2.0
    cyo = y + h / 2.0 + sy * h / 2.0
    p = c.beginPath()
    p.moveTo(cxo, cyo)
    p.lineTo(cxo - sx * lado, cyo)
    p.lineTo(cxo, cyo - sy * lado)
    p.close()
    c.saveState()
    c.setFillColor(black)
    c.setFillAlpha(0.14)
    c.translate(1.2, -1.2)
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()
    c.setFillColor(color)
    c.drawPath(p, fill=1, stroke=0)


def _sombra_rect(c, x, y, w, h, r=6, dx=3, dy=-3, alpha=0.20):
    """La sombra de una casilla, un desplazamiento sutil para que "flote"
       sobre el fondo — la diferencia entre un icono plano y uno con cuerpo.
       Se pinta ANTES que la casilla, en negro translucido."""
    c.saveState()
    c.setFillColor(black)
    c.setFillAlpha(alpha)
    c.roundRect(x + dx, y + dy, w, h, r, fill=1, stroke=0)
    c.restoreState()


def _dibujar_casilla(c, x, y, w, h, numero, clave_instrumento, giro):
    tipo = _tipo_casilla(numero)
    _sombra_rect(c, x, y, w, h)
    if tipo is None:
        c.setFillColor(PLAIN_BG)
        c.setStrokeColor(white)
        c.setLineWidth(1.4)
        c.roundRect(x, y, w, h, 7, fill=1, stroke=1)
        if giro:
            _cuna(c, x, y, w, h, giro[0], giro[1], MAGENTA,
                 jit=((numero * 19) % 11 - 5) * 0.006)
        r = min(w, h) * 0.30
        # la sombra propia del instrumento, para que "flote" sobre la
        # casilla igual que la casilla flota sobre el tablero
        c.saveState()
        c.setFillColor(black)
        c.setFillAlpha(0.12)
        c.ellipse(x + w * 0.5 - r * 0.85, y + h * 0.53 - r * 0.72,
                 x + w * 0.5 + r * 0.85, y + h * 0.53 - r * 0.42, fill=1, stroke=0)
        c.restoreState()
        if numero == 1:
            simbolo(c, x + w / 2.0, y + h * 0.56, r, 'clave_sol', white)
        else:
            # un pelin de giro y de escala, distinto y determinista por
            # casilla: es lo que evita que sesenta iconos identicos, todos
            # rectos y del mismo tamano, delaten un tablero hecho a maquina
            ang = ((numero * 47) % 17) - 8
            esc = 1.0 + (((numero * 31) % 9) - 4) * 0.012
            c.saveState()
            c.translate(x + w / 2.0, y + h * 0.53)
            c.rotate(ang)
            c.scale(esc, esc)
            instrumento(c, 0, 0, r, clave_instrumento, fondo=PLAIN_BG)
            c.restoreState()
        _chip_numero(c, x, y, w, h, numero, NAVY, white)
        if numero == 1:
            c.setFont('DejaVuSans-Bold', w * 0.075)
            c.setFillColor(white)
            c.drawCentredString(x + w / 2.0, y + h * 0.06, 'SALIDA')
        return
    color = COLOR_TIPO[tipo]
    c.setFillColor(color)
    c.setStrokeColor(white)
    c.setLineWidth(1.4)
    c.roundRect(x, y, w, h, 7, fill=1, stroke=1)
    if giro:
        _cuna(c, x, y, w, h, giro[0], giro[1], MAGENTA,
             jit=((numero * 19) % 11 - 5) * 0.006)
    r = min(w, h) * 0.25
    cy = y + h * 0.58
    simbolo(c, x + w / 2.0, cy, r, tipo, white)
    _chip_numero(c, x, y, w, h, numero, color, white)
    extra = None
    if tipo == 'ligadura':
        extra = '→%d' % LIGADURAS[numero]
    elif tipo == 'becuadro':
        extra = '→%d' % BECUADRO_DESTINO
    elif tipo == 'dacapo':
        extra = '→1'
    elif tipo == 'redonda_espera':
        extra = '2 turnos'
    elif tipo == 'escalera':
        extra = '↑%d' % ESCALERAS[numero]
    if extra:
        c.setFont('DejaVuSans-Bold', w * 0.052)
        c.setFillColor(white)
        c.drawCentredString(x + w / 2.0, y + h * 0.05, extra)


def _chip_numero(c, x, y, w, h, numero, color_texto, color_chip):
    """El numero en una pastilla blanca redondeada, no suelto sobre el
       fondo — se lee igual de bien tenga la casilla el color que tenga, y
       da ese acabado "con cuerpo" que un numero pintado a pelo no tiene."""
    texto = str(numero)
    cw = w * (0.20 if len(texto) > 1 else 0.14)
    ch = h * 0.16
    cx0, cy0 = x + w * 0.08, y + h - ch - h * 0.07
    c.saveState()
    c.setFillColor(black)
    c.setFillAlpha(0.15)
    c.roundRect(cx0 + 1, cy0 - 1, cw, ch, ch / 2.0, fill=1, stroke=0)
    c.restoreState()
    c.setFillColor(color_chip)
    c.roundRect(cx0, cy0, cw, ch, ch / 2.0, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', ch * 0.62)
    c.setFillColor(color_texto)
    c.drawCentredString(cx0 + cw / 2.0, cy0 + ch * 0.28, texto)


def _escaleras_dibujo(c, orden, gx0, gy_top, cell_w, cell_h):
    """La escalera de verdad: no un icono suelto en una casilla, sino un
       pentagrama que CRUZA EL TABLERO en diagonal de la casilla de abajo a
       la de arriba — cinco lineas de pentagrama dobladas en peldaños, con
       una escalilla de notas que sube por encima. Es la pieza que rompe la
       cuadricula: todo lo demas en el tablero vive dentro de su casilla,
       esto vuela por encima de varias.

       Se dibuja DESPUES de la cuadricula, asi que "sobrevuela" lo que pisa
       en el camino — a proposito: una escalera de verdad tambien tapa un
       poco de lo que hay debajo."""
    def centro(numero):
        gx, gy = orden[numero - 1]
        px = gx0 + gx * cell_w
        py = gy_top - (gy + 1) * cell_h
        return (px + cell_w / 2.0, py + cell_h / 2.0)

    for origen, destino in sorted(ESCALERAS.items()):
        x0, y0 = centro(origen)
        x1, y1 = centro(destino)
        dx, dy = x1 - x0, y1 - y0
        dist = math.hypot(dx, dy)
        ux, uy = dx / dist, dy / dist
        px, py = -uy, ux
        paso = cell_h * 0.115

        c.saveState()
        c.setFillColor(black)
        c.setStrokeColor(black)
        c.setFillAlpha(0.15)
        c.setStrokeAlpha(0.15)
        for i in range(5):
            off = (i - 2) * paso
            c.setLineWidth(2.6 if i in (0, 4) else 1.7)
            c.line(x0 + px * off + 2.5, y0 + py * off - 2.5,
                  x1 + px * off + 2.5, y1 + py * off - 2.5)
        c.restoreState()

        c.saveState()
        c.setStrokeColor(ESCALERA_COLOR)
        c.setFillColor(ESCALERA_COLOR)
        for i in range(5):
            off = (i - 2) * paso
            c.setLineWidth(2.8 if i in (0, 4) else 1.8)
            c.line(x0 + px * off, y0 + py * off, x1 + px * off, y1 + py * off)
        # los peldaños: travesaños perpendiculares que atraviesan las cinco
        # lineas, el gesto que convierte un pentagrama en una escalera
        n_peldanos = max(4, int(dist / (cell_w * 0.85)))
        for k in range(1, n_peldanos):
            t = k / float(n_peldanos)
            rx, ry = x0 + dx * t, y0 + dy * t
            c.setLineWidth(2.0)
            c.line(rx + px * paso * 2.3, ry + py * paso * 2.3,
                  rx - px * paso * 2.3, ry - py * paso * 2.3)
        # una escalilla de notas subiendo, de peldaño en peldaño — la
        # metafora entera en tres golpes: subir la escalera ES subir la
        # escala
        for j, t in enumerate((0.22, 0.5, 0.78)):
            nx, ny = x0 + dx * t, y0 + dy * t
            off = (j - 1) * paso * 1.5
            nhx, nhy = nx + px * off, ny + py * off
            c.saveState()
            c.translate(nhx, nhy)
            ang_grados = math.degrees(math.atan2(uy, ux))
            c.rotate(ang_grados - 20)
            c.ellipse(-cell_w * 0.052, -cell_w * 0.036,
                     cell_w * 0.052, cell_w * 0.036, fill=1, stroke=0)
            c.setLineWidth(cell_w * 0.018)
            c.line(cell_w * 0.05, 0, cell_w * 0.05, cell_w * 0.16)
            c.restoreState()
        c.restoreState()

        # flecha en el extremo de llegada, apuntando en la direccion de la
        # subida, para que no quepa duda de hacia donde tira la escalera
        c.saveState()
        c.setFillColor(ESCALERA_COLOR)
        c.translate(x1 - ux * cell_h * 0.30, y1 - uy * cell_h * 0.30)
        ang_grados = math.degrees(math.atan2(uy, ux))
        c.rotate(ang_grados - 90)
        p = c.beginPath()
        lado = cell_w * 0.11
        p.moveTo(0, lado)
        p.lineTo(-lado * 0.8, -lado * 0.5)
        p.lineTo(lado * 0.8, -lado * 0.5)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        c.restoreState()


def _marco_decorativo(c):
    """El marco del poster: dos filetes (azul noche grueso, oro fino por
       dentro) y un adorno redondo en cada esquina — lo que hace que el
       tablero se lea como una pieza diseñada y no como una cuadricula
       suelta flotando en la hoja."""
    OUTER = 24
    c.saveState()
    c.setStrokeColor(NAVY)
    c.setLineWidth(3.2)
    c.roundRect(OUTER, OUTER, BOARD_W - 2 * OUTER, BOARD_H - 2 * OUTER, 16,
               fill=0, stroke=1)
    c.setStrokeColor(FINE_GOLD)
    c.setLineWidth(1.1)
    c.roundRect(OUTER + 6, OUTER + 6, BOARD_W - 2 * (OUTER + 6),
               BOARD_H - 2 * (OUTER + 6), 12, fill=0, stroke=1)
    c.restoreState()
    for (cx, cy) in ((OUTER, OUTER), (BOARD_W - OUTER, OUTER),
                     (OUTER, BOARD_H - OUTER), (BOARD_W - OUTER, BOARD_H - OUTER)):
        c.setFillColor(white)
        c.circle(cx, cy, 11, fill=1, stroke=0)
        c.setFillColor(FINE_GOLD)
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.4)
        c.circle(cx, cy, 9, fill=1, stroke=1)
        simbolo(c, cx, cy, 4.6, 'corchea', NAVY)
    return OUTER


def _hoja_tablero(c):
    c.setPageSize((BOARD_W, BOARD_H))
    c.setFillColor(CREAM)
    c.rect(0, 0, BOARD_W, BOARD_H, fill=1, stroke=0)

    outer = _marco_decorativo(c)
    pad = 18
    content_l = outer + pad
    content_r = BOARD_W - outer - pad
    content_t = BOARD_H - outer - pad
    content_b = outer + pad

    band_h = 62
    band_y = content_t - band_h
    c.setFillColor(NAVY)
    c.roundRect(content_l, band_y, content_r - content_l, band_h, 10, fill=1, stroke=0)
    c.rect(content_l, band_y, content_r - content_l, band_h / 2.0, fill=1, stroke=0)
    c.setFont('DejaVuSerif-Bold', 27)
    c.setFillColor(white)
    c.drawString(content_l + 22, band_y + band_h - 34, 'Oca musical')
    c.setFont('DejaVuSans', 11)
    c.setFillColor(HexColor('#C3CEDB'))
    c.drawString(content_l + 22, band_y + 16, 'de corchea en corchea, y tiro porque me toca')
    logo_tclas(c, content_r - 34, band_y + band_h / 2.0, 22)

    gy_top = band_y - 20
    grid_bottom = content_b + 26
    grid_h = gy_top - grid_bottom
    grid_w_max = content_r - content_l
    # celda CUADRADA (no rectangular): un tablero de Oca se lee como tal
    # cuando las casillas son cuadradas, no ladrillos anchos. El limite lo
    # pone la altura de la hoja; sobra ancho, y ese sobrante se reparte en
    # los dos margenes laterales.
    cell = min(grid_w_max / COLS, grid_h / ROWS)
    grid_w = cell * COLS
    gx0 = content_l + (grid_w_max - grid_w) / 2.0
    cell_w = cell_h = cell

    orden = _espiral(COLS, ROWS)
    giros = _giros(orden)

    # un instrumento distinto por casilla llana, en el orden en que se
    # juegan (asi dos casillas vecinas casi nunca repiten instrumento);
    # las especiales y la salida no cuentan para el ciclo.
    ronda_instrumentos = []
    ii = 0
    for idx in range(len(orden)):
        numero = idx + 1
        if numero != 1 and _tipo_casilla(numero) is None:
            ronda_instrumentos.append(INSTRUMENTOS[ii % len(INSTRUMENTOS)])
            ii += 1
        else:
            ronda_instrumentos.append(None)

    GAP = 3.0
    centro_px = None
    for idx, (gx, gy) in enumerate(orden):
        numero = idx + 1
        x = gx0 + gx * cell_w
        y = gy_top - (gy + 1) * cell_h
        if numero == FINE:
            centro_px = (x + cell_w / 2.0, y + cell_h / 2.0)
        _dibujar_casilla(c, x + GAP / 2.0, y + GAP / 2.0,
                         cell_w - GAP, cell_h - GAP, numero,
                         ronda_instrumentos[idx], giros.get(idx))

    _escaleras_dibujo(c, orden, gx0, gy_top, cell_w, cell_h)

    # el medallon central. La primera version lo hacia mas grande que una
    # casilla y tapaba el numero de las vecinas — dos de ellas especiales
    # (52 y 54), no solo llanas. Ahora el disco solido se queda DENTRO del
    # hueco de su propia casilla (no invade ninguna vecina) y el "premio"
    # visual viene de un halo dorado en capas, translucido, que sí se
    # derrama sobre las vecinas pero sin taparlas — se ve, no se lee encima.
    mx, my = centro_px
    for rad, alpha in ((cell * 1.55, 0.05), (cell * 1.15, 0.09), (cell * 0.82, 0.14)):
        c.saveState()
        c.setFillColor(FINE_GOLD)
        c.setFillAlpha(alpha)
        c.circle(mx, my, rad, fill=1, stroke=0)
        c.restoreState()

    mr = cell * 0.56
    c.saveState()
    c.setFillColor(black)
    c.setFillAlpha(0.22)
    c.circle(mx + 3, my - 3, mr, fill=1, stroke=0)
    c.restoreState()
    c.setFillColor(white)
    c.circle(mx, my, mr + 4, fill=1, stroke=0)
    c.setFillColor(FINE_GOLD)
    c.setStrokeColor(white)
    c.setLineWidth(2.6)
    c.circle(mx, my, mr, fill=1, stroke=1)
    c.setStrokeColor(white)
    c.setLineWidth(1)
    c.circle(mx, my, mr - 6, fill=0, stroke=1)
    c.setFont('DejaVuSerif-Bold', mr * 0.30)
    c.setFillColor(white)
    c.drawCentredString(mx, my + mr * 0.52, 'OCA')
    c.drawCentredString(mx, my + mr * 0.20, 'MUSICAL')
    instrumento(c, mx, my - mr * 0.42, mr * 0.32, 'gramofono', fondo=FINE_GOLD)
    c.setFont('DejaVuSans-Bold', mr * 0.17)
    c.setFillColor(white)
    c.drawCentredString(mx, my - mr * 0.85, 'FINE · 63')

    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawCentredString(BOARD_W / 2.0, content_b - 6, 'El Cuaderno del Pianista · T-Clas')
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
        'ESCALERA: el pentagrama cruza el tablero y te sube directo a la '
        'casilla de arriba — solo se sube, nunca se baja.',
        'CAMBIO: cambias de sitio con quien va primero — para bien o para mal.',
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
    """La chuleta de las nueve casillas especiales, a dos columnas — mismo
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
    orden = ['corchea', 'ligadura', 'calderon', 'silencio', 'escalera',
             'cambio', 'becuadro', 'redonda_espera', 'dacapo', 'fine']
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
