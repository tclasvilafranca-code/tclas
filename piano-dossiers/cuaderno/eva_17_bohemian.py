# -*- coding: utf-8 -*-
"""Bohemian Rhapsody (canción 17 de Eva, nivel avanzado). PIEZA NUEVA:
   no está en el álbum de Dilan. Ver TRANSCRIPCION_E17_BOHEMIAN.md.

   De dónde sale lo que se cita
   ----------------------------
   Esta edición imprime el CIFRADO encima de cada compás y escribe el bajo
   detrás de la barra cuando el acorde va invertido (Cm/B, Cm/Si♭, F/A,
   Fm/A♭, E♭/D, Fm/E♭, Fm/D, E♭/G, B♭/D, F7sus4/C). Con eso, la línea del
   bajo de la pieza entera está impresa en letras y se puede citar sin
   interpretar nada.

   Comprobado a ojo sobre las dos páginas: Si♭ mayor (dos bemoles), ♩=66, 4/4
   con el c. 3 en 5/4 y el penúltimo en 2/4, segno en el último compás de la
   página 1, «Fine» en el primero de la página 2 y «D.S. al Fine» al final.

   NO se citan las alturas de la melodía ni el voicing exacto de la izquierda:
   donde hacen falta notas concretas va rotulado ANDAMIO. El bajo no es
   andamio — lo dice el cifrado.

   Es la última del álbum por una razón que no es la velocidad: es la única
   pieza donde hay que hacer todo a la vez —leer un recorrido que salta,
   contar dos compases irregulares, seguir una armonía llena de alteraciones
   escritas a mano y cambiar de textura al pasar de página—. Ninguna de esas
   cosas es difícil por separado. Juntas, sí.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SIb = 'Sib mayor'
_B = [3300]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='w'):
    return {'pitches': list(ps), 'dur': d}


def sil(d='q'):
    return {'rest': True, 'dur': d}


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


# --- el bajo, que viene IMPRESO en el cifrado -----------------------------
# «Mama»: Cm · Cm/B · Cm/Si b · F/La · Fm/La b  -> Do Si Sib La Lab
BAJO_MAMA = [n('C3', 'w'), n('Bn2', 'w'), n('Bb2', 'w'), n('A2', 'w'), n('Ab2', 'w')]

# el mismo gesto, dos veces mas: Mi b -> Re -> Do  y  Fa -> Mi b -> Re
BAJO_OTRAS = [n('Eb3', 'h'), n('D3', 'h'), n('C3', 'w'),
              n('F2', 'h'), n('Eb3', 'h'), n('D3', 'w')]

CANCION = dict(
    alumno='Eva', num=17, nivel='avanzado', slug='BohemianRhapsody',
    titulo_corto='Bohemian Rhapsody', time_sig=(4, 4), key_sig=SIb,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'bohemian-rhapsody.pdf'),
    yt='https://www.youtube.com/results?search_query=queen+bohemian+rhapsody',

    ficha=dict(
        titulo='Bohemian Rhapsody',
        autor='Queen · Freddie Mercury (1975) · arr. para piano y voz',
        datos=[('Tonalidad', 'Si♭ mayor'), ('Compás', '4/4 · 5/4 · 2/4'), ('Tempo', '♩ = 66'),
               ('Recorrido', 'Segno · Fine · D.S.'), ('Páginas', 'dos')],
        armonia=dict(
            titulo='Un bajo que baja medio tono cada vez',
            tarjetas=[
                ('EL DESCENSO', 'Do · Si · Si♭ · La · La♭',
                 'Cm · Cm/B · Cm/Si♭ · F/La · Fm/La♭. Eso es la sección de “Mama”, y es una línea.'),
                ('VUELVE DOS VECES', 'Y dos veces más',
                 'El mismo gesto, más corto. Cuando lo reconozcas, media pieza deja de ser nueva.'),
                ('LOS CC. 10–11', 'Do♭ · Si♭ · La · Si♭',
                 'Cuatro acordes en un compás, uno por tiempo: vecinos del Si♭ por arriba y por abajo.'),
                ('TRES COMPASES RAROS', '5/4 y 2/4',
                 'El c. 3 tiene cinco tiempos y el penúltimo, dos. Están señalados: hay que contarlos.'),
            ],
            pie='La fama de esta canción asusta, pero la parte que tocas tú no es rápida ni tiene '
                'pasajes de virtuosismo: va a ♩=66. Lo que la pone la última del álbum es que hay que '
                'hacer varias cosas a la vez, y ninguna se puede improvisar sobre la marcha.',
        ),
        ritmos=[
            ('MI · el bajo', 'una nota por compás, bajando medio tono cada vez',
             [n('C3', 'w')], OCRE, 'bass', SIb),
            ('MI · página 2', 'la misma armonía, en corcheas (andamio)',
             corch(['Bb2', 'D3', 'F3', 'Bb3']) + corch(['F3', 'D3', 'Bb2', 'D3']), OCRE, 'bass', SIb),
        ],
        especial=[
            'Armadura de dos bemoles: Si y Mi son ♭. Estamos en Si♭ mayor.',
            'El cifrado va impreso encima de cada compás, con el bajo de las inversiones.',
            'El c. 3 está en 5/4 y el penúltimo en 2/4: los dos vienen señalados.',
            'Hay acordes disminuidos escritos: Do♯dim y Fa♯dim.',
            'Al final pone “D.S. al Fine”: se vuelve al segno y se acaba en el “Fine”.',
            'La izquierda cambia de textura entera al pasar a la página 2.',
            'La letra va debajo del pentagrama, sílaba a sílaba.',
        ],
        reto='Hacer varias cosas a la vez y ninguna de oído: contar dos compases irregulares, seguir un '
             'recorrido que salta, leer alteraciones escritas a mano en casi todos los compases y '
             'cambiar de textura al pasar de página. Por separado, nada de eso es difícil.',
        truco='Empieza por el bajo, que es donde está la canción: Do · Si · Si♭ · La · La♭. Tócalo solo, '
              'una nota por compás, y verás que no es una lista de acordes raros sino una línea que baja '
              'medio tono cada vez. Con eso en el oído, las alteraciones dejan de ser sorpresas.',
        sabias='Dura casi seis minutos, no tiene estribillo repetido y mezcla balada, ópera y rock en la '
               'misma canción. La discográfica se negó a publicarla como single por larga; Freddie '
               'Mercury le pasó una copia a un locutor de radio, que la puso catorce veces en dos días.',
        qr=dict(titulo='Escucha la original',
                texto='Escucha solo el bajo del piano en la primera parte. Baja, y no para de bajar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='El cifrado viene impreso encima de cada compás, y con el bajo escrito cuando el acorde va '
              'invertido. Eso quiere decir que la línea del bajo entera te la dan hecha, y esa línea es '
              'la canción: baja medio tono cada vez. Empieza por ahí y todo lo demás deja de parecer '
              'raro.',
        reglas=['EL BAJO ESTÁ EN EL CIFRADO', 'UNA NOTA POR COMPÁS, PARA EMPEZAR', '♩ = 66, NI UNO MÁS'],
        bloques=[
            dict(num=1, titulo='El bajo que baja, que es toda la canción', clef='bass',
                 pista='cifrado medido · Cm · Cm/B · Cm/Si♭ · F/La · Fm/La♭ · una nota por compás',
                 sistemas=[
                     dict(cap='a) solo el bajo · Do · Si · Si♭ · La · La♭: cinco notas, y cada una '
                              'medio tono más abajo que la anterior',
                          events=BAJO_MAMA, bars=5, clef='bass'),
                     dict(cap='b) y los otros dos sitios donde vuelve a pasar lo mismo · Mi♭ · Re · Do, '
                              'y después Fa · Mi♭ · Re: el mismo gesto, más corto',
                          events=BAJO_OTRAS, bars=4, clef='bass', show_time=False),
                     dict(cap='c) y ahora con el acorde encima (andamio: el voicing exacto míralo en la '
                              'partitura) · el bajo sigue siendo el mismo de la a)',
                          events=[ac(['C3', 'Eb3', 'G3']), ac(['Bn2', 'Eb3', 'G3']),
                                  ac(['Bb2', 'Eb3', 'G3']), ac(['A2', 'C3', 'F3']),
                                  ac(['Ab2', 'C3', 'F3'])],
                          cresc=4,
                          bars=5, clef='bass', show_time=False),
                     dict(cap='d) y los cc. 10–11, que son el otro cromatismo · Do♭ · Si♭ · La · Si♭, '
                              'cuatro acordes en un compás: los vecinos del Si♭ por arriba y por abajo',
                          events=[n('Cb3'), n('Bb2'), n('A2'), n('Bb2'),
                                  n('Cb3'), n('Bb2'), n('A2'), n('Bb2'),
                                  n('Bb2', 'w')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTE BAJO ES LA PIEZA ENTERA',
                 texto='Mira las barras del cifrado: Cm/B quiere decir acorde de Do menor con SI en el '
                       'bajo, y Cm/Si♭, con Si♭. No son adornos ni rarezas del arreglista: son la manera '
                       'de escribir que la nota de abajo va bajando medio tono mientras el acorde de '
                       'arriba casi no se mueve. Toca solo esa línea diez veces y te vas a dar cuenta de '
                       'que ya reconoces la canción. A partir de ahí, las alteraciones escritas a mano '
                       'dejan de ser sorpresas: son las notas que hacen falta para que el bajo baje.'),
            dict(num=2, titulo='Los tres compases que no son de cuatro', clef='bass',
                 pista='el c. 3 va en 5/4 y el penúltimo en 2/4 · están señalados, pero hay que contarlos',
                 sistemas=[
                     dict(cap='a) el c. 3, con CINCO tiempos · cuenta uno-dos-tres-cuatro-cinco en voz '
                              'alta, y el acorde es Fa7 todo el compás',
                          events=[ac(['F2', 'A2', 'Eb3'], 'w'), ac(['F2', 'A2', 'Eb3'], 'q')],
                          bars=1, clef='bass', time_sig=(5, 4)),
                     dict(cap='b) y el penúltimo, con DOS · aquí lo fácil es meter un tiempo de más por '
                              'costumbre y llegar tarde al final',
                          events=[ac(['F#2', 'A2', 'C3'], 'h'), ac(['F2', 'Ab2', 'C3'], 'h')],
                          bars=2, clef='bass', time_sig=(2, 4)),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='Queda lo que hace que esta pieza esté la última del álbum: que la izquierda cambie de '
              'ropa al pasar de página y que la hoja no se lea de arriba abajo. Las dos cosas se '
              'resuelven antes de tocar, no tocando.',
        reglas=['ES LA MISMA ARMONÍA CON OTRA ROPA', 'EL RECORRIDO, CON LÁPIZ', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='Dos izquierdas para la misma armonía', clef='bass',
                 pista='andamio sobre el cifrado medido · página 1 en bloques, página 2 en corcheas',
                 sistemas=[
                     dict(cap='a) así suena en la página 1 · el acorde entero de una vez, y se deja '
                              'sonar: la mano no se mueve dentro del compás',
                          events=[ac(['Bb2', 'D3', 'F3']), ac(['C3', 'En3', 'Bb3']),
                                  ac(['Bb2', 'D3', 'F3']), ac(['G2', 'Bb2', 'D3'])],
                          bars=4, clef='bass'),
                     dict(cap='b) y así en la página 2 · las mismas notas del acorde, pero una detrás '
                              'de otra y sin parar: es la misma armonía con otra ropa',
                          events=corch(['Bb2', 'F3', 'Bb3', 'D4']) + corch(['Bb3', 'F3', 'D3', 'F3']) +
                                 corch(['G2', 'D3', 'G3', 'Bb3']) + corch(['G3', 'D3', 'Bb2', 'D3']),
                          bars=2, clef='bass', show_time=False),
                     dict(cap='c) y el truco para leer la página 2: el acorde en bloque de cada compás '
                              'ANTES de leer las corcheas · Si♭ · Sol m · Do m · Fa',
                          events=[ac(['Bb2', 'D3', 'F3']), ac(['G2', 'Bb2', 'D3']),
                                  ac(['C3', 'Eb3', 'G3']), ac(['F2', 'A2', 'C3'])],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA IZQUIERDA CAMBIA ENTERA AL PASAR DE PÁGINA',
                 texto='En la página 1 la izquierda toca acordes en bloque y se está quieta. En la '
                       'página 2 esos mismos acordes se rompen en corcheas que no paran, y de repente '
                       'parece otra pieza. No lo es: son las mismas notas. Si te aprendes primero el '
                       'acorde en bloque de cada compás de la página 2, lo que estás leyendo deja de '
                       'ser una nube de corcheas y pasa a ser un acorde que ya conoces, escrito de otra '
                       'manera. Ese es el atajo, y funciona en toda la página.'),
            dict(num=4, titulo='El recorrido: segno, Fine y D.S.',
                 pista='sin piano y con lápiz · esta hoja no se lee de arriba abajo',
                 sistemas=[]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE HACE EL PASO 4',
                 texto='Busca tres marcas antes de tocar nada. El SEGNO (𝄋) está en el último compás de '
                       'la página 1. La palabra FINE está encima del primer compás de la página 2. Y '
                       '“D.S. al Fine” está al final del todo. Se toca seguido hasta el final, y ahí se '
                       'vuelve al segno y se acaba en el Fine. Sigue ese camino con el dedo y dilo en '
                       'voz alta dos veces; después márcalo con flechas a lápiz. Y ojo con el compás de '
                       '2/4 justo antes del D.S.: cuenta los dos tiempos, porque el sitio donde más se '
                       'falla no es una nota, es un compás de más.'),
            dict(tipo='escalera', valores=[40, 46, 52, 58, 62, 66],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
