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

# la celula reducida a una sola vuelta por acorde: los enlaces, sin relleno
ENLACES = (corcheas(CELULA_I, 1) + corcheas(CELULA_ii, 1) +
           corcheas(CELULA_I7, 1) + corcheas(CELULA_I, 1))

PAG1 = dict(
    kicker=KICKER,
    esquina='Al piano · desmontar la pieza',
    titulo='Al piano · por partes',
    page_num=7,
    time_sig=(3, 4),
    key_sig=SOL,
    gap=7.0,
    intro='La partitura, abierta en trozos. Cada ejercicio dice de qué compases sale. Cuando los '
          'tengas, no hay ejercicio final: vuelves a la partitura de la página 1, que es donde '
          'de verdad se comprueba.',
    reglas=['ARMADURA DE SOL', 'LA IZQUIERDA SIEMPRE MÁS FLOJA', 'CUENTA LOS TRES TIEMPOS'],
    bloques=[
        dict(num=1, titulo='La mano izquierda sola',
             pista='cc. 1–8 tal cual · es el 90 % del trabajo de esta pieza',
             sistemas=[dict(cap='a)  ocho compases seguidos, sin parar, muy flojo y muy igual',
                            events=corcheas(CELULA_I, 4), bars=4, clef='bass'),
                       dict(cap='b)  cambia el acorde: La menor sobre Sol, y el Sol maj7 del c. 8',
                            events=corcheas(CELULA_ii, 3) + corcheas(CELULA_I7, 1),
                            bars=4, clef='bass')]),
        dict(num=2, titulo='El pedal desnudo',
             pista='el mismo bajo, sin arpegio · para oír que el Sol NO se mueve en 12 compases',
             sistemas=[dict(cap='una sola nota por compás: así suena el suelo sobre el que va todo',
                            events=PEDAL, bars=6, clef='bass')]),
        dict(num=3, titulo='Los enlaces, sin relleno',
             pista='la pieza repite cada acorde tres o cuatro compases · aquí cambias cada compás',
             sistemas=[dict(cap='Sol › La menor/Sol › Sol maj7 › Sol · el cambio es lo único difícil',
                            events=ENLACES, bars=4, clef='bass')]),
        dict(tipo='nota',
             etiqueta='POR QUÉ ESTA PIEZA NO ES DE DEDOS',
             texto='Técnicamente la izquierda no tiene nada raro: es un arpegio de tres notas que '
                   'se repite. Lo difícil es que suene igual 55 compases seguidos y por debajo de '
                   'la melodía. Eso no se arregla tocando más veces, se arregla escuchando: toca '
                   'la izquierda mirando a otro lado y pregúntate si alguna de las seis corcheas '
                   'suena más fuerte que las demás. Casi siempre es la primera.'),
        dict(num=4, titulo='La melodía sola',
             pista='cc. 3–4 · notas largas, y una digitación impresa que ya está pensada',
             sistemas=[dict(cap='cántala mientras la tocas · si no puedes cantarla, vas demasiado rápido',
                            events=MD_3_4, bars=2)]),
    ],
)

PAG2 = dict(
    kicker=KICKER,
    esquina='Al piano · montar la pieza',
    titulo='Al piano · montarla',
    page_num=8,
    time_sig=(3, 4),
    key_sig=SOL,
    gap=7.0,
    intro='La primera frase entera, la escala que la pieza lleva escondida dentro, y la forma de '
          'subir de velocidad sin ensuciarla. El tempo final es Andante ♩=96, no más.',
    reglas=['ANDANTE ♩=96 ES EL TECHO', 'RESPIRA DONDE ACABA LA LIGADURA', 'PRIMERO LIMPIO, LUEGO RÁPIDO'],
    bloques=[
        dict(num=5, titulo='La escala que la pieza lleva dentro',
             pista='cc. 7–9 · de Mi4 a Sol5 sin un solo salto, y termina en la nota más alta',
             sistemas=[dict(cap='la blanca del principio no es una pausa: es el impulso de la subida',
                            events=MD_7_9, bars=3)]),
        dict(tipo='nota',
             etiqueta='DÓNDE RESPIRA LA FRASE',
             texto='La edición trae las ligaduras de fraseo dibujadas: úsalas como marcas de '
                   'respiración. La primera frase va del c. 3 al c. 9 y respira al llegar al Sol5. '
                   'Toca la melodía sin piano, solo cantándola, y verás que respiras exactamente '
                   'donde acaba la ligadura. Si al piano respiras en otro sitio, la frase se parte.'),
        dict(num=6, titulo='Las dos manos, por fin',
             pista='cc. 1–4 en la partitura de la página 1 · aquí solo va la izquierda, de guía',
             sistemas=[dict(cap='monta la derecha encima leyendo de la partitura, no de esta hoja',
                            events=corcheas(CELULA_I, 4), bars=4, clef='bass')]),
        dict(tipo='nota',
             etiqueta='CÓMO ESTUDIARLA ESTA SEMANA',
             texto='1 · La izquierda sola, cc. 1–12, hasta que salga sin pensarla. '
                   '2 · La melodía sola, cantándola. '
                   '3 · Las dos manos solo los cc. 1–4, con la izquierda deliberadamente más '
                   'floja de lo que te parece necesario. '
                   '4 · Empieza por el c. 7, no por el 1: si siempre arrancas del principio, '
                   'acabarás tocando bien solo el principio.'),
        dict(tipo='escalera',
             valores=[48, 60, 72, 84, 92, 96],
             regla='SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        dict(tipo='tracker',
             titulo='La prueba de la semana',
             pie='Marca el día en que hayas tocado los cc. 1–12 enteros, sin parar y sin acelerar.'),
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
