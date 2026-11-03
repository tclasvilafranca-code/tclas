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
from arnau_comun import (rutina, juego, acuerdate, diferencias, contar, teclado,
                         verdadero_falso, palmas, rodear, dibujar)

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

    # Reparto de `arnau_recetas`: semana 1 la R3 (diferencias · cuenta ·
    # teclado) y semana 2 la R4 (verdadero o falso · palmas · rodea · dibuja).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Clementine · para hacer en casa',
            intro='Esta semana hay que mirar muy fino y contar. Todo sale de la primera frase de tu '
                  'partitura, la que está medida nota a nota.',
            bloques=[
                diferencias(
                    [n('C4'), n('C4'), n('C4'), n('E4'), n('E4'), n('E4'), n('C4'), n('C4')],
                    [n('C4'), n('C4'), n('D4'), n('E4'), n('E4'), n('F4'), n('C4'), n('C4', 'h')],
                    cuantas=3,
                    titulo='Busca las tres diferencias',
                    pista='el de arriba es tu canción · en el de abajo hay tres cosas cambiadas'),
                contar([n('D4'), n('E4'), n('F4'), n('F4'), n('E4'), n('D4')],
                       ['¿Cuántos Fa hay?', '¿Cuántas veces sale el Mi?',
                        '¿Cuántas notas hay en total?'],
                       titulo='Cuenta lo que ves',
                       pista='es el final de la primera frase de tu canción'),
                teclado({0: 1, 2: 2, 3: 3, 4: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'El dedo 1 va en la número 1 y el dedo 3 en la número 2: lo dice tu '
                         'partitura.'],
                        titulo='En el teclado',
                        pista='las teclas con número son las de esta canción'),
                acuerdate('Tu canción empieza con dos notas cortas ANTES del primer compás '
                          'completo. Son la entrada: se cuenta un-dos-TRES y en el tres empiezas. '
                          'Si empiezas en el uno, la canción entera va desplazada.',
                          etiqueta='LAS DOS NOTAS DEL PRINCIPIO'),
                rutina('La primera frase con la derecha sola, cinco veces',
                       'El dedo 1 en el Do y el 3 en el Mi, sin mirar la mano',
                       'Contar un-dos-tres en voz alta mientras tocas'),
                juego('Quien esté contigo cuenta “un, dos” y tú entras en el tres, como en la '
                      'canción. Diez veces, y que vaya cambiando de velocidad.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Clementine · para hacer en casa',
            intro='Esta semana hay preguntas de sí o no, ritmo de palabras, y a escribir notas.',
            bloques=[
                verdadero_falso([
                    'Esta canción tiene tres golpes en cada compás.',
                    'La mano izquierda lleva la melodía.',
                    'El dedo 1 se pone en el Do.',
                    'La canción empieza en el primer golpe del primer compás.',
                    'En esta canción no hay ninguna tecla negra.',
                ], titulo='Verdadero o falso', pista='de tu canción · marca la casilla'),
                palmas([('CLE-MEN-TI-NA', 4), ('MI-NE-RO', 3), ('CA-JA', 2)],
                       titulo='El ritmo de las palabras',
                       pista='dilo en voz alta y escríbelo con figuras en la caja'),
                rodear([[n('C4'), n('E4'), n('E4')], [n('E4'), n('C4'), n('C4')],
                        [n('C4'), n('E4'), n('E4')], [n('F4'), n('E4'), n('D4')]],
                       titulo='Rodea los dos compases que son iguales',
                       pista='tres notas en cada compás · míralas de una en una'),
                dibujar(['Do', 'Mi', 'Re', 'Fa', 'Mi', 'Do', 'Re', 'Do'],
                        titulo='Dibuja tú las notas',
                        pista='solo el óvalo · debajo pone cuál va en cada sitio'),
                rutina('La primera frase entera, sin pararse',
                       'Las dos manos juntas, los cuatro primeros compases',
                       'Decir los nombres de las notas en voz alta'),
                acuerdate('La mano izquierda casi no toca en esta canción, y eso es a propósito: '
                          'hay compases en los que no hace nada. No te olvides de ella, solo '
                          'espera con los dedos apoyados encima de las teclas.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
