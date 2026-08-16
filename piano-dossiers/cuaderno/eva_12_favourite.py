# -*- coding: utf-8 -*-
"""My Favourite Things (canción 12 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico); el material medido se
   importa de `dilan_15_favourite`. Ver TRANSCRIPCION_D15_17.md.

   Camino distinto al de Dilan:

     - A Dilan se le entra por el VALS ENTERO y después se le aísla el salto.
     - A Eva se le entra por LOS DOS GOLPES DE ARRIBA, sin el bajo. A ♩=160 el
       problema de esta pieza no es dar con la tecla: es que los golpes dos y
       tres del compás pesan lo mismo que el bajo, y entonces el vals deja de
       ser un vals y se convierte en tres negras iguales. Trabajarlos solos,
       con el silencio en el uno, es la única forma de oír cuánto pesan de
       verdad; el bajo se pone encima después y ya no las arrastra.

   Sol mayor, un sostenido: todos los Fa son sostenidos y no se escriben. La
   pieza vive casi siempre en Mi menor, que es el relativo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_15_favourite import n, ac, vals, MIm, DO, RE

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'


def sil(d='q'):
    return {'rest': True, 'dur': d}


def golpes(a, b, veces=1):
    """Los golpes dos y tres del vals, SIN el bajo: silencio en el uno."""
    return [sil('q'), ac((a, b), 'q'), ac((a, b), 'q')] * veces


CANCION = dict(
    alumno='Eva', num=12, nivel='avanzado', slug='MyFavouriteThings',
    titulo_corto='My Favourite Things', time_sig=(3, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'my-favourite-things-the-sound-.pdf'),
    yt='https://www.youtube.com/results?search_query=my+favourite+things+sound+of+music',

    ficha=dict(
        titulo='My Favourite Things',
        autor='Richard Rodgers y Oscar Hammerstein II (1959) · de "Sonrisas y lágrimas" · arr. Kaitlin',
        datos=[('Tonalidad', 'Sol mayor · vive en Mi menor'), ('Compás', '3/4'),
               ('Tempo', '♩=160'), ('Mano izq.', 'Vals'), ('Extras', 'Cifrados')],
        armonia=dict(
            titulo='Un vals a 160: el reloj manda',
            tarjetas=[
                ('EL VALS', 'Bajo · golpe · golpe',
                 'La fundamental abajo con peso, y los dos golpes de arriba casi sin sonido.'),
                ('MEDIO SEGUNDO', '♩=160',
                 'Es lo que dura un tiempo. La mano tiene ese rato para viajar de un acorde al otro.'),
                ('LOS CIFRADOS', 'Em · C · Am · D · G · B',
                 'Vienen impresos encima del pentagrama: la armonía te la dan hecha.'),
                ('DÓNDE DESCANSA', 'Mi menor',
                 'La armadura dice Sol mayor, pero la música empieza y acaba en Mi menor.'),
            ],
            pie='Las dos tonalidades comparten armadura: son relativas, y lo que decide cuál manda es '
                'sobre qué nota descansa la música. Aquí descansa en Mi, y por eso una canción cuya '
                'letra habla de gotas de lluvia y bigotes de gato suena seria. No busques que suene '
                'alegre: no lo es.',
        ),
        ritmos=[
            ('MI · los golpes', 'dos y tres del compás, sin el bajo: casi sin sonido',
             golpes('G3', 'B3'), OCRE, 'bass', SOL),
            ('MI · el vals entero', 'y ahora con la fundamental debajo',
             MIm, OCRE, 'bass', SOL),
        ],
        especial=[
            'Armadura de un sostenido: todos los Fa son ♯ y no se escriben.',
            'La edición trae los cifrados impresos encima del pentagrama.',
            'Compás de 3/4: es un vals, y va a ♩=160, que es rápido.',
            'Hay barra de repetición y casillas 1.ª y 2.ª: el recorrido no es lineal.',
            'La pieza empieza y termina en Mi menor, el relativo de Sol mayor.',
            'La melodía va casi toda por grados y con muy pocos saltos.',
        ],
        reto='La velocidad del salto. A ♩=160 cada tiempo dura poco más de un tercio de segundo: la '
             'mano izquierda tiene ese rato para soltar un acorde, viajar y llegar colocada al '
             'siguiente. Si llega tarde una sola vez por vuelta, el vals cojea.',
        truco='Trabaja los golpes dos y tres SIN el bajo, con silencio en el uno. Así oyes cuánto pesan '
              'de verdad, que casi siempre es el triple de lo que debería. Cuando suenen a nada, pon el '
              'bajo debajo: ya no los arrastra, y el salto deja de ser un problema de velocidad para '
              'ser uno de puntería.',
        sabias='La canción no es de Navidad, aunque suene a eso: es de "Sonrisas y lágrimas" (1959) y la '
               'cantan para calmar a unos niños durante una tormenta. Lo de asociarla a diciembre vino '
               'mucho después, de las versiones de jazz que se pusieron de moda en invierno.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en que los golpes de arriba casi no se oyen. Ese es el efecto.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Aquí se empieza por arriba y sin el bajo. A ♩=160 lo que estropea un vals no es fallar la '
              'tecla: es que los golpes dos y tres pesen lo mismo que el uno. Trabajarlos solos, con un '
              'silencio en el primer tiempo, es la única forma de oír de verdad cuánto pesan.',
        reglas=['LOS GOLPES DE ARRIBA, CASI SIN SONIDO', 'EL SILENCIO DEL UNO SE CUENTA', 'DESPACIO ANTES QUE A 160'],
        bloques=[
            dict(num=1, titulo='Los dos golpes de arriba, sin el bajo', clef='bass',
                 pista='cifrado Em medido · el uno es un silencio y hay que contarlo, no saltárselo',
                 sistemas=[
                     dict(cap='a) sobre Mi menor, cuatro compases · tienen que sonar a nada: si los '
                              'oyes claramente, están pesando demasiado',
                          events=golpes('G3', 'B3', 4), bars=4, clef='bass'),
                     dict(cap='b) y cambiando de acorde · Do · Re · Mi menor: el peso no cambia porque '
                              'cambie el acorde',
                          events=golpes('E3', 'G3') + golpes('F#3', 'A3') + golpes('G3', 'B3', 2),
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y ahora sí, con el bajo debajo · Em · Do · Re · Em: el bajo con peso '
                              'y los de arriba igual de flojos que en la a)',
                          events=MIm + DO + RE + MIm, bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE EMPIEZA POR ARRIBA',
                 texto='Un vals suena a vals por una sola razón: el primer tiempo pesa y los otros dos '
                       'no. Cuando se estudia el compás entero desde el principio, la mano aprende los '
                       'tres golpes con el mismo peso y ya no hay manera de quitárselo. Empezando por '
                       'los dos de arriba, en cambio, los aprendes ligeros de entrada, y el bajo se pone '
                       'encima sin arrastrarlos. Es cinco minutos más de trabajo y te ahorra la semana '
                       'de quitarle el peso a algo que ya lo tiene.'),
            dict(num=2, titulo='Y el bajo, que es el que viaja', clef='bass',
                 pista='los cifrados de la primera página · a ♩=160 el bajo tiene un tercio de segundo '
                       'para llegar al siguiente',
                 sistemas=[
                     dict(cap='a) solo las fundamentales, una por compás · La · Re · Sol · Do · Sol · '
                              'Do · La · Mi: dilas en voz alta mientras las tocas',
                          events=[n('A2', 'h.'), n('D3', 'h.'), n('G2', 'h.'), n('C3', 'h.'),
                                  n('G2', 'h.'), n('C3', 'h.'), n('A2', 'h.'), n('E3', 'h.')],
                          bars=8, clef='bass'),
                     dict(cap='b) los seis acordes de la pieza, en bloque y uno por compás · aquí no '
                              'hay ritmo que valga: solo la mano encontrando la posición',
                          events=[ac(('E3', 'G3', 'B3')), ac(('C3', 'E3', 'G3')),
                                  ac(('A2', 'C3', 'E3')), ac(('D3', 'F3', 'A3')),
                                  ac(('G2', 'B2', 'D3')), ac(('E3', 'G3', 'B3'))],
                          bars=6, clef='bass', show_time=False),
                     dict(cap='c) y el salto solo · toca el bajo y, mientras suena, coloca la mano en '
                              'el aire sobre el siguiente: llegar tarde es el único fallo posible',
                          events=[n('E3'), ac(('G3', 'B3'), 'h'),
                                  n('C3'), ac(('E3', 'G3'), 'h'),
                                  n('D3'), ac(('F#3', 'A3'), 'h'),
                                  n('E3'), ac(('G3', 'B3'), 'h')],
                          bars=4, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='El vals ya está montado. Queda encadenarlo entero, ponerle la melodía —que se coloca sola '
              'si cantas la letra— y, sobre todo, saber por dónde va la hoja: hay repetición y dos '
              'casillas, y ahí es donde se pierde la gente, no en las notas.',
        reglas=['EL RECORRIDO, ANTES QUE LAS NOTAS', 'LA IZQUIERDA DE MEMORIA', 'SUBIR DESPACIO A 160'],
        bloques=[
            dict(num=3, titulo='Los ocho compases seguidos', clef='bass',
                 pista='los cifrados de la primera página, encadenados · sin parar entre acorde y acorde',
                 sistemas=[
                     dict(cap='a) es lo que vas a repetir toda la semana · sin parar en el cambio, y '
                              'el bajo siempre a tiempo',
                          events=(vals('A2', 'C3', 'E3') + vals('D3', 'F3', 'A3') +
                                  vals('G2', 'B2', 'D3') + vals('C3', 'E3', 'G3') +
                                  vals('G2', 'B2', 'D3') + vals('C3', 'E3', 'G3') +
                                  vals('A2', 'C3', 'E3') + MIm),
                          bars=4, clef='bass'),
                 ]),
            dict(num=4, titulo='La melodía, cantada',
                 pista='cc. 1–4 · las notas son las de la partitura; el ritmo, simplificado a negras',
                 sistemas=[
                     dict(cap='a) “Rain-drops on ro-ses” · canta la letra mientras la lees y el ritmo '
                              'se coloca solo',
                          events=[n('F4'), n('E4'), n('E4'),
                                  n('B3'), n('E4'), n('E4'),
                                  n('F4', 'h.'),
                                  n('E4', 'h.')],
                          bars=4),
                     dict(cap='b) y las mismas notas en blancas con puntillo, una por compás · para '
                              'oír el dibujo de la frase sin la prisa del ritmo',
                          events=[n('F4', 'h.'), n('E4', 'h.'), n('B3', 'h.'), n('E4', 'h.'),
                                  n('F4', 'h.'), n('E4', 'h.'), n('B4', 'h.')],
                          bars=7, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA PIEZA ESTÁ EN MI MENOR, NO EN SOL',
                 texto='La armadura dice Sol mayor, pero mira dónde empieza y dónde acaba: en Mi menor. '
                       'Las dos tonalidades comparten armadura, son relativas, y lo que decide cuál '
                       'manda es sobre qué nota descansa la música. Aquí descansa en Mi. Cuando toques, '
                       'no busques que suene alegre: no lo es, y esa es justamente la gracia de la '
                       'canción.'),
            dict(tipo='nota',
                 etiqueta='EL RECORRIDO DE LA HOJA',
                 texto='Hay una barra de repetición hacia el c. 15 y, más adelante, casillas 1.ª y 2.ª. '
                       'Llegas al final de la primera vuelta, tocas la casilla 1, vuelves atrás, y la '
                       'segunda vez te saltas esa casilla y entras por la 2. Antes de tocar una sola '
                       'nota, sigue la partitura con el dedo y di en voz alta por dónde vas: son cinco '
                       'minutos de trabajo que te ahorran tres semanas de lío.'),
            dict(tipo='escalera', valores=[80, 100, 116, 132, 148, 160],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
