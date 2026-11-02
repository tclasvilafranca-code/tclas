# -*- coding: utf-8 -*-
"""DICIEMBRE · Escala de Do mayor."""
from k1_base import *
from k1_comun import *
from n1_base import _abs_idx

MES = 'Diciembre'
ESC = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']


def construir(d):
    KB.MES_ACTUAL[0] = MES
    d.nuevo('Diciembre')
    d.add(K_titulo('Diciembre', 'Escala de Do mayor', 'Este mes toco ocho notas seguidas: la escala de DO.'),
          K_mussol('Una escala son notas que suben o bajan en orden. La escala de DO usa solo teclas blancas.'),
          K_panel('', 'MI PLAN DEL MES', [K_plan(['Toco la escala de DO subiendo y bajando.', 'Uso los números de los dedos.', 'Cuento cuántas notas hay entre dos notas.', 'Escribo una melodía con una canción de Navidad.'])]))
    d.nuevo()
    d.add(K_titulo('Diciembre', 'La escala de DO', 'DO RE MI FA SOL LA SI DO'),
          K_mussol('Son ocho notas seguidas. Subo y después bajo.'),
          K_panel('', 'MIRA', [K_notas('treble', ESC, titulo='Subiendo'), K_espacio(8), K_notas('treble', list(reversed(ESC)), titulo='Bajando')]),
          K_cajita('RECUERDA', 'Se toca con las teclas blancas, de un DO al siguiente DO.'))
    d.nuevo()
    d.add(K_titulo('Diciembre', 'Los números de los dedos', 'Los números te dicen qué dedo usar.'),
          K_mussol('Mano derecha subiendo: 1 2 3, y el pulgar pasa por debajo: 1 2 3 4 5.'),
          K_panel('', 'MIRA', [Blk(120, lambda c, x, y, w: (K.teclat(c, x + 6, y - 90, w - 12, 82, nb=8, dits={i: n for i, n in enumerate([1, 2, 3, 1, 2, 3, 4, 5])}),
                                                           txt(c, x, y - 10, 'MANO DERECHA SUBIENDO', 11, ETQ, OCRE))),
                               Blk(120, lambda c, x, y, w: (K.teclat(c, x + 6, y - 90, w - 12, 82, nb=8, dits={i: n for i, n in enumerate([5, 4, 3, 2, 1, 3, 2, 1])}),
                                                           txt(c, x, y - 10, 'MANO IZQUIERDA SUBIENDO', 11, ETQ, OCRE)))]))
    actividad(d, 1, 'Escribo la escala', 'La primera nota es DO. Escribe las que faltan.',
              ['Dibuja las notas de la escala subiendo.', 'Escribe el nombre debajo.', 'Escribe también el número del dedo de la mano derecha: 1 2 3 1 2 3 4 5.'],
              [K_notas('treble', ['C4'] + [None] * 7, nombres=['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI', 'DO'], titulo='Subiendo')])
    sol(MES, 1, 'Escribo la escala', ['DO RE MI FA SOL LA SI DO — dedos 1 2 3 1 2 3 4 5'])
    d.nuevo('Diciembre')
    d.add(K_titulo('Diciembre', 'Pausa', 'Es momento de mover el cuerpo.'), K_mussol('Hacemos una pausa.'), K_pausa(3))
    r = rnd(30)
    pool = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
    f1 = [r.choice(pool) for _ in range(8)]
    f1[1] = 'C5'; f1[5] = 'C4'
    actividad(d, 2, '¿Dónde está DO?', 'DO aparece en el pentagrama muchas veces.',
              ['Mira todas las notas.', 'Rodea con un círculo rojo las notas que son DO.', 'Escribe el nombre de cada nota en su casilla.'],
              [K_notas('treble', f1, rotulos='caja', color=False)])
    sol(MES, 2, '¿Dónde está DO?', [' · '.join(nom_nota(p) for p in f1)])
    d.nuevo()
    d.add(K_titulo('Diciembre', 'Intervalos', 'Un intervalo es la distancia entre dos notas.'),
          K_mussol('Para saber la distancia, cuenta las dos notas. De DO a MI: DO, RE, MI. Son 3.'),
          K_panel('', 'MIRA', [K_notas('treble', ['C4', 'D4', 'E4'], titulo='DO – MI = 3', nombres=['1', '2', '3'], color=False), K_espacio(8),
                               K_notas('treble', ['C4', 'D4', 'E4', 'F4', 'G4'], titulo='DO – SOL = 5', nombres=['1', '2', '3', '4', '5'], color=False)]))
    actividad(d, 3, 'Cuento las notas', 'Usa la escala como ayuda y cuenta con los dedos.',
              ['Cuenta las dos notas de cada pareja.', 'Escribe el número.'],
              [K_vf(['DO – FA = ___', 'RE – LA = ___', 'MI – SOL = ___', 'FA – SI = ___', 'SOL – DO agudo = ___', 'DO – DO agudo = ___'], 14)])
    sol(MES, 3, 'Cuento las notas', ['DO–FA 4 · RE–LA 5 · MI–SOL 3 · FA–SI 4 · SOL–DO agudo 5 · DO–DO agudo 8'])
    # villancico
    d.nuevo()
    ev = ['E4', 'E4', 'E4']
    d.add(K_titulo('Diciembre', 'Mi villancico', 'Copio una melodía y le pongo mi propia letra.'),
          K_mussol('Esta melodía es el principio de Jingle Bells. Cópiala en el pentagrama.'),
          K_panel('', 'MELODÍA PARA COPIAR', [K_notas('treble', ['E4', 'E4', 'E4', 'E4', 'E4', 'E4', 'E4', 'G4', 'C4', 'D4', 'E4'], titulo='Jingle Bells · J. Pierpont (1857)', gap=11),
                                             K_espacio(8), K_pauta_vacia('treble', 1, 11, 'Copia aquí'), K_lineas(2, 'Mi letra', 30), K_hecho()]))
    sol(MES, 4, 'Mi villancico', ['Mi Mi Mi (blanca) · Mi Mi Mi (blanca) · Mi Sol Do Re · Mi (redonda). Aquí cada nota va con la misma figura para copiar; el ritmo real lo toca el profesor.'])
    d.nuevo()
    d.add(K_titulo('Diciembre', 'Mis logros', 'Mira todo lo que has hecho este mes.'), K_mussol('Pinta una casilla por cada cosa que ya sabes.'),
          K_panel('', 'TABLERO', [K_tablero('diciembre', ['Sé las 8 notas de la escala de DO.', 'Sé los números de los dedos.', 'Sé encontrar DO en el pentagrama.', 'Sé contar la distancia entre dos notas.'])]))
