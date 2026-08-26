# -*- coding: utf-8 -*-
"""I Have a Dream — pieza 11 de Eduard. Formato ADULTO.

   Medido sobre el PDF de su carpeta (vectorial, dos pentagramas por sistema):

     - 4/4 y detras de la clave no hay nada.
     - Arriba, impreso en la propia partitura: **TEMPO 120**. Es la primera
       pieza del cuaderno que trae numero de metronomo escrito, asi que la
       casilla de la ficha se llama "Tempo" y no "Caracter".
     - Debajo del pentagrama de arriba va la **letra**, silaba a silaba.
     - La melodia del principio, medida a 300 ppp:

         c. 1   (silencio de negra) La3 · Mi4 · Re4
                negra, negra con puntillo y corchea      ["I have a"]
         c. 2   Fa4                                      redonda   ["dream,"]
         c. 3   (silencio de negra) Fa3 · Do4 · Si3      lo mismo, mas grave

     - La izquierda, medida:

         c. 1   Do3                    redonda
         c. 2   Sol3 y Do4 juntas      redonda de dos notas
         c. 3   un acorde y despues silencios

   DOS COSAS QUE HUBO QUE MIRAR AMPLIADAS. La primera nota de la derecha
   cuelga de DOS lineas adicionales (La3) y el lector se la come, porque esta
   pegada a la cifra de compas: la lectura buena esta anotada en
   `auditar_alturas.MIRADAS`. Y las dos redondas del c. 2 de la izquierda estan
   tan juntas que el lector las promedia en una sola; ampliadas se ve que la de
   arriba esta ATRAVESADA por su linea adicional —o sea, el do central— y la de
   abajo se apoya en la linea de arriba del pentagrama de fa, que es el Sol3.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, sil, plan, objetivo, diferencias, figuras,
                      rodear, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los compases 1 y 2 de la DERECHA, medidos. Cita literal.
ARRANQUE = [sil('q'), n('A3'), n('E4', 'q.'), n('D4', 'e'), n('F4', 'w')]

# Los compases 1 y 2 de la IZQUIERDA, medidos.
BAJO = [n('C3', 'w'), ac(('G3', 'C4'), 'w')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=11, nivel='iniciación',
    slug='IHaveADream', formato='adulto',
    titulo_corto='I Have a Dream', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'I Have a Dream.pdf'),
    yt='https://www.youtube.com/results?search_query=abba+i+have+a+dream+piano+easy',

    ficha=dict(
        titulo='I Have a Dream',
        autor='ABBA · Benny Andersson y Björn Ulvaeus · arreglo fácil',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '120'), ('Manos', 'Las dos, distintas'),
               ('Extras', 'Lleva letra')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura. Arriba, los compases 1 y 2 de la derecha, con su '
                   'silencio de entrada. Abajo, la izquierda de esos mismos dos compases.',
        armonia=dict(
            titulo='La derecha canta y la izquierda sostiene',
            tarjetas=[
                ('EL TEMPO', '120',
                 'Aquí sí viene escrito el número: 120 golpes por minuto, dos por segundo. Es la '
                 'primera pieza de tu cuaderno que lo dice.'),
                ('LA ENTRADA', 'En el dos',
                 'El primer tiempo es un silencio de negra. La voz entra en el segundo golpe, y ese '
                 'retraso es justo lo que le da el aire a la canción.'),
                ('NOTAS LARGAS ABAJO', 'Redondas',
                 'La izquierda hace una nota por compás, que dura los cuatro tiempos. En el compás '
                 '2 son dos notas a la vez.'),
                ('LA LETRA', 'Debajo',
                 'Cada sílaba va bajo su nota. "I have a dream" son cuatro sílabas y cuatro notas: '
                 'cantarla mientras tocas resuelve el ritmo solo.'),
            ],
            pie='Fíjate en la forma de la frase: tres notas cortas que suben y una larga que se '
                'queda. Eso se repite toda la canción con distintas alturas, así que aprender el '
                'dibujo vale más que aprender las notas.',
        ),
        ritmos=[
            ('LA DERECHA', 'cc. 1 y 2, medidos · entra en el segundo tiempo',
             ARRANQUE, OCRE, 'treble', None),
            ('LA IZQUIERDA', 'cc. 1 y 2, medidos · una nota por compás',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Compás de 4/4, y no hay ni un sostenido ni un bemol.',
            'Arriba pone TEMPO 120: es el número de metrónomo.',
            'El primer tiempo del compás 1 es un silencio de negra.',
            'La izquierda hace redondas: una nota que dura el compás.',
            'En el compás 2 la izquierda toca dos notas a la vez.',
            'Debajo del pentagrama va la letra de la canción.',
        ],
        reto='La negra con puntillo. Es una nota que dura tiempo y medio, y el medio que sobra hace '
             'que la nota siguiente caiga a destiempo. Si la cuentas mal, la frase se descoloca.',
        truco='Cuenta en corcheas: "un-y-dos-y-tres-y-cua-tro". La negra con puntillo ocupa tres de '
              'esas ocho partes, y la corchea que va detrás ocupa una. Dicho así deja de tener '
              'misterio.',
        sabias='ABBA grabó esta canción en 1979 con un coro de niños de un colegio de Estocolmo. '
               'Björn escribió la letra pensando en que la canción tenía que poder cantarla '
               'cualquiera, y por eso la melodía se mueve tan poco.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuatro golpes desde el principio y verás que la voz no entra en el '
                      'uno, sino en el dos.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo de esta semana es una figura: la negra con puntillo. Se trabaja aparte, '
              'contando en corcheas, y después se mete en la frase.',
        reglas=['CUENTA EN CORCHEAS: UN-Y-DOS-Y', 'LA IZQUIERDA AGUANTA LOS CUATRO TIEMPOS',
                'DI LA LETRA MIENTRAS TOCAS'],
        bloques=[
            dict(num=1, titulo='La negra con puntillo, sola',
                 pista='andamio en Do mayor · tiempo y medio, y la corchea detrás',
                 sistemas=[
                     dict(cap='a) primero en negras, para tener el sitio de los golpes',
                          events=[n('G4'), n('F4'), n('E4'), n('D4')],
                          bars=1),
                     dict(cap='b) y ahora con puntillo: la primera dura una y media',
                          events=[n('G4', 'q.'), n('F4', 'e'), n('E4', 'h'),
                                  n('F4', 'q.'), n('G4', 'e'), n('F4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ HACE EL PUNTILLO',
                 texto='Un puntillo detrás de una nota le añade la mitad de lo que ya dura. Una '
                       'negra vale un tiempo; con puntillo vale uno y medio. Eso significa que la '
                       'nota siguiente no cae en un golpe, sino justo en el medio, y ahí es donde '
                       'se pierde todo el mundo. La solución no es tocar más despacio: es contar '
                       'las mitades en voz alta.'),
            dict(num=2, titulo='La frase del principio, tal y como está escrita',
                 pista='cc. 1–2 · medidos en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) las tres notas de "I have a", sin el silencio ni la larga',
                          events=[n('A3'), n('E4', 'q.'), n('D4', 'e'), sil('q')],
                          bars=1),
                     dict(cap='b) y la frase entera dos veces, con su silencio delante y su redonda detrás',
                          events=[sil('q'), n('A3'), n('E4', 'q.'), n('D4', 'e'), n('F4', 'w'),
                                  sil('q'), n('A3'), n('E4', 'q.'), n('D4', 'e'), n('F4', 'w')],
                          bars=4, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda, y las dos manos',
                 pista='cc. 1–2 · medidos · abajo no hay nada que correr',
                 sistemas=[
                     dict(cap='a) la izquierda, partida en mitades para colocar la mano · en tu '
                              'partitura cada una es una nota larga',
                          events=[n('C3', 'h'), n('C3', 'h'),
                                  ac(('G3', 'C4'), 'h'), ac(('G3', 'C4'), 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) y las dos manos, con la izquierda sosteniendo debajo',
                          events=[ac(('C3',), 'q'), ac(('A3',)), ac(('E4',), 'q.'),
                                  ac(('D4',), 'e'), ac(('G3', 'C4', 'F4'), 'w')],
                          bars=2, manos='sostiene', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='I Have a Dream · para casa',
            intro='Quince minutos al día. Toda la semana gira alrededor de una figura: la negra con '
                  'puntillo. Cuando la tengas, la canción entera se abre.',
            bloques=[
                plan((4, 'Contar "un-y-dos-y-tres-y-cua-tro" con el pie, sin tocar'),
                     (4, 'La negra con puntillo y su corchea, en dos teclas'),
                     (4, 'La frase del compás 1, con su silencio de entrada'),
                     (3, 'Los dos primeros compases con las dos manos')),
                objetivo('Que la corchea de después del puntillo caiga en su sitio. Si suena '
                         'pegada a la nota siguiente, es que la larga se ha quedado corta.'),
                diferencias([n('A3'), n('E4', 'q.'), n('D4', 'e'), n('F4', 'w')],
                            [n('A3'), n('E4', 'h'), n('D4', 'e'), n('F4', 'w')],
                            cuantas=1,
                            titulo='Busca la diferencia',
                            pista='arriba, tu frase medida · abajo, con una figura cambiada'),
                figuras([('q.', 'negra con puntillo'), ('e', 'corchea'), ('w', 'redonda'),
                         ('q', 'negra')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='las cuatro están en tus dos primeros compases'),
                rodear([[n('A3'), n('E4', 'q.'), n('D4', 'e')],
                        [n('A3'), n('E4', 'q.'), n('D4', 'e')],
                        [n('A3'), n('D4', 'q.'), n('E4', 'e')],
                        [n('C4'), n('E4', 'q.'), n('D4', 'e')]],
                       titulo='Rodea los dos grupos que son iguales',
                       pista='uno de ellos es el compás 1 de tu partitura'),
                para_clase('Los dos primeros compases con las dos manos, y el ritmo del puntillo '
                           'contado en voz alta. Si no te sale, tráelo sin arreglar: se arregla '
                           'mejor entre los dos.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 71, 'E4', 'C3',
    'la negra con puntillo, que descoloca la nota de detrás',
    desde=4, time_sig=(4, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
