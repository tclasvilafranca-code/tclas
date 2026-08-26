# -*- coding: utf-8 -*-
"""America (My Country, 'Tis of Thee) — pieza 2 de José María. Formato ADULTO.

   Lo medido sobre el PDF de su carpeta de Drive (arr. Gilbert DeBenedetti,
   "Level Two", Gradimi.com, 1 página, 16 compases):

     - Do mayor: detrás de la clave no hay nada. Compás de 3/4. Pone
       "With Reverence".
     - La melodía de los cuatro primeros compases, MEDIDA cabeza a cabeza con
       `cabezas.py` y contrastada con la melodía conocida (es God Save the King
       transportada a Do):

         c. 1   Do · Do · Re          tres negras
         c. 2   Si · Do · Re          negra con puntillo · corchea · negra
         c. 3   Mi · Mi · Fa          tres negras
         c. 4   Mi · Re · Do          negra con puntillo · corchea · negra

       Alturas: C4 C4 D4 | B3 C4 D4 | E4 E4 F4 | E4 D4 C4.
     - La digitación viene impresa en LAS DOS MANOS: 2 · 3 · 1 · 4 · 3 arriba,
       y 3/5 · 1 · 2 · 5 abajo.
     - La izquierda toca acordes de dos notas y blancas con puntillo: una cosa
       por compás y nada más.
     - Lleva la letra debajo del pentagrama, sílaba a sílaba.

   Es la segunda del cuaderno porque es la primera melodía de verdad: en el
   Romance las dos manos hacían lo mismo, y aquí ya son dos cosas distintas.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloque_puntillo, bloques_extra
from jm_comun import (n, ac, plan, metronomo, diferencias, nombres, escribir,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los cuatro primeros compases, medidos. Esto SÍ es cita literal.
FRASE = [n('C4'), n('C4'), n('D4'),
         n('B3', 'q.'), {'pitch': 'C4', 'dur': 'e'}, n('D4'),
         n('E4'), n('E4'), n('F4'),
         n('E4', 'q.'), {'pitch': 'D4', 'dur': 'e'}, n('C4')]

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=2, nivel='iniciación',
    slug='America', formato='adulto',
    titulo_corto='America', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           'himno America.pdf'),
    yt='https://www.youtube.com/results?search_query=my+country+tis+of+thee+piano',

    ficha=dict(
        titulo='America',
        autor="My Country, 'Tis of Thee · arreglo de Gilbert DeBenedetti · Level Two",
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'With Reverence'), ('Compases', '16'),
               ('Dedos', 'Escritos')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='La derecha son los tres primeros golpes de la melodía, medidos en tu partitura. '
                   'La izquierda es andamio: el dibujo es el suyo y las notas exactas están allí.',
        armonia=dict(
            titulo='La melodía entera cabe en siete notas',
            tarjetas=[
                ('COMPASES 1-2', 'Do · Do · Re',
                 'Empieza repitiendo la misma tecla y solo después se mueve. Esos dos primeros '
                 'compases son media pieza.'),
                ('COMPASES 3-4', 'Mi · Mi · Fa',
                 'El mismo dibujo un escalón más arriba. Si te aprendes el primero, el segundo va '
                 'de regalo.'),
                ('EL RITMO', 'Larga y corta',
                 'Los compases pares llevan negra con puntillo y corchea: "LAAA-ar-ga". Es lo que le '
                 'da el aire de himno.'),
                ('LA IZQUIERDA', 'Una por compás',
                 'Dos notas a la vez, largas, una vez por compás. Mientras la derecha canta, la '
                 'izquierda solo aguanta.'),
            ],
            pie='Toda la melodía se mueve entre el Si y el Fa: siete teclas blancas seguidas y ni una '
                'más. La mano se coloca una vez y ya no hay que buscar nada.',
        ),
        ritmos=[
            ('MANO DERECHA', 'los tres primeros golpes, medidos',
             [n('C4'), n('C4'), n('D4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos notas a la vez, y duran el compás · andamio',
             [ac(('C3', 'E3'), 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'La digitación viene impresa en las dos manos. Respétala: está pensada para que la mano '
            'no tenga que moverse de sitio.',
            'La letra va debajo del pentagrama, sílaba a sílaba. Sirve para el ritmo: si la dices en '
            'voz alta, el ritmo sale solo.',
            'Los compases 2 y 4 llevan negra con puntillo y corchea, que es la figura nueva de esta '
            'pieza.',
            'La izquierda toca una sola vez por compás y aguanta los tres golpes.',
            'Al final pone "rit.": ir frenando poco a poco en los dos últimos compases.',
        ],
        reto='La negra con puntillo. Es la primera figura larga-corta del cuaderno y casi siempre se '
             'toca mal por lo mismo: se acorta la larga y la corta llega antes de tiempo.',
        truco='Di la letra en voz alta mientras tocas, sílaba a sílaba: "my COUN-try TIS of THEE". La '
              'letra ya lleva el ritmo dentro, así que si la dices bien no puedes tocarlo mal. Es más '
              'fiable que contar, y para eso está impresa.',
        sabias='La melodía es la del himno del Reino Unido, "God Save the King". En 1831 un pastor de '
               'Boston le puso letra nueva en inglés americano y durante casi cien años fue el himno '
               'no oficial de Estados Unidos, hasta que en 1931 lo fue el que tú tocas en la pieza '
               'siguiente.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en cómo frena al final: eso es el "rit." de tu partitura.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza tiene dos cosas nuevas y ninguna es de notas: la primera figura con '
              'puntillo y la izquierda haciendo algo distinto de la derecha. Trabaja las dos por '
              'separado y júntalas al final; si empiezas juntándolas, la que sale mal contagia a la '
              'otra.',
        reglas=['LA MANO NO CAMBIA DE SITIO', 'LA LETRA TE DA EL RITMO', 'LA IZQUIERDA SOLO AGUANTA'],
        bloques=[
            dict(num=1, titulo='La melodía de los cuatro primeros compases',
                 pista='cc. 1-4 · medidos en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) las alturas medidas de los cc. 1–4, en negras y sin el puntillo · así se ven las notas sin '
                              'pelearse con el ritmo',
                          events=[n('C4'), n('C4'), n('D4'),
                                  n('B3'), n('C4'), n('D4'),
                                  n('E4'), n('E4'), n('F4'),
                                  n('E4'), n('D4'), n('C4')],
                          bars=4),
                     dict(cap='b) y ahora con el ritmo de verdad · di la letra en voz alta mientras '
                              'lo tocas',
                          events=FRASE, bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UNA NEGRA CON PUNTILLO',
                 texto='El puntito de detrás de una nota le añade la mitad de lo que dura. Una negra '
                       'vale un golpe, así que una negra con puntillo vale golpe y medio, y la corchea '
                       'que va detrás ocupa el medio que queda. Contando: "UN dos-y TRES", y la corta '
                       'cae en la "y". Si dices la letra impresa, sale sola.'),
            dict(num=2, titulo='La izquierda: tocar y aguantar', clef='bass',
                 pista='andamio en Do mayor · las notas exactas están en tu partitura, con su '
                       'digitación escrita',
                 sistemas=[
                     dict(cap='a) dos notas a la vez, una vez por compás, y no se sueltan hasta el '
                              'compás siguiente',
                          events=[ac(('C3', 'E3'), 'h.'), ac(('B2', 'D3'), 'h.'),
                                  ac(('C3', 'E3'), 'h.'), ac(('C3', 'F3'), 'h.')],
                          bars=4, clef='bass'),
                     dict(cap='b) y el mismo ejercicio soltando en el tres · así la mano descansa y '
                              'llega colocada al compás siguiente',
                          events=[ac(('C3', 'E3'), 'h'), n('C3'),
                                  ac(('B2', 'D3'), 'h'), n('B2'),
                                  ac(('C3', 'E3'), 'h'), n('C3')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, los dos primeros compases',
                 pista='la derecha va medida (cc. 1–2) · muy despacio · la izquierda entra en el '
                       'uno y no se mueve más',
                 sistemas=[
                     dict(cap='a) la derecha con su ritmo y la izquierda aguantando debajo · cuenta '
                              'un-dos-tres en voz alta',
                          events=[n('C4'), n('C4'), n('D4'),
                                  n('B3', 'q.'), {'pitch': 'C4', 'dur': 'e'}, n('D4')],
                          bars=2),
                     dict(cap='b) esto es lo que hace la izquierda a la vez (andamio) · una vez por '
                              'compás, en el primer golpe',
                          events=[ac(('C3', 'E3'), 'h.'), ac(('B2', 'D3'), 'h.')],
                          bars=2, clef='bass', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='America · para casa',
            intro='Veinte minutos al día. La pieza es corta: lo que hay que trabajar es el ritmo con '
                  'puntillo, no las notas.',
            bloques=[
                plan((5, 'Los cuatro primeros compases en negras, sin puntillo'),
                     (5, 'Los mismos, con el ritmo bueno y diciendo la letra'),
                     (5, 'La izquierda sola: entrar en el uno y aguantar'),
                     (5, 'Las dos manos, dos compases, muy despacio')),
                metronomo('Empieza a ♩ = 60 y sube de cinco en cinco.',
                          'Solo subes cuando salga entera y sin pararte tres veces seguidas.'),
                diferencias(
                    [n('C4'), n('C4'), n('D4'), n('B3'), n('C4'), n('D4')],
                    [n('C4'), n('D4'), n('D4'), n('B3'), n('C4'), n('E4')],
                    cuantas=2,
                    titulo='Busca las dos diferencias',
                    pista='arriba, los compases 1 y 2 de tu partitura · abajo, con dos cambios'),
                nombres(['C4', 'D4', 'E4', 'F4', 'B3', 'E4', 'D4', 'C4'],
                        titulo='Los nombres, sin mirar la partitura',
                        pista='son las notas que usa la pieza · escríbelos debajo'),
                escribir(titulo='Copia aquí el compás 2 de tu partitura',
                         pista='con su puntillo y su corchea · cópialo y luego tócalo cinco veces'),
                para_clase('La melodía sola, y el compás donde entra la negra con puntillo. Si hay un sitio donde siempre te tropiezas, tráelo marcado.'),
            ],
        ),
    ],
)

# El ritmo con puntillo que esta pieza EXPLICA en su texto y no dibujaba en
# ningún sitio. Lo destapó el auditor de vocabulario al ganar la entrada de
# esta figura, que antes no miraba nadie.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 33, 'C4', 'C3',
    'la mano en Do antes de contar el puntillo',
    desde=5, time_sig=(3, 4)) + [
    bloque_puntillo('Do mayor', 4, 'C4', 'el ritmo con puntillo de "My country, ’tis of thee"',
                    time_sig=(3, 4), lento=True)]

if __name__ == '__main__':
    print('generado', construir(CANCION))
