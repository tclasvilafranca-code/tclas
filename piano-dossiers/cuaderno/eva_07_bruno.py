# -*- coding: utf-8 -*-
"""When I Was Your Man (canción 7 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico), así que el material medido
   se importa de `dilan_09_bruno`. Ver TRANSCRIPCION_D09_11.md.

   Camino distinto al de Dilan:

     - A Dilan se le entra por el ARPEGIO ya hecho, y después se le reduce a
       las cinco posiciones.
     - A Eva se le entra por el BAJO DESNUDO y se construye hacia arriba:
       primero las seis fundamentales solas —que son una melodía por sí mismas—,
       luego la tercera encima, luego el acorde entero, y solo al final se pone
       en fila y se convierte en arpegio. Construir el acorde en vez de
       reducirlo es lo que hace que se aprenda de oído y no de memoria visual.

   Sin armadura: todas las alteraciones van escritas una a una.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_09_bruno import n, ac, corch, arp, REm, DO, FA, SOL, DOM7

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# las seis fundamentales, en el orden en que las recorre la pieza: el bajo
# desnudo es lo primero que ve Eva, antes que ningun acorde
BAJOS = ['D3', 'C3', 'F3', 'G2', 'B2', 'C3']

# el mismo recorrido con la tercera encima: el acorde a dos voces
TERCERAS = [('D3', 'F3'), ('C3', 'E3'), ('F3', 'A3'),
            ('G2', 'B2'), ('B2', 'D3'), ('C3', 'E3')]

ACORDES = [REm, DO, FA, SOL, DOM7, DO]

CANCION = dict(
    alumno='Eva', num=7, nivel='avanzado', slug='WhenIWasYourMan',
    titulo_corto='When I Was Your Man', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'WHEN I WAS YOUR MAN _ Bruno Mars.pdf'),
    yt='https://www.youtube.com/results?search_query=bruno+mars+when+i+was+your+man',

    ficha=dict(
        titulo='When I Was Your Man',
        autor='Bruno Mars (2012) · arr. musicaparadisfrutar.com',
        # La edición NO imprime indicación de tempo: la casilla dice "Carácter".
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'), ('Carácter', 'Balada'),
               ('Mano izq.', 'Seis acordes'), ('Mano dcha.', 'Semicorcheas')],
        armonia=dict(
            titulo='Toda la canción son seis acordes de Do mayor',
            tarjetas=[
                ('EL BAJO', 'Re·Do·Fa·Sol·Si·Do',
                 'Las seis fundamentales, en orden. Tócalas seguidas y ya reconocerás la canción.'),
                ('LOS DOS DE REPOSO', 'Do y Fa',
                 'Cuando llega uno de ellos la frase respira. Son los sitios donde se puede soltar.'),
                ('EL QUE EMPUJA', 'Sol · Si · Re',
                 'Después de él la música quiere volver a Do. No lo toques igual que los otros.'),
                ('SI · RE · FA', 'Sin fundamental',
                 'La dominante a la que le falta el Sol de abajo. Suena a que algo va a pasar.'),
            ],
            pie='No hay armadura, así que cada alteración que veas está escrita a mano y hay que '
                'mirarla una por una. Y como la edición no numera los compases, en este cuaderno se '
                'cita por ACORDE: es lo que está medido y es lo que no puede fallar.',
        ),
        ritmos=[
            ('MI', 'el bajo desnudo: seis notas y ahí está la canción entera',
             [n(p, 'h') for p in BAJOS], OCRE, 'bass', None),
            ('MI · lo escrito', 'ese acorde puesto en fila',
             corch(['D3', 'F3', 'A3', 'F3', 'A3', 'F3']) + [n('D3')], OCRE, 'bass', None),
            ('MD', 'la melodía se planta en una nota y la repite',
             corch(['C5', 'C5', 'C5', 'B4', 'C5', 'C5', 'B4', 'A4']), AZUL, 'treble', None),
        ],
        especial=[
            'No hay armadura: cada sostenido o bemol está escrito delante de su nota.',
            'El primer compás es de introducción y lleva dos acordes con alteraciones escritas.',
            'La izquierda alterna entre arpegios en corcheas y notas largas sostenidas.',
            'La derecha va en semicorcheas y repite mucho la misma nota antes de moverse.',
            'Hay ligaduras de unión por todas partes: muchas notas no se vuelven a atacar.',
            'La edición no numera los compases, así que aquí se cita por acorde y no por número.',
        ],
        reto='Que la izquierda no tape a la derecha. Un arpegio en corcheas ocupa mucho sitio, y esta '
             'canción es una balada donde lo único que importa es la voz de arriba. Si el '
             'acompañamiento se oye igual que la melodía, la canción se cae.',
        truco='No empieces por el arpegio: empieza por las seis notas del bajo. Tócalas solas, en '
              'redondas, hasta que las reconozcas de oído. Cuando el oído sabe a dónde va la '
              'armonía, la mano llega colocada al acorde siguiente sin tener que mirarlo.',
        sabias='Bruno Mars la grabó él solo al piano, sin banda: en el disco no hay batería, ni bajo, '
               'ni guitarras. Es la única canción de "Unorthodox Jukebox" grabada así, y la escribió '
               'después de que un amigo le contara que su novia le había dejado por no cuidarla.',
        qr=dict(titulo='Escucha la original',
                texto='Solo hay piano y voz. Fíjate en lo poco que suena la izquierda.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Esta canción son seis acordes y nada más. Aquí no se empieza por el arpegio: se empieza '
              'por el bajo desnudo y se construye el acorde hacia arriba, una voz cada vez. Cuando el '
              'oído sabe a dónde va la armonía, la mano llega colocada sola.',
        reglas=['SE CITA POR ACORDE, NO POR COMPÁS', 'DE ABAJO HACIA ARRIBA', 'LA IZQUIERDA, MÁS FLOJA'],
        bloques=[
            dict(num=1, titulo='El bajo desnudo, y el acorde encima', clef='bass',
                 pista='acordes medidos · tócalo las tres veces seguidas y escucha cómo va creciendo',
                 sistemas=[
                     dict(cap='a) las seis fundamentales solas · Re · Do · Fa · Sol · Si · Do: eso ya '
                              'es la canción, y son seis notas',
                          events=[n(p, 'w') for p in BAJOS], bars=6, clef='bass'),
                     dict(cap='b) ahora la tercera encima · dos voces, y ya se oye si el acorde es '
                              'mayor o menor',
                          events=[ac(par, 'w') for par in TERCERAS],
                          ligar=True,
                          pedal=4,
                          bars=6, clef='bass', show_time=False),
                     dict(cap='b) y AHORA con su figura de verdad, la semicorchea · el mismo dibujo el doble de rápido, tal y como está impreso en tu partitura',
                          events=[{'pitch': 'F3', 'dur': 's', 'beam': 9180},
                                  {'pitch': 'A3', 'dur': 's', 'beam': 9180},
                                  {'pitch': 'C4', 'dur': 's', 'beam': 9180},
                                  {'pitch': 'A3', 'dur': 's', 'beam': 9180},
                                  {'pitch': 'C4', 'dur': 's', 'beam': 9181},
                                  {'pitch': 'A3', 'dur': 's', 'beam': 9181},
                                  {'pitch': 'F3', 'dur': 's', 'beam': 9181},
                                  {'pitch': 'A3', 'dur': 's', 'beam': 9181},
                                  {'pitch': 'F3', 'dur': 'q'},
                                  {'pitch': 'A3', 'dur': 'q'}],
                          bars=1, show_time=False, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE CONSTRUYE Y NO SE REDUCE',
                 texto='Podrías tocar el arpegio tal como está escrito y quitarle notas hasta ver el '
                       'acorde. Se aprende antes al revés: primero el bajo, luego la tercera, luego la '
                       'quinta. Así cada nota que añades la oyes entrar, y el acorde deja de ser un '
                       'dibujo de tres bolitas en el papel para convertirse en un sonido que reconoces. '
                       'A partir de ahí no lees el acompañamiento: lo recuerdas.'),
            dict(num=2, titulo='Y ahora se pone en fila: el arpegio', clef='bass',
                 pista='el mismo acorde de antes, en corcheas · muy flojo y sin marcar la primera',
                 sistemas=[
                     dict(cap='a) sobre Fa · el gesto entero, cuatro veces: sube, baja y vuelve',
                          events=arp(*FA) * 4, bars=4, clef='bass'),
                     dict(cap='b) y los seis encadenados, en el orden de la canción · el gesto no '
                              'cambia nunca; lo único difícil es llegar colocada al siguiente',
                          events=arp(*REm) + arp(*DO) + arp(*FA) + arp(*SOL) + arp(*DOM7) + arp(*DO),
                          bars=3, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='La izquierda ya no se lee: se recuerda. Lo que queda es la derecha —que se mueve mucho '
              'menos de lo que parece— y la otra cara de la izquierda, que es sostener y no hacer nada '
              'más. Y el pedal, que en esta canción no es un adorno.',
        reglas=['SEIS ACORDES Y YA', 'EL PEDAL CAMBIA CON EL ACORDE', 'CUENTA EN VOZ ALTA'],
        bloques=[
            dict(num=3, titulo='La derecha: primero el esqueleto',
                 pista='andamio · el ritmo real va en semicorcheas; aquí en figuras largas, para verlo',
                 sistemas=[
                     dict(cap='a) solo las notas que cambian, sin las repeticiones · mira qué poco se '
                              'mueve la mano',
                          events=[n('C5', 'h'), n('B4', 'h'), n('A4', 'w'),
                                  n('B4', 'h'), n('A4', 'h'), n('F4', 'h'), n('A4', 'h')],
                          bars=4),
                     dict(cap='b) y ahora con las repeticiones, que es como está escrita: se planta en '
                              'una nota y la dice tres o cuatro veces antes de moverse',
                          events=corch(['C5', 'C5', 'C5', 'B4', 'C5', 'C5', 'B4', 'A4']) +
                                 corch(['B4', 'B4', 'B4', 'A4', 'B4', 'A4', 'F4', 'A4']) +
                                 [n('A4', 'w')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL PROBLEMA NO ES LEER, ES CONTAR',
                 texto='Miras la derecha y ves una nube de semicorcheas. Pero acabas de comprobar que '
                       'casi todas son la misma nota repetida: hay muy pocas alturas distintas. Lo que '
                       'cuesta es el ritmo, y el ritmo no se arregla leyendo más rápido, se arregla '
                       'contando en voz alta y muy despacio. Empieza a media velocidad y no subas hasta '
                       'que puedas cantar el compás entero sin mirar.'),
            dict(num=4, titulo='La izquierda que solo sostiene', clef='bass',
                 pista='la otra cara de esta mano · notas largas, atacadas una vez y dejadas sonar',
                 sistemas=[
                     dict(cap='a) cuando la partitura pone una redonda, no la vuelvas a tocar: '
                              'aguántala con el pedal y no hagas nada más',
                          events=[n('D2', 'w'), n('G2', 'w'), n('C2', 'w'), n('F2', 'w'),
                                  n('A2', 'w'), n('D2', 'w'), n('G2', 'w'), n('C2', 'w')],
                          bars=8, clef='bass'),
                     dict(cap='b) y esto es lo que el pedal tiene que estar aguantando mientras tanto: '
                              'el acorde entero, aunque tú ya hayas levantado los dedos',
                          events=[ac(DO, 'w'), ac(FA, 'w'), ac(SOL, 'w'), ac(DO, 'w')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL PEDAL, QUE AQUÍ ES OBLIGATORIO',
                 texto='Un arpegio suena a acorde solo si el pedal aguanta las notas que ya has '
                       'soltado. Sin pedal esta canción suena a ejercicio; con pedal suena a piano de '
                       'balada. La regla es simple: el pedal cambia cuando cambia el ACORDE, no cuando '
                       'cambia la melodía. Pisa al atacar la primera nota del arpegio nuevo y suelta '
                       'justo un pelo antes. Y como ya te sabes los seis acordes de memoria, sabes '
                       'exactamente dónde va cada cambio.'),
            dict(tipo='escalera', valores=[44, 52, 58, 64, 70, 76],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
