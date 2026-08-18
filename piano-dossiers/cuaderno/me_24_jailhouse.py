# -*- coding: utf-8 -*-
"""Jailhouse Rock — pieza 24 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive (Elvis Presley, arr.
   Sadie King, 1 página; el mismo archivo que la pieza 8 de José María y la 9
   de Josep, byte a byte), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA, pero lleva Si bemol y Fa sostenido
       escritos delante de las notas: es blues, y el Si bemol le da ese
       color.
     - 4/4, con "♩ = 150  Swing" y "mf".
     - EMPIEZA CON SILENCIO: blanca, negra y corchea calladas antes de la
       primera nota. No arranca en el uno.
     - La izquierda hace redondas de dos notas los primeros compases.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from me_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=24, nivel='intermedio', slug='JailhouseRock',
    formato='adulto',
    titulo_corto='Jailhouse Rock', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'Jailhouse Elvis Presley.pdf'),
    yt='https://www.youtube.com/results?search_query=jailhouse+rock+elvis+easy+piano',

    ficha=dict(
        titulo='Jailhouse Rock',
        autor='Elvis Presley · arr. Sadie King',
        datos=[('Tonalidad', 'Do, con blues'), ('Compás', '4/4'),
               ('Tempo', '♩ = 150 · Swing'), ('Empieza', 'Con silencio'),
               ('Izquierda', 'Redondas dobles')],
        titulo_ritmos='Un silencio largo antes de la primera nota',
        pie_ritmos='Andamio con el color de blues de la pieza. Lo literal es la entrada: blanca, '
                   'negra y corchea calladas antes del primer sonido.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('COLOR DE BLUES', 'Notas fuera de escala',
                 'No hay armadura fija, pero estas dos notas aparecen escritas delante de la nota '
                 'una y otra vez: son las que le dan a la pieza su sonido característico.'),
                ('EMPIEZA CALLADA', 'Tres silencios',
                 'Blanca, negra y corchea en silencio antes de la primera nota. La pieza no arranca '
                 'en el golpe uno: hay que contar hasta el final del primer compás.'),
                ('♩ = 150 SWING', 'Rápido y desigual',
                 'Además de ser rápida, el swing hace que las corcheas no se toquen exactamente '
                 'iguales: la primera de cada pareja dura un poco más.'),
                ('LA IZQUIERDA SOSTIENE', 'Redonda doble',
                 'Los primeros compases, la izquierda toca dos notas a la vez y las sostiene el '
                 'compás entero, dejando toda la marcha rítmica a la derecha.'),
            ],
            pie='Es una de las canciones más famosas de Elvis, estrenada en la película del mismo '
                'nombre en 1957, con una coreografía que se hizo tan icónica como la canción.',
        ),
        ritmos=[
            ('MANO DERECHA', 'tres silencios y la primera nota · literal',
             [sil('h'), sil('q'), sil('e'), n('C4', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos notas, el compás entero · literal',
             [ac(('C3', 'G3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada, pero hay Si bemol y Fa sostenido escritos dentro.',
            'Compás de 4/4, con "♩ = 150 Swing" y "mf" escritos arriba.',
            'La pieza empieza con tres silencios seguidos: blanca, negra y corchea.',
            'La primera nota suena en la última corchea del primer compás.',
            'La izquierda hace redondas de dos notas los primeros compases.',
            'El swing hace que las corcheas no duren exactamente igual.',
        ],
        reto='Contar tres tiempos y tres cuartos en silencio sin perder el sitio, a una velocidad '
             'rápida donde hay poco margen para dudar.',
        truco='Cuenta en corcheas todo el primer compás ("un-y, dos-y, tres-y, cuatro-y") y toca '
              'solo en la última "y". Practícalo despacio primero, y sube la velocidad solo cuando '
              'entres siempre en el mismo sitio sin fallar.',
        sabias='La escena de baile de la película se rodó en un único día y se convirtió en una de '
               'las coreografías más imitadas del cine musical, aunque a Elvis al principio no le '
               'convencía la idea.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta el primer compás entero antes de que entre la voz. Ese hueco inicial '
                      'es justo lo que vas a tocar tú con la mano derecha en silencio.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El silencio inicial y el swing son lo nuevo de esta semana. Se estudian despacio '
              'antes de subir a la velocidad real.',
        reglas=['CUENTA EL SILENCIO EN CORCHEAS', 'LA IZQUIERDA SOSTIENE SIN MOVERSE',
                'EMPIEZA DESPACIO, EL 150 VIENE DESPUÉS'],
        bloques=[
            dict(num=1, titulo='Entrar tras el silencio inicial',
                 pista='andamio · el silencio del primer compás es el de tu partitura',
                 sistemas=[
                     dict(cap='a) tres silencios y entras en la última corchea',
                          events=[sil('h'), sil('q'), sil('e'), n('C4', 'e'),
                                  n('D4'), n('Eb4'), n('D4'), n('C4')],
                          bars=2),
                     dict(cap='b) lo mismo, con el color de blues',
                          events=[sil('h'), sil('q'), sil('e'), n('F#4', 'e'),
                                  n('G4'), n('Bb4'), n('G4'), n('F4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: redondas de dos notas',
                 pista='andamio · sostenidas el compás entero, sin melodía',
                 sistemas=[
                     dict(cap='a) el acorde se sostiene sin repetirse',
                          events=[ac(('C3', 'G3'), 'w'), ac(('F2', 'C3'), 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de acorde cada compás',
                          events=[ac(('G2', 'D3'), 'w'), ac(('C3', 'G3'), 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES EL COLOR DE BLUES',
                 texto='Notas como el Si bemol o el Fa sostenido, escritas fuera de la escala '
                       'esperada, no son errores ni adornos: son la marca del estilo blues, que se '
                       'coló en el rock and roll desde el principio. Tocarlas con seguridad, sin '
                       'dudar si "suenan raro", es parte de aprender el estilo, no solo la pieza.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda sostiene mientras la derecha entra tarde · despacio',
                 sistemas=[
                     dict(cap='a) el silencio es de las dos manos a la vez, y entran juntas',
                          events=[sil('h'), sil('q'), sil('e'), ac(('C3', 'G3', 'C4'), 'e'),
                                  n('D4'), n('Eb4'), n('D4'), n('C4')],
                          bars=2),
                     dict(cap='b) y con el color de blues encima',
                          events=[sil('h'), sil('q'), sil('e'), ac(('F2', 'C3', 'F#4'), 'e'),
                                  n('G4'), n('Bb4'), n('G4'), n('F4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
