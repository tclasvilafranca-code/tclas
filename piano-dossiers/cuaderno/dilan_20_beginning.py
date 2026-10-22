# -*- coding: utf-8 -*-
"""It's Beginning to Look a Lot Like Christmas (arr. Rachel Chytelman)
   — Dilan, avanzado. Ver TRANSCRIPCION_D18_20.md.

   Segunda pieza a CUATRO MANOS del album, y con una diferencia respecto a la
   Arabesque: aqui el Piano 2 lleva los DOS pentagramas en clave de fa, asi
   que hay que leerla con lector_4manos.CLAVES = ['treble','treble','bass','bass'].

   Do mayor, 6/8. El Primo (la parte del alumno) toca la MISMA melodia con las
   dos manos, separadas por una octava, de principio a fin.

   MEDIDO DE NUEVO EL 1 DE SEPTIEMBRE DE 2026, y hubo que rehacer las citas.
   Este dosier se escribio antes de que existiera `medir_arranque`, y lo que
   llamaba "cc. 1-4 medidos" no era lo impreso: ni el silencio de entrada, ni
   el Fa sostenido, ni las figuras. Se midio a 300 ppp sobre el PDF (mismo
   archivo, md5 4d98ecda..., que el de Aida y el de Eva), localizando las
   divisorias por columnas de tinta que cruzan el sistema del Piano 1 —en una
   pieza a cuatro manos la divisoria NO une los dos pianos— y leyendo cada
   cabeza por su centro contra las cinco lineas.

   PIANO 1, pentagrama de arriba (el de abajo lleva lo mismo una octava mas
   abajo, comprobado en los cc. 1 a 4):

       c. 1   silencio de negra con puntillo · Mi5 (negra) · Fa5 (corchea)
       c. 2   Sol5 · La5 · Sol5 (corcheas) · Fa#5 (negra) · Sol5 (corchea)
       c. 3   La5 (negra con puntillo) · Do6 (negra con puntillo)
       c. 4   Mi6 (negra con puntillo) · Sol5 (negra con puntillo)
       c. 5   compas entero de silencio
       c. 6   Mi6 (negra con puntillo) LIGADA a Mi6 (negra) · Mi6 (corchea)
       c. 7   Re6 (negra con puntillo) LIGADA a Re6 (negra) · Do6 (corchea)
       c. 8   La5 (blanca con puntillo)
       c. 9   silencio de negra con puntillo · La5 (negra) · Si5 (corchea)
       c. 10  Do6 · Re6 · Do6 (corcheas) · La5 (negra) · La#5 (corchea)
       c. 11  Si5 (blanca con puntillo)
       c. 12  Si5 · Do6 · Si5 (corcheas) · Sol5 (negra) · Sol#5 (corchea)
       c. 13  La5 (blanca) · silencio de corchea · La#5 (corchea)
       c. 14  Si5 (negra) · Do6 (corchea) · Re6 (negra) · Mi6 (corchea)

   Cada compas cierra en tres tiempos de negra, que es lo que vale un 6/8.

   PIANO 2 (la profesora), tambien medido:

       pentagrama de arriba   silencio de negra con puntillo + el ACORDE en
                              negra con puntillo. NO es un acorde sostenido
                              todo el compas, que es lo que decia este dosier.
                              c. 2 Mi3+Sol3+Do4 · c. 3 Fa3+La3+Do4
       pentagrama de abajo    UNA nota por compas, en blanca con puntillo:
                              cc. 2 a 14  Do3 · Fa2 · Do3 · Do3 · Do3 · Sol2 ·
                              Fa2 · Fa2 · Fa2 · Sol2 · Sol2 · La2 · Sol2

   Y el c. 1 lo toca el PRIMO, no el Secondo: el Piano 2 tiene un compas
   entero de silencio en los dos pentagramas. Este dosier decia lo contrario.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
_B = [2800]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='q'):
    return {'pitches': list(ps), 'dur': d}


def sil(d='q'):
    return {'rest': True, 'dur': d}


def corch(ps, agrupar=3):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


DO = ('E3', 'G3', 'C4')
FA = ('F3', 'A3', 'C4')
SOL = ('D3', 'G3', 'B3')
LAm = ('E3', 'A3', 'C4')

# --- lo MEDIDO del Piano 1, que es la parte del alumno ---------------------
C1 = [sil('q.'), n('E5'), n('F5', 'e')]
C2 = corch(['G5', 'A5', 'G5']) + [n('F#5'), n('G5', 'e')]
C34 = [n('A5', 'q.'), n('C6', 'q.'), n('E6', 'q.'), n('G5', 'q.')]
C67 = [dict(n('E6', 'q.'), lig=True), n('E6'), n('E6', 'e'),
       dict(n('D6', 'q.'), lig=True), n('D6'), n('C6', 'e')]
C910 = ([sil('q.'), n('A5'), n('B5', 'e')] +
        corch(['C6', 'D6', 'C6']) + [n('A5'), n('A#5', 'e')])
# el mismo material una octava mas abajo: el pentagrama de abajo del Piano 1
B1 = [sil('q.'), n('E4'), n('F4', 'e')]
B2 = corch(['G4', 'A4', 'G4']) + [n('F#4'), n('G4', 'e')]
B67 = [dict(n('E5', 'q.'), lig=True), n('E5'), n('E5', 'e'),
       dict(n('D5', 'q.'), lig=True), n('D5'), n('C5', 'e')]
# y la fundamental del Secondo, cc. 2 a 7
BAJO_SECONDO = [n('C3', 'h.'), n('F2', 'h.'), n('C3', 'h.'),
                n('C3', 'h.'), n('C3', 'h.'), n('G2', 'h.')]

CANCION = dict(
    alumno='Dilan', num=20, nivel='avanzado', slug='BeginningChristmas',
    titulo_corto="It's Beginning to Look a Lot Like Christmas",
    time_sig=(6, 8), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           ' its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf'),
    yt='https://www.youtube.com/results?search_query=its+beginning+to+look+a+lot+like+christmas',

    ficha=dict(
        titulo="It's Beginning to Look a Lot Like Christmas",
        autor='Meredith Willson (1951) · arreglo a cuatro manos de Rachel Chytelman',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '6/8'), ('Formato', '4 manos'),
               ('Tu parte', 'Primo'), ('Mano izq.', 'Igual que la dcha.')],
        armonia=dict(
            titulo='Cómo está repartida la pieza',
            tarjetas=[
                ('TU PARTE · PRIMO', 'La melodía, doble',
                 'Los dos pentagramas de arriba, en clave de sol. Las dos manos tocan lo mismo, '
                 'separadas por una octava.'),
                ('LA OTRA · SECONDO', 'Dos claves de fa',
                 'La profesora: arriba, un silencio y el acorde en negra con puntillo; abajo, una '
                 'sola nota que dura el compás entero.'),
                ('LA ARMONÍA', 'Do · Fa · Sol · La m',
                 'Medida en la nota grave del Secondo: en toda la primera página solo hay esos '
                 'cuatro apoyos.'),
                ('EL 6/8', 'Seis corcheas',
                 'Se cuenta en dos: "UN-dos-tres DOS-dos-tres". No en seis.'),
            ],
            pie='En 6/8 hay seis corcheas por compás, pero no se cuentan seis: se cuentan dos grupos de '
                'tres. Por eso suena a balanceo y no a marcha. Si lo cuentas en seis, la canción se '
                'vuelve pesada; si lo cuentas en dos, sale sola.',
        ),
        ritmos=[
            ('PRIMO', 'el c. 1 MEDIDO · entras a la mitad, después del silencio',
             list(C1), AZUL, 'treble', None),
            ('SECONDO', 'su c. 2, medido · el silencio y luego el acorde',
             [sil('q.'), ac(DO, 'q.')], OCRE, 'bass', None),
            ('SECONDO · el siguiente', 'el c. 3, mismo dibujo sobre Fa',
             [sil('q.'), ac(FA, 'q.')], OCRE, 'bass', None),
        ],
        especial=[
            'No hay armadura: la tonalidad es Do mayor.',
            'Va en 6/8: seis corcheas por compás, contadas en DOS grupos de tres.',
            'Es una pieza a CUATRO MANOS: cuatro pentagramas por sistema.',
            'Tú tocas el PRIMO, los dos pentagramas de arriba, los dos en clave de sol.',
            'Tus dos manos tocan LO MISMO, separadas por una octava, de principio a fin.',
            'El Piano 2 lleva los dos pentagramas en clave de FA: suena todo por debajo de ti.',
            'El primer compás lo empiezas TÚ: el Piano 2 tiene ahí un compás de silencio.',
            'Tu entrada llega después de un silencio de negra con puntillo.',
        ],
        reto='Que tus dos manos suenen como una sola. Tocan lo mismo a una octava, así que cualquier '
             'desajuste, por pequeño que sea, se oye como un eco. Y encima hay que encajar con otra '
             'persona.',
        truco='Estudia siempre las dos manos juntas desde el primer día, nunca por separado: el problema '
              'no es aprenderse las notas, es que caigan exactamente a la vez. Y cuenta en dos, no en '
              'seis: "UN-dos-tres DOS-dos-tres".',
        sabias='Meredith Willson la escribió en 1951, el mismo año en que empezó a componer "The Music '
               'Man". Perry Como y Bing Crosby la grabaron el mismo mes, sin saberlo, y las dos '
               'versiones salieron a la venta a la vez.',
        qr=dict(titulo='Escúchala a cuatro manos',
                texto='Busca una versión a dúo y fíjate en cómo se coordinan al empezar.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. Tu parte pide dos manos que toquen lo mismo '
              'exactamente a la vez, y un 6/8 contado en dos. Aquí se entrenan las dos cosas, en '
              'Do mayor.',
        reglas=['SIN ARMADURA · DO MAYOR', 'LAS DOS MANOS, EXACTAMENTE A LA VEZ', 'CUENTA EN DOS'],
        ejercicios=[
            dict(num=1, titulo='Escala de Do mayor · dos octavas',
                 pista='LAS DOS MANOS a la vez, en octava · es lo que hace tu parte todo el rato',
                 events=corch(['C4', 'D4', 'E4']) + corch(['F4', 'G4', 'A4']) +
                        corch(['B4', 'C5', 'D5']) + corch(['E5', 'F5', 'G5']) +
                        corch(['A5', 'B5', 'C6']) + corch(['B5', 'A5', 'G5']) +
                        corch(['F5', 'E5', 'D5']) + corch(['C5', 'B4', 'A4']) +
                        corch(['G4', 'F4', 'E4']) + corch(['D4', 'C4', 'C4']),
                 bars_per_line=5),
            dict(num=2, titulo='Contar en dos, no en seis',
                 pista='seis corcheas por compás, pero solo dos golpes de pie · aprieta la 1.ª de cada tres',
                 events=corch(['C5', 'D5', 'E5']) + corch(['F5', 'E5', 'D5']) +
                        corch(['C5', 'D5', 'E5']) + corch(['G5', 'F5', 'E5']) +
                        corch(['D5', 'E5', 'F5']) + corch(['E5', 'D5', 'C5']) +
                        [n('C5', 'h.')],
                 bars_per_line=4),
            dict(num=3, titulo='Arpegio de Do mayor · dos octavas',
                 pista='fundamental · 3ª · 5ª · 8ª · con las dos manos, siempre a la vez',
                 events=corch(['C4', 'E4', 'G4']) + corch(['C5', 'E5', 'G5']) +
                        corch(['C6', 'G5', 'E5']) + corch(['C5', 'G4', 'E4']) +
                        [n('C4', 'h.')],
                 bars_per_line=5),
            dict(num=4, titulo='Las dos manos, una octava aparte',
                 pista='el gesto exacto de tu parte · si oyes un eco, no están cayendo juntas',
                 events=corch(['G4', 'A4', 'B4']) + corch(['C5', 'B4', 'A4']) +
                        corch(['G4', 'F4', 'E4']) + corch(['D4', 'E4', 'F4']) +
                        [n('G4', 'h.')],
                 bars_per_line=5),
            dict(num=5, titulo='El acompañamiento del Secondo', clef='bass',
                 pista='lo que toca la profesora · un acorde por compás, sostenido los seis tiempos',
                 events=[ac(DO, 'h.'), ac(FA, 'h.'), ac(SOL, 'h.'), ac(LAm, 'h.'),
                         ac(FA, 'h.'), ac(SOL, 'h.'), ac(DO, 'h.'), ac(DO, 'h.')],
                 bars_per_line=8),
            dict(num=6, titulo='Y ahora en el registro agudo',
                 pista='tu mano derecha vive arriba · con líneas adicionales, sin cambiar el gesto',
                 events=corch(['C6', 'B5', 'A5']) + corch(['G5', 'A5', 'B5']) +
                        corch(['C6', 'D6', 'E6']) + corch(['D6', 'C6', 'B5']) +
                        [n('C6', 'h.')],
                 bars_per_line=5),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta: tu parte va en clave de sol en los dos '
              'pentagramas, así que se practica sobre todo esa. Abajo se escucha.',
        sub_leer='di el nombre en voz alta · no hay armadura, y casi no hay alteraciones',
        chuleta_clef='treble',
        chuleta_titulo='EL REGISTRO DEL PRIMO (CLAVE DE SOL)',
        chuleta_pitches=['C4', 'E4', 'G4', 'C5', 'E5', 'G5', 'C6'],
        chuleta_nombres=['Do', 'Mi', 'Sol', 'Do', 'Mi', 'Sol', 'Do'],
        ejercicios=[
            dict(num=1, titulo='Clave de Sol, registro medio',
                 pista='donde toca tu mano izquierda · también en clave de sol',
                 events=[n(p, 'e') for p in ('C4', 'G4', 'E4', 'A4', 'F4', 'B4', 'D4', 'C5',
                                             'G4', 'E4', 'A4', 'F4')],
                 bars_per_line=4),
            dict(num=2, titulo='Clave de Sol, registro alto',
                 pista='donde toca tu mano derecha · con líneas adicionales por arriba',
                 events=[n(p, 'e') for p in ('C5', 'G5', 'E5', 'B5', 'A5', 'D6', 'F5', 'C6',
                                             'E6', 'G5', 'B5', 'C5')],
                 bars_per_line=4),
            dict(num=3, titulo='Clave de Fa · la parte de la profesora', clef='bass',
                 pista='sus dos pentagramas van en clave de fa · saber dónde está ayuda a encajar',
                 events=[n(p, 'e') for p in ('C3', 'G3', 'E3', 'A3', 'F3', 'B3', 'D3', 'C4',
                                             'G2', 'E2', 'A2', 'F2')],
                 bars_per_line=4),
        ],
        crono='¿Cuánto tardas en el ejercicio 2, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca dos notas a la vez separadas por una OCTAVA, y otras veces por una quinta. '
                      'Que diga cuál era: la octava es lo que hacen sus dos manos.'),
                ('B', 'Toca seis corcheas agrupadas en DOS o en TRES. Que diga cómo iban: es la '
                      'diferencia entre 6/8 y 3/4.'),
                ('C', 'Toca una tríada suelta: MAYOR o MENOR.'),
                ('+', 'Y lo más importante: contad "un-dos-tres dos-dos-tres" juntos y empezad a la vez.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Octava o quinta?', pista='las dos notas, a la vez',
                     n=10, opciones=['8ª', '5ª']),
                dict(letra='B', titulo='¿De dos o de tres?', pista='cómo se agrupan las seis corcheas',
                     n=8, opciones=['2', '3']),
                dict(letra='C', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=6, opciones=['M', 'm']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Todo lo que se cita es del PRIMO, que es tu parte. Tus dos manos tocan exactamente lo '
              'mismo separadas por una octava: solo hay una línea que aprender, pero cualquier desajuste '
              'entre ellas se oye como un eco. Por eso se estudian juntas desde el primer día.',
        reglas=['ESTO ES SOLO TU PARTE · EL PRIMO', 'LAS DOS MANOS A LA VEZ', 'CUENTA EN DOS'],
        bloques=[
            dict(num=1, titulo='La melodía, frase por frase',
                 pista='cc. 1–10 MEDIDOS · tu derecha lo toca aquí y tu izquierda una octava más abajo',
                 sistemas=[
                     dict(cap='a) cc. 1–4 · entras después del silencio, y el cuarto sonido es un FA '
                              'SOSTENIDO: la única tecla negra de toda la frase',
                          events=C1 + C2 + C34, bars=4),
                     dict(cap='b) cc. 6–7 · las dos notas largas ATADAS · la ligadura no se vuelve a '
                              'tocar: se suma, y por eso la frase parece que se para',
                          events=list(C67), bars=2, show_time=False),
                     dict(cap='c) cc. 9–10 · la misma entrada un grado más arriba, y otra tecla negra '
                              'al final: el La sostenido que empuja hacia el compás siguiente',
                          events=list(C910), bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA MELODÍA VA ARRIBA DEL TODO',
                 texto='Tu mano derecha toca por encima del Do5 casi siempre, y ahí hay muchas líneas '
                       'adicionales. No cuentes líneas cada vez: aprende de memoria dónde están el Do5, '
                       'el Mi5 y el Sol5, y lee el resto por distancia respecto a ellos. Con tres notas '
                       'de referencia se lee todo el registro agudo sin contar ni una línea.'),
            dict(num=2, titulo='La misma frase, donde la toca tu izquierda',
                 pista='cc. 1–2 y 6–7 MEDIDOS · exactamente lo mismo, una octava más abajo',
                 sistemas=[
                     dict(cap='a) los cc. 1 y 2 · léela aquí y tócala con la izquierda sola una vez · '
                              'después junta las dos y escucha si hay eco',
                          events=B1 + B2, bars=2),
                     dict(cap='b) los cc. 6–7 de la izquierda, con las mismas ligaduras · es donde la '
                              'nota larga delata cualquier desajuste entre las dos manos',
                          events=list(B67), bars=2, show_time=False),
                     dict(cap='c) y solo la primera nota de cada compás, en figuras largas · andamio: '
                              'para colocar la mano antes de meterle las corcheas',
                          events=[n('E4', 'h.'), n('G4', 'h.'), n('A4', 'h.'), n('E5', 'h.')],
                          bars=4, show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='Quedan dos cosas: el 6/8, que es el compás que más se cuenta mal de todo el cuaderno, y '
              'tocar con otra persona. Lo primero se resuelve en casa; lo segundo, solo en clase.',
        reglas=['CUENTA EN DOS, NO EN SEIS', 'LAS DOS MANOS, UNA SOLA COSA', 'EMPEZAD JUNTAS'],
        bloques=[
            dict(num=3, titulo='El 6/8, en dos golpes',
                 pista='andamio · aprieta un poco la primera de cada tres corcheas y no las demás',
                 sistemas=[
                     dict(cap='a) el pie marca solo dos veces por compás · si marcas seis, ya lo estás '
                              'contando mal',
                          events=corch(['G4', 'A4', 'B4']) + corch(['C5', 'B4', 'A4']) +
                                 corch(['G4', 'A4', 'B4']) + corch(['C5', 'D5', 'E5']) +
                                 corch(['D5', 'C5', 'B4']) + corch(['A4', 'G4', 'F4']) +
                                 [n('G4', 'h.')],
                          bars=4),
                     dict(cap='b) y la frase entera sin parar · si te equivocas, no repitas el compás: '
                              'vuelve al principio de la frase, que es como se toca en pareja',
                          events=corch(['E5', 'F5', 'G5']) + corch(['A5', 'G5', 'F5']) +
                                 corch(['G5', 'A5', 'B5']) + [n('C6', 'h.')] +
                                 corch(['C6', 'B5', 'A5']) + corch(['G5', 'A5', 'B5']) +
                                 corch(['A5', 'G5', 'F5']) + [n('E5', 'h.')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL 6/8 NO SE CUENTA EN SEIS',
                 texto='Hay seis corcheas en cada compás, y la tentación es contar “un-dos-tres-cuatro-'
                       'cinco-seis”. No lo hagas: se cuenta en DOS, “UN-dos-tres DOS-dos-tres”, con solo '
                       'dos golpes de pie por compás. Esa es la diferencia entre que la canción suene a '
                       'balanceo, que es lo que es, o a marcha militar. Cuenta así desde el primer día y '
                       'no tendrás que corregirlo después.'),
            dict(num=4, titulo='Lo que toca la otra parte', clef='bass',
                 pista='Secondo MEDIDO · cc. 2–7 · esto NO lo tocas tú, pero es lo que oyes debajo',
                 sistemas=[
                     dict(cap='a) su nota grave, cc. 2–7 · una por compás, sostenida entera: Do · Fa · '
                              'Do · Do · Do · Sol. El cambio de nota es lo que te dice si vais juntas',
                          events=list(BAJO_SECONDO), bars=6, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE ENSAYA UNA PIEZA A DÚO',
                 texto='Lo que se estudia en casa es tu parte sola, y eso es lo fácil. Lo difícil solo se '
                       'puede trabajar en clase, las dos sentadas al piano, y son tres cosas: empezar a '
                       'la vez, respirar juntas al empezar cada frase, y no acelerar por tu cuenta cuando '
                       'te sientas segura. Si te pierdes en medio, no pares: cuenta hasta el principio '
                       'del compás siguiente y engancha ahí.'),
            dict(tipo='escalera', valores=[54, 63, 72, 80, 88, 96],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
