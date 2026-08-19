# -*- coding: utf-8 -*-
"""Largo, de la Sinfonía del Nuevo Mundo — pieza 18 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Largo-Sinfonía nº5
   Op. 95 — Sinfonía del nuevo mundo", A. Dvorák, arr. A. C. Escobés,
   1 página), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4, y arriba pone "Largo" y "p".
     - La derecha hace negra con puntillo, corchea y una nota larga ligada al
       compás siguiente.
     - La izquierda sostiene notas muy largas, ligadas de un compás al otro.
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
    alumno='Mercè', carpeta='Merce', num=18, nivel='intermedio', slug='LargoDvorak',
    formato='adulto',
    titulo_corto='Largo · Sinfonía del Nuevo Mundo', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source',
                           '-Largo-Sinfonia 5 Dvorak.pdf'),
    yt='https://www.youtube.com/results?search_query=dvorak+largo+new+world+symphony+piano',

    ficha=dict(
        titulo='Largo · Sinfonía del Nuevo Mundo',
        autor='Antonín Dvořák · arr. A. C. Escobés',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Largo · p'), ('Izquierda', 'Notas ligadas'),
               ('Derecha', 'Largo-corto')],
        titulo_ritmos='Notas que cruzan de un compás a otro',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la derecha respira en '
                   'largo-corto y la izquierda sostiene notas que se ligan al compás siguiente.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('NOTAS LIGADAS', 'De un compás a otro',
                 'La izquierda sostiene una nota tan larga que cruza la barra de compás: se toca '
                 'una vez y sigue sonando en el compás de al lado.'),
                ('LARGO Y p', 'Muy despacio y suave',
                 'Es la marca más lenta y más callada que has visto en tu cuaderno. La tentación es '
                 'ir más rápido de lo que pide el "Largo".'),
                ('LARGO-CORTO', 'En la melodía',
                 'La derecha respira con negra con puntillo, corchea, y una nota que también se '
                 'liga hacia el compás siguiente.'),
                ('MELODÍA FAMOSA', 'De cine y de anuncios',
                 'Es una de las melodías clásicas más usadas fuera de la sala de conciertos, aunque '
                 'poca gente sepa de dónde viene.'),
            ],
            pie='Es el tema del segundo movimiento de la sinfonía, escrito para el corno inglés. '
                'Se hizo tan popular que hoy circula como canción independiente con letra propia.',
        ),
        ritmos=[
            ('MANO DERECHA', 'largo-corto y una nota que liga · literal',
             [n('E4', 'q.'), n('D4', 'e'), n('C4', 'h')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una nota que cruza el compás · literal',
             [n('C3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4, con "Largo" y "p" escritos arriba.',
            'La izquierda sostiene notas que se ligan de un compás al siguiente.',
            'La derecha hace negra con puntillo, corchea, y una nota que también se liga.',
            'Es la marca de tempo más lenta que has tocado hasta ahora.',
            'Es una melodía muy conocida fuera de las salas de concierto.',
        ],
        reto='Que las notas ligadas no se corten ni se repitan por accidente. Al ser tan largas y '
             'tan lentas, la tentación es tocar de nuevo la nota a mitad de su duración.',
        truco='Toca solo la nota ligada y cuenta en voz alta todos los tiempos que dura, sin soltar '
              'la tecla ni volver a pulsarla, hasta que llegues al tiempo exacto en que cambia. '
              'Repite hasta que la duración salga siempre igual.',
        sabias='Dvořák compuso la sinfonía en 1893 durante su estancia en Nueva York, y este tema se '
               'convirtió después en la canción "Goin\' Home", con letra añadida por un alumno suyo.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la versión orquestal con el corno inglés. Fíjate en lo larga que '
                      'suena cada frase antes de respirar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí lo difícil no son las notas: es sostenerlas el tiempo exacto sin cortarlas ni '
              'repetirlas. Se practica muy despacio, contando en voz alta.',
        reglas=['LAS NOTAS LIGADAS NO SE REPITEN', 'LARGO ES MUY DESPACIO, NO SOLO LENTO',
                'CUENTA EN VOZ ALTA MIENTRAS SOSTIENES'],
        bloques=[
            dict(num=1, titulo='La izquierda: sostener a través del compás',
                 pista='andamio en Do mayor · el reparto es el de tu partitura',
                 sistemas=[
                     dict(cap='a) una nota que dura dos compases enteros',
                          events=[n('C3', 'w'), n('C3', 'w')],
                          ligar=True,
                          bars=2, clef='bass'),
                     dict(cap='b) y cambiando de nota, con la misma sujeción',
                          events=[n('F2', 'w'), n('F2', 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: largo-corto y una nota que liga',
                 pista='andamio · cuenta "UUUN, y-dos" y sostén la última nota',
                 sistemas=[
                     dict(cap='a) el dibujo de la pieza, con la nota final ligada al compás siguiente',
                          events=[n('E4', 'q.'), n('D4', 'e'), n('C4', 'h'), n('C4', 'w')],
                          bars=2),
                     dict(cap='b) el mismo dibujo, una frase más arriba',
                          events=[n('G4', 'q.'), n('F4', 'e'), n('E4', 'h'), n('E4', 'w')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE ESCRIBE UNA NOTA QUE CRUZA EL COMPÁS',
                 texto='Cuando una nota dura más que el resto del compás, se escribe partida en dos '
                       'trozos —uno en cada compás— y se unen con una ligadura, una curva por '
                       'encima. Se toca una sola vez, al principio del primer trozo, y se sostiene '
                       'hasta el final del segundo sin volver a pulsarla.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda sostiene mientras la derecha respira · muy despacio',
                 sistemas=[
                     dict(cap='a) la nota larga de la izquierda no se mueve en dos compases',
                          events=[ac(('C3', 'E4'), 'q.'), n('D4', 'e'), ac(('C3', 'C4'), 'h'),
                                  ac(('C3', 'C4'), 'w')],
                          bars=2),
                     dict(cap='b) y con la frase que sube',
                          events=[ac(('F2', 'G4'), 'q.'), n('F4', 'e'), ac(('F2', 'E4'), 'h'),
                                  ac(('F2', 'E4'), 'w')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
