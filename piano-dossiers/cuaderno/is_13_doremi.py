# -*- coding: utf-8 -*-
"""Do Re Mi, de Sonrisas y Lágrimas — pieza 13 de Isaac.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Do Re Mi", Richard
   Rodgers, arr. A. C. Escobés, 1 página; el mismo archivo que la pieza 7 de
   Mercè, byte a byte):

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4, y arriba pone "Andantino".
     - La derecha combina el dibujo largo-corto (negra con puntillo y
       corchea) con una carrerilla de cuatro corcheas seguidas.
     - La izquierda hace un patrón que alterna una nota grave y otra más
       aguda, en negras, como un bajo que camina.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra, bloque_puntillo
from is_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Isaac', carpeta='Isaac', num=13, nivel='intermedio', slug='DoReMi',
    formato='adulto',
    titulo_corto='Do Re Mi', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'isaac', 'source', 'Sonrisas y Lagrimas.pdf'),
    yt='https://www.youtube.com/results?search_query=do+re+mi+sound+of+music+easy+piano',

    ficha=dict(
        titulo='Do Re Mi',
        autor='Richard Rodgers · de Sonrisas y Lágrimas · arr. A. C. Escobés',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Andantino'), ('Izquierda', 'Bajo que camina'),
               ('Derecha', 'Largo-corto')],
        titulo_ritmos='El bajo que camina, y el ritmo largo-corto',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la izquierda alterna grave y '
                   'agudo en negras, y la derecha combina el largo-corto con una carrerilla.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('EL BAJO CAMINA', 'Grave y agudo',
                 'La izquierda no se queda quieta ni sostiene: se mueve todo el rato entre una nota '
                 'baja y otra más alta, como pasos.'),
                ('LARGO-CORTO', 'Puntillo y corchea',
                 'La melodía respira con ese dibujo: una nota que dura más y otra que dura menos.'),
                ('UNA CARRERILLA', 'Cuatro corcheas',
                 'En algún punto de la frase la melodía se mueve más rápido, cuatro notas iguales '
                 'antes de volver a respirar.'),
                ('MELODÍA CONOCIDA', 'Se afina con el oído',
                 'Conocer la canción ayuda a detectar un error antes de que la vista lo vea.'),
            ],
            pie='Es la canción con la que Julie Andrews enseña las notas a los niños en la película. '
                'No es casualidad que sea también una buena pieza para aprender ritmo.',
        ),
        ritmos=[
            ('MANO DERECHA', 'largo-corto y una carrerilla de corcheas · andamio',
             [n('D4', 'q.'), n('E4', 'e')] + corch(['F4', 'G4', 'A4', 'F4']),
             OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'grave, agudo, grave, agudo · andamio',
             [n('C3'), n('G3'), n('C3'), n('G3')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4, con "Andantino" escrito arriba.',
            'La izquierda alterna una nota grave y otra más aguda, en negras.',
            'La derecha combina negra con puntillo y corchea con una carrerilla de cuatro corcheas.',
            'La carrerilla siempre resuelve en una nota que respira antes de la siguiente frase.',
            'Es una melodía muy conocida, así que el oído ayuda mucho a corregir errores.',
        ],
        reto='Que la carrerilla de corcheas no se acelere respecto al resto de la frase.',
        truco='Toca solo la carrerilla de cuatro corcheas contando "un-y-dos-y" en voz alta y '
              'parando justo después.',
        sabias='Rodgers y Hammerstein escribieron la canción para explicar el solfeo con una '
               'historia: cada nota de la escala tiene una palabra asociada.',
        qr=dict(titulo='Escúchala',
                texto='Sigue con el dedo cada nota de la escala mientras suena la canción.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda camina y la derecha respira en largo-corto. Se aprenden por separado y '
              'la carrerilla se aísla antes de nada.',
        reglas=['LA IZQUIERDA CAMINA, GRAVE-AGUDO', 'LA CARRERILLA SE AÍSLA Y SE CUENTA',
                'ANDANTINO: A PASO TRANQUILO'],
        bloques=[
            dict(num=1, titulo='La izquierda: el bajo que camina',
                 pista='andamio en Do mayor · otro par de acordes',
                 sistemas=[
                     dict(cap='a) grave, agudo, grave, agudo, empezando distinto',
                          events=[n('D3'), n('A3'), n('D3'), n('A3'),
                                  n('E3'), n('B3'), n('E3'), n('B3')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de acorde cada compás',
                          events=[n('A2'), n('E3'), n('A2'), n('E3'),
                                  n('D3'), n('A3'), n('D3'), n('A3')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: largo-corto y la carrerilla',
                 pista='andamio · aísla la carrerilla y cuenta antes de tocarla entera',
                 sistemas=[
                     dict(cap='a) largo-corto, con la carrerilla bajando',
                          events=[n('G4', 'q.'), n('F4', 'e')] + corch(['E4', 'D4', 'C4', 'E4']),
                          bars=1),
                     dict(cap='b) el mismo dibujo, una frase más arriba',
                          events=[n('B4', 'q.'), n('A4', 'e')] + corch(['G4', 'F4', 'E4', 'G4']),
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE AÍSLA LA CARRERILLA',
                 texto='Cuatro corcheas seguidas, tocadas sueltas del resto de la frase, son fáciles '
                       'de acelerar sin darse cuenta porque no hay nada alrededor que marque el '
                       'pulso.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · el bajo no cambia su paso cuando llega la carrerilla · despacio',
                 sistemas=[
                     dict(cap='a) el bajo camina bajo el largo-corto y la carrerilla',
                          events=[ac(('D3', 'G4'), 'q.'), n('F4', 'e')]
                                 + [ac(('A3', 'E4'), 'e'), n('D4', 'e'), ac(('D3', 'C4'), 'e'), n('E4', 'e')],
                          bars=1),
                     dict(cap='b) y con la frase que baja',
                          events=[ac(('E3', 'B4'), 'q.'), n('A4', 'e')]
                                 + [ac(('B3', 'G4'), 'e'), n('F4', 'e'), ac(('E3', 'E4'), 'e'), n('G4', 'e')],
                          bars=1, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 64, 'C4', 'C3',
                          'la escala ES la canción, así que aquí se estudia doble',
                          desde=4, time_sig=(4, 4))[:1],
    ),
)

# El ritmo con puntillo que esta pieza EXPLICA en su texto y no dibujaba en
# ningún sitio. Lo destapó el auditor de vocabulario al ganar la entrada de
# esta figura, que antes no miraba nadie.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + [
    bloque_puntillo('Do mayor', 6, 'C4', 'el puntillo que lleva la melodía',
                    time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
