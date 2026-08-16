# -*- coding: utf-8 -*-
"""El Cisne (canción 6 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico); la medición se importa de
   `dilan_01_data`. Ver TRANSCRIPCION_D01_EL_CISNE.md.

   Camino distinto al de Dilan:

     - A Dilan se le entra por la MANO IZQUIERDA, que es el 90 % del trabajo, y
       la melodía llega después.
     - A Eva se le entra por LA ESCALA QUE LA PIEZA LLEVA ESCONDIDA: los cc. 7
       al 9 son una escala de Sol mayor completa, de Mi4 a Sol5, sin un solo
       salto. Empezar por ahí tiene una ventaja que no es de dedos: cuando ves
       que la melodía de una pieza famosa es una escala, dejas de leerla nota a
       nota y empiezas a leerla por gestos, que es como se lee de verdad.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_01_data import corcheas, CELULA_I, CELULA_ii, CELULA_I7, MD_3_4, MD_7_9

HERE = os.path.dirname(__file__)
SOL = 'Sol mayor'
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='h.'):
    return {'pitches': list(ps), 'dur': d}


# la escala de los cc. 7-9 con el ritmo aplanado, para colocar la mano antes
# de ponerle la figuracion: nueve negras y la de arriba larga = 4 compases
ESCALA_LISA = [n(p) for p in ('E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5')] + \
              [n('G5', 'h.')]

# las tres celulas de la izquierda, sin romper: el acorde que hay debajo
AC_I = ['G2', 'D3', 'B3']        # Sol mayor      · cc. 1-4
AC_ii = ['G2', 'E3', 'A3']       # La menor /Sol  · cc. 5-7
AC_I7 = ['G2', 'D3', 'F3']       # Sol maj7       · c.  8

CANCION = dict(
    alumno='Eva', num=6, nivel='avanzado', slug='ElCisne',
    titulo_corto='El Cisne', time_sig=(3, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA', 'the-swan.pdf'),
    yt='https://www.youtube.com/results?search_query=saint-saens+le+cygne+the+swan+cello',

    ficha=dict(
        titulo='El Cisne',
        autor='Camille Saint-Saëns (1886) · rev. Ricardo Boppré',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '3/4'), ('Tempo', 'Andante ♩=96'),
               ('Dinámica', 'pp'), ('Compases', '55')],
        armonia=dict(
            titulo='Una escala escondida dentro de la melodía',
            tarjetas=[
                ('LOS CC. 7–9', 'Mi4 → Sol5',
                 'Una escala de Sol mayor entera, sin un solo salto. Es la frase que todo el mundo reconoce.'),
                ('LA IZQUIERDA', 'Sol · Re · Si · Re',
                 'Un arpegio de tres notas en seis corcheas, y no cambia en 55 compases.'),
                ('LA FORMA', 'A · B · A’',
                 'Los cc. 35 y 36 son idénticos a los cc. 3 y 4 en las dos manos. Comprobado.'),
            ],
            pie='La izquierda no tiene ninguna dificultad técnica. La dificultad es que suene igual '
                'durante 55 compases y por debajo de la melodía.',
        ),
        especial=[
            'La armadura de Sol mayor lleva un sostenido: todos los Fa.',
            'La melodía de los cc. 7 al 9 es la escala de Sol mayor completa.',
            'La izquierda hace seis corcheas por compás, siempre el mismo dibujo.',
            'Está escrita en pp: es la dinámica más floja de todo el cuaderno.',
            'Los cc. 35 y 36 son, nota por nota, los cc. 3 y 4.',
            'La sección de en medio (cc. 13–34) se va de Sol mayor y se llena de alteraciones.',
        ],
        ritmos=[
            ('MI', 'seis corcheas: el arpegio que no para',
             corcheas(CELULA_I), OCRE, 'bass', SOL),
            ('MD', 'una blanca: la melodía va en notas largas',
             [n('B4', 'h.')], AZUL, 'treble', SOL),
        ],
        reto='Que la izquierda suene igual 55 compases seguidos y siempre por debajo de la melodía. '
             'El arpegio tiende a marcar la primera corchea de cada compás, y en cuanto la marcas la '
             'pieza se convierte en un vals.',
        truco='Empieza por la escala de los cc. 7–9. Cuando veas que la melodía de El Cisne es una '
              'escala de Sol mayor, dejas de leerla nota a nota: la lees como un gesto. Y a partir de '
              'ahí la izquierda es solo el fondo.',
        sabias='Saint-Saëns escribió «El Carnaval de los Animales» como una broma privada y prohibió '
               'que se publicara en vida: le parecía que le quitaría seriedad. Hizo una sola excepción '
               'con El Cisne, que es justamente la pieza por la que hoy se le conoce.',
        qr=dict(titulo='Escucha la versión de violonchelo',
                texto='La melodía la toca un chelo. Fíjate en que nunca se apresura.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Esta pieza esconde una escala: los cc. 7 al 9 son la escala de Sol mayor entera, de Mi4 '
              'a Sol5, sin un solo salto. Empezar por ahí no es un capricho — cuando ves que la '
              'melodía es una escala, dejas de leerla nota a nota y la lees como un gesto.',
        reglas=['ARMADURA DE SOL', 'LEE POR GESTOS, NO POR NOTAS', 'ANDANTE ♩=96 ES EL TECHO'],
        bloques=[
            dict(num=1, titulo='La escala que la pieza lleva dentro',
                 pista='cc. 7–9 medidos · de Mi4 a Sol5, y termina en la nota más alta de la frase',
                 sistemas=[
                     dict(cap='a) con las figuras aplanadas, para colocar los dedos sin la prisa '
                              'del ritmo · nueve negras y larga la de arriba',
                          events=ESCALA_LISA, bars=4),
                     dict(cap='b) y como está escrita · la blanca del principio no es una pausa: es el '
                              'impulso de la subida',
                          events=MD_7_9, bars=3, show_time=False),
                     dict(cap='c) cc. 3–4 · la otra frase de la melodía, en notas largas y con la '
                              'digitación que ya trae la edición',
                          events=MD_3_4, bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='DÓNDE RESPIRA LA FRASE',
                 texto='La edición trae las ligaduras de fraseo dibujadas: úsalas como marcas de '
                       'respiración. La primera frase va del c. 3 al c. 9 y respira al llegar al Sol5. '
                       'Canta la melodía sin piano y verás que respiras exactamente donde acaba la '
                       'ligadura. Si al piano respiras en otro sitio, la frase se parte.'),
            dict(num=2, titulo='Y ahora el fondo, pero quieto', clef='bass',
                 pista='la izquierda de los cc. 1–8 sin romper · el Sol de abajo es el mismo en los '
                       'ocho compases: aquí solo se escucha, no se toca rápido',
                 sistemas=[
                     dict(cap='a) los tres acordes que hay debajo de toda la primera frase · Sol · '
                              'La menor sobre Sol · Sol maj7 · Sol: escúchalos antes de romperlos',
                          events=[ac(AC_I), ac(AC_ii), ac(AC_I7), ac(AC_I)],
                          bars=4, clef='bass'),
                     dict(cap='b) y compás a compás como está escrito · cuatro de Sol, tres de La '
                              'menor sobre Sol y el maj7 del c. 8: ocho compases, tres acordes',
                          events=[ac(AC_I)] * 4 + [ac(AC_ii)] * 3 + [ac(AC_I7)],
                          bars=8, clef='bass', show_time=False),
                     dict(cap='c) y solo las dos de arriba · Re-Si → Mi-La → Re-Fa: cada una se mueve '
                              'un grado, ninguna salta, y por eso la mano no viaja',
                          events=[ac(['D3', 'B3'])] * 4 + [ac(['E3', 'A3'])] * 3 + [ac(['D3', 'F3'])],
                          bars=8, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='Ya sabes cómo suena la melodía y qué acordes hay debajo. Lo único que falta es '
              'romperlos: la izquierda de esta pieza no es más que esos tres acordes convertidos en '
              'seis corcheas por compás. Y una vez rotos, que suenen igual y por debajo.',
        reglas=['LA IZQUIERDA SIEMPRE MÁS FLOJA', 'RESPIRA DONDE ACABA LA LIGADURA', 'PRIMERO LIMPIO, LUEGO RÁPIDO'],
        bloques=[
            dict(num=3, titulo='El acorde, roto en seis corcheas', clef='bass',
                 pista='es el mismo acorde de la página anterior · seis corcheas por compás, bajo una '
                       'sola barra, y ninguna pesa más que las otras',
                 sistemas=[
                     dict(cap='a) cc. 1–4 · el acorde de Sol roto: cuatro compases sin cambiar nada',
                          events=corcheas(CELULA_I, 4), bars=4, clef='bass'),
                     dict(cap='b) cc. 5–8 · aquí se mueven dos notas y nada más: Re→Mi y Si→La',
                          events=corcheas(CELULA_ii, 3) + corcheas(CELULA_I7, 1),
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y los ocho seguidos, sin parar entre el 4 y el 5 · así es como va, '
                              'y así hay que poder tocarla mirando a otro lado',
                          events=corcheas(CELULA_I, 4) + corcheas(CELULA_ii, 3) + corcheas(CELULA_I7, 1),
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA PIEZA NO ES DE DEDOS',
                 texto='La izquierda no tiene nada raro: un arpegio de tres notas que se repite. Lo '
                       'difícil es que suene igual 55 compases y por debajo de la melodía. Eso no se '
                       'arregla tocándolo más veces: toca la izquierda mirando a otro lado y '
                       'pregúntate si alguna corchea suena más fuerte. Casi siempre es la primera.'),
            dict(num=4, titulo='Las dos manos · cc. 3–9',
                 pista='este paso NO lleva pentagrama a propósito: se hace en la partitura de la página 1',
                 sistemas=[]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE HACE EL PASO 4, Y LA FORMA',
                 texto='Coloca la izquierda de memoria, sin mirártela, y lee solo la línea de la '
                       'derecha. Si para leer la melodía necesitas mirar la izquierda, vuelve al paso '
                       '2. Y empieza por el c. 7, no por el 1 — si siempre arrancas del principio, '
                       'acabarás tocando bien solo el principio. Sobre la forma: A va del c. 1 al 12, '
                       'B del 13 al 34 (ahí se va de Sol mayor y se llena de alteraciones, y esa parte '
                       'no se cita en este cuaderno porque no está medida nota a nota), y A’ del 35 al '
                       '55 — y los cc. 35 y 36 son idénticos a los cc. 3 y 4 en las dos manos.'),
            dict(tipo='escalera', valores=[48, 60, 72, 84, 92, 96],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
