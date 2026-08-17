# -*- coding: utf-8 -*-
"""Puff the Magic Dragon (canción 12 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive (arr. Eric Moore, descarga de
   Musescore, 1 pagina):

     - Do mayor (nada detras de la clave) y compas de 4/4.
     - La melodia empieza repitiendo el Do de arriba cuatro veces, y despues
       baja al Fa y al Mi. Medido: Do·Do·Do·Do | Do·Do | Fa·Fa·Sol·Fa |
       Mi·Sol·Do·Do·Do.
     - LO NUEVO: la mano izquierda toca acordes de TRES notas a la vez, y muy
       largos: uno por compas, que dura los cuatro golpes.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import n, ac, sil, corch, rutina, juego, escribir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Arnau', num=12, nivel='iniciación', slug='PuffDragon',
    formato='corto', titulo_corto='Puff the Magic Dragon',
    time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'puff-the-magic-dragon.pdf'),
    yt='https://www.youtube.com/results?search_query=puff+the+magic+dragon+piano',

    ficha=dict(
        titulo='Puff the Magic Dragon',
        autor='Peter, Paul and Mary · arreglo de Eric Moore',
        datos=[('Teclas', 'Solo blancas'), ('Golpes', '4 por compás'),
               ('Novedad', 'Acordes de tres'), ('Mano izq.', 'Uno por compás'),
               ('Mano dcha.', 'La melodía')],
        armonia=dict(
            titulo='Tres teclas a la vez con una mano',
            tarjetas=[
                ('LO NUEVO', 'Tres notas',
                 'La izquierda ya no toca dos teclas: toca tres a la vez, en un solo golpe.'),
                ('DURAN MUCHO', 'Un compás',
                 'Cada acorde dura los cuatro golpes. Se toca una vez y se deja sonar.'),
                ('LA MELODÍA', 'Repite y baja',
                 'Empieza diciendo cuatro veces el mismo Do y después baja al Fa.'),
                ('LOS DEDOS', '5 · 3 · 1',
                 'Para tres teclas se usan el meñique, el corazón y el pulgar. Los otros descansan.'),
            ],
            pie='Un acorde de tres notas no es más difícil que uno de dos: es la misma mano abierta, '
                'solo que con un dedo más apoyado. Lo que hay que conseguir es que las tres teclas '
                'bajen exactamente a la vez, y eso se mira, no se toca deprisa.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='El primer compás de cada mano. Arriba, la melodía; abajo, el acorde entero.',
        ritmos=[
            ('LA DERECHA', 'cuatro veces la misma nota',
             [n('C5'), n('C5'), n('C5'), n('C5')], AZUL, 'treble', None),
            ('LA IZQUIERDA', 'tres teclas a la vez, todo el compás',
             [ac(('C3', 'E3', 'G3'), 'w')], OCRE, 'bass', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'La izquierda toca TRES teclas a la vez.',
            'Cada acorde dura el compás entero: se toca una vez y se deja.',
            'La melodía empieza repitiendo cuatro veces la misma nota.',
            'La canción es larga pero repite mucho: hay pocos acordes distintos.',
        ],
        reto='Que las tres teclas del acorde suenen a la vez. Si una baja un pelín antes que las '
             'otras, en vez de un acorde se oye un ruidito y luego el acorde. Y con tres dedos pasa '
             'más que con dos.',
        truco='Coloca los tres dedos encima de las teclas SIN apretar, mira que estén los tres bien '
              'puestos, y entonces deja caer la mano entera de golpe, como si fuera una sola pieza. No '
              'aprietes con los dedos: deja caer el brazo.',
        sabias='La canción cuenta la historia de un dragón que se queda solo cuando el niño con el que '
               'jugaba se hace mayor. Es de 1963 y la escribió un estudiante a partir de un poema; '
               'durante años la gente dijo que hablaba de otras cosas y los autores siempre lo negaron.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que el piano toca un acorde y lo deja sonar mucho rato.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Lo nuevo aquí son los acordes de tres notas de la izquierda. Se aprenden mirando la '
              'mano, no tocando deprisa: colocar, comprobar, y dejar caer.',
        reglas=['LAS TRES TECLAS, A LA VEZ', 'COLOCA Y MIRA ANTES DE TOCAR', 'DEJA SONAR'],
        bloques=[
            dict(num=1, titulo='Los acordes de la izquierda', clef='bass',
                 pista='medido · uno por compás, y dura los cuatro golpes',
                 sistemas=[
                     dict(cap='a) coloca los tres dedos, míralos, y deja caer la mano entera',
                          events=[ac(('C3', 'E3', 'G3'), 'w'), ac(('F2', 'A2', 'C3'), 'w'),
                                  ac(('C3', 'E3', 'G3'), 'w'), ac(('G2', 'B2', 'D3'), 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) y ahora cambiando cada dos golpes · prepara la mano en el aire antes '
                              'de que llegue el siguiente',
                          events=[ac(('C3', 'E3', 'G3'), 'h'), ac(('F2', 'A2', 'C3'), 'h'),
                                  ac(('G2', 'B2', 'D3'), 'h'), ac(('C3', 'E3', 'G3'), 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE TOCAN TRES TECLAS A LA VEZ',
                 texto='No se aprietan tres dedos: se deja caer la mano entera. Pon el meñique, el '
                       'corazón y el pulgar encima de sus teclas sin hacer fuerza, comprueba con los '
                       'ojos que están los tres bien colocados, y entonces suelta el peso del brazo. '
                       'Si te sale un ruidito antes del acorde, es que un dedo iba por libre.'),
            dict(num=2, titulo='La melodía',
                 pista='medida en tu partitura · cuatro veces la misma nota y después baja',
                 sistemas=[
                     dict(cap='a) Do · Do · Do · Do, y otra vez · las cuatro son la misma tecla',
                          events=[n('C5'), n('C5'), n('C5'), n('C5'),
                                  n('C5'), n('C5'), n('A4', 'h')],
                          bars=2),
                     dict(cap='b) y lo que sigue · baja al Fa y vuelve a subir al Do',
                          events=[n('F4'), n('F4'), n('G4'), n('F4'),
                                  n('E4'), n('G4'), n('C5'), n('C5')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Y ahora las dos manos',
                 pista='la izquierda toca una vez por compás y la derecha va por encima',
                 sistemas=[
                     dict(cap='a) esto es lo que hace la derecha mientras el acorde suena debajo',
                          events=[n('C5'), n('C5'), n('C5'), n('C5'),
                                  n('A4'), n('G4'), n('F4', 'h')],
                          bars=2),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE JUNTAN',
                 texto='Las dos manos coinciden solo en el primer golpe de cada compás: ahí bajan a la '
                       'vez. Después la izquierda se queda quieta aguantando y la derecha sigue sola. '
                       'Así que junta primero ese golpe, párate, y sigue solo con la derecha. Cuando '
                       'salga, ya está la canción entera.'),
        ],
    ),

    deberes=[
        dict(titulo='Deberes · semana 1', esquina='Puff the Magic Dragon · para hacer en casa',
             intro='Esta semana toca aprender los acordes de tres notas. Todo lo de aquí está en tu '
                   'partitura.',
             bloques=[
                 dict(tipo='nombres', num=1, titulo='¿Cómo se llama cada nota?',
                      pista='escríbelas en la cajita de debajo',
                      notas=['C5', 'A4', 'G4', 'F4', 'E4', 'G4', 'B4', 'C5']),
                 dict(tipo='figuras', num=2, titulo='¿Cuántos golpes dura cada una?',
                      pista='los acordes de esta canción son redondas: los más largos',
                      figuras=[('w', 'redonda'), ('h', 'blanca'), ('q', 'negra'),
                               ('h.', 'blanca con puntito')]),
                 dict(tipo='dibuja', num=3, titulo='Dibuja tú las notas',
                      pista='solo el óvalo, sin el palito',
                      nombres=['Do', 'La', 'Sol', 'Fa', 'Mi', 'Sol', 'Do', 'Fa']),
                 dict(tipo='une', num=4, titulo='Une cada dedo con lo que hace en el acorde',
                      pista='una raya de un punto al otro',
                      pares=[('El meñique (5)', 'la nota de en medio'),
                             ('El corazón (3)', 'la nota de arriba'),
                             ('El pulgar (1)', 'la nota de abajo')]),
                 rutina('Colocar los tres dedos, mirar, y dejar caer la mano: veinte veces',
                        'Los cuatro acordes seguidos, uno por compás',
                        'La melodía sola, los cuatro primeros compases'),
                 juego('Toca un acorde de tres notas y quien esté contigo dice si ha sonado UNA vez o '
                       'si ha oído un ruidito antes. Cinco veces. Es el oído de otra persona el que te '
                       'dice si las tres teclas bajaron juntas: tú desde dentro no lo notas.'),
             ]),
        dict(titulo='Deberes · semana 2', esquina='Puff the Magic Dragon · para hacer en casa',
             intro='Esta semana toca juntar las manos y darse cuenta de que hay pocos acordes '
                   'distintos.',
             bloques=[
                 dict(tipo='rodea', num=1, titulo='Rodea los dos compases que son iguales',
                      pista='fíjate en las notas de una en una',
                      compases=[[n('C5'), n('C5'), n('C5'), n('C5')],
                                [n('F4'), n('F4'), n('G4'), n('F4')],
                                [n('C5'), n('C5'), n('C5'), n('C5')],
                                [n('E4'), n('G4'), n('C5'), n('C5')]]),
                 dict(tipo='nombres', num=2, titulo='Otra vez los nombres, a ver si te los sabes',
                      pista='sin mirar los deberes de la semana pasada',
                      notas=['G4', 'C5', 'E4', 'A4', 'F4', 'D5', 'B4', 'C5']),
                 dict(tipo='colorea', num=3, titulo='Colorea las notas que se repiten',
                      pista='esta melodía dice cuatro veces la misma nota antes de moverse',
                      eventos=[n('C5'), n('C5'), n('C5'), n('C5'),
                               n('A4'), n('G4'), n('F4', 'h')],
                      leyenda=['Repetir la misma tecla es lo más fácil que hay.',
                               'Lo que cuesta es que el acorde de abajo llegue a tiempo.']),
                 dict(tipo='nota', etiqueta='ACUÉRDATE',
                      texto='El acorde se toca UNA vez por compás. No hay que repetirlo cada vez que '
                            'la derecha toca una nota: se deja sonar y ya. Si lo repites, la canción '
                            'suena a martillo.'),
                 rutina('El primer golpe de cada compás con las dos manos',
                        'La melodía entera con la derecha sola',
                        'Los cuatro primeros compases con las dos manos'),
                 juego('Toca un acorde y déjalo sonar sin volver a tocarlo. Quien esté contigo cuenta '
                       'en voz alta hasta que deje de oírse. Probad con el acorde muy fuerte y muy '
                       'flojo: verás que el fuerte dura más. Por eso el primer golpe del compás hay '
                       'que darlo con ganas.', 'esta vez de aguantar'),
                 escribir(4),
             ]),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
