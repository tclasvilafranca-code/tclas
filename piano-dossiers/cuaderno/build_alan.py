# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Alan.

   Formato ADULTO (seis hojas por pieza), en su versión EXIGENTE (reto, escalera,
   cifrado donde la edición lo trae, cuatro manos en los duetos), con tono de
   doce años. Alan es un niño con base musical y muy exigente consigo mismo: lleva
   23 piezas, sus 23 partituras de Drive, todas.

   Los cuatro duetos (Romance, Bella Ciao, The Beginner y Scherzo) se ven
   abiertos: `ensamblar.anadir_dosier` intercala una hoja de pauta delante cuando
   la partitura caería empezando en página impar.

   Antes de ejecutarlo tiene que salir TODO OK en auditar_alan.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import build_cover, build_index, build_plan_curso, W, H
from ensamblar import anadir_dosier

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')
OUT_DIR = os.path.join(HERE, '..', 'output')

ALUMNO = 'Alan'
SUBTITULO = 'Veintitrés piezas'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('Empezar con lo conocido', 'canciones que ya suenan, con un dueto para tocar con alguien', [
        dict(num=1, titulo='Counting Stars', autor='OneRepublic · arr. Becky Messer',
             tonalidad='Do mayor', compas='4/4', trabaja='Cuatro compases seguidos sin mirarte las manos'),
        dict(num=2, titulo='Romance', autor='Anton Diabelli · Primo, a cuatro manos',
             tonalidad='Do mayor', compas='2/2', trabaja='Sonar como una sola mano con la otra persona'),
        dict(num=3, titulo='Heart and Soul', autor='Hoagy Carmichael · versión fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='El bajo con acorde, que ande solo'),
        dict(num=4, titulo='Tetris', autor='Korobeiniki · canción popular rusa',
             tonalidad='Sin armadura', compas='4/4', trabaja='La izquierda sin parar mientras la derecha canta'),
    ]),
    ('Vals, contratiempos y Navidad', 'entrar donde no suena el clic, y tres villancicos de diciembre', [
        dict(num=5, titulo='Up · tema principal', autor='Michael Giacchino · Easy version',
             tonalidad='Fa mayor', compas='3/4', trabaja='Entrar bien tras los dos silencios, tranquilo'),
        dict(num=6, titulo='Boig per tu', autor='Sau · arr. Pilar Sanz',
             tonalidad='Sin armadura', compas='4/4', trabaja='Entrar a tiempo y medio, donde no hay clic'),
        dict(num=7, titulo='White Christmas', autor='Irving Berlin · versión de Musescore',
             tonalidad='Do mayor', compas='4/4', trabaja='Respirar la frase y el giro del Mi bemol'),
        dict(num=8, titulo='Santa Claus Is Coming to Town', autor='J. Fred Coots',
             tonalidad='Do mayor', compas='4/4', trabaja='Llegar a ♩ = 130 sin atropellar las corcheas'),
        dict(num=9, titulo='Have Yourself a Merry Little Christmas', autor='Martin y Blane · arr. Sadie King',
             tonalidad='Do mayor', compas='4/4', trabaja='El sonido unido y el pedal limpio'),
    ]),
    ('Ritmo y resistencia', 'ostinatos que no se aceleran y silencios que se cuentan', [
        dict(num=10, titulo='Bella Ciao', autor='popular italiana · a cuatro manos',
             tonalidad='Sol menor', compas='4/4', trabaja='Aguantar el pulso cuando tu compañero toca poco'),
        dict(num=11, titulo='Eye of the Tiger', autor='Survivor · arr. Sadie King',
             tonalidad='Sin armadura', compas='4/4', trabaja='El largo-largo-corto, igual las seis veces'),
        dict(num=12, titulo="Can't Stop the Feeling!", autor='Justin Timberlake · versión fácil',
             tonalidad='Sin armadura', compas='4/4', trabaja='Entrar a tiempo tras los silencios largos'),
        dict(num=13, titulo='Lovely', autor='Billie Eilish con Khalid · arr. Amy Kieran',
             tonalidad='Mi menor', compas='4/4', trabaja='Ocho corcheas iguales durante diez compases'),
    ]),
    ('Compases distintos y notas que vuelven', 'el vals, el 6/8 y las piezas que se repiten', [
        dict(num=14, titulo='Para Elisa', autor='Ludwig van Beethoven',
             tonalidad='La menor', compas='3/4', trabaja='La oscilación del arranque, liviana y sin prisa'),
        dict(num=15, titulo='The Beginner', autor='Cornelius Gurlitt · a cuatro manos',
             tonalidad='Do mayor', compas='3/4', trabaja='Contar tres y no cuatro, entre dos'),
        dict(num=16, titulo='A Thousand Years', autor='Hodges y Perri · arr. Piano Seeds STUDIO',
             tonalidad='Sin armadura', compas='6/8', trabaja='Contar en dos, no en seis'),
        dict(num=17, titulo='Viva la Vida', autor='Coldplay · versión Easy Piano',
             tonalidad='Sin armadura', compas='4/4', trabaja='La izquierda de corcheas y silencios, sin acelerar'),
    ]),
    ('Acordes, cifrado y silencios', 'canciones que se estudian por acordes y se tocan con el silencio', [
        dict(num=18, titulo='Someone You Loved', autor='Lewis Capaldi · Bye Bye Beethoven',
             tonalidad='Sin armadura', compas='4/4', trabaja='El arpegio parejo mientras la izquierda aguanta'),
        dict(num=19, titulo='Perfect', autor='Ed Sheeran · arr. Bye Bye Beethoven',
             tonalidad='Sol mayor', compas='12/8', trabaja='Contar el 12/8 en cuatro y no en doce'),
        dict(num=20, titulo='What Was I Made For?', autor='Billie Eilish · versión de Musescore',
             tonalidad='Do mayor', compas='4/4', trabaja='Tres compases de silencio y la entrada a tiempo'),
        dict(num=21, titulo='Shallow', autor='Lady Gaga y Bradley Cooper · Bye Bye Beethoven',
             tonalidad='Mi menor', compas='4/4', trabaja='Corcheas iguales y dos semicorcheas'),
    ]),
    ('Los dos retos del final', 'aquí el cuaderno deja de ser cómodo, y a propósito', [
        dict(num=22, titulo='Scherzo', autor='Anton Diabelli · a cuatro manos',
             tonalidad='Do mayor', compas='3/4', trabaja='El staccato corto, el p y el f, y el Trio con tres bemoles'),
        dict(num=23, titulo='Interstellar', autor='Hans Zimmer · Bye Bye Beethoven',
             tonalidad='Sin armadura', compas='3/4', trabaja='Seis corcheas iguales durante cien compases'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# 23 piezas en 43 semanas más la audición: tres piezas de una semana (Santa
# Claus, Have Yourself y The Beginner, las más cortas) y veinte de dos. Los tres
# villancicos van juntos en diciembre.
PLAN = [
    ('Septiembre', [
        (1, '1 · Counting Stars — cuatro compases sin mirar', 'obra'),
        (2, '1 · Counting Stars — las corcheas del c. 3', 'obra'),
        (3, '2 · Romance — las dos manos exactamente juntas', 'obra'),
        (4, '2 · Romance — el dúo con la otra persona', 'obra'),
    ]),
    ('Octubre', [
        (5, '3 · Heart and Soul — el bajo con acorde', 'obra'),
        (6, '3 · Heart and Soul — el ritmo con swing', 'obra'),
        (7, '4 · Tetris — la izquierda sola, sin parar', 'obra'),
        (8, '4 · Tetris — la melodía encima', 'obra'),
    ]),
    ('Noviembre', [
        (9, '5 · Up — la entrada tras los dos silencios', 'obra'),
        (10, '5 · Up — el cambio de clave del c. 18', 'obra'),
        (11, '6 · Boig per tu — entrar a tiempo y medio', 'obra'),
        (12, '6 · Boig per tu — el Fa♯ y la balada entera', 'obra'),
    ]),
    ('Diciembre', [
        (13, '7 · White Christmas — el giro del Mi♭', 'especial'),
        (14, '7 · White Christmas — el cifrado', 'especial'),
        (15, '8 · Santa Claus Is Coming to Town — hasta ♩ = 130', 'especial'),
        (16, '9 · Have Yourself a Merry Little Christmas — el sonido unido', 'especial'),
    ]),
    ('Enero', [
        (17, '10 · Bella Ciao — el tono menor, con la profesora', 'obra'),
        (18, '10 · Bella Ciao — el dúo, con metrónomo', 'obra'),
        (19, '11 · Eye of the Tiger — el largo-largo-corto', 'obra'),
        (20, '11 · Eye of the Tiger — las semicorcheas del c. 5', 'obra'),
    ]),
    ('Febrero', [
        (21, "12 · Can't Stop the Feeling! — contar los silencios", 'obra'),
        (22, "12 · Can't Stop the Feeling! — las dos manos alternándose", 'obra'),
        (23, '13 · Lovely — el arpegio de los diez primeros compases', 'obra'),
        (24, '13 · Lovely — la melodía y las semicorcheas', 'obra'),
    ]),
    ('Marzo', [
        (25, '14 · Para Elisa — el arranque liviano', 'obra'),
        (26, '14 · Para Elisa — la semicorchea del c. 20', 'obra'),
        (27, '15 · The Beginner — contar tres, entre dos', 'obra'),
        (28, '16 · A Thousand Years — contar en dos', 'obra'),
    ]),
    ('Abril', [
        (29, '16 · A Thousand Years — las tres corcheas que bajan', 'obra'),
        (30, '17 · Viva la Vida — la izquierda sola', 'obra'),
        (31, '17 · Viva la Vida — la derecha y las repeticiones', 'obra'),
        (32, '18 · Someone You Loved — las graves y las agudas', 'obra'),
    ]),
    ('Mayo', [
        (33, '18 · Someone You Loved — la repetición con casillas y el 8va', 'obra'),
        (34, '19 · Perfect — contar en cuatro', 'obra'),
        (35, '19 · Perfect — el cifrado y la anacrusa', 'obra'),
        (36, '20 · What Was I Made For? — la entrada del c. 4', 'obra'),
    ]),
    ('Junio', [
        (37, '20 · What Was I Made For? — la figura con ligadura', 'obra'),
        (38, '21 · Shallow — las corcheas del c. 3', 'obra'),
        (39, '21 · Shallow — el estribillo y las semicorcheas', 'obra'),
        (40, '22 · Scherzo — el staccato y el p y f', 'obra'),
    ]),
    ('Julio', [
        (41, '22 · Scherzo — el Trio y la vuelta D.C. al Fine', 'obra'),
        (42, '23 · Interstellar — el arpegio y el mapa de la pieza', 'obra'),
        (43, '23 · Interstellar — la melodía, y cien compases', 'obra'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]

NOTA_PLAN = ('Las 44 semanas del curso, repartidas. Los tres villancicos y The Beginner, que son los '
             'más cortos, llevan una semana; las demás piezas, dos. De cada una te llevas la hoja de '
             'trabajo con el plan de minutos y, según la pieza, el reto de la semana, la escalera '
             'del metrónomo, el cifrado o lo que haya que acordar con la otra persona. Es una '
             'propuesta, no una obligación: si una pieza pide una semana más, se le da, y si sale '
             'antes, se pasa a la siguiente.')

DOSIERES = [
    'Alan_01_CountingStars_CUADERNO.pdf',
    'Alan_02_RomanceDiabelli_CUADERNO.pdf',
    'Alan_03_HeartAndSoul_CUADERNO.pdf',
    'Alan_04_Tetris_CUADERNO.pdf',
    'Alan_05_Up_CUADERNO.pdf',
    'Alan_06_BoigPerTu_CUADERNO.pdf',
    'Alan_07_WhiteChristmas_CUADERNO.pdf',
    'Alan_08_SantaClaus_CUADERNO.pdf',
    'Alan_09_HaveYourself_CUADERNO.pdf',
    'Alan_10_BellaCiao_CUADERNO.pdf',
    'Alan_11_EyeOfTheTiger_CUADERNO.pdf',
    'Alan_12_CantStop_CUADERNO.pdf',
    'Alan_13_Lovely_CUADERNO.pdf',
    'Alan_14_ParaElisa_CUADERNO.pdf',
    'Alan_15_Beginner_CUADERNO.pdf',
    'Alan_16_AThousandYears_CUADERNO.pdf',
    'Alan_17_VivaLaVida_CUADERNO.pdf',
    'Alan_18_SomeoneYouLoved_CUADERNO.pdf',
    'Alan_19_Perfect_CUADERNO.pdf',
    'Alan_20_WhatWasIMadeFor_CUADERNO.pdf',
    'Alan_21_Shallow_CUADERNO.pdf',
    'Alan_22_Scherzo_CUADERNO.pdf',
    'Alan_23_Interstellar_CUADERNO.pdf',
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Alan_Portada_Indice.pdf')
    c = canvas.Canvas(tapas, pagesize=(W, H))
    build_cover(c, os.path.join(ASSETS, 'asset_logo_tclas_v2.png'), ALUMNO, SUBTITULO, CURSO)
    pag = build_index(c, ALUMNO, ETAPAS)
    build_plan_curso(c, ALUMNO, PLAN, page_num=pag + 1, nota=NOTA_PLAN)
    c.save()

    wr = PdfWriter()
    for p in PdfReader(tapas).pages:
        wr.add_page(p)
    faltan = []
    for nombre in DOSIERES:
        ruta = os.path.join(OUT_DIR, nombre)
        if not os.path.exists(ruta):
            faltan.append(nombre)
            continue
        if anadir_dosier(wr, ruta):
            print('  %s: hoja de pauta intercalada para que el dúo se vea abierto' % nombre)
    out = os.path.join(OUT_DIR, 'Alan_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
