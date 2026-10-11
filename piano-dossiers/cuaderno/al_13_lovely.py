# -*- coding: utf-8 -*-
"""Lovely (Billie Eilish y Khalid) — pieza 13 de Alan. ADULTO exigente, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Amy Kieran,
   2 páginas, imagen a 54 ppp), mirado a 200 ppp:

     - UN SOSTENIDO detrás de la clave (Fa♯): la pieza arranca en Mi, Sol, Si, es decir,
       MI MENOR. 4/4. Trae ♩ = 115. No trae intensidad.
     - 44 compases: 25 en la primera página y 19 en la segunda. Barra de repetición
       al principio del c. 11 y al final del c. 44. La letra va impresa.
     - MEDIDO, mano derecha (a 200 ppp, contra las líneas del pentagrama):
       cc. 1-3: ocho corcheas por compás que alternan Mi4 y Sol4
       c. 4: Mi4 · Sol4 · Mi4 · Sol4 · Si4 · Sol4 · Mi4 · Sol4 (ocho corcheas)
     - MEDIDO, mano izquierda: cc. 1 y 2, silencio de compás entero; c. 3, un
       acorde de tres notas en redonda ligado a un acorde de blanca en el c. 4;
       c. 4, dos acordes de blanca; c. 5, acorde de redonda.
     - c. 11 y c. 12 (la melodía con letra): cuatro corcheas y una blanca ligada
       a la redonda del compás siguiente.
     - c. 35: negra ligada a corchea · dos semicorcheas pegadas · negra · negra
       ligada. c. 36: negra, silencio de corchea, dos semicorcheas y blanca.
       El mismo pasaje vuelve en los cc. 39-40.
   Las notas de la melodía no se miden con seguridad en este escaneo: todo lo que
   lleva notas más allá del c. 4 va como ANDAMIO y solo se cita el ritmo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, plan, metronomo, verdadero_falso, inventa, dibujar,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
MI = 'Mi menor'

# MEDIDO: cc. 1 y 4 (derecha)
C1 = [n('E4', 'e'), n('G4', 'e')] * 4
C4 = [n('E4', 'e'), n('G4', 'e'), n('E4', 'e'), n('G4', 'e'),
      n('B4', 'e'), n('G4', 'e'), n('E4', 'e'), n('G4', 'e')]
ACORDE = ('E3', 'G3', 'B3')

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=13, nivel='intermedio', slug='Lovely',
    formato='adulto',
    titulo_corto='Lovely', time_sig=(4, 4), key_sig=MI,
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source', 'LOVELY.'),
    yt='https://www.youtube.com/results?search_query=lovely+billie+eilish+khalid+piano',

    ficha=dict(
        titulo='Lovely',
        autor='Billie Eilish con Khalid · arreglo de Amy Kieran',
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 115'), ('Letra', 'Impresa'),
               ('Páginas', 'Dos')],
        titulo_ritmos='El c. 1, medido, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: ocho corcheas que alternan Mi y Sol. Abajo, '
                   'andamio: la izquierda calla dos compases y entra con un acorde largo.',
        armonia=dict(
            titulo='Un arpegio que no se detiene, y una melodía que entra tarde',
            tarjetas=[
                ('EL ARPEGIO', 'Mi, Sol, Mi, Sol',
                 'Los diez primeros compases de la derecha son ocho corcheas por compás que '
                 'alternan Mi4 y Sol4. En el c. 4 aparece un Si4 y vuelve el dibujo. No cambia: '
                 'lo difícil es no acelerarlo.'),
                ('LA IZQUIERDA', 'Calla y entra',
                 'Los dos primeros compases son silencio de compás entero. En el c. 3 entra un '
                 'acorde de tres notas en redonda, ligado al acorde del c. 4.'),
                ('LA MELODÍA', 'Con letra',
                 'En el c. 11 empieza la parte cantada, con la letra impresa debajo de las '
                 'notas, entre una barra de repetición al principio y otra al final.'),
                ('LAS SEMICORCHEAS', 'cc. 35-36',
                 'Dos semicorcheas pegadas caben donde cabría una corchea: salen en el c. 35 y el '
                 '36, y vuelven en los cc. 39-40. Sin prisa: pesan menos de lo que parecen.'),
            ],
            pie='Son 44 compases en dos páginas, con un sostenido y el número de metrónomo '
                'escrito. Lo difícil no son las notas: es mantener la derecha pareja mientras la '
                'izquierda cambia de acorde.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido', C1, OCRE, 'treble', MI),
            ('MANO IZQUIERDA', 'andamio · dos compases de silencio y un acorde',
             [sil('w'), sil('w'), ac(ACORDE, 'w')], AZUL, 'bass', MI),
        ],
        especial=[
            'Un sostenido detrás de la clave: Fa♯. La pieza está en Mi menor.',
            'El compás es 4/4 y trae ♩ = 115.',
            'Los cc. 1-3 de la derecha son ocho corcheas que alternan Mi y Sol.',
            'La izquierda no toca hasta el c. 3.',
            'Hay barra de repetición en el c. 11 y al final.',
            'En los cc. 35, 36, 39 y 40 aparecen semicorcheas.',
        ],
        reto='Mantener las ocho corcheas iguales durante diez compases, sin acelerar cuando entra '
             'el Si4 del c. 4 ni cuando entran los acordes de la izquierda.',
        truco='Cuenta "uno-y-dos-y-tres-y-cuatro-y" en voz alta. Si la "y" te sale más rápida a '
              'partir del c. 4, es que la mano se emociona con el salto: vuelve al principio.',
        sabias='Lovely es de Billie Eilish y Khalid, de 2018, para la serie 13 Reasons Why. Billie '
               'Eilish tenía dieciséis años cuando salió: muchos pianistas empiezan por el '
               'arpegio del principio, que es el que reconoce todo el mundo.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo el piano no se detiene en ningún momento y las voces entran '
                      'por encima. Eso es lo que hace tu derecha: tiene que sonar como un reloj.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El arpegio se estudia con la derecha sola y el metrónomo, sin mirar, hasta que '
              'salga solo. Después se añade la izquierda y, al final, la melodía.',
        reglas=['EL ARPEGIO NO SE ACELERA', 'LA IZQUIERDA ENTRA EN EL C. 3',
                'LAS SEMICORCHEAS SE CUENTAN'],
        bloques=[
            dict(num=1, titulo='El Si4 del c. 4',
                 pista='c. 4 · medido sobre tu partitura · ocho corcheas, con un Si4 en medio',
                 sistemas=[
                     dict(cap='a) Mi, Sol, Mi, Sol, Si, Sol, Mi, Sol · el Si es la única nota '
                              'nueva de los diez primeros compases',
                          events=C4, bars=1, key_sig=MI),
                     dict(cap='b) el mismo dibujo una nota más grave · andamio · cambia el sitio, '
                              'no la forma de la mano',
                          events=[n('A3', 'e'), n('C4', 'e'), n('A3', 'e'), n('C4', 'e'),
                                  n('E4', 'e'), n('C4', 'e'), n('A3', 'e'), n('C4', 'e')],
                          bars=1, key_sig=MI, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda entra con un acorde ligado',
                 pista='cc. 3-5 · el ritmo es el de tu partitura · los acordes son andamio en '
                       'Mi menor',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) una redonda ligada a una blanca, otra blanca y una redonda · '
                              'la ligadura no se vuelve a tocar',
                          events=[dict(ac(ACORDE, 'w'), lig=True), ac(ACORDE, 'h'),
                                  ac(('E3', 'A3', 'C4'), 'h'), ac(ACORDE, 'w')],
                          bars=3, clef='bass', key_sig=MI),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL ARPEGIO SE ESTUDIA SIN LA IZQUIERDA',
                 texto='El arpegio son ocho notas iguales por compás: si lo estudias con la '
                       'izquierda desde el primer día, la mano que cambia de acorde te hace '
                       'acelerar la que no cambia. Primero la derecha sola con metrónomo, hasta '
                       'que no te ocupe la cabeza; luego la izquierda.'),
            dict(num=3, titulo='Las dos manos, con el acorde debajo',
                 pista='andamio en Mi menor · la derecha repite el dibujo de los cc. 1-4 y el '
                       'acorde de la izquierda se sostiene',
                 sistemas=[
                     dict(cap='a) la derecha alterna dos notas mientras el acorde largo de la '
                              'izquierda se queda sonando · acorde distinto, mismo dibujo',
                          events=[ac(('B2', 'D3', 'F#3', 'B3'), 'e'), n('D4', 'e'),
                                  n('F#4', 'e'), n('D4', 'e'), n('B3', 'e'), n('D4', 'e'),
                                  n('F#4', 'e'), n('D4', 'e')],
                          bars=1, key_sig=MI, manos='sostiene'),
                 ]),
            dict(num=4, titulo='El ritmo de la melodía, cc. 11-12',
                 pista='cc. 11-12 · el ritmo es el de tu partitura · las notas son andamio',
                 sistemas=[
                     dict(cap='a) cuatro corcheas y una blanca ligada a la redonda del compás '
                              'siguiente · las corcheas se dicen a la vez que se tocan',
                          events=[n('A4', 'e'), n('B4', 'e'), n('B4', 'e'), n('A4', 'e'),
                                  dict(n('A4', 'h'), lig=True), n('A4', 'w')],
                          bars=2, key_sig=MI),
                 ]),
            dict(num=5, titulo='Las dos semicorcheas, cc. 35-36',
                 pista='cc. 35-36 · el ritmo es el de tu partitura · las notas son andamio',
                 sistemas=[
                     dict(cap='a) una negra ligada a una corchea, dos semicorcheas pegadas, y dos '
                              'negras · las dos cortas caben donde cabría una corchea',
                          events=[dict(n('A4'), lig=True), n('A4', 'e'), n('G4', 's'),
                                  n('F#4', 's'), n('E4'), n('D4')],
                          bars=1, key_sig=MI),
                     dict(cap='b) el c. 36: una negra, un silencio de corchea, otras dos '
                              'semicorcheas y una blanca',
                          events=[n('E4'), sil('e'), n('A4', 's'), n('G4', 's'),
                                  n('F#4', 'h')],
                          bars=1, key_sig=MI, show_time=False),
                 ]),
        ] + bloques_extra(MI, 13, 'E4', 'E2',
                          'la derecha pareja mientras la izquierda cambia de acorde',
                          desde=6, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Lovely · para casa',
            intro='Veinte minutos al día. Hay una sola cosa que cuidar durante toda la pieza: que '
                  'la derecha suene igual al principio que al final.',
            bloques=[
                plan((6, 'El arpegio de la derecha, cc. 1-4, con metrónomo y sin mirar'),
                     (4, 'Los acordes de la izquierda, cc. 3-5'),
                     (5, 'Las dos manos, cc. 1-5, sin parar'),
                     (5, 'La melodía de los cc. 11-12 cantada por encima')),
                metronomo('Empieza a ♩ = 70 con el arpegio de la derecha y sube de diez en diez '
                          'hasta 110, sin mirar las manos.',
                          'La meta son 115, que es lo que pone tu partitura. Si a una velocidad '
                          'te sale desigual, no subas: baja diez y repítelo.',
                          titulo='A qué velocidad te sale'),
                verdadero_falso([
                    'Detrás de la clave hay un sostenido.',
                    'La partitura trae ♩ = 115.',
                    'Los cc. 1-4 de la derecha son ocho corcheas por compás.',
                    'La izquierda toca desde el c. 1.',
                    'La partitura no trae letra.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                inventa(['Dos compases en 4/4.',
                         'Con ocho corcheas por compás.',
                         'Que alternen dos notas como Mi y Sol.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases como los del principio',
                        pista='con la forma de los cc. 1-4 de tu partitura, pero tuyo'),
                dibujar(['Mi', 'Sol', 'Si', 'La', 'Re'],
                        titulo='Dibuja tú las notas',
                        pista='son notas del arpegio y de la melodía · solo el óvalo, en clave de sol'),
                para_clase('Los cc. 1-5 con las dos manos y a qué velocidad llegas con el '
                           'metrónomo. Si te sale limpio a 90, esta semana pasamos a la melodía '
                           'de los cc. 11-12.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
