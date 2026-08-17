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
from arnau_comun import n, ac, sil, corch, rutina, juego, escribir

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
                 pista='medido · cambia de nota casi en cada golpe, y trae los dedos escritos',
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

    deberes=[
        dict(titulo='Deberes · semana 1', esquina='We Wish You a Merry Christmas · para casa',
             intro='Esta semana toca aprender las dos manos por separado. Todo lo de aquí está en tu '
                   'partitura.',
             bloques=[
                 dict(tipo='nombres', num=1, titulo='¿Cómo se llama cada nota?',
                      pista='escríbelas en la cajita de debajo',
                      notas=['C4', 'D4', 'E4', 'F4', 'E4', 'D4', 'G4', 'C4']),
                 dict(tipo='nombres', num=2, titulo='Y estas, que son de la mano izquierda',
                      pista='ojo: aquí la clave es distinta, las notas no están donde antes',
                      notas=['C3', 'B2', 'A2', 'G2', 'A2', 'B2', 'C3', 'G2'], clef='bass'),
                 dict(tipo='figuras', num=3, titulo='¿Cuántos golpes dura cada una?',
                      pista='acuérdate: aquí cada compás tiene tres golpes',
                      figuras=[('q', 'negra'), ('h', 'blanca'), ('h.', 'blanca con puntito'),
                               ('w', 'redonda')]),
                 dict(tipo='une', num=4, titulo='Une cada dedo con su número',
                      pista='una raya de un punto al otro',
                      pares=[('El pulgar', 'el 5'), ('El corazón', 'el 1'), ('El meñique', 'el 3')]),
                 rutina('La derecha sola, los cuatro primeros compases',
                        'La izquierda sola, los cuatro primeros compases',
                        'Decir en voz alta el nombre de las notas sin tocar'),
                 juego('Toca tres golpes seguidos marcando el primero un poco más fuerte: UN-dos-tres. '
                       'Quien esté contigo tiene que dar una palmada solo en el fuerte. Después '
                       'cambiad. Ese golpe fuerte es el que hace que esta canción suene a villancico y '
                       'no a lista de notas.'),
             ]),
        dict(titulo='Deberes · semana 2', esquina='We Wish You a Merry Christmas · para casa',
             intro='Esta semana toca juntar las manos, un compás cada día, y mirar la partitura con '
                   'lápiz.',
             bloques=[
                 dict(tipo='rodea', num=1, titulo='Rodea los dos compases que son iguales',
                      pista='fíjate en las notas de una en una',
                      compases=[[n('C4'), n('C4'), n('D4')],
                                [n('E4'), n('E4'), n('F4')],
                                [n('C4'), n('C4'), n('D4')],
                                [n('D4'), n('C4'), n('B3')]]),
                 dict(tipo='dibuja', num=2, titulo='Dibuja tú las notas',
                      pista='solo el óvalo, sin el palito',
                      nombres=['Do', 'Re', 'Mi', 'Fa', 'Mi', 'Re', 'Do', 'Sol']),
                 dict(tipo='colorea', num=3, titulo='Colorea el primer golpe de cada compás',
                      pista='es el que pesa un poquito más que los otros dos',
                      eventos=[n('C4'), n('C4'), n('D4'), n('E4'), n('E4'), n('F4'),
                               n('E4'), n('D4'), n('C4')],
                      leyenda=['En un compás de tres, el primero pesa más.',
                               'Los otros dos van más flojitos, como de puntillas.']),
                 dict(tipo='nombres', num=4, titulo='Otra vez los nombres, a ver si te los sabes',
                      pista='sin mirar los deberes de la semana pasada',
                      notas=['E4', 'G4', 'F4', 'D4', 'C4', 'A4', 'B4', 'E4']),
                 dict(tipo='nota', etiqueta='ACUÉRDATE',
                      texto='Un compás nuevo al día es suficiente. Si intentas cuatro de golpe, al día '
                            'siguiente no te acuerdas de ninguno; si haces uno bien, la semana que '
                            'viene tienes siete.'),
                 rutina('Un compás con las dos manos, veinte veces',
                        'La canción entera con la derecha sola',
                        'Contar un-dos-tres en voz alta mientras tocas'),
             ]),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
