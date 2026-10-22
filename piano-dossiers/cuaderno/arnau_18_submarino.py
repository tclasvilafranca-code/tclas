# -*- coding: utf-8 -*-
"""El submarino amarillo (canción 18 de Arnau, iniciación). Formato CORTO.

   Medido sobre el PDF de su carpeta de Drive (Lennon y McCartney, arr. A. C.
   Escobes, 1 pagina):

     - SOL MAYOR: comprobado a zoom, un sostenido detras de la clave, o sea
       que todos los Fa van en la tecla negra.
     - Compas de 4/4 y pone "Allegro": rapido.
     - La izquierda hace un molde de acordes que se repite: medido Sol · Si ·
       Re · Si · Re, y el mismo dibujo movido a La · Do · Do y a Re · La · Do.
     - La melodia se mueve por escalones y repite mucho la misma nota.
     - LO NUEVO: es la primera cancion del cuaderno con las dos manos
       moviendose Y a una velocidad de verdad (Allegro).
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         camino, nombres, inventa, unir, sopa, ordenar,
                         colorear, acuerdate)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'

CANCION = dict(
    alumno='Arnau', num=18, nivel='iniciación', slug='SubmarinoAmarillo',
    formato='corto', titulo_corto='El submarino amarillo',
    time_sig=(4, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'ElSubmarinoAmarillo-.pdf'),
    yt='https://www.youtube.com/results?search_query=yellow+submarine+piano+facil',

    ficha=dict(
        titulo='El submarino amarillo',
        autor='John Lennon y Paul McCartney (1966) · arr. A. C. Escobés',
        datos=[('Tecla negra', 'Todos los Fa'), ('Golpes', '4 por compás'),
               ('Velocidad', 'Allegro'), ('Mano izq.', 'Un molde'),
               ('Las dos manos', 'Se mueven')],
        armonia=dict(
            titulo='La primera que va deprisa de verdad',
            tarjetas=[
                ('ALLEGRO', 'Rápido',
                 'Es la más rápida del cuaderno. Pero se aprende igual: despacio primero.'),
                ('EL SOSTENIDO', 'Todos los Fa',
                 'Como en Popeye: está al principio y vale para toda la canción.'),
                ('LA IZQUIERDA', 'Un molde',
                 'Sol · Si · Re · Si · Re, y el mismo dibujo movido a otros sitios.'),
                ('LA MELODÍA', 'Repite mucho',
                 'Se mueve por escalones y dice varias veces la misma nota. Es de cantar.'),
            ],
            pie='Que ponga Allegro no quiere decir que la aprendas rápido: quiere decir que ACABARÁS '
                'tocándola rápido. Se empieza lento igual que todas, y la velocidad se sube al final, '
                'cuando ya no hay fallos.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='La derecha, medida nota a nota en tu partitura. Abajo, el molde que '
                   'repite la izquierda, que no es una copia literal.',
        ritmos=[
            # Medido sobre el PDF a 300 ppp (21 ago 2026): la cancion entra ANTES
            # del primer compas con dos corcheas, Si y Do, y el Re de despues es
            # la nota larga. Antes ponia un Do4 delante que no esta en el papel.
            ('LA DERECHA', 'Si · Do · Re: sube por escalones y el Re se queda',
             corch(['B4', 'C5']) + [n('D5', 'h'), n('B4')], AZUL, 'treble', SOL),
            ('LA IZQUIERDA', 'el molde que se repite',
             [n('G3'), n('B3'), n('D4'), n('B3')], OCRE, 'bass', SOL),
        ],
        especial=[
            'Hay UN SOSTENIDO detrás de la clave: todos los Fa van en la tecla negra.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'Pone «Allegro»: rápido. Es la más rápida del cuaderno.',
            'La izquierda hace un molde de notas que se repite y se muda de sitio.',
            'La melodía se mueve por escalones y repite mucho la misma nota.',
            'Las dos manos se mueven a la vez: hay que aprender cada una por su lado.',
            'El molde de la izquierda se muda de sitio, pero el dibujo no cambia.',
            'La canción repite mucho: hay pocos trozos distintos de verdad.',
        ],
        reto='La velocidad. Cuando una canción pone «rápido» dan ganas de tocarla rápido desde el '
             'primer día, y entonces se aprende con fallos dentro. Y los fallos aprendidos deprisa '
             'cuesta muchísimo quitarlos después.',
        truco='Elige una velocidad en la que te salga ENTERA sin parar, aunque sea lentísima, y quédate '
              'ahí hasta que salga tres veces seguidas. Solo entonces sube un poquito. Así llegarás a '
              'Allegro en tres semanas; del otro modo, no llegas.',
        sabias='La canción la cantaba Ringo Starr, el batería, porque los Beatles querían una canción '
               'para niños en el disco. Está llena de ruidos de verdad: en el estudio soplaron burbujas '
               'en un cubo de agua y movieron cadenas para que sonara a submarino.',
        qr=dict(titulo='Escúchala',
                texto='Escucha los ruidos de fondo: son burbujas y cadenas de verdad.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Aquí no hay nada nuevo que no sepas ya: un sostenido al principio, las dos manos '
              'moviéndose y un molde que se repite. Lo nuevo es la velocidad, y esa se deja para el '
              'final.',
        reglas=['TODOS LOS FA, EN LA TECLA NEGRA', 'DESPACIO HASTA QUE SALGA ENTERA',
                'LA VELOCIDAD, AL FINAL'],
        bloques=[
            dict(num=1, titulo='El molde de la izquierda', clef='bass',
                 pista='medido · Sol · Si · Re · Si · Re, y siempre el mismo dibujo',
                 sistemas=[
                     dict(cap='a) el molde entero, dos veces · el primero pesa más que los demás',
                          events=[n('G3'), n('B3'), n('D4'), n('B3'),
                                  n('G3'), n('B3'), n('D4'), n('B3')],
                          bars=2, clef='bass'),
                     dict(cap='b) y el mismo dibujo movido de sitio · lo único que cambia es dónde empieza',
                          events=[n('A3'), n('C4'), n('E4'), n('C4'),
                                  n('D3'), n('A3'), n('C4'), n('A3')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='POR QUÉ UN MOLDE ES BUENA NOTICIA',
                 texto='Si la izquierda hace siempre el mismo dibujo y solo cambia de sitio, no tienes '
                       'que aprender la izquierda de la canción entera: tienes que aprender UN dibujo y '
                       'saber dónde se pone cada vez. Eso es mucho menos trabajo, y es lo que hace que '
                       'una canción larga se pueda tocar en dos semanas.'),
            dict(num=2, titulo='La melodía',
                 pista='medida en tu partitura · sube por escalones y repite mucho',
                 sistemas=[
                     dict(cap='a) el principio · sube de una en una hasta el Re y se queda',
                          events=[n('C4'), n('B4'), n('C5'), n('D5'),
                                  n('B4'), n('A4'), n('B4', 'h')],
                          bars=2),
                     dict(cap='b) y lo que sigue · baja al Mi y vuelve a subir al Si',
                          events=[n('A4'), n('G4'), n('E4'), n('E4'),
                                  n('E4'), n('B4'), n('B4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Los Fa de la tecla negra',
                 pista='el sostenido del principio vale para toda la canción',
                 sistemas=[
                     dict(cap='a) sube y baja pasando por el Fa · ese Fa es la tecla negra',
                          events=[n('D4'), n('E4'), n('F#4'), n('G4'),
                                  n('F#4'), n('E4'), n('D4', 'h')],
                          bars=2),
                 ]),
            dict(tipo='nota', etiqueta='CÓMO SE LLEGA A TOCAR RÁPIDO',
                 texto='No se llega tocando rápido: se llega tocando lento sin fallos y subiendo poco a '
                       'poco. Elige la velocidad a la que te sale entera y sin pararte, aunque sea muy '
                       'lenta. Cuando salga tres veces seguidas, sube un poquito. Si al subir empiezas '
                       'a fallar, has subido demasiado: baja otra vez. Eso es todo el secreto.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R5 (camino · nombres · inventa ·
    # une) y semana 2 la R6 (sopa · ordena · colorea).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='El submarino amarillo · para hacer en casa',
            intro='Lo nuevo: Allegro, o sea rápido. Y la izquierda hace un molde que se repite.',
            bloques=[
                camino([['igual', 'molde', 'igual', 'igual', 'nuevo', 'igual'],
                        ['nuevo', 'molde', 'molde', 'igual', 'igual', 'igual'],
                        ['igual', 'igual', 'molde', 'nuevo', 'igual', 'nuevo'],
                        ['igual', 'nuevo', 'molde', 'molde', 'igual', 'igual'],
                        ['igual', 'igual', 'igual', 'molde', 'nuevo', 'igual']],
                       titulo='El camino del molde',
                       pista='colorea solo donde dice “molde” y sale un camino'),
                nombres(['B4', 'C5', 'D5', 'A4', 'G4', 'E4', 'F#4', 'B4'],
                        pista='son las notas de tu melodía · cuidado con el Fa'),
                inventa(['Solo Sol, La, Si y Do.',
                         'Dos compases de cuatro golpes.',
                         'Que el segundo compás sea el primero movido de sitio, como el molde.'],
                        time_sig=(4, 4),
                        titulo='Inventa tu propio molde',
                        pista='tiene que cumplir las tres cosas'),
                unir([('El sostenido del principio', 'el mismo dibujo movido de sitio'),
                      ('“Allegro”', 'todos los Fa van en la tecla negra'),
                      ('El molde de la izquierda', 'rápido'),
                      ('Los cuatro golpes del compás', 'se cuentan igual, aunque vayas deprisa')],
                     titulo='Une cada cosa con lo que significa',
                     pista='están desordenadas · una raya de un punto al otro'),
                rutina('El molde de la izquierda, solo, hasta que salga sin pensar',
                       'La melodía sola, despacio',
                       'Las dos manos, cuatro compases'),
                juego('Canta el estribillo del submarino amarillo mientras tocas solo la izquierda. '
                      'Quien esté contigo canta contigo. Es más difícil de lo que parece.'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='El submarino amarillo · para hacer en casa',
            intro='Segunda semana: sopa de letras, los pasos para subir la velocidad, y colores.',
            bloques=[
                sopa(['SUBMARINO', 'AMARILLO', 'BEATLES', 'ALLEGRO', 'MOLDE', 'RAPIDO',
                      'SOSTENIDO', 'SOL', 'SI', 'RE'], semilla=1818, filas=8,
                     titulo='Sopa de letras de tu canción',
                     pista='diez palabras · tumbadas, de pie o en diagonal'),
                ordenar(['Subir un poquito la velocidad.',
                         'Tocarla tres veces seguidas sin fallos a esa velocidad.',
                         'Tocarla a la velocidad a la que te sale entera y sin pararte.',
                         'Si al subir empiezas a fallar, bajar otra vez.'],
                        titulo='Pon en orden los pasos para tocar rápido',
                        pista='escribe 1, 2, 3 y 4 en las casillas'),
                colorear([n('G4'), n('B4'), n('D5', 'h'),
                          n('A4'), n('C5'), n('E5', 'h'), n('F#4'), n('G4')],
                         ['Un color para las de un golpe y otro para las de dos.'],
                         titulo='Colorea según lo que duran',
                         pista='dos colores'),
                rutina('La canción entera a la velocidad que te salga sin fallos',
                       'Subir un poquito solo si te ha salido tres veces seguidas',
                       'El molde de la izquierda, sin mirarse la mano'),
                acuerdate('No se llega a tocar rápido tocando rápido: se llega tocando lento sin '
                          'fallos y subiendo poco a poco. Si al subir empiezas a fallar, has subido '
                          'demasiado: baja otra vez. Eso es todo el secreto.',
                          etiqueta='CÓMO SE LLEGA A TOCAR RÁPIDO'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
