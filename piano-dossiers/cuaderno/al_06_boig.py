# -*- coding: utf-8 -*-
"""Boig per tu (Sau) — pieza 6 de Alan. ADULTO exigente, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Pilar Sanz,
   soldesolfa.com, 1 página, escaneo a 86 ppp), mirado a 220-300 ppp:

     - Detrás de la clave no hay nada. 4/4. No trae tempo ni intensidad.
     - La izquierda toca un acorde de dos notas en redonda por compás.
     - Hay sostenidos escritos delante de algunas notas (un Fa♯ en los cc. 17-18).
     - Ninguna figura más corta que la corchea: corcheas sueltas y de dos en dos, negras con puntillo,
       blancas y redondas. Ni una barra doble.
     - MEDIDO (a 300 ppp), c. 1 de la derecha: silencio de negra con puntillo ·
       Sol4 · Si4 (corcheas) · Do5 (negra) · Re5 (corchea). 1,5 + 0,5 + 0,5 + 1 +
       0,5 = 4.
   Es la misma partitura que la de Aída: lo literal coincide, y el andamio va por
   otros caminos (aquí, por el eco de la frase y por contar las mitades).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, corch, reto, plan, metronomo, escribir, diferencias,
                      acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: c. 1 de la derecha
C1 = [sil('q.')] + corch(['G4', 'B4']) + [n('C5'), n('D5', 'e')]

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=6, nivel='intermedio', slug='BoigPerTu',
    formato='adulto',
    titulo_corto='Boig per tu', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source', 'Boig per tu, Sau.'),
    yt='https://www.youtube.com/results?search_query=boig+per+tu+sau+piano',

    ficha=dict(
        titulo='Boig per tu',
        autor='Sau · arreglo de Pilar Sanz',
        datos=[('Tonalidad', 'Sin armadura'), ('Compás', '4/4'),
               ('Carácter', 'Sin marcar'), ('Empieza', 'A contratiempo'),
               ('Izquierda', 'Redondas')],
        titulo_ritmos='El compás 1, y lo que hace la izquierda',
        pie_ritmos='Arriba, el c. 1 de la derecha MEDIDO sobre tu partitura, con su silencio de '
                   'entrada. Abajo, andamio: la izquierda toca dos notas en redonda, una por compás.',
        armonia=dict(
            titulo='Entrar donde no hay golpe',
            tarjetas=[
                ('EL SILENCIO', 'Tiempo y medio',
                 'La pieza empieza con un silencio de negra con puntillo: la melodía entra en la '
                 'segunda mitad del segundo tiempo, justo donde un metrónomo no suena.'),
                ('LA IZQUIERDA', 'Una redonda',
                 'Dos notas que duran el compás entero. Es el suelo: mientras esté ahí, la '
                 'entrada a contratiempo tiene algo con lo que medirse.'),
                ('SIN ARMADURA', 'Y algún sostenido',
                 'Detrás de la clave no hay nada, pero hacia el c. 17 aparece un Fa♯ escrito '
                 'delante de la nota, y vale solo hasta el final del compás.'),
                ('SIN METRÓNOMO', 'Lo eliges tú',
                 'La partitura no trae número. Es una balada: lenta, con sitio para respirar '
                 'entre una frase y la siguiente.'),
            ],
            pie='Es una partitura escaneada, con una marca de agua grande: se lee, pero las notas '
                'pequeñas hay que mirarlas dos veces antes de fiarte.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido', C1, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · una redonda por compás',
             [ac(('A2', 'E3'), 'w'), ac(('F2', 'C3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El c. 1 empieza con un silencio de negra con puntillo.',
            'La izquierda toca una redonda de dos notas por compás.',
            'No viene ningún número de metrónomo.',
            'Hay sostenidos escritos delante de algunas notas, como el Fa♯ del c. 17.',
            'Es un escaneo con marca de agua: hay que mirarlo con atención.',
        ],
        reto='Entrar a tiempo y medio. El metrónomo suena en el uno y en el dos, y tú entras '
             'entre el dos y el tres: justo donde no hay clic.',
        truco='Cuenta "un-y-dos-Y" y entra en la última "y", que es la que va en mayúscula. '
              'Contar solo los números no sirve: la nota de entrada no cae en ningún número.',
        sabias='Boig per tu es de Sau, un grupo catalán, y se canta en toda España aunque la letra '
               'esté en catalán. Es de las canciones que todo el mundo se sabe sin saber de '
               'dónde.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta "un-y-dos-y" desde el primer acorde. La voz entra justo en la última '
                      '"y", y ese pequeño retraso es toda la gracia de la frase.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La entrada no se aprende tocando: se aprende contando. Los primeros cinco minutos '
              'de cada día van sin piano.',
        reglas=['CUENTA "UN-Y-DOS-Y" SIEMPRE', 'LA ENTRADA CAE EN LA SEGUNDA "Y"',
                'LA IZQUIERDA NO SE SUELTA'],
        bloques=[
            dict(num=1, titulo='El sitio donde entra la melodía',
                 pista='andamio · lo que se practica es el hueco, no las notas',
                 sistemas=[
                     dict(cap='a) primero el compás entero en negras, para tener los cuatro golpes',
                          events=[n('C5'), n('D5'), n('E5'), n('D5')], bars=1),
                     dict(cap='b) y ahora quitando la primera negra y media · ese hueco es tu '
                              'silencio de entrada',
                          events=[sil('q.'), n('C5', 'e'), n('D5'), n('E5')],
                          bars=1, show_time=False),
                     dict(cap='c) y tres veces seguidas, sin parar · entrar siempre en el mismo '
                              'sitio es lo que hay que automatizar',
                          events=[sil('q.'), n('C5', 'e'), n('D5'), n('E5'),
                                  sil('q.'), n('E5', 'e'), n('D5'), n('C5'),
                                  sil('q.'), n('C5', 'e'), n('D5'), n('E5')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA ENTRADA NO ES UNA ANACRUSA',
                 texto='En una anacrusa entras ANTES del compás y el sitio se encuentra contando '
                       'hacia atrás desde el uno. Aquí entras DENTRO del compás, en la mitad de un '
                       'tiempo, y no hay ningún golpe con el que coincidir: el metrónomo suena en '
                       'el dos y tú entras después. Cuenta las mitades en voz alta hasta que la '
                       'mano se acostumbre; con los números solos no se llega.'),
            dict(num=2, titulo='El compás 1, tal y como está escrito',
                 pista='c. 1 · medido sobre tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) el c. 1 con el silencio partido en negra y corchea, para contarlo '
                              '· en tu partitura es UN silencio de negra con puntillo',
                          events=[sil('q'), sil('e')] + corch(['G4', 'B4']) +
                                 [n('C5'), n('D5', 'e')],
                          bars=1),
                     dict(cap='b) el mismo compás sin el silencio · NO es lo que pone tu partitura: '
                              'sirve para ver lo que cambia el hueco',
                          events=corch(['G4', 'B4']) + [n('C5'), n('D5', 'e'), sil('q.')],
                          bars=1, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, con el suelo debajo',
                 pista='el c. 1 de la derecha está medido · el acorde de abajo es andamio',
                 sistemas=[
                     dict(cap='a) la derecha es la MEDIDA del c. 1 de tu partitura · el acorde suena en '
                              'el uno y se aguanta hasta el final del compás',
                          events=[ac(('A2', 'E3'), 'q.'), ac(('G4',), 'e'), ac(('B4',), 'e'),
                                  ac(('C5',)), ac(('D5',), 'e')],
                          bars=1, manos='sostiene'),
                 ]),
            dict(num=4, titulo='Un sostenido que hay que anunciar',
                 pista='cc. 17-18 · el Fa♯ de tu partitura · aquí, andamio para que la mano lo conozca',
                 sistemas=[
                     dict(cap='a) un Mi, un Fa♯ y un Sol · el sostenido sube el Fa a la tecla negra '
                              'y vale solo hasta el final del compás',
                          events=[n('E5'), n('F#5'), n('G5'), n('E5')], bars=1),
                 ]),
        ] + bloques_extra('La menor', 96, 'A4', 'A2',
                          'entrar a tiempo y medio, donde el metrónomo no suena',
                          desde=5, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Boig per tu · para casa',
            intro='Quince minutos al día, y los cinco primeros contando sin tocar. Es la manera más '
                  'rápida de ganar esta pieza.',
            bloques=[
                reto('Entrar a tiempo y medio cinco veces seguidas, sin que el metrónomo te lo '
                     'ponga fácil.',
                     'Pon el metrónomo a 60, cuenta "un-y-dos-Y" y entra en la última "y". Anota '
                     'cuántas entradas seguidas te salen: el objetivo es cinco.'),
                plan((5, 'Contar "un-y-dos-y" y dar una palmada en la segunda "y"'),
                     (4, 'El c. 1 de la derecha, con su silencio'),
                     (3, 'Los acordes de la izquierda, en redondas'),
                     (3, 'Los dos primeros compases con las dos manos')),
                metronomo('Empieza a ♩ = 60 con la derecha sola: a esa velocidad da tiempo a oír el '
                          'hueco entero antes de entrar.',
                          'Tu partitura no trae número de metrónomo, así que estos son de trabajo. '
                          'Sube a 76 solo cuando la entrada salga tres veces seguidas.'),
                escribir(titulo='Copia aquí el c. 1 de la derecha',
                         pista='un silencio de negra con puntillo, dos corcheas, una negra y una '
                               'corchea · y escribe debajo el nombre de cada nota'),
                diferencias(list(C1),
                            [sil('q')] + corch(['G4', 'B4']) + [n('C5'), n('D5')],
                            cuantas=2,
                            titulo='Busca las diferencias',
                            pista='arriba, tu c. 1 medido · abajo, con el silencio y una figura '
                                  'cambiados'),
                acuerdate('El silencio de negra con puntillo se cuenta entero: tiempo y medio. Si '
                          'entras en el dos exacto, ya no es lo que pone tu partitura.',
                          etiqueta='EL SILENCIO ES MÚSICA'),
                para_clase('Los dos primeros compases con las dos manos, y la entrada contada en '
                           'voz alta. Si te sale bien sin contar, dímelo: entonces la semana que '
                           'viene subimos la velocidad en vez de repetirla.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
