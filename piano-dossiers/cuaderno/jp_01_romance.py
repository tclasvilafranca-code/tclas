# -*- coding: utf-8 -*-
"""Romance, de Diabelli (pieza 1 de Josep). Formato ADULTO exigente.

   Josep tiene la edad y el nivel de José María, pero lleva más tiempo en clase
   y le gustan los retos. El formato es el mismo (seis hojas, con dedos y
   lectura separadas) y lo que cambia es el listón: cada hoja de trabajo nombra
   la dificultad concreta de la semana en un recuadro de RETO, y la meta se
   escribe con números.

   Lo comprobado sobre el PDF de su carpeta de Drive (free-scores.com,
   "6 Sonatas for Piano 4-hands op. 163, no. 1, Mvmt. 2", 2 páginas):

     - Do mayor: detrás de la clave no hay nada.
     - Compás partido (¢): cuatro tiempos contados de dos en dos. Pone
       "Andantino", "p dolce" y "sempre legato".
     - La edición lo dice en el título: "Primo part for 5 fingers with
       stationary hand position". La mano no se mueve en toda la pieza.
     - Los dos pentagramas del Primo van en clave de sol, con 8va encima del
       de arriba, y las dos manos tocan lo mismo a distancia de octava.
     - Es a cuatro manos: el Secondo lo toca la profesora.

   El archivo es EL MISMO que el de José María (md5 idéntico), así que lo
   literal coincide y lo inventado no puede: aquí el andamio arranca por
   arriba y baja, y en el de José María sube. Lo comprueba `cruzar_josep.py`.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jp_comun import (n, ac, reto, plan, a_cuatro_manos, ordenar, nombres,
                      figuras, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=1, nivel='intermedio', slug='RomanceDiabelli',
    formato='adulto',
    titulo_corto='Romance · Diabelli', time_sig=(2, 2), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'Romance-Diabelli 4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=diabelli+op+163+romance+piano+4+hands',

    ficha=dict(
        titulo='Romance',
        autor='Anton Diabelli · 6 Sonatinas a cuatro manos, op. 163 nº 1 · parte del Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', 'Partido (¢)'),
               ('Carácter', 'Andantino'), ('Manos', 'Las dos, al unísono'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='El mismo compás, en las dos manos',
        pie_ritmos='Andamio en Do mayor: el dibujo baja, que es lo que hace la frase, y las notas '
                   'exactas están en tu partitura. Las dos manos tocan lo mismo a una octava.',
        armonia=dict(
            titulo='Por qué esta pieza abre el curso y no lo cierra',
            tarjetas=[
                ('POSICIÓN FIJA', 'Cinco dedos',
                 'Lo dice el título de la edición. Es la única pieza del cuaderno donde no tienes '
                 'que buscar ni una tecla: colocas la mano y ya está.'),
                ('AL UNÍSONO', 'Las dos igual',
                 'Las dos manos hacen lo mismo a una octava. Suena fácil y es al revés: cualquier '
                 'desajuste de milésimas se oye como dos golpes en vez de uno.'),
                ('SE CUENTA EN DOS', 'Compás partido',
                 'Cuatro tiempos, pero el pulso va a la blanca. Contar cuatro aquí te va a dejar '
                 'la frase troceada.'),
                ('EL SECONDO', 'A cuatro manos',
                 'La parte de abajo la toca la profesora. Tu papel no es acompañar: llevas la '
                 'melodía, y la que se adapta es ella.'),
            ],
            pie='Diabelli escribió estas sonatinas para que un alumno pudiera tocar música de verdad '
                'desde el primer día. Que sea la más fácil del cuaderno no la hace un ejercicio: es '
                'una pieza terminada, y hay que tocarla como tal.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la frase baja y se para · andamio',
             [n('G4', 'h'), n('F4'), n('E4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'lo mismo, una octava más abajo · andamio',
             [n('G3', 'h'), n('F3'), n('E3')], AZUL, 'bass', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'La edición pone "Primo part for 5 fingers with stationary hand position".',
            'Los dos pentagramas del Primo llevan clave de sol, no uno de sol y otro de fa.',
            'Encima del pentagrama de arriba hay un 8va: suena una octava más alto de lo escrito.',
            'Pone "p dolce" (flojito y dulce) y "sempre legato" (siempre ligado).',
            'El compás es partido: cuatro tiempos contados de dos en dos.',
        ],
        reto='Que las dos manos caigan exactamente juntas. Como tocan lo mismo, no hay nada que '
             'disimule: si una llega una milésima antes, el oyente oye dos notas, no una.',
        truco='Toca las dos manos con el pedal levantado y muy fuerte. Fuerte y seco es donde peor '
              'se disimula el desajuste, así que es donde antes lo oyes. Cuando ahí caiga junto, '
              'bájalo a "p dolce" y ya no se te va a mover.',
        sabias='Diabelli fue editor además de compositor, y es el mismo que le mandó un vals a '
               'cincuenta músicos de su época para que cada uno escribiera una variación. Beethoven '
               'no escribió una: escribió treinta y tres, y salieron las Variaciones Diabelli.',
        qr=dict(titulo='Escúchala',
                texto='Escucha primero solo la parte de arriba y luego las dos. La de abajo no es '
                      'un acompañamiento cualquiera: contesta a lo que tú tocas.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La mano no se mueve y las dos hacen lo mismo, así que aquí no hay trabajo de notas: '
              'hay trabajo de precisión y de sonido. Los dos primeros pasos parecen tontos y son '
              'los que deciden cómo suena la pieza.',
        reglas=['LA MANO NO SE MUEVE DE SITIO', 'LAS DOS MANOS, EXACTAMENTE A LA VEZ',
                'SIEMPRE LIGADO, SIN CORTAR'],
        bloques=[
            dict(num=1, titulo='La posición, de arriba abajo',
                 pista='andamio en Do mayor · empieza por el dedo 5 y baja: es el orden que peor '
                       'controla todo el mundo',
                 sistemas=[
                     dict(cap='a) bajando de cinco a uno y volviendo · sin mirarte la mano',
                          events=[n('G4'), n('F4'), n('E4'), n('D4'),
                                  n('C4'), n('D4'), n('E4'), n('F4')],
                          matiz='p',
                          pedal=4,
                          bars=2),
                     dict(cap='b) y ahora de dos en dos, saltando · la mano sigue sin moverse',
                          events=[n('G4'), n('E4'), n('F4'), n('D4'),
                                  n('E4'), n('C4'), n('D4'), n('E4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE EMPIEZA BAJANDO',
                 texto='Subiendo, la mano se apoya en el pulgar y los dedos van cayendo solos. '
                       'Bajando hay que llevar cada dedo a su sitio, y ahí es donde se ve si la '
                       'posición está de verdad o solo lo parece. Si el b) te sale peor que el a), '
                       'no es casualidad: es lo que hay que arreglar esta semana.'),
            dict(num=2, titulo='La izquierda sola, con el mismo dibujo', clef='bass',
                 pista='andamio · es lo mismo del paso 1, una octava más abajo',
                 sistemas=[
                     dict(cap='a) toca esto sin mirar la derecha · el 5 de la izquierda es el '
                              'meñique, y es el que menos fuerza tiene',
                          events=[n('C3'), n('D3'), n('E3'), n('F3'),
                                  n('G3'), n('F3'), n('E3'), n('D3')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=3, titulo='Las dos a la vez, y fuerte',
                 pista='andamio · fuerte y seco: es donde antes se oye el desajuste',
                 sistemas=[
                     dict(cap='a) las dos manos tocando lo mismo · si oyes dos golpecitos en vez '
                              'de uno, para y baja la velocidad a la mitad',
                          events=[ac(('C3', 'C4'), 'h'), ac(('D3', 'D4')), ac(('E3', 'E4')),
                                  ac(('F3', 'F4'), 'h'), ac(('G3', 'G4'), 'h')],
                          bars=3),
                     dict(cap='b) y con la figura que de verdad usa la pieza: una larga y dos '
                              'cortas · cuenta "UN, dos" y las cortas caen en el dos',
                          events=[ac(('C3', 'C4'), 'h'), ac(('E3', 'E4')), ac(('D3', 'D4')),
                                  ac(('E3', 'E4'), 'h'), ac(('C3', 'C4'), 'h')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Coge los ocho primeros compases de verdad y haz lo mismo: derecha sola, '
                       'izquierda sola, las dos fuerte, las dos en "p dolce". Ocho, no toda la '
                       'pieza. Que la primera semana del curso te salgan ocho compases sonando de '
                       'verdad vale más que las dos páginas a medias.'),
        ] + bloques_extra('Do mayor', 21, 'C4', 'C3',
                          'compás de dos blancas: se cuenta de dos, no de cuatro',
                          desde=4, time_sig=(2, 2)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Romance · para casa',
            intro='Veinte minutos al día, cinco días. Esta semana no hay velocidad que ganar.',
            bloques=[
                reto('Que las dos manos caigan exactamente juntas en los ocho primeros compases.',
                     'Tócalos fuerte y seco, sin pedal, a la mitad de velocidad. Fuerte es donde '
                     'peor se disimula el desajuste: si ahí suena una sola nota, ya está.'),
                plan((5, 'La posición bajando de cinco a uno, sin mirar la mano'),
                     (5, 'Derecha sola, los ocho primeros compases'),
                     (5, 'Izquierda sola, los mismos ocho'),
                     (5, 'Las dos juntas, fuerte y lento, contando "un, dos"')),
                a_cuatro_manos('Esta pieza no se acaba en casa: la mitad de la música la toca la '
                               'profesora. Llévala aprendida a tu velocidad y decidid en clase a '
                               'cuál se toca, porque no tiene por qué ser la tuya.'),
                ordenar(['Las dos manos juntas, en "p dolce" y ligado.',
                         'Colocar la mano y hacer los cinco dedos sin mirar.',
                         'Las dos manos juntas, fuerte y seco, a media velocidad.',
                         'Cada mano por separado, los ocho primeros compases.'],
                        titulo='El orden de los cuatro pasos',
                        pista='numéralos del 1 al 4 · el orden importa'),
                nombres(['G4', 'F4', 'E4', 'D4', 'C4', 'E4', 'G4'],
                        titulo='Las notas de tu posición',
                        pista='son las cinco de siempre, desordenadas'),
                figuras([('h', 'blanca'), ('q', 'negra'), ('w', 'redonda'),
                         ('h.', 'blanca con puntillo')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='y ojo: aquí el pulso va a la blanca, no a la negra'),
                para_clase('Los ocho primeros compases con las dos manos, y a qué velocidad te '
                           'salen juntos de verdad. Si en algún sitio se te desajustan siempre en '
                           'el mismo compás, tráelo marcado.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
