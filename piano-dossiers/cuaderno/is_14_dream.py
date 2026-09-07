# -*- coding: utf-8 -*-
"""I Have a Dream, de Abba — pieza 14 de Isaac.

   Lo comprobado sobre el PDF de su carpeta de Drive ("I have a dream", Abba,
   "TEMPO-120", INeVENT Music Academy, 2 páginas; el mismo archivo que la
   pieza 20 de Mercè y la 6 de Luisa, byte a byte):

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4, y pone "TEMPO=120".
     - Trae la letra de la canción debajo del pentagrama.
     - La derecha combina negras con el primer dibujo de puntillo del álbum:
       negra con puntillo y corchea.
     - La izquierda hace redondas y alguna blanca.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra, bloque_puntillo
from is_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Isaac', carpeta='Isaac', num=14, nivel='intermedio', slug='IHaveADream',
    formato='adulto',
    titulo_corto='I Have a Dream', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'isaac', 'source', 'i-have-a-dream-abba-.pdf'),
    yt='https://www.youtube.com/results?search_query=i+have+a+dream+abba+easy+piano',

    ficha=dict(
        titulo='I Have a Dream',
        autor='ABBA · INeVENT Music Academy',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 120'), ('Izquierda', 'Redondas'),
               ('Derecha', 'Puntillo')],
        titulo_ritmos='Un puntillo para trabajar con precisión',
        pie_ritmos='Andamio en Do mayor. Lo literal es el dibujo: negra con puntillo y corchea en '
                   'la derecha, redondas en la izquierda.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('EL PUNTILLO', 'Larga y corta',
                 'Es la primera vez en tu cuaderno que aparece este dibujo: una nota que dura '
                 'tiempo y medio, seguida de una corta que completa el tiempo que falta.'),
                ('LA IZQUIERDA SOSTIENE', 'Redondas',
                 'Vuelve al reparto más sencillo: una nota que dura el compás entero, sin '
                 'complicarse mientras la derecha trabaja el puntillo.'),
                ('LETRA COMPLETA', 'Sílaba a sílaba',
                 'Trae la canción entera escrita, sílaba a sílaba, lo que ayuda a sentir dónde cae '
                 'cada nota con puntillo.'),
                ('♩ = 120', 'Con número',
                 'Tiene tempo escrito, así que puedes comprobar con el metrónomo si el puntillo '
                 'mantiene su proporción exacta a esa velocidad.'),
            ],
            pie='Es una de las canciones más conocidas de ABBA, con un mensaje de esperanza que la '
                'ha hecho durar generaciones después de su estreno en 1979.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negra con puntillo y corchea · andamio',
             [n('G4', 'q.'), n('A4', 'e'), n('B4', 'q.'), n('A4', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una redonda por compás · literal',
             [n('C3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4, con "♩ = 120" escrito arriba.',
            'Trae la letra de la canción completa, debajo del pentagrama.',
            'La derecha combina negra con puntillo y corchea.',
            'La izquierda hace redondas, con alguna blanca.',
            'El dibujo de puntillo se repite varias veces a lo largo de la melodía.',
        ],
        reto='Que la corchea del puntillo no se alargue ni se acorte.',
        truco='Cuenta en corcheas todo el compás ("un-y, dos-y, tres-y, cuatro-y") y toca la nota '
              'larga en "un" sosteniéndola hasta "dos".',
        sabias='ABBA la publicó en 1979 y se ha convertido en una de sus canciones más versionadas, '
               'incluida una famosa grabación de Westlife casi veinte años después.',
        qr=dict(titulo='Escúchala',
                texto='Sigue la letra mientras escuchas y marca con el dedo dónde cae cada sílaba.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El puntillo es lo nuevo de esta semana. Se aísla, se cuenta en corcheas, y solo '
              'entonces se junta con la izquierda.',
        reglas=['CUENTA EN CORCHEAS EL COMPÁS ENTERO', 'LA LARGA DURA TIEMPO Y MEDIO EXACTO',
                'LA IZQUIERDA SOSTIENE, SIN MÁS'],
        bloques=[
            dict(num=1, titulo='El puntillo, aislado y contado',
                 pista='andamio en Do mayor · cuenta en voz alta antes de tocar',
                 sistemas=[
                     dict(cap='a) larga, corta, empezando más arriba',
                          events=[n('G4', 'q.'), n('A4', 'e'), n('B4', 'q.'), n('G4', 'e')],
                          bars=1),
                     dict(cap='b) el mismo dibujo, una frase más abajo',
                          events=[n('D4', 'q.'), n('E4', 'e'), n('F4', 'q.'), n('D4', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: redondas que sostienen',
                 pista='andamio · una nota por compás, sin moverse',
                 sistemas=[
                     dict(cap='a) toca en el uno y aguanta el compás entero, otra combinación',
                          events=[n('D3', 'w'), n('G2', 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de nota, con la misma sujeción',
                          events=[n('A2', 'w'), n('D3', 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SUENA UN PUNTILLO BIEN CONTADO',
                 texto='Un puntillo añade la mitad del valor de la nota: una negra con puntillo dura '
                       'lo mismo que negra más corchea juntas. Si se cuenta en corcheas todo el '
                       'compás, el sitio exacto de la nota corta aparece solo, sin necesidad de '
                       'adivinarlo.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda no se mueve mientras la derecha marca el puntillo',
                 sistemas=[
                     dict(cap='a) la redonda sostiene bajo el dibujo de puntillo, otro punto de '
                              'partida',
                          events=[ac(('D3', 'D4'), 'q.'), n('E4', 'e'),
                                  ac(('D3', 'F4'), 'q.'), n('D4', 'e')],
                          bars=1),
                     dict(cap='b) y con la frase que baja',
                          events=[ac(('G2', 'B4'), 'q.'), n('C5', 'e'),
                                  ac(('G2', 'A4'), 'q.'), n('B4', 'e')],
                          bars=1, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 69, 'C5', 'C3',
                          'entra después del silencio, en el segundo golpe',
                          desde=4, time_sig=(4, 4))[:1],
    ),
)

# El ritmo con puntillo que esta pieza EXPLICA en su texto y no dibujaba en
# ningún sitio. Lo destapó el auditor de vocabulario al ganar la entrada de
# esta figura, que antes no miraba nadie.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + [
    bloque_puntillo('Do mayor', 6, 'C4', 'el puntillo del estribillo',
                    time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
