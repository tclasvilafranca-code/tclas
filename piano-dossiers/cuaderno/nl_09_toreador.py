# -*- coding: utf-8 -*-
"""Toreador, de Carmen — pieza 9 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (Georges Bizet, arreglo
   de Gilbert DeBenedetti, "Level Four", 1 página; el mismo archivo que la
   pieza 15 de José María y una pieza de Mercè, byte a byte):

     - Fa mayor: un bemol detrás de la clave. Todos los Si van a la tecla
       negra.
     - El compás se escribe con una C, que es 4/4. Pone "March time".
     - Es "Level Four": el escalón más alto de este arreglista.
     - La digitación viene impresa, y la melodía arranca con negra con
       puntillo y corchea, la figura de marcha.
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
FA = 'Fa mayor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=9, nivel='avanzado', slug='Toreador',
    formato='adulto',
    titulo_corto='Toreador · Carmen', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source',
                           'Copia de Copia de Toreador. Bizet'),
    yt='https://www.youtube.com/results?search_query=toreador+song+carmen+piano+easy',

    ficha=dict(
        titulo='Toreador',
        autor='Georges Bizet · de la ópera Carmen · arr. Gilbert DeBenedetti · Level Four',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', 'C (4/4)'),
               ('Carácter', 'March time'), ('Nivel', 'Level Four'),
               ('Páginas', 'Una')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Fa mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Los Si, todos a la tecla negra.',
        armonia=dict(
            titulo='Una marcha de verdad',
            tarjetas=[
                ('LEVEL FOUR', 'El más alto',
                 'Del mismo arreglista, es el nivel más exigente de todos: más notas por compás y '
                 'las dos manos siempre ocupadas.'),
                ('LA ARMADURA', 'Un bemol',
                 'Fa mayor: todos los Si van a la tecla negra de al lado, del primer compás al '
                 'último.'),
                ('EL RITMO', 'De marcha',
                 'Negra con puntillo y corchea, una y otra vez: es lo que hace que suene a desfile y '
                 'no a canción tranquila.'),
                ('MARCH TIME', 'Ni rápido ni lento',
                 'A paso de marcha: firme y regular. No es una velocidad, es un carácter que no se '
                 'mueve ni un poco.'),
            ],
            pie='Bizet la escribió a disgusto: le pidieron un número pegadizo para el torero y él lo '
                'llamó "porquería", pero es, con diferencia, lo más conocido que compuso.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el ritmo de marcha: larga y corta · andamio',
             [n('C5', 'q.'), {'pitch': 'A4', 'dur': 'e'}, n('F4'), n('A4')],
             OCRE, 'treble', FA),
            ('MANO IZQUIERDA', 'firme, marcando el paso · andamio',
             [ac(('F2', 'C3'), 'h'), ac(('C3', 'F3'), 'h')], AZUL, 'bass', FA),
        ],
        especial=[
            'Hay un bemol detrás de la clave: todos los Si van a la tecla negra.',
            'El compás se escribe con una C, que quiere decir 4/4.',
            'Pone "March time": a paso de marcha, firme y regular.',
            'La melodía va en negra con puntillo y corchea casi todo el rato.',
            'La digitación viene impresa.',
            'El arreglista la marca como Level Four, el nivel más alto de esta colección.',
        ],
        reto='Que el ritmo de marcha no se ablande: la negra con puntillo tiende a acortarse y la '
             'corchea a adelantarse, y en cuanto eso pasa deja de sonar a marcha.',
        truco='Marca el paso con el pie mientras tocas: pie abajo en el uno y en el tres, y la '
              'corchea cae justo antes de que el pie vuelva a bajar.',
        sabias='Murió tres meses después del estreno de Carmen, convencido de que había sido un '
               'fracaso. Hoy es una de las óperas más representadas del mundo entero.',
        qr=dict(titulo='Escúchala',
                texto='Escucha una versión de orquesta y fíjate en el pulso: no acelera ni un poco en '
                      'toda la pieza. Eso es "March time".'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La tonalidad ya la conoces. Lo que sube de nivel aquí es que el ritmo de marcha y las '
              'dos manos ocupadas van juntos y rápido. Trabájalas por separado y júntalas al final.',
        reglas=['LOS SI, EN LA TECLA NEGRA', 'LA LARGA DURA LO QUE DURA',
                'EL PULSO NO SE MUEVE'],
        bloques=[
            dict(num=1, titulo='El ritmo de marcha, con un salto más amplio',
                 pista='andamio en Fa mayor · negra con puntillo y corchea',
                 sistemas=[
                     dict(cap='a) primero todo en negras, con el salto de la melodía',
                          events=[n('F4'), n('C5'), n('A4'), n('F4'),
                                  n('D4'), n('Bb4'), n('G4'), n('F4')],
                          bars=2, key_sig=FA),
                     dict(cap='b) y ahora con el puntillo · cuenta "UN dos-y TRES cuatro" y marca el '
                              'paso con el pie',
                          events=[n('F4', 'q.'), {'pitch': 'C5', 'dur': 'e'}, n('A4'), n('F4'),
                                  n('D4', 'q.'), {'pitch': 'Bb4', 'dur': 'e'}, n('G4'), n('F4')],
                          bars=2, key_sig=FA, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: el paso', clef='bass',
                 pista='andamio en Fa mayor · firme, y sin acelerar nunca',
                 sistemas=[
                     dict(cap='a) dos apoyos por compás, un acorde distinto en cada uno',
                          events=[ac(('Bb2', 'F3'), 'h'), ac(('D3', 'A3'), 'h'),
                                  ac(('G2', 'D3'), 'h'), ac(('C3', 'G3'), 'h')],
                          bars=2, clef='bass', key_sig=FA),
                     dict(cap='b) y cambiando de acorde sin que el paso se note · el pulso manda',
                          events=[ac(('Bb2', 'F3'), 'h'), ac(('F2', 'C3'), 'h'),
                                  ac(('G2', 'D3'), 'h'), ac(('C3', 'G3'), 'h'),
                                  ac(('F2', 'C3'), 'h'), ac(('Bb2', 'F3'), 'h')],
                          bars=3, clef='bass', key_sig=FA, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL PULSO NO PUEDE MOVERSE',
                 texto='En una marcha, el pulso es lo único que no se negocia: puede haber notas más '
                       'difíciles, saltos más grandes, pero el paso sigue firme siempre igual. Si el '
                       'pulso se mueve cuando llega una nota complicada, deja de sonar a desfile y '
                       'suena a duda. Practica primero muy despacio, con el pie marcando, hasta que '
                       'ninguna nota lo haga temblar.'),
            dict(num=3, titulo='Las dos manos, dos compases',
                 pista='andamio · despacio, con el pie marcando el paso',
                 sistemas=[
                     dict(cap='a) la derecha con su marcha encima del paso de la izquierda',
                          events=[n('F4', 'q.'), {'pitch': 'C5', 'dur': 'e'}, n('A4'), n('F4'),
                                  n('D4', 'h'), n('F4', 'h')],
                          bars=2, key_sig=FA),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · el paso no cambia porque '
                              'la derecha se complique',
                          events=[ac(('Bb2', 'F3'), 'h'), ac(('D3', 'A3'), 'h'),
                                  ac(('G2', 'D3'), 'h'), ac(('Bb2', 'F3'), 'h')],
                          bars=2, clef='bass', key_sig=FA, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
