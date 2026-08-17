# -*- coding: utf-8 -*-
"""Rasputin — pieza 14 de José María. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Boney M, descarga de
   Musescore, "Easy piano", 2 páginas):

     - SI MENOR: dos sostenidos detrás de la clave (los mismos que Re mayor,
       que ya viste en la pieza 11), y el cifrado empieza en Bm. Los Fa y los
       Do van a la tecla negra.
     - Compás de 4/4 y ♩ = 124 impreso.
     - La izquierda tiene SILENCIOS DE COMPÁS ENTERO al principio: la melodía
       entra sola y el acompañamiento llega después.
     - Las letras de los acordes vienen impresas encima (Bm, Em…).

   Lo que NO se cita nota a nota: el material va como ANDAMIO en Si menor y
   remite a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jm_comun import (n, ac, sil, corch, plan, verdadero_falso, inventa,
                      dibujar, metronomo)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SIM = 'Si menor'

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=14, nivel='iniciación',
    slug='Rasputin', formato='adulto',
    titulo_corto='Rasputin', time_sig=(4, 4), key_sig=SIM,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           'Rasputin.pdf'),
    yt='https://www.youtube.com/results?search_query=rasputin+boney+m+piano+easy',

    ficha=dict(
        titulo='Rasputin',
        autor='Boney M · arreglo "easy piano" de Musescore',
        datos=[('Tonalidad', 'Si menor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 124'), ('Mano izq.', 'Entra tarde'),
               ('Encima', 'El cifrado')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Si menor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Los Fa y los Do van a la tecla negra, como en la pieza 11.',
        armonia=dict(
            titulo='Los mismos dos sostenidos, pero en menor',
            tarjetas=[
                ('LA ARMADURA', 'Ya la conoces',
                 'Dos sostenidos, exactamente los mismos que Can\'t Help Falling in Love. La mano ya '
                 'sabe dónde van; lo que cambia es el color.'),
                ('MAYOR Y MENOR', 'Misma armadura',
                 'Re mayor y Si menor comparten armadura y suenan completamente distinto. Lo que '
                 'decide el carácter no es la armadura: es dónde descansa la música.'),
                ('LA IZQUIERDA', 'Llega tarde',
                 'Compases enteros de silencio al principio. La melodía arranca sola, y el '
                 'acompañamiento entra después.'),
                ('LA VELOCIDAD', '♩ = 124',
                 'Rápida, pero menos que Jailhouse Rock. Y ya sabes el método: lento y limpio, y '
                 'subir de cinco en cinco.'),
            ],
            pie='Es la primera vez en el cuaderno que dos piezas comparten armadura y suenan a mundos '
                'distintos. Merece la pena tocar cuatro compases de cada una seguidos alguna vez: la '
                'diferencia entre mayor y menor se entiende oyéndola, no leyéndola.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, que entra sola · andamio',
             [n('B3'), n('D4'), n('E4'), n('F#4')], OCRE, 'treble', SIM),
            ('MANO IZQUIERDA', 'los primeros compases, callada',
             [sil('w')], AZUL, 'bass', SIM),
        ],
        especial=[
            'Hay DOS sostenidos detrás de la clave: los Fa y los Do van a la tecla negra.',
            'La pieza está en Si menor, aunque la armadura sea la misma que la de Re mayor.',
            'Pone ♩ = 124.',
            'La mano izquierda tiene compases enteros de silencio al principio.',
            'Las letras de los acordes vienen impresas encima del pentagrama.',
            'Son dos páginas.',
        ],
        reto='Contar los compases en los que la izquierda no toca. Como la derecha está ocupada y '
             'sonando, es facilísimo perder la cuenta y entrar donde no toca.',
        truco='Cuenta los compases de silencio EN VOZ ALTA y con el número del compás, no del golpe: '
              '"uno-dos-tres-cuatro, DOS-dos-tres-cuatro, TRES-dos-tres-cuatro". Así sabes en todo '
              'momento cuántos llevas, y no solo por dónde vas dentro del compás.',
        sabias='La canción es de 1978 y cuenta, bailando, la historia del monje que asesoraba a la '
               'familia del zar. Boney M nunca la tocó en Rusia: se la prohibieron durante años, y '
               'cuando por fin fueron, tuvieron que dejarla fuera del concierto.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuántos compases pasan antes de que entre el bajo. Ese es tu ejercicio '
                      'de la semana.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La armadura ya la sabes de la pieza 11, así que aquí el trabajo es de cuenta: la '
              'izquierda entra tarde y hay que saber cuándo sin mirar el reloj. Y de velocidad, pero '
              'esa se deja para el final, como siempre.',
        reglas=['LOS COMPASES DE SILENCIO SE CUENTAN POR NÚMERO',
                'LOS FA Y LOS DO, EN TECLA NEGRA', 'LA VELOCIDAD, LA ÚLTIMA'],
        bloques=[
            dict(num=1, titulo='La melodía sola, que es la que arranca',
                 pista='andamio en Si menor · la izquierda todavía no ha entrado',
                 sistemas=[
                     dict(cap='a) despacio, comprobando los Fa y los Do',
                          events=[n('B3'), n('D4'), n('E4'), n('F#4'),
                                  n('E4'), n('D4'), n('B3'), n('C#4')],
                          bars=2, key_sig=SIM),
                     dict(cap='b) y con el ritmo que tiene, en corcheas · sin acelerar',
                          events=corch(['B3', 'D4']) + corch(['E4', 'F#4']) +
                                 corch(['E4', 'D4']) + corch(['B3', 'A3']),
                          bars=1, key_sig=SIM, show_time=False),
                 ]),
            dict(num=2, titulo='Contar los compases en los que no tocas', clef='bass',
                 pista='andamio · di el número del compás en voz alta, no solo el golpe',
                 sistemas=[
                     dict(cap='a) tres compases callado y entras en el cuarto · cuenta "UNO, DOS, '
                              'TRES" y toca',
                          events=[sil('w'), sil('w'), sil('w'),
                                  ac(('B2', 'F#3'), 'w')],
                          bars=4, clef='bass', key_sig=SIM),
                     dict(cap='b) y ahora la izquierda ya entrada · una vez por compás y aguanta',
                          events=[ac(('B2', 'F#3'), 'w'), ac(('E2', 'B2'), 'w'),
                                  ac(('G2', 'D3'), 'w'), ac(('F#2', 'C#3'), 'w')],
                          bars=4, clef='bass', key_sig=SIM, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='MAYOR Y MENOR CON LA MISMA ARMADURA',
                 texto='Re mayor y Si menor llevan los dos sostenidos exactamente iguales. Lo que las '
                       'diferencia es dónde descansa la música: una acaba en Re y suena luminosa, la '
                       'otra acaba en Si y suena oscura. No hace falta que te lo aprendas: toca cuatro '
                       'compases de la pieza 11 y cuatro de esta seguidos, y lo oirás sin que nadie '
                       'te lo explique.'),
            dict(num=3, titulo='Las dos manos, cuando ya han entrado las dos',
                 pista='andamio · muy despacio, y con metrónomo',
                 sistemas=[
                     dict(cap='a) la derecha con su melodía encima del acompañamiento',
                          events=[n('B3'), n('D4'), n('E4'), n('F#4'),
                                  n('E4'), n('C#4'), n('B3', 'h')],
                          bars=2, key_sig=SIM),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · una vez por compás, en el '
                              'primer golpe, y aguanta',
                          events=[ac(('B2', 'F#3'), 'w'), ac(('E2', 'B2'), 'w')],
                          bars=2, clef='bass', key_sig=SIM, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Rasputin · para casa',
            intro='Veinte minutos al día. La velocidad final es 124, pero esta semana no.',
            bloques=[
                plan((5, 'La melodía sola, comprobando los Fa y los Do'),
                     (5, 'Contar tres compases callado y entrar en el cuarto'),
                     (5, 'La izquierda ya entrada, una vez por compás'),
                     (5, 'Las dos manos, dos compases con metrónomo')),
                verdadero_falso([
                    'Si menor y Re mayor tienen la misma armadura.',
                    'Un compás de silencio se puede acortar si te aburres.',
                    'En esta pieza los Fa van a la tecla negra.',
                    'Las letras de encima del pentagrama son notas para tocar.',
                    'La pieza va a ♩ = 124.',
                ], titulo='Verdadero o falso', pista='marca la casilla'),
                inventa(['Solo Si, Re, Mi y Fa♯.',
                         'Dos compases de cuatro golpes.',
                         'Que el primer compás sea entero de silencio.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases en Si menor',
                        pista='con el silencio delante, como hace la izquierda de la pieza'),
                dibujar(['Si', 'Do♯', 'Re', 'Mi', 'Fa♯', 'Sol', 'La', 'Si'],
                        titulo='Dibuja la escala de Si menor',
                        pista='solo el óvalo · el Do♯ y el Fa♯ se dibujan igual que el Do y el Fa'),
                metronomo('Empieza donde te salga sin pararte, aunque sea a ♩ = 70.',
                          'La meta son 124. Sube de cinco en cinco y solo tras tres pasadas limpias.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
