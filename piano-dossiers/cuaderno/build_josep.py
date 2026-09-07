# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Josep.

   Formato ADULTO (seis hojas por pieza), el mismo que el de José María, con el
   listón subido: un recuadro de RETO en cada hoja de trabajo, la escalera del
   metrónomo con una meta escrita, el cifrado que su partitura trae impreso y
   un bloque propio para los cuatro duetos.

   Antes de ejecutarlo tiene que salir TODO OK en auditar_josep.py y 0 solapes
   en cruzar_josep.py.
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

ALUMNO = 'Josep'
SUBTITULO = 'Diecinueve retos'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('La mano quieta, y entre dos', 'las dos primeras son duetos: se empieza tocando con alguien', [
        dict(num=1, titulo='Romance', autor='Anton Diabelli · Primo, a cuatro manos',
             tonalidad='Do mayor', compas='¢', trabaja='Posición fija, y las dos manos exactamente juntas'),
        dict(num=2, titulo='Petite Chanson', autor='Riccardo Collu · a cuatro manos',
             tonalidad='Do mayor', compas='4/4', trabaja='La anacrusa, y un salto de octava en el primer compás'),
    ]),
    ('La izquierda sostiene', 'el reparto más común del piano, en su forma más pura', [
        dict(num=3, titulo='Peaches', autor='Jack Black · Super Mario Bros.',
             tonalidad='Do mayor', compas='4/4', trabaja='Doce compases de redondas sin acelerarse'),
        dict(num=4, titulo='Counting Stars', autor='OneRepublic · arr. Becky Messer',
             tonalidad='Do mayor', compas='4/4', trabaja='Obedecer la digitación impresa, toda'),
        dict(num=5, titulo='What Was I Made For?', autor='Billie Eilish',
             tonalidad='Do mayor', compas='4/4', trabaja='Entrar a contratiempo, y el primer cifrado'),
    ]),
    ('El swing y el acorde', 'la izquierda deja de aguantar y empieza a acompañar', [
        dict(num=6, titulo='Heart and Soul', autor='Hoagy Carmichael · easy piano',
             tonalidad='Do mayor', compas='4/4', trabaja='El swing, y el bajo con acorde'),
        dict(num=7, titulo='Hit the Road Jack', autor='Popularizada por Ray Charles',
             tonalidad='Fa mayor', compas='4/4', trabaja='La primera armadura: no olvidarse del Si bemol'),
        dict(num=8, titulo='Deck the Halls', autor='villancico · arr. Jim Paterson',
             tonalidad='Fa mayor', compas='4/4', trabaja='Dobles notas, y el primer acorde con séptima'),
        dict(num=9, titulo='Jailhouse Rock', autor='Elvis Presley · arr. Sadie King',
             tonalidad='Do · blues', compas='4/4', trabaja='Subir a ♩ = 150 sin practicar ni un fallo'),
    ]),
    ('Más tonalidades, y las dos manos de verdad', 'cuando ninguna mano descansa', [
        dict(num=10, titulo='Bella Ciao', autor='popular italiana · a cuatro manos',
             tonalidad='Sol menor', compas='4/4', trabaja='El primer tono menor, y una sensible que va y viene'),
        dict(num=11, titulo="Can't Help Falling in Love", autor='Elvis Presley · arr. Seb Alejandro',
             tonalidad='Re mayor', compas='3/4', trabaja='Una izquierda que no se para, y cinco acordes'),
        dict(num=12, titulo='Lovely', autor='Billie Eilish con Khalid · arr. Amy Kieran',
             tonalidad='Mi menor', compas='4/4', trabaja='Corcheas sin parar: resistencia, no dificultad'),
        dict(num=13, titulo='Rasputin', autor='Boney M · easy piano',
             tonalidad='Si menor', compas='4/4', trabaja='Contar los compases callados a ♩ = 124'),
        dict(num=14, titulo="It's Beginning to Look a Lot Like Christmas",
             autor='Meredith Willson · dúo de piano',
             tonalidad='Do mayor', compas='6/8', trabaja='El único 6/8 del cuaderno: contar en dos'),
    ]),
    ('Los cinco retos del final', 'aquí el cuaderno deja de ser cómodo, y a propósito', [
        dict(num=15, titulo='My Favourite Things', autor='Rodgers y Hammerstein · arr. Kaitlin',
             tonalidad='Mi menor', compas='3/4', trabaja='55 compases a ♩ = 160 sin perder el sitio'),
        dict(num=16, titulo="Sweet Child O' Mine", autor="Guns N' Roses · arr. Sadie King",
             tonalidad='Si bemol', compas='4/4', trabaja='El pedal, que aquí viene escrito compás a compás'),
        dict(num=17, titulo='Un Beso y una Flor', autor='Nino Bravo',
             tonalidad='Fa mayor', compas='C', trabaja='Semicorcheas: cuatro notas por golpe, iguales'),
        dict(num=18, titulo='Merry Go Round of Life', autor='Joe Hisaishi · piano solo',
             tonalidad='Si bemol', compas='3/4', trabaja='Terceras en corcheas, y dos velocidades escritas'),
        dict(num=19, titulo='A comme amour', autor='Richard Clayderman',
             tonalidad='Mi m → La m', compas='4/4', trabaja='El único cambio de armadura del cuaderno'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# Dos semanas por pieza en las catorce primeras y TRES en las cinco últimas:
# los retos del final no caben en dos. Con las de Navidad adelantadas a
# diciembre, salen 44 semanas justas.
PLAN = [
    ('Septiembre', [
        (1, '1 · Romance — colocar la mano y no moverla', 'obra'),
        (2, '1 · Romance — las dos manos exactamente juntas', 'obra'),
        (3, '2 · Petite Chanson — la anacrusa y el salto de octava', 'obra'),
        (4, '2 · Petite Chanson — a ♩ = 80, con la profesora', 'obra'),
    ]),
    ('Octubre', [
        (5, '3 · Peaches — los doce primeros, sin acelerar', 'obra'),
        (6, '3 · Peaches — la segunda mitad', 'obra'),
        (7, '4 · Counting Stars — la digitación impresa, toda', 'obra'),
        (8, '4 · Counting Stars — las dos manos', 'obra'),
    ]),
    ('Noviembre', [
        (9, '5 · What Was I Made For — la izquierda como reloj', 'obra'),
        (10, '5 · What Was I Made For — las entradas a contratiempo', 'obra'),
        (11, '6 · Heart and Soul — el bajo con acorde', 'obra'),
        (12, 'REPASO · las cinco primeras, una detrás de otra', 'repaso'),
    ]),
    ('Diciembre', [
        (13, '6 · Heart and Soul — el swing, y las dos manos', 'obra'),
        (14, 'NAVIDAD · 8 Deck the Halls — las dobles notas', 'especial'),
        (15, 'NAVIDAD · 8 Deck the Halls — entera, con el Dm7', 'especial'),
        (16, 'NAVIDAD · 14 It\'s Beginning — contar en dos', 'especial'),
    ]),
    ('Enero', [
        (17, '14 · It\'s Beginning — el dueto entero', 'obra'),
        (18, '7 · Hit the Road Jack — marcar todos los Si', 'obra'),
        (19, '7 · Hit the Road Jack — la intro y la melodía', 'obra'),
        (20, '9 · Jailhouse Rock — la entrada y el Si bemol', 'obra'),
    ]),
    ('Febrero', [
        (21, '9 · Jailhouse Rock — subir por escalones a 150', 'obra'),
        (22, '10 · Bella Ciao — el primer tono menor', 'obra'),
        (23, '10 · Bella Ciao — el dueto, con metrónomo', 'obra'),
        (24, 'REPASO · elige tres y tócalas seguidas', 'repaso'),
    ]),
    ('Marzo', [
        (25, "11 · Can't Help Falling — la izquierda sin pararse", 'obra'),
        (26, "11 · Can't Help Falling — los cinco acordes, de memoria", 'obra'),
        (27, '12 · Lovely — cuatro compases y parar', 'obra'),
        (28, '12 · Lovely — veinte compases con las corcheas iguales', 'obra'),
    ]),
    ('Abril', [
        (29, '13 · Rasputin — los tres acordes y los compases callados', 'obra'),
        (30, '13 · Rasputin — subir a ♩ = 124', 'obra'),
        (31, '15 · My Favourite Things — marcar las frases a lápiz', 'obra'),
        (32, '15 · My Favourite Things — leer por acordes', 'obra'),
    ]),
    ('Mayo', [
        (33, '15 · My Favourite Things — la página entera a 160', 'obra'),
        (34, "16 · Sweet Child O' Mine — el pedal, con la izquierda sola", 'obra'),
        (35, "16 · Sweet Child O' Mine — el riff, con la mano quieta", 'obra'),
        (36, "16 · Sweet Child O' Mine — las dos manos y el pie", 'obra'),
    ]),
    ('Junio', [
        (37, '17 · Un Beso y una Flor — grupos de cuatro con parada', 'obra'),
        (38, '17 · Un Beso y una Flor — los saltos de la izquierda', 'obra'),
        (39, '17 · Un Beso y una Flor — entera, con los tresillos', 'obra'),
        (40, '18 · Merry Go Round — las terceras, pareja a pareja', 'obra'),
    ]),
    ('Julio', [
        (41, '18 · Merry Go Round — el vals del c. 27, a 152', 'obra'),
        (42, '19 · A comme amour — el cambio de armadura del c. 10', 'obra'),
        (43, '19 · A comme amour — entera, a ♩ = 69', 'obra'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]

NOTA_PLAN = ('Las 44 semanas del curso, repartidas. Cada pieza tiene dos semanas —las cinco últimas, '
             'tres, porque en dos no caben— y de cada una te llevas la hoja de trabajo con el plan de '
             'minutos, el reto de la semana y la escalera del metrónomo. Es una propuesta, no una '
             'obligación: si una pieza pide una semana más, se le da, y si sale antes, se pasa a la '
             'siguiente.')

DOSIERES = [
    'Josep_01_RomanceDiabelli_CUADERNO.pdf',
    'Josep_02_PetiteChanson_CUADERNO.pdf',
    'Josep_03_Peaches_CUADERNO.pdf',
    'Josep_04_CountingStars_CUADERNO.pdf',
    'Josep_05_WhatWasIMadeFor_CUADERNO.pdf',
    'Josep_06_HeartAndSoul_CUADERNO.pdf',
    'Josep_07_HitTheRoadJack_CUADERNO.pdf',
    'Josep_08_DeckTheHalls_CUADERNO.pdf',
    'Josep_09_JailhouseRock_CUADERNO.pdf',
    'Josep_10_BellaCiao_CUADERNO.pdf',
    'Josep_11_CantHelpFalling_CUADERNO.pdf',
    'Josep_12_Lovely_CUADERNO.pdf',
    'Josep_13_Rasputin_CUADERNO.pdf',
    'Josep_14_BeginningChristmas_CUADERNO.pdf',
    'Josep_15_MyFavouriteThings_CUADERNO.pdf',
    'Josep_16_SweetChildOMine_CUADERNO.pdf',
    'Josep_17_UnBesoYUnaFlor_CUADERNO.pdf',
    'Josep_18_MerryGoRoundOfLife_CUADERNO.pdf',
    'Josep_19_AcommeAmour_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Josep_Portada_Indice.pdf')
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
    out = os.path.join(OUT_DIR, 'Josep_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
