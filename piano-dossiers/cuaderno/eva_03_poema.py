# -*- coding: utf-8 -*-
"""Poema de Amor (canción 3 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico); la medición se importa de
   `dilan_06_poema`. Ver TRANSCRIPCION_D06_08.md.

   Camino distinto al de Dilan, a propósito:

     - A Dilan se le da el MOLDE ENTERO (fundamental, octava, quinta, octava) y
       se le enseña a moverlo por la página.
     - A Eva se le CONSTRUYE el molde desde dentro: primero las dos notas que
       de verdad definen el acorde —fundamental y quinta—, después la octava
       encima, y solo entonces el gesto completo. Es el camino de quien va a
       tener que inventarse el acompañamiento algún día, no solo repetirlo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_06_poema import n, bajo, RE7, DOm, SOL, FA7, SIb

HERE = os.path.dirname(__file__)
SOLm = 'Sol menor'
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def ac(ps, d='w'):
    return {'pitches': list(ps), 'dur': d}


# fundamental + quinta de cada cifrado, que es el esqueleto del acorde
QUINTAS = [('D2', 'A2'), ('C2', 'G2'), ('G2', 'D2'), ('F2', 'C3'), ('B2', 'F2')]

CANCION = dict(
    alumno='Eva', num=3, nivel='avanzado', slug='PoemaDeAmor',
    titulo_corto='Poema de Amor', time_sig=(4, 4), key_sig=SOLm,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'poema-de-amor-joan-manuel-serrat.pdf'),
    yt='https://www.youtube.com/results?search_query=serrat+poema+de+amor',

    ficha=dict(
        titulo='Poema de Amor',
        autor='Joan Manuel Serrat',
        datos=[('Tonalidad', 'Sol menor'), ('Compás', '4/4'), ('Tempo', 'Andante'),
               ('Mano izq.', 'Cuatro negras'), ('Compases', '28')],
        armonia=dict(
            titulo='Un molde y seis sitios donde ponerlo',
            tarjetas=[
                ('EL MOLDE', 'Fund · 8ª · 5ª · 8ª',
                 'Cuatro negras, siempre el mismo dibujo. No hay ni un compás distinto en 28.'),
                ('LOS CIFRADOS', 'Re7 · Dom · Solm · Fa7 · Si♭',
                 'Con esos cinco y la vuelta a Re7 se toca la primera página entera.'),
                ('EL FA♯', 'solo en el Re7',
                 'La armadura de Sol menor no lleva sostenidos: cada Fa♯ está escrito a mano, y siempre en el mismo sitio.'),
            ],
            pie='Esta izquierda no se lee: se coloca. Miras el cifrado, pones el molde y ya está. '
                'Por eso se aprende de memoria casi sin querer.',
        ),
        especial=[
            'La armadura de Sol menor lleva dos bemoles: todos los Si y todos los Mi.',
            'La izquierda hace fundamental, octava, quinta y octava. Siempre.',
            'Los cc. 19 y 20 son, nota por nota, los cc. 2 y 3. Está medido.',
            'La partitura pone «Recitado» encima de la primera frase: ahí el tempo es libre.',
            'No hay ni una dinámica escrita en toda la pieza.',
            'El Fa♯ del Re7 es la nota que hace que la música tire hacia Sol menor.',
        ],
        ritmos=[
            ('MI', 'cuatro negras: fundamental, octava, quinta, octava',
             RE7, OCRE, 'bass', SOLm),
            ('MD', 'una redonda: la melodía va muy por encima',
             [n('D4', 'w')], AZUL, 'treble', SOLm),
        ],
        reto='Que no suene a caja de música. Cuatro negras iguales durante veintiocho compases, sin '
             'ninguna dinámica escrita: lo único que puedes mover es cuánto pesa cada nota.',
        truco='Construye el acorde desde dentro. Toca primero solo la fundamental y la quinta —las dos '
              'notas que deciden qué acorde es—, después añade la octava, y solo entonces el molde '
              'entero. Cuando lo hayas montado así, vas a poder inventártelo en cualquier tonalidad.',
        sabias='Serrat escribió «Poema de Amor» en 1969, en catalán y en castellano a la vez. La '
               'palabra «Recitado» que ves encima de la primera frase no es una indicación de piano: '
               'es de canción, y quiere decir que ahí la voz habla en vez de cantar.',
        qr=dict(titulo='Escucha a Serrat',
                texto='Fíjate en la primera frase: no la canta, la dice. Y el piano la espera.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Esta izquierda no se lee: se coloca. Pero antes de colocar nada conviene saber qué se '
              'está colocando, así que el acorde se construye desde dentro — primero las dos notas '
              'que lo definen, después la octava, y al final el molde entero.',
        reglas=['ARMADURA DE SOL MENOR', 'PRIMERO EL ESQUELETO', 'DI EL CIFRADO EN VOZ ALTA'],
        bloques=[
            dict(num=1, titulo='Las dos notas que deciden el acorde', clef='bass',
                 pista='fundamental y quinta · sin la octava y sin el ritmo: solo el esqueleto',
                 sistemas=[
                     dict(cap='a) los cinco cifrados de la primera página, en quintas sostenidas · '
                              'Re · Do · Sol · Fa · Si♭',
                          events=[ac(q) for q in QUINTAS], bars=5, clef='bass'),
                     dict(cap='b) y solo la fundamental, una por compás · esto es por dónde viaja la mano',
                          events=[n('D2', 'w'), n('C2', 'w'), n('G2', 'w'),
                                  n('F2', 'w'), n('B2', 'w'), n('D2', 'w')],
                          bars=6, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTO NO SE LEE, SE COLOCA',
                 texto='Una vez que ves que la izquierda hace siempre fundamental, octava, quinta y '
                       'octava, deja de haber notas que leer: hay un molde y un cifrado que te dice '
                       'dónde ponerlo. Mira los cifrados de tu partitura y tócalos sin leer el '
                       'pentagrama de abajo. Te va a salir casi entero a la primera, y encima te lo '
                       'aprendes de memoria sin querer.'),
            dict(num=2, titulo='Y ahora el molde entero', clef='bass',
                 pista='cc. 1–6 medidos · cuatro negras: la primera pesa, las otras tres acompañan',
                 sistemas=[
                     dict(cap='a) sobre Do menor y Sol menor, los dos más cómodos · para coger el gesto',
                          events=DOm + SOL, bars=2, clef='bass'),
                     dict(cap='b) los dos que se salen de la mano · Fa7 y Si♭: el Si♭ abre la octava '
                              'desde tecla negra, así que colócala en el aire y déjala caer abierta',
                          events=FA7 + SIb, bars=2, clef='bass', show_time=False),
                     dict(cap='c) y la primera página entera · Re7 · Dom · Solm · Fa7 · Si♭ y vuelta',
                          events=RE7 + DOm + SOL + FA7 + SIb + RE7, bars=3, clef='bass',
                          show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='El molde ya está colocado. Lo que queda no son notas nuevas: es aguantarlo veintiocho '
              'compases sin que suene a caja de música, y entender que la primera frase no se canta, '
              'se recita.',
        reglas=['EL RECITADO NO LLEVA PRISA', 'NO SUENE A CAJA DE MÚSICA', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='Aguantar sin endurecerse', clef='bass',
                 pista='ocho compases seguidos · aquí se ve si el brazo está suelto o si estás golpeando',
                 sistemas=[
                     dict(cap='a) cuatro sobre Si♭, que es el que peor cae en la mano, y cuatro sobre '
                              'Re7 · si a mitad empiezas a golpear, para y empieza más flojo',
                          events=SIb * 4 + RE7 * 4, bars=4, clef='bass'),
                     dict(cap='b) y el mismo recorrido con un solo golpe por compás · así se oye la '
                              'forma sin que el relleno la tape',
                          events=[ac(('D2', 'D3')), ac(('C2', 'C3')), ac(('G2', 'G3')),
                                  ac(('F2', 'F3')), ac(('B2', 'B3')), ac(('D2', 'D3'))],
                          bars=6, clef='bass', show_time=False),
                     dict(cap='c) y el paso intermedio: dos golpes por compás, fundamental y octava · '
                              'de aquí al molde entero solo falta rellenar',
                          events=[n('D2', 'h'), n('D3', 'h'), n('C2', 'h'), n('C3', 'h'),
                                  n('G2', 'h'), n('G3', 'h'), n('F2', 'h'), n('F3', 'h'),
                                  n('B2', 'h'), n('B3', 'h'), n('D2', 'h'), n('D3', 'h')],
                          bars=6, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='«RECITADO»: QUÉ SIGNIFICA',
                 texto='La partitura pone Recitado encima de la primera frase. Quiere decir que ahí la '
                       'voz habla en vez de cantar, y que el tempo es libre: la izquierda espera. Al '
                       'piano se traduce así: toca esos compases sin metrónomo, dejando aire entre '
                       'frase y frase, y no entres en tempo hasta que la melodía empiece a cantar de '
                       'verdad. Es el único sitio de la pieza donde puedes hacer lo que quieras con '
                       'el tiempo.'),
            dict(num=4, titulo='El peso, que es lo único que tienes',
                 pista='sin pentagrama: se hace sobre el paso 3, cambiando solo cuánto pesa cada nota',
                 sistemas=[]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE HACE EL PASO 4',
                 texto='Cuatro negras iguales, veintiocho compases, ni una dinámica escrita. Lo único '
                       'que puedes mover es cuánto pesa cada nota: la primera, la fundamental, lleva '
                       'el peso del brazo; las otras tres caen solas, casi sin dedo. Si las cuatro '
                       'pesan igual, esto suena a metrónomo. Si la primera pesa y las otras se apagan, '
                       'suena a guitarra acompañando a alguien. Y ojo al c. 19: los cc. 19 y 20 son, '
                       'nota por nota, los cc. 2 y 3 — ahí no hay nada nuevo que montar.'),
            dict(tipo='escalera', valores=[50, 58, 64, 70, 76, 84],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
