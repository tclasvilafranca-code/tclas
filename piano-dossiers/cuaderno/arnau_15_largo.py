# -*- coding: utf-8 -*-
"""Largo, de la Sinfonía del Nuevo Mundo (canción 15 de Arnau). CORTO.

   Medido sobre el PDF de su carpeta de Drive (Dvorak, arr. A. C. Escobes,
   1 pagina):

     - Do mayor: detras de la clave no hay nada, comprobado a zoom (clave de
       sol y directamente el 4/4).
     - Compas de 4/4 y pone "Largo", que quiere decir muy lento.
     - LO NUEVO: la melodia va en NOTA CON PUNTILLO mas nota corta. El puntito
       de detras de la nota la hace durar la mitad mas: una negra con puntillo
       dura golpe y medio.
     - Las alturas del principio, medidas: Mi · Sol | Mi · Re | Re · Mi · Sol ·
       Mi.
     - La izquierda toca acordes muy largos, y en varios sitios la misma nota
       sigue sonando de un compas al siguiente porque los une una ligadura.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from arnau_comun import (n, ac, sil, corch, rutina, juego, escribir,
                         palmas, inventa, nombres, verdadero_falso, acuerdate,
                         sopa, teclado)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Arnau', num=15, nivel='iniciación', slug='LargoNuevoMundo',
    formato='corto', titulo_corto='Largo · Sinfonía del Nuevo Mundo',
    time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'arnau', 'source', 'ARNAU',
                           'Largo-Sinfonia 5 Dvorak.pdf'),
    yt='https://www.youtube.com/results?search_query=dvorak+largo+new+world+piano',

    ficha=dict(
        titulo='Largo · Sinfonía del Nuevo Mundo',
        autor='Antonín Dvořák (1893) · arreglo de A. C. Escobés',
        datos=[('Novedad', 'El puntillo'), ('Golpes', '4 por compás'),
               ('Velocidad', 'Muy lento'), ('Mano izq.', 'Acordes largos'),
               ('Teclas', 'Solo blancas')],
        armonia=dict(
            titulo='La primera pieza de música clásica del cuaderno',
            tarjetas=[
                ('EL PUNTILLO', 'Golpe y medio',
                 'Un puntito detrás de la nota la hace durar la mitad más de lo normal.'),
                ('LARGO', 'Muy lento',
                 'Es una palabra italiana. Aquí no hay ninguna prisa: al contrario.'),
                ('LA MELODÍA', 'Mi · Sol · Mi · Re',
                 'Cuatro notas y ya la reconoce todo el mundo. Es de las más famosas que existen.'),
                ('LAS LIGADURAS', 'Siguen sonando',
                 'Unas líneas curvas unen notas: la de después no se toca, se deja sonar.'),
            ],
            pie='Esta melodía la escribió Dvořák hace más de cien años para una orquesta enorme, y '
                'aquí caben en tus dos manos. Es lenta, así que no hay ninguna nota difícil: lo que se '
                'aprende es a contar figuras largas y a no tener prisa.',
        ),
        titulo_ritmos='Así empieza',
        pie_ritmos='El primer compás de cada mano. Fíjate en el puntito de la primera nota.',
        ritmos=[
            ('LA DERECHA', 'una nota con puntillo, una corta y una larga',
             [n('E4', 'q.'), {'pitch': 'G4', 'dur': 'e'}, n('E4', 'h')], AZUL, 'treble', None),
            ('LA IZQUIERDA', 'un acorde que dura el compás entero',
             [ac(('C3', 'E3', 'G3'), 'w')], OCRE, 'bass', None),
        ],
        especial=[
            'No hay ni sostenidos ni bemoles: todo son teclas blancas.',
            'Cada compás lleva cuatro golpes: un-dos-tres-cuatro.',
            'Pone «Largo»: muy lento. Es lo más lento del cuaderno.',
            'Hay notas con un puntito detrás: duran la mitad más.',
            'Hay líneas curvas que unen notas: la segunda no se vuelve a tocar.',
            'La izquierda toca acordes muy largos y los deja sonar.',
        ],
        reto='El puntillo. Una negra con puntillo dura golpe y medio, así que la nota corta que viene '
             'detrás no cae en un número: cae en medio. Contar eso bien es lo único difícil que tiene '
             'esta pieza.',
        truco='Cuenta «un-y-dos-y-tres-y-cuatro-y». La nota con puntillo ocupa el un-y-dos, y la corta '
              'cae justo en la Y del dos. Dilo en voz alta muy despacio y verás que encaja: el '
              'puntillo deja de ser un misterio en cuanto lo cuentas con las Y.',
        sabias='Dvořák escribió esta sinfonía cuando vivía en Estados Unidos y echaba de menos su '
               'pueblo. Años después alguien le puso letra a esta melodía y la llamó «Volver a casa». '
               'Es tan famosa que la tocaron en la Luna: los astronautas del Apolo 11 se la llevaron.',
        qr=dict(titulo='Escúchala',
                texto='Escúchala con la orquesta entera. Es la misma melodía que vas a tocar tú.'),
    ),

    taller=dict(),

    piano1=dict(
        titulo='Cómo se aprende', esquina='Al piano · tres pasos',
        intro='Aquí no hay notas difíciles y todo va muy lento. Lo único nuevo es el puntillo, que '
              'cambia lo que dura una nota. Así que se aprende contando primero, y tocando después.',
        reglas=['CUENTA CON LAS Y', 'PONE LARGO: MUY LENTO', 'LAS LIGADURAS NO SE TOCAN'],
        bloques=[
            dict(num=1, titulo='El puntillo, contado',
                 pista='una negra con puntillo dura golpe y medio · la corta cae en la Y',
                 sistemas=[
                     dict(cap='a) primero sin puntillo, para comparar · dos notas normales y una larga',
                          events=[n('E4'), n('G4'), n('E4', 'h'),
                                  n('E4'), n('D4'), n('D4', 'h')],
                          ligar=True,
                          bars=2),
                     dict(cap='b) y ahora con el puntillo, que es como está escrito · di “un-y-dos-y”',
                          events=[n('E4', 'q.'), {'pitch': 'G4', 'dur': 'e'}, n('E4', 'h'),
                                  n('E4', 'q.'), {'pitch': 'D4', 'dur': 'e'}, n('D4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota', etiqueta='QUÉ HACE EL PUNTITO',
                 texto='Un puntito detrás de una nota le añade la mitad de lo que ya duraba. Una negra '
                       'dura un golpe; con puntillo, golpe y medio. Y como se ha comido medio golpe de '
                       'más, la nota que viene detrás ya no empieza en un número: empieza en la mitad, '
                       'en la Y. Eso es todo el misterio.'),
            dict(num=2, titulo='La melodía del principio',
                 pista='medida en tu partitura · Mi · Sol · Mi · Re, y después vuelve a subir',
                 sistemas=[
                     dict(cap='a) tal como está escrita · muy lento, que pone Largo',
                          events=[n('E4', 'q.'), {'pitch': 'G4', 'dur': 'e'}, n('E4', 'h'),
                                  n('E4', 'q.'), {'pitch': 'D4', 'dur': 'e'}, n('D4', 'h')],
                          bars=2),
                     dict(cap='b) y lo que sigue · Re · Mi · Sol · Mi, y se queda quieta',
                          events=[n('D4'), n('E4'), n('G4'), n('E4'),
                                  n('D4', 'h'), n('C4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda: acordes que duran mucho', clef='bass',
                 pista='andamio · uno por compás, y en la partitura algunos siguen sonando en el siguiente',
                 sistemas=[
                     dict(cap='a) tócalo en el uno y cuenta cuatro sin levantar los dedos',
                          events=[ac(('C3', 'E3', 'G3'), 'w'), ac(('C3', 'F3', 'A3'), 'w'),
                                  ac(('C3', 'E3', 'G3'), 'w'), ac(('B2', 'D3', 'G3'), 'w')],
                          bars=4, clef='bass'),
                 ]),
            dict(tipo='nota', etiqueta='LAS LÍNEAS CURVAS QUE UNEN NOTAS',
                 texto='Cuando dos notas iguales están unidas por una línea curva, la segunda NO se '
                       'toca: la primera sigue sonando y ya está. Sirve para que un acorde dure más de '
                       'un compás. Si la tocas otra vez, se oye un golpe donde no tenía que haber nada '
                       'y la música se corta justo cuando debía seguir.'),
        ],
    ),

    # Reparto de `arnau_recetas`: semana 1 la R19 (palmas · inventa · nombres ·
    # verdadero o falso) y semana 2 la R20 (sopa · teclado · escribe).
    deberes=[
        dict(
            titulo='Deberes · semana 1',
            esquina='Largo · Sinfonía del Nuevo Mundo · para hacer en casa',
            intro='Lo nuevo: el puntito de detrás de la nota, que la hace durar la mitad más.',
            bloques=[
                palmas([('LAR-GO', 2), ('DVO-RAK', 2), ('SIN-FO-NI-A', 4)],
                       titulo='El ritmo de las palabras',
                       pista='dilo en voz alta y escríbelo con figuras en la caja'),
                inventa(['Solo Mi, Sol y Re, que son las de tu melodía.',
                         'Dos compases de cuatro golpes.',
                         'Que una nota lleve puntito y la de después sea corta.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases muy lentos',
                        pista='tiene que cumplir las tres cosas'),
                nombres(['E4', 'G4', 'D4', 'C4', 'A4', 'F4', 'E4', 'G4'],
                        pista='son las notas de tu melodía · escríbelas debajo'),
                verdadero_falso([
                    'Una negra con puntillo dura golpe y medio.',
                    '“Largo” quiere decir que hay que tocar deprisa.',
                    'La mano izquierda toca acordes muy largos.',
                    'Hay notas que siguen sonando de un compás al siguiente.',
                ], titulo='Verdadero o falso', pista='de tu canción · marca la casilla'),
                acuerdate('El puntito de detrás de una nota le añade la mitad de lo que ya duraba. '
                          'Una negra dura un golpe, así que una negra con puntillo dura golpe y '
                          'medio. Cuenta “UN-dos” y toca la corta justo en el “dos”: verás que sale '
                          'el vaivén de esta melodía.',
                          etiqueta='QUÉ HACE EL PUNTITO'),
                rutina('Mi · Sol · Mi con la derecha, contando cuatro',
                       'La negra con puntillo y la corta, veinte veces',
                       'La izquierda sola, dejando los acordes sonar'),
            ],
        ),
        dict(
            titulo='Deberes · semana 2',
            esquina='Largo · Sinfonía del Nuevo Mundo · para hacer en casa',
            intro='Segunda semana: sopa de letras, teclado y un compás para copiar.',
            bloques=[
                sopa(['PUNTILLO', 'LARGO', 'DVORAK', 'ACORDES', 'LENTO', 'LIGADURA',
                      'ATADAS', 'MI', 'SOL', 'RE'], semilla=1515, filas=8,
                     titulo='Sopa de letras de tu canción',
                     pista='diez palabras · tumbadas, de pie o en diagonal'),
                teclado({2: 1, 4: 2, 1: 3, 0: 4},
                        ['Escribe el nombre de las cuatro teclas marcadas.',
                         'La 1 y la 2 son las dos primeras notas de tu melodía.'],
                        titulo='En el teclado',
                        pista='las cuatro marcadas son de esta canción'),
                escribir(titulo='Copia aquí un compás con puntillo',
                         pista='búscalo en tu partitura, cópialo tal cual y tócalo cinco veces'),
                rutina('La melodía entera, muy lenta y sin acelerar',
                       'Los sitios donde la nota sigue sonando en el compás siguiente',
                       'Las dos manos, cuatro compases sin parar'),
                juego('Quien esté contigo cuenta “un, dos, tres, cuatro” muy despacio y tú tocas la '
                      'melodía encima. Lo difícil de esta pieza es no acelerar: si aceleras, se nota '
                      'enseguida que ya no vas con la cuenta.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
