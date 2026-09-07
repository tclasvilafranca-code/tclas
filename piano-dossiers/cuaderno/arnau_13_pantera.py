# -*- coding: utf-8 -*-
"""La Pantera Rosa (canción 13 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive ("La Panthère rose (Première
   année)", descarga de Musescore, 1 pagina):

     - No hay nada detras de la clave, pero SI hay sostenidos escritos a mano
       delante de algunas notas. Es la primera pieza del cuaderno donde una
       tecla negra aparece de repente en medio, sin avisar desde el principio.
     - Compas de 4/4.
     - LO NUEVO: la cancion empieza con TRES COMPASES en los que la derecha no
       toca nada, y despues entra con notas sueltas separadas por silencios.
     - La izquierda toca redondas: una nota que dura el compas entero.
     - La digitacion viene impresa: 1, 2, 3, 4 encima de la melodia, y 5 y 1
       debajo de la izquierda.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         sopa, diferencias, acuerdate, verdadero_falso, ordenar,
                         figuras, dibujar)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Arnau', num=13, nivel='iniciación', slug='PanteraRosa',
    formato='corto', titulo_corto='La Pantera Rosa',
    time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'La Pantera Rosa.pdf'),
    yt='https://www.youtube.com/results?search_query=pink+panther+piano+facil',

    ficha=dict(
        titulo='La Pantera Rosa',
        autor='Henry Mancini (1963) · versión «Première année»',
        datos=[('Novedad', 'Teclas negras'), ('Golpes', '4 por compás'),
               ('Empieza', 'Con silencio'), ('Mano izq.', 'Redondas'),
               ('Dedos', 'Escritos')],
        armonia=dict(
            titulo='La canción que empieza sin tocar nada',
            tarjetas=[
                ('EL PRINCIPIO', 'Tres compases',
                 'La derecha no toca nada durante tres compases enteros. Hay que contarlos.'),
                ('LOS SOSTENIDOS', 'A mitad de camino',
                 'Aquí las teclas negras aparecen de repente, escritas delante de la nota.'),
                ('LA MELODÍA', 'A trocitos',
                 'Notas sueltas separadas por silencios. Nunca suena seguida: es la gracia.'),
                ('LA IZQUIERDA', 'Redondas',
                 'Una nota que dura los cuatro golpes. Se toca y se deja sonar.'),
            ],
            pie='Esta melodía está hecha de trocitos con huecos en medio, como si la pantera fuera de '
                'puntillas y se parara a mirar. Por eso los silencios son la mitad de la canción: si '
                'los rellenas, deja de sonar a Pantera Rosa.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='Un trozo de la melodía y lo que hace la izquierda debajo.',
        ritmos=[
            ('LA DERECHA', 'notas sueltas con huecos en medio',
             [sil('q'), n('C4'), sil('q'), n('D4')], AZUL, 'treble', None),
            ('LA IZQUIERDA', 'una nota que dura el compás entero',
             [n('C3', 'w')], OCRE, 'bass', None),
        ],
        especial=[
            'No hay nada detrás de la clave, pero sí sostenidos escritos delante de algunas notas.',
            'Un sostenido delante de una nota quiere decir: esa vez, tecla negra.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'La canción empieza con tres compases en los que la derecha no toca.',
            'La melodía va a trocitos, con silencios en medio.',
            'La izquierda toca redondas: una nota por compás, y se deja sonar.',
            'Los números de encima y de debajo de las notas son los dedos.',
            'La misma frase vuelve varias veces a lo largo de la canción.',
        ],
        reto='Los huecos. Esta melodía tiene casi tantos silencios como notas, y hay que contarlos '
             'todos: si los acortas, las notas se juntan y la canción deja de sonar a lo que es.',
        truco='Cuenta los cuatro golpes en voz alta SIEMPRE, tanto cuando tocas como cuando no. En los '
              'huecos di el número más fuerte. Y cuando llegue el primer sostenido, para un momento, '
              'míralo, y toca esa vez la tecla negra: no vale acordarse a medias.',
        sabias='Henry Mancini escribió esta música para la película de 1963, y la parte más famosa la '
               'toca un saxofón. La melodía va a trozos y con silencios a propósito: quería que sonara '
               'como alguien caminando de puntillas para que no le pillen.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta los huecos. Hay casi tantos como notas, y son la mitad de la gracia.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Aquí hay dos cosas nuevas: la canción empieza sin tocar nada y aparecen teclas negras '
              'de repente. Las dos se resuelven igual: contando en voz alta y mirando el papel antes '
              'de tocar.',
        reglas=['CUENTA TAMBIÉN LOS HUECOS', 'UN SOSTENIDO ES UNA TECLA NEGRA', 'DESPACIO'],
        bloques=[
            dict(num=1, titulo='Entrar después de los silencios',
                 pista='la derecha no toca en los tres primeros compases · hay que contarlos igual',
                 sistemas=[
                     dict(cap='a) un compás entero sin tocar y entras · cuenta los cuatro golpes en voz alta',
                          events=[sil('q'), sil('q'), sil('q'), sil('q'),
                                  sil('q'), n('C4'), sil('q'), n('D4')],
                          bars=2),
                     dict(cap='b) y ahora con más huecos · el silencio dura lo mismo que la nota',
                          events=[sil('q'), n('C4'), sil('q'), n('D4'),
                                  sil('q'), n('E4'), n('D4'), sil('q')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='QUÉ ES UN SOSTENIDO SUELTO',
                 texto='Hasta ahora, cuando había una tecla negra te lo decían al principio de la '
                       'canción, detrás de la clave, y valía para toda la pieza. Aquí no: el signo '
                       'aparece justo delante de una nota concreta y vale solo para ese compás. Cuando '
                       'lo veas, esa nota se toca en la tecla negra de al lado, la de arriba.'),
            dict(num=2, titulo='Las teclas negras que aparecen de repente',
                 pista='andamio · así se ve la diferencia entre la tecla blanca y la negra de al lado',
                 sistemas=[
                     dict(cap='a) primero las dos seguidas · toca una y luego la otra, y escucha',
                          events=[n('F4'), n('F#4'), n('F4'), n('F#4'),
                                  n('G4', 'h'), sil('h')],
                          bars=2),
                     dict(cap='b) y ahora dentro de la melodía · para un momento antes de la negra',
                          events=[n('C4'), n('D4'), n('D#4'), n('E4'),
                                  n('D4'), n('C4'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda: una nota y ya', clef='bass',
                 pista='medido · redondas, una por compás, y se dejan sonar',
                 sistemas=[
                     dict(cap='a) tócala en el uno y cuenta hasta cuatro sin levantar el dedo',
                          events=[n('C3', 'w'), n('G2', 'w'), n('C3', 'w'), n('G2', 'w')],
                          bars=4, clef='bass'),
                 ]),
            dict(tipo='nota', etiqueta='POR QUÉ ESTA CANCIÓN SUENA ASÍ',
                 texto='La melodía está hecha de trocitos con huecos: dos notas, silencio, dos notas, '
                       'silencio. Eso es lo que hace que suene a alguien andando de puntillas y '
                       'parándose a mirar. Si tocas los huecos más cortos de lo que son, la pantera '
                       'deja de ir de puntillas y sale corriendo.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R15 (sopa · diferencias) y semana
    # 2 la R16 (verdadero o falso · ordena · figuras · dibuja).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='La Pantera Rosa · para hacer en casa',
            intro='Esta es la canción misteriosa del cuaderno: empieza con tres compases callada y '
                  'de repente aparecen teclas negras en medio.',
            bloques=[
                sopa(['PANTERA', 'MISTERIO', 'SOSTENIDO', 'NEGRA', 'SILENCIO', 'REDONDA',
                      'ESPERAR', 'MI', 'RE', 'DO'], semilla=1313, filas=8,
                     titulo='Sopa de letras de tu canción',
                     pista='diez palabras · tumbadas, de pie o en diagonal'),
                diferencias(
                    [n('C4'), n('D4'), n('E4'), n('D4'), n('C4'), n('D4'), n('E4', 'h')],
                    [n('C4'), n('D4'), n('D#4'), n('D4'), n('C4'), n('E4'), n('E4')],
                    cuantas=3,
                    titulo='Busca las tres diferencias',
                    pista='el de arriba no tiene teclas negras · el de abajo sí, y hay más trampas'),
                acuerdate('Hasta ahora las teclas negras venían avisadas al principio de la canción y '
                          'valían para toda. Aquí no: el sostenido está escrito delante de una nota '
                          'suelta, en medio, y solo vale para ESE compás. Márcalos con lápiz antes de '
                          'tocar, que si no se pasan.',
                          etiqueta='LOS SOSTENIDOS QUE APARECEN DE REPENTE'),
                rutina('Contar los tres compases del principio sin tocar',
                       'Las notas con sostenido, una por una, muy despacio',
                       'La izquierda sola: una nota que dura todo el compás'),
                juego('Quien esté contigo cuenta tres compases de cuatro golpes en voz alta y tú '
                      'entras justo después, con la primera nota. Diez veces.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='La Pantera Rosa · para hacer en casa',
            intro='Esta semana hay preguntas, pasos que ordenar y notas que dibujar.',
            bloques=[
                verdadero_falso([
                    'Esta canción empieza tocando en el primer compás.',
                    'Los sostenidos están escritos delante de las notas, en medio.',
                    'Un sostenido escrito así solo vale para su compás.',
                    'La mano izquierda toca notas que duran el compás entero.',
                    'Esta canción tiene cuatro golpes en cada compás.',
                ], titulo='Verdadero o falso', pista='de tu canción · marca la casilla'),
                ordenar(['Tocar la melodía entera, con los sostenidos.',
                         'Marcar con lápiz todos los sostenidos de la partitura.',
                         'Contar los tres compases del principio.',
                         'Añadir la izquierda, que aguanta cada nota.'],
                        titulo='Pon los pasos en el orden bueno',
                        pista='escribe 1, 2, 3 y 4 en las casillas'),
                figuras([('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'),
                         ('q.', 'negra con puntito')],
                        titulo='¿Cuántos golpes dura cada una?',
                        pista='el puntito le añade la mitad'),
                dibujar(['Do', 'Re', 'Mi', 'Sol', 'Fa', 'La', 'Si', 'Do'],
                        titulo='Dibuja tú las notas',
                        pista='solo el óvalo · debajo pone cuál va en cada sitio'),
                rutina('La melodía entera con los sostenidos puestos',
                       'La izquierda sola, contando cuatro',
                       'Las dos manos, sin correr'),
                acuerdate('En esta canción los silencios son casi tan importantes como las notas: es '
                          'lo que hace que suene misteriosa. Si los acortas, la Pantera Rosa deja de '
                          'ser la Pantera Rosa.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
