# -*- coding: utf-8 -*-
"""Un beso y una flor, de Nino Bravo — pieza 16 de Aida. Formato ADULTO
   exigente.

   Abre la ultima etapa, la de la mano abierta y la semicorchea. Y es la pieza
   donde por primera vez las semicorcheas NO van en fila: van sueltas, mezcladas
   con corcheas dentro del mismo golpe, que es bastante mas dificil que una
   carrerilla de cuatro iguales.

   Lo comprobado sobre el PDF de SU carpeta (Musescore · Musicaymaestro.com,
   2 paginas, vectorial; el mismo archivo, byte a byte, que el de Josep):

     - Detras de la clave hay **UN BEMOL**: Fa mayor.
     - El compas esta escrito con la **C** de compasillo, que es **4/4**.
     - Arriba pone **Allegro**, sin numero de metronomo.
     - Trae el **CIFRADO IMPRESO** encima del pentagrama: F, Dm, B♭, A y Am.
     - La derecha lleva semicorcheas sueltas; la izquierda, OCTAVAS.

   LAS ALTURAS Y LAS FIGURAS de los cuatro primeros compases, medidas a 150 ppp
   sobre las cinco lineas de cada pentagrama, y las figuras leidas contando las
   barras de cada grupo (una barra = corchea, dos = semicorchea):

       DERECHA  c. 1  silencio de corchea · La4 La4 (semicorcheas) ·
                      La4 (corchea) La4 Si4 (semicorcheas) ·
                      Si4 (semicorchea) La4 (corchea) Sol4 (semicorchea) ·
                      La4 (negra)
                c. 2  igual hasta la mitad, y el ultimo golpe cambia:
                      silencio de corchea · La4 La4 (semicorcheas) ·
                      La4 (corchea) La4 Do5 (semicorcheas) ·
                      Do5 Si4 La4 Sol4 (cuatro corcheas)
                c. 3  Fa4 (blanca) · Fa4 Mi4 Fa4 Sol4 (corcheas)
                c. 4  Fa4 (blanca) · silencio de blanca

       IZQUIERDA  c. 1 y c. 2  Fa2+Fa3 (blanca) · Fa2+Fa3 (negra con puntillo) ·
                               Mi2+Mi3 (corchea)
                  c. 3 y c. 4  Re2+Re3 (blanca) · Re2+Re3 (negra con puntillo) ·
                               Do2+Do3 (corchea)

   Los cuatro compases cierran en 4. El c. 1 lo hace asi: 0,5 + 0,25x2 +
   (0,5 + 0,25 + 0,25) + (0,25 + 0,5 + 0,25) + 1.

   LO QUE COSTO LEER, y es justo lo que hay que contarle: los grupos de la
   derecha NO son cuatro semicorcheas seguidas. En el tercer golpe del c. 1 la
   barra de abajo esta PARTIDA —un trocito a la izquierda y otro a la derecha—
   y eso quiere decir semicorchea, corchea, semicorchea. Se lee mirando cuantas
   barras toca cada plica, no el grupo entero.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, semi, reto, plan, cifrado, colorear,
                      figuras, acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

_B = [16000]


def gr(*eventos):
    """Un grupo barrado: la barra la marca el golpe, no la figura.

       Se escribe a mano y no con `corch`/`semi` porque aqui cada golpe mezcla
       corcheas y semicorcheas, que es el rasgo de la pieza."""
    _B[0] += 1
    for e in eventos:
        e['beam'] = _B[0]
    return list(eventos)


# Los cuatro primeros compases de la DERECHA, medidos. Cita literal.
C1 = ([sil('e')] +
      gr(n('A4', 's'), n('A4', 's')) +
      gr(n('A4', 'e'), n('A4', 's'), n('B4', 's')) +
      gr(n('B4', 's'), n('A4', 'e'), n('G4', 's')) +
      [n('A4')])
C2 = ([sil('e')] +
      gr(n('A4', 's'), n('A4', 's')) +
      gr(n('A4', 'e'), n('A4', 's'), n('C5', 's')) +
      gr(n('C5', 'e'), n('B4', 'e'), n('A4', 'e'), n('G4', 'e')))
C3 = [n('F4', 'h')] + gr(n('F4', 'e'), n('E4', 'e'), n('F4', 'e'), n('G4', 'e'))
C4 = [n('F4', 'h'), sil('h')]

# Y la IZQUIERDA: octavas que aguantan. Tambien medido.
IZQ_F = [ac(('F2', 'F3'), 'h'), ac(('F2', 'F3'), 'q.'), ac(('E2', 'E3'), 'e')]
IZQ_D = [ac(('D2', 'D3'), 'h'), ac(('D2', 'D3'), 'q.'), ac(('C2', 'C3'), 'e')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=16, nivel='intermedio',
    slug='UnBesoYUnaFlor', formato='adulto',
    titulo_corto='Un beso y una flor', time_sig=(4, 4), key_sig='Fa mayor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'Un beso y una flor.pdf'),
    yt='https://www.youtube.com/results?search_query=un+beso+y+una+flor+piano',

    ficha=dict(
        titulo='Un beso y una flor',
        autor='Nino Bravo · arr. Musicaymaestro.com',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', '4/4 (C)'),
               ('Carácter', 'Allegro'), ('Armadura', 'Un bemol'),
               ('Trae', 'Cifrado impreso')],
        titulo_ritmos='El compás 1, medido',
        pie_ritmos='Arriba, el c. 1 de la derecha MEDIDO en tu partitura: mira cuántas barras toca '
                   'cada plica, porque dentro de un mismo golpe hay corcheas y semicorcheas. Abajo, '
                   'la izquierda de ese mismo compás: octavas que aguantan.',
        armonia=dict(
            titulo='Cinco letras y una mano abierta',
            tarjetas=[
                ('EL CIFRADO', 'F Dm B♭ A Am',
                 'Cinco letras impresas encima del pentagrama. Son las mismas cinco de toda la '
                 'canción: aprendidas esas, ya sabes por dónde va la armonía entera.'),
                ('LA OCTAVA', 'Los dos extremos',
                 'La izquierda toca la misma nota con el 5 y con el 1, separadas por ocho teclas '
                 'blancas. La mano se abre y se queda abierta: no hay que volver a medirla en cada '
                 'compás.'),
                ('SEMICORCHEAS SUELTAS', 'No en fila',
                 'Cuatro semicorcheas seguidas se aprenden rápido. Lo de aquí es otra cosa: dentro '
                 'de un golpe hay una corta, una larga y otra corta, y eso solo sale contando.'),
                ('EL BEMOL', 'Si en tecla negra',
                 'Fa mayor: todos los Si van a la negra, incluido el Si♭ del acorde de B♭, que es '
                 'el tercero que trae impreso tu partitura.'),
            ],
            pie='La izquierda de esta pieza no tiene ritmo que aprender: blanca, negra con puntillo '
                'y corchea, y vuelta a empezar. Lo suyo es la apertura. Colócala y no la muevas: '
                'todo el trabajo de la semana está en la mano derecha.',
        ),
        ritmos=[
            ('DERECHA', 'el c. 1, MEDIDO · cortas y largas en el mismo golpe',
             C1, OCRE, 'treble', 'Fa mayor'),
            ('IZQUIERDA', 'el c. 1, medido · octavas que aguantan',
             list(IZQ_F), AZUL, 'bass', 'Fa mayor'),
        ],
        especial=[
            'Detrás de la clave hay un bemol: la tonalidad es Fa mayor.',
            'El compás está escrito con una C, y quiere decir 4/4.',
            'Arriba pone Allegro, pero no hay número de metrónomo.',
            'Encima del pentagrama están impresas las letras F, Dm, B♭, A y Am.',
            'La derecha mezcla corcheas y semicorcheas dentro del mismo golpe.',
            'La izquierda toca octavas: la misma nota con el 5 y con el 1.',
            'Los compases 3 y 4 son de notas largas: ahí se respira.',
        ],
        reto='Leer las figuras de una en una. En esta pieza un grupo barrado no dice "todas '
             'iguales": hay que mirar cuántas barras toca cada plica, porque dentro del mismo golpe '
             'conviven la corchea y la semicorchea.',
        truco='Parte cada tiempo en cuatro y di "1-2-3-4" mientras lo tocas. Una corchea ocupa dos '
              'de esos cuatro y una semicorchea, uno. Con el tiempo partido, el grupo se lee solo.',
        sabias='Nino Bravo la grabó en 1972 y murió meses después, a los veintiocho años, en un '
               'accidente de coche cuando iba a un concierto. La canción habla de irse lejos y '
               'volver, y acabó siendo lo contrario: la que se quedó.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en la entrada de cada frase: no empieza en el golpe, empieza justo '
                      'después y con dos notas rápidas. Ese arranque es toda la pieza.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí no hay notas difíciles: hay figuras difíciles. Casi todo el trabajo de esta '
              'semana es contar en cuatro partes y colocar cada nota en la suya.',
        reglas=['TODOS LOS SI, EN TECLA NEGRA', 'CUENTA CADA TIEMPO EN CUATRO',
                'LA IZQUIERDA SE ABRE Y NO SE MUEVE'],
        bloques=[
            dict(num=1, titulo='El compás 2, tal y como está escrito',
                 pista='c. 2 · MEDIDO en tu partitura · los dos primeros golpes mezclan corchea y '
                       'semicorchea, y el último son cuatro corcheas iguales',
                 sistemas=[
                     dict(cap='a) el compás 2 entero · mira cuántas barras toca cada plica antes de '
                              'tocarlo',
                          events=list(C2), bars=1, key_sig='Fa mayor'),
                     dict(cap='b) y el mismo dibujo con todo en corcheas iguales · NO es lo que pone '
                              'tu partitura: es para oír qué se pierde al igualarlo',
                          events=corch(['A4', 'A4']) + corch(['A4', 'A4']) +
                                 corch(['C5', 'C5']) + corch(['B4', 'A4']),
                          bars=1, show_time=False, key_sig='Fa mayor'),
                     dict(cap='c) y las cuatro semicorcheas seguidas, que es lo fácil · andamio, '
                              'para tener con qué comparar',
                          events=semi(['A4', 'B4', 'C5', 'B4']) + semi(['A4', 'G4', 'A4', 'B4']) +
                                 [n('C5'), n('A4')],
                          bars=1, show_time=False, key_sig='Fa mayor'),
                     dict(cap='d) y el golpe que más cuesta, repetido cuatro veces · andamio: '
                              'corta, larga y corta, que es el tercer golpe del c. 1',
                          events=gr(n('A4', 's'), n('G4', 'e'), n('F4', 's')) +
                                 gr(n('G4', 's'), n('A4', 'e'), n('B4', 's')) +
                                 gr(n('C5', 's'), n('B4', 'e'), n('A4', 's')) +
                                 gr(n('B4', 's'), n('A4', 'e'), n('G4', 's')),
                          bars=1, show_time=False, key_sig='Fa mayor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE LEE UN GRUPO BARRADO',
                 texto='La barra de arriba une el grupo; las de abajo dicen la figura. Si una plica '
                       'toca UNA barra, es corchea; si toca DOS, es semicorchea. Cuando dentro del '
                       'grupo hay de las dos, la barra de abajo aparece PARTIDA: un trocito pegado '
                       'a la plica de cada semicorchea. Eso es lo que pasa en el tercer golpe del '
                       'compás 1 de tu partitura, y por eso ese golpe suena corta-larga-corta y no '
                       'tres notas iguales.'),
            dict(num=2, titulo='La izquierda: octavas que aguantan',
                 pista='cc. 1 a 4 de la mano izquierda · MEDIDO · el mismo ritmo en los cuatro',
                 sistemas=[
                     dict(cap='a) los cc. 1 y 2 · blanca, negra con puntillo y corchea, dos veces',
                          events=IZQ_F + IZQ_F, bars=2, clef='bass', key_sig='Fa mayor'),
                     dict(cap='b) y los cc. 3 y 4, que es el mismo ritmo movido de sitio · la mano '
                              'no cambia de forma, solo de tecla',
                          events=IZQ_D + IZQ_D, bars=2, clef='bass', show_time=False,
                          key_sig='Fa mayor'),
                     dict(cap='c) y solo la nota de abajo de cada octava, para oír el camino del '
                              'bajo · en tu partitura son dos notas a la vez',
                          events=[n('F2', 'h'), n('F2', 'q.'), n('E2', 'e'),
                                  n('D2', 'h'), n('D2', 'q.'), n('C2', 'e')],
                          bars=2, clef='bass', show_time=False, key_sig='Fa mayor'),
                     dict(cap='d) y las cuatro primeras letras de acorde en octavas, una por compás · '
                              'andamio sobre el cifrado que trae impreso tu partitura',
                          events=[ac(('F2', 'F3'), 'w'), ac(('D2', 'D3'), 'w'),
                                  ac(('Bb1', 'Bb2'), 'w'), ac(('A1', 'A2'), 'w')],
                          bars=4, clef='bass', show_time=False, key_sig='Fa mayor'),
                 ]),
            dict(num=3, titulo='Los compases 3 y 4, donde se respira',
                 pista='cc. 3-4 con las dos manos · MEDIDO · dos notas largas y cuatro corcheas',
                 sistemas=[
                     dict(cap='a) los dos compases con las dos manos · la derecha se para y la '
                              'izquierda sigue haciendo lo mismo de siempre',
                          events=[ac(('D2', 'D3', 'F4'), 'h'), ac(('D2', 'D3', 'F4'), 'e'),
                                  n('E4', 'e'), n('F4', 'e'), ac(('C2', 'C3', 'G4'), 'e'),
                                  ac(('D2', 'D3', 'F4'), 'h'), ac(('D2', 'D3'), 'q.'),
                                  ac(('C2', 'C3'), 'e')],
                          bars=2, manos='sostiene', key_sig='Fa mayor'),
                     dict(cap='b) y la derecha sola de esos dos compases, para leer las cuatro '
                              'corcheas sin la mano de abajo encima',
                          events=C3 + C4, bars=2, show_time=False, key_sig='Fa mayor'),
                     dict(cap='c) y las cuatro corcheas del c. 3 repetidas, para que la mano se '
                              'quede colocada · andamio sobre esas mismas cuatro notas',
                          events=corch(['F4', 'E4']) + corch(['F4', 'G4']) +
                                 corch(['A4', 'G4']) + corch(['F4', 'E4']),
                          bars=1, show_time=False, key_sig='Fa mayor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Los cuatro primeros compases con las dos manos, contando cada tiempo en '
                       'cuatro partes en voz alta. Tu edición pone Allegro pero no da número, así '
                       'que empieza a la velocidad en la que puedas contar en cuatro sin '
                       'atragantarte, y apunta a lápiz cuál es. Y mira las letras de acorde: están '
                       'impresas y te dicen dónde va la mano izquierda antes de leer una sola nota.'),
        ] + bloques_extra('Fa mayor', 111, 'F4', 'F2',
                          'las semicorcheas sueltas: dentro de un golpe hay cortas y largas',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Un beso y una flor · para casa',
            intro='Quince minutos al día, y los cinco primeros contando sin tocar. Esta pieza se '
                  'gana con la cuenta, no con los dedos.',
            bloques=[
                reto('Distinguir la corchea de la semicorchea DENTRO del mismo golpe.',
                     'Cuenta cada tiempo en cuatro partes en voz alta mientras tocas. Si el grupo te '
                     'sale con las tres notas iguales, es que estás contando el golpe entero en vez '
                     'de sus cuatro partes.'),
                plan((5, 'Contar "1-2-3-4" por tiempo y decir dónde cae cada nota'),
                     (4, 'El c. 2 de la derecha, despacio y con la cuenta en voz alta'),
                     (3, 'La izquierda sola: las octavas de los cc. 1 a 4'),
                     (3, 'Los cc. 1 a 4 con las dos manos')),
                cifrado([('F', 'Fa'), ('Dm', 'Re menor'), ('Bb', 'Si bemol'), ('Am', 'La menor')],
                        ['¿Cuáles de los cuatro son menores?',
                         '¿Cuál de los cuatro lleva el Si bemol de la armadura en su nombre?'],
                        titulo='Las letras de acorde que trae tu partitura',
                        pista='están impresas encima del pentagrama · escribe sus tres notas'),
                colorear(list(C1),
                         [('las semicorcheas', 'las que tocan dos barras'),
                          ('las corcheas', 'las que tocan una')],
                         titulo='Colorea por figuras tu compás 1',
                         pista='queda una sin color: es la negra del final'),
                figuras([('q', 'negra'), ('e', 'corchea'), ('s', 'semicorchea'), ('h', 'blanca')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='y di cuántas semicorcheas caben en una negra'),
                acuerdate('Una octava son dos notas con el mismo nombre y ocho teclas blancas de '
                          'distancia. Suenan tan parecidas que el oído las toma por una sola nota '
                          'más gorda, y por eso la izquierda de esta pieza se oye llena tocando '
                          'solo una nota de la armonía.',
                          etiqueta='QUÉ ES UNA OCTAVA'),
                para_clase('Los cuatro primeros compases con las dos manos, a la velocidad que te '
                           'salga la cuenta en cuatro partes. Y tráete marcado con lápiz dónde '
                           'están las semicorcheas del compás 1: lo miramos juntas.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
