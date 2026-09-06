# -*- coding: utf-8 -*-
"""Simón dice musical — el único de los juegos de clase que no necesita ni
   tablero ni fichas: es un juego de voz y de cuerpo, se juega de pie, y lo
   único que hace falta es esta hoja.

   POR QUÉ ASÍ. Mismo encargo que la Oca y el Scrabble: es para el final de
   clase, para pasarlo bien. Pero un Simón dice no tiene casillas que
   recortar — su material es la CADENA que va inventando quien hace de
   Simón, ronda a ronda. Lo único que de verdad hacía falta imprimir no
   eran fichas: era un repertorio amplio de acciones para que Simón no se
   quede repitiendo las mismas tres siempre (la hoja 2).

   DOS FORMAS DE JUGAR, no una — para que no se agote a la tercera partida:

     MEMORIA  Simón dice una acción; el grupo la repite. Ronda a ronda
              Simón añade una acción más a la cadena. Se pierde por
              olvidar el orden.
     TRAMPA   El juego de "Simón dice" de toda la vida: solo se obedece si
              Simón ha dicho "Simón dice" antes de la acción. Se pierde por
              obedecer sin que lo haya dicho — o por no obedecer cuando sí
              lo ha dicho.

   El repertorio de acciones reutiliza a propósito el mismo vocabulario que
   el UNO y la Oca musicales (los instrumentos, los símbolos de silencio y
   calderón, las dinámicas) — un alumno que ya los reconoce de los otros
   juegos entra jugando desde la primera ronda.

   Uso:  python3 juego_simon.py
"""
import os
import sys

from reportlab.pdfgen import canvas as rl_canvas

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

from juegos_comun import (W, H, NAVY, CREAM, INK, MUTED, ACCENT,             # noqa: E402
                          portada_juego, INSTRUMENTOS)
from portada import _wrap                                                    # noqa: E402

SALIDA = os.path.join(HERE, '..', 'output', 'juegos')

# INSTRUMENTOS trae las claves en minuscula y sin tilde porque son las que
# usa internamente `instrumento()` para elegir el dibujo — no estan
# pensadas para imprimirse tal cual (perderian la tilde: "violin", no
# "Violín"). Este mapa es solo el nombre bien escrito de cada una.
NOMBRE_INSTRUMENTO = {
    'guitarra': 'Guitarra', 'piano': 'Piano', 'tambor': 'Tambor',
    'trompeta': 'Trompeta', 'violin': 'Violín', 'saxofon': 'Saxofón',
    'maracas': 'Maracas', 'pandereta': 'Pandereta', 'xilofono': 'Xilófono',
    'acordeon': 'Acordeón', 'trombon': 'Trombón', 'arpa': 'Arpa',
    'platillos': 'Platillos', 'microfono': 'Micrófono', 'flauta': 'Flauta',
}

# --------------------------------------------------------------------------
# El repertorio de Simón — el "mazo" de este juego, aunque no se recorte
# --------------------------------------------------------------------------
REPERTORIO = {
    'Notas (cantadas o tocadas)': [
        'DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI',
    ],
    'Ritmos y silencios': [
        'una palmada (negra)', 'dos palmadas rápidas (corcheas)',
        'un pisotón', 'un chasquido de dedos',
        'silencio — te quedas quieto y callado',
    ],
    'Dinámica': [
        'forte — fuerte', 'piano — flojito',
        'un crescendo — subes el volumen poco a poco',
    ],
    'Instrumentos imaginarios (mímica)': [
        NOMBRE_INSTRUMENTO[i] for i in INSTRUMENTOS
    ],
    'Gestos de director': [
        'marca el compás con la mano', 'accelerando — más rápido',
        'ritardando — más despacio',
    ],
}


def reglas():
    return [
        'Uno hace de Simón (empieza el profesor, luego cualquiera); el '
        'resto responde de pie, todos a la vez.',
        'Elegid una de las dos formas de jugar antes de empezar — o '
        'cambiad a mitad de partida para variar.',
        'MODO MEMORIA: Simón dice una acción de la hoja siguiente '
        '("Do"). El grupo la repite. Simón la repite y añade una más '
        '("Do, palmada"). Así ronda a ronda, cada vez la cadena es más '
        'larga.',
        'En el modo memoria se pierde por decir la cadena en el orden '
        'que no es, o por olvidar una acción. Quien se pierde se sienta '
        '— o, si preferís no eliminar a nadie, simplemente empieza otra '
        'vez la cadena desde cero.',
        'MODO TRAMPA: Simón dice acciones sueltas. El grupo solo obedece '
        'si Simón ha dicho "Simón dice…" ANTES de la acción. Si Simón la '
        'dice sin ese preámbulo y alguien la hace igual, esa persona '
        'queda eliminada — igual que si no obedece cuando sí tocaba.',
        'Simón puede repetir acciones, mezclarlas, hacerlas más rápido o '
        'despacio: cuanto más varíe, más cuesta seguirle.',
        'Cambiad quién hace de Simón cada 2 o 3 rondas, para que todos '
        'prueben a dirigir y no solo a seguir.',
    ]


MATERIALES = [
    'Nada que recortar — el material de este juego es la hoja siguiente, '
    'que Simón consulta mientras juega.',
    'Si hay un teclado o un piano a mano, Simón puede tocar la nota de '
    'verdad en vez de solo cantarla; no hace falta para jugar.',
    'De 3 jugadores en adelante — cuantos más, más divertido.',
]


def _hoja_reglas(c):
    return portada_juego(
        c, 'Simón dice musical', 'El único juego de la colección que no necesita ni tablero ni fichas',
        None,
        'Es el Simón dice de toda la vida, con acciones musicales en vez '
        'de "tócate la nariz": notas cantadas, ritmos con las manos, '
        'instrumentos de mentira, dinámicas de fuerte y flojito. Se juega '
        'de pie, sin nada que montar, y vale para las dos versiones '
        'clásicas del juego — la de memoria y la del despiste.',
        reglas(), MATERIALES)


# --------------------------------------------------------------------------
# La hoja del repertorio
# --------------------------------------------------------------------------
def _hoja_repertorio(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFont('DejaVuSerif-Bold', 22)
    c.setFillColor(NAVY)
    c.drawString(52, H - 78, 'El repertorio de Simón')
    c.setFont('DejaVuSans', 10)
    c.setFillColor(MUTED)
    _wrap(c, 'Todo lo que Simón puede pedir — mézclalo, repítelo, cambia '
             'el orden. Cuantas más categorías uses en una partida, más '
             'cuesta seguirte.',
         52, H - 98, 'DejaVuSans', 10, W - 104, 14, MUTED)

    categorias = list(REPERTORIO.items())
    gutter = 22
    colw = (W - 104 - gutter) / 2.0
    col_izq = categorias[0::2]
    col_der = categorias[1::2]

    def _columna(x0, cats):
        y = H - 140
        for titulo, acciones in cats:
            c.setFont('DejaVuSans-Bold', 10.6)
            c.setFillColor(ACCENT)
            c.drawString(x0, y, titulo.upper())
            c.setStrokeColor(ACCENT)
            c.setLineWidth(1.1)
            c.line(x0, y - 4, x0 + colw, y - 4)
            y -= 18
            texto = ' · '.join(acciones)
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
def construir():
    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, 'Simon_dice_musical.pdf')
    c = rl_canvas.Canvas(ruta, pagesize=(W, H))
    c.setTitle('Simón dice musical')

    _hoja_reglas(c)
    _hoja_repertorio(c)
    c.save()
    return ruta


def main(argv):
    ruta = construir()
    print('Simón dice musical · %s' % os.path.basename(ruta))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
