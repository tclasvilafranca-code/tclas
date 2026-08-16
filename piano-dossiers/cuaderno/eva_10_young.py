# -*- coding: utf-8 -*-
"""When We Were Young (canción 10 de Eva, nivel avanzado). PIEZA NUEVA:
   no está en el álbum de Dilan. Ver TRANSCRIPCION_E10_WWWY.md.

   De dónde sale lo que se cita
   ----------------------------
   Esta edición (musicaparadisfrutar.com, 4 páginas) imprime tres cosas que
   se leen sin ninguna ambigüedad y que son las que usa este cuaderno:

     1. EL CIFRADO encima de cada compás, con el bajo escrito cuando es una
        inversión (Fmaj7/A, F/A, A/C♯, F/C). O sea: la línea del bajo entera
        está impresa en letras, compás a compás.
     2. LA NUMERACIÓN de compases cada sistema (5, 9, 13, 17, 21, 25, 28, 31,
        35, 38, 41, 44, 47, 51, 54, 57, 60), que permite citar por número.
     3. LA LETRA debajo del pentagrama, sílaba a sílaba.

   Comprobado a ojo sobre las cuatro páginas: ♩=72, armadura de un bemol
   (Re menor), 4/4 hasta el c. 61, el c. 62 cambia a 5/4, y la pieza acaba en
   el c. 63. Marcas de 8vb sobre la derecha en los cc. 7-8 y 15-16. Tresillos
   marcados con un 3 en los cc. 21, 23 y 60.

   Lo que NO se cita: las alturas de la melodía (corcheas y semicorcheas muy
   densas, con ligaduras) y el voicing exacto de la izquierda (cabezas huecas).
   Donde hacen falta notas concretas para un ejercicio, va rotulado ANDAMIO.
   El BAJO, en cambio, no es andamio: lo dice el cifrado.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
REm = 'Re menor'
_B = [3100]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='h'):
    return {'pitches': list(ps), 'dur': d}


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


# --- el bajo, que viene IMPRESO en el cifrado -------------------------------
# ciclo de la estrofa: |Dm  Fmaj7/A |Si b  F/A |Gm7 |F |
BAJO_ESTROFA = [n('D3', 'h'), n('A2', 'h'),
                n('Bb2', 'h'), n('A2', 'h'),
                n('G2', 'w'),
                n('F2', 'w')]

# estribillo cc. 25-30: |F Am6 |Si b  C |F Am6 |Si b  C |Dm7 Am |Si bmaj7 Si bm|
BAJO_ESTRIBILLO = [n('F2', 'h'), n('A2', 'h'),
                   n('Bb2', 'h'), n('C3', 'h'),
                   n('F2', 'h'), n('A2', 'h'),
                   n('Bb2', 'h'), n('C3', 'h'),
                   n('D3', 'h'), n('A2', 'h'),
                   n('Bb2', 'h'), n('Bb2', 'h')]

# cc. 31-34: |Gm7 |C  A/Do# |Dm  F/Do |Si b  F/La |
BAJO_ESTRIBILLO2 = [n('G2', 'w'),
                    n('C3', 'h'), n('C#3', 'h'),
                    n('D3', 'h'), n('C3', 'h'),
                    n('Bb2', 'h'), n('A2', 'h')]

# los acordes de los que el cifrado no deja ninguna duda
DM = ['D3', 'F3', 'A3']
SIb = ['Bb2', 'D3', 'F3']
FA = ['F2', 'A2', 'C3']
GM7 = ['G2', 'Bb2', 'D3', 'F3']
DO = ['C3', 'E3', 'G3']
LA = ['C#3', 'E3', 'A3']          # A mayor en primera inversión: A/Do#
DM7 = ['D3', 'F3', 'A3', 'C4']
LAm = ['A2', 'C3', 'E3']

CANCION = dict(
    alumno='Eva', num=10, nivel='avanzado', slug='WhenWeWereYoung',
    titulo_corto='When We Were Young', time_sig=(4, 4), key_sig=REm,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'WHEN WE WERE YOUNG _ Adele Dm .pdf'),
    yt='https://www.youtube.com/results?search_query=adele+when+we+were+young',

    ficha=dict(
        titulo='When We Were Young',
        autor='Adele (2015) · arr. musicaparadisfrutar.com',
        datos=[('Tonalidad', 'Re menor'), ('Compás', '4/4 · y 5/4 en el c. 62'),
               ('Tempo', '♩ = 72'), ('Compases', '63'), ('Páginas', 'cuatro')],
        total_compases=63,
        secciones=[
            ('Intro', 1, 4, 'El ciclo, sin cantar', OCRE),
            ('Estrofa', 5, 20, 'El mismo ciclo, cuatro vueltas', AZUL),
            ('Puente', 21, 24, 'Si♭ · Do · La m7 · aquí llegan los tresillos', OCRE),
            ('Estribillo', 25, 37, '“When we were young” · aparece el Do♯', AZUL),
            ('Todo otra vez', 38, 63, 'Se repite y se cierra en 5/4', OCRE),
        ],
        armonia=dict(
            titulo='El cifrado está impreso: la armonía te la dan hecha',
            tarjetas=[
                ('EL CICLO', 'Dm · Fmaj7/A · Si♭ · F/A · Gm7 · F',
                 'Cuatro compases. Se repite cuatro veces seguidas, de los cc. 5 al 20.'),
                ('EL BAJO BAJA', 'Re · La · Si♭ · La · Sol · Fa',
                 'Ese ciclo, leído solo por abajo, es una línea que desciende. Ahí está la canción.'),
                ('EL DO♯', 'A /Do♯ · cc. 32 y 36',
                 'La única nota de fuera de la tonalidad. Es la que hace que duela el estribillo.'),
                ('EL C. 62', 'Cambia a 5/4',
                 'Un solo compás de cinco tiempos, justo antes del final. Si no lo cuentas, te caes.'),
            ],
            pie='Esta edición escribe el acorde encima de cada compás y pone el bajo detrás de la '
                'barra cuando es una inversión (Fmaj7/A, F/A, A/Do♯, F/Do). Eso significa que la línea '
                'del bajo entera está impresa en letras: no hay que sacarla de oído ni leerla nota a '
                'nota, solo entenderla.',
        ),
        ritmos=[
            ('MI', 'dos blancas por compás · el bajo lo dice el cifrado',
             [n('D3', 'h'), n('A2', 'h')], OCRE, 'bass', REm),
            ('MD', 'corcheas seguidas, casi sin respirar (andamio)',
             corch(['A4', 'A4', 'Bb4', 'A4', 'G4', 'F4', 'G4', 'A4']), AZUL, 'treble', REm),
        ],
        especial=[
            'Armadura de un bemol: todos los Si son ♭. Estamos en Re menor.',
            'El cifrado está impreso encima de cada compás, con el bajo de las inversiones.',
            'La letra va debajo del pentagrama, sílaba a sílaba: úsala para el fraseo.',
            'Hay una marca de 8vb sobre la derecha en los cc. 7–8 y en los cc. 15–16.',
            'Tresillos marcados con un 3 en los cc. 21, 23 y 60.',
            'El c. 62 cambia a 5/4 y es el único compás de cinco tiempos de la pieza.',
            'La izquierda va casi siempre en blancas: dos golpes por compás y nada más.',
        ],
        reto='Aguantar cuatro páginas sin perder el sitio. La derecha lleva corcheas seguidas con letra '
             'y casi sin silencios: es la pieza más larga de tu álbum, y lo que cansa no son las notas, '
             'es no saber por dónde vas.',
        truco='Aprende la canción por el CIFRADO antes de leer una sola nota. Toca el bajo solo, dos '
              'blancas por compás, siguiendo las letras de encima: en veinte minutos te sabes la pieza '
              'entera de memoria. A partir de ahí, leer la melodía es leer una sola línea sobre un '
              'terreno que ya conoces.',
        sabias='Adele la escribió a los veintiséis años, y va justamente de mirar atrás. En el disco la '
               'acompaña un piano que casi no se mueve, exactamente como esta edición: la voz lo hace '
               'todo y el piano solo sostiene por debajo.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en que el piano nunca compite con la voz. Ni una sola vez.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Esta partitura trae el cifrado impreso encima de cada compás, y con el bajo escrito '
              'cuando el acorde va invertido. Eso es un regalo: la armonía entera te la dan hecha. Por '
              'eso aquí se empieza por el bajo y por los acordes, no por la melodía — cuando conoces el '
              'terreno, leer cuatro páginas de corcheas deja de dar miedo.',
        reglas=['EL BAJO ESTÁ EN EL CIFRADO', 'DOS BLANCAS POR COMPÁS', '♩ = 72, Y NO MÁS'],
        bloques=[
            dict(num=1, titulo='El ciclo de la estrofa, por abajo', clef='bass',
                 pista='cc. 5–8 · el bajo lo dice el cifrado: Dm · Fmaj7/A · Si♭ · F/A · Gm7 · F',
                 sistemas=[
                     dict(cap='a) solo el bajo · Re · La · Si♭ · La · Sol · Fa: léelo entero y verás '
                              'que es una línea que baja',
                          events=BAJO_ESTROFA, bars=4, clef='bass'),
                     dict(cap='b) y con el acorde encima (andamio: el voicing exacto míralo en la '
                              'partitura) · el bajo sigue siendo el mismo',
                          events=[ac(DM), ac(['A2', 'E3', 'F3']),
                                  ac(SIb), ac(['A2', 'C3', 'F3']),
                                  ac(GM7, 'w'), ac(FA, 'w')],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y ahora cuatro veces seguidas · eso son los cc. 5 al 20, la estrofa '
                              'entera: dieciséis compases y un solo ciclo',
                          events=BAJO_ESTROFA * 2, bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LO QUE ESTA EDICIÓN TE DA Y OTRAS NO',
                 texto='El acorde escrito encima del compás, y con el bajo detrás de la barra cuando va '
                       'invertido: Fmaj7/A quiere decir acorde de Fa con La en el bajo. Súmalos todos y '
                       'tienes la línea del bajo de la canción entera, impresa en letras. Apréndete eso '
                       'primero: los cc. 5 al 20 son cuatro vueltas del MISMO ciclo, y la cuarta solo '
                       'cambia el último acorde, que en el c. 20 es Do en vez de Fa.'),
            dict(num=2, titulo='El estribillo, también por abajo', clef='bass',
                 pista='cc. 25–30 · aquí el bajo deja de bajar y empieza a moverse a saltos',
                 sistemas=[
                     dict(cap='a) el bajo de los cc. 25–30 · Fa · La · Si♭ · Do, dos veces, y luego '
                              'Re · La · Si♭ · Si♭',
                          events=BAJO_ESTRIBILLO, bars=6, clef='bass'),
                     dict(cap='b) y el puente de los cc. 21–24, que es lo que lleva hasta aquí · '
                              'Si♭ · Do · La · Si♭, dos veces: es donde están los tresillos',
                          events=[n('Bb2', 'h'), n('C3', 'h'), n('A2', 'h'), n('Bb2', 'h'),
                                  n('Bb2', 'h'), n('C3', 'h'), n('A2', 'h'), n('C3', 'h')],
                          bars=4, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='Queda el sitio donde la canción se sale de la tonalidad —que es el que hay que oír bien— '
              'y el final, que cambia de compás en el penúltimo. Los dos se estudian aparte, y los dos '
              'se aprenden en cinco minutos si sabes lo que estás mirando.',
        reglas=['EL DO♯ NO ES UN ERROR', 'EL C. 62 TIENE CINCO TIEMPOS', 'CUENTA EN VOZ ALTA'],
        bloques=[
            dict(num=3, titulo='Los cc. 31–34, donde aparece el Do♯', clef='bass',
                 pista='Gm7 · C · A/Do♯ · Dm · F/Do · Si♭ · F/La · el Do♯ es la única nota de fuera',
                 sistemas=[
                     dict(cap='a) el bajo · Sol · Do · Do♯ · Re: tres notas seguidas subiendo de medio '
                              'en medio tono, y por eso empuja tanto hacia el Re',
                          events=BAJO_ESTRIBILLO2, bars=4, clef='bass'),
                     dict(cap='b) y con los acordes (andamio) · escucha el La MAYOR del c. 32: en una '
                              'canción en Re menor, ese acorde es el que hace que duela',
                          events=[ac(GM7, 'w'), ac(DO), ac(LA),
                                  ac(DM), ac(['C3', 'F3', 'A3']),
                                  ac(SIb), ac(['A2', 'C3', 'F3'])],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESE DO♯ LO CAMBIA TODO',
                 texto='La armadura no lo lleva: está escrito a mano en la partitura. Es la tercera del '
                       'acorde de La mayor, y La mayor es la dominante de Re menor — el acorde que pide '
                       'volver a casa. Por eso justo detrás viene el Dm del c. 33. Cuando toques ese '
                       'compás, no lo pases de largo: es el punto más tenso de la canción, y aparece '
                       'dos veces, en el c. 32 y en el c. 36.'),
            dict(num=4, titulo='El final, y el compás de cinco tiempos', clef='bass',
                 pista='cc. 60–63 · Si♭maj7 · Si♭m · Gm7 · Do · Fa, y el c. 62 va en 5/4',
                 sistemas=[
                     dict(cap='a) los cc. 60 y 61 · el Si♭m del c. 60 es el otro acorde prestado de la '
                              'pieza: el mismo Si♭ de siempre, pero menor',
                          events=[ac(['Bb2', 'D3', 'F3', 'A3'], 'h'), ac(['Bb2', 'Db3', 'F3'], 'h'),
                                  ac(GM7, 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) y el c. 62, que tiene CINCO tiempos · la izquierda son dos golpes, '
                              'blanca y blanca con puntillo: dos más tres. Detrás ya solo queda el Fa',
                          events=[ac(DO, 'h'), ac(DO, 'h.')],
                          bars=1, clef='bass', time_sig=(5, 4)),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO NO PERDERSE EN CUATRO PÁGINAS',
                 texto='Marca a lápiz dónde vuelve a empezar cada cosa: cc. 5–20 son cuatro vueltas del '
                       'ciclo; los cc. 25–30 y los cc. 51–56 son el mismo estribillo; los cc. 31–37 y '
                       'los cc. 47–50 son el “when we were young”. De sesenta y tres compases, material '
                       'distinto hay menos de veinte. Y usa la letra: cada sílaba está debajo de su '
                       'nota, así que si te pierdes leyendo, canta y vuelve a engancharte.'),
            dict(tipo='escalera', valores=[48, 54, 60, 64, 68, 72],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
