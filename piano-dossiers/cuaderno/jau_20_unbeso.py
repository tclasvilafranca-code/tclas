# -*- coding: utf-8 -*-
"""Un beso y una flor (Nino Bravo) — pieza 20 de Jaume. ADULTO exigente, con cifrado.

   Lo comprobado sobre el PDF de su carpeta de Drive (Musescore · Musicaymaestro,
   2 páginas, vectorial, 34 compases), a 110-250 ppp:

     - FA MAYOR: un bemol detrás de la clave. El compás se escribe con una C
       (4/4). Arriba pone "Allegro", sin número de metrónomo.
     - Trae el CIFRADO IMPRESO encima del pentagrama: F, Dm, B♭, Am, A, C y F/A.
     - La derecha va en semicorcheas sueltas mezcladas con corcheas; la
       izquierda, en octavas. Trae una barra de repetición y dos casillas (1 y 2).
     - MEDIDO (a 250 ppp y contando las barras de cada grupo):
       derecha c. 1: silencio de corchea · La4 La4 (semicorcheas) · La4 (corchea)
                     La4 Si♭4 (semicorcheas) · Si♭4 (semicorchea) La4 (corchea)
                     Sol4 (semicorchea) · La4 (negra)
       derecha c. 3: Fa4 (blanca, ligada) · Fa4 Mi4 Fa4 Sol4 (corcheas)
       derecha c. 4: Fa4 (blanca) y silencio de blanca
       izquierda cc. 1-2: Fa2+Fa3 (blanca, ligada) · Fa2+Fa3 (negra con puntillo) ·
                     Mi2+Mi3 (corchea)
       izquierda cc. 3-4: lo mismo sobre Re2+Re3 y Do2+Do3
   Es el mismo archivo que el de Aída y el de Josep. Aquí lo literal es lo medido
   y el andamio es otro.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, reto, plan, cifrado, verdadero_falso, figuras,
                       para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'


def lig(p, d='q'):
    return dict(pitch=p, dur=d, lig=True)


# MEDIDO: c. 1 (derecha)
C1 = [sil('e'), n('A4', 's'), n('A4', 's'), n('A4', 'e'), n('A4', 's'), n('Bb4', 's'),
      n('Bb4', 's'), n('A4', 'e'), n('G4', 's'), n('A4')]
# MEDIDO: cc. 3 y 4 (derecha)
C34 = [lig('F4', 'h'), n('F4', 'e'), n('E4', 'e'), n('F4', 'e'), n('G4', 'e'),
       n('F4', 'h'), sil('h')]
# MEDIDO: octavas de la izquierda, cc. 1-2 y 3-4
L12 = [dict(pitches=['F2', 'F3'], dur='h', lig=True), ac(('F2', 'F3'), 'q.'), ac(('E2', 'E3'), 'e')]
L34 = [dict(pitches=['D2', 'D3'], dur='h', lig=True), ac(('D2', 'D3'), 'q.'), ac(('C2', 'C3'), 'e')]

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=20, nivel='intermedio', slug='UnBesoYUnaFlor',
    formato='adulto',
    titulo_corto='Un beso y una flor', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source',
                           'Un beso y una flor Nino Bravo'),
    yt='https://www.youtube.com/results?search_query=un+beso+y+una+flor+nino+bravo+piano',

    ficha=dict(
        titulo='Un beso y una flor',
        autor='Nino Bravo · versión para piano de Musescore (Musicaymaestro)',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', '4/4'),
               ('Carácter', 'Allegro'), ('Cifrado', 'Impreso'),
               ('Estructura', 'Con casillas')],
        titulo_ritmos='El c. 1, medido, y las octavas',
        pie_ritmos='Medido sobre tu partitura: arriba la derecha del c. 1, con las semicorcheas sueltas; '
                   'abajo la izquierda del mismo compás, en octavas (Fa y Mi).',
        armonia=dict(
            titulo='Semicorcheas sueltas, octavas y un cifrado completo',
            tarjetas=[
                ('LAS SEMICORCHEAS', 'Sueltas, no en fila',
                 'En el c. 1 aparecen mezcladas con corcheas dentro del mismo golpe: dos '
                 'semicorcheas, una corchea, dos semicorcheas… Es más difícil que una carrerilla de '
                 'cuatro iguales, porque el ojo no puede adivinar.'),
                ('LAS OCTAVAS', 'Dos teclas',
                 'La mano de abajo toca cada nota y su octava a la vez: Fa y Fa, Mi y Mi, Re y Re. '
                 'La mano se abre una octava justa y no se cierra entre acorde y acorde.'),
                ('EL CIFRADO', 'Siete letras',
                 'Encima del pentagrama van siete letras. Casi todo se mueve entre F, Dm y B♭, y la '
                 'A y la F/A son las que se salen de lo habitual.'),
                ('LAS CASILLAS', '1 y 2',
                 'La pieza acaba en una barra de repetición con dos finales. La primera vez se '
                 'toca el compás de la casilla 1 y al llegar a la barra se vuelve atrás.'),
            ],
            pie='Son dos páginas y 34 compases. El cifrado impreso permite estudiar la pieza por '
                'acordes y no compás a compás, que es como se entiende de verdad.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido', C1, OCRE, 'treble', FA),
            ('MANO IZQUIERDA', 'c. 1 · medido, en octavas', L12, AZUL, 'bass', FA),
        ],
        especial=[
            'Detrás de la clave hay un bemol: todos los Si van a la tecla negra.',
            'El compás se escribe con una C: es 4/4. Arriba pone Allegro, sin número de metrónomo.',
            'Encima del pentagrama va el cifrado: F, Dm, B♭, Am, A, C y F/A.',
            'La derecha mezcla semicorcheas y corcheas; la izquierda va en octavas.',
            'Acaba en una barra de repetición con casilla 1 y casilla 2.',
            'Lleva semicorcheas, ligaduras de unión y silencios de corchea y de blanca.',
        ],
        reto='Tocar el c. 1 sin que las semicorcheas se aprieten ni las corcheas se estiren: son '
             'nueve notas con cuatro figuras distintas dentro de un solo compás.',
        truco='Cuenta el compás en semicorcheas, 1-2-3-4 por tiempo, y escribe a lápiz el número de '
              'la cuenta bajo cada nota. Si una semicorchea se te adelanta, estás contando '
              'corcheas.',
        sabias='Un beso y una flor es de 1972, y la cantó Nino Bravo, que murió al año siguiente '
               'en un accidente de coche. La música es de Manuel Alejandro y la letra, de Ana '
               'Magdalena.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la canción siguiendo el cifrado: casi toda se mueve entre F, Dm y '
                      'B♭, y la A es la que cambia el color de la frase.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia por acordes: primero las letras con la izquierda en octavas, y después la '
              'melodía encima, con las semicorcheas contadas en voz alta.',
        reglas=['LAS LETRAS ANTES QUE LAS NOTAS', 'LAS SEMICORCHEAS SE CUENTAN',
                'LAS OCTAVAS SIN CERRAR LA MANO'],
        bloques=[
            dict(num=1, titulo='El ritmo del c. 1, en tres pasos',
                 pista='el c. 1 está medido en la ficha · aquí se desmonta · cuatro figuras distintas '
                       'dentro de un solo compás',
                 sistemas=[
                     dict(cap='a) el esqueleto en corcheas · NO es lo que pone tu partitura: sirve '
                              'para tener los golpes antes de apretar',
                          events=[sil('e'), n('A4', 'e'), n('A4', 'e'), n('Bb4', 'e'),
                                  n('A4', 'e'), n('G4', 'e'), n('A4')],
                          bars=1, key_sig=FA),
                     dict(cap='b) el ritmo exacto del c. 1 sobre una sola nota · andamio · cuenta '
                              'semicorcheas, 1-2-3-4',
                          events=[sil('e'), n('F4', 's'), n('F4', 's'), n('F4', 'e'), n('F4', 's'),
                                  n('F4', 's'), n('F4', 's'), n('F4', 'e'), n('F4', 's'), n('F4')],
                          bars=1, show_time=False, key_sig=FA),
                     dict(cap='c) los cc. 3 y 4, que van detrás · la blanca ligada, cuatro corcheas '
                              'y la blanca con su silencio',
                          events=C34, bars=2, show_time=False, key_sig=FA),
                 ]),
            dict(num=2, titulo='Las octavas de la izquierda, cc. 3-4',
                 pista='cc. 3-4 · medido sobre tu partitura · una blanca ligada a una negra con '
                       'puntillo y una corchea, en octavas',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) Re y su octava, la blanca ligada a la negra con puntillo, y Do y '
                              'su octava de corchea · los dos compases son iguales',
                          events=L34 + L34, bars=2, clef='bass', key_sig=FA),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE CUENTA EN SEMICORCHEAS',
                 texto='Cuando una figura corta se mezcla con otra larga dentro del mismo golpe, '
                       'contar corcheas no sirve: la semicorchea cae entre dos números. La salida '
                       'es contar los cuatro cuartos de cada tiempo, 1-2-3-4, y colocar cada nota '
                       'en el número que le toca. Al principio es lento; a la semana es automático.'),
            dict(num=3, titulo='Los acordes del cifrado, en inversión',
                 pista='andamio sobre las letras IMPRESAS en tu partitura (F, Dm, B♭, Am, C)',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) uno por compás, en la inversión más cercana al anterior · F, '
                              'Dm, B♭ y C, que son los que más se repiten',
                          events=[ac(('F2', 'C3', 'A3'), 'w'), ac(('D3', 'F3', 'A3'), 'w'),
                                  ac(('D3', 'F3', 'Bb3'), 'w'), ac(('E3', 'G3', 'C4'), 'w')],
                          bars=4, clef='bass', key_sig=FA),
                     dict(cap='b) Am y A, que solo se distinguen en una nota · el segundo trae una '
                              'tecla negra que no está en la armadura',
                          events=[ac(('A2', 'E3', 'A3'), 'w'), ac(('A2', 'E3', 'C#4'), 'w')],
                          bars=2, clef='bass', show_time=False, key_sig=FA),
                 ]),
            dict(num=4, titulo='Las casillas y la barra de repetición',
                 pista='andamio · el signo se lee igual en cualquier pieza · en tu partitura '
                       'localiza dónde está cada uno',
                 sistemas=[
                     dict(cap='a) casilla 1: la primera vez se toca este compás y al llegar a la '
                              'barra de repetición se vuelve atrás',
                          events=[n('C5'), n('A4'), n('G4'), n('F4')],
                          bars=1, repetir='cierra', casilla='1', key_sig=FA),
                     dict(cap='b) casilla 2: la segunda vez se salta la casilla 1 y se toca este '
                              'compás, que es el final',
                          events=[n('G4'), n('E4'), n('F4', 'h')],
                          bars=1, casilla='2', show_time=False, key_sig=FA),
                 ]),
        ] + bloques_extra(FA, 20, 'F4', 'F3',
                          'las semicorcheas mezcladas con corcheas y las octavas de la izquierda',
                          desde=5, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Un beso y una flor · para casa',
            intro='Veinte minutos al día. Se estudia por acordes: primero las letras, luego las '
                  'notas, y las semicorcheas solo al final.',
            bloques=[
                plan((5, 'Las letras del cifrado, con la izquierda, diciéndolas en voz alta'),
                     (5, 'Las octavas de los cc. 1-4, sin la derecha'),
                     (6, 'La derecha del c. 1 contando en semicorcheas'),
                     (4, 'Las dos manos, cc. 1-4, despacio')),
                cifrado(['F', 'Dm', 'B♭', 'Am', 'A', 'C', 'F/A'],
                        ['Escribe las tres notas de cada uno, de grave a agudo.',
                         'Rodea el que lleva una tecla negra que no está en la armadura.',
                         'Marca con una cruz los que comparten dos notas con el de al lado.'],
                        titulo='Las siete letras de tu partitura',
                        pista='están impresas encima del pentagrama: F, Dm y B♭ son las que más '
                              'se repiten'),
                verdadero_falso([
                    'El compás se escribe con una C y es 4/4.',
                    'Detrás de la clave hay un sostenido.',
                    'La izquierda toca octavas en los cc. 1-4.',
                    'La partitura trae un número de metrónomo.',
                    'El c. 4 de la derecha acaba en un silencio de blanca.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                figuras([('s', 'semicorchea'), ('e', 'corchea'), ('q.', 'negra con puntillo'),
                         ('h', 'blanca')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='cuatro de las figuras del c. 1 y de los cc. 3-4 de tu partitura'),
                para_clase('El c. 1 con las dos manos y las letras del cifrado sin mirar la '
                           'partitura. Y dime en qué número de la cuenta se te adelantan las '
                           'semicorcheas: ahí es donde lo arreglamos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
