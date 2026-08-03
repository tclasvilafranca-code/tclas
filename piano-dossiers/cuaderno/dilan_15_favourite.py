# -*- coding: utf-8 -*-
"""My Favourite Things (Rodgers y Hammerstein, arr. Kaitlin) — Dilan, avanzado.
   Ver TRANSCRIPCION_D15_17.md.

   Sol mayor, un sostenido: todos los Fa son sostenidos y NO se escriben. La
   pieza vive casi siempre en Mi menor, que es el relativo.

   La edicion trae CIFRADOS impresos (Em, C, Am, D, G, B), asi que la armonia
   viene dada. Lo medido con el lector son los acordes que la izquierda
   arpegia en el vals.

   No se cita el total de compases: los numeros impresos (14, 27, 40, 52) no
   cuadran con el recuento del lector.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'
_B = [2400]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='h.'):
    return {'pitches': list(ps), 'dur': d}


def corch(ps, agrupar=6):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


def vals(fund, a, b):
    """El vals: la fundamental abajo y despues las otras dos notas."""
    return [n(fund), n(a), n(b)]


# --- los acordes medidos, contrastados con el cifrado impreso --------------
MIm = vals('E3', 'G3', 'B3')
DO = vals('C3', 'E3', 'G3')
RE = vals('D3', 'F3', 'A3')          # el Fa es sostenido por armadura
MIm_G = vals('B2', 'E3', 'G3')

CANCION = dict(
    alumno='Dilan', num=15, nivel='avanzado', slug='MyFavouriteThings',
    titulo_corto='My Favourite Things', time_sig=(3, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           'my-favourite-things-the-sound-.pdf'),
    yt='https://www.youtube.com/results?search_query=my+favourite+things+sound+of+music',

    ficha=dict(
        titulo='My Favourite Things',
        autor='Richard Rodgers y Oscar Hammerstein II (1959) · de "Sonrisas y lágrimas" · arr. Kaitlin',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '3/4'), ('Tempo', '♩=160'),
               ('Mano izq.', 'Vals'), ('Extras', 'Cifrados')],
        armonia=dict(
            titulo='El vals de la mano izquierda',
            tarjetas=[
                ('CIFRADO Em', 'Mi · Sol · Si',
                 'La fundamental abajo y las otras dos encima. Tres notas por compás.'),
                ('CIFRADO C', 'Do · Mi · Sol',
                 'El mismo dibujo movido. Medido.'),
                ('CIFRADO D', 'Re · Fa♯ · La',
                 'El Fa es sostenido por armadura: no está escrito, pero suena.'),
                ('EL MOLDE', '1 · después 2 y 3',
                 'Es el vals de toda la vida: el bajo cae y el acorde rebota encima.'),
            ],
            pie='La pieza está en Sol mayor pero vive en Mi menor, que es su relativo: por eso empieza y '
                'acaba en Em y suena más seria de lo que la letra dice. Los cifrados vienen impresos, '
                'así que la izquierda se puede tocar leyéndolos: fundamental abajo, y el resto del '
                'acorde en los tiempos dos y tres.',
        ),
        ritmos=[
            ('MI · Mi menor', 'el vals: la fundamental y después el acorde', MIm, OCRE, 'bass', SOL),
            ('MI · Do', 'el mismo dibujo, movido', DO, OCRE, 'bass', SOL),
            ('MD', 'la melodía, en el registro medio', [n('F4'), n('E4'), n('E4')], AZUL, 'treble', SOL),
        ],
        especial=[
            'Armadura de un sostenido: todos los Fa son ♯. La tonalidad escrita es Sol mayor.',
            'La pieza vive en MI MENOR, el relativo: empieza y acaba ahí.',
            'Los CIFRADOS vienen impresos: Em, C, Am, D, G y B. Úsalos.',
            'Pone ♩=160 y va en 3/4: es un vals rápido, no una balada.',
            'Hay barra de repetición y casillas 1.ª y 2.ª: el orden no es el orden escrito.',
            'El cifrado B (Si mayor) lleva un Re♯ escrito a mano: no está en la armadura.',
        ],
        reto='La velocidad del vals. A ♩=160 no hay tiempo de pensar dónde va la mano izquierda entre el '
             'bajo y el acorde: el salto tiene que estar automatizado. Si tienes que mirarte la mano, ya '
             'has llegado tarde.',
        truco='Estudia la izquierda sola mirando al techo. Toca la fundamental, y mientras suena, coloca '
              'ya la mano en el acorde sin tocarlo. Ese "preparar en el aire" es todo el secreto del '
              'vals rápido, y no se aprende tocando más veces: se aprende tocando más despacio.',
        sabias='En la película la canta Julie Andrews para calmar a los niños durante una tormenta. Años '
               'después John Coltrane la grabó en jazz, en una versión de casi catorce minutos, y desde '
               'entonces es de las melodías más versionadas del siglo XX.',
        qr=dict(titulo='Escucha la original',
                texto='Y busca también la versión de John Coltrane: es la misma melodía.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta pieza es un vals rápido, y lo que pide es '
              'que la izquierda salte del bajo al acorde sin mirar. Aquí se entrena ese salto por toda '
              'la tonalidad, y también la escala de Mi menor, que es donde vive la melodía.',
        reglas=['ARMADURA DE SOL: TODOS LOS FA SON ♯', 'PREPARA EL ACORDE EN EL AIRE', 'EMPIEZA LENTO'],
        ejercicios=[
            dict(num=1, titulo='Escala de Mi menor · dos octavas', clef='bass',
                 pista='manos separadas · el relativo de Sol mayor, misma armadura',
                 events=corch(['E2', 'F2', 'G2', 'A2', 'B2', 'C3']) +
                        corch(['D3', 'E3', 'F3', 'G3', 'A3', 'B3']) +
                        corch(['C4', 'D4', 'E4', 'D4', 'C4', 'B3']) +
                        corch(['A3', 'G3', 'F3', 'E3', 'D3', 'C3']) +
                        corch(['B2', 'A2', 'G2', 'F2', 'E2', 'E2']),
                 bars_per_line=5),
            dict(num=2, titulo='El vals, por toda la tonalidad', clef='bass',
                 pista='fundamental y después el acorde · sobre los seis grados de Mi menor',
                 events=(vals('A2', 'C3', 'E3') + vals('B2', 'D3', 'F3') +
                         vals('C3', 'E3', 'G3') + vals('D3', 'F3', 'A3') +
                         vals('G2', 'B2', 'D3') + vals('A2', 'C3', 'E3')),
                 bars_per_line=6),
            dict(num=3, titulo='El vals al revés', clef='bass',
                 pista='ahora el acorde cae en el uno y el bajo en el tres · descoloca, y por eso sirve',
                 events=([n('C3'), n('E3'), n('A2')] + [n('D3'), n('F3'), n('B2')] +
                         [n('E3'), n('G3'), n('C3')] + [n('F3'), n('A3'), n('D3')] +
                         [n('B2'), n('D3'), n('G2')] + [n('C3'), n('E3'), n('A2')]),
                 bars_per_line=6),
            dict(num=4, titulo='El salto solo, sin el acorde', clef='bass',
                 pista='el bajo en el uno y silencio en el dos y el tres · usa ese hueco para colocarte',
                 events=[n('A2'), {'rest': True, 'dur': 'h'},
                         n('B2'), {'rest': True, 'dur': 'h'},
                         n('C3'), {'rest': True, 'dur': 'h'},
                         n('D3'), {'rest': True, 'dur': 'h'},
                         n('G2'), {'rest': True, 'dur': 'h'},
                         n('A2'), {'rest': True, 'dur': 'h'}],
                 bars_per_line=6),
            dict(num=5, titulo='El Re sostenido del acorde B',
                 pista='no está en la armadura y aparece una sola vez · es fácil comérselo',
                 events=[n('B4'), n('D#5'), n('F#5'),
                         n('E5', 'h.'),
                         n('F#5'), n('D#5'), n('B4'),
                         n('E5', 'h.')],
                 bars_per_line=4),
            dict(num=6, titulo='Arpegio de Mi menor · dos octavas', clef='bass',
                 pista='fundamental · 3ª · 5ª · 8ª · el acorde con el que empieza y acaba la pieza',
                 events=corch(['E2', 'G2', 'B2', 'E3', 'G3', 'B3']) +
                        corch(['E4', 'B3', 'G3', 'E3', 'B2', 'G2']),
                 bars_per_line=4),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves. Abajo se escucha: '
              'lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · armadura de Sol: todos los Fa son ♯',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DEL VALS (CLAVE DE FA)',
        chuleta_pitches=['E2', 'G2', 'B2', 'E3', 'G3', 'B3'],
        chuleta_nombres=['Mi', 'Sol', 'Si', 'Mi', 'Sol', 'Si'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa', clef='bass',
                 pista='donde vive el vals · el orden está desordenado a propósito',
                 events=[n(p) for p in ('E3', 'B2', 'G3', 'D3', 'A2', 'F3', 'C3', 'E2',
                                        'B3', 'G2', 'A3', 'D2', 'C4', 'F2', 'E3')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · registro medio, casi todo entre Si3 y Si4',
                 events=[n(p) for p in ('E4', 'B4', 'G4', 'D5', 'A4', 'F4', 'C5', 'B3',
                                        'E5', 'D4', 'G5', 'A3', 'F5', 'C4', 'E4')]),
            dict(num=3, titulo='Leer la tríada de golpe', clef='bass',
                 pista='las tres notas a la vez · nómbralas de abajo arriba, sin contar las líneas',
                 events=[ac(('E3', 'G3', 'B3'), 'h.'), ac(('A2', 'C3', 'E3'), 'h.'),
                         ac(('B2', 'D3', 'F3'), 'h.'), ac(('C3', 'E3', 'G3'), 'h.'),
                         ac(('D3', 'F3', 'A3'), 'h.'), ac(('G2', 'B2', 'D3'), 'h.')],
                 bars_per_line=6),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca un vals: bajo, acorde, acorde. Acentúa unas veces el bajo y otras el '
                      'segundo golpe, y que diga cuál pesaba.'),
                ('B', 'Toca una tríada suelta: MAYOR o MENOR. La pieza alterna las dos sin avisar.'),
                ('C', 'Marca tres tiempos y toca una nota en uno. Que diga en cuál cayó.'),
                ('+', 'Y sin escribir: toca el vals y que cuente "un-dos-tres" encima.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Qué pesa más?', pista='el bajo, o el acorde de después',
                     n=10, opciones=['bajo', 'acorde']),
                dict(letra='B', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=8, opciones=['M', 'm']),
                dict(letra='C', titulo='¿En qué tiempo cae?', pista='cuenta los tres por dentro',
                     n=6, opciones=['1', '2', '3']),
            ],
        ),
    ),

    piano1=dict(
        intro='La partitura, abierta en trozos. La armonía viene de los cifrados impresos y los acordes '
              'de la izquierda están medidos. Los números de compás no se citan: los impresos y el '
              'recuento del lector no coinciden.',
        reglas=['SE CITA POR CIFRADO', 'PREPARA EL ACORDE EN EL AIRE', 'EMPIEZA MUY POR DEBAJO DE 160'],
        bloques=[
            dict(num=1, titulo='El vals sobre Mi menor', clef='bass',
                 pista='cifrado Em medido · Mi · Sol · Si · el acorde con el que empieza la pieza',
                 sistemas=[dict(cap='cuatro compases seguidos · el bajo con peso y los dos golpes de '
                                    'arriba casi sin sonido',
                                events=MIm * 4, bars=4, clef='bass')]),
            dict(num=2, titulo='Los cuatro cifrados de la primera página', clef='bass',
                 pista='Em · C · D · Em · lo único que cambia es dónde pones la mano',
                 sistemas=[dict(cap='el salto de Do a Re es el que más cuesta: prepáralo mientras suena '
                                    'el acorde anterior',
                                events=MIm + DO + RE + MIm + DO + RE, bars=6, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ UN VALS RÁPIDO ES DIFÍCIL',
                 texto='En un vals la mano izquierda hace dos cosas distintas en el mismo compás: una '
                       'nota grave en el uno y un acorde en el dos y el tres, y entre las dos hay un '
                       'salto. A ♩=160 ese salto dura menos de medio segundo. La única forma de que salga '
                       'es no hacerlo con prisa, sino con antelación: mientras suena el bajo, la mano ya '
                       'tiene que estar viajando. Se practica lento y mirando al techo.'),
            dict(num=3, titulo='La misma armonía, sin el vals', clef='bass',
                 pista='solo la fundamental de cada cifrado · para oír por dónde va la pieza',
                 sistemas=[dict(cap='Mi · Do · Re · Mi · Do · Re · Sol · Mi · así viaja la mano',
                                events=[n('E3', 'h.'), n('C3', 'h.'), n('D3', 'h.'), n('E3', 'h.'),
                                        n('C3', 'h.'), n('D3', 'h.'), n('G2', 'h.'), n('E3', 'h.')],
                                bars=8, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='LOS CIFRADOS SON TU ATAJO',
                 texto='Encima del pentagrama tienes escritos Em, C, Am, D, G y B. Son seis acordes en '
                       'toda la pieza. Si te aprendes las seis posiciones de la mano, puedes tocar la '
                       'izquierda sin leer el pentagrama de abajo ni una vez: miras el cifrado, colocas '
                       'la mano y haces el vals. A ♩=160 eso no es un lujo, es la única manera.'),
            dict(num=5, titulo='La melodía de los cc. 1–4 · alturas medidas',
                 pista='cc. 1–4 · las notas son las de la partitura; el ritmo, simplificado a negras',
                 sistemas=[dict(cap='"Rain-drops on ro-ses" · canta la letra mientras la lees y el '
                                    'ritmo se coloca solo',
                                events=[n('F4'), n('E4'), n('E4'),
                                        n('B3'), n('E4'), n('E4'),
                                        n('F4', 'h.'),
                                        n('E4'), n('B4'), n('B4')],
                                bars=4)]),
            dict(num=4, titulo='El mismo acorde, más grave', clef='bass',
                 pista='cifrado Em medido en otra posición · Si · Mi · Sol, con el Si abajo',
                 sistemas=[dict(cap='el mismo acorde con otra nota debajo suena más abierto: la edición '
                                    'lo usa para no repetirse',
                                events=MIm_G * 2 + MIm * 2, bars=4, clef='bass')]),
        ],
    ),

    piano2=dict(
        intro='Montarla es dos cosas: automatizar el salto del vals y saber por dónde va la hoja, porque '
              'hay repetición y dos casillas. Las notas, en esta pieza, son lo de menos.',
        reglas=['EL RECORRIDO, ANTES QUE LAS NOTAS', 'LA IZQUIERDA DE MEMORIA', 'SUBIR DESPACIO A 160'],
        bloques=[
            dict(tipo='nota',
                 etiqueta='EL RECORRIDO DE LA HOJA',
                 texto='Hay una barra de repetición hacia el c. 15 y, más adelante, casillas 1.ª y 2.ª. '
                       'Eso quiere decir que llegas al final de la primera vuelta, tocas la casilla 1, '
                       'vuelves atrás, y la segunda vez te saltas esa casilla y entras por la 2. Antes de '
                       'tocar una sola nota, sigue la partitura con el dedo y di en voz alta por dónde '
                       'vas. Es cinco minutos de trabajo que te ahorran tres semanas de lío.'),
            dict(num=5, titulo='El salto, aislado', clef='bass',
                 pista='solo el bajo y el primer golpe del acorde · lo demás sobra para este ejercicio',
                 sistemas=[dict(cap='toca el bajo, y mientras suena, coloca la mano arriba sin tocar · '
                                    'después baja el dedo',
                                events=[n('E3'), ac(('G3', 'B3'), 'h'),
                                        n('C3'), ac(('E3', 'G3'), 'h'),
                                        n('D3'), ac(('F3', 'A3'), 'h'),
                                        n('E3'), ac(('G3', 'B3'), 'h'),
                                        n('G2'), ac(('B2', 'D3'), 'h'),
                                        n('E3'), ac(('G3', 'B3'), 'h')],
                                bars=6, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='LA PIEZA ESTÁ EN MI MENOR, NO EN SOL',
                 texto='La armadura dice Sol mayor, pero mira dónde empieza y dónde acaba: en Mi menor. '
                       'Las dos tonalidades comparten armadura, son relativas, y lo que decide cuál de '
                       'las dos manda es sobre qué nota descansa la música. Aquí descansa en Mi, y por '
                       'eso una canción cuya letra habla de gotas de lluvia y bigotes de gato suena '
                       'seria. Cuando toques, no busques que suene alegre: no lo es.'),
            dict(tipo='nota',
                 etiqueta='CÓMO ESTUDIARLA ESTA SEMANA',
                 texto='1 · El recorrido, con el dedo y en voz alta, sin piano. '
                       '2 · El salto del vals, aislado, mirando al techo. '
                       '3 · La izquierda de la primera página leyendo solo los cifrados. '
                       '4 · La melodía sola, cantándola. '
                       '5 · Las dos manos a la mitad de velocidad, y solo hasta la repetición.'),
            dict(num=6, titulo='La izquierda de la primera vuelta', clef='bass',
                 pista='los cifrados de la primera página, encadenados · sin parar entre acorde y acorde',
                 sistemas=[dict(cap='ocho compases seguidos: es lo que vas a repetir toda la semana',
                                events=(vals('A2', 'C3', 'E3') + vals('D3', 'F3', 'A3') +
                                        vals('G2', 'B2', 'D3') + vals('C3', 'E3', 'G3') +
                                        vals('G2', 'B2', 'D3') + vals('C3', 'E3', 'G3') +
                                        vals('A2', 'C3', 'E3') + MIm),
                                bars=8, clef='bass')]),
            dict(tipo='escalera', valores=[80, 100, 116, 132, 148, 160],
                 regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='tracker', titulo='La prueba de la semana',
                 pie='Marca el día en que hayas hecho el salto del vals sin mirarte la mano izquierda.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
