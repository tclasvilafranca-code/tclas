# -*- coding: utf-8 -*-
"""What Was I Made For? (Billie Eilish) — Dilan, avanzado.
   Ver TRANSCRIPCION_D12_14.md.

   Do mayor, sin armadura. La edicion trae CIFRADOS impresos (C, Em, F, Am,
   Dm, G) y LETRA, asi que la armonia no hay que deducirla: esta escrita.

   La izquierda va en blancas (cabezas huecas) y el lector no la lee entera;
   lo unico medido de ella es el registro del acorde de Fa, que sale Fa3 ·
   La3 · Do4, en estado fundamental. Los demas acordes se escriben en esa
   misma posicion y se dice en la hoja que la posicion exacta esta en la
   partitura.

   La melodia si esta medida entera.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
_B = [2100]


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


# --- los cifrados impresos, en la posicion medida del acorde de Fa ---------
DO = ('C3', 'E3', 'G3')
MIm = ('E3', 'G3', 'B3')
FA = ('F3', 'A3', 'C4')          # medido
LAm = ('A3', 'C4', 'E4')
REm = ('D3', 'F3', 'A3')
SOL = ('G3', 'B3', 'D4')

CANCION = dict(
    alumno='Dilan', num=13, nivel='avanzado', slug='WhatWasIMadeFor',
    titulo_corto='What Was I Made For?', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           'what-was-i-made-for-billie-eilish.pdf'),
    yt='https://www.youtube.com/results?search_query=billie+eilish+what+was+i+made+for',

    ficha=dict(
        titulo='What Was I Made For?',
        autor='Billie Eilish y Finneas O’Connell (2023) · edición con cifrados y letra',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'), ('Tempo', '♩=78'),
               ('Mano izq.', 'Tríadas'), ('Extras', 'Cifrados')],
        armonia=dict(
            titulo='El bucle que sostiene la canción',
            tarjetas=[
                ('EL BUCLE', 'Do · Mi m · Fa',
                 'Tres acordes, cada dos compases, durante casi toda la canción.'),
                ('CIFRADO F', 'Fa3 · La3 · Do4',
                 'El único acorde medido nota por nota. Estado fundamental, mano media.'),
                ('LOS OTROS', 'Am · Dm · G',
                 'Aparecen al final de cada estrofa y son los que rompen el bucle.'),
                ('LA IZQUIERDA', 'Blancas',
                 'Dos acordes por compás, o uno sostenido. No hay ni un movimiento rápido.'),
            ],
            pie='Los cifrados están impresos encima del pentagrama, así que la armonía no hay que '
                'deducirla: viene dada. Y son solo seis acordes en toda la canción. Si te aprendes las '
                'seis posiciones de la mano izquierda, esta pieza deja de ser un problema de lectura y '
                'pasa a ser un problema de contar, que es donde está de verdad la dificultad.',
        ),
        ritmos=[
            ('MI', 'dos tríadas por compás, en blancas',
             [ac(DO), ac(MIm)], OCRE, 'bass', None),
            ('MI · el compás siguiente', 'y en el siguiente solo uno, sostenido',
             [ac(FA, 'w')], OCRE, 'bass', None),
            ('MD', 'la melodía, con la letra debajo',
             [sil(), n('G4', 'e'), n('B4', 'e'), n('C5', 'h')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay armadura: la tonalidad es Do mayor y casi no hay alteraciones escritas.',
            'Los CIFRADOS vienen impresos: C, Em, F, Am, Dm y G. Son seis acordes en toda la canción.',
            'También trae la LETRA: úsala, te coloca el fraseo sola.',
            'Los cuatro primeros compases son de piano solo: la voz entra en el c. 4.',
            'La izquierda no toca ni una nota rápida: todo son blancas y redondas.',
            'Hay barra de repetición: la estrofa se toca dos veces con letra distinta.',
            'Un compás lleva DOS acordes y el siguiente solo uno: ese hueco es donde respira la voz.',
        ],
        reto='Contar. La izquierda va tan despacio que no marca ningún pulso, y la melodía entra casi '
             'siempre después de un silencio. Si no llevas la cuenta por dentro, la voz se te adelanta '
             'o se te retrasa y no hay nada en la partitura que te avise.',
        truco='Estudia con el metrónomo puesto MUY flojo, solo marcando el uno de cada compás, y canta '
              'la letra en voz alta mientras tocas la izquierda. Cuando la letra encaje sola, quita el '
              'metrónomo y añade la derecha.',
        sabias='Billie Eilish y su hermano Finneas la escribieron para la película de Barbie en dos '
               'días, después de ver un montaje sin acabar. Ganó el Oscar a la mejor canción original '
               'en 2024. La grabaron casi entera en el dormitorio de él, como todo lo que hacen.',
        qr=dict(titulo='Escucha la original',
                texto='El piano toca poquísimo. Todo lo demás es silencio y voz.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta canción no pide velocidad: pide colocar '
              'tríadas limpias con la izquierda y entrar a tiempo con la derecha después de un silencio. '
              'Aquí se entrenan las dos cosas, en Do mayor.',
        reglas=['SIN ARMADURA · DO MAYOR', 'LAS TRES NOTAS, A LA VEZ', 'CUENTA LOS SILENCIOS'],
        ejercicios=[
            dict(num=1, titulo='Escala de Do mayor · dos octavas', clef='bass',
                 pista='manos separadas · sin alteraciones, pero el pulgar tiene que pasar limpio',
                 events=corch(['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4']) +
                        corch(['D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'C5']) +
                        corch(['C5', 'B4', 'A4', 'G4', 'F4', 'E4', 'D4', 'C4']) +
                        corch(['B3', 'A3', 'G3', 'F3', 'E3', 'D3', 'C3', 'C3']),
                 bars_per_line=4),
            dict(num=2, titulo='Las seis tríadas de la canción', clef='bass',
                 pista='C · Em · F · Am · Dm · G · las seis posiciones que hay que saberse de memoria',
                 events=[ac(DO), ac(MIm), ac(FA), ac(LAm), ac(REm), ac(SOL),
                         ac(DO, 'w')],
                 bars_per_line=4),
            dict(num=3, titulo='Tríadas por toda la escala', clef='bass',
                 pista='ahora por los siete grados · para que la mano no dependa de reconocer el cifrado',
                 events=[ac(('C3', 'E3', 'G3'), 'h'), ac(('D3', 'F3', 'A3'), 'h'),
                         ac(('E3', 'G3', 'B3'), 'h'), ac(('F3', 'A3', 'C4'), 'h'),
                         ac(('G3', 'B3', 'D4'), 'h'), ac(('A3', 'C4', 'E4'), 'h'),
                         ac(('B3', 'D4', 'F4'), 'h'), ac(('C4', 'E4', 'G4'), 'h'),
                         ac(('C3', 'E3', 'G3'), 'w')],
                 bars_per_line=5),
            dict(num=4, titulo='Entrar después del silencio',
                 pista='lo que hace la melodía casi siempre · cuenta el silencio en voz alta y entra',
                 events=[sil('h'), n('G4'), n('B4'),
                         sil('h'), n('C5'), n('B4'),
                         sil(), n('G4'), n('B4'), n('C5'),
                         n('B4', 'w')],
                 bars_per_line=4),
            dict(num=5, titulo='La misma tríada, rota',
                 pista='el acorde nota a nota, para oír las tres por separado antes de juntarlas',
                 events=corch(['C4', 'E4', 'G4', 'E4', 'E4', 'G4', 'B4', 'G4']) +
                        corch(['F4', 'A4', 'C5', 'A4', 'C4', 'E4', 'G4', 'C4']),
                 bars_per_line=4),
            dict(num=6, titulo='Notas largas, contadas',
                 pista='la melodía de esta canción vive en redondas · aguántalas hasta el final',
                 events=[n('G4', 'w'), n('B4', 'w'), n('C5', 'w'), n('A4', 'w'),
                         n('G4', 'w'), n('E4', 'w'), n('F4', 'w'), n('E4', 'w')],
                 bars_per_line=8),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y sin armadura. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · no hay armadura, así que no hay trampas',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DE LAS TRÍADAS (CLAVE DE FA)',
        chuleta_pitches=['C3', 'E3', 'G3', 'B3', 'D4', 'F4'],
        chuleta_nombres=['Do', 'Mi', 'Sol', 'Si', 'Re', 'Fa'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa', clef='bass',
                 pista='donde viven las tríadas · el orden está desordenado a propósito',
                 events=[n(p) for p in ('C3', 'G3', 'E3', 'B3', 'F3', 'D4', 'A3', 'C4',
                                        'D3', 'F4', 'G2', 'E4', 'B2', 'A2', 'C3', 'G3')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · registro medio, casi todo entre Mi4 y Do5',
                 events=[n(p) for p in ('G4', 'C5', 'E4', 'B4', 'A4', 'F4', 'D5', 'G4',
                                        'E5', 'C4', 'B4', 'D4', 'F5', 'A4', 'G4', 'C5')]),
            dict(num=3, titulo='Leer la tríada entera', clef='bass',
                 pista='tres notas de golpe · nómbralas de abajo arriba antes de pasar a la siguiente',
                 events=[ac(DO, 'q'), ac(MIm, 'q'), ac(FA, 'q'), ac(LAm, 'q'),
                         ac(REm, 'q'), ac(SOL, 'q'), ac(DO, 'q'), ac(DO, 'q')],
                 bars_per_line=4),
        ],
        crono='¿Cuánto tardas en el ejercicio 3, diciendo las tres notas de cada acorde?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca una tríada suelta: MAYOR o MENOR. En esta canción se alternan sin avisar y '
                      'es lo que le da el color triste.'),
                ('B', 'Marca cuatro tiempos y toca una nota en uno de ellos. Que diga en cuál cayó: si '
                      'en el 1, el 2, el 3 o el 4.'),
                ('C', 'Toca dos acordes seguidos y que diga si el segundo sube o baja respecto al '
                      'primero, sin mirar.'),
                ('+', 'Y sin escribir: toca el bucle Do · Mi m · Fa y que lo cante encima.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=10, opciones=['M', 'm']),
                dict(letra='B', titulo='¿En qué tiempo cae?', pista='cuenta los cuatro por dentro',
                     n=8, opciones=['1', '2', '3', '4']),
                dict(letra='C', titulo='¿Sube o baja?', pista='del primer acorde al segundo',
                     n=6, opciones=['↑', '↓']),
            ],
        ),
    ),

    piano1=dict(
        intro='La partitura, abierta en trozos. La armonía no la he deducido yo: los cifrados vienen '
              'impresos. Lo que sí está medido nota por nota es el acorde de Fa y la melodía entera.',
        reglas=['LOS CIFRADOS VIENEN IMPRESOS', 'LA IZQUIERDA, MUY FLOJA', 'CUENTA LOS SILENCIOS'],
        bloques=[
            dict(num=1, titulo='El bucle de la estrofa', clef='bass',
                 pista='cifrados C · Em · F · el bucle que se repite cada dos compases',
                 sistemas=[dict(cap='dos acordes en el primer compás y uno sostenido en el segundo · '
                                    'nada más, y así casi toda la canción',
                                events=[ac(DO), ac(MIm), ac(FA, 'w'),
                                        ac(DO), ac(MIm), ac(FA, 'w')],
                                bars=4, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='SEIS ACORDES Y SE ACABÓ',
                 texto='Cuenta los cifrados de tu partitura: C, Em, F, Am, Dm y G. Seis, y cuatro de '
                       'ellos aparecen solo al final de las estrofas. Toda la canción se sostiene sobre '
                       'tres acordes dando vueltas. Eso quiere decir que la izquierda hay que '
                       'memorizarla, no leerla: cuando te sepas las seis posiciones, vas a poder mirar '
                       'solo la línea de arriba, que es donde de verdad pasan cosas.'),
            dict(num=2, titulo='Los acordes que rompen el bucle', clef='bass',
                 pista='cifrados Am · Dm · G · aparecen al final de la estrofa y avisan de que algo cambia',
                 sistemas=[dict(cap='fíjate en el salto de Fa a La menor: la mano sube entera, no cambia '
                                    'de forma',
                                events=[ac(LAm), ac(MIm), ac(FA, 'w'),
                                        ac(REm), ac(SOL), ac(DO, 'w')],
                                bars=4, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA IZQUIERDA SE ESCRIBE ASÍ',
                 texto='Dos acordes en un compás y uno solo en el siguiente. Parece un capricho, pero no '
                       'lo es: la voz canta encima y el piano se calla justo donde ella respira. Por eso '
                       'la izquierda alterna. Cuando toques, no rellenes ese segundo compás con nada: el '
                       'hueco está puesto a propósito y es la mitad del efecto de esta canción.'),
            dict(num=3, titulo='La melodía de la primera frase',
                 pista='cc. 4–6 · alturas medidas · el ritmo va simplificado a corcheas',
                 sistemas=[dict(cap='"I used to float, now I just fall down" · canta la letra mientras la '
                                    'lees y verás dónde respira',
                                events=[sil('h'), n('C5'), n('B4'),
                                        n('C5', 'h'), n('E4'), n('G4'),
                                        n('G4', 'h'), n('B4'), n('C5'),
                                        n('E4', 'h'), n('G4', 'h')],
                                bars=4)]),
            dict(num=4, titulo='Y la frase que cierra',
                 pista='cc. 7–9 medidos · baja Sol · Fa · Re · Mi · Fa y se queda ahí',
                 sistemas=[dict(cap='acaba en Fa, que no es la tónica: por eso la frase se queda '
                                    'colgando y quiere seguir',
                                events=[n('G4'), n('F4'), n('D4'), n('E4'),
                                        n('F4', 'h'), n('F4', 'h'),
                                        n('F4', 'h'), n('E4', 'h'),
                                        n('E4', 'w')],
                                bars=4)]),
            dict(num=5, titulo='El estribillo, que sube', clef='treble',
                 pista='cc. 18–19 medidos · aquí la melodía sube hasta el Mi5 y es lo más alto de la pieza',
                 sistemas=[dict(cap='sube por grados desde el Sol y llega arriba sin forzar: no la '
                                    'empujes, ya sube sola',
                                events=[n('B4'), n('G4'), n('G4'), n('A4'),
                                        n('B4', 'h'), n('C5', 'h'),
                                        n('B4'), n('E5'), n('B4'), n('A4'),
                                        n('G4', 'w')],
                                bars=4)]),
        ],
    ),

    piano2=dict(
        intro='Montarla es aprenderse seis posiciones de mano izquierda y después dedicarle todo el '
              'tiempo a contar. En esta canción los silencios ocupan más sitio que las notas.',
        reglas=['SEIS POSICIONES DE MEMORIA', 'LA LETRA MANDA', 'EL METRÓNOMO, MUY FLOJO'],
        bloques=[
            dict(num=5, titulo='Cambiar de acorde sin mirarse la mano', clef='bass',
                 pista='las seis posiciones encadenadas, una por compás · prepara la mano en el aire',
                 sistemas=[dict(cap='mira al techo mientras lo tocas: si tienes que mirarte los dedos, '
                                    'todavía no está',
                                events=[ac(DO, 'w'), ac(MIm, 'w'), ac(FA, 'w'), ac(LAm, 'w'),
                                        ac(REm, 'w'), ac(SOL, 'w'), ac(DO, 'w'), ac(DO, 'w')],
                                bars=8, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='LA LETRA ES EL METRÓNOMO',
                 texto='Esta edición trae la letra debajo del pentagrama. En una canción tan lenta y con '
                       'tantos silencios, es la única referencia fiable que tienes: cada sílaba cae en '
                       'un sitio exacto del compás. Canta "I used to float, now I just fall down" en voz '
                       'alta, sin tocar, hasta que te salga sin pensar. Después toca exactamente lo que '
                       'has cantado y no vas a necesitar contar.'),
            dict(num=6, titulo='Solo la fundamental de cada cifrado', clef='bass',
                 pista='quita el acorde y quédate con la nota de abajo · así se oye la forma entera',
                 sistemas=[dict(cap='Do · Mi · Fa · Do · Mi · Fa · La · Re · Sol · Do · esto es la '
                                    'canción, en diez notas',
                                events=[n('C3', 'w'), n('E3', 'w'), n('F3', 'w'),
                                        n('C3', 'w'), n('E3', 'w'), n('F3', 'w'),
                                        n('A3', 'w'), n('D3', 'w'), n('G3', 'w'), n('C3', 'w')],
                                bars=10, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='CÓMO ESTUDIARLA ESTA SEMANA',
                 texto='1 · Las seis posiciones, sin partitura, hasta que salgan de memoria. '
                       '2 · La letra cantada, sin piano, con el pie marcando el uno. '
                       '3 · La izquierda sola de la primera página, contando en voz alta. '
                       '4 · La derecha sola, entrando después de cada silencio. '
                       '5 · Las dos manos de los cc. 1 al 9 y ahí paras.'),
            dict(tipo='nota',
                 etiqueta='LOS CUATRO PRIMEROS COMPASES SON TUYOS',
                 texto='La voz no entra hasta el c. 4: los tres primeros compases son piano solo. Eso '
                       'quiere decir que ahí no hay nada que te tape ni nada con lo que encajar, y que '
                       'todo lo que se oiga mal se va a oír. Son tres acordes: móntalos como si fueran '
                       'el final de la canción y no el principio, porque es donde más se nota si la '
                       'mano llega tarde o si un dedo suena más fuerte que los otros.'),
            dict(tipo='escalera', valores=[50, 58, 64, 70, 74, 78],
                 regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='tracker', titulo='La prueba de la semana',
                 pie='Marca el día en que hayas tocado los seis acordes de memoria, sin mirar la hoja.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
