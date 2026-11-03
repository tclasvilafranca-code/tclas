# -*- coding: utf-8 -*-
"""Titanic (My Heart Will Go On) — pieza 16 de Martina. ADULTO exigente, tono de niña.

   Lo comprobado sobre el PDF de su carpeta de Drive (James Horner, arreglo de
   Ana Cristina Escobés, elcuartodelpiano.com, 1 página, vectorial; el mismo
   archivo que el de Luisa y el de Aída), mirado a 110 y a 250 dpi:

     - Detrás de la clave no hay nada: Do mayor. **2/4**.
     - "Adagio" y "mp" al empezar, "mf" en el c. 11. NO trae número de
       metrónomo: la casilla de la ficha se llama "Carácter".
     - Barras de repetición con casillas de primera y segunda vez (dos veces).
     - Casi toda la pieza va bajo ligaduras de frase largas.
     - MEDIDO (`medir_arranque`): el c. 1 de la derecha es Do5 corchea con
       puntillo · Do5 semicorchea · Do5 · Do5 corcheas.
     - MEDIDO nota a nota (`cabezas`, 250 dpi) en el segundo bloque, el de los
       cc. 11-14, que ahí cambia la textura: la derecha es **Do5 blanca | Re5
       negra con puntillo · Sol4 corchea | Sol5 negra · Fa5 · Mi5 corcheas | Re5
       negra · Mi5 · Fa5 corcheas**, y la izquierda deja de hacer blancas y pasa a
       **dos negras por compás, la grave y luego la aguda**: La3-Mi4 | Sol3-Re4 |
       Fa3-Do4 | Sol3-Re4.

   Mismo archivo que el de Jaume, Luisa y Aída: lo literal coincide, lo inventado no.
   Aquí el material de apoyo va por el **segundo bloque** (la izquierda en
   negras, la derecha con una línea larga) y por las **ligaduras de frase**,
   que son lo que separa tocar las notas de tocar la canción.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, plan, metronomo, nombres, colorear, diferencias,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

D1 = [n('C5', 'e.'), n('C5', 's'), n('C5', 'e'), n('C5', 'e')]
# el segundo bloque, cc. 11-14, medido
D_11 = [n('C5', 'h')]
D_12 = [n('D5', 'q.'), n('G4', 'e')]
D_13 = [n('G5'), n('F5', 'e'), n('E5', 'e')]
D_14 = [n('D5'), n('E5', 'e'), n('F5', 'e')]
I_11_14 = [n('A3'), n('E4'), n('G3'), n('D4'), n('F3'), n('C4'), n('G3'), n('D4')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=16, nivel='intermedio', slug='Titanic',
    formato='adulto',
    titulo_corto='Titanic', time_sig=(2, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source', 'Titanic'),
    yt='https://www.youtube.com/results?search_query=titanic+my+heart+will+go+on+easy+piano',

    ficha=dict(
        titulo='Titanic · My Heart Will Go On',
        autor='James Horner · arreglo de Ana Cristina Escobés',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '2/4'),
               ('Carácter', 'Adagio'), ('Figura corta', 'Semicorchea'),
               ('Páginas', 'Una')],
        titulo_ritmos='El c. 1 y el cambio de textura',
        pie_ritmos='Medido sobre tu partitura. Arriba, el c. 1 de la derecha. Abajo, la izquierda de '
                   'los cc. 11-12, donde las blancas pasan a dos negras por compás.',
        armonia=dict(
            titulo='Dos texturas en una página',
            tarjetas=[
                ('LOS CC. 1-10', 'Blancas',
                 'La izquierda hace una blanca por compás, sin moverse, y toda la pieza es la '
                 'derecha. El tempo lo marca el segundo tiempo vacío de cada compás.'),
                ('DESDE EL C. 11', 'Dos negras',
                 'La izquierda se mueve: una nota grave y una aguda en cada compás, y la derecha '
                 'pasa a una melodía larga. Es "mf", un escalón por encima de donde empezó.'),
                ('LAS LIGADURAS', 'Frases largas',
                 'Casi todo va bajo ligaduras que abarcan dos y hasta siete notas. Si cortas la '
                 'frase en cada compás, tocas las notas pero no la canción.'),
                ('LA SEMICORCHEA', 'Corta, y al final',
                 'En el c. 1 la corchea con puntillo se lleva tres cuartos del tiempo y la '
                 'semicorchea el último. Es el único sitio de la pieza con esa figura.'),
            ],
            pie='Es una pieza para tocar con la línea, no con la nota: las ligaduras de frase son '
                'más importantes que cualquier digitación. Con tu base, lo difícil es dejar de '
                'respirar cada compás.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido', D1, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'cc. 11-12 · medido: ahora dos negras por compás',
             [n('A3'), n('E4'), n('G3'), n('D4')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada, y el compás es 2/4: dos negras por compás.',
            'Pone "Adagio" y "mp", y salta a "mf" en el c. 11. No trae número de metrónomo.',
            'Hay barras de repetición con casillas de primera y segunda vez.',
            'Casi todo va bajo ligaduras largas de frase.',
            'En el c. 1 hay una corchea con puntillo y una semicorchea.',
            'Del c. 11 en adelante la izquierda deja las blancas y toca dos negras por compás.',
        ],
        reto='Que la línea no se corte. La ligadura de frase pide una respiración cada cuatro '
             'compases, no una por compás, y con un 2/4 tan corto el instinto es respirar '
             'cada dos tiempos.',
        truco='Canta la melodía en voz alta y marca con lápiz dónde tienes que respirar de verdad; '
              'ese es el sitio donde acaba cada ligadura. Después toca solo la derecha sin '
              'cortar donde no has marcado.',
        sabias='En la película, la melodía que abre el tema no la toca un piano sino una flauta '
               'irlandesa, el "low whistle", y se oye antes de que cante nadie. Muchos pianistas '
               'la tocan intentando imitar ese sonido: una línea larga sin ataque.',
        qr=dict(titulo='Escúchala',
                texto='Escucha dónde respira la voz y compáralo con las ligaduras de tu partitura: '
                      'coinciden. Las ligaduras de frase marcan exactamente lo que el cantante '
                      'hace sin pensarlo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas que ya sabes y una nueva: las blancas de la izquierda, la melodía en '
              'corcheas y la línea larga del segundo bloque, que es donde se decide la pieza.',
        reglas=['LA LÍNEA NO SE CORTA', 'LA IZQUIERDA CAMBIA EN EL C. 11',
                'LA CORTA ENTRA AL FINAL'],
        bloques=[
            dict(num=1, titulo='El primer compás, con la semicorchea',
                 pista='c. 1 · MEDIDO sobre tu partitura · corchea con puntillo y semicorchea '
                       'seguidas de dos corcheas',
                 sistemas=[
                     dict(cap='a) el c. 1 y el c. 2 literales · la pareja larga-corta ocupa un tiempo '
                              'entero y la semicorchea cae en la "a"',
                          events=D1 + [n('B4', 'e'), n('C5', 'e'), sil('e'), n('C5', 'e')],
                          bars=2, matiz='mp'),
                     dict(cap='b) la misma pareja larga-corta sobre otra nota · andamio · el '
                              'puntillo alarga la primera y la semicorchea llega tarde, en la "a"',
                          events=[n('G4', 'e.'), n('G4', 's'), n('A4', 'e'), n('B4', 'e'),
                                  n('A4', 'e'), n('G4', 'e'), sil('e'), n('E4', 'e')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Las dos manos, los dos primeros compases',
                 pista='cc. 1-2 · MEDIDO · la izquierda es una blanca por compás, Do y Sol',
                 sistemas=[
                     dict(cap='a) el bajo no se mueve · deja que suene el compás entero aunque la '
                              'derecha ya vaya por la tercera nota',
                          events=[ac(('C3', 'C5'), 'e.'), n('C5', 's'), n('C5', 'e'), n('C5', 'e'),
                                  ac(('G3', 'B4'), 'e'), n('C5', 'e'), sil('e'), n('C5', 'e')],
                          bars=2, manos='sostiene'),
                 ]),
            dict(tipo='nota',
                 etiqueta='AQUÍ CAMBIA LA PIEZA: EL C. 11',
                 texto='Hasta el c. 10 la izquierda hace una blanca por compás. En el 11, con el '
                       '"mf" y la barra de repetición, pasa a dos negras: una nota grave y otra '
                       'aguda. Si tocas el bloque entero con la misma mano izquierda de antes, '
                       'la pieza no sube; se queda en donde estaba.'),
            dict(num=3, titulo='La derecha del segundo bloque',
                 pista='cc. 11-14 · MEDIDO nota a nota · una melodía larga bajo dos ligaduras',
                 sistemas=[
                     dict(cap='a) la primera ligadura abarca dos compases · el Re de puntillo no '
                              'se corta: lleva a la corchea del Sol',
                          events=[dict(pitch='C5', dur='h', lig=1), n('D5', 'q.'), n('G4', 'e')],
                          bars=2),
                     dict(cap='b) la segunda abarca siete notas de un tirón · respira solo donde '
                              'acaba',
                          events=[sil('q.'), dict(pitch='G4', dur='e', lig=6), n('G5'),
                                  n('F5', 'e'), n('E5', 'e'), n('D5'), n('E5', 'e'),
                                  n('F5', 'e')],
                          bars=3, show_time=False),
                 ]),
            dict(num=4, titulo='La izquierda del segundo bloque',
                 pista='cc. 11-14 · MEDIDO nota a nota · una nota grave y una aguda por compás',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) La, Sol, Fa y Sol de grave, y Mi, Re, Do y Re de agudo · el '
                              'movimiento es el de las manecillas: sube y baja a la vez',
                          events=I_11_14, bars=4, clef='bass'),
                 ]),
        ] + bloques_extra('Do mayor', 16, 'C5', 'C3',
                          'dos tiempos por compás: la línea corre más que el pulso',
                          desde=5, time_sig=(2, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Titanic · para casa',
            intro='Quince minutos al día. Se estudia por frases, no por compases.',
            bloques=[
                plan((4, 'El c. 1 y la semicorchea, diez veces'),
                     (5, 'La derecha sola, cc. 11-14, sin cortar la línea'),
                     (5, 'La izquierda sola, cc. 11-14, grave y agudo'),
                     (5, 'Las dos manos, el bloque entero')),
                metronomo('Empieza a ♩ = 44 con la derecha sola y sube de cuatro en cuatro '
                          'mientras la semicorchea siga sonando más corta que la corchea.',
                          'Tu partitura solo pone "Adagio": el número lo decides tú y lo apuntas '
                          'a lápiz. Si a una velocidad la semicorchea suena igual que una '
                          'corchea, baja cuatro y repítelo.',
                          titulo='A qué velocidad te sale'),
                nombres(['C5', 'D5', 'G4', 'G5', 'F5', 'E5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='son de los cc. 1 y 11-14 de la derecha'),
                colorear(D1 + [n('D5', 'q.'), n('G4', 'e')],
                         ['La corchea con puntillo, de azul.',
                          'La semicorchea, de rojo.',
                          'Las corcheas sueltas, de verde.'],
                         titulo='Colorea según la figura',
                         pista='el c. 1 y el c. 12 de tu partitura'),
                diferencias(D_13 + D_14,
                            D_13 + [n('D5'), n('F5', 'e'), n('F5', 'e')],
                            cuantas=1,
                            titulo='Busca la diferencia en la melodía',
                            pista='arriba, los cc. 13 y 14 de tu partitura · abajo, los mismos con '
                                  'una nota cambiada'),
                para_clase('El bloque de los cc. 11-14 con las dos manos, y dónde has marcado las '
                           'respiraciones. Si la semicorchea del c. 1 sigue sonando como corchea, '
                           'tráela.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
