# -*- coding: utf-8 -*-
"""Aloha Oe (canción 16 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive (Liliuokalani, arr. Regina
   Pratley, 2 paginas):

     - Do mayor: comprobado a zoom, detras de la clave no hay nada.
     - El compas se escribe con un signo raro, una C con una raya en medio.
       Quiere decir que el compas lleva cuatro golpes pero se cuentan de DOS
       en dos, con notas largas. Pone "Con moto".
     - LO NUEVO: la melodia empieza con SALTOS GRANDES: Do · Sol · Do, o sea
       que la mano tiene que viajar de verdad, no ir por escalones.
     - Es la primera pieza del cuaderno que ocupa DOS paginas.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         sopa, figuras, adivinar, crucigrama, nombres, colorear)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Arnau', num=16, nivel='iniciación', slug='AlohaOe',
    formato='corto', titulo_corto='Aloha Oe', time_sig=(2, 2), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Aloha oe.sib.pdf'),
    yt='https://www.youtube.com/results?search_query=aloha+oe+piano',

    ficha=dict(
        titulo='Aloha Oe',
        autor='Reina Liliʻuokalani de Hawái (1878) · arr. Regina Pratley',
        datos=[('Novedad', 'Saltos grandes'), ('Compás', 'Se cuenta en dos'),
               ('Páginas', 'Dos'), ('Teclas', 'Solo blancas'),
               ('Carácter', 'Con moto')],
        armonia=dict(
            titulo='Aquí la mano tiene que viajar',
            tarjetas=[
                ('LOS SALTOS', 'Do · Sol · Do',
                 'La melodía empieza dando dos saltos grandes. Ya no va por escalones.'),
                ('EL COMPÁS', 'Una C con raya',
                 'Ese signo quiere decir: cuatro golpes, pero contados de dos en dos.'),
                ('DOS PÁGINAS', 'La primera larga',
                 'Es la pieza más larga del cuaderno hasta ahora. Hay que saber por dónde vas.'),
                ('CON MOTO', 'Con movimiento',
                 'Ni lenta ni rápida: que se note que va hacia algún sitio.'),
            ],
            pie='Hasta ahora las melodías iban de una tecla a la de al lado. Aquí hay saltos de verdad, '
                'y un salto no se acierta por suerte: se mira antes. Cuando la mano sabe a dónde va, un '
                'salto es igual de fácil que un escalón.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='Los primeros compases de la melodía, medidos en tu partitura.',
        ritmos=[
            ('LA DERECHA', 'dos saltos grandes seguidos',
             [n('C4'), n('G4'), n('C5', 'h')], AZUL, 'treble', None),
            ('Y SE PARA', 'y arriba se queda quieta un buen rato',
             [n('D5', 'h'), n('C5', 'h')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles detrás de la clave.',
            'El compás se escribe con una C con una raya: se cuenta de dos en dos.',
            'La melodía empieza con dos saltos grandes: Do, Sol, Do.',
            'Ocupa DOS páginas: es la más larga del cuaderno hasta ahora.',
            'Pone «Con moto»: con movimiento, que no se pare.',
            'Las notas son largas casi todas: no hay carreras.',
            'Las notas largas son los sitios donde da tiempo a preparar el salto.',
            'La melodía sube a saltos y luego baja despacio, de una en una.',
        ],
        reto='Los saltos. Cuando la mano tiene que viajar de una tecla a otra que está lejos, lo normal '
             'es pararse a buscarla. Y como aquí las notas son largas, ese parón se oye clarísimo.',
        truco='Mira la tecla de destino MIENTRAS suena la nota anterior. Como las notas son largas, te '
              'sobra tiempo: no hace falta ir rápido, hace falta mirar antes. Practica el salto solo, '
              'sin ritmo, diez veces, hasta que la mano vaya sin dudar.',
        sabias='La escribió la última reina de Hawái en 1878, y es la canción con la que allí se '
               'despiden. «Aloha oe» significa «adiós a ti». La reina la compuso viendo despedirse a '
               'dos personas en un puerto.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en lo tranquila que va, aunque la melodía dé saltos grandes.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Lo nuevo aquí son los saltos: la melodía ya no va de una tecla a la de al lado. Un '
              'salto se prepara con los ojos, y como en esta pieza las notas son largas, hay tiempo de '
              'sobra para mirar.',
        reglas=['MIRA LA TECLA ANTES DE SALTAR', 'LAS NOTAS SON LARGAS: HAY TIEMPO',
                'CON MOTO, QUE NO SE PARE'],
        bloques=[
            dict(num=1, titulo='El salto, suelto',
                 pista='medido · Do · Sol · Do: los dos saltos del principio, practicados aparte',
                 sistemas=[
                     dict(cap='a) primero muy lento, mirando la tecla de destino antes de moverte',
                          events=[n('C4', 'h'), n('G4', 'h'), n('C5', 'h'), n('G4', 'h')],
                          bars=2),
                     dict(cap='b) y ahora sin mirar la mano · si te equivocas, no pasa nada: mira otra vez',
                          events=[n('C4', 'h'), n('C5', 'h'), n('G4', 'h'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE ACIERTA UN SALTO',
                 texto='No se acierta con los dedos: se acierta con los ojos. Mientras suena la nota '
                       'que ya has tocado, mira ya la tecla siguiente y lleva la mano hacia allí por el '
                       'aire. Cuando llegue el momento, la mano ya está encima y solo hay que dejarla '
                       'caer. Si miras el teclado cuando ya tenías que haber tocado, llegas tarde '
                       'siempre.'),
            dict(num=2, titulo='La melodía del principio',
                 pista='medida en tu partitura · sube a saltos y arriba se queda quieta',
                 sistemas=[
                     dict(cap='a) tal como está escrita · las notas largas son para respirar',
                          events=[n('C4'), n('G4'), n('C5', 'h'),
                                  n('D5', 'h'), n('C5', 'h')],
                          bars=2),
                     dict(cap='b) y lo que sigue · baja despacio, de una en una',
                          events=[n('C5'), n('B4'), n('C5'), n('A4'),
                                  n('G4', 'h'), n('G4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Contar de dos en dos', clef='bass',
                 pista='andamio · el compás lleva cuatro golpes pero se cuentan dos, con notas largas',
                 sistemas=[
                     dict(cap='a) dos notas largas por compás · di “un... dos...” bien despacio',
                          events=[n('C3', 'h'), n('G3', 'h'), n('C3', 'h'), n('G3', 'h')],
                          bars=2, clef='bass'),
                 ]),
            dict(tipo='nota', etiqueta='ESA C CON UNA RAYA',
                 texto='Es una manera antigua de escribir el compás. Quiere decir que en cada compás '
                       'caben cuatro golpes, pero que se cuentan de dos en dos: cada cuenta dura dos '
                       'golpes. Para ti cambia una sola cosa: que las notas largas son las normales, y '
                       'las cortas casi no salen. Por eso esta pieza suena tan tranquila.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R1 (sopa · figuras · adivina) y
    # semana 2 la R2 (crucigrama · nombres · colorea).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Aloha Oe · para hacer en casa',
            intro='Lo nuevo: saltos grandes, y por primera vez una pieza de dos páginas.',
            bloques=[
                sopa(['HAWAI', 'ALOHA', 'SALTOS', 'VIAJAR', 'DOS', 'PAGINAS',
                      'LARGAS', 'SOL', 'DO', 'RE'], semilla=1616, filas=8,
                     titulo='Sopa de letras de tu canción',
                     pista='diez palabras · tumbadas, de pie o en diagonal'),
                figuras([('h', 'blanca'), ('w', 'redonda'), ('q', 'negra'),
                         ('h.', 'blanca con puntito')],
                        titulo='¿Cuántos golpes dura cada una?',
                        pista='en esta pieza mandan las largas'),
                adivinar([('Cuando la mano va de golpe a un sitio lejano.', 'SALTO'),
                          ('Soy dos y en esta pieza hay que pasarme.', 'PAGINAS'),
                          ('En hawaiano valgo para saludar y para despedirse.', 'ALOHA')],
                         titulo='Adivina quién soy',
                         pista='una letra en cada casilla'),
                rutina('Do · Sol · Do, mirando antes adónde va la mano',
                       'La melodía entera muy despacio, sin fallar los saltos',
                       'Pasar de la primera página a la segunda sin pararse'),
                juego('Cierra los ojos, toca un Do y salta al Sol de arriba sin mirar. Quien esté '
                      'contigo te dice si has acertado. Diez veces.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Aloha Oe · para hacer en casa',
            intro='Segunda semana: crucigrama, nombres y colores.',
            bloques=[
                crucigrama('SALTOS', [
                    ('MANOS', 4, 'Tienes dos, y en esta pieza viajan mucho.'),
                    ('BLANCA', 5, 'La figura hueca que dura dos golpes.'),
                    ('ALOHA', 1, 'La primera palabra del título: en hawaiano es hola y adiós.'),
                    ('CUATRO', 3, 'Los golpes que lleva cada compás de esta pieza.'),
                    ('SOL', 1, 'La segunda nota de tu melodía, después del primer salto.'),
                    ('COMPAS', 5, 'El trozo que hay entre dos rayas de arriba abajo.'),
                ], cierre='Las casillas grises dicen lo que hace la mano cuando viaja de golpe.'),
                nombres(['C4', 'G4', 'C5', 'D5', 'B4', 'A4', 'G4', 'E4'],
                        pista='son las notas de tu melodía · escríbelas debajo'),
                colorear([n('C4'), n('G4'), n('C5', 'h'),
                          n('D5'), n('B4'), n('A4', 'h'), n('G4'), n('E4')],
                         ['Un color para las de un golpe y otro para las de dos.'],
                         titulo='Colorea según lo que duran',
                         pista='dos colores'),
                rutina('Los tres saltos más grandes, veinte veces cada uno',
                       'Las dos páginas seguidas, sin pararse en el cambio',
                       'Contar dos golpes largos por compás'),
                juego('Quien esté contigo pasa la página mientras tú tocas, para que no tengas que '
                      'soltar las manos. Ensayadlo cinco veces: eso también se practica.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
