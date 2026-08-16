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
    kicker=KICKER, esquina='Al piano · pasos 1 y 2 de 5',
    titulo='Cómo se estudia', page_num=7,
    time_sig=(3, 4), key_sig=TON, gap=7.0,
    intro='La izquierda hace SIEMPRE el mismo dibujo: fundamental, tercera, quinta, octava y de '
          'vuelta. No hay nada difícil de dedos. Lo difícil es que las seis corcheas suenen iguales, '
          'y por eso los dos primeros pasos son de izquierda sola.',
    reglas=['ARMADURA DE RE', 'LA IZQUIERDA SIEMPRE MÁS FLOJA', 'LEE EL CIFRADO, NO LA NOTA'],
    bloques=[
        dict(num=1, titulo='El acompañamiento, tal cual', clef='bass',
             pista='muy flojo y muy igual · sin marcar la primera nota de cada compás',
             sistemas=[
                 dict(cap='a) cc. 1–3 · Re mayor, Fa♯ menor, Si menor: el gesto de toda la canción',
                      events=MI_1_3, bars=3, clef='bass'),
                 dict(cap='b) La mayor, cuatro compases · es la dominante, donde la canción pide aire '
                          'y donde más se nota si aburre',
                      events=arpegio(*LA, n=4), bars=4, clef='bass', show_time=False),
                 dict(cap='c) cc. 1–3 y el La seguidos · así suena la primera frase entera, que es '
                          'lo que hay que tener antes de tocar nada con la derecha',
                      events=MI_1_3 + arpegio(*LA), bars=4, clef='bass', show_time=False),
                 dict(cap='d) los dos acordes del estribillo, cifrados G y A · el gesto es el mismo, '
                          'la mano se coloca en otro sitio',
                      events=arpegio('G2', 'B2', 'D3', 'G3', n=2) +
                             arpegio('A2', 'C3', 'E3', 'A3', n=2),
                      bars=4, clef='bass', show_time=False),
             ]),
        dict(tipo='nota',
             etiqueta='POR QUÉ ESTA CANCIÓN NO ES DE DEDOS',
             texto='El acorde roto tiende a marcar la primera corchea de cada compás, y en cuanto la '
                   'marcas la canción se convierte en un vals de verbena. Toca la izquierda mirando a '
                   'otro lado y pregúntate si alguna suena más fuerte. Casi siempre es la primera.'),
        dict(num=2, titulo='Quitarle el relleno', clef='bass',
             pista='el mismo material, desnudo · para oír por dónde va la armonía',
             sistemas=[
                 dict(cap='a) una nota por compás: Re · Fa♯ · Si · La · Re · Fa♯',
                      events=BAJO, bars=6, clef='bass'),
                 dict(cap='b) y ahora un acorde cada dos corcheas · el salto de mano es lo único '
                          'difícil que tiene esta mano',
                      events=[{'pitch': p, 'dur': 'e', 'beam': 500 + i // 2}
                              for i, p in enumerate(['D3', 'A3', 'F3', 'C4', 'B2', 'F3',
                                                     'A2', 'E3', 'D3', 'A3', 'F3', 'C4',
                                                     'B2', 'F3', 'A2', 'E3', 'D3', 'A3'])],
                      bars=3, clef='bass', show_time=False),
             ]),
    ],
)

PAG2 = dict(
    kicker=KICKER, esquina='Al piano · pasos 3, 4 y 5',
    titulo='Cómo se estudia (sigue)', page_num=8,
    time_sig=(3, 4), key_sig=TON, gap=7.0,
    intro='La izquierda ya está. Ahora la melodía —que en esta canción va pegada a la letra— y el '
          'mapa de toda la primera página. Esta canción no mejora yendo más rápido: mejora yendo '
          'más igual.',
    reglas=['CANTA LA LETRA MIENTRAS TOCAS', 'LA VOZ MANDA SOBRE LA MANO', 'PRIMERO IGUAL, LUEGO RÁPIDO'],
    bloques=[
        dict(num=3, titulo='La melodía sola',
             pista='cc. 1–3 · una nota por compás, y una sílaba para cada una',
             sistemas=[
                 dict(cap='a) “Wise — men — say”, y otra vez “Shall — I — stay”: misma melodía, dos letras',
                      events=MELODIA_1_3 + [dict(e) for e in MELODIA_1_3], bars=6),
             ]),
        dict(num=4, titulo='El mapa entero, leído del cifrado', clef='bass',
             pista='los cifrados los imprime la edición: son la armonía del editor, no un análisis mío',
             sistemas=[
                 dict(cap='a) D · F♯m · Bm · G · D · A · A7 · G · A · Bm · G · D — una nota por compás, '
                          'y léelo en voz alta antes de tocarlo',
                      events=[{'pitch': p, 'dur': 'h.'} for p in
                              ('D3', 'F3', 'B2', 'G2', 'D3', 'A2',
                               'A2', 'G2', 'A2', 'B2', 'G2', 'D3')],
                      bars=6, clef='bass'),
                 dict(cap='b) y el final, que se va de la tonalidad: F♯m · C♯7 · F♯m · C♯7',
                      events=[{'pitch': p, 'dur': 'h.'} for p in ('F3', 'C3', 'F3', 'C3')],
                      bars=4, clef='bass', show_time=False),
             ]),
        dict(tipo='nota',
             etiqueta='LA LETRA ES LA PARTITURA DE VERDAD',
             texto='Esta edición trae la letra debajo. Úsala: cada sílaba es una nota de la mano '
                   'derecha, y donde respira la frase cantada tiene que respirar la mano. Si cantas '
                   '“Wise men say” y luego tomas aire, ya sabes dónde acaba la primera frase sin que '
                   'nadie te lo marque.'),
        dict(num=5, titulo='Las dos manos · cc. 1–3',
             pista='este paso NO lleva pentagrama a propósito: se hace en la partitura de la página 1',
             sistemas=[]),
        dict(tipo='nota',
             etiqueta='CÓMO SE HACE EL PASO 5, Y EL FINAL',
             texto='Pon la izquierda de memoria, sin mirarla, y lee solo la línea de la derecha; si '
                   'para leer la melodía tienes que mirarte la izquierda, vuelve al paso 1. Y empieza '
                   'alguna vez por el estribillo, no siempre por el principio. Aparte: en la última '
                   'sección aparecen F♯m y C♯7, y ese Do♯7 no pertenece a Re mayor — trae un Mi♯ '
                   'escrito a mano. Ese trozo se monta aparte, despacio, marcando cada alteración '
                   'con lápiz antes de tocar.'),
        dict(tipo='escalera', valores=[50, 60, 69, 76, 84, 92],
             regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
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
