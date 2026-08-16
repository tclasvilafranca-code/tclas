# -*- coding: utf-8 -*-
"""Adagio en Sol menor (Albinoni, arr. A. C. Escobes) — Dilan, avanzado.
   Ver TRANSCRIPCION_D15_17.md.

   El hallazgo de esta pieza esta medido compas a compas en quince compases
   seguidos: la mano izquierda hace SIEMPRE fundamental - octava -
   fundamental, en tres negras, y las notas graves dibujan el bajo
   descendente que es la identidad del Adagio.

   Con armadura de Sol menor los Si y los Mi son bemoles y no se escriben; el
   Fa sostenido de la sensible SI se escribe, y no esta medido (el lector no
   ve alteraciones), asi que no se cita ninguna alteracion accidental.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOLm = 'Sol menor'
_B = [2300]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


def pie(grave, agudo):
    """El gesto de la izquierda: fundamental, octava, fundamental."""
    return [n(grave), n(agudo), n(grave)]


# --- el bajo descendente, medido compas a compas ---------------------------
BAJO_1 = [('G2', 'G3'), ('F2', 'F3'), ('E2', 'E3'), ('D2', 'D3'),
          ('C2', 'C3'), ('D2', 'D3'), ('G2', 'G3')]
BAJO_2 = [('G2', 'G3'), ('A2', 'A3'), ('B2', 'B3'), ('B2', 'B3'),
          ('C3', 'C4'), ('A2', 'A3'), ('B2', 'B3'), ('A2', 'A3')]

CANCION = dict(
    alumno='Dilan', num=16, nivel='avanzado', slug='AdagioAlbinoni',
    titulo_corto='Adagio en Sol menor', time_sig=(3, 4), key_sig=SOLm,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           'Adagio en sol menor. Albinoni.pdf'),
    yt='https://www.youtube.com/results?search_query=albinoni+adagio+in+g+minor',

    ficha=dict(
        titulo='Adagio en Sol menor',
        autor='Atribuido a Tomaso Albinoni · arr. A. C. Escobés',
        datos=[('Tonalidad', 'Sol menor'), ('Compás', '3/4'), ('Tempo', 'Adagio'),
               ('Dinámica', 'p'), ('Mano izq.', '3 negras')],
        armonia=dict(
            titulo='El bajo que baja',
            tarjetas=[
                ('EL GESTO', 'Grave · octava · grave',
                 'Tres negras por compás, siempre igual. Cambia la nota, nunca el dibujo.'),
                ('CC. 1–7', 'Sol · Fa · Mi♭ · Re',
                 'Y sigue: Do, Re, Sol. Un bajo que baja por grados hasta volver a casa.'),
                ('CC. 8–15', 'Sol · La · Si♭ · Do',
                 'Ahora sube. Medido compás a compás, sin una sola excepción.'),
                ('POR QUÉ IMPORTA', 'Es la pieza',
                 'Ese bajo es lo que reconoce todo el mundo. La melodía va encima, pero manda él.'),
            ],
            pie='Un bajo que baja por grados y da vueltas se llama bajo obstinado, y es un recurso del '
                'Barroco: la misma línea de graves repitiéndose mientras encima cambia todo. Aquí está '
                'medido y no admite duda, porque las notas de la izquierda son negras sueltas y se leen '
                'sin ninguna ambigüedad. Es lo primero que hay que montar.',
        ),
        ritmos=[
            ('MI', 'tres negras: grave, la octava y otra vez el grave',
             pie('G2', 'G3'), OCRE, 'bass', SOLm),
            ('MI · el siguiente', 'lo mismo, un grado más abajo',
             pie('F2', 'F3'), OCRE, 'bass', SOLm),
            ('MD', 'la melodía, con puntillos y notas muy cortas',
             [n('G4', 'h'), n('A4')], AZUL, 'treble', SOLm),
        ],
        especial=[
            'Armadura de dos bemoles: todos los Si y los Mi son ♭. La tonalidad es Sol menor.',
            'Pone Adagio y pone p: es la pieza más lenta y más suave del cuaderno.',
            'La izquierda toca TRES NEGRAS por compás y nada más, en toda la página.',
            'La nota de en medio es siempre la octava de la primera: la mano no cambia de forma.',
            'Hay FA♯ escritos a mano: es la sensible, y la armadura no la lleva.',
            'La derecha tiene puntillos, fusas y tresillos: es donde está toda la dificultad.',
        ],
        reto='Que la izquierda no suene a metrónomo. Tres negras iguales, compás tras compás, a una '
             'velocidad lentísima: si las tocas todas con el mismo peso, esto deja de ser un Adagio y '
             'se convierte en un ejercicio de mecánica.',
        truco='Toca la izquierda sola y busca que la primera negra de cada compás pese y las otras dos '
              'se apaguen. Después canta la melodía encima sin tocarla. Y cuando pongas la derecha, '
              'sigue pensando en el bajo: es lo que sostiene la pieza.',
        sabias='La escribió Remo Giazotto en 1958, no Albinoni: dijo haberla reconstruido a partir de un '
               'fragmento encontrado en Dresde que nunca enseñó a nadie. Hoy se acepta que es suya casi '
               'por completo, pero se sigue llamando Adagio de Albinoni.',
        qr=dict(titulo='Escúchalo con cuerdas',
                texto='El original es para cuerda y órgano. Escucha el bajo: es tu mano izquierda.',
                png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta pieza pide dos cosas: una izquierda que '
              'sostenga un bajo lentísimo sin sonar a máquina, y una derecha que sepa cantar por encima. '
              'Aquí se trabaja el gesto de la izquierda por toda la tonalidad de Sol menor.',
        reglas=['ARMADURA DE SOL MENOR: SI♭ Y MI♭', 'LA PRIMERA NEGRA PESA MÁS', 'ADAGIO DE VERDAD'],
        ejercicios=[
            dict(num=1, titulo='Escala de Sol menor · dos octavas', clef='bass',
                 pista='manos separadas · dos bemoles, y el pulgar por debajo sin bache',
                 events=corch(['G2', 'A2', 'B2', 'C3', 'D3', 'E3']) +
                        corch(['F3', 'G3', 'A3', 'B3', 'C4', 'D4']) +
                        corch(['E4', 'F4', 'G4', 'F4', 'E4', 'D4']) +
                        corch(['C4', 'B3', 'A3', 'G3', 'F3', 'E3']) +
                        corch(['D3', 'C3', 'B2', 'A2', 'G2', 'G2']),
                 bars_per_line=5),
            dict(num=2, titulo='El gesto, por toda la tonalidad', clef='bass',
                 pista='grave · octava · grave, sobre los seis grados de Sol menor',
                 events=(pie('C3', 'C4') + pie('B2', 'B3') + pie('A2', 'A3') +
                         pie('G2', 'G3') + pie('F2', 'F3') + pie('C3', 'C4')),
                 bars_per_line=6),
            dict(num=3, titulo='El gesto al revés', clef='bass',
                 pista='octava · grave · octava · lo que la pieza nunca te hace practicar',
                 events=([n('G3'), n('G2'), n('G3')] + [n('F3'), n('F2'), n('F3')] +
                         [n('E3'), n('E2'), n('E3')] + [n('D3'), n('D2'), n('D3')] +
                         [n('C3'), n('C2'), n('C3')] + [n('G3'), n('G2'), n('G3')]),
                 bars_per_line=6),
            dict(num=4, titulo='La octava sola, abriendo la mano', clef='bass',
                 pista='el 5 y el 1 · que las dos suenen exactamente a la vez',
                 events=[{'pitches': ['G2', 'G3'], 'dur': 'h.'},
                         {'pitches': ['F2', 'F3'], 'dur': 'h.'},
                         {'pitches': ['E2', 'E3'], 'dur': 'h.'},
                         {'pitches': ['D2', 'D3'], 'dur': 'h.'},
                         {'pitches': ['C2', 'C3'], 'dur': 'h.'},
                         {'pitches': ['G2', 'G3'], 'dur': 'h.'}],
                 bars_per_line=6),
            dict(num=5, titulo='La sensible de Sol menor',
                 pista='el Fa♯ que la armadura no lleva · es la nota que hace volver a la tónica',
                 events=[n('D4'), n('F#4'), n('A4'),
                         n('G4', 'h.'),
                         n('C5'), n('A4'), n('F#4'),
                         n('G4', 'h.')],
                 bars_per_line=4),
            dict(num=6, titulo='Cantar con la derecha',
                 pista='notas largas, una por compás · lo que hace la melodía cuando no corre',
                 events=[n('G4', 'h.'), n('A4', 'h.'), n('B4', 'h.'), n('C5', 'h.'),
                         n('D5', 'h.'), n('C5', 'h.'), n('B4', 'h.'), n('G4', 'h.')],
                 bars_per_line=8),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con dos bemoles. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · armadura de Sol menor: Si y Mi son bemol',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DEL BAJO (CLAVE DE FA)',
        chuleta_pitches=['C2', 'E2', 'G2', 'C3', 'E3', 'G3'],
        chuleta_nombres=['Do', 'Mi♭', 'Sol', 'Do', 'Mi♭', 'Sol'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa, registro grave', clef='bass',
                 pista='donde vive el bajo · con líneas adicionales por abajo',
                 events=[n(p) for p in ('G2', 'C2', 'E2', 'D2', 'F2', 'A2', 'B2', 'C3',
                                        'G3', 'E3', 'D3', 'A3', 'F3', 'B3', 'C2')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · registro medio-alto',
                 events=[n(p) for p in ('G4', 'D5', 'B4', 'F5', 'C5', 'A4', 'E5', 'G5',
                                        'D4', 'F4', 'C5', 'B4', 'A4', 'E4', 'G4')]),
            dict(num=3, titulo='Con el Fa sostenido',
                 pista='la sensible · una alteración suelta vale hasta la barra de compás, no más',
                 events=[n('D4'), n('F#4'), n('A4'),
                         n('G4'), n('F4'), n('D4'),
                         n('C5'), n('A4'), n('F#4'),
                         n('G4', 'h.')]),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca el gesto de tres negras y unas veces pon la octava en medio y otras la '
                      'quinta. Que diga cuál fue.'),
                ('B', 'Toca dos notas graves seguidas y que diga si la segunda sube o baja.'),
                ('C', 'Toca una tríada suelta: MAYOR o MENOR. Esta pieza es menor de principio a fin.'),
                ('+', 'Y sin escribir: toca el bajo Sol–Fa–Mi♭–Re y que lo cante.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Octava o quinta?', pista='la nota de en medio del gesto',
                     n=10, opciones=['8ª', '5ª']),
                dict(letra='B', titulo='¿Sube o baja?', pista='de una nota grave a la siguiente',
                     n=8, opciones=['↑', '↓']),
                dict(letra='C', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=6, opciones=['M', 'm']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Esta pieza no se estudia leyendo de arriba abajo: se monta por capas, y la izquierda va '
              'primero porque en el Adagio la izquierda ES la pieza. Cinco pasos, en este orden, sin '
              'saltarse ninguno. Cada paso está entero aquí abajo: se toca, no se lee.',
        reglas=['UN PASO NO SE ABANDONA A MEDIAS', 'LA PRIMERA NEGRA PESA MÁS', 'ADAGIO, NO LENTO A MEDIAS'],
        bloques=[
            dict(num=1, titulo='El esqueleto: una nota por compás', clef='bass',
                 pista='cc. 1–15 medidos · son siete notas y ocho notas, y son toda la pieza',
                 sistemas=[
                     dict(cap='a) cc. 1–7 · Sol · Fa · Mi♭ · Re · Do · Re · Sol — baja por grados y vuelve',
                          events=[n(g, 'h.') for g, _ in BAJO_1], bars=7, clef='bass'),
                     dict(cap='b) cc. 8–15 · Sol · La · Si♭ · Si♭ · Do · La · Si♭ · La — ahora sube, y la música se abre',
                          events=[n(g, 'h.') for g, _ in BAJO_2], bars=8, clef='bass', show_time=False),
                     dict(cap='c) las dos seguidas, sin parar entre el 7 y el 8 · esto se aprende DE MEMORIA antes de pasar al 2',
                          events=[n(g, 'h.') for g, _ in BAJO_1] + [n(g, 'h.') for g, _ in BAJO_2],
                          bars=8, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='ESTO ES UN BAJO OBSTINADO',
                 texto='Esa línea de graves dando vueltas mientras encima cambia la melodía se llama bajo '
                       'obstinado, y es un recurso del Barroco. Puedes tocar solo la izquierda delante de '
                       'cualquiera y va a saber qué es. Por eso se aprende de memoria: para leer después la '
                       'derecha sin mirar nunca hacia abajo.'),
            dict(num=2, titulo='El mismo bajo, como está escrito', clef='bass',
                 pista='tres negras por compás · la primera con peso de brazo, las otras dos casi sin dedo',
                 sistemas=[
                     dict(cap='a) cc. 1–7 · grave · octava · grave: cambia la nota, nunca el gesto',
                          events=[e for g, a in BAJO_1 for e in pie(g, a)], bars=7, clef='bass'),
                     dict(cap='b) y los quince compases seguidos · este es el paso 2 terminado',
                          events=[e for g, a in BAJO_1 for e in pie(g, a)] +
                                 [e for g, a in BAJO_2 for e in pie(g, a)],
                          bars=8, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='Los pasos 1 y 2 ya están en los dedos y de memoria. Ahora se coloca la mano, se entra en '
              'la melodía y se sube de velocidad. El paso 5 se repite todas las semanas hasta fin de curso.',
        reglas=['LA IZQUIERDA, DE MEMORIA', 'LA DERECHA, CONTANDO EN VOZ ALTA', 'ADAGIO Y p'],
        bloques=[
            dict(num=3, titulo='La octava sola, para colocar la mano', clef='bass',
                 pista='las dos notas a la vez, el 5 abajo y el 1 arriba · si no llega, no estires: mueve el brazo entero',
                 sistemas=[
                     dict(cap='a) cc. 1–7 · se coloca y se suelta, sin apretar',
                          events=[{'pitches': [g, a], 'dur': 'h.'} for g, a in BAJO_1],
                          bars=7, clef='bass'),
                     dict(cap='b) cc. 8–15 · la misma mano, más arriba',
                          events=[{'pitches': [g, a], 'dur': 'h.'} for g, a in BAJO_2],
                          bars=8, clef='bass', show_time=False),
                 ]),
            dict(num=4, titulo='La derecha: las alturas de los cc. 3 y 6',
                 pista='las notas son las de la partitura; el ritmo, simplificado a corcheas para poder leerlas',
                 sistemas=[
                     dict(cap='a) en la partitura esto lleva puntillos y fusas · aquí solo las alturas, para saber dónde va la mano',
                          events=corch(['G4', 'A4', 'B4', 'B4']) + [n('G4')] +
                                 corch(['A4', 'G4', 'A4', 'A4']) + [n('G4')] +
                                 [n('F4', 'h.')],
                          bars=3),
                     dict(cap='b) y ahora solo la primera nota de cada compás, contando los tres tiempos en voz alta',
                          events=[n('G4', 'h.'), n('A4', 'h.'), n('F4', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL RESTO DE LA DERECHA, Y LOS FA SOSTENIDOS',
                 texto='La derecha no la cito entera: lleva fusas y tresillos que no he medido con la '
                       'seguridad que necesito. Se estudia compás a compás, contando los tres tiempos en voz '
                       'alta y colocando cada nota donde caiga, aunque haya que parar entre nota y nota. '
                       'Y antes de tocar, coge el lápiz: la armadura de Sol menor no lleva sostenidos, así '
                       'que cada Fa♯ está escrito a mano y es facilísimo comérselo. Rodéalos todos.'),
            dict(tipo='escalera', valores=[40, 44, 48, 52, 56, 60],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · El esqueleto de los cc. 1–15, de memoria y sin partitura.   '
                       '2 · El mismo bajo escrito, tres negras por compás.   '
                       '3 · La octava puesta, colocando la mano sin apretar.   '
                       '4 · La derecha, contando en voz alta.   '
                       '5 · La escalera de tempo.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
