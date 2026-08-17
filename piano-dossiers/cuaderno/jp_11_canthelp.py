# -*- coding: utf-8 -*-
"""Can't Help Falling in Love — pieza 11 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Elvis Presley, arreglo de
   Seb Alejandro, Musescore, 2 páginas, marcado "Piano ~ Chords ~ Lyrics"):

     - DOS SOSTENIDOS detrás de la clave: Re mayor.
     - Compás de 3/4.
     - CIFRADO IMPRESO encima del pentagrama, compás a compás: D · F#m · Bm ·
       G · A. Cinco acordes, y con ellos está la canción entera.
     - Lleva la LETRA escrita debajo del pentagrama, sílaba a sílaba.
     - La izquierda va en corcheas seguidas: no descansa en toda la pieza.

   El archivo es EL MISMO que el de José María (md5 idéntico). Allí el trabajo
   iba por los dos sostenidos y la izquierda; aquí va por el CIFRADO, que su
   partitura trae impreso y que a estas alturas del curso ya puede leer.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, reto, plan, cifrado, verdadero_falso, figuras,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=11, nivel='intermedio', slug='CantHelpFalling',
    formato='adulto',
    titulo_corto="Can't Help Falling in Love", time_sig=(3, 4), key_sig='Re mayor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'cant-help-falling-in-love-elvis-presley.'),
    yt='https://www.youtube.com/results?search_query=cant+help+falling+in+love+piano+easy',

    ficha=dict(
        titulo="Can't Help Falling in Love",
        autor='Elvis Presley · arreglo de Seb Alejandro',
        datos=[('Tonalidad', 'Re mayor'), ('Compás', '3/4'),
               ('Carácter', 'Sin tempo impreso'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Dos')],
        titulo_ritmos='Un vals con la izquierda sin parar',
        pie_ritmos='Andamio en Re mayor. Lo literal es el reparto: melodía larga arriba y corcheas '
                   'seguidas abajo, en compás de tres.',
        armonia=dict(
            titulo='Cinco acordes y ya está la canción',
            tarjetas=[
                ('DOS SOSTENIDOS', 'Re mayor',
                 'Fa sostenido y Do sostenido. Todos los Fa y todos los Do de la pieza van a tecla '
                 'negra, de principio a fin.'),
                ('EL CIFRADO', 'D F#m Bm G A',
                 'Cinco acordes impresos encima del pentagrama y con ellos está toda la canción. '
                 'Dos de ellos son menores: la m pequeña es lo que lo dice.'),
                ('TRES POR COMPÁS', 'Es un vals',
                 'Compás de 3/4. El primer golpe pesa y los otros dos no. Si los tres pesan igual, '
                 'la canción se convierte en una marcha.'),
                ('LA LETRA', 'Debajo',
                 'Está escrita sílaba a sílaba. Sirve para algo muy concreto: cantar la melodía te '
                 'dice dónde respira la frase, y ahí es donde hay que aflojar.'),
            ],
            pie='Es la primera pieza donde el cifrado impreso te da de verdad la pieza entera. Si '
                'sabes los cinco acordes, puedes acompañar la canción sin la partitura, y eso es un '
                'salto de nivel que no se ve en el papel.',
        ),
        ritmos=[
            ('MANO DERECHA', 'notas largas, una por compás · andamio',
             [n('F#4', 'h.')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'corcheas seguidas, sin descansar · andamio',
             [n('D3', 'e'), n('A3', 'e'), n('F#3', 'e'), n('A3', 'e'),
              n('D3', 'e'), n('A3', 'e')], AZUL, 'bass', None),
        ],
        especial=[
            'Dos sostenidos detrás de la clave: Fa sostenido y Do sostenido.',
            'Compás de 3/4: un vals.',
            'El cifrado viene impreso: D, F#m, Bm, G y A.',
            'Dos de los cinco acordes son menores (F#m y Bm).',
            'La letra está escrita debajo del pentagrama, sílaba a sílaba.',
            'La izquierda va en corcheas seguidas de principio a fin.',
        ],
        reto='Que la izquierda no se pare a pensar. Va en corcheas sin descanso, y cada vez que la '
             'derecha cambia de nota larga hay una tentación de frenar abajo para colocarla.',
        truco='Toca la izquierda sola de principio a fin, dos veces, sin la derecha y sin mirar la '
              'melodía. Cuando puedas hacerlo hablando en voz alta a la vez, ya no se te va a '
              'parar cuando pongas la derecha encima.',
        sabias='La melodía no es de los años cincuenta: viene de "Plaisir d\'amour", una canción '
               'francesa de 1784. Elvis la grabó en 1961 para una película, y desde entonces se '
               'toca más en bodas que en conciertos.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el balanceo del acompañamiento: no para nunca y no pesa nunca. Esa '
                      'es la izquierda que estás estudiando.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La melodía es de notas largas y la izquierda no para: son dos trabajos distintos y '
              'hay que hacerlos por separado. La izquierda primero, y hasta que salga sola.',
        reglas=['DOS SOSTENIDOS: FA Y DO', 'LA IZQUIERDA NO SE PARA',
                'EL PRIMER GOLPE PESA, LOS OTROS DOS NO'],
        bloques=[
            dict(num=1, titulo='La izquierda, sola y sin parar', clef='bass',
                 pista='andamio en Re mayor · la FORMA es literal: corcheas seguidas en 3/4',
                 sistemas=[
                     dict(cap='a) seis corcheas por compás, iguales · el primer golpe pesa un poco '
                              'más y los demás no pesan nada',
                          events=[n('D3', 'e'), n('A3', 'e'), n('F#3', 'e'),
                                  n('A3', 'e'), n('D3', 'e'), n('A3', 'e'),
                                  n('D3', 'e'), n('A3', 'e'), n('F#3', 'e'),
                                  n('A3', 'e'), n('D3', 'e'), n('A3', 'e')],
                          bars=2, clef='bass', key_sig='Re mayor', time_sig=(3, 4)),
                     dict(cap='b) cambiando de acorde, que es donde se para todo el mundo · el '
                              'cambio se prepara en la última corchea del compás anterior',
                          events=[n('B2', 'e'), n('F#3', 'e'), n('D3', 'e'),
                                  n('F#3', 'e'), n('B2', 'e'), n('F#3', 'e'),
                                  n('G2', 'e'), n('D3', 'e'), n('B2', 'e'),
                                  n('D3', 'e'), n('G2', 'e'), n('D3', 'e')],
                          bars=2, clef='bass', key_sig='Re mayor', time_sig=(3, 4), show_time=False),
                 ]),
            dict(num=2, titulo='Los cinco acordes del cifrado, en bloque', clef='bass',
                 pista='son los que trae impresos tu partitura · tocarlos ayuda a leerlos',
                 sistemas=[
                     dict(cap='a) D, F#m y Bm · los dos últimos son menores y suenan más cerrados',
                          events=[ac(('D3', 'F#3', 'A3'), 'h.'), ac(('F#2', 'A2', 'C#3'), 'h.'),
                                  ac(('B2', 'D3', 'F#3'), 'h.')],
                          bars=3, clef='bass', key_sig='Re mayor', time_sig=(3, 4)),
                     dict(cap='b) G y A, y vuelta a D · escucha cómo el A pide volver a casa',
                          events=[ac(('G2', 'B2', 'D3'), 'h.'), ac(('A2', 'C#3', 'E3'), 'h.'),
                                  ac(('D3', 'F#3', 'A3'), 'h.')],
                          bars=3, clef='bass', key_sig='Re mayor', time_sig=(3, 4), show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='PARA QUÉ SIRVE SABERSE EL CIFRADO',
                 texto='Si sabes que el compás pone Bm y sabes qué notas son, ya no necesitas leer '
                       'nota a nota lo que hace la izquierda: te basta con ver el cambio de acorde '
                       'y tu mano va sola. Es la diferencia entre leer letra por letra y leer '
                       'palabras enteras, y es lo que hace que se pueda tocar una canción sin '
                       'haberla estudiado.'),
            dict(num=3, titulo='Las dos manos, con la melodía encima',
                 pista='andamio en Re mayor · la derecha aguanta y la izquierda sigue moviéndose',
                 sistemas=[
                     dict(cap='a) una nota larga arriba por cada seis corcheas abajo · si la '
                              'izquierda se para al entrar la derecha, vuelve al paso 1',
                          events=[ac(('D3', 'F#4'), 'e'), n('A3', 'e'), n('F#3', 'e'),
                                  n('A3', 'e'), n('D3', 'e'), n('A3', 'e'),
                                  ac(('B2', 'G4'), 'e'), n('F#3', 'e'), n('D3', 'e'),
                                  n('F#3', 'e'), n('B2', 'e'), n('F#3', 'e')],
                          bars=2, key_sig='Re mayor', time_sig=(3, 4)),
                     dict(cap='b) y con la melodía moviéndose dentro del compás · la izquierda no '
                              'se entera de que arriba ha cambiado algo',
                          events=[ac(('G2', 'B4'), 'e'), n('D3', 'e'), n('B2', 'e'),
                                  n('D3', 'e'), n('G2', 'e'), n('D3', 'e'),
                                  ac(('A2', 'A4'), 'e'), n('E3', 'e'), n('C#3', 'e'),
                                  n('E3', 'e'), n('A2', 'e'), n('E3', 'e')],
                          bars=2, key_sig='Re mayor', time_sig=(3, 4), show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina="Can't Help Falling in Love · para casa",
            intro='Veinte minutos, y diez de ellos con la mano izquierda sola.',
            bloques=[
                reto('Tocar la izquierda entera, dos veces, sin pararse ni una sola vez.',
                     'Tócala sola y hablando en voz alta a la vez: di los nombres de los acordes '
                     'según pasan. Si puedes hablar mientras tocas, la mano ya va sola y ya puedes '
                     'poner la derecha.'),
                plan((6, 'La izquierda sola, de principio a fin'),
                     (4, 'Los cinco acordes en bloque, diciendo su nombre'),
                     (5, 'La melodía sola, cantando la letra'),
                     (5, 'Las dos juntas, de cuatro en cuatro compases')),
                cifrado(['D', 'F#m', 'Bm', 'G', 'A'],
                        ['Escribe las tres notas de cada uno, de grave a agudo.',
                         'Rodea los dos que son menores: lo dice la m pequeña.'],
                        pista='son los cinco que trae impresos tu partitura'),
                verdadero_falso([
                    'En Re mayor todos los Fa y todos los Do van a tecla negra.',
                    'La m pequeña del cifrado quiere decir que el acorde es menor.',
                    'En 3/4 los tres golpes del compás pesan igual.',
                    'Con estos cinco acordes se puede acompañar la canción entera.',
                    'La letra escrita debajo del pentagrama sirve para saber dónde respira la frase.'],
                    titulo='Verdadero o falso',
                    pista='solo una es falsa'),
                figuras([('h.', 'blanca con puntillo'), ('q', 'negra'), ('e', 'corchea'),
                         ('q.', 'negra con puntillo')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='la primera es la que llena un compás entero de 3/4'),
                para_clase('La izquierda sola de principio a fin, y los cinco acordes escritos. Si '
                           'te los sabes, en clase probamos a tocar la canción solo con el cifrado, '
                           'sin leer la partitura.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
