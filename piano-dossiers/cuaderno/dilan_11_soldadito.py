# -*- coding: utf-8 -*-
"""Soldadito de Hierro (Nil Moliner) — Dilan, avanzado. Ver TRANSCRIPCION_D09_11.md.

   Esta es de las partituras mas agradecidas del album: la izquierda toca UNA
   quinta vacia en redonda por compas y la melodia esta medida entera. Todo lo
   que se cita aqui esta comprobado dos veces:

     - la izquierda con huecas.py, y todas las posiciones caen a menos de 0,15
       de linea o espacio;
     - la melodia con score_reader, con posiciones igual de limpias.

   Lo unico que NO se escribe es el ritmo real de la derecha: va lleno de
   tresillos y silencios de semicorchea, y el motor no sabe escribir eso. Se
   dice expresamente en cada bloque que lo cita.

   La numeracion: el lector cuenta la anacrusa como compas 1, la edicion no.
   Aqui se usa SIEMPRE la numeracion impresa (= lector - 1).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
_B = [1700]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='w'):
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


# --- lo medido -------------------------------------------------------------
# la izquierda: una quinta vacia en redonda por compas (cc. 1-7 impresos)
QUINTAS = [ac(('C3', 'G3')), ac(('D3', 'A3')), ac(('G2', 'D3')), ac(('C3', 'G3')),
           ac(('F2', 'C3')), ac(('G2', 'D3')), ac(('F2', 'C3'))]

# La melodia de los cc. 1-3: ALTURAS medidas, ritmo simplificado. El ritmo
# real va en tresillos y el motor no los escribe, asi que se reparte en
# corcheas y se dice en cada bloque que el ritmo esta simplificado.
MEL_1 = corch(['D4', 'E4', 'C4', 'C4', 'G4', 'G4', 'G4', 'G4']) + [n('F4', 'h'), n('E4', 'h')]
MEL_2 = corch(['D4', 'E4', 'G4', 'G4', 'G4', 'G4']) + [n('F4'), n('E4', 'w')]
MEL_3 = corch(['E4', 'D4', 'D4', 'D4', 'C4', 'C4', 'D4', 'D4'])

CANCION = dict(
    alumno='Dilan', num=11, nivel='avanzado', slug='Soldadito',
    titulo_corto='Soldadito de Hierro', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' SOLDADITO DE HIERRO _ Nil Moliner_.pdf'),
    yt='https://www.youtube.com/results?search_query=nil+moliner+soldadito+de+hierro',

    ficha=dict(
        titulo='Soldadito de Hierro',
        autor='Nil Moliner (2019) · arr. Campamento Musical Bye Bye Beethoven',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'), ('Tempo', '♩=84'),
               ('Compases', '30'), ('Mano izq.', 'Quintas')],
        total_compases=30,
        secciones=[
            ('A', 1, 3, 'La frase', OCRE),
            ('B', 4, 14, 'El cuerpo de la canción', AZUL),
            ("B'", 15, 24, 'Los cc. 4–13 otra vez', OCRE),
            ('final', 25, 30, 'Cierra', AZUL),
        ],
        armonia=dict(
            titulo='Los acordes son solo dos notas',
            tarjetas=[
                ('LA IZQUIERDA', 'Quintas vacías',
                 'Dos notas por compás, a distancia de quinta, en redonda. Nunca hay tercera: '
                 'por eso suena hueco y abierto.'),
                ('CC. 1–4', 'Do · Rem · Sol · Do',
                 'Do3–Sol3, Re3–La3, Sol2–Re3 y otra vez Do3–Sol3. Medido nota por nota.'),
                ('CC. 5–7', 'Fa · Sol · Fa',
                 'Fa2–Do3, Sol2–Re3, Fa2–Do3. Cuatro acordes en toda la primera página.'),
                ('LOS CC. 15–24', 'Son los cc. 4–13',
                 'Idénticos, comprobados uno a uno. Media canción se aprende sola.'),
            ],
            pie='Una quinta vacía es un acorde sin su tercera, que es la nota que decide si suena '
                'mayor o menor. Al quitarla el acorde se queda abierto, casi como un eco. Aquí se usa '
                'para que la voz tenga sitio: el piano no dice nada, solo sostiene.',
        ),
        ritmos=[
            ('MI', 'una quinta en redonda por compás: se ataca y se deja',
             [ac(('C3', 'G3'))], OCRE, 'bass', None),
            ('MD', 'la melodía cantada · el ritmo real lleva tresillos',
             corch(['G4', 'G4', 'G4', 'G4']) + [n('F4'), n('E4')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay armadura: ni sostenidos ni bemoles. La tonalidad es Do mayor.',
            'La izquierda toca DOS notas por compás, en redonda, y no hace nada más en toda la pieza.',
            'Empieza en ANACRUSA: la sílaba "Me" va antes del primer compás.',
            'Hay TRESILLOS por todas partes en la derecha, marcados con un 3.',
            'Los cc. 15 al 24 son exactamente los cc. 4 al 13.',
        ],
        reto='Los tresillos. La melodía casi no para de hacerlos, y como la izquierda va en redondas no '
             'hay nada que marque el pulso: si te descolocas, no tienes dónde agarrarte.',
        truco='Toca primero la izquierda sola de toda la canción: son treinta redondas y se aprende en '
              'diez minutos. Después cuenta el pulso con el pie y canta la letra encima, sin tocar la '
              'derecha: los tresillos se colocan solos cuando cantas.',
        sabias='Nil Moliner la escribió pensando en su abuelo, que tenía alzhéimer: el "soldadito de '
               'hierro que aguanta de pie en la batalla" es él. Salió en 2019 y se hizo conocida años '
               'después.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en que el piano casi no se mueve: son dos notas por compás.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta canción pide dos cosas: quintas limpias '
              'con la izquierda y un pulso que no se caiga cuando la derecha hace tresillos. Aquí se '
              'trabajan las dos, en Do mayor, que es la tonalidad de la pieza.',
        reglas=['SIN ARMADURA · DO MAYOR', 'LAS DOS NOTAS, A LA VEZ', 'EL PIE NO SE PARA'],
        ejercicios=[
            dict(num=1, titulo='Escala de Do mayor · dos octavas', clef='bass',
                 pista='manos separadas · sin alteraciones, pero el pulgar tiene que pasar limpio',
                 events=corch(['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3']) +
                        corch(['D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'C4']) +
                        corch(['C4', 'B3', 'A3', 'G3', 'F3', 'E3', 'D3', 'C3']) +
                        corch(['B2', 'A2', 'G2', 'F2', 'E2', 'D2', 'C2', 'C2']),
                 bars_per_line=4),
            dict(num=2, titulo='Quintas por toda la escala', clef='bass',
                 pista='el gesto de la izquierda · las dos teclas al fondo exactamente a la vez',
                 events=[ac(('C3', 'G3'), 'h'), ac(('D3', 'A3'), 'h'),
                         ac(('E3', 'B3'), 'h'), ac(('F3', 'C4'), 'h'),
                         ac(('G3', 'D4'), 'h'), ac(('A3', 'E4'), 'h'),
                         ac(('B3', 'F4'), 'h'), ac(('C4', 'G4'), 'h'),
                         ac(('C3', 'G3'))],
                 bars_per_line=5),
            dict(num=3, titulo='Y ahora bajando', clef='bass',
                 pista='hacia el grave, que es donde la canción las pone · el 5 abajo y el 1 arriba',
                 events=[ac(('C3', 'G3'), 'h'), ac(('B2', 'F3'), 'h'),
                         ac(('A2', 'E3'), 'h'), ac(('G2', 'D3'), 'h'),
                         ac(('F2', 'C3'), 'h'), ac(('E2', 'B2'), 'h'),
                         ac(('D2', 'A2'), 'h'), ac(('C2', 'G2'), 'h'),
                         ac(('C2', 'G2'))],
                 bars_per_line=5),
            dict(num=4, titulo='La quinta, y luego el acorde entero', clef='bass',
                 pista='primero hueco, después con la tercera puesta · escucha la diferencia',
                 events=[ac(('C3', 'G3'), 'h'), ac(('C3', 'E3', 'G3'), 'h'),
                         ac(('F2', 'C3'), 'h'), ac(('F2', 'A2', 'C3'), 'h'),
                         ac(('G2', 'D3'), 'h'), ac(('G2', 'B2', 'D3'), 'h'),
                         ac(('C3', 'G3'))],
                 bars_per_line=4),
            dict(num=5, titulo='Tres notas donde caben dos',
                 pista='el tresillo, con notas fáciles · di "man-za-na" mientras el pie marca dos golpes',
                 events=corch(['C4', 'D4', 'E4', 'D4', 'E4', 'F4', 'E4', 'F4']) +
                        corch(['G4', 'F4', 'E4', 'D4', 'E4', 'D4', 'C4', 'C4']),
                 bars_per_line=4),
            dict(num=6, titulo='Empezar antes del compás',
                 pista='la anacrusa de la canción · la primera nota cae ANTES del uno',
                 events=[sil('h'), sil('q'), n('E4'),
                         n('D4'), n('E4'), n('C4', 'h'),
                         sil('h'), sil('q'), n('G4'),
                         n('F4'), n('E4'), n('C4', 'h'),
                         n('C4', 'w')],
                 bars_per_line=5),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y sin armadura. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · no hay armadura, así que no hay trampas',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DE LAS QUINTAS (CLAVE DE FA)',
        chuleta_pitches=['C2', 'F2', 'G2', 'C3', 'D3', 'G3', 'A3'],
        chuleta_nombres=['Do', 'Fa', 'Sol', 'Do', 'Re', 'Sol', 'La'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa', clef='bass',
                 pista='donde vive la izquierda · el orden está desordenado a propósito',
                 events=[n(p) for p in ('C3', 'G2', 'D3', 'F2', 'A3', 'E3', 'B2', 'C2',
                                        'G3', 'D2', 'F3', 'A2', 'E2', 'B3', 'C3', 'G2')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · registro medio, casi todo entre Do4 y Sol4',
                 events=[n(p) for p in ('E4', 'C4', 'G4', 'D4', 'F4', 'A4', 'B3', 'E4',
                                        'C5', 'G4', 'D4', 'F4', 'A3', 'B4', 'E4', 'C4')]),
            dict(num=3, titulo='Leer quintas', clef='bass',
                 pista='dos notas de golpe · nómbralas de abajo arriba, sin contar las líneas',
                 events=[ac(('C3', 'G3'), 'q'), ac(('F2', 'C3'), 'q'),
                         ac(('G2', 'D3'), 'q'), ac(('D3', 'A3'), 'q'),
                         ac(('E3', 'B3'), 'q'), ac(('A2', 'E3'), 'q'),
                         ac(('B2', 'F3'), 'q'), ac(('C3', 'G3'), 'q')],
                 bars_per_line=4),
        ],
        crono='¿Cuánto tardas en el ejercicio 3, diciendo las dos notas de cada quinta?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca dos notas a la vez, unas veces una QUINTA y otras una tríada entera. Que '
                      'diga si sonaban DOS o TRES.'),
                ('B', 'Marca cuatro tiempos y mete DOS notas o TRES en uno de ellos. Que diga cuántas '
                      'eran. Es el tresillo, que en esta canción está por todas partes.'),
                ('C', 'Toca una tríada suelta: MAYOR o MENOR. Después la misma sin la tercera, para '
                      'que oiga que ahí ya no se puede decir.'),
                ('+', 'Y sin escribir: toca Do–Sol, Re–La y Sol–Re, y que las cante.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Dos notas o tres?', pista='la quinta es hueca; la tríada, llena',
                     n=10, opciones=['2', '3']),
                dict(letra='B', titulo='¿Dos o tres en un tiempo?', pista='el tresillo',
                     n=8, opciones=['2', '3']),
                dict(letra='C', titulo='¿Mayor o menor?', pista='solo cuando suene la tríada entera',
                     n=6, opciones=['M', 'm']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='En esta canción está medido casi todo: la izquierda entera y la melodía de la primera '
              'frase. Lo único que no se escribe aquí es el ritmo de la derecha, porque va en tresillos '
              'y con estas figuras no se puede poner sin mentirte. Se empieza por la izquierda, que no '
              'cambia de gesto ni una vez en toda la pieza.',
        reglas=['LAS DOS NOTAS DE LA IZQUIERDA, A LA VEZ', 'LA DERECHA, EN TRESILLOS', 'LENTO'],
        bloques=[
            dict(num=1, titulo='La izquierda, que solo sostiene', clef='bass',
                 pista='cc. 1–7 medidos · ataca, suelta el brazo y no vuelvas a tocar hasta el compás siguiente',
                 sistemas=[
                     dict(cap='a) cc. 1–7 · Do · Rem · Sol · Do · Fa · Sol · Fa, una redonda doble por compás',
                          events=QUINTAS, bars=7, clef='bass'),
                     dict(cap='b) y la izquierda entera, doce compases sin parar · es lo que vas a '
                              'tocar treinta veces: que salga sin mirarte la mano',
                          events=[ac(('C3', 'G3')), ac(('D3', 'A3')), ac(('G2', 'D3')),
                                  ac(('C3', 'G3')), ac(('F2', 'C3')), ac(('G2', 'D3')),
                                  ac(('F2', 'C3')), ac(('C3', 'G3')), ac(('G2', 'D3')),
                                  ac(('A2', 'E3')), ac(('F2', 'C3')), ac(('C3', 'G3'))],
                          bars=6, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SUENA HUECO',
                 texto='Las dos notas de la izquierda están siempre a distancia de quinta, y eso quiere '
                       'decir que falta la tercera: la nota que decide si un acorde es mayor o menor. Sin '
                       'ella el acorde no dice nada, solo sostiene. Es una decisión del arreglo, no una '
                       'simplificación: si le pones la tercera, la canción se vuelve dulce y deja de '
                       'sonar a lo que suena. Pruébalo una vez y luego déjalo como está.'),
            dict(num=2, titulo='La melodía de la primera frase',
                 pista='cc. 1–3 · las notas son las de la partitura; el ritmo, simplificado a corcheas',
                 sistemas=[
                     dict(cap='a) cc. 1–2 · en la partitura esto va en tresillos, aquí en corcheas solo '
                              'para leerlo',
                          events=MEL_1 + MEL_2, bars=2),
                     dict(cap='b) el c. 3, que cierra la frase · no acaba en la tónica, y por eso sigue',
                          events=MEL_3 + [n('D4', 'w')], bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ AQUÍ NO ESTÁ EL RITMO DE VERDAD',
                 texto='Las notas de este paso son exactamente las de tu partitura, pero el ritmo no: en '
                       'la pieza van casi todas en tresillos. Léelas de aquí, tócalas de aquí, y para el '
                       'ritmo mira la página 1 y cuenta.'),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='Hay mucho menos que aprender de lo que parece: diez compases de la canción están escritos '
              'dos veces. Lo que queda es el tresillo, que se resuelve cantando la letra, no contando.',
        reglas=['LOS CC. 15–24 SON LOS CC. 4–13', 'CANTA LA LETRA MIENTRAS TOCAS', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='El tresillo, y colocar la primera frase',
                 pista='andamio rítmico · tres notas por tiempo, sin cambiar de velocidad al pasar de compás',
                 sistemas=[
                     dict(cap='a) cuenta “un-dos-tres” por cada golpe del pie y no aceleres en la barra',
                          events=corch(['E4', 'F4', 'G4', 'F4', 'E4', 'D4', 'C4', 'D4']) +
                                 corch(['E4', 'D4', 'C4', 'D4', 'E4', 'F4', 'G4', 'G4']) +
                                 [n('E4', 'w')],
                          bars=3),
                     dict(cap='b) y lo mismo en notas largas, para colocar la mano antes de meterle '
                              'los tresillos',
                          events=[n('E4', 'h'), n('G4', 'h'), n('E4', 'h'), n('C4', 'h'),
                                  n('E4', 'h'), n('C4', 'h'), n('E4', 'h'), n('G4', 'h'),
                                  n('E4', 'w')],
                          bars=5, show_time=False),
                     dict(cap='c) y la izquierda de esos mismos compases, para tenerla colocada antes '
                              'de juntar las dos manos',
                          events=QUINTAS[:3], bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='DIEZ COMPASES REGALADOS',
                 texto='Los cc. 15 al 24 son, nota por nota, los cc. 4 al 13. No es una impresión: está '
                       'comprobado compás a compás, siete parejas seguidas idénticas. Coge un lápiz, '
                       'busca el c. 15 en tu partitura y escribe al lado “= c. 4”. Cuando llegues ahí '
                       'tocando, no leas: ya te lo sabes.'),
            dict(num=4, titulo='La letra, que manda sobre el ritmo',
                 pista='cantando · y con el tresillo escrito, para verle la forma',
                 sistemas=[
                     dict(cap='a) así se escribe un tresillo: TRES notas dentro de un solo golpe · '
                              'di "u-ni-dad" en cada grupo y que las tres duren igual',
                          events=[{'pitch': 'E4', 'dur': 'e', 'tresillo': 71, 'beam': 7101},
                                  {'pitch': 'D4', 'dur': 'e', 'tresillo': 71, 'beam': 7101},
                                  {'pitch': 'D4', 'dur': 'e', 'tresillo': 71, 'beam': 7101},
                                  {'pitch': 'D4', 'dur': 'e', 'tresillo': 72, 'beam': 7102},
                                  {'pitch': 'C4', 'dur': 'e', 'tresillo': 72, 'beam': 7102},
                                  {'pitch': 'C4', 'dur': 'e', 'tresillo': 72, 'beam': 7102},
                                  {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}],
                          bars=1),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE HACE EL PASO 4',
                 texto='La letra va debajo del pentagrama, y aquí es la mejor ayuda que tienes: los '
                       'tresillos están donde la frase cantada los pide. Canta “Me mue-ro al pen-sar '
                       'que al-gún dí-a…” en voz alta, sin tocar, y después toca lo que has cantado.'),
            dict(tipo='escalera', valores=[52, 60, 66, 72, 78, 84],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · La izquierda entera, sin mirarte la mano.   '
                       '2 · La melodía de los cc. 1–3, alturas medidas.   '
                       '3 · El tresillo, contado y después en notas largas.   '
                       '4 · La letra cantada, sin piano.   '
                       '5 · La escalera, y las dos manos de los cc. 1–7.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
