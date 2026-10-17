# -*- coding: utf-8 -*-
"""Himno de la alegría — pieza 1 de Jaume. Formato ADULTO (versión exigente).

   Lo leído sobre el PDF de su carpeta de Drive (Beethoven, arreglo de Gilbert
   DeBenedetti, edición Gradimi "Primer Level · C position", 1 página). El
   archivo es una imagen de 72 ppi, así que NO se puede medir con
   `medir_figuras`: se ha mirado a 100 y a 220 dpi, compás a compás.

     - 4/4 (la C de compás), sin armadura y sin tempo impreso. Va sin indicaciones de intensidad.
     - 16 compases en cuatro sistemas de cuatro.
     - La DIGITACIÓN va impresa en las dos manos, solo en el primer apoyo de
       cada frase y en los cambios de posición.
     - Derecha, cc. 1-4: Mi Mi Fa Sol · Sol Fa Mi Re · Do Do Re Mi · Mi Re Re(blanca).
       Los cc. 5-8 son los mismos, acabando en Re Do Do(blanca). Los cc. 13-16,
       iguales que los 5-8.
     - Izquierda: redondas de Do3 (dedo 5) y Sol3 (dedo 1). En los cc. 4, 8 y
       16 el compás se parte en dos blancas: Sol3 y Do3.
     - CC. 9-11 (el único trozo distinto): Re Re Mi Do · Re Mi-Fa Mi Do · Re Mi-Fa
       Mi Re, con las dos únicas parejas de CORCHEAS de la página.
     - C. 12: la derecha trae solo dos negras (Do, Re) y la izquierda un FA
       SOSTENIDO en blanca seguido de Sol en blanca: es la única tecla negra de
       la página.

   Primera pieza del álbum, y a propósito la más quieta: posición fija, sin
   armadura y con la digitación delante. Jaume tiene base musical, así que aquí
   no se trata de aprender las notas sino de **colocar la mano y no
   moverla**, y de **empezar a oír las dos manos como una sola cosa**.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, reto, plan, rodear, unir, colorear, acuerdate,
                       para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# La derecha y la izquierda tal como las trae su partitura (leídas a 220 dpi)
D_1_4 = [n('E4'), n('E4'), n('F4'), n('G4'), n('G4'), n('F4'), n('E4'), n('D4'),
         n('C4'), n('C4'), n('D4'), n('E4'), n('E4'), n('D4'), n('D4', 'h')]
I_1_4 = [n('C3', 'w'), n('G3', 'w'), n('C3', 'w'), n('G3', 'h'), n('C3', 'h')]

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=1, nivel='intermedio', slug='HimnoAlegria',
    formato='adulto',
    titulo_corto='Himno de la alegría', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source',
                           'Himno de la alegria'),
    yt='https://www.youtube.com/results?search_query=ode+to+joy+beethoven+piano+easy',

    ficha=dict(
        titulo='Himno de la alegría',
        autor='Beethoven · arreglo de Gilbert DeBenedetti',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Sin indicación'), ('Manos', 'Las dos, fija'),
               ('Páginas', 'Una')],
        titulo_ritmos='El final de la primera frase',
        pie_ritmos='La derecha son los cc. 3-4, donde la frase se cierra con la blanca, y la izquierda los '
                   'cc. 1-2, copiados de tu partitura. Los dedos están en tu partitura: apúntalos tú.',
        armonia=dict(
            titulo='La más quieta del cuaderno, y por eso la primera',
            tarjetas=[
                ('POSICIÓN FIJA', 'Ni un salto de mano',
                 'Dice "C position" arriba a la izquierda: la derecha en Do-Re-Mi-Fa-Sol y la '
                 'izquierda en Do y Sol. No se mueve nada de principio a fin.'),
                ('LA IZQUIERDA', 'Solo redondas',
                 'Do y Sol en redondas, con la digitación 5 y 1 impresa. En los cc. 4, 8 y 16 el '
                 'compás se parte en dos blancas, Sol y Do.'),
                ('LAS CORCHEAS', 'Solo dos parejas',
                 'En los cc. 10 y 11 aparecen las únicas corcheas de la página: Mi-Fa dentro de '
                 'una negra. Son el único trozo que no se parece a nada de antes.'),
                ('EL C. 12', 'La única tecla negra',
                 'La izquierda toca un Fa sostenido en blanca antes de volver al Sol. Es lo único '
                 'de la página que no está en las teclas blancas.'),
            ],
            pie='Con tu base, las notas no son el problema: la pieza se estudia por otra cosa. Se '
                'trata de que la mano derecha cante sin que la izquierda se oiga mecánica, y de '
                'que el c. 12 no sorprenda.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 3-4 · de tu partitura',
             [n('C4'), n('C4'), n('D4'), n('E4'), n('E4'), n('D4'), n('D4', 'h')],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'cc. 1-2 · de tu partitura',
             [n('C3', 'w'), n('G3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Pone "C position": las dos manos tocan sin salirse de cinco teclas.',
            'No lleva armadura ni tempo impreso: la velocidad la eliges tú.',
            'La digitación está impresa en las dos manos: 3 en el primer Mi, 5 y 1 en la izquierda.',
            'Dieciséis compases: la primera frase se repite, y lo único distinto son los cc. 9-12.',
            'En los cc. 10 y 11 hay dos parejas de corcheas, las únicas de toda la página.',
            'En el c. 12 la izquierda toca un Fa sostenido, la única tecla negra de la pieza.',
        ],
        reto='Tocarla sin que se note que la izquierda no sabe qué hacer: redondas limpias, '
             'aguantadas hasta el final del compás y sin pegar el golpe.',
        truco='Toca primero la izquierda sola contando cuatro, y la derecha encima solo cuando la '
              'izquierda ya no necesita tu atención. Si la redonda se te corta cuando cambia la '
              'derecha, vas todavía demasiado deprisa para ti.',
        sabias='Beethoven escribió la melodía para el último movimiento de su Novena Sinfonía, '
               'estrenada en 1824, sobre un poema de Schiller. En 1972 el Consejo de Europa la '
               'adoptó como himno, y desde 1985 es también el himno de la Unión Europea.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo se alarga la última nota de cada frase: esa blanca es la única '
                      'que respira. Cántala antes de tocarla.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí no hay nada que no sepas leer. Lo que se estudia es la mano quieta, la '
              'redonda de la izquierda y los dos únicos sitios donde la página cambia de aspecto.',
        reglas=['LA MANO NO SE MUEVE', 'LA IZQUIERDA AGUANTA', 'DOS SITIOS NUEVOS'],
        bloques=[
            dict(num=1, titulo='La izquierda sola, cuatro compases',
                 pista='cc. 1-4 · literal de tu partitura · dedos 5 y 1 impresos', clef='bass',
                 sistemas=[
                     dict(cap='a) cuenta cuatro en voz alta y no levantes el dedo hasta el cuatro · '
                              'en el c. 4 la redonda se parte en dos blancas',
                          events=I_1_4, bars=4, clef='bass'),
                 ]),
            dict(num=2, titulo='La derecha sola: la frase entera',
                 pista='cc. 1-4 · literal · el Mi del c. 1 lleva el dedo 3 impreso',
                 sistemas=[
                     dict(cap='a) cántala con los nombres de las notas antes de tocarla · si la '
                              'cantas bien, la mano ya sabe dónde ir',
                          events=D_1_4, bars=4),
                 ]),
            dict(num=3, titulo='Las dos manos, primera frase',
                 pista='cc. 1-4 · literal · la izquierda aguanta mientras la derecha cuenta',
                 sistemas=[
                     dict(cap='a) sin pedal y sin prisa · la nota grave tiene que seguir sonando '
                              'cuando la derecha ya va por la tercera',
                          events=[ac(('C3', 'E4')), n('E4'), n('F4'), n('G4'),
                                  ac(('G3', 'G4')), n('F4'), n('E4'), n('D4'),
                                  ac(('C3', 'C4')), n('C4'), n('D4'), n('E4'),
                                  ac(('G3', 'E4')), n('D4'), ac(('C3', 'D4'), 'h')],
                          bars=4, manos='sostiene'),
                 ]),
            dict(tipo='nota',
                 etiqueta='LO ÚNICO DISTINTO: LOS CC. 9 A 12',
                 texto='La primera frase se repite al final, así que solo estos cuatro compases son '
                       'nuevos. En el 10 y el 11 hay una pareja de corcheas dentro de la tercera '
                       'negra, y en el 12 la izquierda toca un Fa sostenido. Estudia esto aparte, '
                       'antes que la pieza entera.'),
            dict(num=4, titulo='Las corcheas de los cc. 10 y 11',
                 pista='cc. 10-11 · literal · Mi-Fa son dos notas dentro de UN golpe',
                 sistemas=[
                     dict(cap='a) dilo en voz alta: "uno, dos-y, tres, cuatro" · las dos corcheas '
                              'ocupan lo mismo que una negra',
                          events=[n('D4'), n('E4', 'e'), n('F4', 'e'), n('E4'), n('C4'),
                                  n('D4'), n('E4', 'e'), n('F4', 'e'), n('E4'), n('D4')],
                          bars=2),
                 ]),
            dict(num=5, titulo='El Fa sostenido del c. 12',
                 pista='cc. 9-12 de la izquierda · literal · la blanca con sostenido y luego Sol',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) tres redondas de Sol y el compás del Fa sostenido · el sostenido '
                              'va delante de la nota y vale solo para ese compás',
                          events=[n('G3', 'w'), n('G3', 'w'), n('G3', 'w'),
                                  n('F#3', 'h'), n('G3', 'h')],
                          bars=4, clef='bass'),
                 ]),
            dict(num=6, titulo='Las dos manos del trozo nuevo',
                 pista='cc. 9-11 · literal · la izquierda es un Sol de redonda en cada compás',
                 sistemas=[
                     dict(cap='a) vuelve a empezar por la frase de las corcheas · primero muy '
                              'despacio, y sin que la redonda se mueva cuando entran las '
                              'corcheas',
                          events=[ac(('G3', 'D4')), n('D4'), n('E4'), n('C4'),
                                  ac(('G3', 'D4')), n('E4', 'e'), n('F4', 'e'), n('E4'), n('C4'),
                                  ac(('G3', 'D4')), n('E4', 'e'), n('F4', 'e'), n('E4'), n('D4')],
                          bars=3, manos='sostiene'),
                 ]),
        ] + bloques_extra('Do mayor', 1, 'C4', 'C3',
                          'la posición fija: la mano no se mueve y el oído sí se mueve',
                          desde=7, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Himno de la alegría · para casa',
            intro='Veinte minutos al día. Es la pieza más quieta del cuaderno: se estudia por '
                  'limpieza, no por dificultad.',
            bloques=[
                reto('Tocar la izquierda con redondas completas, sin cortar ninguna antes del '
                     'cuatro.',
                     'Cuenta en voz alta y mira el reloj de la pared, no la mano. Si la redonda '
                     'se corta cuando cambia la derecha, la izquierda está esperando que le '
                     'toque la atención: dásela de golpe y se queda tranquila.'),
                plan((4, 'La izquierda sola, cc. 1-4, contando cuatro en voz alta'),
                     (5, 'La derecha sola, la frase entera cantando los nombres'),
                     (6, 'Las dos manos, de cuatro en cuatro compases'),
                     (5, 'Los cc. 10, 11 y 12 aparte, diez veces cada uno')),
                dict(rodear([[n('E4'), n('E4'), n('F4'), n('G4')],
                             [n('G4'), n('F4'), n('E4'), n('D4')],
                             [n('C4'), n('C4'), n('D4'), n('E4')],
                             [n('E4'), n('E4'), n('F4'), n('G4')]],
                            titulo='Rodea los dos compases que son iguales',
                            pista='son los cc. 1, 2, 3 y 5 de tu partitura · el pentagrama es '
                                  'nuestro, la partitura es la tuya'),
                     clef='treble'),
                unir([('"C position"', 'las dos manos no salen de cinco teclas'),
                      ('Redonda de la izquierda', 'se aguanta los cuatro golpes'),
                      ('Dos corcheas', 'ocupan lo mismo que una negra'),
                      ('Sostenido delante de la nota', 'vale solo para ese compás')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                colorear([n('D4'), n('E4', 'e'), n('F4', 'e'), n('E4'), n('C4'),
                          n('G3', 'w'), n('F#3', 'h'), n('G3', 'h')],
                         ['Las corcheas, de rojo.',
                          'Las blancas, de verde.',
                          'Las negras, de azul.'],
                         titulo='Colorea según la figura',
                         pista='salen de los cc. 10-12 · las redondas déjalas sin color'),
                acuerdate('La pieza no lleva tempo impreso: la velocidad la eliges tú. Elígela una '
                          'vez, apúntala a lápiz en la partitura y no la muevas en toda la '
                          'semana.',
                          etiqueta='ELIGE LA VELOCIDAD Y APÚNTALA'),
                para_clase('La pieza entera con las dos manos, y el número de metrónomo que '
                           'hayas elegido. Si el c. 12 te sigue descolocando, tráelo: se arregla '
                           'en cinco minutos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
