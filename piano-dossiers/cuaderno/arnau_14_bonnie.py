# -*- coding: utf-8 -*-
"""My Bonnie Lies Over the Ocean (canción 14 de Arnau, iniciación). CORTO.

   Medido sobre el PDF de su carpeta de Drive (arr. Gilbert DeBenedetti,
   "Level Two", 1 pagina):

     - Do mayor, compas de 3/4, y pone "Slowly, longingly".
     - Es la primera del cuaderno marcada como "Level Two": las otras eran
       Primer Level o Level One.
     - LO NUEVO, y esta escrito en la partitura con esas palabras:
         · "shift" en varios sitios -> la mano CAMBIA DE SITIO en el teclado.
           Hasta ahora la mano se colocaba una vez y no se movia.
         · "l.h. over" al final -> la mano izquierda pasa POR ENCIMA de la
           derecha para tocar mas arriba.
     - La melodia empieza bajando: Mi · Re · Do, y despues Re · Do.
     - La digitacion viene impresa en las dos manos, y en la izquierda salen
       los numeros 1, 2, 3, 4 y 5.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         crucigrama, contar, unir, acuerdate, camino, adivinar,
                         rodear, teclado)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Arnau', num=14, nivel='iniciación', slug='MyBonnie',
    formato='corto', titulo_corto='My Bonnie Lies Over the Ocean',
    time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'MyBonnie.pdf'),
    yt='https://www.youtube.com/results?search_query=my+bonnie+lies+over+the+ocean+piano',

    ficha=dict(
        titulo='My Bonnie Lies Over the Ocean',
        autor='Canción popular · arreglo de Gilbert DeBenedetti · «Level Two»',
        datos=[('Novedad', 'La mano se mueve'), ('Golpes', '3 por compás'),
               ('Y también', 'Cruce de manos'), ('Teclas', 'Solo blancas'),
               ('Carácter', 'Slowly')],
        armonia=dict(
            titulo='La primera vez que la mano cambia de sitio',
            tarjetas=[
                ('SHIFT', 'Cambia de sitio',
                 'Esa palabra está escrita en tu partitura: ahí la mano entera se muda de posición.'),
                ('L.H. OVER', 'La izquierda cruza',
                 'Al final, la izquierda pasa por encima de la derecha para tocar más arriba.'),
                ('LA MELODÍA', 'Empieza bajando',
                 'Mi · Re · Do, y otra vez Re · Do. Muy poquitas notas distintas.'),
                ('LEVEL TWO', 'Un nivel más',
                 'Es la primera del cuaderno de este nivel. Ya no eres principiante del todo.'),
            ],
            pie='Hasta ahora colocabas la mano una vez y ahí se quedaba. Aquí, por primera vez, hay '
                'que soltar la mano entera y volver a colocarla en otro sitio mientras la canción '
                'sigue. Eso se prepara mirando: no se acierta por suerte.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='El primer compás de cada mano, medido en tu partitura.',
        ritmos=[
            ('LA DERECHA', 'baja tres escalones seguidos',
             [n('E4'), n('D4'), n('C4')], AZUL, 'treble', None),
            ('LA IZQUIERDA', 'notas sueltas, una o dos por compás',
             [n('G3'), n('E3'), n('C3')], OCRE, 'bass', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva tres golpes: un-dos-tres.',
            'En la partitura está escrita la palabra «shift»: ahí la mano cambia de sitio.',
            'Al final pone «l.h. over»: la izquierda cruza por encima de la derecha.',
            'La digitación viene escrita en las dos manos.',
            'Pone «Slowly, longingly»: despacio y con nostalgia, no deprisa.',
            'Las notas largas son los sitios donde da tiempo a mudar la mano.',
            'La melodía se mueve por escalones de uno en uno, casi sin saltos.',
        ],
        reto='Cambiar de sitio sin parar la canción. Cuando la mano se muda, lo normal es pararse un '
             'segundo a buscar la tecla. Y ese segundo se oye: la música se queda colgada.',
        truco='Prepara el cambio ANTES de que llegue. Mientras suena la última nota de la posición '
              'vieja, mira ya la tecla nueva y lleva la mano hacia allí por el aire. Cuando llegue el '
              'momento, la mano ya está puesta y no hay que buscar nada.',
        sabias='Esta canción es escocesa y muy antigua, y en su época la cantaban en secreto: «bonnie» '
               'era el nombre en clave de un príncipe que estaba escondido al otro lado del mar. '
               'Cantarla era una manera de decir que le echaban de menos sin que nadie se enterara.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que va despacio. No es una canción para correr.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Lo nuevo de esta canción está escrito en la propia partitura con dos palabras: «shift» '
              'y «l.h. over». Las dos quieren decir que una mano se va a otro sitio. Se preparan '
              'mirando antes, y se practican sueltas.',
        reglas=['MIRA LA TECLA NUEVA ANTES DE LLEGAR', 'DESPACIO, QUE PONE SLOWLY',
                'CUENTA UN-DOS-TRES'],
        bloques=[
            dict(num=1, titulo='La melodía del principio',
                 pista='medida en tu partitura · baja tres escalones y repite',
                 sistemas=[
                     dict(cap='a) Mi · Re · Do, y otra vez Re · Do · sin mover la mano de sitio todavía',
                          events=[n('E4'), n('D4'), n('C4'), n('D4'), n('C4'), n('D4'),
                                  n('E4', 'h.')],
                          bars=3),
                     dict(cap='b) y la vuelta · sube y baja, siempre por escalones de uno en uno',
                          events=[n('C4'), n('D4'), n('E4'), n('F4'), n('E4'), n('D4'),
                                  n('C4', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(num=2, titulo='El cambio de sitio, suelto',
                 pista='andamio · esto es el «shift» de tu partitura, practicado aparte',
                 sistemas=[
                     dict(cap='a) toca las tres primeras, mira la tecla nueva, y sigue · sin parar',
                          events=[n('C4'), n('D4'), n('E4'), n('G4'), n('A4'), n('B4'),
                                  n('C5', 'h.')],
                          bars=3),
                     dict(cap='b) y ahora de vuelta · el salto es el mismo, pero hacia abajo',
                          events=[n('C5'), n('B4'), n('A4'), n('E4'), n('D4'), n('C4'),
                                  n('C4', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='QUÉ QUIERE DECIR «SHIFT»',
                 texto='Es una palabra inglesa que significa mudarse de sitio. En tu partitura está '
                       'escrita justo donde la mano entera tiene que cambiar de posición en el teclado. '
                       'No es que un dedo se estire: es que toda la mano se levanta y se vuelve a poner '
                       'más arriba o más abajo. Mira la tecla nueva mientras suena la nota anterior y '
                       'llegarás a tiempo.'),
            dict(num=3, titulo='Y el cruce de manos del final', clef='bass',
                 pista='andamio · esto es el «l.h. over»: la izquierda pasa por encima de la derecha',
                 sistemas=[
                     dict(cap='a) primero coloca la izquierda arriba sin tocar, cinco veces · después toca',
                          events=[n('C4'), n('E4'), n('G4'),
                                  n('E4'), n('C4'), n('E4'),
                                  n('C4', 'h.')],
                          bars=3, clef='bass'),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE CRUZA UNA MANO POR ENCIMA DE LA OTRA',
                 texto='La izquierda pasa por encima del brazo derecho para llegar a las teclas de '
                       'arriba. No se hace con la muñeca: se lleva el codo hacia fuera y el brazo '
                       'entero viaja. Hazlo cinco veces sin tocar nada, solo el movimiento, y mirando. '
                       'Cuando el brazo sepa el camino, ya puedes tocar.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R17 (crucigrama · cuenta · une) y
    # semana 2 la R18 (camino · adivina · rodea · teclado · escribe).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='My Bonnie Lies Over the Ocean · para hacer en casa',
            intro='Lo nuevo: la mano cambia de sitio en el teclado, y al final la izquierda pasa por '
                  'encima de la derecha.',
            bloques=[
                crucigrama('CRUCE', [
                    ('OCEANO', 1, 'El sitio del que habla el título de esta canción.'),
                    ('ARRIBA', 2, 'Adónde va la mano izquierda al final.'),
                    ('PULGAR', 1, 'El dedo número 1, el más gordo.'),
                    ('BLANCA', 4, 'La figura hueca que dura dos golpes.'),
                    ('MENIQUE', 1, 'El dedo más pequeño, el número 5.'),
                ], cierre='Las casillas grises dicen lo que hacen las manos al final de la canción.'),
                contar([n('E4'), n('D4'), n('C4'), n('D4'), n('C4'), n('D4'), n('E4')],
                       ['¿Cuántos Re hay?', '¿Cuántas veces sale el Do?',
                        '¿Cuántas notas hay en total?'],
                       titulo='Cuenta lo que ves',
                       pista='es el principio de tu melodía, medido en tu partitura'),
                unir([('“shift” en la partitura', 'la izquierda pasa por encima de la derecha'),
                      ('“l.h. over” al final', 'muy despacio y con nostalgia'),
                      ('“Slowly, longingly”', 'la mano se cambia de sitio'),
                      ('“Level Two”', 'esta pieza es de segundo curso')],
                     titulo='Une cada cosa escrita con lo que quiere decir',
                     pista='están desordenadas · una raya de un punto al otro'),
                rutina('Mi · Re · Do con la derecha, contando tres',
                       'Los cambios de sitio, mirando antes adónde va la mano',
                       'El cruce del final, muy despacio'),
                acuerdate('Cuando la mano cambia de sitio, lo que se mueve es la mano ENTERA, no los '
                          'dedos estirándose. Mira adónde vas antes de saltar, y aprovecha una nota '
                          'larga para hacer el viaje sin que se note.',
                          etiqueta='CAMBIAR DE SITIO'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='My Bonnie Lies Over the Ocean · para hacer en casa',
            intro='Segunda semana: un camino de manos, adivinanzas y el teclado.',
            bloques=[
                camino([['queda', 'cambia', 'queda', 'queda', 'cruza', 'queda'],
                        ['queda', 'cambia', 'cambia', 'queda', 'queda', 'cruza'],
                        ['cruza', 'queda', 'cambia', 'cambia', 'queda', 'queda'],
                        ['queda', 'queda', 'queda', 'cambia', 'cambia', 'queda'],
                        ['queda', 'cruza', 'queda', 'queda', 'cambia', 'queda']],
                       titulo='El camino de los cambios de sitio',
                       pista='colorea solo donde dice “cambia” y sale un camino'),
                adivinar([('Me muevo entera cuando la canción sube o baja mucho.', 'MANO'),
                          ('Soy el dedo número 5, el más pequeño.', 'MENIQUE'),
                          ('Al final de esta canción paso por encima de la otra.', 'IZQUIERDA')],
                         titulo='Adivina quién soy',
                         pista='una letra en cada casilla'),
                rodear([[n('E4'), n('D4'), n('C4')], [n('D4'), n('C4'), n('D4')],
                        [n('E4'), n('D4'), n('C4')], [n('F4'), n('E4'), n('D4')]],
                       titulo='Rodea los dos compases que son iguales',
                       pista='tres notas en cada compás · míralas de una en una'),
                teclado({0: 1, 4: 2, 7: 3, 11: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'De la 1 a la 4 hay un buen viaje: eso es un cambio de sitio.'],
                        titulo='En el teclado',
                        pista='fíjate en lo lejos que está la 4 de la 1'),
                escribir(titulo='Copia aquí el compás donde la mano cambia de sitio',
                         pista='cópialo tal cual y luego tócalo cinco veces'),
                rutina('La melodía entera, con los cambios de sitio',
                       'El cruce del final, diez veces seguidas',
                       'Las dos manos, sin parar aunque haya fallos'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
