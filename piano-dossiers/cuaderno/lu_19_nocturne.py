# -*- coding: utf-8 -*-
"""Nocturne op. 9, de Chopin — pieza 19 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Nocturne Op.9 —
   Frédéric Chopin, arr: Benny Chaw", 1 página), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor. (El nocturno original está en
       Mi bemol; este arreglo lo pasa a Do para que no haya bemoles.)
     - 3/4 y "mp".
     - **ANACRUSA de un solo tiempo**: la izquierda toca una negra sola, con
       el dedo 4 escrito, y la derecha calla.
     - El primer compás de la derecha es una BLANCA CON PUNTILLO ligada al
       compás siguiente. Después, tres negras.
     - La izquierda calla dos compases enteros después de esa nota inicial.

   Va la última del cuaderno a propósito: de notas es de las más fáciles y de
   sonido es la más difícil. Es la pieza de la audición.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from lu_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=19, nivel='iniciación', slug='Nocturne',
    formato='adulto',
    titulo_corto='Nocturne op. 9', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source', 'nocturne-op9-chopin. easy'),
    yt='https://www.youtube.com/results?search_query=chopin+nocturne+op+9+no+2+easy+piano',

    ficha=dict(
        titulo='Nocturne op. 9',
        autor='Frédéric Chopin · hacia 1831 · arr. Benny Chaw',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'mp · cantando'), ('Empieza', 'Antes del compás'),
               ('Derecha', 'Notas largas')],
        titulo_ritmos='Pocas notas y muy largas',
        pie_ritmos='Andamio en Do mayor. Lo literal es el arranque: la izquierda toca una negra '
                   'sola antes del compás y la derecha entra con una nota de tres tiempos.',
        armonia=dict(
            titulo='Por qué esta va la última',
            tarjetas=[
                ('POCAS NOTAS', 'Y muy largas',
                 'De leer es de las más fáciles del cuaderno: una nota que dura el compás entero y '
                 'luego tres negras. No hay ninguna carrera de dedos.'),
                ('Y ES LA MÁS DIFÍCIL', 'De sonido',
                 'Cuando hay pocas notas se oyen todas. Aquí no se puede tapar nada con la '
                 'velocidad: cada nota tiene que salir con el sonido justo.'),
                ('EMPIEZA LA IZQUIERDA', 'Una negra sola',
                 'Antes del primer compás hay una sola nota, de la mano izquierda, con el dedo 4 '
                 'escrito. La derecha entra después.'),
                ('UNA LIGADURA LARGA', 'Se aguanta',
                 'La primera nota de la melodía pasa de un compás al siguiente sin volver a tocar. '
                 'Se toca una vez y se deja sonar.'),
            ],
            pie='Es la pieza que se guarda para el final del curso, y es la que se lleva a la '
                'audición. No por difícil de dedos: por bonita.',
        ),
        ritmos=[
            ('MANO IZQUIERDA', 'la negra del principio · con silencios delante',
             [sil('h'), n('G2')], AZUL, 'bass', None),
            ('MANO DERECHA', 'una nota que dura el compás entero · literal',
             [n('G4', 'h.')], OCRE, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: no hay teclas negras fijas.',
            'Compás de 3/4 y "mp": suave.',
            'Empieza la mano izquierda, con una sola negra antes del primer compás.',
            'La primera nota de la melodía dura el compás entero.',
            'Esa nota está ligada al compás siguiente: se toca una vez y se aguanta.',
            'La izquierda calla dos compases después de la nota del principio.',
        ],
        reto='El sonido. Con notas tan largas se oye todo: si una entra más fuerte que la anterior, '
             'la frase se rompe. Es lo contrario de las corcheas de la pieza anterior.',
        truco='Toca las tres primeras notas y escucha solo el final de cada una, cuando ya casi no '
              'suena. Si el sonido se apaga antes de que llegue la siguiente, la frase se corta. '
              'Toca un poco más fuerte solo la primera de cada grupo, y deja que las otras caigan.',
        sabias='Chopin escribió veintiún nocturnos y este es el más conocido de todos. La palabra '
               '"nocturno" la inventó el irlandés John Field: piezas para tocar de noche, con la '
               'mano izquierda haciendo de guitarra.',
        qr=dict(titulo='Escúchala',
                texto='Escúchala entera con los ojos cerrados antes de tocar una sola nota. Esta es '
                      'de las que hay que tener en el oído antes que en las manos.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Pocas notas, así que el trabajo es de sonido. Primero las notas largas solas, después '
              'la entrada de la izquierda y al final las dos.',
        reglas=['ESCÚCHALA ANTES DE TOCARLA', 'LAS NOTAS LARGAS, HASTA EL FINAL',
                'LA PRIMERA DE CADA GRUPO PESA UN POCO MÁS'],
        bloques=[
            dict(num=1, titulo='Notas largas, y escuchar cómo acaban',
                 pista='andamio en Do mayor · lo que se practica es el sonido, no los dedos',
                 sistemas=[
                     dict(cap='a) una nota por compás, aguantada entera · escucha el final de cada '
                              'una antes de tocar la siguiente',
                          events=[n('G4', 'h.'), n('E4', 'h.'), n('F4', 'h.'), n('D4', 'h.')],
                          bars=4),
                     dict(cap='b) y con tres negras detrás · la primera pesa un poco más que las '
                              'otras dos',
                          events=[n('C5', 'h.'), n('B4'), n('A4'), n('G4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Empezar antes del compás, con la izquierda',
                 pista='andamio · la negra suelta del principio es la de tu partitura',
                 sistemas=[
                     dict(cap='a) una negra sola y ya empieza el compás · esa nota no lleva acento',
                          events=[sil('h'), n('G2'), n('C3', 'h.'), n('G2', 'h.')],
                          bars=3, clef='bass'),
                     dict(cap='b) y después la izquierda calla dos compases · la cuenta no se para',
                          events=[n('F2'), sil('h'), sil('q'), sil('h'), sil('q'), n('C3', 'h')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA VA LA ÚLTIMA',
                 texto='No porque tenga notas difíciles: no las tiene. Va la última porque para que '
                       'suene bien hace falta todo lo de las dieciocho anteriores —contar, esperar, '
                       'aguantar una nota entera, entrar antes del compás— y además algo que no se '
                       'puede escribir en una hoja, que es escuchar mientras tocas. Es la pieza para '
                       'la audición de fin de curso.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la melodía por encima y la izquierda muy suave · sin prisa',
                 sistemas=[
                     dict(cap='a) la izquierda entra antes y la derecha aguanta el compás entero',
                          events=[sil('h'), n('G2'), ac(('C3', 'G4'), 'h.'),
                                  ac(('G2', 'E4'), 'h.')],
                          bars=3),
                     dict(cap='b) y con las tres negras de la melodía encima · la izquierda no sube '
                              'de volumen',
                          events=[ac(('F2', 'A4')), n('G4'), n('F4'),
                                  ac(('C3', 'E4'), 'h.')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
