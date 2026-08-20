# -*- coding: utf-8 -*-
"""Chim Chim Cher-ee (Mary Poppins) — pieza 16 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive (Richard M. Sherman, arr.
   A. C. Escobés, 1 página), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: La menor. Los sostenidos van escritos
       delante de la nota, y casi todos caen en la mano izquierda.
     - 3/4, "Allegro" y "mp".
     - La derecha empieza con SILENCIO DE NEGRA en el primer tiempo y luego
       DOS NOTAS A LA VEZ, dos veces: negra doble, negra doble.
     - La izquierda hace UNA BLANCA CON PUNTILLO por compás: el compás entero
       de una sola nota.

   Lo nuevo: tocar dos teclas a la vez con la mano derecha, y empezar en el
   segundo tiempo en vez de en el primero.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import sistemas_extra
from lu_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=16, nivel='iniciación', slug='ChimChimCheree',
    formato='adulto',
    titulo_corto='Chim Chim Cher-ee', time_sig=(3, 4), key_sig='La menor',
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source', 'Mary Popins FACIL.pdf'),
    yt='https://www.youtube.com/results?search_query=chim+chim+cheree+easy+piano',

    ficha=dict(
        titulo='Chim Chim Cher-ee',
        autor='Richard M. Sherman · de Mary Poppins · arr. A. C. Escobés',
        datos=[('Tonalidad', 'La menor'), ('Compás', '3/4'),
               ('Carácter', 'Allegro'), ('Derecha', 'Dos notas'),
               ('Empieza', 'En el dos')],
        titulo_ritmos='Dos teclas a la vez, y el uno callado',
        pie_ritmos='Andamio en La menor. Lo literal es el reparto: silencio en el primer tiempo, dos '
                   'notas juntas en el dos y en el tres, y la izquierda con el compás entero.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('DOS TECLAS A LA VEZ', 'Con la derecha',
                 'Es la primera vez que la mano derecha toca dos notas al mismo tiempo. Los dos '
                 'dedos tienen que bajar juntos, y eso no sale solo: hay que mirarlo.'),
                ('EL UNO ESTÁ CALLADO', 'Silencio de negra',
                 'La derecha no toca en el primer tiempo de cada compás. Y aun así el uno existe: '
                 'lo marca la izquierda y hay que contarlo.'),
                ('LA IZQUIERDA AGUANTA', 'Compás entero',
                 'Una sola nota por compás, de tres tiempos. Es la mano fácil, y es la que lleva la '
                 'cuenta mientras la derecha calla.'),
                ('TECLAS NEGRAS ABAJO', 'Escritas',
                 'Los sostenidos de esta pieza están casi todos en la mano izquierda, escritos '
                 'delante de la nota. Valen para su compás.'),
            ],
            pie='Es un vals rápido y con gracia. Allegro no quiere decir corriendo: quiere decir '
                'alegre. Si suena pesado, es que va demasiado lento, no demasiado rápido.',
        ),
        ritmos=[
            ('MANO DERECHA', 'silencio y dos notas juntas · literal',
             [sil('q'), ac(('A4', 'C5')), ac(('A4', 'C5'))], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una nota, el compás entero · literal',
             [n('A2', 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada; los sostenidos van escritos dentro.',
            'La tonalidad es La menor.',
            'Compás de 3/4, "Allegro" y "mp".',
            'La derecha no toca en el primer tiempo: hay un silencio de negra.',
            'La derecha toca dos notas a la vez, en el dos y en el tres.',
            'La izquierda hace una sola nota por compás y la aguanta entera.',
        ],
        reto='Que las dos notas de la derecha suenen a la vez. Si un dedo llega un poco antes se oye '
             'un ruidito doble, y se nota mucho más de lo que parece.',
        truco='Pon los dos dedos encima de sus teclas y bájalos con el brazo, no con los dedos. '
              'Piensa en dejar caer la mano entera. Hazlo cinco veces seguidas mirando las teclas y '
              'escuchando si suena un golpe o dos.',
        sabias='Los hermanos Sherman escribieron la canción del deshollinador después de leer que en '
               'Inglaterra tocar a uno da buena suerte. Ganó el Óscar a la mejor canción en 1965.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que la melodía nunca empieza en el golpe fuerte. Ese hueco al '
                      'principio de cada compás es lo que le da el aire de vals.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo son dos dedos que bajan a la vez. Primero el gesto, después el silencio '
              'del uno, y al final la izquierda.',
        reglas=['LOS DOS DEDOS BAJAN JUNTOS', 'EL UNO SE CUENTA AUNQUE NO SUENE',
                'ALLEGRO ES ALEGRE, NO CORRIENDO'],
        bloques=[
            dict(num=1, titulo='Dos notas a la vez, sin prisa',
                 pista='andamio en La menor · lo que se practica es el gesto, no la melodía',
                 sistemas=[
                     dict(cap='a) baja la mano entera, no los dedos · escucha si suena un golpe o dos',
                          events=[ac(('A4', 'C5'), 'h.'), ac(('B4', 'D5'), 'h.')],
                          matiz='mp',
                          bars=2),
                     dict(cap='b) y ahora en negras, cambiando de sitio · si suena doble, vuelve a '
                              'las notas largas',
                          events=[ac(('C5', 'E5')), ac(('B4', 'D5')), ac(('A4', 'C5')),
                                  ac(('G4', 'B4')), ac(('A4', 'C5')), ac(('B4', 'D5'))],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='El primer tiempo callado',
                 pista='andamio · el silencio de negra es el de tu partitura',
                 sistemas=[
                     dict(cap='a) callas en el uno y tocas en el dos y en el tres · cuenta el uno '
                              'en voz alta',
                          events=[sil('q'), ac(('A4', 'C5')), ac(('A4', 'C5')),
                                  sil('q'), ac(('B4', 'D5')), ac(('B4', 'D5'))],
                          bars=2),
                     dict(cap='b) y con la melodía en notas sueltas, que también aparece · el uno '
                              'sigue callado',
                          events=[sil('q'), n('E5'), n('D5'), sil('q'), n('C5'), n('B4')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE CUENTA UN TIEMPO QUE NO SUENA',
                 texto='El primer tiempo de la derecha está siempre vacío, y es fácil acabar '
                       'tocando la primera nota como si fuera el uno. Entonces el vals se desplaza '
                       'entero y deja de sonar a vals. La izquierda es la que salva esto: ella sí '
                       'toca en el uno.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda en el uno, la derecha en el dos y el tres · despacio',
                 sistemas=[
                     dict(cap='a) nunca coinciden · la izquierda marca el uno y la derecha rellena',
                          events=[n('A2'), ac(('A4', 'C5')), ac(('A4', 'C5')),
                                  n('G2'), ac(('B4', 'D5')), ac(('B4', 'D5'))],
                          bars=2),
                     dict(cap='b) con el sostenido escrito en la izquierda · vale para ese compás',
                          events=[n('F#2'), ac(('C5', 'E5')), ac(('C5', 'E5')),
                                  n('E2'), ac(('B4', 'D5')), ac(('B4', 'D5'))],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('La menor', 'A3', 'E2', time_sig=(3, 4), variante=55,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
