# -*- coding: utf-8 -*-
"""Petite Chanson, de Riccardo Collu — pieza 1 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (Musescore, 2 páginas,
   24 compases; el mismo archivo que la pieza 2 de Josep, byte a byte):

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4, y pone "♩ = 80 andante".
     - Es a cuatro manos. Tu parte (el Primo) lleva los dos pentagramas en
       clave de sol.
     - Empieza con ANACRUSA: dos corcheas antes del primer compás.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from nl_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=1, nivel='avanzado', slug='PetiteChanson',
    formato='adulto',
    titulo_corto='Petite Chanson', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source', 'petite chanson.(4 manos)'),
    yt='https://www.youtube.com/results?search_query=petite+chanson+riccardo+collu+piano',

    ficha=dict(
        titulo='Petite Chanson',
        autor='Riccardo Collu · a cuatro manos · tu parte es el Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 80'), ('Empieza', 'Con anacrusa'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Dos corcheas antes del compás',
        pie_ritmos='Andamio en Do mayor. Lo literal es la entrada: dos corcheas antes del primer '
                   'compás, y luego tres negras.',
        armonia=dict(
            titulo='Por qué abre tu cuaderno',
            tarjetas=[
                ('ANACRUSA DE DOS CORCHEAS', 'Antes del compás',
                 'La pieza no empieza en el uno: entran dos corcheas antes, como impulso hacia el '
                 'primer compás completo.'),
                ('A CUATRO MANOS', 'Con la profesora',
                 'Tu parte lleva la melodía en los dos pentagramas de clave de sol; la otra parte '
                 'completa la armonía por debajo.'),
                ('ANDANTE', 'A paso tranquilo',
                 'No es lenta ni rápida: es un tempo de caminar, ni arrastrado ni apresurado.'),
                ('ABRE EL CUADERNO', 'Y a propósito',
                 'De todo tu repertorio de este curso, es la más sencilla de leer. El resto sube '
                 'rápido desde aquí.'),
            ],
            pie='Es una pieza contemporánea, escrita pensando en el mismo tipo de dueto que tocaban '
                'los alumnos hace dos siglos: profesor y alumno, cada uno con su parte.',
        ),
        ritmos=[
            ('MANO DERECHA', 'anacrusa de dos corcheas y tres negras · literal',
             corch(['E4', 'F4']) + [n('G4'), n('G4'), n('G4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'lo mismo, una octava abajo · andamio',
             [n('G3'), n('G3'), n('G3'), n('G3')], AZUL, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4, con "♩ = 80 andante" escrito arriba.',
            'La pieza empieza con dos corcheas antes del primer compás.',
            'El segundo Sol del primer compás suena una octava por encima del primero.',
            'Tu parte lleva los dos pentagramas en clave de sol.',
            'La otra parte, la de abajo, la toca la profesora.',
        ],
        reto='Que las dos corcheas de la anacrusa no se cuenten como un compás completo. Es un '
             'impulso corto hacia el primer tiempo fuerte, no una frase por sí sola.',
        truco='Cuenta "tres, cuatro" en voz alta antes de tocar la anacrusa, como si ya estuvieras a '
              'mitad de un compás anterior imaginario, y entra justo en el "uno" siguiente.',
        sabias='Riccardo Collu es un compositor contemporáneo que escribe piezas pedagógicas a '
               'cuatro manos pensadas específicamente para que un alumno y su profesor las toquen '
               'juntos desde las primeras semanas de clase.',
        qr=dict(titulo='Escúchala',
                texto='Escucha las dos partes juntas y localiza la anacrusa: son solo dos notas, '
                      'pero marcan todo el carácter de la entrada.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La anacrusa es lo único realmente nuevo. Se aísla, se cuenta, y luego se toca la '
              'pieza entera con ella ya integrada.',
        reglas=['LA ANACRUSA ES UN IMPULSO, NO UN COMPÁS', 'CUENTA ANTES DE ENTRAR',
                'ANDANTE: NI RÁPIDO NI ARRASTRADO'],
        bloques=[
            dict(num=1, titulo='La anacrusa, aislada',
                 pista='andamio en Do mayor · el mismo dibujo de la partitura',
                 sistemas=[
                     dict(cap='a) dos corcheas y entra el compás',
                          events=corch(['E4', 'F4']) + [n('G4'), n('A4'), n('G4'), n('F4'),
                                                          n('E4'), n('D4'), n('C4')],
                          bars=2),
                     dict(cap='b) el mismo dibujo, una frase más arriba',
                          events=corch(['G4', 'A4']) + [n('B4'), n('C5'), n('B4'), n('A4'),
                                                          n('G4'), n('F4'), n('E4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: la misma melodía, más grave',
                 pista='andamio · una octava por debajo',
                 sistemas=[
                     dict(cap='a) el mismo dibujo que la derecha',
                          events=[n('G3'), n('A3'), n('G3'), n('F3')],
                          bars=1, clef='bass'),
                     dict(cap='b) y la frase que sigue',
                          events=[n('B3'), n('C4'), n('B3'), n('A3')],
                          bars=1, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='La frase que baja hasta el Do',
                 pista='andamio en Do mayor · el descenso que cierra cada frase de tu partitura',
                 sistemas=[
                     dict(cap='a) bajando por grados hasta la nota de casa · ninguna se acelera '
                              'al final, que es lo que pasa cuando se ve venir el Do',
                          events=[n('G4'), n('F4'), n('E4'), n('D4'),
                                  n('C4', 'h'), sil('h')],
                          bars=2),
                     dict(cap='b) y el mismo descenso empezando más arriba · la última se sostiene '
                              'entera, sin soltarla antes de tiempo',
                          events=[n('C5'), n('B4'), n('A4'), n('G4'),
                                  n('F4'), n('E4'), n('D4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UNA ANACRUSA',
                 texto='Una nota, o un par de notas, que suenan antes de que empiece el primer '
                       'compás completo de la pieza. No llevan el peso del pulso: son un impulso '
                       'hacia la nota siguiente. Se cuenta como si el compás ya hubiera empezado '
                       'antes, y se entra en el tiempo exacto que le corresponde.'),
            dict(num=4, titulo='Las dos juntas',
                 pista='andamio · la izquierda dobla a la derecha, una octava abajo · despacio',
                 sistemas=[
                     dict(cap='a) las dos manos con la anacrusa a la vez',
                          events=[ac(('G3', 'E4'), 'e'), ac(('A3', 'F4'), 'e'),
                                  ac(('G3', 'G4')), ac(('A3', 'A4')), ac(('G3', 'G4')),
                                  ac(('F3', 'F4')), ac(('E3', 'E4')), n('D4'), n('C4')],
                          bars=2),
                     dict(cap='b) y con la frase que sube',
                          events=[ac(('B3', 'G4'), 'e'), ac(('C4', 'A4'), 'e'),
                                  ac(('B3', 'B4')), ac(('C4', 'C5')), ac(('B3', 'B4')),
                                  ac(('A3', 'A4')), ac(('G3', 'G4')), n('F4'), n('E4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=5, titulo='Y ahora seguido, sin parar entre frase y frase',
                 pista='andamio · las dos frases enganchadas, que es como suena en la pieza',
                 sistemas=[
                     dict(cap='a) las dos frases enganchadas · el sitio donde todo el mundo para '
                              'es justo el que no lleva silencio',
                          events=corch(['E4', 'F4']) + [n('G4'), n('A4'), n('G4'), n('F4'),
                                                        n('E4'), n('D4'), n('C4')]
                                 + [n('B4'), n('C5'), n('B4'), n('A4'),
                                    n('G4'), n('F4'), n('E4'), n('D4')],
                          bars=2),
                     dict(cap='b) y con la izquierda debajo, ya del tirón',
                          events=[ac(('C3', 'E4'), 'e'), ac(('D3', 'F4'), 'e'),
                                  ac(('E3', 'G4')), ac(('F3', 'A4')), ac(('E3', 'G4')),
                                  ac(('D3', 'F4')), ac(('C3', 'E4')), n('D4'), n('C4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
