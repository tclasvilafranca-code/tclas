# -*- coding: utf-8 -*-
"""Clementine / Found a Peanut (canción 2 de Arnau, iniciación). Formato CORTO.

   Lo medido sobre el PDF de su carpeta de Drive (arr. Gilbert DeBenedetti,
   "Primer Level", 1 página):

     - Do mayor (no hay ni un sostenido ni un bemol detrás de la clave) y
       compás de 3/4.
     - La mano derecha lleva TODA la melodía; la izquierda solo toca alguna
       nota larga suelta, y hay compases enteros en los que no toca nada.
     - La digitación viene impresa: 1 sobre el Do y 3 sobre el Mi.
     - Las alturas de la primera frase, medidas dos veces (con el lector de
       partituras y midiendo pixel a pixel la distancia de cada cabeza a la
       linea de abajo del pentagrama, que dio -1,99 y 0,00 espacios exactos):
       Do · Do | Do · Mi · Mi | Mi · Do · Do · Mi | Re · Mi | Fa · Fa · Mi · Re
     - La pieza empieza con dos corcheas ANTES del primer compás completo.

   Es la segunda del cuaderno porque es la primera melodía de verdad: en la 1
   las dos manos hacían lo mismo, y aquí la derecha ya va sola.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
_B = [4100]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def corch(ps, agrupar=2):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


# la primera frase, medida: dos corcheas de entrada y despues los compases
FRASE = (corch(['C4', 'C4']) +
         [n('C4')] + corch(['E4', 'E4']) +
         [n('E4'), n('C4')] + corch(['C4', 'E4']))

CANCION = dict(
    alumno='Arnau', num=2, nivel='iniciación', slug='Clementine',
    formato='corto',
    titulo_corto='Clementine', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Clementine.pdf'),
    yt='https://www.youtube.com/results?search_query=oh+my+darling+clementine+piano',

    ficha=dict(
        titulo='Clementine',
        autor='Canción popular · arreglo de Gilbert DeBenedetti · «Found a Peanut»',
        datos=[('Teclas', 'Solo blancas'), ('Golpes', '3 por compás'),
               ('Mano dcha.', 'La melodía'), ('Mano izq.', 'Casi nada'),
               ('Dedos', '1 y 3')],
        armonia=dict(
            titulo='Aquí la derecha va sola',
            tarjetas=[
                ('LA DERECHA', 'Toda la canción',
                 'Ella lleva la melodía de principio a fin. Es la mano que se oye.'),
                ('LA IZQUIERDA', 'Casi nada',
                 'Solo alguna nota muy larga de vez en cuando. Hay compases en los que no toca.'),
                ('DOS DEDOS', '1 y 3',
                 'Vienen escritos en la partitura: el 1 (el pulgar) en el Do y el 3 en el Mi.'),
                ('LA ENTRADA', 'Dos corcheas',
                 'La canción empieza ANTES del primer compás, con dos notas cortas de carrerilla.'),
            ],
            pie='Esta es la primera canción del cuaderno en la que cada mano hace una cosa distinta. '
                'Como la izquierda casi no toca, puedes dedicarle toda la cabeza a la derecha, que es '
                'de lo que se trata.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='Los dos primeros compases, para que veas de un vistazo por dónde va la melodía. '
                   'Las notas con la barra arriba son las cortas.',
        ritmos=[
            ('EL PRIMER COMPÁS', 'una larga y dos cortas, subiendo del Do al Mi',
             [n('C4')] + corch(['E4', 'E4']) + [n('E4')], AZUL, 'treble', None),
            ('Y EL SIGUIENTE', 'tres largas: aquí la melodía se para',
             [n('E4'), n('C4'), n('C4')], AZUL, 'treble', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva tres golpes: un-dos-tres.',
            'La canción empieza con dos notas cortas antes del primer compás.',
            'La melodía se mueve entre el Do de en medio y el Fa, muy poquito.',
            'Los números que hay encima de algunas notas son los dedos que tienes que usar.',
            'La misma frase se repite tres veces seguidas casi igual.',
        ],
        reto='Que las notas cortas suenen cortas y las largas, largas. Cuando una canción tiene notas '
             'de dos duraciones mezcladas, lo más fácil es tocarlas todas iguales sin darse cuenta, y '
             'entonces la canción deja de reconocerse.',
        truco='Canta la letra antes de tocar: «Oh my dar-ling, oh my dar-ling». Donde la letra corre, '
              'las notas son cortas; donde se para, son largas. Tu voz ya sabe el ritmo aunque tus '
              'dedos todavía no.',
        sabias='Esta melodía tiene dos letras: una habla de Clementine, la hija de un buscador de oro, '
               'y la otra dice «encontré un cacahuete». En tu partitura están escritas las dos, una '
               'debajo de otra, y puedes cantar la que más te guste.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que la canción arranca antes de tiempo, con carrerilla.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende',
        esquina='Al piano · tres pasos',
        intro='Aquí solo trabaja la derecha, así que ponla en su sitio y no la muevas: el pulgar en el '
              'Do de en medio y el dedo 3 en el Mi. Con la mano quieta, la canción entera te sale sin '
              'buscar ninguna tecla.',
        reglas=['EL PULGAR EN EL DO DE EN MEDIO', 'LA MANO NO SE MUEVE DE SITIO', 'CUENTA UN-DOS-TRES'],
        bloques=[
            dict(num=1, titulo='Coloca la mano y no la muevas',
                 pista='las dos notas de toda la primera frase: Do con el dedo 1 y Mi con el dedo 3',
                 sistemas=[
                     dict(cap='a) primero solo las dos notas, largas · una, la otra, y otra vez',
                          events=[n('C4', 'h.'), n('E4', 'h.'), n('C4', 'h.'), n('E4', 'h.')],
                          bars=4),
                     dict(cap='b) y ahora cambiando de dedo más deprisa, sin mover la mano de sitio',
                          events=[n('C4'), n('E4'), n('C4'), n('E4'), n('C4'), n('E4'),
                                  n('C4', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ NO HAY QUE MOVER LA MANO',
                 texto='Si dejas el pulgar puesto en el Do, el dedo 3 cae solo en el Mi sin que tengas '
                       'que mirar. Cada vez que levantas la mano entera para buscar una tecla pierdes el '
                       'sitio y hay que volver a empezar. Coloca una vez, bien, y luego solo se mueven '
                       'los dedos.'),
            dict(num=2, titulo='La primera frase, tal como está escrita',
                 pista='medida en tu partitura · empieza con dos notas cortas antes del primer compás',
                 sistemas=[
                     dict(cap='a) Do · Do | Do · Mi · Mi | Mi · Do · Do · Mi · las cortas van de dos '
                              'en dos, unidas por una barra',
                          events=FRASE, bars=3),
                 ]),
            dict(num=3, titulo='Y lo mismo, pero contando',
                 pista='las mismas notas en figuras largas: aquí no hay prisa, solo se cuenta',
                 sistemas=[
                     dict(cap='a) una nota por golpe · di “un, dos, tres” en voz alta mientras tocas',
                          events=[n('C4'), n('C4'), n('C4'),
                                  n('E4'), n('E4'), n('E4'),
                                  n('C4'), n('C4'), n('E4'),
                                  n('C4', 'h.')],
                          bars=4, show_time=False),
                     dict(cap='b) y ahora una larga y dos cortas en cada compás, que es como está '
                              'escrito · las dos cortas caben en un solo golpe',
                          events=([n('C4')] + corch(['E4', 'E4'])) * 2 +
                                 [n('E4')] + corch(['C4', 'C4']) + [n('C4', 'h.')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA IZQUIERDA, QUE CASI NO TOCA',
                 texto='Busca en tu partitura el pentagrama de abajo: verás que está vacío casi todo el '
                       'rato y que solo hay alguna nota muy larga suelta. Cuando llegue una, la tocas y '
                       'la dejas sonar sin volver a apretar. No hay que hacer nada más con esa mano.'),
        ],
    ),

    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Clementine · para hacer en casa',
            intro='Esta semana toca colocar bien la mano y aprender a distinguir las notas cortas de '
                  'las largas. Todo lo de aquí está en tu partitura.',
            bloques=[
                dict(tipo='nombres', num=1,
                     titulo='¿Cómo se llama cada nota?',
                     pista='son las notas de la primera frase · escríbelas en la cajita',
                     notas=['E4', 'G4', 'F4', 'E4', 'G4', 'A4', 'F4', 'G4']),
                dict(tipo='figuras', num=2,
                     titulo='¿Cuántos golpes dura cada una?',
                     pista='escribe el número en la caja · la negra dura un golpe',
                     figuras=[('q', 'negra'), ('h', 'blanca'), ('h.', 'blanca con puntito'),
                              ('w', 'redonda')]),
                dict(tipo='une', num=3,
                     titulo='Une cada dedo con su tecla',
                     pista='mira los números que hay escritos encima de las notas de tu partitura',
                     pares=[('Dedo 1 (el pulgar)', 'el Mi'),
                            ('Dedo 3 (el corazón)', 'el Do de en medio')]),
                dict(tipo='rutina',
                     titulo='Lo que hay que tocar cada día',
                     pista='pon una cruz cuando lo hagas · cinco minutos bastan',
                     tareas=['Colocar la mano: pulgar en el Do y dedo 3 en el Mi',
                             'Do y Mi alternando, veinte veces, sin mover la mano',
                             'La primera frase entera, muy despacio']),
                dict(tipo='colorea', num=4,
                     titulo='Colorea las notas cortas de un color y las largas de otro',
                     pista='las cortas van unidas de dos en dos',
                     eventos=[n('C4'), n('E4', 'h'), n('C4'), n('E4'),
                              n('F4', 'h'), n('E4'), n('D4'), n('C4', 'h')],
                     leyenda=['Las que van solas y con el óvalo pintado duran UN golpe.',
                              'Las que tienen el óvalo hueco duran DOS golpes.']),
                dict(tipo='escucha',
                     titulo='UN JUEGO, CON ALGUIEN DE CASA',
                     pista='no hace falta que sepa música',
                     texto='Toca una nota muy corta o muy larga, sin decir cuál. Quien esté contigo '
                           'tiene que adivinar si ha sido CORTA o LARGA. Cinco veces cada uno. Parece '
                           'muy fácil, pero es justo lo que hay que oír para que esta canción se '
                           'reconozca.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Clementine · para hacer en casa',
            intro='Ahora que la mano ya está colocada, esta semana toca mirar la partitura y darse '
                  'cuenta de que hay mucho menos que aprender de lo que parece.',
            bloques=[
                dict(tipo='rodea', num=1,
                     titulo='Rodea los dos compases que son iguales',
                     pista='mira las notas de uno en uno · hay dos exactamente iguales',
                     compases=[[n('C4'), n('E4'), n('E4')],
                               [n('E4'), n('C4'), n('C4')],
                               [n('C4'), n('E4'), n('E4')],
                               [n('D4'), n('E4'), n('F4')]]),
                dict(tipo='dibuja', num=2,
                     titulo='Dibuja tú las notas',
                     pista='solo el óvalo, sin el palito · debajo pone cuál va en cada sitio',
                     nombres=['Do', 'Mi', 'Do', 'Mi', 'Re', 'Fa', 'Mi', 'Do']),
                dict(tipo='nota',
                     etiqueta='ACUÉRDATE',
                     texto='Cuando dos notas cortas van unidas por una barra de arriba, las dos juntas '
                           'duran lo mismo que UNA negra. Por eso hay que decirlas más deprisa: no es '
                           'que corran, es que caben dos donde antes cabía una.'),
                dict(tipo='rutina',
                     titulo='Lo que hay que tocar cada día',
                     pista='pon una cruz cuando lo hagas',
                     tareas=['La primera frase, contando un-dos-tres en voz alta',
                             'La canción entera, aunque sea muy despacio',
                             'Cantar la letra sin tocar, una vez']),
                dict(tipo='nombres', num=3,
                     titulo='Otra vez los nombres, a ver si ya te los sabes',
                     pista='sin mirar los deberes de la semana pasada',
                     notas=['G4', 'E4', 'F4', 'A4', 'E4', 'G4', 'B4', 'F4']),
                dict(tipo='escucha',
                     titulo='UN JUEGO, CON ALGUIEN DE CASA',
                     pista='esta vez de subir y bajar',
                     texto='Toca dos notas seguidas y quien esté contigo dice si la segunda SUBE o '
                           'BAJA respecto a la primera. Diez veces. Luego cambiad. Es lo mismo que '
                           'tienes que ver en el papel cuando lees.'),
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
