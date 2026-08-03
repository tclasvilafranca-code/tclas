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
        intro='La partitura, abierta en trozos. El bajo está medido compás a compás en quince compases '
              'seguidos, así que se cita entero. La melodía no: lleva fusas y tresillos que el motor no '
              'escribe, y las alteraciones que le faltan al lector.',
        reglas=['EL BAJO ESTÁ MEDIDO', 'LA PRIMERA NEGRA PESA MÁS', 'ADAGIO, NO LENTO A MEDIAS'],
        bloques=[
            dict(num=1, titulo='El bajo de los cc. 1–7', clef='bass',
                 pista='cc. 1–7 medidos · Sol · Fa · Mi♭ · Re · Do · Re · Sol',
                 sistemas=[dict(cap='tres negras por compás · la primera con peso de brazo, las otras '
                                    'dos casi sin dedo',
                                events=[e for g, a in BAJO_1 for e in pie(g, a)],
                                bars=7, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='ESTO ES UN BAJO OBSTINADO',
                 texto='Fíjate en lo que hace la izquierda: baja por grados, Sol, Fa, Mi bemol, Re, y '
                       'después vuelve a subir. Esa línea de graves dando vueltas mientras encima cambia '
                       'la melodía se llama bajo obstinado, y es un recurso del Barroco. En esta pieza '
                       'es lo que reconoce todo el mundo: puedes tocar solo la izquierda delante de '
                       'cualquiera y va a saber qué es.'),
            dict(num=2, titulo='Y el bajo de los cc. 8–15', clef='bass',
                 pista='cc. 8–15 medidos · Sol · La · Si♭ · Si♭ · Do · La · Si♭ · La',
                 sistemas=[dict(cap='ahora sube, y por eso la música se abre: es la respuesta a la '
                                    'primera frase',
                                events=[e for g, a in BAJO_2 for e in pie(g, a)],
                                bars=8, clef='bass')]),
            dict(num=3, titulo='Solo la nota grave, sin la octava', clef='bass',
                 pista='quita la del medio y quédate con la línea desnuda · es el esqueleto de la pieza',
                 sistemas=[dict(cap='una nota por compás: Sol · Fa · Mi♭ · Re · Do · Re · Sol',
                                events=[n(g, 'h.') for g, _ in BAJO_1],
                                bars=7, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE EMPIEZA POR LA MANO IZQUIERDA',
                 texto='En casi todas las piezas del cuaderno la izquierda acompaña y la derecha canta. '
                       'Aquí no: aquí la izquierda ES la pieza. Ese bajo que baja se escribió primero y '
                       'la melodía se puso encima después. Si lo montas y te lo aprendes de memoria, vas '
                       'a poder leer la mano derecha sin tener que mirar nunca hacia abajo, que es la '
                       'única forma de sacar adelante una melodía tan llena de figuras cortas.'),
            dict(num=4, titulo='La octava sola, en el registro de la pieza', clef='bass',
                 pista='cc. 1–7 · las dos notas juntas, para colocar la mano antes de separarlas',
                 sistemas=[dict(cap='el 5 abajo y el 1 arriba, sin apretar · si la mano no llega, no '
                                    'estires: coloca el brazo entero',
                                events=[{'pitches': [g, a], 'dur': 'h.'} for g, a in BAJO_1],
                                bars=7, clef='bass')]),
        ],
    ),

    piano2=dict(
        intro='Montarla es entender que en esta pieza no hay nada rápido, y que todo lo que suena a '
              'difícil en la mano derecha es cuestión de contar despacio. La izquierda ya la tienes.',
        reglas=['LA IZQUIERDA, DE MEMORIA', 'LA DERECHA, CONTANDO', 'ADAGIO Y p'],
        bloques=[
            dict(num=4, titulo='El bajo entero, encadenado', clef='bass',
                 pista='cc. 1–15 · los dos tramos seguidos, que es una frase entera de la pieza',
                 sistemas=[dict(cap='sin parar entre el compás 7 y el 8: es la misma frase, no dos',
                                events=[n(g, 'h.') for g, _ in BAJO_1] +
                                       [n(g, 'h.') for g, _ in BAJO_2],
                                bars=8, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='QUÉ HACER CON LA MANO DERECHA',
                 texto='La derecha de esta pieza lleva puntillos, fusas y algún tresillo, y no la cito '
                       'aquí porque no la he medido con la seguridad que necesito. Lo que sí puedo '
                       'decirte es cómo se estudia: coge un compás, cuenta los tres tiempos en voz alta '
                       'muy despacio y coloca cada nota donde caiga, aunque tengas que parar entre nota '
                       'y nota. Cuando el compás esté colocado, únelo al siguiente. Nunca leas dos '
                       'compases seguidos sin haber colocado el primero.'),
            dict(tipo='nota',
                 etiqueta='LO QUE MÁS SE FALLA: LOS FA SOSTENIDOS',
                 texto='La armadura de Sol menor no lleva ningún sostenido, así que cada Fa♯ que veas '
                       'está escrito a mano. Son la sensible: la nota que hace que la música quiera '
                       'volver a Sol. Y como no están en la armadura, es facilísimo comérselos. Coge el '
                       'lápiz, recórrete la página entera y rodea todos los sostenidos ANTES de tocar '
                       'una sola nota.'),
            dict(tipo='nota',
                 etiqueta='CÓMO ESTUDIARLA ESTA SEMANA',
                 texto='1 · El bajo de los cc. 1 al 15, de memoria, sin partitura. '
                       '2 · El mismo bajo con la octava puesta, cuidando que la primera negra pese. '
                       '3 · Rodea con lápiz todas las alteraciones de la página. '
                       '4 · La derecha, compás a compás, contando en voz alta. '
                       '5 · Las dos manos de los cc. 1 al 7 y ahí paras.'),
            dict(num=5, titulo='La melodía de los cc. 3 y 6 · alturas medidas',
                 pista='cc. 3 y 6 · las notas son las de la partitura; el ritmo, simplificado',
                 sistemas=[dict(cap='en la partitura esto lleva puntillos y fusas · aquí en corcheas, '
                                    'solo para leer las alturas',
                                events=corch(['G4', 'A4', 'B4', 'B4']) + [n('G4')] +
                                       corch(['A4', 'G4', 'A4', 'A4']) + [n('G4')] +
                                       [n('F4', 'h.')],
                                bars=3)]),
            dict(tipo='escalera', valores=[40, 44, 48, 52, 56, 60],
                 regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='tracker', titulo='La prueba de la semana',
                 pie='Marca el día en que hayas tocado el bajo entero sin partitura.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
