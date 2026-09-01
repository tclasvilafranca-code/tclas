# -*- coding: utf-8 -*-
"""Für Elise, de Beethoven (edición real) — pieza 19 de Isaac.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Fur Elise", Beethoven,
   1 página; el mismo archivo que la pieza 26 de Mercè, byte a byte). Es la
   edición REAL de la pieza, no una versión fácil, y con diferencia la más
   exigente de toda tu carpeta antes del Diabelli:

     - Detrás de la clave NO HAY NADA: La menor, con sostenidos y becuadros
       escritos delante de la nota.
     - 3/4.
     - El famoso arranque va EN CORCHEAS, con el dibujo
       Mi-Re#-Mi-Re#-Mi-Si-Re-Do-La. Esta edicion no es la original en 3/8 con
       semicorcheas: pasa el mismo dibujo a 3/4 y a corcheas.
     - La UNICA semicorchea de toda la pieza esta en el c. 20, como nota corta
       de una figura larga-corta.
     - En el ultimo compas hay notas de adorno (pequenas, sin valor propio).
     - La izquierda, cuando entra, toca acordes arpegiados que a veces suben
       por encima de donde está la melodía.

   CORRECCION IMPORTANTE: esta hoja escribia el arranque en semicorcheas y
   decia que asi estaba impreso. Es FALSO. Se ha vuelto a mirar el PDF entero
   a zoom, compas a compas: todas las barras del arranque son simples, y la
   unica barra doble de la pieza esta en el c. 20. Aqui se escribe lo que la
   partitura trae, y la semicorchea aparece donde de verdad aparece.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from is_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
LAm = 'La menor'

CANCION = dict(
    alumno='Isaac', carpeta='Isaac', num=19, nivel='intermedio', slug='FurElise',
    formato='adulto',
    titulo_corto='Für Elise', time_sig=(3, 4), key_sig=LAm,
    partitura=os.path.join(HERE, '..', 'students', 'isaac', 'source', 'Para Elisa.pdf'),
    yt='https://www.youtube.com/results?search_query=fur+elise+beethoven+piano',

    ficha=dict(
        titulo='Für Elise',
        autor='Ludwig van Beethoven · hacia 1810 · edición real, sin simplificar',
        datos=[('Tonalidad', 'La menor'), ('Compás', '3/4'),
               ('Figuras', 'Corcheas'), ('Izquierda', 'Arpegios'),
               ('Hoy trabajas', 'Solo el arranque')],
        titulo_ritmos='El arranque, tal como está escrito',
        pie_ritmos='Andamio en La menor. El dibujo del arranque va en corcheas en tu edición, y '
                   'así está escrito aquí: es la figura de tu partitura, no una reducción.',
        armonia=dict(
            titulo='Por qué esta es la más exigente antes del Diabelli',
            tarjetas=[
                ('LA PIEZA REAL', 'No una versión fácil',
                 'A diferencia de casi todo tu cuaderno, esta es la edición íntegra: figuras más '
                 'rápidas, saltos de octava y arpegios en la izquierda.'),
                ('TU EDICIÓN, EN CORCHEAS', 'No es la original',
                 'Beethoven la escribió en 3/8 y con semicorcheas. Tu edición pasa el mismo dibujo '
                 'a 3/4 y a corcheas: suena igual y se lee mucho mejor.'),
                ('LA IZQUIERDA SUBE', 'Sobre la melodía',
                 'En algunos compases, los arpegios de la izquierda suben más alto que donde está '
                 'la mano derecha en ese momento.'),
                ('OBJETIVO A LARGO PLAZO', 'No para esta semana',
                 'Esta pieza se trabaja poco a poco durante varias semanas, con ayuda de la '
                 'profesora en clase.'),
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
            'El arranque va en corcheas, y así está escrito en tu partitura.',
            'En el compás 20 hay una semicorchea: es la única de toda la pieza.',
            'La izquierda, cuando entra, toca acordes arpegiados.',
            'Es un objetivo a varias semanas, no una pieza para dominar en una sola.',
        ],
        reto='Aprender el dibujo del arranque sin correr. Esta pieza se ha estropeado más veces '
             'por prisa que por dificultad.',
        truco='Toca el dibujo del arranque muy despacio, tantas veces como haga falta hasta que la '
              'mano lo recuerde sin mirar. La velocidad viene después; el dibujo, no.',
        sabias='Nadie sabe con certeza quién era "Elise": una teoría dice que el copista leyó mal '
               'el título y que en realidad decía "Therese", una alumna de Beethoven.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el arranque muchas veces antes de tocarlo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Solo se trabaja el arranque, que en tu edición va en corcheas. Primero muy '
              'despacio para aprender el dibujo, y solo después buscando el aire de la pieza.',
        reglas=['PRIMERO EL DIBUJO, DESPUÉS LA VELOCIDAD', 'DOS DEDOS QUE SE TURNAN',
                'ES DE VARIAS SEMANAS'],
        bloques=[
            dict(num=1, titulo='El dibujo del arranque, y su única excepción',
                 pista='andamio en La menor · la corchea es la figura que trae tu edición',
                 sistemas=[
                     dict(cap='a) ida y vuelta entre dos teclas vecinas · las seis notas duran '
                              'exactamente lo mismo',
                          events=corch(['E5', 'D#5', 'E5', 'D#5', 'E5', 'B4']),
                          bars=1),
                     dict(cap='b) el mismo dibujo con el becuadro, que quita el sostenido · el '
                              'segundo Re NO es el mismo que el primero',
                          events=corch(['E4', 'D#4', 'E4', 'Dn4', 'E4', 'B3']),
                          bars=1, show_time=False),
                     dict(cap='c) c. 20 · el único sitio de la pieza con una nota más corta: la '
                              'última del grupo lleva una barra más y va pegada a la siguiente',
                          events=[n('B3', 'e'), n('C4', 'e'), n('D4', 'e.'),
                                  n('C4', 's'), n('B3', 'e'), n('A3', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: el primer acorde arpegiado',
                 pista='andamio · cuando entra, sube hacia donde está la melodía',
                 sistemas=[
                     dict(cap='a) el acorde grave, sostenido, con otra combinación',
                          events=[ac(('E2', 'B2'), 'h.')],
                          bars=1, clef='bass'),
                     dict(cap='b) y el arpegio que sube desde ahí',
                          events=[n('E2'), n('B2'), n('E3')],
                          bars=1, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE EMPIEZA MUY DESPACIO',
                 texto='Esta pieza se ha estropeado más veces por prisa que por dificultad real: '
                       'exige que la mano repita el mismo gesto muchísimas veces sin tensarse.'),
            dict(num=3, titulo='Las dos juntas, cuando entra la izquierda',
                 pista='andamio · muy despacio, sin buscar la velocidad todavía',
                 sistemas=[
                     dict(cap='a) el arranque de la derecha, sola · en corcheas, que es su figura',
                          events=corch(['E4', 'D#4', 'E4', 'C5', 'B4', 'A4']),
                          bars=1),
                     dict(cap='b) y con el acorde de la izquierda entrando debajo',
                          events=[ac(('D2', 'A2', 'E4'), 'e'), n('D#4', 'e'), n('E4', 'e'),
                                  n('D#4', 'e'), n('E4', 'e'), n('C5', 'e')],
                          bars=1, show_time=False),
                 ]),
        ] + bloques_extra('La menor', 7, 'A4', 'A2',
                          'las seis notas del grupo duran exactamente lo mismo',
                          desde=4, time_sig=(3, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
