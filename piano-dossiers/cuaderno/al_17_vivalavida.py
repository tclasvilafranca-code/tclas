# -*- coding: utf-8 -*-
"""Viva la Vida (Coldplay) — pieza 17 de Alan. ADULTO exigente, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (Easy Piano, imagen a 56 ppp,
   mirada a 200 ppp). OJO: el PDF trae TRES páginas y la tercera está en blanco;
   para el álbum se genera una copia de las dos primeras (`_dos_paginas`).

     - Detrás de la clave no hay nada, pero hay sostenidos escritos delante de
       algunas notas (Fa♯ en los cc. 3, 15, 16 y 20). 4/4. No trae tempo ni intensidad.
     - 32 compases en dos páginas. Hay varias barras de repetición, la última con barra
       final. Notas ligadas entre compases.
     - Solo corcheas con silencios, negras, blancas con puntillo y redondas.
       Ninguna figura más corta que la corchea.
     - MEDIDO, mano izquierda (alturas medidas contra las líneas a 200 ppp):
       c. 1: Do3 · silencio · Do3 · silencio · Do3 · silencio · Do3 · Do3 (corcheas)
       c. 2: silencio · Re3 · silencio · Re3 · Re3 · silencio · Re3 · silencio
       c. 3: lo mismo que el c. 1 sobre Sol3
       c. 4: lo mismo que el c. 2 sobre Mi3
     - Mano derecha, cc. 1-4: un acorde de tres notas en blanca con puntillo, silencio
       de corchea y un acorde de corchea ligado a una redonda del compás siguiente.
   Las notas de la derecha no se distinguen con seguridad en este escaneo: lo que
   lleva notas va como ANDAMIO y solo se cita el ritmo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, reto, plan, metronomo, escribir, diferencias,
                      acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

ORIGEN = os.path.join(HERE, '..', 'students', 'alan', 'source', 'Viva la vida')
DOS = os.path.join(HERE, '..', 'students', 'alan', 'source', 'VIVA_LA_VIDA_2p.pdf')


def _dos_paginas(src, dst):
    """La partitura de Drive trae una tercera página en blanco: copia sin ella."""
    from pypdf import PdfReader, PdfWriter
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        return dst
    r = PdfReader(src)
    w = PdfWriter()
    for p in r.pages[:2]:
        w.add_page(p)
    with open(dst, 'wb') as f:
        w.write(f)
    return dst


if os.path.exists(ORIGEN):
    _dos_paginas(ORIGEN, DOS)


def ostinato(p, desfase=False):
    """MEDIDO: el dibujo de corcheas y silencios de la izquierda sobre la nota p."""
    if desfase:
        return [sil('e'), n(p, 'e'), sil('e'), n(p, 'e'), n(p, 'e'), sil('e'),
                n(p, 'e'), sil('e')]
    return [n(p, 'e'), sil('e'), n(p, 'e'), sil('e'), n(p, 'e'), sil('e'),
            n(p, 'e'), n(p, 'e')]


C1L = ostinato('C3')
C2L = ostinato('D3', True)
ACORDE = ('G4', 'B4', 'D5')

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=17, nivel='intermedio', slug='VivaLaVida',
    formato='adulto',
    titulo_corto='Viva la Vida', time_sig=(4, 4), key_sig=None,
    partitura=DOS,
    yt='https://www.youtube.com/results?search_query=viva+la+vida+coldplay+piano+easy',

    ficha=dict(
        titulo='Viva la Vida',
        autor='Coldplay · versión Easy Piano',
        datos=[('Tonalidad', 'Sin armadura'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Alteración', 'Fa sostenido'),
               ('Páginas', 'Dos')],
        titulo_ritmos='La izquierda, medida, y la derecha',
        pie_ritmos='Arriba, andamio sobre el ritmo de tu partitura: un acorde largo, un silencio y '
                   'otro acorde. Abajo, medido: las corcheas con silencios de los cc. 3 y 4.',
        armonia=dict(
            titulo='Una izquierda que no se detiene y una derecha que aguanta',
            tarjetas=[
                ('LA IZQUIERDA', 'Corcheas y silencios',
                 'Casi todo el cuaderno de la izquierda es el mismo dibujo: corchea, silencio, '
                 'corchea, silencio… En cada compás la nota cambia: Do3, Re3, Sol3, Mi3.'),
                ('LA DERECHA', 'Acordes largos',
                 'La derecha toca acordes de tres notas en blanca con puntillo y los liga con la '
                 'redonda del compás siguiente. Entra y se queda sonando.'),
                ('LAS REPETICIONES', 'Cuatro veces',
                 'Hay varias barras de repetición: se vuelve atrás, y a veces un compás es '
                 'distinto la segunda vez. Mira dónde están antes de empezar.'),
                ('EL SOSTENIDO', 'Fuera de la clave',
                 'Detrás de la clave no hay nada, pero delante de algunas notas aparece un Fa♯. '
                 'Vale solo hasta el final del compás: al siguiente hay que volver a mirar.'),
            ],
            pie='32 compases, dos páginas, y la sensación de que se toca sola: porque la izquierda '
                'es siempre el mismo dibujo. La dificultad es que no se acelere ni un compás.',
        ),
        ritmos=[
            ('MANO DERECHA', 'andamio · un acorde largo, silencio y otro acorde',
             [ac(ACORDE, 'h.'), sil('e'), ac(ACORDE, 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'cc. 3-4 · medido', ostinato('G3') + ostinato('E3', True), AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada, pero hay sostenidos escritos delante de las notas.',
            'El compás es 4/4 y no trae número de metrónomo.',
            'La izquierda toca corcheas con silencios, siempre el mismo dibujo.',
            'La nota de la izquierda cambia en cada compás: Do, Re, Sol, Mi.',
            'Hay barras de repetición y notas ligadas entre compases.',
            'El PDF de Drive trae una tercera página en blanco.',
        ],
        reto='Mantener el dibujo de la izquierda, corchea y silencio, sin que se acelere cuando '
             'la derecha cambia de acorde.',
        truco='Cuenta "uno-y-dos-y-tres-y-cuatro-y" y toca solo en las "y" o solo en los números, '
              'según el compás. Si la izquierda se te va, di las sílabas en voz alta.',
        sabias='El título viene de un cuadro de Frida Kahlo, "Viva la Vida", que pintó justo antes '
               'de morir. Coldplay la publicó en 2008 y fue de las primeras canciones con '
               'violines y timbales en llegar al número uno.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo la izquierda hace de reloj: corchea y silencio, siempre igual. '
                      'Eso es lo que tienes que conseguir con la mano, sin mirarla.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda manda: se aprende sola hasta que es automática, y la derecha se le '
              'pone encima. Los silencios son de la partitura: se cuentan.',
        reglas=['LA IZQUIERDA, PRIMERO Y SOLA', 'LOS SILENCIOS SE CUENTAN',
                'EL SOSTENIDO VALE UN COMPÁS'],
        bloques=[
            dict(num=1, titulo='El dibujo del c. 1, sobre el Do',
                 pista='c. 1 · medido sobre tu partitura · cuatro corcheas con silencio y dos '
                       'seguidas al final',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) corchea, silencio, corchea, silencio, corchea, silencio y dos '
                              'corcheas seguidas · cuenta "uno-y-dos-y-tres-y-cuatro-y"',
                          events=C1L, bars=1, clef='bass'),
                 ]),
            dict(num=2, titulo='El c. 2: el mismo dibujo, pero desplazado',
                 pista='c. 2 · medido sobre tu partitura · el silencio va delante y las notas caen '
                       'en el "y" de cada tiempo',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) silencio, Re, silencio, Re, Re, silencio, Re, silencio · el '
                              'silencio abre el compás: ahí no se toca',
                          events=C2L, bars=1, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA IZQUIERDA VA SOLA PRIMERO',
                 texto='El dibujo es el mismo en todos los compases y solo cambia la nota. Si lo '
                       'aprendes con la mano sola y el metrónomo, ya sabes la mitad de la pieza '
                       'entera. Después, la derecha solo tiene que sostener un acorde: el '
                       'trabajo duro ya está hecho.'),
            dict(num=3, titulo='Las cuatro notas, una por compás',
                 pista='cc. 1-4 · medidas sobre tu partitura · aquí en redondas, para verlas '
                       'seguidas',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) Do, Re, Sol y Mi · la nota que repite la izquierda en cada '
                              'compás de los cuatro primeros',
                          events=[n('C3', 'w'), n('D3', 'w'), n('G3', 'w'), n('E3', 'w')],
                          bars=4, clef='bass'),
                 ]),
            dict(num=4, titulo='El acorde de la derecha, ligado',
                 pista='cc. 1-2 · el ritmo es el de tu partitura · las notas son andamio',
                 sistemas=[
                     dict(cap='a) una blanca con puntillo, un silencio de corchea y un acorde de '
                              'corchea ligado a la redonda del compás siguiente · no se vuelve a '
                              'pulsar',
                          events=[ac(ACORDE, 'h.'), sil('e'), dict(ac(ACORDE, 'e'), lig=True),
                                  ac(ACORDE, 'w')],
                          bars=2),
                 ]),
            dict(num=5, titulo='El Fa♯ escrito delante de la nota',
                 pista='andamio · lo que hace una alteración que no está en la clave',
                 sistemas=[
                     dict(cap='a) un Mi, un Fa♯ y un Sol · el sostenido vale hasta la línea '
                              'divisoria y se anula en el compás siguiente',
                          events=[n('E4'), n('F#4'), n('G4'), n('F#4')], bars=1),
                 ]),
            dict(num=6, titulo='La barra de repetición',
                 pista='andamio · lo que dicen los dos puntos de la barra de tu partitura',
                 sistemas=[
                     dict(cap='a) dos compases con la barra de repetición al final · se vuelve al '
                              'principio y se toca otra vez',
                          events=[n('G4'), n('A4'), n('B4'), n('A4'), n('G4', 'h'), n('D4', 'h')],
                          bars=2, repetir='cierra'),
                 ]),
        ] + bloques_extra('Do mayor', 17, 'E4', 'C3',
                          'la izquierda constante mientras la derecha aguanta',
                          desde=7, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Viva la Vida · para casa',
            intro='Veinte minutos al día. Hoy el trabajo es de la izquierda: lo que sale solo en la '
                  'mano, sale solo en la pieza.',
            bloques=[
                reto('Tocar los cuatro primeros compases de la izquierda sin mirar y sin que '
                     'cambie la velocidad, tres veces seguidas.',
                     'Pon el metrónomo a 60 y apunta cuántas veces seguidas lo consigues sin '
                     'mirarte la mano. Si te aceleras, vuelves a cero.'),
                plan((6, 'La izquierda sola, cc. 1-4, sin mirar'),
                     (4, 'La derecha sola: los acordes largos y los silencios'),
                     (5, 'Las dos manos, cc. 1-4, despacio'),
                     (5, 'Las repeticiones: dónde empiezan y dónde acaban')),
                metronomo('Empieza a ♩ = 60 con la izquierda sola y sube de cuatro en cuatro '
                          'hasta que no tengas que pensarla.',
                          'Tu partitura no trae tempo: la meta la eliges tú y la apuntas a '
                          'lápiz.',
                          titulo='A qué velocidad te sale'),
                escribir(titulo='Copia el c. 1 de la izquierda',
                         pista='cuatro corcheas con silencios y dos corcheas seguidas · y escribe '
                               'debajo la nota que repite'),
                diferencias(list(C1L),
                            [n('C3', 'e'), sil('e'), n('C3', 'e'), n('C3', 'e'), n('C3', 'e'),
                             sil('e'), n('C3', 'e'), sil('e')],
                            cuantas=2,
                            titulo='Busca las diferencias',
                            pista='arriba, el c. 1 de tu partitura · abajo, el dibujo con los '
                                  'silencios cambiados de sitio'),
                acuerdate('Entre las notas hay silencios, y los silencios también se tocan: sin '
                          'ellos, la pieza no tiene ese aire. Cuéntalos en voz alta hasta que '
                          'la mano los respete sola.',
                          etiqueta='EL SILENCIO ES MÚSICA'),
                para_clase('La izquierda de los cc. 1-4 sin mirar y a la velocidad que has '
                           'elegido. Y dime cuál es el compás donde te cuesta más no acelerar: '
                           'empezamos por ahí.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
