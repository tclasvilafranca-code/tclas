# -*- coding: utf-8 -*-
"""Romance, de Diabelli (pieza 1 de Eduard). Formato ADULTO, seis hojas.

   El mismo repertorio que José María, con el mismo nivel: no le agobia.

   Lo comprobado sobre el PDF de su carpeta (free-scores.com, "6 Sonatas for
   Piano 4-hands op. 163, no. 1, Mvmt. 2", 2 páginas; el mismo archivo que la
   pieza 1 de José María, byte a byte):

     - Do mayor: detrás de la clave no hay nada.
     - Compás partido (la C con la raya): cuatro tiempos que se cuentan de DOS
       en dos. Pone "Andantino", "p dolce" y "sempre legato".
     - La edición lo dice en el propio título: "Primo part for 5 fingers with
       stationary hand position". La mano NO se mueve de sitio en toda la
       pieza.
     - El Primo lleva DOS pentagramas en clave de sol y las dos manos tocan lo
       mismo, a distancia de octava. Encima del de arriba hay un 8va.
     - Es a cuatro manos: el Secondo lo toca la profesora.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from ed_comun import n, ac, sil, plan, objetivo, escalera, contar, figuras, para_clase

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=1, nivel='iniciación', slug='RomanceDiabelli',
    formato='adulto',
    titulo_corto='Romance · Diabelli', time_sig=(2, 2), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source',
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
                 'Las dos manos tocan la misma melodía, la izquierda una octava más abajo.'),
                ('SE CUENTA EN DOS', 'Compás partido',
                 'El compás lleva cuatro tiempos pero se cuentan de dos en dos, con notas largas.'),
                ('NO ESTÁS SOLO', 'A cuatro manos',
                 'La otra parte, el Secondo, la toca la profesora. Tú llevas la melodía.'),
            ],
            pie='Diabelli escribió estas sonatinas justo para esto: para que un alumno que acaba de '
                'empezar pueda tocar música de verdad, y bien, desde el primer día.',
        ),
        ritmos=[
            ('MANO DERECHA', 'una nota larga y dos cortas · andamio',
             [n('C4', 'h'), n('D4'), n('E4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'lo mismo, una octava más abajo · andamio',
             [n('C3', 'h'), n('D3'), n('E3')], AZUL, 'bass', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'La edición pone "Primo part for 5 fingers with stationary hand position".',
            'Los dos pentagramas del Primo llevan clave de sol, no uno de sol y otro de fa.',
            'Encima del pentagrama de arriba hay un 8va: suena una octava más alto de lo escrito.',
            'Pone "p dolce" y "sempre legato".',
            'El compás es partido: cuatro tiempos contados de dos en dos.',
        ],
        reto='Que las dos manos toquen exactamente a la vez. Como hacen lo mismo, cualquier '
             'desajuste se oye muchísimo.',
        truco='Toca solo la mano derecha hasta que te salga sin pensar. Después pon la izquierda '
              'encima de sus cinco teclas SIN tocar, y toca solo la derecha otra vez.',
        sabias='Diabelli fue editor además de compositor, y es el mismo que le mandó un vals a '
               'cincuenta músicos para que cada uno escribiera una variación. Beethoven escribió '
               'treinta y tres, y salieron las Variaciones Diabelli.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que la parte de arriba, la tuya, es la sencilla.'),
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
                 pista='andamio en Do mayor · otro dibujo, misma posición fija',
                 sistemas=[
                     dict(cap='a) los cinco dedos, en zigzag esta vez · sin levantar la mano',
                          events=[n('E4'), n('C4'), n('F4'), n('D4'),
                                  n('G4'), n('E4'), n('F4'), n('D4')],
                          bars=2),
                     dict(cap='b) y bajando desde arriba · la mano sigue sin moverse de sitio',
                          events=[n('G4'), n('E4'), n('D4'), n('F4'),
                                  n('C4'), n('E4'), n('D4'), n('G4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTO ES LO PRIMERO',
                 texto='Casi todo lo que sale mal al empezar sale mal por buscar la tecla. Si la '
                       'mano está colocada y no se mueve, no hay nada que buscar: cada dedo tiene '
                       'su tecla y solo hay que decidir cuál baja.'),
            dict(num=2, titulo='La izquierda hace lo mismo, una octava más abajo', clef='bass',
                 pista='andamio · toca esto solo, y fíjate en que es el mismo dibujo de antes',
                 sistemas=[
                     dict(cap='a) los mismos cinco dedos, en la otra mano, en zigzag · el 1 de la '
                              'izquierda es el pulgar, igual que en la derecha',
                          events=[n('E3'), n('C3'), n('F3'), n('D3'),
                                  n('G3'), n('E3'), n('F3'), n('D3')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=3, titulo='Y ahora las dos a la vez',
                 pista='es el paso de verdad · muy despacio, y contando dos por compás',
                 sistemas=[
                     dict(cap='a) las dos manos tocando lo mismo, con otro dibujo',
                          events=[ac(('E3', 'E4'), 'h'), ac(('C3', 'C4')), ac(('F3', 'F4')),
                                  ac(('D3', 'D4'), 'h'), ac(('G3', 'G4'), 'h')],
                          bars=3),
                     dict(cap='b) y con una larga y dos cortas · cuenta "UN, dos"',
                          events=[ac(('G3', 'G4'), 'h'), ac(('F3', 'F4')), ac(('E3', 'E4')),
                                  ac(('D3', 'D4'), 'h'), ac(('C3', 'C4'), 'h')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LO QUE VIENE DESPUÉS',
                 texto='Cuando esto salga, coge la partitura y haz lo mismo con los cuatro primeros '
                       'compases de verdad: derecha sola, izquierda sola, y las dos juntas. No pases '
                       'de los cuatro compases esta semana aunque te veas capaz. Es mejor tener '
                       'cuatro que suenen bien que dieciséis a medias.'),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Romance · para casa',
            intro='Veinte minutos al día bastan, y es mejor cinco días de veinte que uno de dos horas.',
            bloques=[
                objetivo('Tocar los cuatro primeros compases con las dos manos a la vez, muy '
                         'despacio y sin parar.'),
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
                contar([n('E4'), n('C4'), n('F4'), n('D4'), n('G4'), n('E4'), n('F4'), n('D4')],
                       ['¿Cuántas notas hay en total?', '¿Cuál es la nota más grave?',
                        '¿Cuál es la nota más aguda?'],
                       titulo='Mira y cuenta',
                       pista='es el ejercicio a) de la hoja de al lado'),
                figuras([('h', 'blanca'), ('q', 'negra'), ('w', 'redonda'),
                         ('h.', 'blanca con puntillo')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='escribe el número en la caja'),
                para_clase('Los cuatro primeros compases con las dos manos, y a qué número del '
                           'metrónomo te salen juntos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
