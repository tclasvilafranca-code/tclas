# -*- coding: utf-8 -*-
"""Thinking Out Loud (Ed Sheeran) — dosier de Dilan, nivel avanzado.

   Ver TRANSCRIPCION_D04_THINKING.md. Esta cancion no va de notas: va de
   RITMO y de SOSTENER. La izquierda casi no se mueve y la derecha entra a
   contratiempo con tresillos. Por eso el cuaderno no cita ni una nota de la
   melodia (no esta medida) y en cambio trabaja a fondo su ritmo, que se ve
   sin ninguna ambiguedad.

   Con armadura de Re mayor los Fa y los Do se escriben sin sostenido.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
RE = 'Re mayor'
R = {'rest': True, 'dur': 'q'}
Rh = {'rest': True, 'dur': 'h'}
_B = [800]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


# --- lo unico literal que se cita de la izquierda: la nota grave sostenida --
SOSTEN = [n('D2', 'w'), n('D2', 'w'), n('A2', 'w'), n('A2', 'w')]

# el ritmo de entrada de la derecha: silencio primero, y entra en el 3er tiempo
CONTRA = [Rh, n('D4', 'e'), n('E4', 'e'), n('F4', 'q'),
          n('G4', 'q'), n('F4', 'q'), n('E4', 'h'),
          Rh, n('D4', 'e'), n('E4', 'e'), n('F4', 'q'),
          n('A4', 'h.'), n('G4', 'q')]

CANCION = dict(
    alumno='Dilan', num=4, nivel='avanzado',
    slug='ThinkingOutLoud', titulo_corto='Thinking Out Loud',
    time_sig=(4, 4), key_sig=RE,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' THINKING OUT LOUD _ Ed Sheeran_.pdf'),
    yt='https://www.youtube.com/results?search_query=ed+sheeran+thinking+out+loud',

    ficha=dict(
        titulo='Thinking Out Loud',
        autor='Ed Sheeran y Amy Wadge (2014)',
        datos=[('Tonalidad', 'Re mayor'), ('Compás', '4/4'), ('Tempo', '♩=145'),
               ('Compases', '55'), ('Mano izq.', 'Sostener')],
        secciones=None, total_compases=None,
        armonia=dict(
            titulo='De qué va de verdad esta canción',
            tarjetas=[
                ('LA IZQUIERDA', 'Sostener',
                 'Blanca con puntillo y redondas ligadas. Toca poquísimo y deja sonar mucho.'),
                ('LA DERECHA', 'A contratiempo',
                 'Casi ningún compás empieza con nota: primero hay silencio, y la melodía entra después.'),
                ('EL TRESILLO', 'Tres en dos',
                 'Marcado con un 3. Tres notas en el sitio de dos: es lo que le da el aire hablado.'),
                ('LA FORMA', 'Cuatro compases',
                 'Los cc. 4, 7, 10, 17, 38 y 41 son idénticos. Aprendes cuatro y tienes media canción.'),
            ],
            pie='Aquí no hay ninguna dificultad de dedos: hay una dificultad de reloj. Todo lo que suena '
                'raro al principio es porque la mano derecha no cae donde el pie marca. Si el ritmo está, '
                'la canción está.',
        ),
        ritmos=[
            ('MI', 'una nota grave, sostenida dos compases enteros',
             [n('D2', 'w'), n('D2', 'w')], OCRE, 'bass', RE),
            ('MD', 'silencio primero, y la melodía entra después',
             [Rh, n('D4', 'e'), n('E4', 'e'), n('F4', 'q')], AZUL, 'treble', RE),
            ('EL ACENTO', 'ocho corcheas, pero agrupadas de tres en tres',
             [{'pitch': p, 'dur': 'e', 'beam': b} for p, b in
              [('B4', 71), ('B4', 71), ('B4', 71),
               ('A4', 72), ('A4', 72), ('A4', 72), ('B4', 73), ('B4', 73)]], AZUL, 'treble', RE),
        ],
        especial=[
            'Armadura de dos sostenidos: todos los Fa y los Do son ♯.',
            'La izquierda son notas LIGADAS: se atacan una vez y siguen sonando compases enteros.',
            'La derecha entra casi siempre después del primer tiempo, no en él.',
            'Hay TRESILLOS marcados con un 3: tres notas donde caben dos.',
            'Pone ♩=145, pero la armonía cambia cada dos compases: la sensación es la mitad de rápida.',
            'Seis compases de la pieza son exactamente iguales entre sí (cc. 4, 7, 10, 17, 38, 41).',
            'Casi todo lo que suena lleno lo hace el pedal, no la mano: la izquierda ataca una nota y '
            'se queda quieta compases enteros.',
        ],
        reto='Que la mano derecha entre tarde a propósito y no por despiste. Toda la gracia de esta '
             'canción está en que la melodía llega un poco después de donde la esperas, y eso solo sale '
             'si por dentro estás contando el tiempo que te saltas.',
        truco='Cuenta los cuatro tiempos en voz alta y toca solo en los que toca, dejando los demás en '
              'silencio pero contándolos igual. Y para los tresillos, di "man-za-na" mientras el pie '
              'marca dos: tres sílabas en el sitio de dos golpes.',
        sabias='Ed Sheeran la escribió con Amy Wadge en el sofá de su casa, en una tarde. Wadge había '
               'ido a visitarle y se puso a tocar el riff mientras esperaba; en veinte minutos tenían la '
               'canción. Es la primera que llegó a mil millones de reproducciones en Spotify.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en el piano: toca poquísimo y suena lleno. Eso es el pedal.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Esta canción no pide dedos, pide reloj: '
              'aquí se trabajan por separado el entrar tarde y el acento desplazado, con notas fáciles, '
              'para que cuando llegues a la partitura el ritmo ya no sea el problema.',
        reglas=['ARMADURA DE RE: FA♯ Y DO♯', 'CUENTA SIEMPRE EN VOZ ALTA', 'EL PIE NO SE PARA'],
        ejercicios=[
            dict(num=1, titulo='Escala de Re mayor · dos octavas', clef='bass',
                 pista='manos separadas · el pulgar por debajo sin que se oiga el bache',
                 events=corch(['D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3']) +
                        corch(['E3', 'F3', 'G3', 'A3', 'G3', 'F3', 'E3', 'D3']) +
                        corch(['C3', 'B2', 'A2', 'G2', 'F2', 'E2', 'D2', 'D2']),
                 bars_per_line=3),
            dict(num=2, titulo='Entrar tarde, a propósito',
                 pista='el gesto de la canción · el compás empieza en silencio y tú entras después',
                 events=[Rh, n('D4'), n('E4'), Rh, n('F4'), n('G4'),
                         Rh, n('A4'), n('G4'), Rh, n('F4'), n('E4'),
                         {'rest': True, 'dur': 'q'}, n('D4'), n('E4'), n('F4'),
                         n('D4', 'w')],
                 bars_per_line=3),
            dict(num=3, titulo='Agrupar de tres en tres',
                 pista='ocho corcheas agrupadas 3+3+2 · el acento cae donde no lo esperas',
                 events=[{'pitch': p, 'dur': 'e', 'beam': b} for p, b in
                         [('D4', 91), ('E4', 91), ('F4', 91),
                          ('G4', 92), ('F4', 92), ('E4', 92), ('D4', 93), ('E4', 93)]] +
                        [{'pitch': p, 'dur': 'e', 'beam': b} for p, b in
                         [('F4', 94), ('G4', 94), ('A4', 94),
                          ('G4', 95), ('F4', 95), ('E4', 95), ('F4', 96), ('G4', 96)]] +
                        [n('D4', 'w')],
                 bars_per_line=3),
            dict(num=4, titulo='Sostener sin volver a tocar', clef='bass',
                 pista='el gesto de la izquierda, por otros grados · una vez, y dejar sonar',
                 events=[n('E2', 'w'), n('B2', 'w'), n('C3', 'w'), n('A2', 'w'),
                         n('F2', 'w'), n('C3', 'w'), n('D3', 'w'), n('B2', 'w')],
                 bars_per_line=8),
            dict(num=5, titulo='Los acordes de la tonalidad, sostenidos', clef='bass',
                 pista='tríadas de Re mayor grado a grado · se atacan una vez y se dejan sonar',
                 events=[{'pitches': list(t), 'dur': 'w'} for t in
                         [('D2', 'A2', 'D3'), ('E2', 'B2', 'E3'), ('F2', 'C3', 'F3'),
                          ('G2', 'D3', 'G3'), ('A2', 'E3', 'A3'), ('B2', 'F3', 'B3'),
                          ('A2', 'E3', 'A3'), ('D2', 'A2', 'D3')]],
                 bars_per_line=8),
            dict(num=6, titulo='La misma nota, entrando cada vez más tarde',
                 pista='en el uno, en el dos, en el tres, en el cuatro · el pie no se para',
                 events=[n('A4'), n('A4', 'h.'),
                         R, n('A4'), n('A4', 'h'),
                         Rh, n('A4'), n('A4'),
                         {'rest': True, 'dur': 'h.'}, n('A4'),
                         n('A4', 'w')],
                 bars_per_line=5),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con dos sostenidos. '
              'Abajo se escucha, y aquí lo que se entrena no son notas: es el reloj.',
        sub_leer='di el nombre en voz alta · armadura de Re: Fa y Do son ♯',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO GRAVE DE LA MANO IZQUIERDA (CLAVE DE FA)',
        chuleta_pitches=['D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3'],
        chuleta_nombres=['Re', 'Mi', 'Fa♯', 'Sol', 'La', 'Si', 'Do♯', 'Re', 'Mi'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa, registro grave', clef='bass',
                 pista='la izquierda de esta canción vive abajo · con líneas adicionales',
                 events=[n(p) for p in ('D2', 'A2', 'F2', 'C3', 'E2', 'B2', 'G2', 'D3',
                                        'F3', 'A2', 'E3', 'D2', 'C3', 'G2', 'B2', 'F2')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · orden irregular a propósito',
                 events=[n(p) for p in ('D4', 'A4', 'F4', 'D5', 'B4', 'G4', 'E4', 'C5',
                                        'A4', 'F4', 'E5', 'B4', 'G4', 'D4', 'C5', 'A4')]),
            dict(num=3, titulo='Leyendo los silencios',
                 pista='igual que la pieza: casi ningún compás empieza sonando · cuenta los que callas',
                 events=[Rh, n('D4', 'q'), n('E4', 'q'),
                         R, n('F4', 'q'), n('G4', 'h'),
                         Rh, n('A4', 'q'), n('G4', 'q'),
                         n('F4', 'q'), R, n('E4', 'h'),
                         n('D4', 'w')]),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca un acorde marcando cuatro tiempos, y en uno de ellos mete una nota suelta. '
                      'Que diga si esa nota cayó A TIEMPO (con el pulso) o A CONTRATIEMPO (entre dos).'),
                ('B', 'Toca cuatro tiempos iguales y mete DOS notas o TRES en uno. Que diga cuántas eran.'),
                ('C', 'Toca una tríada suelta: mayor o menor. Sigue haciendo falta, aunque aquí el '
                      'problema sea el ritmo.'),
                ('+', 'Y sin escribir: marca tú el pulso y que dé palmas justo entre tus golpes.'),
            ],
            filas=[
                dict(letra='A', titulo='¿A tiempo o a contratiempo?', pista='la nota respecto al pulso que marcas tú',
                     n=10, opciones=['a tiempo', 'contra']),
                dict(letra='B', titulo='¿Dos o tres?', pista='cuántas notas caben en ese tiempo',
                     n=8, opciones=['2', '3']),
                dict(letra='C', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=6, opciones=['M', 'm']),
            ],
        ),
    ),

    piano1=dict(
        intro='La partitura, abierta en trozos. En esta canción los trozos no son de notas: son de '
              'tiempo. Lo único que se cita de la izquierda es la nota grave, que es lo que está '
              'medido sin ninguna duda.',
        reglas=['ARMADURA DE RE', 'TOCA POCO Y DEJA SONAR', 'CUENTA LO QUE NO TOCAS'],
        bloques=[
            dict(num=1, titulo='Lo que sostiene la izquierda',
                 pista='cc. 1–4 · un Re dos compases y un La otros dos · se ataca una vez y ya está',
                 sistemas=[dict(cap='no vuelvas a tocar la nota: es una sola vez y suena cuatro tiempos',
                                events=SOSTEN, bars=4, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ CUESTA TOCAR TAN POCO',
                 texto='La izquierda de esta canción hace cuatro cosas en cuatro compases. Suena a poco, '
                       'pero es lo más difícil de sostener: en cuanto te aburres, vuelves a atacar la nota '
                       '"por si acaso" y se acabó el efecto. La canción tiene que sonar llena sin que tú '
                       'estés haciendo nada, y eso solo pasa si dejas la tecla apoyada y confías en el '
                       'pedal. Ponte un reloj delante y aguanta los cuatro tiempos mirándolo.'),
            dict(num=2, titulo='El contratiempo, desnudo',
                 pista='el ritmo real de la entrada de la melodía, con notas fáciles',
                 sistemas=[dict(cap='silencio de blanca, y entras · cuenta UN-dos-TRES-cuatro en voz alta',
                                events=CONTRA, bars=4)]),
            dict(num=3, titulo='Las dos cosas a la vez',
                 pista='la izquierda quieta mientras la derecha llega tarde · el problema entero de la pieza',
                 sistemas=[dict(cap='a)  primero la izquierda sola, contando los cuatro tiempos',
                                events=[n('D2', 'w'), n('A2', 'w')], bars=2, clef='bass'),
                           dict(cap='b)  ahora la derecha sola, encima de ese mismo silencio mental',
                                events=[Rh, n('D4', 'e'), n('E4', 'e'), n('F4', 'q'),
                                        n('G4', 'h.'), n('E4', 'q')], bars=2)]),
            dict(tipo='nota',
                 etiqueta='EL PEDAL ES LA TERCERA MANO',
                 texto='Escucha la grabación con auriculares y fíjate en el piano: suena lleno todo el '
                       'rato y sin embargo casi no se mueve nada. Eso no lo hace la mano, lo hace el pie. '
                       'La izquierda ataca una nota grave y la deja; el pedal se encarga de que siga '
                       'sonando mientras la derecha canta por encima. Si tocas esta canción sin pedal vas '
                       'a pensar que la partitura está mal, porque suena vacía. No está mal: falta el pie.'),
            dict(num=4, titulo='El acento que se corre de sitio',
                 pista='ocho corcheas iguales, pero agrupadas 3+3+2 · aprieta un poco la primera de cada grupo',
                 sistemas=[dict(cap='dilo en voz alta: UN-o-o DOS-o-o TRES-o · y que el pie siga marcando '
                                    'cuatro',
                                events=[{'pitch': p, 'dur': 'e', 'beam': b} for p, b in
                                        [('A4', 81), ('A4', 81), ('A4', 81),
                                         ('A4', 82), ('A4', 82), ('A4', 82),
                                         ('A4', 83), ('A4', 83)]] +
                                       [{'pitch': p, 'dur': 'e', 'beam': b} for p, b in
                                        [('B4', 84), ('B4', 84), ('B4', 84),
                                         ('B4', 85), ('B4', 85), ('B4', 85),
                                         ('B4', 86), ('B4', 86)]] +
                                       [n('A4', 'w')],
                                bars=3)]),
        ],
    ),

    piano2=dict(
        intro='Montarla es, en esta canción, entender que hay muchísimo menos que aprender de lo que '
              'parece: cuatro compases que vuelven una y otra vez.',
        reglas=['CUATRO COMPASES SON MEDIA CANCIÓN', 'EL PEDAL CAMBIA CON EL BAJO', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(tipo='nota',
                 etiqueta='HAY MENOS QUE APRENDER DE LO QUE PARECE',
                 texto='Comparando la partitura compás a compás salen seis compases exactamente iguales '
                       '(los cc. 4, 7, 10, 17, 38 y 41) y otros tres más (39, 42 y 45). La canción está '
                       'construida sobre una célula de cuatro compases que vuelve todo el rato. Antes de '
                       'estudiar nada, marca con lápiz en tu partitura los compases que se repiten: vas a '
                       'ver que lo nuevo de verdad es muy poco.'),
            dict(num=5, titulo='El cambio de pedal',
                 pista='el pedal se cambia cuando cambia la nota grave, no cuando cambia la melodía',
                 sistemas=[dict(cap='pisa al atacar, suelta y vuelve a pisar justo al cambiar de nota grave',
                                events=[n('D2', 'w'), n('A2', 'w'), n('B2', 'w'), n('G2', 'w'),
                                        n('D2', 'w'), n('A2', 'w'), n('G2', 'w'), n('D2', 'w')],
                                bars=4, clef='bass')]),
            dict(tipo='nota',
                 etiqueta='LA CÉLULA DE CUATRO COMPASES',
                 texto='La canción entera está montada sobre un ciclo de cuatro compases de armonía que '
                       'da vueltas: cambia la letra, cambia la melodía, pero la izquierda vuelve al mismo '
                       'sitio cada cuatro. Cuando lo sepas, deja de leer la izquierda y tócala de memoria: '
                       'vas a poder mirar solo la mano derecha, que es donde de verdad pasan cosas, y la '
                       'canción se vuelve la mitad de difícil de un día para otro.'),
            dict(tipo='nota',
                 etiqueta='CÓMO ESTUDIARLA ESTA SEMANA',
                 texto='1 · Marca en la partitura los compases repetidos. '
                       '2 · La izquierda sola de los cuatro primeros, contando en voz alta los tiempos '
                       'que no tocas. '
                       '3 · El ritmo de la derecha sin piano: dando palmas. '
                       '4 · Las dos manos solo de esos cuatro compases. '
                       '5 · Y una vez al día, tócalos con los ojos cerrados: si el ritmo está por dentro, '
                       'no necesitas mirar.'),
            dict(num=6, titulo='Cuatro entradas seguidas, sin parar',
                 pista='andamio · cuatro frases que empiezan tarde, encadenadas · no pares entre medias',
                 sistemas=[dict(cap='el compás que callas también se cuenta: si paras a pensar, ya has '
                                    'perdido el sitio',
                                events=[Rh, n('A4'), n('B4'),
                                        Rh, n('D5'), n('B4'),
                                        R, n('A4'), n('G4', 'h'),
                                        n('F4', 'h'), n('E4', 'h'),
                                        n('D4', 'w')],
                                bars=5)]),
            dict(tipo='escalera', valores=[80, 96, 110, 122, 134, 145],
                 regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='tracker', titulo='La prueba de la semana',
                 pie='Marca el día en que hayas tocado los cuatro primeros compases sin adelantar la entrada.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
