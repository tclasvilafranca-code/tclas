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
from arnau_comun import n, ac, sil, corch, rutina, juego, escribir

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
        pie_ritmos='Un compás de cada mano, medido en tu partitura.',
        ritmos=[
            ('LA DERECHA', 'sube por escalones y se queda arriba',
             [n('C4'), n('B4'), n('C5'), n('D5')], AZUL, 'treble', SOL),
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

    deberes=[
        dict(titulo='Deberes · semana 1', esquina='El submarino amarillo · para hacer en casa',
             intro='Esta semana toca aprender el molde de la izquierda, que es casi toda la canción.',
             bloques=[
                 dict(tipo='nombres', num=1, titulo='¿Cómo se llama cada nota?',
                      pista='ojo: en esta canción todos los Fa son tecla negra',
                      notas=['G3', 'B3', 'D4', 'A3', 'C4', 'E4', 'F#3', 'G3'], clef='bass'),
                 dict(tipo='nombres', num=2, titulo='Y estas, que son de la melodía',
                      pista='aquí la clave es la de arriba',
                      notas=['B4', 'C5', 'D5', 'A4', 'G4', 'E4', 'F#4', 'B4']),
                 dict(tipo='figuras', num=3, titulo='¿Cuántos golpes dura cada una?',
                      pista='escribe el número en la caja',
                      figuras=[('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'),
                               ('h.', 'blanca con puntito')]),
                 dict(tipo='colorea', num=4, titulo='Rodea todos los Fa',
                      pista='en esta canción todos van en la tecla negra',
                      eventos=[n('D4'), n('F#4'), n('G4'), n('F#4'),
                               n('E4'), n('F#4'), n('G4'), n('D4', 'h')],
                      leyenda=['El sostenido del principio manda en toda la canción.',
                               'La tecla negra del Fa está justo a su derecha.']),
                 rutina('El molde de la izquierda, veinte veces',
                        'El mismo molde movido a los otros sitios',
                        'Tocar todos los Fa en la tecla negra, subiendo y bajando'),
                 juego('Toca el molde de la izquierda mientras quien esté contigo lleva el pulso dando '
                       'palmadas. Que vaya cambiando de velocidad sin avisar: unas veces lento y otras '
                       'más rápido. Tú tienes que seguirle. Es la manera de aprender a no acelerar por '
                       'tu cuenta.'),
             ]),
        dict(titulo='Deberes · semana 2', esquina='El submarino amarillo · para hacer en casa',
             intro='Esta semana toca juntar las manos y empezar a subir la velocidad, pero con cabeza.',
             bloques=[
                 dict(tipo='rodea', num=1, titulo='Rodea los dos compases que son iguales',
                      pista='fíjate en las notas de una en una',
                      compases=[[n('G3'), n('B3'), n('D4'), n('B3')],
                                [n('A3'), n('C4'), n('E4'), n('C4')],
                                [n('G3'), n('B3'), n('D4'), n('B3')],
                                [n('D3'), n('A3'), n('C4'), n('A3')]], clef='bass'),
                 dict(tipo='dibuja', num=2, titulo='Dibuja tú las notas',
                      pista='solo el óvalo, sin el palito',
                      nombres=['Si', 'Do', 'Re', 'La', 'Sol', 'Mi', 'Fa', 'Si']),
                 dict(tipo='une', num=3, titulo='Une cada cosa con lo que quiere decir',
                      pista='una raya de un punto al otro',
                      pares=[('Allegro', 'todos los Fa, tecla negra'),
                             ('El sostenido del principio', 'el mismo dibujo movido de sitio'),
                             ('Un molde', 'rápido')]),
                 dict(tipo='nota', etiqueta='ACUÉRDATE',
                      texto='Subir de velocidad solo vale si la canción sale ENTERA y sin pararse. Si '
                            'tienes que parar en un sitio, ese sitio hay que trabajarlo aparte, muy '
                            'lento, y luego volver a probar. Subir con un agujero dentro no sirve de '
                            'nada.'),
                 dict(tipo='colorea', num=4, titulo='Colorea las notas que se repiten',
                      pista='la melodía dice varias veces la misma nota antes de moverse',
                      eventos=[n('B4'), n('C5'), n('D5'), n('B4'),
                               n('E4'), n('E4'), n('E4'), n('B4', 'h')],
                      leyenda=['Repetir una tecla es lo más fácil que hay para los dedos.',
                               'Por eso esta canción se puede tocar rápida sin ser difícil.']),
                 rutina('Los cuatro primeros compases con las dos manos',
                        'La canción entera muy lenta, sin parar',
                        'Un poquito más rápido, solo si la anterior salió tres veces'),
                 escribir(4),
             ]),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
