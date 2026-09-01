# -*- coding: utf-8 -*-
"""The Sound of Silence — pieza 14 de Aida. Formato ADULTO exigente.

   Segunda de la etapa del modo menor, y la primera del cuaderno en la que la
   izquierda toca ACORDES DE TRES NOTAS todo el rato mientras la derecha lleva
   la melodia. Hasta aqui la izquierda hacia una nota, o dos; aqui son tres a
   la vez y hay que colocarlas antes de tocar.

   Lo comprobado sobre el PDF de SU carpeta (edicion "PianoSampol · Repertorio,
   Siglo XX / siglo XXI", "Version I", 2 paginas). Es solo suya.

     - Detras de la clave hay **UN BEMOL**: Re menor.
     - El compas esta escrito con la **C** de compasillo, que es **4/4**.
     - NO trae tempo impreso ni caracter escrito. Lo que se diga de la
       velocidad sale de la clase, y asi esta dicho en la hoja.
     - La derecha entra despues de un compas entero callado, y las dos frases
       siguientes empiezan tambien con un silencio.

   LAS ALTURAS de los cuatro primeros compases, medidas a 150 ppp sobre las
   cinco lineas de cada pentagrama:

       DERECHA    c. 1  compas entero de silencio
                  c. 2  silencio de negra · Re4 · Re4 · Fa4 · Fa4 · La4 · La4
                        (las seis, corcheas)
                  c. 3  Sol4, redonda
                  c. 4  silencio de corchea · Do4 · Do4 · Do4 · Mi4 · Mi4 ·
                        Sol4 · Sol4  (las siete, corcheas)

       IZQUIERDA  cc. 1 y 2  el acorde de RE MENOR (Re3 · Fa3 · La3), dos
                             blancas por compas
                  cc. 3 y 4  el acorde de DO MAYOR (Do3 · Mi3 · Sol3), igual

   Cada compas cierra en 4: 1 + 0,5 x 6 en el segundo, y 0,5 x 8 en el cuarto.

   Y una cosa que se ve al medir y no al mirar: las dos frases de la derecha
   son la MISMA forma —dos notas repetidas, dos mas arriba, dos mas arriba— una
   sobre el acorde de Re menor y otra sobre el de Do mayor. Aprendida una, la
   otra es la misma mano movida de sitio.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, reto, plan, objetivo, teclado,
                      ordenar, figuras, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los cc. 2, 3 y 4 de la DERECHA, medidos. Cita literal.
D2 = [sil('q')] + corch(['D4', 'D4']) + corch(['F4', 'F4']) + corch(['A4', 'A4'])
D3 = [n('G4', 'w')]
D4 = [sil('e')] + corch(['C4', 'C4']) + corch(['C4', 'E4']) + corch(['E4', 'G4']) + \
     corch(['G4'])

# Y la IZQUIERDA: dos blancas por compas, siempre el acorde entero. Medido.
REM = ac(('D3', 'F3', 'A3'), 'h')
DOM = ac(('C3', 'E3', 'G3'), 'h')

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=14, nivel='intermedio',
    slug='TheSoundOfSilence', formato='adulto',
    titulo_corto='The Sound of Silence', time_sig=(4, 4), key_sig='Re menor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'The Sound of Silence.pdf'),
    yt='https://www.youtube.com/results?search_query=the+sound+of+silence+piano',

    ficha=dict(
        titulo='The Sound of Silence',
        autor='Simon & Garfunkel · ed. PianoSampol · Versión I',
        datos=[('Tonalidad', 'Re menor'), ('Compás', '4/4 (C)'),
               ('Armadura', 'Un bemol'), ('Izquierda', 'Acordes de tres'),
               ('Empieza', 'Un compás después')],
        titulo_ritmos='El compás 2, medido',
        pie_ritmos='Arriba, el c. 2 de la derecha MEDIDO en tu partitura: entra después de un '
                   'silencio de negra y va toda en corcheas. Abajo, la izquierda del c. 1, medida: '
                   'el acorde de Re menor en dos blancas.',
        armonia=dict(
            titulo='Dos acordes y dos frases',
            tarjetas=[
                ('Re menor', 'Re · Fa · La',
                 'El acorde de los cc. 1 y 2, y el de la primera frase. Las tres notas de la '
                 'melodía de esa frase salen de él: Re, Fa y La, cada una dos veces.'),
                ('Do mayor', 'Do · Mi · Sol',
                 'El de los cc. 3 y 4. Y otra vez: las tres notas de la segunda frase son las tres '
                 'del acorde. La melodía no se inventa nada, sube por el acorde de debajo.'),
                ('LA MISMA FORMA', 'Dos veces',
                 'Dos notas repetidas, dos más arriba, dos más arriba. Aprendida la primera frase, '
                 'la segunda es la misma mano puesta un grado más abajo.'),
                ('LA C DEL COMPÁS', 'Es 4/4',
                 'Esa C no quiere decir "compás de Do": es la manera antigua de escribir el 4/4, y '
                 'se lee igual, cuatro negras por compás.'),
            ],
            pie='Cuando la melodía sale del acorde que hay debajo, no hay que aprender dos cosas: '
                'se aprende el acorde y la melodía cae sola. Colócate primero la mano izquierda en '
                'Re menor y busca con la derecha esas mismas tres notas una octava más arriba.',
        ),
        ritmos=[
            ('DERECHA', 'el c. 2, MEDIDO · entra tras un silencio de negra',
             D2, OCRE, 'treble', 'Re menor'),
            ('IZQUIERDA', 'el c. 1, medido · el acorde de Re menor, dos blancas',
             [REM, REM], AZUL, 'bass', 'Re menor'),
        ],
        especial=[
            'Detrás de la clave hay un bemol: la tonalidad es Re menor.',
            'El compás está escrito con una C, y quiere decir 4/4.',
            'La partitura no trae ni tempo ni carácter escritos.',
            'El compás 1 es un compás entero de silencio en la derecha.',
            'La izquierda toca acordes de tres notas, dos por compás.',
            'Las dos frases de la derecha van todas en corcheas.',
            'La segunda frase empieza con un silencio de corchea, no de negra.',
        ],
        reto='Colocar tres notas a la vez con la izquierda sin mirarla, mientras la derecha lleva '
             'la melodía. Es la primera pieza del cuaderno en la que la izquierda hace acordes de '
             'tres de principio a fin.',
        truco='Aprende el acorde con la mano sola y en silencio: pon los dedos, levántalos, vuelve '
              'a ponerlos. Cuando caigan a la primera diez veces seguidas, mete la derecha.',
        sabias='Paul Simon la escribió con la guitarra en el cuarto de baño de su casa, a oscuras y '
               'con el grifo abierto, porque decía que el eco le ayudaba a pensar. El disco pasó '
               'sin pena ni gloria hasta que el productor le añadió batería y bajo sin decírselo a '
               'nadie: esa versión fue la que llegó al número uno.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo las dos primeras frases y cuenta las notas de cada una: seis en '
                      'la primera y siete en la segunda. Y fíjate en que las dos suben igual.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana se empieza por la izquierda, y no es lo normal: los acordes de tres se '
              'colocan antes de tocar nada, porque si no la mano llega tarde siempre.',
        reglas=['LA IZQUIERDA PRIMERO, Y SOLA', 'TRES NOTAS A LA VEZ, SIN MIRARLAS',
                'LA C DEL PRINCIPIO ES UN 4/4'],
        bloques=[
            dict(num=1, titulo='Los dos acordes de la izquierda',
                 pista='cc. 1 a 4 de la mano izquierda · MEDIDO · dos blancas por compás',
                 sistemas=[
                     dict(cap='a) los cuatro compases tal y como están · dos compases de Re menor y '
                              'dos de Do mayor, dos blancas en cada uno',
                          events=[REM, REM, REM, REM, DOM, DOM, DOM, DOM],
                          bars=4, clef='bass', key_sig='Re menor'),
                     dict(cap='b) y con un solo acorde por compás, para practicar el cambio · en tu '
                              'partitura son dos blancas, no una redonda',
                          events=[ac(('D3', 'F3', 'A3'), 'w'), ac(('C3', 'E3', 'G3'), 'w'),
                                  ac(('D3', 'F3', 'A3'), 'w'), ac(('C3', 'E3', 'G3'), 'w')],
                          bars=4, clef='bass', show_time=False, key_sig='Re menor'),
                     dict(cap='c) y los dos acordes desplegados, nota a nota, para oír de qué están '
                              'hechos · andamio sobre esos mismos dos acordes',
                          events=[n('D3'), n('F3'), n('A3'), n('D4'),
                                  n('C3'), n('E3'), n('G3'), n('C4')],
                          bars=2, clef='bass', show_time=False, key_sig='Re menor'),
                     dict(cap='d) y los dos alternando cada dos tiempos, que es el cambio al doble '
                              'de rápido · andamio: en la pieza el acorde dura dos compases',
                          events=[REM, DOM, REM, DOM],
                          bars=2, clef='bass', show_time=False, key_sig='Re menor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ UN ACORDE SE COLOCA Y NO SE BUSCA',
                 texto='Tres notas a la vez no se leen de una en una: si lees "Re, luego Fa, luego '
                       'La" llegas tarde siempre, porque la mano tiene que hacer tres viajes. Lo '
                       'que se aprende es la FORMA: los dedos 5, 3 y 1 abiertos a la misma '
                       'distancia, un salto de tres teclas blancas entre cada dos. Cuando la mano '
                       'sabe la forma, cambiar de Re menor a Do mayor es mover el bloque entero un '
                       'sitio, y eso se hace sin mirar.'),
            dict(num=2, titulo='La melodía sale del acorde',
                 pista='cc. 2 y 4 de la derecha · MEDIDO · dos notas repetidas, dos más arriba, dos '
                       'más arriba',
                 sistemas=[
                     dict(cap='a) el c. 4 · Do, Mi y Sol: son las tres notas del acorde que toca la '
                              'izquierda debajo, y entra tras un silencio de corchea',
                          events=list(D4), matiz='mp', bars=1, key_sig='Re menor'),
                     dict(cap='b) y el mismo compás con una nota por tiempo, para colocar la mano · '
                              'en tu partitura son corcheas',
                          events=[n('C4'), n('C4'), n('E4'), n('G4')],
                          bars=1, show_time=False, key_sig='Re menor'),
                     dict(cap='c) y la misma forma sobre el acorde de Re menor · andamio: dos notas '
                              'repetidas, dos más arriba, dos más arriba, y la vuelta',
                          events=corch(['D4', 'D4']) + corch(['F4', 'F4']) +
                                 corch(['A4', 'A4']) + corch(['F4', 'D4']),
                          bars=1, show_time=False, key_sig='Re menor'),
                     dict(cap='d) y la misma forma sobre el de Do mayor, subiendo y bajando · si te '
                              'sale igual de fácil que la de arriba, la pieza ya está leída',
                          events=corch(['C4', 'C4']) + corch(['E4', 'E4']) +
                                 corch(['G4', 'G4']) + corch(['E4', 'C4']),
                          bars=1, show_time=False, key_sig='Re menor'),
                 ]),
            dict(num=3, titulo='Las dos manos, con los silencios contados',
                 pista='cc. 1 y 2 con las dos manos · MEDIDO · la derecha calla un compás entero y '
                       'luego una negra más',
                 sistemas=[
                     dict(cap='a) los cc. 1 y 2 · el primer compás la derecha calla entero y la '
                              'izquierda ya está tocando; cuéntalo, no lo saltes',
                          events=[REM, REM, ac(('D3', 'F3', 'A3'), 'q')] +
                                 corch(['D4', 'D4']) +
                                 [ac(('D3', 'F3', 'A3', 'F4'), 'e'), n('F4', 'e')] +
                                 corch(['A4', 'A4']),
                          bars=2, manos='sostiene', key_sig='Re menor'),
                     dict(cap='b) y los cc. 2 y 3, con el cambio de acorde dentro · el Sol largo '
                              'va aquí en dos blancas, y en tu partitura es una redonda',
                          events=[ac(('D3', 'F3', 'A3'), 'q')] + corch(['D4', 'D4']) +
                                 [ac(('D3', 'F3', 'A3', 'F4'), 'e'), n('F4', 'e')] +
                                 corch(['A4', 'A4']) +
                                 [ac(('C3', 'E3', 'G3', 'G4'), 'h'), ac(('C3', 'E3', 'G3'), 'h')],
                          bars=2, manos='sostiene', show_time=False, key_sig='Re menor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Los cuatro primeros compases con las dos manos, contando el compás de '
                       'silencio del principio en voz alta. Tu edición no dice a qué velocidad hay '
                       'que tocarla: empieza a la que te salgan los acordes sin mirarte la mano, y '
                       'apunta a lápiz el número que te sale para que lo veamos en clase.'),
        ] + bloques_extra('Re menor', 107, 'D4', 'D3',
                          'los acordes de tres notas de la izquierda, colocados de una vez',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Sound of Silence · para casa',
            intro='Quince minutos al día, y los cinco primeros con la izquierda sola. Esta semana '
                  'la mano izquierda es la que manda.',
            bloques=[
                reto('Poner los tres dedos del acorde a la vez y sin mirar la mano.',
                     'Colócalos en silencio, levanta la mano un palmo y vuelve a bajarla. Diez '
                     'veces seguidas sin fallo y con los ojos en la partitura, no en el teclado.'),
                plan((5, 'Los dos acordes con la izquierda sola, colocando sin mirar'),
                     (4, 'El cambio de Re menor a Do mayor, mano entera'),
                     (3, 'La derecha sola, los cc. 2 y 4'),
                     (3, 'Los cc. 1 a 4 con las dos manos, contando el silencio')),
                objetivo('Que el acorde de la izquierda caiga entero y a la vez, sin que se oiga una '
                         'nota antes que las otras. Si suena desigual, es que estás buscando las '
                         'teclas de una en una.'),
                teclado({1: 1, 3: 2, 5: 3},
                        ['Escribe el nombre de las tres teclas marcadas.',
                         '¿Qué acorde forman las tres, y en qué compases lo tocas?'],
                        titulo='En el teclado',
                        pista='son las tres notas que tu izquierda toca en los cc. 1 y 2'),
                ordenar(['Colocar el acorde de Re menor con la izquierda, en silencio.',
                         'Tocarlo dos veces por compás, contando cuatro.',
                         'Cambiar a Do mayor moviendo la mano entera.',
                         'Añadir la derecha del c. 2, contando el silencio de negra.',
                         'Los cuatro compases seguidos con las dos manos.'],
                        titulo='Pon los pasos en el orden en que hay que hacerlos',
                        pista='escribe 1, 2, 3… en las casillas'),
                figuras([('w', 'redonda'), ('h', 'blanca'), ('q', 'negra'), ('e', 'corchea')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='y di cuál de las cuatro llena ella sola un compás de 4/4'),
                para_clase('Los cuatro primeros compases con las dos manos, a la velocidad que te '
                           'salgan los acordes sin mirarte la mano. Y tráeme apuntado ese número: '
                           'la velocidad de la pieza la decidimos a partir de ahí.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
