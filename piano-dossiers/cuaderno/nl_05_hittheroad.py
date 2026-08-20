# -*- coding: utf-8 -*-
"""Hit the Road Jack — pieza 5 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (Musescore, 1 página,
   24 compases, sin arreglista impreso; el mismo archivo que la pieza 7 de
   Josep, byte a byte):

     - Fa mayor: un bemol detrás de la clave, desde el compás 1.
     - 4/4. No imprime tempo.
     - Los seis primeros compases la derecha hace acordes en bloque con
       silencios entre medias, y la izquierda negras sueltas: introducción.
     - Del c. 7 al 19 la derecha lleva la melodía y la izquierda hace redondas.
     - Del c. 20 al final vuelven los acordes en bloque de la introducción.
     - Hay barras de repetición en los cc. 12 y 20.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import escala, cadencia, arpegio, giro
from nl_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=5, nivel='avanzado', slug='HitTheRoadJack',
    formato='adulto',
    titulo_corto='Hit the Road Jack', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source', 'hit-the-road-jack-ray-.pdf'),
    yt='https://www.youtube.com/results?search_query=hit+the+road+jack+piano+easy',

    ficha=dict(
        titulo='Hit the Road Jack',
        autor='Popularizada por Ray Charles · arreglo de Musescore',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Teclas negras', 'El Si bemol'),
               ('Páginas', 'Una')],
        titulo_ritmos='Las dos caras de la pieza',
        pie_ritmos='Andamio en Fa mayor. Lo literal es la estructura: acordes en bloque con '
                   'silencios en la introducción y melodía con redondas en el centro.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('UN BEMOL', 'Desde el c. 1',
                 'Todos los Si de la pieza son Si bemol, la tecla negra, del primer compás al '
                 'último, sin excepción.'),
                ('LA INTRODUCCIÓN', 'cc. 1-6',
                 'Acordes en bloque con silencios entre medias en la derecha, y negras sueltas en '
                 'la izquierda. Todavía no es la melodía.'),
                ('EL CENTRO', 'cc. 7-19',
                 'Ahí entra la melodía, la parte que canta todo el mundo, con la izquierda quieta en '
                 'redondas.'),
                ('Y VUELTA', 'cc. 20-24',
                 'Regresan los acordes del principio: la pieza cierra igual que abrió.'),
            ],
            pie='Ray Charles la grabó en 1961 y llegó al número uno, pero la escribió otro: Percy '
                'Mayfield, que la mandó al estudio grabada a capela en una cinta como maqueta.',
        ),
        ritmos=[
            ('MANO DERECHA · INTRO', 'acordes y silencios · andamio',
             [sil('q'), ac(('A3', 'C4', 'F4')), sil('q'), ac(('A3', 'C4', 'F4'))],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA · CENTRO', 'una redonda por compás · literal',
             [n('F2', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Un bemol detrás de la clave desde el compás 1: todos los Si son Si bemol.',
            'Los seis primeros compases son acordes en bloque con silencios en medio.',
            'Del compás 7 al 19 la izquierda hace una redonda por compás.',
            'Del compás 20 al final vuelven los acordes del principio.',
            'Hay barras de repetición en los compases 12 y 20.',
            'La edición no imprime tempo.',
        ],
        reto='No olvidarte del Si bemol a mitad de frase, cuando ya no estás pendiente de la '
             'armadura y la mano vuelve por costumbre a la tecla blanca.',
        truco='Antes de tocar, marca a lápiz todos los Si de tu partitura con un circulito. Son '
              'pocos, y verlos marcados evita veinte correcciones sueltas.',
        sabias='La versión de Ray Charles con las voces respondiendo a cada frase fue una idea del '
               'estudio de grabación, no del compositor original.',
        qr=dict(titulo='Escúchala',
                texto='Compara la introducción con la parte cantada: son dos texturas distintas, y '
                      'en tu partitura están escritas de forma distinta.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos texturas distintas y una armadura nueva. El Si bemol primero, luego la '
              'introducción, y la melodía al final: es la parte que ya te suena de oído.',
        reglas=['TODOS LOS SI SON SI BEMOL', 'LA INTRO NO ES LA MELODÍA',
                'LOS SILENCIOS SE CUENTAN'],
        bloques=[
            dict(num=1, titulo='El Si bemol, hasta que el otro suene raro',
                 pista='andamio en Fa mayor · el bemol vale para toda la pieza',
                 sistemas=[
                     dict(cap='a) arpegio en Fa, con el Si bemol de paso',
                          events=[n('F3'), n('A3'), n('C4'), n('F4'),
                                  n('D4'), n('Bb3'), n('G3'), n('F3')],
                          bars=2, key_sig=FA),
                     dict(cap='b) y girando alrededor del Si bemol, que es donde se olvida',
                          events=[n('C4'), n('Bb3'), n('C4'), n('D4'),
                                  n('Bb3'), n('A3'), n('F3', 'h')],
                          bars=2, key_sig=FA, show_time=False),
                 ]),
            dict(num=2, titulo='La introducción: acordes y silencios',
                 pista='la FORMA es literal (acorde, silencio, acorde); las notas, andamio en Fa',
                 sistemas=[
                     dict(cap='a) el acorde cae y se levanta, un peldaño más arriba cada vez',
                          events=[sil('q'), ac(('C4', 'F4', 'A4')), sil('q'), ac(('C4', 'F4', 'A4')),
                                  sil('q'), ac(('D4', 'F4', 'Bb4')), sil('h')],
                          bars=2, key_sig=FA),
                     dict(cap='b) con la izquierda de la introducción debajo, en negras sueltas',
                          events=[n('A2'), sil('q'), n('A2'), sil('q'),
                                  n('D3'), sil('q'), n('D3'), sil('q')],
                          bars=2, clef='bass', key_sig=FA, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE MARCAN LOS SI',
                 texto='Una armadura no se olvida por falta de técnica: se olvida porque el ojo deja '
                       'de mirar el principio del pentagrama en cuanto lleva un par de líneas '
                       'leyendo. Marcarlos a lápiz la primera semana no es hacer trampa: es lo que '
                       'hace cualquiera con una tonalidad nueva, y en la tercera semana ya se borra.'),
            dict(num=3, titulo='La escala de Fa, con su Si bemol dentro',
                 pista='andamio en Fa mayor · el bemol dejará de sorprenderte cuando lo toques '
                       'veinte veces seguidas',
                 sistemas=[
                     dict(cap='a) los siete grados desde Fa · el cuarto es el Si bemol, y va sin '
                              'pensarlo',
                          events=escala('Fa mayor', 'F4'), bars=2),
                     dict(cap='b) y bajando desde arriba · aquí es donde suele escaparse',
                          events=escala('Fa mayor', 'F5', sentido='baja'),
                          bars=2, show_time=False),
                 ]),
            dict(num=4, titulo='La melodía sobre las redondas',
                 pista='andamio en Fa mayor · cc. 7-19 de tu partitura',
                 sistemas=[
                     dict(cap='a) la izquierda aguanta la redonda entera mientras la derecha se mueve',
                          events=[ac(('A2', 'F5')), n('D5'), n('C5'), n('Bb4'),
                                  ac(('D3', 'Bb4'), 'h'), n('C5'), n('A4')],
                          bars=2, key_sig=FA),
                     dict(cap='b) y bajando hasta la tónica, que es como acaba cada frase',
                          events=[n('Bb4'), n('A4'), n('G4'), n('F4'),
                                  n('D4'), n('F4'), n('F4', 'h')],
                          bars=2, key_sig=FA, show_time=False),
                 ]),
            dict(num=5, titulo='Los tres acordes de Fa mayor',
                 pista='andamio en Fa mayor · la armonía de la canción, en lo mínimo',
                 sistemas=[
                     dict(cap='a) I - IV - V - I · el de IV lleva el Si bemol: si suena raro, es '
                              'que has puesto Si natural',
                          events=cadencia('Fa mayor', 'F2'), bars=4, clef='bass'),
                 ]),
            dict(num=6, titulo='El acorde de Fa y el giro sobre el bemol',
                 pista='andamio en Fa mayor · lo mismo de antes, pero con la mano quieta',
                 sistemas=[
                     dict(cap='a) el acorde de Fa desplegado, sube y baja',
                          events=arpegio('Fa mayor', 'F4'), bars=2),
                     dict(cap='b) y el giro alrededor del Si bemol · el dedo va a la tecla negra '
                              'sin mirar, que es de lo que se trata',
                          events=giro('Fa mayor', 'Bb4'), bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
