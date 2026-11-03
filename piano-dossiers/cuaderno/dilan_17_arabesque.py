# -*- coding: utf-8 -*-
"""Arabesque (Burgmuller op. 100 nº 2, arr. a cuatro manos por MB) — Dilan.
   Ver TRANSCRIPCION_D15_17.md.

   OJO CON LA LECTURA: esta partitura lleva CUATRO pentagramas por sistema y
   sistemas() los empareja de dos en dos, mezclando al Primo con el Secondo.
   Se ha leido con engine/lector_4manos.py, que los agrupa de cuatro en
   cuatro: 0-1 = Primo (las dos manos en clave de sol), 2-3 = Secondo.

   El dosier esta escrito para el PRIMO, que es la parte que toca el alumno.
   La otra la toca la profesora, y por eso la hoja de montar habla de cosas
   que en el resto del cuaderno no salen: entrar juntos, mirar a la otra
   persona y no acelerar por su cuenta.

   La menor, sin armadura: todas las alteraciones van escritas.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
_B = [2500]


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


# --- lo medido en el Primo -------------------------------------------------
# la celula que da nombre a la pieza (cc. 3, 9, 31)
CELULA = corch(['A4', 'B4', 'C5', 'B4']) + [n('A4', 'h')]
# la escala que sube (cc. 4, 25, 30)
SUBIDA = corch(['D5', 'E5', 'F5', 'G5']) + [n('A5', 'h')]
# la escala entera bajando (c. 33)
BAJADA = corch(['E5', 'D5', 'C5', 'B4']) + [n('A4', 'h')]

# --- lo medido en el Secondo ----------------------------------------------
LAm = ('A3', 'C4', 'E4')
REm = ('A3', 'D4', 'F4')
DO = ('G3', 'C4', 'E4')
SOL7 = ('G3', 'B3', 'F4')

CANCION = dict(
    alumno='Dilan', num=17, nivel='avanzado', slug='Arabesque',
    titulo_corto='Arabesque', time_sig=(2, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' arabesque-burgmuller-( 4 manos).pdf'),
    yt='https://www.youtube.com/results?search_query=burgmuller+arabesque+op+100',

    ficha=dict(
        titulo='Arabesque',
        autor='Johann Friedrich Burgmüller · op. 100 nº 2 (1851) · arreglo a cuatro manos de MB',
        datos=[('Tonalidad', 'La menor'), ('Compás', '2/4'), ('Tempo', 'Allegro scherzando'),
               ('Formato', '4 manos'), ('Tu parte', 'Primo')],
        armonia=dict(
            titulo='Cómo está repartida la pieza',
            tarjetas=[
                ('TU PARTE · PRIMO', 'Las dos manos igual',
                 'Los dos pentagramas de arriba, los dos en clave de sol. Tocan lo mismo, a veces '
                 'en octava y a veces al unísono.'),
                ('LA OTRA · SECONDO', 'Acordes picados',
                 'La profesora: acordes staccato dos veces por compás y octavas en el bajo.'),
                ('LA CÉLULA', 'La · Si · Do · Si · La',
                 'Es el dibujo que da nombre a la pieza. Aparece en los cc. 3, 9 y 31.'),
                ('LA SUBIDA', 'Re · Mi · Fa · Sol · La',
                 'La escala que sube, en los cc. 4, 25 y 30. Medida.'),
            ],
            pie='En una pieza a cuatro manos no hay una mano derecha y una izquierda: hay dos personas '
                'sentadas en el mismo piano. Tú tocas el Primo, que es la melodía, y la profesora el '
                'Secondo, que es el acompañamiento. Los dos primeros compases los toca ella sola: tú '
                'entras en el tercero, y ahí ya hay que estar mirando.',
        ),
        ritmos=[
            ('PRIMO', 'la célula: cuatro semicorcheas y una nota larga',
             CELULA, AZUL, 'treble', None),
            ('SECONDO', 'acordes picados, dos por compás',
             [ac(LAm), ac(LAm)], OCRE, 'treble', None),
        ],
        especial=[
            'No hay armadura: la tonalidad es La menor y las alteraciones van escritas una a una.',
            'Es una pieza a CUATRO MANOS: cuatro pentagramas por sistema, no dos.',
            'Tú tocas el PRIMO, los dos pentagramas de arriba. Los dos van en clave de sol.',
            'Tus dos manos tocan casi siempre LO MISMO: unas veces en octava, otras al unísono.',
            'Los cc. 1 y 2 los toca solo la otra parte: tú entras en el c. 3.',
            'En el c. 5 hay un 8va: esa frase se toca una octava más arriba de lo escrito.',
        ],
        reto='Entrar juntos y seguir juntos. Todo lo que en las demás piezas del cuaderno depende de ti, '
             'aquí depende de dos. Puedes tocar tu parte perfecta y que la pieza no funcione porque cada '
             'uno va a su tempo.',
        truco='Antes de tocar, contad dos compases en voz alta los dos a la vez. Y mientras tocáis, '
              'respirad juntos al empezar cada frase: se nota más de lo que parece. Si te pierdes, no '
              'pares: salta al principio del compás siguiente y engancha.',
        sabias='Burgmüller escribió los 25 estudios del op. 100 para enseñar, no para concierto, y sin '
               'embargo la Arabesque se ha convertido en una de las piezas de piano más tocadas del '
               'mundo. Casi todo el mundo que ha estudiado piano la ha tocado alguna vez.',
        qr=dict(titulo='Escúchala a cuatro manos',
                texto='Busca una versión a cuatro manos y fíjate en cómo se miran al empezar.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Tu parte pide dos cosas: dedos rápidos y '
              'parejos en las dos manos a la vez, porque hacen lo mismo. Aquí se entrena eso en La '
              'menor, que es la tonalidad de la pieza.',
        reglas=['SIN ARMADURA · LA MENOR', 'LAS DOS MANOS, EXACTAMENTE IGUAL', 'EMPIEZA MUY LENTO'],
        ejercicios=[
            dict(num=1, titulo='Escala de La menor · dos octavas',
                 pista='LAS DOS MANOS a la vez, en octava · es lo que hace tu parte todo el rato',
                 events=corch(['A3', 'B3', 'C4', 'D4']) + corch(['E4', 'F4', 'G4', 'A4']) +
                        corch(['B4', 'C5', 'D5', 'E5']) + corch(['F5', 'G5', 'A5', 'A5']) +
                        corch(['A5', 'G5', 'F5', 'E5']) + corch(['D5', 'C5', 'B4', 'A4']) +
                        corch(['G4', 'F4', 'E4', 'D4']) + corch(['C4', 'B3', 'A3', 'A3']),
                 bars_per_line=8),
            dict(num=2, titulo='La célula, por toda la escala',
                 pista='sube · baja · vuelve · el dibujo de la pieza, movido grado a grado',
                 events=(corch(['A4', 'B4', 'C5', 'B4']) + corch(['B4', 'C5', 'D5', 'C5']) +
                         corch(['C5', 'D5', 'E5', 'D5']) + corch(['D5', 'E5', 'F5', 'E5']) +
                         corch(['E5', 'D5', 'C5', 'B4']) + corch(['A4', 'B4', 'A4', 'A4'])),
                 bars_per_line=6),
            dict(num=3, titulo='La célula al revés',
                 pista='baja · sube · vuelve · lo que la pieza no te hace practicar nunca',
                 events=(corch(['A4', 'G4', 'F4', 'G4']) + corch(['G4', 'F4', 'E4', 'F4']) +
                         corch(['F4', 'E4', 'D4', 'E4']) + corch(['E4', 'D4', 'C4', 'D4']) +
                         corch(['D4', 'E4', 'F4', 'G4']) + corch(['A4', 'A4', 'A4', 'A4'])),
                 bars_per_line=6),
            dict(num=4, titulo='Arpegio de La menor · dos octavas',
                 pista='fundamental · 3ª · 5ª · 8ª · el acorde sobre el que se apoya la pieza entera',
                 events=corch(['A3', 'C4', 'E4', 'A4']) + corch(['C5', 'E5', 'A5', 'A5']) +
                        corch(['A5', 'E5', 'C5', 'A4']) + corch(['E4', 'C4', 'A3', 'A3']),
                 bars_per_line=8),
            dict(num=5, titulo='Notas picadas', clef='bass',
                 pista='el gesto del Secondo · la mano rebota y no se queda apoyada',
                 events=[ac(('D3', 'F3', 'A3')), ac(('D3', 'F3', 'A3')),
                         ac(('E3', 'G3', 'B3')), ac(('E3', 'G3', 'B3')),
                         ac(('F3', 'A3', 'C4')), ac(('F3', 'A3', 'C4')),
                         ac(('E3', 'G3', 'B3')), ac(('E3', 'G3', 'B3')),
                         ac(('D3', 'F3', 'A3'), 'h')],
                 bars_per_line=5),
            dict(num=6, titulo='Y ahora una octava más arriba',
                 pista='el 8va del c. 5 · el mismo gesto, pero la mano se va a la derecha del teclado',
                 events=corch(['E5', 'F5', 'G5', 'A5']) + corch(['B5', 'C6', 'D6', 'C6']) +
                        corch(['B5', 'A5', 'G5', 'F5']) + corch(['E5', 'E5', 'E5', 'E5']),
                 bars_per_line=8),
            dict(num=7, titulo='Cuatro notas y parar',
                 pista='el gesto de la pieza · cuatro rápidas y una que se queda · sin acelerar en las cuatro',
                 events=(corch(['C5', 'D5', 'E5', 'D5']) + [n('C5', 'h')] +
                         corch(['D5', 'E5', 'F5', 'E5']) + [n('D5', 'h')] +
                         corch(['E5', 'F5', 'G5', 'F5']) + [n('E5', 'h')] +
                         corch(['C5', 'B4', 'A4', 'B4']) + [n('A4', 'h')]),
                 bars_per_line=8),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta: tu parte va en clave de sol en los dos '
              'pentagramas, así que aquí se practica sobre todo esa. Abajo se escucha.',
        sub_leer='di el nombre en voz alta · no hay armadura, pero sí alteraciones sueltas',
        chuleta_clef='treble',
        chuleta_titulo='EL REGISTRO DEL PRIMO (CLAVE DE SOL)',
        chuleta_pitches=['A3', 'C4', 'E4', 'A4', 'C5', 'E5', 'A5'],
        chuleta_nombres=['La', 'Do', 'Mi', 'La', 'Do', 'Mi', 'La'],
        ejercicios=[
            dict(num=1, titulo='Clave de Sol, registro medio',
                 pista='donde toca tu mano izquierda en esta pieza · también en clave de sol',
                 events=[n(p) for p in ('A3', 'E4', 'C4', 'G4', 'B3', 'F4', 'D4', 'A4',
                                        'C5', 'E4', 'G4', 'B4')],
                 bars_per_line=6),
            dict(num=2, titulo='Clave de Sol, registro alto',
                 pista='donde toca tu mano derecha · con líneas adicionales por arriba',
                 events=[n(p) for p in ('A4', 'C5', 'E5', 'A5', 'B4', 'D5', 'F5', 'C6',
                                        'G5', 'B5', 'E5', 'A5')],
                 bars_per_line=6),
            dict(num=3, titulo='Clave de Fa · la parte de la profesora', clef='bass',
                 pista='no la vas a tocar, pero sí la vas a oír · saber dónde está ayuda a encajar',
                 events=[n(p) for p in ('A2', 'E3', 'C3', 'G2', 'D3', 'B2', 'F3', 'A3',
                                        'C3', 'G3', 'E2', 'D2')],
                 bars_per_line=6),
        ],
        crono='¿Cuánto tardas en el ejercicio 2, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca cuatro notas seguidas rápidas, unas veces subiendo y otras bajando. Que diga '
                      'hacia dónde iban.'),
                ('B', 'Toca un acorde PICADO o LIGADO. Que diga cuál era: es la diferencia entre las dos '
                      'partes de esta pieza.'),
                ('C', 'Toca una tríada suelta: MAYOR o MENOR.'),
                ('+', 'Y lo más importante: contad dos compases juntos y empezad los dos a la vez.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Sube o baja?', pista='el grupo de cuatro notas rápidas',
                     n=10, opciones=['↑', '↓']),
                dict(letra='B', titulo='¿Picado o ligado?', pista='el acorde, corto o pegado',
                     n=8, opciones=['picado', 'ligado']),
                dict(letra='C', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=6, opciones=['M', 'm']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Todo lo que se cita es del PRIMO, que es tu parte. En esta pieza tus dos manos hacen lo '
              'mismo, así que el problema de siempre —coordinar las manos— no existe; el problema es '
              'coordinarte con otra persona. Por eso los pasos 1 y 2 son tu parte, que se estudia en '
              'casa, y los pasos 3 a 5 son lo que solo se puede trabajar en clase.',
        reglas=['ESTO ES SOLO TU PARTE · EL PRIMO', 'LAS DOS MANOS, IGUAL', 'EMPIEZA MUY LENTO'],
        bloques=[
            dict(num=1, titulo='La célula y la subida', clef='treble',
                 pista='cc. 3–4 medidos · La·Si·Do·Si·La y después Re·Mi·Fa·Sol·La · primero en '
                       'corcheas para leerlo, y al final con su figura de verdad',
                 sistemas=[
                     dict(cap='a) tu derecha lo toca aquí y tu izquierda una octava más abajo, '
                              'exactamente igual',
                          events=CELULA + SUBIDA + CELULA + SUBIDA, bars=4),
                     dict(cap='b) y la escala que baja del c. 33, que cierra la pieza · el último La '
                              'tiene que sonar a punto final',
                          events=BAJADA + BAJADA, bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='TUS DOS MANOS TOCAN LO MISMO',
                 texto='Míralo bien: en tu parte los dos pentagramas están en clave de sol y dicen lo '
                       'mismo. Unas veces la izquierda va una octava más abajo y otras las dos tocan '
                       'exactamente las mismas notas. Eso quiere decir dos cosas buenas: que solo hay que '
                       'aprender una línea, y que cualquier desajuste entre tus manos se oye muchísimo. '
                       'Estudia siempre las dos juntas, nunca por separado.'),
            dict(num=2, titulo='El 8va del c. 5, ya en su sitio',
                 pista='cc. 5–6 · andamio sobre las notas medidas, escrito donde de verdad se toca',
                 sistemas=[
                     dict(cap='a) practícala ya en la octava buena · si la lees donde está escrita y '
                              'luego la subes, se te caerá siempre en el mismo punto',
                          events=corch(['A5', 'B5', 'C6', 'B5']) + [n('A5', 'h')] +
                                 corch(['A5', 'B5', 'C6', 'C6']) + [n('C6', 'h')],
                          staccato=True,
                          bars=4),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES EL 8VA',
                 texto='Sobre tu parte aparece “8va” con una línea de puntos: todo lo que hay debajo se '
                       'toca una octava más arriba de lo escrito. No cambia nada del gesto, solo el sitio '
                       'del teclado. Cuando la línea de puntos se acaba, vuelves a tocar donde pone.'),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='Tu parte puede estar perfecta y la pieza no funcionar. Lo que viene aquí no se estudia '
              'solo: se trabaja en clase, las dos sentadas al piano. Ven con los pasos 1 y 2 sabidos y '
              'aprovecha la clase para esto.',
        reglas=['ENTRÁIS EN EL C. 3, NO EN EL 1', 'CONTAD JUNTOS EN VOZ ALTA', 'NADIE ACELERA POR SU CUENTA'],
        bloques=[
            dict(num=3, titulo='Los dos compases de espera',
                 pista='cc. 1–3 · lo que tú haces mientras suena la introducción: contar',
                 sistemas=[
                     dict(cap='a) dos compases de silencio y entras · cuéntalos en voz alta, no de memoria',
                          events=[sil('h'), sil('h')] + CELULA, bars=4),
                 ]),
            dict(tipo='nota',
                 etiqueta='TÚ NO EMPIEZAS LA PIEZA',
                 texto='Los cc. 1 y 2 los toca la otra parte sola: acordes picados y el bajo. Tú entras '
                       'en el c. 3, y ese es el momento más delicado de toda la pieza. No cuentes por '
                       'dentro: contad los dos en voz alta “un-dos, un-dos” durante los dos compases de '
                       'introducción, y respira justo antes de entrar. Si respiras, entras a tiempo casi '
                       'sin querer.'),
            dict(num=4, titulo='Lo que toca la otra parte', clef='bass',
                 pista='Secondo medido · La m · Re m · Do · Sol7 · esto NO lo tocas tú',
                 sistemas=[
                     dict(cap='a) escúchalo y aprende dónde cambia: es lo que te va a decir si vas bien',
                          events=[ac(('A2', 'C3', 'E3')), ac(('A2', 'C3', 'E3')),
                                  ac(('A2', 'D3', 'F3')), ac(('A2', 'D3', 'F3')),
                                  ac(('G2', 'C3', 'E3')), ac(('G2', 'C3', 'E3')),
                                  ac(('G2', 'B2', 'F3')), ac(('G2', 'B2', 'F3'))],
                          bars=4, clef='bass'),
                     dict(cap='b) y solo su bajo, una nota por compás · apréndetelo de oído: cuando '
                              'cambia, tú tienes que estar en el sitio',
                          events=[n('A2', 'h'), n('A2', 'h'), n('G2', 'h'), n('G2', 'h')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA PIEZA SE ESTUDIA DISTINTO',
                 texto='En todas las demás del cuaderno el problema es coordinar tus dos manos. Aquí tus '
                       'dos manos hacen lo mismo, así que ese problema no existe. La parte que se estudia '
                       'en casa es la fácil, y la difícil solo se puede trabajar en pareja: entrad juntas '
                       'en el c. 3 una y otra vez, hasta que no haga falta ninguna señal.'),
            dict(tipo='escalera', valores=[60, 76, 88, 100, 112, 126],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · La célula, la subida y la bajada, las dos manos juntas desde el primer día.   '
                       '2 · El 8va, directamente en la octava alta.   '
                       '3 · Los dos compases de espera, contados en voz alta veinte veces.   '
                       '4 · Escuchar la otra parte y saber dónde cambia.   '
                       '5 · La escalera, y en clase: entrar juntas en el c. 3.'),
        ],
    ),

)

# El recurso que la pieza EXPLICA y no dibujaba: durante meses se anotó como
# "no cabe en la hoja". Desde que la hoja se pagina sola, esa excusa dejó de
# ser cierta.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 20, 'C4', 'C3',
    'la mano en Do antes de la carrera de semicorcheas',
    desde=6, time_sig=(2, 4)) + [
    # Antes aqui iba `bloque_semicorcheas`, que escribe una escala generica de
    # la tonalidad. La figura la veia, si, pero no sobre SU pieza. Como la
    # carrera de semicorcheas es literalmente el material de los cc. 3-4 y del
    # c. 33, que ya estan medidos, se cita eso: mismo coste de hoja y el alumno
    # lee en el cuaderno exactamente lo que va a leer en la partitura.
    dict(num=5, titulo='La carrera de semicorcheas, la de tu partitura',
         pista='cc. 3–4 y c. 33 medidos · la misma célula que ya has tocado en corcheas, ahora '
               'con la figura que trae impresa',
         sistemas=[
             dict(cap='a) cc. 3–4 · cuatro notas por golpe, y las cuatro del mismo peso',
                  events=[{'pitch': q, 'dur': 's', 'beam': 9310 + i // 4}
                          for i, q in enumerate(['A4', 'B4', 'C5', 'B4',
                                                 'A4', 'D5', 'E5', 'F5'])],
                  bars=1),
             dict(cap='b) c. 33 · la bajada que cierra la pieza, también en semicorcheas',
                  events=[{'pitch': q, 'dur': 's', 'beam': 9312 + i // 4}
                          for i, q in enumerate(['E5', 'D5', 'C5', 'B4',
                                                 'A4', 'G4', 'F4', 'E4'])],
                  bars=1, show_time=False),
         ])]

if __name__ == '__main__':
    print('generado', construir(CANCION))
