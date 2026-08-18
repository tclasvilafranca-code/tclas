# -*- coding: utf-8 -*-
"""Diamonds (Rihanna) — pieza 12 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Rihanna - Diamond,
   easy piano - short form", medido a 230 dpi; la única partitura de sus 17
   que no coincide byte a byte con la de ningún otro alumno):

     - RE MAYOR: dos sostenidos detrás de la clave.
     - 4/4, y pone "♩ = 91".
     - Empieza con ANACRUSA: silencio y una corchea de entrada.
     - La melodía lleva una nota larga ligada al final de cada frase.
     - La izquierda hace acordes de dos y tres notas: una redonda en el
       primer compás y después notas dobles en negras.
     - Trae letra completa y digitación impresa en las dos manos.

   Lo que NO se cita nota a nota: no se ha medido cabeza por cabeza (a '
   diferencia de las 16 piezas heredadas de otros alumnos, esta se ha
   comprobado solo a nivel de estructura). El material va como ANDAMIO en
   Re mayor y remite a la partitura.
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
RE = 'Re mayor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=12, nivel='avanzado', slug='Diamonds',
    formato='adulto',
    titulo_corto='Diamonds', time_sig=(4, 4), key_sig=RE,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source', 'rihanna-diamond-.pdf'),
    yt='https://www.youtube.com/results?search_query=diamonds+rihanna+piano+easy',

    ficha=dict(
        titulo='Diamonds',
        autor='Rihanna · easy piano, short form',
        datos=[('Tonalidad', 'Re mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 91'), ('Empieza', 'Con anacrusa'),
               ('Trae', 'Letra completa')],
        titulo_ritmos='La anacrusa, y el reparto de las dos manos',
        pie_ritmos='Andamio en Re mayor. Lo literal es la entrada: silencio y una corchea antes del '
                   'primer compás, y la izquierda con una redonda al principio.',
        armonia=dict(
            titulo='Tu pieza propia de este álbum',
            tarjetas=[
                ('ANACRUSA CORTA', 'Antes del compás',
                 'La pieza no empieza en el uno: hay un silencio y una sola corchea de entrada antes '
                 'del primer compás completo.'),
                ('NOTAS LIGADAS', 'Al final de cada frase',
                 'La melodía sostiene una nota larga, ligada, al terminar cada frase: no se vuelve a '
                 'tocar, se deja sonar.'),
                ('LA IZQUIERDA CAMBIA', 'De textura',
                 'Empieza con una redonda entera en el primer compás y después pasa a notas dobles '
                 'en negras: dos texturas distintas en la misma pieza.'),
                ('TODO ESCRITO', 'Letra y dedos',
                 'Trae la letra completa debajo del pentagrama y la digitación impresa en las dos '
                 'manos, nota a nota.'),
            ],
            pie='Es la única partitura de tu carpeta que no comparte archivo con ningún otro alumno '
                'del cuaderno: esta es completamente tuya.',
        ),
        ritmos=[
            ('MANO DERECHA', 'anacrusa de silencio y corchea · andamio',
             [sil('e'), {'pitch': 'A4', 'dur': 'e'}, n('D5'), n('D5'), n('C#5')],
             OCRE, 'treble', RE),
            ('MANO IZQUIERDA', 'redonda y después dobles en negras · andamio',
             [n('D3', 'w')], AZUL, 'bass', RE),
        ],
        especial=[
            'Hay dos sostenidos detrás de la clave: Fa y Do.',
            'Compás de 4/4, "♩ = 91" impreso.',
            'La pieza empieza con un silencio y una sola corchea antes del primer compás.',
            'La melodía sostiene una nota larga ligada al final de cada frase.',
            'La izquierda empieza con una redonda y después pasa a notas dobles en negras.',
            'Trae letra completa y digitación impresa en las dos manos.',
        ],
        reto='Que la nota ligada del final de cada frase no se vuelva a tocar: con tanta letra debajo '
             'del pentagrama es fácil perder de vista qué sílaba va con qué nota, y repetir un golpe '
             'que no toca.',
        truco='Canta la letra en voz alta mientras sigues la partitura con el dedo, sin tocar. Una '
              'vez que la frase esté clara en la voz, las notas ligadas dejan de sorprender.',
        sabias='La canción participó en la composición Sia, que la escribió pensando en cantarla ella '
               'misma antes de ofrecérsela a Rihanna, y se convirtió en uno de sus mayores éxitos.',
        qr=dict(titulo='Escúchala',
                texto='Sigue la letra mientras escuchas y localiza dónde cae cada nota larga ligada: '
                      'suele coincidir con el final de una idea de la frase.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas de verdad: la anacrusa corta de una sola corchea y que la izquierda '
              'cambia de textura a mitad de pieza. Se aíslan las dos por separado antes de juntarlas.',
        reglas=['LA ANACRUSA ES UNA CORCHEA, NO MÁS', 'LAS LIGADAS NO SE VUELVEN A TOCAR',
                'LA IZQUIERDA CAMBIA DE TEXTURA A MITAD'],
        bloques=[
            dict(num=1, titulo='La anacrusa, aislada',
                 pista='andamio en Re mayor · el mismo dibujo de la partitura',
                 sistemas=[
                     dict(cap='a) silencio, una corchea, y entra el compás',
                          events=[sil('e'), {'pitch': 'A4', 'dur': 'e'},
                                  n('D5'), n('D5'), n('C#5'), n('B4'), n('A4'), n('F#4'), n('D4')],
                          bars=2),
                     dict(cap='b) el mismo dibujo, una frase más abajo',
                          events=[sil('e'), {'pitch': 'F#4', 'dur': 'e'},
                                  n('B4'), n('B4'), n('A4'), n('G4'), n('F#4'), n('D4'), n('A4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: redonda y después dobles', clef='bass',
                 pista='andamio · dos texturas distintas en la misma pieza',
                 sistemas=[
                     dict(cap='a) la redonda del principio, sostenida entera',
                          events=[n('D3', 'w'), n('A2', 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) y ahora las notas dobles en negras, que llegan después',
                          events=[ac(('D3', 'F#3')), ac(('A2', 'D3')),
                                  ac(('G2', 'B2')), ac(('A2', 'C#3'))],
                          bars=1, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LAS LIGADAS NO SE VUELVEN A TOCAR',
                 texto='Una nota ligada al compás siguiente es la misma nota que sigue sonando: no '
                       'hay un segundo golpe. En esta pieza, además, suele caer justo donde termina '
                       'una frase de la letra: cantarla en voz alta ayuda a sentir dónde se sostiene '
                       'y dónde empieza otra vez.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda cambia de textura, la derecha sigue con sus ligadas',
                 sistemas=[
                     dict(cap='a) con la redonda sosteniendo bajo la anacrusa',
                          events=[ac(('D3', 'A4')), sil('e'), {'pitch': 'A4', 'dur': 'e'},
                                  n('D5'), n('D5'), n('C#5'), n('B4'), n('A4'), n('F#4')],
                          bars=2),
                     dict(cap='b) y ya con las dobles de la izquierda debajo',
                          events=[ac(('D3', 'F#3', 'A4')), ac(('A2', 'D3', 'D5')),
                                  ac(('G2', 'B2', 'C#5')), ac(('A2', 'C#3', 'B4')),
                                  ac(('D3', 'F#3', 'A4')), ac(('A2', 'D3', 'C#5')),
                                  ac(('G2', 'B2', 'B4'), 'h')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
