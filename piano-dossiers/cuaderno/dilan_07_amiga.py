# -*- coding: utf-8 -*-
"""Amiga Mia (Alejandro Sanz) — Dilan, avanzado. Ver TRANSCRIPCION_D06_08.md.

   ATENCION: de esta pieza NO se cita ninguna altura. La izquierda va en
   redondas (cabezas huecas, que el lector no distingue) y la derecha es muy
   densa, asi que no hay medicion fiable. Lo que si se ve sin ambiguedad, y es
   lo que trabaja el cuaderno, es la TEXTURA: la derecha lleva dos voces a la
   vez y la izquierda solo sostiene. Todo lo escrito aqui es ANDAMIO, con los
   grados de Re mayor, y esta rotulado como tal: para las notas, la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import sistemas_extra, bloque_tresillos, bloques_extra

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
RE = 'Re mayor'
_B = [1100]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


CANCION = dict(
    alumno='Dilan', num=7, nivel='avanzado', slug='AmigaMia',
    titulo_corto='Amiga Mía', time_sig=(4, 4), key_sig=RE,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           'Amiga mia-alejandro Sanz.pdf'),
    yt='https://www.youtube.com/results?search_query=alejandro+sanz+amiga+mia',

    ficha=dict(
        titulo='Amiga Mía', autor='Alejandro Sanz (2000) · edición con letra',
        datos=[('Tonalidad', 'Re mayor'), ('Compás', '4/4'), ('Tempo', 'Lento'),
               ('Mano izq.', 'Redondas'), ('Mano dcha.', 'Dos voces')],
        armonia=dict(
            titulo='Dónde está la dificultad',
            tarjetas=[
                ('LA IZQUIERDA', 'Una nota',
                 'Redondas: una sola nota por compás, sostenida los cuatro tiempos. Nada más.'),
                ('LA DERECHA', 'Dos a la vez',
                 'Sostiene un acorde abajo mientras los dedos de arriba mueven la melodía.'),
                ('POR ESO CUESTA', 'Dos a la vez',
                 'El 1 y el 2 se quedan quietos apretando; el 4 y el 5 tienen que correr.'),
                ('EL TRESILLO', 'Tres en dos',
                 'Marcado con un 3. Aparece varias veces y descoloca si no lo cuentas.'),
            ],
            pie='Casi todas las canciones reparten el trabajo entre las dos manos: una acompaña y otra '
                'canta. Aquí no. La izquierda casi no hace nada y la derecha hace las dos cosas a la vez. '
                'Ese es el problema entero de la pieza, y es un problema de independencia DENTRO de una '
                'sola mano.',
        ),
        ritmos=[
            ('MI', 'una redonda por compás: se ataca y se deja',
             [n('D3', 'w')], OCRE, 'bass', RE),
            ('MD · abajo', 'el acorde que se queda quieto los cuatro tiempos (andamio)',
             [{'pitches': ['D4', 'F4', 'A4'], 'dur': 'w'}], OCRE, 'treble', RE),
            ('MD · arriba', 'y a la vez, con la misma mano, esto (andamio, no la pieza)',
             corch(['D5', 'E5', 'F5', 'E5', 'D5', 'E5', 'F5', 'A5']), AZUL, 'treble', RE),
        ],
        especial=[
            'Armadura de dos sostenidos: todos los Fa y los Do son ♯.',
            'La izquierda toca UNA nota por compás, en redonda. Es lo más fácil de la partitura.',
            'La derecha lleva dos voces: un acorde que se mantiene y la melodía por encima.',
            'Las dos voces de la derecha están escritas con las plicas al revés: las de abajo hacia '
            'abajo y las de arriba hacia arriba. Sirve para verlas separadas.',
            'Viene con LETRA debajo: cántala y el fraseo se coloca solo.',
            'Hay TRESILLOS marcados con un 3.',
            'Pone Lento: no hay ninguna prisa, y la partitura lo dice.',
        ],
        reto='Sostener con el pulgar y el índice mientras el anular y el meñique se mueven, todo con la '
             'misma mano. No es fuerza: es que unos dedos aprendan a quedarse quietos mientras los otros '
             'trabajan.',
        truco='Estudia las dos voces por separado con la MISMA mano: primero solo las notas de abajo, '
              'sosteniéndolas cuatro tiempos; luego solo las de arriba. Cuando las juntes, piensa solo en '
              'las de abajo: las de arriba ya se saben solas.',
        sabias='Alejandro Sanz la escribió pensando en una amiga real que se había enamorado de alguien '
               'que no la quería. La grabó en "El Alma al Aire", en 2000, un disco que compuso en apenas '
               'unas semanas y que acabó siendo el más vendido de su carrera en España.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en que el piano casi no se mueve: todo lo hace la voz.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta canción pide una cosa muy concreta: que '
              'unos dedos de la mano derecha aguanten quietos mientras los otros se mueven. Aquí se '
              'entrena eso con notas fáciles, en Re mayor.',
        reglas=['ARMADURA DE RE: FA♯ Y DO♯', 'LOS DEDOS 1 Y 2 NO SE LEVANTAN', 'LENTO DE VERDAD'],
        ejercicios=[
            dict(num=1, titulo='Escala de Re mayor · dos octavas',
                 pista='manos separadas · dos sostenidos, y el pulgar por debajo sin bache',
                 events=corch(['D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5']) +
                        corch(['E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'D6']) +
                        corch(['D6', 'C6', 'B5', 'A5', 'G5', 'F5', 'E5', 'D5']) +
                        corch(['C5', 'B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'D4']),
                 bars_per_line=4),
            dict(num=2, titulo='Abajo quieto, arriba andando',
                 pista='el gesto de la canción · el dedo 1 aguanta el Re mientras los de arriba se mueven',
                 events=[{'pitches': ['D4', 'F4'], 'dur': 'q'}, {'pitches': ['D4', 'G4'], 'dur': 'q'},
                         {'pitches': ['D4', 'A4'], 'dur': 'q'}, {'pitches': ['D4', 'G4'], 'dur': 'q'},
                         {'pitches': ['D4', 'F4'], 'dur': 'q'}, {'pitches': ['D4', 'A4'], 'dur': 'q'},
                         {'pitches': ['D4', 'B4'], 'dur': 'q'}, {'pitches': ['D4', 'A4'], 'dur': 'q'},
                         {'pitches': ['D4', 'F4'], 'dur': 'w'}],
                 bars_per_line=3),
            dict(num=3, titulo='Ahora al revés',
                 pista='ahora el que aguanta es el dedo 5 y los que andan son los de abajo',
                 events=[{'pitches': ['D4', 'D5'], 'dur': 'q'}, {'pitches': ['E4', 'D5'], 'dur': 'q'},
                         {'pitches': ['F4', 'D5'], 'dur': 'q'}, {'pitches': ['E4', 'D5'], 'dur': 'q'},
                         {'pitches': ['G4', 'D5'], 'dur': 'q'}, {'pitches': ['F4', 'D5'], 'dur': 'q'},
                         {'pitches': ['E4', 'D5'], 'dur': 'q'}, {'pitches': ['D4', 'D5'], 'dur': 'q'},
                         {'pitches': ['D4', 'D5'], 'dur': 'w'}],
                 bars_per_line=3),
            dict(num=4, titulo='Y ahora lo mismo con la izquierda', clef='bass',
                 pista='el 5 aguanta abajo y el 1 se mueve arriba · cuesta más que con la derecha',
                 events=[{'pitches': ['D3', 'A3'], 'dur': 'q'}, {'pitches': ['D3', 'B3'], 'dur': 'q'},
                         {'pitches': ['D3', 'C4'], 'dur': 'q'}, {'pitches': ['D3', 'B3'], 'dur': 'q'},
                         {'pitches': ['D3', 'A3'], 'dur': 'q'}, {'pitches': ['D3', 'C4'], 'dur': 'q'},
                         {'pitches': ['D3', 'D4'], 'dur': 'q'}, {'pitches': ['D3', 'C4'], 'dur': 'q'},
                         {'pitches': ['D3', 'A3'], 'dur': 'w'}],
                 bars_per_line=3),
            dict(num=5, titulo='Terceras rotas de Re mayor',
                 pista='dos notas saltando una · para que la mano deje de ir siempre de vecina en vecina',
                 events=corch(['D4', 'F4', 'E4', 'G4', 'F4', 'A4', 'G4', 'B4']) +
                        corch(['A4', 'C5', 'B4', 'D5', 'C5', 'E5', 'D5', 'F5']) +
                        corch(['E5', 'C5', 'D5', 'B4', 'C5', 'A4', 'B4', 'G4']) +
                        corch(['A4', 'F4', 'G4', 'E4', 'F4', 'D4', 'D4', 'D4']),
                 bars_per_line=4),
            dict(num=6, titulo='La izquierda, que solo sostiene', clef='bass',
                 pista='una redonda por compás, por los grados de Re mayor · atacar y soltar el brazo',
                 events=[n(p, 'w') for p in ('D3', 'A2', 'B2', 'G2', 'E3', 'A2', 'D3', 'D3')],
                 bars_per_line=8),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con dos sostenidos. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · armadura de Re: Fa y Do son ♯',
        chuleta_clef='treble',
        chuleta_titulo='EL REGISTRO DE LA MANO DERECHA (CLAVE DE SOL)',
        chuleta_pitches=['D4', 'F4', 'A4', 'B4', 'D5', 'F5', 'A5'],
        chuleta_nombres=['Re', 'Fa♯', 'La', 'Si', 'Re', 'Fa♯', 'La'],
        ejercicios=[
            dict(num=1, titulo='Clave de Sol, registro alto',
                 pista='donde vive la melodía · con líneas adicionales por arriba',
                 events=[n(p) for p in ('D5', 'A5', 'F5', 'B4', 'G5', 'E5', 'C5', 'A4',
                                        'F4', 'D4', 'B5', 'G4', 'E4', 'C5', 'A5', 'D5')]),
            dict(num=2, titulo='Clave de Fa', clef='bass',
                 pista='la izquierda vive aquí, y solo toca una nota por compás',
                 events=[n(p) for p in ('D3', 'A2', 'F2', 'B2', 'G2', 'E3', 'C3', 'D2',
                                        'A3', 'F3', 'B3', 'G3', 'E2', 'C3', 'D3', 'A2')]),
            dict(num=3, titulo='Leyendo dos a la vez',
                 pista='dos notas en cada golpe · nombra las dos, de abajo arriba',
                 events=[{'pitches': list(d), 'dur': 'q'} for d in
                         [('D4', 'A4'), ('F4', 'B4'), ('E4', 'C5'), ('D4', 'D5'),
                          ('G4', 'B4'), ('F4', 'D5'), ('E4', 'A4'), ('D4', 'F5')]] +
                        [{'pitches': ['D4', 'D5'], 'dur': 'w'}],
                 bars_per_line=3),
        ],
        crono='¿Cuánto tardas en el ejercicio 3, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca dos notas a la vez y luego mueve SOLO una de las dos. Que diga cuál se ha '
                      'movido, la de arriba o la de abajo. Es exactamente lo que hace su mano derecha.'),
                ('B', 'Toca cuatro tiempos y mete DOS notas o TRES en uno de ellos (tresillo). Que diga '
                      'cuántas eran.'),
                ('C', 'Toca una tríada suelta: MAYOR o MENOR.'),
                ('+', 'Y sin escribir: que sostenga una tecla con el pulgar mientras el meñique toca '
                      'cuatro notas. La de abajo no puede cortarse.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Cuál se ha movido?', pista='de las dos notas, solo una cambia',
                     n=10, opciones=['arriba', 'abajo']),
                dict(letra='B', titulo='¿Dos o tres?', pista='cuántas notas caben en ese tiempo',
                     n=8, opciones=['2', '3']),
                dict(letra='C', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=6, opciones=['M', 'm']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Aviso: de esta partitura no se citan notas. Su izquierda va en redondas y su derecha es '
              'muy densa, y no he podido medirlas con seguridad. Lo de aquí es ANDAMIO con los grados '
              'de Re mayor para trabajar EL GESTO; las notas están en la partitura de la página 1. El '
              'gesto es el problema de verdad: una mano haciendo dos cosas a la vez.',
        reglas=['ESTO ES ANDAMIO, NO LA PIEZA', 'LOS DEDOS 1 Y 2 NO SE LEVANTAN', 'LENTO'],
        bloques=[
            dict(num=1, titulo='La mano derecha, voz por voz',
                 pista='andamio · primero la que se queda quieta, después la que se mueve, nunca las dos',
                 sistemas=[
                     dict(cap='a) solo la voz de abajo: se ataca y se aguanta los cuatro tiempos',
                          events=[n('D4', 'w'), n('B3', 'w'), n('E4', 'w'), n('D4', 'w')],
                          bars=4),
                     dict(cap='b) solo la voz de arriba, con la misma mano, sin tocar la de abajo',
                          events=corch(['A4', 'B4', 'D5', 'B4', 'A4', 'G4', 'F4', 'A4']) +
                                 corch(['B4', 'D5', 'E5', 'D5', 'B4', 'A4', 'G4', 'A4']),
                          bars=4, show_time=False),
                     dict(cap='c) y ahora las dos juntas · el dedo 1 no se levanta aunque los de arriba '
                              'corran; si se corta la de abajo, vuelve a la a)',
                          events=[{'pitches': ['D4', 'A4'], 'dur': 'q'},
                                  {'pitches': ['D4', 'B4'], 'dur': 'q'},
                                  {'pitches': ['D4', 'D5'], 'dur': 'q'},
                                  {'pitches': ['D4', 'B4'], 'dur': 'q'},
                                  {'pitches': ['B3', 'A4'], 'dur': 'q'},
                                  {'pitches': ['B3', 'G4'], 'dur': 'q'},
                                  {'pitches': ['B3', 'F4'], 'dur': 'q'},
                                  {'pitches': ['B3', 'A4'], 'dur': 'q'},
                                  {'pitches': ['D4', 'D5'], 'dur': 'w'}],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA CANCIÓN ENGAÑA',
                 texto='Miras la partitura y la izquierda tiene una nota por compás: parece la pieza más '
                       'fácil del cuaderno. Y lo es, si solo miras la izquierda. Toda la dificultad se ha '
                       'ido a la derecha, que tiene que hacer dos cosas a la vez: unos dedos apretando sin '
                       'moverse y otros corriendo por encima. Cuando algo suene sucio, no busques el fallo '
                       'en la izquierda: casi siempre es que has levantado el pulgar sin darte cuenta.'),
            dict(num='1b', semis=True, titulo='Y la voz de arriba, con su figura de verdad',
                 pista='la voz que se mueve va en SEMICORCHEAS en tu partitura · aquí sola, sin la '
                       'nota de abajo, que es como se estudia',
                 sistemas=[
                     dict(cap='a) cuatro por golpe, y las cuatro del mismo peso · si una pesa más '
                              'que las otras, para y vuelve a empezar',
                          events=[{'pitch': 'A4', 'dur': 's', 'beam': 9400}, {'pitch': 'B4', 'dur': 's', 'beam': 9400}, {'pitch': 'C#5', 'dur': 's', 'beam': 9400}, {'pitch': 'B4', 'dur': 's', 'beam': 9400}, {'pitch': 'A4', 'dur': 's', 'beam': 9401}, {'pitch': 'G4', 'dur': 's', 'beam': 9401}, {'pitch': 'F#4', 'dur': 's', 'beam': 9401}, {'pitch': 'G4', 'dur': 's', 'beam': 9401}, {'pitch': 'A4', 'dur': 's', 'beam': 9402}, {'pitch': 'B4', 'dur': 's', 'beam': 9402}, {'pitch': 'C#5', 'dur': 's', 'beam': 9402}, {'pitch': 'D5', 'dur': 's', 'beam': 9402}, {'pitch': 'E5', 'dur': 's', 'beam': 9403}, {'pitch': 'D5', 'dur': 's', 'beam': 9403}, {'pitch': 'C#5', 'dur': 's', 'beam': 9403}, {'pitch': 'B4', 'dur': 's', 'beam': 9403}],
                          bars=1),
                     dict(cap='b) y bajando · el dedo que va a aguantar el Re no se mete todavía',
                          events=[{'pitch': 'D5', 'dur': 's', 'beam': 9404}, {'pitch': 'C#5', 'dur': 's', 'beam': 9404}, {'pitch': 'B4', 'dur': 's', 'beam': 9404}, {'pitch': 'A4', 'dur': 's', 'beam': 9404}, {'pitch': 'G4', 'dur': 's', 'beam': 9405}, {'pitch': 'F#4', 'dur': 's', 'beam': 9405}, {'pitch': 'E4', 'dur': 's', 'beam': 9405}, {'pitch': 'F#4', 'dur': 's', 'beam': 9405}, {'pitch': 'G4', 'dur': 's', 'beam': 9406}, {'pitch': 'A4', 'dur': 's', 'beam': 9406}, {'pitch': 'B4', 'dur': 's', 'beam': 9406}, {'pitch': 'C#5', 'dur': 's', 'beam': 9406}, {'pitch': 'D5', 'dur': 's', 'beam': 9407}, {'pitch': 'C#5', 'dur': 's', 'beam': 9407}, {'pitch': 'B4', 'dur': 's', 'beam': 9407}, {'pitch': 'A4', 'dur': 's', 'beam': 9407}],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='Sostener mientras la de arriba salta',
                 pista='andamio · lo mismo, pero arriba ya no va por grados: va a saltos',
                 sistemas=[
                     dict(cap='a) el dedo 1 clavado en el Re y los de arriba saltando de tercera en tercera',
                          events=[{'pitches': ['D4', 'F4'], 'dur': 'q'},
                                  {'pitches': ['D4', 'A4'], 'dur': 'q'},
                                  {'pitches': ['D4', 'F5'], 'dur': 'q'},
                                  {'pitches': ['D4', 'A4'], 'dur': 'q'},
                                  {'pitches': ['D4', 'B4'], 'dur': 'q'},
                                  {'pitches': ['D4', 'G4'], 'dur': 'q'},
                                  {'pitches': ['D4', 'E5'], 'dur': 'q'},
                                  {'pitches': ['D4', 'A4'], 'dur': 'q'},
                                  {'pitches': ['D4', 'D5'], 'dur': 'w'}],
                          bars=3),
                     dict(cap='b) la izquierda, que aquí solo sostiene · ataca, suelta el brazo y no '
                              'vuelvas a tocar: el brazo se queda muerto encima de la tecla',
                          events=[n(p, 'w') for p in ('D2', 'A2', 'B2', 'G2', 'D2', 'A2')],
                          bars=6, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA PRUEBA QUE NO ENGAÑA',
                 texto='Toca el paso 1c y canta en voz alta la nota de abajo, la que estás sosteniendo. '
                       'Si dejas de oírla, es que el dedo se te ha levantado. Nadie tiene que decírtelo: '
                       'lo oyes tú.'),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='El gesto ya está. Ahora se alarga: primero cuatro compases sin que se corte la voz de '
              'abajo, después los ocho de una frase entera. Y la letra, que la edición trae debajo, '
              'coloca el fraseo sola.',
        reglas=['CANTA LA LETRA MIENTRAS TOCAS', 'PRIMERO LAS VOCES SUELTAS', 'LENTO DE VERDAD'],
        bloques=[
            dict(num=3, titulo='Sostener y cantar a la vez',
                 pista='andamio · la voz de abajo aguanta mientras la de arriba hace la frase',
                 sistemas=[
                     dict(cap='a) cuatro compases seguidos sin que se corte ni una vez la nota de abajo',
                          events=[{'pitches': ['D4', 'A4'], 'dur': 'h'},
                                  {'pitches': ['D4', 'B4'], 'dur': 'h'},
                                  {'pitches': ['D4', 'D5'], 'dur': 'h'},
                                  {'pitches': ['D4', 'B4'], 'dur': 'h'},
                                  {'pitches': ['B3', 'G4'], 'dur': 'h'},
                                  {'pitches': ['B3', 'A4'], 'dur': 'h'},
                                  {'pitches': ['D4', 'F5'], 'dur': 'h'},
                                  {'pitches': ['D4', 'D5'], 'dur': 'h'}],
                          bars=4),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL TRESILLO, Y LA LETRA',
                 texto='Cuando veas un 3 encima de un grupo, ahí caben tres notas donde normalmente caben '
                       'dos. No se cuenta más rápido: se reparte el mismo tiempo entre tres. Di '
                       '“man-za-na” mientras el pie marca dos golpes. Y usa la letra que trae la edición: '
                       'cada sílaba te dice dónde cae una nota, y donde respira la voz respira la mano. '
                       'Canta “A-mi-ga mí-a, lo sé…” y el fraseo se coloca solo.'),
            dict(num=4, titulo='La frase entera, sin cortar la de abajo',
                 pista='andamio · ocho compases seguidos, que es lo que dura una frase de la canción',
                 sistemas=[
                     dict(cap='a) si te cortas, no repitas el compás: vuelve al principio de los ocho',
                          events=[{'pitches': ['D4', 'A4'], 'dur': 'h'},
                                  {'pitches': ['D4', 'B4'], 'dur': 'h'},
                                  {'pitches': ['D4', 'A4'], 'dur': 'h'},
                                  {'pitches': ['D4', 'G4'], 'dur': 'h'},
                                  {'pitches': ['B3', 'G4'], 'dur': 'h'},
                                  {'pitches': ['B3', 'A4'], 'dur': 'h'},
                                  {'pitches': ['B3', 'B4'], 'dur': 'h'},
                                  {'pitches': ['B3', 'A4'], 'dur': 'h'},
                                  {'pitches': ['E4', 'C5'], 'dur': 'h'},
                                  {'pitches': ['E4', 'B4'], 'dur': 'h'},
                                  {'pitches': ['E4', 'A4'], 'dur': 'h'},
                                  {'pitches': ['E4', 'G4'], 'dur': 'h'},
                                  {'pitches': ['D4', 'F5'], 'dur': 'h'},
                                  {'pitches': ['D4', 'D5'], 'dur': 'h'},
                                  {'pitches': ['D4', 'A4'], 'dur': 'w'}],
                          bars=4),
                     dict(cap='b) y la voz de arriba sola, para oír la frase que estabas tapando · '
                              'cántala mientras la tocas',
                          events=[n(p, 'h') for p in ('A4', 'B4', 'A4', 'G4', 'G4', 'A4', 'B4', 'A4',
                                                      'C5', 'B4', 'A4', 'G4', 'F5', 'D5')] +
                                 [n('A4', 'w')],
                          bars=8, show_time=False),
                 ]),
            dict(tipo='escalera', valores=[40, 46, 52, 58, 64, 70],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · La derecha voz por voz, y después las dos juntas.   '
                       '2 · Lo mismo con la de arriba saltando, y la izquierda sosteniendo.   '
                       '3 · Cuatro compases sin que se corte la voz de abajo.   '
                       '4 · La frase entera, ocho compases.   '
                       '5 · La escalera de tempo, y las dos manos cantando la letra.'),
        ],
    ),

)

_S1, _S2, _S3 = sistemas_extra('Re mayor', 'D4', 'D3', time_sig=(4, 4),
                               variante=49, letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques']
          if b.get('num') and not b.get('semis')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
# La tercera tanda de `sistemas_extra` estaba escrita y sin colocar; con el
# bloque nuevo de semicorcheas hace falta para llenar la ultima hoja.
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

# La escalera de tempo pasa de la segunda hoja de estudio a la primera: es
# papel, no pentagrama, así que se mueve sin perder nada, y con ella fuera la
# segunda vuelve a caber en una hoja en vez de abrir una cuarta casi vacía.
_ESC = [b for b in CANCION['piano2']['bloques'] if b.get('tipo') == 'escalera']
if _ESC:
    CANCION['piano2']['bloques'] = [b for b in CANCION['piano2']['bloques']
                                    if b.get('tipo') != 'escalera']
    CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + _ESC

# El recurso que la pieza EXPLICA y no dibujaba: durante meses se anotó como
# "no cabe en la hoja". Desde que la hoja se pagina sola, esa excusa dejó de
# ser cierta.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Re mayor', 64, 'D4', 'D3',
    'la mano en el tono antes de los tresillos',
    desde=5, time_sig=(4, 4)) + [
    bloque_tresillos('Re mayor', 4, 'D4', 'los tresillos marcados con un 3', time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
