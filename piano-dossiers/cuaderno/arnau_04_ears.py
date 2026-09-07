# -*- coding: utf-8 -*-
"""Do Your Ears Hang Low? (canción 4 de Arnau, iniciación). Formato CORTO.

   Lo medido sobre el PDF de su carpeta de Drive (arr. Gilbert DeBenedetti,
   "Level One", 1 página):

     - Do mayor (nada detrás de la clave) y compás de 4/4. Pone "Silly!".
     - Aquí SE MUEVEN LAS DOS MANOS: es la primera del cuaderno en la que la
       izquierda no se queda quieta.
     - La melodía empieza bajando: Mi · Re · Do · Do · Do.
     - Hay SILENCIOS en las dos manos, y notas cortas de dos en dos.
     - La digitación viene impresa en varios sitios (1 2 1 3 1 · 1 3 2 ...).

   Lo que NO se cita compás a compás: la izquierda se mueve mucho y el lector
   no separa bien los compases en esta edición, así que sus ejercicios van
   rotulados como ANDAMIO en Do mayor y remiten a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (rutina, juego, acuerdate, crucigrama, palmas, figuras,
                         teclado, adivinar, rodear, contar)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
_B = [4300]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def sil(d='q'):
    return {'rest': True, 'dur': d}


def corch(ps, agrupar=2):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


CANCION = dict(
    alumno='Arnau', num=4, nivel='iniciación', slug='DoYourEars',
    formato='corto',
    titulo_corto='Do Your Ears Hang Low?', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Do Your Ears Hang Low?.pdf'),
    yt='https://www.youtube.com/results?search_query=do+your+ears+hang+low+piano',

    ficha=dict(
        titulo='Do Your Ears Hang Low?',
        autor='Canción popular · arreglo de Gilbert DeBenedetti',
        datos=[('Teclas', 'Solo blancas'), ('Golpes', '4 por compás'),
               ('Las dos manos', 'Se mueven'), ('Novedad', 'Silencios'),
               ('Carácter', 'Silly!')],
        armonia=dict(
            titulo='La primera en la que se mueven las dos manos',
            tarjetas=[
                ('LO NUEVO', 'Las dos manos',
                 'Hasta ahora una se quedaba quieta. Aquí las dos tocan y las dos cambian.'),
                ('LOS SILENCIOS', 'Ratos sin tocar',
                 'Aparecen unos dibujos que quieren decir “aquí no toques”. El tiempo sigue.'),
                ('LA MELODÍA', 'Empieza bajando',
                 'Mi · Re · Do, y después se queda repitiendo el Do tres veces.'),
                ('LOS DEDOS', 'Vienen escritos',
                 'Los números de encima de las notas te dicen con qué dedo tocarlas. Úsalos.'),
            ],
            pie='Esta canción no tiene notas difíciles: lo que tiene son huecos. Y los huecos hay que '
                'contarlos igual que las notas, porque si te los saltas llegas antes de tiempo y ya no '
                'encaja nada de lo que viene después.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='Los dos primeros compases de la mano derecha, medidos en tu partitura.',
        ritmos=[
            ('LA DERECHA', 'baja tres escalones y se queda quieta en el Do',
             [n('E4'), n('D4'), n('C4'), n('C4')], AZUL, 'treble', None),
            ('Y UN SILENCIO', 'un golpe sin tocar, contándolo igual',
             [n('C4'), sil('q'), n('C4'), n('C4')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'Las DOS manos se mueven: es la primera del cuaderno en la que pasa.',
            'Hay silencios: ratos en los que no se toca pero se sigue contando.',
            'Hay notas cortas de dos en dos, unidas por una barra.',
            'Los números de encima de las notas son los dedos.',
        ],
        reto='Los silencios. Un hueco dura exactamente lo mismo que una nota, pero como no suena nada '
             'es facilísimo pasar de largo. Y si entras antes de tiempo una sola vez, todo lo que viene '
             'detrás va corrido.',
        truco='Cuando llegues a un silencio, no dejes de contar: di el número en voz alta y más fuerte '
              'que los demás. También puedes dar una palmada muy floja en el aire, sin tocar el piano. '
              'Lo importante es que el hueco tenga la misma duración siempre.',
        sabias='Esta canción se canta en los campamentos de medio mundo y tiene versos cada vez más '
               'tontos, por eso el arreglo pone «Silly!» arriba: está pensada para reírse mientras se '
               'canta, no para tocarla muy seria.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuatro golpes con el pie y busca dónde están los huecos.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende',
        esquina='Al piano · tres pasos',
        intro='Lo nuevo aquí son los silencios y que las dos manos se muevan. Así que primero se '
              'aprende a contar los huecos sin tocar nada, y después se ponen las notas.',
        reglas=['UN SILENCIO SE CUENTA IGUAL', 'CUENTA HASTA CUATRO EN VOZ ALTA',
                'PRIMERO CADA MANO POR SU LADO'],
        bloques=[
            dict(num=1, titulo='La melodía del principio',
                 pista='medida en tu partitura · baja tres escalones y luego repite el Do',
                 sistemas=[
                     dict(cap='a) Mi · Re · Do · Do · muy despacio, contando los cuatro golpes',
                          events=[n('E4'), n('D4'), n('C4'), n('C4'),
                                  n('C4'), n('D4'), n('E4'), n('E4')],
                          bars=2),
                     dict(cap='b) y ahora con notas cortas de dos en dos, que es como está escrito',
                          events=corch(['E4', 'D4']) + [n('C4'), n('C4'), n('C4')] +
                                 corch(['C4', 'D4']) + [n('E4'), n('E4'), n('E4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Los huecos: aquí no se toca',
                 pista='el silencio dura lo mismo que una nota · cuenta el número en voz alta y más fuerte',
                 sistemas=[
                     dict(cap='a) toca, hueco, toca, hueco · el hueco no es un descanso: es parte de la '
                              'canción',
                          events=[n('C4'), sil('q'), n('C4'), sil('q'),
                                  n('E4'), sil('q'), n('E4'), sil('q')],
                          bars=2),
                     dict(cap='b) y ahora el hueco cambia de sitio · fíjate en que sigue durando igual',
                          events=[n('C4'), n('D4'), sil('q'), n('E4'),
                                  sil('q'), n('E4'), n('D4'), n('C4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LOS HUECOS SE CUENTAN',
                 texto='Cuando no suena nada parece que el tiempo se para, y no se para: sigue '
                       'corriendo igual. Si te saltas un hueco, entras antes de tiempo y a partir de '
                       'ahí todo va corrido, aunque las notas sean las correctas. Por eso en esta '
                       'canción se cuenta EN VOZ ALTA hasta que salga sin pensar.'),
            dict(num=3, titulo='La izquierda, que aquí también se mueve', clef='bass',
                 pista='andamio en Do mayor: el dibujo es el de tu partitura, las notas exactas míralas allí',
                 sistemas=[
                     dict(cap='a) tres notas que suben y vuelven · una por golpe, sin correr',
                          events=[n('C3'), n('E3'), n('G3'), n('E3'),
                                  n('C3'), n('E3'), n('G3'), n('E3')],
                          bars=2, clef='bass'),
                     dict(cap='b) y con huecos también · la izquierda calla en los mismos sitios que '
                              'la derecha, así que se cuenta una sola vez para las dos',
                          events=[n('C3'), sil('q'), n('G3'), sil('q'),
                                  n('C3'), sil('q'), n('G3'), sil('q')],
                          bars=2, clef='bass', show_time=False),
                 ]),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R7 (crucigrama · palmas ·
    # figuras) y semana 2 la R8 (teclado · adivina · rodea · cuenta).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Do Your Ears Hang Low? · para hacer en casa',
            intro='La novedad son los huecos: ratos en los que no tocas nada y el tiempo sigue.',
            bloques=[
                crucigrama('PAUSA', [
                    ('COMPAS', 3, 'El trozo que hay entre dos rayas de arriba abajo.'),
                    ('NEGRA', 4, 'La figura que dura un golpe.'),
                    ('CUATRO', 1, 'Los golpes que hay en cada compás de esta canción.'),
                    ('MANOS', 4, 'En esta canción, por fin, se mueven las dos.'),
                    ('CORTAS', 4, 'Las notas que van de dos en dos, unidas por una barra.'),
                ], cierre='Las casillas grises dicen lo que hay en los huecos donde no se toca.'),
                palmas([('SI-LEN-CIO', 3), ('O-RE-JAS', 3)],
                       titulo='El ritmo de las palabras',
                       pista='dilo en voz alta y escríbelo con figuras en la caja'),
                figuras([('q', 'negra'), ('e', 'corchea'), ('h', 'blanca'),
                         ('w', 'redonda')],
                        titulo='¿Cuántos golpes dura cada una?',
                        pista='la corchea es la mitad de una negra'),
                acuerdate('Cuando no suena nada parece que el tiempo se para, y no se para: sigue '
                          'corriendo igual. Si te saltas un hueco entras antes de tiempo, y a '
                          'partir de ahí todo va corrido aunque las notas sean las buenas. Cuenta '
                          'los huecos en voz alta y más fuerte que las notas.',
                          etiqueta='POR QUÉ LOS HUECOS SE CUENTAN'),
                rutina('Mi · Re · Do · Do, contando los cuatro golpes',
                       'Toca-hueco-toca-hueco, sin acelerar en el hueco',
                       'Las dos manos, los dos primeros compases'),
                juego('Quien esté contigo da palmadas y de vez en cuando se salta una a propósito. '
                      'Tú tienes que decir en qué golpe estaba el hueco. Diez veces.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Do Your Ears Hang Low? · para hacer en casa',
            intro='Esta semana se empieza en el teclado y se acaba contando. Ten la partitura al '
                  'lado, que hace falta para el ejercicio de rodear.',
            bloques=[
                teclado({0: 1, 1: 2, 2: 3, 4: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'La 1, la 2 y la 3 son las tres primeras notas de tu melodía, al revés.'],
                        titulo='En el teclado',
                        pista='las cuatro marcadas son de esta canción'),
                adivinar([('No sueno, pero ocupo mi sitio y hay que contarme.', 'SILENCIO'),
                          ('Vamos de dos en dos, unidas por una barra de arriba.', 'CORCHEAS'),
                          ('En esta canción, por primera vez, nos movemos las dos.', 'MANOS')],
                         titulo='Adivina quién soy',
                         pista='una letra en cada casilla'),
                rodear([[n('C4'), n('D4'), n('E4'), n('E4')],
                        [n('E4'), n('D4'), n('C4'), n('C4')],
                        [n('C4'), n('D4'), n('E4'), n('E4')],
                        [n('E4'), n('E4'), n('D4'), n('C4')]],
                       titulo='Rodea los dos compases que son iguales',
                       pista='cuatro notas en cada compás · míralas de una en una'),
                contar([n('E4'), n('D4'), n('C4'), n('C4'), n('C4'), n('D4'), n('E4'), n('E4')],
                       ['¿Cuántos Do hay?', '¿Cuántos Mi hay?',
                        '¿Cuántas notas hay en total?'],
                       titulo='Cuenta lo que ves',
                       pista='es el principio de tu melodía, medido en tu partitura'),
                rutina('La melodía entera con la derecha sola',
                       'Los compases con hueco, contando en voz alta',
                       'Las dos manos, cuatro compases sin parar'),
                juego('Tú tocas la melodía y quien esté contigo lleva el pulso con palmadas. Si te '
                      'saltas un hueco, se nota enseguida: la palmada y tu nota dejan de ir juntas.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
