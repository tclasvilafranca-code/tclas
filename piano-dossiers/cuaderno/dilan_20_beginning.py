# -*- coding: utf-8 -*-
"""It's Beginning to Look a Lot Like Christmas (arr. Rachel Chytelman)
   — Dilan, avanzado. Ver TRANSCRIPCION_D18_20.md.

   Segunda pieza a CUATRO MANOS del album, y con una diferencia respecto a la
   Arabesque: aqui el Piano 2 lleva los DOS pentagramas en clave de fa, asi
   que hay que leerla con lector_4manos.CLAVES = ['treble','treble','bass','bass'].

   Do mayor, 6/8. El Primo (la parte del alumno) toca la MISMA melodia con las
   dos manos, separadas por una octava, de principio a fin.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
_B = [2800]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='q'):
    return {'pitches': list(ps), 'dur': d}


def sil(d='q'):
    return {'rest': True, 'dur': d}


def corch(ps, agrupar=3):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


DO = ('E3', 'G3', 'C4')
FA = ('F3', 'A3', 'C4')
SOL = ('D3', 'G3', 'B3')
LAm = ('E3', 'A3', 'C4')

CANCION = dict(
    alumno='Dilan', num=20, nivel='avanzado', slug='BeginningChristmas',
    titulo_corto="It's Beginning to Look a Lot Like Christmas",
    time_sig=(6, 8), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf'),
    yt='https://www.youtube.com/results?search_query=its+beginning+to+look+a+lot+like+christmas',

    ficha=dict(
        titulo="It's Beginning to Look a Lot Like Christmas",
        autor='Meredith Willson (1951) · arreglo a cuatro manos de Rachel Chytelman',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '6/8'), ('Formato', '4 manos'),
               ('Tu parte', 'Primo'), ('Mano izq.', 'Igual que la dcha.')],
        armonia=dict(
            titulo='Cómo está repartida la pieza',
            tarjetas=[
                ('TU PARTE · PRIMO', 'La melodía, doble',
                 'Los dos pentagramas de arriba, en clave de sol. Las dos manos tocan lo mismo, '
                 'separadas por una octava.'),
                ('LA OTRA · SECONDO', 'Dos claves de fa',
                 'La profesora: el acorde arriba y la fundamental abajo, en blanca con puntillo.'),
                ('LA ARMONÍA', 'Do · Fa · Sol · La m',
                 'Medida en el Secondo. Cuatro acordes en toda la primera página.'),
                ('EL 6/8', 'Seis corcheas',
                 'Se cuenta en dos: "UN-dos-tres DOS-dos-tres". No en seis.'),
            ],
            pie='En 6/8 hay seis corcheas por compás, pero no se cuentan seis: se cuentan dos grupos de '
                'tres. Por eso suena a balanceo y no a marcha. Si lo cuentas en seis, la canción se '
                'vuelve pesada; si lo cuentas en dos, sale sola.',
        ),
        ritmos=[
            ('PRIMO', 'la melodía · las dos manos tocan esto, a una octava de distancia',
             corch(['E5', 'F5', 'G5']) + corch(['A5', 'G5', 'F5']), AZUL, 'treble', None),
            ('SECONDO', 'un acorde por compás, sostenido entero',
             [ac(DO, 'h.')], OCRE, 'bass', None),
            ('SECONDO · el siguiente', 'el mismo gesto, movido a Fa',
             [ac(FA, 'h.')], OCRE, 'bass', None),
        ],
        especial=[
            'No hay armadura: la tonalidad es Do mayor.',
            'Va en 6/8: seis corcheas por compás, contadas en DOS grupos de tres.',
            'Es una pieza a CUATRO MANOS: cuatro pentagramas por sistema.',
            'Tú tocas el PRIMO, los dos pentagramas de arriba, los dos en clave de sol.',
            'Tus dos manos tocan LO MISMO, separadas por una octava, de principio a fin.',
            'El Piano 2 lleva los dos pentagramas en clave de FA: suena todo por debajo de ti.',
            'Los dos primeros compases los toca solo la otra parte: tú entras después.',
        ],
        reto='Que tus dos manos suenen como una sola. Tocan lo mismo a una octava, así que cualquier '
             'desajuste, por pequeño que sea, se oye como un eco. Y encima hay que encajar con otra '
             'persona.',
        truco='Estudia siempre las dos manos juntas desde el primer día, nunca por separado: el problema '
              'no es aprenderse las notas, es que caigan exactamente a la vez. Y cuenta en dos, no en '
              'seis: "UN-dos-tres DOS-dos-tres".',
        sabias='Meredith Willson la escribió en 1951, el mismo año en que empezó a componer "The Music '
               'Man". Perry Como y Bing Crosby la grabaron el mismo mes, sin saberlo, y las dos '
               'versiones salieron a la venta a la vez.',
        qr=dict(titulo='Escúchala a cuatro manos',
                texto='Busca una versión a dúo y fíjate en cómo se coordinan al empezar.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Tu parte pide dos manos que toquen lo mismo '
              'exactamente a la vez, y un 6/8 contado en dos. Aquí se entrenan las dos cosas, en '
              'Do mayor.',
        reglas=['SIN ARMADURA · DO MAYOR', 'LAS DOS MANOS, EXACTAMENTE A LA VEZ', 'CUENTA EN DOS'],
        ejercicios=[
            dict(num=1, titulo='Escala de Do mayor · dos octavas',
                 pista='LAS DOS MANOS a la vez, en octava · es lo que hace tu parte todo el rato',
                 events=corch(['C4', 'D4', 'E4']) + corch(['F4', 'G4', 'A4']) +
                        corch(['B4', 'C5', 'D5']) + corch(['E5', 'F5', 'G5']) +
                        corch(['A5', 'B5', 'C6']) + corch(['B5', 'A5', 'G5']) +
                        corch(['F5', 'E5', 'D5']) + corch(['C5', 'B4', 'A4']) +
                        corch(['G4', 'F4', 'E4']) + corch(['D4', 'C4', 'C4']),
                 bars_per_line=5),
            dict(num=2, titulo='Contar en dos, no en seis',
                 pista='seis corcheas por compás, pero solo dos golpes de pie · aprieta la 1.ª de cada tres',
                 events=corch(['C5', 'D5', 'E5']) + corch(['F5', 'E5', 'D5']) +
                        corch(['C5', 'D5', 'E5']) + corch(['G5', 'F5', 'E5']) +
                        corch(['D5', 'E5', 'F5']) + corch(['E5', 'D5', 'C5']) +
                        [n('C5', 'h.')],
                 bars_per_line=4),
            dict(num=3, titulo='Arpegio de Do mayor · dos octavas',
                 pista='fundamental · 3ª · 5ª · 8ª · con las dos manos, siempre a la vez',
                 events=corch(['C4', 'E4', 'G4']) + corch(['C5', 'E5', 'G5']) +
                        corch(['C6', 'G5', 'E5']) + corch(['C5', 'G4', 'E4']) +
                        [n('C4', 'h.')],
                 bars_per_line=5),
            dict(num=4, titulo='Las dos manos, una octava aparte',
                 pista='el gesto exacto de tu parte · si oyes un eco, no están cayendo juntas',
                 events=corch(['G4', 'A4', 'B4']) + corch(['C5', 'B4', 'A4']) +
                        corch(['G4', 'F4', 'E4']) + corch(['D4', 'E4', 'F4']) +
                        [n('G4', 'h.')],
                 bars_per_line=5),
            dict(num=5, titulo='El acompañamiento del Secondo', clef='bass',
                 pista='lo que toca la profesora · un acorde por compás, sostenido los seis tiempos',
                 events=[ac(DO, 'h.'), ac(FA, 'h.'), ac(SOL, 'h.'), ac(LAm, 'h.'),
                         ac(FA, 'h.'), ac(SOL, 'h.'), ac(DO, 'h.'), ac(DO, 'h.')],
                 bars_per_line=8),
            dict(num=6, titulo='Y ahora en el registro agudo',
                 pista='tu mano derecha vive arriba · con líneas adicionales, sin cambiar el gesto',
                 events=corch(['C6', 'B5', 'A5']) + corch(['G5', 'A5', 'B5']) +
                        corch(['C6', 'D6', 'E6']) + corch(['D6', 'C6', 'B5']) +
                        [n('C6', 'h.')],
                 bars_per_line=5),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta: tu parte va en clave de sol en los dos '
              'pentagramas, así que se practica sobre todo esa. Abajo se escucha.',
        sub_leer='di el nombre en voz alta · no hay armadura, y casi no hay alteraciones',
        chuleta_clef='treble',
        chuleta_titulo='EL REGISTRO DEL PRIMO (CLAVE DE SOL)',
        chuleta_pitches=['C4', 'E4', 'G4', 'C5', 'E5', 'G5', 'C6'],
        chuleta_nombres=['Do', 'Mi', 'Sol', 'Do', 'Mi', 'Sol', 'Do'],
        ejercicios=[
            dict(num=1, titulo='Clave de Sol, registro medio',
                 pista='donde toca tu mano izquierda · también en clave de sol',
                 events=[n(p, 'e') for p in ('C4', 'G4', 'E4', 'A4', 'F4', 'B4', 'D4', 'C5',
                                             'G4', 'E4', 'A4', 'F4')],
                 bars_per_line=4),
            dict(num=2, titulo='Clave de Sol, registro alto',
                 pista='donde toca tu mano derecha · con líneas adicionales por arriba',
                 events=[n(p, 'e') for p in ('C5', 'G5', 'E5', 'B5', 'A5', 'D6', 'F5', 'C6',
                                             'E6', 'G5', 'B5', 'C5')],
                 bars_per_line=4),
            dict(num=3, titulo='Clave de Fa · la parte de la profesora', clef='bass',
                 pista='sus dos pentagramas van en clave de fa · saber dónde está ayuda a encajar',
                 events=[n(p, 'e') for p in ('C3', 'G3', 'E3', 'A3', 'F3', 'B3', 'D3', 'C4',
                                             'G2', 'E2', 'A2', 'F2')],
                 bars_per_line=4),
        ],
        crono='¿Cuánto tardas en el ejercicio 2, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca dos notas a la vez separadas por una OCTAVA, y otras veces por una quinta. '
                      'Que diga cuál era: la octava es lo que hacen sus dos manos.'),
                ('B', 'Toca seis corcheas agrupadas en DOS o en TRES. Que diga cómo iban: es la '
                      'diferencia entre 6/8 y 3/4.'),
                ('C', 'Toca una tríada suelta: MAYOR o MENOR.'),
                ('+', 'Y lo más importante: contad "un-dos-tres dos-dos-tres" juntos y empezad a la vez.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Octava o quinta?', pista='las dos notas, a la vez',
                     n=10, opciones=['8ª', '5ª']),
                dict(letra='B', titulo='¿De dos o de tres?', pista='cómo se agrupan las seis corcheas',
                     n=8, opciones=['2', '3']),
                dict(letra='C', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=6, opciones=['M', 'm']),
            ],
        ),
    ),

    piano1=dict(
        intro='La partitura, abierta en trozos. Todo lo que se cita es del PRIMO, que es tu parte, y '
              'está medido con el lector de cuatro manos. Recuerda que tu izquierda toca exactamente lo '
              'mismo, una octava más abajo.',
        reglas=['ESTO ES SOLO TU PARTE · EL PRIMO', 'LAS DOS MANOS A LA VEZ', 'CUENTA EN DOS'],
        bloques=[
            dict(num=1, titulo='La melodía de los cc. 1–4',
                 pista='cc. 1–4 medidos · Mi · Fa · Sol · La · Sol · Fa · Sol · La · Do · Do · Sol',
                 sistemas=[dict(cap='tu derecha lo toca aquí y tu izquierda una octava más abajo, a la vez',
                                events=corch(['E5', 'F5', 'G5']) + corch(['A5', 'G5', 'F5']) +
                                       [n('G5', 'h.')] +
                                       corch(['A5', 'C6', 'C6']) + corch(['C6', 'B5', 'A5']) +
                                       [n('G5', 'h.')],
                                bars=4)]),
            dict(tipo='nota',
                 etiqueta='TUS DOS MANOS SON UNA SOLA',
                 texto='Los dos pentagramas de tu parte dicen lo mismo, separados por una octava. Solo '
                       'hay una línea que aprender, pero cualquier desajuste entre tus manos se oye como '
                       'un eco. Estudia siempre las dos juntas: el problema no son las notas, es que '
                       'caigan a la vez.'),
            dict(num=2, titulo='Y los cc. 6–7, con la nota repetida',
                 pista='cc. 6–7 medidos · Do repetido, que es donde la frase se planta',
                 sistemas=[dict(cap='las dos manos repiten la misma nota: es donde más se oye si una '
                                    'llega antes que la otra',
                                events=corch(['C6', 'C6', 'C6']) + corch(['C6', 'C6', 'C6']) +
                                       corch(['A5', 'B5', 'C6']) + corch(['B5', 'A5', 'G5']) +
                                       [n('C6', 'h.')],
                                bars=3)]),
            dict(num=3, titulo='La frase del c. 12',
                 pista='c. 12 medido · Si · Do · Si · Sol · Sol · baja y se queda',
                 sistemas=[dict(cap='es la frase que cierra la primera parte: tiene que sonar a punto y '
                                    'aparte',
                                events=corch(['B5', 'C6', 'B5']) + corch(['G5', 'G5', 'G5']) +
                                       [n('A5', 'h.')],
                                bars=3)]),
            dict(tipo='nota',
                 etiqueta='LA MELODÍA VA ARRIBA DEL TODO',
                 texto='Tu mano derecha toca por encima del Do5 casi siempre, y ahí hay muchas líneas '
                       'adicionales. No cuentes líneas cada vez: aprende de memoria dónde están el Do5, '
                       'el Mi5 y el Sol5, y lee el resto por distancia respecto a ellos. Con tres notas '
                       'de referencia se lee todo el registro agudo sin contar ni una línea.'),
            dict(num=4, titulo='Lo que toca la otra parte', clef='bass',
                 pista='Secondo medido · Do · Fa · Do · Fa · Sol · La m · para que sepas qué estás oyendo',
                 sistemas=[dict(cap='esto NO lo tocas tú · escúchalo: el cambio de acorde te dice si '
                                    'vais juntas',
                                events=[ac(DO, 'h.'), ac(FA, 'h.'), ac(DO, 'h.'), ac(FA, 'h.'),
                                        ac(SOL, 'h.'), ac(LAm, 'h.')],
                                bars=6, clef='bass')]),
            dict(num=5, titulo='Lo mismo, pero donde lo toca tu izquierda',
                 pista='cc. 1–2 · exactamente la misma frase, una octava más abajo',
                 sistemas=[dict(cap='léela aquí y tócala con la izquierda sola una vez · después junta '
                                    'las dos y escucha si hay eco',
                                events=corch(['E4', 'F4', 'G4']) + corch(['A4', 'G4', 'F4']) +
                                       [n('G4', 'h.')],
                                bars=2)]),
        ],
    ),

    piano2=dict(
        intro='Montarla es, como en la Arabesque, un problema de dos. Y además hay que resolver el 6/8, '
              'que es el compás que más se cuenta mal de todo el cuaderno.',
        reglas=['CUENTA EN DOS, NO EN SEIS', 'LAS DOS MANOS, UNA SOLA COSA', 'EMPEZAD JUNTAS'],
        bloques=[
            dict(tipo='nota',
                 etiqueta='EL 6/8 NO SE CUENTA EN SEIS',
                 texto='Hay seis corcheas en cada compás, y la tentación es contar "un-dos-tres-cuatro-'
                       'cinco-seis". No lo hagas: se cuenta en DOS, "UN-dos-tres DOS-dos-tres", con solo '
                       'dos golpes de pie por compás. Esa es la diferencia entre que la canción suene a '
                       'balanceo, que es lo que es, o a marcha militar. Cuenta así desde el primer día y '
                       'no tendrás que corregirlo después.'),
            dict(num=5, titulo='El 6/8, en dos golpes',
                 pista='andamio · aprieta un poco la primera de cada tres corcheas y no las demás',
                 sistemas=[dict(cap='el pie marca solo dos veces por compás · si marcas seis, ya lo '
                                    'estás contando mal',
                                events=corch(['G4', 'A4', 'B4']) + corch(['C5', 'B4', 'A4']) +
                                       corch(['G4', 'A4', 'B4']) + corch(['C5', 'D5', 'E5']) +
                                       corch(['D5', 'C5', 'B4']) + corch(['A4', 'G4', 'F4']) +
                                       [n('G4', 'h.')],
                                bars=4)]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE ENSAYA UNA PIEZA A DÚO',
                 texto='Lo que se estudia en casa es tu parte sola, y eso es lo fácil. Lo difícil solo se '
                       'puede trabajar en clase, las dos sentadas al piano, y son tres cosas: empezar a '
                       'la vez, respirar juntas al empezar cada frase, y no acelerar por tu cuenta cuando '
                       'te sientas segura. Si te pierdes en medio, no pares: cuenta hasta el principio '
                       'del compás siguiente y engancha ahí.'),
            dict(num=6, titulo='La frase entera, sin parar',
                 pista='andamio sobre las notas medidas · ocho compases seguidos, contando en dos',
                 sistemas=[dict(cap='si te equivocas, no repitas el compás: vuelve al principio de la '
                                    'frase, que es como se toca en pareja',
                                events=corch(['E5', 'F5', 'G5']) + corch(['A5', 'G5', 'F5']) +
                                       corch(['G5', 'A5', 'B5']) + [n('C6', 'h.')] +
                                       corch(['C6', 'B5', 'A5']) + corch(['G5', 'A5', 'B5']) +
                                       corch(['A5', 'G5', 'F5']) + [n('E5', 'h.')],
                                bars=4)]),
            dict(tipo='nota',
                 etiqueta='CÓMO ESTUDIARLA ESTA SEMANA',
                 texto='1 · Tu parte, las dos manos juntas desde el primer día, muy lento. '
                       '2 · Cuenta el 6/8 en dos, en voz alta, sin tocar. '
                       '3 · La frase de los cc. 1 al 4, hasta que las dos manos caigan exactamente juntas. '
                       '4 · La misma frase mirando al techo, sin mirarte las manos. '
                       '5 · Y en clase: los dos primeros compases, una y otra vez, hasta empezar juntas.'),
            dict(tipo='escalera', valores=[54, 63, 72, 80, 88, 96],
                 regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='tracker', titulo='La prueba de la semana',
                 pie='Marca el día en que tus dos manos hayan sonado como una sola, sin eco.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
