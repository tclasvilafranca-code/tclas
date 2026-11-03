# -*- coding: utf-8 -*-
"""A comme amour (Richard Clayderman) — pieza 19 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (musicaparadisfrutar.com,
   1 página, 18 compases):

     - UN SOSTENIDO detrás de la clave y la música descansa en Mi: Mi menor.
     - **CAMBIA DE ARMADURA en el compás 10**: desaparece el sostenido y la
       pieza sigue en La menor. Es el único cambio de armadura del cuaderno.
     - 4/4, y pone "♩ = 69".
     - CIFRADO IMPRESO encima del pentagrama: Em · B7 · E7 · Am · A7 · Dm.
     - La derecha lleva SEMICORCHEAS de principio a fin.
     - La izquierda hace acordes de redonda, uno por compás.
     - Hay dos tresillos marcados con el número 3 (cc. 8 y 16).

   El archivo es EL MISMO que el de José María (md5 idéntico). Allí era la
   pieza 17 y el trabajo iba por los grupos de cuatro; aquí es la última del
   curso y va por el CIFRADO y por el cambio de armadura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra, bloque_tresillos
from jp_comun import (n, ac, semi, reto, plan, cifrado, verdadero_falso, figuras,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=19, nivel='intermedio', slug='AcommeAmour',
    formato='adulto',
    titulo_corto='A comme amour', time_sig=(4, 4), key_sig='Mi menor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'A COMME AMOUR _ Richard Clayderman.'),
    yt='https://www.youtube.com/results?search_query=a+comme+amour+clayderman+piano',

    ficha=dict(
        titulo='A comme amour',
        autor='Richard Clayderman · edición de musicaparadisfrutar.com',
        datos=[('Tonalidad', 'Mi m → La m'), ('Compás', '4/4'),
               ('Tempo', '♩ = 69'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Una')],
        titulo_ritmos='Semicorcheas arriba, redonda abajo',
        pie_ritmos='Andamio escrito en corcheas para que se lea. En tu partitura son SEMICORCHEAS: '
                   'cuatro por golpe, de principio a fin.',
        armonia=dict(
            titulo='La última del curso, y por qué',
            tarjetas=[
                ('CAMBIA LA ARMADURA', 'En el c. 10',
                 'El sostenido desaparece y la pieza sigue en La menor. Es lo único parecido en '
                 'todo el cuaderno: hasta ahora la armadura era la misma de principio a fin.'),
                ('SEMICORCHEAS', 'Sin descanso',
                 'Cuatro notas por golpe desde el compás 1 hasta el final. No hay ni un compás en '
                 'el que la derecha descanse.'),
                ('SEIS ACORDES', 'Impresos',
                 'Em, B7, E7, Am, A7 y Dm. Tres de ellos con séptima, que a estas alturas del curso '
                 'ya sabes qué quiere decir.'),
                ('♩ = 69', 'Lento, y difícil',
                 'Es de las piezas más lentas del cuaderno y de las más difíciles. Que vaya lento '
                 'no ayuda: da tiempo a oír cada nota, y por eso las cuatro tienen que ser iguales.'),
            ],
            pie='Es la última del curso porque junta todo lo demás: cifrado con séptimas, tono '
                'menor, cambio de armadura y cuatro notas por golpe. Ninguna de esas cosas es nueva '
                'a estas alturas; lo nuevo es tenerlas todas a la vez.',
        ),
        ritmos=[
            # Notas distintas de las del ejercicio: la ficha ENSEÑA el dibujo y
            # la hoja al piano lo TRABAJA. Con las mismas ocho notas, el
            # cuaderno repetía hoja sin que se notara al maquetar.
            ('MANO DERECHA', 'en tu partitura son cuatro por golpe · andamio',
             [n('E5', 'e'), n('D5', 'e'), n('B4', 'e'), n('G4', 'e'),
              n('A4', 'e'), n('B4', 'e'), n('D5', 'e'), n('B4', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'un acorde de redonda por compás · andamio',
             [ac(('E2', 'B2', 'E3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Un sostenido detrás de la clave al empezar: Fa sostenido, Mi menor.',
            'En el compás 10 CAMBIA la armadura: desaparece el sostenido y sigue en La menor.',
            'Pone "♩ = 69".',
            'El cifrado viene impreso: Em, B7, E7, Am, A7 y Dm.',
            'La derecha lleva semicorcheas de principio a fin.',
            'Hay dos tresillos marcados con un 3, en los compases 8 y 16.',
        ],
        reto='El cambio de armadura del compás 10. Llevas nueve compases con el Fa sostenido puesto '
             'y de repente deja de estar, y la mano tiene nueve compases de costumbre en contra.',
        truco='Toca los compases 8, 9, 10 y 11 seguidos, solo esos cuatro, veinte veces. El cambio '
              'no se aprende leyendo el aviso: se aprende pasando por él tantas veces que la mano '
              'ya no tiene que decidir. Y marca el compás 10 con un círculo grande a lápiz.',
        sabias='Richard Clayderman ha vendido más discos que casi cualquier pianista vivo y casi '
               'ningún crítico lo toma en serio. "A comme amour" es de 1978 y sigue siendo, en '
               'muchos países, la primera pieza "de piano de verdad" que alguien intenta tocar.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que la mano derecha no para nunca y aun así la melodía se oye '
                      'clarísima. Esa melodía son las notas más agudas de cada grupo de cuatro.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La última del curso, y la que junta todo. Trabaja el cambio de armadura primero: es '
              'lo único que no has hecho nunca, y es lo que va a fallar.',
        reglas=['EL C. 10 CAMBIA DE ARMADURA', 'CUATRO NOTAS POR GOLPE, IGUALES',
                'LA MELODÍA ES LA NOTA MÁS AGUDA'],
        bloques=[
            dict(num=1, titulo='El cambio de armadura, de frente',
                 pista='cc. 9-11 · el cambio del c. 10 es literal; las notas, andamio',
                 sistemas=[
                     dict(cap='a) con el Fa sostenido puesto, como los nueve primeros compases',
                          events=[n('E4', 'e'), n('G4', 'e'), n('B4', 'e'), n('F#4', 'e'),
                                  n('G4', 'e'), n('B4', 'e'), n('E5', 'e'), n('B4', 'e')],
                          bars=2, key_sig='Mi menor'),
                     dict(cap='b) y AHORA con su figura de verdad, la semicorchea · el mismo dibujo el doble de rápido, tal y como está impreso en tu partitura',
                          events=semi(['E4', 'G4', 'B4', 'F#4']) + semi(['G4', 'B4', 'E5', 'B4']) + [n('E4'), n('G4')],
                          bars=1, show_time=False, key_sig='Mi menor'),
                 ]),
            dict(num=2, titulo='Los seis acordes del cifrado', clef='bass',
                 pista='son los que trae impresos tu partitura · tres llevan séptima',
                 sistemas=[
                     dict(cap='a) Em, B7 y E7 · los de la primera mitad, con el sostenido puesto',
                          events=[ac(('E2', 'B2', 'E3'), 'w'),
                                  ac(('B1', 'D#2', 'F#2', 'A2'), 'w'),
                                  ac(('E2', 'G#2', 'B2', 'D3'), 'w')],
                          bars=3, clef='bass', key_sig='Mi menor'),
                     dict(cap='b) Am, A7 y Dm · los de la segunda mitad, ya sin armadura',
                          events=[ac(('A2', 'E3', 'A3'), 'w'),
                                  ac(('A2', 'C#3', 'E3', 'G3'), 'w'),
                                  ac(('D2', 'A2', 'D3'), 'w')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='DÓNDE ESTÁ LA MELODÍA',
                 texto='Con cuatro notas por golpe parece que suenan todas igual, y no: la melodía '
                       'es la nota más aguda de cada grupo, y las otras tres son relleno. Toca solo '
                       'las agudas, sin las demás, y verás aparecer la canción. Después vuelve a '
                       'meterlas: ya sabes cuál de las cuatro tiene que oírse.'),
            dict(num=3, titulo='Las dos manos, con la melodía marcada',
                 pista='andamio · a la mitad de 69, y con la nota aguda un poco más fuerte',
                 sistemas=[
                     dict(cap='a) el acorde abajo y los grupos arriba · la aguda de cada grupo pesa, '
                              'las otras tres no',
                          events=[ac(('E2', 'B4'), 'e'), n('E5', 'e'), n('D5', 'e'), n('B4', 'e'),
                                  n('G4', 'e'), n('B4', 'e'), n('E5', 'e'), n('D5', 'e')],
                          bars=2, key_sig='Mi menor'),
                     dict(cap='b) y en la segunda mitad, sin armadura · el mismo trabajo con las '
                              'teclas cambiadas',
                          events=[ac(('A2', 'A4'), 'e'), n('E5', 'e'), n('C5', 'e'), n('A4', 'e'),
                                  n('F4', 'e'), n('A4', 'e'), n('E5', 'e'), n('C5', 'e')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Mi menor', 26, 'E4', 'E2',
                          'el cambio de armadura del compás 10, oído antes que tocado',
                          desde=4, time_sig=(4, 4))[:1],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='A comme amour · para casa',
            intro='La última del curso. Veinte minutos, y el primero para marcar el compás 10.',
            bloques=[
                reto('Pasar del compás 9 al 10 sin tocar ni un Fa sostenido de más.',
                     'Toca solo los compases 8 al 11, veinte veces seguidas. El cambio no se '
                     'aprende leyendo el aviso: se aprende pasando por él tantas veces que la mano '
                     'ya no tenga que decidir. Y marca el compás 10 con un círculo grande.'),
                plan((5, 'Los compases 8 al 11, con el cambio de armadura'),
                     (5, 'Solo las notas agudas de cada grupo: la melodía sola'),
                     (5, 'Los grupos de cuatro completos, con la aguda marcada'),
                     (5, 'Las dos manos, a la mitad de velocidad')),
                cifrado(['Em', 'B7', 'E7', 'Am', 'A7', 'Dm'],
                        ['Escribe las notas de cada uno, de grave a agudo.',
                         'Tres llevan séptima y por tanto cuatro notas: tienes una casilla de más.'],
                        filas=4, alto_caja=12.0,
                        pista='son los seis que trae impresos tu partitura'),
                verdadero_falso([
                    'La armadura de esta pieza cambia a mitad de camino.',
                    'A partir del compás 10 el Fa es tecla blanca.',
                    'La melodía es la nota más grave de cada grupo de cuatro.',
                    'Un acorde con 7 tiene cuatro notas.',
                    'Que la pieza vaya lenta la hace más fácil.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas'),
                figuras([('w', 'redonda'), ('h', 'blanca'), ('q', 'negra'), ('e', 'corchea')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='y una más para pensar: ¿cuánto dura una semicorchea?'),
                para_clase('Los compases 8 al 11 con el cambio de armadura, y los seis acordes '
                           'escritos. Con esto se acaba el curso: trae también cuál de las '
                           'diecinueve quieres tocar en la audición.'),
            ],
        ),
    ],
)

# El recurso que la pieza EXPLICA y no dibujaba: durante meses se anotó como
# "no cabe en la hoja". Desde que la hoja se pagina sola, esa excusa dejó de
# ser cierta.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + [
    bloque_tresillos('Mi menor', 6, 'E4', 'los tresillos, que salen tras el cambio de armadura', time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
