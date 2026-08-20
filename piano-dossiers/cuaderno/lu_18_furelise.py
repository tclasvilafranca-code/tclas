# -*- coding: utf-8 -*-
"""Für Elise, de Beethoven (*Easy Ver.*) — pieza 18 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Fur Elise — Easy Ver.",
   1 página), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: La menor. Los sostenidos y el becuadro
       van escritos delante de la nota.
     - 3/4, "mp".
     - El primer compás es medio silencio y dos corcheas; el segundo son SEIS
       CORCHEAS SEGUIDAS.
     - Después aparece un compás con negra, silencio de corchea y corcheas.
     - La izquierda está callada dos compases y luego hace una blanca y un
       silencio de negra.

   Es la pieza con más corcheas seguidas de todo el cuaderno de Luisa, y por
   eso va la penúltima: lo que se trabaja es que las corcheas suenen iguales.
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
    alumno='Luisa', carpeta='Luisa', num=18, nivel='iniciación', slug='FurElise',
    formato='adulto',
    titulo_corto='Für Elise', time_sig=(3, 4), key_sig='La menor',
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source', 'Para  Elisa easy.pdf'),
    yt='https://www.youtube.com/results?search_query=fur+elise+easy+piano+beginner',

    ficha=dict(
        titulo='Für Elise',
        autor='Ludwig van Beethoven · hacia 1810 · versión fácil',
        datos=[('Tonalidad', 'La menor'), ('Compás', '3/4'),
               ('Carácter', 'mp · suave'), ('Derecha', 'Corcheas'),
               ('Izquierda', 'Entra tarde')],
        titulo_ritmos='Corcheas seguidas, todas iguales',
        pie_ritmos='Andamio en La menor. Lo literal es el arranque: medio compás callado, dos '
                   'corcheas, y el compás siguiente entero de corcheas.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('SEIS CORCHEAS', 'Un compás entero',
                 'Es lo que más dedos pide de todo tu cuaderno. No son rápidas de reloj: son muchas '
                 'seguidas, y lo difícil es que todas duren lo mismo.'),
                ('DOS DEDOS QUE SE TURNAN', 'Arriba y abajo',
                 'La melodía del principio va y viene entre dos teclas vecinas, una blanca y una '
                 'negra. Se hace con dos dedos que se alternan, sin mover la mano.'),
                ('TECLAS NEGRAS ESCRITAS', 'Y un becuadro',
                 'No hay armadura, pero sí sostenidos delante de la nota. Y hay un becuadro, que es '
                 'la señal de quitar el sostenido y volver a la tecla blanca.'),
                ('LA IZQUIERDA LLEGA', 'Dos compases',
                 'Empieza callada y entra con una blanca. Cuando entra, la derecha ya lleva doce '
                 'corcheas y no puede alterarse.'),
            ],
            pie='Es la pieza de piano más conocida del mundo y Beethoven no la publicó nunca. Se '
                'encontró cuarenta años después de su muerte.',
        ),
        ritmos=[
            ('MANO DERECHA', 'medio compás callado y dos corcheas · literal',
             [sil('h')] + corch(['E5', 'D#5']), OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una blanca y un silencio · literal',
             [n('A2', 'h'), sil('q')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada; los sostenidos van escritos dentro.',
            'La tonalidad es La menor.',
            'Compás de 3/4 y "mp": suave.',
            'El primer compás está callado medio compás y luego hay dos corcheas.',
            'El segundo compás son seis corcheas seguidas.',
            'La izquierda entra en el tercer compás con una blanca y un silencio.',
        ],
        reto='Que las seis corcheas duren lo mismo. Lo normal es que las dos primeras salgan bien y '
             'las últimas se aceleren, y entonces la melodía suena atropellada.',
        truco='Toca las seis corcheas contando "un-y, dos-y, tres-y" en voz alta, muy despacio, y '
              'para al final de cada compás. Cuando las seis suenen iguales tres veces seguidas, '
              'quita la parada. La velocidad viene sola; la igualdad, no.',
        sabias='Beethoven la escribió hacia 1810 y no se publicó hasta 1867. Nadie sabe quién era '
               'Elise: hay quien piensa que el copista leyó mal y ponía "Therese", una alumna suya a '
               'la que pidió en matrimonio.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo el principio, las dos primeras notas que van y vienen. Fíjate en '
                      'que suenan igual de largas las dos. Ese es todo el trabajo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Muchas corcheas seguidas. Se estudia por trozos cortos y contando, que es la única '
              'manera de que no se aceleren.',
        reglas=['TODAS LAS CORCHEAS, IGUAL DE LARGAS', 'DOS DEDOS QUE SE TURNAN, LA MANO QUIETA',
                'DESPACIO Y POR TROZOS CORTOS'],
        bloques=[
            dict(num=1, titulo='Dos teclas vecinas, dos dedos que se turnan',
                 pista='andamio en La menor · el sostenido va escrito delante de la nota',
                 sistemas=[
                     dict(cap='a) ida y vuelta entre dos teclas · la mano no se mueve, solo los dedos',
                          events=corch(['E5', 'D#5']) + corch(['E5', 'D#5']) + corch(['E5', 'D#5']),
                          matiz='mp',
                          bars=1),
                     dict(cap='b) y con el becuadro, que quita el sostenido · la misma nota, tecla '
                              'blanca',
                          events=corch(['E5', 'Dn5']) + corch(['E5', 'Dn5']) + corch(['E5', 'Dn5']),
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='Un compás entero de corcheas',
                 pista='andamio · cuenta "un-y, dos-y, tres-y" y para al acabar el compás',
                 sistemas=[
                     dict(cap='a) seis corcheas seguidas · si las últimas corren, es que has dejado '
                              'de contar',
                          events=corch(['E5', 'B4']) + corch(['D5', 'C5']) + corch(['A4', 'C4']),
                          bars=1),
                     dict(cap='b) y el compás que empieza con silencio de corchea · la mano espera '
                              'media parte',
                          events=[n('A4'), sil('e')] + corch(['C4', 'E4']) + [n('A4', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE ESTUDIAN LAS CORCHEAS SEGUIDAS',
                 texto='Nunca de corrido. Se toca un compás, se para, se comprueba que las seis han '
                       'durado lo mismo y se vuelve a empezar. Parar es parte del ejercicio: si '
                       'tocas seguido, aceleras sin darte cuenta y lo que aprendes es a acelerar. '
                       'Cuando un compás salga igualado tres veces, únelo con el siguiente.'),
            dict(num=3, titulo='Las dos juntas, cuando entra la izquierda',
                 pista='andamio · la izquierda llega en el tercer compás · muy despacio',
                 sistemas=[
                     dict(cap='a) la izquierda calla y entra con una blanca y un silencio',
                          events=[sil('h'), sil('q'), n('A2', 'h'), sil('q')],
                          bars=2, clef='bass'),
                     dict(cap='b) y con las corcheas encima · la izquierda toca una vez y la derecha '
                              'seis',
                          events=[ac(('A2', 'C5'), 'e'), n('B4', 'e')] + corch(['C5', 'E5'])
                                 + corch(['A4', 'B4']),
                          bars=1, show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('La menor', 'A3', 'A2', time_sig=(3, 4), variante=12,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
