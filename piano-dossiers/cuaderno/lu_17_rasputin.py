# -*- coding: utf-8 -*-
"""Rasputin, de Boney M — pieza 17 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Rasputin A · Bony M",
   Musescore, *Easy piano*, 2 páginas), leído a 230 dpi:

     - Detrás de la clave hay DOS SOSTENIDOS: Si menor.
     - 4/4, y pone "♩ = 124".
     - Hay barra de repetición al principio.
     - **La mano izquierda está callada compases enteros** al empezar: silencio
       de compás tras silencio de compás.
     - Encima del pentagrama hay LETRAS DE ACORDE impresas: Bm, Em…
     - La derecha empieza con negra, negra, negra con puntillo y corchea.

   ES EL MISMO ARCHIVO que la pieza 14 de José María y la 13 de Josep. Las
   citas literales pueden coincidir; el material inventado no. Lo comprueba
   `cruzar_luisa.py`, y por eso aquí el andamio va por otro sitio: los otros
   dos trabajan los acordes y el registro grave; Luisa trabaja la armadura de
   dos sostenidos y la espera de la izquierda.
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
    alumno='Luisa', carpeta='Luisa', num=17, nivel='iniciación', slug='Rasputin',
    formato='adulto',
    titulo_corto='Rasputin', time_sig=(4, 4), key_sig='Si menor',
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source', 'rasputin easy.pdf'),
    yt='https://www.youtube.com/results?search_query=rasputin+boney+m+easy+piano',

    ficha=dict(
        titulo='Rasputin',
        autor='Boney M · 1978 · versión Easy piano',
        datos=[('Tonalidad', 'Si menor'), ('Armadura', 'Dos sostenidos'),
               ('Compás', '4/4'), ('Tempo', '♩ = 124'),
               ('Izquierda', 'Entra tarde')],
        titulo_ritmos='Dos sostenidos para toda la pieza',
        pie_ritmos='Andamio en Si menor. Lo literal es el reparto: la derecha lleva la melodía desde '
                   'el principio y la izquierda pasa varios compases callada antes de entrar.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('DOS SOSTENIDOS', 'Fa y Do',
                 'Es la armadura más cargada de tu cuaderno. Todos los Fa y todos los Do son teclas '
                 'negras, en las dos manos y en toda la pieza.'),
                ('LA IZQUIERDA ESPERA', 'Compases enteros',
                 'Empieza callada y entra más adelante. Mientras tanto la derecha lleva sola el '
                 'pulso, y eso es lo que hay que sostener.'),
                ('LETRAS DE ACORDE', 'Bm, Em…',
                 'Bm es Si menor y Em es Mi menor. Están impresas encima y te dicen sobre qué acorde '
                 'está la melodía en cada momento.'),
                ('♩ = 124', 'Con número',
                 'Se puede comprobar con el metrónomo. Es una canción de baile, así que el pulso '
                 'tiene que ser exacto: aquí no se puede respirar entre frases.'),
            ],
            pie='Es la pieza con más teclas negras del cuaderno, y aun así las notas van casi todas '
                'seguidas. Lo que cuesta no son los saltos: es acordarse de la armadura.',
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
            'Al principio hay una barra de repetición.',
            'La mano izquierda está callada compases enteros al empezar.',
            'Encima del pentagrama hay letras de acorde: Bm, Em…',
        ],
        reto='Acordarse de los dos sostenidos cuando la melodía va seguida. Con la armadura no se '
             'discute: no está escrita en la nota, está al principio de la línea.',
        truco='Antes de tocar, toca solo las dos teclas negras de la armadura —el Fa sostenido y el '
              'Do sostenido— tres veces, diciendo su nombre. Es medio minuto y quita casi todos los '
              'fallos de la semana.',
        sabias='Boney M la publicó en 1978 y la letra se inventa media historia: Rasputín no murió '
               'como cuenta la canción. En Rusia estuvo prohibida durante años, y hoy es lo primero '
               'que suena en cualquier fiesta.',
        qr=dict(titulo='Escúchala',
                texto='Marca el pulso con el pie de principio a fin. Vas a notar que no para nunca: '
                      'esa es la diferencia entre esta pieza y las lentas de antes.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La armadura primero, siempre. Cuando la mano ya sabe dónde están las dos teclas '
              'negras, lo demás de esta pieza es fácil.',
        reglas=['TODOS LOS FA Y LOS DO SON NEGROS', 'LA IZQUIERDA ENTRA CUANDO LE TOCA',
                'EL PULSO NO SE PARA NUNCA'],
        bloques=[
            dict(num=1, titulo='La mano en Si menor',
                 pista='andamio en Si menor · los sostenidos están en la armadura, no en la nota',
                 sistemas=[
                     dict(cap='a) subiendo y bajando por las notas de la tonalidad · di el nombre '
                              'de cada tecla negra al tocarla',
                          events=[n('F#4'), n('G4'), n('A4'), n('B4'),
                                  n('C#5'), n('B4'), n('A4'), n('G4')],
                          bars=2),
                     dict(cap='b) y saltando de dos en dos · las teclas negras siguen siendo las '
                              'mismas dos',
                          events=[n('B3'), n('D4'), n('C#4'), n('E4'),
                                  n('D4'), n('F#4'), n('E4'), n('G4')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La derecha sola, con el largo-corto',
                 pista='andamio · el ritmo del primer compás es el de tu partitura',
                 sistemas=[
                     dict(cap='a) tres negras y luego una larga y una corta · cuenta "un, dos, '
                              'treees y"',
                          events=[n('B4'), n('A4'), n('G4', 'q.'), n('F#4', 'e'),
                                  n('E4'), n('F#4'), n('G4', 'h')],
                          bars=2),
                     dict(cap='b) el mismo ritmo más abajo · a ♩=124 la nota corta se escapa: '
                              'empieza a la mitad de velocidad',
                          events=[n('D4'), n('E4'), n('F#4', 'q.'), n('G4', 'e'),
                                  n('A4'), n('G4'), n('F#4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA ARMADURA NO SE OLVIDA, SE PRACTICA',
                 texto='Dos sostenidos son dos teclas negras que valen para toda la pieza y para las '
                       'dos manos. No hay ningún truco de lectura que ayude: lo que funciona es '
                       'tocarlas antes de empezar, sueltas y diciendo su nombre, para que la mano '
                       'las tenga localizadas. Medio minuto al principio de cada sesión.'),
            dict(num=3, titulo='Las dos juntas, cuando la izquierda entra',
                 pista='andamio · primero un compás callada y después acompañando · despacio',
                 sistemas=[
                     dict(cap='a) la izquierda calla un compás entero y entra en el siguiente',
                          events=[sil('w'), n('B2', 'h'), n('F#3', 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) y ya con la melodía encima · la izquierda cae en el uno y en el tres',
                          events=[ac(('B2', 'B4')), n('A4'), ac(('F#3', 'G4')), n('F#4'),
                                  ac(('E2', 'E4')), n('F#4'), ac(('B2', 'G4')), n('A4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('Si menor', 'B3', 'B2', time_sig=(4, 4), variante=0,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
