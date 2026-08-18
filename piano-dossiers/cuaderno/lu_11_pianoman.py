# -*- coding: utf-8 -*-
"""Piano Man, de Billy Joel — pieza 11 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Piano Man (Easy) —
   Simplified version from SimplyPiano", arr. JuanM04, 2 páginas), leído a
   230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 3/4, y pone "♩ = 178".
     - La derecha empieza con medio compás callado y una negra: silencio de
       blanca y nota en el tercer tiempo.
     - **La izquierda casi no toca.** La mayoría de los compases son silencio
       de compás entero, y cuando entra hace UNA BLANCA CON PUNTILLO de dos
       notas a la vez, que ocupa el compás completo.
     - En la segunda página hay una anotación del arreglista: "10 real song
       compasses".

   Es la pieza rápida de reloj y lenta de manos: 178 es un número alto, pero
   con la izquierda casi parada el trabajo real es no acelerarse.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from lu_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=11, nivel='iniciación', slug='PianoMan',
    formato='adulto',
    titulo_corto='Piano Man', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source', 'piano-man-easy.'),
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
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('♩ = 178', 'Rápido de reloj',
                 'Parece mucho, y lo es de reloj. Pero en compás de tres eso son 59 compases por '
                 'minuto: un compás por segundo. Contado así ya no asusta.'),
                ('LA IZQUIERDA DESCANSA', 'Compases enteros',
                 'La mayoría de compases de la mano izquierda son silencio. Cuando entra, toca dos '
                 'notas a la vez y las aguanta los tres tiempos.'),
                ('ENTRA EN EL TERCERO', 'Medio compás',
                 'La derecha empieza con un silencio de blanca. Hay que contar uno y dos en '
                 'silencio y tocar en el tres.'),
                ('CONTAR MIENTRAS CALLAS', 'Lo de verdad difícil',
                 'Con la izquierda parada tantos compases es fácil perder el sitio. La cuenta no '
                 'se para nunca, aunque no suene nada.'),
            ],
            pie='Es una canción para cantar, y se nota: la melodía respira cada pocos compases. '
                'Esos huecos son sitio para colocar la mano, no para pararse.',
        ),
        ritmos=[
            ('MANO DERECHA', 'medio compás callada y entra en el tres · literal',
             [sil('h'), n('C4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos notas que ocupan el compás entero · literal',
             [ac(('C3', 'G3'), 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 3/4 y "♩ = 178" escrito arriba.',
            'La derecha entra en el tercer tiempo del primer compás.',
            'La izquierda pasa compases enteros callada.',
            'Cuando la izquierda entra, toca dos notas juntas y las aguanta los tres tiempos.',
            'En la segunda página el arreglista anota cuántos compases son de la canción de verdad.',
        ],
        reto='No perder la cuenta en los compases en los que la izquierda no toca. El silencio es '
             'largo y la mano se queda quieta, pero el compás sigue corriendo igual.',
        truco='Cuenta en voz alta los tres tiempos de TODOS los compases, también los callados, y '
              'apoya la mano izquierda en sus teclas sin hundirlas. Tenerla puesta en el sitio hace '
              'que la entrada llegue sola.',
        sabias='Billy Joel la escribió sobre el bar de Los Ángeles donde tocaba en 1972 bajo un '
               'nombre falso, mientras esperaba a poder salir de un contrato. Los personajes de la '
               'letra eran clientes de verdad.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en cuántos compases pasan sin que la mano izquierda haga nada. En la '
                      'grabación eso lo tapa la banda; en tu partitura, no.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana lo que se estudia es la cuenta. Las notas son fáciles; lo que cuesta es '
              'seguir contando cuando no suena nada.',
        reglas=['CUENTA TAMBIÉN LOS COMPASES CALLADOS', 'LA IZQUIERDA, PUESTA EN LAS TECLAS',
                'PRIMERO LENTO, EL 178 VIENE SOLO'],
        bloques=[
            dict(num=1, titulo='Entrar en el tercer tiempo',
                 pista='andamio en Do mayor · el primer compás es el de tu partitura',
                 sistemas=[
                     dict(cap='a) uno y dos en silencio, y tocas en el tres · cuenta en voz alta '
                              'desde antes de empezar',
                          events=[sil('h'), n('C4'), n('E4'), n('D4'), n('C4')],
                          bars=2),
                     dict(cap='b) lo mismo desde otra nota · lo que se practica es la espera',
                          events=[sil('h'), n('G4'), n('F4'), n('E4'), n('D4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: compases enteros callada',
                 pista='andamio · dos notas juntas que duran los tres tiempos',
                 sistemas=[
                     dict(cap='a) un compás callado y uno tocando · la mano se queda encima de las '
                              'teclas todo el rato',
                          events=[sil('h'), sil('q'), ac(('C3', 'G3'), 'h.')],
                          bars=2, clef='bass'),
                     dict(cap='b) dos callados seguidos y entras · aquí es donde se pierde la '
                              'cuenta, así que cuenta en voz alta',
                          events=[sil('h'), sil('q'), sil('h'), sil('q'), ac(('F2', 'C3'), 'h.')],
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
                          events=[ac(('C3', 'G3', 'E4'), 'q'), n('D4'), n('C4'),
                                  ac(('G2', 'D3', 'D4'), 'q'), n('C4'), n('B3')],
                          bars=2),
                     dict(cap='b) un compás sin izquierda y otro con ella · así es como está '
                              'escrita la pieza casi entera',
                          events=[n('E4'), n('F4'), n('G4'),
                                  ac(('F2', 'C3', 'A4'), 'q'), n('G4'), n('F4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
