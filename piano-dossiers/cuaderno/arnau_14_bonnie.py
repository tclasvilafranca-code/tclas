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
from arnau_comun import n, ac, sil, corch, rutina, juego, escribir

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

    deberes=[
        dict(titulo='Deberes · semana 1', esquina='My Bonnie · para hacer en casa',
             intro='Esta semana toca practicar el cambio de sitio de la mano, que es lo nuevo.',
             bloques=[
                 dict(tipo='nombres', num=1, titulo='¿Cómo se llama cada nota?',
                      pista='escríbelas en la cajita de debajo',
                      notas=['E4', 'D4', 'C4', 'F4', 'G4', 'A4', 'B4', 'C5']),
                 dict(tipo='dibuja', num=2, titulo='Dibuja tú las notas',
                      pista='solo el óvalo, sin el palito',
                      nombres=['Mi', 'Re', 'Do', 'Sol', 'La', 'Si', 'Do', 'Fa']),
                 dict(tipo='figuras', num=3, titulo='¿Cuántos golpes dura cada una?',
                      pista='acuérdate: aquí cada compás tiene tres golpes',
                      figuras=[('q', 'negra'), ('h', 'blanca'), ('h.', 'blanca con puntito'),
                               ('w', 'redonda')]),
                 dict(tipo='une', num=4, titulo='Une cada palabra con lo que quiere decir',
                      pista='las dos están escritas en tu partitura',
                      pares=[('shift', 'la izquierda pasa por encima'),
                             ('l.h. over', 'despacio y con nostalgia'),
                             ('slowly', 'la mano cambia de sitio')]),
                 rutina('El cambio de sitio suelto, diez veces, mirando la tecla nueva',
                        'La melodía del principio, muy despacio',
                        'El movimiento del cruce de manos, sin tocar'),
                 juego('Pon un objeto pequeño en una tecla lejana. Toca una nota cerca, mira el objeto, '
                       'y lleva la mano hasta esa tecla sin mirar el camino, solo el destino. Quien '
                       'esté contigo comprueba si has acertado. Diez veces. Eso es lo que hace la mano '
                       'en un «shift».'),
             ]),
        dict(titulo='Deberes · semana 2', esquina='My Bonnie · para hacer en casa',
             intro='Esta semana toca buscar en la partitura todos los sitios donde la mano se muda.',
             bloques=[
                 dict(tipo='rodea', num=1, titulo='Rodea los dos compases que son iguales',
                      pista='fíjate en las notas de una en una',
                      compases=[[n('E4'), n('D4'), n('C4')],
                                [n('D4'), n('C4'), n('D4')],
                                [n('E4'), n('D4'), n('C4')],
                                [n('C4'), n('D4'), n('E4')]]),
                 dict(tipo='nombres', num=2, titulo='Otra vez los nombres, a ver si te los sabes',
                      pista='sin mirar los deberes de la semana pasada',
                      notas=['G4', 'C5', 'A4', 'E4', 'B4', 'D4', 'F4', 'C4']),
                 dict(tipo='colorea', num=3, titulo='Colorea las notas largas',
                      pista='son los sitios donde la canción respira y donde te da tiempo a mudarte',
                      eventos=[n('E4'), n('D4'), n('C4'), n('D4'),
                               n('C4', 'h.'), n('E4'), n('F4'), n('G4', 'h.')],
                      leyenda=['La blanca con puntito dura tres golpes: el compás entero.',
                               'Ahí es donde da tiempo a mirar la tecla siguiente.']),
                 dict(tipo='nota', etiqueta='ACUÉRDATE',
                      texto='Los cambios de sitio se preparan en las notas largas, que es cuando hay '
                            'tiempo. Busca en tu partitura la palabra «shift», mira qué nota hay justo '
                            'antes, y aprovecha ese rato para llevar la mano.'),
                 rutina('Buscar y rodear a lápiz todos los «shift» de la partitura',
                        'Los cuatro primeros compases con las dos manos',
                        'El cruce de manos del final, cinco veces'),
                 juego('Toca una nota, cierra los ojos, y sin mirar lleva la mano cinco teclas más '
                       'arriba y toca. Quien esté contigo dice si has acertado. Diez veces. Se puede '
                       'aprender a medir distancias sin mirar, y es lo que hace que un «shift» salga '
                       'sin pararse.', 'esta vez con los ojos cerrados'),
                 escribir(4),
             ]),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
