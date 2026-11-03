# -*- coding: utf-8 -*-
"""We Wish You a Merry Christmas — pieza 3 de Aida. Formato ADULTO exigente.

   Cierra la primera etapa. Las dos anteriores tenian la mano quieta y las dos
   manos al unisono; aqui entra por primera vez lo que va a ser normal en todo
   el resto del cuaderno: una ARMADURA, una ANACRUSA y el CIFRADO impreso.

   Lo comprobado sobre el PDF de SU carpeta (arreglo de Gilbert DeBenedetti,
   gmajormusictheory.org, 2 paginas; el mismo archivo, byte a byte, que el de
   Mercè y el de Isaac):

     - SOL MAYOR: un sostenido detras de la clave. Todos los Fa a la tecla
       negra.
     - 3/4, y empieza con una ANACRUSA de una negra: la silaba "We" se canta
       antes de que arranque el primer compas completo.
     - Encima del pentagrama van las LETRAS DE ACORDE (G, C, A7, D, B7, Am,
       D7), y debajo la letra de la cancion, silaba a silaba.
     - La digitacion viene impresa en las dos manos.

   LAS ALTURAS, medidas a 300 ppp y comprobadas ademas contra la letra impresa,
   que es la mejor prueba que hay: cada silaba tiene su nota.

       anacrusa   Re4                      negra        "1.We"
       c. 1       Sol4                     negra        "wish"
                  Sol4 · La4               corcheas     "you a"
                  Sol4 · Fa#4              corcheas     "mer-ry"
       c. 2       Mi4 · Mi4 · Mi4          negras       "Christ-mas, We"

   ESTA LECTURA DESTAPO UN FALLO YA IMPRESO. Los cuadernos de Mercè y de Isaac
   —que usan este mismo archivo— citaban el arranque como Re4 · Sol4 · La4 ·
   Si4 (blanca con puntillo). Ni el ritmo ni las alturas: no hay ningun Si4 y
   no hay ninguna blanca con puntillo. La aritmetica cuadraba (1+1+1+3 son dos
   compases de 3/4) y por eso no lo cazo ningun auditor. Se corrigio en los dos
   y la lectura quedo anotada en `auditar_alturas.MIRADAS`, para que a partir
   de ahora se cruce sola.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, reto, plan, cifrado, colorear,
                      figuras, acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1, medido. Cita literal. (La anacrusa va antes y se cuenta aparte:
# una fila de la ficha tiene que sumar compases enteros.)
ARRANQUE = [n('G4')] + corch(['G4', 'A4']) + corch(['G4', 'F#4'])

# El compas 2, medido: tres negras iguales.
SEGUNDO = [n('E4'), n('E4'), n('E4')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=3, nivel='intermedio',
    slug='WeWishYouAMerryChristmas', formato='adulto',
    titulo_corto='We Wish You a Merry Christmas', time_sig=(3, 4), key_sig='Sol mayor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'We Wish You a Merry Christmas.pdf'),
    yt='https://www.youtube.com/results?search_query=we+wish+you+a+merry+christmas+easy+piano',

    ficha=dict(
        titulo='We Wish You a Merry Christmas',
        autor='villancico inglés tradicional · arreglo de Gilbert DeBenedetti',
        datos=[('Tonalidad', 'Sol mayor'), ('Armadura', 'Un sostenido'),
               ('Compás', '3/4'), ('Empieza', 'Antes del compás'),
               ('Trae', 'Cifrado y letra')],
        titulo_ritmos='Los dos primeros compases, medidos',
        pie_ritmos='MEDIDO en tu partitura a 300 puntos por pulgada, y comprobado contra la letra '
                   'impresa: cada sílaba tiene su nota. Antes del compás 1 hay una anacrusa de una '
                   'negra (la sílaba "We") que no se dibuja aquí porque no llena un compás.',
        armonia=dict(
            titulo='Tres cosas nuevas de golpe, y las tres se quedan',
            tarjetas=[
                ('LA ARMADURA', 'Un sostenido',
                 'Detrás de la clave hay un Fa sostenido, y vale para toda la pieza. No hay que '
                 'acordarse compás a compás: se mira una vez, al principio.'),
                ('LA ANACRUSA', 'Un tiempo antes',
                 'La canción empieza en el tercer tiempo del compás anterior. Cuentas "un, dos" en '
                 'silencio y entras en el "tres".'),
                ('EL CIFRADO', 'G, C, A7, D',
                 'Las letras encima del pentagrama dicen qué acorde suena debajo. Saber leerlas es '
                 'lo que te va a permitir acompañar sin partitura.'),
                ('LA LETRA', 'Debajo',
                 'Cada sílaba va bajo su nota, y por eso el ritmo se puede comprobar cantando: si '
                 'la letra encaja, el ritmo está bien.'),
            ],
            pie='Es un villancico inglés de los que se cantaban de puerta en puerta pidiendo un '
                '"figgy pudding" a cambio de la canción. La estrofa que exige el pudin y avisa de '
                'que no se van hasta que se lo den es del original: no es una broma moderna.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1 y 2, MEDIDOS · antes va la anacrusa',
             ARRANQUE + SEGUNDO, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio sobre el cifrado impreso (G y C)',
             [ac(('G2', 'D3', 'B3'), 'h.'), ac(('C3', 'G3', 'E4'), 'h.')],
             AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa son teclas negras.',
            'Empieza con una anacrusa: una negra antes del primer compás completo.',
            'Encima del pentagrama van las letras de acorde: G, C, A7, D, B7, Am, D7.',
            'Debajo del pentagrama va la letra, sílaba a sílaba.',
            'La digitación viene impresa en las dos manos.',
            'Son dos páginas, y la segunda trae más estrofas de la letra.',
        ],
        reto='Que la anacrusa no se convierta en un compás entero. Es UN tiempo, y la tentación es '
             'darle tres porque psicológicamente parece el principio de todo.',
        truco='Cuenta dos compases enteros en voz alta antes de tocar y entra en el "tres" del '
              'segundo. Si cuentas solo uno, casi siempre entras tarde; si no cuentas ninguno, la '
              'anacrusa se estira sola.',
        sabias='Gilbert DeBenedetti publica estos arreglos gratis desde hace veinte años en '
               'gmajormusictheory.org, con la digitación puesta a propósito para adultos que '
               'vuelven al piano. Cuatro piezas de tu cuaderno son suyas.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta "un, dos" antes de que entre la voz. Ese hueco es tu anacrusa, y es '
                      'lo único que hay que clavar esta semana.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Las notas de esta pieza no son el problema: son siete y todas están a mano. Lo que '
              'hay que montar es la entrada, y para eso lo primero es contar sin tocar.',
        reglas=['TODOS LOS FA VAN A LA TECLA NEGRA', 'CUENTA DOS COMPASES ANTES DE ENTRAR',
                'LA LETRA TE DICE SI EL RITMO ESTÁ BIEN'],
        bloques=[
            dict(num=1, titulo='La armadura, antes que nada',
                 pista='andamio en Sol mayor · para que la mano encuentre el Fa sostenido sola',
                 sistemas=[
                     dict(cap='a) la escala de Sol, subiendo · el séptimo grado es la tecla negra',
                          events=[n('G4'), n('A4'), n('B4'), n('C5'),
                                  n('D5'), n('E5'), n('F#5'), n('G5', 'h')],
                          matiz='mp',
                          bars=3),
                     dict(cap='b) y bajando, que es donde el Fa sostenido se olvida',
                          events=[n('G5'), n('F#5'), n('E5'), n('D5'),
                                  n('C5'), n('B4'), n('A4'), n('G4', 'h')],
                          bars=3, show_time=False),
                     dict(cap='c) y con la izquierda, en su clave · la misma tecla negra, otro dedo',
                          events=[n('G3'), n('A3'), n('B3'), n('C4'),
                                  n('B3'), n('A3'), n('F#3'), n('G3', 'h')],
                          bars=3, clef='bass', show_time=False),
                     dict(cap='d) y el acorde de Sol desplegado con la izquierda · es el primero '
                              'que trae impreso tu partitura, la letra G',
                          events=[n('G2'), n('D3'), n('G3'), n('D3'),
                                  n('B3'), n('G3'), n('D3'), n('G2', 'h')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA ANACRUSA SE ESTIRA',
                 texto='Porque el oído no tiene con qué medirla: es la primera nota que suena y no '
                       'hay nada antes con lo que compararla. La solución no es contar más despacio '
                       'sino contar ANTES: dos compases enteros en voz alta, con el pie, y entrar '
                       'en el tercer tiempo del segundo. Con eso la anacrusa deja de ser el '
                       'principio y pasa a ser lo que es, el final de un compás que ya estaba '
                       'corriendo.'),
            dict(num=2, titulo='La entrada, tal y como está escrita',
                 pista='cc. 1–2 · MEDIDOS en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) el compás 1 en negras, para colocar las alturas · en tu partitura '
                              'las cuatro últimas son corcheas',
                          events=[n('G4'), n('G4'), n('A4'),
                                  n('G4'), n('F#4'), n('E4')],
                          bars=2),
                     dict(cap='b) el compás 1 con la anacrusa delante, escrita como el tercer '
                              'tiempo de un compás que empieza en silencio',
                          events=[sil('h'), n('D4')] + list(ARRANQUE),
                          bars=2, show_time=False),
                     dict(cap='c) el compás 2 y la vuelta al 1 · así se practica el salto de las '
                              'tres negras iguales a las corcheas',
                          events=list(SEGUNDO) + list(ARRANQUE),
                          bars=2, show_time=False),
                     dict(cap='d) y el compás 2 solo, dos veces · tres notas iguales seguidas es de '
                              'lo que más cuesta mantener a tiempo',
                          events=list(SEGUNDO) + list(SEGUNDO),
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, con el acorde de la letra',
                 pista='andamio sobre el cifrado IMPRESO en tu partitura (G y C)',
                 sistemas=[
                     dict(cap='a) la melodía encima y el acorde de Sol debajo, uno por compás',
                          events=[ac(('G2', 'D3', 'G4')), ac(('G4',)), ac(('A4',)),
                                  ac(('G2', 'D3', 'G4')), ac(('F#4',)), ac(('E4',))],
                          bars=2, manos='sostiene'),
                     dict(cap='b) y cambiando a Do, que es la segunda letra que trae tu partitura',
                          events=[ac(('C3', 'G3', 'E4')), ac(('E4',)), ac(('D4',)),
                                  ac(('C3', 'G3', 'C4')), ac(('D4',)), ac(('E4',))],
                          bars=2, manos='sostiene', show_time=False),
                     dict(cap='c) y los tres acordes seguidos, Sol, Do y La7 · es la vuelta que '
                              'trae impresa la primera línea de tu partitura',
                          events=[ac(('G2', 'D3', 'B4'), 'h.'),
                                  ac(('C3', 'G3', 'C5'), 'h.'),
                                  ac(('A2', 'E3', 'C#5'), 'h.'),
                                  ac(('D3', 'A3', 'D5'), 'h.')],
                          bars=4, manos='dobla', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Coge la primera línea con la partitura delante y tócala tres veces seguidas '
                       'sin parar, contando los dos compases de entrada cada vez. Lo que se practica '
                       'ahí no son las notas: es empezar. Y empezar es lo que más veces se hace en '
                       'una clase y lo que menos se estudia en casa.'),
        ] + bloques_extra('Sol mayor', 83, 'G4', 'G2',
                          'la anacrusa: entrar en el tercer tiempo, no en el uno',
                          desde=4, time_sig=(3, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='We Wish You · para casa',
            intro='Veinte minutos al día. Media semana para la armadura y media para la entrada: '
                  'las notas ya las tienes desde el primer día.',
            bloques=[
                reto('Entrar en la anacrusa sin estirarla.',
                     'Pon el metrónomo, cuenta DOS compases enteros en voz alta y entra en el '
                     '"tres" del segundo. Si entras antes o después, no vuelvas a intentarlo: '
                     'vuelve a contar los dos compases.'),
                plan((5, 'La escala de Sol, subiendo y bajando, sin mirar la mano'),
                     (5, 'Contar dos compases y entrar en el "tres", sin tocar'),
                     (5, 'Los compases 1 y 2, con la anacrusa delante'),
                     (5, 'La primera línea entera, cantando la letra')),
                cifrado([('G', 'Sol'), ('C', 'Do'), ('A7', 'La'), ('D', 'Re')],
                        ['¿Cuál de los cuatro lleva el Fa sostenido de la armadura?',
                         '¿Cuál de los cuatro es el que da la sensación de "ya hemos llegado"?'],
                        titulo='Las letras de acorde que trae tu partitura',
                        pista='están impresas encima del pentagrama · escribe sus tres notas'),
                colorear(list(ARRANQUE) + list(SEGUNDO),
                         [('negras', 'las notas que duran un tiempo'),
                          ('corcheas', 'las que duran medio')],
                         titulo='Colorea por figuras tus dos primeros compases',
                         pista='un color para las negras y otro para las corcheas'),
                figuras([('q', 'negra'), ('e', 'corchea'), ('h.', 'blanca con puntillo'),
                         ('h', 'blanca')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='y di cuál de las cuatro llena ella sola un compás de 3/4'),
                acuerdate('La armadura no es una nota: es una instrucción que vale para toda la '
                          'pieza. Ese sostenido de detrás de la clave dice que TODOS los Fa, en '
                          'las dos manos y en cualquier octava, se tocan en la tecla negra. No hay '
                          'que buscarlo compás a compás.',
                          etiqueta='LA ARMADURA'),
                para_clase('La primera línea entera con las dos manos, entrando en la anacrusa. Y '
                           'dime en voz alta las cuatro letras de acorde de la primera página: si '
                           'te las sabes, la semana que viene empezamos a acompañar sin leer.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
