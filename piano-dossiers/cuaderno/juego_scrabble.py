# -*- coding: utf-8 -*-
"""Scrabble musical — el crucigrama de fichas de toda la vida, con las
   casillas de premio hechas de figuras musicales y un empujón extra si la
   palabra que formas es de música.

   POR QUÉ ASÍ. Mismo encargo que la Oca: esto es para el final de clase,
   para pasarlo bien, no para seguir estudiando con otro disfraz. Así que
   NO hay una lista cerrada de palabras "permitidas" — eso limitaría el
   juego a un puñado de términos y lo dejaría cojo a la tercera partida.
   La regla es la de siempre: **cualquier palabra española vale**. Lo que
   trae el disfraz musical es un BONUS: si la palabra que formas es un
   término de música (la lista de la hoja siguiente), su valor se dobla
   otra vez. Así el juego sigue siendo Scrabble de verdad y además premia
   a quien conoce el vocabulario de clase.

   EL TABLERO: 11×11 en vez de las 15×15 de un Scrabble de caja — una
   partida de verdad con 15×15 no se acaba en el rato que sobra al final
   de clase. Las casillas de premio son las mismas cuatro de siempre
   (palabra ×3, palabra ×2, letra ×3, letra ×2) pero dibujadas con una
   figura real en vez de un texto plano: REDONDA para ×3 palabra, BLANCA
   para ×2 palabra, CORCHEA para ×3 letra, SEMICORCHEA para ×2 letra — a
   más grande la nota, más manda; y las letras, con las notas cortas. Un
   alumno que ya sabe leer estas figuras del UNO y de la Oca las reconoce
   aquí también, sin aprender un símbolo nuevo.

   LAS FICHAS: el abecedario completo, de la A a la Z (con la Ñ, que en
   español es una letra de pleno derecho) — en una tanda más pequeña que
   un Scrabble de caja (que trae unas 100) para que una partida de dos o
   tres manos quepa en el rato de clase. Los valores de punto son los de
   siempre: cuanto más rara la letra, más vale — K y W son tan raras en
   español que valen lo mismo que la J, la Ñ o la X.

   Uso:  python3 juego_scrabble.py
"""
import os
import sys

from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfgen import canvas as rl_canvas

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from juegos_comun import (W, H, NAVY, CREAM, INK, MUTED, ACCENT, RULE,        # noqa: E402
                          logo_tclas, portada_juego, figura_en_caja)
from portada import _wrap                                                    # noqa: E402
from notation import BLEED_SAFE                                              # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

# --------------------------------------------------------------------------
# El tablero: 11x11, simetria de 4 giros alrededor del centro
# --------------------------------------------------------------------------
COLS = ROWS = 11
BOARD_W, BOARD_H = landscape(A3)
CENTRO_CELDA = (5, 5)

TW_COLOR = HexColor('#8C1F1F')   # palabra x3 — REDONDA, la nota mas grande
DW_COLOR = HexColor('#C13C74')   # palabra x2 — BLANCA
TL_COLOR = HexColor('#20364F')   # letra x3   — CORCHEA
DL_COLOR = HexColor('#2E7391')   # letra x2   — SEMICORCHEA
CENTRO_COLOR = HexColor('#C9962B')
PLAIN_BG = HexColor('#F2EAD9')

COLOR_TIPO = {'TW': TW_COLOR, 'DW': DW_COLOR, 'TL': TL_COLOR, 'DL': DL_COLOR,
             'CENTRO': CENTRO_COLOR}
FIGURA_TIPO = {'TW': 'w', 'DW': 'h', 'TL': 'e', 'DL': 's', 'CENTRO': 'h'}
NOMBRE_TIPO = {'TW': 'PALABRA ×3', 'DW': 'PALABRA ×2', 'TL': 'LETRA ×3',
              'DL': 'LETRA ×2', 'CENTRO': 'SALIDA · PALABRA ×2'}
DETALLE_TIPO = {
    'TW': 'La REDONDA, la nota más larga — la casilla que más aprieta: '
          'multiplica por TRES el valor de la palabra entera.',
    'DW': 'La BLANCA dobla el valor de la palabra entera.',
    'TL': 'La CORCHEA multiplica por TRES el valor de esa letra sola '
          '(no el resto de la palabra).',
    'DL': 'La SEMICORCHEA dobla el valor de esa letra sola.',
    'CENTRO': 'Por aquí tiene que pasar la primera palabra de la partida. '
              'Cuenta también como PALABRA ×2.',
}


def _rotar(r, c):
    """Un giro de 90 grados alrededor del centro del tablero (5,5)."""
    return (c, (COLS - 1) - r)


def _orbita(seed):
    pts = set()
    r, c = seed
    for _ in range(4):
        pts.add((r, c))
        r, c = _rotar(r, c)
    return pts


# Una sola casilla semilla por cada "brazo" de la simetria; el resto del
# tablero sale solo, girandola 90/180/270 grados. Es como se construye de
# verdad un tablero de Scrabble (el real tambien es simetrico a 4 giros).
SEEDS_TW = [(0, 0), (0, 5)]
SEEDS_DW = [(2, 2), (4, 4)]
SEEDS_TL = [(1, 4), (4, 1)]
SEEDS_DL = [(0, 2), (2, 0)]


def _construir_mapa():
    mapa = {}
    for tipo, seeds in (('TW', SEEDS_TW), ('DW', SEEDS_DW),
                        ('TL', SEEDS_TL), ('DL', SEEDS_DL)):
        for seed in seeds:
            for p in _orbita(seed):
                mapa[p] = tipo
    mapa[CENTRO_CELDA] = 'CENTRO'
    return mapa


MAPA_CASILLAS = _construir_mapa()

# --------------------------------------------------------------------------
# Las fichas: alfabeto español clásico de Scrabble (sin K ni W), en una
# tanda mas pequeña para que una partida quepa en el rato de clase.
# (letra, valor, cuantas)
# --------------------------------------------------------------------------
LETRAS = [
    ('A', 1, 6), ('E', 1, 6), ('O', 1, 5), ('I', 1, 3), ('S', 1, 3),
    ('N', 1, 3), ('R', 1, 3), ('U', 1, 3), ('L', 1, 2), ('T', 1, 2),
    ('D', 2, 3), ('G', 2, 1),
    ('C', 3, 2), ('M', 3, 1), ('P', 3, 1), ('B', 3, 1),
    ('H', 4, 1), ('F', 4, 1), ('V', 4, 1), ('Y', 4, 1),
    ('Q', 5, 1),
    ('J', 8, 1), ('K', 8, 1), ('Ñ', 8, 1), ('W', 8, 1), ('X', 8, 1),
    ('Z', 10, 1),
    ('★', 0, 2),
]
TOTAL_FICHAS = sum(n for _l, _v, n in LETRAS)

# --------------------------------------------------------------------------
# Las palabras musicales — el bonus, no una lista cerrada de lo permitido
# --------------------------------------------------------------------------
PALABRAS_MUSICALES = {
    'Notas y solfeo': [
        'DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI', 'BEMOL', 'SOSTENIDO',
        'BECUADRO', 'ARMADURA', 'CLAVE', 'PENTAGRAMA', 'COMPAS', 'OCTAVA',
        'ESCALA', 'TONALIDAD',
    ],
    'Figuras y silencios': [
        'REDONDA', 'BLANCA', 'NEGRA', 'CORCHEA', 'SEMICORCHEA', 'SILENCIO',
        'PUNTILLO', 'LIGADURA', 'BARRA', 'CALDERON', 'PLICA',
    ],
    'Instrumentos': [
        'PIANO', 'VIOLIN', 'GUITARRA', 'ARPA', 'FLAUTA', 'TROMPETA',
        'TAMBOR', 'SAXOFON', 'ACORDEON', 'TROMBON', 'XILOFONO',
        'PANDERETA', 'MARACAS', 'PLATILLOS', 'MICROFONO',
    ],
    'Tempo y carácter': [
        'ALLEGRO', 'ADAGIO', 'LARGO', 'PRESTO', 'ANDANTE', 'MODERATO',
        'VIVACE', 'LENTO',
    ],
    'Dinámica y expresión': [
        'FORTE', 'CRESCENDO', 'STACCATO', 'LEGATO', 'VIBRATO', 'ACENTO',
        'REGULADOR',
    ],
    'Forma y conjunto': [
        'MELODIA', 'ARMONIA', 'ACORDE', 'RITMO', 'DUO', 'TRIO', 'CORO',
        'BATUTA', 'PARTITURA', 'SOLFEO', 'ENSAYO', 'CONCIERTO',
        'SINFONIA', 'OPERA', 'SONATA', 'ORQUESTA',
    ],
}


def reglas():
    return [
        'Repartid 7 fichas a cada jugador, sacadas SIN MIRAR de una bolsa '
        'o un bote opaco.',
        'La primera palabra tiene que cruzar la casilla central (la '
        'ESTRELLA). Las siguientes se cruzan con letras ya puestas en el '
        'tablero, como en un crucigrama.',
        'Cada ficha vale los puntos que trae escritos; el valor de la '
        'palabra es la suma de sus letras.',
        'Las casillas de color multiplican, y SOLO la primera vez que se '
        'pone una ficha encima: LETRA ×2/×3 multiplica solo esa letra; '
        'PALABRA ×2/×3 multiplica el total de toda la palabra.',
        'BONUS MUSICAL: si la palabra que formas está en la lista de la '
        'hoja siguiente, su valor final se dobla otra vez.',
        'Cualquier palabra española vale, esté o no en la lista — la '
        'lista solo da el bonus, no decide lo que se puede jugar.',
        'Al terminar el turno, repón fichas de la bolsa hasta volver a '
        'tener 7.',
        'Se acaba cuando se terminan las fichas de la bolsa o nadie puede '
        'colocar ninguna más. Gana quien más puntos tenga sumados.',
    ]


MATERIALES = [
    'El tablero (hoja 3) y las fichas de letra (hoja 4) — recorta las '
    'fichas y mételas en una bolsa opaca para sacarlas sin mirar.',
    'Papel y bolígrafo para apuntar los puntos de cada jugador.',
    'De 2 a 4 jugadores.',
]


def _hoja_reglas(c):
    return portada_juego(
        c, 'Scrabble musical', 'El crucigrama de fichas, con premio si la palabra es de música',
        None,
        'Es el Scrabble de toda la vida: se forman palabras cruzando '
        'letras sobre el tablero, y cada una suma los puntos de sus '
        'fichas. Cualquier palabra española vale — no hace falta que sea '
        'de música. Lo que trae el disfraz es un bonus: si la palabra '
        'que formas es un término musical, su valor se dobla otra vez.',
        reglas(), MATERIALES)


# --------------------------------------------------------------------------
# La hoja de la lista de palabras musicales
# --------------------------------------------------------------------------
def _hoja_palabras(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFont('DejaVuSerif-Bold', 22)
    c.setFillColor(NAVY)
    c.drawString(52, H - 78, 'Las palabras musicales')
    c.setFont('DejaVuSans', 10)
    c.setFillColor(MUTED)
    _wrap(c, 'Si formas una de estas, dobla su valor otra vez — no hace '
             'falta memorizarlas, basta con tenerla al lado mientras juegas.',
         52, H - 98, 'DejaVuSans', 10, W - 104, 14, MUTED)

    categorias = list(PALABRAS_MUSICALES.items())
    gutter = 22
    colw = (W - 104 - gutter) / 2.0
    col_izq = categorias[0::2]
    col_der = categorias[1::2]

    def _columna(x0, cats):
        y = H - 140
        for titulo, palabras in cats:
            c.setFont('DejaVuSans-Bold', 10.6)
            c.setFillColor(ACCENT)
            c.drawString(x0, y, titulo.upper())
            c.setStrokeColor(ACCENT)
            c.setLineWidth(1.1)
            c.line(x0, y - 4, x0 + colw, y - 4)
            y -= 18
            texto = ' · '.join(palabras)
            y = _wrap(c, texto, x0, y, 'DejaVuSans', 8.8, colw, 13.0, INK)
            y -= 16
        return y

    _columna(52, col_izq)
    _columna(52 + colw + gutter, col_der)

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2.0, 30, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()


# --------------------------------------------------------------------------
# La hoja del tablero
# --------------------------------------------------------------------------
def _sombra_rect(c, x, y, w, h, r=5, dx=2.4, dy=-2.4, alpha=0.16):
    c.saveState()
    c.setFillColor(black)
    c.setFillAlpha(alpha)
    c.roundRect(x + dx, y + dy, w, h, r, fill=1, stroke=0)
    c.restoreState()


def _dibujar_casilla(c, x, y, w, h, tipo):
    _sombra_rect(c, x, y, w, h)
    color = COLOR_TIPO.get(tipo, PLAIN_BG)
    c.setFillColor(color)
    c.setStrokeColor(white if tipo else RULE)
    c.setLineWidth(1.1 if tipo else 0.6)
    c.roundRect(x, y, w, h, 4, fill=1, stroke=1)
    if tipo is None:
        return
    clave = FIGURA_TIPO[tipo]
    r = min(w, h) * 0.42
    figura_en_caja(c, x + w / 2.0, y + h * 0.56, r * 1.3, r * 1.6, clave, white)
    etiqueta = {'TW': 'x3 PAL.', 'DW': 'x2 PAL.', 'TL': 'x3 LET.',
               'DL': 'x2 LET.', 'CENTRO': 'SALIDA'}[tipo]
    c.setFont('DejaVuSans-Bold', w * 0.16)
    c.setFillColor(white)
    c.drawCentredString(x + w / 2.0, y + h * 0.09, etiqueta)


def _marco_decorativo(c):
    OUTER = 24
    c.saveState()
    c.setStrokeColor(NAVY)
    c.setLineWidth(3.2)
    c.roundRect(OUTER, OUTER, BOARD_W - 2 * OUTER, BOARD_H - 2 * OUTER, 16,
               fill=0, stroke=1)
    c.setStrokeColor(CENTRO_COLOR)
    c.setLineWidth(1.1)
    c.roundRect(OUTER + 6, OUTER + 6, BOARD_W - 2 * (OUTER + 6),
               BOARD_H - 2 * (OUTER + 6), 12, fill=0, stroke=1)
    c.restoreState()
    for (cx, cy) in ((OUTER, OUTER), (BOARD_W - OUTER, OUTER),
                     (OUTER, BOARD_H - OUTER), (BOARD_W - OUTER, BOARD_H - OUTER)):
        c.setFillColor(white)
        c.circle(cx, cy, 11, fill=1, stroke=0)
        c.setFillColor(CENTRO_COLOR)
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.4)
        c.circle(cx, cy, 9, fill=1, stroke=1)
        figura_en_caja(c, cx, cy, 6.4, 6.4, 'e', NAVY)
    return OUTER


def _panel_leyenda(c, x, y_top, ancho, y_bottom):
    """El panel lateral: para que el ancho que sobra a la derecha del
       tablero cuadrado no se quede en blanco, aqui va la leyenda de
       multiplicadores y la tabla de valores de letra — lo que un
       jugador necesita consultar mientras juega, al lado del tablero y
       no en otra hoja."""
    y = y_top
    c.setFont('DejaVuSerif-Bold', 15)
    c.setFillColor(NAVY)
    c.drawString(x, y, 'Las casillas')
    y -= 26
    for tipo in ('TW', 'DW', 'TL', 'DL', 'CENTRO'):
        color = COLOR_TIPO[tipo]
        r = 15
        c.setFillColor(color)
        c.circle(x + r, y - r, r, fill=1, stroke=0)
        figura_en_caja(c, x + r, y - r + 3, r * 1.0, r * 1.2, FIGURA_TIPO[tipo], white)
        c.setFont('DejaVuSans-Bold', 9.6)
        c.setFillColor(NAVY)
        c.drawString(x + 2 * r + 10, y - r + 5, NOMBRE_TIPO[tipo])
        c.setFont('DejaVuSans', 7.6)
        c.setFillColor(INK)
        y2 = _wrap(c, DETALLE_TIPO[tipo], x + 2 * r + 10, y - r - 8,
                  'DejaVuSans', 7.6, ancho - 2 * r - 10, 10.4, INK)
        y = min(y2, y - 2 * r - 6) - 14

    y -= 6
    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    c.line(x, y, x + ancho, y)
    y -= 22
    c.setFont('DejaVuSerif-Bold', 15)
    c.setFillColor(NAVY)
    c.drawString(x, y, 'Valor de las fichas')
    y -= 20
    por_valor = {}
    for letra, valor, _n in LETRAS:
        por_valor.setdefault(valor, []).append(letra)
    for valor in sorted(por_valor):
        c.setFillColor(CENTRO_COLOR if valor >= 8 else NAVY)
        c.circle(x + 9, y - 3, 9, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 8.6)
        c.setFillColor(white)
        c.drawCentredString(x + 9, y - 6, str(valor))
        c.setFont('DejaVuSans', 8.4)
        c.setFillColor(INK)
        c.drawString(x + 24, y - 6, ' · '.join(letras for letras in por_valor[valor]))
        y -= 20
        if y < y_bottom:
            break


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
    c.drawString(content_l + 22, band_y + band_h - 34, 'Scrabble musical')
    c.setFont('DejaVuSans', 11)
    c.setFillColor(HexColor('#C3CEDB'))
    c.drawString(content_l + 22, band_y + 16, 'cualquier palabra vale — la musical, doble')
    logo_tclas(c, content_r - 34, band_y + band_h / 2.0, 22)

    gy_top = band_y - 20
    grid_bottom = content_b + 26
    grid_h = gy_top - grid_bottom
    # el tablero llena el alto disponible entero y se queda CUADRADO — hay
    # que poder posar encima una ficha de verdad — y lo que sobra de ancho
    # a la derecha no se deja en blanco: ahi va el panel de la leyenda.
    cell = grid_h / ROWS
    grid_w = cell * COLS
    gx0 = content_l

    GAP = 2.4
    for r in range(ROWS):
        for col in range(COLS):
            x = gx0 + col * cell
            y = gy_top - (r + 1) * cell
            tipo = MAPA_CASILLAS.get((r, col))
            _dibujar_casilla(c, x + GAP / 2.0, y + GAP / 2.0, cell - GAP, cell - GAP, tipo)

    panel_x = gx0 + grid_w + 34
    panel_ancho = content_r - panel_x
    _panel_leyenda(c, panel_x, gy_top - 6, panel_ancho, grid_bottom)

    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawCentredString(BOARD_W / 2.0, content_b - 6, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()
    c.setPageSize((W, H))


# --------------------------------------------------------------------------
# Las fichas de letra
# --------------------------------------------------------------------------
TILE = 62
TGAP = 7


def _ficha(c, x, y, s, letra, valor):
    _sombra_rect(c, x, y, s, s, r=6, dx=1.6, dy=-1.6, alpha=0.18)
    c.setFillColor(HexColor('#E8D9B0'))
    c.setStrokeColor(HexColor('#B79256'))
    c.setLineWidth(1.0)
    c.roundRect(x, y, s, s, 6, fill=1, stroke=1)
    c.setFillColor(HexColor('#3B2413'))
    if letra == '★':
        c.setFont('DejaVuSans-Bold', s * 0.42)
    else:
        c.setFont('DejaVuSerif-Bold', s * 0.50)
    c.drawCentredString(x + s / 2.0, y + s * 0.30, letra)
    if valor:
        c.setFont('DejaVuSans-Bold', s * 0.17)
        c.drawRightString(x + s - s * 0.10, y + s * 0.08, str(valor))


def _hoja_fichas(c):
    tiles = []
    for letra, valor, n in LETRAS:
        tiles.extend([(letra, valor)] * n)

    margin = 46
    top_y = H - 118
    x0 = margin
    cols = int((W - 2 * margin + TGAP) / (TILE + TGAP))
    row_y = top_y

    def _cabecera(pagina):
        c.setFillColor(CREAM)
        c.rect(0, 0, W, H, fill=1, stroke=0)
        c.setFont('DejaVuSerif-Bold', 22)
        c.setFillColor(NAVY)
        c.drawString(52, H - 78, 'Fichas de letra')
        c.setFont('DejaVuSans', 10)
        c.setFillColor(MUTED)
        sub = ('Recorta las %d fichas y mételas en una bolsa opaca — se sacan '
              'sin mirar.' % TOTAL_FICHAS) if pagina == 1 else '(continúan de la hoja anterior)'
        c.drawString(52, H - 98, sub)

    pagina = 1
    _cabecera(pagina)
    i = 0
    x, y = x0, row_y
    col = 0
    for letra, valor in tiles:
        if y - TILE < 40:
            c.setFont('DejaVuSans', 7.4)
            c.setFillColor(MUTED)
            c.drawCentredString(W / 2.0, 24, 'El Cuaderno del Pianista · T-Clas')
            c.showPage()
            pagina += 1
            _cabecera(pagina)
            x, y, col = x0, row_y, 0
        _ficha(c, x, y - TILE, TILE, letra, valor)
        col += 1
        if col >= cols:
            col = 0
            x = x0
            y -= TILE + TGAP
        else:
            x += TILE + TGAP

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2.0, 24, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()


# --------------------------------------------------------------------------
def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'Scrabble_musical.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('Scrabble musical')

    _hoja_reglas(c)
    _hoja_palabras(c)
    _hoja_tablero(c)
    _hoja_fichas(c)
    c.save()
    return ruta


def main(argv):
    ruta = construir()
    print('Scrabble musical · %s' % os.path.basename(ruta))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
