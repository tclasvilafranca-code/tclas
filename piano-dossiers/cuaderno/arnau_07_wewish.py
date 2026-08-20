# -*- coding: utf-8 -*-
"""We Wish You a Merry Christmas (canción 7 de Arnau, iniciación). CORTO.

   Medido sobre el PDF de su carpeta de Drive (arr. Gilbert DeBenedetti,
   "Primer Level", 1 pagina):

     - Do mayor (nada detras de la clave), 3/4, y pone "Brightly".
     - Las DOS manos se mueven, y las dos llevan digitacion impresa: en la
       izquierda salen los numeros 4, 3, 2 y 1, o sea que la mano cambia de
       dedo en casi cada nota.
     - La melodia empieza repitiendo el Do y luego sube: Do · Do · Re, y mas
       adelante Mi · Mi · Fa · Mi · Re.
     - Es de Navidad: en el plan de curso va en diciembre.
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
    alumno='Arnau', num=7, nivel='iniciación', slug='WeWishYou',
    formato='corto', titulo_corto='We Wish You a Merry Christmas',
    time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'WE WISH A MERRY CRISTMAS.pdf'),
    yt='https://www.youtube.com/results?search_query=we+wish+you+a+merry+christmas+piano',

    ficha=dict(
        titulo='We Wish You a Merry Christmas',
        autor='Villancico popular · arreglo de Gilbert DeBenedetti',
        datos=[('Teclas', 'Solo blancas'), ('Golpes', '3 por compás'),
               ('Las dos manos', 'Se mueven'), ('Dedos', 'Escritos'),
               ('Carácter', 'Brightly')],
        armonia=dict(
            titulo='Las dos manos con números encima',
            tarjetas=[
                ('LA MELODÍA', 'Repite y sube',
                 'Do · Do · Re para empezar, y más adelante Mi · Mi · Fa · Mi · Re.'),
                ('LA IZQUIERDA', 'Se mueve',
                 'Ya no se queda quieta: cambia de nota casi en cada golpe.'),
                ('LOS NÚMEROS', '4 · 3 · 2 · 1',
                 'Son los dedos, y en esta canción vienen escritos también en la izquierda.'),
                ('EL VAIVÉN', 'Tres golpes',
                 'Un-dos-tres, un-dos-tres. El primero pesa un poco más que los otros dos.'),
                ('SE REPITE', 'Tres veces',
                 'La misma frase vuelve tres veces, empezando cada vez desde más arriba.'),
            ],
            pie='Es la primera canción del cuaderno en la que las dos manos se mueven Y además te '
                'dicen con qué dedo tocar cada nota. Los números no son un adorno: si los usas, la '
                'mano llega sola a la nota siguiente.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='El primer compás de cada mano, medido en tu partitura.',
        ritmos=[
            ('LA DERECHA', 'repite el Do y sube al Re',
             [n('C4'), n('C4'), n('D4')], AZUL, 'treble', None),
            ('LA IZQUIERDA', 'aquí ya se mueve ella también',
             [n('C3'), n('B2'), n('A2')], OCRE, 'bass', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva tres golpes: un-dos-tres.',
            'Las DOS manos se mueven, cada una por su lado.',
            'Los números de encima y de debajo de las notas son los dedos.',
            'La melodía empieza repitiendo la misma nota dos veces.',
            'Pone «Brightly», que quiere decir con alegría.',
            'El primer golpe de cada compás pesa un poco más que los otros dos.',
            'La misma frase aparece tres veces seguidas, empezando cada vez más arriba.',
        ],
        reto='Que cada mano vaya a lo suyo. Cuando las dos se mueven, lo que suele pasar es que las '
             'dos hacen lo mismo sin querer: si la derecha sube, la izquierda sube también. Y aquí no '
             'van juntas, cada una lleva su camino y hay que pensarlas por separado.',
        truco='Aprende cada mano por separado hasta que salga sin mirar, y solo entonces júntalas, un '
              'compás cada vez. Nunca dos compases nuevos el mismo día: uno, bien, y mañana el '
              'siguiente.',
        sabias='Este villancico es de hace más de 400 años, de Inglaterra, y lo cantaban los pobres '
               'que iban de casa en casa pidiendo pudin a cambio de una canción. Por eso la letra dice '
               '«traednos un pudin» y luego «no nos iremos hasta que nos lo deis».',
        qr=dict(titulo='Escúchala',
                texto='Marca tres golpes con el pie: un-dos-tres, un-dos-tres.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Lo nuevo aquí es que las dos manos se mueven a la vez y cada una va a lo suyo. Así que '
              'cada mano por separado hasta que salga sola, y solo después las dos juntas.',
        reglas=['CADA MANO POR SEPARADO PRIMERO', 'USA LOS DEDOS QUE PONE', 'UN-DOS-TRES'],
        bloques=[
            dict(num=1, titulo='La derecha',
                 pista='medido · repite el Do y sube, y más adelante hace lo mismo desde el Mi',
                 sistemas=[
                     dict(cap='a) Do · Do · Re, y otra vez · las dos primeras son la misma tecla',
                          events=[n('C4'), n('C4'), n('D4'), n('C4'), n('C4'), n('D4'),
                                  n('E4', 'h.')],
                          bars=3),
                     dict(cap='b) y la parte que sube más · Mi · Mi · Fa · Mi · Re, bajando otra vez',
                          events=[n('E4'), n('E4'), n('F4'), n('E4'), n('D4'), n('C4'),
                                  n('C4', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda, que aquí también anda', clef='bass',
                 pista='medido · cambia de nota casi en cada golpe · los dedos vienen en tu '
                       'partitura: cópialos aquí encima antes de empezar',
                 sistemas=[
                     dict(cap='a) tres notas bajando, una por golpe · usa los dedos que pone la partitura',
                          events=[n('C3'), n('B2'), n('A2'), n('G2'), n('A2'), n('B2'),
                                  n('C3', 'h.')],
                          bars=3, clef='bass'),
                     dict(cap='b) y ahora sin mirar la mano · si te pierdes, vuelve a colocar el pulgar',
                          events=[n('C3'), n('B2'), n('A2'), n('B2'), n('C3'), n('B2'),
                                  n('C3', 'h.')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='POR QUÉ CADA MANO POR SEPARADO',
                 texto='Cuando las dos manos se mueven a la vez y todavía no te sabes ninguna, tu '
                       'cabeza tiene que hacer dos cosas nuevas al mismo tiempo y no le da. Si primero '
                       'aprendes una hasta que salga sola, cuando juntes las dos solo tendrás una cosa '
                       'nueva que pensar. No es ir más lento: es llegar antes.'),
            dict(num=3, titulo='Y ahora un compás con las dos',
                 pista='un solo compás, veinte veces · mañana el siguiente',
                 sistemas=[
                     dict(cap='a) lo que hace la derecha en el primer compás',
                          events=[n('C4'), n('C4'), n('D4'), n('C4', 'h.')],
                          bars=2),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE JUNTAN',
                 texto='Toca el primer golpe de las dos manos a la vez y para. Míralo: las dos teclas '
                       'apretadas. Luego el segundo golpe, y para. Así todo el compás, golpe a golpe. '
                       'Cuando los tres golpes salgan sin parar, ese compás ya es tuyo.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R13 (crucigrama · diferencias ·
    # adivina) y semana 2 la R14 (teclado · palmas · nombres · camino).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='We Wish You a Merry Christmas · para hacer en casa',
            intro='Villancico, y la primera canción en la que tu partitura te dice qué dedo usar en '
                  'casi cada nota.',
            bloques=[
                crucigrama('DEDOS', [
                    ('REDONDA', 2, 'La figura más larga: dura cuatro golpes.'),
                    ('NEGRA', 1, 'La figura que dura un golpe.'),
                    ('NAVIDAD', 4, 'La fiesta en la que se canta esta canción.'),
                    ('SOL', 1, 'La clave que lleva tu mano derecha.'),
                    ('MANOS', 4, 'En esta canción las dos se mueven.'),
                ], cierre='Las casillas grises dicen lo que tu partitura lleva escrito con números.'),
                diferencias(
                    [n('C4'), n('C4'), n('D4'), n('C4'), n('C4'), n('D4')],
                    [n('C4'), n('D4'), n('D4'), n('C4'), n('C4'), n('E4', 'h')],
                    cuantas=3,
                    titulo='Busca las tres diferencias',
                    pista='el de arriba es el principio de tu canción · el de abajo tiene trampas'),
                adivinar([('Vengo escrito con números debajo de las notas.', 'DEDOS'),
                          ('Duro cuatro golpes y soy la figura más larga.', 'REDONDA'),
                          ('Somos tres en cada compás de esta canción.', 'GOLPES')],
                         titulo='Adivina quién soy',
                         pista='una letra en cada casilla'),
                rutina('Do · Do · Re con la derecha, contando tres',
                       'La izquierda sola, mirando los números de los dedos',
                       'Las dos manos, los cuatro primeros compases'),
                juego('Canta el villancico y quien esté contigo lleva el pulso con palmadas. '
                      'Después al revés: él canta y tú tocas solo el primer golpe de cada compás.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='We Wish You a Merry Christmas · para hacer en casa',
            intro='Esta semana se empieza en el teclado y se acaba con un camino de dedos.',
            bloques=[
                teclado({0: 1, 1: 2, 2: 3, 3: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'La 1 y la 3 son las dos primeras notas distintas de tu melodía.'],
                        titulo='En el teclado',
                        pista='las cuatro marcadas son de esta canción'),
                palmas([('NA-VI-DAD', 3), ('VI-LLAN-CI-CO', 4), ('TU-RRON', 2)],
                       titulo='El ritmo de las palabras',
                       pista='dilo en voz alta y escríbelo con figuras en la caja'),
                nombres(['C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'G4', 'C4'],
                        pista='son las notas de tu melodía · escríbelas debajo'),
                camino([['4', '3', '2', '1', '3', '2'],
                        ['3', '4', '2', '3', '1', '4'],
                        ['2', '3', '4', '1', '2', '3'],
                        ['1', '2', '3', '4', '4', '1']],
                       titulo='El camino de los dedos gordos',
                       pista='colorea solo los 1, que es el pulgar, y verás el camino'),
                acuerdate('Los números de tu partitura no son notas: son dedos. El 1 es el pulgar y '
                          'el 5 el meñique, en las dos manos. Si los respetas, la mano llega sola a '
                          'la nota siguiente y no tienes que mirarte los dedos.',
                          etiqueta='LOS NÚMEROS NO SON NOTAS'),
                rutina('El villancico entero, muy despacio',
                       'Las dos manos, con los dedos que dice la partitura',
                       'Contar un-dos-tres en voz alta mientras tocas'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
