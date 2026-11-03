# -*- coding: utf-8 -*-
"""Rasputin, de Boney M — pieza 16 de Isaac.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Rasputin A · Bony M",
   Musescore, *Easy piano*, 2 páginas; el mismo archivo que piezas de
   Mercè, José María, Josep, Luisa y Nel, byte a byte):

     - Detrás de la clave hay DOS SOSTENIDOS: Si menor.
     - 4/4, y pone "♩ = 124".
     - La mano izquierda está callada compases enteros al empezar.
     - Encima del pentagrama hay letras de acorde impresas: Bm, Em…
     - La derecha empieza con negra, negra, negra con puntillo y corchea.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra, bloque_puntillo, encajar
from is_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SIm = 'Si menor'

CANCION = dict(
    alumno='Isaac', carpeta='Isaac', num=16, nivel='intermedio', slug='Rasputin',
    formato='adulto',
    titulo_corto='Rasputin', time_sig=(4, 4), key_sig=SIm,
    partitura=os.path.join(HERE, '..', 'students', 'isaac', 'source', 'Rasputin.pdf'),
    yt='https://www.youtube.com/results?search_query=rasputin+boney+m+easy+piano',

    ficha=dict(
        titulo='Rasputin',
        autor='Boney M · 1978 · versión Easy piano',
        datos=[('Tonalidad', 'Si menor'), ('Armadura', 'Dos sostenidos'),
               ('Compás', '4/4'), ('Tempo', '♩ = 124'),
               ('Izquierda', 'Entra tarde')],
        titulo_ritmos='Dos sostenidos para toda la pieza',
        pie_ritmos='Andamio en Si menor. Lo literal es el reparto: la derecha lleva la melodía '
                   'desde el principio y la izquierda pasa compases callada antes de entrar.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('DOS SOSTENIDOS', 'Fa y Do',
                 'Es la armadura más cargada que has tocado con dos alteraciones: todos los Fa y '
                 'todos los Do son teclas negras, en las dos manos.'),
                ('LA IZQUIERDA ESPERA', 'Compases enteros',
                 'Empieza callada y entra más adelante. Mientras tanto la derecha lleva sola el '
                 'pulso de toda la pieza.'),
                ('LETRAS DE ACORDE', 'Bm, Em…',
                 'Bm es Si menor y Em es Mi menor. Están impresas encima y dicen sobre qué acorde '
                 'está la melodía en cada momento.'),
                ('♩ = 124', 'Pulso firme',
                 'Es una canción de baile: el pulso tiene que ser exacto, no hay margen para '
                 'respirar entre frases.'),
            ],
            pie='Es la pieza con más teclas negras de tu cuaderno, y aun así las notas van casi '
                'todas seguidas: lo que cuesta no son los saltos, es acordarse de la armadura.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negras y luego largo-corto · literal',
             [n('B3'), n('D4'), n('E4', 'q.'), n('F#4', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'un compás entero callada · literal',
             [sil('w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay dos sostenidos: todos los Fa y todos los Do son negros.',
            'La tonalidad es Si menor.',
            'Compás de 4/4 y "♩ = 124" escrito arriba.',
            'La mano izquierda está callada compases enteros al empezar.',
            'Encima del pentagrama hay letras de acorde: Bm, Em…',
            'La derecha lleva la melodía completa mientras la izquierda espera.',
        ],
        reto='Acordarse de los dos sostenidos cuando la melodía va seguida y rápida.',
        truco='Antes de tocar, toca solo las dos teclas negras de la armadura —Fa sostenido y Do '
              'sostenido— tres veces, diciendo su nombre en voz alta.',
        sabias='Boney M la publicó en 1978, y la letra se inventa buena parte de la historia real de '
               'Rasputín. En la Unión Soviética estuvo prohibida durante años.',
        qr=dict(titulo='Escúchala',
                texto='Marca el pulso con el pie de principio a fin. No para nunca.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La armadura primero, siempre. Con las dos teclas negras localizadas, el resto de '
              'esta pieza es más sencillo de lo que parece.',
        reglas=['TODOS LOS FA Y LOS DO SON NEGROS', 'LA IZQUIERDA ENTRA CUANDO LE TOCA',
                'EL PULSO NO SE PARA NUNCA'],
        bloques=[
            dict(num=1, titulo='La mano en Si menor',
                 pista='andamio · los sostenidos están en la armadura, no en la nota',
                 sistemas=[
                     dict(cap='a) subiendo por grados, con otro dibujo',
                          events=[n('B3'), n('C#4'), n('D4'), n('E4'),
                                  n('F#4'), n('G4'), n('A4'), n('B4')],
                          bars=2),
                     dict(cap='b) y bajando con un salto de cuarta',
                          events=[n('D4'), n('A3'), n('E4'), n('B3'),
                                  n('F#4'), n('C#4'), n('G4'), n('D4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La derecha sola, con el largo-corto',
                 pista='andamio · el ritmo del primer compás es el de tu partitura',
                 sistemas=[
                     dict(cap='a) dos negras y luego larga y corta, empezando más arriba',
                          events=[n('F#4'), n('E4'), n('D4', 'q.'), n('C#4', 'e'),
                                  n('B3'), n('C#4'), n('D4', 'h')],
                          bars=2),
                     dict(cap='b) el mismo ritmo más abajo, empezando despacio',
                          events=encajar([n('A3'), n('G3'), n('F#3', 'q.'), n('E3', 'e'),
                                          n('D3'), n('E3'), n('F#3', 'h')], 'treble'),
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA ARMADURA NO SE OLVIDA, SE PRACTICA',
                 texto='Dos sostenidos son dos teclas negras que valen para toda la pieza. No hay '
                       'ningún truco de lectura que sustituya a esto: lo que funciona es tocarlas '
                       'sueltas antes de empezar, diciendo su nombre.'),
            dict(num=3, titulo='Las dos juntas, cuando la izquierda entra',
                 pista='andamio · un compás callada y después acompañando · despacio',
                 sistemas=[
                     dict(cap='a) la izquierda calla un compás entero y entra en el siguiente',
                          events=[sil('w'), n('F#3', 'h'), n('B2', 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) y ya con la melodía encima',
                          events=[ac(('F#3', 'F#4')), n('E4'), ac(('B2', 'D4')), n('B3'),
                                  ac(('E3', 'E4')), n('D4'), ac(('D3', 'C#4')), n('B3')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Si menor', 14, 'B3', 'B2',
                          'los dos sostenidos siguen ahí cuando la melodía va seguida',
                          desde=3, time_sig=(4, 4))[:1],
    ),
)

# El ritmo con puntillo que esta pieza EXPLICA en su texto y no dibujaba en
# ningún sitio. Lo destapó el auditor de vocabulario al ganar la entrada de
# esta figura, que antes no miraba nadie.
CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + [
    bloque_puntillo('Si menor', 5, 'B3', 'el puntillo que empuja el ritmo',
                    time_sig=(4, 4))]

if __name__ == '__main__':
    print('generado', construir(CANCION))
