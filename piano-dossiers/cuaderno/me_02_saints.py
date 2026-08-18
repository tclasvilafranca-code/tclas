# -*- coding: utf-8 -*-
"""Oh, When the Saints — pieza 2 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Oh, When the Saints",
   Primer Level, arr. Gilbert DeBenedetti, 1 página), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4, y arriba pone "Lively".
     - La melodía lleva los dedos escritos (1 y 3 en las primeras notas) y
       letra debajo de cada nota.
     - La derecha alterna negras sueltas con una redonda al final de cada
       frase de dos compases.
     - La izquierda hace un silencio de negra seguido de tres negras, que se
       repite compás a compás.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from me_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=2, nivel='intermedio', slug='OhWhenTheSaints',
    formato='adulto',
    titulo_corto='Oh, When the Saints', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'OH WHEN THE SAINT.pdf'),
    yt='https://www.youtube.com/results?search_query=oh+when+the+saints+go+marching+in+easy+piano',

    ficha=dict(
        titulo='Oh, When the Saints',
        autor='Tradicional · arr. Gilbert DeBenedetti · Primer nivel',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Lively · animado'), ('Izquierda', 'Silencio y negras'),
               ('Trae', 'Dedos y letra')],
        titulo_ritmos='Un silencio que se repite cada compás',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la izquierda calla el primer '
                   'tiempo de cada compás y luego hace tres negras seguidas.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('EL SILENCIO SE REPITE', 'Cada compás',
                 'La izquierda calla siempre en el mismo sitio: el primer tiempo. Una vez lo tienes '
                 'en el cuerpo, ya no hay que pensarlo compás a compás.'),
                ('FRASES DE DOS COMPASES', 'Y acaban en redonda',
                 'La melodía se organiza en frases cortas que siempre terminan igual: una nota larga '
                 'que dura el compás entero.'),
                ('LOS DEDOS VIENEN ESCRITOS', 'Al principio',
                 'Solo aparecen en las primeras notas, para que arranques con la mano bien '
                 'colocada; el resto lo continúa la misma posición.'),
                ('LIVELY', 'Animado, no rápido',
                 'Es una marcha de banda de Nueva Orleans: se camina con ella, no se corre.'),
            ],
            pie='Es una de las piezas más grabadas de la historia del jazz, y aquí llega en su '
                'versión más sencilla: solo negras y alguna redonda.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negras y la redonda que cierra la frase · andamio',
             [n('C4'), n('D4'), n('E4'), n('F4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'silencio y tres negras, cada compás · literal',
             [sil('q'), n('C3'), n('C3'), n('C3')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4, con "Lively" escrito arriba.',
            'La melodía trae los dedos escritos al principio, y la letra debajo de las notas.',
            'La derecha combina negras sueltas con una redonda al final de cada frase.',
            'La izquierda calla el primer tiempo de cada compás y hace tres negras después.',
            'El silencio de la izquierda se repite igual, compás tras compás.',
        ],
        reto='Que el silencio de la izquierda no se coma el primer tiempo de la derecha. Aunque una '
             'mano calle, la cuenta de las dos sigue exactamente igual.',
        truco='Toca solo la izquierda contando "UNO (silencio), dos, tres, cuatro" en voz alta, '
              'marcando el "uno" con la cabeza aunque no suene nada. Cuando el hueco te salga sin '
              'dudar, añade la derecha.',
        sabias='Es un espiritual afroamericano de origen incierto que se hizo famoso como marcha de '
               'las bandas de Nueva Orleans en los entierros: alegre a la ida, solemne a la vuelta.',
        qr=dict(titulo='Escúchala',
                texto='Escucha una versión de banda y cuenta en qué tiempo entra cada instrumento. '
                      'El "silencio que se repite" de tu izquierda es el mismo hueco que dejan ellos.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El silencio de la izquierda es lo único nuevo. Se aprende solo, después con la '
              'derecha, y al final entero.',
        reglas=['LA IZQUIERDA CALLA EL PRIMER TIEMPO', 'CUENTA EN VOZ ALTA, TAMBIÉN EL SILENCIO',
                'LIVELY: CON GANAS, SIN CORRER'],
        bloques=[
            dict(num=1, titulo='La izquierda: silencio y tres negras',
                 pista='andamio en Do mayor · el reparto es el de tu partitura',
                 sistemas=[
                     dict(cap='a) callas el primer tiempo y tocas los otros tres · marca el hueco '
                              'con la cabeza',
                          events=[sil('q'), n('C3'), n('C3'), n('C3'),
                                  sil('q'), n('F2'), n('F2'), n('F2')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de acorde cada compás · el silencio siempre en el mismo '
                              'sitio',
                          events=[sil('q'), n('G2'), n('G2'), n('G2'),
                                  sil('q'), n('C3'), n('C3'), n('C3')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: negras y una redonda final',
                 pista='andamio · la frase acaba siempre en una nota larga',
                 sistemas=[
                     dict(cap='a) cuatro negras y la redonda que cierra la frase',
                          events=[n('C4'), n('D4'), n('E4'), n('F4'), n('C4', 'w')],
                          bars=2),
                     dict(cap='b) y la frase siguiente, con el mismo dibujo',
                          events=[n('E4'), n('F4'), n('G4'), n('A4'), n('E4', 'w')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL SILENCIO SE ESTUDIA SOLO PRIMERO',
                 texto='Un silencio que se repite parece que no hace falta practicarlo, y es al '
                       'revés: como no suena nada, la mano tiende a entrar antes de tiempo sin '
                       'darse cuenta. Contarlo en voz alta durante unos compases, solo con la '
                       'izquierda, es lo que evita ese adelanto cuando se junta con la derecha.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · muy despacio, contando el silencio en voz alta',
                 sistemas=[
                     dict(cap='a) la derecha entra sola en el primer tiempo, donde calla la '
                              'izquierda; luego se juntan',
                          events=[n('C4'), ac(('C3', 'D4')), ac(('C3', 'E4')), ac(('C3', 'F4')),
                                  ac(('C3', 'C4'), 'w')],
                          bars=2),
                     dict(cap='b) y con la frase que sube más',
                          events=[n('E4'), ac(('F2', 'F4')), ac(('F2', 'G4')), ac(('F2', 'A4')),
                                  ac(('F2', 'E4'), 'w')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
