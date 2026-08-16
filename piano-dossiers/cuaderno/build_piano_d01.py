# -*- coding: utf-8 -*-
"""Hojas de trabajo al piano de El Cisne, para Dilan (nivel avanzado).

   Todos los compases salen de TRANSCRIPCION_D01_EL_CISNE.md. La sección
   central (cc. 13-42) no se cita nota a nota porque no se ha medido: los
   ejercicios trabajan la primera frase y el mecanismo, que es lo que se
   repite en toda la pieza.

   El paso de REINSERTAR aquí no necesita pentagrama propio: la partitura
   está en la página 1 del dosier, y a este nivel lo correcto es mandar al
   alumno a la obra, no a una copia.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import W, H
from hoja_piano import build_piano
from dilan_01_data import corcheas, CELULA_I, CELULA_ii, CELULA_I7, MD_3_4, MD_7_9

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')
SOURCE_PDF = os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN', 'the-swan.pdf')

KICKER = 'Dilan · canción 1 · El Cisne'
SOL = 'Sol mayor'

# solo el bajo de cada compas: quita el arpegio y deja el pedal desnudo
PEDAL = [{'pitch': 'G2', 'dur': 'h.'} for _ in range(6)]

# los cc. 7-9 con todas las notas iguales de largas: mismas alturas medidas,
# ritmo aplanado, solo para colocar la mano antes de ponerle la figuracion
ESCALA_LISA = ([{'pitch': 'E4', 'dur': 'h'}] +
               [{'pitch': p, 'dur': 'q'} for p in
                ['F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']] +
               [{'pitch': 'G5', 'dur': 'h'}])          # 12 tiempos = 4 compases

# la celula reducida a una sola vuelta por acorde: los enlaces, sin relleno
ENLACES = (corcheas(CELULA_I, 1) + corcheas(CELULA_ii, 1) +
           corcheas(CELULA_I7, 1) + corcheas(CELULA_I, 1))

PAG1 = dict(
    kicker=KICKER,
    esquina='Al piano · pasos 1 y 2 de 5',
    titulo='Cómo se estudia',
    page_num=7,
    time_sig=(3, 4),
    key_sig=SOL,
    gap=7.0,
    intro='Esta pieza no es de dedos: la izquierda no tiene nada raro, un arpegio de tres notas que '
          'se repite. Lo difícil es que suene igual durante 55 compases y por debajo de la melodía. '
          'Por eso los dos primeros pasos son solo de izquierda, y son el 90 % del trabajo.',
    reglas=['ARMADURA DE SOL', 'LA IZQUIERDA SIEMPRE MÁS FLOJA', 'CUENTA LOS TRES TIEMPOS'],
    bloques=[
        dict(num=1, titulo='La izquierda sola, los ocho primeros compases',
             pista='cc. 1–8 tal cual · muy flojo y muy igual, sin que ninguna corchea pese más',
             sistemas=[
                 dict(cap='a) cc. 1–4 · Sol mayor: la célula, cuatro veces sin cambiar nada',
                      events=corcheas(CELULA_I, 4), bars=4, clef='bass'),
                 dict(cap='b) cc. 5–8 · La menor sobre Sol, y el Sol maj7 del c. 8',
                      events=corcheas(CELULA_ii, 3) + corcheas(CELULA_I7, 1),
                      bars=4, clef='bass', show_time=False),
                 dict(cap='c) los ocho seguidos, sin parar entre el 4 y el 5 · así es como va',
                      events=corcheas(CELULA_I, 4) + corcheas(CELULA_ii, 3) + corcheas(CELULA_I7, 1),
                      bars=4, clef='bass', show_time=False),
             ]),
        dict(tipo='nota',
             etiqueta='POR QUÉ ESTA PIEZA NO ES DE DEDOS',
             texto='Toca la izquierda mirando a otro lado y pregúntate si alguna corchea suena más '
                   'fuerte que las demás. Casi siempre es la primera, y casi siempre es la que '
                   'estropea la pieza. Eso no se arregla tocándola más veces: se arregla oyéndola.'),
        dict(num=2, titulo='Quitarle el relleno: el suelo y los cambios',
             pista='el mismo material, desnudo · para oír que el Sol NO se mueve en doce compases',
             sistemas=[
                 dict(cap='a) una sola nota por compás: el suelo sobre el que va todo lo demás',
                      events=PEDAL, bars=6, clef='bass'),
                 dict(cap='b) y ahora un acorde por compás · el cambio es lo único difícil de esta mano',
                      events=ENLACES, bars=4, clef='bass', show_time=False),
             ]),
    ],
)

PAG2 = dict(
    kicker=KICKER,
    esquina='Al piano · pasos 3, 4 y 5',
    titulo='Cómo se estudia (sigue)',
    page_num=8,
    time_sig=(3, 4),
    key_sig=SOL,
    gap=7.0,
    intro='La izquierda ya está. Ahora la melodía, que en esta pieza son notas largas y una escala '
          'que sube entera, y después juntar las dos manos. El tempo final es Andante ♩=96, no más.',
    reglas=['ANDANTE ♩=96 ES EL TECHO', 'RESPIRA DONDE ACABA LA LIGADURA', 'PRIMERO LIMPIO, LUEGO RÁPIDO'],
    bloques=[
        dict(num=3, titulo='La melodía sola',
             pista='cc. 3–4 y cc. 7–9 · cántala mientras la tocas: si no puedes cantarla, vas rápido',
             sistemas=[
                 dict(cap='a) cc. 3–4 · notas largas, con la digitación que ya trae la edición',
                      events=MD_3_4, bars=2),
                 dict(cap='b) cc. 7–9 · de Mi4 a Sol5 sin un solo salto · la blanca del principio no '
                          'es una pausa, es el impulso de la subida',
                      events=MD_7_9, bars=3, show_time=False),
                 dict(cap='c) las mismas notas de los cc. 7–9, todas iguales de largas · solo para '
                          'colocar los dedos antes de ponerles el ritmo',
                      events=ESCALA_LISA, bars=4, show_time=False),
             ]),
        dict(tipo='nota',
             etiqueta='DÓNDE RESPIRA LA FRASE',
             texto='La edición trae las ligaduras de fraseo dibujadas: úsalas como marcas de '
                   'respiración. La primera frase va del c. 3 al c. 9 y respira al llegar al Sol5. '
                   'Canta la melodía sin piano y verás que respiras exactamente donde acaba la '
                   'ligadura. Si al piano respiras en otro sitio, la frase se parte.'),
        dict(num=4, titulo='Las dos manos · cc. 1–4', clef='bass',
             pista='este paso NO lleva pentagrama a propósito: se hace en la partitura de la página 1',
             sistemas=[]),
        dict(tipo='nota',
             etiqueta='CÓMO SE HACE EL PASO 4',
             texto='Coloca la izquierda de memoria, sin mirártela, y lee solo la línea de la derecha. '
                   'Si para leer la melodía necesitas mirar la mano izquierda, es que todavía no está '
                   'lista: vuelve al paso 1. Y empieza por el c. 7, no por el 1 — si siempre arrancas '
                   'del principio, acabarás tocando bien solo el principio.'),
        dict(tipo='nota',
             etiqueta='LA FORMA, MEDIDA COMPÁS A COMPÁS',
             texto='A · cc. 1–12: el tema, sobre un Sol que no se mueve. B · cc. 13–34: modula y se '
                   'llena de alteraciones; esa parte no se cita aquí porque no la he medido nota por '
                   'nota. A\' · cc. 35–55: vuelve el tema, y los cc. 35 y 36 son idénticos a los cc. 3 '
                   'y 4 en las dos manos, comprobado. Cuando llegues al 35 no aprendes nada nuevo.'),
        dict(tipo='escalera',
             valores=[48, 60, 72, 84, 92, 96],
             regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
    ],
)

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = os.path.join(HERE, '_pd_tmp.pdf')
    c = canvas.Canvas(tmp, pagesize=(W, H))
    build_piano(c, PAG1)
    build_piano(c, PAG2)
    c.save()
    wr = PdfWriter()
    for p in PdfReader(tmp).pages: wr.add_page(p)
    for p in PdfReader(SOURCE_PDF).pages: wr.add_page(p)
    out = os.path.join(OUT_DIR, 'Dilan_01_Al_Piano_y_Partitura.pdf')
    with open(out, 'wb') as f: wr.write(f)
    os.remove(tmp)
    print('generated', out)


if __name__ == '__main__':
    main()
