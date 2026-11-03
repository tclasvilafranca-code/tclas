# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Martina.

   Formato ADULTO (seis hojas por pieza), en su versión EXIGENTE (reto, escalera,
   cifrado donde la edición lo trae, cuatro manos en los duetos), con tono de
   niña de diez a doce años que empieza de cero: las primeras piezas enseñan a
   leer y el nivel sube hasta Merry-go-round of Life y The Entertainer, que son las
   dos últimas. Lleva 24 piezas, sus 24 partituras de Drive, todas, ordenadas de
   la más fácil a la más difícil.

   Los seis duetos (Sonatina per bambini, Romance, The Beginner, Sonatina nº 2,
   Bella Ciao y Scherzo) se ven abiertos: `ensamblar.anadir_dosier` intercala una
   hoja de pauta delante cuando la partitura caería empezando en página impar.

   Antes de ejecutarlo tiene que salir TODO OK en auditar_todo.py martina.
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

ALUMNO = 'Martina'
SUBTITULO = 'Veinticuatro piezas'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('Empezar de cero', 'las notas, el pentagrama y las figuras, con tres duetos para tocar con alguien', [
        dict(num=1, titulo='Sonatina per bambini', autor='Maurizio Bazzoni · a cuatro manos',
             tonalidad='La menor', compas='4/4', trabaja='Que las dos manos bajen exactamente a la vez'),
        dict(num=2, titulo='Heart and Soul', autor='Hoagy Carmichael · versión fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='El bajo con acorde, que ande solo'),
        dict(num=3, titulo='Romance', autor='Anton Diabelli · Primo, a cuatro manos',
             tonalidad='Do mayor', compas='2/2', trabaja='Sonar como una sola mano con la otra persona'),
        dict(num=4, titulo='The Beginner', autor='Cornelius Gurlitt · a cuatro manos',
             tonalidad='Do mayor', compas='3/4', trabaja='Contar tres y no cuatro, entre dos'),
    ]),
    ('Melodías y villancicos', 'corcheas, cifrado y el vals de la Navidad', [
        dict(num=5, titulo='Counting Stars', autor='OneRepublic · arr. Becky Messer',
             tonalidad='Do mayor', compas='4/4', trabaja='Seguir cuando las negras se convierten en corcheas'),
        dict(num=6, titulo='Greensleeves', autor='canción popular inglesa',
             tonalidad='La menor', compas='3/4', trabaja='Leer el cifrado y el arpegio a la vez'),
        dict(num=7, titulo='Silent Night', autor='Franz Gruber · versión de Piano Moonlight',
             tonalidad='Do mayor', compas='3/4', trabaja='Contar tres y no cuatro'),
        dict(num=8, titulo='We Wish You a Merry Christmas', autor='villancico inglés · arr. G. DeBenedetti',
             tonalidad='Sol mayor', compas='3/4', trabaja='Entrar a tiempo con una sola nota'),
    ]),
    ('Navidad, un dueto y los Beatles', 'cantar la frase mientras suena, y un molde que se repite', [
        dict(num=9, titulo='White Christmas', autor='Irving Berlin · versión de Musescore',
             tonalidad='Do mayor', compas='4/4', trabaja='Cantar la frase mientras la tocas'),
        dict(num=10, titulo='Have Yourself a Merry Little Christmas', autor='Martin y Blane · arr. Sadie King',
             tonalidad='Do mayor', compas='4/4', trabaja='El sonido unido, sin cortes entre notas'),
        dict(num=11, titulo='Sonatina nº 2', autor='Maurizio Bazzoni · en Sol mayor, a cuatro manos',
             tonalidad='Sol mayor', compas='4/4', trabaja='El Fa♯ de la armadura, sin que se escape'),
        dict(num=12, titulo='El submarino amarillo', autor='Lennon y McCartney · arr. A. C. Escobés',
             tonalidad='Sol mayor', compas='4/4', trabaja='Que las notas repetidas no se aceleren'),
    ]),
    ('Entrar tarde, tonos menores y staccato', 'silencios que se cuentan, dos bemoles y dos duetos', [
        dict(num=13, titulo='I Have a Dream', autor='Abba · INeVENT Music Academy',
             tonalidad='Do mayor', compas='4/4', trabaja='Entrar en el dos sin adelantarte'),
        dict(num=14, titulo='Bella Ciao', autor='popular italiana · a cuatro manos',
             tonalidad='Sol menor', compas='4/4', trabaja='Aguantar el pulso cuando tu compañero toca poco'),
        dict(num=15, titulo='Scherzo', autor='Anton Diabelli · a cuatro manos',
             tonalidad='Do mayor', compas='3/4', trabaja='El staccato corto y el salto de p a f'),
        dict(num=16, titulo='Titanic', autor='James Horner · arr. A. C. Escobés',
             tonalidad='Do mayor', compas='2/4', trabaja='Que la línea no se corte entre compases'),
    ]),
    ('Arpegios, silencios y un clásico', 'notas que no se aceleran y tres compases de espera', [
        dict(num=17, titulo='Lovely', autor='Billie Eilish con Khalid · arr. Amy Kieran',
             tonalidad='Mi menor', compas='4/4', trabaja='Ocho corcheas iguales durante diez compases'),
        dict(num=18, titulo='Interstellar', autor='Hans Zimmer · Bye Bye Beethoven',
             tonalidad='Sin armadura', compas='3/4', trabaja='Seis corcheas iguales, y el mapa de cien compases'),
        dict(num=19, titulo='What Was I Made For?', autor='Billie Eilish · versión de Musescore',
             tonalidad='Do mayor', compas='4/4', trabaja='Tres compases de silencio y la entrada a tiempo'),
        dict(num=20, titulo='Para Elisa', autor='Ludwig van Beethoven',
             tonalidad='La menor', compas='3/4', trabaja='La oscilación del arranque, liviana y sin prisa'),
    ]),
    ('Los cuatro retos del final', 'doce corcheas por compás, dos tempos y un rag', [
        dict(num=21, titulo='Perfect', autor='Ed Sheeran · arr. Bye Bye Beethoven',
             tonalidad='Sol mayor', compas='12/8', trabaja='Contar el 12/8 en cuatro y no en doce'),
        dict(num=22, titulo='Shallow', autor='Lady Gaga y Bradley Cooper · Bye Bye Beethoven',
             tonalidad='Mi menor', compas='4/4', trabaja='Corcheas iguales y dos semicorcheas'),
        dict(num=23, titulo='Merry-go-round of Life', autor='Joe Hisaishi · para piano solo',
             tonalidad='Si bemol mayor', compas='3/4', trabaja='Las terceras de la entrada y los dos tempos'),
        dict(num=24, titulo='The Entertainer', autor='Scott Joplin · arr. G. DeBenedetti',
             tonalidad='Do mayor', compas='2/2', trabaja='El bajo que salta y el staccato corto'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# 24 piezas en 43 semanas más la audición: cinco piezas de una semana (los cuatro
# villancicos de diciembre y la Sonatina nº 2, las más cortas) y diecinueve de
# dos. Los villancicos van juntos en diciembre. Las primeras piezas llevan dos
# semanas porque Martina empieza de cero.
PLAN = [
    ('Septiembre', [
        (1, '1 · Sonatina per bambini — el pentagrama y los nombres de las notas', 'obra'),
        (2, '1 · Sonatina per bambini — las dos manos juntas, con alguien', 'obra'),
        (3, '2 · Heart and Soul — el bajo con acorde', 'obra'),
        (4, '2 · Heart and Soul — que ande solo', 'obra'),
    ]),
    ('Octubre', [
        (5, '3 · Romance — las dos manos exactamente juntas', 'obra'),
        (6, '3 · Romance — el dúo con la otra persona', 'obra'),
        (7, '4 · The Beginner — contar tres, no cuatro', 'obra'),
        (8, '4 · The Beginner — el dúo, con metrónomo', 'obra'),
    ]),
    ('Noviembre', [
        (9, '5 · Counting Stars — los tres primeros compases', 'obra'),
        (10, '5 · Counting Stars — las corcheas', 'obra'),
        (11, '6 · Greensleeves — el cifrado y el arpegio', 'obra'),
        (12, '6 · Greensleeves — la pieza entera', 'obra'),
    ]),
    ('Diciembre', [
        (13, '7 · Silent Night — contar tres', 'especial'),
        (14, '8 · We Wish You a Merry Christmas — entrar con una sola nota', 'especial'),
        (15, '9 · White Christmas — cantar la frase mientras la tocas', 'especial'),
        (16, '10 · Have Yourself a Merry Little Christmas — el sonido unido', 'especial'),
    ]),
    ('Enero', [
        (17, '11 · Sonatina nº 2 — el Fa♯ de la armadura', 'obra'),
        (18, '12 · El submarino amarillo — el molde de la izquierda', 'obra'),
        (19, '12 · El submarino amarillo — las notas repetidas', 'obra'),
        (20, '13 · I Have a Dream — entrar en el dos', 'obra'),
    ]),
    ('Febrero', [
        (21, '13 · I Have a Dream — la ligadura y la semicorchea', 'obra'),
        (22, '14 · Bella Ciao — el tono menor y el Mi♭', 'obra'),
        (23, '14 · Bella Ciao — el dúo con la repetición', 'obra'),
        (24, '15 · Scherzo — el staccato corto', 'obra'),
    ]),
    ('Marzo', [
        (25, '15 · Scherzo — el Trio y la vuelta D.C. al Fine', 'obra'),
        (26, '16 · Titanic — la semicorchea del c. 1', 'obra'),
        (27, '16 · Titanic — la línea larga del segundo bloque', 'obra'),
        (28, '17 · Lovely — el arpegio de los diez primeros compases', 'obra'),
    ]),
    ('Abril', [
        (29, '17 · Lovely — la melodía y las semicorcheas', 'obra'),
        (30, '18 · Interstellar — el arpegio y el mapa de la pieza', 'obra'),
        (31, '18 · Interstellar — la melodía de los cc. 12-15', 'obra'),
        (32, '19 · What Was I Made For? — la entrada del c. 4', 'obra'),
    ]),
    ('Mayo', [
        (33, '19 · What Was I Made For? — el cifrado y las ligaduras', 'obra'),
        (34, '20 · Para Elisa — el arranque liviano', 'obra'),
        (35, '20 · Para Elisa — la semicorchea del c. 20', 'obra'),
        (36, '21 · Perfect — contar en cuatro', 'obra'),
    ]),
    ('Junio', [
        (37, '21 · Perfect — el cifrado y la anacrusa', 'obra'),
        (38, '22 · Shallow — las corcheas iguales del c. 3', 'obra'),
        (39, '22 · Shallow — el estribillo y las semicorcheas', 'obra'),
        (40, '23 · Merry-go-round of Life — las terceras de la entrada', 'obra'),
    ]),
    ('Julio', [
        (41, '23 · Merry-go-round of Life — el vals y los dos tempos', 'obra'),
        (42, '24 · The Entertainer — el motivo y el 8va', 'obra'),
        (43, '24 · The Entertainer — el bajo y el staccato', 'obra'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]

NOTA_PLAN = ('Las 44 semanas del curso, repartidas. Los cuatro villancicos y la Sonatina nº 2, que son '
             'los más cortos, llevan una semana; las demás piezas, dos. De cada una te llevas la hoja '
             'de trabajo con el plan de minutos y, según la pieza, el reto de la semana, la escalera '
             'del metrónomo, el cifrado o lo que haya que acordar con la otra persona. Es una '
             'propuesta, no una obligación: si una pieza pide una semana más, se le da, y si sale '
             'antes, se pasa a la siguiente.')

import glob as _glob
DOSIERES = sorted(os.path.basename(p) for p in
                  _glob.glob(os.path.join(OUT_DIR, 'Martina_[0-9][0-9]_*_CUADERNO.pdf')))


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Martina_Portada_Indice.pdf')
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
    out = os.path.join(OUT_DIR, 'Martina_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
