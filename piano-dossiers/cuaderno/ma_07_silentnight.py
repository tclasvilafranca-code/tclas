# -*- coding: utf-8 -*-
"""Silent Night (Franz Gruber) — pieza 7 de Martina (NAVIDAD, una semana). ADULTO
   exigente, tono de niña que empieza de cero.

   Lo comprobado sobre el PDF de su carpeta de Drive (versión de Piano Moonlight,
   Musescore, 1 página, VECTORIAL), medido a 300 ppp y mirado a 130 ppp:

     - Detrás de la clave no hay nada: Do mayor. 3/4. Trae ♩ = 100. 24 compases,
       con barra final.
     - Trae CIFRADO impreso (C, F, G7/B, G7/D, G/B), las notas de la izquierda escritas
       con letra debajo del pentagrama y la digitación impresa.
     - Solo negras con puntillo, negras, corcheas y blancas (con y sin puntillo).
     - MEDIDO, mano derecha:
       c. 1: Sol4 (negra con puntillo) · La4 (corchea) · Sol4 (negra)
       c. 2: Mi4 (blanca con puntillo)         cc. 3 y 4: lo mismo
       c. 5: Re5 (blanca) · Re5 (negra)        c. 6: Si4 (blanca con puntillo)
       c. 7: Do5 (blanca) · Do5 (negra)        c. 8: Sol4 (blanca con puntillo)
       c. 9: La4 (blanca) · La4 (negra)    c. 10: Do5 (negra con puntillo) · Si4 (corchea) · La4
     - MEDIDO, mano izquierda: tres negras por compás que suben.
       cc. 1-4: Do3 · Mi3 · Sol3        c. 5: Si2 · Fa3 · Sol3        c. 6: Re3 · Fa3 · Sol3
       cc. 7-8: Do3 · Mi3 · Sol3        c. 9: Fa3 · La3 · Do4
     - Los dos últimos compases: una blanca ligada a otra, y un silencio de negra.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, plan, metronomo, ordenar, contar, teclado,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: derecha, cc. 1-2 y 5-8
C1 = [n('G4', 'q.'), n('A4', 'e'), n('G4')]
C2 = [n('E4', 'h.')]
C5 = [n('D5', 'h'), n('D5')]
C6 = [n('B4', 'h.')]
C7 = [n('C5', 'h'), n('C5')]
C8 = [n('G4', 'h.')]
# MEDIDO: izquierda, cc. 1, 5, 6 y 9
L1 = [n('C3'), n('E3'), n('G3')]
L5 = [n('B2'), n('F3'), n('G3')]
L6 = [n('D3'), n('F3'), n('G3')]
L9 = [n('F3'), n('A3'), n('C4')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=7, nivel='iniciación', slug='SilentNight',
    formato='adulto',
    titulo_corto='Silent Night', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source', 'Silent-night'),
    yt='https://www.youtube.com/results?search_query=silent+night+easy+piano',

    ficha=dict(
        titulo='Silent Night',
        autor='Franz Gruber · versión de Piano Moonlight · NAVIDAD',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Tempo', '♩ = 100'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Una')],
        titulo_ritmos='El c. 1 de cada mano, medido',
        pie_ritmos='Arriba, medido sobre tu partitura: una negra con puntillo, una corchea y una '
                   'negra. Abajo, medido: tres negras que suben, Do, Mi y Sol.',
        armonia=dict(
            titulo='Un vals despacio, con las letras de los acordes puestas',
            tarjetas=[
                ('EL 3/4', 'Un, dos, tres',
                 'Tres golpes en cada compás, como un vals. El primero pesa un poco más. Es un '
                 'compás distinto del 4/4, y lo único que hay que hacer es contar hasta tres.'),
                ('EL RITMO', 'Largo y corto',
                 'El c. 1 empieza con una negra con puntillo (un golpe y medio), una corchea (medio '
                 'golpe) y una negra (un golpe): suma tres, justo el compás.'),
                ('LAS LETRAS', 'C, F, G7',
                 'Encima de la música hay letras: son los acordes. Tu partitura incluso trae debajo '
                 'las notas de cada uno (C es Do, Mi, Sol), para que no tengas que adivinar.'),
                ('LA IZQUIERDA', 'Tres negras',
                 'Cada compás de la izquierda son tres negras que suben: Do, Mi y Sol. Es el '
                 'acorde, tocado nota a nota en vez de todo junto.'),
            ],
            pie='Son 24 compases y una página. La melodía es la que ya conoces de oído; lo que '
                'tienes que aprender ahora es cómo se escribe.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido', C1, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'c. 1 · medido', L1, AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: todo son teclas blancas.',
            'El compás es 3/4 y arriba viene impreso el metrónomo: negra = 100.',
            'Encima del pentagrama van las letras de los acordes: C, F, G7/B, G7/D.',
            'Debajo de la izquierda vienen escritas las notas de los acordes, con letra.',
            'La partitura trae los números de dedo impresos.',
            'Acaba con una blanca ligada a otra y un silencio de negra.',
        ],
        reto='Contar tres y no cuatro. Con las canciones de cuatro golpes recién tocadas, la mano '
             'se va al cuatro sin que te des cuenta, y el vals se rompe.',
        truco='Cuenta "UN, dos, tres" en voz alta antes de tocar una sola nota y sigue contando '
              'mientras tocas: el "UN" cae siempre en la primera nota de cada compás.',
        sabias='Silent Night se estrenó en Navidad de 1818 en una iglesia de Austria, con guitarra, '
               'porque el órgano se había estropeado. La letra la escribió el cura, Joseph Mohr, y '
               'la música Franz Gruber, el maestro del pueblo.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la melodía y marca el pie de tres en tres. Verás que el primer '
                      'golpe de cada compás es el más largo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia como un vals: contando tres en voz alta, primero cada mano sola y luego las '
              'dos. La melodía ya la sabes de oído; aquí se aprende a leerla.',
        reglas=['CUENTA "UN, DOS, TRES"', 'EL PRIMERO PESA UN POCO MÁS', 'UNA MANO Y DESPUÉS LAS DOS'],
        bloques=[
            dict(num=1, titulo='El ritmo largo-corto de los cc. 1 y 2',
                 pista='cc. 1-2 · medidos sobre tu partitura · una negra con puntillo, una corchea '
                       'y una negra, y una blanca con puntillo',
                 sistemas=[
                     dict(cap='a) la negra con puntillo dura uno y medio, la corchea completa el '
                              'golpe · después, una blanca con puntillo llena el compás',
                          events=C1 + C2, bars=2),
                     dict(cap='b) el mismo ritmo en otras notas · andamio · para comprobar que '
                              'sabes el ritmo y no la canción',
                          events=[n('C5', 'q.'), n('D5', 'e'), n('C5'), n('A4', 'h.')], bars=2,
                          show_time=False),
                 ]),
            dict(num=2, titulo='La parte del medio, cc. 5-8',
                 pista='cc. 5-8 · medidos sobre tu partitura · blancas y negras que bajan por '
                       'escalones',
                 sistemas=[
                     dict(cap='a) Re y Re, Si; Do y Do, Sol · una blanca y una negra, y una blanca '
                              'con puntillo que cierra la frase',
                          events=C5 + C6 + C7 + C8, bars=4),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE CUENTA EN TRES',
                 texto='En un compás de 3/4 caben tres negras, y la primera pesa un poco más: es la '
                       'forma de un vals. Si lo cuentas en cuatro, la música se estira y se rompe. '
                       'Cuenta tres con la voz y con el pie, y la melodía cae donde tiene que '
                       'caer.'),
            dict(num=3, titulo='La izquierda: tres negras que suben',
                 pista='cc. 1-4, 5 y 6 · medidos sobre tu partitura · el acorde, nota a nota',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) Do, Mi, Sol, cuatro veces · es el acorde de C tocado de abajo '
                              'arriba, y se estudia hasta que salga sin mirar',
                          events=L1 * 4, bars=4, clef='bass'),
                     dict(cap='b) y los dos acordes de los cc. 5 y 6, que llevan la letra G7 · '
                              'el bajo es Si en el primero y Re en el segundo',
                          events=L5 + L6, bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=4, titulo='Las dos manos, con la derecha simplificada',
                 pista='andamio · la derecha en negras para juntar las manos antes de poner el '
                       'ritmo de verdad',
                 sistemas=[
                     dict(cap='a) el acorde de Do subiendo en la izquierda y tres negras sencillas '
                              'arriba · cuando salga, vuelve al ritmo largo-corto',
                          events=[ac(('C3', 'G4')), ac(('E3', 'A4')), ac(('G3', 'G4')),
                                  ac(('C3', 'E4'), 'h.')],
                          bars=2, manos='dobla'),
                 ]),
            dict(num=5, titulo='El final: una nota atada a otra, cc. 23-24',
                 pista='cc. 23-24 · medidos sobre tu partitura · la ligadura une dos blancas',
                 sistemas=[
                     dict(cap='a) una blanca con puntillo ligada a una blanca, y un silencio de '
                              'negra · se toca una vez y suena cinco golpes; el silencio se cuenta',
                          events=[dict(n('C4', 'h.'), lig=True), n('C4', 'h'), sil('q')],
                          bars=2),
                 ]),
            dict(num=6, titulo='Los tres acordes con letra, juntos',
                 pista='andamio sobre las letras IMPRESAS en tu partitura (C, F y G7) · las tres '
                       'notas a la vez',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) C, F y G7, cada uno en un compás · el acorde de G7 lleva cuatro '
                              'notas: Sol, Si, Re y Fa',
                          events=[ac(('C3', 'E3', 'G3'), 'h.'), ac(('F2', 'A2', 'C3'), 'h.'),
                                  ac(('G2', 'B2', 'D3', 'F3'), 'h.')],
                          bars=3, clef='bass'),
                 ]),
            dict(num=7, titulo='La segunda frase, cc. 9 y 10',
                 pista='cc. 9-10 · medidos sobre tu partitura · el ritmo largo-corto vuelve, ahora '
                       'bajando',
                 sistemas=[
                     dict(cap='a) La blanca y La negra; y después Do con puntillo, Si en corchea y '
                              'La · el largo-corto del principio, pero hacia abajo',
                          events=[n('A4', 'h'), n('A4'), n('C5', 'q.'), n('B4', 'e'), n('A4')],
                          bars=2),
                     dict(cap='b) el mismo gesto empezando una nota más arriba · andamio · para ver '
                              'si el largo-corto sale igual con otras notas',
                          events=[n('B4', 'h'), n('B4'), n('D5', 'q.'), n('C5', 'e'), n('B4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=8, titulo='Las blancas con puntillo, contadas',
                 pista='cc. 2, 4, 6 y 8 · medidos sobre tu partitura · una nota que dura el compás '
                       'entero',
                 sistemas=[
                     dict(cap='a) Mi, Si y Sol, cada una una blanca con puntillo · tres golpes con '
                              'la tecla bajada: "un, dos, tres"',
                          events=[n('E4', 'h.'), n('B4', 'h.'), n('G4', 'h.')], bars=3),
                 ]),
        ] + bloques_extra('Do mayor', 7, 'E4', 'C3',
                          'el vals se cuenta en tres y el primer golpe pesa un poco más',
                          desde=9, time_sig=(3, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Silent Night · para casa',
            intro='Diez o quince minutos al día. Es la semana corta de Navidad, y la melodía ya '
                  'la sabes: lo que se entrena es leerla y contarla en tres.',
            bloques=[
                plan((3, 'Contar "un, dos, tres" y marcar el golpe con el pie, sin tocar'),
                     (4, 'La derecha sola, cc. 1-8, con el ritmo largo-corto'),
                     (4, 'La izquierda sola: Do, Mi, Sol, y los acordes de los cc. 5 y 6'),
                     (4, 'Las dos manos, cc. 1-4, despacio')),
                metronomo('Empieza a ♩ = 60 con la derecha sola y sube de diez en diez hasta 100, '
                          'que es el número que trae tu partitura.',
                          'Si a una velocidad pierdes el golpe, no subas: baja diez y repítelo.',
                          titulo='A qué velocidad te sale'),
                ordenar(['Tocar los cc. 1-4 con las dos manos.',
                         'Contar "un, dos, tres" en voz alta, sin tocar.',
                         'Tocar los cc. 1-4 con la derecha sola.',
                         'Tocar los cc. 1-4 con la izquierda sola.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='del más fácil al más completo · uno de ellos va antes de tocar nada'),
                contar(C1 + C2,
                       ['¿Cuántas negras hay?', '¿Cuántas corcheas hay?',
                        '¿Cuántos golpes dura el Mi del c. 2?'],
                       titulo='Cuenta sobre los cc. 1 y 2',
                       pista='son los dos primeros compases de la derecha de tu partitura'),
                teclado({4: 1, 5: 2, 2: 3},
                        ['Escribe el nombre de las tres teclas marcadas.',
                         'La número 1 es el Sol, la nota con la que empieza la melodía.'],
                        titulo='En el teclado',
                        pista='son las tres notas distintas del primer compás y el segundo'),
                para_clase('Los cc. 1-8 con la derecha, contando en voz alta, y los cc. 1-4 con las '
                           'dos manos. Si el vals se te rompe en algún sitio, dime en cuál.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
