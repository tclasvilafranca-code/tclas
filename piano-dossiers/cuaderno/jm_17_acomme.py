# -*- coding: utf-8 -*-
"""A comme amour — pieza 17 de José María. Formato ADULTO. RETO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Richard Clayderman,
   musicaparadisfrutar.com, 1 página):

     - UN SOSTENIDO detrás de la clave y el cifrado empieza en Em: es MI
       MENOR. Todos los Fa van a la tecla negra.
     - Compás de 4/4 y ♩ = 69 impreso.
     - La derecha EMPIEZA CON SILENCIOS (un silencio de blanca y uno de negra)
       y entra al final del primer compás.
     - LO DIFÍCIL: la melodía va en SEMICORCHEAS seguidas, cuatro notas por
       golpe, casi de principio a fin. Es la única pieza del cuaderno que las
       lleva de forma sostenida.
     - El cifrado viene impreso encima: Em, B7…
     - Y CAMBIA DE ARMADURA en el c. 10: doble barra y un becuadro que
       quita el Fa sostenido. De ahi en adelante no hay armadura: pasa de
       Mi menor a La menor. Lo tenian los dosieres de Josep y de Nel, que
       tocan este mismo PDF, y este no lo decia: el alumno llegaba al c. 10
       y se encontraba el Fa natural sin que nadie se lo hubiera avisado.

   Por qué está en el bloque de los retos: por las semicorcheas. A ♩=69 no son
   rápidas de reloj, pero son cuatro notas por golpe y eso exige una igualdad
   de dedos que no se ha pedido en ninguna pieza anterior.

   Lo que NO se cita nota a nota: el material va como ANDAMIO en Mi menor y
   remite a la partitura.

   LA SEMICORCHEA SE ESCRIBE. Esta hoja decia que "las semicorcheas NO se
   dibujan (el motor escribe hasta corchea)". Eso era verdad antes de que el
   motor supiera dibujarlas, y dejo de serlo hace tiempo: la pieza esta en el
   bloque de los retos PRECISAMENTE por las semicorcheas, y el alumno no las
   veia ni una vez en su cuaderno. Medido sobre el PDF: 45 pares de barras
   dobles. El trabajo por grupos de cuatro sigue escrito en corcheas, que es
   como se estudia un pasaje rapido, pero ahora hay un sistema con la figura
   de verdad para que sepa lo que va a leer.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jm_comun import (n, ac, sil, corch, semi, objetivo, plan, diferencias, figuras,
                      acuerdate, cifrado, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
MIM = 'Mi menor'

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=17, nivel='iniciación',
    slug='AcommeAmour', formato='adulto',
    titulo_corto='A comme amour', time_sig=(4, 4), key_sig=MIM,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           'A COMME AMOUR _ Richard Clayderman.'),
    yt='https://www.youtube.com/results?search_query=a+comme+amour+clayderman+piano',

    ficha=dict(
        titulo='A comme amour',
        autor='Richard Clayderman · musicaparadisfrutar.com',
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 69'), ('Novedad', 'Semicorcheas'),
               ('Empieza', 'Con silencio')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Mi menor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Las semicorcheas no se pueden escribir en estas hojas; aquí van en corcheas '
                   'y se tocan al doble de lento, que es como hay que estudiarlas.',
        armonia=dict(
            titulo='Cuatro notas por golpe: eso es todo el reto',
            tarjetas=[
                ('LA NOVEDAD', 'Semicorcheas',
                 'Cuatro notas en el tiempo de un golpe. Hasta ahora lo máximo eran dos. Es la única '
                 'pieza del cuaderno que las lleva seguidas.'),
                ('EL TEMPO', '♩ = 69',
                 'Lento de reloj. Pero con cuatro notas por golpe, el dedo se mueve al mismo ritmo que '
                 'en una pieza de 138 con corcheas.'),
                ('LA IGUALDAD', 'Lo que se juzga',
                 'Con cuatro notas por golpe se oye enseguida si una es más larga o más fuerte que las '
                 'otras. Ese es el trabajo, no las notas.'),
                ('LA ENTRADA', 'Al final del c. 1',
                 'Silencio de blanca y de negra, y entras en el último golpe del primer compás.'),
            ],
            pie='La forma de estudiar semicorcheas es la misma desde hace trescientos años: tocarlas '
                'al doble de lento, en grupos de cuatro, y solo subir cuando las cuatro suenan '
                'exactamente iguales. No hay atajo, y tampoco hace falta: funciona.',
        ),
        ritmos=[
            ('MANO DERECHA', 'las rápidas, escritas al doble de lento',
             corch(['B4', 'A4']) + corch(['G4', 'F#4']) + corch(['E4', 'F#4']) +
             corch(['G4', 'B4']), OCRE, 'treble', MIM),
            ('MANO IZQUIERDA', 'notas largas, sostiene y ya está · andamio',
             [ac(('E2', 'B2'), 'w')], AZUL, 'bass', MIM),
        ],
        especial=[
            'Hay UN sostenido detrás de la clave, y la pieza está en Mi menor.',
            'Pone ♩ = 69: es lenta de reloj.',
            'La melodía va en semicorcheas: cuatro notas en cada golpe.',
            'La derecha entra en el último golpe del primer compás, después de dos silencios.',
            'El cifrado viene impreso encima: Em, B7…',
            'En el c. 10 CAMBIA DE ARMADURA: doble barra y un becuadro que quita el Fa sostenido, '
            'y la pieza pasa de Mi menor a La menor. Márcalo con lápiz antes de estudiar nada.',
            'La mano izquierda toca notas largas y no estorba: todo el trabajo es de la derecha.',
        ],
        reto='Que las cuatro notas de cada golpe suenen exactamente iguales. En cuanto una se alarga o '
             'se acentúa, el grupo entero deja de sonar a Clayderman y suena a ejercicio de dedos.',
        truco='Tócalas en grupos de cuatro y PARA después de cada grupo, con la mano relajada. Cuando '
              'los grupos sueltos salgan iguales, únelos de dos en dos, luego de cuatro en cuatro. No '
              'toques la frase entera hasta que los grupos estén: si lo haces, lo que aprendes es a '
              'tocarla desigual.',
        sabias='Clayderman ha vendido más discos de piano que nadie en la historia y en Francia lo '
               'detestan los críticos desde hace cincuenta años. "A comme amour" es de 1977 y se sigue '
               'usando en las escuelas de piano de medio mundo, precisamente porque suena a mucho más '
               'difícil de lo que es.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que las notas rápidas suenan como un chorro continuo, sin bultos. Esa '
                      'igualdad es todo el trabajo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Todo lo de esta semana va de una sola cosa: que cuatro notas seguidas suenen iguales. '
              'Los ejercicios están escritos en corcheas a propósito, al doble de lento, que es como '
              'se estudia un pasaje rápido. El último los pone con su figura de verdad.',
        reglas=['EN GRUPOS DE CUATRO, Y PARANDO', 'TODAS IGUALES: NI MÁS LARGA NI MÁS FUERTE',
                'LA IZQUIERDA NO ESTORBA'],
        bloques=[
            dict(num=1, titulo='Grupos de cuatro, parando entre uno y otro',
                 pista='andamio en Mi menor · escrito al doble de lento a propósito',
                 sistemas=[
                     dict(cap='a) cuatro notas, y para · la mano se queda floja mientras esperas',
                          events=corch(['E4', 'F#4']) + corch(['G4', 'A4']) + [sil('h')] +
                                 corch(['B4', 'A4']) + corch(['G4', 'F#4']) + [sil('h')],
                          bars=2, key_sig=MIM),
                     dict(cap='b) y ahora dos grupos seguidos, sin parar en medio',
                          events=corch(['E4', 'F#4']) + corch(['G4', 'A4']) +
                                 corch(['B4', 'A4']) + corch(['G4', 'F#4']),
                          bars=1, key_sig=MIM, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE PARA ENTRE GRUPO Y GRUPO',
                 texto='Parando obligas a la mano a soltarse cuatro veces por compás, y una mano que se '
                       'suelta no se agarrota. Si tocas la frase entera de seguido desde el primer día, '
                       'la tensión se va acumulando y a los ocho compases los dedos ya no obedecen. No '
                       'es cuestión de fuerza: es que un músculo que no descansa deja de responder. Los '
                       'grupos de cuatro con parada son el descanso.'),
            dict(num=2, titulo='La igualdad: el mismo grupo, muchas veces',
                 pista='andamio · lo que se juzga es que las cuatro suenen igual, no que vayan rápido',
                 sistemas=[
                     dict(cap='a) el mismo grupo cuatro veces · si una nota se te escapa más fuerte, '
                              'empieza otra vez',
                          events=corch(['E4', 'F#4']) + corch(['G4', 'A4']) +
                                 corch(['E4', 'F#4']) + corch(['G4', 'A4']) +
                                 corch(['E4', 'F#4']) + corch(['G4', 'A4']) +
                                 corch(['E4', 'F#4']) + corch(['G4', 'A4']),
                          bars=2, key_sig=MIM),
                     dict(cap='b) y AHORA con la figura que vas a leer de verdad: la semicorchea · '
                              'cuatro por golpe, que es como está impresa toda tu partitura',
                          events=semi(['E4', 'F#4', 'G4', 'A4']) + semi(['B4', 'A4', 'G4', 'F#4']) +
                                 [n('E4'), n('B4')],
                          bars=1, key_sig=MIM, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda, y la entrada del principio', clef='bass',
                 pista='andamio en Mi menor · la izquierda sostiene y no hace nada más',
                 sistemas=[
                     dict(cap='a) notas largas, una por compás · toca y deja sonar',
                          events=[ac(('E2', 'B2'), 'w'), ac(('B2', 'F#3'), 'w'),
                                  ac(('E2', 'B2'), 'w'), ac(('A2', 'E3'), 'w')],
                          bars=4, clef='bass', key_sig=MIM),
                     dict(cap='b) y la entrada de la derecha (andamio) · dos silencios y entras en el '
                              'último golpe',
                          events=[sil('h'), sil('q')] + corch(['E4', 'F#4']),
                          bars=1, key_sig=MIM, show_time=False),
                     dict(cap='c) la entrada seguida del primer grupo · así se practica junto lo que '
                              'de verdad va junto',
                          events=[sil('h'), sil('q')] + corch(['E4', 'F#4']) +
                                 corch(['G4', 'A4']) + corch(['B4', 'A4']) +
                                 corch(['G4', 'F#4']) + [n('E4')],
                          bars=2, key_sig=MIM, show_time=False),
                 ]),
            # Al escribir la semicorchea la hoja pasa a dos, y la segunda hay
            # que llenarla: tecnica de Mi menor, que es la tonalidad de la pieza.
        ] + bloques_extra('Mi menor', 17, 'E4', 'E2',
                          'cuatro notas por golpe, y todas del mismo peso',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='A comme amour · para casa',
            intro='Veinte minutos al día. Esta semana no se toca la pieza entera ni una vez.',
            bloques=[
                objetivo('Que un grupo de cuatro notas suene con las cuatro exactamente iguales, diez '
                         'veces seguidas. Nada más, y no es poco.'),
                plan((6, 'Grupos de cuatro, parando entre uno y otro'),
                     (6, 'El mismo grupo cuatro veces, buscando la igualdad'),
                     (4, 'Dos grupos seguidos, sin parar en medio'),
                     (4, 'La izquierda sola, y la entrada del primer compás')),
                diferencias(
                    corch(['E4', 'F#4']) + corch(['G4', 'A4']) + corch(['B4', 'A4']),
                    corch(['E4', 'F#4']) + corch(['G4', 'B4']) + corch(['B4', 'G4']),
                    cuantas=2,
                    titulo='Busca las dos diferencias',
                    pista='andamio · arriba el dibujo bueno, abajo con dos cambios'),
                figuras([('e', 'corchea'), ('q', 'negra'), ('h', 'blanca'), ('w', 'redonda')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='la semicorchea, que es la de esta pieza, vale la mitad que la corchea'),
                cifrado(['Em', 'B7', 'E7', 'Am', 'A7', 'Dm'],
                        ['Escribe las notas de cada uno, de grave a agudo.',
                         'Tres llevan un 7 y por tanto cuatro notas: tienes una casilla de más.'],
                        filas=4, alto_caja=12.0,
                        pista='son los seis que tu partitura lleva impresos encima del pentagrama'),
                para_clase('Un grupo de cuatro con las cuatro notas iguales, y los acordes '
                           'escritos. Si al unir dos grupos se te desiguala el segundo, tráelo así: '
                           'es justo lo que hay que mirar juntos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
