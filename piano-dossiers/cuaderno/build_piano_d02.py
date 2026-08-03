# -*- coding: utf-8 -*-
"""Hojas al piano de Can't Help Falling in Love (Dilan, avanzado).

   Compases LITERALES, citados con su numero. Todo sale de
   TRANSCRIPCION_D02_CANT_HELP.md; lo que no esta medido no aparece.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import W, H
from hoja_piano import build_piano
from dilan_02_data import arpegio, RE, FAm, SIm, LA, MELODIA_1_3

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                          ' cant-help-falling-in-love-.pdf')
KICKER = 'Dilan · canción 2 · Can’t Help Falling in Love'
TON = 'Re mayor'

# los tres primeros compases, tal como estan escritos
MI_1_3 = arpegio(*RE) + arpegio(*FAm) + arpegio(*SIm)
# solo la fundamental de cada acorde: el esqueleto del bajo
BAJO = [{'pitch': p, 'dur': 'h.'} for p in ('D3', 'F3', 'B2', 'A2', 'D3', 'F3')]

PAG1 = dict(
    kicker=KICKER, esquina='Al piano · desmontar la pieza',
    titulo='Al piano · por partes', page_num=7,
    time_sig=(3, 4), key_sig=TON, gap=7.0,
    intro='La partitura, abierta en trozos. Cada ejercicio dice de qué compases sale. Cuando los '
          'tengas, vuelves a la partitura de la página 1: ahí es donde se comprueba.',
    reglas=['ARMADURA DE RE', 'LA IZQUIERDA SIEMPRE MÁS FLOJA', 'LEE EL CIFRADO, NO LA NOTA'],
    bloques=[
        dict(num=1, titulo='El acompañamiento, tal cual',
             pista='cc. 1–3 · Re mayor, Fa♯ menor, Si menor · es el gesto de toda la canción',
             sistemas=[dict(cap='tres compases seguidos, muy flojo y muy igual · sin marcar la primera nota',
                            events=MI_1_3, bars=3, clef='bass')]),
        dict(num=2, titulo='Solo el bajo',
             pista='la fundamental de cada acorde, sin el arpegio · para oír por dónde va la armonía',
             sistemas=[dict(cap='una nota por compás: Re · Fa♯ · Si · La · Re · Fa♯',
                            events=BAJO, bars=6, clef='bass')]),
        dict(tipo='nota',
             etiqueta='POR QUÉ ESTA CANCIÓN NO ES DE DEDOS',
             texto='La izquierda hace SIEMPRE el mismo dibujo: fundamental, tercera, quinta, octava y '
                   'de vuelta. No hay nada técnicamente difícil. Lo difícil es que las seis corcheas '
                   'suenen iguales: el acorde roto tiende a marcar la primera de cada compás, y en '
                   'cuanto la marcas la canción se convierte en un vals de verbena. Toca la izquierda '
                   'mirando a otro lado y pregúntate si alguna suena más fuerte. Casi siempre es la primera.'),
        dict(num=3, titulo='Los cambios, sin relleno',
             pista='la pieza da seis corcheas por acorde · aquí cambias de acorde cada dos',
             sistemas=[dict(cap='Re › Fa♯m › Sim › La y vuelta · el salto de mano es lo único difícil',
                            events=[{'pitch': p, 'dur': 'e', 'beam': 500 + i // 2}
                                    for i, p in enumerate(['D3', 'A3', 'F3', 'C4', 'B2', 'F3',
                                                           'A2', 'E3', 'D3', 'A3', 'F3', 'C4',
                                                           'B2', 'F3', 'A2', 'E3', 'D3', 'A3'])],
                            bars=3, clef='bass')]),
        dict(num=4, titulo='La melodía sola',
             pista='cc. 1–3 · una nota por compás, y una sílaba para cada una',
             sistemas=[dict(cap='“Wise — men — say” y otra vez “Shall — I — stay”: misma melodía, dos letras',
                            events=MELODIA_1_3 + [dict(e) for e in MELODIA_1_3], bars=6)]),
        dict(num=5, titulo='El bajo de toda la primera página',
             pista='de los cifrados: D · F♯m · Bm · G · D · A · A7 · G · A · Bm · G · D',
             sistemas=[dict(cap='una nota por compás, sin arpegio · esto es el mapa entero de la canción',
                            events=[{'pitch': p, 'dur': 'h.'} for p in
                                    ('D3', 'F3', 'B2', 'G2', 'D3', 'A2',
                                     'A2', 'G2', 'A2', 'B2', 'G2', 'D3')],
                            bars=6, clef='bass')]),
    ],
)

PAG2 = dict(
    kicker=KICKER, esquina='Al piano · montar la pieza',
    titulo='Al piano · montarla', page_num=8,
    time_sig=(3, 4), key_sig=TON, gap=7.0,
    intro='Las dos manos, la letra como guía de fraseo y la forma de subir de velocidad sin '
          'ensuciarla. Esta canción no mejora yendo más rápido: mejora yendo más igual.',
    reglas=['CANTA LA LETRA MIENTRAS TOCAS', 'LA VOZ MANDA SOBRE LA MANO', 'PRIMERO IGUAL, LUEGO RÁPIDO'],
    bloques=[
        dict(num=5, titulo='El acompañamiento de la segunda frase',
             pista='La mayor · es la dominante, y es donde la canción pide aire',
             sistemas=[dict(cap='cuatro compases sobre el mismo acorde: el reto es que no aburra',
                            events=arpegio(*LA, n=4), bars=4, clef='bass')]),
        dict(tipo='nota',
             etiqueta='LA LETRA ES LA PARTITURA DE VERDAD',
             texto='Esta edición trae la letra debajo. Úsala: cada sílaba es una nota de la mano '
                   'derecha, y donde respira la frase cantada es donde tiene que respirar la mano. '
                   'Si cantas “Wise men say” y luego tomas aire, ya sabes dónde acaba la primera '
                   'frase sin necesidad de que nadie te lo marque. Y los cifrados de encima te dicen '
                   'dónde estás: léelos en voz alta antes de tocar.'),
        dict(tipo='nota',
             etiqueta='LAS DOS MANOS · CC. 1–3',
             texto='Sin pentagrama a propósito: se hace en la partitura de la página 1. Pon la '
                   'izquierda de memoria, sin mirarla, y lee solo la línea de la derecha. Si para '
                   'leer la melodía tienes que mirarte la izquierda, vuelve al ejercicio 1.'),
        dict(tipo='nota',
             etiqueta='CÓMO ESTUDIARLA ESTA SEMANA',
             texto='1 · La izquierda sola de los cc. 1–3, hasta que no tengas que pensarla. '
                   '2 · Los cifrados en voz alta, sin tocar: Re, Fa♯ menor, Si menor, La… '
                   '3 · Las dos manos solo los cc. 1–3, con la izquierda más floja de lo que te '
                   'parece necesario. '
                   '4 · Empieza alguna vez por el estribillo, no siempre por el principio.'),
        dict(num=6, titulo='Los dos acordes del estribillo',
             pista='cifrados G y A · el gesto es el mismo, pero la mano se coloca en otro sitio',
             sistemas=[dict(cap='dos compases sobre Sol y dos sobre La · cambia sin mirarte la mano',
                            events=arpegio('G2', 'B2', 'D3', 'G3', n=2) +
                                   arpegio('A2', 'C3', 'E3', 'A3', n=2),
                            bars=4, clef='bass')]),
        dict(tipo='nota',
             etiqueta='EL FINAL SE VA DE LA TONALIDAD',
             texto='En la última sección aparecen F♯m y C♯7, y ese Do♯7 no pertenece a Re mayor: trae '
                   'un Mi♯ que no está en la armadura y que la edición escribe a mano. No lo estudies '
                   'con la primera página: móntalo aparte, despacio, y marca con lápiz cada alteración '
                   'antes de tocar. Es el único sitio de la canción donde hace falta leer de verdad.'),
        dict(tipo='escalera', valores=[50, 60, 69, 76, 84, 92],
             regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        dict(tipo='tracker', titulo='La prueba de la semana',
             pie='Marca el día en que hayas tocado la primera página entera, cantando la letra.'),
    ],
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = os.path.join(HERE, '_p2_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_piano(c, PAG1); build_piano(c, PAG2); c.save()
    wr = PdfWriter()
    for p in PdfReader(tmp).pages: wr.add_page(p)
    for p in PdfReader(SOURCE_PDF).pages: wr.add_page(p)
    out = os.path.join(OUT_DIR, 'Dilan_02_Al_Piano_y_Partitura.pdf')
    with open(out, 'wb') as f: wr.write(f)
    os.remove(tmp); print('generated', out)


if __name__ == '__main__':
    main()
