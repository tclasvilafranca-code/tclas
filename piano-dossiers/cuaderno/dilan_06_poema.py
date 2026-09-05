# -*- coding: utf-8 -*-
"""Poema de Amor (Serrat) — Dilan, avanzado. Ver TRANSCRIPCION_D06_08.md.

   Lo verificado y medido en cinco compases distintos: la mano izquierda hace
   SIEMPRE fundamental - octava - quinta - octava, en cuatro negras. Cambia el
   acorde, nunca el gesto. Con armadura de Sol menor los Si y los Mi son
   bemoles y no se escriben.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOLm = 'Sol menor'
_B = [1000]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def bajo(fund, quinta, oct_):
    """El dibujo de la izquierda: fundamental, octava, quinta, octava."""
    return [n(fund), n(oct_), n(quinta), n(oct_)]


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


# medidos, compas a compas
RE7 = bajo('D2', 'A2', 'D3')
DOm = bajo('C2', 'G2', 'C3')
SOL = bajo('G2', 'D2', 'G3')
FA7 = bajo('F2', 'C3', 'F3')
SIb = bajo('B2', 'F2', 'B3')

CANCION = dict(
    alumno='Dilan', num=6, nivel='avanzado', slug='PoemaDeAmor',
    titulo_corto='Poema de Amor', time_sig=(4, 4), key_sig=SOLm,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' poema-de-amor-joan-manuel-serrat_.pdf'),
    yt='https://www.youtube.com/results?search_query=serrat+poema+de+amor',

    ficha=dict(
        titulo='Poema de Amor', autor='Joan Manuel Serrat · edición con cifrados en español',
        datos=[('Tonalidad', 'Sol menor'), ('Compás', '4/4'), ('Tempo', 'Andante'),
               ('Compases', '28'), ('Mano izq.', 'Bajo alterno')],
        armonia=dict(
            titulo='El dibujo de la mano izquierda',
            tarjetas=[
                ('CC. 1–2  ·  Re7', 'Re · Re · La · Re',
                 'Fundamental, octava, quinta, octava. Cuatro negras, siempre igual.'),
                ('C. 3  ·  Dom', 'Do · Do · Sol · Do',
                 'El mismo dibujo, movido a Do. No cambia nada más.'),
                ('C. 5  ·  Fa7', 'Fa · Fa · Do · Fa',
                 'Y otra vez igual sobre Fa. Es un molde, no cuatro notas sueltas.'),
                ('EL MOLDE', '1 · 8 · 5 · 8',
                 'Aprende el molde y ya no lees notas: lees el cifrado y lo colocas.'),
            ],
            pie='Este acompañamiento se llama bajo alterno y es el pan de la canción de autor: la mano '
                'izquierda marca la fundamental, sube a la octava, pasa por la quinta y vuelve. Medido en '
                'cinco compases distintos de la pieza y siempre sale lo mismo. Si te lo aprendes como '
                'molde, la izquierda de esta canción deja de tener notas.',
        ),
        ritmos=[
            ('MI · sobre Re7', 'el molde: fundamental, octava, quinta, octava', RE7, OCRE, 'bass', SOLm),
            ('MI · sobre Dom', 'el mismo molde, movido: no hay que leerlo otra vez', DOm, OCRE, 'bass', SOLm),
            ('MD', 'la melodía, en notas largas sobre ese balanceo',
             [n('D5', 'h'), n('C5', 'q'), n('B4', 'q')], AZUL, 'treble', SOLm),
        ],
        especial=[
            'Armadura de dos bemoles: todos los Si y los Mi son ♭. La tonalidad es Sol menor.',
            'Los cifrados vienen impresos y EN ESPAÑOL: Solm, Dom, Re7, Fa7, Si♭M, Mi♭M.',
            'La primera frase pone "Recitado": se dice, no se canta. Casi sin tempo.',
            'La izquierda hace el mismo dibujo en los 28 compases. Solo cambia sobre qué acorde.',
            'Los cc. 2 y 19 son idénticos entre sí, y los cc. 3 y 20 también.',
            'El Re7 lleva Fa♯: es la alteración que hace que quiera volver a Sol menor.',
            'La octava del molde se toca con el 5 y el 1, y la quinta con el 2 o el 3: la mano no '
            'se cierra ni se abre en todo el compás.',
        ],
        reto='Que el bajo alterno no se convierta en un tic. Cuatro negras iguales durante veintiocho '
             'compases pueden sonar a acompañamiento de cantante o a caja de música, y la diferencia '
             'está solo en el peso que le pongas a cada una.',
        truco='Toca la izquierda sola diciendo el cifrado en voz alta antes de cada compás: "Re siete", '
              '"Do menor", "Sol menor". Cuando sepas dónde estás sin mirar, pon la derecha encima.',
        sabias='Serrat grabó "Poema de Amor" en 1969, en su primer disco en castellano. Hasta entonces '
               'había cantado solo en catalán, y aquel cambio le costó una polémica que le persiguió '
               'años. La canción es de las pocas suyas que empieza recitada, sin cantar.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en la primera frase: la dice, no la canta.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. La tonalidad es Sol menor y el gesto de la '
              'canción es un bajo alterno de cuatro negras. Aquí se trabaja ese molde por toda la '
              'tonalidad, no solo sobre los cuatro acordes que la pieza usa.',
        reglas=['ARMADURA DE SOL MENOR: SI♭ Y MI♭', 'EL PRIMER GOLPE PESA MÁS', 'MANOS SEPARADAS'],
        ejercicios=[
            dict(num=1, titulo='Escala de Sol menor · dos octavas', clef='bass',
                 pista='manos separadas · dos bemoles, y el pulgar por debajo sin bache',
                 events=corch(['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3']) +
                        corch(['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'G4']) +
                        corch(['G4', 'F4', 'E4', 'D4', 'C4', 'B3', 'A3', 'G3']) +
                        corch(['F3', 'E3', 'D3', 'C3', 'B2', 'A2', 'G2', 'G2']),
                 bars_per_line=4),
            dict(num=2, titulo='El molde, por toda la tonalidad', clef='bass',
                 pista='fundamental · octava · quinta · octava, sobre los seis grados de Sol menor',
                 events=(bajo('G2', 'D3', 'G3') + bajo('A2', 'E3', 'A3') +
                         bajo('B2', 'F3', 'B3') + bajo('C3', 'G3', 'C4') +
                         bajo('D3', 'A3', 'D4') + bajo('G2', 'D3', 'G3')),
                 bars_per_line=3),
            dict(num=3, titulo='El molde al revés', clef='bass',
                 pista='octava · fundamental · octava · quinta · lo que la pieza nunca te hace practicar',
                 events=([n('G3'), n('G2'), n('G3'), n('D3')] +
                         [n('C4'), n('C3'), n('C4'), n('G3')] +
                         [n('F3'), n('F2'), n('F3'), n('C3')] +
                         [n('G3'), n('G2'), n('G3'), n('D3')]),
                 bars_per_line=4),
            dict(num=4, titulo='El Fa sostenido que pide volver',
                 pista='la nota del Re7 · sube medio tono y la canción quiere resolver en Sol menor',
                 events=[n('D4'), n('F#4'), n('A4'), n('C5'),
                         n('D5', 'h'), n('G4', 'h'),
                         n('C5'), n('A4'), n('F#4'), n('D4'),
                         n('G4', 'w')],
                 bars_per_line=2),
            dict(num=5, titulo='El molde, pero con la derecha',
                 pista='la mano que nunca lo toca · el 1 abajo, el 5 en la octava y el 2 en la quinta',
                 events=(bajo('G3', 'D4', 'G4') + bajo('C4', 'G4', 'C5') +
                         bajo('F3', 'C4', 'F4') + bajo('G3', 'D4', 'G4')),
                 bars_per_line=4),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con dos bemoles. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · armadura de Sol menor: Si y Mi son bemol',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DEL BAJO ALTERNO (CLAVE DE FA)',
        chuleta_pitches=['C2', 'D2', 'F2', 'G2', 'B2', 'C3', 'D3', 'F3', 'G3'],
        chuleta_nombres=['Do', 'Re', 'Fa', 'Sol', 'Si♭', 'Do', 'Re', 'Fa', 'Sol'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa, registro grave', clef='bass',
                 pista='donde vive el bajo alterno · con líneas adicionales por abajo',
                 events=[n(p) for p in ('D2', 'G3', 'C2', 'F3', 'A2', 'D3', 'G2', 'B3',
                                        'F2', 'C3', 'E3', 'D2', 'A3', 'G2', 'C3', 'F2')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · orden irregular a propósito',
                 events=[n(p) for p in ('G4', 'D5', 'B4', 'F5', 'C5', 'A4', 'E5', 'G5',
                                        'D4', 'F4', 'C5', 'B4', 'A4', 'E4', 'G4', 'D5')]),
            dict(num=3, titulo='Con el Fa sostenido',
                 pista='el del acorde Re7 · una alteración suelta vale hasta la barra, no más',
                 events=[n('D4'), n('F#4', 'h'), n('A4'),
                         n('G4'), n('F4'), n('D4', 'h'),
                         n('C5'), n('A4'), n('F#4'), n('D4'),
                         n('G4', 'w')]),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca el molde de cuatro negras sobre un acorde. Que diga si la SEGUNDA nota fue '
                      'la octava (como en la pieza) o la quinta.'),
                ('B', 'Toca una tríada suelta: MAYOR o MENOR. La pieza alterna las dos.'),
                ('C', 'Toca dos acordes y acaba unas veces en Sol menor y otras en Re. Que diga si la '
                      'frase queda CERRADA o ABIERTA.'),
                ('+', 'Y sin escribir: toca el molde y que lo repita en otro acorde, de oído.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Octava o quinta?', pista='la segunda nota del molde',
                     n=10, opciones=['8ª', '5ª']),
                dict(letra='B', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=8, opciones=['M', 'm']),
                dict(letra='C', titulo='¿Cerrada o abierta?', pista='acaba en la tónica, o se queda esperando',
                     n=6, opciones=['cerrada', 'abierta']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Esta izquierda no se lee: se coloca. Hace siempre lo mismo —fundamental, octava, quinta, '
              'octava— y lo único que cambia es dónde pones el molde. Por eso el paso 1 es el molde y '
              'el paso 2 es moverlo por la página.',
        reglas=['ARMADURA DE SOL MENOR', 'PRIMERO EL MOLDE, LUEGO LAS NOTAS', 'DI EL CIFRADO EN VOZ ALTA'],
        bloques=[
            dict(num=1, titulo='El molde, y por dónde viaja', clef='bass',
                 pista='cc. 1–6 medidos · cuatro negras: la primera pesa, las otras tres solo acompañan',
                 sistemas=[
                     dict(cap='a) cc. 1–2 · Re7 → Re · Re · La · Re, dos veces igual',
                          events=RE7 + RE7, bars=2, clef='bass'),
                     dict(cap='b) quita el relleno y quédate con la primera nota de cada compás · '
                              'Re · Do · Sol · Fa · Si♭ · Re: así es como viaja la mano',
                          events=[n('D2', 'w'), n('C2', 'w'), n('G2', 'w'),
                                  n('F2', 'w'), n('B2', 'w'), n('D2', 'w')],
                          bars=6, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTO NO SE LEE, SE COLOCA',
                 texto='Una vez que ves que la izquierda hace siempre fundamental, octava, quinta y octava, '
                       'deja de haber notas que leer: hay un molde y un cifrado que te dice dónde ponerlo. '
                       'Mira los cifrados de tu partitura y tócalos sin leer el pentagrama de abajo, solo '
                       'colocando el molde. Te va a salir casi entero a la primera, y encima te lo aprendes '
                       'de memoria sin querer.'),
            dict(num=2, titulo='El molde puesto en su sitio', clef='bass',
                 pista='cc. 1–6 medidos · Re7 · Dom · Sol m · Fa7 · Si♭ · y vuelta',
                 sistemas=[
                     dict(cap='a) los dos que se salen de la mano: Fa7 y Si♭ · el Si♭ abre la octava '
                              'desde tecla negra — colócala en el aire y déjala caer ya abierta',
                          events=FA7 + SIb + FA7 + SIb, bars=4, clef='bass'),
                     dict(cap='b) y la primera página entera · el molde no cambia nunca: lo único que '
                              'cambia es dónde lo pones',
                          events=RE7 + DOm + SOL + FA7 + SIb + RE7, bars=3, clef='bass',
                          show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL FA♯ DEL RE7',
                 texto='La armadura de Sol menor no lleva ningún sostenido, así que cada Fa♯ está escrito '
                       'a mano delante de la nota. Y aparece siempre en el mismo sitio: en el acorde de '
                       'Re7. Ese Fa♯ es lo que convierte el Re en dominante y hace que la música tire '
                       'hacia Sol menor. Si te lo comes, el acorde deja de pedir nada y la frase se queda '
                       'plana. Búscalo en tu partitura y márcalo con lápiz.'),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='El molde ya está colocado. Lo que queda no son notas nuevas: es aguantarlo veintiocho '
              'compases sin que suene a caja de música, y entender que la primera frase no se canta, '
              'se recita.',
        reglas=['EL RECITADO NO LLEVA PRISA', 'NO SUENE A CAJA DE MÚSICA', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='Aguantar el molde', clef='bass',
                 pista='ocho compases seguidos · aquí se ve si el brazo está suelto o si estás golpeando',
                 sistemas=[
                     dict(cap='a) cuatro compases sobre Sol menor y cuatro sobre Do menor, sin parar · '
                              'si a mitad empiezas a golpear, para y vuelve a empezar más flojo',
                          events=SOL * 4 + DOm * 4, bars=4, clef='bass'),
                     dict(cap='b) y el mismo molde con un solo golpe por compás · así se oye la forma '
                              'sin que el relleno la tape',
                          events=[{'pitches': ['G2', 'G3'], 'dur': 'w'},
                                  {'pitches': ['C2', 'C3'], 'dur': 'w'},
                                  {'pitches': ['D2', 'D3'], 'dur': 'w'},
                                  {'pitches': ['G2', 'G3'], 'dur': 'w'}],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='“RECITADO”: QUÉ SIGNIFICA',
                 texto='La partitura pone Recitado encima de la primera frase. Quiere decir que ahí la voz '
                       'habla en vez de cantar, y que el tempo es libre: la izquierda espera. Al piano se '
                       'traduce así: toca esos compases sin metrónomo, dejando aire entre frase y frase, y '
                       'no entres en tempo hasta que la melodía empiece a cantar de verdad. Es el único '
                       'sitio de la pieza donde puedes hacer lo que quieras con el tiempo.'),
            dict(num=4, titulo='El peso, que es lo único que tienes',
                 pista='sin pentagrama: se hace sobre el paso 3, cambiando solo cuánto pesa cada nota',
                 sistemas=[]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE HACE EL PASO 4',
                 texto='Cuatro negras iguales, veintiocho compases. No hay dinámicas escritas, no hay '
                       'cambios de figura: lo único que puedes mover es cuánto pesa cada nota. La primera, '
                       'la fundamental, lleva el peso del brazo; las otras tres caen solas, casi sin dedo. '
                       'Si las cuatro pesan igual, esto suena a metrónomo. Si la primera pesa y las otras '
                       'se apagan, suena a guitarra acompañando a alguien. Y ojo al c. 19: los cc. 19 y 20 '
                       'son, nota por nota, los cc. 2 y 3 — está medido, así que ahí no hay nada nuevo que '
                       'montar, solo que suene reconocible.'),
            dict(tipo='escalera', valores=[50, 58, 64, 70, 76, 84],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · El molde solo, y por dónde viaja la mano.   '
                       '2 · El molde puesto sobre los cifrados de la primera página.   '
                       '3 · Ocho compases seguidos sin endurecer el brazo.   '
                       '4 · El peso: la primera negra pesa, las otras tres caen solas.   '
                       '5 · La escalera de tempo, y las dos manos desde el c. 3.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
