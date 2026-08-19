# -*- coding: utf-8 -*-
"""Thinking Out Loud (canción 5 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico); la medición se importa de
   `dilan_04_thinking`. Ver TRANSCRIPCION_D04_THINKING.md, y en particular su
   apartado "Lo que NO está verificado": de la mano derecha NO se cita ninguna
   altura, solo el RITMO, que es lo único que se ve sin ambigüedad.

   Camino distinto al de Dilan:

     - A Dilan se le entra por la IZQUIERDA, que aguanta redondas, y desde ahí
       se le añade la derecha que entra tarde.
     - A Eva se le entra por el ACENTO 3+3+2, que es la firma de la canción y
       lo que la hace sonar a Ed Sheeran y no a una balada cualquiera. Es un
       ejercicio de percusión antes que de piano: se hace en una sola nota.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_04_thinking import n, corch, R, Rh, SOSTEN, CONTRA

HERE = os.path.dirname(__file__)
RE = 'Re mayor'
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def _en_una_nota(eventos, altura='D5'):
    """El mismo ritmo, en una sola nota. Las alturas de esta mano no estan
       medidas; el ritmo si, y es lo unico que hay que tener exacto."""
    return [e if 'rest' in e else n(altura, e['dur']) for e in eventos]


CANCION = dict(
    alumno='Eva', num=5, nivel='avanzado', slug='ThinkingOutLoud',
    titulo_corto='Thinking Out Loud', time_sig=(4, 4), key_sig=RE,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'THINKING OUT LOUD _ Ed Sheeran .pdf'),
    yt='https://www.youtube.com/results?search_query=ed+sheeran+thinking+out+loud',

    ficha=dict(
        titulo='Thinking Out Loud',
        autor='Ed Sheeran y Amy Wadge (2014)',
        datos=[('Tonalidad', 'Re mayor'), ('Compás', '4/4'), ('Tempo', '♩=145'),
               ('Mano izq.', 'Redondas'), ('Mano dcha.', 'A contratiempo')],
        armonia=dict(
            titulo='Cuatro compases, y ya está',
            tarjetas=[
                ('EL CICLO', 'Re · La · Si · Sol',
                 'Cuatro notas graves que vuelven cada cuatro compases durante toda la canción.'),
                ('EL ACENTO', '3 + 3 + 2',
                 'Ocho corcheas iguales, agrupadas de tres en tres y las dos últimas juntas. Ahí está el carácter.'),
                ('LA ENTRADA', 'nunca en el uno',
                 'La derecha llega siempre tarde a propósito. Si entras en el uno, la canción se desplaza entera.'),
            ],
            pie='De la mano derecha este cuaderno solo cita el RITMO: sus alturas no están medidas con '
                'seguridad, y lo que no está medido no se escribe.',
        ),
        especial=[
            'La armadura de Re mayor lleva dos sostenidos: todos los Fa y todos los Do.',
            'La izquierda ataca una nota grave y la deja sonar cuatro tiempos. Nada más.',
            'Seis compases son exactamente iguales: los cc. 4, 7, 10, 17, 38 y 41.',
            'Y otros tres más: los cc. 39, 42 y 45. Comparado compás a compás.',
            'El acento va 3+3+2, no 2+2+2+2, aunque el pie siga marcando cuatro.',
            'Sin pedal esta canción suena vacía: el pedal es la tercera mano.',
        ],
        ritmos=[
            ('MI', 'una redonda: se ataca una vez y ya está',
             [n('D2', 'w')], OCRE, 'bass', RE),
            ('MD', 'el ritmo, en una sola nota: entra en el tercer tiempo',
             [Rh, n('D5', 'e'), n('D5', 'e'), n('D5', 'q')], AZUL, 'treble', RE),
        ],
        reto='Entrar tarde y no adelantarse. La izquierda no te ayuda —está quieta— así que el sitio '
             'de la entrada lo tienes que llevar tú por dentro.',
        truco='Empieza por el acento 3+3+2 en una sola nota, sin melodía y sin izquierda. Dilo en voz '
              'alta: UN-o-o DOS-o-o TRES-o, mientras el pie marca cuatro. Cuando eso salga solo, la '
              'canción está resuelta: todo lo demás son notas largas.',
        sabias='Ed Sheeran la escribió con Amy Wadge en una tarde, en el sofá de su casa. El acento '
               '3+3+2 no es suyo: viene del pop latino y del góspel, y es lo que hace que una balada '
               'en 4/4 no suene cuadrada.',
        qr=dict(titulo='Escucha la original',
                texto='Cuenta con el pie hasta cuatro y fíjate en que la voz nunca entra en el uno.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Esta canción no es de dedos: es de reloj. Y su reloj es el acento 3+3+2, que es lo que '
              'la hace sonar a lo que suena. Por eso el paso 1 no se toca con las dos manos ni con '
              'melodía: es percusión en una sola nota. De la derecha solo se cita el ritmo, porque sus '
              'alturas no están medidas.',
        reglas=['ARMADURA DE RE', 'EL PIE MARCA CUATRO', 'EN UNA SOLA NOTA'],
        bloques=[
            dict(num=1, titulo='El acento que se corre de sitio',
                 pista='ocho corcheas iguales agrupadas 3+3+2 · aprieta un poco la primera de cada grupo',
                 sistemas=[
                     dict(cap='a) dilo en voz alta: UN-o-o DOS-o-o TRES-o · y que el pie siga marcando cuatro',
                          events=[{'pitch': p, 'dur': 'e', 'beam': b} for p, b in
                                  [('D5', 91), ('D5', 91), ('D5', 91),
                                   ('D5', 92), ('D5', 92), ('D5', 92),
                                   ('D5', 93), ('D5', 93)]] +
                                 [{'pitch': p, 'dur': 'e', 'beam': b} for p, b in
                                  [('F5', 94), ('F5', 94), ('F5', 94),
                                   ('F5', 95), ('F5', 95), ('F5', 95),
                                   ('F5', 96), ('F5', 96)]] +
                                 [n('D5', 'w')],
                          acento=True,
                          bars=3),
                     dict(cap='b) y el ritmo de la entrada, también en una sola nota · silencio de '
                              'blanca y entras: cuenta UN-dos-TRES-cuatro',
                          events=_en_una_nota(CONTRA), bars=4, show_time=False),
                     dict(cap='c) el 3+3+2 y la entrada, encadenados · así es como se alternan en la '
                              'canción, y así es como hay que poder contarlos sin parar',
                          events=[{'pitch': 'D5', 'dur': 'e', 'beam': 97 + i // 3}
                                  for i in range(6)] +
                                 [{'pitch': 'D5', 'dur': 'e', 'beam': 99} for _ in range(2)] +
                                 _en_una_nota(CONTRA[:7]),
                          pedal=4,
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTO VA EN UNA SOLA NOTA',
                 texto='Porque de la mano derecha de esta pieza no he medido las alturas con la '
                       'seguridad que necesito, y lo que no está medido no se escribe. Pero el ritmo sí '
                       'se ve sin ninguna duda, y resulta que el ritmo es justo lo difícil: si lo '
                       'tienes, las notas las lees de la partitura sin problema. Al revés no funciona.'),
            dict(num=2, titulo='La izquierda: cuatro cosas en cuatro compases', clef='bass',
                 pista='se ataca una vez y ya está · no vuelvas a tocar la nota “por si acaso”',
                 sistemas=[
                     dict(cap='a) cc. 1–4 · un Re dos compases y un La otros dos: eso es todo',
                          events=SOSTEN, bars=4, clef='bass'),
                     dict(cap='b) el ciclo entero, que es lo que vuelve toda la canción · y cada nota '
                              'nueva es un cambio de pedal',
                          events=[n('D2', 'w'), n('A2', 'w'), n('B2', 'w'), n('G2', 'w'),
                                  n('D2', 'w'), n('A2', 'w'), n('G2', 'w'), n('D2', 'w')],
                          bars=4, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='El reloj ya está por dentro y la izquierda no cambia. Lo que queda es juntarlas — y '
              'darse cuenta de que hay muchísimo menos que aprender de lo que parece.',
        reglas=['CUATRO COMPASES SON MEDIA CANCIÓN', 'EL PEDAL CAMBIA CON EL BAJO', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='Juntarlas, cc. 1–2', clef='bass',
                 pista='primero cada una contando en voz alta, y solo después las dos a la vez',
                 sistemas=[
                     dict(cap='a) la izquierda sola, contando los cuatro tiempos que NO tocas',
                          events=[n('D2', 'w'), n('A2', 'w')], bars=2, clef='bass'),
                     dict(cap='b) y la derecha sola encima de ese mismo silencio mental, en una nota',
                          events=[Rh, n('F5', 'e'), n('F5', 'e'), n('F5', 'q'),
                                  n('F5', 'h.'), n('F5', 'q')], bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='HAY MENOS QUE APRENDER DE LO QUE PARECE',
                 texto='Comparando la partitura compás a compás salen seis compases exactamente iguales '
                       '(los cc. 4, 7, 10, 17, 38 y 41) y otros tres más (39, 42 y 45). La canción está '
                       'construida sobre una célula de cuatro compases que vuelve todo el rato. Antes '
                       'de estudiar nada, marca con lápiz los compases que se repiten: lo nuevo de '
                       'verdad es muy poco.'),
            dict(num=4, titulo='El pedal, que es la tercera mano', clef='bass',
                 pista='el pedal cambia cuando cambia la nota grave, no cuando cambia la melodía',
                 sistemas=[
                     dict(cap='a) pisa al atacar y cambia justo al llegar la nota nueva · ocho compases '
                              'seguidos, escuchando que no se emborrone',
                          events=[n('D2', 'w'), n('B2', 'w'), n('G2', 'w'), n('A2', 'w'),
                                  n('D2', 'w'), n('B2', 'w'), n('G2', 'w'), n('A2', 'w')],
                          bars=8, clef='bass'),
                     dict(cap='b) y el mismo ciclo en blancas, dos por compás · para notar en la mano '
                              'dónde cae exactamente el cambio de pedal',
                          events=[n('D2', 'h'), n('D2', 'h'), n('B2', 'h'), n('B2', 'h'),
                                  n('G2', 'h'), n('G2', 'h'), n('A2', 'h'), n('A2', 'h')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='SIN PEDAL VAS A PENSAR QUE LA PARTITURA ESTÁ MAL',
                 texto='Escucha la grabación con auriculares: el piano suena lleno todo el rato y casi '
                       'no se mueve nada. Eso no lo hace la mano, lo hace el pie. La izquierda ataca '
                       'una nota grave y la deja; el pedal se encarga de que siga sonando mientras la '
                       'derecha canta encima. Si tocas esta canción sin pedal va a sonar vacía, y no '
                       'es que esté mal escrita: es que falta el pie.'),
            dict(tipo='escalera', valores=[80, 96, 110, 122, 134, 145],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
