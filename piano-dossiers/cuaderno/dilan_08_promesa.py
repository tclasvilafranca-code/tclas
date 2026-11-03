# -*- coding: utf-8 -*-
"""La Promesa (Melendi) — Dilan, avanzado. Ver TRANSCRIPCION_D06_08.md.

   Que esta medido y por tanto se puede citar:
     - Sol mayor, 4/4, Lento, 32 compases (el lector contaba 33: una de las
       barras era la doble del :||: del c. 28).
     - La forma: c.1 de entrada, bloque A cc. 2-28 con repeticion, bloque A'
       cc. 29-32 con repeticion. Los cc. 29-32 vuelven a poner las mismas
       notas en el pentagrama que los cc. 2-5.
     - La derecha repite la misma nota cuatro y cinco veces seguidas en
       muchos compases (6, 7, 8, 25, 26, 27). De ahi que suene hablada.
     - El c. 16 es el unico en el que la izquierda anda: cuatro negras.
     - El c. 5 (y el 32, que es el mismo) baja Re-Re-Do-Si-La-La por debajo
       del pentagrama. Medido con el lector y comprobado a zoom dos veces.

   Que NO esta medido, y por tanto NO se cita:
     - Los acordes de la izquierda. Van en blancas (cabezas huecas) y solo se
       leen las notas graves sueltas, no el acorde entero.
     - El ritmo real de la derecha: semicorcheas, fusas y silencios de
       semicorchea. El motor no escribe esas figuras, asi que donde se citan
       alturas se dice expresamente que el ritmo esta simplificado.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloque_tresillos, bloques_extra

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'
_B = [1400]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='h'):
    return {'pitches': list(ps), 'dur': d}


def sil(d='e'):
    return {'rest': True, 'dur': d}


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


CANCION = dict(
    alumno='Dilan', num=8, nivel='avanzado', slug='LaPromesa',
    titulo_corto='La Promesa', time_sig=(4, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' la-promesa-MELENDI.pdf'),
    yt='https://www.youtube.com/results?search_query=melendi+la+promesa',

    ficha=dict(
        titulo='La Promesa', autor='Ramón Melendi Espina (2004)',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'), ('Tempo', 'Lento'),
               ('Compases', '32'), ('Repeticiones', 'dos')],
        total_compases=32,
        secciones=[
            ('A', 1, 28, 'Entrada en el c. 1 · todo el cuerpo · con repetición', AZUL),
            ("A'", 29, 32, 'Vuelve el principio', OCRE),
        ],
        armonia=dict(
            titulo='Cómo está montada',
            tarjetas=[
                ('LA IZQUIERDA', 'Dos capas',
                 'Una nota grave abajo, con líneas adicionales, y encima un acorde de tres notas. '
                 'Las dos cosas a la vez, en blancas: dos por compás.'),
                ('LA DERECHA', 'Habla',
                 'Semicorcheas con silencios entre medias, y la misma nota repetida cuatro o cinco '
                 'veces seguidas. Por eso suena a alguien contando algo.'),
                ('EL C. 16', 'El único que anda',
                 'Es el compás en el que la izquierda deja las blancas y toca cuatro negras. Marca '
                 'el sitio donde la canción se pone en marcha.'),
                ('LOS CC. 29–32', 'El principio otra vez',
                 'Las mismas notas del c. 2 al 5. Cuando llegas al final ya te lo sabías.'),
            ],
            pie='Los dos bloques llevan barra de repetición: el primero va del c. 2 al 28 y el segundo '
                'del 29 al 32. La canción entera son 32 compases, pero solo hay que aprender 28: los '
                'cuatro últimos son los cuatro primeros.',
        ),
        ritmos=[
            ('MI', 'dos blancas por compás: grave abajo y acorde encima (andamio)',
             [ac(['G2', 'B3', 'D4']), ac(['G2', 'B3', 'D4'])], OCRE, 'bass', SOL),
            ('MD', 'la misma nota, repetida, con silencios: así habla (andamio)',
             [sil('e')] + corch(['B4', 'B4', 'B4', 'B4']) + [sil('e')] +
             corch(['B4', 'B4']), AZUL, 'treble', SOL),
        ],
        especial=[
            'Armadura de un sostenido: todos los Fa son ♯.',
            'La izquierda toca DOS cosas a la vez: una nota grave y un acorde encima.',
            'El c. 1 es solo silencio y dos notas de entrada: la canción empieza de verdad en el 2.',
            'La derecha repite la misma nota cuatro y cinco veces seguidas.',
            'Hay TRESILLOS marcados con un 3 entre los cc. 24 y 27.',
            'Pone Lento, y va en serio: esta canción se cuenta, no se corre.',
        ],
        reto='Que la nota grave y el acorde suenen a la vez y en el mismo golpe. Si el acorde entra un '
             'pelo antes que el bajo, la izquierda suena rota, y se nota mucho en una canción tan lenta.',
        truco='Estudia la izquierda mirándote la mano, sin partitura: coloca los cuatro dedos, aprieta el '
              'fondo de las teclas a la vez y suelta el brazo. Cuando eso salga limpio diez veces '
              'seguidas, entonces sí, abre la partitura.',
        sabias='Melendi la escribió cuando todavía cantaba en bares de Oviedo. Salió en "Sin noticias de '
               'Holanda" en 2004, y durante años la tocó en directo solo con guitarra: la versión de '
               'piano vino después, y por eso el acompañamiento es tan sencillo de acordes.',
        qr=dict(titulo='Escucha la original',
                texto='Cuenta cuántas veces repite la misma nota en cada frase.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta canción pide dos cosas: que la izquierda '
              'salte del bajo al acorde sin romperse y que la derecha repita la misma nota sin atascarse.',
        reglas=['ARMADURA DE SOL: TODOS LOS FA SON ♯', 'GOLPE ÚNICO EN LA IZQUIERDA', 'LENTO DE VERDAD'],
        ejercicios=[
            dict(num=1, titulo='Escala de Sol mayor · dos octavas',
                 pista='manos separadas · un solo sostenido, y el pulgar por debajo sin bache',
                 events=corch(['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4']) +
                        corch(['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'G5']) +
                        corch(['G5', 'F5', 'E5', 'D5', 'C5', 'B4', 'A4', 'G4']) +
                        corch(['F4', 'E4', 'D4', 'C4', 'B3', 'A3', 'G3', 'G3']),
                 bars_per_line=4),
            dict(num=2, titulo='Terceras rotas',
                 pista='dos notas de la escala, saltando una · así la mano deja de ir sólo de vecina en vecina',
                 events=corch(['G3', 'B3', 'A3', 'C4', 'B3', 'D4', 'C4', 'E4']) +
                        corch(['D4', 'F4', 'E4', 'G4', 'F4', 'A4', 'G4', 'B4']) +
                        corch(['A4', 'F4', 'G4', 'E4', 'F4', 'D4', 'E4', 'C4']) +
                        corch(['D4', 'B3', 'C4', 'A3', 'B3', 'G3', 'G3', 'G3']),
                 bars_per_line=4),
            dict(num=3, titulo='El acorde solo', clef='bass',
                 pista='tres notas a la vez, bajando por la escala · que las tres entren en el mismo golpe',
                 events=[ac(['G3', 'B3', 'D4']), ac(['F3', 'A3', 'C4']),
                         ac(['E3', 'G3', 'B3']), ac(['D3', 'F3', 'A3']),
                         ac(['C3', 'E3', 'G3']), ac(['B2', 'D3', 'F3']),
                         ac(['A2', 'C3', 'E3']), ac(['G2', 'B2', 'D3']),
                         ac(['G3', 'B3', 'D4'], 'w')],
                 bars_per_line=5),
            dict(num=4, titulo='El salto del bajo al acorde', clef='bass',
                 pista='el gesto de la canción · el brazo va abajo, coge la grave y sube al acorde sin mirar',
                 events=[n('G2'), ac(['B2', 'D3', 'G3'], 'q'), n('G2'), ac(['B2', 'D3', 'G3'], 'q'),
                         n('E2'), ac(['G2', 'B2', 'E3'], 'q'), n('E2'), ac(['G2', 'B2', 'E3'], 'q'),
                         n('C2'), ac(['E2', 'G2', 'C3'], 'q'), n('C2'), ac(['E2', 'G2', 'C3'], 'q'),
                         n('D2'), ac(['F2', 'A2', 'D3'], 'q'), ac(['D2', 'A2', 'D3'], 'h')],
                 bars_per_line=4),
            dict(num=5, titulo='La misma nota, cambiando de dedo',
                 pista='dedos 3 · 2 · 1 · 3 · 2 · 1 · lo que hace su mano derecha todo el rato',
                 events=corch(['C5'] * 8) + corch(['B4'] * 8) +
                        corch(['A4'] * 8) + corch(['G4'] * 8),
                 bars_per_line=4),
            dict(num=6, titulo='Entrar después del silencio',
                 pista='la derecha de esta canción empieza casi siempre tarde · cuenta el silencio en voz alta',
                 events=[sil('q'), n('B4'), n('B4'), n('B4'),
                         sil('q'), n('C5'), n('C5'), n('C5'),
                         sil('q'), n('D5'), n('D5'), n('D5'),
                         sil('q'), n('B4'), n('B4'), n('B4')],
                 bars_per_line=4),
            dict(num=7, titulo='El bajo solo, en redondas', clef='bass',
                 pista='una por compás, sin prisa · atacar el fondo de la tecla y soltar el brazo entero',
                 events=[n(p, 'w') for p in ('G2', 'E2', 'C2', 'D2', 'G2', 'E2', 'A2', 'D2')],
                 bars_per_line=8),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con un sostenido. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · armadura de Sol: todos los Fa son ♯',
        chuleta_clef='treble',
        chuleta_titulo='EL REGISTRO DE LA MANO DERECHA (CLAVE DE SOL)',
        chuleta_pitches=['G4', 'B4', 'D5', 'G5'],
        chuleta_nombres=['Sol', 'Si', 'Re', 'Sol'],
        ejercicios=[
            dict(num=1, titulo='Clave de Sol',
                 pista='donde vive la melodía · el orden está desordenado a propósito',
                 events=[n(p) for p in ('B4', 'G5', 'D5', 'A4', 'F5', 'C5', 'E5', 'G4',
                                        'A5', 'B4', 'F4', 'D5', 'C5', 'E4', 'G5', 'B4')]),
            dict(num=2, titulo='Clave de Fa · abajo del todo', clef='bass',
                 pista='la nota grave de la izquierda vive aquí, con líneas adicionales por debajo',
                 events=[n(p) for p in ('G2', 'C2', 'E2', 'D2', 'A2', 'F2', 'B2', 'G2',
                                        'D3', 'C3', 'E3', 'A3', 'F3', 'B3', 'G3', 'C2')]),
            dict(num=3, titulo='Leer un acorde de tres', clef='bass',
                 pista='nómbralas de abajo arriba, las tres, antes de pasar a la siguiente',
                 events=[ac(['G3', 'B3', 'D4'], 'q'), ac(['A3', 'C4', 'E4'], 'q'),
                         ac(['B3', 'D4', 'F4'], 'q'), ac(['C4', 'E4', 'G4'], 'q'),
                         ac(['D3', 'F3', 'A3'], 'q'), ac(['E3', 'G3', 'B3'], 'q'),
                         ac(['F3', 'A3', 'C4'], 'q'), ac(['G3', 'B3', 'D4'], 'q')],
                 bars_per_line=4),
        ],
        crono='¿Cuánto tardas en el ejercicio 3, diciendo las tres notas de cada acorde?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca una nota grave y un acorde encima, como hace su izquierda, y unas veces '
                      'júntalos y otras entra el acorde un poco antes. Que diga si ha sonado A LA VEZ '
                      'o ROTO. Es el fallo que más se le va a escapar en esta canción.'),
                ('B', 'Repite una misma nota varias veces seguidas, entre dos y cinco. Que cuente '
                      'cuántas fueron, sin mirar.'),
                ('C', 'Toca una tríada suelta: MAYOR o MENOR.'),
                ('+', 'Y sin escribir: toca la frase del c. 5 tal cual está en la partitura y que te '
                      'diga si sube o si baja. Que la reconozca de oído, porque vuelve al final.'),
            ],
            filas=[
                dict(letra='A', titulo='¿A la vez o roto?', pista='el bajo y el acorde, en el mismo golpe',
                     n=10, opciones=['=', '≠']),
                dict(letra='B', titulo='¿Cuántas repeticiones?', pista='la misma nota, seguida',
                     n=8, opciones=['2', '3', '4', '5']),
                dict(letra='C', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=6, opciones=['M', 'm']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Aviso: solo se citan las notas que he podido medir, que son las de la derecha. Los '
              'acordes de la izquierda van en blancas y no se leen con seguridad, así que sus '
              'ejercicios son ANDAMIO en Sol mayor: el dibujo es el de la partitura, el acorde exacto '
              'míralo allí. Se empieza por la izquierda porque es la que sostiene la canción entera.',
        reglas=['ANDAMIO EN LA IZQUIERDA · NOTAS MEDIDAS EN LA DERECHA', 'GOLPE ÚNICO', 'LENTO'],
        bloques=[
            dict(num=1, titulo='La izquierda, capa por capa', clef='bass',
                 pista='cc. 2–5 · andamio · el bajo y el acorde tienen que entrar SIEMPRE a la vez',
                 sistemas=[
                     dict(cap='a) solo la nota grave, en blancas: dos por compás',
                          events=[n('G2', 'h'), n('G2', 'h'), n('E2', 'h'), n('E2', 'h'),
                                  n('C2', 'h'), n('C2', 'h'), n('D2', 'h'), n('D2', 'h')],
                          pedal=4,
                          bars=4, clef='bass'),
                     dict(cap='b) y ahora la nota grave con el acorde encima, en el mismo golpe',
                          events=[ac(['G2', 'B3', 'D4']), ac(['G2', 'B3', 'D4']),
                                  ac(['E2', 'G3', 'B3']), ac(['E2', 'G3', 'B3']),
                                  ac(['C2', 'E3', 'G3']), ac(['C2', 'E3', 'G3']),
                                  ac(['D2', 'F3', 'A3']), ac(['D2', 'F3', 'A3'])],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='b) y AHORA con su figura de verdad, la semicorchea · el mismo dibujo el doble de rápido, tal y como está impreso en tu partitura',
                          events=[{'pitch': 'G2', 'dur': 's', 'beam': 9130},
                                  {'pitch': 'G2', 'dur': 's', 'beam': 9130},
                                  {'pitch': 'E2', 'dur': 's', 'beam': 9130},
                                  {'pitch': 'E2', 'dur': 's', 'beam': 9130},
                                  {'pitch': 'C2', 'dur': 's', 'beam': 9131},
                                  {'pitch': 'C2', 'dur': 's', 'beam': 9131},
                                  {'pitch': 'D2', 'dur': 's', 'beam': 9131},
                                  {'pitch': 'D2', 'dur': 's', 'beam': 9131},
                                  {'pitch': 'G2', 'dur': 'q'},
                                  {'pitch': 'G2', 'dur': 'q'}],
                          bars=1, show_time=False, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='ESTO NO SE SOSTIENE CON LA MANO',
                 texto='La nota grave y el acorde están escritos como blancas: suenan los dos tiempos. '
                       'Pero entre ellos hay más de una octava y media, y esa distancia no la aguanta '
                       'ninguna mano. Se aguanta con el PEDAL, y el pedal se cambia justo DESPUÉS de '
                       'tocar el acorde nuevo, nunca antes.'),
            dict(num=2, titulo='La derecha, que no canta: habla',
                 pista='cc. 5–8 · las alturas son las de la partitura; el ritmo, simplificado para leerlo',
                 sistemas=[
                     dict(cap='a) el suspiro del c. 5 · en la partitura va en semicorcheas y baja por '
                              'debajo del pentagrama; aquí en negras, solo para leerlo',
                          events=[n('D4'), n('D4'), n('C4'), n('B3'),
                                  n('A3'), n('A3', 'h'), {'rest': True, 'dur': 'q'},
                                  n('A3', 'w')],
                          bars=3),
                     dict(cap='b) y los cc. 6, 7 y 8 · cada compás se planta en una nota y la repite: '
                              'Si, luego Do, luego Mi — sepáralas, no las ligues',
                          events=[n('B4'), n('B4'), n('B4'), n('B4'),
                                  n('C5'), n('C5'), n('C5'), n('C5'),
                                  n('E5'), n('E5'), n('E5'), n('E5'),
                                  n('E5', 'w')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SUENA HABLADA',
                 texto='La misma nota repetida cuatro y cinco veces, con silencios de semicorchea entre '
                       'medias. Eso es lo que hace que suene a alguien contándote algo y no a una melodía '
                       'cantada. No ligues esas notas: sepáralas. Lo que suena largo es la izquierda.'),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='Hay menos canción de la que parece. Son 32 compases, pero los cuatro últimos son los '
              'cuatro primeros y los dos bloques llevan repetición: lo que se aprende de verdad son '
              'los cc. 2 al 28.',
        reglas=['LOS CC. 29–32 SON LOS CC. 2–5', 'PRIMERO LA IZQUIERDA SOLA', 'LENTO DE VERDAD'],
        bloques=[
            dict(num=3, titulo='Solo el primer golpe de cada compás', clef='bass',
                 pista='andamio · toca únicamente el acorde que cae en el uno y salta al compás siguiente',
                 sistemas=[
                     dict(cap='a) ocho compases seguidos, un acorde por compás: así se oye por dónde va '
                              'la canción sin tocar ni una nota de la melodía',
                          events=[ac(['G2', 'B2', 'D3'], 'w'), ac(['E2', 'G2', 'B2'], 'w'),
                                  ac(['C2', 'E2', 'G2'], 'w'), ac(['D2', 'F2', 'A2'], 'w'),
                                  ac(['G2', 'B2', 'D3'], 'w'), ac(['E2', 'G2', 'B2'], 'w'),
                                  ac(['A2', 'C3', 'E3'], 'w'), ac(['D2', 'F2', 'A2'], 'w')],
                          bars=8, clef='bass'),
                     dict(cap='b) y lo mismo quitando el acorde: solo la nota grave · dilo en voz alta '
                              'mientras lo tocas — Sol, Mi, Do, Re, Sol, Mi, La, Re',
                          events=[n(p, 'w') for p in ('G2', 'E2', 'C2', 'D2',
                                                      'G2', 'E2', 'A2', 'D2')],
                          bars=8, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA FORMA, EN UNA LÍNEA',
                 texto='c. 1 de entrada · ‖: cc. 2–28 :‖ · ‖: cc. 29–32 :‖. Dos bloques, los dos con '
                       'barra de repetición, y el segundo son las mismas notas que los cc. 2 al 5. No es '
                       'una interpretación mía: está medido compás a compás, y las notas de los cc. 29 a '
                       '32 caen exactamente en los mismos sitios del pentagrama que las de los cc. 2 a 5, '
                       'con algún sostenido añadido. Cuando te sepas los cuatro primeros, tienes el final '
                       'regalado.'),
            dict(num=4, titulo='La costura del c. 28 al c. 29',
                 pista='andamio · el sitio donde se cierra el bloque grande y vuelve a empezar la frase',
                 sistemas=[
                     dict(cap='a) para y respira en la barra: lo que viene detrás es la frase del '
                              'principio, y tiene que sonar igual de tranquila',
                          events=[n('B4', 'h'), n('C5', 'h'), n('G4', 'h'), {'rest': True, 'dur': 'h'},
                                  n('G4'), n('G4'), n('F4'), n('G4'),
                                  n('G4', 'w')],
                          bars=4),
                 ]),
            dict(tipo='nota',
                 etiqueta='LOS TRESILLOS DE LOS CC. 24 AL 27',
                 texto='Ahí aparece un 3 encima de algunos grupos: en ese tiempo caben tres notas donde '
                       'normalmente caben dos. No se toca más rápido, se reparte el mismo tiempo entre '
                       'tres. Y es el sitio donde la canción se calienta: los tresillos empujan justo '
                       'antes de que vuelva la frase del principio. Cuéntalos con el pie hasta que salgan '
                       'sin pensar, y luego olvídate de contar.'),
            dict(tipo='escalera', valores=[44, 50, 56, 62, 68, 72],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · La izquierda capa por capa, cc. 2–5, y el c. 16 aparte.   '
                       '2 · La derecha, separando las notas repetidas.   '
                       '3 · Un golpe por compás, ocho compases seguidos.   '
                       '4 · La costura del 28 al 29.   '
                       '5 · La escalera, y del c. 2 al 28 seguido con la repetición.'),
        ],
    ),

)

# El recurso que la pieza EXPLICA y no dibujaba: durante meses se anotó como
# "no cabe en la hoja". Desde que la hoja se pagina sola, esa excusa dejó de
# ser cierta.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Sol mayor', 69, 'G3', 'G2',
    'el Fa sostenido, antes de que llegue el tresillo',
    desde=6, time_sig=(4, 4)) + [
    bloque_tresillos('Sol mayor', 5, 'G3', 'los tresillos de la melodía', time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
