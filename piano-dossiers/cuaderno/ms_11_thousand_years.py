# -*- coding: utf-8 -*-
"""Pieza 11 · A Thousand Years (Christina Perri y David Hodges), arreglo de Piano Seeds STUDIO.
   MEDIDO sobre el PDF de Drive: 2 paginas A4, 33 compases, sin armadura (Do mayor: acaba en un
   acorde de Do), 6/8, sin tempo ni matices impresos, sin repeticiones, dedos impresos por el
   arreglista, corchea como figura mas corta (cc. 8, 10, 12-14, 16-19, 25-30). Derecha en
   intervalos de negra con puntillo los cc. 1-8, izquierda en acordes de tres notas desde el c. 9;
   las notas mas altas (lineas adicionales encima del pentagrama) estan en los cc. 22-24;
   ligadura de union de acorde entre los cc. 21 y 22."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=11, slug='thousand_years', pdf='copia_de_a_thousand_years.pdf', time_sig=(6, 8),
    titulo='A Thousand Years', autor='Christina Perri y David Hodges · arreglo de Piano Seeds STUDIO',
    kicker='Sharifa · pieza 11 · A Thousand Years', mes='Mayo · 2.ª quincena',
    yt='https://www.youtube.com/results?search_query=christina+perri+a+thousand+years+piano+tutorial',
    credito='Partitura: arreglo de Piano Seeds STUDIO (copia de Drive). Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '6/8'), ('Carácter', 'Sin tempo escrito'),
               ('Figura corta', 'Corchea'), ('Compases', '33')],
        total=33,
        secciones=[('A', 1, 8, 'Introducción', AZUL),
                   ('B', 9, 17, 'Primera frase', OCRE),
                   ('C', 18, 24, 'La melodía sube', AZUL),
                   ('D', 25, 33, 'Final', OCRE)],
        ideas=[('INTRODUCCIÓN', 'Solo dos notas',
                'En los cc. 1-8 la derecha toca dos notas a la vez, dos veces por compás. '
                'La izquierda, una nota larga.'),
               ('IZQUIERDA', 'Acordes de tres notas',
                'Desde el c. 9 la izquierda toca acordes, casi siempre uno por compás.'),
               ('DERECHA', 'Melodía de notas largas',
                'Notas largas con puntillo y grupos de tres corcheas que bajan.'),
               ('LO MÁS ALTO', 'Cc. 22-24',
                'Las notas más agudas están en estos compases, con rayitas encima del pentagrama.')],
        especial=[
            'Es 6/8: dos golpes por compás, cada uno con tres corcheas.',
            'No hay armadura: no hay sostenidos ni bemoles. Termina en un acorde de Do mayor.',
            'La partitura no pone tempo ni matices: eliges tú un pulso lento y cómodo.',
            'Tu partitura trae números de dedo escritos por el arreglista; úsalos si te ayudan.',
            'Hay una ligadura de acorde entre los cc. 21 y 22: se toca una vez y se deja sonar.',
            'No hay repeticiones: son 33 compases, de principio a fin.'],
        reto='Tocar las notas altas de los cc. 22-24 sin que la mano se tense, y que la '
             'izquierda no se despiste mientras tanto.',
        truco='Aprende la introducción (cc. 1-8) de memoria: son dos notas, y te deja mirar la mano '
              'izquierda al empezar la melodía.',
        sabias='«A Thousand Years» (2011) fue escrita por Christina Perri y David Hodges para la banda '
               'sonora de la película «Crepúsculo: Amanecer, parte 1».',
        qr_texto='Escúchala con la partitura delante y cuenta dos golpes por compás.',
        ts=(6, 8), cuenta_pie='Un compás de 6/8: dos golpes, cada uno con tres corcheas. Aquí '
                              'solo el ritmo, sobre una nota cualquiera.'),
    manos=dict(
        izq=[('Una nota larga', 'En los cc. 1-8 la izquierda toca una sola nota larga, a veces '
                                'ligada al compás siguiente. Cuenta 1-2-3, 4-5-6.'),
             ('Un acorde, un compás', 'Desde el c. 9 hay un acorde de tres notas por compás. '
                                      'Pon la mano en forma y baja las tres a la vez.'),
             ('Dos acordes por compás', 'En los cc. 25-33 el acorde cambia en cada golpe. '
                                        'Cuenta 1-2-3, 4-5-6.'),
             ('De memoria', 'Los acordes se repiten mucho: aprende la izquierda sin mirar.')],
        der=[('Dos notas a la vez', 'En los cc. 1-8 la derecha toca intervalos de dos notas, dos '
                                    'veces por compás. Tócalas juntas y parejas.'),
             ('Notas con puntillo', 'La melodía va en negras con puntillo: cada una dura tres '
                                    'corcheas. Cuenta 1-2-3.'),
             ('Las corcheas', 'Los grupos de tres corcheas bajan paso a paso. Tócalas tranquilas, '
                              'no corras.'),
             ('Las notas altas', 'En los cc. 22-24 hay notas con rayitas encima del pentagrama. '
                                 'Léelas despacio y di su nombre.')],
        tecnica=['Muñeca suelta y brazo pesado: el sonido es dulce, no golpeado.',
                 'Cuenta dos golpes largos por compás (1-2-3, 4-5-6).',
                 'Empieza muy lenta y sube el pulso poco a poco.']),
    bloques=[
        B(1, 'cc. 1-4', 'Introducción', (0, 0),
          D('grupos', 'Un compás de 6/8 = 2 golpes · 3 corcheas cada uno',
            (2, 3, ['golpe 1', 'golpe 2'])),
          [('DERECHA', 'Dos notas a la vez, dos veces por compás. Cuenta 1-2-3, 4-5-6.'),
           ('IZQUIERDA', 'Una nota larga por compás, ligada a la siguiente.'),
           ('JUNTAS', 'Empieza con la derecha y la izquierda juntas: los cuatro compases.'),
           ('A TEMPO', 'Muy despacio. Elige un pulso que puedas mantener.')]),
        B(2, 'cc. 5-8', 'La introducción sigue', (1, 1),
          D('cadena', 'Para entrar en la melodía', [('dos notas', False), ('dos notas', False),
                                                    ('3 corcheas', True)]),
          [('DERECHA', 'Mismas dos notas y, en el c. 8, tres corcheas que bajan.'),
           ('IZQUIERDA', 'Una nota larga por compás. En el c. 8 toca una nota y descansa el segundo golpe.'),
           ('JUNTAS', 'Los cuatro compases en bucle.'),
           ('OJO', 'En el c. 8 la izquierda descansa en el segundo golpe: cuéntalo.')]),
        B(3, 'cc. 9-11', 'Entra la melodía', (2, 2),
          D('cadena', 'En el compás', [('nota con puntillo', False), ('tres corcheas', True)]),
          [('DERECHA', 'Dos notas con puntillo y, en el c. 10, tres corcheas que bajan.'),
           ('IZQUIERDA', 'Acorde de tres notas, uno por compás, en clave de fa.'),
           ('JUNTAS', 'Cuenta 1-2-3, 4-5-6 y toca los tres compases.'),
           ('OJO', 'En el c. 9 empieza la melodía: antes de este compás solo había dos notas.')]),
        B(4, 'cc. 12-14', 'Sigue la frase', (3, 3),
          D('cadena', 'La frase', [('nota larga', False), ('corcheas', False),
                                   ('nota larga', True)]),
          [('DERECHA', 'Combina notas largas con grupos de corcheas.'),
           ('IZQUIERDA', 'Un acorde por compás, igual que en el bloque anterior.'),
           ('JUNTAS', 'Los tres compases, despacio, sin pararte.'),
           ('A TEMPO', 'Cuenta dos golpes por compás.')]),
        B(5, 'cc. 15-17', 'Se prepara el cambio', (4, 4),
          D('cadena', 'El camino', [('c. 15', False), ('c. 16', False), ('c. 17', True)]),
          [('DERECHA', 'Sigue con notas largas y corcheas. El c. 17 acaba la frase.'),
           ('IZQUIERDA', 'Un acorde por compás.'),
           ('JUNTAS', 'Los cc. 15-17 y la entrada del c. 18.'),
           ('OJO', 'Antes del c. 18 respira: empieza otra frase.')]),
        B(6, 'cc. 18-20', 'La frase continúa', (5, 5),
          D('cadena', 'El camino', [('nota larga', False), ('corcheas', False), ('nota larga',
                                                                                   True)]),
          [('DERECHA', 'Notas largas y corcheas, parecido a los cc. 12-14.'),
           ('IZQUIERDA', 'Un acorde por compás, igual que antes.'),
           ('JUNTAS', 'Cuenta 1-2-3, 4-5-6 en cada compás.'),
           ('A TEMPO', 'Los cc. 15-20 seguidos, sin parar.')]),
        B(7, 'cc. 21-24', 'La melodía sube', (6, 6),
          D('cadena', 'Hacia lo más alto', [('c. 21', False), ('c. 22', False),
                                            ('c. 23-24', True)]),
          [('DERECHA', 'Las notas suben y llegan a las más altas de la pieza (cc. 22-24).'),
           ('IZQUIERDA', 'Acorde largo ligado entre los cc. 21 y 22: se toca una vez.'),
           ('JUNTAS', 'Los cuatro compases, despacio. Di el nombre de las notas altas.'),
           ('OJO', 'Las rayitas encima del pentagrama son notas muy agudas.')]),
        B(8, 'cc. 25-33', 'Final', (7, 9),
          D('cadena', 'Hacia el final',
            [('6 corcheas', False), ('ligaduras', False), ('notas largas', False),
             ('Do', True)]),
          [('DERECHA', 'Seis corcheas por compás en los cc. 25-27. Al final, notas largas que bajan.'),
           ('IZQUIERDA', 'Dos acordes por compás (uno por golpe) en los cc. 25-33.'),
           ('JUNTAS', 'Tres tramos: cc. 25-27, 28-30 y 31-33.'),
           ('A TEMPO', 'La pieza entera, sin parar, hasta el acorde final de Do mayor.')]),
    ],
    cortes={1: [254.2, 388.8, 549.2, 679.5], 2: [211.0, 365.8, 522.2, 680.2]},
    corte_titulo=127.5, fin={1: 822.0, 2: 806.0},
    burb={
        0: [('abajo', 330, 'AMB', 'Introducción: la derecha toca dos notas a la vez, dos veces por '
                                  'compás. La izquierda sostiene una nota larga.', 0.3)],
        1: [('abajo', 330, 'OJO', 'En el c. 8 llegan tres corcheas que bajan y llevan a la melodía '
                                  'del c. 9.', 0.9)],
        2: [('arriba', 330, 'IZQ', 'Desde aquí, un acorde de tres notas por compás. Baja las tres '
                                   'a la vez.', 0.1),
            ('abajo', 330, 'DER', 'Entra la melodía: dos notas largas, y en el c. 10, tres '
                                  'corcheas que bajan.', 0.5)],
        3: [('arriba', 330, 'DER', 'Notas largas y grupos de corcheas: cuenta 1-2-3, 4-5-6.',
             0.2)],
        4: [('arriba', 330, 'OJO', 'Fin de la primera frase: respira antes del c. 18.', 0.3)],
        5: [('arriba', 330, 'AMB', 'Misma forma que en los cc. 12-14: notas largas y grupos de '
                                   'tres corcheas.', 0.2)],
        6: [('arriba', 330, 'DER', 'Las notas suben: las más altas de la pieza están en los '
                                   'cc. 22-24 (rayitas encima del pentagrama).', 0.3),
            ('abajo', 330, 'IZQ', 'Acorde ligado entre los cc. 21 y 22: se toca una vez y se '
                                  'deja sonar.', 0.15)],
        7: [('arriba', 330, 'DER', 'Seis corcheas por compás. En la izquierda, dos acordes por '
                                   'compás.', 0.2)],
        8: [('arriba', 330, 'OJO', 'Las ligaduras de los cc. 29-30 unen notas iguales: se '
                                   'tocan una sola vez.', 0.5)],
        9: [('arriba', 330, 'AMB', 'Las notas bajan paso a paso. El último acorde, de Do mayor, '
                                   'se deja sonar entero.', 0.4)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia un compás o escribe la escala de Do mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_thousand_years.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
