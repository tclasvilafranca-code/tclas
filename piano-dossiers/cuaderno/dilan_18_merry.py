# -*- coding: utf-8 -*-
"""Have Yourself a Merry Little Christmas — Dilan, avanzado.
   Ver TRANSCRIPCION_D18_20.md.

   Do mayor, sin armadura. Lo medido: el acompanamiento de la izquierda es
   una nota grave y despues el acorde, dos veces por compas, y la melodia de
   los cc. 1-4 esta medida entera. Los cc. 2 y 6 son identicos.

   No se citan alteraciones accidentales: hay sostenidos y bemoles escritos a
   mano en la izquierda y el lector no los ve.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
_B = [2600]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='q'):
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


def oompah(grave, acorde):
    """El acompanamiento: la nota grave y despues el acorde, dos veces."""
    return [n(grave, 'q'), ac(acorde), n(grave, 'q'), ac(acorde)]


DO = ('E3', 'G3', 'C4')
FA = ('F3', 'A3', 'C4')
SOL = ('D3', 'G3', 'B3')
LAm = ('E3', 'A3', 'C4')

CANCION = dict(
    alumno='Dilan', num=18, nivel='avanzado', slug='MerryLittleChristmas',
    titulo_corto='Have Yourself a Merry Little Christmas', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           'have-yourself-a-merry-little-NAVIDAD       ADhristmas_.pdf'),
    yt='https://www.youtube.com/results?search_query=have+yourself+a+merry+little+christmas',

    ficha=dict(
        titulo='Have Yourself a Merry Little Christmas',
        autor='Hugh Martin y Ralph Blane (1944) · edición con letra',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'), ('Tempo', '♩=66'),
               ('Dinámica', 'mp'), ('Mano izq.', 'Bajo y acorde')],
        armonia=dict(
            titulo='El acompañamiento de balada',
            tarjetas=[
                ('EL GESTO', 'Grave · acorde',
                 'Una nota grave en el uno, el acorde en el dos, y otra vez en el tres y el cuatro.'),
                ('POR QUÉ FUNCIONA', 'Separa registros',
                 'El bajo abajo y el acorde en el medio: así la melodía tiene sitio arriba.'),
                ('LOS CC. 2 Y 6', 'Son el mismo',
                 'Idénticos en las dos manos. Medido compás a compás.'),
                ('LAS ALTERACIONES', 'Escritas a mano',
                 'No hay armadura, así que cada ♯ y cada ♭ que veas está puesto a propósito.'),
            ],
            pie='Este acompañamiento es el mismo que usan casi todas las baladas americanas de los años '
                'cuarenta: bajo, acorde, bajo, acorde. Suena a poco escrito y a mucho tocado, y el '
                'secreto está en el reparto de volumen: el bajo se oye, el acorde casi no, y la melodía '
                'por encima de las dos cosas.',
        ),
        ritmos=[
            ('MI', 'grave y acorde, dos veces por compás', oompah('C3', DO), OCRE, 'bass', None),
            ('MI · otro acorde', 'el mismo gesto, movido a Fa', oompah('F2', FA), OCRE, 'bass', None),
            ('MD', 'la melodía, con la letra debajo',
             corch(['G4', 'F4', 'E4', 'D4']) + [n('A3'), n('C4')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay armadura: cada sostenido o bemol está escrito delante de su nota.',
            'Pone ♩=66 y mp: es una balada, y suave. No hay ni un forte en la primera página.',
            'La izquierda hace bajo y acorde, dos veces por compás, en toda la pieza.',
            'Viene con LETRA: cántala y el fraseo se coloca solo.',
            'Los cc. 2 y 6 son idénticos en las dos manos.',
            'Hay acordes con alteraciones escritas: son los que le dan el color de jazz.',
        ],
        reto='El reparto de volumen entre las tres cosas que suenan a la vez: el bajo, el acorde y la '
             'melodía. Los tres los tocas tú, pero tienen que sonar a tres alturas distintas. Si el '
             'acorde del medio se oye igual que la melodía, la canción se apelmaza.',
        truco='Toca solo el bajo y la melodía, sin el acorde de en medio, hasta que suene bien. Después '
              'añade el acorde tocándolo tan flojo que casi no se oiga, y sube desde ahí. Es más fácil '
              'subir de menos a más que bajar de más a menos.',
        sabias='Judy Garland la cantó en 1944 y pidió que le cambiaran la letra: la original decía "puede '
               'que sea nuestra última Navidad juntos" y a ella le pareció demasiado triste para una '
               'película de Navidad. La versión que hoy conoce todo el mundo es la retocada.',
        qr=dict(titulo='Escucha la original',
                texto='La de Judy Garland. Fíjate en lo despacio que va.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta balada pide una izquierda que salte del '
              'bajo al acorde sin ruido y un oído que sepa repartir volumen entre tres cosas a la vez. '
              'Aquí se entrena lo primero, en Do mayor.',
        reglas=['SIN ARMADURA · DO MAYOR', 'EL BAJO SE OYE, EL ACORDE NO', 'MP DE VERDAD'],
        ejercicios=[
            dict(num=1, titulo='Escala de Do mayor · dos octavas', clef='bass',
                 pista='manos separadas · sin alteraciones, pero el pulgar tiene que pasar limpio',
                 events=corch(['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3']) +
                        corch(['D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'C4']) +
                        corch(['C4', 'B3', 'A3', 'G3', 'F3', 'E3', 'D3', 'C3']) +
                        corch(['B2', 'A2', 'G2', 'F2', 'E2', 'D2', 'C2', 'C2']),
                 bars_per_line=4),
            dict(num=2, titulo='Bajo y acorde, por toda la tonalidad', clef='bass',
                 pista='el gesto de la canción sobre los seis grados de Do mayor',
                 events=(oompah('D3', ('F3', 'A3', 'D4')) + oompah('E3', ('G3', 'B3', 'E4')) +
                         oompah('G2', ('B2', 'D3', 'G3')) + oompah('A2', ('C3', 'E3', 'A3'))),
                 bars_per_line=4),
            dict(num=3, titulo='Y ahora al revés', clef='bass',
                 pista='el acorde en el uno y el bajo en el dos · descoloca, y por eso sirve',
                 events=([ac(('F3', 'A3', 'D4')), n('D3'), ac(('F3', 'A3', 'D4')), n('D3')] +
                         [ac(('G3', 'B3', 'E4')), n('E3'), ac(('G3', 'B3', 'E4')), n('E3')] +
                         [ac(('B2', 'D3', 'G3')), n('G2'), ac(('B2', 'D3', 'G3')), n('G2')] +
                         [ac(('C3', 'E3', 'A3')), n('A2'), ac(('C3', 'E3', 'A3')), n('A2')]),
                 bars_per_line=4),
            dict(num=4, titulo='El salto solo', clef='bass',
                 pista='toca el bajo y coloca la mano en el acorde sin tocarlo · usa el silencio',
                 events=[n('C3'), sil('h.'), n('F2'), sil('h.'),
                         n('G2'), sil('h.'), n('A2'), sil('h.'),
                         n('C3', 'w')],
                 bars_per_line=5),
            dict(num=5, titulo='Los acordes solos, sin el bajo', clef='bass',
                 pista='para que la mano aprenda las posiciones antes de tener que saltar',
                 events=[ac(DO, 'h'), ac(FA, 'h'), ac(SOL, 'h'), ac(LAm, 'h'),
                         ac(FA, 'h'), ac(SOL, 'h'), ac(DO, 'w')],
                 bars_per_line=4),
            dict(num=6, titulo='Cantar con la derecha',
                 pista='notas largas · lo que hace la melodía cuando la letra se estira',
                 events=[n('G4', 'h'), n('E4', 'h'), n('C5', 'h'), n('G4', 'h'),
                         n('A4', 'h'), n('F4', 'h'), n('E4', 'w')],
                 bars_per_line=4),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y sin armadura. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · no hay armadura, pero sí alteraciones sueltas',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DE LA MANO IZQUIERDA (CLAVE DE FA)',
        chuleta_pitches=['C2', 'F2', 'G2', 'C3', 'E3', 'G3', 'C4'],
        chuleta_nombres=['Do', 'Fa', 'Sol', 'Do', 'Mi', 'Sol', 'Do'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa', clef='bass',
                 pista='donde vive el acompañamiento · el orden está desordenado a propósito',
                 events=[n(p) for p in ('C3', 'G2', 'E3', 'F2', 'A3', 'D3', 'B2', 'C2',
                                        'G3', 'D2', 'F3', 'A2', 'E2', 'B3', 'C4', 'C3')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · registro medio, con la letra debajo en la partitura',
                 events=[n(p) for p in ('G4', 'C5', 'E4', 'A4', 'D5', 'F4', 'B4', 'C4',
                                        'E5', 'G4', 'A3', 'D4', 'F5', 'B3', 'C5', 'G4')]),
            dict(num=3, titulo='Leer el acorde de en medio', clef='bass',
                 pista='tres notas de golpe · nómbralas de abajo arriba antes de pasar a la siguiente',
                 events=[ac(DO), ac(FA), ac(SOL), ac(LAm),
                         ac(FA), ac(SOL), ac(DO), ac(DO)],
                 bars_per_line=4),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca bajo y acorde. Unas veces que se oiga más el bajo y otras más el acorde. '
                      'Que diga cuál pesaba.'),
                ('B', 'Toca una tríada suelta: MAYOR o MENOR.'),
                ('C', 'Toca una tríada y a veces añádele una nota más (una séptima). Que diga si '
                      'sonaban TRES notas o CUATRO: es el color de jazz de esta canción.'),
                ('+', 'Y sin escribir: toca el bajo y la melodía a la vez y que cante la melodía.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Qué pesa más?', pista='el bajo, o el acorde de después',
                     n=10, opciones=['bajo', 'acorde']),
                dict(letra='B', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=8, opciones=['M', 'm']),
                dict(letra='C', titulo='¿Tres notas o cuatro?', pista='la cuarta es la que suena a jazz',
                     n=6, opciones=['3', '4']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='En esta canción suenan tres cosas a la vez —el bajo abajo, el acorde en medio y la '
              'melodía arriba— y las tres las tocas tú. Por eso se estudia por capas: primero el '
              'acompañamiento solo, decidiendo qué se oye y qué no, y solo después la melodía. Las '
              'alteraciones escritas a mano no aparecen aquí: el lector no las ve.',
        reglas=['EL BAJO SE OYE, EL ACORDE NO', 'MIRA LAS ALTERACIONES EN LA PARTITURA', 'MP'],
        bloques=[
            dict(num=1, titulo='El acompañamiento, y qué se oye de él', clef='bass',
                 pista='cc. 1–8 · el bajo con peso de brazo y el acorde casi sin dedo',
                 sistemas=[
                     dict(cap='a) solo el bajo de cada compás · si esta línea suena bien, la canción va '
                              'a sonar bien',
                          events=[n('D3', 'w'), n('C3', 'w'), n('D3', 'w'), n('E3', 'w'),
                                  n('D3', 'w'), n('C3', 'w'), n('D3', 'w'), n('C3', 'w')],
                          bars=8, clef='bass'),
                     dict(cap='b) cc. 1–4 con el acorde encima, dos veces por compás · si los dos suenan '
                              'igual, la melodía se pierde',
                          events=oompah('D3', SOL) + oompah('C3', DO) +
                                 oompah('D3', ('F3', 'A3', 'D4')) + oompah('E3', LAm),
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y los cc. 5–8, que es la segunda frase · cuando esto salga sin mirarte '
                              'la mano, pon la derecha encima',
                          events=oompah('F2', FA) + oompah('E3', LAm) +
                                 oompah('G2', SOL) + oompah('C3', DO),
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='TRES COSAS A LA VEZ, TRES VOLÚMENES',
                 texto='La regla es: la melodía por encima de todo, el bajo se tiene que oír porque '
                       'sostiene, y el acorde del medio es relleno y casi no debería notarse. Cuando algo '
                       'suene apelmazado, casi siempre es que el acorde de en medio está sonando '
                       'demasiado. Y hay un compás regalado: el c. 6 es el c. 2 en las dos manos, medido. '
                       'Móntalo una vez y no lo vuelvas a leer.'),
            dict(num=2, titulo='La melodía, frase por frase',
                 pista='cc. 1–4 medidos · “Have your-self a mer-ry lit-tle Christ-mas”',
                 sistemas=[
                     dict(cap='a) cc. 1–2 · canta la letra mientras la lees y verás dónde respira la frase',
                          events=corch(['G4', 'F4', 'E4', 'D4']) + [n('A3'), n('C4')] +
                                 corch(['C4', 'E4', 'G4', 'C5']) + [n('C5'), n('G4')],
                          bars=2),
                     dict(cap='b) cc. 3–4 · baja desde el Re5 y se queda en La · es la respuesta a los '
                              'dos primeros: tiene que sonar más floja, no más fuerte',
                          events=corch(['D5', 'C5', 'B4', 'A4']) + [n('G4'), n('F4')] +
                                 [n('E4'), n('C5'), n('B4'), n('A4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA CANCIÓN SE PONE TRISTE',
                 texto='Está en Do mayor, la tonalidad más neutra que existe, y sin embargo suena '
                       'melancólica. El truco está en los acordes con alteraciones: el arreglista mete '
                       'notas que no pertenecen a Do mayor y que tiran hacia abajo. Cuando llegues a uno '
                       'de ellos, no lo toques más fuerte: tócalo más lento. Esa clase de acorde pide '
                       'tiempo, no volumen.'),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='Lo que queda es de oído: oírse tocando tres cosas a la vez y decidir cuál suena más. Y '
              'antes de nada, el lápiz: las alteraciones de esta canción están escritas una a una.',
        reglas=['MARCA LAS ALTERACIONES CON LÁPIZ', 'CANTA LA LETRA', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='La melodía entera, con la letra',
                 pista='cc. 1–4 · alturas medidas, ritmo simplificado · cántala mientras la tocas',
                 sistemas=[
                     dict(cap='a) si no puedes cantarla mientras la tocas, es que vas demasiado rápido',
                          events=corch(['G4', 'F4', 'E4', 'D4']) + [n('A3'), n('C4')] +
                                 corch(['D5', 'C5', 'B4', 'A4']) + [n('G4'), n('F4')] +
                                 [n('E4', 'h'), n('C5', 'h')] + [n('A4', 'w')],
                          bars=4),
                     dict(cap='b) y la misma frase en notas largas, una por compás · para oír su dibujo '
                              'sin la prisa de las corcheas',
                          events=[n('G4', 'h'), n('D4', 'h'), n('C4', 'h'), n('C5', 'h'),
                                  n('D5', 'h'), n('A4', 'h'), n('G4', 'h'), n('E4', 'h'),
                                  n('A4', 'w')],
                          bars=5, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LAS ALTERACIONES ESCRITAS A MANO',
                 texto='Esta canción no tiene armadura, así que cada sostenido y cada bemol que veas está '
                       'puesto uno a uno por el arreglista, y son justo los que le dan el color: sin '
                       'ellos suena a villancico y con ellos suena a jazz. Coge un lápiz y rodéalos todos '
                       'antes de tocar una sola nota. Es el ejercicio más rentable de esta semana.'),
            dict(num=4, titulo='Las tres capas juntas', clef='bass',
                 pista='cc. 1–4 · el acompañamiento reducido a un golpe por compás, para poder escuchar',
                 sistemas=[
                     dict(cap='a) un solo acorde por compás: así te queda oreja libre para oír la '
                              'melodía por encima',
                          events=[ac(('D3', 'G3', 'B3'), 'w'), ac(('C3', 'E3', 'G3'), 'w'),
                                  ac(('D3', 'F3', 'A3'), 'w'), ac(('E3', 'A3', 'C4'), 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) y lo mismo de los cc. 5–8',
                          events=[ac(('F2', 'A2', 'C3'), 'w'), ac(('E3', 'A3', 'C4'), 'w'),
                                  ac(('G2', 'B2', 'D3'), 'w'), ac(('C3', 'E3', 'G3'), 'w')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE HACE EL PASO 4',
                 texto='Toca los cc. 1 al 4 muy lento, y en cada pasada escucha UNA sola cosa: primera '
                       'pasada, ¿se oye la melodía por encima de todo? Segunda, ¿se oye el bajo? Tercera, '
                       '¿el acorde de en medio está lo bastante flojo? No intentes arreglar las tres a la '
                       'vez: una por pasada, y anota cuál te falla siempre.'),
            dict(tipo='escalera', valores=[44, 50, 54, 58, 62, 66],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · El acompañamiento: primero el bajo solo, después con el acorde.   '
                       '2 · La melodía, frase por frase.   '
                       '3 · La melodía entera, cantando la letra.   '
                       '4 · Las tres capas juntas, escuchando una por pasada.   '
                       '5 · La escalera de tempo.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
