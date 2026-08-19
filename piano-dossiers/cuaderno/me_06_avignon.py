# -*- coding: utf-8 -*-
"""Sur le Pont d'Avignon — pieza 6 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Sur le Pont d'Avignon
   — On the Bridge at Avignon", Deuxième Niveau / Level Two, arr. Gilbert
   DeBenedetti, 1 página), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4 (escrito como "c").
     - La derecha se mueve en corcheas agrupadas de tres en tres, con puntos
       de staccato, y algún silencio de corchea entre grupos.
     - La izquierda toca acordes de dos notas también en corcheas, siguiendo
       el mismo pulso que la derecha.
     - Trae dedos escritos (1 y 2).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from me_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=6, nivel='intermedio', slug='SurLePontDAvignon',
    formato='adulto',
    titulo_corto="Sur le Pont d'Avignon", time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', "SUR LE PONT D'AVIGNON.pdf"),
    yt='https://www.youtube.com/results?search_query=sur+le+pont+davignon+piano',

    ficha=dict(
        titulo="Sur le Pont d'Avignon",
        autor='Tradicional francesa · arr. Gilbert DeBenedetti · Nivel dos',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Figuras', 'Corcheas'), ('Carácter', 'Not too fast'),
               ('Trae', 'Dedos escritos')],
        titulo_ritmos='Corcheas en las dos manos, a la vez',
        pie_ritmos='Andamio en Do mayor. Lo literal es el pulso: las dos manos se mueven en '
                   'corcheas juntas, con algún silencio corto entre grupos.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('CORCHEAS EN LAS DOS MANOS', 'A la vez',
                 'Hasta ahora la izquierda solía sostener notas largas. Aquí se mueve en corcheas, '
                 'igual que la derecha, y las dos tienen que ir sincronizadas.'),
                ('STACCATO', 'Cortas y separadas',
                 'Los puntitos sobre las notas piden que suenen cortas, casi picadas, no ligadas '
                 'unas con otras.'),
                ('GRUPOS DE TRES', 'Con un hueco',
                 'La melodía se organiza en grupitos de tres corcheas seguidas de un pequeño hueco. '
                 'Contar el hueco es tan importante como tocar las notas.'),
                ('ACORDES DE DOS NOTAS', 'En la izquierda',
                 'La mano izquierda toca intervalos, no notas sueltas, y los repite en el mismo '
                 'ritmo que la melodía.'),
            ],
            pie='Es una de las canciones populares francesas más conocidas, y aquí en una versión '
                'con las dos manos activas, un paso por delante de las piezas anteriores.',
        ),
        ritmos=[
            ('MANO DERECHA', 'grupos de tres corcheas y un silencio · andamio',
             corch(['G4', 'A4', 'B4']) + [sil('e')] + corch(['A4', 'B4', 'C5']) + [sil('e')],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'acordes de dos notas en corcheas · andamio',
             [ac(('G2', 'B2'), 'e'), ac(('G2', 'B2'), 'e'), ac(('G2', 'B2'), 'e'), sil('e')] * 2,
             AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4, escrito como "c".',
            'La derecha se mueve en grupos de tres corcheas con puntos de staccato.',
            'Entre los grupos aparece un pequeño silencio de corchea.',
            'La izquierda toca acordes de dos notas, también en corcheas.',
            'Trae los dedos 1 y 2 escritos sobre las primeras notas.',
        ],
        reto='Que el silencio entre grupos de corcheas no se coma ni se alargue. Al ser tan corto, '
             'es fácil perder la cuenta exacta y desajustar todo lo que viene después.',
        truco='Cuenta en corcheas todo el rato ("un-y, dos-y, tres-y, cuatro-y") y toca solo los '
              'puntos donde caen las notas, dejando el resto en silencio real. Cuando el hueco te '
              'salga igual todas las veces, añade el staccato.',
        sabias='La canción habla de bailar sobre un puente de Aviñón que, en realidad, era demasiado '
               'estrecho para bailar encima: se bailaba debajo, en una isla del río, y el título se '
               'simplificó con el tiempo.',
        qr=dict(titulo='Escúchala',
                texto='Escucha los pequeños silencios entre frases. Son cortísimos, pero están, y '
                      'son los que le dan el aire de baile a la melodía.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo son las corcheas en las dos manos y el staccato. Se aprenden por separado '
              'antes de juntarlas.',
        reglas=['CUENTA EN CORCHEAS TODO EL RATO', 'STACCATO: CORTO, NO LIGADO',
                'EL SILENCIO SE CUENTA IGUAL QUE UNA NOTA'],
        bloques=[
            dict(num=1, titulo='La derecha: grupos de tres corcheas y un hueco',
                 pista='andamio en Do mayor · el reparto es el de tu partitura',
                 sistemas=[
                     dict(cap='a) tres corcheas cortas y un silencio, dos veces',
                          events=corch(['C4', 'D4', 'E4']) + [sil('e')]
                                 + corch(['D4', 'E4', 'F4']) + [sil('e')],
                          staccato=True,
                          bars=1),
                     dict(cap='b) el mismo dibujo un poco más arriba',
                          events=corch(['E4', 'F4', 'G4']) + [sil('e')]
                                 + corch(['F4', 'G4', 'A4']) + [sil('e')],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: acordes de dos notas en corcheas',
                 pista='andamio · el mismo pulso que la derecha, sin melodía',
                 sistemas=[
                     dict(cap='a) el intervalo se repite y calla en el mismo hueco',
                          events=[ac(('C3', 'E3'), 'e'), ac(('C3', 'E3'), 'e'),
                                  ac(('C3', 'E3'), 'e'), sil('e')] * 2,
                          bars=1, clef='bass'),
                     dict(cap='b) cambiando de acorde, con el mismo silencio',
                          events=[ac(('F2', 'A2'), 'e'), ac(('F2', 'A2'), 'e'),
                                  ac(('F2', 'A2'), 'e'), sil('e')] * 2,
                          bars=1, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL SILENCIO CUENTA COMO UNA NOTA MÁS',
                 texto='En un grupo de "tres corcheas y silencio" el hueco no es una pausa libre: '
                       'dura exactamente lo mismo que cualquiera de las tres notas que lo rodean. Si '
                       'se toca sin contar, el grupo siguiente entra a destiempo y toda la frase se '
                       'desplaza. Contar en corcheas todo el rato, incluso en el silencio, es lo que '
                       'mantiene el pulso.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · el mismo silencio en las dos manos a la vez · despacio',
                 sistemas=[
                     dict(cap='a) las corcheas y el silencio coinciden en las dos manos',
                          events=[ac(('C3', 'E3', 'C4'), 'e'), ac(('C3', 'E3', 'D4'), 'e'),
                                  ac(('C3', 'E3', 'E4'), 'e'), sil('e'),
                                  ac(('F2', 'A2', 'D4'), 'e'), ac(('F2', 'A2', 'E4'), 'e'),
                                  ac(('F2', 'A2', 'F4'), 'e'), sil('e')],
                          bars=1),
                     dict(cap='b) y con la frase que sube',
                          events=[ac(('C3', 'E3', 'E4'), 'e'), ac(('C3', 'E3', 'F4'), 'e'),
                                  ac(('C3', 'E3', 'G4'), 'e'), sil('e'),
                                  ac(('F2', 'A2', 'F4'), 'e'), ac(('F2', 'A2', 'G4'), 'e'),
                                  ac(('F2', 'A2', 'A4'), 'e'), sil('e')],
                          bars=1, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
