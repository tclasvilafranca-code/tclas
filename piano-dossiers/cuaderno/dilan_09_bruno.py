# -*- coding: utf-8 -*-
"""When I Was Your Man (Bruno Mars) — Dilan, avanzado. Ver TRANSCRIPCION_D09_11.md.

   Lo medido y por tanto citable:
     - los acordes que la izquierda arpegia: Rem, Do, Fa, Sol y un Si-Re-Fa
       que hace de dominante;
     - el caracter de la melodia, que se planta en una nota y la repite tres,
       cuatro y cinco veces antes de moverse.

   Lo que NO se cita: numeros de compas (la edicion no los numera y la
   deteccion de barras de esta partitura no es fiable) ni el ritmo de la
   derecha (semicorcheas con ligaduras y silencios que el motor no escribe).

   Sin armadura: todas las alteraciones van escritas una a una.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
_B = [1900]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='h'):
    return {'pitches': list(ps), 'dur': d}


def sil(d='q'):
    return {'rest': True, 'dur': d}


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


def arp(a, b, c):
    """El gesto de la izquierda tal como esta escrito: fundamental, tercera,
       quinta y vuelta a la tercera, en corcheas. Un compas entero."""
    return corch([a, b, c, b, c, b, a, b], agrupar=4)


def arp_var(a, b, c):
    """La VARIANTE para el calentamiento: fundamental, quinta, tercera,
       quinta. Es el mismo acorde pero otro recorrido, que es lo que pide la
       regla del cuaderno: el calentamiento deriva, no copia."""
    return corch([a, c, b, c, a, c, b, c], agrupar=4)


# --- los acordes medidos ---------------------------------------------------
REm = ('D3', 'F3', 'A3')
DO = ('C3', 'E3', 'G3')
FA = ('F3', 'A3', 'C4')
SOL = ('G2', 'B2', 'D3')
DOM7 = ('B2', 'D3', 'F3')        # la dominante, sin su fundamental

CANCION = dict(
    alumno='Dilan', num=9, nivel='avanzado', slug='WhenIWasYourMan',
    titulo_corto='When I Was Your Man', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' WHEN I WAS YOUR MAN _ Bruno Mars_.pdf'),
    yt='https://www.youtube.com/results?search_query=bruno+mars+when+i+was+your+man',

    ficha=dict(
        titulo='When I Was Your Man',
        autor='Bruno Mars (2012) · arr. musicaparadisfrutar.com',
        # La edición NO imprime ninguna indicación de tempo: la casilla dice
        # "Carácter", no "Tempo", para no atribuirle a la partitura algo que
        # no pone. El metrónomo lo decide la profesora.
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'), ('Carácter', 'Balada'),
               ('Mano izq.', 'Arpegios'), ('Mano dcha.', 'Semicorcheas')],
        armonia=dict(
            titulo='Qué arpegia la mano izquierda',
            tarjetas=[
                ('RE MENOR', 'Re · Fa · La',
                 'El acorde que más aparece. La izquierda lo sube y lo baja en corcheas.'),
                ('DO Y FA', 'Do·Mi·Sol · Fa·La·Do',
                 'Los dos acordes de reposo. Cuando llega uno de ellos, la frase respira.'),
                ('SOL', 'Sol · Si · Re',
                 'El que empuja. Después de él la música quiere volver a Do.'),
                ('SI · RE · FA', 'Sin fundamental',
                 'La dominante a la que le falta el Sol de abajo. Suena a que algo va a pasar.'),
            ],
            pie='No hay armadura, así que cada alteración que veas está escrita a mano y hay que '
                'mirarla una por una. El acompañamiento entero se reduce a cinco acordes de Do mayor '
                'arpegiados: si te aprendes las cinco posiciones de la mano, la izquierda de esta '
                'canción deja de ser un problema de lectura y pasa a ser un problema de memoria.',
        ),
        ritmos=[
            ('MI', 'el acorde arpegiado, en corcheas',
             corch(['D3', 'F3', 'A3', 'F3', 'A3', 'F3']) + [n('D3')], OCRE, 'bass', None),
            ('MI · otro acorde', 'la misma forma, movida a Fa',
             corch(['F3', 'A3', 'C4', 'A3', 'C4', 'A3']) + [n('F3')], OCRE, 'bass', None),
            ('MD', 'la melodía se planta en una nota y la repite (andamio)',
             corch(['G5', 'G5', 'G5', 'F5', 'G5', 'G5', 'F5', 'E5']), AZUL, 'treble', None),
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
        truco='Estudia la izquierda hasta que puedas tocarla mirando a otro lado, y entonces ponle la '
              'derecha encima tocando la izquierda deliberadamente más floja de lo que te parece '
              'necesario. Casi siempre "demasiado flojo" es exactamente lo que hace falta.',
        sabias='Bruno Mars la grabó él solo al piano, sin banda: en el disco no hay batería, ni bajo, '
               'ni guitarras. Es la única canción de "Unorthodox Jukebox" grabada así, y la escribió '
               'después de que un amigo le contara que su novia le había dejado por no cuidarla.',
        qr=dict(titulo='Escucha la original',
                texto='Solo hay piano y voz. Fíjate en lo poco que suena la izquierda.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta canción pide arpegios largos con la '
              'izquierda y notas repetidas con la derecha. Aquí se entrenan las dos cosas en Do mayor, '
              'que es la tonalidad de la pieza, y por grados que la pieza no usa.',
        reglas=['SIN ARMADURA · DO MAYOR', 'LA IZQUIERDA, SIEMPRE MÁS FLOJA', 'MANOS SEPARADAS'],
        ejercicios=[
            dict(num=1, titulo='Escala de Do mayor · dos octavas',
                 pista='manos separadas · sin alteraciones, pero el pulgar tiene que pasar limpio',
                 events=corch(['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']) +
                        corch(['D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'C6']) +
                        corch(['C6', 'B5', 'A5', 'G5', 'F5', 'E5', 'D5', 'C5']) +
                        corch(['B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4', 'C4']),
                 bars_per_line=4),
            dict(num=2, titulo='El arpegio, por toda la tonalidad', clef='bass',
                 pista='el gesto de la izquierda sobre los seis grados de Do mayor, no solo sobre cinco',
                 events=(arp_var('C3', 'E3', 'G3') + arp_var('D3', 'F3', 'A3') +
                         arp_var('E3', 'G3', 'B3') + arp_var('F3', 'A3', 'C4') +
                         arp_var('G2', 'B2', 'D3') + arp_var('A2', 'C3', 'E3')),
                 bars_per_line=3),
            dict(num=3, titulo='El arpegio al revés', clef='bass',
                 pista='la pieza sube y baja · aquí bajas y subes, que es lo que nunca practicas',
                 events=(corch(['G3', 'E3', 'C3', 'E3']) + corch(['A3', 'F3', 'D3', 'F3']) +
                         corch(['C4', 'A3', 'F3', 'A3']) + corch(['D3', 'B2', 'G2', 'B2'])),
                 bars_per_line=4),
            dict(num=4, titulo='Notas repetidas, cambiando de dedo',
                 pista='dedos 3 · 2 · 1 · lo que hace la derecha de esta canción todo el rato',
                 events=corch(['E5'] * 8) + corch(['D5'] * 8) +
                        corch(['C5'] * 8) + corch(['E5'] * 8),
                 bars_per_line=4),
            dict(num=5, titulo='Sostener con la izquierda', clef='bass',
                 pista='la otra cara de la izquierda · una nota grave, atacada una vez y ya',
                 events=[n(p, 'w') for p in ('C2', 'G2', 'A2', 'F2', 'D2', 'G2', 'C2', 'C2')],
                 bars_per_line=8),
            dict(num=6, titulo='Los cinco acordes, en bloque', clef='bass',
                 pista='sin arpegiar · para que la mano aprenda las posiciones antes de tener que correr',
                 events=[ac(REm, 'h'), ac(DO, 'h'), ac(FA, 'h'), ac(SOL, 'h'),
                         ac(DOM7, 'h'), ac(DO, 'h'), ac(DO, 'w')],
                 bars_per_line=4),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y sin armadura. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · no hay armadura, pero sí alteraciones sueltas',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DE LOS ARPEGIOS (CLAVE DE FA)',
        chuleta_pitches=['G2', 'B2', 'D3', 'F3', 'A3', 'C4'],
        chuleta_nombres=['Sol', 'Si', 'Re', 'Fa', 'La', 'Do'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa', clef='bass',
                 pista='donde viven los arpegios · el orden está desordenado a propósito',
                 events=[n(p) for p in ('D3', 'A3', 'F3', 'C4', 'G2', 'B2', 'E3', 'C3',
                                        'A2', 'F2', 'D2', 'B3', 'G3', 'E2', 'C3', 'D3')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · registro alto, con líneas adicionales',
                 events=[n(p) for p in ('E5', 'C5', 'A5', 'D5', 'G5', 'B4', 'F5', 'A4',
                                        'C6', 'E4', 'D5', 'G4', 'B5', 'F4', 'A5', 'C5')]),
            dict(num=3, titulo='Leer el acorde entero', clef='bass',
                 pista='tres notas de golpe · nómbralas de abajo arriba antes de pasar a la siguiente',
                 events=[ac(REm, 'q'), ac(DO, 'q'), ac(FA, 'q'), ac(SOL, 'q'),
                         ac(DOM7, 'q'), ac(FA, 'q'), ac(DO, 'q'), ac(DO, 'q')],
                 bars_per_line=4),
        ],
        crono='¿Cuánto tardas en el ejercicio 3, diciendo las tres notas de cada acorde?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca un acorde entero de golpe y luego el mismo arpegiado. Que diga cuál de las '
                      'dos veces fue el ARPEGIO, sin mirar.'),
                ('B', 'Toca una tríada suelta: MAYOR o MENOR. Esta canción alterna las dos sin avisar.'),
                ('C', 'Repite una misma nota varias veces seguidas, entre dos y cinco. Que cuente '
                      'cuántas. Es lo que hace la melodía todo el rato.'),
                ('+', 'Y sin escribir: toca dos acordes seguidos y que diga cuál sonaba más fuerte.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Bloque o arpegio?', pista='las mismas notas, juntas o seguidas',
                     n=10, opciones=['bloque', 'arpegio']),
                dict(letra='B', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=8, opciones=['M', 'm']),
                dict(letra='C', titulo='¿Cuántas repeticiones?', pista='la misma nota, seguida',
                     n=6, opciones=['2', '3', '4', '5']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Esta canción son cinco posiciones de la mano izquierda y nada más. El arpegio en sí no '
              'tiene dificultad: lo que se estudia es el SALTO de una posición a la siguiente. Por eso '
              'el paso 1 es el arpegio y el paso 2 es moverlo. Aquí no hay números de compás: la '
              'edición no los numera, así que se cita por ACORDE, que sí está medido.',
        reglas=['SE CITA POR ACORDE, NO POR COMPÁS', 'LA IZQUIERDA, MÁS FLOJA', 'DESPACIO'],
        bloques=[
            dict(num=1, titulo='El arpegio, y por dónde viaja', clef='bass',
                 pista='acordes medidos · muy flojo y muy igual, sin marcar la primera corchea',
                 sistemas=[
                     dict(cap='a) Re menor · Re · Fa · La — el acorde que más veces aparece en la canción',
                          events=arp(*REm) * 4, bars=4, clef='bass'),
                     dict(cap='b) quita el arpegio y quédate con la primera nota de cada acorde · '
                              'Re · Do · Fa · Sol · Si · Do: así es como viaja la mano',
                          events=[n('D3', 'w'), n('C3', 'w'), n('F3', 'w'),
                                  n('G2', 'w'), n('B2', 'w'), n('C3', 'w')],
                          ligar=True,
                          pedal=4,
                          bars=6, clef='bass', show_time=False),
                     dict(cap='b) y AHORA con su figura de verdad, la semicorchea · el mismo dibujo el doble de rápido, tal y como está impreso en tu partitura',
                          events=[{'pitch': 'D3', 'dur': 's', 'beam': 9140},
                                  {'pitch': 'F3', 'dur': 's', 'beam': 9140},
                                  {'pitch': 'A3', 'dur': 's', 'beam': 9140},
                                  {'pitch': 'F3', 'dur': 's', 'beam': 9140},
                                  {'pitch': 'A3', 'dur': 's', 'beam': 9141},
                                  {'pitch': 'F3', 'dur': 's', 'beam': 9141},
                                  {'pitch': 'D3', 'dur': 's', 'beam': 9141},
                                  {'pitch': 'F3', 'dur': 's', 'beam': 9141},
                                  {'pitch': 'D3', 'dur': 'q'},
                                  {'pitch': 'F3', 'dur': 'q'}],
                          bars=1, show_time=False, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='LO QUE SE ESTUDIA AQUÍ NO ES EL ARPEGIO',
                 texto='Son tres notas del acorde subiendo y bajando: eso no tiene misterio. Lo que hay '
                       'que estudiar es el SALTO, que es donde se pierde el tiempo. Prepara la mano en el '
                       'aire mientras suena la última corchea del compás anterior y llega a la posición '
                       'nueva ya colocada. Si la mano busca la tecla después de haber empezado el compás, '
                       'llegarás tarde por mucho que practiques.'),
            dict(num=2, titulo='Las cinco posiciones, sin arpegiar', clef='bass',
                 pista='en bloque primero · es la forma de aprendérselas de memoria y no volver a leerlas',
                 sistemas=[
                     dict(cap='a) un acorde por compás, en bloque: prepara la mano en el aire antes de '
                              'cada cambio',
                          events=[ac(REm, 'w'), ac(DO, 'w'), ac(FA, 'w'), ac(SOL, 'w'),
                                  ac(DOM7, 'w'), ac(DO, 'w')],
                          bars=6, clef='bass'),
                     dict(cap='b) y ahora en negras, un acorde por tiempo · es el paso previo a '
                              'arpegiarlo sin pensar',
                          events=[ac(DO, 'q'), ac(DO, 'q'), ac(FA, 'q'), ac(FA, 'q'),
                                  ac(SOL, 'q'), ac(SOL, 'q'), ac(DO, 'q'), ac(DO, 'q'),
                                  ac(DO, 'w')],
                          bars=3, clef='bass', show_time=False),
                     dict(cap='c) y el salto aislado, de dos en dos · esto es lo único que hay que '
                              'estudiar de verdad en esta mano',
                          events=[ac(REm, 'h'), ac(DO, 'h'),
                                  ac(DO, 'h'), ac(FA, 'h'),
                                  ac(FA, 'h'), ac(SOL, 'h'),
                                  ac(SOL, 'h'), ac(DOM7, 'h'),
                                  ac(DOM7, 'h'), ac(DO, 'h')],
                          bars=5, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='La izquierda ya está y no se vuelve a leer: se recuerda. Lo que queda es la otra cara de '
              'esa mano —las notas largas que solo se sostienen— y una derecha que se mueve mucho menos '
              'de lo que parece.',
        reglas=['CINCO POSICIONES Y YA', 'EL PEDAL CAMBIA CON EL ACORDE', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='La izquierda que solo sostiene', clef='bass',
                 pista='la otra cara de esta mano · notas largas, atacadas una vez y dejadas sonar',
                 sistemas=[
                     dict(cap='a) cuando la partitura pone una redonda, no la vuelvas a tocar: aguántala '
                              'con el pedal y no hagas nada más',
                          events=[n('C2', 'w'), n('A2', 'w'), n('F2', 'w'), n('G2', 'w'),
                                  n('C2', 'w'), n('F2', 'w'), n('G2', 'w'), n('C2', 'w')],
                          bars=8, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL PEDAL, QUE AQUÍ ES OBLIGATORIO',
                 texto='Un arpegio suena a acorde solo si el pedal aguanta las notas que ya has soltado. '
                       'Sin pedal, esta canción suena a ejercicio de arpegios; con pedal, suena a piano de '
                       'balada. La regla es simple: el pedal cambia cuando cambia el acorde, no cuando '
                       'cambia la melodía. Pisa al atacar la primera nota del arpegio nuevo y suelta justo '
                       'un pelo antes.'),
            dict(num=4, titulo='La derecha, plantada en una nota',
                 pista='andamio · el ritmo real va en semicorcheas; aquí en corcheas, para poder leerlo',
                 sistemas=[
                     dict(cap='a) el carácter de la melodía: se queda en una nota y la repite antes de '
                              'moverse',
                          events=corch(['E5', 'E5', 'E5', 'D5', 'E5', 'E5', 'D5', 'C5']) +
                                 corch(['D5', 'D5', 'D5', 'C5', 'D5', 'C5', 'A4', 'C5']) +
                                 [n('C5', 'w')],
                          bars=3),
                     dict(cap='b) y la misma frase quitando las repeticiones: solo las notas que cambian '
                              '· mira qué poco se mueve en realidad',
                          events=[n('E5', 'h'), n('D5', 'h'), n('C5', 'w'),
                                  n('D5', 'h'), n('C5', 'h'), n('A4', 'h'), n('C5', 'h')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA MELODÍA NO SE MUEVE TANTO COMO PARECE',
                 texto='Miras la derecha y ves una nube de semicorcheas, y da respeto. Pero mide las '
                       'alturas y verás que casi todas son la misma nota repetida: la melodía se planta en '
                       'un Mi o en un Re y lo dice tres, cuatro y cinco veces antes de moverse. Lo difícil '
                       'no es leer las notas, que son pocas: es el ritmo, y el ritmo se resuelve contando '
                       'en voz alta, no leyendo más rápido. Y por eso aquí no hay números de compás: la '
                       'edición no los numera, y prefiero no darte uno que luego no cuadre.'),
            dict(tipo='escalera', valores=[44, 52, 58, 64, 70, 76],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · El arpegio de Re menor, y por dónde viaja la mano.   '
                       '2 · Las cinco posiciones en bloque, de memoria.   '
                       '3 · Las notas largas, sostenidas con el pedal.   '
                       '4 · La derecha, contando el ritmo en voz alta.   '
                       '5 · La escalera de tempo, y las dos manos de la primera página.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
