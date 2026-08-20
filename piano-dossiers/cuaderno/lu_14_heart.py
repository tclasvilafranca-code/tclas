# -*- coding: utf-8 -*-
"""Heart and Soul, de Hoagy Carmichael — pieza 14 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Heart and Soul — Easy
   Piano Version", 1 página, Musescore), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4, y arriba pone "♩ = 110" y **Swing**.
     - Primer compás de la derecha: negra, negra, blanca. Del segundo en
       adelante entra un silencio de corchea y corcheas seguidas.
     - La izquierda hace DOS BLANCAS por compás hasta el compás 8. Después de
       la barra de repetición cambia: **bajo y acorde**, negra y negra.

   ES EL MISMO ARCHIVO que la pieza 6 de Josep, byte a byte. Las citas
   literales pueden coincidir; el material inventado no. Lo comprueba
   `cruzar_luisa.py`, y por eso aquí el andamio está escrito desde otro ángulo:
   Josep trabaja el bajo-acorde y las corcheas; Luisa trabaja el swing y las
   dos blancas.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import sistemas_extra
from lu_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=14, nivel='iniciación', slug='HeartAndSoul',
    formato='adulto',
    titulo_corto='Heart and Soul', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source',
                           'heart-and-soul-hoagy-carmIchael easy.pdf'),
    yt='https://www.youtube.com/results?search_query=heart+and+soul+easy+piano',

    ficha=dict(
        titulo='Heart and Soul',
        autor='Hoagy Carmichael · 1938 · Easy Piano Version',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 110'), ('Estilo', 'Swing'),
               ('Izquierda', 'Dos blancas')],
        titulo_ritmos='Dos blancas debajo de la melodía',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la izquierda hace dos blancas '
                   'por compás y, pasada la repetición, cambia a bajo y acorde.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('SWING', 'Escrito arriba',
                 'Quiere decir que las parejas de corcheas no suenan iguales: la primera dura un '
                 'poco más que la segunda. Está escrito con notas iguales y se toca desigual.'),
                ('LA IZQUIERDA CAMBIA', 'A mitad de pieza',
                 'La primera mitad son dos blancas por compás. Después de la repetición pasa a una '
                 'nota grave y luego dos notas juntas: bajo y acorde.'),
                ('♩ = 110', 'Con número',
                 'Se puede comprobar con el metrónomo. En swing conviene ir por debajo al principio: '
                 'el balanceo se pierde antes que las notas.'),
                ('SE TOCA ENTRE DOS', 'A cuatro manos',
                 'Es la canción que dos personas tocan juntas en las películas. Con esta ya puedes '
                 'sentarte con alguien y tocar sin ensayar.'),
            ],
            pie='Es la primera pieza tuya con un estilo escrito, no solo un carácter. El swing no se '
                'lee: se imita. Escúchala antes de tocarla.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negra, negra y blanca · literal',
             [n('C4'), n('C4'), n('C4', 'h')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos blancas por compás · literal',
             [n('C3', 'h'), n('A2', 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4, con "♩ = 110" y "Swing" escritos arriba.',
            'La derecha empieza con negra, negra y blanca.',
            'A partir del segundo compás hay un silencio de corchea y corcheas seguidas.',
            'La izquierda hace dos blancas por compás en la primera mitad.',
            'Después de la repetición, la izquierda hace bajo y acorde.',
        ],
        reto='El swing. Las corcheas están escritas iguales y no se tocan iguales: la primera de '
             'cada pareja dura más. Leído no se ve; escuchado, se pega enseguida.',
        truco='Di "trom-pe-ta, trom-pe-ta" con la grabación puesta. Esa palabra tiene exactamente '
              'el balanceo del swing. Cuando la digas al mismo tiempo que la música, tócalo diciendo '
              'la palabra por dentro.',
        sabias='Carmichael la escribió en 1938 y se convirtió en la pieza que dos personas tocan '
               'juntas sentadas al mismo piano. En la película "Big", Tom Hanks la baila sobre un '
               'teclado gigante.',
        qr=dict(titulo='Escúchala',
                texto='No mires las notas: escucha solo las parejas de corcheas. Vas a oír que la '
                      'primera es más larga. Eso es todo el swing.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El swing se aprende con el oído y las manos se aprenden por separado. Los dos '
              'primeros pasos son de manos; el balanceo va encima al final.',
        reglas=['ESCÚCHALA ANTES DE TOCARLA', 'LA IZQUIERDA, DOS BLANCAS Y NADA MÁS',
                'DESPACIO, QUE EL BALANCEO SE PIERDE ANTES'],
        bloques=[
            dict(num=1, titulo='La izquierda: dos blancas por compás',
                 pista='andamio en Do mayor · el reparto de figuras es el de tu partitura',
                 sistemas=[
                     dict(cap='a) una en el uno y otra en el tres · el acorde va cambiando cada '
                              'compás y la mano casi no se mueve',
                          events=[n('C3', 'h'), n('A2', 'h'), n('F2', 'h'), n('G2', 'h')],
                          acento=True,
                          bars=2, clef='bass'),
                     dict(cap='b) y la vuelta · cuatro compases seguidos así y ya te sabes toda la '
                              'primera mitad',
                          events=[n('C3', 'h'), n('A2', 'h'), n('D3', 'h'), n('G2', 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha, con el silencio de media parte',
                 pista='andamio · la melodía entra justo después del golpe, no en el golpe',
                 sistemas=[
                     dict(cap='a) el primer compás es literal: negra, negra y blanca',
                          events=[n('C4'), n('C4'), n('C4', 'h'), n('D4'), n('E4'), n('D4', 'h')],
                          bars=2),
                     dict(cap='b) y con el silencio de corchea y las corcheas seguidas · aquí es '
                              'donde vive el swing',
                          events=[sil('e')] + corch(['C4', 'D4']) + corch(['E4', 'D4'])
                                 + [n('C4', 'e'), n('C4'), n('D4', 'h'), n('E4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE TOCA EL SWING',
                 texto='Las corcheas están escritas iguales, pero no se tocan iguales: la primera de '
                       'cada pareja dura casi el doble que la segunda. No hay manera de escribirlo '
                       'con exactitud, y por eso se pone la palabra arriba y se deja al oído. '
                       'Escucha la grabación dos veces antes de tocar y no intentes contarlo: se '
                       'aprende imitando, como un acento.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda cae en el uno y en el tres · muy despacio',
                 sistemas=[
                     dict(cap='a) la melodía encima de las dos blancas · fíjate en que solo '
                              'coinciden en el uno y en el tres',
                          events=[ac(('C3', 'C4')), n('C4'), ac(('A2', 'C4'), 'h'),
                                  ac(('F2', 'D4')), n('E4'), ac(('G2', 'D4'), 'h')],
                          bars=2),
                     dict(cap='b) y el cambio de la segunda mitad: bajo y acorde, negra y negra',
                          events=[n('C3'), ac(('E3', 'G3')), n('A2'), ac(('C3', 'E3')),
                                  n('F2'), ac(('A2', 'C3')), n('G2'), ac(('B2', 'D3'))],
                          bars=2, clef='bass', show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('Do mayor', 'C4', 'G2', time_sig=(4, 4), variante=21,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
