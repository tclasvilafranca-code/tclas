# -*- coding: utf-8 -*-
"""Carol of the Bells — pieza 12 de José María. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Mykola Leontovych,
   arreglo de Jim Paterson, mfiles.co.uk, 1 página, 36 compases):

     - DOS BEMOLES detrás de la clave, y la pieza suena en menor: es Sol
       menor. Es la primera pieza en tono menor del cuaderno.
     - Compás de 3/4.
     - LA MANO DERECHA REPITE EL MISMO DIBUJO DE CUATRO NOTAS casi de
       principio a fin. Eso es lo que hace abordable una pieza de 36 compases.
     - La izquierda NO TOCA en los cuatro primeros compases; después entra con
       blancas con puntillo y más adelante con acordes repetidos.
     - En el c. 15 pone "lightly", y al final "2nd time: molto rit.". Hay
       barras de repetición.

   Lo que NO se cita nota a nota: el ostinato de la derecha se lee bien pero
   el acompañamiento no; el material va como ANDAMIO en Sol menor y remite a
   la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jm_comun import (n, ac, sil, corch, plan, metronomo, diferencias, nombres,
                      escribir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOLM = 'Sol menor'


def celula(a, b, c_, d):
    """El dibujo que repite la derecha: negra, dos corcheas y negra. Son
       cuatro notas y TRES tiempos, que es lo que cuadra en 3/4 y lo que se ve
       en la partitura (la segunda y la tercera van unidas por una barra)."""
    return [n(a)] + corch([b, c_]) + [n(d)]

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=12, nivel='iniciación',
    slug='CarolOfTheBells', formato='adulto',
    titulo_corto='Carol of the Bells', time_sig=(3, 4), key_sig=SOLM,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           'carol-of-the-bells   NAVIDAD.'),
    yt='https://www.youtube.com/results?search_query=carol+of+the+bells+piano+easy',

    ficha=dict(
        titulo='Carol of the Bells',
        autor='Mykola Leontovych · villancico ucraniano · arr. Jim Paterson',
        datos=[('Tonalidad', 'Sol menor'), ('Novedad', 'Tono menor'),
               ('Compás', '3/4'), ('Mano dcha.', 'Un dibujo repetido'),
               ('Compases', '36')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Sol menor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Lo literal es que la derecha repite y la izquierda calla al principio.',
        armonia=dict(
            titulo='36 compases que en realidad son cuatro notas',
            tarjetas=[
                ('LA DERECHA', 'Siempre igual',
                 'El mismo dibujo de cuatro notas, compás tras compás, casi de principio a fin. Se '
                 'aprende una vez y vale para toda la pieza.'),
                ('LA IZQUIERDA', 'Entra tarde',
                 'Los cuatro primeros compases no toca nada. Después va cambiando: notas largas, '
                 'acordes repetidos, y al final acordes rotos.'),
                ('EL TONO MENOR', 'Dos bemoles',
                 'Es la primera pieza triste del cuaderno. Los dos bemoles van al Si y al Mi, y son '
                 'los que le dan ese color.'),
                ('LO ESCRITO', '"lightly"',
                 'En el c. 15 el arreglista pide que se toque ligero. Con un dibujo que se repite '
                 'tanto, es lo que evita que suene a martillo.'),
            ],
            pie='Es la pieza más larga que has tocado, y a la vez la que menos material tiene. Cuando '
                'veas una partitura larga, lo primero es siempre buscar qué se repite: casi nunca hay '
                'tanto que aprender como parece.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el dibujo que se repite toda la pieza · andamio',
             celula('G4', 'F#4', 'G4', 'Eb4'), OCRE, 'treble', SOLM),
            ('MANO IZQUIERDA', 'los primeros compases, callada',
             [sil('h.')], AZUL, 'bass', SOLM),
        ],
        especial=[
            'Hay DOS bemoles detrás de la clave: van al Si y al Mi.',
            'La pieza está en tono menor, y por eso suena distinta a todo lo anterior.',
            'La mano derecha repite el mismo dibujo de cuatro notas casi de principio a fin.',
            'La izquierda no toca nada en los cuatro primeros compases.',
            'En el compás 15 pone "lightly": ligero.',
            'Al final pone "2nd time: molto rit.": la segunda vez, frenando mucho.',
        ],
        reto='Que el dibujo repetido no suene a máquina. Cuando algo se repite treinta veces, la mano '
             'se pone rígida y todas las notas salen igual de fuertes.',
        truco='Piensa el dibujo de cuatro notas como una sola palabra, no como cuatro golpes: la '
              'primera un poco más y las otras tres más ligeras, todas dentro del mismo gesto. Prueba '
              'a decir "TIN-ti-ni-ta" mientras lo tocas. Es exactamente lo que pide el "lightly" del '
              'compás 15.',
        sabias='En Ucrania no es un villancico de Navidad: es una canción de Año Nuevo sobre una '
               'golondrina que entra en casa a anunciar un año próspero. La letra inglesa de las '
               'campanas se la pusieron en Estados Unidos en 1936, veinte años después.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que las cuatro notas de arriba no paran nunca. Todo lo que cambia '
                      'está debajo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza se estudia al revés que las demás: primero se busca lo que se repite y '
              'luego se aprende solo lo que cambia. Media hora de lápiz sobre la partitura vale por '
              'tres al piano.',
        reglas=['LA DERECHA REPITE: APRÉNDELA UNA VEZ', 'LA IZQUIERDA ENTRA EN EL COMPÁS 5',
                'LIGERO, NO FUERTE'],
        bloques=[
            dict(num=1, titulo='El dibujo de cuatro notas',
                 pista='andamio en Sol menor · es lo que hace la derecha casi toda la pieza',
                 sistemas=[
                     dict(cap='a) el dibujo, cuatro veces seguidas · la primera nota pesa y las otras '
                              'tres van ligeras',
                          events=(celula('G4', 'F#4', 'G4', 'Eb4') * 4),
                          bars=4, key_sig=SOLM),
                     dict(cap='b) y el mismo dibujo movido de sitio, que es lo único que cambia en '
                              'toda la pieza',
                          events=(celula('F4', 'Eb4', 'F4', 'D4') +
                                  celula('G4', 'F#4', 'G4', 'Eb4') +
                                  celula('F4', 'Eb4', 'F4', 'D4')),
                          bars=3, key_sig=SOLM, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LO PRIMERO ES EL LÁPIZ',
                 texto='Numera los 36 compases y marca con un color los que llevan el dibujo tal cual. '
                       'Vas a ver que son casi todos. Después marca con otro color los cuatro o cinco '
                       'sitios donde cambia. Eso es lo que hay que aprender: cinco compases, no '
                       'treinta y seis. Es la diferencia entre que esta pieza dé miedo o no.'),
            dict(num=2, titulo='La izquierda, por partes', clef='bass',
                 pista='andamio en Sol menor · va cambiando de trabajo a lo largo de la pieza',
                 sistemas=[
                     dict(cap='a) primero calla cuatro compases, y luego entra con notas largas',
                          events=[sil('h.'), sil('h.'),
                                  n('G2', 'h.'), n('Eb3', 'h.')],
                          bars=4, clef='bass', key_sig=SOLM),
                     dict(cap='b) y más adelante, acordes repetidos · ligeros, que no tapen a la '
                              'derecha',
                          events=[ac(('G2', 'D3')), ac(('G2', 'D3')), ac(('G2', 'D3')),
                                  ac(('Eb2', 'Bb2')), ac(('Eb2', 'Bb2')), ac(('Eb2', 'Bb2'))],
                          bars=2, clef='bass', key_sig=SOLM, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, los compases 5 al 8',
                 pista='andamio · la derecha sigue con lo suyo y la izquierda entra por debajo',
                 sistemas=[
                     dict(cap='a) la derecha no cambia nada cuando entra la izquierda: eso es lo que '
                              'hay que conseguir',
                          events=(celula('G4', 'F#4', 'G4', 'Eb4') * 2 +
                                  celula('G4', 'F#4', 'G4', 'D4')),
                          bars=3, key_sig=SOLM),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · entra en el compás 5 y no '
                              'estorba: notas largas debajo del dibujo',
                          events=[n('G2', 'h.'), n('Eb3', 'h.'), n('D3', 'h.')],
                          bars=3, clef='bass', key_sig=SOLM, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Carol of the Bells · para casa',
            intro='Veinte minutos al día, y el primer día entero con el lápiz.',
            bloques=[
                plan((5, 'El dibujo de cuatro notas, ligero, ocho veces seguidas'),
                     (5, 'El mismo dibujo movido de sitio'),
                     (5, 'La izquierda: contar cuatro compases y entrar'),
                     (5, 'Los compases 5 al 8 con las dos manos')),
                metronomo('Empieza lento: con un dibujo que se repite, acelerar es facilísimo.',
                          'Si el clic se te adelanta al final del compás, estás corriendo.'),
                diferencias(
                    celula('G4', 'F#4', 'G4', 'Eb4') + celula('G4', 'F#4', 'G4', 'Eb4'),
                    celula('G4', 'F#4', 'G4', 'E4') + celula('G4', 'F#4', 'A4', 'Eb4'),
                    cuantas=2,
                    titulo='Busca las dos diferencias',
                    pista='arriba el dibujo bueno · abajo, con dos cambios'),
                nombres(['G4', 'F#4', 'Eb4', 'D4', 'Bb4', 'C5', 'A4', 'G4'],
                        titulo='Los nombres, con dos bemoles en la armadura',
                        pista='ojo: en esta pieza el Si y el Mi van a la tecla negra'),
                escribir(titulo='Copia aquí el dibujo de cuatro notas',
                         pista='cópialo con su armadura · cuatro compases seguidos'),
                para_clase('El dibujo que se repite, y a qué velocidad te sale seguido. Si la izquierda se te desajusta siempre en el mismo compás, tráelo marcado.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
