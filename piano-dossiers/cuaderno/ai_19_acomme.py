# -*- coding: utf-8 -*-
"""A comme amour, de Paul de Senneville (Richard Clayderman) — pieza 19 y
   ultima de Aida. Formato ADULTO exigente.

   Es el reto del curso, y va la ultima a proposito: llega detras del bajo
   obstinado de Pachelbel y del dibujo de mano del Preludio de Bach, que son las
   dos que preparan lo que aqui hace falta —la mano abierta y las semicorcheas
   seguidas— y llega con el 6/8, el 2/4, el doble puntillo y la semicorchea
   suelta ya trabajados en las etapas anteriores.

   Lo comprobado sobre el PDF de SU carpeta (musicaparadisfrutar.com, 1 pagina,
   vectorial; el mismo archivo, byte a byte, que el de Jose Maria, Josep y Nel):

     - Detras de la clave hay **UN SOSTENIDO** (Fa): Mi menor.
     - **4/4**.
     - Trae tempo impreso: **negra = 69**.
     - Trae el **CIFRADO IMPRESO** encima del pentagrama: Em, B7, E7, Am, A7 y
       Dm. Son seis letras y cubren la pieza entera.
     - Semicorcheas de principio a fin: 45 pares de barras dobles medidos.

   LAS ALTURAS Y LAS FIGURAS de los dos primeros compases, medidas a 150 ppp
   sobre las cinco lineas de cada pentagrama, y las figuras leidas contando las
   barras que toca cada plica:

       DERECHA  c. 1  silencio de blanca · silencio de negra · Si3 (negra)
                c. 2  Si4 (negra) LIGADA a Si4 (corchea con puntillo) ·
                      Re5 (semicorchea) ·
                      Re5 · Do5 · Do5 · Si4 (semicorcheas) ·
                      Si4 · Do5 · Si4 · Sol4 (semicorcheas)

       IZQUIERDA  c. 1  compas entero de silencio
                  c. 2  Mi3 + Sol3 + Si3 en REDONDA: el acorde de Mi menor,
                        que es la primera letra impresa del cifrado

   El c. 2 cierra en 4: 1 + 0,75 + 0,25 + 1 + 1.

   LO QUE HACE DIFICIL ESTA PIEZA no es ninguna nota suelta: es que la derecha
   no para. Ocho semicorcheas seguidas por compas, y la mano izquierda quieta
   debajo aguantando un acorde entero. Por eso la hoja empieza por la ligadura y
   el puntillo —que es donde se pierde la cuenta— y no por las notas.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, semi, plan, escalera, cifrado,
                      verdadero_falso, escribir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El c. 1 de la DERECHA, medido: dos silencios y la nota de entrada.
C1 = [sil('h'), sil('q'), n('B3')]

# Y el c. 2, medido. Cita literal: es el compas que da el caracter a la pieza.
C2 = ([dict(n('B4'), lig=True), n('B4', 'e.'), n('D5', 's')] +
      semi(['D5', 'C5', 'C5', 'B4'], 4) + semi(['B4', 'C5', 'B4', 'G4'], 4))

# La izquierda del c. 2: el acorde de Mi menor en redonda. Medido.
EM = [ac(('E3', 'G3', 'B3'), 'w')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=19, nivel='intermedio',
    slug='AComme', formato='adulto',
    titulo_corto='A comme amour', time_sig=(4, 4), key_sig='Mi menor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'A comme amour.pdf'),
    yt='https://www.youtube.com/results?search_query=a+comme+amour+clayderman+piano',

    ficha=dict(
        titulo='A comme amour',
        autor='Paul de Senneville · Richard Clayderman',
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 69'), ('Armadura', 'Un sostenido'),
               ('Trae', 'Cifrado impreso')],
        titulo_ritmos='La entrada y el primer acorde',
        pie_ritmos='Arriba, el c. 1 de la derecha MEDIDO en tu partitura: casi todo silencio, y la '
                   'nota de entrada en el cuarto tiempo. Abajo, la izquierda del c. 2, medida: el '
                   'acorde de Mi menor en una redonda, que es la primera letra del cifrado.',
        armonia=dict(
            titulo='Seis letras y una mano que no para',
            tarjetas=[
                ('EL CIFRADO', 'Em B7 E7 Am A7 Dm',
                 'Seis letras impresas encima del pentagrama, y con esas seis está la pieza entera. '
                 'La izquierda no toca nada que no salga de una de ellas.'),
                ('LA LIGADURA', 'Y el puntillo',
                 'El c. 2 empieza con una negra ligada a una corchea con puntillo. Entre las dos '
                 'suenan como UNA sola nota de 1 tiempo y ¾, y ahí es donde se pierde la cuenta.'),
                ('LAS SEMICORCHEAS', 'Ocho seguidas',
                 'Después del puntillo la derecha no para: dos grupos de cuatro por compás. No hay '
                 'ninguna difícil; lo difícil es que suenen todas iguales.'),
                ('EL TEMPO', '♩ = 69',
                 'Viene impreso, así que no hay nada que decidir. Es lento de verdad: cada golpe '
                 'dura casi un segundo, y dentro caben cuatro semicorcheas.'),
            ],
            pie='Esta es la última del cuaderno y no es casualidad: pide la mano abierta del '
                'Pachelbel, el dibujo repetido del Preludio de Bach y la semicorchea suelta del '
                'Nino Bravo, todo a la vez. Si llegas aquí con esas tres, esta pieza es cuestión de '
                'semanas, no de suerte.',
        ),
        ritmos=[
            ('DERECHA', 'el c. 1, MEDIDO · entras en el cuarto tiempo',
             C1, OCRE, 'treble', 'Mi menor'),
            ('IZQUIERDA', 'el c. 2, medido · el acorde de Mi menor en redonda',
             list(EM), AZUL, 'bass', 'Mi menor'),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa van en tecla negra.',
            'El tempo está impreso: negra = 69.',
            'Encima del pentagrama están las letras Em, B7, E7, Am, A7 y Dm.',
            'El compás 1 es casi todo silencio: entras en el cuarto tiempo.',
            'El compás 2 empieza con una negra ligada a una corchea con puntillo.',
            'Después del puntillo hay ocho semicorcheas seguidas.',
            'La izquierda toca acordes largos: una redonda por compás.',
        ],
        reto='Que las ocho semicorcheas suenen todas iguales, con la izquierda quieta debajo. No '
             'hay ninguna nota difícil en toda la página: lo difícil es no acelerar en cuanto la '
             'mano se suelta.',
        truco='Toca los dos grupos de cuatro parando en seco al final de cada uno, como si fueran '
              'dos ejercicios distintos. Cuando los dos salgan iguales, quita la parada y únelos: '
              'el desnivel casi siempre está en la primera nota del segundo grupo.',
        sabias='Paul de Senneville la escribió en 1977 y se la dio a un pianista de veinticuatro '
               'años que hasta entonces tocaba en estudios de grabación: Richard Clayderman. Vendió '
               'veintidós millones de discos con ella y con la que la acompañaba, y desde entonces '
               'está en todos los métodos de piano.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta los golpes: son cuatro por compás y muy lentos. Dentro de cada uno '
                      'caben cuatro notas de la mano derecha, y por eso parece que va más rápida '
                      'de lo que va.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La última del cuaderno, y la que junta todo lo anterior. Empieza por la ligadura del '
              'principio: si esa cuenta no sale, lo que viene detrás entra tarde siempre.',
        reglas=['TODOS LOS FA, EN TECLA NEGRA', 'LA LIGADURA SUENA COMO UNA SOLA NOTA',
                'OCHO SEMICORCHEAS, TODAS IGUALES'],
        bloques=[
            dict(num=1, titulo='La entrada y la ligadura',
                 pista='cc. 1-2 · MEDIDO en tu partitura · entras en el cuarto tiempo del c. 1',
                 sistemas=[
                     dict(cap='a) el c. 1 con los silencios partidos en negras, para contarlos uno '
                              'a uno · en tu partitura son un silencio de blanca y otro de negra',
                          events=[sil('q'), sil('q'), sil('q'), n('B3')],
                          bars=1, key_sig='Mi menor'),
                     dict(cap='b) y el principio del c. 2 con la ligadura y el puntillo, y el resto '
                              'del compás en notas largas · andamio para contar la entrada',
                          events=[dict(n('B4'), lig=True), n('B4', 'e.'), n('D5', 's'),
                                  n('C5', 'h')],
                          bars=1, show_time=False, key_sig='Mi menor'),
                     dict(cap='c) y la misma ligadura sin el puntillo, para oír qué añade · esto NO '
                              'es lo que pone tu partitura',
                          events=[dict(n('B4'), lig=True), n('B4', 'e'), n('D5', 'e'),
                                  n('C5', 'h')],
                          bars=1, show_time=False, key_sig='Mi menor'),
                     dict(cap='d) y la misma entrada empezando en otras dos notas · andamio: lo que '
                              'se practica es la cuenta, no las alturas',
                          events=[dict(n('G4'), lig=True), n('G4', 'e.'), n('B4', 's'),
                                  dict(n('A4'), lig=True), n('A4', 'e.'), n('C5', 's')],
                          bars=2, show_time=False, key_sig='Mi menor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA LIGADURA CAMBIA LA CUENTA',
                 texto='Una ligadura entre dos notas iguales no se vuelve a tocar: se suman las dos '
                       'duraciones y sale UN solo sonido. Aquí son una negra y una corchea con '
                       'puntillo, o sea 1 + 0,75 = 1 tiempo y tres cuartos. Lo que engaña es que en '
                       'el papel se ven dos cabezas de nota, y la mano quiere volver a atacar. Si '
                       'la atacas, el compás te sale largo y todo lo demás entra tarde.'),
            dict(num=2, titulo='Las ocho semicorcheas',
                 pista='c. 2 · MEDIDO · dos grupos de cuatro, y ninguna nota difícil',
                 sistemas=[
                     dict(cap='a) el compás 2 entero, tal y como está escrito',
                          events=list(C2), bars=1, key_sig='Mi menor'),
                     dict(cap='b) y los dos grupos de cuatro con una parada entre medias · andamio: '
                              'lo que se mira es si el segundo suena igual que el primero',
                          events=semi(['D5', 'C5', 'C5', 'B4'], 4) + [sil('q')] +
                                 semi(['B4', 'C5', 'B4', 'G4'], 4) + [sil('q')],
                          bars=1, show_time=False, key_sig='Mi menor'),
                     dict(cap='c) y las mismas ocho notas en corcheas, al doble de lento · andamio: '
                              'primero se colocan y después se aprietan',
                          events=corch(['D5', 'C5']) + corch(['C5', 'B4']) +
                                 corch(['B4', 'C5']) + corch(['B4', 'G4']),
                          bars=1, show_time=False, key_sig='Mi menor'),
                     dict(cap='d) y los dos grupos al revés, de abajo arriba · andamio: la mano '
                              'aprende el camino en los dos sentidos y deja de ir de memoria',
                          events=semi(['G4', 'B4', 'C5', 'B4'], 4) +
                                 semi(['B4', 'C5', 'C5', 'D5'], 4) +
                                 semi(['D5', 'C5', 'C5', 'B4'], 4) +
                                 semi(['B4', 'C5', 'B4', 'G4'], 4),
                          bars=1, show_time=False, key_sig='Mi menor'),
                 ]),
            dict(num=3, titulo='La izquierda: un acorde y quieta',
                 pista='c. 2 de la mano izquierda · MEDIDO · el acorde de Mi menor en redonda',
                 sistemas=[
                     dict(cap='a) las tres notas del acorde del c. 2 de una en una, de grave a '
                              'agudo · andamio: para '
                              'colocar la mano antes de cerrarla',
                          events=[n('E3'), n('G3'), n('B3'), n('E4')],
                          bars=1, clef='bass', show_time=False, key_sig='Mi menor'),
                     dict(cap='b) y los cuatro primeros acordes del cifrado impreso, uno por compás '
                              '· andamio sobre Em, B7, E7 y Am',
                          events=[ac(('E3', 'G3', 'B3'), 'w'), ac(('B2', 'D#3', 'A3'), 'w'),
                                  ac(('E3', 'G#3', 'D4'), 'w'), ac(('A2', 'C3', 'E3'), 'w')],
                          bars=4, clef='bass', show_time=False, key_sig='Mi menor'),
                     dict(cap='c) y los dos que faltan, que salen más adelante · andamio sobre el '
                              'A7 y el Dm que también trae impresos tu partitura',
                          events=[ac(('A2', 'C#3', 'G3'), 'w'), ac(('D3', 'F3', 'A3'), 'w')],
                          bars=2, clef='bass', show_time=False, key_sig='Mi menor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Los dos primeros compases con las dos manos y el metrónomo a 69, que es lo '
                       'que trae impreso tu partitura: no hay que decidir nada. Empieza más despacio '
                       'si hace falta, pero la meta está escrita en el papel. Y cuando salgan, mira '
                       'las letras de acorde de la página entera: son seis y no hay ninguna más, '
                       'así que la mano izquierda de toda la pieza cabe en seis posiciones.'),
        ] + bloques_extra('Mi menor', 117, 'E4', 'E2',
                          'ocho semicorcheas seguidas con la izquierda quieta debajo',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='A comme amour · para casa',
            intro='Quince minutos al día. Es la última del cuaderno y la más larga de aprender: no '
                  'se gana en una semana, se empieza en una semana.',
            bloques=[
                plan((4, 'Contar la ligadura y el puntillo del c. 2, sin tocar'),
                     (4, 'Los dos grupos de cuatro semicorcheas, con parada entre medias'),
                     (3, 'La izquierda: el acorde de Mi menor y los tres siguientes'),
                     (4, 'Los cc. 1 y 2 con las dos manos, con el metrónomo a 69')),
                escalera((50, 'los dos grupos de cuatro, parando entre medias'),
                         (58, 'el c. 2 entero y seguido'),
                         (69, 'los cc. 1 y 2 con las dos manos'),
                         (69, 'y ahí nos quedamos: 69 es lo que pide la partitura'),
                         meta='La meta NO la ponemos nosotras: ♩ = 69 viene impreso en tu '
                              'partitura, encima del primer compás. Los tres números de debajo sí '
                              'son de trabajo.'),
                cifrado([('Em', 'Mi menor'), ('B7', 'Si séptima'),
                         ('E7', 'Mi séptima'), ('Am', 'La menor')],
                        ['¿Cuáles de los cuatro son menores?',
                         '¿Cuál de los cuatro es el que la izquierda toca en el compás 2?'],
                        titulo='Las letras de acorde que trae tu partitura',
                        pista='están impresas encima del pentagrama · escribe sus notas'),
                verdadero_falso([
                    'Una ligadura entre dos notas iguales se toca dos veces.',
                    'Cuatro semicorcheas ocupan un tiempo de negra.',
                    'Esta partitura trae escrito el número de metrónomo.',
                    'El compás 1 tiene más silencio que música.',
                    'La mano izquierda cambia de acorde dentro del compás 2.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas'),
                escribir(titulo='Copia aquí el segundo grupo de cuatro semicorcheas del c. 2',
                         pista='Si, Do, Si, Sol · cópialas con su barra doble y tócalas cinco veces'),
                para_clase('Los dos primeros compases con las dos manos, a la velocidad más alta a '
                           'la que las ocho semicorcheas te salgan iguales. Y dime cuál de las ocho '
                           'se te desnivela: siempre hay una, y por ahí empezamos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
