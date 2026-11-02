# -*- coding: utf-8 -*-
"""NOVIEMBRE · El teclado y sus notas."""
from k1_base import *
from k1_comun import *

MES = 'Noviembre'


def teclado_dos_octavas(**kw):
    return K_teclado(nb=8, **kw)


def construir(d):
    KB.MES_ACTUAL[0] = MES
    d.nuevo('Noviembre')
    d.add(K_titulo('Noviembre', 'El teclado y sus notas', 'Este mes aprendo a encontrar las notas en el piano.'),
          K_mussol('El piano tiene teclas blancas y teclas negras. Las negras van en grupos de dos y de tres.'),
          K_panel('', 'MI PLAN DEL MES', [K_plan(['Encuentro DO, RE, MI, FA, SOL, LA y SI en el teclado.', 'Sé qué mano toca los sonidos graves y cuál los agudos.', 'Conozco la clave de fa.', 'Pongo bien las manos sobre el piano.'])]))
    d.nuevo()
    d.add(K_titulo('Noviembre', 'Las teclas', 'Las notas blancas tienen nombre. Las negras sirven de referencia.'),
          K_mussol('DO está siempre a la izquierda del grupo de 2 teclas negras.'),
          K_panel('', 'MIRA', [K_teclado(nb=8, resalta={0: 'DO', 1: 'RE', 2: 'MI', 3: 'FA', 4: 'SOL', 5: 'LA', 6: 'SI'}, noms='resalta', color=True, h=110)]),
          K_cajita('RECUERDA', 'Las notas se repiten: después de SI vuelve DO.'))
    d.nuevo()
    d.add(K_titulo('Noviembre', 'Manos y territorio', 'Cada mano toca una zona del piano.'),
          K_mussol('La mano derecha toca los sonidos agudos. La mano izquierda toca los graves. El DO central está en medio.'),
          K_panel('', 'MIRA', [Blk(190, lambda c, x, y, w: (K.teclat(c, x + 6, y - 90, w - 12, 80, nb=14, inici=3, noms=None, color=False),
                                                           c.setFillColor(OCRE), c.circle(x + 6 + (w - 12) / 14 * 3.5, y - 80, 5, stroke=0, fill=1),
                                                           txt(c, x + 6 + (w - 12) / 14 * 3.5, y - 108, 'DO CENTRAL', 11, ETQ, NAVY, 'c'),
                                                           txt(c, x + 70, y - 128, '◄ mano izquierda · graves · clave de fa', 11.5, ETQ, OCRE),
                                                           txt(c, x + w - 70, y - 150, 'mano derecha · agudos · clave de sol ►', 11.5, ETQ, OCRE, 'r')))]),
          K_cajita('RECUERDA', 'Dedos curvados, como si sujetaras una pelota pequeña. Muñecas relajadas.'))

    actividad(d, 1, '¿Dónde está cada nota?', 'Cada tecla blanca tiene un nombre.',
              ['Mira el teclado.', 'Escribe el nombre de cada tecla blanca en su casilla.', 'Coloréala de su color.'],
              [K_teclado(nb=8, h=100, casillas=True, titulo='Del DO al DO')])
    sol(MES, 1, '¿Dónde está cada nota?', ['DO RE MI FA SOL LA SI DO'])

    d.nuevo()
    d.add(K_titulo('Noviembre', 'Pausa', 'Es momento de mover el cuerpo.'), K_mussol('Hacemos una pausa.'), K_pausa(2))
    d.nuevo()
    d.add(K_titulo('Noviembre', 'La clave de fa', 'Sirve para las notas graves, las de la mano izquierda.'),
          K_mussol('La clave de fa tiene dos puntos. Los dos puntos rodean la línea 4. Esa línea es FA.'),
          K_panel('', 'MIRA', [K_notas('bass', ['F3', 'G3', 'A3', 'B3', 'C4'], titulo='FA en la línea 4 y las notas siguientes', rotulos='nombre', gap=12)]))

    actividad(d, 2, 'Subo y bajo desde FA', 'La primera nota es FA. Cuenta desde ella.',
              ['FA está en la línea 4.', 'Dibuja las notas que faltan hasta el siguiente FA.', 'Escribe su nombre debajo.'],
              [K_notas('bass', ['F2'] + [None] * 7, nombres=['FA', 'SOL', 'LA', 'SI', 'DO', 'RE', 'MI', 'FA'], titulo='Subiendo', gap=12), K_espacio(8),
               K_notas('bass', ['F3'] + [None] * 7, nombres=['FA', 'MI', 'RE', 'DO', 'SI', 'LA', 'SOL', 'FA'], titulo='Bajando', gap=12)])
    sol(MES, 2, 'Subo y bajo desde FA', ['Subiendo (desde el FA grave): FA SOL LA SI DO RE MI FA · Bajando: FA MI RE DO SI LA SOL FA'])

    actividad(d, 3, 'Busco la nota escondida', 'Los grupos de teclas negras te ayudan a orientarte.',
              ['Lee las notas de la lista.', 'Rodea con un círculo esa tecla blanca.', 'Mira siempre las teclas negras: te dicen dónde estás.'],
              [K_par('DO · MI · SOL · SI', 14, NAVY, bold=True), K_teclado(nb=8, h=90), K_par('RE · FA · LA · DO', 14, NAVY, bold=True), K_teclado(nb=8, h=90)])
    sol(MES, 3, 'Busco la nota escondida', ['Teclado de 8 blancas desde DO: DO=1.ª, RE=2.ª, MI=3.ª, FA=4.ª, SOL=5.ª, LA=6.ª, SI=7.ª, DO=8.ª.'])

    actividad(d, 4, '¿Grave o agudo?', 'La izquierda del piano suena grave. La derecha suena aguda.',
              ['Pinta de azul las 4 teclas de la izquierda.', 'Pinta de rojo las 4 teclas de la derecha.', 'Escribe GRAVE en la parte azul y AGUDO en la parte roja.'],
              [K_teclado(nb=8, h=100), K_lineas(2, '¿Qué parte suena más grave? ¿Y cuál más aguda?', 34)], mes=None)
    d.nuevo()
    d.add(K_titulo('Noviembre', 'Mis logros', 'Mira todo lo que has hecho este mes.'), K_mussol('Pinta una casilla por cada cosa que ya sabes.'),
          K_panel('', 'TABLERO', [K_tablero('noviembre', ['Encuentro las 7 notas en el teclado.', 'Sé dónde está el DO central.', 'Sé qué mano toca graves y cuál agudos.', 'Sé que la clave de fa tiene su FA en la línea 4.'])]))
