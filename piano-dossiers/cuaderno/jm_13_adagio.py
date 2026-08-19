# -*- coding: utf-8 -*-
"""Adagio, de Albinoni — pieza 13 de José María. Formato ADULTO.

   OJO CON EL ARCHIVO: en la carpeta de Drive este no es un PDF, es un JPEG
   (736 × 1041). Lo convierte `fuente.normalizar` al montar, que es el mismo
   sitio donde se arreglan los PDF que pypdf no sabe copiar.

   Lo comprobado sobre esa imagen (music-scores.com, arr. A. L. Christopherson,
   1 página, 28 compases):

     - Detrás de la clave NO HAY armadura. La propia edición avisa: "The
       original is in the key of G minor", o sea que este arreglo está
       transportado y simplificado.
     - Compás de 3/4. Pone "Adagio ♩ = 60": es la pieza más lenta del cuaderno.
     - Es la primera pieza del cuaderno con DINÁMICAS ESCRITAS de verdad:
       p · mp · cresc. poco a poco · f · rit. · a tempo, y reguladores.
     - Hay TRESILLOS marcados con un 3.
     - Tiene casillas de primera y segunda vez al final.
     - La izquierda va en negras sueltas casi todo el rato, muy sencilla.

   Lo que NO se cita nota a nota: la imagen es de baja resolución y la
   medición de cabezas no es fiable. El material va como ANDAMIO en La menor
   y remite a la partitura. Los tresillos NO se dibujan en las hojas: el motor
   de notación no los escribe, así que se explican con palabras.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jm_comun import (n, ac, sil, objetivo, plan, rodear, unir, colorear,
                      acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FUENTE = os.path.join(HERE, '..', 'students', 'jose_maria', 'source', 'ADAGIO.')


CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=13, nivel='iniciación',
    slug='AdagioAlbinoni', formato='adulto',
    titulo_corto='Adagio · Albinoni', time_sig=(3, 4), key_sig=None,
    partitura=FUENTE,
    yt='https://www.youtube.com/results?search_query=albinoni+adagio+piano+easy',

    ficha=dict(
        titulo='Adagio',
        autor='Tomaso Albinoni · arreglo de A. L. Christopherson · music-scores.com',
        datos=[('Compás', '3/4'), ('Tempo', 'Adagio ♩ = 60'),
               ('Novedad', 'Dinámicas escritas'), ('Compases', '28'),
               ('Mano izq.', 'Negras sueltas')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio: el dibujo es el de tu partitura y las notas exactas están allí. Los '
                   'tresillos no se pueden dibujar aquí; se explican en la hoja de al lado.',
        armonia=dict(
            titulo='La primera pieza en la que lo difícil es el sonido',
            tarjetas=[
                ('EL TEMPO', '♩ = 60',
                 'Un golpe por segundo. Es lento de verdad, y eso no lo hace fácil: con notas largas '
                 'no hay dónde esconderse.'),
                ('LAS DINÁMICAS', 'p, mp, f',
                 'Está escrito cuándo suena flojo y cuándo fuerte, y hasta cuándo crecer poco a poco. '
                 'Es lo nuevo de la semana.'),
                ('LOS TRESILLOS', 'El 3',
                 'Tres notas en el sitio de dos. Se cuentan "u-ni-dad", tres sílabas iguales dentro '
                 'de un solo golpe.'),
                ('LA IZQUIERDA', 'Muy sencilla',
                 'Negras sueltas casi todo el rato. Está así a propósito: la atención tiene que ir al '
                 'sonido, no a los dedos.'),
            ],
            pie='Esta pieza está aquí justamente porque las notas son fáciles. Cuando no hay que pelear '
                'con los dedos es cuando se puede empezar a trabajar en cómo suena, que es la parte '
                'que de verdad separa tocar de sonar.',
        ),
        ritmos=[
            ('MANO DERECHA', 'notas largas, y hay que sostenerlas · andamio',
             [n('A4', 'h.'), n('G4', 'h.')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'negras sueltas, una por golpe · andamio',
             [n('A2'), n('E3'), n('A3')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay armadura. La edición avisa de que el original está en Sol menor '
            'y este arreglo está cambiado de tono.',
            'Pone "Adagio ♩ = 60": un golpe por segundo.',
            'Es la primera pieza del cuaderno con dinámicas escritas: p, mp, f y reguladores.',
            'Pone "cresc. poco a poco": crecer poquito a poco, no de golpe.',
            'Hay tresillos marcados con un 3: tres notas en el sitio de dos.',
            'Al final hay casillas de primera y segunda vez, y un "rit." antes del "a tempo".',
        ],
        reto='Aguantar. A ♩=60 cada compás dura tres segundos, y tres segundos son eternos si no sabes '
             'qué estás haciendo con el sonido mientras la nota suena.',
        truco='Toca una nota larga y ESCÚCHALA hasta el final, sin pensar en la siguiente. Cuenta los '
              'tres golpes mirando a la nota, no a la mano. Suena a tontería y es exactamente el '
              'trabajo: en las piezas lentas se falla por adelantarse, y uno se adelanta cuando deja '
              'de escuchar lo que ya está sonando.',
        sabias='Casi seguro que Albinoni no la escribió. La compuso en 1958 un musicólogo italiano, '
               'Remo Giazotto, que dijo haberla reconstruido de un fragmento de Albinoni encontrado '
               'entre ruinas. El fragmento nunca ha aparecido.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la versión de orquesta con órgano. Fíjate en cómo crece: eso es el '
                      '"cresc. poco a poco" de tu partitura.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí las notas no son el problema. El trabajo de esta semana es de oído y de brazo: '
              'sostener el sonido, hacerlo crecer donde lo pide la partitura y no adelantarse. Ve '
              'despacio de verdad, que para eso pone Adagio.',
        reglas=['ESCUCHA LA NOTA HASTA EL FINAL', 'CRECER POCO A POCO, NO DE GOLPE',
                'A ♩ = 60, NI UN PELÍN MÁS'],
        bloques=[
            dict(num=1, titulo='Sostener: la nota larga de verdad',
                 pista='andamio · cuenta los tres golpes mirando la nota, no la mano',
                 sistemas=[
                     dict(cap='a) una nota por compás, y se escucha hasta el final · si se apaga antes '
                              'de tiempo, has soltado el dedo',
                          events=[n('A4', 'h.'), n('G4', 'h.'), n('F4', 'h.'), n('E4', 'h.')],
                          matiz='mp',
                          bars=4),
                     dict(cap='b) y ahora con una nota que se mueve dentro del compás · sin que la '
                              'línea se rompa',
                          events=[n('A4', 'h'), n('G4'),
                                  n('F4', 'h'), n('E4'),
                                  n('D4', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UN TRESILLO',
                 texto='Un tresillo son TRES notas en el hueco donde normalmente caben dos. Se marca '
                       'con un 3 encima. No se cuenta con números: se dice una palabra de tres sílabas '
                       'seguidas, siempre la misma, dentro de un solo golpe. "Ma-ri-po", "u-ni-dad". '
                       'Lo importante es que las tres duren igual y que quepan justo en el golpe, sin '
                       'que el compás se estire.'),
            dict(num=2, titulo='La izquierda, que aquí es la fácil', clef='bass',
                 pista='andamio · negras sueltas, una por golpe, sin acentuar ninguna',
                 sistemas=[
                     dict(cap='a) tres negras por compás, todas igual de suaves',
                          events=[n('A2'), n('E3'), n('A3'),
                                  n('F2'), n('C3'), n('F3'),
                                  n('G2'), n('D3'), n('G3')],
                          bars=3, clef='bass'),
                     dict(cap='b) y bajando, que es lo que hace la pieza · sin acentuar ninguna, '
                              'todas del mismo tamaño',
                          events=[n('A2'), n('G2'), n('F2'),
                                  n('E2'), n('F2'), n('G2'),
                                  n('A2'), n('E3'), n('A2')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='Crecer poco a poco',
                 pista='andamio · el "cresc." de tu partitura dura varios compases, no uno',
                 sistemas=[
                     dict(cap='a) la misma frase cuatro veces, cada una un poquito más · el salto de '
                              'la primera a la última tiene que oírse claramente',
                          events=[n('E4'), n('F4'), n('G4'),
                                  n('E4'), n('F4'), n('G4'),
                                  n('E4'), n('F4'), n('G4'),
                                  n('A4', 'h.')],
                          bars=4),
                     dict(cap='b) y ahora al revés, bajando de fuerte a flojo · frenar el sonido es '
                              'más difícil que subirlo',
                          events=[n('A4'), n('G4'), n('F4'),
                                  n('A4'), n('G4'), n('F4'),
                                  n('E4', 'h.')],
                          bars=3, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Adagio · para casa',
            intro='Veinte minutos al día, y esta semana con los oídos más que con los dedos.',
            bloques=[
                objetivo('Tocar cuatro compases a ♩ = 60 sin adelantarte ni una vez, escuchando cada '
                         'nota hasta que se apaga.'),
                plan((5, 'Notas largas sueltas: tocar y escuchar hasta el final'),
                     (5, 'La izquierda sola, tres negras por compás, suaves'),
                     (5, 'La frase que crece, cuatro veces cada una más'),
                     (5, 'Cuatro compases con las dos manos, a ♩ = 60')),
                rodear([[n('A4', 'h.')], [n('G4', 'h.')], [n('A4', 'h.')], [n('F4', 'h.')]],
                       titulo='Rodea los dos compases iguales',
                       pista='andamio · aquí lo difícil no es verlo, es que suenen igual'),
                unir([('p', 'crecer poquito a poco'),
                      ('f', 'flojito'),
                      ('cresc. poco a poco', 'volver al tempo de antes'),
                      ('a tempo', 'fuerte')],
                     titulo='Une cada indicación con lo que quiere decir',
                     pista='están desordenadas · todas salen en tu partitura'),
                colorear([n('A4', 'h.'), n('G4', 'h.'), n('F4'), n('E4'),
                          n('D4'), n('E4', 'h.')],
                         ['Un color para las que duran el compás entero y otro para las de un golpe.'],
                         titulo='Colorea según lo que duran',
                         pista='dos colores'),
                acuerdate('Una pieza lenta no es una pieza fácil: es una pieza donde no puedes '
                          'esconder nada. Cada nota se oye entera, y si el sonido se apaga a mitad o '
                          'entra antes de tiempo, se nota muchísimo más que en una rápida.',
                          etiqueta='LENTO NO ES FÁCIL'),
                para_clase('Cuatro compases a ♩ = 60, y una duda: dónde empieza y dónde acaba el '
                           '"cresc. poco a poco" de tu partitura.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
