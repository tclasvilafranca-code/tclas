# -*- coding: utf-8 -*-
"""A Sky Full of Stars (Coldplay) — Dilan, avanzado. Ver TRANSCRIPCION_D12_14.md.

   Fa mayor, un bemol: todos los Si son bemoles y NO se escriben.

   Lo medido: el riff de la izquierda son QUINTAS (Si♭2-Fa3 y Fa2-Do3) que se
   alternan compas a compas, y la forma es un bucle de cuatro compases (los
   cc. 5, 9 y 17 son identicos; los 7 y 11 tambien; los 12 y 20 tambien).

   Lo que NO se escribe: el ritmo. El riff va en corchea con puntillo mas
   semicorchea y el motor no sabe escribir esas figuras, asi que aqui va en
   corcheas iguales y se dice en cada bloque que lo cita.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'
_B = [2000]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='h'):
    return {'pitches': list(ps), 'dur': d}


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


def riff(baja, alta, veces=1):
    """El riff de la izquierda: la quinta, picoteada. Ritmo simplificado."""
    return corch([baja, alta] * (4 * veces), agrupar=4)


# --- las quintas medidas ---------------------------------------------------
SIb = ('B2', 'F3')          # Si bemol por armadura
FAq = ('F2', 'C3')
LAm7 = ('A2', 'E3', 'G3')   # el acorde de la introduccion
SOL = ('G2', 'D3', 'A3')

CANCION = dict(
    alumno='Dilan', num=12, nivel='avanzado', slug='SkyFullOfStars',
    titulo_corto='A Sky Full of Stars', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' a-sky-full-of-stars-coldplay.pdf'),
    yt='https://www.youtube.com/results?search_query=coldplay+a+sky+full+of+stars',

    ficha=dict(
        titulo='A Sky Full of Stars',
        autor='Coldplay y Avicii (2014) · arr. Piano Seeds Studio',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', '4/4'), ('Compases', '23'),
               ('Mano izq.', 'Riff'), ('Extras', 'Digitación')],
        total_compases=23,
        secciones=[
            ('intro', 1, 4, 'Las dos manos tocan lo mismo', OCRE),
            ('A', 5, 16, 'Entra la melodía · bucle de 4 compases', AZUL),
            ("A'", 17, 23, 'Lo mismo, y cierra', OCRE),
        ],
        armonia=dict(
            titulo='El riff de la mano izquierda',
            tarjetas=[
                ('QUINTA DE SI♭', 'Si♭2 · Fa3',
                 'Dos notas, picoteadas sin parar. Son los compases impares del bucle.'),
                ('QUINTA DE FA', 'Fa2 · Do3',
                 'La misma forma de la mano, movida. Son los compases pares.'),
                ('LA INTRO', 'La m7 y Sol',
                 'Los cc. 3 y 4 llevan tres notas: La·Mi·Sol y Sol·Re·La.'),
                ('EL BUCLE', 'Cuatro compases',
                 'Los cc. 5, 9 y 17 son idénticos. Y los cc. 7 y 11. Medido.'),
            ],
            pie='Este riff lo tocaba un sintetizador en el disco, no un piano, y por eso no se detiene '
                'nunca: es una máquina. Al piano el reto es exactamente ese, aguantar el motor sin que '
                'se note el cansancio. Fíjate en que casi todo son quintas, sin tercera: por eso suena '
                'tan abierto y tan grande.',
        ),
        ritmos=[
            ('MI', 'la quinta picoteada · el ritmo real lleva puntillo',
             corch(['B2', 'F3', 'B2', 'F3']) + [n('B2'), n('F3')], OCRE, 'bass', FA),
            ('MD', 'la melodía, en notas largas por encima del riff',
             [n('C5', 'h'), n('A4'), n('B4')], AZUL, 'treble', FA),
        ],
        especial=[
            'Armadura de un bemol: todos los Si son ♭. La tonalidad es Fa mayor.',
            'La edición trae la DIGITACIÓN impresa en las dos manos: úsala, está pensada.',
            'Los cc. 1–4 son introducción y las DOS manos tocan lo mismo, en octavas.',
            'Hay barra de repetición al final de la introducción y otra al empezar la estrofa.',
            'El riff son quintas: dos notas sin tercera, y por eso suena tan abierto.',
            'La derecha, cuando entra, va en notas larguísimas: redondas y blancas ligadas.',
        ],
        reto='Aguantar. El riff de la izquierda no para en veintitrés compases y tiene que sonar igual '
             'de parejo al final que al principio. No es difícil de leer ni de colocar: es difícil de '
             'sostener sin que el brazo se ponga duro.',
        truco='Toca el riff dieciséis compases seguidos mirando el reloj y comprueba que puedes hablar '
              'en voz alta mientras. Si no puedes hablar, es que estás apretando.',
        sabias='La escribieron Coldplay con Avicii, que era DJ y no tocaba el piano: le mandaron la '
               'canción por internet y él les devolvió el riff que hoy es lo primero que suena. Es de '
               'las pocas canciones de Coldplay donde el piano no lo toca Chris Martin.',
        qr=dict(titulo='Escucha la original',
                texto='Ese riff que no para es lo que tú vas a tocar con la izquierda.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta canción pide una sola cosa: que la mano '
              'izquierda repita una quinta sin cansarse ni acelerar. Aquí se entrena eso por toda la '
              'tonalidad de Fa mayor, no solo sobre los dos acordes que la pieza usa.',
        reglas=['ARMADURA DE FA: TODOS LOS SI SON ♭', 'EL BRAZO, SUELTO', 'NADA DE ACELERAR'],
        ejercicios=[
            dict(num=1, titulo='Escala de Fa mayor · dos octavas', clef='bass',
                 pista='manos separadas · un bemol, y el pulgar por debajo sin bache',
                 events=corch(['F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3']) +
                        corch(['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'F4']) +
                        corch(['F4', 'E4', 'D4', 'C4', 'B3', 'A3', 'G3', 'F3']) +
                        corch(['E3', 'D3', 'C3', 'B2', 'A2', 'G2', 'F2', 'F2']),
                 bars_per_line=4),
            dict(num=2, titulo='Quintas por toda la escala', clef='bass',
                 pista='las dos teclas a la vez · las mismas que la canción, pero por todos los grados',
                 events=[ac(('F2', 'C3'), 'h'), ac(('G2', 'D3'), 'h'),
                         ac(('A2', 'E3'), 'h'), ac(('B2', 'F3'), 'h'),
                         ac(('C3', 'G3'), 'h'), ac(('D3', 'A3'), 'h'),
                         ac(('E3', 'B3'), 'h'), ac(('F3', 'C4'), 'h'),
                         ac(('F2', 'C3'), 'w')],
                 bars_per_line=5),
            dict(num=3, titulo='Y ahora picoteadas, no juntas', clef='bass',
                 pista='el gesto real de la canción · primero la de abajo, luego la de arriba, sin parar',
                 events=riff('C3', 'G3') + riff('D3', 'A3') + riff('E3', 'B3') + riff('C3', 'G3'),
                 bars_per_line=4),
            dict(num=4, titulo='El mismo picoteo, bajando', clef='bass',
                 pista='ahora primero la de arriba · es lo que la canción nunca te hace practicar',
                 events=riff('G3', 'C3') + riff('A3', 'D3') + riff('B3', 'E3') + riff('G3', 'C3'),
                 bars_per_line=4),
            dict(num=5, titulo='Arpegio de Fa mayor · dos octavas', clef='bass',
                 pista='fundamental · 3ª · 5ª · 8ª · la quinta de la canción, con la tercera puesta',
                 events=corch(['F2', 'A2', 'C3', 'F3', 'A3', 'C4', 'F4', 'F4']) +
                        corch(['F4', 'C4', 'A3', 'F3', 'C3', 'A2', 'F2', 'F2']),
                 bars_per_line=4),
            dict(num=6, titulo='Notas largas encima de nada',
                 pista='lo que hace la derecha · una nota, y aguantarla contando los cuatro tiempos',
                 events=[n('C5', 'w'), n('A4', 'w'), n('B4', 'w'), n('G4', 'w'),
                         n('A4', 'w'), n('F4', 'w'), n('G4', 'w'), n('F4', 'w')],
                 bars_per_line=8),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con un bemol. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · armadura de Fa: todos los Si son ♭',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DEL RIFF (CLAVE DE FA)',
        chuleta_pitches=['F2', 'A2', 'C3', 'F3', 'A3', 'C4'],
        chuleta_nombres=['Fa', 'La', 'Do', 'Fa', 'La', 'Do'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa', clef='bass',
                 pista='donde vive el riff · el orden está desordenado a propósito',
                 events=[n(p) for p in ('F2', 'C3', 'B2', 'F3', 'A2', 'E3', 'G2', 'D3',
                                        'C4', 'A3', 'F3', 'B3', 'E2', 'G3', 'D2', 'F2')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde canta la melodía · registro medio-alto',
                 events=[n(p) for p in ('C5', 'A4', 'F5', 'B4', 'G4', 'E5', 'D5', 'F4',
                                        'A5', 'C4', 'B5', 'E4', 'G5', 'D4', 'A4', 'C5')]),
            dict(num=3, titulo='Leer quintas', clef='bass',
                 pista='dos notas de golpe · nómbralas de abajo arriba antes de pasar a la siguiente',
                 events=[ac(('B2', 'F3'), 'q'), ac(('F2', 'C3'), 'q'),
                         ac(('C3', 'G3'), 'q'), ac(('A2', 'E3'), 'q'),
                         ac(('G2', 'D3'), 'q'), ac(('D3', 'A3'), 'q'),
                         ac(('E3', 'B3'), 'q'), ac(('F2', 'C3'), 'q')],
                 bars_per_line=4),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca dos notas: unas veces una QUINTA y otras una tríada entera. Que diga si '
                      'sonaban DOS o TRES.'),
                ('B', 'Toca la quinta picoteada empezando unas veces por la de abajo y otras por la de '
                      'arriba. Que diga por cuál empezaste.'),
                ('C', 'Toca una tríada suelta: MAYOR o MENOR.'),
                ('+', 'Y sin escribir: toca el riff y que dé palmas exactamente encima, sin adelantarse.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Dos notas o tres?', pista='la quinta es hueca; la tríada, llena',
                     n=10, opciones=['2', '3']),
                dict(letra='B', titulo='¿Empieza abajo o arriba?', pista='la primera nota del picoteo',
                     n=8, opciones=['abajo', 'arriba']),
                dict(letra='C', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=6, opciones=['M', 'm']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Aquí hay cuatro compases de música y el resto es repetirlos sin que se note. La '
              'dificultad no está en las notas, está en el aguante. Por eso el paso 1 es el riff y el '
              'paso 2 es aprenderse el ORDEN antes que el gesto. Lo único que no se escribe es el '
              'puntillo del riff: en la partitura va con puntillo, aquí en corcheas iguales.',
        reglas=['ARMADURA DE FA', 'EL RITMO REAL LLEVA PUNTILLO', 'EL BRAZO SUELTO'],
        bloques=[
            dict(num=1, titulo='El riff, y lo que hay debajo', clef='bass',
                 pista='cc. 5–8 medidos · los impares en Si♭ y los pares en Fa · el ritmo, simplificado',
                 sistemas=[
                     dict(cap='a) el riff sobre Si♭ solo, dos compases · sin acentuar ninguna nota, '
                              'el brazo quieto',
                          events=riff(*SIb) + riff(*SIb), bars=2, clef='bass'),
                     dict(cap='b) y sobre Fa, que es la otra mitad de la canción',
                          events=riff(*FAq) + riff(*FAq), bars=2, clef='bass', show_time=False),
                     dict(cap='c) los cuatro compases seguidos, alternando · aquí es donde se nota si '
                              'llegas colocado al cambio',
                          events=riff(*SIb) + riff(*FAq) + riff(*SIb) + riff(*FAq),
                          bars=4, clef='bass', show_time=False),
                     dict(cap='d) quita el picoteo y quédate con la nota de abajo · Si♭ · Fa · Si♭ · Fa: '
                              'eso es la canción entera',
                          events=[n('B2', 'w'), n('F2', 'w')] * 4,
                          bars=8, clef='bass', show_time=False),
                     dict(cap='e) y las mismas quintas en blancas · di en voz alta “Si bemol, Fa” '
                              'mientras las tocas, hasta sabértelo de memoria',
                          events=[ac(SIb, 'h'), ac(SIb, 'h'), ac(FAq, 'h'), ac(FAq, 'h'),
                                  ac(SIb, 'h'), ac(SIb, 'h'), ac(FAq, 'h'), ac(FAq, 'h'),
                                  ac(SIb, 'w')],
                          bars=5, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ AQUÍ EL RITMO NO ESTÁ ESCRITO',
                 texto='En tu partitura la primera nota de cada pareja dura un poco más que la segunda: '
                       'es una corchea con puntillo seguida de una semicorchea, y eso es lo que le da el '
                       'balanceo. Aquí no lo puedo escribir, así que las verás iguales. Léelas de aquí y '
                       'mira el ritmo en la página 1: si tocas las dos iguales, el riff se queda plano.'),
            dict(num=2, titulo='La introducción, que sí lleva tres notas', clef='bass',
                 pista='cc. 3–4 medidos · La·Mi·Sol y Sol·Re·La · en la intro las dos manos tocan lo mismo',
                 sistemas=[
                     dict(cap='a) tócalo primero con una sola mano y después júntalas',
                          events=[ac(LAm7, 'h'), ac(LAm7, 'h'), ac(SOL, 'h'), ac(SOL, 'h'),
                                  ac(LAm7, 'w')],
                          bars=3, clef='bass'),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='La melodía de esta canción son cuatro notas larguísimas: lo difícil es contarlas, no '
              'tocarlas. Y después queda la prueba de verdad, que es aguantar el riff sin que el brazo '
              'se ponga duro.',
        reglas=['CUATRO COMPASES SON LA CANCIÓN', 'IGUAL DE FLOJO AL FINAL QUE AL PRINCIPIO', 'SIN ACELERAR'],
        bloques=[
            dict(num=3, titulo='La melodía, que son cuatro notas',
                 pista='cc. 5–8 y 13–16 medidos · cuenta los cuatro tiempos de cada nota en voz alta',
                 sistemas=[
                     dict(cap='a) cc. 5–8 · aguántalas enteras, no las sueltes antes de tiempo',
                          events=[n('C5', 'w'), n('A4', 'h'), n('B4', 'h'),
                                  n('A4', 'w'), n('G4', 'w')],
                          bars=4),
                     dict(cap='b) cc. 13–16 · las mismas notas largas, una octava arriba: no cambies '
                              'de gesto, solo de sitio',
                          events=[n('F5', 'h'), n('C5'), n('D5'),
                                  n('C5', 'h'), n('F5', 'h'),
                                  n('F5', 'h'), n('G5'), n('E5'),
                                  n('F5', 'h'), n('A5', 'h')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='HAY CUATRO COMPASES, NO VEINTITRÉS',
                 texto='Comparando compás a compás salen tres parejas idénticas: los cc. 5, 9 y 17 son el '
                       'mismo compás; los cc. 7 y 11 también; y los cc. 12 y 20 también. La canción está '
                       'construida sobre un bucle de cuatro compases. Antes de estudiar, marca en tu '
                       'partitura dónde vuelve a empezar el bucle: de veintitrés compases solo hay que '
                       'aprender cuatro.'),
            dict(num=4, titulo='Ocho compases de aguante', clef='bass',
                 pista='la prueba de verdad · si el brazo se pone duro, para y empieza otra vez',
                 sistemas=[
                     dict(cap='a) que el compás ocho suene exactamente igual de flojo que el primero',
                          events=[ac(SIb, 'q'), ac(SIb, 'q'), ac(SIb, 'q'), ac(SIb, 'q'),
                                  ac(FAq, 'q'), ac(FAq, 'q'), ac(FAq, 'q'), ac(FAq, 'q'),
                                  ac(SIb, 'q'), ac(SIb, 'q'), ac(SIb, 'q'), ac(SIb, 'q'),
                                  ac(FAq, 'w')],
                          bars=4, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA DIGITACIÓN VIENE PUESTA',
                 texto='Esta edición trae los números de los dedos escritos encima y debajo de los '
                       'pentagramas: 3-1, 4-1, 5-1, 1-5… No los ignores. En una canción que repite el '
                       'mismo gesto doscientas veces, usar siempre los mismos dedos es la diferencia '
                       'entre que salga solo a la tercera semana o no salir nunca. Y si un día decides '
                       'cambiar una digitación, escríbela con lápiz y no vuelvas a cambiarla.'),
            dict(tipo='escalera', valores=[60, 72, 84, 96, 108, 118],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · El riff, y la nota de abajo que lo sostiene.   '
                       '2 · La introducción, con una mano y luego con las dos.   '
                       '3 · La melodía, contando cada nota larga en voz alta.   '
                       '4 · Ocho compases de aguante, sin endurecer el brazo.   '
                       '5 · La escalera, y del c. 5 al 12 seguido: el bucle dos veces.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
