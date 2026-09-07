# -*- coding: utf-8 -*-
"""A comme amour (Richard Clayderman) — pieza 16 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive (musicaparadisfrutar.com,
   1 página, 18 compases; el mismo archivo que piezas de José María y de
   Josep, byte a byte):

     - Un sostenido detrás de la clave y la música descansa en Mi: Mi menor.
     - Cambia de armadura en el compás 10: desaparece el sostenido y la
       pieza sigue en La menor.
     - 4/4, y pone "♩ = 69".
     - Cifrado impreso encima del pentagrama: Em · B7 · E7 · Am · A7 · Dm.
     - La derecha lleva semicorcheas de principio a fin.
     - La izquierda hace acordes de redonda, uno por compás.
     - Hay dos tresillos marcados con el número 3 (cc. 8 y 16).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import escala, cadencia, arpegio, giro, bloque_tresillos, bloques_extra
from nl_comun import n, ac, corch, semi

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
MIm = 'Mi menor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=16, nivel='avanzado', slug='AcommeAmour',
    formato='adulto',
    titulo_corto='A comme amour', time_sig=(4, 4), key_sig=MIm,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source',
                           'Copia de Copia de  A COMME AMOUR _ Richard Clayderman.'),
    yt='https://www.youtube.com/results?search_query=a+comme+amour+clayderman+piano',

    ficha=dict(
        titulo='A comme amour',
        autor='Richard Clayderman · edición de musicaparadisfrutar.com',
        datos=[('Tonalidad', 'Mi m → La m'), ('Compás', '4/4'),
               ('Tempo', '♩ = 69'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Una')],
        titulo_ritmos='Semicorcheas arriba, redonda abajo',
        pie_ritmos='Andamio escrito en corcheas para que se lea. En tu partitura son semicorcheas: '
                   'cuatro por golpe, de principio a fin.',
        armonia=dict(
            titulo='El único cambio de armadura de tu álbum',
            tarjetas=[
                ('CAMBIA LA ARMADURA', 'En el c. 10',
                 'El sostenido desaparece y la pieza sigue en La menor: hasta ahora la armadura era '
                 'la misma de principio a fin en todo lo demás que has tocado.'),
                ('SEMICORCHEAS', 'Sin descanso',
                 'Cuatro notas por golpe desde el compás 1 hasta el final: no hay ni un compás en el '
                 'que la derecha descanse.'),
                ('SEIS ACORDES', 'Impresos',
                 'Em, B7, E7, Am, A7 y Dm: tres de ellos con séptima, cuatro notas cada uno.'),
                ('♩ = 69', 'Lento y difícil',
                 'Que vaya lento no ayuda: da tiempo a oír cada nota, y por eso las cuatro tienen que '
                 'ser iguales.'),
            ],
            pie='Richard Clayderman ha vendido más discos que casi cualquier pianista vivo. Esta '
                'pieza es de 1978 y sigue siendo, en muchos países, la primera pieza "de piano de '
                'verdad" que alguien intenta tocar.',
        ),
        ritmos=[
            ('MANO DERECHA', 'en tu partitura son cuatro por golpe · andamio',
             [n('A4', 'e'), n('D5', 'e'), n('C5', 'e'), n('A4', 'e'),
              n('F4', 'e'), n('A4', 'e'), n('D5', 'e'), n('C5', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'un acorde de redonda por compás · andamio',
             [ac(('E2', 'B2', 'E3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Un sostenido detrás de la clave al empezar: Fa sostenido, Mi menor.',
            'En el compás 10 cambia la armadura: desaparece el sostenido y sigue en La menor.',
            'Pone "♩ = 69".',
            'El cifrado viene impreso: Em, B7, E7, Am, A7 y Dm.',
            'La derecha lleva semicorcheas de principio a fin.',
            'Hay dos tresillos marcados con un 3, en los compases 8 y 16.',
        ],
        reto='El cambio de armadura del compás 10: nueve compases con el Fa sostenido puesto y de '
             'repente deja de estar, con la mano llevando nueve compases de costumbre en contra.',
        truco='Toca los compases 8, 9, 10 y 11 seguidos, solo esos cuatro, veinte veces. El cambio no '
              'se aprende leyendo el aviso, se aprende pasando por él tantas veces que la mano ya no '
              'tiene que decidir.',
        sabias='Aunque casi ningún crítico lo toma en serio, Clayderman ha vendido más discos que '
               'prácticamente cualquier otro pianista de la historia.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que la mano derecha no para nunca y aun así la melodía se oye '
                      'clarísima: son las notas más agudas de cada grupo de cuatro.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Trabaja el cambio de armadura primero: es lo único que no has hecho nunca en tu '
              'repertorio, y es lo que va a fallar si no se estudia por separado.',
        reglas=['EL C. 10 CAMBIA DE ARMADURA', 'CUATRO NOTAS POR GOLPE, IGUALES',
                'LA MELODÍA ES LA NOTA MÁS AGUDA'],
        bloques=[
            dict(num=1, titulo='El cambio de armadura, de frente',
                 pista='cc. 9-11 · el cambio del c. 10 es literal; las notas, andamio',
                 sistemas=[
                     dict(cap='a) con otro dibujo, con el Fa sostenido puesto',
                          events=[n('G4', 'e'), n('B4', 'e'), n('E5', 'e'), n('F#4', 'e'),
                                  n('D4', 'e'), n('G4', 'e'), n('B4', 'e'), n('E5', 'e')],
                          bars=2, key_sig=MIm),
                     dict(cap='b) y AHORA con su figura de verdad, la semicorchea · el mismo dibujo el doble de rápido, tal y como está impreso en tu partitura',
                          events=semi(['G4', 'B4', 'E5', 'F#4']) + semi(['D4', 'G4', 'B4', 'E5']) + [n('G4'), n('B4')],
                          bars=1, show_time=False, key_sig='Mi menor'),
                 ]),
            dict(num=2, titulo='Los seis acordes del cifrado', clef='bass',
                 pista='son los que trae impresos tu partitura · tres llevan séptima',
                 sistemas=[
                     dict(cap='a) B7, E7 y Em en otro orden, con el sostenido puesto',
                          events=[ac(('B1', 'D#2', 'F#2', 'A2'), 'w'),
                                  ac(('E2', 'G#2', 'B2', 'D3'), 'w'),
                                  ac(('E2', 'B2', 'E3'), 'w')],
                          bars=3, clef='bass', key_sig=MIm),
                     dict(cap='b) A7, Dm y Am en otro orden, ya sin armadura',
                          events=[ac(('A2', 'C#3', 'E3', 'G3'), 'w'),
                                  ac(('D2', 'A2', 'D3'), 'w'),
                                  ac(('A2', 'E3', 'A3'), 'w')],
                          bars=3, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='DÓNDE ESTÁ LA MELODÍA',
                 texto='Con cuatro notas por golpe parece que suenan todas igual, y no: la melodía es '
                       'la nota más aguda de cada grupo, y las otras tres son relleno. Toca solo las '
                       'agudas, sin las demás, y verás aparecer la canción.'),
            dict(num=3, titulo='Las dos escalas, una detrás de otra',
                 pista='andamio · primero Mi menor y después La menor, que es el cambio del c. 10',
                 sistemas=[
                     dict(cap='a) Mi menor, con su Fa sostenido · así suenan los nueve primeros '
                              'compases',
                          events=escala('Mi menor', 'B3'), bars=2),
                     dict(cap='b) y La menor, sin ningún sostenido · el oído tiene que notar el '
                              'cambio antes de que lo note la mano',
                          events=escala('La menor', 'A4'), bars=2, show_time=False),
                 ]),
            dict(num=4, titulo='Las dos manos, con la melodía marcada',
                 pista='andamio · a la mitad de 69, y con la nota aguda un poco más fuerte',
                 sistemas=[
                     dict(cap='a) el acorde abajo y los grupos arriba, con otro dibujo',
                          events=[ac(('E2', 'G4'), 'e'), n('B4', 'e'), n('E5', 'e'), n('F#4', 'e'),
                                  n('D4', 'e'), n('G4', 'e'), n('B4', 'e'), n('E5', 'e')],
                          bars=2, key_sig=MIm),
                     dict(cap='b) y en la segunda mitad, sin armadura',
                          events=[ac(('A2', 'G4'), 'e'), n('C5', 'e'), n('E5', 'e'), n('F4', 'e'),
                                  n('D4', 'e'), n('G4', 'e'), n('C5', 'e'), n('E5', 'e')],
                          bars=2, show_time=False),
                 ]),
            dict(num=5, titulo='Los acordes del tono nuevo',
                 pista='andamio en La menor · la armonía a partir del compás 10',
                 sistemas=[
                     dict(cap='a) i - iv - v - i en La menor · ni un sostenido: si te sale el Fa '
                              'negro, sigues en el tono de antes',
                          events=cadencia('La menor', 'A2'), bars=4, clef='bass'),
                 ]),
            dict(num=6, titulo='Los dos acordes, uno al lado del otro',
                 pista='andamio · el de antes del compás 10 y el de después, para oír la distancia',
                 sistemas=[
                     dict(cap='a) el acorde de Mi menor desplegado · con Fa sostenido dentro',
                          events=arpegio('Mi menor', 'B3'), bars=2),
                     dict(cap='b) y el de La menor · sin ningún sostenido, y se nota',
                          events=arpegio('La menor', 'A4'), bars=2, show_time=False),
                 ]),
        ],
    ),
)

# El recurso que la pieza EXPLICA y no dibujaba: durante meses se anotó como
# "no cabe en la hoja". Desde que la hoja se pagina sola, esa excusa dejó de
# ser cierta.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Mi menor', 62, 'E4', 'E2',
    'la mano en Mi menor antes de contar los tresillos',
    desde=8, time_sig=(4, 4))[:1] + [
    bloque_tresillos('Mi menor', 7, 'E4', 'los tresillos, que salen tras el cambio de armadura', time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
