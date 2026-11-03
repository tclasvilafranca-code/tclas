# -*- coding: utf-8 -*-
"""Romance, de Diabelli — pieza 2 de Alan (dueto). Formato ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive (free-scores.com, "6
   Sonatas for Piano 4-hands op. 163, no. 1, Mvmt. 2", 2 páginas), mirado a 110
   y a 220 dpi compás a compás:

     - ¢ (compás partido), sin armadura, "Andantino", "p dolce", "sempre
       legato". 24 compases, con barra de repetición al final del c. 8 y un
       calderón sobre el último acorde (c. 24).
     - **El 8va va encima de todo el Primo**, en las seis líneas de la pieza.
     - Los dos pentagramas del Primo van en clave de sol y escriben casi lo
       mismo (el de abajo se separa en los últimos compases, donde hace
       acordes). El Secondo, dos pentagramas en clave de fa: corcheas arriba y
       notas largas abajo.
     - MEDIDO (`medir_arranque`): el c. 1 de la derecha es **Mi5 blanca, La4
       negra, La4 negra**.
     - **Tiene alteraciones, y no pocas**: Do sostenido en el c. 6 y Si bemol
       en el c. 14 (con su becuadro en el c. 15) en el Primo, y Si bemol y Sol
       sostenido repartidos por el Secondo. Es lo que no se esperaría de una
       pieza "de cinco dedos".
     - Muchísima dinámica: p dolce, cresc., sf, f, mf, mp, pp y reguladores.
     - Notas pequeñas pegadas delante de la nota en los cc. 3, 7, 19, 20 y 21.

   El archivo es EL MISMO que el de Josep y José María (misma edición), así
   que lo literal coincide y lo inventado no puede coincidir: aquí el material
   de apoyo va por las alteraciones, la dinámica y el 8va.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, reto, plan, a_cuatro_manos, ordenar, nombres,
                       figuras, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=2, nivel='intermedio', slug='RomanceDiabelli',
    formato='adulto',
    titulo_corto='Romance · Diabelli', time_sig=(2, 2), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source',
                           'Romance 4 manos'),
    yt='https://www.youtube.com/results?search_query=diabelli+op+163+romance+piano+4+hands',

    ficha=dict(
        titulo='Romance',
        autor='Anton Diabelli · 6 Sonatinas a cuatro manos, op. 163 nº 1 · parte del Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', 'Partido (¢)'),
               ('Carácter', 'Andantino'), ('Manos', 'A la octava'),
               ('Páginas', 'Dos')],
        titulo_ritmos='El c. 1 en las dos manos',
        pie_ritmos='Arriba, medido sobre tu partitura: Mi5 de blanca y dos La4 de negra. Abajo, andamio: el '
                   'Secondo no es esto, pero así se lee. Los dedos, en tu partitura.',
        armonia=dict(
            titulo='Cinco dedos, sí, pero con sorpresas',
            tarjetas=[
                ('EL TÍTULO', 'Posición fija',
                 'La edición anuncia "Primo part for 5 fingers with stationary hand position". '
                 'Es verdad en lo esencial: la mano casi no se mueve de sitio en toda la pieza.'),
                ('LAS ALTERACIONES', 'Tres alteraciones',
                 'Un Do sostenido en el c. 6 y un Si bemol en el c. 14, que se anula con un '
                 'becuadro en el c. 15. Son las únicas notas fuera de la posición.'),
                ('LA DINÁMICA', 'Mucha dinámica',
                 'Empieza en "p dolce", crece, estalla en f, baja a mf y mp y se apaga en pp. La '
                 'mitad del trabajo es leer qué toca en cada compás.'),
                ('EL DÚO', 'Cuatro manos',
                 'Veinticuatro compases, con una barra de repetición al final del c. 8 y un '
                 'calderón en el último acorde. Se lee abierto, con el Secondo al lado.'),
            ],
            pie='Las notas no son el problema. El trabajo está en la sincronía con la '
                'otra persona y en que el crescendo no sea un golpe: es una curva de ocho compases.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido',
             [n('E5', 'h'), n('A4'), n('A4')], OCRE, 'treble', None),
            ('EL SECONDO', 'una nota larga debajo · andamio',
             [ac(('A2', 'E3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Pone "Andantino" y, al lado de la primera nota, "p dolce": flojo y dulce.',
            'El 8va va encima de todo el Primo: suena una octava más alto de lo escrito.',
            'Los dos pentagramas del Primo van en clave de sol y escriben casi lo mismo.',
            'Hay una barra de repetición al final del c. 8: se vuelve al principio una vez.',
            'Aparecen un Do sostenido (c. 6), un Si bemol (c. 14) y un becuadro (c. 15).',
            'Acaba con un calderón sobre el último acorde (c. 24).',
        ],
        reto='Sonar como una sola mano. En el Primo las dos manos escriben lo mismo, así que no '
             'hay nada que disimule el desajuste, y encima hay que compartir el pulso con otra '
             'persona.',
        truco='Toca el Primo con las dos manos fuerte y seco, sin pedal. Si ahí se oye un solo golpe, '
              'bájalo a "p dolce" y ya no se mueve. Después, con la otra persona, contad dos '
              'compases en voz alta antes de entrar: el pulso es de blanca.',
        sabias='Diabelli fue editor además de compositor. Mandó un vals suyo a cincuenta músicos de '
               'su época para que cada uno escribiera una variación; Beethoven no escribió una, '
               'escribió treinta y tres: son las Variaciones Diabelli.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el Primo solo y luego con el Secondo. La parte de abajo no acompaña '
                      'sin más: se apoya en las mismas frases y las contesta.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La mano se queda quieta y las dos hacen casi lo mismo, así que el trabajo es de '
              'precisión: las alteraciones, la dinámica y el pulso de blanca. Se estudia sola '
              'y después con el Secondo.',
        reglas=['LA MANO CASI NO SE MUEVE', 'LAS ALTERACIONES, ANTES QUE NADA',
                'LA DINÁMICA ES PARTE DE LA PIEZA'],
        bloques=[
            dict(num=1, titulo='El primer compás, tal como está escrito',
                 pista='c. 1 · MEDIDO sobre tu partitura · Mi5 de blanca y dos La4 de negra, '
                       'con el 8va encima',
                 sistemas=[
                     dict(cap='a) el c. 1 literal, dos veces seguidas · la blanca ocupa la mitad del '
                              'compás · fíjate en el 8va: suena una octava más alto de lo escrito',
                          events=[n('E5', 'h'), n('A4'), n('A4'),
                                  n('E5', 'h'), n('A4'), n('A4')],
                          bars=2, ottava=True, matiz='p'),
                     dict(cap='b) el mismo gesto empezando en otra nota · andamio para sentir el '
                              'salto de quinta hacia abajo en lugar de verlo',
                          events=[n('C5', 'h'), n('F4'), n('F4'),
                                  n('B4', 'h'), n('E4'), n('E4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Las tres alteraciones',
                 pista='cc. 6, 14 y 15 · el Do♯, el Si♭ y el becuadro · lo de abajo es andamio '
                       'para que la mano los conozca antes',
                 sistemas=[
                     dict(cap='a) el Do sostenido, de paso entre el Do y el Re · el sostenido '
                              'vale solo para ese compás',
                          events=[n('B4'), n('C#5'), n('D5', 'h'),
                                  n('D5'), n('C#5'), n('B4', 'h')],
                          bars=2),
                     dict(cap='b) el Si bemol, y el Si natural que lo desmiente · son dos teclas '
                              'distintas, una negra y una blanca',
                          events=[n('G4'), n('Bb4'), n('A4', 'h'),
                                  n('G4'), n('B4'), n('C5', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='MÁRCALAS ANTES DE TOCAR',
                 texto='Coge un lápiz y rodea en tu partitura las tres alteraciones del Primo: el '
                       'Do sostenido del c. 6, el Si bemol del c. 14 y el becuadro del c. 15. En '
                       'una pieza que parece de cinco dedos, lo que falla no es la mano: es que '
                       'se olvida que estaban.'),
            dict(num=3, titulo='La dinámica, de una en una',
                 pista='andamio · la pieza pasa de p dolce a f y vuelve a pp: son curvas, no escalones',
                 sistemas=[
                     dict(cap='a) de flojo a fuerte en dos compases · el crescendo no empieza al '
                              'principio del compás, empieza donde empieza la frase',
                          events=[n('D5', 'h'), n('E5'), n('E5'),
                                  n('F5', 'h'), n('G5'), n('F5')],
                          bars=2, matiz='p', cresc=6),
                     dict(cap='b) y bajando otra vez hasta el pianísimo · se apaga más despacio de '
                              'lo que ha subido',
                          events=[n('F5', 'h'), n('E5'), n('D5'),
                                  n('C5', 'h'), n('B4'), n('B4')],
                          bars=2, show_time=False, matiz='f', dim=6),
                 ]),
            dict(num=4, titulo='Parar sobre el último acorde',
                 pista='c. 24 · el calderón del final · acorde de Sol mayor desplegado, andamio',
                 sistemas=[
                     dict(cap='a) tres compases y el acorde final con calderón · el calderón se '
                              'alarga lo que pida el Secondo, no lo que pida tu mano',
                          events=[n('D5'), n('G5'), n('B4'), n('G5'),
                                  n('D5'), n('G5'), n('B4'), n('G5'),
                                  ac(('G4', 'B4', 'D5'), 'w')],
                          bars=3, matiz='pp', calderon=True),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA CON LA OTRA PERSONA',
                 texto='Con el Secondo al lado, la regla es una sola: entráis juntos y sale '
                       'mejor si la que lleva el pulso es la mano de abajo. Contad en voz alta '
                       'un compás de silencio antes de empezar, de dos en dos, y no os miréis las '
                       'manos: miraos solo en el calderón.'),
        ] + bloques_extra('Do mayor', 52, 'C5', 'C3',
                          'compás de dos blancas: se cuenta de dos, no de cuatro',
                          desde=5, time_sig=(2, 2)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Romance · para casa',
            intro='Veinte minutos al día. Esta semana no hay velocidad que ganar: hay que entrar '
                  'limpio y con las alteraciones sabidas.',
            bloques=[
                reto('Tocar los ocho primeros compases con las dos manos exactamente juntas y con '
                     'las dos alteraciones del c. 6 y del c. 14 a la primera.',
                     'Tócalos a media velocidad, fuerte y seco. Si en el c. 6 la mano se ha ido '
                     'al Do natural, no es la mano: es que no has mirado la partitura antes de '
                     'tocar.'),
                plan((4, 'El c. 1 con el 8va: las dos manos, diez veces'),
                     (5, 'Los cc. 1-8, derecha sola y luego izquierda sola'),
                     (6, 'Las dos juntas, de cuatro en cuatro compases'),
                     (5, 'Con la otra persona, solo el principio y el final')),
                a_cuatro_manos('Antes de tocar nada, acordad tres cosas: quién cuenta el compás '
                               'de entrada, a qué velocidad vais y quién espera en el calderón '
                               'del final. Se decide en voz alta y se apunta a lápiz en el '
                               'margen, para no volver a discutirlo.'),
                ordenar(['Con la otra persona, desde el principio hasta el calderón.',
                         'Marcar a lápiz las tres alteraciones del Primo.',
                         'Cada mano sola, los ocho primeros compases.',
                         'Las dos manos juntas, fuerte y seco, a media velocidad.'],
                        titulo='El orden de los cuatro pasos',
                        pista='numéralos del 1 al 4 · el orden importa'),
                nombres(['E5', 'A4', 'G4', 'C5', 'D5', 'B4', 'A4'],
                        titulo='Las notas del primer compás y sus vecinas',
                        pista='la primera y la segunda son las del c. 1 de tu partitura'),
                figuras([('h', 'blanca'), ('q', 'negra'), ('w', 'redonda'), ('e', 'corchea')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='y ojo: aquí el pulso va a la blanca, no a la negra'),
                para_clase('Los ocho primeros compases con las dos manos, y los tres sitios donde '
                           'se te desajustan con la otra persona. Si en algún compás fallas '
                           'siempre, tráelo marcado.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
