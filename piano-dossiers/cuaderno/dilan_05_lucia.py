# -*- coding: utf-8 -*-
"""Lucía (Joan Manuel Serrat) — dosier de Dilan, nivel avanzado.

   Ver TRANSCRIPCION_D05_LUCIA.md. La menor, sin armadura. Lo verificado dos
   veces (lector + cifrado impreso) son los acordes de la mano izquierda y,
   sobre todo, que el BAJO oscila Mi-Fa: un semitono que va y viene mientras
   los acordes cambian por encima. Ese es el hallazgo de esta cancion.

   La melodia NO se cita: lleva tresillos y semicorcheas y no esta medida.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloque_tresillos, bloques_extra

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
R = {'rest': True, 'dur': 'q'}
_B = [900]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(notas, d='q', veces=1):
    return [{'pitches': list(notas), 'dur': d} for _ in range(veces)]


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


# --- lo medido: los dos acordes de la primera frase, tal como suenan -------
AmE = ('E3', 'A3', 'C4')        # c. 4 y c. 7 · cifrado Am/E
DmF = ('F3', 'A3', 'D4')        # c. 5        · cifrado Dm/F

# el bajo solo: Mi y Fa, que es todo el secreto
BAJO_MIFA = [n('E3', 'w'), n('F3', 'w'), n('E3', 'w'), n('F3', 'w')]

CANCION = dict(
    alumno='Dilan', num=5, nivel='avanzado',
    slug='Lucia', titulo_corto='Lucía',
    time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' Lucia_.pdf'),
    yt='https://www.youtube.com/results?search_query=joan+manuel+serrat+lucia',

    ficha=dict(
        titulo='Lucía',
        autor='Joan Manuel Serrat (1971) · edición con cifrados',
        datos=[('Tonalidad', 'La menor'), ('Compás', '4/4'), ('Tempo', '♩=75'),
               ('Compases', '36'), ('Mano izq.', '4 acordes/compás')],
        armonia=dict(
            titulo='El bajo que va y viene',
            tarjetas=[
                ('c. 4  ·  Am/E', 'La menor /Mi',
                 'Mi3 · La3 · Do4. El acorde es La menor, pero abajo hay un Mi.'),
                ('c. 5  ·  Dm/F', 'Re menor /Fa',
                 'Fa3 · La3 · Re4. Cambia el acorde y el bajo sube un semitono.'),
                ('EL BAJO', 'Mi → Fa → Mi',
                 'Un semitono que oscila. Casi todos los cifrados llevan barra por eso.'),
                ('POR QUÉ SUENA ASÍ', 'Casi no se mueve',
                 'La armonía cambia mucho y el bajo apenas. De ahí la sensación de balanceo.'),
            ],
            pie='Mira los cifrados de toda la página: Am/E, Dm/F, E7, Am/E, F, G/F, C/E, B°/F, E7. '
                'Casi todos llevan barra, y si te quedas solo con la nota de después de la barra sale '
                'Mi, Fa, Mi, Mi, Fa, Fa, Mi, Fa, Mi. La canción entera se balancea sobre un semitono.',
        ),
        ritmos=[
            ('MI', 'cuatro acordes por compás, en negras',
             ac(AmE, veces=4), OCRE, 'bass', None),
            ('BAJO', 'y debajo, solo dos notas: Mi y Fa',
             [n('E3', 'h'), n('F3', 'h')], AZUL, 'bass', None),
            ('MD', 'la melodía no entra en el uno: entra antes (andamio)',
             [R, R, R, n('A4'), n('C5', 'h'), n('B4', 'h')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay armadura: ni sostenidos ni bemoles de salida. Es La menor.',
            'La izquierda toca CUATRO acordes por compás, todo el rato. Es lo que más cansa.',
            'Casi todos los cifrados llevan barra: el bajo no es la fundamental del acorde.',
            'La melodía empieza en ANACRUSA, antes del primer tiempo del compás.',
            'Hay TRESILLOS marcados con un 3 en la mano derecha.',
            'El E7 lleva Sol♯: es la alteración que hace que quiera volver a La menor.',
            'Los acordes se repiten sin cambiar de posición: la mano se queda colocada y solo '
            'vuelve a apretar. No hay que buscar teclas cuatro veces.',
        ],
        reto='Cuatro acordes por compás durante treinta y seis compases. El problema no es tocarlos: '
             'es que no suenen a máquina. Si los cuatro pesan igual, la canción se convierte en un '
             'metrónomo con acordes.',
        truco='Toca los cuatro acordes de cada compás bajando de volumen: el primero es el que manda y '
              'los otros tres solo lo acompañan. Y estudia aparte la nota de abajo: si sabes en todo '
              'momento si estás en Mi o en Fa, ya no te pierdes.',
        sabias='Serrat la escribió en 1971 y siempre ha dicho que es la canción suya que más quiere. '
               'Lucía no existió: es un nombre que le sonaba bien. La grabó en el disco "Mediterráneo", '
               'que compuso encerrado en una casa de Calafell mirando al mar.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en lo poco que se mueve el bajo mientras todo lo demás cambia.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. La tonalidad es La menor y el gesto de la '
              'canción es un acorde repetido cuatro veces sobre un bajo que apenas se mueve. Aquí se '
              'trabaja ese gesto por toda la tonalidad, no solo donde la pieza lo usa, y se acaba con '
              'las dos únicas notas que sostienen la canción entera.',
        reglas=['SIN ARMADURA · LA MENOR', 'EL PRIMER ACORDE PESA MÁS', 'MANOS SEPARADAS'],
        ejercicios=[
            dict(num=1, titulo='Escala de La menor · dos octavas', clef='bass',
                 pista='manos separadas · sin alteraciones, pero el pulgar tiene que pasar limpio',
                 events=corch(['A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3']) +
                        corch(['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'A4']) +
                        corch(['A4', 'G4', 'F4', 'E4', 'D4', 'C4', 'B3', 'A3']) +
                        corch(['G3', 'F3', 'E3', 'D3', 'C3', 'B2', 'A2', 'A2']),
                 bars_per_line=4),
            dict(num=2, titulo='Cuatro veces el mismo acorde', clef='bass',
                 pista='el gesto de la izquierda · el primero pesa, los otros tres acompañan',
                 events=ac(('A2', 'C3', 'E3'), veces=4) + ac(('B2', 'D3', 'F3'), veces=4) +
                        ac(('C3', 'E3', 'G3'), veces=4) + ac(('D3', 'F3', 'A3'), veces=4),
                 bars_per_line=4),
            dict(num=3, titulo='El bajo se mueve un semitono', clef='bass',
                 pista='lo que hace la pieza todo el rato · el acorde encima apenas cambia',
                 events=ac(('E3', 'A3', 'C4'), veces=2) + ac(('F3', 'A3', 'C4'), veces=2) +
                        ac(('E3', 'A3', 'C4'), veces=2) + ac(('F3', 'A3', 'D4'), veces=2),
                 bars_per_line=2),
            dict(num=4, titulo='El Sol♯ que pide volver',
                 pista='la nota del acorde E7 · sube medio tono y la canción quiere resolver en La',
                 events=[n('E4'), n('G#4'), n('B4'), n('D5'),
                         n('E5', 'h'), n('A4', 'h'),
                         n('D5'), n('B4'), n('G#4'), n('E4'),
                         n('A4', 'w')],
                 bars_per_line=2),
            dict(num=5, titulo='Solo Mi y Fa, en negras', clef='bass',
                 pista='sin acorde encima · el esqueleto de la canción entera son estas dos teclas',
                 events=[n('E3'), n('E3'), n('F3'), n('F3'),
                         n('E3'), n('F3'), n('E3'), n('F3'),
                         n('E3', 'h'), n('F3', 'h'),
                         n('E3'), n('F3'), n('F3'), n('E3'),
                         n('F3'), n('F3'), n('E3'), n('E3'),
                         n('F3'), n('E3'), n('F3'), n('E3'),
                         n('E3', 'h'), n('F3', 'h'),
                         n('E3', 'w')],
                 bars_per_line=4),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves. Abajo se escucha: '
              'lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · sin armadura, pero atención a las alteraciones sueltas',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DE LOS ACORDES (CLAVE DE FA)',
        chuleta_pitches=['A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'C4'],
        chuleta_nombres=['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Do'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa', clef='bass',
                 pista='donde viven los acordes · orden irregular a propósito',
                 events=[n(p) for p in ('E3', 'A3', 'C4', 'F3', 'D3', 'G3', 'B2', 'A2',
                                        'C3', 'E3', 'D4', 'F3', 'A3', 'C3', 'E3', 'B2')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · registro medio-alto',
                 events=[n(p) for p in ('A4', 'C5', 'E5', 'B4', 'D5', 'F5', 'G4', 'E4',
                                        'C5', 'A4', 'D5', 'B4', 'F4', 'E5', 'G4', 'C5')]),
            dict(num=3, titulo='Con el Sol sostenido',
                 pista='el del acorde E7 · una alteración suelta vale hasta la barra de compás',
                 events=[n('E4'), n('G#4', 'h'), n('B4'),
                         n('A4'), n('G4'), n('E4', 'h'),
                         n('D5'), n('B4'), n('G#4'), n('E4'),
                         n('A4', 'w')]),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca un acorde y repítelo cambiando SOLO la nota de abajo un semitono arriba o '
                      'abajo. Que diga hacia dónde se ha movido el bajo. Es el gesto de esta canción.'),
                ('B', 'Toca una tríada suelta: MAYOR o MENOR. La pieza alterna las dos sin avisar.'),
                ('C', 'Toca un acorde de tres notas, y a veces añádele la séptima (como el E7). Que diga '
                      'si sonaba a tres notas o a cuatro: la cuarta es la que pide resolver.'),
                ('+', 'Y sin escribir: toca solo Mi y Fa alternando, con el pulso de la canción, y que '
                      'reconozca de qué pieza son. Con dos notas basta.'),
            ],
            filas=[
                dict(letra='A', titulo='¿El bajo sube o baja?', pista='medio tono · el acorde de arriba no cambia',
                     n=10, opciones=['↑', '↓']),
                dict(letra='B', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=8, opciones=['M', 'm']),
                dict(letra='C', titulo='¿Con séptima?', pista='tres notas, o cuatro como el E7',
                     n=6, opciones=['3', '4']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Toda esta canción se sostiene sobre una nota grave que se mueve medio tono y vuelve. '
              'Por eso el paso 1 es solo esa nota: si la tienes, lo demás es rellenar. La melodía no '
              'aparece en esta hoja porque no está medida, y no se inventa.',
        reglas=['LA MENOR, SIN ARMADURA', 'EL PRIMER ACORDE PESA MÁS', 'MIRA SIEMPRE LA NOTA DE ABAJO'],
        bloques=[
            dict(num=1, titulo='Solo la nota de abajo', clef='bass',
                 pista='de los cifrados impresos · una nota por compás, y ya se balancea como la canción',
                 sistemas=[
                     dict(cap='a) Am/E · Dm/F · E7 · Am/E → Mi · Fa · Mi · Mi',
                          events=BAJO_MIFA, bars=4, clef='bass'),
                     dict(cap='b) y AHORA con su figura de verdad, la semicorchea · el mismo dibujo el doble de rápido, tal y como está impreso en tu partitura',
                          events=[{'pitch': 'E3', 'dur': 's', 'beam': 9120},
                                  {'pitch': 'F3', 'dur': 's', 'beam': 9120},
                                  {'pitch': 'E3', 'dur': 's', 'beam': 9120},
                                  {'pitch': 'E3', 'dur': 's', 'beam': 9120},
                                  {'pitch': 'F3', 'dur': 's', 'beam': 9121},
                                  {'pitch': 'F3', 'dur': 's', 'beam': 9121},
                                  {'pitch': 'E3', 'dur': 's', 'beam': 9121},
                                  {'pitch': 'F3', 'dur': 's', 'beam': 9121},
                                  {'pitch': 'E3', 'dur': 'q'},
                                  {'pitch': 'F3', 'dur': 'q'}],
                          bars=1, show_time=False, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SUENA A SERRAT',
                 texto='Entre los dos acordes de la primera frase el La se queda quieto, y lo único que '
                       'se mueve de verdad es la nota de abajo, medio tono. Toda la canción está '
                       'construida así, y por eso se balancea en vez de avanzar. Cuando toques, no '
                       'pienses “ahora La menor, ahora Re menor”: piensa “ahora Mi abajo, ahora Fa '
                       'abajo”. Es más fácil y suena mejor.'),
            dict(num=2, titulo='El acorde encima de esa nota', clef='bass',
                 pista='cc. 4 y 5 medidos · Am/E = Mi·La·Do, Dm/F = Fa·La·Re · cuatro golpes por compás',
                 sistemas=[
                     dict(cap='a) los dos acordes de la primera frase · el primer golpe manda, los otros '
                              'tres acompañan',
                          events=ac(AmE, veces=4) + ac(DmF, veces=4), bars=2, clef='bass'),
                     dict(cap='b) y alternándolos, que es el balanceo de la canción · baja el volumen del '
                              'segundo golpe al cuarto; si los cuatro pesan igual, se acabó',
                          events=ac(AmE, veces=4) + ac(DmF, veces=4) +
                                 ac(AmE, veces=4) + ac(DmF, veces=4),
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) los nueve compases seguidos · la disposición de los cinco últimos '
                              'sale del cifrado impreso, no está medida · el paso 2 terminado',
                          events=(ac(AmE, veces=4) + ac(DmF, veces=4) +
                                  ac(('E3', 'G#3', 'D4'), veces=4) + ac(AmE, veces=4) +
                                  ac(('F3', 'A3', 'C4'), veces=4) + ac(('F3', 'G3', 'B3'), veces=4) +
                                  ac(('E3', 'G3', 'C4'), veces=4) + ac(('F3', 'B3', 'D4'), veces=4) +
                                  ac(('E3', 'G#3', 'D4'), veces=4)),
                          bars=5, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='El balanceo ya está. Quedan los dos acordes que tienen truco, aguantar treinta y seis '
              'compases sin que suene a máquina, y entrar en el sitio: la melodía empieza antes del '
              'primer tiempo.',
        reglas=['NO SUENE A METRÓNOMO', 'LA ANACRUSA VA ANTES DEL 1', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='Los dos acordes que tienen truco', clef='bass',
                 pista='uno pide resolver y el otro se disfraza de La menor · cambia UNA nota',
                 sistemas=[
                     dict(cap='a) el E7 lleva Sol♯ · uno por compás, y para a escuchar: vas a notar tú '
                              'solo hacia dónde tira',
                          events=ac(('E3', 'G#3', 'D4'), 'w') + ac(('E3', 'A3', 'C4'), 'w') +
                                 ac(('E3', 'G#3', 'D4'), 'w') + ac(('E3', 'A3', 'C4'), 'w'),
                          bars=4, clef='bass'),
                     dict(cap='b) C/E y Am/E · Mi·Sol·Do y Mi·La·Do: seguidos y sostenidos, hasta que '
                              'oigas cuál es la nota que se mueve',
                          events=ac(('E3', 'G3', 'C4'), 'w') + ac(('E3', 'A3', 'C4'), 'w') +
                                 ac(('E3', 'G3', 'C4'), 'w') + ac(('E3', 'A3', 'C4'), 'w'),
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ SIGNIFICA LA BARRA DEL CIFRADO',
                 texto='Am/E quiere decir: acorde de La menor, pero con un Mi como nota más grave. Lo de '
                       'antes de la barra es el acorde; lo de después, lo que toca el meñique. Aquí casi '
                       'todos los cifrados llevan barra, y ahí está el color de la pieza.'),
            dict(num=4, titulo='Aguantar sin endurecerse', clef='bass',
                 pista='ocho compases seguidos de cuatro golpes · aquí se ve si el brazo está suelto',
                 sistemas=[
                     dict(cap='a) si a mitad de camino empiezas a golpear, para y empieza otra vez más flojo',
                          events=(ac(('A2', 'C3', 'E3'), veces=4) + ac(('F2', 'A2', 'C3'), veces=4) +
                                  ac(('C3', 'E3', 'G3'), veces=4) + ac(('E3', 'G#3', 'B3'), veces=4)),
                          bars=4, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA ANACRUSA, Y DÓNDE PARAR',
                 texto='La melodía no empieza en el primer tiempo: empieza antes, en el último tiempo del '
                       'compás anterior. Eso es la anacrusa, y es lo que hace que la frase suene hablada. '
                       'Cuenta un compás entero en voz alta antes de tocar y entra en el “cuatro”; si '
                       'entras en el “uno”, la canción se desplaza entera. Y esta semana se para en la '
                       'barra de repetición del c. 6: seis compases bien montados, con cuatro acordes '
                       'cada uno, son más trabajo del que parece.'),
            dict(tipo='escalera', valores=[45, 52, 58, 64, 70, 75],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · Solo los bajos de la primera página: Mi, Fa, Mi, Mi, Fa, Fa, Mi, Fa, Mi.   '
                       '2 · Los acordes encima, bajando de volumen dentro de cada compás.   '
                       '3 · El E7 y el C/E, oyendo la nota que se mueve.   '
                       '4 · Ocho compases seguidos sin endurecer el brazo.   '
                       '5 · La escalera de tempo, y las dos manos hasta el c. 6.'),
        ],
    ),

)

# El recurso que la pieza EXPLICA y no dibujaba: durante meses se anotó como
# "no cabe en la hoja". Desde que la hoja se pagina sola, esa excusa dejó de
# ser cierta.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 59, 'C4', 'C3',
    'la mano en Do antes de apretar los grupos de tres',
    desde=6, time_sig=(4, 4)) + [
    bloque_tresillos('Do mayor', 5, 'C4', 'los tresillos que marca el 3', time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
