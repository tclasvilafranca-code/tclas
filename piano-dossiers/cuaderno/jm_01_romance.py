# -*- coding: utf-8 -*-
"""Romance, de Diabelli (pieza 1 de José María). Formato ADULTO, seis hojas.

   José María tiene unos 60 años, empezó hace poco, viene a clase y se ha
   comprado un teclado para practicar en casa. El encargo del cliente:
   material para trabajar de verdad, pero a un nivel que no agobie. De ahí las
   seis hojas (partitura · ficha · dedos · leer · cómo se estudia · el trabajo
   de la semana · papel pautado) y de ahí que la hoja de la semana lleve un
   plan de minutos por día: es lo que se lleva de la clase para los días que
   hay en medio.

   Lo comprobado sobre el PDF de su carpeta de Drive (free-scores.com,
   "6 Sonatas for Piano 4-hands op. 163, no. 1, Mvmt. 2", 2 páginas):

     - Do mayor: detrás de la clave no hay nada.
     - Compás partido (la C con la raya): cuatro tiempos que se cuentan de DOS
       en dos. Pone "Andantino", "p dolce" y "sempre legato".
     - La edición lo dice en el propio título: "Primo part for 5 fingers with
       stationary hand position". La mano NO se mueve de sitio en toda la
       pieza. Por eso es la primera del cuaderno.
     - El Primo lleva DOS pentagramas en clave de sol y las dos manos tocan lo
       mismo, a distancia de octava. Encima del de arriba hay un 8va.
     - Es a cuatro manos: el Secondo lo toca la profesora.

   Lo que NO se cita: las alturas exactas. El 8va y las ligaduras ensucian la
   medición de las cabezas, así que los ejercicios van rotulados como ANDAMIO
   en Do mayor y remiten a la partitura. (Ver TRANSCRIPCION_JM_FUENTES.md.)
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jm_comun import (n, ac, sil, plan, objetivo, escalera, contar, figuras,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# La posición fija de cinco dedos de la mano derecha del Primo, en Do mayor.
# Es andamio: la posición es la que dice la edición, las notas concretas se
# miran en la partitura.
POS = ['C4', 'D4', 'E4', 'F4', 'G4']

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=1, nivel='iniciación', slug='RomanceDiabelli',
    formato='adulto',
    titulo_corto='Romance · Diabelli', time_sig=(2, 2), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           'Romance-Diabelli 4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=diabelli+op+163+romance+piano+4+hands',

    ficha=dict(
        titulo='Romance',
        autor='Anton Diabelli · 6 Sonatinas a cuatro manos, op. 163 nº 1 · parte del Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', 'Partido (¢)'),
               ('Carácter', 'Andantino'), ('Manos', 'Las dos, al unísono'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Do mayor: el dibujo es el de tu partitura y las notas exactas las '
                   'miras allí. Las dos manos tocan lo mismo, una octava más abajo la izquierda.',
        armonia=dict(
            titulo='Por qué esta pieza es la primera del cuaderno',
            tarjetas=[
                ('LA MANO NO SE MUEVE', 'Cinco dedos',
                 'Lo dice el título de la edición: posición fija. Colocas la mano una vez y ya no '
                 'la mueves en toda la pieza.'),
                ('LAS DOS IGUALES', 'Al unísono',
                 'Las dos manos tocan la misma melodía, la izquierda una octava más abajo. Aprendes '
                 'una cosa y te sirve para las dos.'),
                ('SE CUENTA EN DOS', 'Compás partido',
                 'El compás lleva cuatro tiempos pero se cuentan de dos en dos, con notas largas. '
                 'Va más tranquilo de lo que parece.'),
                ('NO ESTÁS SOLO', 'A cuatro manos',
                 'La otra parte, el Secondo, la toca la profesora. Tú llevas la melodía y ella pone '
                 'el acompañamiento debajo.'),
            ],
            pie='Diabelli escribió estas sonatinas justo para esto: para que un alumno que acaba de '
                'empezar pueda tocar música de verdad, y bien, desde el primer día. La parte fácil '
                'no suena a ejercicio porque no lo es.',
        ),
        ritmos=[
            ('MANO DERECHA', 'una nota larga y dos cortas · andamio',
             [n('C4', 'h'), n('D4'), n('E4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'lo mismo, una octava más abajo · andamio',
             [n('C3', 'h'), n('D3'), n('E3')], AZUL, 'bass', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'La edición pone "Primo part for 5 fingers with stationary hand position": la mano se '
            'coloca una vez y no se mueve.',
            'Los dos pentagramas del Primo llevan clave de sol, no uno de sol y otro de fa.',
            'Encima del pentagrama de arriba hay un 8va: eso quiere decir que suena una octava más '
            'alto de lo que está escrito.',
            'Pone "p dolce" (flojito y dulce) y "sempre legato" (siempre ligado, sin cortar).',
            'El compás es partido: cuatro tiempos contados de dos en dos.',
        ],
        reto='Que las dos manos toquen exactamente a la vez. Como hacen lo mismo, cualquier desajuste '
             'se oye muchísimo: en vez de un sonido gordo se oyen dos golpecitos seguidos.',
        truco='Toca solo la mano derecha hasta que te salga sin pensar. Después pon la izquierda '
              'encima de sus cinco teclas SIN tocar, y toca solo la derecha otra vez, sintiendo la '
              'izquierda apoyada. Y solo entonces bájalas juntas. Es más rápido así que intentando '
              'las dos desde el principio.',
        sabias='Diabelli fue editor además de compositor, y es el mismo que le mandó un vals a '
               'cincuenta músicos de su época para que cada uno escribiera una variación. Beethoven '
               'no escribió una: escribió treinta y tres, y salieron las Variaciones Diabelli.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que la parte de arriba, la tuya, es la sencilla. Lo que suena '
                      'complicado es el acompañamiento de abajo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza tiene una ventaja enorme para empezar: la mano no se mueve de sitio y las '
              'dos hacen lo mismo. Así que el trabajo no es de notas, es de juntar las manos y de '
              'sonido. Ve por este orden y no te saltes el paso 2.',
        reglas=['LA MANO NO SE MUEVE DE SITIO', 'LAS DOS MANOS, EXACTAMENTE A LA VEZ',
                'SIEMPRE LIGADO, SIN CORTAR'],
        bloques=[
            dict(num=1, titulo='Colocar la mano y dejarla ahí',
                 pista='andamio en Do mayor · los cinco dedos sobre cinco teclas blancas seguidas',
                 sistemas=[
                     dict(cap='a) los cinco dedos, uno detrás de otro, subiendo y bajando · sin '
                              'levantar la mano, y en "p dolce" como pide tu partitura',
                          events=[dict(n('C4'), matiz='p'), n('D4'), n('E4'), n('F4'),
                                  n('G4'), n('F4'), n('E4'), n('D4')],
                          ligar=True,
                          bars=2),
                     dict(cap='b) y ahora salteados, que es lo que hace la música de verdad · la '
                              'mano sigue sin moverse de sitio',
                          events=[n('C4'), n('E4'), n('D4'), n('F4'),
                                  n('E4'), n('G4'), n('F4'), n('E4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTO ES LO PRIMERO',
                 texto='Casi todo lo que sale mal al empezar sale mal por buscar la tecla. Si la mano '
                       'está colocada y no se mueve, no hay nada que buscar: cada dedo tiene su tecla '
                       'y solo hay que decidir cuál baja. Esta pieza está escrita justo para eso, así '
                       'que aprovéchalo: no la toques mirándote las manos.'),
            dict(num=2, titulo='La izquierda hace lo mismo, una octava más abajo', clef='bass',
                 pista='andamio · toca esto solo, y fíjate en que es el mismo dibujo de antes',
                 sistemas=[
                     dict(cap='a) los mismos cinco dedos, en la otra mano · el 1 de la izquierda es '
                              'el pulgar, igual que en la derecha',
                          events=[n('G3'), n('F3'), n('E3'), n('D3'),
                                  n('C3'), n('D3'), n('E3'), n('F3')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=3, titulo='Y ahora las dos a la vez',
                 pista='es el paso de verdad · muy despacio, y contando dos por compás',
                 sistemas=[
                     dict(cap='a) las dos manos tocando lo mismo · si oyes dos golpecitos seguidos '
                              'en vez de uno, para y ve más lento',
                          events=[ac(('C3', 'C4'), 'h'), ac(('D3', 'D4')), ac(('E3', 'E4')),
                                  ac(('F3', 'F4'), 'h'), ac(('E3', 'E4'), 'h')],
                          bars=3),
                     dict(cap='b) y con el dibujo que de verdad usa la pieza: una larga y dos '
                              'cortas · cuenta "UN, dos" y las cortas caen en el dos',
                          events=[ac(('E3', 'E4'), 'h'), ac(('D3', 'D4')), ac(('C3', 'C4')),
                                  ac(('D3', 'D4'), 'h'), ac(('C3', 'C4'), 'h')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LO QUE VIENE DESPUÉS',
                 texto='Cuando esto salga, coge la partitura y haz lo mismo con los cuatro primeros '
                       'compases de verdad: derecha sola, izquierda sola, y las dos juntas. No pases '
                       'de los cuatro compases esta semana aunque te veas capaz. Es mejor tener '
                       'cuatro que suenen bien que dieciséis a medias.'),
        ] + bloques_extra('Do mayor', 28, 'C4', 'C3',
                          'compás de dos blancas: se cuenta de dos, no de cuatro',
                          desde=4, time_sig=(2, 2)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Romance · para casa',
            intro='Veinte minutos al día bastan, y es mejor cinco días de veinte que uno de dos horas.',
            bloques=[
                objetivo('Tocar los cuatro primeros compases con las dos manos a la vez, muy '
                         'despacio y sin parar. La velocidad no importa esta semana.'),
                plan((5, 'Colocar la mano y hacer los cinco dedos, sin mirar'),
                     (5, 'La derecha sola, los cuatro primeros compases'),
                     (5, 'La izquierda sola, los mismos cuatro compases'),
                     (5, 'Las dos juntas, contando dos por compás en voz alta')),
                escalera((40, 'las dos manos, muy lento y sin parar'),
                         (55, 'los cuatro primeros compases seguidos'),
                         (70, 'los ocho, en "p dolce" y ligado'),
                         meta='tocar los ocho primeros compases seguidos y ligados · tu partitura '
                              'pone "Andantino" pero no trae número de metrónomo',
                         notas=['Apunta cada día el número al que te has quedado.']),
                contar([n('C4'), n('E4'), n('D4'), n('F4'), n('E4'), n('G4'), n('F4'), n('E4')],
                       ['¿Cuántos Mi hay?', '¿Cuántas notas hay en total?',
                        '¿Cuál es la nota más aguda?'],
                       titulo='Mira y cuenta',
                       pista='es el ejercicio b) de la hoja de al lado'),
                figuras([('h', 'blanca'), ('q', 'negra'), ('w', 'redonda'),
                         ('h.', 'blanca con puntillo')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='escribe el número en la caja'),
                para_clase('Los cuatro primeros compases con las dos manos, y a qué número del '
                           'metrónomo te salen juntos. El Secondo lo toco yo: ven con lo tuyo '
                           'aprendido a tu velocidad y ya lo ajustamos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
