# -*- coding: utf-8 -*-
"""UNO MUSICAL — una sola baraja, para todo el mundo.

   LA IDEA. Es el UNO de siempre con una sustitucion y un anadido. La
   sustitucion: donde el UNO pone un NUMERO, aqui va una FIGURA (o su
   silencio). El anadido: TAMBIEN hay numerales de verdad —¼, ½, ¾, 1, 1½, 2,
   3, 4—, que valen exactamente lo mismo que la figura de su valor y se
   pueden jugar unos sobre otros. Si sale un "1" se puede tirar una negra
   encima, y al reves.

   Tres caminos para encadenar una carta sobre la de arriba:

     - por PALO   (color y forma), como en el UNO;
     - por FIGURA/NUMERAL IGUAL (la misma cara), como en el UNO;
     - por VALOR: una negra vale lo mismo que un "1", y DOS corcheas valen lo
       que UNA negra, y eso tambien se puede jugar y cantar.

   Ese ultimo camino es todo el aprendizaje del juego, y no hace falta
   explicarlo: se descubre porque sirve para ganar. LA REGLA QUE HACE QUE SEA
   MUSICA Y NO CROMOS: la carta se gana, no se tira — para soltarla hay que
   DECIR lo que vale en voz alta ("media", "uno y medio"), o palmearla. Sin
   esta regla el juego funciona igual... y no ensena nada, que es como acaban
   casi todos los juegos educativos.

   POR QUE UNA SOLA BARAJA Y NO TRES. Decision del cliente: esta la juega
   cualquiera, no hace falta escalonarla por figuras como el resto del
   material (eso ya lo hacen los propios dosieres). Lleva las CINCO figuras
   completas —de la semicorchea a la redonda— con sus CINCO silencios y el
   PUNTILLO en las dos que lo admiten (blanca y negra), que es mas de lo que
   llevaba cualquiera de los tres niveles antiguos por separado.

   LAS ESPECIALES, la mitad clasicas del UNO y la mitad nuevas:

     SILENCIO        el siguiente se calla un turno           (el "salta")
     BECUADRO        cambia el sentido de la ronda             (el "reverse")
     DOBLE BARRA     el siguiente roba dos                     (el "+2")
     CANON           cambias tu mano con la de otro jugador
     STACCATO        el siguiente tiene 3 segundos o roba una

   Y los comodines, sin palo, con el sello de T-Clas:

     ARMADURA        eliges el color a partir de ahora          (el "wild")
     CALDERÓN        eliges color y el siguiente roba cuatro    (el "wild +4")
     CLAVE DE SOL    cambias DOS cartas tuyas por otras del mazo
     CLAVE DE FA     cambias UNA carta tuya por otra del mazo

   Uso:  python3 juego_uno.py
"""
import os
import sys

from reportlab.lib.colors import white
from reportlab.pdfgen import canvas as rl_canvas

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from juegos_comun import (W, H, NAVY, CREAM, INK, MUTED, ACCENT, RULE,        # noqa: E402
                          PALOS, COLOR_PALO, FORMA_PALO, FIGURAS, figura,
                          figura_en_caja, forma, marco, oval_central,
                          logo_tclas, hoja_de_cartas, hoja_dorso,
                          portada_juego, CARTA_W, CARTA_H, simbolo as _simbolo)

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

# --------------------------------------------------------------------------
# La baraja: que lleva y cuantas copias
# --------------------------------------------------------------------------
# Las siete figuras que suenan (con puntillo en blanca y negra, la corchea
# se queda lisa) y sus cinco silencios. Dos copias de cada una por color: con
# una sola, una mano de siete se atasca y hay que robar todo el rato.
FIGURAS_CARTA = ['w', 'h.', 'h', 'q.', 'q', 'e', 's',
                 'Rw', 'Rh', 'Rq', 'Re', 'Rs']
COPIAS_FIGURA = 2

# Los numerales, con mas peso en los cuatro valores que de verdad se usan
# tocando (corchea, negra, blanca, redonda) que en los otros tres (los dos
# con puntillo y la semicorchea), que aparecen menos en una pieza real.
NUMERAL_DOS_COPIAS = ['w', 'h', 'q', 'e']
NUMERAL_UNA_COPIA = ['h.', 'q.', 's']

# Cuantas copias de cada especial, UNA por color salvo la que se dijo a
# proposito que llevara el doble (como el "+2" del UNO real, que tambien
# lleva dos copias por color).
ESPECIALES = {
    'silencio':   1,
    'becuadro':   1,
    'doblebarra': 2,
    'canon':      1,
    'staccato':   1,
}
# Los comodines no llevan palo: valen igual sobre cualquier carta. Las dos
# claves son mulligan contra el MAZO (no contra otro jugador, que es lo que
# ya hace CANON): mismo reparto de 6 copias que armadura/calderón.
COMODINES = {'armadura': 6, 'calderon': 6, 'clave_sol': 6, 'clave_fa': 6}

NOMBRE_ESPECIAL = {
    'silencio':   ('SILENCIO', 'se calla un turno'),
    'becuadro':   ('BECUADRO', 'cambia el sentido'),
    'doblebarra': ('+2', 'el siguiente roba dos'),
    'canon':      ('CANON', 'cambias tu mano con otro'),
    'staccato':   ('STACCATO', '3 segundos o robas'),
    'armadura':   ('ARMADURA', 'eliges color'),
    'calderon':   ('CALDERÓN', 'color y el siguiente roba cuatro'),
    'clave_sol':  ('CLAVE DE SOL', 'cambias 2 cartas por el mazo'),
    'clave_fa':   ('CLAVE DE FA', 'cambias 1 carta por el mazo'),
}


# --------------------------------------------------------------------------
# La baraja
# --------------------------------------------------------------------------
def baraja():
    cartas = []
    for clave in FIGURAS_CARTA:
        for palo, _c, _f in PALOS:
            for _ in range(COPIAS_FIGURA):
                cartas.append(dict(tipo='figura', palo=palo, clave=clave))
    for clave in NUMERAL_DOS_COPIAS:
        for palo, _c, _f in PALOS:
            for _ in range(2):
                cartas.append(dict(tipo='numeral', palo=palo, clave=clave))
    for clave in NUMERAL_UNA_COPIA:
        for palo, _c, _f in PALOS:
            cartas.append(dict(tipo='numeral', palo=palo, clave=clave))
    for esp, copias in ESPECIALES.items():
        for palo, _c, _f in PALOS:
            for _ in range(copias):
                cartas.append(dict(tipo='especial', palo=palo, cual=esp))
    for cual, copias in COMODINES.items():
        for _ in range(copias):
            cartas.append(dict(tipo='comodin', cual=cual))
    return cartas


def _reparto(cartas):
    """Las cartas se colocan en la hoja AGRUPADAS, no barajadas: recortar una
       hoja donde todo es distinto es un suplicio, y con las iguales juntas se
       ve de un vistazo si falta alguna."""
    orden_palo = dict((p, i) for i, (p, _c, _f) in enumerate(PALOS))
    orden_clave = dict((k, i) for i, k in enumerate(FIGURAS_CARTA))
    orden_num = dict((k, i) for i, k in enumerate(
        NUMERAL_DOS_COPIAS + NUMERAL_UNA_COPIA))

    def clave(k):
        if k['tipo'] == 'comodin':
            return (4, 0, k['cual'])
        if k['tipo'] == 'especial':
            return (3, orden_palo[k['palo']], k['cual'])
        if k['tipo'] == 'numeral':
            return (2, orden_num[k['clave']], orden_palo[k['palo']])
        return (1, orden_clave[k['clave']], orden_palo[k['palo']])
    return sorted(cartas, key=clave)


# --------------------------------------------------------------------------
# Dibujar una carta
# --------------------------------------------------------------------------
def pintar(c, x, y, w, h, carta):
    if carta['tipo'] == 'comodin':
        _comodin(c, x, y, w, h, carta)
    elif carta['tipo'] == 'especial':
        _especial(c, x, y, w, h, carta)
    elif carta['tipo'] == 'numeral':
        _numeral(c, x, y, w, h, carta)
    else:
        _figura(c, x, y, w, h, carta)


# El centro del ovalo va por encima de la mitad de la carta: abajo hay que
# dejar sitio para el nombre, que es lo que convierte la carta en material de
# clase y no en un cromo.
CY_OVALO = 0.575


def _figura(c, x, y, w, h, carta):
    col = COLOR_PALO[carta['palo']]
    nombre, _valor, etiqueta = FIGURAS[carta['clave']]
    cy = y + h * CY_OVALO
    marco(c, x, y, w, h, col)
    oval_central(c, x, y, w, h, cy=cy)
    figura_en_caja(c, x + w * 0.5, cy, w * 0.46, h * 0.40, carta['clave'])
    _esquinas(c, x, y, w, h, etiqueta, carta['palo'])
    _rotulo(c, x, y, w, nombre.upper(), None)


def _numeral(c, x, y, w, h, carta):
    """El numeral: MISMO valor que su figura gemela, pero la cara es un
       numero grande, como en el UNO de verdad. Es lo que deja jugar un "1"
       encima de una negra o al reves: la carta cambia, el valor no."""
    col = COLOR_PALO[carta['palo']]
    nombre, _valor, etiqueta = FIGURAS[carta['clave']]
    cy = y + h * CY_OVALO
    marco(c, x, y, w, h, col)
    oval_central(c, x, y, w, h, cy=cy)
    c.setFont('DejaVuSerif-Bold', h * 0.30)
    c.setFillColor(col)
    c.drawCentredString(x + w * 0.5, cy - h * 0.10, etiqueta)
    _esquinas(c, x, y, w, h, etiqueta, carta['palo'])
    _rotulo(c, x, y, w, nombre.upper(), 'vale lo mismo que la figura')


def _especial(c, x, y, w, h, carta):
    col = COLOR_PALO[carta['palo']]
    rotulo, que = NOMBRE_ESPECIAL[carta['cual']]
    cy = y + h * CY_OVALO
    marco(c, x, y, w, h, col)
    oval_central(c, x, y, w, h, cy=cy)
    _simbolo(c, x + w * 0.5, cy, w * 0.30, carta['cual'], INK)
    _esquinas(c, x, y, w, h, None, carta['palo'])
    _rotulo(c, x, y, w, rotulo, que)


def _comodin(c, x, y, w, h, carta):
    """El comodin no tiene palo, y eso hay que VERLO desde el otro lado de la
       mesa: fondo azul noche (ninguna otra carta lo es), el sello de T-Clas
       arriba —igual que el dorso, para que se reconozca a la vez como
       comodin y como "de esta baraja"— y los cuatro palos en las esquinas,
       como el arco iris del comodin del UNO de verdad.

       Las tres variantes (calderón, clave de sol, clave de fa) llevan ADEMÁS
       una segunda burbuja BLANCA, clara y separada de la del sello —no una
       marca suelta flotando en el azul, que quedaba pegada al sello y a
       medias invisible (blanco sobre blanco donde se solapaban)— con su
       icono en tinta azul noche, mismo lenguaje que el sello (oscuro sobre
       claro), para que se lea como parte del mismo diseño."""
    rotulo, que = NOMBRE_ESPECIAL[carta['cual']]
    marco(c, x, y, w, h, NAVY)
    cx = x + w / 2.0
    cy_logo = y + h * 0.66
    logo_tclas(c, cx, cy_logo, w * 0.24)
    if carta['cual'] in ('calderon', 'clave_sol', 'clave_fa'):
        rb = w * 0.125
        cy_b = y + h * 0.305
        c.setFillColor(white)
        c.circle(cx, cy_b, rb, fill=1, stroke=0)
        if carta['cual'] == 'calderon':
            _simbolo(c, cx, cy_b + rb * 0.34, rb * 0.55, 'calderon', NAVY)
            c.setFont('DejaVuSerif-Bold', rb * 0.92)
            c.setFillColor(NAVY)
            c.drawCentredString(cx, cy_b - rb * 0.62, '+4')
        else:
            _simbolo(c, cx, cy_b, rb * 0.82, carta['cual'], NAVY)
    for (ex, ey) in ((x + 13, y + h - 19), (x + w - 13, y + 19)):
        lado = 5.6
        for i, (_p, color, _fm) in enumerate(PALOS):
            c.setFillColor(color)
            dx = -lado if i % 2 == 0 else 0
            dy = 0 if i < 2 else -lado
            c.rect(ex + dx, ey + dy, lado, lado, fill=1, stroke=0)
    _rotulo(c, x, y, w, rotulo, que)


def _rotulo(c, x, y, w, titulo, pie):
    """El nombre, al pie de la carta. Se encoge si hace falta: 'silencio de
       corchea' es el doble de largo que 'negra' y a cuerpo fijo se sale."""
    from portada import _fit
    if pie:
        t = _fit(titulo, 'DejaVuSans-Bold', 7.4, w - 16, floor=5.2)
        c.setFont('DejaVuSans-Bold', t)
        c.setFillColor(white)
        c.drawCentredString(x + w / 2.0, y + 27, titulo)
        p = _fit(pie, 'DejaVuSans', 6.2, w - 14, floor=4.6)
        c.setFont('DejaVuSans', p)
        c.drawCentredString(x + w / 2.0, y + 18, pie)
    else:
        t = _fit(titulo, 'DejaVuSans-Bold', 7.6, w - 16, floor=5.0)
        c.setFont('DejaVuSans-Bold', t)
        c.setFillColor(white)
        c.drawCentredString(x + w / 2.0, y + 21, titulo)


def _esquinas(c, x, y, w, h, etiqueta, palo):
    """El valor en golpes y la forma del palo, arriba a la izquierda y abajo a
       la derecha girado. Es lo que permite jugar con la mano en abanico sin
       abrirla del todo: en el UNO de verdad son los numeros, aqui son los
       golpes. Y la FORMA va siempre, tenga o no numero la carta: es lo que
       salva la partida si un dia se imprime en blanco y negro."""
    fm = FORMA_PALO[palo]
    for (ex, ey, giro) in ((x + 12, y + h - 18, 0), (x + w - 12, y + 18, 180)):
        c.saveState()
        c.translate(ex, ey)
        c.rotate(giro)
        if etiqueta:
            c.setFont('DejaVuSans-Bold', 11.5)
            c.setFillColor(white)
            c.drawCentredString(0, 0, etiqueta)
            forma(c, 0, -9.5, 3.2, fm, white)
        else:
            forma(c, 0, 0, 4.3, fm, white)
        c.restoreState()


# --------------------------------------------------------------------------
# La tira de ejemplo. Es lo que de verdad explica el juego: seis lineas de
# reglas se leen una vez y se olvidan, y una fila de cartas con una flecha
# entre ellas no hace falta leerla dos veces.
# --------------------------------------------------------------------------
def _cadena():
    return [
        (dict(tipo='figura', palo='rojo', clave='q'), 'sale una NEGRA roja'),
        (dict(tipo='numeral', palo='azul', clave='q'), 'vale: mismo valor (1), aunque sea un numeral'),
        (dict(tipo='figura', palo='azul', clave='e'), 'vale: mismo palo'),
        (dict(tipo='figura', palo='azul', clave='e'), 'y otra corchea: las dos juntas valen una negra'),
    ]


def _tira_ejemplo(c, y):
    from portada import _wrap as _w
    cadena = _cadena()
    esc = 0.60
    cw, ch = CARTA_W * esc, CARTA_H * esc
    hueco = 26
    ancho = len(cadena) * cw + (len(cadena) - 1) * hueco
    x0 = (W - ancho) / 2.0
    alto = ch + 66

    c.setFillColor(white)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    c.roundRect(52, y - alto, W - 104, alto, 8, fill=1, stroke=1)

    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(ACCENT)
    c.drawString(68, y - 20, 'UNA MANO DE EJEMPLO')
    c.setFont('DejaVuSans', 8.2)
    c.setFillColor(MUTED)
    c.drawString(68 + 148, y - 20, 'de izquierda a derecha, y cada una dice por qué vale')

    cy = y - 34 - ch
    for i, (carta, pie) in enumerate(cadena):
        cx = x0 + i * (cw + hueco)
        c.saveState()
        c.translate(cx, cy)
        c.scale(esc, esc)
        pintar(c, 0, 0, CARTA_W, CARTA_H, carta)
        c.restoreState()
        c.setFont('DejaVuSans', 6.9)
        c.setFillColor(INK)
        _w(c, pie, cx - 6, cy - 11, 'DejaVuSans', 6.9, cw + 12, 8.6, INK)
        if i:                      # la flecha entre carta y carta
            fx = cx - hueco / 2.0
            fy = cy + ch / 2.0
            c.setStrokeColor(ACCENT)
            c.setFillColor(ACCENT)
            c.setLineWidth(1.3)
            c.line(fx - 7, fy, fx + 3, fy)
            pth = c.beginPath()
            pth.moveTo(fx + 8, fy); pth.lineTo(fx + 1, fy + 3.4)
            pth.lineTo(fx + 1, fy - 3.4); pth.close()
            c.drawPath(pth, fill=1, stroke=0)
    return y - alto


# --------------------------------------------------------------------------
# Las reglas, en una hoja
# --------------------------------------------------------------------------
def reglas():
    return [
        'Se reparten SIETE cartas a cada uno. El resto es el mazo, boca abajo, '
        'y se levanta la primera para empezar el montón.',
        'En tu turno sueltas UNA carta que coincida con la de encima: en el '
        'palo (color y forma), en la cara (misma figura o mismo numeral), o '
        'en el VALOR — un numeral "1" y una negra valen igual, y se pueden '
        'jugar una sobre otra.',
        'Y hay un tercer camino: puedes soltar VARIAS cartas cortas si entre '
        'todas valen lo mismo que la de encima. Dos corcheas encima de una '
        'negra, por ejemplo, o una negra con puntillo encima de una blanca '
        'con puntillo menos media.',
        'Para soltarla hay que DECIR EN VOZ ALTA lo que vale: «una», «media», '
        '«dos y media». Si no lo dices, la carta se vuelve a tu mano. Ésta es '
        'la única regla que no se puede saltar.',
        'Si no puedes o no quieres, robas una del mazo. Si la robada sirve, '
        'puedes soltarla en el mismo turno.',
        'Cuando te quede UNA sola carta tienes que decir «¡ÚLTIMO COMPÁS!» '
        'antes de que te lo diga otro. Si no, robas dos.',
        'Gana quien se queda sin cartas. Si el mazo se acaba, se baraja el '
        'montón y se sigue.',
    ]


MATERIALES = [
    'Esta baraja recortada. Dos jugadores como mínimo; cuatro es lo ideal.',
    'Nada más: no hace falta piano. Se puede jugar en la mesa, en el suelo o '
    'esperando a que llegue el siguiente.',
]

VARIANTES = [
    ('AL PIANO', 'la carta no se canta: se TOCA. Cualquier tecla, pero con la '
                 'duración de la figura. Quien alarga o acorta, roba.'),
    ('A CONTRARRELOJ', 'con el metrónomo puesto a ♩=60, la carta se suelta en '
                       'el clic siguiente o no se suelta.'),
    ('EL COMPÁS ENTERO', 'no se suelta una carta: se sueltan las que hagan '
                         'falta para sumar exactamente cuatro golpes.'),
]


def _hoja_reglas(c):
    return portada_juego(
        c, 'UNO musical', 'La baraja donde los números también son figuras', None,
        'Es el UNO de siempre con una diferencia y un añadido: donde el UNO '
        'pone un número, aquí hay una figura (o su silencio) — y ADEMÁS hay '
        'numerales de verdad, que valen igual que la figura de su mismo '
        'valor. Encadenar deja de ser solo cuestión de color y pasa a ser '
        'cuestión de cuánto dura cada cosa.',
        reglas(), MATERIALES, dibujo=_tira_ejemplo)


DETALLE = {
    'silencio':   'El siguiente pierde el turno. Con dos jugadores, vuelves a '
                  'tirar tú: es la carta más cruel de la baraja.',
    'becuadro':   'Se invierte el sentido de la ronda. Un becuadro deshace lo '
                  'que había, igual que en la partitura.',
    'doblebarra': 'El siguiente roba dos y pierde el turno. Se pueden encadenar: '
                  'si él también tiene una, la pasa y roban cuatro.',
    'canon':      'Cambias TODA tu mano por la de otro jugador, el que tú '
                  'elijas. Un canon es una voz que repite lo que hace otra: '
                  'aquí es literal.',
    'staccato':   'El siguiente tiene tres segundos —contados en voz alta— '
                  'para jugar o robar. Picado quiere decir corto: no hay '
                  'tiempo de pensarlo.',
    'armadura':   'Vale sobre cualquier carta. Dices en voz alta qué color manda '
                  'a partir de ahora, igual que la armadura manda sobre la pieza.',
    'calderon':   'Eliges color y el siguiente roba cuatro. Sólo se puede soltar '
                  'si de verdad no tienes ninguna carta del color de encima.',
    'clave_sol':  'Cambias DOS cartas tuyas por otras del mazo, boca abajo y '
                  'sin mirar.',
    'clave_fa':   'Cambias UNA carta tuya por otra del mazo, boca abajo y sin '
                  'mirar — la pequeña de la clave de sol.',
}


def _explicar(c, x, y, cual, ancho):
    from portada import _wrap
    _wrap(c, DETALLE[cual], x, y, 'DejaVuSans', 8.6, ancho, 12.0, INK)


def _hoja_especiales(c):
    """La chuleta de las especiales y los comodines, para dejarla en la mesa.
       A DOS COLUMNAS: con 5 especiales + 4 comodines (9 filas) una sola
       columna no cabe en la hoja."""
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFont('DejaVuSerif-Bold', 22)
    c.setFillColor(NAVY)
    c.drawString(52, H - 78, 'Las cartas especiales')
    c.setFont('DejaVuSans', 10)
    c.setFillColor(MUTED)
    c.drawString(52, H - 98, 'Déjala encima de la mesa las primeras partidas. '
                             'A la tercera ya no hace falta.')
    todas = [(e, 'palo') for e in ESPECIALES] + [(cu, 'comodin') for cu in COMODINES]
    gutter = 22
    colw = (W - 104 - gutter) / 2.0
    filas = (len(todas) + 1) // 2
    alto, paso = 76, 84
    y0 = H - 150
    esc = 0.30
    for i, (cual, clase) in enumerate(todas):
        col, fila = divmod(i, filas)
        x0 = 52 + col * (colw + gutter)
        y = y0 - fila * paso
        rotulo, que = NOMBRE_ESPECIAL[cual]
        c.setFillColor(white)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.7)
        c.roundRect(x0, y - alto, colw, alto, 7, fill=1, stroke=1)
        carta = (dict(tipo='comodin', cual=cual) if clase == 'comodin'
                 else dict(tipo='especial', palo='azul', cual=cual))
        c.saveState()
        c.translate(x0 + 14, y - alto + (alto - CARTA_H * esc) / 2.0)
        c.scale(esc, esc)
        pintar(c, 0, 0, CARTA_W, CARTA_H, carta)
        c.restoreState()
        tx = x0 + 14 + CARTA_W * esc + 14
        c.setFont('DejaVuSans-Bold', 10.6)
        c.setFillColor(NAVY)
        c.drawString(tx, y - 24, rotulo)
        c.setFont('DejaVuSans', 8.6)
        c.setFillColor(INK)
        _explicar(c, tx, y - 39, cual, x0 + colw - tx - 10)

    y = y0 - filas * paso - 8
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(NAVY)
    c.drawString(52, y - 8, 'TRES MANERAS DE JUGAR LA MISMA BARAJA')
    y -= 20
    from portada import _wrap
    for rotulo, texto in VARIANTES:
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(NAVY)
        c.drawString(52, y, rotulo)
        c.setFont('DejaVuSans', 9.0)
        c.setFillColor(INK)
        y = _wrap(c, texto, 52 + 128, y, 'DejaVuSans', 9.0, W - 52 - 128 - 52, 12.6, INK)
        y -= 8
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2.0, 30, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()


# --------------------------------------------------------------------------
def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'UNO_musical.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('UNO musical')

    _hoja_reglas(c)
    _hoja_especiales(c)

    cartas = _reparto(baraja())
    total = len(cartas)
    hoja = 1
    while cartas:
        pie = 'UNO musical · hoja %d de cartas' % hoja
        cartas = hoja_de_cartas(c, cartas, pintar, pie)
        hoja += 1
    hoja_dorso(c, 'UNO MUSICAL')
    c.save()
    return ruta, total, hoja - 1


def main(argv):
    ruta, total, hojas = construir()
    print('%3d cartas · %d hojas de recorte · %s'
          % (total, hojas, os.path.basename(ruta)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
