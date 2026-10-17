# -*- coding: utf-8 -*-
"""Can't Help Falling in Love (canción 1 de Eva, nivel avanzado).

   La partitura es la MISMA edición que la de Dilan, byte a byte (comprobado
   por sha256), asi que la medicion vale para las dos: medir es medir la
   partitura, no al alumno. Por eso el material medido se importa de
   `dilan_02_data` en vez de copiarlo — copiarlo seria arriesgarse a que las
   dos versiones se separen y una de las dos deje de cuadrar con el papel.

   Lo que NO se reutiliza es el cuaderno. Eva recibe hojas propias, y no por
   cortesia: el camino de estudio es distinto a proposito.

     - A Dilan se le entra por el ARPEGIO ESCRITO y se le va quitando relleno
       hasta llegar al bajo.
     - A Eva se le entra por el CIFRADO: primero el acorde en bloque, leyendo
       el nombre impreso encima del pentagrama, y solo despues se rompe en
       arpegio. Es el camino del que ya sabe leer cifrados, y deja la pieza
       lista para tocarla de memoria.

   Ver TRANSCRIPCION_D02_CANT_HELP.md: los cifrados los imprime la edicion, y
   la melodia de los cc. 1-3 esta medida en ventana aislada dos veces.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_02_data import arpegio, RE, FAm, SIm, LA, MELODIA_1_3

HERE = os.path.dirname(__file__)
TON = 'Re mayor'
OCRE = HexColor('#8C6A3F')
AZUL = HexColor('#3E6E8F')


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='h.'):
    return {'pitches': list(ps), 'dur': d}


# Los cifrados que imprime la edicion, en bloque y en el registro en el que
# los toca la mano izquierda. La disposicion sale del cifrado, no de una
# medicion nota a nota: la edicion escribe el acorde roto, no el bloque.
BLOQUE = {
    'D':   ('D3', 'F3', 'A3'),
    'F#m': ('F3', 'A3', 'C4'),
    'Bm':  ('B2', 'D3', 'F3'),
    'G':   ('G2', 'B2', 'D3'),
    'A':   ('A2', 'C3', 'E3'),
}
# el mapa entero de la primera pagina, tal como lo imprime la edicion
MAPA = ['D', 'F#m', 'Bm', 'G', 'D', 'A', 'A', 'G', 'A', 'Bm', 'G', 'D']

CANCION = dict(
    alumno='Eva', num=1, nivel='avanzado', slug='CantHelp',
    titulo_corto='Can’t Help Falling in Love', time_sig=(3, 4), key_sig=TON,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'cant-help-falling-in-love-.pdf'),
    yt='https://www.youtube.com/results?search_query=elvis+presley+cant+help+falling+in+love',

    ficha=dict(
        titulo='Can’t Help Falling in Love',
        autor='Elvis Presley (1961) · arr. con cifrados y letra',
        datos=[('Tonalidad', 'Re mayor'), ('Compás', '3/4'),
               ('Mano izq.', 'Acorde roto'), ('Mano dcha.', '1 nota por compás'),
               ('Extras', 'Letra + cifrados')],
        armonia=dict(
            titulo='Los cifrados, que aquí lo son todo',
            tarjetas=[
                ('EL GESTO', 'Fund · 3ª · 5ª · 8ª · 5ª · 3ª',
                 'Seis corcheas por compás, siempre el mismo dibujo. Cambia el acorde, nunca la forma.'),
                ('LA PRIMERA FRASE', 'D · F♯m · Bm · A',
                 'Cuatro acordes y ya suena la canción entera. Léelos, no los deduzcas.'),
                ('EL FINAL', 'F♯m · C♯7',
                 'El Do♯7 no pertenece a Re mayor: trae un Mi♯ escrito a mano. Es el único sitio que hay que leer de verdad.'),
            ],
            pie='Los cifrados los imprime la edición encima del pentagrama, y la letra debajo. '
                'Con esas dos cosas se toca la izquierda sin mirar el pentagrama de abajo ni una vez.',
        ),
        especial=[
            'La armadura de Re mayor lleva dos sostenidos: todos los Fa y todos los Do.',
            'La izquierda hace SIEMPRE el mismo dibujo de seis corcheas. No hay ni un compás distinto.',
            'La melodía de los tres primeros compases es una nota por compás: Re, La, Re.',
            'La misma melodía sirve para dos letras distintas: «Wise men say» y «Shall I stay».',
            'Al final aparecen F♯m y C♯7, y ese Do♯7 se sale de la tonalidad.',
        ],
        ritmos=[
            ('MI', 'seis corcheas por compás: el acorde roto',
             arpegio(*RE), OCRE, 'bass', TON),
            ('MD', 'una blanca con puntillo, con su sílaba',
             [n('D4', 'h.')], AZUL, 'treble', TON),
        ],
        reto='Que las seis corcheas suenen iguales. El acorde roto tiende a marcar de más la primera '
             'de cada compás, y en cuanto la marcas esto se convierte en un vals de verbena.',
        truco='Lee los cifrados en voz alta antes de tocar: «Re, Fa sostenido menor, Si menor, La…». '
              'Media canción es saber dónde estás. Y toca la izquierda cantando la letra por encima: '
              'si la voz se te va detrás de la mano, es que estás acentuando.',
        sabias='La melodía no es de 1961: viene de «Plaisir d’amour», una romanza francesa que '
               'Jean-Paul Égide Martini escribió en 1784. Elvis la grabó para «Blue Hawaii» y acabó '
               'siendo la canción con la que cerraba sus conciertos.',
        qr=dict(titulo='Escucha la versión de Elvis',
                texto='Fíjate en lo despacio que va. La prisa es el enemigo de esta canción.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Esta edición imprime los cifrados encima del pentagrama. Aprovéchalo: el paso 1 es '
              'colocar el acorde leyendo solo el nombre, sin mirar el pentagrama de abajo. Cuando las '
              'cinco posiciones estén en la mano, romperlas en arpegio no cuesta nada.',
        reglas=['ARMADURA DE RE', 'LEE EL CIFRADO, NO LA NOTA', 'LA IZQUIERDA SIEMPRE MÁS FLOJA'],
        bloques=[
            dict(num=1, titulo='El acorde en bloque, leyendo el cifrado', clef='bass',
                 pista='un acorde por compás · di el nombre en voz alta antes de bajar la mano',
                 sistemas=[
                     dict(cap='a) la primera frase · D · F♯m · Bm · A, y vuelta a D',
                          events=[ac(BLOQUE['D']), ac(BLOQUE['F#m']), ac(BLOQUE['Bm']),
                                  ac(BLOQUE['A']), ac(BLOQUE['D'])],
                          bars=5, clef='bass'),
                     dict(cap='b) las dos que faltan, que salen en el estribillo · G y A',
                          events=[ac(BLOQUE['G']), ac(BLOQUE['A']),
                                  ac(BLOQUE['G']), ac(BLOQUE['A'])],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y la primera página entera · D · F♯m · Bm · G · D · A · A7 · G · '
                              'A · Bm · G · D',
                          events=[ac(BLOQUE[c]) for c in MAPA],
                          bars=6, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE EMPIEZA POR EL BLOQUE Y NO POR EL ARPEGIO',
                 texto='El arpegio no tiene ninguna dificultad: son las notas del acorde subiendo y '
                       'bajando. Lo que cuesta es llegar colocada al acorde siguiente. Si montas el '
                       'bloque primero, la mano aprende las cinco posiciones y el arpegio sale solo; '
                       'si empiezas por el arpegio, te pasas tres semanas buscando teclas.'),
            dict(num=2, titulo='Y ahora se rompe en arpegio', clef='bass',
                 pista='fund · 3ª · 5ª · 8ª · 5ª · 3ª · seis corcheas, y ninguna suena más que otra',
                 sistemas=[
                     dict(cap='a) sobre Re, cuatro compases · sin marcar la primera de cada compás',
                          events=arpegio(*RE, n=4), bars=4, clef='bass'),
                     dict(cap='b) y sobre Si menor, que es el que peor cae en la mano · el meñique '
                              'baja a la tecla negra sin estirar el brazo',
                          events=arpegio(*SIm, n=4), bars=4, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='Las cinco posiciones ya están en la mano. Ahora se encadenan, entra la melodía —que son '
              'tres notas— y se monta el final, que es el único sitio de la canción donde hay que leer '
              'de verdad.',
        reglas=['CANTA LA LETRA MIENTRAS TOCAS', 'LA VOZ MANDA SOBRE LA MANO', 'PRIMERO IGUAL, LUEGO RÁPIDO'],
        bloques=[
            dict(num=3, titulo='El arpegio, cambiando de acorde', clef='bass',
                 pista='aquí es donde se ve si el paso 1 está hecho: la mano tiene que llegar colocada',
                 sistemas=[
                     dict(cap='a) en el orden que imprime la edición · D · F♯m · Bm · G · D · A',
                          events=(arpegio(*RE) + arpegio(*FAm) + arpegio(*SIm) +
                                  arpegio('G2', 'B2', 'D3', 'G3') + arpegio(*RE) + arpegio(*LA)),
                          bars=6, clef='bass'),
                     dict(cap='b) y con el estribillo detrás, sin parar · G · A · G · A',
                          events=arpegio('G2', 'B2', 'D3', 'G3') + arpegio('A2', 'C3', 'E3', 'A3') +
                                 arpegio('G2', 'B2', 'D3', 'G3') + arpegio('A2', 'C3', 'E3', 'A3'),
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA PRUEBA DE QUE NO ESTÁS ACENTUANDO',
                 texto='Toca la izquierda sola y canta la letra por encima. Si la voz se te va detrás '
                       'de la mano, es que estás marcando la primera corchea de cada compás. No es un '
                       'problema de dedos: es que el brazo cae en el uno. Toca mirando a otro lado y '
                       'escucha si alguna suena más fuerte que las demás.'),
            dict(num=4, titulo='La melodía, que son tres notas',
                 pista='cc. 1–3 medidos · tócala otra vez cantando «Shall I stay»: la melodía es la '
                       'misma y la letra no',
                 sistemas=[
                     dict(cap='a) Re · La · Re · una sílaba por nota: «Wise — men — say»',
                          events=MELODIA_1_3, bars=3),
                 ]),
            dict(num=5, titulo='El final, que se va de la tonalidad', clef='bass',
                 pista='cifrados F♯m y C♯7 · el Do♯7 no pertenece a Re mayor',
                 sistemas=[
                     dict(cap='a) los dos acordes en bloque · el C♯7 trae un Mi♯ escrito a mano: '
                              'márcalo con lápiz antes de tocar',
                          events=[ac(BLOQUE['F#m']), ac(('C3', 'E#3', 'G3')),
                                  ac(BLOQUE['F#m']), ac(('C3', 'E#3', 'G3'))],
                          bars=4, clef='bass'),
                 ]),
            dict(tipo='escalera', valores=[50, 60, 69, 76, 84, 92],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · Los acordes en bloque, leyendo el cifrado.   '
                       '2 · El arpegio sobre Re.   '
                       '3 · El arpegio cambiando de acorde, y el estribillo detrás.   '
                       '4 · La melodía, cantando la letra.   '
                       '5 · El final con el Mi♯ marcado, y la escalera de tempo.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
