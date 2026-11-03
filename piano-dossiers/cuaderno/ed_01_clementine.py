# -*- coding: utf-8 -*-
"""Clementine (…OR: Found a Peanut) — pieza 1 de Eduard. Formato ADULTO.

   Medido sobre el PDF de SU carpeta (arr. Gilbert DeBenedetti, **Primer
   Level**, Gradimi.com, 1 pagina):

     - 3/4 y detras de la clave no hay nada: todo teclas blancas.
     - UN SOLO PENTAGRAMA, en clave de sol. La izquierda no toca. Es la unica
       manera decente de empezar con un adulto: una cosa cada vez.
     - Empieza con ANACRUSA: dos corcheas antes del primer compas, las dos en
       el mismo Do. Es la primera cosa que hay que explicarle, porque si
       cuenta desde la primera nota le sobra un tiempo todo el rato.
     - La melodia del principio, medida a 300 ppp:

         anacrusa   Do4 · Do4              dos corcheas
         c. 1       Do4 · Mi4 · Mi4        blanca y dos corcheas
         c. 2       Mi4 · Do4 · Do4 · Mi4

     - La digitacion viene impresa (se ven el 1 y el 3 encima del pentagrama).
     - Lleva DOS letras: la de Clementine y la de "Found a Peanut", que es la
       misma musica con una letra de broma. Arriba pone "Tongue in cheek".

   POR QUE EL RITMO DEL c. 1 SE AFIRMA SIN VERLO DEL TODO. Este PDF lleva
   dentro una foto de 72 ppi, y a esa resolucion el agujero de una blanca
   desaparece: la cabeza sale rellena y parece una negra. Pero la aritmetica no
   deja escapatoria: la anacrusa vale un tiempo, el compas es de tres, y detras
   de esa nota solo hay dos corcheas. Negra + corchea + corchea son DOS
   tiempos; blanca + corchea + corchea son TRES. Es una blanca. *Cuando una
   figura no cuadre a la vista, sumala.*
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, sil, corch, plan, metronomo, objetivo, nombres,
                      contar, escribir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# La anacrusa y el primer compas, medidos. Cita literal.
#
# Delante va un SILENCIO DE BLANCA que no esta en la partitura, y esta puesto a
# proposito: es el compas que no suena. Dibujarlo entero —dos tiempos callados y
# la anacrusa en el tercero— es la unica forma de que se vea de un golpe por que
# hay que contar un compas antes de entrar. Ademas hace que la fila sume dos
# compases justos, que es lo que pide el auditor de compases.
ARRANQUE = ([sil('h')] + corch(['C4', 'C4']) +
            [n('C4', 'h'), n('E4', 'e'), n('E4', 'e')])

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=1, nivel='iniciación',
    slug='Clementine', formato='adulto',
    titulo_corto='Clementine', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Clementine.pdf'),
    yt='https://www.youtube.com/results?search_query=oh+my+darling+clementine+piano',

    ficha=dict(
        titulo='Clementine',
        autor='canción popular · arreglo de Gilbert DeBenedetti · Primer Level',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Manos', 'Solo la derecha'), ('Carácter', 'Tongue in cheek'),
               ('Dedos', 'Escritos')],
        titulo_ritmos='Así empieza',
        pie_ritmos='La anacrusa y el primer compás, medidos en tu partitura. Las dos primeras '
                   'notas van ANTES del primer compás.',
        armonia=dict(
            titulo='Una sola mano, y cinco teclas',
            tarjetas=[
                ('UN PENTAGRAMA', 'Solo la derecha',
                 'Esta pieza no tiene pentagrama de abajo. La izquierda descansa el curso entero: '
                 'aquí solo se aprende a leer y a contar.'),
                ('LA ANACRUSA', 'Dos notas antes',
                 'La música empieza antes del primer compás. Esas dos notas de delante no son el '
                 'primer tiempo: son lo que sobra del compás anterior.'),
                ('EL COMPÁS', 'Tres golpes',
                 'Un-dos-tres, un-dos-tres. El peso va siempre en el UNO y los otros dos '
                 'acompañan.'),
                ('LAS TECLAS', 'Todas blancas',
                 'Detrás de la clave no hay nada, así que no hay ni un sostenido ni un bemol en '
                 'toda la pieza.'),
            ],
            pie='La melodía entera se mueve entre el Do y el Mi de la mano derecha. La mano se '
                'coloca una vez, al principio, y ya no hay que buscar ninguna tecla más.',
        ),
        ritmos=[
            ('LA DERECHA', 'el compás que no suena, y la entrada · medido',
             ARRANQUE, OCRE, 'treble', None),
            ('Y SIGUE ASÍ', 'el compás 2, medido · las mismas teclas',
             [n('E4'), n('C4'), n('C4')], AZUL, 'treble', None),
        ],
        especial=[
            'Un solo pentagrama: la mano izquierda no toca en toda la pieza.',
            'Empieza con dos notas antes del primer compás.',
            'Compás de 3/4: tres golpes, y el primero es el fuerte.',
            'No hay ni un sostenido ni un bemol.',
            'La digitación viene impresa encima del pentagrama.',
            'Trae dos letras: la de Clementine y una de broma sobre un cacahuete.',
        ],
        reto='Entrar a tiempo. Con anacrusa la tentación es empezar a contar en la primera nota, y '
             'entonces toda la pieza va corrida un tiempo y no encaja con nadie.',
        truco='Cuenta un compás entero en voz alta antes de tocar —"un, dos, tres"— y entra en el '
              'TRES. Esas dos notas de la anacrusa son el tres de un compás que no suena.',
        sabias='La letra original es de 1884 y va de la hija de un buscador de oro. La de "Found a '
               'Peanut" se la inventaron los niños americanos para cantarla en los viajes largos: '
               'la misma música, y por eso arriba pone "tongue in cheek", con guasa.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta un-dos-tres con el pie mientras suena, y fíjate en que la voz entra '
                      'antes del primer golpe.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí no hay nada difícil de dedos: lo difícil es CONTAR. Se trabaja primero la '
              'cuenta, después las notas, y solo al final las dos cosas juntas.',
        reglas=['LA MANO NO CAMBIA DE SITIO', 'CUENTA UN-DOS-TRES EN VOZ ALTA',
                'ENTRAS EN EL TRES, NO EN EL UNO'],
        bloques=[
            dict(num=1, titulo='Contar tres, sin tocar nada difícil',
                 pista='andamio en Do mayor · la mano quieta, y la cuenta en voz alta',
                 sistemas=[
                     dict(cap='a) una nota en cada golpe · di "un-dos-tres" mientras tocas',
                          events=[n('C4'), n('D4'), n('E4'), n('D4'), n('C4'), n('D4')],
                          bars=2),
                     dict(cap='b) y ahora la primera dura los tres · la mano no se mueve',
                          events=[n('C4', 'h.'), n('D4', 'h.')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UNA ANACRUSA',
                 texto='Hay piezas que no empiezan en el primer golpe del compás, sino antes: una '
                       'o dos notas sueltas que hacen de impulso, como cuando coges aire antes de '
                       'hablar. Se llama anacrusa. Lo importante es que esas notas NO son el uno '
                       'del compás; son el final de un compás que no llegó a sonar. Por eso, para '
                       'entrar bien, hay que contar un compás entero antes de tocar.'),
            dict(num=2, titulo='La anacrusa y el compás 1',
                 pista='cc. 1–2 · medidos en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) los dos tiempos callados y la entrada · no toques hasta el tres',
                          events=[sil('h')] + corch(['C4', 'C4']) + [n('C4', 'h.')],
                          bars=2),
                     dict(cap='b) y el compás 1 solo, que es donde de verdad empieza la cuenta',
                          events=[n('C4', 'h'), n('E4', 'e'), n('E4', 'e'),
                                  n('E4'), n('C4'), n('C4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Las cinco teclas de la pieza',
                 pista='andamio en Do mayor · sin mirar el teclado',
                 sistemas=[
                     dict(cap='a) sube y baja despacio, diciendo el nombre de cada una',
                          events=[n('C4'), n('D4'), n('E4'), n('F4'), n('E4'), n('D4')],
                          bars=2),
                     dict(cap='b) y saltando de Do a Mi, que es el salto de esta canción',
                          events=[n('C4'), n('E4'), n('C4'), n('E4'), n('D4'), n('C4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Clementine · para casa',
            intro='Quince minutos al día, y once de ellos contando. Las notas de esta pieza las '
                  'tienes en una semana; la cuenta es lo que hay que asentar.',
            bloques=[
                plan((4, 'Contar "un-dos-tres" en voz alta, con el pie, sin tocar'),
                     (4, 'La anacrusa sola: contar un compás y entrar en el tres'),
                     (4, 'Los cuatro primeros compases, muy despacio'),
                     (3, 'La pieza entera de principio a fin, aunque salga lenta')),
                metronomo('Empieza a ♩ = 60, que es un golpe por segundo.',
                          'Sube de cinco en cinco solo cuando salga entera sin pararte.'),
                objetivo('Entrar en el sitio. Si al final de la semana entras bien tres veces '
                         'seguidas, esta pieza está hecha.'),
                contar([n('C4'), n('C4'), n('C4'), n('E4'), n('E4'), n('E4'), n('C4')],
                       ['¿Cuántos Do hay?', '¿Cuántos Mi hay?', '¿Cuántas notas en total?'],
                       titulo='Cuenta lo que ves',
                       pista='son las notas del principio de tu partitura'),
                nombres(['C4', 'D4', 'E4', 'C4', 'E4', 'D4', 'C4'],
                        titulo='Los nombres, sin mirar la partitura',
                        pista='escríbelos debajo de cada nota'),
                escribir(titulo='Copia aquí la anacrusa y el compás 1',
                         pista='cópialos tal cual y luego tócalos cinco veces seguidas'),
                para_clase('La pieza entera y, sobre todo, la entrada. Si hay algún sitio donde '
                           'siempre te pierdes la cuenta, tráelo marcado con lápiz.'),
            ],
        ),
    ],
)

# El andamio de apoyo que llena la hoja al piano: escala y acorde de Do mayor,
# que es la tonalidad de la pieza. Nada que no sea de su escalón.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 61, 'C4', 'C3',
    'la mano en Do, que es donde vive toda la pieza',
    desde=4, time_sig=(3, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
