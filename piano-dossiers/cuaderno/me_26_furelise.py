# -*- coding: utf-8 -*-
"""Für Elise, de Beethoven (edición real) — pieza 26 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Fur Elise", Beethoven,
   1 página), leído a 230 dpi. Es la edición REAL de la pieza, no una versión
   fácil, y con diferencia la más exigente de toda tu carpeta:

     - Detrás de la clave NO HAY NADA: La menor, con sostenidos y becuadros
       escritos delante de la nota.
     - 3/4.
     - El famoso arranque va en semicorcheas (más rápidas que cualquier figura
       de tu cuaderno), con el dibujo Mi-Re#-Mi-Re#-Mi-Si-Re-Do-La.
     - La izquierda, cuando entra, toca acordes arpegiados que a veces suben
       por encima de donde está la melodía.

   Nuestro motor de hojas no dibuja semicorcheas, así que aquí no se trabaja
   la pieza entera: se trabaja SOLO el arranque, reducido a corcheas, para
   que la mano aprenda el dibujo antes de llevarlo a la velocidad y a la
   figura real de la partitura, con ayuda de la profesora en clase.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from me_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=26, nivel='intermedio', slug='FurElise',
    formato='adulto',
    titulo_corto='Für Elise', time_sig=(3, 4), key_sig='La menor',
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'Para Elisa.pdf'),
    yt='https://www.youtube.com/results?search_query=fur+elise+beethoven+piano',

    ficha=dict(
        titulo='Für Elise',
        autor='Ludwig van Beethoven · hacia 1810 · edición real, sin simplificar',
        datos=[('Tonalidad', 'La menor'), ('Compás', '3/4'),
               ('Figuras', 'Semicorcheas'), ('Izquierda', 'Arpegios'),
               ('Hoy trabajas', 'Solo el arranque')],
        titulo_ritmos='El arranque, reducido para empezar',
        pie_ritmos='Andamio en La menor. El dibujo real de la pieza va en semicorcheas; aquí se '
                   'trabaja el mismo dibujo en corcheas, más despacio, como primer paso.',
        armonia=dict(
            titulo='Por qué esta es la más exigente',
            tarjetas=[
                ('LA PIEZA REAL', 'No una versión fácil',
                 'A diferencia de casi todo tu cuaderno, esta es la edición íntegra: figuras más '
                 'rápidas, saltos de octava y arpegios en la izquierda.'),
                ('SEMICORCHEAS', 'Muy rápidas',
                 'El arranque famoso va en notas cuatro veces más cortas que una negra. Hoy se '
                 'trabaja el mismo dibujo, pero en corcheas, para aprenderlo antes de acelerarlo.'),
                ('LA IZQUIERDA SUBE', 'Sobre la melodía',
                 'En algunos compases, los arpegios de la izquierda suben más alto que donde está '
                 'la mano derecha en ese momento.'),
                ('OBJETIVO A LARGO PLAZO', 'No para esta semana',
                 'Esta pieza se trabaja poco a poco durante varias semanas, con ayuda de la '
                 'profesora en clase para las partes que aquí no se cubren.'),
            ],
            pie='Es la pieza de piano más conocida del mundo, y Beethoven no llegó a publicarla: se '
                'encontró entre sus papeles cuarenta años después de su muerte.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el dibujo del arranque, en corcheas · andamio',
             corch(['E4', 'D#4', 'E4', 'D#4', 'E4', 'D5']), OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'un acorde grave, cuando entra · andamio',
             [ac(('D2', 'A2'), 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada; los sostenidos y becuadros van escritos dentro.',
            'La tonalidad es La menor.',
            'Compás de 3/4.',
            'El arranque real va en semicorcheas; hoy se trabaja el mismo dibujo en corcheas.',
            'La izquierda, cuando entra, toca acordes arpegiados.',
            'Es un objetivo a varias semanas, no una pieza para dominar en una sola.',
        ],
        reto='Aprender el dibujo de notas del arranque sin la velocidad real todavía. Ir rápido '
             'demasiado pronto es lo que hace que esta pieza salga mal para siempre.',
        truco='Toca el dibujo del arranque en corcheas, muy despacio, tantas veces como haga falta '
              'hasta que la mano lo recuerde sin mirar. Solo entonces, y con ayuda en clase, se '
              'empieza a acercar a la velocidad y a las semicorcheas reales.',
        sabias='Nadie sabe con certeza quién era "Elise": una teoría dice que el copista leyó mal '
               'el título y que en realidad decía "Therese", una alumna de Beethoven a la que '
               'pidió matrimonio y que rechazó la propuesta.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el arranque muchas veces antes de tocarlo. Tenerlo en el oído es '
                      'tan importante aquí como tenerlo en los dedos.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Solo se trabaja el arranque, y en una versión reducida a corcheas. El objetivo de '
              'hoy es el dibujo de notas, no la velocidad.',
        reglas=['SOLO EL DIBUJO, TODAVÍA SIN VELOCIDAD', 'DOS DEDOS QUE SE TURNAN, MANO QUIETA',
                'ES UN OBJETIVO DE VARIAS SEMANAS'],
        bloques=[
            dict(num=1, titulo='El dibujo del arranque, en corcheas',
                 pista='andamio en La menor · el mismo dibujo, más despacio que en la partitura real',
                 sistemas=[
                     dict(cap='a) ida y vuelta entre dos teclas vecinas',
                          events=corch(['E4', 'D#4', 'E4', 'D#4', 'E4', 'B4']),
                          bars=1),
                     dict(cap='b) y con el becuadro, que quita el sostenido',
                          events=corch(['E4', 'Dn4', 'E4', 'Dn4', 'E4', 'B4']),
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: el primer acorde arpegiado',
                 pista='andamio · cuando entra, sube hacia donde está la melodía',
                 sistemas=[
                     dict(cap='a) el acorde grave, sostenido',
                          events=[ac(('A2', 'E3'), 'h.')],
                          bars=1, clef='bass'),
                     dict(cap='b) y el arpegio que sube desde ahí',
                          events=[n('A2'), n('E3'), n('A3')],
                          bars=1, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE EMPIEZA MUY DESPACIO',
                 texto='Esta pieza se ha estropeado más veces por prisa que por dificultad real: el '
                       'dibujo del arranque no es complicado de entender, pero exige que la mano '
                       'repita el mismo gesto muchísimas veces sin tensarse. Ir despacio ahora, '
                       'semana tras semana, es lo que permite llegar a la velocidad real sin tener '
                       'que deshacer una mala costumbre después.'),
            dict(num=3, titulo='Las dos juntas, cuando entra la izquierda',
                 pista='andamio · muy despacio, sin buscar la velocidad todavía',
                 sistemas=[
                     dict(cap='a) el arranque de la derecha, sola',
                          events=corch(['E4', 'D#4', 'E4', 'D#4', 'E4', 'C5']),
                          bars=1),
                     dict(cap='b) y con el acorde de la izquierda entrando debajo',
                          events=[ac(('A2', 'E3', 'E4'), 'e'), n('D#4', 'e'), n('E4', 'e'),
                                  n('D#4', 'e'), n('E4', 'e'), n('C5', 'e')],
                          bars=1, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
