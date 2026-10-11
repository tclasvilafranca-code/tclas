# -*- coding: utf-8 -*-
"""Merry-go-round of Life (Joe Hisaishi) — pieza 23 de Martina. ADULTO exigente, tono de niña.

   Lo comprobado sobre el PDF de su carpeta de Drive ("for Piano Solo", Musescore,
   2 páginas, 45 compases, VECTORIAL), medido a 220 ppp y mirado a 110, 220 y 300 ppp:

     - DOS BEMOLES detrás de la clave (Si♭ y Mi♭): Si♭ mayor. 3/4. Pone "♩ = 120" al
       empezar y "♩ = 152" en el c. 27: dos tempos escritos.
     - Los cuatro primeros compases la derecha hace TERCERAS EN CORCHEAS seguidas
       (acordes de dos notas) y la izquierda calla; esa mano está escrita en clave de sol
       hasta el c. 4 y pasa a clave de fa en el c. 5.
     - MEDIDO, derecha (alturas escritas):
       c. 1: Si♭4-Re5 · Do5-Mi♭5 (corcheas), tres veces
       c. 2: La4-Do5 · Si♭4-Re5 (corcheas), tres veces
       c. 3: Sol4-Si♭4 · La4-Do5 (corcheas), tres veces
       c. 4: Fa♯4-La4 · Mi♭4-Sol4 (dos SEMICORCHEAS) · Re4-Fa4 (corchea, ligada) ·
             Re4-Fa4 (blanca, ligada al c. 5)
       c. 5: Re4-Fa4 (blanca) · Re4-Fa♯4 (negra, con CALDERÓN)
       c. 6: Re4 · Sol4 · Si♭4 (negras)
       c. 7: Sol4-Si♭4-Re5 (blanca y negra)     c. 8: Do5 · Si♭4 · La4 (negras)
       c. 9: Si♭4 (blanca con puntillo, ligada)   c. 10: Si♭4 (negra con puntillo) · Sol4 ·
             Si♭4 · Re5 (corcheas)    c. 11: Sol5 (blanca) · Sol5     c. 12: Sol5 · Fa5 · Mi♭5
     - MEDIDO, izquierda: c. 5: Re3 · La3 (corcheas), Re4 (negra) y silencio de negra;
       c. 6: silencio de compás; c. 9: Sol3 (negra) · Si♭3 (blanca); c. 10: Sol3 · Re4;
       c. 11: Do3 · Si♭3; c. 12: Fa3 · Do4.
     - "rit." en el c. 5 y en el c. 22, "a tempo" en el c. 6, calderón también en el c. 26.
     - Más semicorcheas en los cc. 23 y 25. Barra de repetición al final.
     - Del c. 27 en adelante la izquierda hace bajo y acorde de vals.
   Mismo archivo que el de Josep y el de Nel: lo literal coincide, lo inventado no.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, reto, plan, metronomo, escribir, diferencias, acuerdate,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SIB = 'Sib mayor'


def terc(a, b, d='e'):
    return ac((a, b), d)


# MEDIDO: derecha, cc. 1-3 (seis corcheas de tercera por compás)
C1 = [terc('Bb4', 'D5'), terc('C5', 'Eb5')] * 3
C2 = [terc('A4', 'C5'), terc('Bb4', 'D5')] * 3
C3 = [terc('G4', 'Bb4'), terc('A4', 'C5')] * 3
# MEDIDO: c. 4 (dos semicorcheas, corchea y blanca, ligadas) y c. 5
C4 = [terc('F#4', 'A4', 's'), terc('Eb4', 'G4', 's'),
      dict(terc('D4', 'F4'), lig=True), dict(terc('D4', 'F4', 'h'), lig=True)]
C5 = [terc('D4', 'F4', 'h'), dict(terc('D4', 'F#4', 'q'), art='calderon')]
C6 = [n('D4'), n('G4'), n('Bb4')]
C7 = [ac(('G4', 'Bb4', 'D5'), 'h'), ac(('G4', 'Bb4', 'D5'), 'q')]
C8 = [n('C5'), n('Bb4'), n('A4')]
# MEDIDO: izquierda, c. 5 y cc. 9-12
L5 = [n('D3', 'e'), n('A3', 'e'), n('D4'), sil('q')]
L9 = [n('G3'), n('Bb3', 'h'), n('G3'), n('D4', 'h'), n('C3'), n('Bb3', 'h'),
      n('F3'), n('C4', 'h')]
# MEDIDO: derecha, cc. 9-12
R9 = [dict(n('Bb4', 'h.'), lig=True), n('Bb4', 'q.'), n('G4', 'e'), n('Bb4', 'e'),
      n('D5', 'e'), n('G5', 'h'), n('G5'), n('G5'), n('F5'), n('Eb5')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=23, nivel='avanzado', slug='MerryGoRoundOfLife',
    formato='adulto',
    titulo_corto='Merry-go-round of Life', time_sig=(3, 4), key_sig=SIB,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source',
                           'Merry-go-round-of-life'),
    yt='https://www.youtube.com/results?search_query=merry+go+round+of+life+piano',

    ficha=dict(
        titulo='Merry-go-round of Life',
        autor='Joe Hisaishi · de "El castillo ambulante" · para piano solo',
        datos=[('Tonalidad', 'Si bemol mayor'), ('Compás', '3/4'),
               ('Tempo', '♩ = 120 → 152'), ('Introducción', 'Terceras'),
               ('Páginas', 'Dos · 45 compases')],
        titulo_ritmos='Las terceras del c. 1 y la izquierda del c. 5',
        pie_ritmos='Arriba, medido sobre tu partitura: el c. 1, seis corcheas de dos notas. Abajo, '
                   'medido también: la izquierda del c. 5, que hasta ahí había callado.',
        armonia=dict(
            titulo='Dos velocidades y una introducción de dobles notas',
            tarjetas=[
                ('DOS TEMPOS', '120 y 152',
                 'Empieza a ♩ = 120 y en el c. 27 pasa a ♩ = 152. Son dos piezas en una: '
                 'cada velocidad se estudia por separado.'),
                ('LAS TERCERAS', 'Dos notas a la vez',
                 'Los cuatro primeros compases son corcheas de dos notas con la izquierda '
                 'callada. En el c. 4 aparecen dos semicorcheas seguidas, rápidas y '
                 'ligeras.'),
                ('FRENAR Y PARAR', 'rit. y calderón',
                 'En el c. 5 pone "rit." (frenar) y un calderón sobre el acorde: se aguanta '
                 'más de lo que dura. En el c. 6, "a tempo": se vuelve a la velocidad.'),
                ('EL VALS', 'Desde el c. 27',
                 'La izquierda pasa a bajo en el uno y acorde en el dos y el tres, a ♩ = 152. '
                 'La derecha calla tres compases y vuelve con la melodía.'),
            ],
            pie='La melodía que se oye en toda la pieza es la de los cc. 6-12, y la tocas casi '
                'entera con notas largas. Lo difícil es la entrada y el cambio de velocidad.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido', C1, OCRE, 'treble', SIB),
            ('MANO IZQUIERDA', 'c. 5 · medido', L5, AZUL, 'bass', SIB),
        ],
        especial=[
            'Dos bemoles detrás de la clave: Si bemol y Mi bemol.',
            'Compás de 3/4. Pone "♩ = 120" al empezar y "♩ = 152" en el compás 27.',
            'Los cuatro primeros compases son terceras en corcheas, con la izquierda callada.',
            'En el compás 5 pone "rit." y un calderón; en el 6, "a tempo".',
            'Hay semicorcheas en los compases 4, 23 y 25.',
            'Del compás 27 en adelante la izquierda hace bajo y acorde de vals.',
        ],
        reto='Las terceras de la introducción, seis corcheas por compás, sin que ninguna pareja '
             'de notas se separe y sin acelerar hacia el c. 4.',
        truco='Trabaja las terceras de dos en dos: toca la pareja, para, toca la siguiente. Une de '
              'cuatro en cuatro solo cuando las parejas sueltas salgan limpias.',
        sabias='El vals aparece una y otra vez en la película con orquestaciones muy distintas: es '
               'el mismo tema, y nunca suena igual dos veces.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en cómo frena la música en el c. 5 y en cómo arranca después, '
                      'primero despacio y luego mucho más deprisa a mitad de pieza.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza empieza por lo más difícil: las dobles notas. Los cuatro primeros '
              'compases son el trabajo de las primeras semanas, y la melodía, que viene después, '
              'es casi toda de notas largas.',
        reglas=['LAS TERCERAS, DE DOS EN DOS', 'DOS VELOCIDADES: 120 Y 152',
                'EL "rit." Y EL CALDERÓN VIENEN ESCRITOS'],
        bloques=[
            dict(num=1, titulo='Las terceras de los cc. 2 y 3',
                 pista='cc. 2-3 · medidos sobre tu partitura · el dibujo baja un escalón cada '
                       'compás',
                 sistemas=[
                     dict(cap='a) seis corcheas de dos notas por compás · en el c. 2 empiezan en '
                              'La-Do y en el c. 3 en Sol-Si bemol',
                          events=C2 + C3, bars=2, key_sig=SIB, time_sig=(3, 4)),
                     dict(cap='b) el mismo dibujo sobre otras notas · andamio · parejas de dos '
                              'notas seguidas, de una en una',
                          events=[terc('F4', 'A4'), terc('G4', 'Bb4'), terc('F4', 'A4'),
                                  terc('Eb4', 'G4'), terc('F4', 'A4'), terc('G4', 'Bb4')],
                          bars=1, key_sig=SIB, time_sig=(3, 4), show_time=False),
                 ]),
            dict(num=2, titulo='El c. 4: dos semicorcheas y la nota que se ata',
                 pista='cc. 4-5 · medidos sobre tu partitura · el calderón del c. 5 está sobre '
                       'el último acorde',
                 sistemas=[
                     dict(cap='a) dos semicorcheas, una corchea ligada a la blanca, y la blanca '
                              'ligada al c. 5 · al final, el acorde con calderón: se aguanta',
                          events=C4 + C5, bars=2, key_sig=SIB, time_sig=(3, 4)),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA CURVA ATA, EL CALDERÓN ALARGA',
                 texto='Las dos curvas del c. 4 unen acordes iguales: se tocan una sola vez y se '
                       'aguantan. El calderón es otra cosa: alarga el acorde más de lo que '
                       'dura, y cuánto lo decides tú. Cuenta los tres golpes del c. 5 y '
                       'aguanta un poco más.'),
            dict(num=3, titulo='La izquierda entra en el c. 5',
                 pista='cc. 5-6 · medidos sobre tu partitura · dos corcheas, una negra y un '
                       'silencio, y después un compás entero sin tocar',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) Re y La en corcheas, Re de negra y silencio de negra, y el '
                              'compás entero de silencio del c. 6',
                          events=L5 + [sil('h.')], bars=2, clef='bass', key_sig=SIB,
                          time_sig=(3, 4)),
                 ]),
            dict(num=4, titulo='La melodía llega, cc. 6-8',
                 pista='cc. 6-8 · medidos sobre tu partitura · primero tres negras, luego un '
                       'acorde y tres negras que bajan',
                 sistemas=[
                     dict(cap='a) Re, Sol y Si bemol · el acorde de Sol-Si bemol-Re, una blanca y '
                              'una negra · y Do, Si bemol y La que bajan',
                          events=C6 + C7 + C8, bars=3, key_sig=SIB, time_sig=(3, 4)),
                 ]),
            dict(num=5, titulo='La melodía larga, cc. 9-12',
                 pista='cc. 9-12 · medidos sobre tu partitura · una nota larga ligada y la '
                       'melodía subiendo',
                 sistemas=[
                     dict(cap='a) el Si bemol ligado, tres corcheas que suben y el Sol de arriba, '
                              'que baja Fa, Mi bemol',
                          events=R9, bars=4, key_sig=SIB, time_sig=(3, 4)),
                 ]),
            dict(num=6, titulo='La izquierda de la melodía, cc. 9-12',
                 pista='cc. 9-12 · medidos sobre tu partitura · una negra y una blanca por '
                       'compás: el bajo en el uno y la nota larga detrás',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) Sol y Si bemol, Sol y Re, Do y Si bemol, Fa y Do · la negra '
                              'es la nota grave y la blanca queda encima',
                          events=L9, bars=4, clef='bass', key_sig=SIB, time_sig=(3, 4)),
                 ]),
            dict(num=7, titulo='Las dos manos, la melodía sobre el bajo',
                 pista='andamio en Si bemol mayor · el bajo cae en el uno y la mano de arriba '
                       'se queda',
                 sistemas=[
                     dict(cap='a) un bajo por compás y una melodía de tres negras que sube · '
                              'la mano de abajo no se mueve hasta cambiar de compás',
                          events=[ac(('F2', 'F4'), 'q'), n('A4'), n('Bb4'),
                                  ac(('Eb2', 'G4'), 'q'), n('Bb4'), n('C5')],
                          bars=2, key_sig=SIB, time_sig=(3, 4), manos='sostiene'),
                 ]),
            dict(num=8, titulo='El vals de la izquierda, cc. 27-28',
                 pista='cc. 27-28 · medidos sobre tu partitura · ya a ♩ = 152 · bajo en el uno y '
                       'dos veces el acorde',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) Sol grave y dos veces Si bemol-Re, y después Re grave y lo mismo '
                              '· el bajo pesa y los dos acordes no',
                          events=[n('G3'), terc('Bb3', 'D4', 'q'), terc('Bb3', 'D4', 'q'),
                                  n('D3'), terc('Bb3', 'D4', 'q'), terc('Bb3', 'D4', 'q')],
                          bars=2, clef='bass', key_sig=SIB, time_sig=(3, 4)),
                     dict(cap='b) el mismo vals sobre otras notas · andamio · el bajo cambia, la '
                              'forma de la mano no',
                          events=[n('Eb3'), terc('G3', 'C4', 'q'), terc('G3', 'C4', 'q'),
                                  n('F3'), terc('A3', 'C4', 'q'), terc('A3', 'C4', 'q')],
                          bars=2, clef='bass', key_sig=SIB, time_sig=(3, 4), show_time=False),
                 ]),
            dict(num=9, titulo='La melodía vuelve, cc. 30-31',
                 pista='cc. 30-31 · medidos sobre tu partitura · las tres negras del c. 6, y una '
                       'blanca y una negra de Re',
                 sistemas=[
                     dict(cap='a) Re, Sol y Si bemol, y la blanca de Re con la negra de Re · es '
                              'la misma entrada que en el c. 6, ahora más deprisa',
                          events=C6 + [n('D5', 'h'), n('D5')], bars=2, key_sig=SIB,
                          time_sig=(3, 4)),
                 ]),
        ] + bloques_extra(SIB, 23, 'D5', 'G2',
                          'las dobles notas y el cambio de velocidad',
                          desde=10, time_sig=(3, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Merry-go-round of Life · para casa',
            intro='Quince minutos al día. Son los cuatro primeros compases y la melodía de los '
                  'cc. 6-8: lo demás vendrá después.',
            bloques=[
                reto('Tocar las seis terceras del c. 1 sin que ninguna pareja se separe, tres '
                     'veces seguidas.',
                     'Pon el metrónomo a ♩ = 60 y apunta cuántas veces seguidas te sale. Si una '
                     'vez las dos notas de una pareja no suenan a la vez, vuelves a cero.'),
                plan((5, 'Las terceras de los cc. 1-3, de dos en dos parejas'),
                     (4, 'El c. 4 con las semicorcheas, despacio'),
                     (4, 'La melodía de los cc. 6-8 con la derecha'),
                     (5, 'La izquierda de los cc. 5 y 9-12, y las dos manos juntas')),
                metronomo('Empieza a ♩ = 60 con las terceras del c. 1 y sube de cuatro en cuatro '
                          'hasta 120, que es el número con que empieza tu partitura.',
                          'El 152 del c. 27 se deja para más adelante: es una segunda pieza. Si a '
                          'una velocidad las parejas se separan, baja cuatro y repítelo.',
                          titulo='A qué velocidad te sale'),
                escribir(titulo='Copia el c. 6 de la derecha',
                         pista='tres negras: Re, Sol y Si bemol · escribe debajo cómo se llama '
                               'cada una',
                         lineas=1),
                diferencias(C6 + C8,
                            [n('D4'), n('G4'), n('Bb4'), n('C5'), n('A4'), n('A4')],
                            cuantas=1,
                            titulo='Busca la diferencia en la melodía',
                            pista='arriba, tus cc. 6 y 8 · abajo, los mismos con una nota '
                                  'cambiada'),
                acuerdate('Una pieza con dos velocidades escritas son dos ejercicios distintos. '
                          'Si estudias el principio a 152 te saldrá sucio, y si estudias el '
                          'vals a 120 te quedará lento: cada trozo con su número.',
                          etiqueta='CADA TROZO, SU VELOCIDAD'),
                para_clase('Los cc. 1-8 a la velocidad que te salga limpia, y qué pareja de '
                           'terceras te cuesta más. Si el calderón del c. 5 te saca del compás, '
                           'tráelo.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
