# -*- coding: utf-8 -*-
"""Rasputin — pieza 11 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (Boney M, descarga de
   Musescore, "Easy piano", 2 páginas; el mismo archivo que piezas de José
   María, Luisa, Josep y Mercè, byte a byte):

     - Si menor: dos sostenidos detrás de la clave (los mismos que Re mayor,
       la tonalidad de la pieza 8), y el cifrado empieza en Bm.
     - Compás de 4/4 y ♩ = 124 impreso.
     - La izquierda tiene silencios de compás entero al principio: la
       melodía entra sola y el acompañamiento llega después.
     - Las letras de los acordes vienen impresas encima (Bm, Em…).
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
SIM = 'Si menor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=11, nivel='avanzado', slug='Rasputin',
    formato='adulto',
    titulo_corto='Rasputin', time_sig=(4, 4), key_sig=SIM,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source', 'Rasputin.pdf'),
    yt='https://www.youtube.com/results?search_query=rasputin+boney+m+piano+easy',

    ficha=dict(
        titulo='Rasputin',
        autor='Boney M · arreglo "easy piano" de Musescore',
        datos=[('Tonalidad', 'Si menor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 124'), ('Mano izq.', 'Entra tarde'),
               ('Encima', 'El cifrado')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Si menor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Los Fa y los Do van a la tecla negra, como en Can\'t Help Falling in Love.',
        armonia=dict(
            titulo='Los mismos dos sostenidos, pero en menor',
            tarjetas=[
                ('LA ARMADURA', 'Ya la conoces',
                 'Dos sostenidos, exactamente los mismos que Can\'t Help Falling in Love. La mano ya '
                 'sabe dónde van; lo que cambia es el color.'),
                ('MAYOR Y MENOR', 'Misma armadura',
                 'Re mayor y Si menor comparten armadura y suenan completamente distinto: lo que '
                 'decide el carácter es dónde descansa la música, no la armadura.'),
                ('LA IZQUIERDA', 'Llega tarde',
                 'Compases enteros de silencio al principio: la melodía arranca sola, y el '
                 'acompañamiento entra después.'),
                ('LA VELOCIDAD', '♩ = 124',
                 'Rápida, pero menos que Jailhouse Rock. Mismo método: lento y limpio, subiendo de '
                 'cinco en cinco.'),
            ],
            pie='Es de 1978 y cuenta, bailando, la historia del monje que asesoraba a la familia del '
                'zar. Boney M nunca la tocó en Rusia: se la prohibieron durante años.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, que entra sola · andamio',
             [n('B3'), n('D4'), n('E4'), n('F#4')], OCRE, 'treble', SIM),
            ('MANO IZQUIERDA', 'los primeros compases, callada',
             [sil('w')], AZUL, 'bass', SIM),
        ],
        especial=[
            'Hay dos sostenidos detrás de la clave: los Fa y los Do van a la tecla negra.',
            'La pieza está en Si menor, aunque la armadura sea la misma que la de Re mayor.',
            'Pone ♩ = 124.',
            'La mano izquierda tiene compases enteros de silencio al principio.',
            'Las letras de los acordes vienen impresas encima del pentagrama.',
            'Son dos páginas.',
        ],
        reto='Contar los compases en los que la izquierda no toca: como la derecha está ocupada y '
             'sonando, es fácil perder la cuenta y entrar donde no toca.',
        truco='Cuenta los compases de silencio en voz alta y con el número del compás, no del golpe: '
              '"uno-dos-tres-cuatro, DOS-dos-tres-cuatro, TRES-dos-tres-cuatro".',
        sabias='La versión que todo el mundo baila lleva un ritmo de discoteca deliberadamente pegado '
               'a una historia bastante oscura: la de un personaje real de la corte rusa.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuántos compases pasan antes de que entre el bajo. Ese es tu ejercicio '
                      'de la semana.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La armadura ya la sabes de Can\'t Help Falling in Love, así que aquí el trabajo es de '
              'cuenta: la izquierda entra tarde y hay que saber cuándo sin mirar el reloj.',
        reglas=['LOS COMPASES DE SILENCIO SE CUENTAN POR NÚMERO',
                'LOS FA Y LOS DO, EN TECLA NEGRA', 'LA VELOCIDAD, LA ÚLTIMA'],
        bloques=[
            dict(num=1, titulo='La melodía sola, que es la que arranca',
                 pista='andamio en Si menor · la izquierda todavía no ha entrado',
                 sistemas=[
                     dict(cap='a) empezando más arriba y bajando por la escala',
                          events=[n('F#4'), n('E4'), n('D4'), n('C#4'),
                                  n('B3'), n('C#4'), n('D4'), n('E4')],
                          bars=2, key_sig=SIM),
                     dict(cap='b) y con el ritmo que tiene, en corcheas · sin acelerar',
                          events=corch(['F#4', 'E4']) + corch(['D4', 'C#4']) +
                                 corch(['B3', 'D4']) + corch(['F#4', 'A4']),
                          bars=1, key_sig=SIM, show_time=False),
                 ]),
            dict(num=2, titulo='Contar los compases en los que no tocas', clef='bass',
                 pista='andamio · di el número del compás en voz alta, no solo el golpe',
                 sistemas=[
                     dict(cap='a) dos compases callado y entras en el tercero · cuenta "UNO, DOS" y '
                              'toca',
                          events=[sil('w'), sil('w'),
                                  ac(('E2', 'B2'), 'w'), ac(('F#2', 'C#3'), 'w')],
                          bars=4, clef='bass', key_sig=SIM),
                     dict(cap='b) y ahora la izquierda ya entrada, con otro orden de acordes',
                          events=[ac(('G2', 'D3'), 'w'), ac(('F#2', 'C#3'), 'w'),
                                  ac(('E2', 'B2'), 'w'), ac(('B2', 'F#3'), 'w')],
                          bars=4, clef='bass', key_sig=SIM, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='MAYOR Y MENOR CON LA MISMA ARMADURA',
                 texto='Re mayor y Si menor llevan los dos sostenidos exactamente iguales. Lo que las '
                       'diferencia es dónde descansa la música: una acaba en Re y suena luminosa, la '
                       'otra acaba en Si y suena oscura. Toca cuatro compases de Can\'t Help Falling '
                       'in Love y cuatro de esta seguidos, y lo oirás sin que nadie te lo explique.'),
            dict(num=3, titulo='Las dos manos, cuando ya han entrado las dos',
                 pista='andamio · muy despacio, y con metrónomo',
                 sistemas=[
                     dict(cap='a) la derecha con su melodía encima del acompañamiento',
                          events=[n('F#4'), n('E4'), n('D4'), n('C#4'),
                                  n('D4'), n('F#4'), n('B4', 'h')],
                          bars=2, key_sig=SIM),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · una vez por compás',
                          events=[ac(('G2', 'D3'), 'w'), ac(('F#2', 'C#3'), 'w')],
                          bars=2, clef='bass', key_sig=SIM, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
