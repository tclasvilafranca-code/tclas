# -*- coding: utf-8 -*-
"""Titanic, de James Horner — pieza 10 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Ana Cristina
   Escobés, 1 página), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - **2/4**. Es el primer compás de dos de todo el cuaderno de Luisa.
     - Arriba pone "Adagio" y "mp". No trae número de metrónomo.
     - La derecha empieza con corchea con puntillo · semicorchea y sigue con
       corcheas. La izquierda hace UNA BLANCA por compás, que en 2/4 es el
       compás entero.
     - Hay barras de repetición y casillas de primera y segunda vez.

   Aviso sobre el andamio: el motor del cuaderno no escribe semicorcheas. El
   largo-corto de la partitura vive DENTRO de un tiempo; en las hojas se
   escribe un tamaño mayor (negra con puntillo y corchea, que ocupa el compás)
   y se dice en el propio pie. Es el mismo gesto contado más despacio, no otro
   ritmo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import sistemas_extra
from lu_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=10, nivel='iniciación', slug='Titanic',
    formato='adulto',
    titulo_corto='Titanic', time_sig=(2, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source', 'Titanic easy.pdf'),
    yt='https://www.youtube.com/results?search_query=my+heart+will+go+on+easy+piano',

    ficha=dict(
        titulo='Titanic',
        autor='James Horner · arr. Ana Cristina Escobés',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '2/4'),
               ('Carácter', 'Adagio · despacio'), ('Izquierda', 'Una por compás'),
               ('Trae', '1ª y 2ª vez')],
        titulo_ritmos='Dos tiempos por compás',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la izquierda aguanta el compás '
                   'entero y la derecha se mueve por encima, larga y corta.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('COMPÁS DE DOS', 'Un fuerte y un flojo',
                 'Es el primero de tu cuaderno. Se cuenta uno-dos, uno-dos, y no hay tercer tiempo '
                 'donde descansar. Va más rápido de contar y más lento de tocar.'),
                ('ADAGIO', 'Sin prisa ninguna',
                 'No trae número de metrónomo, trae una palabra: despacio. Aquí eso es una ventaja, '
                 'porque el largo-corto se oye mejor cuanto más lento vas.'),
                ('LARGO Y CORTO', 'En un solo golpe',
                 'La primera nota dura y la segunda entra justo antes del siguiente golpe. No son '
                 'dos notas iguales: si suenan iguales, la melodía no se reconoce.'),
                ('PRIMERA Y SEGUNDA VEZ', 'Dos finales',
                 'Al final hay dos casillas numeradas. La primera vez se toca la del 1 y se vuelve; '
                 'la segunda vez se salta esa y se toca la del 2.'),
            ],
            pie='La izquierda hace una sola nota por compás y la aguanta entera. Es la mano fácil '
                'de toda la pieza, y por eso puedes dedicar la cabeza a la derecha.',
        ),
        ritmos=[
            ('MANO DERECHA', 'larga y corta · andamio, un tamaño mayor',
             [n('E4', 'q.'), n('E4', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una nota, el compás entero · literal',
             [n('C3', 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 2/4: solo dos tiempos, uno fuerte y uno flojo.',
            'Arriba pone "Adagio" y "mp": despacio y con poco volumen.',
            'La izquierda hace una blanca por compás, que en 2/4 llena el compás entero.',
            'La derecha empieza con una nota larga y una corta pegada a la siguiente.',
            'Al final hay casillas de primera y segunda vez.',
        ],
        reto='Que el compás de dos no se convierta en uno de cuatro. Es fácil juntar dos compases '
             'sin querer y perder el uno; entonces la melodía se queda sin apoyo.',
        truco='Di "UN, dos" en voz alta marcando siempre el UN, y toca solo la izquierda: una nota '
              'en cada UN y nada más. Cuando lleves ocho compases sin dudar, pon la derecha encima.',
        sabias='James Horner escribió el tema antes de que la película lo pidiera: al director no '
               'le convencía tener una canción. Se grabó una maqueta a escondidas y así entró en '
               'la película.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta "un, dos" con la grabación. Vas a notar que el uno cae siempre en la '
                      'nota larga; ese es el sitio al que agarrarse.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Compás nuevo, así que el trabajo empieza por contar. Primero el pulso de dos, luego '
              'el largo-corto y solo al final las dos manos.',
        reglas=['CUENTA "UN, DOS" EN VOZ ALTA SIEMPRE', 'LA IZQUIERDA AGUANTA EL COMPÁS ENTERO',
                'DESPACIO: ES UN ADAGIO'],
        bloques=[
            dict(num=1, titulo='El pulso de dos, con las dos manos por separado',
                 pista='andamio en Do mayor · dos negras por compás, nada más',
                 sistemas=[
                     dict(cap='a) la derecha, dos notas por compás · marca el uno un poco más fuerte',
                          events=[n('E4'), n('E4'), n('G4'), n('G4'),
                                  n('F4'), n('E4'), n('D4'), n('D4')],
                          matiz='mp',
                          bars=4),
                     dict(cap='b) y la izquierda, una sola nota que ocupa el compás entero',
                          events=[n('C3', 'h'), n('G2', 'h'), n('A2', 'h'), n('F2', 'h')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='Largo y corto',
                 pista='andamio · escrito un tamaño mayor que en la partitura, para poder contarlo',
                 sistemas=[
                     dict(cap='a) la larga ocupa golpe y medio y la corta entra justo antes del '
                              'compás siguiente · cuenta "UUUN y"',
                          events=[n('E4', 'q.'), n('F4', 'e'), n('G4', 'q.'), n('F4', 'e')],
                          bars=2),
                     dict(cap='b) y ahora con las dos corcheas seguidas que vienen después · aquí '
                              'las dos duran lo mismo',
                          events=corch(['G4', 'F4']) + [n('E4')] + corch(['D4', 'E4']) + [n('C4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL ANDAMIO ESTÁ ESCRITO MÁS GRANDE',
                 texto='En tu partitura el largo-corto pasa dentro de un solo golpe, y a esa '
                       'velocidad casi no se puede contar. Aquí está escrito el doble de grande: el '
                       'mismo gesto, pero ocupando el compás entero. Cuando lo tengas en el cuerpo, '
                       've a la partitura y hazlo igual pero en la mitad de tiempo. Es el mismo '
                       'ritmo, no otro.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda toca en el uno y ya no se mueve · muy despacio',
                 sistemas=[
                     dict(cap='a) las dos caen en el uno; en el dos solo se mueve la derecha',
                          events=[ac(('C3', 'E4')), n('F4'), ac(('G2', 'G4')), n('F4')],
                          bars=2),
                     dict(cap='b) y con el largo-corto encima · la izquierda no se entera de nada, '
                              'ella aguanta',
                          events=[ac(('A2', 'E4'), 'q.'), n('D4', 'e'),
                                  ac(('F2', 'C4'), 'q.'), n('D4', 'e')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('Do mayor', 'C4', 'F2', time_sig=(2, 4), variante=30,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
