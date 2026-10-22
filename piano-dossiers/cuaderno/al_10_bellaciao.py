# -*- coding: utf-8 -*-
"""Bella Ciao (a cuatro manos) — pieza 10 de Alan (dueto). Formato ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Bella Ciao 4 mains",
   Musescore, 1 página), mirado a 110 y a 300 dpi:

     - **DOS BEMOLES** detrás de la clave (Si♭ y Mi♭, confirmado ampliando a
       300 dpi: el Mi♭ queda por encima de la quinta línea y es fácil perderlo
       en un recorte pequeño). La melodía gira alrededor de Sol: Sol menor.
     - 4/4, sin tempo impreso.
     - Dos sistemas de piano por línea: PIANO 1 (clave de sol arriba, clave de fa
       abajo) y PIANO 2 (igual). La melodía va en el Piano 1, arriba.
     - MEDIDO (`medir_partitura` + lectura a 300 dpi): el c. 1 de la derecha
       del Piano 1 es **Re4 · Sol4 · La4 · Si♭4**, cuatro negras. El c. 2 es una
       blanca con puntillo de Sol y silencio de negra; los cc. 3 y 4 repiten.
     - **El Piano 2 NO hace corcheas**: la derecha toca un acorde de tres notas
       en el uno y otro en el tres, con silencios de negra entre medias, y la
       izquierda un bajo en blancas y negras (Sol y Re). Mirado ampliado.
     - Fa sostenidos escritos delante de la nota, y un becuadro (la sensible
       del tono menor).
     - Barra de repetición al final de la primera vuelta y casilla "2." en la
       segunda.
     - El c. 13 y el c. 17 empiezan igual: Re5 · Do5 · Si♭4 · La4, bajando.

   Mismo archivo que el de Josep y Nel (misma edición): lo literal coincide, lo
   inventado no. Aquí el material de apoyo va por la **repetición con casilla**
   y por el descenso Re-Do-Si♭-La, que es lo que la melodía hace al final de
   cada vuelta.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra, encajar
from al_comun import (n, ac, sil, plan, escalera, a_cuatro_manos, diferencias,
                       nombres, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=10, nivel='intermedio', slug='BellaCiao',
    formato='adulto',
    titulo_corto='Bella Ciao', time_sig=(4, 4), key_sig='Sol menor',
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source', 'Bella-ciao-4 manos'),
    yt='https://www.youtube.com/results?search_query=bella+ciao+piano+4+manos',

    ficha=dict(
        titulo='Bella Ciao',
        autor='Canción popular italiana · versión a cuatro manos · parte del Piano 1',
        datos=[('Tonalidad', 'Sol menor'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Alteración', 'Fa sostenido'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Melodía arriba, acordes abajo',
        pie_ritmos='Arriba, medido sobre tu partitura: el c. 1 son Re, Sol, La y Si bemol, cuatro negras. Abajo, '
                   'andamio: la mano derecha del Piano 2 pone un acorde en el uno y otro en el tres.',
        armonia=dict(
            titulo='Un tono menor y un compañero que no te acompaña igual',
            tarjetas=[
                ('DOS BEMOLES', 'Sol menor',
                 'Si♭ y Mi♭ detrás de la clave. El Mi♭ está por encima de la quinta línea y es '
                 'fácil de olvidar: si te falla una nota, mira primero ahí.'),
                ('LA SENSIBLE', 'Fa♯ con becuadro',
                 'El Fa♯ va escrito delante de la nota y se anula con un becuadro. Es la nota que '
                 'empuja al Sol: sin ella, la pieza sonaría a modo antiguo.'),
                ('EL PIANO 2', 'Uno y tres',
                 'La otra parte toca un acorde de tres notas en el primer y el tercer golpe, con '
                 'silencio de negra entre medias. No son corcheas: son negras que respiran.'),
                ('LA REPETICIÓN', 'Casilla 2',
                 'Una barra de repetición al final de la primera vuelta y una casilla "2." en la '
                 'segunda. Las dos vueltas empiezan igual y acaban distinto.'),
            ],
            pie='Con un compañero que marca el pulso en el uno y el tres, tu parte no puede '
                'esconderse: si una negra se retrasa, se oye en el acorde siguiente. Metrónomo '
                'en casa y paciencia en clase.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido',
             [n('D4'), n('G4'), n('A4'), n('Bb4')],
             OCRE, 'treble', None),
            ('PIANO 2', 'un acorde en el uno y otro en el tres · andamio',
             [ac(('D3', 'G3', 'Bb3')), sil('q'), ac(('D3', 'G3', 'Bb3')), sil('q')],
             AZUL, 'treble', None),
        ],
        especial=[
            'Dos bemoles detrás de la clave: Si bemol y Mi bemol (el segundo, sobre la quinta línea).',
            'La melodía gira alrededor de Sol: es Sol menor, no Si bemol mayor.',
            'Hay Fa sostenidos escritos delante de las notas y un becuadro que los anula.',
            'Compás de 4/4 y ningún número de metrónomo.',
            'El Piano 2 toca acordes de negra en el primer y el tercer golpe.',
            'Hay barra de repetición y casilla de segunda vez.',
        ],
        reto='Aguantar el pulso cuando tu compañero solo toca dos veces por compás. El Piano 2 toca dos veces por compás y '
             'tu melodía tiene que caer entre sus golpes, no encima: si los pisas, se oyen cuatro '
             'notas en el sitio de dos.',
        truco='Estudia la melodía con las palmas del otro piano: tú dices la melodía y golpeas '
              'el uno y el tres con la mano izquierda sobre la mesa. Cuando lo hagas sin pensarlo, '
              'la pieza ya no te sorprende en clase.',
        sabias='La melodía es más antigua que la letra política que la hizo famosa. Se cantaba en los '
               'arrozales del norte de Italia con otra letra; la versión partisana se difundió '
               'después de la Segunda Guerra Mundial.',
        qr=dict(titulo='Escúchala',
                texto='Escucha los dos acordes por compás del acompañamiento y cuenta cuántos '
                      'silencios hay entre ellos: son los que le dan a la melodía el aire para '
                      'respirar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La melodía es corta y sencilla. Lo que se estudia es que el tono menor suene a '
              'menor, que la repetición se tome por el sitio correcto y que las negras caigan '
              'entre los acordes del otro piano.',
        reglas=['EL MI BEMOL NO SE OLVIDA', 'LA MELODÍA CAE ENTRE LOS ACORDES',
                'LA SEGUNDA VUELTA ACABA DISTINTO'],
        bloques=[
            dict(num=1, titulo='Los cuatro primeros compases de la melodía',
                 pista='cc. 1-4 · MEDIDO sobre tu partitura · Re, Sol, La, Si♭ y una blanca con '
                       'puntillo de Sol',
                 sistemas=[
                     dict(cap='a) las cuatro negras suben y la blanca con puntillo se queda · el '
                              'silencio de negra del final es el golpe en que entra el otro piano',
                          events=[n('D4'), n('G4'), n('A4'), n('Bb4'),
                                  n('G4', 'h.'), sil('q'),
                                  n('D4'), n('G4'), n('A4'), n('Bb4'),
                                  n('G4', 'h.'), sil('q')],
                          bars=4, key_sig='Sol menor'),
                 ]),
            dict(num=2, titulo='El descenso del final de cada vuelta',
                 pista='cc. 13 y 17 · leído de tu partitura · Re, Do, Si♭, La, bajando a ritmo de negras',
                 sistemas=[
                     dict(cap='a) el compás tal como está en tu partitura · cuatro negras seguidas '
                              'hacia abajo, sin silencios de por medio',
                          events=[n('D5'), n('C5'), n('Bb4'), n('A4')],
                          bars=1, key_sig='Sol menor'),
                     dict(cap='b) y rematado hacia el Sol, para que el oído oiga a dónde va · '
                              'andamio, el Fa♯ de paso es la sensible',
                          events=[n('A4'), n('Bb4'), n('A4'), n('G4'),
                                  n('F#4'), n('G4', 'h.')],
                          bars=2, key_sig='Sol menor', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL MI BEMOL, UNA VEZ POR LÍNEA',
                 texto='Antes de tocar nada, escribe a lápiz un Mi bemol enorme sobre cada una de '
                       'las cuatro líneas de tu partitura, en el lado izquierdo, donde está la '
                       'armadura. Es una tontería y funciona: lo que falla en una pieza con dos '
                       'bemoles casi nunca es el Si, que está dentro del pentagrama; es el Mi, '
                       'que está encima.'),
            dict(num=3, titulo='La repetición, con la casilla de segunda vez',
                 pista='andamio · primera vuelta con barra de repetición, segunda vuelta con la '
                       'casilla "2."',
                 sistemas=[
                     dict(cap='a) la primera vez acaba así y se vuelve atrás · el compás de la '
                              'casilla no se toca la primera vez',
                          events=[n('A4'), n('Bb4'), n('A4'), n('G4'),
                                  n('A4', 'h'), n('F#4', 'h')],
                          bars=2, key_sig='Sol menor', repetir='cierra'),
                     dict(cap='b) la segunda vez saltas el final de arriba y tocas este · fíjate en '
                              'cómo cambia el último compás',
                          events=[n('G4', 'h'), n('Bb4', 'h'),
                                  n('G4', 'w')],
                          bars=2, key_sig='Sol menor', show_time=False, casilla='2'),
                 ]),
            dict(num=4, titulo='Las dos manos del Piano 1, los dos primeros compases',
                 pista='cc. 1-2 · leído de tu partitura · la izquierda calla un compás y luego '
                       'sostiene un Sol',
                 sistemas=[
                     dict(cap='a) la izquierda entra en el compás 2 con una redonda de Sol y no se '
                              'mueve · si la derecha te arrastra, el bajo se acorta',
                          events=[n('D4'), n('G4'), n('A4'), n('Bb4'),
                                  ac(('G3', 'G4'), 'h.'), sil('q')],
                          bars=2, key_sig='Sol menor', manos='sostiene'),
                 ]),
        ] + bloques_extra('Sol menor', 56, 'G3', 'G2',
                          'dos bemoles, y ninguno se olvida a mitad de camino',
                          desde=5, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Bella Ciao · para casa',
            intro='Veinte minutos, con metrónomo desde el primer día y el compañero a mano para los dos últimos.',
            bloques=[
                plan((4, 'Escribir el Mi bemol en cada línea y tocar la escala de Sol menor'),
                     (6, 'La melodía sola, con metrónomo y sin mirar las teclas'),
                     (5, 'Las palmas del otro piano con la mano izquierda, y la melodía encima'),
                     (5, 'Las dos juntas con el compañero, hasta la barra de repetición')),
                a_cuatro_manos('El Piano 2 toca solo en el uno y en el tres, así que si el pulso '
                               'se te va, te dejas sin guía justo a la mitad del compás. Acordad '
                               'quién cuenta el compás de entrada y a qué velocidad.'),
                escalera((54, 'la melodía sola, sin mirar'),
                         (66, 'las cuatro primeras líneas'),
                         (80, 'la primera vuelta con la repetición'),
                         (92, 'las dos vueltas, con la casilla 2'),
                         meta='La partitura no trae ningún número de metrónomo: la meta la eliges '
                              'tú y se apunta a lápiz.',
                         titulo='La escalera del metrónomo'),
                diferencias([n('D4'), n('G4'), n('A4'), n('Bb4'), n('G4', 'h.'), sil('q')],
                            [n('D4'), n('G4'), n('Bb4'), n('A4'), n('G4', 'h.'), sil('q')],
                            1,
                            titulo='Busca la diferencia en la melodía',
                            pista='el de arriba es tu compás 1 y el 2 · el de abajo ha cambiado una nota'),
                nombres(['Eb5', 'Bb4', 'D5', 'A4', 'F#4', 'G4', 'C5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='estamos en Sol menor: dos bemoles, y la sensible es la quinta'),
                para_clase('La melodía con metrónomo y a qué número la llevas, y si el Mi bemol te '
                           'ha fallado alguna vez. Y una pregunta: cuándo cae el acorde del otro '
                           'piano en tu compás 2.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
