# -*- coding: utf-8 -*-
"""Nocturne op. 9, de Chopin — pieza 27 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Nocturne Op.9 —
   Frédéric Chopin, arr: Benny Chaw", 1 página; el mismo archivo que la pieza
   19 de Luisa, byte a byte), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor. (El nocturno original está
       en Mi bemol; este arreglo lo pasa a Do.)
     - 3/4 y "mp".
     - Anacrusa de un solo tiempo en la izquierda, con el dedo 4 escrito.
     - El primer compás de la derecha es una nota que dura el compás entero,
       ligada al siguiente. Después, tres negras.
     - La izquierda calla dos compases después de la nota inicial.

   Cierra el álbum a propósito: de notas es de las más fáciles y de sonido es
   de las más difíciles. Es la pieza para la audición de fin de curso.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from me_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=27, nivel='intermedio', slug='Nocturne',
    formato='adulto',
    titulo_corto='Nocturne op. 9', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'nocturne-op9-chopin.'),
    yt='https://www.youtube.com/results?search_query=chopin+nocturne+op+9+no+2+piano',

    ficha=dict(
        titulo='Nocturne op. 9',
        autor='Frédéric Chopin · hacia 1831 · arr. Benny Chaw',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'mp'), ('Empieza', 'Antes del compás'),
               ('Derecha', 'Notas largas')],
        titulo_ritmos='Pocas notas, y muy largas',
        pie_ritmos='Andamio en Do mayor. Lo literal es el arranque: la izquierda entra con una '
                   'negra sola y la derecha con una nota que dura el compás entero.',
        armonia=dict(
            titulo='Por qué esta cierra el álbum',
            tarjetas=[
                ('POCAS NOTAS', 'Y muy largas',
                 'De leer es de las más fáciles de tu carpeta: una nota que dura el compás entero y '
                 'luego tres negras. No hay ninguna carrera de dedos.'),
                ('Y ES LA MÁS DIFÍCIL', 'De sonido',
                 'Con tan pocas notas se oye todo: si una entra más fuerte que la anterior, la '
                 'frase se rompe. No se puede tapar nada con velocidad.'),
                ('EMPIEZA LA IZQUIERDA', 'Una negra sola',
                 'Antes del primer compás hay una sola nota de la izquierda, con el dedo 4 escrito. '
                 'La derecha entra después.'),
                ('UNA LIGADURA LARGA', 'Se aguanta',
                 'La primera nota de la melodía pasa de un compás al siguiente sin volver a tocarse: '
                 'se toca una vez y se deja sonar.'),
            ],
            pie='Es la pieza que se guarda para el final del curso: no por difícil de dedos, sino '
                'porque exige todo lo que has trabajado a lo largo del año, junto.',
        ),
        ritmos=[
            ('MANO IZQUIERDA', 'la negra del principio, con silencios delante',
             [sil('h'), n('G2')], AZUL, 'bass', None),
            ('MANO DERECHA', 'una nota que dura el compás entero · literal',
             [n('E4', 'h.')], OCRE, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 3/4 y "mp": suave.',
            'Empieza la izquierda, con una sola negra antes del primer compás.',
            'La primera nota de la melodía dura el compás entero.',
            'Esa nota está ligada al compás siguiente: se toca una vez y se aguanta.',
            'La izquierda calla dos compases después de la nota del principio.',
        ],
        reto='El sonido, no las notas. Con tan pocas y tan largas, cualquier diferencia de volumen '
             'entre una y la siguiente se nota muchísimo.',
        truco='Toca las tres primeras notas y escucha solo el final de cada una, cuando el sonido '
              'casi ha desaparecido. Si se corta antes de que llegue la siguiente, la frase se '
              'rompe. Deja que el sonido caiga solo, sin apagarlo tú.',
        sabias='Chopin escribió veintiún nocturnos y este es de los más interpretados. La palabra '
               '"nocturno" la inventó el compositor irlandés John Field: piezas pensadas para tocar '
               'de noche, con la mano izquierda imitando a una guitarra.',
        qr=dict(titulo='Escúchala',
                texto='Escúchala entera con los ojos cerrados antes de tocar una sola nota. Es de '
                      'las piezas que hay que tener primero en el oído.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Pocas notas, así que el trabajo es de sonido. Primero las notas largas solas, '
              'después la entrada de la izquierda, y al final las dos.',
        reglas=['ESCÚCHALA ANTES DE TOCARLA', 'LAS NOTAS LARGAS, HASTA EL FINAL',
                'LA PRIMERA DE CADA GRUPO PESA UN POCO MÁS'],
        bloques=[
            dict(num=1, titulo='Notas largas, escuchando cómo acaban',
                 pista='andamio en Do mayor · lo que se practica es el sonido, no los dedos',
                 sistemas=[
                     dict(cap='a) una nota por compás, aguantada entera',
                          events=[n('E4', 'h.'), n('C4', 'h.'), n('D4', 'h.'), n('B3', 'h.')],
                          matiz='mp',
                          ligar=True,
                          bars=4),
                     dict(cap='b) y con tres negras detrás, la primera con un poco más de peso',
                          events=[n('G4', 'h.'), n('F4'), n('E4'), n('D4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Empezar antes del compás, con la izquierda',
                 pista='andamio · la negra suelta del principio es la de tu partitura',
                 sistemas=[
                     dict(cap='a) una negra sola y ya empieza el compás',
                          events=[sil('h'), n('G2'), n('C3', 'h.'), n('G2', 'h.')],
                          bars=3, clef='bass'),
                     dict(cap='b) y después la izquierda calla dos compases',
                          events=[n('F2'), sil('h'), sil('q'), sil('h'), sil('q'), n('C3', 'h')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA PIEZA CIERRA EL ÁLBUM',
                 texto='No porque tenga notas difíciles: no las tiene. Cierra el álbum porque para '
                       'que suene bien hace falta todo lo trabajado durante el curso —contar, '
                       'esperar, sostener una nota entera, entrar antes del compás— y además algo '
                       'que no se escribe en una hoja: escuchar mientras se toca. Es la pieza para '
                       'la audición de fin de curso.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la melodía por encima y la izquierda muy suave · sin prisa',
                 sistemas=[
                     dict(cap='a) la izquierda entra antes y la derecha sostiene el compás entero',
                          events=[sil('h'), n('G2'), ac(('C3', 'E4'), 'h.'), ac(('G2', 'C4'), 'h.')],
                          bars=3),
                     dict(cap='b) y con las tres negras de la melodía encima',
                          events=[ac(('F2', 'D4')), n('C4'), n('B3'), ac(('C3', 'B3'), 'h.')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 55, 'C4', 'C3',
                          'el sonido: aquí no se puede esconder ninguna nota',
                          desde=4, time_sig=(3, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
