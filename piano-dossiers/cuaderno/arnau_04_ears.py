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

    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Do Your Ears Hang Low? · para hacer en casa',
            intro='Esta semana toca aprenderse los silencios y practicar el contar. Todo lo de aquí '
                  'está en tu partitura.',
            bloques=[
                dict(tipo='nombres', num=1,
                     titulo='¿Cómo se llama cada nota?',
                     pista='escríbelas en la cajita de debajo',
                     notas=['E4', 'D4', 'C4', 'F4', 'G4', 'E4', 'A4', 'C5']),
                dict(tipo='figuras', num=2,
                     titulo='¿Cuántos golpes dura cada una?',
                     pista='escribe el número en la caja',
                     figuras=[('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'),
                              ('h.', 'blanca con puntito')]),
                dict(tipo='colorea', num=3,
                     titulo='Rodea los huecos',
                     pista='busca en tu partitura y rodea todos los silencios que encuentres',
                     eventos=[n('C4'), n('D4'), n('E4'), n('D4'),
                              n('C4'), n('E4'), n('G4'), n('E4')],
                     leyenda=['Un silencio dura lo mismo que una nota, pero no suena.',
                              'Cuéntalo igual: un-dos-tres-cuatro, sin parar.']),
                dict(tipo='rutina',
                     titulo='Lo que hay que tocar cada día',
                     pista='pon una cruz cuando lo hagas · cinco minutos bastan',
                     tareas=['La melodía del principio, contando en voz alta',
                             'Toca-hueco-toca-hueco, ocho veces seguidas',
                             'La izquierda sola, muy despacio']),
                dict(tipo='une', num=4,
                     titulo='Une cada figura con lo que dura',
                     pista='una raya de un punto al otro',
                     pares=[('Redonda', 'un golpe'),
                            ('Blanca', 'cuatro golpes'),
                            ('Negra', 'dos golpes')]),
                dict(tipo='escucha',
                     titulo='UN JUEGO, CON ALGUIEN DE CASA',
                     pista='no hace falta que sepa música',
                     texto='Quien esté contigo cuenta en voz alta un-dos-tres-cuatro sin parar, y tú '
                           'tocas SOLO en el uno y en el tres. Luego al revés: solo en el dos y en el '
                           'cuatro, que es mucho más difícil. Cinco veces cada uno.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Do Your Ears Hang Low? · para hacer en casa',
            intro='Ahora que los huecos ya no te pillan, esta semana toca mirar la partitura con un '
                  'lápiz y juntar las dos manos.',
            bloques=[
                dict(tipo='rodea', num=1,
                     titulo='Rodea los dos compases que son iguales',
                     pista='fíjate en las notas de una en una',
                     compases=[[n('E4'), n('D4'), n('C4'), n('C4')],
                               [n('C4'), n('D4'), n('E4'), n('E4')],
                               [n('E4'), n('D4'), n('C4'), n('C4')],
                               [n('G4'), n('E4'), n('C4'), n('C4')]]),
                dict(tipo='dibuja', num=2,
                     titulo='Dibuja tú las notas',
                     pista='solo el óvalo, sin el palito',
                     nombres=['Mi', 'Re', 'Do', 'Fa', 'Sol', 'Do', 'La', 'Mi']),
                dict(tipo='nota',
                     etiqueta='ACUÉRDATE',
                     texto='Los números que hay encima de las notas no son la nota: son el DEDO con el '
                           'que hay que tocarla. El 1 es el pulgar y el 5 es el meñique. Si los usas, '
                           'la mano llega sola a la siguiente nota y no tienes que mirarte los dedos.'),
                dict(tipo='rutina',
                     titulo='Lo que hay que tocar cada día',
                     pista='pon una cruz cuando lo hagas',
                     tareas=['Los cuatro primeros compases con las dos manos',
                             'La canción entera con la derecha sola',
                             'Contar en voz alta mientras tocas, sin parar en los fallos']),
                dict(tipo='nombres', num=3,
                     titulo='Otra vez los nombres, a ver si ya te los sabes',
                     pista='sin mirar los deberes de la semana pasada',
                     notas=['G4', 'E4', 'C5', 'A4', 'F4', 'D4', 'B4', 'E4']),
                dict(tipo='escucha',
                     titulo='UN JUEGO, CON ALGUIEN DE CASA',
                     pista='esta vez de huecos',
                     texto='Toca cuatro golpes seguidos, pero deja UNO sin tocar, el que tú quieras. '
                           'Quien esté contigo tiene que decir cuál faltaba: el uno, el dos, el tres o '
                           'el cuatro. Cinco veces cada uno.'),
                dict(tipo='escribe', num=4,
                     titulo='Copia aquí el compás que más te cueste',
                     pista='cópialo tal cual y luego tócalo cinco veces',
                     lineas=1),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
