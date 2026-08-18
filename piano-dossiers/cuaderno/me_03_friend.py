# -*- coding: utf-8 -*-
"""You've Got a Friend in Me — pieza 3 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("You've Got A Friend In
   Me - Easy", arr. Megan Harper, 1 página; el mismo archivo que la pieza 4 de
   Luisa, byte a byte), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4.
     - La izquierda hace una redonda por compás, una sola nota que se
       aguanta entera.
     - La derecha se mueve en negras y alguna blanca, con la melodía de la
       canción.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from me_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=3, nivel='intermedio', slug='FriendInMe',
    formato='adulto',
    titulo_corto="You've Got a Friend in Me", time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'Hay un amigo en mi.pdf'),
    yt='https://www.youtube.com/results?search_query=you+got+a+friend+in+me+easy+piano',

    ficha=dict(
        titulo="You've Got a Friend in Me",
        autor='Randy Newman · de Toy Story · arr. Megan Harper',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Izquierda', 'Una redonda'), ('Derecha', 'Negras y blancas'),
               ('Se toca', 'Con base')],
        titulo_ritmos='Una nota que sostiene todo el compás',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la izquierda toca una vez por '
                   'compás y la deja sonar, y la derecha lleva la melodía en negras.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('LA IZQUIERDA SOSTIENE', 'Una nota, un compás',
                 'No hay que tocarla más de una vez por compás. El trabajo es dejarla sonar entera, '
                 'sin repetirla ni cortarla antes de tiempo.'),
                ('LA DERECHA CANTA', 'Negras y blancas',
                 'La melodía es la que todo el mundo reconoce. Las notas largas caen siempre al '
                 'final de una frase.'),
                ('POCOS CAMBIOS DE ACORDE', 'La mano casi no viaja',
                 'La izquierda se queda en la misma zona del teclado durante toda la pieza; solo '
                 'cambia de nota, no de posición.'),
                ('MELODÍA CONOCIDA', 'Se afina sola',
                 'Como la conoces de memoria, el oído te avisa antes que la vista si una nota sale '
                 'mal. Aprovéchalo.'),
            ],
            pie='Es la canción de la amistad de Toy Story, y aquí en su versión más limpia: sin '
                'saltos raros ni ritmos complicados, solo la melodía y su base.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negras, y blanca al cerrar frase · andamio',
             [n('C4'), n('D4'), n('E4'), n('F4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una redonda por compás · literal',
             [n('C3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4.',
            'La izquierda toca una sola nota por compás y la sostiene entera.',
            'La derecha lleva la melodía en negras, con alguna blanca al final de frase.',
            'La izquierda apenas cambia de posición durante toda la pieza.',
            'Es una melodía muy conocida: el oído ayuda a detectar un error antes que la vista.',
        ],
        reto='Aguantar la redonda de la izquierda el compás entero sin acortarla. La tentación es '
             'soltarla en cuanto la derecha se mueve, y tiene que sonar hasta el último tiempo.',
        truco='Toca solo la izquierda y cuenta en voz alta los cuatro tiempos de cada compás sin '
              'soltar la tecla hasta decir "cuatro". Cuando la mano aguante sola sin que te dé '
              'prisa, añade la melodía.',
        sabias='Randy Newman la escribió para la primera película de Toy Story, en 1995, y ha '
               'sonado en las cuatro películas de la saga. Es de las pocas canciones de Pixar que se '
               'canta entera sin coro.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo el bajo, sin la melodía. Vas a notar que casi no se mueve: eso '
                      'es exactamente lo que hace tu mano izquierda.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda no tiene notas difíciles, tiene paciencia: hay que dejarla sonar. Se '
              'estudia sola primero, y solo entonces se junta.',
        reglas=['LA IZQUIERDA SUENA UN COMPÁS ENTERO', 'LA MELODÍA SE CANTA ANTES DE TOCARLA',
                'SIN PRISA: LA CANCIÓN ES TRANQUILA'],
        bloques=[
            dict(num=1, titulo='La izquierda: una redonda, y aguantarla',
                 pista='andamio en Do mayor · el reparto es el de tu partitura',
                 sistemas=[
                     dict(cap='a) una nota por compás, sostenida entera',
                          events=[n('C3', 'w'), n('F2', 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de nota, sin cambiar de zona del teclado',
                          events=[n('G2', 'w'), n('C3', 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: la melodía en negras',
                 pista='andamio · canta la frase antes de tocarla',
                 sistemas=[
                     dict(cap='a) cuatro negras y la blanca que cierra la frase',
                          events=[n('C4'), n('D4'), n('E4'), n('F4'), n('E4', 'h'), n('C4', 'h')],
                          bars=2),
                     dict(cap='b) y la frase siguiente, con el mismo dibujo más arriba',
                          events=[n('E4'), n('F4'), n('G4'), n('A4'), n('G4', 'h'), n('E4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ NO HAY QUE TOCAR LA IZQUIERDA DOS VECES',
                 texto='Repetir la nota de la izquierda a mitad de compás, aunque suene parecido, '
                       'rompe el efecto de fondo continuo que tiene esta canción. La redonda está '
                       'para sostener, no para acompañar el pulso de la melodía: se toca una vez y '
                       'se deja vivir sola hasta el compás siguiente.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda no se mueve mientras la derecha canta · despacio',
                 sistemas=[
                     dict(cap='a) la redonda aguanta todo el compás bajo la melodía',
                          events=[ac(('C3', 'C4')), n('D4'), n('E4'), n('F4'),
                                  ac(('F2', 'E4'), 'h'), n('C4', 'h')],
                          bars=2),
                     dict(cap='b) y con la frase que sube',
                          events=[ac(('G2', 'E4')), n('F4'), n('G4'), n('A4'),
                                  ac(('C3', 'G4'), 'h'), n('E4', 'h')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
