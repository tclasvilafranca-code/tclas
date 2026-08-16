# -*- coding: utf-8 -*-
"""What Was I Made For? (canción 4 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico); la medición se importa de
   `dilan_13_what`. Ver TRANSCRIPCION_D12_14.md.

   Camino distinto al de Dilan:

     - A Dilan se le entra por los SEIS ACORDES, que son pocos y se memorizan.
     - A Eva se le entra por el SILENCIO. En esta canción los huecos ocupan
       más sitio que las notas, y el fallo tipico no es tocar mal un acorde:
       es rellenar el compas que hay que dejar vacio. Por eso el paso 1 no
       tiene ni una nota de melodia — solo el esqueleto del tiempo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_13_what import n, ac, sil, corch, DO, MIm, FA, LAm, REm, SOL

HERE = os.path.dirname(__file__)
DOM = 'Do mayor'
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Eva', num=4, nivel='avanzado', slug='WhatWasIMadeFor',
    titulo_corto='What Was I Made For?', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'what-was-i-made-for-billie-eilish.pdf'),
    yt='https://www.youtube.com/results?search_query=billie+eilish+what+was+i+made+for',

    ficha=dict(
        titulo='What Was I Made For?',
        autor='Billie Eilish y Finneas O’Connell · de «Barbie» (2023)',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'), ('Tempo', '♩=78'),
               ('Mano izq.', '1–2 acordes por compás'), ('Acordes', '6')],
        armonia=dict(
            titulo='Seis acordes, y mucho hueco',
            tarjetas=[
                ('EL BUCLE', 'C · Em · F',
                 'Dos acordes en un compás y uno solo en el siguiente. Así casi toda la canción.'),
                ('LOS QUE ROMPEN', 'Am · Dm · G',
                 'Aparecen solo al final de la estrofa, y avisan de que algo cambia.'),
                ('EL HUECO', 'el compás que se calla',
                 'No es un descanso: la voz respira ahí. Rellenarlo se carga la canción.'),
            ],
            pie='Los cifrados vienen impresos en la edición. La armonía no hay que deducirla: hay que '
                'leerla, y después memorizarla para poder mirar solo la línea de arriba.',
        ),
        especial=[
            'No hay armadura: ni un sostenido ni un bemol en la clave.',
            'La izquierda alterna dos acordes en un compás y uno solo en el siguiente.',
            'La voz no entra hasta el c. 4: los tres primeros compases son piano solo.',
            'La melodía llega al Mi5 en el estribillo, y es la nota más alta de la pieza.',
            'La frase de la estrofa acaba en Fa, que no es la tónica: por eso queda colgando.',
            'La edición trae la letra debajo del pentagrama, sílaba a sílaba.',
            'Los cifrados vienen impresos: C, Em, F, Am, Dm y G. Seis en toda la canción.',
        ],
        ritmos=[
            ('MI', 'dos acordes en el compás, y el siguiente se calla',
             [ac(DO, 'h'), ac(MIm, 'h'), ac(FA, 'w')], OCRE, 'bass', None),
            ('MD', 'entra después del silencio, nunca en el uno',
             [sil('h'), n('C5'), n('B4')], AZUL, 'treble', None),
        ],
        reto='Contar. En esta canción los silencios ocupan más sitio que las notas, y el error típico '
             'no es tocar mal un acorde: es rellenar el compás que hay que dejar vacío.',
        truco='Estudia primero solo el tiempo, sin melodía: toca el acorde donde toca y cuenta en voz '
              'alta el compás que se calla. Cuando el hueco te resulte natural, la canción está medio '
              'montada. Y usa la letra impresa: cada sílaba cae en un sitio exacto.',
        sabias='La escribieron Billie Eilish y su hermano Finneas para la película «Barbie», y ganó el '
               'Óscar en 2024. Está en Do mayor —la tonalidad más neutra que existe— y aun así suena '
               'triste: lo que la pone triste no son los acordes, son los silencios.',
        qr=dict(titulo='Escucha la original',
                texto='Cuenta los compases en los que el piano no toca nada. Son casi la mitad.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Aquí los huecos ocupan más sitio que las notas. Por eso el paso 1 no lleva ni una nota '
              'de melodía: es solo el esqueleto del tiempo, para que el compás que se calla deje de '
              'dar miedo. Los cifrados vienen impresos, así que la armonía se lee, no se deduce.',
        reglas=['SIN ARMADURA', 'EL HUECO NO SE RELLENA', 'CUENTA EN VOZ ALTA'],
        bloques=[
            dict(num=1, titulo='Solo el tiempo, sin melodía', clef='bass',
                 pista='cuenta en voz alta los cuatro tiempos del compás que se calla',
                 sistemas=[
                     dict(cap='a) el bucle de la estrofa · dos acordes en un compás y uno en el otro',
                          events=[ac(DO), ac(MIm), ac(FA, 'w'),
                                  ac(DO), ac(MIm), ac(FA, 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) y los que rompen el bucle, al final de la estrofa · fíjate en el '
                              'salto de Fa a La menor: la mano sube entera, no cambia de forma',
                          events=[ac(LAm), ac(MIm), ac(FA, 'w'),
                                  ac(REm), ac(SOL), ac(DO, 'w')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL HUECO ESTÁ PUESTO A PROPÓSITO',
                 texto='Dos acordes en un compás y uno solo en el siguiente parece un capricho, pero no '
                       'lo es: la voz canta encima y el piano se calla justo donde ella respira. Cuando '
                       'toques, no rellenes ese segundo compás con nada. Ese silencio es la mitad del '
                       'efecto de la canción, y es lo que la gente recuerda de ella.'),
            dict(num=2, titulo='La forma entera, en diez notas', clef='bass',
                 pista='quita el acorde y quédate con la fundamental de cada cifrado',
                 sistemas=[
                     dict(cap='a) Do · Mi · Fa · Do · Mi · Fa · La · Re · Sol · Do — esto es la canción',
                          events=[n('C3', 'w'), n('E3', 'w'), n('F3', 'w'),
                                  n('C3', 'w'), n('E3', 'w'), n('F3', 'w'),
                                  n('A3', 'w'), n('D3', 'w'), n('G3', 'w'), n('C3', 'w')],
                          bars=10, clef='bass'),
                     dict(cap='b) y las seis posiciones encadenadas, una por compás · mira al techo '
                              'mientras las tocas: si tienes que mirarte los dedos, todavía no están',
                          events=[ac(DO, 'w'), ac(MIm, 'w'), ac(FA, 'w'), ac(LAm, 'w'),
                                  ac(REm, 'w'), ac(SOL, 'w')],
                          bars=6, clef='bass', show_time=False),
                     dict(cap='c) las mismas seis, en blancas y de dos en dos · es el paso previo a '
                              'meterlas en el compás de la canción',
                          events=[ac(DO, 'h'), ac(MIm, 'h'), ac(FA, 'h'), ac(LAm, 'h'),
                                  ac(REm, 'h'), ac(SOL, 'h'), ac(DO, 'h'), ac(DO, 'h')],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='d) y el bucle entero de la estrofa, ocho compases sin parar · el hueco '
                              'de los compases pares se cuenta, no se rellena',
                          events=[ac(DO), ac(MIm), ac(FA, 'w'),
                                  ac(DO), ac(MIm), ac(FA, 'w'),
                                  ac(LAm), ac(MIm), ac(FA, 'w'),
                                  ac(REm), ac(SOL), ac(DO, 'w')],
                          bars=8, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='El tiempo y la armonía ya están. Ahora entra la melodía, que en esta canción va pegada '
              'a la letra: cada sílaba cae en un sitio exacto del compás, y esa es la única referencia '
              'fiable que tienes.',
        reglas=['LA LETRA ES EL METRÓNOMO', 'ENTRA DESPUÉS DEL SILENCIO', 'EL METRÓNOMO, MUY FLOJO'],
        bloques=[
            dict(num=3, titulo='La melodía, frase por frase',
                 pista='cc. 4–9 · alturas medidas · el ritmo va simplificado a corcheas',
                 sistemas=[
                     dict(cap='a) «I used to float, now I just fall down» · canta la letra mientras la '
                              'lees y verás dónde respira',
                          events=[sil('h'), n('C5'), n('B4'),
                                  n('C5', 'h'), n('E4'), n('G4'),
                                  n('G4', 'h'), n('B4'), n('C5'),
                                  n('E4', 'h'), n('G4', 'h')],
                          bars=4),
                     dict(cap='b) la frase que cierra · acaba en Fa, que no es la tónica: por eso se '
                              'queda colgando y quiere seguir',
                          events=[n('G4'), n('F4'), n('D4'), n('E4'),
                                  n('F4', 'h'), n('F4', 'h'),
                                  n('F4', 'h'), n('E4', 'h'),
                                  n('E4', 'w')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA LETRA ES EL METRÓNOMO',
                 texto='En una canción tan lenta y con tantos silencios, la letra impresa es la única '
                       'referencia fiable que tienes: cada sílaba cae en un sitio exacto del compás. '
                       'Canta «I used to float, now I just fall down» en voz alta, sin tocar, hasta que '
                       'te salga sin pensar. Después toca exactamente lo que has cantado y no vas a '
                       'necesitar contar.'),
            dict(num=4, titulo='El estribillo, que sube al Mi5',
                 pista='cc. 18–19 medidos · es la nota más alta de la pieza, y no hay que empujarla',
                 sistemas=[
                     dict(cap='a) sube por grados desde el Sol y llega arriba sin forzar',
                          events=[n('B4'), n('G4'), n('G4'), n('A4'),
                                  n('B4', 'h'), n('C5', 'h'),
                                  n('B4'), n('E5'), n('B4'), n('A4'),
                                  n('G4', 'w')],
                          bars=4),
                     dict(cap='b) y las mismas notas en blancas · el salto al Mi5 se prepara mirando, '
                              'no se busca con el dedo',
                          events=[n('B4', 'h'), n('G4', 'h'), n('G4', 'h'), n('A4', 'h'),
                                  n('B4', 'h'), n('C5', 'h'), n('B4', 'h'), n('E5', 'h'),
                                  n('B4', 'h'), n('A4', 'h'), n('G4', 'w')],
                          bars=6, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LOS TRES PRIMEROS COMPASES SON TUYOS',
                 texto='La voz no entra hasta el c. 4: los tres primeros son piano solo. Ahí no hay '
                       'nada que te tape, y todo lo que suene mal se va a oír. Son tres acordes: '
                       'móntalos como si fueran el final de la canción y no el principio, porque es '
                       'donde más se nota si la mano llega tarde o si un dedo suena más que los otros.'),
            dict(tipo='escalera', valores=[50, 58, 64, 70, 74, 78],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
