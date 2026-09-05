# -*- coding: utf-8 -*-
"""Romance, de Diabelli — pieza 1 de Aida. Formato ADULTO exigente.

   ABRE EL ALBUM, y no por casualidad. El encargo del cliente fue "tiene cierto
   nivel, algo como Josep, pero quiero que vaya asentando bases antes de
   correr", y esta es la unica partitura de su carpeta que trae la base escrita
   en el propio titulo: *"Primo part for 5 fingers with stationary hand
   position"*. La mano se coloca y no se mueve en toda la pieza.

   Lo comprobado sobre el PDF de SU carpeta (free-scores.com, "6 Sonatas for
   Piano 4-hands op. 163, no. 1, Mvmt. 2", 2 paginas; el mismo archivo, byte a
   byte, que el de Jose Maria y el de Josep):

     - Do mayor: detras de la clave no hay nada.
     - Compas PARTIDO (¢): cuatro tiempos contados de dos en dos. Arriba pone
       "Andantino", y debajo "p dolce" y "sempre legato".
     - Los DOS pentagramas del Primo van en clave de sol —no uno de sol y otro
       de fa— y traen lo mismo nota por nota. El de arriba lleva un 8va, asi
       que las dos manos suenan a distancia de octava tocando lo escrito.
     - Es a cuatro manos: el Secondo lo toca la profesora.

   LAS ALTURAS, medidas a 300 ppp sobre el pentagrama de arriba (apertura
   morfologica de las cabezas llenas, cabezas huecas leidas a ojo con las
   lineas del pentagrama marcadas):

       c. 1   Mi5 (blanca) · La4 · La4
       c. 2   Si4 (negra con puntillo) · Do5 (corchea) · Si4 · silencio de negra

   El puntillo del c. 2 se leyo mirando DONDE ESTA EL PUNTO: cae medio espacio
   por encima de la cabeza, que es lo que hace una edicion cuando la nota va
   sobre una linea. O sea que el Si4 esta en la linea, no en el espacio.

   El archivo es el mismo que el de Jose Maria y el de Josep, asi que la CITA
   coincide y debe coincidir; lo que no puede coincidir es el andamio. El de
   Josep baja del cinco al uno y el de Jose Maria sube; aqui el andamio va por
   TERCERAS dentro de la posicion, que es otro eje. Lo comprueba
   `cruzar_aida.py`.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, reto, plan, a_cuatro_manos, nombres,
                      diferencias, acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1 del Primo, medido. Cita literal.
ARRANQUE = [n('E5', 'h'), n('A4'), n('A4')]

# El compas 2, medido: el puntillo y el silencio con que respira la frase.
SEGUNDO = [n('B4', 'q.'), n('C5', 'e'), n('B4'), sil('q')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=1, nivel='intermedio',
    slug='RomanceDiabelli', formato='adulto',
    titulo_corto='Romance · Diabelli', time_sig=(2, 2), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'Romance Diabelli 4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=diabelli+op+163+romance+piano+4+hands',

    ficha=dict(
        titulo='Romance',
        autor='Anton Diabelli · 6 Sonatinas a cuatro manos, op. 163 nº 1 · parte del Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', 'Partido (¢)'),
               ('Carácter', 'Andantino'), ('Manos', 'Al unísono'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Los dos primeros compases, medidos',
        pie_ritmos='Medido en tu partitura, a 300 puntos por pulgada. Los dos pentagramas del Primo '
                   'traen esto mismo, así que lo de arriba y lo de abajo se lee una sola vez.',
        armonia=dict(
            titulo='Por qué el curso empieza por aquí',
            tarjetas=[
                ('POSICIÓN FIJA', 'Cinco dedos',
                 'Lo dice el título de la edición, impreso: "for 5 fingers with stationary hand '
                 'position". Colocas la mano y no la mueves. Es la única del cuaderno.'),
                ('AL UNÍSONO', 'Las dos igual',
                 'Los dos pentagramas del Primo llevan clave de sol y traen lo mismo. Suena fácil y '
                 'es al revés: no hay nada que disimule un desajuste.'),
                ('SE CUENTA EN DOS', 'Compás partido',
                 'La ¢ son cuatro tiempos, pero el pulso va a la blanca. Contar cuatro aquí te deja '
                 'la frase troceada en cuatro trozos que no son.'),
                ('EL SECONDO', 'La profesora',
                 'La parte de abajo la toca ella en clase. Tú no acompañas: llevas la melodía, y la '
                 'que se adapta a ti es la otra parte.'),
            ],
            pie='Volver al piano después de años tiene una trampa conocida: las manos se acuerdan de '
                'más de lo que se acuerda la cabeza, y eso empuja a correr. Esta pieza no deja. Por '
                'eso está la primera.',
        ),
        ritmos=[
            ('COMPÁS 1', 'medido · una larga y dos cortas',
             ARRANQUE, OCRE, 'treble', None),
            ('COMPÁS 2', 'medido · el puntillo, y un silencio para respirar',
             SEGUNDO, AZUL, 'treble', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'La edición pone "Primo part for 5 fingers with stationary hand position".',
            'Los dos pentagramas del Primo llevan clave de sol, no uno de sol y otro de fa.',
            'Encima del pentagrama de arriba hay un 8va: suena una octava más alto de lo escrito.',
            'Pone "p dolce" y "sempre legato".',
            'El compás es partido: cuatro tiempos contados de dos en dos.',
        ],
        reto='Que las dos manos caigan exactamente juntas. Como tocan lo mismo, no hay armonía que '
             'tape nada: si una llega una milésima antes, se oyen dos notas en vez de una.',
        truco='Tócalo fuerte y seco, sin pedal, a la mitad de velocidad. Fuerte es donde peor se '
              'disimula el desajuste, o sea donde antes lo oyes. Cuando ahí suene una sola nota, '
              'bájalo a "p dolce" y ya no se mueve.',
        sabias='Diabelli era editor además de compositor, y es el mismo que mandó un vals suyo a '
               'cincuenta músicos para que cada uno escribiera una variación. Beethoven no escribió '
               'una: escribió treinta y tres, y de ahí salieron las Variaciones Diabelli.',
        qr=dict(titulo='Escúchala',
                texto='Escucha primero la parte de arriba sola y después las dos. La de abajo no '
                      'acompaña: contesta.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí no hay trabajo de notas: son cinco teclas blancas y la mano no se mueve. Hay '
              'trabajo de precisión y de sonido, que es otra cosa y cuesta más.',
        reglas=['LA MANO NO SE MUEVE DE SITIO', 'LAS DOS, EXACTAMENTE A LA VEZ',
                'SIEMPRE LIGADO, SIN CORTAR'],
        bloques=[
            dict(num=1, titulo='La posición, por terceras',
                 pista='andamio en Do mayor · saltando un dedo cada vez, que es lo que peor se '
                       'controla cuando la mano está quieta',
                 sistemas=[
                     dict(cap='a) de tercera en tercera, subiendo y bajando · sin mirarte la mano',
                          events=[n('C4'), n('E4'), n('D4'), n('F4'),
                                  n('E4'), n('C4'), n('D4'), n('C4')],
                          matiz='p',
                          bars=2),
                     dict(cap='b) y ahora la misma idea con la nota de fuera primero · el 5 entra '
                              'antes de que la mano esté lista, y ahí se ve',
                          events=[n('G4'), n('E4'), n('F4'), n('D4'),
                                  n('E4'), n('G4'), n('F4'), n('E4')],
                          bars=2, show_time=False),
                     dict(cap='c) y lo mismo con la izquierda sola, en su sitio del teclado · el 5 '
                              'de esta mano es el meñique y es el que menos fuerza tiene',
                          events=[n('C3'), n('E3'), n('D3'), n('F3'),
                                  n('E3'), n('G3'), n('F3'), n('E3')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ TERCERAS Y NO ESCALA',
                 texto='Una escala se toca sola: los dedos van cayendo por orden y la mano se apoya '
                       'en el pulgar. En terceras hay que llevar cada dedo a su tecla sin que el de '
                       'al lado ayude, y ahí es donde se ve si la posición está de verdad o solo lo '
                       'parece. Si el b) te sale peor que el a), no es mala suerte: es exactamente '
                       'lo que hay que arreglar esta semana.'),
            dict(num=2, titulo='Los dos primeros compases, como están escritos',
                 pista='cc. 1–2 · MEDIDOS en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) el compás 1 con la blanca partida en dos, para sentir el pulso '
                              '· en tu partitura la primera nota es UNA blanca, no dos negras',
                          events=[n('E5'), n('E5'), n('A4'), n('A4')],
                          bars=1),
                     dict(cap='b) y los dos compases tal y como están escritos, con su puntillo y '
                              'su silencio',
                          events=list(ARRANQUE) + list(SEGUNDO),
                          bars=2, show_time=False),
                     dict(cap='c) y los mismos dos compases con las dos manos, a la octava · es lo '
                              'que suena de verdad cuando tocas el Primo',
                          events=[ac(('E4', 'E5'), 'h'), ac(('A3', 'A4')), ac(('A3', 'A4')),
                                  ac(('B3', 'B4'), 'q.'), ac(('C4', 'C5'), 'e'),
                                  ac(('B3', 'B4')), sil('q')],
                          bars=2, manos='dobla', show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, y fuerte',
                 pista='andamio · fuerte y seco es donde antes se oye el desajuste',
                 sistemas=[
                     dict(cap='a) las dos tocando lo mismo a la octava · si oyes dos golpecitos en '
                              'vez de uno, baja a la mitad de velocidad',
                          events=[ac(('C3', 'C4'), 'h'), ac(('E3', 'E4')), ac(('D3', 'D4')),
                                  ac(('F3', 'F4'), 'h'), ac(('E3', 'E4'), 'h')],
                          bars=3, manos='dobla'),
                     dict(cap='b) y con la figura de la pieza: larga, corta, corta · las cortas '
                              'caen en el "dos"',
                          events=[ac(('E3', 'E4'), 'h'), ac(('C3', 'C4')), ac(('D3', 'D4')),
                                  ac(('E3', 'E4'), 'q.'), ac(('F3', 'F4'), 'e'),
                                  ac(('E3', 'E4')), ac(('C3', 'C4'))],
                          bars=3, manos='dobla', show_time=False),
                     dict(cap='c) y con un silencio al final de cada frase, que es lo que hace tu '
                              'partitura · el silencio también se toca: se cuenta',
                          events=[ac(('D3', 'D4'), 'h'), ac(('E3', 'E4')), sil('q'),
                                  ac(('F3', 'F4'), 'h'), ac(('E3', 'E4')), sil('q'),
                                  ac(('C3', 'C4'), 'h'), ac(('C3', 'C4'), 'h')],
                          bars=3, manos='dobla', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Coge los ocho primeros compases de verdad y haz este mismo recorrido: mano '
                       'derecha sola, mano izquierda sola, las dos fuerte y lento, las dos en "p '
                       'dolce". Ocho compases, no las dos páginas. Que la primera semana del curso '
                       'te salgan ocho compases sonando de verdad vale más que la pieza entera a '
                       'medias, y además es lo que hace que la segunda semana empiece de otro '
                       'sitio.'),
        ] + bloques_extra('Do mayor', 81, 'C4', 'C3',
                          'la mano quieta: cinco teclas y ni una más',
                          desde=4, time_sig=(2, 2), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Romance · para casa',
            intro='Veinte minutos al día, cinco días. Esta semana no hay velocidad que ganar: hay '
                  'una manera de tocar que montar.',
            bloques=[
                reto('Que las dos manos caigan exactamente juntas en los ocho primeros compases.',
                     'Tócalos fuerte y seco, sin pedal, a la mitad de velocidad. Fuerte es donde '
                     'peor se disimula el desajuste: si ahí suena una sola nota, ya está.'),
                plan((5, 'Las terceras del paso 1, sin mirarte la mano'),
                     (5, 'Mano derecha sola, los ocho primeros compases'),
                     (5, 'Mano izquierda sola, los mismos ocho'),
                     (5, 'Las dos juntas, fuerte y lento, contando "un, dos"')),
                a_cuatro_manos('La mitad de esta música la toca la profesora. Llévala aprendida a '
                               'tu velocidad y decidid en clase a cuál se toca, porque no tiene por '
                               'qué ser la tuya: el Secondo se mueve más que el Primo.'),
                nombres(['E5', 'A4', 'B4', 'C5', 'A4', 'B4', 'E5'],
                        titulo='Las notas de tus dos primeros compases',
                        pista='están desordenadas · escríbelas debajo de cada una'),
                diferencias(list(ARRANQUE) + list(SEGUNDO),
                            [n('E5', 'h'), n('A4'), n('A4'),
                             n('B4', 'q.'), n('C5', 'e'), n('C5'), sil('q')],
                            cuantas=1,
                            titulo='Busca la diferencia',
                            pista='arriba, tus compases 1 y 2 medidos · abajo, con una nota cambiada'),
                acuerdate('El compás partido no es un 4/4 con otro nombre. El pulso va a la blanca, '
                          'o sea dos golpes por compás y no cuatro. Si lo cuentas de cuatro, la '
                          'frase se te parte por la mitad y el "Andantino" se convierte en algo '
                          'que anda a trompicones.',
                          etiqueta='EL COMPÁS PARTIDO'),
                para_clase('Los ocho primeros compases con las dos manos, y a qué velocidad te '
                           'salen juntos de verdad. Si se te desajustan siempre en el mismo sitio, '
                           'tráelo marcado con lápiz: eso se arregla en dos minutos entre los dos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
