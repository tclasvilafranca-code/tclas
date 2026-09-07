# -*- coding: utf-8 -*-
"""Deck the Halls — pieza 3 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (mfiles.co.uk, arreglo de
   Jim Paterson, 1 página, 16 compases con repetición; el mismo archivo que la
   pieza 7 de José María y la pieza de Josep, byte a byte):

     - FA MAYOR: un bemol detrás de la clave.
     - Compás de 4/4. Pone "mp".
     - Las dos manos tocan acordes de dos notas.
     - Encima vienen los diagramas de guitarra y las letras de los acordes:
       F · C · F · C · F · Dm7 · G · C · B♭.
     - Los números de compás vienen impresos (5, 9, 13).
     - Muy repetitiva: los compases 1-4 vuelven casi igual en el 5 y en el 13.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloque_puntillo, bloques_extra
from nl_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=3, nivel='avanzado', slug='DeckTheHalls',
    formato='adulto',
    titulo_corto='Deck the Halls', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source',
                           'Deck the Halls (NAVIDAD).pdf'),
    yt='https://www.youtube.com/results?search_query=deck+the+halls+piano+easy',

    ficha=dict(
        titulo='Deck the Halls',
        autor='Villancico tradicional · arreglo de Jim Paterson · mfiles.co.uk',
        datos=[('Tonalidad', 'Fa mayor'), ('Novedad', 'Un bemol'),
               ('Compás', '4/4'), ('Las dos manos', 'Con acordes'),
               ('Compases', '16')],
        titulo_ritmos='Acordes en las dos manos, con el bemol',
        pie_ritmos='Andamio en Fa mayor. Lo literal es el reparto: las dos manos tocan acordes de dos '
                   'notas, y todos los Si de la pieza van a la tecla negra.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('EL BEMOL', 'En todos los Si',
                 'Se escribe una vez, al principio, y vale para toda la pieza: cada Si que aparece, '
                 'arriba o abajo, se toca en la tecla negra de al lado.'),
                ('ACORDES EN LAS DOS', 'Ninguna descansa',
                 'Las dos manos tocan a la vez notas dobles: no hay una melodía sola con acompañamiento '
                 'suelto, sino dos líneas de acordes que se mueven juntas.'),
                ('SE REPITE MUCHO', 'Menos trabajo real',
                 'Los compases 1 al 4 casi vuelven iguales en el 5 y en el 13. De dieciséis compases, '
                 'nuevos hay realmente cinco o seis.'),
                ('LAS LETRAS DE ACORDE', 'No son para tocar',
                 'F, C, Dm7, G, B♭ encima del pentagrama son para quien te acompañe con guitarra: tú '
                 'sigues las notas escritas, no las letras.'),
            ],
            pie='Es un villancico galés con más de quinientos años de melodía; la letra en inglés es '
                'de 1862, y el "fa-la-la" repetido era en origen la parte del arpa entre verso y verso.',
        ),
        ritmos=[
            ('MANO DERECHA', 'acordes con puntillo, dos notas cada uno · andamio',
             [ac(('Bb4', 'D5'), 'q.'), {'pitch': 'C5', 'dur': 'e'}, ac(('Bb4', 'D5')), n('A4')],
             OCRE, 'treble', FA),
            ('MANO IZQUIERDA', 'acordes largos, dos notas · literal',
             [ac(('F2', 'A2'), 'h'), ac(('Bb2', 'D3'), 'h')], AZUL, 'bass', FA),
        ],
        especial=[
            'Hay un bemol detrás de la clave: todos los Si van a la tecla negra.',
            'Compás de 4/4.',
            'Las dos manos tocan acordes de dos notas a la vez.',
            'Encima del pentagrama vienen las letras de los acordes y los diagramas de guitarra.',
            'Los números de compás están impresos: 5, 9 y 13.',
            'Los compases 1 al 4 vuelven casi iguales en el 5 y en el 13.',
        ],
        reto='Que las dos manos bajen exactamente a la vez con acordes de dos notas: si una se '
             'adelanta, se nota mucho más que en una pieza de melodía sola.',
        truco='Practica cada acorde de las dos manos por separado, contando en voz alta, antes de '
              'juntarlas. Cuando las dos caigan juntas sin pensarlo, sube el tempo.',
        sabias='El "fa-la-la-la-la" repetido cuatro veces no es relleno: en la melodía original galesa '
               'era el trozo que tocaba el arpa entre verso y verso, antes de que alguien decidiera '
               'ponerle letra y cantarlo.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuántas veces se repite el "fa-la-la": vas a encontrar el mismo dibujo '
                      'exacto una y otra vez.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas: el bemol y las dos manos con acordes a la vez. La pieza se repite '
              'mucho, así que lo que se aprende bien en los primeros compases vale para media pieza.',
        reglas=['TODOS LOS SI, EN LA TECLA NEGRA', 'LOS ACORDES BAJAN A LA VEZ',
                'BUSCA LO QUE SE REPITE ANTES DE TOCAR'],
        bloques=[
            dict(num=1, titulo='El bemol: saltando de un Si a otro',
                 pista='andamio en Fa mayor · el Si de esta pieza siempre es bemol',
                 sistemas=[
                     dict(cap='a) el salto que más se repite en la pieza',
                          events=[n('D5'), n('Bb4'), n('C5'), n('Bb4'),
                                  n('A4'), n('Bb4'), n('D5'), n('Bb4')],
                          matiz='mp',
                          bars=2, key_sig=FA),
                     dict(cap='b) y bajando desde arriba, pasando siempre por el Si bemol',
                          events=[n('F5'), n('D5'), n('C5'), n('Bb4'),
                                  n('A4'), n('G4'), n('F4'), n('D4')],
                          bars=2, key_sig=FA, show_time=False),
                 ]),
            dict(num=2, titulo='Acordes de dos notas, las dos manos juntas',
                 pista='andamio · cuenta en voz alta antes de bajar los dos dedos a la vez',
                 sistemas=[
                     dict(cap='a) la derecha: acordes cortos',
                          events=[ac(('Bb4', 'D5')), ac(('A4', 'C5')), ac(('G4', 'Bb4')),
                                  ac(('F4', 'A4'))],
                          bars=1, key_sig=FA),
                     dict(cap='b) y la izquierda, sostenidos por debajo',
                          events=[ac(('Bb2', 'D3'), 'h'), ac(('F2', 'C3'), 'h'),
                                  ac(('C3', 'G3'), 'h'), ac(('F2', 'A2'), 'h')],
                          bars=2, clef='bass', key_sig=FA, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE ESTUDIA ASÍ ESTA PIEZA',
                 texto='Los compases 1 al 4 casi vuelven iguales en el 5 y en el 13: aprender bien esos '
                       'cuatro compases al detalle, con el bemol seguro y los acordes sincronizados, '
                       'resuelve de golpe más de la mitad de la pieza. Lo nuevo de verdad son solo unos '
                       'pocos compases.'),
            dict(num=3, titulo='El ritmo con puntillo, mano a mano',
                 pista='andamio · "LAAA-la", larga y corta, en las dos manos por separado primero',
                 sistemas=[
                     dict(cap='a) la derecha con el puntillo',
                          events=[ac(('Bb4', 'D5'), 'q.'), {'pitch': 'C5', 'dur': 'e'},
                                  ac(('Bb4', 'D5')), n('A4'),
                                  ac(('G4', 'Bb4'), 'q.'), {'pitch': 'A4', 'dur': 'e'},
                                  ac(('G4', 'Bb4')), n('F4')],
                          bars=2, key_sig=FA),
                     dict(cap='b) y las dos manos juntas, sin el puntillo, para comparar',
                          events=[ac(('Bb4', 'D5')), n('C5'), ac(('Bb4', 'D5')), n('A4'),
                                  ac(('G4', 'Bb4')), n('A4'), ac(('G4', 'Bb4')), n('F4')],
                          bars=2, key_sig=FA, show_time=False),
                 ]),
        ],
    ),
)

# El ritmo con puntillo que esta pieza EXPLICA en su texto y no dibujaba en
# ningún sitio. Lo destapó el auditor de vocabulario al ganar la entrada de
# esta figura, que antes no miraba nadie.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Fa mayor', 47, 'F4', 'F2',
    'el Si bemol, antes de que llegue el puntillo',
    desde=5, time_sig=(4, 4)) + [
    bloque_puntillo('Fa mayor', 4, 'F4', 'el puntillo del villancico, en la melodía',
                    time_sig=(4, 4), lento=True)]

if __name__ == '__main__':
    print('generado', construir(CANCION))
