# -*- coding: utf-8 -*-
"""Toreador, de Carmen — pieza 18 de Isaac.

   Lo comprobado sobre el PDF de su carpeta de Drive (Georges Bizet, arr.
   Gilbert DeBenedetti, *Level Four*, 1 página; el mismo archivo que piezas
   de Mercè, José María y Nel, byte a byte):

     - Detrás de la clave hay UN BEMOL: Fa mayor.
     - El compás se escribe con una C (4/4), y pone "March time".
     - La melodía arranca con la figura de marcha: negra con puntillo y
       corchea.
     - Digitación impresa. Es "Level Four", el escalón más alto de esta
       colección de arreglos.
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
FA = 'Fa mayor'

CANCION = dict(
    alumno='Isaac', carpeta='Isaac', num=18, nivel='intermedio', slug='Toreador',
    formato='adulto',
    titulo_corto='Toreador · Carmen', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'isaac', 'source', 'TOREADOR-BIZET.pdf'),
    yt='https://www.youtube.com/results?search_query=toreador+song+carmen+piano+easy',

    ficha=dict(
        titulo='Toreador · Carmen',
        autor='Georges Bizet · arr. Gilbert DeBenedetti · Nivel cuatro',
        datos=[('Tonalidad', 'Fa mayor'), ('Armadura', 'Un bemol'),
               ('Compás', '4/4'), ('Carácter', 'March time'),
               ('Trae', 'Dedos escritos')],
        titulo_ritmos='La figura de marcha',
        pie_ritmos='Andamio en Fa mayor. Lo literal es el arranque: negra con puntillo y corchea, '
                   'la figura que da a la pieza su paso de marcha.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('UN BEMOL', 'Fa mayor',
                 'Todos los Si de la pieza son bemoles, en las dos manos. Es la misma tonalidad que '
                 'otras piezas de tu cuaderno, así que ya te resulta familiar.'),
                ('FIGURA DE MARCHA', 'Larga y corta',
                 'Es el dibujo rítmico que abre la pieza, y el que le da ese paso firme, como de '
                 'desfile.'),
                ('MARCH TIME', 'Con paso firme',
                 'No es una velocidad concreta, es una manera de tocar: cada golpe cae con la misma '
                 'firmeza, sin arrastrar ninguno.'),
                ('NIVEL CUATRO', 'El más alto',
                 'El propio arreglista la marca como la más exigente de todas las piezas parecidas '
                 'que tienes en tu carpeta.'),
            ],
            pie='Es una de las melodías de ópera más reconocibles del mundo, del tercer acto de '
                'Carmen, cuando el torero Escamillo hace su entrada triunfal.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la figura de marcha · literal',
             [n('F4', 'q.'), n('G4', 'e'), n('Bb4', 'q'), n('C5', 'q')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'acordes que marcan el paso · andamio',
             [n('F2'), ac(('F2', 'A2', 'C3')), n('F2'), ac(('F2', 'A2', 'C3'))], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay un bemol: todos los Si son teclas negras.',
            'El compás se escribe con una C, que equivale a 4/4.',
            'Arriba pone "March time".',
            'La melodía arranca con negra con puntillo y corchea.',
            'Trae la digitación completa impresa.',
            'Es la pieza de nivel más alto de esta colección de arreglos.',
        ],
        reto='Mantener el paso de marcha firme sin acelerarse ni arrastrar. Cada golpe tiene que '
             'sonar igual de decidido que el anterior, del primero al último.',
        truco='Marca el pulso golpeando suavemente con el pie mientras tocas solo la melodía, muy '
              'despacio. Si el pie se desajusta de las manos, es que el compás se ha movido.',
        sabias='La ópera Carmen se estrenó en 1875 y fue un fracaso en su noche de estreno; Bizet '
               'murió tres meses después sin saber que se convertiría en una de las óperas más '
               'representadas de la historia.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la orquesta completa y fíjate en cómo los metales marcan el paso de '
                      'marcha: esa firmeza es la que tiene que tener tu mano derecha.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La figura de marcha es lo nuevo. Se estudia aislada, con el pulso muy marcado, antes '
              'de añadir la izquierda.',
        reglas=['LA FIGURA DE MARCHA, BIEN CONTADA', 'CADA GOLPE, LA MISMA FIRMEZA',
                'MARCH TIME: SIN ARRASTRAR NINGUNO'],
        bloques=[
            dict(num=1, titulo='La mano en Fa mayor',
                 pista='andamio · el bemol está en la armadura',
                 sistemas=[
                     dict(cap='a) bajando desde arriba, con otro dibujo',
                          events=[n('C5'), n('Bb4'), n('A4'), n('G4'),
                                  n('F4'), n('G4'), n('A4'), n('C5')],
                          bars=2),
                     dict(cap='b) y la izquierda, con saltos de cuarta',
                          events=[n('F3'), n('Bb2'), n('F3'), n('Bb2'),
                                  n('C3'), n('F2'), n('C3'), n('F2')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La figura de marcha, aislada',
                 pista='andamio · cuenta "UUUN, y" y marca el paso con el pie',
                 sistemas=[
                     dict(cap='a) larga, corta y dos negras firmes, empezando más arriba',
                          events=[n('A4', 'q.'), n('Bb4', 'e'), n('C5'), n('D5')],
                          bars=1),
                     dict(cap='b) el mismo dibujo, una frase más abajo',
                          events=[n('D4', 'q.'), n('E4', 'e'), n('F4'), n('G4')],
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ SIGNIFICA "MARCH TIME"',
                 texto='No es una cifra de metrónomo, sino una manera de tocar: cada tiempo pesa lo '
                       'mismo que el anterior, sin acelerones ni frenazos.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · los acordes marcan el paso bajo la marcha · despacio',
                 sistemas=[
                     dict(cap='a) el acorde firme en cada tiempo, con otra progresión',
                          events=[ac(('Bb2', 'D4'), 'q.'), n('Eb4', 'e'),
                                  ac(('F2', 'Bb2', 'F4')), ac(('C3', 'F2', 'A4'))],
                          bars=1),
                     dict(cap='b) y con la frase que sube',
                          events=[ac(('C3', 'F4'), 'q.'), n('G4', 'e'),
                                  ac(('C3', 'F3', 'A4')), ac(('F2', 'C3', 'C5'))],
                          bars=1, show_time=False),
                 ]),
        ] + bloques_extra('Fa mayor', 14, 'F4', 'F2',
                          'el Si bemol cae donde la mano ya va deprisa',
                          desde=4, time_sig=(4, 4))[:1],
    ),
)

# El ritmo con puntillo que esta pieza EXPLICA en su texto y no dibujaba en
# ningún sitio. Lo destapó el auditor de vocabulario al ganar la entrada de
# esta figura, que antes no miraba nadie.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + [
    bloque_puntillo('Fa mayor', 6, 'F4', 'el ritmo con puntillo de la marcha',
                    time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
