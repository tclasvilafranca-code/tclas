# -*- coding: utf-8 -*-
"""Preludio nº 1 en Do mayor, BWV 846, de J. S. Bach — pieza 18 de Aida.
   Formato ADULTO exigente.

   EL ARCHIVO SE LLAMA "AVE MARIA" Y NO LO ES, y por eso el cuaderno lo llama
   por su nombre. Decision del cliente, literal: "Preludio nº 1, y explico el
   Ave Maria". Lo que trae impreso el PDF es **"Book 1, Prelude 1"** de J. S.
   Bach, sin una sola nota de la melodia de Gounod. La explicacion va en la
   ficha porque es teoria de verdad y ademas responde a la pregunta que ella se
   va a hacer al abrir la hoja: en 1853 Charles Gounod escribio una melodia
   NUEVA por encima de este preludio, tal cual, sin tocarle una nota; el
   preludio es de 1722 y la melodia, de siglo y medio despues. Lo que se toca
   aqui es el preludio entero, que se sostiene solo.

   Segunda de las tres que van seguidas en mayo y junio. Detras del bajo
   obstinado de Pachelbel viene el caso extremo del mismo principio: **un solo
   dibujo de mano**, repetido compas tras compas, en el que lo unico que cambia
   son las notas de dentro.

   Lo comprobado sobre el PDF de SU carpeta (arreglo de mfiles.co.uk,
   2 paginas, vectorial). Es solo suya.

     - Detras de la clave no hay nada: Do mayor.
     - **4/4**.
     - NO trae tempo impreso ni caracter escrito.
     - Semicorcheas de principio a fin: 276 pares de barras dobles medidos en
       el PDF, que es con diferencia el numero mas alto de las diecinueve.
     - **35 compases**, contados sobre el papel: se localizaron las divisorias
       por columnas de tinta que cruzan el sistema entero, descontando la
       llave del principio y la doble barra del final. Salen tres compases en
       cada uno de los diez primeros sistemas, dos en el penultimo y tres en
       el ultimo. El indice del album cita ese numero, asi que estaba obligado
       a medirse.

   LAS ALTURAS del compas 1, medidas a 150 ppp sobre las cinco lineas de cada
   pentagrama. El compas son DOS MITADES IGUALES, y cada mitad es:

       DERECHA    silencio de CORCHEA · Sol4 · Do5 (semicorcheas) ·
                  Mi5 · Sol4 · Do5 · Mi5 (semicorcheas)
                  0,5 + 0,25x2 + 0,25x4 = 2 tiempos

       IZQUIERDA  dos voces a la vez:
                  la de abajo, un Do4 en blanca;
                  la de arriba, silencio de corchea · Mi4 (corchea) ligado a
                  Mi4 (negra).
                  Las dos suman 2 tiempos.

   JUNTANDO LAS DOS MANOS sale el acorde entero desplegado de grave a agudo —
   Do4 · Mi4 · Sol4 · Do5 · Mi5— y ese es el dibujo que se repite. La edicion
   reparte las dos primeras notas a la izquierda y las tres de arriba a la
   derecha; en otras ediciones va todo en la derecha. Es la misma musica.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, semi, plan, objetivo, verdadero_falso,
                      inventa, unir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Media parte del compas 1 de la DERECHA, medida. Cita literal: el compas son
# dos mitades iguales.
MITAD = [sil('e')] + semi(['G4', 'C5'], 2) + semi(['E5', 'G4', 'C5', 'E5'], 4)

# Y media parte del c. 2, medida igual: el mismo dibujo sobre otras notas. La
# armonia cambia (aqui sale Re-Fa-La-Do) y el dibujo de mano no.
MITAD2 = [sil('e')] + semi(['A4', 'D5'], 2) + semi(['F5', 'A4', 'D5', 'F5'], 4)

# La IZQUIERDA del c. 1, con sus dos voces separadas. Tambien medido.
IZQ_LARGA = [n('C4', 'h'), n('C4', 'h')]
IZQ_ALTA = [sil('e'), dict(n('E4', 'e'), lig=True), n('E4'),
            sil('e'), dict(n('E4', 'e'), lig=True), n('E4')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=18, nivel='intermedio',
    slug='PreludioBach', formato='adulto',
    titulo_corto='Preludio nº 1', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'Preludio n1 Bach.pdf'),
    yt='https://www.youtube.com/results?search_query=bach+prelude+1+c+major+bwv+846+piano',

    ficha=dict(
        titulo='Preludio nº 1',
        autor='J. S. Bach · BWV 846 · el del Ave María de Gounod',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Armadura', 'Ninguna'), ('La figura', 'Semicorchea'),
               ('El compás', 'Dos mitades iguales')],
        titulo_ritmos='El compás 1, medido',
        pie_ritmos='Arriba, el c. 1 de la derecha MEDIDO en tu partitura: son dos mitades '
                   'exactamente iguales. Abajo, la voz larga de la izquierda en ese mismo compás: '
                   'un Do en blanca por cada mitad.',
        armonia=dict(
            titulo='Por qué se llama Ave María en tu carpeta',
            tarjetas=[
                ('LO QUE PONE', 'Book 1, Prelude 1',
                 'Eso es lo que trae impreso tu partitura, y eso es lo que vas a tocar: el '
                 'Preludio nº 1 en Do mayor de Bach, escrito hacia 1722. No hay ninguna melodía '
                 'de Ave María escrita en el papel.'),
                ('LO QUE HIZO GOUNOD', 'Ciento treinta años',
                 'En 1853 Charles Gounod escribió una melodía NUEVA por encima de este preludio, '
                 'sin tocarle una sola nota. Lo que se canta como Ave María es esa melodía; lo de '
                 'debajo es esto.'),
                ('EL DIBUJO DE MANO', 'Uno solo',
                 'Do · Mi · Sol · Do · Mi de grave a agudo, y vuelta a subir. Ese dibujo se repite '
                 'compás tras compás: lo único que cambia son las notas que lo forman.'),
                ('LAS DOS MANOS', 'Se reparten el acorde',
                 'Tu edición da las dos notas graves a la izquierda y las tres agudas a la derecha. '
                 'Otras ediciones lo escriben todo en la derecha: es la misma música.'),
            ],
            pie='Aquí no hay melodía que aprender, y por eso engaña: parece fácil hasta que se '
                'intenta que las cinco notas suenen iguales de fuertes y a la misma distancia una '
                'de otra. Lo que se estudia en esta pieza es la mano, no la música.',
        ),
        ritmos=[
            ('DERECHA', 'el c. 1, MEDIDO · son dos mitades iguales',
             MITAD + MITAD, OCRE, 'treble', None),
            ('IZQUIERDA', 'la voz larga del c. 1, medida · un Do por mitad',
             list(IZQ_LARGA), AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'La partitura pone "Book 1, Prelude 1", no "Ave María".',
            'No trae ni tempo ni carácter escritos.',
            'El compás 1 son dos mitades exactamente iguales.',
            'Cada mitad empieza con un silencio de corchea.',
            'La izquierda lleva dos voces a la vez: una larga y otra ligada.',
            'Es la pieza con más semicorcheas de tu cuaderno.',
        ],
        reto='Que las cinco notas del dibujo suenen IGUALES: mismo volumen y misma distancia entre '
             'unas y otras. Con una melodía encima los desniveles se disimulan; aquí no hay melodía '
             'que los tape.',
        truco='Toca el dibujo entero como un acorde, las cinco notas a la vez, y escucha si suenan '
              'las cinco. Después desplégalo despacio sin cambiar nada más: si una nota se pierde, '
              'es la que hay que trabajar.',
        sabias='Bach escribió los preludios y fugas del Clave bien temperado para probar que un '
               'teclado afinado de la manera nueva podía tocar en las veinticuatro tonalidades. '
               'Este es el primero de los cuarenta y ocho, y es también el más tocado: casi todo el '
               'mundo lo ha oído aunque no sepa de quién es.',
        qr=dict(titulo='Escúchala',
                texto='Busca una versión sin voz y otra con el Ave María cantada encima. La mano '
                      'del piano es exactamente la misma en las dos: eso es lo que hizo Gounod.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Un solo dibujo y todo el trabajo dentro de él. Esta semana no se aprende una pieza: '
              'se aprende una mano.',
        reglas=['UN SOLO DIBUJO, REPETIDO', 'LAS CINCO NOTAS, IGUALES DE FUERTES',
                'LA IZQUIERDA LLEVA DOS VOCES'],
        bloques=[
            dict(num=1, titulo='El dibujo de la mano derecha',
                 pista='c. 1 de la derecha · MEDIDO · el compás son dos mitades iguales',
                 sistemas=[
                     dict(cap='a) el compás 2 entero · el mismo dibujo de mano sobre otras notas: '
                              'lo único que cambia entre un compás y el siguiente es el acorde',
                          events=MITAD2 + MITAD2, bars=1),
                     dict(cap='b) y el dibujo del c. 1 tocado como acorde, las tres notas a la vez '
                              '· andamio: sirve para oír si suenan las tres',
                          events=[ac(('G4', 'C5', 'E5'), 'h'), ac(('G4', 'C5', 'E5'), 'h')],
                          bars=1, show_time=False),
                     dict(cap='c) y desplegado en corcheas, al doble de lento · andamio: las mismas '
                              'notas con el doble de tiempo para colocar cada dedo',
                          events=corch(['G4', 'C5']) + corch(['E5', 'G4']) +
                                 corch(['C5', 'E5']) + corch(['C5', 'G4']),
                          bars=1, show_time=False),
                     dict(cap='d) y el del c. 2, también en corcheas · andamio: si los dos salen '
                              'igual de fáciles, el resto de la pieza es más de lo mismo',
                          events=corch(['A4', 'D5']) + corch(['F5', 'A4']) +
                                 corch(['D5', 'F5']) + corch(['D5', 'A4']),
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA PIEZA ENGAÑA',
                 texto='No tiene melodía. Eso suena a ventaja —no hay nada que "cantar"— y es justo '
                       'al revés: en una pieza con melodía, si una nota del acompañamiento sale '
                       'floja no se nota, porque el oído está en otro sitio. Aquí el acompañamiento '
                       'ES la pieza, y cualquier nota que se quede corta o llegue tarde se oye '
                       'entera. Por eso se estudia despacio y escuchando, no repitiendo.'),
            dict(num=2, titulo='La izquierda, que lleva dos voces',
                 pista='c. 1 de la mano izquierda · MEDIDO · las dos voces suenan a la vez',
                 sistemas=[
                     dict(cap='a) la voz de arriba: entra tras un silencio de corchea y se queda '
                              'ligada · esa ligadura es lo que la hace durar hasta el final',
                          events=list(IZQ_ALTA), bars=1, clef='bass'),
                     dict(cap='b) y las dos voces juntas, escritas como acorde para colocarlas · en '
                              'tu partitura cada una tiene su figura y su silencio',
                          events=[ac(('C4', 'E4'), 'h'), ac(('C4', 'E4'), 'h')],
                          bars=1, clef='bass', show_time=False),
                     dict(cap='c) y el mismo acorde bajando por los grados de Do mayor · andamio: '
                              'la mano hace lo mismo y solo cambia de sitio',
                          events=[ac(('C4', 'E4'), 'h'), ac(('B3', 'D4'), 'h'),
                                  ac(('A3', 'C4'), 'h'), ac(('G3', 'B3'), 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos: el acorde entero',
                 pista='c. 1 con las dos manos · MEDIDO · juntando las dos sale Do · Mi · Sol · Do '
                       '· Mi de grave a agudo',
                 sistemas=[
                     # `corte='G4'` en los dos acordes: en ESTA edicion el Do
                     # central y el Mi de encima los toca la IZQUIERDA (van en
                     # clave de fa, sobre lineas adicionales) y la derecha
                     # empieza en el Sol4. Con el corte de siempre —el Do
                     # central— las cinco notas se iban al pentagrama de sol y
                     # salia un acorde de cinco para una mano, que no lo es.
                     dict(cap='a) las cinco notas del acorde, de grave a agudo · andamio: es lo que '
                              'suena cuando las dos manos van juntas',
                          events=[n('C4', 'h'), n('E4', 'h'), n('G4', 'h'),
                                  n('C5', 'h'), n('E5', 'w')],
                          bars=3, manos='dobla'),
                     dict(cap='b) y el acorde entero de una vez, para oírlo antes de desplegarlo',
                          events=[ac(('C4', 'E4', 'G4', 'C5', 'E5'), 'w')],
                          bars=1, manos='dobla', corte='G4', show_time=False),
                     dict(cap='c) y el del c. 2, que es el mismo dibujo un grado más arriba · '
                              'andamio: las dos manos juntas, primero acorde y luego desplegado',
                          events=[ac(('D4', 'F4', 'A4', 'D5', 'F5'), 'w')],
                          bars=1, manos='dobla', corte='A4', show_time=False),
                     dict(cap='d) y los dos acordes seguidos, desplegados en negras · andamio: es '
                              'el camino que hace la mano al pasar del c. 1 al c. 2',
                          events=[n('C4'), n('E4'), n('G4'), n('C5'),
                                  n('D4'), n('F4'), n('A4'), n('D5')],
                          bars=2, manos='dobla', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Los cuatro primeros compases, y con una condición: sin metrónomo el primer '
                       'día. Toca despacio y escucha si las cinco notas suenan iguales; cuando '
                       'suenen, entonces pon el metrónomo. Tu edición no da número, así que la '
                       'velocidad la eliges tú y la anotas a lápiz. Y fíjate en lo que cambia de un '
                       'compás al siguiente: casi nunca son las cinco notas, casi siempre son una o '
                       'dos.'),
        ] + bloques_extra('Do mayor', 115, 'C5', 'C3',
                          'el dibujo de mano que se repite: cinco notas de grave a agudo',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Preludio nº 1 · para casa',
            intro='Quince minutos al día, y esta semana con el oído puesto: la pieza es una sola '
                  'mano repetida, así que lo que se corrige es cómo suena, no qué notas son.',
            bloques=[
                plan((4, 'El acorde entero, las cinco notas a la vez, escuchando si suenan todas'),
                     (5, 'El dibujo desplegado, muy despacio y sin metrónomo'),
                     (3, 'La izquierda sola, con sus dos voces'),
                     (3, 'Los cc. 1 a 4 con las dos manos')),
                objetivo('Que las cinco notas del dibujo suenen igual de fuertes. Grábate con el '
                         'móvil una vez y escúchalo: es la manera más rápida de saber cuál se te '
                         'está quedando corta.'),
                verdadero_falso([
                    'Esta partitura trae escrita la melodía del Ave María.',
                    'El compás 1 son dos mitades exactamente iguales.',
                    'Cada mitad empieza con un silencio de corchea.',
                    'La mano izquierda toca una sola voz.',
                    'Bach escribió este preludio antes que Gounod su melodía.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas'),
                inventa(['Solo Do, Mi, Sol, Do y Mi.',
                         'Un compás de cuatro tiempos.',
                         'Que empiece con un silencio de corchea, como el tuyo.'],
                        time_sig=(4, 4),
                        titulo='Inventa un compás con el mismo dibujo',
                        pista='las mismas cinco notas, en el orden que tú quieras · y tócalo'),
                unir([('Preludio', 'una pieza que abre y no cierra nada'),
                      ('Ligadura', 'une dos notas iguales en un solo sonido'),
                      ('Semicorchea', 'cuatro caben en una negra'),
                      ('Ave María', 'una melodía escrita encima, 130 años después')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                para_clase('Los cuatro primeros compases con las dos manos y a la velocidad que te '
                           'salgan las cinco notas iguales. Y dime qué nota se te queda corta: '
                           'siempre hay una, y es lo que vamos a mirar.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
