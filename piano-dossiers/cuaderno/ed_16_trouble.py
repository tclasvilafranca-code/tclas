# -*- coding: utf-8 -*-
"""Trouble — pieza 16 de Eduard. Formato ADULTO. PRIMERA DE LOS RETOS.

   Lo comprobado sobre el PDF de su carpeta (Coldplay, arreglo de Unai Karam,
   4 páginas; el mismo archivo que la pieza 16 de José María, byte a byte):

     - SOL MAYOR: un sostenido detrás de la clave. Todos los Fa a la tecla
       negra. Ya la conoces de las piezas 9 y 10.
     - Compás de 4/4 y ♩ = 138 impreso.
     - Las letras de los acordes vienen impresas encima (G, Em, Bm…).
     - Son CUATRO PÁGINAS: la pieza más larga del cuaderno junto con
       Interstellar.

   Por qué está en el bloque de los retos: no por las notas, que están en una
   tonalidad conocida, sino por la combinación de velocidad (138) y longitud
   (cuatro páginas). Eso es resistencia, y la resistencia se entrena por
   trozos.

   El dosier ACOTA el trabajo a la primera página, y lo dice en el objetivo y
   en un recuadro. No es dejar la pieza a medias: es la única forma de que
   cuatro páginas acaben saliendo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from ed_comun import (n, ac, sil, corch, plan, metronomo, nombres, colorear,
                      escribir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=16, nivel='iniciación',
    slug='Trouble', formato='adulto',
    titulo_corto='Trouble', time_sig=(4, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source', 'Trouble.'),
    yt='https://www.youtube.com/results?search_query=coldplay+trouble+piano',

    ficha=dict(
        titulo='Trouble',
        autor='Coldplay · arreglo de Unai Karam',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 138'), ('Páginas', 'Cuatro'),
               ('Esta semana', 'La primera')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Sol mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. La armadura ya la conoces de las piezas 9 y 10.',
        armonia=dict(
            titulo='Empieza el bloque de los retos',
            tarjetas=[
                ('LO QUE NO ES NUEVO', 'Sol mayor',
                 'La misma armadura que Grandfather\'s Clock y Shallow. Ni una tonalidad nueva en las '
                 'cuatro últimas piezas del curso: es a propósito.'),
                ('LO QUE SÍ', 'La resistencia',
                 'Cuatro páginas a ♩ = 138. La dificultad no está en ningún compás concreto: está en '
                 'llegar al final sin desmontarse.'),
                ('CÓMO SE COME', 'Por páginas',
                 'Esta semana, la primera página y solo la primera. Las otras tres llegan cuando esta '
                 'salga entera y sin pararse.'),
                ('EL CIFRADO', 'G, Em, Bm',
                 'Las letras de encima son los acordes. Aquí sirven además para orientarte cuando te '
                 'pierdas: te dicen dónde estás sin tener que contar compases.'),
            ],
            pie='Las cuatro últimas piezas del curso son las difíciles, y ninguna trae tonalidad ni '
                'figura nueva. Lo que traen es cantidad: más páginas, más velocidad, más rato '
                'seguido. Eso no se aprende, se entrena.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, en corcheas · andamio',
             corch(['A4', 'F#4']) + corch(['E4', 'D4']) + corch(['E4', 'F#4']) +
             corch(['A4', 'D4']), OCRE, 'treble', SOL),
            ('MANO IZQUIERDA', 'notas largas, una o dos por compás · andamio',
             [ac(('D3', 'A3'), 'h'), ac(('B2', 'F#3'), 'h')], AZUL, 'bass', SOL),
        ],
        especial=[
            'Hay UN sostenido detrás de la clave: todos los Fa a la tecla negra.',
            'Pone ♩ = 138: es rápida.',
            'Son cuatro páginas, la más larga del cuaderno junto con Interstellar.',
            'Las letras de los acordes vienen impresas encima del pentagrama.',
            'La tonalidad es la misma que la de las piezas 9 y 10: no hay nada nuevo que aprender ahí.',
            'El trabajo de esta semana es SOLO la primera página.',
        ],
        reto='Llegar al final. No hay ningún compás imposible en esta pieza: lo que falla es la '
             'concentración a partir del minuto y medio, y eso pasa aunque las notas estén sabidas.',
        truco='Estudia por páginas y en orden inverso: empieza por el final de la página, no por el '
              'principio. Así los compases que más veces tocas son los del final, que son justo los '
              'que siempre salen peor porque se llega cansado. Es el truco más útil de todo el '
              'cuaderno y sirve para cualquier pieza larga.',
        sabias='Es de "Parachutes", el primer disco de Coldplay, grabado cuando todavía eran cuatro '
               'estudiantes de Londres. La escribieron sobre un piano vertical desafinado del estudio, '
               'y el sonido de ese piano es el que se oye en la grabación: no lo cambiaron.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo el primer minuto: es lo que vas a tocar esta semana.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza no se estudia entera. Se estudia por páginas, y cada página empezando por '
              'el final. Suena raro y es lo que hace que las piezas largas acaben saliendo: los '
              'compases del final son los que menos se tocan y los que peor salen.',
        reglas=['ESTA SEMANA, SOLO LA PRIMERA PÁGINA', 'DE ATRÁS HACIA ADELANTE',
                'LA VELOCIDAD, LA ÚLTIMA'],
        bloques=[
            dict(num=1, titulo='La melodía de la primera página',
                 pista='andamio en Sol mayor · el dibujo es el de tu partitura',
                 sistemas=[
                     dict(cap='a) primero en negras, la mitad de rápido y con las mismas notas',
                          events=[n('E4'), n('D4'), n('C4'), n('D4'),
                                  n('E4'), n('G4'), n('E4'), n('C4')],
                          bars=2, key_sig=SOL),
                     dict(cap='b) y ahora en corcheas · si te cansas antes de acabar el compás, ve más '
                              'lento',
                          events=corch(['E4', 'D4']) + corch(['C4', 'D4']) +
                                 corch(['E4', 'G4']) + corch(['E4', 'C4']),
                          bars=1, key_sig=SOL, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='ESTUDIAR DE ATRÁS HACIA ADELANTE',
                 texto='Divide la página en cuatro trozos y numéralos. Estudia el 4, luego el 3 y el 4 '
                       'seguidos, luego el 2, 3 y 4, y por último la página entera. Así el final se '
                       'toca cuatro veces más que el principio, que es exactamente al revés de lo que '
                       'pasa cuando se estudia empezando siempre por arriba. Pruébalo una semana y ya '
                       'no vuelves a estudiar de otra forma.'),
            dict(num=2, titulo='La izquierda, que aquí descansa', clef='bass',
                 pista='andamio en Sol mayor · notas largas, una o dos por compás',
                 sistemas=[
                     dict(cap='a) dos apoyos por compás y a esperar',
                          events=[ac(('D3', 'A3'), 'h'), ac(('B2', 'F#3'), 'h'),
                                  ac(('G2', 'D3'), 'h'), ac(('A2', 'E3'), 'h')],
                          bars=2, clef='bass', key_sig=SOL),
                     dict(cap='b) y con uno solo por compás, que es como está en varios sitios',
                          events=[ac(('D3', 'A3'), 'w'), ac(('B2', 'F#3'), 'w'),
                                  ac(('G2', 'D3'), 'w'), ac(('A2', 'E3'), 'w')],
                          bars=4, clef='bass', key_sig=SOL, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, cuatro compases',
                 pista='andamio · con metrónomo, y a la velocidad que salga limpia',
                 sistemas=[
                     dict(cap='a) la derecha encima de la izquierda · si tienes que parar a pensar, '
                              'baja el metrónomo',
                          events=corch(['E4', 'D4']) + corch(['C4', 'D4']) +
                                 [n('E4'), n('G4')] +
                                 corch(['E4', 'D4']) + corch(['C4', 'B3']) +
                                 [n('C4', 'h')],
                          bars=2, key_sig=SOL),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · dos apoyos por compás y '
                              'nada más: aquí no es ella la que cansa',
                          events=[ac(('D3', 'A3'), 'h'), ac(('B2', 'F#3'), 'h'),
                                  ac(('G2', 'D3'), 'h'), ac(('A2', 'E3'), 'h')],
                          bars=2, clef='bass', key_sig=SOL, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Trouble · para casa',
            intro='Veinte minutos al día, y SOLO la primera página. Las otras tres no son de esta '
                  'semana.',
            bloques=[
                plan((3, 'Numerar la primera página en cuatro trozos, con lápiz'),
                     (6, 'El trozo 4, luego el 3 y el 4 seguidos'),
                     (6, 'El 2, 3 y 4 seguidos'),
                     (5, 'La página entera, despacio y sin parar')),
                metronomo('Empieza donde la página entera salga sin pararte.',
                          'La meta son 138, pero primero es no pararse. Sube de cinco en cinco.'),
                nombres(['E4', 'D4', 'C4', 'G4', 'B3', 'A3', 'F#4', 'E4'],
                        titulo='Los nombres, con la armadura puesta',
                        pista='ojo con el Fa: en esta pieza lleva sostenido'),
                colorear([n('E4'), n('D4'), n('C4', 'h'), n('D4'),
                          n('E4'), n('G4', 'h'), n('E4'), n('C4')],
                         ['Un color para las de un golpe y otro para las de dos.'],
                         titulo='Colorea según lo que duran',
                         pista='dos colores'),
                escribir(titulo='Copia el compás que peor te salga',
                         pista='con su armadura · y luego tócalo cinco veces'),
                para_clase('La primera página entera, sin pararte, a la velocidad que sea. Y con '
                           'qué número del metrónomo lo has conseguido.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
