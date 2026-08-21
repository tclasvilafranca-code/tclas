# -*- coding: utf-8 -*-
"""UNO MUSICAL — tres barajas, una por nivel.

   LA IDEA. Es el UNO de siempre con una sola sustitucion: donde el UNO pone un
   NUMERO, aqui va una FIGURA. Y como cada figura vale lo que vale, se puede
   encadenar de dos maneras:

     - por PALO   (color y forma), como en el UNO;
     - por FIGURA (el mismo dibujo), como en el UNO;
     - y, en las barajas media y dificil, tambien **por VALOR**: una blanca
       encima de una negra con puntillo no vale, pero DOS corcheas valen lo que
       una negra y eso si se puede cantar.

   Ese tercer camino es todo el aprendizaje del juego, y no hace falta
   explicarlo: el alumno lo descubre porque le sirve para ganar. Nadie ha
   aprendido nunca que dos corcheas son una negra por que se lo dijeran; se
   aprende usandolo.

   LA REGLA QUE HACE QUE SEA MUSICA Y NO CROMOS. **La carta se gana, no se
   tira**: para soltar una carta hay que DECIR lo que vale en voz alta ("media"),
   o palmearla. Si no se dice, no se suelta. Sin esta regla el juego funciona
   igual de bien... y no ensena absolutamente nada, que es como acaban casi
   todos los juegos educativos.

   LAS ESPECIALES SALEN SOLAS DEL LENGUAJE, no hay que inventarse nada:

     SILENCIO        el siguiente se calla un turno
     BECUADRO        cambia el sentido (deshace lo que habia)
     DOBLE BARRA     el siguiente roba dos
     ARMADURA        comodin: eliges palo
     CALDERON        comodin: eliges palo y el siguiente roba cuatro

   QUE LLEVA CADA BARAJA (sale de `niveles.py`, no de la cabeza de nadie):

     FACIL    redonda, blanca, negra, corchea y dos silencios       60 cartas
     MEDIO    entra el puntillo                                     76 cartas
     DIFICIL  entra la semicorchea y la corchea con puntillo        92 cartas

   Uso:  python3 juego_uno.py            (las tres barajas)
         python3 juego_uno.py 1          (solo la facil)
"""
import os
import sys

from reportlab.lib.colors import white
from juegos_comun import ACCENT, RULE
from reportlab.pdfgen import canvas as rl_canvas

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from juegos_comun import (W, H, NAVY, CREAM, INK, MUTED, PALOS, COLOR_PALO,     # noqa: E402
                          FORMA_PALO, FIGURAS, NIVELES, figura, figura_en_caja,
                          forma, marco, oval_central, sello_nivel,
                          hoja_de_cartas, hoja_dorso, portada_juego,
                          CARTA_W, CARTA_H)

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

# Cuantas copias de cada figura por palo. Dos es lo que hace que una mano de
# siete tenga jugada casi siempre; con una sola copia el juego se atasca y hay
# que robar cuatro veces seguidas, que es cuando un nino de diez anos se va.
COPIAS = 2

ESPECIALES = {
    1: ['silencio', 'doblebarra'],
    2: ['silencio', 'becuadro', 'doblebarra'],
    3: ['silencio', 'becuadro', 'doblebarra'],
}
COMODINES = {1: [('armadura', 4)],
             2: [('armadura', 4), ('calderon', 2)],
             3: [('armadura', 4), ('calderon', 4)]}

NOMBRE_ESPECIAL = {
    'silencio':   ('SILENCIO', 'se calla un turno'),
    'becuadro':   ('BECUADRO', 'cambia el sentido'),
    'doblebarra': ('DOBLE BARRA', 'robas dos'),
    'armadura':   ('ARMADURA', 'eliges palo'),
    'calderon':   ('CALDERÓN', 'palo y robas cuatro'),
}


# --------------------------------------------------------------------------
# La baraja
# --------------------------------------------------------------------------
def baraja(nivel):
    cartas = []
    for clave in NIVELES[nivel]['figuras']:
        for palo, _c, _f in PALOS:
            for _ in range(COPIAS):
                cartas.append(dict(tipo='figura', palo=palo, clave=clave))
    for esp in ESPECIALES[nivel]:
        for palo, _c, _f in PALOS:
            cartas.append(dict(tipo='especial', palo=palo, cual=esp))
    for cual, cuantas in COMODINES[nivel]:
        for _ in range(cuantas):
            cartas.append(dict(tipo='comodin', cual=cual))
    return cartas


def _reparto(cartas):
    """Las cartas se colocan en la hoja AGRUPADAS POR PALO y por figura, no
       barajadas. Recortar una hoja donde todo es distinto es un suplicio; con
       las iguales juntas, la tijera va de corrido y ademas se ve de un vistazo
       si falta alguna."""
    orden = dict((p, i) for i, (p, _c, _f) in enumerate(PALOS))
    figs = NIVELES_ORDEN
    def clave(k):
        if k['tipo'] == 'comodin':
            return (3, 0, k['cual'])
        if k['tipo'] == 'especial':
            return (2, orden[k['palo']], k['cual'])
        return (1, figs.index(k['clave']), orden[k['palo']])
    return sorted(cartas, key=clave)


# --------------------------------------------------------------------------
# Dibujar una carta
# --------------------------------------------------------------------------
def pintar(c, x, y, w, h, carta):
    if carta['tipo'] == 'comodin':
        _comodin(c, x, y, w, h, carta)
    elif carta['tipo'] == 'especial':
        _especial(c, x, y, w, h, carta)
    else:
        _figura(c, x, y, w, h, carta)
    sello_nivel(c, x, y, w, PINTANDO['nivel'])


PINTANDO = dict(nivel=1)


# El centro del ovalo va por encima de la mitad de la carta: abajo hay que
# dejar sitio para el nombre de la figura, que es lo que convierte la carta en
# material de clase y no en un cromo.
CY_OVALO = 0.575


def _figura(c, x, y, w, h, carta):
    col = COLOR_PALO[carta['palo']]
    nombre, _valor, etiqueta = FIGURAS[carta['clave']]
    cy = y + h * CY_OVALO
    marco(c, x, y, w, h, col)
    oval_central(c, x, y, w, h, cy=cy)
    figura_en_caja(c, x + w * 0.5, cy, w * 0.46, h * 0.44, carta['clave'])
    _esquinas(c, x, y, w, h, etiqueta, carta['palo'])
    _rotulo(c, x, y, w, nombre.upper(), None)


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
       mesa: fondo azul noche (ninguna otra carta lo es) y los cuatro palos
       rodeando el simbolo, como los cuatro colores del comodin del UNO."""
    rotulo, que = NOMBRE_ESPECIAL[carta['cual']]
    cy = y + h * CY_OVALO
    marco(c, x, y, w, h, NAVY)
    cx = x + w / 2.0
    # los cuatro palos en cruz, POR FUERA del ovalo, no debajo
    r = w * 0.34
    for i, (_palo, color, fm) in enumerate(PALOS):
        ang = [(0, 1), (1, 0), (0, -1), (-1, 0)][i]
        forma(c, cx + ang[0] * r * 1.02, cy + ang[1] * r * 1.34,
              w * 0.055, fm, color)
    oval_central(c, x, y, w, h, cy=cy, rx=0.30, ry=0.235)
    _simbolo(c, cx, cy, w * 0.20, carta['cual'], INK)
    for (ex, ey) in ((x + 13, y + h - 19), (x + w - 13, y + 19)):
        lado = 5.2
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
        t = _fit(titulo, 'DejaVuSans-Bold', 6.8, w - 16, floor=5.0)
        c.setFont('DejaVuSans-Bold', t)
        c.setFillColor(white)
        c.drawCentredString(x + w / 2.0, y + 26, titulo)
        p = _fit(pie, 'DejaVuSans', 5.8, w - 14, floor=4.4)
        c.setFont('DejaVuSans', p)
        c.drawCentredString(x + w / 2.0, y + 18, pie)
    else:
        t = _fit(titulo, 'DejaVuSans-Bold', 7.0, w - 16, floor=4.8)
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
    for (ex, ey, giro) in ((x + 12, y + h - 20, 0), (x + w - 12, y + 20, 180)):
        c.saveState()
        c.translate(ex, ey)
        c.rotate(giro)
        if etiqueta:
            c.setFont('DejaVuSans-Bold', 12.5)
            c.setFillColor(white)
            c.drawCentredString(0, 0, etiqueta)
            forma(c, 0, -9.5, 3.4, fm, white)
        else:
            forma(c, 0, 0, 4.6, fm, white)
        c.restoreState()


def _simbolo(c, cx, cy, r, cual, color):
    """Los simbolos de las especiales. Se dibujan, no se buscan en una fuente:
       ningun tipo de texto trae una doble barra de compas ni un calderon con la
       proporcion que hace falta a este tamano."""
    c.saveState()
    c.setFillColor(color)
    c.setStrokeColor(color)
    if cual == 'silencio':
        from juegos_comun import figura_en_caja as _fc
        _fc(c, cx, cy, r * 1.5, r * 1.9, 'Rq', color)
    elif cual == 'becuadro':
        c.setFont('FreeSerif', r * 2.4)
        c.drawCentredString(cx, cy - r * 0.75, '♮')
    elif cual == 'doblebarra':
        c.setLineWidth(r * 0.13)
        c.line(cx - r * 0.30, cy - r * 0.85, cx - r * 0.30, cy + r * 0.85)
        c.setLineWidth(r * 0.34)
        c.line(cx + r * 0.22, cy - r * 0.85, cx + r * 0.22, cy + r * 0.85)
    elif cual == 'armadura':
        # uno al lado del otro y con aire: pegados se leen como un solo garabato
        c.setFont('FreeSerif', r * 1.55)
        c.drawCentredString(cx - r * 0.52, cy - r * 0.52, '♯')
        c.drawCentredString(cx + r * 0.54, cy - r * 0.42, '♭')
    elif cual == 'calderon':
        c.setLineWidth(r * 0.13)
        c.arc(cx - r * 0.92, cy - r * 0.80, cx + r * 0.92, cy + r * 1.00,
              startAng=0, extent=180)
        c.circle(cx, cy - r * 0.10, r * 0.15, fill=1, stroke=0)
    c.restoreState()


# --------------------------------------------------------------------------
# La tira de ejemplo. Es lo que de verdad explica el juego: seis lineas de
# reglas se leen una vez y se olvidan, y una fila de cuatro cartas con una
# flecha entre ellas no hace falta leerla dos veces.
# --------------------------------------------------------------------------
def _cadena(nivel):
    if nivel == 1:
        return [
            (dict(tipo='figura', palo='rojo', clave='q'), 'sale una NEGRA roja'),
            (dict(tipo='figura', palo='rojo', clave='h'), 'vale: mismo palo'),
            (dict(tipo='figura', palo='azul', clave='h'), 'vale: misma figura'),
            (dict(tipo='especial', palo='azul', cual='silencio'), 'y te callas un turno'),
        ]
    return [
        (dict(tipo='figura', palo='rojo', clave='q'), 'sale una NEGRA roja'),
        (dict(tipo='figura', palo='azul', clave='q'), 'vale: misma figura'),
        (dict(tipo='figura', palo='azul', clave='e'), 'vale: mismo palo'),
        (dict(tipo='figura', palo='azul', clave='e'), 'y otra: las dos valen una'),
    ]


def _tira_ejemplo(c, y):
    from portada import _wrap as _w
    from juegos_comun import RULE
    nivel = PINTANDO['nivel']
    cadena = _cadena(nivel)
    esc = 0.52
    cw, ch = CARTA_W * esc, CARTA_H * esc
    hueco = 30
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
    c.drawString(68 + 132, y - 20, 'de izquierda a derecha, y cada una dice por qué vale')

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
def reglas(nivel):
    n = NIVELES[nivel]
    valor = ('Y hay un tercer camino, que es de donde sale todo lo que se '
             'aprende aquí: puedes soltar VARIAS cartas cortas si entre todas '
             'valen lo mismo que la de encima. Dos corcheas encima de una '
             'negra, por ejemplo.') if nivel > 1 else ''
    return [
        'Se reparten SIETE cartas a cada uno. El resto es el mazo, boca abajo, '
        'y se levanta la primera para empezar el montón.',
        'En tu turno sueltas UNA carta que coincida con la de encima: o en el '
        'palo (el color y la forma) o en la figura. ' + valor,
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


def _hoja_reglas(c, nivel):
    n = NIVELES[nivel]
    y = portada_juego(
        c, 'UNO musical', 'La baraja donde los números son figuras', nivel,
        'Es el UNO de siempre con una sola diferencia: donde el UNO pone un '
        'número, aquí hay una figura. Y como cada figura vale lo que vale, '
        'encadenar deja de ser cuestión de color y pasa a ser cuestión de '
        'cuánto dura cada cosa. Esta baraja lleva %s.' % n['que'],
        reglas(nivel), MATERIALES, dibujo=_tira_ejemplo)
    return y


def _hoja_especiales(c, nivel):
    """La chuleta de las especiales, para dejarla encima de la mesa."""
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFont('DejaVuSerif-Bold', 22)
    c.setFillColor(NAVY)
    c.drawString(52, H - 78, 'Las cartas especiales')
    c.setFont('DejaVuSans', 10)
    c.setFillColor(MUTED)
    c.drawString(52, H - 98, 'Déjala encima de la mesa las primeras partidas. '
                             'A la tercera ya no hace falta.')
    y = H - 150
    todas = [(e, 'palo') for e in ESPECIALES[nivel]] + \
            [(cu, 'comodin') for cu, _n in COMODINES[nivel]]
    for cual, clase in todas:
        rotulo, que = NOMBRE_ESPECIAL[cual]
        alto = 92
        c.setFillColor(white)
        c.setStrokeColor(HexColor_rule())
        c.setLineWidth(0.7)
        c.roundRect(52, y - alto, W - 104, alto, 7, fill=1, stroke=1)
        carta = (dict(tipo='comodin', cual=cual) if clase == 'comodin'
                 else dict(tipo='especial', palo='azul', cual=cual))
        esc = 0.42
        c.saveState()
        c.translate(70, y - alto + (alto - CARTA_H * esc) / 2.0)
        c.scale(esc, esc)
        pintar(c, 0, 0, CARTA_W, CARTA_H, carta)
        c.restoreState()
        tx = 70 + CARTA_W * esc + 22
        c.setFont('DejaVuSans-Bold', 12)
        c.setFillColor(NAVY)
        c.drawString(tx, y - 30, rotulo)
        c.setFont('DejaVuSans', 9.6)
        c.setFillColor(INK)
        _explicar(c, tx, y - 48, cual)
        y -= alto + 12

    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(NAVY)
    c.drawString(52, y - 8, 'TRES MANERAS DE JUGAR LA MISMA BARAJA')
    y -= 28
    for rotulo, texto in VARIANTES:
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(NAVY)
        c.drawString(52, y, rotulo)
        c.setFont('DejaVuSans', 9.2)
        c.setFillColor(INK)
        c.drawString(52 + 128, y, texto)
        y -= 17
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2.0, 30, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()


def HexColor_rule():
    from juegos_comun import RULE
    return RULE


DETALLE = {
    'silencio': 'El siguiente pierde el turno. Con dos jugadores, vuelves a '
                'tirar tú: es la carta más cruel de la baraja.',
    'becuadro': 'Se invierte el sentido de la ronda. Un becuadro deshace lo '
                'que había, igual que en la partitura.',
    'doblebarra': 'El siguiente roba dos y pierde el turno. Se pueden encadenar: '
                  'si él también tiene una, la pasa y roban cuatro.',
    'armadura': 'Vale sobre cualquier carta. Dices en voz alta qué palo mandas '
                'a partir de ahora, igual que la armadura manda sobre la pieza.',
    'calderon': 'Eliges palo y el siguiente roba cuatro. Sólo se puede soltar '
                'si de verdad no tienes ninguna carta del palo de encima.',
}


def _explicar(c, x, y, cual):
    from portada import _wrap
    _wrap(c, DETALLE[cual], x, y, 'DejaVuSans', 9.4, W - x - 62, 13.4, INK)


# --------------------------------------------------------------------------
NIVELES_ORDEN = []


def construir(nivel):
    global NIVELES_ORDEN
    NIVELES_ORDEN = NIVELES[nivel]['figuras']
    PINTANDO['nivel'] = nivel
    os.makedirs(SALIDA, exist_ok=True)
    n = NIVELES[nivel]
    ruta = os.path.join(SALIDA, 'UNO_musical_%d_%s.pdf'
                        % (nivel, n['nombre'].lower().replace('í', 'i')))
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('UNO musical · nivel %s' % n['nombre'])

    _hoja_reglas(c, nivel)
    _hoja_especiales(c, nivel)

    cartas = _reparto(baraja(nivel))
    total = len(cartas)
    hoja = 1
    while cartas:
        pie = 'UNO musical · nivel %s · hoja %d de cartas' % (n['nombre'], hoja)
        cartas = hoja_de_cartas(c, cartas, pintar, pie)
        hoja += 1
    hoja_dorso(c, 'UNO', nivel)
    c.save()
    return ruta, total, hoja - 1


def main(argv):
    niveles = [int(a) for a in argv] or [1, 2, 3]
    for nv in niveles:
        ruta, total, hojas = construir(nv)
        print('%-9s %3d cartas · %d hojas de recorte · %s'
              % (NIVELES[nv]['nombre'], total, hojas, os.path.basename(ruta)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
