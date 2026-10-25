# -*- coding: utf-8 -*-
"""Hundir la flota en el teclado — el Hundir la flota de toda la vida,
   pero las coordenadas no son "B7": son una nota y una octava de verdad,
   la misma pareja (nota, octava) que ya usa el motor del cuaderno para
   nombrar cualquier tecla del piano ("Do4" es el Do central). Un alumno
   que dispara a "MI4" está leyendo una nota real, no una celda de
   ajedrez con otro disfraz.

   POR QUÉ ASÍ. Mismo encargo que el resto: final de clase, a pasarlo
   bien, cero preguntas de examen escondidas. El tablero se juega en
   PAPEL Y LÁPIZ, como el Hundir la flota real — no hay fichas que
   recortar, solo una hoja de juego por jugador (fotocopiada dos veces).

   LA FLOTA lleva nombre de conjunto musical en vez de "acorazado" —
   mismo tamaño de piezas que el juego real, más pequeño porque el
   tablero también lo es: LA ORQUESTA (4 casillas seguidas), EL CUARTETO
   (3), dos DÚOS (2 y 2) y dos SOLISTAS (1 y 1). Ni una casilla más que
   eso: con trece casillas de barco sobre 56 del tablero, la partida no
   se alarga más de lo que dura el rato que sobra en clase.

   MARCAR LOS DISPAROS reutiliza el mismo vocabulario visual que el UNO
   y la Oca: una corchea si aciertas, un silencio si fallas — el mismo
   símbolo, el mismo significado ("aquí SUENA algo" / "aquí no hay
   nada"), en el tercer juego de la colección.

   Uso:  python3 juego_flota.py
"""
import os
import sys

from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas as rl_canvas

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from juegos_comun import (W, H, NAVY, CREAM, INK, MUTED, ACCENT, RULE,       # noqa: E402
                          simbolo, portada_juego,
                          JUEGO_DISPLAY_BLACK, JUEGO_DISPLAY_ITALIC,
                          JUEGO_BODY, JUEGO_BODY_MEDIUM, JUEGO_BODY_BOLD)
from portada import _wrap                                                    # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

# --------------------------------------------------------------------------
# El tablero: 7 notas (columnas) x 8 octavas (filas) — la misma pareja
# (nota, octava) que nombra cualquier tecla del piano en el resto del
# cuaderno, asi que "MI4" no es una coordenada nueva que aprender.
# --------------------------------------------------------------------------
NOTAS = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']
OCTAVAS = [8, 7, 6, 5, 4, 3, 2, 1]   # de arriba abajo: mas agudo arriba,
                                     # igual que en un pentagrama

FLOTA = [
    ('LA ORQUESTA', 4, 1),
    ('EL CUARTETO', 3, 1),
    ('EL DÚO', 2, 2),
    ('EL SOLISTA', 1, 2),
]
TOTAL_CASILLAS_BARCO = sum(tam * n for _n, tam, n in FLOTA)


def reglas():
    return [
        'Cada jugador coloca su flota EN SECRETO sobre su propio tablero '
        '"MI FLOTA" (hoja 2) — tapadlo con una carpeta o un libro para '
        'que el otro no lo vea mientras dibujáis.',
        'La flota es la misma para los dos: LA ORQUESTA (4 casillas '
        'seguidas), EL CUARTETO (3), dos DÚOS (2 casillas cada uno) y '
        'dos SOLISTAS (1 casilla cada uno).',
        'Cada pieza va en línea recta, horizontal o vertical — nunca en '
        'diagonal — y ninguna pieza puede tocar a otra, ni siquiera por '
        'una esquina.',
        'Por turnos, cada jugador "dispara" diciendo en voz alta una '
        'nota y su octava — igual que se nombra cualquier tecla del '
        'piano: "MI4", "SOL2", "DO7"…',
        'El otro jugador mira su tablero MI FLOTA en esa casilla y '
        'contesta AGUA (no hay nada) o TOCADO (hay un barco).',
        'Anota el resultado en tu propio TABLERO DE TIRO, en esa misma '
        'casilla: una corchea (♪) si has tocado, un silencio si es '
        'agua — así ves de un vistazo qué casillas ya has probado.',
        'Cuando un barco recibe un disparo en TODAS sus casillas, se '
        'hunde: quien lo hunde lo anuncia en voz alta ("¡Hundido el '
        'dúo!").',
        'Gana quien hunda antes la flota entera del otro.',
    ]


MATERIALES = [
    'Un tablero de juego por jugador (hoja 2 — fotocopiada dos veces, '
    'una para cada uno) y un lápiz o bolígrafo.',
    'Algo para tapar tu tablero MI FLOTA mientras juegas (una carpeta, '
    'un libro, la mano del compañero de al lado).',
    'Se juega por parejas.',
]


def _hoja_reglas(c):
    return portada_juego(
        c, 'Hundir la flota en el teclado', 'El Hundir la flota de toda la vida, con las coordenadas de una tecla real',
        None,
        'Es el Hundir la flota de siempre: cada uno esconde su flota, y '
        'por turnos vais disparando a coordenadas hasta hundir la del '
        'otro. La diferencia es que aquí una coordenada no es "B7": es '
        'una nota real con su octava, la misma pareja que nombra '
        'cualquier tecla del piano.',
        reglas(), MATERIALES)


# --------------------------------------------------------------------------
# La hoja de juego: dos tableros por jugador, uno encima del otro
# --------------------------------------------------------------------------
def _grid(c, x0, y_top, cell, titulo, subtitulo):
    ancho_filas = 22   # el carril de las etiquetas de octava, a la izquierda
    gx0 = x0 + ancho_filas
    gy_top = y_top - 34   # deja sitio al titulo y a las cabeceras de columna

    c.setFont(JUEGO_DISPLAY_BLACK, 13.5)
    c.setFillColor(NAVY)
    c.drawString(x0, y_top, titulo)
    c.setFont(JUEGO_BODY, 8.4)
    c.setFillColor(MUTED)
    c.drawString(x0, y_top - 15, subtitulo)

    # cabeceras de columna (las notas)
    c.setFont(JUEGO_BODY_BOLD, 8.6)
    c.setFillColor(NAVY)
    for j, nota in enumerate(NOTAS):
        cx = gx0 + j * cell + cell / 2.0
        c.drawCentredString(cx, gy_top + 6, nota)

    # la cuadricula y las etiquetas de fila (las octavas)
    for i, octava in enumerate(OCTAVAS):
        ry = gy_top - (i + 1) * cell
        c.setFont(JUEGO_BODY_BOLD, 8.6)
        c.setFillColor(NAVY)
        c.drawCentredString(x0 + ancho_filas / 2.0, ry + cell / 2.0 - 3, str(octava))
        for j in range(len(NOTAS)):
            rx = gx0 + j * cell
            c.setFillColor(white)
            c.setStrokeColor(RULE)
            c.setLineWidth(0.7)
            c.rect(rx, ry, cell, cell, fill=1, stroke=1)

    alto_total = len(OCTAVAS) * cell
    return gy_top - alto_total - 14   # la y libre para lo que venga despues


def _leyenda_marcas(c, x, y, colw):
    c.setFont(JUEGO_BODY_BOLD, 8.6)
    c.setFillColor(NAVY)
    c.drawString(x, y, 'Cómo anotas un disparo:')
    y -= 20
    r = 8
    cx1 = x + r
    simbolo(c, cx1, y + 3, r, 'corchea', ACCENT)
    c.setFont(JUEGO_BODY, 8.4)
    c.setFillColor(INK)
    c.drawString(cx1 + r + 6, y, '= tocado')
    cx2 = x + colw / 2.0 + r
    simbolo(c, cx2, y + 3, r, 'silencio', MUTED)
    c.drawString(cx2 + r + 6, y, '= agua')


def _hoja_juego(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFont(JUEGO_DISPLAY_BLACK, 20)
    c.setFillColor(NAVY)
    c.drawString(52, H - 58, 'Tu tablero')
    c.setFont(JUEGO_BODY, 9.4)
    c.setFillColor(MUTED)
    _wrap(c, 'Fotocopia esta hoja una vez por jugador. A la izquierda '
             'escondes tu flota; a la derecha anotas tus disparos contra '
             'la del otro.',
         52, H - 76, JUEGO_BODY, 9.4, W - 104, 13, MUTED)

    # las dos rejillas van UNA AL LADO DE LA OTRA, no apiladas: asi usan
    # el ancho entero de la hoja en vez de dejarlo en blanco, y de paso
    # la celda puede ser mas grande — mas comoda para escribir a mano,
    # que es lo que de verdad importa en una hoja que se rellena a boli.
    gutter = 24
    colw = (W - 104 - gutter) / 2.0
    x_izq = 52
    x_der = x_izq + colw + gutter
    cell = 30.0
    y_top = H - 112

    y = _grid(c, x_izq, y_top, cell, 'MI FLOTA',
             'Dibuja tu flota SIN que la vea el otro — luego tápala.')
    y -= 8
    c.setFont(JUEGO_BODY_BOLD, 9.2)
    c.setFillColor(ACCENT)
    c.drawString(x_izq, y, 'TU FLOTA:')
    y -= 13
    piezas = ' · '.join('%s (%s)' % (nombre, ' y '.join([str(tam)] * n))
                        for nombre, tam, n in FLOTA)
    y = _wrap(c, piezas, x_izq, y, JUEGO_BODY, 8.6, colw, 11.6, INK)
    y -= 4
    c.setFont(JUEGO_BODY, 7.8)
    c.setFillColor(MUTED)
    _wrap(c, 'En línea recta, horizontal o vertical — nunca en diagonal — '
             'y sin tocarse entre sí, ni por una esquina.',
         x_izq, y, JUEGO_BODY, 7.8, colw, 10.6, MUTED)

    y2 = _grid(c, x_der, y_top, cell, 'TABLERO DE TIRO',
              'Aquí marcas tus disparos contra el tablero del otro.')
    y2 -= 8
    _leyenda_marcas(c, x_der, y2, colw)

    c.setFont(JUEGO_BODY, 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2.0, 24, 'El Cuaderno del Pianista · T-Clas')
    c.showPage()


# --------------------------------------------------------------------------
def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'Hundir_la_flota_musical.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('Hundir la flota en el teclado')

    _hoja_reglas(c)
    _hoja_juego(c)
    c.save()
    return ruta


def main(argv):
    ruta = construir()
    print('Hundir la flota en el teclado · %s' % os.path.basename(ruta))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
