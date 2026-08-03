# -*- coding: utf-8 -*-
"""Your Song (Elton John) — dosier de Dilan, nivel avanzado.

   Todo lo musical sale de TRANSCRIPCION_D03_YOUR_SONG.md. La melodia NO se
   cita: va en semicorcheas con tresillos y no esta medida. Lo que si esta
   verificado, porque lo imprime la propia edicion, es el cifrado y con el la
   LINEA DE BAJO, que es la firma de esta cancion.

   Con armadura de Mi bemol mayor, los Si, Mi y La se escriben SIN bemol.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir, OUT_DIR                                # noqa

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
MIb = 'Mib mayor'
_B = [700]


def bloque(notas, dur='h'):
    return [{'pitches': list(notas), 'dur': dur}]


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


def neg(*ps):
    return [{'pitch': p, 'dur': 'q'} for p in ps]


# --- la linea de bajo, que es lo unico literal que se cita ----------------
# Si y La llevan bemol por armadura; el La NATURAL de Cm/A va con becuadro
BAJO_CROM = [{'pitch': 'C3', 'dur': 'h'}, {'pitch': 'B2', 'dur': 'h'},
             {'pitch': 'An2', 'dur': 'h'}, {'pitch': 'A2', 'dur': 'h'}]
BAJO_MIb = [{'pitch': 'E3', 'dur': 'h'}, {'pitch': 'D3', 'dur': 'h'},
            {'pitch': 'C3', 'dur': 'h'}, {'pitch': 'C3', 'dur': 'h'}]

# El bajo de la estrofa ENTERA, leido de los cifrados impresos:
#   Eb · Ab | Bb · Gm | Cm · Cm/Bb | Cm/A · Ab | Eb/Bb · Bb | G/B · Cm | Eb · Fm | Ab · Bb
# Los Si, Mi y La son bemoles por armadura; los dos naturales van marcados.
BAJO_ESTROFA = [{'pitch': p, 'dur': 'h'} for p in
                ('E3', 'A2', 'B2', 'G2', 'C3', 'B2', 'An2', 'A2',
                 'B2', 'B2', 'Bn2', 'C3', 'E3', 'F2', 'A2', 'B2')]

# acordes de la cancion en bloque (DERIVADOS del cifrado, para el calentamiento)
ACORDES = [('E3', 'G3', 'B3'), ('A2', 'C3', 'E3'), ('B2', 'D3', 'F3'),
           ('G2', 'B2', 'D3'), ('C3', 'E3', 'G3'), ('F2', 'A2', 'C3')]

CANCION = dict(
    alumno='Dilan', num=3, nivel='avanzado',
    slug='YourSong', titulo_corto='Your Song',
    time_sig=(4, 4), key_sig=MIb,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' YOUR SONG _ Elton John_.pdf'),
    yt='https://www.youtube.com/results?search_query=elton+john+your+song',

    ficha=dict(
        titulo='Your Song',
        autor='Elton John y Bernie Taupin (1970) · edición con cifrados',
        datos=[('Tonalidad', 'Mi♭ mayor'), ('Compás', '4/4 (y 2/4)'),
               ('Tempo', '♩=66'), ('Mano izq.', 'Acordes en blancas'),
               ('Estructura', 'Segno + casillas')],
        armonia=dict(
            titulo='La línea de bajo: la firma de la canción',
            tarjetas=[
                ('Cm → Cm/B♭', 'Do → Si♭',
                 'El acorde no cambia; lo que baja es el bajo. Por eso suena a que algo se mueve.'),
                ('Cm/A → A♭', 'La♮ → La♭',
                 'El La es NATURAL: va contra la armadura y está escrito. Es la nota más bonita del tramo.'),
                ('E♭ → B♭/D → Cm', 'Mi♭ → Re → Do',
                 'Otra bajada por grados, esta vez sin alteraciones.'),
                ('Qué significa la barra', 'Acorde / bajo',
                 'Cm/B♭ = acorde de Do menor, pero con Si♭ abajo. La mano izquierda manda.'),
            ],
            pie='Los cifrados con barra no son un adorno del editor: escriben un bajo que desciende por '
                'grados mientras la armonía casi no se mueve. Si tocas solo esos bajos seguidos, ya se '
                'reconoce la canción. Ese es el truco de Elton John aquí, y el que hay que oír antes de '
                'ponerse a tocar acordes.',
        ),
        ritmos=[
            ('MI', 'dos acordes por compás, en blancas',
             bloque(('C3', 'E3', 'G3')) + bloque(('B2', 'D3', 'F3')), OCRE, 'bass', MIb),
            ('BAJO', 'y el bajo, que baja un grado: Do → Si♭',
             [{'pitch': 'C3', 'dur': 'h'}, {'pitch': 'B2', 'dur': 'h'}], AZUL, 'bass', MIb),
        ],
        especial=[
            'Armadura de TRES bemoles: todos los Si, los Mi y los La son ♭.',
            'La edición trae los cifrados impresos, incluidos los de bajo alterado.',
            'Hay compases sueltos de 2/4 en medio del 4/4: cuenta, no te dejes llevar.',
            'Lleva SEGNO y casillas 1ª y 2ª: hay que saber leer el recorrido antes de tocar.',
            'La derecha va en semicorcheas y con tresillos marcados; la izquierda, en blancas.',
            'El La♮ del acorde Cm/A es una alteración accidental, no un error de imprenta.',
        ],
        reto='Leer el recorrido. Entre el segno, la repetición y las dos casillas, esta partitura se '
             'toca en un orden que no es el orden en que está escrita. Si eso no está claro, da igual '
             'lo bien que salgan las notas.',
        truco='Antes de tocar nada, sigue la partitura con el dedo y di en voz alta por dónde vas: '
              '"intro, segno, estrofa, casilla 1, vuelvo al segno, casilla 2". Y estudia la mano '
              'izquierda tocando SOLO el bajo de cada acorde: si esa línea suena bien, el resto es relleno.',
        sabias='Bernie Taupin escribió la letra en el desayuno, en el tejado de la casa de la madre de '
               'Elton John, en 1967. Tardó unos veinte minutos. Elton John compuso la música en otros '
               'diez, y en la hoja original todavía se ven las manchas del café.',
        qr=dict(titulo='Escucha la versión original',
                texto='Fíjate en el bajo del piano: baja por grados casi todo el rato.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. La tonalidad es Mi♭ mayor, tres bemoles, y '
              'el gesto de la canción es un bajo que baja mientras la armonía se queda quieta. Aquí se '
              'trabaja ese gesto por toda la tonalidad, no solo donde la pieza lo usa.',
        reglas=['ARMADURA DE MI♭: SI, MI Y LA SON ♭', 'MANOS SEPARADAS', 'EL BAJO MANDA'],
        ejercicios=[
            dict(num=1, titulo='Escala de Mi♭ mayor · dos octavas', clef='bass',
                 pista='manos separadas · tres bemoles, y el pulgar por debajo sin bache',
                 events=corch(['E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4']) +
                        corch(['D4', 'C4', 'B3', 'A3', 'G3', 'F3', 'E3', 'E3']),
                 bars_per_line=4),
            dict(num=2, titulo='Los acordes de la canción, en bloque', clef='bass',
                 pista='Mi♭ · La♭ · Si♭ · Sol m · Do m · Fa m · las seis casas que visita la pieza',
                 events=[e for t in ACORDES for e in bloque(t)] +
                        [e for t in reversed(ACORDES) for e in bloque(t)],
                 bars_per_line=6),
            dict(num=3, titulo='Bajo que baja, acorde que no se mueve', clef='bass',
                 pista='el gesto de la pieza por toda la escala · quieto el acorde, andando el bajo',
                 events=neg('E3', 'D3', 'C3', 'B2') + neg('A2', 'G2', 'F2', 'E2') +
                        neg('F2', 'G2', 'A2', 'B2') + neg('C3', 'D3', 'E3', 'E3'),
                 bars_per_line=4),
            dict(num=4, titulo='Terceras dobles en Mi♭',
                 pista='lo que la pieza no te da · las dos notas exactamente juntas',
                 events=[{'pitches': list(d), 'dur': 'q'} for d in
                         [('E4', 'G4'), ('F4', 'A4'), ('G4', 'B4'), ('A4', 'C5'),
                          ('B4', 'D5'), ('C5', 'E5'), ('B4', 'D5'), ('A4', 'C5'),
                          ('G4', 'B4'), ('F4', 'A4'), ('E4', 'G4'), ('E4', 'G4')]],
                 bars_per_line=3),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con tres bemoles. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · armadura de Mi♭: Si, Mi y La son bemol',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DE LA MANO IZQUIERDA (CLAVE DE FA)',
        chuleta_pitches=['F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3'],
        chuleta_nombres=['Fa', 'Sol', 'La♭', 'Si♭', 'Do', 'Re', 'Mi♭', 'Fa', 'Sol', 'La♭'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa', clef='bass',
                 pista='donde viven los acordes · orden irregular a propósito',
                 events=neg('C3', 'G2', 'E3', 'B2', 'F3', 'A2', 'D3', 'G3', 'F2', 'C3',
                            'A3', 'E3', 'B2', 'D3', 'G2', 'F3')),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · registro alto, con líneas adicionales',
                 events=neg('E4', 'B4', 'G4', 'E5', 'C5', 'A4', 'F4', 'D5', 'G4', 'C5',
                            'B4', 'F5', 'A4', 'D4', 'E5', 'G4')),
            dict(num=3, titulo='Con el La natural',
                 pista='el ♮ del acorde Cm/A · una alteración accidental dura hasta la barra, no más',
                 events=[{'pitch': 'C3', 'dur': 'q'}, {'pitch': 'B2', 'dur': 'h'},
                         {'pitch': 'A2', 'dur': 'q'},
                         {'pitch': 'An2', 'dur': 'q'}, {'pitch': 'C3', 'dur': 'q'},
                         {'pitch': 'E3', 'dur': 'h'},
                         {'pitch': 'G3', 'dur': 'q'}, {'pitch': 'F3', 'dur': 'q'},
                         {'pitch': 'D3', 'dur': 'h'},
                         {'pitch': 'C3', 'dur': 'w'}],
                 clef='bass'),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca dos acordes seguidos moviendo SOLO el bajo (por ejemplo Do m y luego Do m '
                      'con Si♭ abajo). Que diga si el bajo ha bajado, ha subido o se ha quedado igual.'),
                ('B', 'Toca una tríada suelta. Que diga si es MAYOR o MENOR: la canción alterna las dos.'),
                ('C', 'Toca cuatro tiempos. Unas veces en 4/4 y otras en 2/4. Que diga cuál era: '
                      'esta partitura cambia de compás en medio y hay que notarlo.'),
                ('+', 'Y sin escribir: toca solo los bajos Do–Si♭–La♮–La♭ seguidos y que te diga de qué '
                      'canción son. Si los reconoce, ya ha entendido dónde está la pieza.'),
            ],
            filas=[
                dict(letra='A', titulo='¿El bajo sube o baja?', pista='el acorde casi no se mueve · fíjate solo en la nota de abajo',
                     n=10, opciones=['↑', '↓', '=']),
                dict(letra='B', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=8, opciones=['M', 'm']),
                dict(letra='C', titulo='¿4/4 o 2/4?', pista='cuenta los tiempos hasta el siguiente acento',
                     n=6, opciones=['4/4', '2/4']),
            ],
        ),
    ),

    piano1=dict(
        intro='La partitura, abierta en trozos. Aquí no hay melodía: en esta canción la melodía no es '
              'el problema. El problema es la mano izquierda y el recorrido de la hoja.',
        reglas=['ARMADURA DE MI♭', 'TOCA EL BAJO, NO EL ACORDE', 'CUENTA LOS COMPASES DE 2/4'],
        bloques=[
            dict(num=1, titulo='El bajo de la estrofa entera',
                 pista='leído de los cifrados: E♭ · A♭ · B♭ · Gm · Cm · Cm/B♭ · Cm/A · A♭ · E♭/B♭…',
                 sistemas=[dict(cap='una nota por medio compás · esto solo, sin acordes, ya suena a Your Song',
                                events=BAJO_ESTROFA, bars=4, clef='bass')]),
            dict(num=2, titulo='El tramo que baja cromático',
                 pista='cc. de Cm a A♭ · Do · Si♭ · La♮ · La♭ · el La lleva becuadro',
                 sistemas=[dict(cap='dos veces seguidas, escuchando ese La natural: es la nota del tramo',
                                events=BAJO_CROM + [dict(e) for e in BAJO_CROM],
                                bars=4, clef='bass')]),
            dict(num=3, titulo='La otra bajada',
                 pista='E♭ · B♭/D · Cm → Mi♭ · Re · Do · sin alteraciones, más fácil de oír',
                 sistemas=[dict(cap='mismo gesto, otro tramo de la canción',
                                events=BAJO_MIb, bars=2, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE EMPIEZA POR EL BAJO',
                 texto='Un cifrado con barra, como Cm/B♭, dice dos cosas: qué acorde suena y qué nota va '
                       'debajo. La de debajo es la que decide si la canción avanza o se queda parada, y '
                       'es la que el oído sigue. Si montas los acordes completos antes de tener esa línea '
                       'clara, acabas tocando bloques correctos que no van a ninguna parte. Toca solo los '
                       'bajos hasta que te suenen a melodía, y después les pones el acorde encima.'),
            dict(num=4, titulo='El acorde encima del bajo',
                 pista='ahora sí: la tríada completa sobre cada uno de esos bajos',
                 sistemas=[dict(cap='Do m · Do m/Si♭ · Do m/La♮ · La♭ · el acorde apenas cambia',
                                events=bloque(('C3', 'E3', 'G3')) + bloque(('B2', 'E3', 'G3')) +
                                       bloque(('An2', 'E3', 'G3')) + bloque(('A2', 'C3', 'E3')),
                                bars=2, clef='bass')]),
        ],
    ),

    piano2=dict(
        intro='Montarla es, en esta canción, saber por dónde va la hoja. El segno, la repetición y las '
              'dos casillas hacen que se toque en un orden distinto del que está escrito.',
        reglas=['PRIMERO EL RECORRIDO, LUEGO LAS NOTAS', 'EL 2/4 SE CUENTA', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(tipo='nota',
                 etiqueta='EL RECORRIDO DE LA HOJA',
                 texto='1 · Los dos compases de introducción. 2 · Empieza la estrofa: ahí está el SEGNO, '
                       'la marca a la que vas a volver. 3 · Llegas a la casilla 1ª, la tocas y vuelves al '
                       'segno. 4 · La segunda vez te saltas la casilla 1ª y entras por la 2ª. 5 · Sigue el '
                       'puente. Sigue la partitura con el dedo y di en voz alta dónde estás antes de tocar '
                       'una sola nota.'),
            dict(tipo='nota',
                 etiqueta='EL COMPÁS QUE CAMBIA',
                 texto='En medio del 4/4 hay compases sueltos de 2/4: duran la mitad. No están para '
                       'complicarte la vida, están porque la frase cantada acaba antes y el compás se '
                       'ajusta a ella. Cuenta en voz alta UN-dos-tres-cuatro, UN-dos, UN-dos-tres-cuatro '
                       'y verás que no hay nada raro. El error típico es acelerar en el compás corto '
                       'para llegar al siguiente: dura dos tiempos exactos, ni uno menos.'),
            dict(tipo='nota',
                 etiqueta='CÓMO ESTUDIARLA ESTA SEMANA',
                 texto='1 · El recorrido, con el dedo y en voz alta, sin piano. '
                       '2 · Solo los bajos de toda la estrofa. '
                       '3 · Los acordes completos, todavía sin la derecha. '
                       '4 · La derecha sola, despacio, contando los tresillos. '
                       '5 · Las dos manos, pero solo desde el segno hasta la casilla 1ª. El resto, la '
                       'semana que viene.'),
            dict(tipo='escalera', valores=[40, 46, 52, 58, 62, 66],
                 regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='tracker', titulo='La prueba de la semana',
                 pie='Marca el día en que hayas hecho el recorrido entero sin equivocarte de casilla.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
