# -*- coding: utf-8 -*-
"""Writing's on the Wall (Sam Smith) — Dilan, avanzado.
   Ver TRANSCRIPCION_D12_14.md.

   Re menor, armadura de un bemol: todos los Si son bemoles y NO se escriben.

   Lo medido: el dibujo de la izquierda es siempre el mismo — una corchea
   grave, otra corchea encima y una blanca con puntillo que se queda sonando.
   Las dos corcheas son cabezas llenas y se leen; la blanca con puntillo es
   hueca y no. De los pares medidos sale la armonia: Rem, Fa, Si♭ y Lam.

   Y la forma: los cc. 5 y 11 son identicos, los 6 y 13, los 8 y 14, los 22 y
   32, y los 23 y 34.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
REm_TON = 'Re menor'
_B = [2200]


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


def dibujo(baja, alta, larga):
    """El gesto de la izquierda: dos corcheas y una blanca con puntillo."""
    return [{'pitch': baja, 'dur': 'e', 'beam': _paso()},
            {'pitch': alta, 'dur': 'e', 'beam': _B[0]},
            {'pitch': larga, 'dur': 'h.'}]


def _paso():
    _B[0] += 1
    return _B[0]


# --- los pares medidos, con la nota larga puesta en la octava de arriba ----
REM = ('D2', 'A2', 'D3')
FA = ('F2', 'C3', 'F3')
SIb = ('B2', 'F3', 'B3')
LAM = ('A2', 'E3', 'A3')

CANCION = dict(
    alumno='Dilan', num=14, nivel='avanzado', slug='WritingsOnTheWall',
    titulo_corto="Writing's on the Wall", time_sig=(4, 4), key_sig=REm_TON,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           'WRITING_S ON THE WALL _ Sam Smith_.pdf'),
    yt='https://www.youtube.com/results?search_query=sam+smith+writings+on+the+wall',

    ficha=dict(
        titulo="Writing's on the Wall",
        autor='Sam Smith y Jimmy Napes (2015) · tema de "Spectre" · arr. musicaparadisfrutar.com',
        datos=[('Tonalidad', 'Re menor'), ('Compás', '4/4'), ('Tempo', '♩=68'),
               ('Compases', '38'), ('Mano izq.', 'Un solo dibujo')],
        total_compases=38,
        secciones=[
            ('A', 1, 10, 'La estrofa', AZUL),
            ("A'", 11, 20, 'La misma, con cambios', OCRE),
            ('B', 21, 38, 'El estribillo · sube una octava', AZUL),
        ],
        armonia=dict(
            titulo='El dibujo de la mano izquierda',
            tarjetas=[
                ('EL GESTO', 'Corchea · corchea · larga',
                 'Dos cortas abajo y una blanca con puntillo que se queda sonando. Siempre igual.'),
                ('RE MENOR Y FA', 'Re–La · Fa–Do',
                 'Los dos acordes que se alternan en casi toda la estrofa. Medidos.'),
                ('SI♭ Y LA MENOR', 'Si♭–Fa · La–Mi',
                 'Los que cierran cada frase. Medidos también.'),
                ('LA FORMA', 'Se repite mucho',
                 'Los cc. 5 y 11 son idénticos, los 6 y 13, los 8 y 14, los 22 y 32.'),
            ],
            pie='La izquierda hace exactamente lo mismo en los treinta y ocho compases: ataca una nota '
                'grave, sube a la de al lado y suelta una larga que se queda sonando. Lo único que '
                'cambia es sobre qué acorde: aprende el gesto una vez y el resto es mover la mano.',
        ),
        ritmos=[
            ('MI · Re menor', 'corchea, corchea y una larga que se queda',
             dibujo(*REM), OCRE, 'bass', REm_TON),
            ('MD', 'la melodía, que entra después del silencio',
             [sil(), n('D5', 'e'), n('C5', 'e'), n('A4', 'h')], AZUL, 'treble', REm_TON),
        ],
        especial=[
            'Armadura de un bemol: todos los Si son ♭. La tonalidad es Re menor.',
            'La izquierda hace SIEMPRE el mismo dibujo: dos corcheas y una nota larga.',
            'La melodía casi nunca empieza en el primer tiempo: entra después de un silencio.',
            'Hay SOSTENIDOS escritos a mano en la melodía: alteraciones que no están en la armadura.',
            'En el c. 24 aparece un 8va: la melodía se toca una octava más arriba de lo escrito.',
            'Los cc. 5 y 11 son idénticos, y los 6 y 13, y los 8 y 14, y los 22 y 32.',
        ],
        reto='Que la nota larga de la izquierda se oiga de verdad. Como llega después de dos corcheas, '
             'casi todo el mundo la toca más floja que ellas y la canción se queda sin suelo.',
        truco='Toca la izquierda exagerando: las dos corcheas casi sin sonido y la larga con peso de '
              'brazo. Sonará raro, pero después vuelves al equilibrio normal y ya no se te pierde.',
        sabias='Es el tema de "Spectre", la película de James Bond de 2015, y la primera de la saga '
               'cantada por un hombre que ganó el Oscar. Sam Smith y Jimmy Napes la escribieron en '
               'veinte minutos.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en la nota larga del piano: es lo que sostiene toda la canción.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta canción pide dos cosas: una nota larga '
              'que suene más que las cortas que la preceden, y entrar a tiempo después de un silencio. '
              'Aquí se entrenan las dos, en Re menor.',
        reglas=['ARMADURA DE RE MENOR: SI♭', 'LA NOTA LARGA PESA MÁS', 'CUENTA EL SILENCIO'],
        ejercicios=[
            dict(num=1, titulo='Escala de Re menor · dos octavas', clef='bass',
                 pista='manos separadas · un bemol, y el pulgar por debajo sin bache',
                 events=corch(['D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3']) +
                        corch(['E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'D4']) +
                        corch(['D4', 'C4', 'B3', 'A3', 'G3', 'F3', 'E3', 'D3']) +
                        corch(['C3', 'B2', 'A2', 'G2', 'F2', 'E2', 'D2', 'D2']),
                 bars_per_line=4),
            dict(num=2, titulo='El dibujo, por toda la tonalidad', clef='bass',
                 pista='dos cortas y una larga, sobre los seis grados de Re menor',
                 events=(dibujo('D2', 'A2', 'D3') + dibujo('E2', 'B2', 'E3') +
                         dibujo('F2', 'C3', 'F3') + dibujo('G2', 'D3', 'G3') +
                         dibujo('A2', 'E3', 'A3') + dibujo('D2', 'A2', 'D3')),
                 bars_per_line=3),
            dict(num=3, titulo='El dibujo al revés', clef='bass',
                 pista='ahora la larga va abajo y las cortas arriba · lo que la pieza nunca te hace hacer',
                 events=(dibujo('D3', 'A2', 'D2') + dibujo('C3', 'G2', 'C2') +
                         dibujo('B2', 'F2', 'B1') + dibujo('D3', 'A2', 'D2')),
                 bars_per_line=4),
            dict(num=4, titulo='Entrar después del silencio',
                 pista='la melodía casi nunca empieza en el uno · cuenta el silencio en voz alta',
                 events=[sil('h'), n('D5'), n('C5'),
                         sil('h'), n('A4'), n('G4'),
                         sil(), n('D5'), n('C5'), n('A4'),
                         n('G4', 'w')],
                 bars_per_line=4),
            dict(num=5, titulo='Arpegio de Re menor · dos octavas', clef='bass',
                 pista='fundamental · 3ª · 5ª · 8ª · el acorde de la tonalidad, abierto',
                 events=corch(['D2', 'F2', 'A2', 'D3', 'F3', 'A3', 'D4', 'D4']) +
                        corch(['D4', 'A3', 'F3', 'D3', 'A2', 'F2', 'D2', 'D2']),
                 bars_per_line=4),
            dict(num=6, titulo='Y las mismas notas, en octava alta',
                 pista='el 8va del c. 24 · la mano hace lo mismo, pero ocho notas más arriba',
                 events=corch(['D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6']) +
                        corch(['D6', 'C6', 'B5', 'A5', 'G5', 'F5', 'E5', 'D5']),
                 bars_per_line=4),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con un bemol. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · armadura de Re menor: todos los Si son ♭',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DE LA MANO IZQUIERDA (CLAVE DE FA)',
        chuleta_pitches=['D2', 'F2', 'A2', 'D3', 'F3', 'A3'],
        chuleta_nombres=['Re', 'Fa', 'La', 'Re', 'Fa', 'La'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa', clef='bass',
                 pista='donde vive la izquierda · el orden está desordenado a propósito',
                 events=[n(p) for p in ('D2', 'A2', 'F2', 'C3', 'B2', 'F3', 'A2', 'E3',
                                        'G2', 'D3', 'C3', 'A3', 'E2', 'B3', 'F3', 'D2')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · registro medio-alto, con líneas adicionales',
                 events=[n(p) for p in ('D5', 'A4', 'F5', 'C5', 'G4', 'E5', 'B4', 'D4',
                                        'A5', 'F4', 'C6', 'E4', 'G5', 'B5', 'A4', 'D5')]),
            dict(num=3, titulo='Leer el gesto entero', clef='bass',
                 pista='dos cortas y una larga · nombra las tres antes de pasar al compás siguiente',
                 events=(dibujo('E2', 'B2', 'E3') + dibujo('G2', 'D3', 'G3') +
                         dibujo('C3', 'G3', 'C4') + dibujo('E2', 'B2', 'E3')),
                 bars_per_line=4),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca dos notas cortas y una larga. Unas veces haz que suene más la larga y otras '
                      'que suenen más las cortas. Que diga cuál pesaba más.'),
                ('B', 'Toca una tríada suelta: MAYOR o MENOR. Esta canción es menor y se nota.'),
                ('C', 'Marca cuatro tiempos y entra con una nota en el 1, en el 2 o en el 3. Que diga en '
                      'cuál entraste.'),
                ('+', 'Y sin escribir: toca el gesto de la izquierda y que dé palmas solo en la larga.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Qué pesa más?', pista='las dos cortas, o la larga',
                     n=10, opciones=['cortas', 'larga']),
                dict(letra='B', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=8, opciones=['M', 'm']),
                dict(letra='C', titulo='¿En qué tiempo entra?', pista='cuenta los cuatro por dentro',
                     n=6, opciones=['1', '2', '3']),
            ],
        ),
    ),

    piano1=dict(
        intro='La partitura, abierta en trozos. Lo que se cita está medido: los pares de corcheas de la '
              'izquierda dan la armonía, y la forma se ha comparado compás a compás. La nota larga de '
              'la izquierda va en cabeza hueca y no se lee: la que ves aquí es la octava del par.',
        reglas=['ARMADURA DE RE MENOR', 'LA LARGA PESA MÁS QUE LAS CORTAS', 'CUENTA LOS SILENCIOS'],
        bloques=[
            dict(num=1, titulo='La izquierda de los cc. 1–4', clef='bass',
                 pista='cc. 1–4 medidos · Rem · Fa · Rem · Fa · el gesto no cambia nunca',
                 sistemas=[dict(cap='ataca las dos corcheas casi sin sonido y deja caer el brazo en la '
                                    'larga',
                                events=dibujo(*REM) + dibujo(*FA) + dibujo(*REM) + dibujo(*FA),
                                bars=4, clef='bass')]),
            dict(num=2, titulo='Y los cc. 5–10, que cierran la estrofa', clef='bass',
                 pista='cc. 5–10 medidos · Rem · Rem · Fa · Si♭ · Lam · Lam',
                 sistemas=[dict(cap='el Si♭ es el que avisa de que la frase se acaba: dale un poco más',
                                events=dibujo(*REM) + dibujo(*REM) + dibujo(*FA) +
                                       dibujo(*SIb) + dibujo(*LAM) + dibujo(*LAM),
                                bars=6, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='LA NOTA QUE SE QUEDA SONANDO',
                 texto='De las tres notas de cada compás, la que importa es la última: la blanca con '
                       'puntillo, que dura tres tiempos y sostiene toda la armonía mientras la voz canta '
                       'encima. Las dos corcheas de antes son solo el impulso para llegar a ella. El '
                       'error de casi todo el mundo es tocarlas con el mismo peso, y entonces la canción '
                       'suena a acompañamiento de vals en vez de a lo que es.'),
            dict(num=3, titulo='La melodía de los cc. 1–3',
                 pista='cc. 1–3 · alturas medidas · el ritmo va simplificado y sin las alteraciones',
                 sistemas=[dict(cap='entra después del silencio · cuenta el primer tiempo entero antes de '
                                    'tocar',
                                events=[sil(), n('E5'), n('D5'), n('A4'),
                                        n('G4', 'w'),
                                        sil(), n('E5'), n('D5'), n('C5'),
                                        n('D5', 'h'), n('A4'), n('G4')],
                                bars=4)]),
            dict(tipo='nota',
                 etiqueta='LA MELODÍA NUNCA EMPIEZA EN EL UNO',
                 texto='Mira los primeros compases: la derecha siempre entra después de un silencio de '
                       'corchea o de negra. No es un capricho del arreglista, es cómo canta Sam Smith: '
                       'la voz llega un poco tarde a propósito, y ese retraso es la mitad del carácter '
                       'de la canción. Cuenta el silencio en voz alta antes de cada entrada; si entras '
                       'en el uno, la frase pierde toda la gracia.'),
            dict(num=4, titulo='La frase que más se repite',
                 pista='cc. 8 y 14 medidos · Si repetido y La repetido, idénticos en los dos sitios',
                 sistemas=[dict(cap='cuatro Si y tres La · es la frase que vuelve, y aparece dos veces '
                                    'exactamente igual',
                                events=corch(['B4', 'B4', 'B4', 'B4', 'A4', 'A4', 'A4', 'A4']) +
                                       [n('G4', 'w')],
                                bars=2)]),
        ],
    ),

    piano2=dict(
        intro='Montarla es darse cuenta de que hay muchos compases repetidos y de que la izquierda no '
              'cambia de gesto ni una vez. Lo que sí cambia, y hay que preparar, es el 8va del c. 24.',
        reglas=['LOS CC. 11–14 SON LOS CC. 5–8', 'OJO AL 8VA DEL C. 24', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(tipo='nota',
                 etiqueta='LO QUE YA TE SABES SIN SABERLO',
                 texto='Comparados compás a compás: el c. 11 es el c. 5, el c. 13 es el c. 6, el c. 14 '
                       'es el c. 8, el c. 32 es el c. 22 y el c. 34 es el c. 23. Cinco parejas. Coge el '
                       'lápiz y escríbelo en tu partitura antes de estudiar nada: cuando llegues a esos '
                       'compases no tendrás que leerlos, y eso son casi tres semanas de trabajo menos.'),
            dict(tipo='nota',
                 etiqueta='QUÉ ES EL 8VA DEL C. 24',
                 texto='A partir de ahí verás escrito "8va" con una línea de puntos encima del '
                       'pentagrama. Significa que todo lo que hay debajo de esa línea se toca una octava '
                       'MÁS ARRIBA de donde está escrito. No es un adorno: es que el editor no quería '
                       'llenar la página de líneas adicionales. Cuando la línea de puntos se acaba, '
                       'vuelves a tocar donde pone.'),
            dict(num=5, titulo='El estribillo, con la izquierda quieta', clef='bass',
                 pista='cc. 21–24 · la izquierda se para y deja que la derecha suba sola',
                 sistemas=[dict(cap='aquí la izquierda solo pone el acorde y se calla: no la rellenes',
                                events=[ac(('D3', 'F3', 'A3'), 'w'), ac(('A2', 'E3', 'A3'), 'w'),
                                        ac(('B2', 'F3', 'B3'), 'w'), ac(('F2', 'C3', 'F3'), 'w')],
                                bars=4, clef='bass')]),
            dict(num=6, titulo='Y la derecha, una octava arriba',
                 pista='c. 24 en adelante · las mismas notas de antes, pero con el 8va puesto',
                 sistemas=[dict(cap='no cambies nada del gesto: es la misma frase, solo que más arriba',
                                events=[n('D6'), n('E6'), n('F6'), n('C6'),
                                        n('D6', 'h'), n('C6', 'h'),
                                        n('A5'), n('B5'), n('B5'), n('A5'),
                                        n('D6', 'w')],
                                bars=4)]),
            dict(tipo='nota',
                 etiqueta='CÓMO ESTUDIARLA ESTA SEMANA',
                 texto='1 · Marca en la partitura las cinco parejas de compases repetidos. '
                       '2 · La izquierda sola de los cc. 1 al 10, exagerando la nota larga. '
                       '3 · La derecha sola, contando el silencio de cada entrada en voz alta. '
                       '4 · Las dos manos de los cc. 1 al 10. '
                       '5 · Y el 8va aparte, leyéndolo en voz alta antes de tocarlo.'),
            dict(tipo='escalera', valores=[44, 50, 56, 60, 64, 68],
                 regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='tracker', titulo='La prueba de la semana',
                 pie='Marca el día en que la nota larga de la izquierda se haya oído siempre más que las cortas.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
