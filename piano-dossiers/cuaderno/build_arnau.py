# -*- coding: utf-8 -*-
"""Portada, indice, plan de curso y album completo del cuaderno de Arnau.

   Formato CORTO (cinco hojas por cancion, dos de ellas de deberes escritos),
   porque Arnau tiene 10 anos y clases de media hora. El indice y el plan
   estan escritos en el mismo lenguaje que el resto de su cuaderno: sin
   tecnicismos, y diciendo en cada pieza QUE cosa nueva trae.

   Antes de ejecutarlo tiene que salir TODO OK en auditar_arnau.py.
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

ALUMNO = 'Arnau'
SUBTITULO = 'Primer curso'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('Las dos manos, y la primera melodía', 'empezar a tocar y a leer al mismo tiempo', [
        dict(num=1, titulo='Chopsticks', autor='popular, arr. Gilbert DeBenedetti',
             tonalidad='Do · 3 golpes', compas='3/4', trabaja='Un dedo por mano, y las manos se separan'),
        dict(num=2, titulo='Clementine', autor='popular, arr. Gilbert DeBenedetti',
             tonalidad='Do · 3 golpes', compas='3/4', trabaja='La primera melodía: la derecha va sola'),
        dict(num=3, titulo='Jolly Old Saint Nicholas', autor='villancico, arr. G. DeBenedetti',
             tonalidad='Do · 4 golpes', compas='4/4', trabaja='Una mano se mueve y la otra aguanta'),
    ]),
    ('Los huecos, y la primera tecla negra', 'contar lo que no suena, y mirar la armadura', [
        dict(num=4, titulo='Do Your Ears Hang Low?', autor='popular, arr. G. DeBenedetti',
             tonalidad='Do · 4 golpes', compas='4/4', trabaja='Las dos manos se mueven, y hay silencios'),
        dict(num=5, titulo='The Wheels on the Bus', autor='popular, arr. Jim Paterson',
             tonalidad='Fa · 3 golpes', compas='3/4', trabaja='La primera tecla negra: el bemol'),
        dict(num=6, titulo='Oh, When the Saints', autor='popular, arr. G. DeBenedetti',
             tonalidad='Do · 4 golpes', compas='4/4', trabaja='Entrar antes de que empiece el compás'),
        dict(num=7, titulo='We Wish You a Merry Christmas', autor='villancico, arr. G. DeBenedetti',
             tonalidad='Do · 3 golpes', compas='3/4', trabaja='Las dos manos con los dedos escritos'),
    ]),
    ('Leer más cosas a la vez', 'cuando en el papel pasan dos cosas al mismo tiempo', [
        dict(num=8, titulo='Baa Baa Black Sheep', autor='popular, arr. Jim Paterson',
             tonalidad='Do · 4 golpes', compas='4/4', trabaja='Una mano tocando dos cosas a la vez'),
        dict(num=9, titulo='Polly Put the Kettle On', autor='popular, arr. Jim Paterson',
             tonalidad='Fa · 2 golpes', compas='2/4', trabaja='Dos notas en cada golpe'),
        dict(num=10, titulo='Little Miss Muffet', autor='popular, arr. Jim Paterson',
             tonalidad='Fa · en dos', compas='6/8', trabaja='Seis notas por compás, contadas en dos'),
        dict(num=11, titulo='Eso que tú me das', autor='Jarabe de Palo · Pau Donés',
             tonalidad='Do · 4 golpes', compas='4/4', trabaja='Leer una hoja de melodía y acordes'),
    ]),
    ('Acordes, saltos y puntillos', 'la mano se abre, viaja, y las notas cambian de duración', [
        dict(num=12, titulo='Puff the Magic Dragon', autor='arr. Eric Moore',
             tonalidad='Do · 4 golpes', compas='4/4', trabaja='Acordes de tres notas a la vez'),
        dict(num=13, titulo='La Pantera Rosa', autor='Henry Mancini',
             tonalidad='Do · 4 golpes', compas='4/4', trabaja='Teclas negras que aparecen de repente'),
        dict(num=14, titulo='My Bonnie Lies Over the Ocean', autor='popular, arr. G. DeBenedetti',
             tonalidad='Do · 3 golpes', compas='3/4', trabaja='La mano cambia de sitio, y se cruzan'),
        dict(num=15, titulo='Largo · Sinfonía del Nuevo Mundo', autor='Antonín Dvořák',
             tonalidad='Do · muy lento', compas='4/4', trabaja='El puntillo, y las notas que se atan'),
        dict(num=16, titulo='Aloha Oe', autor='Reina Liliʻuokalani, arr. R. Pratley',
             tonalidad='Do · en dos', compas='¢', trabaja='Saltos grandes, y dos páginas'),
    ]),
    ('Deprisa, y tocando con otra persona', 'lo último no es difícil: es coordinarse', [
        dict(num=17, titulo='Popeye el marinerito', autor='Sammy Lerner, arr. A. C. Escobés',
             tonalidad='Sol · 3 golpes', compas='3/4', trabaja='Un sostenido en la armadura'),
        dict(num=18, titulo='El submarino amarillo', autor='Lennon y McCartney',
             tonalidad='Sol · rápido', compas='4/4', trabaja='Allegro: subir la velocidad con cabeza'),
        dict(num=19, titulo='Rain Rain Go Away', autor='popular, arr. R. Pratley · 4 manos',
             tonalidad='Do · 4 golpes', compas='4/4', trabaja='A cuatro manos: empezar los dos a la vez'),
        dict(num=20, titulo='The Mulberry Bush', autor='popular, arr. R. Pratley · 4 manos',
             tonalidad='Do · 4 golpes', compas='4/4', trabaja='A cuatro manos: no pararse si te pierdes'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# Dos semanas por pieza, como en los otros cuadernos, pero con una diferencia:
# aqui las clases son de media hora, asi que cada semana tiene UNA hoja de
# deberes escritos y no mas. El plan y las hojas de deberes van sincronizados:
# la hoja "semana 1" de cada cancion es para la primera de sus dos semanas.
#
# Las fechas que mandan sobre el orden:
#   · Halloween (semana 8) -> La Pantera Rosa, que es la pieza misteriosa del
#     cuaderno. Solo se lee y se prueba; entera se estudia en su sitio.
#   · Navidad (semanas 15 y 16) -> los dos villancicos.
#   · Final de curso (semanas 42-44) -> programa, ensayo y concierto.
PLAN = [
    ('Septiembre', [
        (1, '1 · Chopsticks — las dos notas vecinas', 'obra'),
        (2, '1 · Chopsticks — las manos se separan', 'obra'),
        (3, '2 · Clementine — colocar la mano', 'obra'),
        (4, '2 · Clementine — la melodía entera', 'obra'),
    ]),
    ('Octubre', [
        (5, '4 · Do Your Ears — contar los huecos', 'obra'),
        (6, '4 · Do Your Ears — las dos manos', 'obra'),
        (7, '5 · The Wheels on the Bus — la tecla negra', 'obra'),
        (8, 'HALLOWEEN · 13 La Pantera Rosa: leerla y probarla', 'especial'),
    ]),
    ('Noviembre', [
        (9, '5 · The Wheels on the Bus — entera', 'obra'),
        (10, '6 · Oh, When the Saints — entrar a tiempo', 'obra'),
        (11, '6 · Oh, When the Saints — las dos manos', 'obra'),
        (12, 'REPASO · las cuatro primeras, seguidas', 'repaso'),
    ]),
    ('Diciembre', [
        (13, '8 · Baa Baa Black Sheep — dos cosas con una mano', 'obra'),
        (14, '8 · Baa Baa Black Sheep — entera', 'obra'),
        (15, 'NAVIDAD · 3 Jolly Old Saint Nicholas', 'especial'),
        (16, 'NAVIDAD · 7 We Wish You a Merry Christmas', 'especial'),
    ]),
    ('Enero', [
        (17, '9 · Polly Put the Kettle On — contar un-y-dos-y', 'obra'),
        (18, '9 · Polly Put the Kettle On — más rápido', 'obra'),
        (19, '10 · Little Miss Muffet — contar en dos', 'obra'),
        (20, '10 · Little Miss Muffet — las dos manos', 'obra'),
    ]),
    ('Febrero', [
        (21, 'REPASO · elige tres y tócalas seguidas', 'repaso'),
        (22, '11 · Eso que tú me das — la melodía y la letra', 'obra'),
        (23, '11 · Eso que tú me das — respirar donde respira', 'obra'),
        (24, '12 · Puff the Magic Dragon — acordes de tres', 'obra'),
    ]),
    ('Marzo', [
        (25, '12 · Puff the Magic Dragon — las dos manos', 'obra'),
        (26, '13 · La Pantera Rosa — los sostenidos', 'obra'),
        (27, '13 · La Pantera Rosa — entera, con los huecos', 'obra'),
        (28, '14 · My Bonnie — la mano cambia de sitio', 'obra'),
    ]),
    ('Abril', [
        (29, '14 · My Bonnie — el cruce de manos', 'obra'),
        (30, 'REPASO · las de Navidad, para no perderlas', 'repaso'),
        (31, '15 · Largo — el puntillo', 'obra'),
        (32, '15 · Largo — las dos manos, muy lento', 'obra'),
    ]),
    ('Mayo', [
        (33, '16 · Aloha Oe — los saltos', 'obra'),
        (34, '16 · Aloha Oe — las dos páginas', 'obra'),
        (35, '17 · Popeye — el sostenido de la armadura', 'obra'),
        (36, '17 · Popeye — el vaivén de la izquierda', 'obra'),
    ]),
    ('Junio', [
        (37, '18 · El submarino amarillo — el molde', 'obra'),
        (38, '18 · El submarino amarillo — subir a Allegro', 'obra'),
        (39, '19 · Rain Rain Go Away — tu parte, en casa', 'obra'),
        (40, '19 · Rain Rain Go Away — a dúo, en clase', 'obra'),
    ]),
    ('Julio', [
        (41, '20 · The Mulberry Bush — a dúo', 'obra'),
        (42, 'Elegir qué tocar en el concierto', 'repaso'),
        (43, 'ENSAYO GENERAL · el programa entero, sin parar', 'concierto'),
        (44, 'CONCIERTO DE FIN DE CURSO', 'concierto'),
    ]),
]

NOTA_PLAN = ('Las 44 semanas del curso, repartidas. Cada canción tiene dos semanas: la primera para '
             'leerla y la segunda para tocarla entera, y en cada una te llevas una hoja de deberes. Es '
             'una propuesta, no una obligación: si una canción pide tres semanas se le dan.')

DOSIERES = [
    'Arnau_01_Chopsticks_CUADERNO.pdf',
    'Arnau_02_Clementine_CUADERNO.pdf',
    'Arnau_03_JollySaintNicholas_CUADERNO.pdf',
    'Arnau_04_DoYourEars_CUADERNO.pdf',
    'Arnau_05_WheelsOnTheBus_CUADERNO.pdf',
    'Arnau_06_WhenTheSaints_CUADERNO.pdf',
    'Arnau_07_WeWishYou_CUADERNO.pdf',
    'Arnau_08_BaaBaaBlackSheep_CUADERNO.pdf',
    'Arnau_09_PollyKettle_CUADERNO.pdf',
    'Arnau_10_LittleMissMuffet_CUADERNO.pdf',
    'Arnau_11_EsoQueTuMeDas_CUADERNO.pdf',
    'Arnau_12_PuffDragon_CUADERNO.pdf',
    'Arnau_13_PanteraRosa_CUADERNO.pdf',
    'Arnau_14_MyBonnie_CUADERNO.pdf',
    'Arnau_15_LargoNuevoMundo_CUADERNO.pdf',
    'Arnau_16_AlohaOe_CUADERNO.pdf',
    'Arnau_17_Popeye_CUADERNO.pdf',
    'Arnau_18_SubmarinoAmarillo_CUADERNO.pdf',
    'Arnau_19_RainRainGoAway_CUADERNO.pdf',
    'Arnau_20_MulberryBush_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Arnau_Portada_Indice.pdf')
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
    if faltan:
        raise SystemExit('faltan dosieres: %s' % faltan)

    out = os.path.join(OUT_DIR, 'Arnau_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    print('generado', out, '·', len(PdfReader(out).pages), 'paginas')


if __name__ == '__main__':
    main()
