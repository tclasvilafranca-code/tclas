# -*- coding: utf-8 -*-
"""Amiga Mía (canción 9 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico). ATENCIÓN: de esta pieza NO
   se cita ninguna altura, ni en el cuaderno de Dilan ni en este. La izquierda
   va en redondas (cabezas huecas que el lector no distingue) y la derecha es
   muy densa: no hay medición fiable. Lo que sí se ve sin ambigüedad es la
   TEXTURA —la derecha lleva dos voces y la izquierda solo sostiene— y eso es
   lo que trabaja el cuaderno. Todo lo escrito aquí es ANDAMIO con los grados
   de Re mayor, y está rotulado como tal.

   Camino distinto al de Dilan, y aquí el andamio también es distinto (no hay
   nada que citar, así que ni siquiera coincide la materia):

     - A Dilan se le da la textura tal cual: abajo quieto, arriba moviéndose,
       cada vez más largo.
     - A Eva se le da además LA VUELTA: un sistema entero con la voz de ARRIBA
       quieta y la de ABAJO moviéndose. Es la combinación que nadie practica y
       la que de verdad prueba si los dedos son independientes o si lo que
       pasa es que el 4 y el 5 se mueven porque el 1 los arrastra.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import sistemas_extra, bloque_tresillos, bloques_extra
from dilan_07_amiga import n

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
RE = 'Re mayor'


def d(a, b, dur='q'):
    """Las dos voces de la mano derecha, en un solo golpe."""
    return {'pitches': [a, b], 'dur': dur}


CANCION = dict(
    alumno='Eva', num=9, nivel='avanzado', slug='AmigaMia',
    titulo_corto='Amiga Mía', time_sig=(4, 4), key_sig=RE,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'Amiga mia-alejandro Sanz.pdf'),
    yt='https://www.youtube.com/results?search_query=alejandro+sanz+amiga+mia',

    ficha=dict(
        titulo='Amiga Mía', autor='Alejandro Sanz (2000) · edición con letra',
        datos=[('Tonalidad', 'Re mayor'), ('Compás', '4/4'), ('Tempo', 'Lento'),
               ('Mano izq.', 'Redondas'), ('Mano dcha.', 'Dos voces')],
        armonia=dict(
            titulo='Toda la dificultad está en una sola mano',
            tarjetas=[
                ('LA IZQUIERDA', 'Una nota',
                 'Redondas: una sola nota por compás, sostenida los cuatro tiempos.'),
                ('LA DERECHA', 'Dos a la vez',
                 'Sostiene una nota abajo mientras los dedos de arriba mueven la melodía.'),
                ('POR ESO CUESTA', 'Dos a la vez',
                 'El 1 y el 2 se quedan apretando; el 4 y el 5 tienen que correr.'),
                ('EL TRESILLO', 'Tres en dos',
                 'Marcado con un 3. Aparece varias veces y descoloca si no lo cuentas.'),
            ],
            pie='Casi todas las canciones reparten el trabajo entre las dos manos. Esta no: la '
                'izquierda no hace nada y la derecha hace las dos cosas. Por eso una pieza que sobre '
                'el papel parece la más fácil del cuaderno acaba siendo de las que más cuestan.',
        ),
        ritmos=[
            ('MD', 'dos voces en el mismo golpe: la de abajo aguanta (andamio)',
             [d('D4', 'A4'), d('D4', 'B4'), d('D4', 'C#5'), d('D4', 'B4')], AZUL, 'treble', RE),
            ('MI', 'una redonda por compás, y ya (andamio)',
             [n('D2', 'w')], OCRE, 'bass', RE),
        ],
        especial=[
            'Armadura de Re mayor: dos sostenidos, Fa♯ y Do♯.',
            'La izquierda va en redondas: se ataca una vez y se deja sonar los cuatro tiempos.',
            'La derecha lleva DOS voces escritas en el mismo pentagrama.',
            'Hay tresillos marcados con un 3 en varios sitios.',
            'La edición trae la letra debajo: cada sílaba dice dónde cae una nota.',
            'Pone Lento. Aquí no hay ninguna prisa por correr.',
        ],
        reto='Que la nota de abajo de la mano derecha no se corte nunca mientras los dedos de arriba '
             'se mueven. Es un problema de dedos independientes, no de velocidad: por eso tocarlo más '
             'despacio no lo arregla solo, hay que mirarlo de frente.',
        truco='Prueba la vuelta: aguanta la de ARRIBA y mueve la de ABAJO. Si eso te sale mucho peor, '
              'ya sabes lo que pasaba — los dedos de arriba se movían porque el pulgar los arrastraba, '
              'no porque fueran solos. Trabaja las dos direcciones y la textura de la pieza se cae de '
              'madura.',
        sabias='Alejandro Sanz la escribió pensando en una amiga de verdad, y la letra está en primera '
               'persona todo el rato. Por eso la edición la trae escrita debajo del pentagrama: si '
               'cantas la letra mientras tocas, el fraseo se coloca solo y no hace falta pensarlo.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en cómo la voz respira. La mano tiene que respirar ahí mismo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Aviso: de esta partitura no se citan notas. Su izquierda va en redondas y su derecha es '
              'muy densa, y no he podido medirlas con seguridad. Todo lo de aquí es ANDAMIO con los '
              'grados de Re mayor para trabajar EL GESTO; las notas están en la partitura de la '
              'página 1. Y el gesto es el problema entero: una mano haciendo dos cosas a la vez.',
        reglas=['ESTO ES ANDAMIO, NO LA PIEZA', 'EL PULGAR NO SE LEVANTA', 'LENTO'],
        bloques=[
            dict(num=1, titulo='Una mano, dos trabajos',
                 pista='andamio · la de abajo se ataca y se queda; la de arriba hace la frase',
                 sistemas=[
                     dict(cap='a) la de abajo clavada en el Re, la de arriba por grados · el dedo 1 no '
                              'se levanta ni una vez',
                          events=[d('D4', 'A4'), d('D4', 'B4'), d('D4', 'C#5'), d('D4', 'B4'),
                                  d('D4', 'A4'), d('D4', 'G4'), d('D4', 'F#4'), d('D4', 'G4'),
                                  d('D4', 'A4', 'w')],
                          bars=3),
                     dict(cap='b) y ahora al revés: la de ARRIBA quieta y la de ABAJO moviéndose · '
                              'esto no lo practica casi nadie, y es lo que de verdad prueba los dedos',
                          events=[d('D4', 'A4'), d('E4', 'A4'), d('F#4', 'A4'), d('E4', 'A4'),
                                  d('D4', 'A4'), d('C#4', 'A4'), d('B3', 'A4'), d('C#4', 'A4'),
                                  d('D4', 'A4', 'w')],
                          bars=3, show_time=False),
                     dict(cap='c) otra vez como en la pieza, pero con la de arriba saltando · si se '
                              'corta la de abajo, vuelve a la a) y no sigas',
                          events=[d('D4', 'A4'), d('D4', 'D5'), d('D4', 'F#5'), d('D4', 'D5'),
                                  d('D4', 'B4'), d('D4', 'E5'), d('D4', 'G5'), d('D4', 'E5'),
                                  d('D4', 'D5', 'w')],
                          bars=3, show_time=False),
                     dict(cap='d) y alternando sin parar · un compás manda la de arriba y el siguiente '
                              'manda la de abajo: aquí es donde se nota si la mano ha entendido',
                          events=[d('D4', 'A4'), d('D4', 'B4'), d('D4', 'C#5'), d('D4', 'B4'),
                                  d('D4', 'A4'), d('E4', 'A4'), d('F#4', 'A4'), d('E4', 'A4'),
                                  d('D4', 'A4', 'w')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='PARA QUÉ SIRVE LA VUELTA DEL EJERCICIO b)',
                 texto='Si la a) te sale y la b) te sale mucho peor, ya sabes lo que estaba pasando: los '
                       'dedos de arriba se movían porque el pulgar tiraba de ellos, no porque fueran '
                       'solos. En cuanto le das la vuelta al reparto, el truco deja de funcionar y '
                       'aparece la verdad. Trabaja las dos direcciones el mismo rato: la textura de esta '
                       'canción se cae de madura después.'),
            dict(num=2, titulo='Y la izquierda, que aquí no hace nada',
                 pista='andamio · una redonda por compás: atacar, soltar el brazo y no volver a tocar',
                 sistemas=[
                     dict(cap='a) la voz de abajo sola, sostenida · cuenta los cuatro tiempos en voz '
                              'alta y comprueba que sigue sonando al llegar al cuatro',
                          events=[n('B3', 'w'), n('D4', 'w'), n('B3', 'w'), n('E4', 'w')],
                          bars=4),
                     dict(cap='b) y la izquierda · el brazo se queda muerto encima de la tecla, no '
                              'apretando: si aprietas, el hombro se carga y no te enteras hasta el final',
                          events=[n(p, 'w') for p in ('D2', 'F#2', 'G2', 'A2',
                                                      'B2', 'G2', 'A2', 'D2')],
                          bars=8, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='El gesto ya está en los dedos. Ahora se alarga hasta donde dura una frase de verdad, y '
              'se le pone la letra encima, que es lo que coloca el fraseo sin tener que pensarlo.',
        reglas=['CANTA LA LETRA MIENTRAS TOCAS', 'SI SE CORTA, VUELVE AL PRINCIPIO', 'LENTO DE VERDAD'],
        bloques=[
            dict(num=3, titulo='La frase entera, sin cortar la de abajo',
                 pista='andamio · ocho compases seguidos, que es lo que dura una frase de la canción',
                 sistemas=[
                     dict(cap='a) si te cortas, no repitas ese compás: vuelve al principio de los ocho, '
                              'porque lo que se entrena es aguantar, no acertar',
                          events=[d('D4', 'D5', 'h'), d('D4', 'C#5', 'h'),
                                  d('D4', 'B4', 'h'), d('D4', 'A4', 'h'),
                                  d('B3', 'B4', 'h'), d('B3', 'A4', 'h'),
                                  d('B3', 'G4', 'h'), d('B3', 'A4', 'h'),
                                  d('E4', 'C#5', 'h'), d('E4', 'D5', 'h'),
                                  d('E4', 'E5', 'h'), d('E4', 'D5', 'h'),
                                  d('D4', 'F#5', 'h'), d('D4', 'E5', 'h'),
                                  d('D4', 'D5', 'w')],
                          bars=4),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL TRESILLO, Y LA LETRA',
                 texto='Cuando veas un 3 encima de un grupo, ahí caben tres notas donde normalmente '
                       'caben dos. No se toca más rápido: se reparte el mismo tiempo entre tres. Di '
                       '“man-za-na” mientras el pie marca dos golpes. Y usa la letra que trae la '
                       'edición: cada sílaba te dice dónde cae una nota, y donde respira la voz respira '
                       'la mano. Canta “A-mi-ga mí-a, lo sé…” y el fraseo se coloca solo.'),
            dict(num=4, titulo='Y ahora escucha lo que estabas tapando',
                 pista='andamio · la voz de arriba sola, que es la que se oye desde fuera',
                 sistemas=[
                     dict(cap='a) cántala mientras la tocas · esta es la línea que el oyente sigue; '
                              'todo lo demás es el colchón donde se apoya',
                          events=[n(p, 'h') for p in ('D5', 'E5', 'F#5', 'E5', 'D5', 'C#5', 'B4', 'C#5',
                                                      'D5', 'F#5', 'A5', 'G5', 'F#5', 'E5')] +
                                 [n('D5', 'w')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA PRUEBA QUE NO ENGAÑA',
                 texto='Toca el paso 3 y canta en voz alta la nota de ABAJO, la que estás sosteniendo, '
                       'no la de arriba. Si dejas de oírla, es que el dedo se te ha levantado. Nadie '
                       'tiene que decírtelo: lo oyes tú, y por eso este es el único control que hace '
                       'falta en esta pieza.'),
            dict(tipo='escalera', valores=[40, 46, 52, 58, 64, 70],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('Re mayor', 'D4', 'D3', time_sig=(4, 4),
                               variante=56, letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2

# La escalera de tempo pasa de la segunda hoja de estudio a la primera: es
# papel, no pentagrama, así que se mueve sin perder nada, y con ella fuera la
# segunda vuelve a caber en una hoja en vez de abrir una cuarta casi vacía.
_ESC = [b for b in CANCION['piano2']['bloques'] if b.get('tipo') == 'escalera']
if _ESC:
    CANCION['piano2']['bloques'] = [b for b in CANCION['piano2']['bloques']
                                    if b.get('tipo') != 'escalera']
    CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + _ESC

# El recurso que la pieza EXPLICA y no dibujaba: durante meses se anotó como
# "no cabe en la hoja". Desde que la hoja se pagina sola, esa excusa dejó de
# ser cierta.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Re mayor', 61, 'D4', 'D3',
    'la mano en el tono antes de los tresillos',
    desde=5, time_sig=(4, 4)) + [
    bloque_tresillos('Re mayor', 4, 'D4', 'los tresillos marcados con un 3', time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
