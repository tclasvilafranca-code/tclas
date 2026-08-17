# -*- coding: utf-8 -*-
"""Little Miss Muffet (canción 10 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive (mfiles.co.uk, arr. Jim
   Paterson, 1 pagina):

     - FA MAYOR: un bemol, o sea que todos los Si van en la tecla negra.
     - LO NUEVO: compas de 6/8. Hay seis notas cortas en cada compas pero NO
       se cuentan seis: se cuentan DOS, agrupandolas de tres en tres. Se ve en
       la partitura porque las notas cortas van unidas de tres en tres.
     - La melodia del principio, medida: Sol · La · Sol · Si · Si | La · Sol ·
       Fa · Do · La.
     - La izquierda hace un vaiven que se repite: una nota grave y otra mas
       arriba, alternando (Do · Sol · Do · Sol).
     - Encima vienen las letras de los acordes: F, C, B b.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import n, ac, sil, corch, rutina, juego, escribir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'

CANCION = dict(
    alumno='Arnau', num=10, nivel='iniciación', slug='LittleMissMuffet',
    formato='corto', titulo_corto='Little Miss Muffet',
    time_sig=(6, 8), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Little Miss Muffet.pdf'),
    yt='https://www.youtube.com/results?search_query=little+miss+muffet+piano',

    ficha=dict(
        titulo='Little Miss Muffet',
        autor='Canción popular · arr. Jim Paterson (mfiles)',
        datos=[('Novedad', 'Compás de 6/8'), ('Se cuenta', 'En dos'),
               ('Teclas negras', 'Los Si'), ('Mano izq.', 'Vaivén'),
               ('Extras', 'Letras encima')],
        armonia=dict(
            titulo='Seis notas por compás, pero se cuentan dos',
            tarjetas=[
                ('EL 6/8', 'Seis cortas',
                 'En cada compás caben seis notas cortas. Van unidas de tres en tres.'),
                ('SE CUENTA EN DOS', 'Un... dos...',
                 'El pie marca solo dos veces por compás, una por cada grupito de tres.'),
                ('LA IZQUIERDA', 'Un vaivén',
                 'Una nota grave y otra más arriba, alternando. Siempre el mismo dibujo.'),
                ('EL BEMOL', 'Todos los Si',
                 'Otra vez la tecla negra. Ya te la sabes de otras canciones.'),
            ],
            pie='Un compás de 6/8 se cuenta en DOS, no en seis. Si cuentas seis, todas las notas pesan '
                'igual y la canción suena a marcha; contando dos, sale sola ese balanceo de canción de '
                'cuna que es lo que la hace bonita.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='El primer compás de cada mano. Fíjate en cómo las notas cortas van de tres en tres.',
        ritmos=[
            ('LA DERECHA', 'seis notas cortas, unidas de tres en tres',
             corch(['G4', 'A4', 'G4'], 3) + corch(['Bb4', 'A4', 'G4'], 3), AZUL, 'treble', FA),
            ('LA IZQUIERDA', 'el vaivén: una abajo y otra arriba',
             [n('C3', 'q.'), n('G3', 'q.')], OCRE, 'bass', FA),
        ],
        especial=[
            'Hay UN BEMOL detrás de la clave: todos los Si van en la tecla negra.',
            'El compás es de 6/8: seis notas cortas por compás.',
            'Se cuenta en DOS, no en seis: el pie marca dos veces.',
            'Las notas cortas van unidas de tres en tres, y eso te dice dónde están los dos golpes.',
            'La izquierda hace siempre el mismo vaivén: grave, arriba, grave, arriba.',
            'Encima del pentagrama hay letras: son los acordes.',
            'Las dos manos solo coinciden dos veces por compás, en los golpes.',
            'La canción se repite: la segunda mitad se parece mucho a la primera.',
        ],
        reto='No contar seis. Es lo que sale solo cuando ves seis notas, y en cuanto lo haces la '
             'canción pierde el balanceo y suena a desfile. Contar dos con seis notas dentro es lo '
             'único que hay que aprender aquí.',
        truco='Di «man-za-na, man-za-na» mientras tocas: cada palabra es un grupito de tres, y el '
              'golpe cae en el MAN. Camina por la habitación diciéndolo, y verás que das dos pasos por '
              'compás sin pensarlo.',
        sabias='La canción cuenta que a Miss Muffet, mientras comía sentada en un taburete, se le '
               'sentó al lado una araña y salió corriendo. Es de 1805 y en Inglaterra se la saben todos '
               'los niños, como aquí «Que llueva, que llueva».',
        qr=dict(titulo='Escúchala',
                texto='Marca DOS golpes con el pie, no seis. Verás que encaja solo.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Lo nuevo de esta canción es cómo se cuenta. Hay seis notas cortas en cada compás pero '
              'solo dos golpes, así que lo primero es aprender a contar dos, y las notas después.',
        reglas=['SE CUENTA EN DOS, NO EN SEIS', 'DI “MAN-ZA-NA”', 'LOS SI, EN LA TECLA NEGRA'],
        bloques=[
            dict(num=1, titulo='Primero, contar en dos',
                 pista='seis notas cortas por compás, agrupadas de tres en tres · el golpe cae en la primera',
                 sistemas=[
                     dict(cap='a) seis notas iguales · aprieta un poquito más la primera de cada grupo',
                          events=corch(['F4', 'G4', 'A4'], 3) + corch(['F4', 'G4', 'A4'], 3) +
                                 corch(['F4', 'G4', 'A4'], 3) + corch(['A4', 'G4', 'F4'], 3),
                          bars=2),
                     dict(cap='b) y ahora solo las dos que llevan el golpe · esto es lo que marca el pie',
                          events=[n('F4', 'q.'), n('F4', 'q.'), n('F4', 'q.'), n('A4', 'q.')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='POR QUÉ SE CUENTA EN DOS',
                 texto='Fíjate en la partitura: las notas cortas no van sueltas ni de dos en dos, van '
                       'unidas de TRES en tres. Eso es una pista que te está dando el papel: cada '
                       'grupito es un golpe. Como hay dos grupitos por compás, hay dos golpes. Si '
                       'cuentas seis, estás contando notas en vez de golpes.'),
            dict(num=2, titulo='La melodía del principio',
                 pista='medida en tu partitura · Sol · La · Sol · Si · Si, y después baja',
                 sistemas=[
                     dict(cap='a) tal como está escrita · di “man-za-na” en cada grupo de tres',
                          events=corch(['G4', 'A4', 'G4'], 3) + corch(['Bb4', 'Bb4', 'A4'], 3) +
                                 corch(['G4', 'F4', 'C5'], 3) + corch(['A4', 'G4', 'F4'], 3),
                          bars=2),
                     dict(cap='b) y las mismas notas en figuras largas, para verlas sin prisa',
                          events=[n('G4', 'q.'), n('Bb4', 'q.'), n('G4', 'q.'), n('A4', 'q.')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda: el vaivén', clef='bass',
                 pista='medido · una grave y otra más arriba, siempre igual',
                 sistemas=[
                     dict(cap='a) abajo, arriba, abajo, arriba · como una cuna que se balancea',
                          events=[n('C3', 'q.'), n('G3', 'q.'), n('C3', 'q.'), n('G3', 'q.')],
                          bars=2, clef='bass'),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE JUNTAN LAS DOS MANOS',
                 texto='Las dos manos coinciden solo en los dos golpes de cada compás: ahí bajan a la '
                       'vez. Todo lo demás que hace la derecha cae en medio, mientras la izquierda '
                       'espera. Empieza tocando SOLO los dos golpes con las dos manos, y cuando eso '
                       'salga, rellena la derecha con las notas de en medio.'),
        ],
    ),

    deberes=[
        dict(titulo='Deberes · semana 1', esquina='Little Miss Muffet · para hacer en casa',
             intro='Esta semana toca aprender a contar en dos aunque veas seis notas.',
             bloques=[
                 dict(tipo='nombres', num=1, titulo='¿Cómo se llama cada nota?',
                      pista='ojo con los Si: en esta canción son tecla negra',
                      notas=['G4', 'A4', 'Bb4', 'F4', 'C5', 'A4', 'G4', 'F4']),
                 dict(tipo='figuras', num=2, titulo='¿Cuántos golpes dura cada una?',
                      pista='escribe el número en la caja',
                      figuras=[('q.', 'negra con puntito'), ('q', 'negra'),
                               ('h', 'blanca'), ('w', 'redonda')]),
                 dict(tipo='dibuja', num=3, titulo='Dibuja tú las notas',
                      pista='solo el óvalo, sin el palito',
                      nombres=['Sol', 'La', 'Si', 'Do', 'La', 'Sol', 'Fa', 'Do']),
                 dict(tipo='colorea', num=4, titulo='Colorea la primera nota de cada grupo de tres',
                      pista='son las que llevan el golpe, las que marca el pie',
                      eventos=corch(['G4', 'A4', 'G4'], 3) + corch(['Bb4', 'A4', 'G4'], 3),
                      leyenda=['Cada grupito de tres notas es UN golpe.',
                               'Como hay dos grupitos, hay dos golpes por compás.']),
                 rutina('Caminar por casa diciendo “man-za-na” en cada paso',
                        'Seis notas cortas por compás, marcando la primera de cada tres',
                        'La izquierda sola: el vaivén, veinte veces'),
                 juego('Camina por el pasillo mientras quien esté contigo cuenta «man-za-na, man-za-na». '
                       'Tienes que dar un paso en cada MAN. Después al revés. Cuando lo tengas en los '
                       'pies, lo tienes en las manos: es exactamente el mismo balanceo.'),
             ]),
        dict(titulo='Deberes · semana 2', esquina='Little Miss Muffet · para hacer en casa',
             intro='Esta semana toca juntar las manos, que en esta canción coinciden solo dos veces '
                   'por compás.',
             bloques=[
                 dict(tipo='rodea', num=1, titulo='Rodea los dos compases que son iguales',
                      pista='fíjate en las notas de una en una',
                      compases=[[n('G4', 'q.'), n('Bb4', 'q.')],
                                [n('A4', 'q.'), n('F4', 'q.')],
                                [n('G4', 'q.'), n('Bb4', 'q.')],
                                [n('C5', 'q.'), n('A4', 'q.')]]),
                 dict(tipo='nombres', num=2, titulo='Otra vez los nombres, a ver si te los sabes',
                      pista='sin mirar los deberes de la semana pasada',
                      notas=['F4', 'Bb4', 'D5', 'G4', 'C5', 'E4', 'A4', 'F4']),
                 dict(tipo='une', num=3, titulo='Une cada cosa con lo que quiere decir',
                      pista='una raya de un punto al otro',
                      pares=[('El 6 y el 8 de la clave', 'todos los Si, tecla negra'),
                             ('Las notas unidas de tres en tres', 'seis notas cortas por compás'),
                             ('El bemol del principio', 'cada grupito es un golpe')]),
                 dict(tipo='colorea', num=4, titulo='Colorea las notas que suben',
                      pista='la melodía sube y baja como una ola, no da saltos',
                      eventos=corch(['G4', 'A4', 'Bb4'], 3) + corch(['A4', 'G4', 'F4'], 3),
                      leyenda=['Subir es ir a una nota que está más arriba en el papel.',
                               'En esta canción casi todo son escalones de uno en uno.']),
                 dict(tipo='nota', etiqueta='ACUÉRDATE',
                      texto='Las dos manos solo coinciden dos veces por compás. Todo lo demás lo hace '
                            'la derecha sola mientras la izquierda espera. Así que junta primero esos '
                            'dos golpes y rellena después.'),
                 rutina('Solo los dos golpes de cada compás, con las dos manos',
                        'La derecha entera, diciendo “man-za-na”',
                        'Los cuatro primeros compases con las dos manos'),
                 escribir(4),
             ]),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
