# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de José María.

   Formato ADULTO (seis hojas por pieza), porque José María empezó hace poco,
   viene a clase y practica en casa con su teclado. El índice y el plan están
   escritos como para un adulto: sin infantilismos y sin jerga, diciendo en
   cada pieza QUÉ trae de nuevo.

   Antes de ejecutarlo tiene que salir TODO OK en auditar_josemaria.py.
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

ALUMNO = 'José María'
SUBTITULO = 'Empezar de mayor'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('La mano quieta', 'la mano se coloca una vez y no se mueve', [
        dict(num=1, titulo='Romance', autor='Anton Diabelli · Primo, a cuatro manos',
             tonalidad='Do mayor', compas='¢', trabaja='Posición fija de cinco dedos, y las dos manos al unísono'),
        dict(num=2, titulo='America', autor="My Country, 'Tis of Thee · arr. G. DeBenedetti",
             tonalidad='Do mayor', compas='3/4', trabaja='La primera melodía, y la negra con puntillo'),
        dict(num=3, titulo='The Star-Spangled Banner', autor='F. S. Key · arr. G. DeBenedetti',
             tonalidad='Do mayor', compas='3/4', trabaja='Entrar después de un silencio'),
    ]),
    ('La izquierda aguanta, la derecha se mueve', 'el reparto de trabajo más común del piano', [
        dict(num=4, titulo='Counting Stars', autor='OneRepublic · arr. Becky Messer',
             tonalidad='Do mayor', compas='4/4', trabaja='Dejar la izquierda quieta mientras la derecha corre'),
        dict(num=5, titulo='Peaches', autor='Jack Black · Super Mario Bros.',
             tonalidad='Do mayor', compas='4/4', trabaja='Lo mismo, y acotar la pieza donde toca'),
        dict(num=6, titulo='Someone You Loved', autor='Lewis Capaldi',
             tonalidad='Do mayor', compas='4/4', trabaja='Corcheas seguidas sin acelerar'),
    ]),
    ('La primera armadura', 'mirar el principio del pentagrama antes de tocar', [
        dict(num=7, titulo='Deck the Halls', autor='villancico · arr. Jim Paterson',
             tonalidad='Fa mayor', compas='4/4', trabaja='Un bemol, y las dos manos con acordes'),
        dict(num=8, titulo='Jailhouse Rock', autor='Elvis Presley · arr. Sadie King',
             tonalidad='Do · blues', compas='4/4', trabaja='La primera pieza rápida, y el swing'),
        dict(num=9, titulo="My Grandfather's Clock", autor='H. C. Work · arr. G. DeBenedetti',
             tonalidad='Sol mayor', compas='4/4', trabaja='El primer sostenido, y a tiempo exacto'),
        dict(num=10, titulo='Shallow', autor='Lady Gaga y Bradley Cooper',
             tonalidad='Sol mayor', compas='4/4', trabaja='Contar los compases en los que no tocas'),
    ]),
    ('Más tonalidades, y las dos manos de verdad', 'cuando ninguna mano descansa', [
        dict(num=11, titulo="Can't Help Falling in Love", autor='Elvis Presley · arr. Seb Alejandro',
             tonalidad='Re mayor', compas='3/4', trabaja='Dos sostenidos, y una izquierda que ya no para'),
        dict(num=12, titulo='Carol of the Bells', autor='M. Leontovych · arr. Jim Paterson',
             tonalidad='Sol menor', compas='3/4', trabaja='El primer tono menor, y buscar lo que se repite'),
        dict(num=13, titulo='Adagio', autor='Albinoni · arr. A. L. Christopherson',
             tonalidad='♩ = 60', compas='3/4', trabaja='Las dinámicas: lo difícil aquí es el sonido'),
        dict(num=14, titulo='Rasputin', autor='Boney M · easy piano',
             tonalidad='Si menor', compas='4/4', trabaja='La misma armadura que la 11, y suena al revés'),
        dict(num=15, titulo='Toreador', autor='Bizet · Carmen · arr. G. DeBenedetti',
             tonalidad='Fa mayor', compas='4/4', trabaja='Level Four: la vara de medir del curso'),
    ]),
    ('Los cuatro retos', 'ninguno trae nada nuevo: traen cantidad', [
        dict(num=16, titulo='Trouble', autor='Coldplay · arr. Unai Karam',
             tonalidad='Sol mayor', compas='4/4', trabaja='Cuatro páginas a ♩=138: resistencia'),
        dict(num=17, titulo='A comme amour', autor='Richard Clayderman',
             tonalidad='Mi menor', compas='4/4', trabaja='Semicorcheas: cuatro notas por golpe, iguales'),
        dict(num=18, titulo='Interstellar', autor='Hans Zimmer',
             tonalidad='♩ = 96', compas='3/4', trabaja='Seis páginas: hacer el mapa antes de tocar'),
        dict(num=19, titulo='Flying Theme', autor='Cómo entrenar a tu dragón · Perfect Harmony',
             tonalidad='Do → Re', compas='4/4', trabaja='Un cambio de tonalidad a mitad de pieza'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# Dos semanas por pieza en las quince primeras, y TRES en las cuatro últimas:
# los retos no caben en dos y fingir que sí sería engañarse. Con las de
# Navidad adelantadas a diciembre, salen 44 semanas justas.
PLAN = [
    ('Septiembre', [
        (1, '1 · Romance — colocar la mano y no moverla', 'obra'),
        (2, '1 · Romance — las dos manos a la vez', 'obra'),
        (3, '2 · America — la melodía, sin el puntillo', 'obra'),
        (4, '2 · America — con el ritmo de verdad', 'obra'),
    ]),
    ('Octubre', [
        (5, '3 · Star-Spangled Banner — entrar tras el silencio', 'obra'),
        (6, '3 · Star-Spangled Banner — las dos manos', 'obra'),
        (7, '4 · Counting Stars — la izquierda quieta', 'obra'),
        (8, '4 · Counting Stars — las corcheas de la derecha', 'obra'),
    ]),
    ('Noviembre', [
        (9, '5 · Peaches — los doce primeros compases', 'obra'),
        (10, '5 · Peaches — los doce, seguidos y sin parar', 'obra'),
        (11, '6 · Someone You Loved — corcheas sin acelerar', 'obra'),
        (12, 'REPASO · las cinco primeras, una detrás de otra', 'repaso'),
    ]),
    ('Diciembre', [
        (13, '6 · Someone You Loved — las dos manos', 'obra'),
        (14, 'NAVIDAD · 7 Deck the Halls — el primer bemol', 'especial'),
        (15, 'NAVIDAD · 7 Deck the Halls — entera', 'especial'),
        (16, 'NAVIDAD · 12 Carol of the Bells — el dibujo que se repite', 'especial'),
    ]),
    ('Enero', [
        (17, '12 · Carol of the Bells — la izquierda, y entera', 'obra'),
        (18, '8 · Jailhouse Rock — la entrada y el Si bemol', 'obra'),
        (19, '8 · Jailhouse Rock — subir la velocidad', 'obra'),
        (20, "9 · Grandfather's Clock — el primer sostenido", 'obra'),
    ]),
    ('Febrero', [
        (21, "9 · Grandfather's Clock — a tiempo exacto", 'obra'),
        (22, '10 · Shallow — los compases en los que no tocas', 'obra'),
        (23, '10 · Shallow — las dos manos', 'obra'),
        (24, 'REPASO · elige tres y tócalas seguidas', 'repaso'),
    ]),
    ('Marzo', [
        (25, "11 · Can't Help Falling — la izquierda, de memoria", 'obra'),
        (26, "11 · Can't Help Falling — las dos manos", 'obra'),
        (27, '13 · Adagio — sostener el sonido', 'obra'),
        (28, '13 · Adagio — las dinámicas escritas', 'obra'),
    ]),
    ('Abril', [
        (29, '14 · Rasputin — contar los compases callados', 'obra'),
        (30, '14 · Rasputin — subir a ♩ = 124', 'obra'),
        (31, '15 · Toreador — el ritmo de marcha', 'obra'),
        (32, '15 · Toreador — entera, comparándola con America', 'obra'),
    ]),
    ('Mayo', [
        (33, '16 · Trouble — la primera página, de atrás hacia adelante', 'obra'),
        (34, '16 · Trouble — la segunda y la tercera', 'obra'),
        (35, '16 · Trouble — las cuatro seguidas', 'obra'),
        (36, '17 · A comme amour — grupos de cuatro, iguales', 'obra'),
    ]),
    ('Junio', [
        (37, '17 · A comme amour — unir los grupos', 'obra'),
        (38, '17 · A comme amour — entera, a su velocidad', 'obra'),
        (39, '18 · Interstellar — el mapa, con lápiz', 'obra'),
        (40, '18 · Interstellar — las dos primeras páginas', 'obra'),
    ]),
    ('Julio', [
        (41, '19 · Flying Theme — el cambio de tonalidad, aislado', 'obra'),
        (42, '19 · Flying Theme — la primera página entera', 'obra'),
        (43, 'ENSAYO · elegir tres piezas y tocarlas sin parar', 'concierto'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]

NOTA_PLAN = ('Las 44 semanas del curso, repartidas. Cada pieza tiene dos semanas —las cuatro últimas, '
             'tres, porque en dos no caben— y de cada una te llevas la hoja de trabajo con el plan de '
             'minutos. Es una propuesta, no una obligación: si una pieza pide una semana más, se le '
             'da, y si sale antes, se pasa a la siguiente.')

DOSIERES = [
    'JoseMaria_01_RomanceDiabelli_CUADERNO.pdf',
    'JoseMaria_02_America_CUADERNO.pdf',
    'JoseMaria_03_StarSpangledBanner_CUADERNO.pdf',
    'JoseMaria_04_CountingStars_CUADERNO.pdf',
    'JoseMaria_05_Peaches_CUADERNO.pdf',
    'JoseMaria_06_SomeoneYouLoved_CUADERNO.pdf',
    'JoseMaria_07_DeckTheHalls_CUADERNO.pdf',
    'JoseMaria_08_JailhouseRock_CUADERNO.pdf',
    'JoseMaria_09_GrandfathersClock_CUADERNO.pdf',
    'JoseMaria_10_Shallow_CUADERNO.pdf',
    'JoseMaria_11_CantHelpFalling_CUADERNO.pdf',
    'JoseMaria_12_CarolOfTheBells_CUADERNO.pdf',
    'JoseMaria_13_AdagioAlbinoni_CUADERNO.pdf',
    'JoseMaria_14_Rasputin_CUADERNO.pdf',
    'JoseMaria_15_Toreador_CUADERNO.pdf',
    'JoseMaria_16_Trouble_CUADERNO.pdf',
    'JoseMaria_17_AcommeAmour_CUADERNO.pdf',
    'JoseMaria_18_Interstellar_CUADERNO.pdf',
    'JoseMaria_19_FlyingTheme_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'JoseMaria_Portada_Indice.pdf')
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
    out = os.path.join(OUT_DIR, 'JoseMaria_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
