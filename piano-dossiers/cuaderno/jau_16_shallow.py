# -*- coding: utf-8 -*-
"""Shallow (Lady Gaga y Bradley Cooper) — pieza 16 de Jaume. ADULTO exigente, sin cifrado.

   Lo comprobado sobre el PDF de su carpeta de Drive (Campamento Musical Bye Bye
   Beethoven, 3 páginas en formato carta, 55 compases), a 250-300 ppp:

     - Un sostenido detrás de la clave. La pieza empieza y acaba en Mi menor
       (el primer y el último acorde de la izquierda son Mi): tonalidad de un
       sostenido, relativa de Sol mayor.
     - 4/4, y arriba va el metrónomo: **negra = 96**.
     - No trae cifrado. Trae digitación impresa y ligaduras de unión.
     - MEDIDO, mano derecha:
       c. 1: silencio de negra, Mi4 · Mi4 · Mi4 (corcheas), Re4 (negra) y Si3
             (corchea, ligada al compás siguiente).
       c. 2: Si3 de blanca (ligada) y silencio de blanca.
       c. 3: silencio de negra y seis corcheas de Do4.
       cc. 17-20: Do5 ×4 (la cuarta ligada a una quinta) y Si4 de negra con
             puntillo · La4 La4 Si4 La4 (ligada) La4 y Sol4 de negra con
             puntillo · Si4 ×3, Re5 (ligada) Re5, Sol4 de negra y Sol4 de
             corchea ligada · Sol4 y La4 de SEMICORCHEA, Si4 de negra con
             puntillo y silencio de blanca.
     - Lleva semicorcheas (c. 20 y los compases que repiten ese final).

   Es el mismo archivo que el de José María, que lo trabajó con andamio. Aquí
   lo literal es lo medido (cc. 1-3 y 17-20) y el andamio es otro.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, plan, metronomo, verdadero_falso, inventa,
                       dibujar, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def lig(p, d='e'):
    return dict(pitch=p, dur=d, lig=True)


# MEDIDO: cc. 1-3
C1 = [sil('q'), n('E4', 'e'), n('E4', 'e'), n('E4', 'e'), n('D4'), lig('B3')]
C2 = [n('B3', 'h'), sil('h')]
C3 = [sil('q')] + [n('C4', 'e')] * 6
# MEDIDO: cc. 17-20
C17 = [n('C5', 'e'), n('C5', 'e'), n('C5', 'e'), lig('C5'), n('C5', 'e'), n('B4', 'q.')]
C18 = [n('A4', 'e'), n('A4', 'e'), n('B4', 'e'), lig('A4'), n('A4', 'e'), n('G4', 'q.')]
C19 = [n('B4', 'e'), n('B4', 'e'), n('B4', 'e'), lig('D5'), n('D5', 'e'), n('G4'), lig('G4')]
C20 = [n('G4', 's'), n('A4', 's'), n('B4', 'q.'), sil('h')]

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=16, nivel='intermedio', slug='Shallow',
    formato='adulto',
    titulo_corto='Shallow', time_sig=(4, 4), key_sig='Mi menor',
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source', 'SHALLOW.'),
    yt='https://www.youtube.com/results?search_query=shallow+lady+gaga+piano+tutorial',

    ficha=dict(
        titulo='Shallow',
        autor='Lady Gaga y Bradley Cooper · Campamento Musical Bye Bye Beethoven',
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 96'), ('Páginas', '3'),
               ('Empieza', 'Con silencio')],
        titulo_ritmos='La entrada, y los acordes de la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: el c. 1 entero. Abajo, andamio: la izquierda '
                   'toca dos notas a la vez, como en tu partitura, aquí sobre Mi menor.',
        armonia=dict(
            titulo='Mi menor, una entrada con silencio y un estribillo con semicorcheas',
            tarjetas=[
                ('LA TONALIDAD', 'Mi menor',
                 'Un sostenido en la armadura, como Sol mayor, pero la pieza empieza y acaba en Mi: '
                 'el primer y el último acorde de la izquierda son Mi. Todos los Fa, a la tecla '
                 'negra.'),
                ('LA ENTRADA', 'Tres corcheas',
                 'El c. 1 empieza con un silencio de negra y entra con tres corcheas de Mi. La '
                 'melodía repite la misma nota, y las ligaduras unen la última de cada frase '
                 'con el compás siguiente.'),
                ('EL ESTRIBILLO', 'Cc. 17-20',
                 'Es lo más escrito de la pieza: corcheas repetidas, ligaduras de unión y, en el '
                 'c. 20, dos semicorcheas seguidas de una negra con puntillo.'),
                ('LA IZQUIERDA', 'Dos notas a la vez',
                 'Casi siempre son dos notas a la vez en la clave de fa. Se estudian como un '
                 'bloque: la mano no cambia de forma, solo de tecla.'),
            ],
            pie='La digitación va impresa en el pentagrama, y las dos últimas páginas son una '
                'repetición variada de la primera: se estudian en ese orden.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido', C1, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · dos notas a la vez',
             [ac(('E2', 'B2'), 'h'), ac(('D3', 'F#3'), 'q.'), ac(('D3', 'G3'), 'e')],
             AZUL, 'bass', None),
        ],
        especial=[
            'Un sostenido detrás de la clave: todos los Fa suenan a la tecla negra.',
            'El compás es 4/4 y arriba viene impreso el metrónomo: negra = 96.',
            'Empieza con un silencio de negra: la primera nota entra en el segundo golpe.',
            'Lleva ligaduras de unión, semicorcheas (c. 20) y compases enteros de silencio.',
            'La izquierda toca casi siempre dos notas a la vez.',
            'La edición trae digitación impresa.',
        ],
        reto='Mantener un hilo de corcheas iguales sobre la misma nota (c. 3) sin que se acorten, y '
             'llegar a las dos semicorcheas del c. 20 sin acelerar las anteriores.',
        truco='Cuenta las corcheas del c. 3 en voz alta, uno-y-dos-y-tres-y, con el pie en el '
              'pulso. Si se aceleran, son pulsos de menos: baja el metrónomo y vuelve a subir.',
        sabias='Shallow es de la película Ha nacido una estrella, de 2018, y ganó el Óscar a la '
               'mejor canción original en la ceremonia de 2019.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo entra la melodía después del silencio, casi susurrada, y cómo '
                      'crece al llegar al estribillo. Esa dinámica es la que hay que reproducir.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Hay poca música distinta y mucha repetida, y por eso se estudia contra el aburrimiento: '
              'primero el principio, después el estribillo, y las dos semicorcheas aparte.',
        reglas=['LA ENTRADA DESPUÉS DEL SILENCIO', 'CORCHEAS IGUALES', 'LA LIGADURA ATA'],
        bloques=[
            dict(num=1, titulo='Los dos primeros compases',
                 pista='cc. 1-2 · medido sobre tu partitura · el silencio, tres corcheas de Mi y una '
                       'nota que se ata al compás siguiente',
                 sistemas=[
                     dict(cap='a) la entrada del c. 1 y la blanca ligada del c. 2 · el Si de la '
                              'corchea no se vuelve a tocar: dura hasta el final de la blanca',
                          events=C1 + C2, bars=2),
                 ]),
            dict(num=2, titulo='Seis corcheas iguales',
                 pista='c. 3 · medido sobre tu partitura · el Do central, con una línea adicional',
                 sistemas=[
                     dict(cap='a) un silencio de negra y seis corcheas sobre el mismo Do · la '
                              'dificultad es que ninguna se acorte',
                          events=C3, bars=1),
                     dict(cap='b) el mismo dibujo sobre otra altura, sin línea adicional · andamio '
                              'para ver si las corcheas siguen iguales cuando la nota ya no pesa',
                          events=[sil('q')] + [n('E4', 'e')] * 6, bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE ACORTAN LAS CORCHEAS IGUALES',
                 texto='Cuando una misma nota se repite seis veces, la mano deja de pensar en cada '
                       'una y empieza a tocar por inercia: se acelera sin que te des cuenta. La '
                       'cura es cantarlas mentalmente con el metrónomo y fijarse en el golpe de '
                       'en medio, no en el primero.'),
            dict(num=3, titulo='El estribillo, cc. 17-18',
                 pista='cc. 17-18 · medido sobre tu partitura · el Do se repite y se ata, el La '
                       'baja al Sol',
                 sistemas=[
                     dict(cap='a) cinco corcheas y una negra con puntillo, dos veces · la '
                              'ligadura de la cuarta a la quinta une dos corcheas en una sola',
                          events=C17 + C18, bars=2),
                 ]),
            dict(num=4, titulo='Cc. 19-20: la ligadura entre compases y las dos semicorcheas',
                 pista='cc. 19-20 · medido sobre tu partitura · el Sol del final del c. 19 se ata '
                       'a la semicorchea del c. 20',
                 sistemas=[
                     dict(cap='a) la ligadura cruza la barra: la semicorchea del c. 20 no se '
                              'vuelve a tocar, solo se aguanta · después, La y Si',
                          events=C19 + C20, bars=2),
                 ]),
            dict(num=5, titulo='La izquierda, dos notas a la vez',
                 pista='andamio sobre Mi menor · los intervalos de dos notas se estudian como un '
                       'bloque, sin mirar',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) tres intervalos para fijar la forma de la mano · quinta, sexta, '
                              'quinta y quinta, cada uno una nota más arriba',
                          events=[ac(('E2', 'B2'), 'h'), ac(('F#2', 'D3'), 'h'),
                                  ac(('G2', 'D3'), 'h'), ac(('A2', 'E3'), 'h')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=6, titulo='Dos manos: el estribillo sobre la izquierda sosteniendo',
                 pista='la derecha es la del c. 17, MEDIDA sobre tu partitura · los acordes de la '
                       'izquierda son andamio',
                 sistemas=[
                     dict(cap='a) el c. 17 con la derecha escrita y la izquierda sosteniendo · la '
                              'mano de abajo no se mueve hasta cambiar de acorde',
                          events=[ac(('C2', 'G2', 'E3', 'C5'), 'e'), ac(('C5',), 'e'),
                                  ac(('C5',), 'e'), ac(('C5',), 'e'), ac(('C5',), 'e'),
                                  ac(('B4',), 'q.')],
                          bars=1, manos='sostiene'),
                 ]),
            dict(num=7, titulo='Contar el silencio largo',
                 pista='andamio en Mi menor · el silencio de blanca de los cc. 2 y 20 se cuenta '
                       'entero, no se espera',
                 sistemas=[
                     dict(cap='a) dos compases con una blanca y un silencio de blanca · cuenta '
                              '1-2 en la nota y 3-4 en el silencio, en voz alta',
                          events=[n('G4', 'h'), sil('h'), n('E4', 'h'), sil('h')], bars=2),
                 ]),
            dict(num=8, titulo='Atar una corchea a la nota larga',
                 pista='andamio · la ligadura de unión suma las dos duraciones, no se toca dos veces',
                 sistemas=[
                     dict(cap='a) la corchea y la blanca ligadas valen dos tiempos y medio · se toca '
                              'una sola vez y se aguanta',
                          events=[sil('q'), n('D4', 'e'), n('E4', 'e'), n('E4', 'e'), n('D4'),
                                  lig('A3'), n('A3', 'h'), sil('h')],
                          bars=2),
                 ]),
        ] + bloques_extra('Mi menor', 16, 'E4', 'E2',
                          'el hilo de corcheas iguales y las dos semicorcheas del c. 20',
                          desde=9, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Shallow · para casa',
            intro='Veinte minutos al día, con el metrónomo puesto desde el principio. Es una pieza de '
                  'paciencia: lo difícil no es leerla, sino sostenerla.',
            bloques=[
                plan((5, 'La entrada del c. 1 y la blanca del c. 2, contando el silencio'),
                     (5, 'Los seis Do del c. 3 con el metrónomo, sin que se acorten'),
                     (6, 'El estribillo, cc. 17-20, con la derecha sola'),
                     (4, 'La izquierda sola, solo los intervalos de dos notas')),
                metronomo('Empieza a ♩ = 60 y sube de seis en seis hasta el 96 que trae tu partitura, '
                          'sin saltarte ningún escalón.',
                          'El tempo está impreso en tu partitura: negra = 96. No lo pases.',
                          titulo='A qué velocidad te sale'),
                verdadero_falso([
                    'La pieza empieza en el primer golpe del c. 1.',
                    'El c. 2 acaba con un silencio de blanca.',
                    'El c. 3 son seis corcheas sobre el mismo Do.',
                    'La armadura trae un bemol.',
                    'El tempo impreso es negra = 96.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                inventa(['Cuatro compases en 4/4.',
                         'Que empiece con un silencio de negra.',
                         'Que un compás sean seis corcheas sobre la misma nota.',
                         'Que acabe en una blanca y un silencio de blanca.'],
                        time_sig=(4, 4),
                        titulo='Inventa un principio de pieza',
                        pista='con el material de tu partitura de esta semana, pero tuyo'),
                dibujar(['Mi', 'Re', 'Si', 'Do', 'Si', 'La'],
                        titulo='Dibuja tú las primeras notas',
                        pista='son las de los cc. 1-4 de tu partitura · solo el óvalo'),
                para_clase('Los cc. 1-4 y 17-20 a 96, y cuántos Do del c. 3 se te acortan. Si las '
                           'dos semicorcheas te salen apretadas, tráelas: se arreglan con una '
                           'cuenta en voz alta.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
