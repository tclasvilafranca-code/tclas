# -*- coding: utf-8 -*-
"""Rasputin (Boney M) — pieza 13 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Musescore, marcada "Easy
   piano", 2 páginas, con letra debajo):

     - DOS SOSTENIDOS detrás de la clave, y la música descansa en Si: Si menor.
     - 4/4, y pone "♩ = 124".
     - CIFRADO IMPRESO encima del pentagrama: Bm · Em · F#7. Tres acordes, y
       con ellos está casi toda la canción.
     - El F#7 lleva séptima: cuatro notas, como el Dm7 de Deck the Halls.
     - Lleva la letra escrita debajo, sílaba a sílaba.
     - Hay compases enteros en los que la derecha calla.

   El archivo es EL MISMO que el de José María (md5 idéntico). Allí el trabajo
   iba por contar los compases callados y subir a 124; aquí va por el CIFRADO
   y por el acorde de séptima, que su partitura trae impresos.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, sil, plan, metronomo, verdadero_falso, inventa,
                      dibujar, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=13, nivel='intermedio', slug='Rasputin',
    formato='adulto',
    titulo_corto='Rasputin', time_sig=(4, 4), key_sig='Si menor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source', 'Rasputin.pdf'),
    yt='https://www.youtube.com/results?search_query=rasputin+boney+m+piano+easy',

    ficha=dict(
        titulo='Rasputin',
        autor='Boney M · edición Easy piano',
        datos=[('Tonalidad', 'Si menor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 124'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Dos')],
        titulo_ritmos='Melodía cantada y acordes debajo',
        pie_ritmos='Andamio en Si menor. Lo literal son los tres acordes del cifrado impreso y los '
                   'compases en los que la derecha calla.',
        armonia=dict(
            titulo='Tres acordes y una canción entera',
            tarjetas=[
                ('EL CIFRADO', 'Bm Em F#7',
                 'Tres acordes impresos y con ellos está casi toda la canción. Dos menores y uno '
                 'con séptima: el que empuja para volver al principio.'),
                ('EL F#7', 'Cuatro notas',
                 'Como el Dm7 de Deck the Halls. La séptima es la nota que hace que el acorde no '
                 'suene terminado y pida seguir.'),
                ('DOS SOSTENIDOS', 'Si menor',
                 'Fa y Do sostenidos, la misma armadura que Re mayor. La diferencia es dónde '
                 'descansa la música: aquí, en Si.'),
                ('LOS SILENCIOS', 'Compases enteros',
                 'Hay compases en los que la derecha no toca nada. A ♩ = 124 pasan volando, y hay '
                 'que contarlos: si te los saltas, entras un compás antes.'),
            ],
            pie='Es la misma armadura que Can\'t Help Falling in Love y suena al revés: una es un '
                'vals lento en Re mayor y esta es una canción de discoteca en Si menor. Las dos '
                'teclas negras son las mismas; lo que cambia es a dónde va la música.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, con letra debajo · andamio',
             [n('F#4'), n('F#4'), n('A4'), n('B4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'el acorde, marcando · andamio',
             [ac(('B2', 'D3', 'F#3'), 'h'), ac(('B2', 'D3', 'F#3'), 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Dos sostenidos detrás de la clave: Fa y Do sostenidos.',
            'La música descansa en Si: es Si menor.',
            'Pone "♩ = 124".',
            'El cifrado viene impreso: Bm, Em y F#7.',
            'El F#7 lleva cuatro notas, no tres.',
            'Hay compases enteros en los que la mano derecha no toca.',
        ],
        reto='Contar los compases en los que no tocas. A ♩ = 124 un compás dura menos de dos '
             'segundos, y sin nada que hacer con las manos la cabeza se adelanta casi siempre.',
        truco='En los compases callados, marca el pulso con la mano izquierda en la tapa del piano, '
              'sin tocar. Contar con el cuerpo funciona; contar con la cabeza, a esta velocidad, '
              'no. Cuando la entrada salga sola, deja de marcar.',
        sabias='Boney M la publicó en 1978 y la letra cuenta, bastante libremente, la historia real '
               'de Grigori Rasputin. En varios países se prohibió en la radio por el estribillo, '
               'que en su momento se consideró subido de tono.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuántas veces se repite el mismo grupo de tres acordes. Cuando lo '
                      'veas, la canción se te hace la mitad de larga.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Tres acordes y una melodía que se repite: corta de aprender y difícil de colocar.',
        reglas=['TRES ACORDES: Bm, Em, F#7', 'LOS COMPASES CALLADOS SE CUENTAN',
                'DOS SOSTENIDOS: FA Y DO'],
        bloques=[
            dict(num=1, titulo='Los tres acordes del cifrado', clef='bass',
                 pista='son los que trae impresos tu partitura · tócalos hasta reconocerlos de oído',
                 sistemas=[
                     dict(cap='a) Bm y Em, los dos menores · suenan cerrados, y son los que sostienen '
                              'la canción',
                          events=[ac(('B2', 'D3', 'F#3'), 'h'), ac(('B2', 'D3', 'F#3'), 'h'),
                                  ac(('E2', 'G2', 'B2'), 'h'), ac(('E2', 'G2', 'B2'), 'h')],
                          bars=2, clef='bass', key_sig='Si menor'),
                     dict(cap='b) y el F#7, con su cuarta nota · escucha cómo pide volver al Bm, y '
                              'vuelve',
                          events=[ac(('F#2', 'A#2', 'C#3', 'E3'), 'h'),
                                  ac(('F#2', 'A#2', 'C#3', 'E3'), 'h'),
                                  ac(('B2', 'D3', 'F#3'), 'w')],
                          bars=2, clef='bass', key_sig='Si menor', show_time=False),
                 ]),
            dict(num=2, titulo='Los compases callados, contados',
                 pista='la FORMA es literal: hay compases enteros en los que la derecha no toca',
                 sistemas=[
                     dict(cap='a) dos compases de silencio y entrar · marca el pulso en la tapa del '
                              'piano mientras esperas',
                          events=[sil('w'), sil('w'), n('F#4'), n('F#4'), n('A4'), n('B4')],
                          bars=3, key_sig='Si menor'),
                     dict(cap='b) y con un compás callado en medio de la frase, que es lo peor · la '
                              'frase no se ha acabado, solo se ha parado',
                          events=[n('B4'), n('A4'), n('F#4', 'h'), sil('w'),
                                  n('F#4'), n('G4'), n('F#4'), n('E4')],
                          bars=3, key_sig='Si menor', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA MISMA ARMADURA, OTRA CANCIÓN',
                 texto='Lleva los mismos dos sostenidos que Can\'t Help Falling in Love y no se '
                       'parecen en nada. La armadura dice qué teclas negras se usan, no dónde '
                       'descansa la música: eso se ve en qué nota acaba la frase.'),
            dict(num=3, titulo='Las dos manos, con el acorde marcando',
                 pista='andamio en Si menor · empieza a 90 y sube por escalones',
                 sistemas=[
                     dict(cap='a) melodía arriba, acorde marcado abajo dos veces por compás',
                          events=[ac(('B2', 'F#4'), 'h'), ac(('B2', 'A4'), 'h'),
                                  ac(('E2', 'B4'), 'h'), ac(('E2', 'A4'), 'h')],
                          bars=2, key_sig='Si menor'),
                     dict(cap='b) y con el F#7 antes de volver al principio · ese acorde es el que '
                              'avisa de que la frase se cierra',
                          events=[ac(('F#2', 'C#5'), 'h'), ac(('F#2', 'B4'), 'h'),
                                  ac(('B2', 'F#4'), 'w')],
                          bars=2, key_sig='Si menor', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Rasputin · para casa',
            intro='Veinte minutos. Los tres acordes primero: son la canción entera.',
            bloques=[
                plan((5, 'Los tres acordes, hasta reconocerlos de oído'),
                     (5, 'La melodía sola, con la letra'),
                     (5, 'Los compases callados, contando y marcando en la tapa'),
                     (5, 'Las dos juntas, subiendo por escalones de metrónomo')),
                metronomo('Empieza a 90 y sube de cinco en cinco cuando salga limpio dos veces.',
                          'La meta son 124. Apunta cada día dónde te has quedado.'),
                verdadero_falso([
                    'El F#7 tiene cuatro notas, no tres.',
                    'Si menor y Re mayor llevan la misma armadura.',
                    'Un compás en el que no toco no hay que contarlo.',
                    'Con Bm, Em y F#7 se acompaña casi toda la canción.',
                    'La m pequeña del cifrado quiere decir que el acorde es mayor.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas'),
                inventa(['Solo notas del acorde de Si menor: Si, Re y Fa sostenido.',
                         'Dos compases de cuatro golpes.',
                         'Que uno de los dos compases sea de silencio entero.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases en Si menor',
                        pista='y cuenta el compás callado en voz alta al tocarlo'),
                dibujar(['Si', 'Re', 'Fa#', 'La', 'Sol', 'Mi', 'Si'],
                        titulo='Dibuja tú las notas',
                        pista='solo el óvalo · las tres primeras son el acorde de Si menor'),
                para_clase('Los tres acordes escritos y a qué número de metrónomo has llegado. Y si '
                           'los compases callados te siguen descolocando, dilo: los contamos juntos '
                           'una vez y ya está.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
