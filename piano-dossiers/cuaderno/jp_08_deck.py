# -*- coding: utf-8 -*-
"""Deck the Halls — pieza 8 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Jim Paterson,
   mfiles.co.uk, 1 página):

     - Fa mayor: un bemol detrás de la clave.
     - 4/4. Pone "mp" y no imprime tempo.
     - CIFRADO IMPRESO encima del pentagrama: F · C · Dm7 · C. Uno de ellos,
       Dm7, es de cuatro notas: el primer acorde con séptima del cuaderno.
     - Las DOS MANOS TOCAN DOBLES NOTAS casi todo el rato: dos teclas a la vez
       en la derecha y dos en la izquierda, compás tras compás.
     - Empieza con anacrusa y hay barra de repetición al principio.
     - La figura que domina es negra con puntillo + corchea, una y otra vez.

   El archivo es EL MISMO que el de José María (md5 idéntico). Aquí el trabajo
   va por las dobles notas y el cifrado; allí iba por el bemol y las dos manos.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloque_puntillo, bloques_extra
from jp_comun import (n, ac, semi, plan, escalera, cifrado, unir, nombres, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=8, nivel='intermedio', slug='DeckTheHalls',
    formato='adulto',
    titulo_corto='Deck the Halls', time_sig=(4, 4), key_sig='Fa mayor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'Deck the Halls  NAVIDAD.pdf'),
    yt='https://www.youtube.com/results?search_query=deck+the+halls+piano+easy',

    ficha=dict(
        titulo='Deck the Halls',
        autor='Villancico tradicional galés · arreglo de Jim Paterson',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', '4/4'),
               ('Carácter', 'mp · sin tempo'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Una')],
        titulo_ritmos='Dos teclas a la vez, en las dos manos',
        pie_ritmos='Andamio en Fa mayor. Lo literal es la textura: dobles notas arriba y abajo, y '
                   'la figura de negra con puntillo y corchea que se repite compás tras compás.',
        armonia=dict(
            titulo='Lo que hace difícil un villancico fácil',
            tarjetas=[
                ('DOBLES NOTAS', 'En las dos manos',
                 'Dos teclas a la vez arriba y dos abajo, compás tras compás. Cuatro notas por '
                 'golpe, y las cuatro tienen que sonar exactamente juntas.'),
                ('EL Dm7', 'Cuatro notas',
                 'El cifrado impreso trae F, C y Dm7. Ese 7 quiere decir que el acorde lleva una '
                 'nota más: es el primero de cuatro notas de tu cuaderno.'),
                ('LA FIGURA', 'Larga-corta',
                 'Negra con puntillo y corchea, una y otra vez. Es lo que le da el aire de '
                 'villancico, y es lo que se aplana si vas rápido.'),
                ('LA ANACRUSA', 'Se entra antes',
                 'La pieza empieza antes del compás, y además tiene barra de repetición: se vuelve '
                 'a entrar por el mismo sitio.'),
            ],
            pie='La melodía la sabe todo el mundo, y eso es una trampa: se toca de memoria y se deja '
                'de leer. Aquí lo que hay que leer no es la melodía, es la segunda nota de cada '
                'mano, que es la que no se sabe de oído.',
        ),
        ritmos=[
            ('MANO DERECHA', 'dos teclas a la vez, larga y corta · andamio',
             [ac(('A4', 'F5'), 'q.'), ac(('G4', 'E5'), 'e'), ac(('A4', 'F5'), 'h')],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'también dobles, sosteniendo · andamio',
             [ac(('F2', 'C3'), 'h'), ac(('A2', 'F3'), 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Un bemol detrás de la clave: Fa mayor, todos los Si son Si bemol.',
            'El cifrado viene impreso: F, C y Dm7.',
            'El Dm7 lleva cuatro notas, no tres.',
            'Las dos manos tocan dobles notas casi todo el rato.',
            'La figura que más se repite es negra con puntillo y corchea.',
            'Empieza con anacrusa y hay barra de repetición.',
        ],
        reto='Que las dos notas de cada mano suenen exactamente juntas. En una doble nota siempre '
             'hay un dedo que llega antes, y casi siempre es el pulgar: se oye como un adorno que '
             'nadie ha escrito.',
        truco='Toca la doble nota muy fuerte y muy corta, como un pellizco, veinte veces. Fuerte y '
              'corto es donde se oye si un dedo se adelanta. Cuando suene un solo golpe, bájalo a '
              '"mp" y ya no se separa.',
        sabias='La melodía es galesa y tiene siglos; la letra en inglés que se canta hoy es del '
               'siglo XIX y la escribió un músico escocés. El "fa-la-la-la-la" original imitaba a '
               'un arpa, que era el instrumento que acompañaba la melodía en Gales.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la diferencia entre la melodía sola y la melodía con la segunda nota '
                      'debajo. Es la misma canción y suena el doble de llena.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La melodía te la sabes, así que el riesgo aquí es tocarla de memoria y no leer. Lo '
              'que hay que trabajar es la SEGUNDA nota de cada mano y que las dos caigan juntas.',
        reglas=['LAS DOS NOTAS, EXACTAMENTE JUNTAS', 'LEE LA DE ABAJO, NO LA DE ARRIBA',
                'LARGA-CORTA, SIN APLANAR'],
        bloques=[
            dict(num=1, titulo='La doble nota, como un pellizco',
                 pista='andamio en Fa mayor · fuerte y corto: es donde se oye si un dedo se adelanta',
                 sistemas=[
                     dict(cap='a) terceras subiendo por la escala de Fa · las dos notas, un solo '
                              'golpe',
                          events=[ac(('F4', 'A4')), ac(('G4', 'Bb4')), ac(('A4', 'C5')),
                                  ac(('Bb4', 'D5')), ac(('C5', 'E5')), ac(('Bb4', 'D5')),
                                  ac(('A4', 'C5'), 'h')],
                          matiz='mp',
                          bars=2, key_sig='Fa mayor'),
                     # Esta linea decia "y AHORA con su figura de verdad, la semicorchea,
                     # tal y como esta impreso en tu partitura". Es FALSO: se ha vuelto a
                     # mirar el PDF entero (mfiles, Jim Paterson, 16 compases) y no hay ni
                     # una barra doble. La figura mas corta de esta pieza es la corchea, y
                     # eso es lo que se escribe.
                     dict(cap='b) y ahora cuatro corcheas seguidas · es lo más rápido que llega a '
                              'haber en tu partitura, y las dos manos caen juntas en cada una',
                          events=[{'pitch': 'C5', 'dur': 'e'}, {'pitch': 'D5', 'dur': 'e'},
                                  {'pitch': 'C5', 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e'},
                                  n('Bb4'), n('A4')],
                          bars=1, show_time=False, key_sig='Fa mayor'),
                 ]),
            dict(num=2, titulo='La figura larga-corta, sin aplanarla',
                 pista='andamio · negra con puntillo y corchea, que es la que domina la pieza',
                 sistemas=[
                     dict(cap='a) la corta es MUY corta y va pegada a la siguiente · cuenta "un-dos-'
                              'tres-Y" y la corchea cae en la "y" del tres',
                          events=[n('F5', 'q.'), n('E5', 'e'), n('D5'), n('C5'),
                                  n('D5', 'q.'), n('C5', 'e'), n('Bb4', 'h')],
                          bars=2, key_sig='Fa mayor'),
                     dict(cap='b) y con la figura invertida, corta-larga, que es como entra la '
                              'anacrusa · la corta empuja hacia la larga, no al revés',
                          events=[n('C5', 'e'), n('F5', 'q.'), n('E5'), n('D5'),
                                  n('C5', 'e'), n('D5', 'q.'), n('C5'), n('A4')],
                          bars=2, key_sig='Fa mayor', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES EL 7 DEL Dm7',
                 texto='Un acorde normal tiene tres notas. El 7 quiere decir que se le añade una '
                       'cuarta, contando siete notas hacia arriba desde la primera. Suena menos '
                       'cerrado, como si pidiera continuar, y por eso casi siempre va justo antes '
                       'de volver al acorde de casa. En tu partitura está impreso encima del '
                       'pentagrama: búscalo y mira cuántas teclas tocas en ese compás.'),
            dict(num=3, titulo='Las dos manos, con dobles arriba y abajo',
                 pista='andamio en Fa mayor · cuatro notas por golpe, y las cuatro juntas',
                 sistemas=[
                     dict(cap='a) empieza muy lento: aquí no hay velocidad que ganar, hay cuatro '
                              'dedos que tienen que caer a la vez',
                          events=[ac(('F2', 'C3', 'A4', 'F5'), 'q.'), ac(('G4', 'E5'), 'e'),
                                  ac(('F4', 'D5')), ac(('G4', 'E5')),
                                  ac(('A2', 'F3', 'A4', 'F5'), 'h'), ac(('F4', 'C5'), 'h')],
                          bars=2, key_sig='Fa mayor'),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Deck the Halls · para casa',
            intro='Veinte minutos, y el primero de cada día en dobles notas sueltas.',
            bloques=[
                plan((5, 'Dobles notas en pellizco: terceras y sextas'),
                     (5, 'La derecha sola, leyendo la nota de ABAJO'),
                     (5, 'La izquierda sola, con sus dos notas juntas'),
                     (5, 'Las dos manos, de dos en dos compases')),
                escalera((60, 'las dobles notas, juntas y en pellizco'),
                         (75, 'la melodía con la figura larga-corta'),
                         (90, 'las dos manos, la pieza entera'),
                         meta='la velocidad a la que las cuatro notas caigan juntas — esta '
                              'partitura no trae tempo impreso',
                         notas=['Si una doble nota se te separa al subir de escalón, baja uno.']),
                cifrado(['F', 'C', 'Dm7'],
                        ['Escribe las notas de cada uno, de grave a agudo.',
                         'Ojo: el Dm7 lleva CUATRO notas, no tres. Tienes una casilla de más.'],
                        filas=4, alto_caja=12.0,
                        pista='son los tres que trae impresos tu partitura'),
                unir([('Negra con puntillo', 'dura un golpe y medio'),
                      ('Dm7', 'un acorde de cuatro notas'),
                      ('Anacrusa', 'la música empieza antes del compás'),
                      ('Doble nota', 'dos teclas a la vez con una sola mano')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro están en tu partitura de esta semana'),
                nombres(['F4', 'A4', 'Bb4', 'D5', 'C5', 'E5', 'F5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='ojo con la tercera: estamos en Fa mayor'),
                para_clase('Las dobles notas de las dos manos y a qué velocidad te suenan juntas. '
                           'Y trae escritas las notas del Dm7: si te ha salido, ya sabes leer todos '
                           'los acordes con séptima que vengan después.'),
            ],
        ),
    ],
)

# El ritmo con puntillo que esta pieza EXPLICA en su texto y no dibujaba en
# ningún sitio. Lo destapó el auditor de vocabulario al ganar la entrada de
# esta figura, que antes no miraba nadie.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Fa mayor', 26, 'F4', 'F2',
    'el Si bemol, antes de que llegue el puntillo',
    desde=5, time_sig=(4, 4)) + [
    bloque_puntillo('Fa mayor', 4, 'F4', 'el puntillo del villancico, en la melodía',
                    time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
