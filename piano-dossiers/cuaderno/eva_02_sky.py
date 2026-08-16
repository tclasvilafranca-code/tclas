# -*- coding: utf-8 -*-
"""A Sky Full of Stars (canción 2 de Eva, nivel avanzado).

   Misma edición que la de Dilan (sha256 idéntico), así que la medición se
   importa de `dilan_12_sky`. Ver TRANSCRIPCION_D12_14.md.

   El camino de estudio es el contrario que el de Dilan, a propósito:

     - A Dilan se le entra por el RIFF y se le va quitando relleno hasta
       descubrir que debajo solo hay dos notas.
     - A Eva se le entra por ARRIBA: primero la melodía, que son cuatro notas
       larguísimas, y desde ahí se baja al acompañamiento. En una pieza que
       tiene cuatro compases de música y veintitrés de repetición, ver el
       conjunto antes que el detalle es lo que evita estudiarla a ciegas.

   Y donde el material es el mismo (el riff no tiene más que una forma), lo
   que cambia es la FIGURA: Eva trabaja primero la quinta sostenida —redondas,
   para oír el acorde— y solo después la picotea. Dilan lo hace al revés.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_12_sky import n, ac, corch, riff, SIb, FAq, LAm7, SOL

HERE = os.path.dirname(__file__)
FA = 'Fa mayor'
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Eva', num=2, nivel='avanzado', slug='SkyFullOfStars',
    titulo_corto='A Sky Full of Stars', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'a-sky-full-of-stars-coldplay.pdf'),
    yt='https://www.youtube.com/results?search_query=coldplay+a+sky+full+of+stars',

    ficha=dict(
        titulo='A Sky Full of Stars',
        autor='Coldplay y Avicii · arr. para piano',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', '4/4'),
               ('Mano izq.', 'Quintas picadas'), ('Mano dcha.', 'Notas larguísimas'),
               ('Compases nuevos', '4')],
        armonia=dict(
            titulo='Cuatro compases y veintitrés de repetición',
            tarjetas=[
                ('EL BUCLE', 'Si♭ · Fa · Si♭ · Fa',
                 'Dos acordes alternando. Eso es la canción entera, de principio a fin.'),
                ('LO QUE SE REPITE', 'cc. 5 = 9 = 17',
                 'Y los cc. 7 y 11 también, y los cc. 12 y 20. Medido compás a compás.'),
                ('LA INTRO', 'La m7 · Sol',
                 'Es el único sitio con tres notas, y el único donde las dos manos tocan lo mismo.'),
            ],
            pie='La dificultad de esta canción no está en las notas: está en que el compás veintitrés '
                'suene igual de flojo que el primero.',
        ),
        especial=[
            'La armadura de Fa mayor lleva un bemol: todos los Si.',
            'La izquierda toca quintas: fundamental y quinta, sin la tercera del acorde.',
            'El ritmo real del riff es corchea con puntillo más semicorchea, no dos corcheas iguales.',
            'La melodía de los cc. 5–8 son cuatro notas: Do, La, Si, La, Sol.',
            'En los cc. 13–16 la melodía es la misma, una octava más arriba.',
            'La edición trae la digitación escrita: 3-1, 4-1, 5-1. Úsala siempre igual.',
            'Los cc. 5, 9 y 17 son el mismo compás; los cc. 7 y 11 también, y los cc. 12 y 20.',
            'La introducción es el único sitio de la pieza donde las dos manos tocan lo mismo.',
        ],
        ritmos=[
            ('MI', 'la quinta, alternando · en la partitura va en corcheas con puntillo',
             [n(SIb[0]), n(SIb[1]), n(SIb[0]), n(SIb[1])], OCRE, 'bass', FA),
            ('MD', 'una redonda: se ataca y se aguanta',
             [n('C5', 'w')], AZUL, 'treble', FA),
        ],
        reto='Aguantar. El riff se repite doscientas veces y el brazo se endurece sin que te des '
             'cuenta; cuando eso pasa, la canción deja de sonar a Coldplay y suena a ejercicio.',
        truco='Empieza por la melodía, no por el riff. Son cuatro notas largas: cuando las tengas, '
              'ya sabes cómo suena la canción entera y el riff se convierte en el fondo, que es lo '
              'que es. Y comprueba el brazo cada dos compases: si pesa, para.',
        sabias='La escribieron Coldplay con Avicii, que era DJ y no pianista: el riff está pensado '
               'como un bucle de música electrónica, y por eso se repite sin cambiar nada. Lo que en '
               'una canción de piano sería un defecto, aquí es el estilo.',
        qr=dict(titulo='Escucha la original',
                texto='Fíjate en que el piano nunca sube de volumen. Es el resto lo que crece.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Esta canción tiene cuatro compases de música y veintitrés de repetición. Por eso se '
              'empieza por arriba: primero la melodía, que son cuatro notas larguísimas, y solo '
              'después se baja al acompañamiento. Si empiezas por el riff, te pasas dos semanas '
              'picoteando sin saber para qué.',
        reglas=['ARMADURA DE FA', 'PRIMERO LA MELODÍA', 'EL BRAZO SUELTO'],
        bloques=[
            dict(num=1, titulo='La melodía: cuatro notas',
                 pista='cc. 5–8 y 13–16 medidos · cuenta los cuatro tiempos de cada nota en voz alta',
                 sistemas=[
                     dict(cap='a) cc. 5–8 · aguántalas enteras y no las sueltes antes de tiempo',
                          events=[n('C5', 'w'), n('A4', 'h'), n('B4', 'h'),
                                  n('A4', 'w'), n('G4', 'w')],
                          bars=4),
                     dict(cap='b) cc. 13–16 · las mismas notas, una octava arriba: aquí se abre',
                          events=[n('F5', 'h'), n('C5'), n('D5'),
                                  n('C5', 'h'), n('F5', 'h'),
                                  n('F5', 'h'), n('G5'), n('E5'),
                                  n('F5', 'h'), n('A5', 'h')],
                          bars=4, show_time=False),
                     dict(cap='c) y solo las notas, sin la espera · así se ve de un vistazo lo poco '
                              'que se mueve la melodía en toda la canción',
                          events=[n('C5', 'h'), n('A4', 'h'), n('B4', 'h'), n('A4', 'h'),
                                  n('G4', 'h'), n('F5', 'h'), n('E5', 'h'), n('F5', 'h')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE EMPIEZA POR LA MELODÍA',
                 texto='Porque son cuatro notas y en cinco minutos ya sabes cómo suena la canción. A '
                       'partir de ahí el riff deja de ser un ejercicio y pasa a ser lo que de verdad '
                       'es: el fondo sobre el que cantan esas cuatro notas. Y cuando algo es el fondo, '
                       'se toca más flojo sin que nadie te lo tenga que decir.'),
            dict(num=2, titulo='Lo que hay debajo son dos notas', clef='bass',
                 pista='quita el picoteo y quédate con la quinta sostenida · Si♭ y Fa, nada más',
                 sistemas=[
                     dict(cap='a) la quinta entera, sostenida · escucha el acorde antes de romperlo',
                          events=[ac(SIb, 'w'), ac(FAq, 'w'), ac(SIb, 'w'), ac(FAq, 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) y solo la nota de abajo · Si♭ · Fa · Si♭ · Fa: eso es la canción entera',
                          events=[n('B2', 'h'), n('F2', 'h')] * 4,
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) cc. 3–4 · la introducción, que es el único sitio con tres notas y el '
                              'único donde las dos manos tocan lo mismo',
                          events=[ac(LAm7, 'h'), ac(LAm7, 'h'), ac(SOL, 'h'), ac(SOL, 'h'),
                                  ac(LAm7, 'w')],
                          bars=3, clef='bass', show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='Ya sabes lo que suena y lo que hay debajo. Solo queda picotearlo — que es lo único que '
              'faltaba— y probar el aguante, que en esta canción es la dificultad de verdad: el riff '
              'se repite doscientas veces y el brazo se endurece sin que te des cuenta.',
        reglas=['CUATRO COMPASES SON LA CANCIÓN', 'IGUAL DE FLOJO AL FINAL QUE AL PRINCIPIO', 'SIN ACELERAR'],
        bloques=[
            dict(num=3, titulo='El picoteo', clef='bass',
                 pista='el ritmo real lleva puntillo · aquí en corcheas iguales, solo para leerlo',
                 sistemas=[
                     dict(cap='a) sobre Fa, cuatro compases seguidos · sin acentuar ninguna nota',
                          events=riff(*FAq, veces=4), bars=4, clef='bass'),
                     dict(cap='b) sobre Si♭, que es donde cae la mano más abierta',
                          events=riff(*SIb, veces=4), bars=4, clef='bass', show_time=False),
                     dict(cap='c) y alternando, que es como está escrito · aquí se ve si llegas '
                              'colocada al cambio',
                          events=riff(*SIb) + riff(*FAq) + riff(*SIb) + riff(*FAq),
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL RITMO QUE NO ESTÁ ESCRITO AQUÍ',
                 texto='En tu partitura la primera nota de cada pareja dura un poco más que la segunda: '
                       'corchea con puntillo y semicorchea. Eso es lo que le da el balanceo, y no lo '
                       'puedo escribir con las figuras de este cuaderno. Léelo aquí y míralo en la '
                       'página 1: si tocas las dos iguales, el riff se queda plano.'),
            dict(num=4, titulo='Ocho compases de aguante', clef='bass',
                 pista='la prueba de verdad · si el brazo se pone duro, para y empieza otra vez',
                 sistemas=[
                     dict(cap='a) seis compases en blancas, dos golpes por compás · que el sexto '
                              'suene igual de flojo que el primero',
                          events=[ac(SIb, 'h'), ac(SIb, 'h'), ac(FAq, 'h'), ac(FAq, 'h'),
                                  ac(SIb, 'h'), ac(SIb, 'h'), ac(FAq, 'h'), ac(FAq, 'h'),
                                  ac(SIb, 'h'), ac(SIb, 'h'), ac(FAq, 'w')],
                          bars=6, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='HAY CUATRO COMPASES, NO VEINTITRÉS',
                 texto='Comparando compás a compás salen tres parejas idénticas: los cc. 5, 9 y 17 son '
                       'el mismo compás; los cc. 7 y 11 también; y los cc. 12 y 20 también. Antes de '
                       'estudiar, marca dónde vuelve a empezar el bucle: de veintitrés compases solo '
                       'hay que aprender cuatro. Y usa la digitación que trae escrita (3-1, 4-1, 5-1): '
                       'en una canción que repite el mismo gesto doscientas veces, usar siempre los '
                       'mismos dedos es la diferencia entre que salga o no salga.'),
            dict(tipo='escalera', valores=[60, 72, 84, 96, 108, 118],
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
