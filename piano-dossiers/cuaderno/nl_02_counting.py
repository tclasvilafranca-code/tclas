# -*- coding: utf-8 -*-
"""Counting Stars — pieza 2 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (OneRepublic, arr. Becky
   Messer, *Easy Version*, 2 páginas; el mismo archivo que piezas de José
   María, Josep y Mercè, byte a byte), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4.
     - La izquierda toca redondas de dos notas, una por compás, con varias
       ligadas al compás siguiente.
     - La derecha lleva corcheas con la digitación impresa.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from nl_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=2, nivel='avanzado', slug='CountingStars',
    formato='adulto',
    titulo_corto='Counting Stars', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source', 'Counting-stars-.pdf'),
    yt='https://www.youtube.com/results?search_query=counting+stars+piano+easy',

    ficha=dict(
        titulo='Counting Stars',
        autor='OneRepublic · arr. Becky Messer',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Izquierda', 'Redonda doble'), ('Derecha', 'Corcheas'),
               ('Trae', 'Dedos escritos')],
        titulo_ritmos='Corcheas arriba, redondas ligadas abajo',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la izquierda sostiene dos notas '
                   'por compás y la derecha corre en corcheas. Los números de dedo están en tu '
                   'partitura, no aquí: cópialos encima de estas notas antes de estudiar.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('REDONDAS LIGADAS', 'Cruzan el compás',
                 'La izquierda no siempre suelta al final del compás: en varios sitios la nota '
                 'sigue sonando en el siguiente sin volver a tocarla.'),
                ('DIGITACIÓN OBLIGADA', 'Impresa nota a nota',
                 'Con tanta corchea seguida, seguir los dedos exactos evita que la mano se enrede a '
                 'mitad de frase.'),
                ('RESISTENCIA', 'No dificultad',
                 'Ninguna nota suelta es difícil; lo que pide es aguantar el ritmo sin frenar del '
                 'principio al final.'),
                ('POCOS ACORDES', 'Que se repiten',
                 'La izquierda usa muy pocas combinaciones en toda la pieza: aprenderlas bien de '
                 'entrada ahorra trabajo después.'),
            ],
            pie='Es una canción de 2013 muy conocida, y esta versión reduce la melodía a corcheas '
                'claras sobre acordes largos y sostenidos.',
        ),
        ritmos=[
            ('MANO DERECHA', 'corcheas seguidas, sin parar · andamio',
             corch(['G4', 'B4', 'D5', 'B4', 'G4', 'E4', 'G4', 'B4']), OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'redonda doble, a veces ligada · literal',
             [ac(('C3', 'E3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4.',
            'La izquierda toca dos notas a la vez, una redonda por compás.',
            'Varias redondas de la izquierda se ligan al compás siguiente sin tocar de nuevo.',
            'La derecha lleva corcheas, con la digitación impresa nota a nota.',
            'La izquierda usa pocas combinaciones distintas a lo largo de la pieza.',
        ],
        reto='Seguir la digitación impresa aunque una mano "por libre" haría otra cosa. Con tanta '
             'corchea, un dedo fuera de sitio se nota en la nota siguiente.',
        truco='Toca la derecha muy despacio diciendo en voz alta el número de dedo antes de bajarlo, '
              'nota por nota. Sube la velocidad solo cuando los dedos salgan solos sin decirlos.',
        sabias='La canción llegó al número uno en varios países en 2013, y su título hace referencia '
               'a contar estrellas en vez de ovejas para no poder dormir.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la base de acordes largos bajo la melodía. Algunos duran más de un '
                      'compás sin que se note el cambio.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Los números de dedo están en tu partitura, no aquí: cópialos encima y luego '
              'estudia mano a mano siguiéndolos siempre.',
        reglas=['SIGUE LOS DEDOS DE TU PARTITURA', 'LAS DOS NOTAS DE LA IZQUIERDA, JUNTAS',
                'LIGADAS: NO SE TOCAN DOS VECES'],
        bloques=[
            dict(num=1, titulo='La izquierda: redondas dobles, algunas ligadas',
                 pista='andamio en Do mayor · el reparto es el de tu partitura',
                 sistemas=[
                     dict(cap='a) dos notas por compás, sostenidas enteras',
                          events=[ac(('C3', 'E3'), 'w'), ac(('F2', 'A2'), 'w')],
                          ligar=True,
                          bars=2, clef='bass'),
                     dict(cap='b) y una ligada, que no se vuelve a tocar en el compás siguiente',
                          events=[ac(('G2', 'B2'), 'w'), ac(('G2', 'B2'), 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: corcheas con dedos fijos',
                 pista='andamio · copia el dedo de tu partitura y dilo en voz alta al tocar',
                 sistemas=[
                     dict(cap='a) subiendo y bajando por corcheas',
                          events=corch(['C4', 'D4', 'E4', 'F4']) + corch(['G4', 'F4', 'E4', 'D4']),
                          bars=1),
                     dict(cap='b) el mismo dibujo, una tercera más arriba',
                          events=corch(['E4', 'F4', 'G4', 'A4']) + corch(['B4', 'A4', 'G4', 'F4']),
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LAS LIGADAS NO SE VUELVEN A TOCAR',
                 texto='Una nota ligada al compás siguiente es la misma nota que sigue sonando: no '
                       'hay un segundo golpe. Volver a pulsarla corta el fondo continuo que sostiene '
                       'la melodía por encima. Se toca una vez y se deja vivir hasta que le toque '
                       'cambiar de verdad.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda no se mueve mientras la derecha corre · despacio',
                 sistemas=[
                     dict(cap='a) la redonda sostiene bajo las corcheas',
                          events=[ac(('C3', 'E3', 'C4'))] + corch(['D4', 'E4', 'F4', 'G4', 'F4', 'E4'])
                                 + [ac(('F2', 'A2', 'D4'))] + corch(['E4', 'F4', 'G4', 'A4', 'G4', 'F4']),
                          bars=2),
                     dict(cap='b) y con la redonda ligada, sin tocarla otra vez',
                          events=[ac(('G2', 'B2', 'F4'))] + corch(['G4', 'A4', 'B4', 'A4', 'G4', 'F4'])
                                 + [n('E4')] + corch(['F4', 'G4', 'A4', 'B4', 'A4', 'G4']),
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
