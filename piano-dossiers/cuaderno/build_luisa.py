# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Luisa.

   Formato ADULTO, las mismas seis hojas que José María y Josep. Lo único que
   cambia es el nivel: iniciación, el más bajo del proyecto, porque Luisa
   empezó hace poco. El encargo del cliente fue literal: *"poquito pero bien,
   que se entienda todo, sencillo"*.

   El plan de curso también va a su ritmo: **dos semanas por pieza en casi
   todas y tres en las cuatro últimas**, que son las que traen material nuevo
   de verdad.

   Antes de ejecutarlo tiene que salir TODO OK en auditar_luisa.py y 0 solapes
   en cruzar_luisa.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import build_cover, build_index, build_plan_curso, W, H

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')
OUT_DIR = os.path.join(HERE, '..', 'output')

ALUMNO = 'Luisa'
SUBTITULO = 'Poquito pero bien'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('Las dos manos hacen lo mismo', 'se empieza el curso tocando con alguien, y sin separar las manos', [
        dict(num=1, titulo='Sonatina per bambini', autor='M. Bazzoni · a cuatro manos',
             tonalidad='La menor', compas='4/4', trabaja='Las dos manos al unísono, y solo negras'),
        dict(num=2, titulo='The Beginner', autor='C. Gurlitt · op. 211 nº 3 · a cuatro manos',
             tonalidad='Do mayor', compas='3/4', trabaja='El compás de tres, con negras y blancas'),
        dict(num=3, titulo='Sonatina nº 2', autor='M. Bazzoni · a cuatro manos',
             tonalidad='Sol mayor', compas='4/4', trabaja='La primera armadura, con las manos juntas'),
    ]),
    ('La izquierda aguanta', 'una nota abajo, la melodía arriba', [
        dict(num=4, titulo="You've Got a Friend in Me", autor='arr. Megan Harper',
             tonalidad='Do mayor', compas='4/4', trabaja='Una redonda por compás: tocar y esperar'),
        dict(num=5, titulo='Puff the Magic Dragon', autor='arr. Eric Moore',
             tonalidad='Do mayor', compas='4/4', trabaja='La redonda, ahora con dos notas a la vez'),
        dict(num=6, titulo='I Have a Dream', autor='ABBA · INeVENT Music Academy',
             tonalidad='Do mayor', compas='4/4', trabaja='Leer con la letra debajo, y los puntillos'),
        dict(num=7, titulo='Christmas Songs', autor='Mindy Liang · a cuatro manos',
             tonalidad='Do mayor', compas='4/4', trabaja='La izquierda se mueve: dos blancas por compás'),
    ]),
    ('Cada mano por su lado', 'la izquierda deja de copiar a la derecha', [
        dict(num=8, titulo='Silent Night', autor='F. X. Gruber · con letra y digitación',
             tonalidad='Do mayor', compas='3/4', trabaja='Dos ritmos a la vez, uno en cada mano'),
        dict(num=9, titulo='Spring', autor='Vivaldi · de Las cuatro estaciones',
             tonalidad='Do mayor', compas='4/4', trabaja='Entrar en el cuarto tiempo, contando'),
        dict(num=10, titulo='Titanic', autor='James Horner · arr. A. C. Escobés',
             tonalidad='Do mayor', compas='2/4', trabaja='El compás de dos, y el largo-corto'),
        dict(num=11, titulo='Piano Man', autor='Billy Joel · versión SimplyPiano',
             tonalidad='Do mayor', compas='3/4', trabaja='No perder la cuenta cuando no suena nada'),
    ]),
    ('Teclas negras y tonos menores', 'la pieza deja de estar toda en teclas blancas', [
        dict(num=12, titulo='La Panthère rose', autor='H. Mancini · Première année',
             tonalidad='Do mayor', compas='4/4', trabaja='Tres compases callados, y sostenidos escritos'),
        dict(num=13, titulo='Bela Ciao', autor='popular italiana · La Casa de Papel',
             tonalidad='Mi menor', compas='2/4', trabaja='El primer tono menor, y entrar media parte tarde'),
        dict(num=14, titulo='Heart and Soul', autor='Hoagy Carmichael · easy piano',
             tonalidad='Do mayor', compas='4/4', trabaja='El swing, que no se lee: se imita'),
        dict(num=15, titulo='Greensleeves', autor='tradicional inglesa · con cifrado',
             tonalidad='La menor', compas='3/4', trabaja='Entrar antes del compás, y tres negras abajo'),
    ]),
    ('Las cuatro del final', 'lo que se guarda para la audición', [
        dict(num=16, titulo='Chim Chim Cher-ee', autor='R. M. Sherman · Mary Poppins',
             tonalidad='La menor', compas='3/4', trabaja='Dos teclas a la vez, y el primer tiempo callado'),
        dict(num=17, titulo='Rasputin', autor='Boney M · easy piano',
             tonalidad='Si menor', compas='4/4', trabaja='Dos sostenidos que valen para toda la pieza'),
        dict(num=18, titulo='Für Elise', autor='Beethoven · versión fácil',
             tonalidad='La menor', compas='3/4', trabaja='Seis corcheas seguidas, todas iguales'),
        dict(num=19, titulo='Nocturne op. 9', autor='Chopin · arr. Benny Chaw',
             tonalidad='Do mayor', compas='3/4', trabaja='Pocas notas: aquí lo que se trabaja es el sonido'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# Dos semanas por pieza en las quince primeras y TRES en las cuatro últimas,
# que son las que traen material nuevo de verdad. Con los villancicos puestos
# en diciembre, salen 44 semanas justas.
PLAN = [
    ('Septiembre', [
        (1, '1 · Sonatina per bambini — la mano derecha sola', 'obra'),
        (2, '1 · Sonatina per bambini — las dos a la vez, con la profesora', 'obra'),
        (3, '2 · The Beginner — el compás de tres', 'obra'),
        (4, '2 · The Beginner — el dueto entero', 'obra'),
    ]),
    ('Octubre', [
        (5, '3 · Sonatina nº 2 — el Fa sostenido de la armadura', 'obra'),
        (6, '3 · Sonatina nº 2 — las dos manos, con la profesora', 'obra'),
        (7, "4 · You've Got a Friend in Me — la izquierda que espera", 'obra'),
        (8, "4 · You've Got a Friend in Me — las dos manos", 'obra'),
    ]),
    ('Noviembre', [
        (9, '5 · Puff the Magic Dragon — dos notas a la vez abajo', 'obra'),
        (10, '5 · Puff the Magic Dragon — entera, despacio', 'obra'),
        (11, '6 · I Have a Dream — la melodía con la letra', 'obra'),
        (12, 'REPASO · las cinco primeras, una detrás de otra', 'repaso'),
    ]),
    ('Diciembre', [
        (13, '6 · I Have a Dream — las dos manos', 'obra'),
        (14, 'NAVIDAD · 7 Christmas Songs — Jingle Bells', 'especial'),
        (15, 'NAVIDAD · 7 Christmas Songs — el segundo villancico', 'especial'),
        (16, 'NAVIDAD · 8 Silent Night — la izquierda sola', 'especial'),
    ]),
    ('Enero', [
        (17, '8 · Silent Night — las dos manos, con su ritmo', 'obra'),
        (18, '9 · Spring — contar tres tiempos y entrar', 'obra'),
        (19, '9 · Spring — las dos manos y la repetición', 'obra'),
        (20, '10 · Titanic — el compás de dos', 'obra'),
    ]),
    ('Febrero', [
        (21, '10 · Titanic — el largo-corto, y las casillas del final', 'obra'),
        (22, '11 · Piano Man — contar los compases callados', 'obra'),
        (23, '11 · Piano Man — entera, sin correr', 'obra'),
        (24, 'REPASO · elige tres y tócalas seguidas', 'repaso'),
    ]),
    ('Marzo', [
        (25, '12 · La Panthère rose — la izquierda sola, los tres primeros', 'obra'),
        (26, '12 · La Panthère rose — la entrada de la melodía', 'obra'),
        (27, '13 · Bela Ciao — el Fa sostenido y el tono menor', 'obra'),
        (28, '13 · Bela Ciao — entrar media parte tarde', 'obra'),
    ]),
    ('Abril', [
        (29, '14 · Heart and Soul — la izquierda, dos blancas', 'obra'),
        (30, '14 · Heart and Soul — el swing, escuchando la grabación', 'obra'),
        (31, '15 · Greensleeves — la izquierda, tres negras iguales', 'obra'),
        (32, '15 · Greensleeves — entrar antes del compás', 'obra'),
    ]),
    ('Mayo', [
        (33, '16 · Chim Chim Cher-ee — dos teclas a la vez', 'obra'),
        (34, '16 · Chim Chim Cher-ee — el primer tiempo callado', 'obra'),
        (35, '16 · Chim Chim Cher-ee — entera, con la izquierda', 'obra'),
        (36, '17 · Rasputin — los dos sostenidos, sueltos', 'obra'),
    ]),
    ('Junio', [
        (37, '17 · Rasputin — la melodía con el largo-corto', 'obra'),
        (38, '17 · Rasputin — las dos manos a ♩ = 124', 'obra'),
        (39, '18 · Für Elise — dos dedos que se turnan', 'obra'),
        (40, '18 · Für Elise — un compás de corcheas, y parar', 'obra'),
    ]),
    ('Julio', [
        (41, '18 · Für Elise — las dos manos, despacio', 'obra'),
        (42, '19 · Nocturne — las notas largas, escuchando el final', 'obra'),
        (43, '19 · Nocturne — entero, para la audición', 'obra'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]

NOTA_PLAN = ('Las 44 semanas del curso, repartidas. Cada pieza tiene dos semanas —las cuatro '
             'últimas, tres— y de cada una te llevas la hoja de calentamiento, la de agudeza '
             'visual, la de cómo se estudia y la de relajación, con el recuadro donde Azucena te '
             'escribe los deberes. Es una propuesta, no una obligación: si una pieza pide una '
             'semana más, se le da.')

DOSIERES = [
    'Luisa_01_SonatinaBambini_CUADERNO.pdf',
    'Luisa_02_TheBeginner_CUADERNO.pdf',
    'Luisa_03_SonatinaSolMayor_CUADERNO.pdf',
    'Luisa_04_FriendInMe_CUADERNO.pdf',
    'Luisa_05_PuffTheMagicDragon_CUADERNO.pdf',
    'Luisa_06_IHaveADream_CUADERNO.pdf',
    'Luisa_07_ChristmasSongs_CUADERNO.pdf',
    'Luisa_08_SilentNight_CUADERNO.pdf',
    'Luisa_09_Spring_CUADERNO.pdf',
    'Luisa_10_Titanic_CUADERNO.pdf',
    'Luisa_11_PianoMan_CUADERNO.pdf',
    'Luisa_12_PanthereRose_CUADERNO.pdf',
    'Luisa_13_BelaCiao_CUADERNO.pdf',
    'Luisa_14_HeartAndSoul_CUADERNO.pdf',
    'Luisa_15_Greensleeves_CUADERNO.pdf',
    'Luisa_16_ChimChimCheree_CUADERNO.pdf',
    'Luisa_17_Rasputin_CUADERNO.pdf',
    'Luisa_18_FurElise_CUADERNO.pdf',
    'Luisa_19_Nocturne_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Luisa_Portada_Indice.pdf')
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
        for p in PdfReader(ruta).pages:
            wr.add_page(p)
    out = os.path.join(OUT_DIR, 'Luisa_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
