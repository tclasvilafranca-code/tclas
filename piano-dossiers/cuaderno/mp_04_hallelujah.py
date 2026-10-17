# -*- coding: utf-8 -*-
"""Pieza 4 · Hallelujah (Leonard Cohen), arreglo de sheetsfree. MEDIDO sobre el PDF (3 pags,
   tamano carta, 17 sistemas de 4 compases = 68 compases): 6/8, "Moderately slow, in 2", negra con
   puntillo = 60, mp, Do mayor sin armadura; barra de repeticion al empezar el c. 5 y casillas
   "1, 2." (c. 29) y "3." (cc. 30-32); doble barra y armadura de dos sostenidos (Re mayor) desde
   el c. 33; "rit." y calderon final; corchea la figura mas corta; izquierda en arpegios de seis
   corcheas por compas (Do, La menor...)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=4, slug='hallelujah', pdf='leonard_cohen_hallelujah.pdf', time_sig=(6, 8),
    titulo='Hallelujah', autor='Leonard Cohen · arreglo para piano (sheetsfree)',
    kicker='Eva · pieza 4 · Hallelujah', mes='Diciembre · 2.ª quincena (concierto de Navidad)',
    yt='https://www.youtube.com/results?search_query=hallelujah+leonard+cohen+piano+tutorial',
    credito='Partitura: Leonard Cohen, Hallelujah (sheetsfree.com). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Do mayor → Re mayor'), ('Compás', '6/8'), ('Tempo', '♩. = 60 lento'),
               ('Figura corta', 'Corchea'), ('Compases', '68')],
        total=68,
        secciones=[('A', 1, 4, 'Introducción', AZUL), ('B', 5, 32, 'Do mayor · se repite', OCRE),
                   ('C', 33, 68, 'Re mayor · final', AZUL)],
        ideas=[('IZQUIERDA', 'Arpegio de seis corcheas',
                'Cada compás, una figura que sube y baja sobre el acorde. Casi no cambia en toda '
                'la pieza.'),
               ('DERECHA', 'Melodía y luego acordes',
                'Empieza con notas sueltas y, al cambiar de tonalidad, pasa a notas dobles con '
                'ligaduras largas.'),
               ('LA REPETICIÓN', 'Tres vueltas, tres casillas',
                'Desde el c. 5 se repite. Las dos primeras veces vas a la casilla 1, 2; la '
                'tercera, a la 3.'),
               ('EL CAMBIO', 'Do mayor → Re mayor',
                'En el c. 33 aparece una doble barra y dos sostenidos: sube un tono.')],
        especial=[
            'Pone "Moderately slow, in 2" y negra con puntillo = 60: lento y a dos.',
            'El compás es 6/8: dos golpes, cada uno de tres corcheas.',
            'Los cc. 5-28 se repiten: casilla "1, 2." (c. 29) y casilla "3." (cc. 30-32).',
            'En el c. 33 hay doble barra y dos sostenidos: Re mayor (fa♯ y do♯).',
            'La izquierda hace el mismo arpegio de seis corcheas casi todo el rato.',
            'Acaba con "rit." y un calderón en el último acorde.'],
        reto='Mantener el arpegio de la izquierda siempre igual mientras la derecha canta, y '
             'acordarse de por dónde se va en las repeticiones y las casillas.',
        truco='Antes de tocar, recorre la partitura con el dedo siguiendo las repeticiones: '
              '5 → 29 → 5 → 29 → 5 → 30-32 → 33. Cuando lo sepas, toca.',
        sabias='Leonard Cohen publicó «Hallelujah» en 1984, en el disco «Various Positions». Se hizo famosa con la versión de Jeff Buckley, de 1994.',
        qr_texto='Escúchala despacio y cuenta "uno-dos" con la cabeza: es un 6/8 lento.',
        ts=(6, 8)),
    manos=dict(
        izq=[('Un arpegio, un compás', 'Cada compás son seis corcheas que suben y bajan sobre el '
                                       'acorde. Toca solo el primer compás, despacio, diez veces '
                                       'seguidas sin fallar.'),
             ('Cambiar de acorde', 'El dibujo es el mismo y cambia la posición. Antes de tocar, '
                                   'mira qué acorde viene y coloca ya la mano.'),
             ('Parejo y suave', 'Metrónomo lento, seis corcheas iguales y en mp: la melodía manda.'),
             ('De memoria', 'Si sabes el dibujo, solo tienes que saber dónde cambia: apréndelo '
                            'sin partitura.')],
        der=[('Contar en dos', 'En 6/8 lento cuentas dos golpes: 1-2-3, 4-5-6. La melodía '
                               'empieza con negras con puntillo.'),
             ('Corchea y puntillo', 'Lee las notas sueltas con su ritmo: dilo en voz alta '
                                    '"ta-a-a ta-a-a" antes de tocar.'),
             ('Notas ligadas y dobles', 'Desde el c. 33 la derecha toca notas dobles con '
                                        'ligaduras: mantén la ligada, no la repitas.'),
             ('Con la izquierda', 'Une despacio un sistema con la izquierda ya segura. Si se '
                                  'rompe, vuelve a una mano.')],
        tecnica=['Muñeca suelta: el arpegio sale solo si no aprietas.',
                 'Cuenta en dos, despacio: 1-2-3, 4-5-6.',
                 'Mira dónde empieza y dónde acaba cada repetición antes de tocar.']),
    bloques=[
        B(1, 'cc. 1-4', 'La introducción', (0, 0),
          D('cuenta', '6/8 lento: dos golpes de tres corcheas', [('un compás', 2, 3)]),
          [('IZQUIERDA', 'Arpegio de seis corcheas por compás: Do, La menor, Do, La menor.'),
           ('DERECHA', 'Notas largas con puntillo; cántalas y cuéntalas enteras.'),
           ('JUNTAS', 'Compás a compás, y después los cuatro.'),
           ('A TEMPO', 'negra con puntillo = 60: muy despacio, en dos.')]),
        B(2, 'cc. 5-12', 'Empieza la repetición', (1, 2),
          D('cadena', 'Desde aquí se repite', [('barra |: en el c. 5', False),
                                              ('tocas hasta la casilla', True)]),
          [('IZQUIERDA', 'El mismo arpegio; cambia el acorde en cada compás.'),
           ('DERECHA', 'Aparecen corcheas y ligaduras entre notas: léelas despacio.'),
           ('JUNTAS', 'Un sistema cada día: cc. 5-8 y cc. 9-12.'),
           ('OJO', 'La barra con puntos del c. 5 marca dónde se vuelve.')]),
        B(3, 'cc. 13-28', 'Lo que se repite', (3, 6),
          D('capas', 'Dos capas a la vez',
            [('Derecha: melodía', 'barras', AZUL), ('Izquierda: arpegio', 'puntos', OCRE)]),
          [('IZQUIERDA', 'Sigue el arpegio: lo difícil es no frenar al cambiar de acorde.'),
           ('DERECHA', 'Las frases acaban en notas largas ligadas: respira ahí.'),
           ('JUNTAS', 'Un sistema cada día hasta el c. 28.'),
           ('OJO', 'Esto se toca tres veces: cuídalo, que lo oirás muchas veces.')]),
        B(4, 'cc. 29-32', 'Las casillas', (7, 7),
          D('cadena', 'Las tres vueltas',
            [('casilla 1, 2 (c. 29)', False), ('↩ al c. 5', False), ('3.ª vez: casilla 3', True)]),
          [('IZQUIERDA', 'Sigue el arpegio en las dos casillas.'),
           ('DERECHA', 'En la casilla 3 hay un compás de silencio: cuéntalo.'),
           ('JUNTAS', 'Recorred el camino con el dedo antes de tocar.'),
           ('OJO', 'Las dos primeras veces, casilla 1, 2 y vuelta al c. 5.')]),
        B(5, 'cc. 33-44', 'Cambio a Re mayor', (8, 10),
          D('cadena', 'La armadura cambia', [('Do mayor: sin alteraciones', False),
                                           ('Re mayor: fa♯ y do♯', True)]),
          [('IZQUIERDA', 'Misma figura, pero ahora con sostenidos: fa♯ y do♯.'),
           ('DERECHA', 'Notas dobles y ligaduras largas: tócalas pesadas y cantadas.'),
           ('JUNTAS', 'Un sistema cada día, sin prisa.'),
           ('OJO', 'Dos sostenidos al principio de cada pentagrama: valen toda la pieza.')]),
        B(6, 'cc. 45-60', 'Re mayor', (11, 14),
          D('capas', 'Dos capas a la vez',
            [('Derecha: notas dobles', 'barras', AZUL), ('Izquierda: arpegio', 'puntos', OCRE)]),
          [('IZQUIERDA', 'El arpegio de siempre en Re mayor: cuida los sostenidos.'),
           ('DERECHA', 'Notas dobles con ligadura: mantén la ligada y cambia la otra.'),
           ('JUNTAS', 'Dos sistemas cada vez.'),
           ('OJO', 'Es el tramo más largo: dividid por sistemas.')]),
        B(7, 'cc. 61-68', 'El final', (15, 16),
          D('cadena', 'Hacia el final', [('notas largas ligadas', False), ('rit.', False),
                                       ('calderón', True)]),
          [('IZQUIERDA', 'Sigue el arpegio hasta el último compás.'),
           ('DERECHA', 'Notas largas ligadas: cuéntalas enteras.'),
           ('JUNTAS', 'Los dos últimos sistemas en bucle.'),
           ('A TEMPO', 'rit.: frena poco a poco. Alarga el último acorde.')]),
    ],
    cortes={1: [225.0, 344.8, 460.5, 583.2], 2: [162.0, 267.8, 387.0, 498.5, 612.5],
            3: [157.8, 266.0, 379.8, 488.8, 596.0]},
    corte_titulo=103.5, inicio={2: 47.0, 3: 44.5}, fin={1: 688.5},
    burb={
        0: [('arriba', 330, 'AMB', 'Moderately slow, in 2: lento y a dos. Negra con puntillo = 60: '
                                   'dos golpes por compás, cada uno de tres corcheas.', 0.3),
            ('abajo', 300, 'IZQ', 'Un arpegio por compás: seis corcheas que suben y bajan. '
                                  'Despacio y parejo.', 0.25)],
        1: [('arriba', 330, 'OJO', 'La barra con puntos al empezar este sistema marca dónde se '
                                   'vuelve cada vez que se repite.', 0.05)],
        4: [('arriba', 300, 'DER', 'Las frases acaban en una nota larga ligada: respira ahí, antes '
                                   'de empezar la siguiente.', 0.5)],
        7: [('arriba', 330, 'OJO', 'Casillas: las dos primeras veces tocas la casilla "1, 2." y '
                                   'vuelves al c. 5. La tercera, la casilla "3.".', 0.3)],
        8: [('arriba', 330, 'AMB', 'Doble barra y dos sostenidos: cambia la tonalidad a Re mayor '
                                   '(fa♯ y do♯ en toda la pieza).', 0.05)],
        9: [('arriba', 330, 'DER', 'Ahora la derecha toca notas dobles con ligaduras: mantén la '
                                   'ligada y no la repitas.', 0.3)],
        13: [('arriba', 300, 'IZQ', 'Misma figura de la izquierda, ahora en Re mayor: cuida los '
                                    'sostenidos.', 0.2)],
        16: [('arriba', 330, 'AMB', 'rit. y calderón: frena poco a poco y alarga el último acorde '
                                    'hasta que se apague.', 0.8)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_hallelujah.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
