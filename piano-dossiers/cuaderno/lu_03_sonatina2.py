# -*- coding: utf-8 -*-
"""Sonatina nº 2, de Bazzoni — pieza 3 de Luisa. Formato adulto, iniciación.

   Lo comprobado sobre el PDF de su carpeta de Drive ("SONATINA N. 2 -
   pianoforte a 4 mani, in sol maggiore - in G Major", M. Bazzoni, 2 páginas):

     - UN SOSTENIDO detrás de la clave: Sol mayor.
     - 4/4.
     - Es a cuatro manos. El Pianoforte 1 lleva LOS DOS PENTAGRAMAS EN CLAVE DE
       SOL con 8va, y las dos manos tocan lo mismo a distancia de octava.
     - En la parte del alumno solo hay negras y blancas.
     - El Pianoforte 2 hace acordes en el segundo y el cuarto golpe.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import sistemas_extra
from lu_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=3, nivel='iniciación', slug='SonatinaSolMayor',
    formato='adulto',
    titulo_corto='Sonatina nº 2 · Bazzoni', time_sig=(4, 4), key_sig='Sol mayor',
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source',
                           '_bazzoni-maurizio-sonatina-sol-maggiore (4 manos).pdf'),
    yt='https://www.youtube.com/results?search_query=bazzoni+sonatina+sol+maggiore+4+mani',

    ficha=dict(
        titulo='Sonatina nº 2',
        autor='Maurizio Bazzoni · en Sol mayor · a cuatro manos · tu parte es la de arriba',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'),
               ('Teclas negras', 'El Fa'), ('Manos', 'Las dos igual'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Negras y blancas, las dos manos igual',
        pie_ritmos='Andamio en Sol mayor. El dibujo es el de tu partitura; lo que hay que mirar es '
                   'el sostenido del principio, que vale para toda la pieza.',
        armonia=dict(
            titulo='Tu primera tecla negra fija',
            tarjetas=[
                ('UN SOSTENIDO', 'Sol mayor',
                 'Justo después de la clave hay un signo, un sostenido. Quiere decir que TODOS los '
                 'Fa de la pieza se tocan en la tecla negra de al lado. Todos, y hasta el final.'),
                ('NO CUESTA', 'Porque van igual',
                 'Es tu primera armadura y llega en la pieza más cómoda para tenerla: las dos manos '
                 'siguen tocando lo mismo, así que solo hay un sitio donde acordarse.'),
                ('CUATRO GOLPES', 'Otra vez',
                 'Volvemos al compás de cuatro. Ya lo hiciste en la primera pieza.'),
                ('LA OTRA PARTE', 'Marca el ritmo',
                 'La profesora toca acordes en el segundo y el cuarto golpe. Tú vas por encima, y '
                 'ella te da el pulso.'),
            ],
            pie='Es la misma clase de pieza que la primera y la segunda, y a propósito: las tres '
                'primeras del cuaderno se tocan igual. Lo único nuevo aquí es mirar el principio '
                'del pentagrama antes de empezar.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negras y una blanca al final · andamio',
             [n('G4'), n('D4'), n('B4'), n('G4')], OCRE, 'treble', 'Sol mayor'),
            ('MANO IZQUIERDA', 'lo mismo, más grave · andamio',
             [n('G3'), n('D3'), n('B3'), n('G3')], AZUL, 'treble', 'Sol mayor'),
        ],
        especial=[
            'Detrás de la clave hay UN sostenido: es Sol mayor.',
            'Ese sostenido quiere decir que todos los Fa van a la tecla negra.',
            'Compás de 4/4.',
            'Tus dos pentagramas van en clave de sol y las dos manos tocan lo mismo.',
            'En tu parte solo hay negras y blancas.',
            'La otra parte, la de la profesora, hace acordes en el segundo y el cuarto golpe.',
        ],
        reto='Acordarte del Fa sostenido a mitad de la pieza. Los primeros compases salen bien '
             'porque estás pendiente; el fallo llega cuando ya te has olvidado de que está.',
        truco='Antes de tocar, coge un lápiz y haz un círculo en todos los Fa de tu partitura. Son '
              'pocos. Marcarlos una vez ahorra veinte correcciones, y en dos semanas ya se pueden '
              'borrar.',
        sabias='Sol mayor es de las primeras tonalidades que se aprenden en casi todo el mundo, y '
               'no es casualidad: solo cambia una tecla respecto a las blancas, y esa tecla cae '
               'justo donde la mano la alcanza sin moverse.',
        qr=dict(titulo='Escúchala',
                texto='Escucha las dos partes juntas. La tuya es la melodía; lo que suena debajo '
                      'marcando el ritmo es la de la profesora.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana lo primero no es tocar: es coger el lápiz y marcar los Fa.',
        reglas=['TODOS LOS FA, EN LA TECLA NEGRA', 'MÁRCALOS CON LÁPIZ',
                'UNA MANO Y DESPUÉS LAS DOS'],
        bloques=[
            dict(num=1, titulo='La escala de Sol, para oír el Fa sostenido',
                 pista='andamio en Sol mayor · la penúltima nota es la de la tecla negra',
                 sistemas=[
                     dict(cap='a) subiendo desde Sol · escucha cómo la penúltima empuja hacia la '
                              'última',
                          events=[n('G4'), n('A4'), n('B4'), n('C5'),
                                  n('D5'), n('E5'), n('F#5'), n('G5')],
                          bars=2, key_sig='Sol mayor'),
                     dict(cap='b) y bajando · el Fa sigue siendo el de la tecla negra también aquí',
                          events=[n('G5'), n('F#5'), n('E5'), n('D5'),
                                  n('C5'), n('B4'), n('A4'), n('G4')],
                          bars=2, key_sig='Sol mayor', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES ESE SIGNO DEL PRINCIPIO',
                 texto='El signo que hay justo después de la clave no es una nota: es un aviso. '
                       'Dice que todos los Fa de la pieza, los graves y los agudos, se tocan en la '
                       'tecla negra que hay a su derecha. No hace falta que lo repitan en cada '
                       'compás: con ponerlo una vez al principio, ya vale para toda la pieza.'),
            dict(num=2, titulo='La melodía, una mano cada vez',
                 pista='andamio en Sol mayor · primero la derecha sola, luego la izquierda sola',
                 sistemas=[
                     dict(cap='a) la mano derecha · negras, y una blanca donde acaba la frase',
                          events=[n('G4'), n('B4'), n('D5'), n('B4'), n('A4'), n('B4'), n('G4', 'h')],
                          bars=2, key_sig='Sol mayor'),
                     dict(cap='b) la mano izquierda, más grave · el mismo dibujo, y también en '
                              'clave de sol',
                          events=[n('G3'), n('B3'), n('D4'), n('B3'), n('A3'), n('B3'), n('G3', 'h')],
                          bars=2, key_sig='Sol mayor', show_time=False),
                 ]),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · despacio · un solo sonido, no dos',
                 sistemas=[
                     dict(cap='a) las dos manos a la vez, con el Fa sostenido puesto',
                          events=[ac(('G3', 'G4')), ac(('A3', 'A4')), ac(('B3', 'B4')),
                                  ac(('C4', 'C5')), ac(('D4', 'D5'), 'h'),
                                  ac(('B3', 'B4'), 'h')],
                          bars=2, key_sig='Sol mayor'),
                     dict(cap='b) y con la vuelta a casa · la última nota se aguanta entera',
                          events=[ac(('E4', 'E5')), ac(('F#4', 'F#5')), ac(('G4', 'G5'), 'h'),
                                  ac(('G3', 'G4'), 'w')],
                          bars=2, key_sig='Sol mayor', show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('Sol mayor', 'G3', 'G2', time_sig=(4, 4), variante=7,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
