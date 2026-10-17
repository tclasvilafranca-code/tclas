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
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         crucigrama, diferencias, adivinar, teclado, palmas,
                         nombres, camino, acuerdate)

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

    # Reparto de `arnau_recetas`: semana 1 la R13 (crucigrama · diferencias ·
    # adivina) y semana 2 la R14 (teclado · palmas · nombres · camino).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Puff the Magic Dragon · para hacer en casa',
            intro='Lo nuevo: la izquierda toca tres notas a la vez. Un acorde por compás.',
            bloques=[
                crucigrama('LARGO', [
                    ('BLANCA', 1, 'La figura hueca que dura dos golpes.'),
                    ('DRAGON', 2, 'El bicho del que habla esta canción.'),
                    ('TRES', 1, 'Las notas que suenan a la vez en cada acorde.'),
                    ('GOLPES', 0, 'Hay cuatro en cada compás de esta canción.'),
                    ('REDONDA', 3, 'La figura que dura cuatro golpes.'),
                ], cierre='Las casillas grises dicen cómo son los acordes de tu mano izquierda.'),
                diferencias(
                    [n('C5'), n('C5'), n('C5'), n('C5'), n('F4'), n('F4'), n('G4')],
                    [n('C5'), n('C5'), n('B4'), n('C5'), n('F4'), n('G4'), n('G4', 'h')],
                    cuantas=3,
                    titulo='Busca las tres diferencias',
                    pista='el de arriba es el principio de tu melodía · el de abajo tiene trampas'),
                adivinar([('Somos tres notas y sonamos todas a la vez.', 'ACORDE'),
                          ('Duro los cuatro golpes del compás enteros.', 'REDONDA'),
                          ('Yo llevo la melodía en esta canción.', 'DERECHA')],
                         titulo='Adivina quién soy',
                         pista='una letra en cada casilla'),
                rutina('El acorde de tres notas, apretando las tres a la vez',
                       'La melodía sola, muy despacio',
                       'Las dos manos, los dos primeros compases'),
                juego('Toca un acorde y quien esté contigo dice si han sonado las tres a la vez.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Puff the Magic Dragon · para hacer en casa',
            intro='Esta semana se empieza en el teclado y se acaba con un camino de acordes.',
            bloques=[
                teclado({0: 1, 2: 2, 4: 3, 7: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'La 1, la 2 y la 3 son las tres del primer acorde de tu izquierda.'],
                        titulo='En el teclado',
                        pista='las tres primeras suenan a la vez'),
                palmas([('DRA-GON', 2), ('PU-FF', 2), ('MA-GI-CO', 3)],
                       titulo='El ritmo de las palabras',
                       pista='dilo en voz alta y escríbelo con figuras en la caja'),
                nombres(['C5', 'A4', 'G4', 'F4', 'E4', 'G4', 'B4', 'C5'],
                        pista='son las notas de tu melodía · escríbelas debajo'),
                camino([['una', 'tres', 'dos', 'una', 'dos', 'una'],
                        ['dos', 'tres', 'tres', 'dos', 'una', 'dos'],
                        ['una', 'dos', 'tres', 'una', 'dos', 'tres'],
                        ['dos', 'una', 'tres', 'tres', 'una', 'dos']],
                       titulo='El camino de los acordes',
                       pista='colorea solo donde dice “tres”, que es cuando suena un acorde'),
                acuerdate('Un acorde de tres notas no se toca de una en una: se aprieta con los tres '
                          'dedos a la vez, como cuando coges un vaso. Colócalos encima de las teclas '
                          'sin apretar, mira que estén bien, y luego baja la mano entera.',
                          etiqueta='LAS TRES A LA VEZ'),
                rutina('Los acordes de la izquierda, uno detrás de otro',
                       'La melodía entera con la derecha sola',
                       'Las dos manos, cuatro compases sin parar'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
