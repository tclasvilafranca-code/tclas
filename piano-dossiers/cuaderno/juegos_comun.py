# -*- coding: utf-8 -*-
"""La lengua visual de los CINCO juegos de clase.

   Aqui no vive ningun juego: vive lo que todos comparten, que es lo que hace
   que parezcan una coleccion y no cinco cosas sueltas. Misma paleta que el
   cuaderno, mismos cuatro palos, mismos dibujos de figura, mismo dorso y las
   mismas marcas de corte. Un alumno que ha aprendido a leer la baraja del UNO
   sabe leer el tablero de la Oca sin que nadie le explique nada.

   LOS TRES NIVELES SE LLAMAN POR DIFICULTAD, NO POR EDAD. "Facil, medio,
   dificil" y no "ninos, adolescentes, adultos". El motivo es concreto: Jose
   Maria tiene sesenta anos y empezo hace poco, y darle una caja que ponga
   ADULTOS con semicorcheas dentro seria mentirle dos veces. Lo que cambia de un
   nivel a otro son las FIGURAS que entran, y salen de `niveles.py`, que ya
   existe y ya lo audita `auditar_niveles.py`:

     FACIL    escalon 1 · redonda, blanca, negra, corchea y sus silencios
     MEDIO    escalon 2 · entra el PUNTILLO
     DIFICIL  escalon 3 · entra la SEMICORCHEA

   LOS PALOS SE DISTINGUEN TAMBIEN EN BLANCO Y NEGRO. Cada palo lleva color y
   ademas FORMA (rombo, circulo, triangulo, cuadrado). Si un dia la impresora
   de la escuela solo tiene toner negro, el juego sigue siendo jugable. Un juego
   que se muere en una fotocopia es un juego que no se lleva a clase.

   EL TAMANO DE CARTA es tamano poker de verdad (63,5 x 88,9 mm — 2,5" x 3,5",
   el mismo que un UNO real), 6 por hoja A4. Antes era baraja mini para que
   saliera mas barajas por hoja, pero a ese tamano una semicorchea con su
   doble corchete no se lee bien ni de cerca; con figuras de por medio el
   tamano manda sobre el numero de hojas.
"""
import os
import sys

from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

import notation as nt                                               # noqa: E402
from portada import (W, H, NAVY, NAVY_SOFT, CREAM, RULE, INK, MUTED,  # noqa: E402
                     ACCENT, _fit, _wrap)

# --------------------------------------------------------------------------
# Los cuatro palos. Color + FORMA, siempre las dos cosas.
# --------------------------------------------------------------------------
PALOS = [
    ('rojo',   HexColor('#B4462F'), 'rombo'),
    ('azul',   HexColor('#2C4C6B'), 'circulo'),
    ('verde',  HexColor('#4A6741'), 'triangulo'),
    ('ocre',   HexColor('#A9762F'), 'cuadrado'),
]
COLOR_PALO = dict((n, c) for n, c, _f in PALOS)
FORMA_PALO = dict((n, f) for n, _c, f in PALOS)

# --------------------------------------------------------------------------
# Las figuras, con su valor en golpes y su nombre. La clave es la misma que usa
# el motor (`notation.DUR_BEATS`), con una R delante para los silencios, para
# que no haya dos vocabularios distintos en el proyecto.
# --------------------------------------------------------------------------
FIGURAS = {
    'w':  ('redonda',               4.0,  '4'),
    'h.': ('blanca con puntillo',   3.0,  '3'),
    'h':  ('blanca',                2.0,  '2'),
    'q.': ('negra con puntillo',    1.5,  '1½'),
    'q':  ('negra',                 1.0,  '1'),
    'e.': ('corchea con puntillo',  0.75, '¾'),
    'e':  ('corchea',               0.5,  '½'),
    's':  ('semicorchea',           0.25, '¼'),
    'Rw': ('silencio de redonda',      4.0,  '4'),
    'Rh': ('silencio de blanca',       2.0,  '2'),
    'Rq': ('silencio de negra',        1.0,  '1'),
    'Re': ('silencio de corchea',      0.5,  '½'),
    'Rs': ('silencio de semicorchea',  0.25, '¼'),
}

NIVELES = {
    1: dict(
        nombre='FÁCIL', color=HexColor('#4A6741'),
        que='redonda, blanca, negra y corchea',
        figuras=['w', 'h', 'q', 'e', 'Rh', 'Rq'],
    ),
    2: dict(
        nombre='MEDIO', color=HexColor('#A9762F'),
        que='entra el puntillo',
        figuras=['w', 'h.', 'h', 'q.', 'q', 'e', 'Rh', 'Rq'],
    ),
    3: dict(
        nombre='DIFÍCIL', color=HexColor('#B4462F'),
        que='entra la semicorchea',
        figuras=['w', 'h.', 'h', 'q.', 'q', 'e.', 'e', 's', 'Rq', 'Re'],
    ),
}


# --------------------------------------------------------------------------
# Dibujar una figura SUELTA, fuera de un pentagrama
# --------------------------------------------------------------------------
def figura(c, cx, cy, gap, clave, color=None):
    """Una figura o un silencio, **centrados de verdad** en (cx, cy).

       El truco para reaprovechar el motor tal cual: se le pasa un pentagrama
       imaginario cuya TERCERA LINEA cae donde queremos la cabeza, y la nota que
       se pide es la de esa linea (Si4 en clave de sol). Asi `note_y` la coloca
       ahi, `ledger_lines_needed` no dibuja ninguna linea adicional porque la
       nota esta dentro, y la plica sale hacia arriba. Ni una constante nueva ni
       una copia del codigo de dibujo.

       Y una cuenta que hay que hacer o el dibujo queda descolgado: una negra NO
       esta centrada en su cabeza, porque le cuelga una plica de tres espacios y
       medio hacia arriba. Su centro visual esta a 1,45 espacios por encima de la
       cabeza. Sin descontarlo, en una carta la figura se va al fondo y parece
       que se ha impreso torcida."""
    alto = alto_figura(gap, clave)
    if clave.startswith('R') or clave == 'w':
        cabeza = cy
    else:
        cabeza = cy - gap * 1.45
    sb = cabeza - 2 * gap              # linea de abajo del pentagrama imaginario
    st = cabeza + 2 * gap              # linea de arriba
    c.saveState()
    with _tinta(color):
        if clave.startswith('R'):
            dur = {'Rw': 'w', 'Rh': 'h', 'Rq': 'q', 'Re': 'e', 'Rs': 's'}[clave]
            nt.draw_rest(c, cx, sb, st, gap, dur)
        else:
            nt.draw_note(c, cx, sb, st, gap, 'B4', clave, stem_dir='up', clef='treble')
    c.restoreState()
    return alto


def alto_figura(gap, clave):
    """Lo que ocupa de alto, para poder encajarla en una caja."""
    return gap * _PROPORCION[_familia(clave)][0]


def _familia(clave):
    if clave.startswith('R'):
        return 'silencio'
    if clave == 'w':
        return 'redonda'
    if clave.endswith('.'):
        return 'puntillo'
    return 'plica'


# (alto, ancho) de cada familia, en espacios de pentagrama. Medido sobre el
# propio motor, no estimado: la plica son 3,4 espacios y la cabeza 0,9.
_PROPORCION = {
    'redonda':  (0.95, 1.35),
    'plica':    (3.95, 1.30),
    'puntillo': (3.95, 1.95),
    'silencio': (2.30, 1.35),
}


def figura_en_caja(c, cx, cy, ancho, alto, clave, color=None):
    """Dibuja la figura AL TAMANO QUE LLENE la caja que se le da.

       Sin esto, todas las figuras se dibujan con el mismo espacio de pentagrama
       y en una carta pasa algo raro: la negra llena el hueco y **la redonda se
       queda como un garbanzo en medio de un plato**, porque una redonda es solo
       una cabeza y una negra tiene tres espacios y medio de plica. En una
       partitura eso es correcto —las figuras se comparan entre si—, pero en una
       carta cada figura esta sola y tiene que mandar en su carta."""
    fa, fw = _PROPORCION[_familia(clave)]
    gap = min(alto / fa, ancho / fw)
    figura(c, cx, cy, gap, clave, color)
    return gap


class _tinta(object):
    """El motor de notacion pinta siempre con SU negro (`notation.INK`). Para
       sacar una figura en blanco encima del color del palo hay que cambiarle el
       tinte mientras dura el dibujo — y devolverselo despues, sin excepciones,
       o la siguiente pagina sale entera del color de la ultima carta."""

    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color is None:
            return self
        self.previo = (nt.INK, nt.GRAY)
        nt.INK = nt.GRAY = self.color
        return self

    def __exit__(self, *_e):
        if self.color is not None:
            nt.INK, nt.GRAY = self.previo
        return False


# --------------------------------------------------------------------------
# Las formas de palo
# --------------------------------------------------------------------------
def forma(c, cx, cy, r, cual, color):
    c.saveState()
    c.setFillColor(color)
    c.setStrokeColor(color)
    if cual == 'circulo':
        c.circle(cx, cy, r, fill=1, stroke=0)
    elif cual == 'cuadrado':
        c.rect(cx - r * 0.88, cy - r * 0.88, r * 1.76, r * 1.76, fill=1, stroke=0)
    elif cual == 'rombo':
        p = c.beginPath()
        p.moveTo(cx, cy + r); p.lineTo(cx + r, cy)
        p.lineTo(cx, cy - r); p.lineTo(cx - r, cy); p.close()
        c.drawPath(p, fill=1, stroke=0)
    else:                                                   # triangulo
        p = c.beginPath()
        p.moveTo(cx, cy + r); p.lineTo(cx + r * 0.92, cy - r * 0.72)
        p.lineTo(cx - r * 0.92, cy - r * 0.72); p.close()
        c.drawPath(p, fill=1, stroke=0)
    c.restoreState()


LOGO_TCLAS = os.path.join(HERE, '..', 'assets', 'asset_logo_tclas_v2.png')


def logo_tclas(c, cx, cy, r):
    """El sello de T-Clas, centrado en (cx, cy) con radio r. Vive aqui y no en
       cada comodin porque el logo real (fondo blanco, clave en circulo azul
       noche) es lo que hace que un comodin se reconozca desde el otro lado de
       la mesa sin leer letra ninguna — igual que el arco iris del UNO de
       verdad.

       El PNG en si es un recorte: su canal de color es azul noche liso en
       toda la imagen y el dibujo entero (aro blanco, texto, clave) vive en
       el canal alfa, pensado para pegarse sobre fondo BLANCO. Sobre una
       carta azul noche, aro y clave desaparecen (azul sobre azul), asi que
       aqui se pinta primero un disco blanco de fondo."""
    c.saveState()
    c.setFillColor(white)
    c.circle(cx, cy, r * 1.02, fill=1, stroke=0)
    c.restoreState()
    try:
        c.drawImage(LOGO_TCLAS, cx - r, cy - r, r * 2, r * 2,
                    mask='auto', preserveAspectRatio=True)
    except Exception:
        pass


# --------------------------------------------------------------------------
# La hoja de cartas: 3 x 4, con marcas de corte
# --------------------------------------------------------------------------
# Ancho de poker de verdad (63.5mm) para que una semicorchea se lea; alto
# recortado de 88.9 a 70.6mm para que quepan doce por hoja en vez de seis. El
# recorte se hace con guillotina, asi que el numero de hojas no es problema;
# lo que si lo era es una carta tan alta que desperdicia media hoja de aire.
CARTA_W, CARTA_H = 180.0, 200.0        # 63.5 x 70.6 mm
COLS, FILAS = 3, 4
POR_HOJA = COLS * FILAS


def _origen():
    ancho = COLS * CARTA_W
    alto = FILAS * CARTA_H
    return (W - ancho) / 2.0, (H - alto) / 2.0


def marcas_de_corte(c):
    """Las rayitas de fuera, no las de dentro.

       Una reticula dibujada ENTRE las cartas se ve en el borde de la carta ya
       recortada y queda sucia. Las marcas van en los margenes, alineadas con
       cada corte, y la tijera une los dos extremos."""
    x0, y0 = _origen()
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    for i in range(COLS + 1):
        x = x0 + i * CARTA_W
        c.line(x, y0 - 16, x, y0 - 5)
        c.line(x, y0 + FILAS * CARTA_H + 5, x, y0 + FILAS * CARTA_H + 16)
    for j in range(FILAS + 1):
        y = y0 + j * CARTA_H
        c.line(x0 - 16, y, x0 - 5, y)
        c.line(x0 + COLS * CARTA_W + 5, y, x0 + COLS * CARTA_W + 16, y)


def hoja_de_cartas(c, cartas, pintar, pie=''):
    """Coloca hasta 16 cartas en una A4 y devuelve las que no han cabido."""
    x0, y0 = _origen()
    marcas_de_corte(c)
    for k, carta in enumerate(cartas[:POR_HOJA]):
        col = k % COLS
        fil = k // COLS
        x = x0 + col * CARTA_W
        y = y0 + (FILAS - 1 - fil) * CARTA_H
        pintar(c, x, y, CARTA_W, CARTA_H, carta)
    if pie:
        c.setFont('DejaVuSans', 6.6)
        c.setFillColor(MUTED)
        c.drawString(x0, y0 - 26, pie)
        c.drawRightString(x0 + COLS * CARTA_W, y0 - 26, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()
    return cartas[POR_HOJA:]


def marco(c, x, y, w, h, fondo, borde=None, r=9):
    """El rectangulo redondeado de una carta, con su filete claro por dentro.

       El filete no es adorno: recortar a mano nunca sale recto, y un margen de
       cortesia de tres puntos hace que un corte torcido no se coma el dibujo."""
    c.setFillColor(fondo)
    c.setStrokeColor(borde or fondo)
    c.setLineWidth(0.6)
    c.roundRect(x + 1.5, y + 1.5, w - 3, h - 3, r, fill=1, stroke=1)


def oval_central(c, x, y, w, h, color=white, giro=-14, cy=None,
                 rx=0.415, ry=0.335):
    """El ovalo blanco inclinado del centro, que es lo que hace que una carta se
       lea como una carta de UNO y no como una ficha de domino.

       Va MENOS inclinado que el del UNO de verdad (14 grados y no 20) por una
       razon de oficio: el numero del UNO es ancho y el ovalo puede tumbarse,
       pero una negra es alta y estrecha, y a veinte grados la plica se sale por
       el borde de arriba."""
    c.saveState()
    c.translate(x + w / 2.0, cy if cy is not None else y + h / 2.0)
    c.rotate(giro)
    c.setFillColor(color)
    c.setStrokeColor(color)
    c.ellipse(-w * rx, -h * ry, w * rx, h * ry, fill=1, stroke=0)
    c.restoreState()


def sello_nivel(c, x, y, w, nivel, color=None):
    """Uno, dos o tres puntitos al pie de la carta. Discreto a proposito: sirve
       para que dos barajas mezcladas se puedan volver a separar, no para
       ponerle una etiqueta de nivel al alumno en la mano."""
    col = color or white
    c.setFillColor(col)
    for i in range(nivel):
        c.circle(x + w / 2.0 + (i - (nivel - 1) / 2.0) * 6.5, y + 9, 1.7,
                 fill=1, stroke=0)


# --------------------------------------------------------------------------
# Portada de juego y dorso, comunes a los cinco
# --------------------------------------------------------------------------
def portada_juego(c, titulo, subtitulo, nivel, resumen, reglas, materiales,
                  dibujo=None):
    """La hoja 1 de cada juego: como se juega, en una sola cara.

       Norma de la coleccion: si las reglas no caben en una hoja, el juego no se
       juega. En una clase de media hora nadie lee dos paginas de reglas.

       `nivel=None` es un juego de una sola baraja para todo el mundo (como el
       UNO musical): se salta la pastilla de nivel, que no pinta nada si no
       hay nada que distinguir."""
    n = NIVELES[nivel] if nivel is not None else None
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFillColor(NAVY)
    c.rect(0, H - 132, W, 132, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(HexColor('#9FB0C4'))
    c.drawString(52, H - 40, 'JUEGOS DE CLASE · EL CUADERNO DEL PIANISTA')
    c.setFont('DejaVuSerif-Bold', 30)
    c.setFillColor(white)
    c.drawString(52, H - 78, titulo)
    c.setFont('DejaVuSans', 10.5)
    c.setFillColor(HexColor('#C3CEDB'))
    c.drawString(52, H - 98, subtitulo)

    if n is not None:
        # la pastilla de nivel, arriba a la derecha
        pw = 108
        c.setFillColor(n['color'])
        c.roundRect(W - 52 - pw, H - 86, pw, 30, 6, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 13)
        c.setFillColor(white)
        c.drawCentredString(W - 52 - pw / 2.0, H - 76, n['nombre'])
        c.setFont('DejaVuSans', 7.4)
        c.setFillColor(HexColor('#C3CEDB'))
        c.drawRightString(W - 52, H - 98, n['que'])

    y = H - 168
    c.setFont('DejaVuSans', 11)
    c.setFillColor(INK)
    y = _wrap(c, resumen, 52, y, 'DejaVuSans', 11, W - 104, 16, INK)

    y -= 18
    y = _bloque(c, y, 'QUÉ HACE FALTA', materiales)
    y -= 6
    y = _bloque(c, y, 'CÓMO SE JUEGA', reglas, numerado=True)
    if dibujo:
        y = dibujo(c, y - 10)

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2.0, 30, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()
    return y


def _bloque(c, y, titulo, lineas, numerado=False):
    c.setFont('DejaVuSans-Bold', 8.6)
    c.setFillColor(ACCENT)
    c.drawString(52, y, titulo)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.4)
    c.line(52, y - 5, 52 + stringWidth(titulo, 'DejaVuSans-Bold', 8.6), y - 5)
    y -= 20
    for i, ln in enumerate(lineas, 1):
        # La vinieta va a la altura de la PRIMERA linea del parrafo, no del
        # centro del bloque: con un texto de tres lineas el punto se quedaba
        # flotando encima y parecia que pertenecia al parrafo anterior.
        if numerado:
            c.setFillColor(NAVY)
            c.circle(58, y - 3.2, 7.6, fill=1, stroke=0)
            c.setFont('DejaVuSans-Bold', 8)
            c.setFillColor(white)
            c.drawCentredString(58, y - 5.8, str(i))
            x = 76
        else:
            c.setFillColor(ACCENT)
            c.circle(57, y - 3.2, 2.2, fill=1, stroke=0)
            x = 68
        y = _wrap(c, ln, x, y, 'DejaVuSans', 9.6, W - x - 52, 13.6, INK)
        y -= 8
    return y


def hoja_dorso(c, titulo, nivel=None):
    """Una hoja entera de dorsos, para pegar por detras si se quiere.

       Es opcional y va la ultima: con cartulina de un solo color la baraja ya
       es opaca, y pegar sesenta dorsos a mano no lo hace nadie dos veces.

       El sello de T-Clas centrado, igual que en los comodines: asi el dorso
       se reconoce desde el otro lado de la mesa como parte de la misma
       coleccion, sin tener que leer nada. `nivel=None` (el caso normal ahora,
       una sola baraja) se salta los puntitos de nivel."""
    x0, y0 = _origen()
    marcas_de_corte(c)
    for k in range(POR_HOJA):
        col, fil = k % COLS, k // COLS
        x = x0 + col * CARTA_W
        y = y0 + (FILAS - 1 - fil) * CARTA_H
        marco(c, x, y, CARTA_W, CARTA_H, NAVY)
        oval_central(c, x, y, CARTA_W, CARTA_H, color=NAVY_SOFT,
                     rx=0.40, ry=0.36)
        logo_tclas(c, x + CARTA_W / 2.0, y + CARTA_H * 0.565, CARTA_W * 0.30)
        c.setFont('DejaVuSerif-Bold', 12)
        c.setFillColor(white)
        c.drawCentredString(x + CARTA_W / 2.0, y + 20, titulo.upper())
        if nivel is not None:
            sello_nivel(c, x, y, CARTA_W, nivel, color=NAVY_SOFT)
    c.setFont('DejaVuSans', 6.6)
    c.setFillColor(MUTED)
    c.drawString(x0, y0 - 26, 'Dorsos · opcional, solo si quieres pegarlos por detrás')
    c.showPage()
