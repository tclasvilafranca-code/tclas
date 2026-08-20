# -*- coding: utf-8 -*-
"""Piano Man, de Billy Joel — pieza 10 de Isaac.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Piano Man (Easy) —
   Simplified version from SimplyPiano", arr. JuanM04, 2 páginas; el mismo
   archivo que la pieza 13 de Mercè y la 11 de Luisa, byte a byte):

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 3/4, y pone "♩ = 178".
     - La derecha empieza con medio compás callado y entra en el tercer
       tiempo.
     - La izquierda pasa la mayoría de los compases callada, y cuando entra
       toca dos notas juntas que ocupan el compás completo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from is_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Isaac', carpeta='Isaac', num=10, nivel='intermedio', slug='PianoMan',
    formato='adulto',
    titulo_corto='Piano Man', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'isaac', 'source', 'Piano Men.pdf'),
    yt='https://www.youtube.com/results?search_query=piano+man+billy+joel+easy+piano',

    ficha=dict(
        titulo='Piano Man',
        autor='Billy Joel · versión simplificada de SimplyPiano · arr. JuanM04',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Tempo', '♩ = 178'), ('Izquierda', 'Casi no toca'),
               ('Empieza', 'En el tercer tiempo')],
        titulo_ritmos='La izquierda entra poco y aguanta',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la derecha lleva toda la '
                   'melodía y la izquierda solo aparece de vez en cuando, con el compás entero.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('♩ = 178', 'Rápido de reloj',
                 'Parece mucho, y lo es de reloj. En compás de tres son unos 59 compases por '
                 'minuto: un compás por segundo. Contado así ya no asusta tanto.'),
                ('LA IZQUIERDA DESCANSA', 'Compases enteros',
                 'La mayoría de compases de la izquierda son silencio. Cuando entra, toca dos notas '
                 'a la vez y las aguanta los tres tiempos.'),
                ('ENTRA EN EL TERCERO', 'Medio compás',
                 'La derecha empieza con un silencio de blanca. Hay que contar uno y dos en '
                 'silencio y tocar en el tres.'),
                ('CONTAR MIENTRAS CALLAS', 'Lo de verdad difícil',
                 'Con la izquierda parada tantos compases es fácil perder el sitio.'),
            ],
            pie='Es una canción para cantar, y se nota: la melodía respira cada pocos compases. '
                'Esos huecos son sitio para colocar la mano, no para pararse.',
        ),
        ritmos=[
            ('MANO DERECHA', 'medio compás callada y entra en el tres · literal',
             [sil('h'), n('D4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos notas que ocupan el compás entero · literal',
             [ac(('D3', 'A3'), 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 3/4 y "♩ = 178" escrito arriba.',
            'La derecha entra en el tercer tiempo del primer compás.',
            'La izquierda pasa compases enteros callada.',
            'Cuando la izquierda entra, toca dos notas juntas y las aguanta los tres tiempos.',
            'La derecha lleva toda la melodía, con la izquierda solo de vez en cuando.',
        ],
        reto='No perder la cuenta en los compases en los que la izquierda no toca.',
        truco='Cuenta en voz alta los tres tiempos de todos los compases, también los callados, y '
              'apoya la mano izquierda en sus teclas sin hundirlas.',
        sabias='Billy Joel la escribió sobre el bar de Los Ángeles donde tocaba en 1972 bajo un '
               'nombre falso, mientras esperaba salir de un contrato discográfico.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en cuántos compases pasan sin que la mano izquierda haga nada.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana se estudia la cuenta: las notas son fáciles, lo difícil es contar '
              'cuando no suena nada.',
        reglas=['CUENTA TAMBIÉN LOS COMPASES CALLADOS', 'LA IZQUIERDA, PUESTA EN LAS TECLAS',
                'PRIMERO LENTO, EL 178 VIENE SOLO'],
        bloques=[
            dict(num=1, titulo='Entrar en el tercer tiempo',
                 pista='andamio en Do mayor · otro dibujo, mismo silencio inicial',
                 sistemas=[
                     dict(cap='a) uno y dos en silencio, y tocas en el tres, bajando esta vez',
                          events=[sil('h'), n('B4'), n('A4'), n('G4'), n('F4')],
                          bars=2),
                     dict(cap='b) lo mismo desde otra nota',
                          events=[sil('h'), n('E4'), n('D4'), n('C4'), n('B3')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: compases enteros callada',
                 pista='andamio · dos notas juntas que duran los tres tiempos',
                 sistemas=[
                     dict(cap='a) un compás callado y uno tocando, con otro par de notas',
                          events=[sil('h.'), ac(('E3', 'B3'), 'h.')],
                          bars=2, clef='bass'),
                     dict(cap='b) dos compases callados y entras',
                          events=[sil('h.'), sil('h.'), ac(('A2', 'E3'), 'h.')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ QUIERE DECIR ♩ = 178',
                 texto='Que caben 178 negras en un minuto: unas tres por segundo. Como el compás '
                       'tiene tres tiempos, eso es un compás por segundo, más o menos el paso de '
                       'andar deprisa. No hace falta empezar ahí: empieza a la mitad.'),
            dict(num=3, titulo='Las dos juntas, en los compases donde coinciden',
                 pista='andamio · la izquierda cae en el uno y ya no se mueve · despacio',
                 sistemas=[
                     dict(cap='a) las dos en el uno, y luego la derecha sola dos tiempos',
                          events=[ac(('E3', 'B3', 'G4'), 'q'), n('F4'), n('E4'),
                                  ac(('A2', 'E3', 'C5'), 'q'), n('B4'), n('A4')],
                          bars=2),
                     dict(cap='b) un compás sin izquierda y otro con ella',
                          events=[n('D4'), n('E4'), n('F4'),
                                  ac(('G2', 'D3', 'G4'), 'q'), n('F4'), n('E4')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 54, 'C5', 'C3',
                          'la cuenta no se pierde aunque la izquierda calle',
                          desde=4, time_sig=(3, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
