# -*- coding: utf-8 -*-
"""Portada, indice, plan de curso y album completo del cuaderno de Eva.

   Une la portada + el indice + el plan de 44 semanas con los diecisiete
   dosieres, en el orden del album (de menos a mas dificil, criterio del
   cliente; el porque de cada puesto esta en PLAN_ALBUM_EVA.md).

   Antes de ejecutarlo tiene que salir TODO OK en auditar_eva.py.
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

ALUMNO = 'Eva'
SUBTITULO = 'Nivel avanzado'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('La izquierda hace siempre lo mismo', 'un molde que se repite; solo cambia dónde se pone', [
        dict(num=1, titulo='Can’t Help Falling in Love', autor='Elvis Presley, arr. Seb Alejandro',
             tonalidad='Re mayor', compas='3/4', trabaja='Un arpegio fijo, y una nota por compás'),
        dict(num=2, titulo='A Sky Full of Stars', autor='Coldplay y Avicii',
             tonalidad='Fa mayor', compas='4/4', trabaja='Cuatro compases de música y veintitrés de bucle'),
        dict(num=3, titulo='Poema de Amor', autor='Joan Manuel Serrat',
             tonalidad='Sol menor', compas='4/4', trabaja='Un molde de cuatro negras que no cambia'),
        dict(num=4, titulo='What Was I Made For?', autor='Billie Eilish y Finneas',
             tonalidad='Do mayor', compas='4/4', trabaja='Contar los silencios cuando nada marca el pulso'),
    ]),
    ('Sostener, y entrar a tiempo', 'la mano se para y el problema pasa a ser el reloj', [
        dict(num=5, titulo='Thinking Out Loud', autor='Ed Sheeran y Amy Wadge',
             tonalidad='Re mayor', compas='4/4', trabaja='Redondas abajo y una derecha que entra tarde'),
        dict(num=6, titulo='El Cisne', autor='Saint-Saëns, rev. Ricardo Boppré',
             tonalidad='Sol mayor', compas='3/4', trabaja='Igualar un arpegio durante 55 compases'),
        dict(num=7, titulo='When I Was Your Man', autor='Bruno Mars',
             tonalidad='Do mayor', compas='4/4', trabaja='Seis acordes de memoria, y el salto'),
    ]),
    ('Dos cosas a la vez', 'aquí empieza la independencia de verdad', [
        dict(num=8, titulo='La Promesa', autor='Melendi',
             tonalidad='Sol mayor', compas='4/4', trabaja='Bajo y acorde a octava y media, con pedal'),
        dict(num=9, titulo='Amiga Mía', autor='Alejandro Sanz',
             tonalidad='Re mayor', compas='4/4', trabaja='Una mano sosteniendo una voz y moviendo otra'),
        dict(num=10, titulo='When We Were Young', autor='Adele',
             tonalidad='Re menor', compas='4/4', trabaja='Cuatro páginas de corcheas, y el cifrado como mapa'),
    ]),
    ('El ritmo manda', 'la dificultad se va del teclado a la cabeza', [
        dict(num=11, titulo='Soldadito de Hierro', autor='Nil Moliner',
             tonalidad='Do mayor', compas='4/4', trabaja='Tresillos de principio a fin'),
        dict(num=12, titulo='My Favourite Things', autor='Rodgers y Hammerstein II',
             tonalidad='Sol mayor', compas='3/4', trabaja='Un vals a ♩=160: el salto y el peso'),
        dict(num=13, titulo='Have Yourself a Merry Little Christmas', autor='Martin y Blane',
             tonalidad='Do mayor', compas='4/4', trabaja='Tres capas, y decidir el volumen de cada una'),
    ]),
    ('Leer la hoja, y tocar con otra persona', 'lo último no es técnica: es orientarse', [
        dict(num=14, titulo='Santa Tell Me', autor='Ariana Grande, arr. Sadie King',
             tonalidad='Sol mayor', compas='4/4', trabaja='Segno, casillas, coda y cruce de manos'),
        dict(num=15, titulo='It’s Beginning to Look a Lot Like Christmas',
             autor='Meredith Willson · a 4 manos',
             tonalidad='Do mayor', compas='6/8', trabaja='El 6/8 contado en dos, y entrar a dúo'),
        dict(num=16, titulo='Arabesque', autor='Burgmüller op. 100 nº 2 · a 4 manos',
             tonalidad='La menor', compas='2/4', trabaja='Picado a velocidad, y las dos manos al unísono'),
        dict(num=17, titulo='Bohemian Rhapsody', autor='Queen · Freddie Mercury',
             tonalidad='Si♭ mayor', compas='4/4 · 5/4',
             trabaja='Un bajo cromático, compases que cambian y D.S. al Fine'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# Mismo criterio que en el cuaderno de Dilan: dos semanas por pieza (una para
# desmontarla y otra para montarla), el orden del indice como hilo principal,
# y las fechas que mandan sobre ese orden porque la alumna las tiene en la
# cabeza igual:
#
#   · Halloween (semana 8) -> las dos piezas en menor del cuaderno, Arabesque
#     (La menor) y Poema de Amor (Sol menor). No se estudian enteras ahi: se
#     leen y se prueban, que es lo que cabe en una semana.
#   · Navidad (semanas 15 y 16) -> las tres de diciembre. Se adelantan a
#     proposito: en enero ya no sirven.
#   · Final de curso (semanas 42-44) -> programa, ensayo y concierto.
#
# Bohemian Rhapsody, que es la ultima y la mas exigente, se lleva tres
# semanas en vez de dos: una solo para el recorrido y los compases raros.
PLAN = [
    ('Septiembre', [
        (1, '1 · Can’t Help Falling in Love — el arpegio', 'obra'),
        (2, '1 · Can’t Help — manos juntas', 'obra'),
        (3, '2 · A Sky Full of Stars — la melodía primero', 'obra'),
        (4, '2 · A Sky Full of Stars — el riff, sin endurecerse', 'obra'),
    ]),
    ('Octubre', [
        (5, '3 · Poema de Amor — el molde de la izquierda', 'obra'),
        (6, '3 · Poema de Amor — manos juntas', 'obra'),
        (7, '4 · What Was I Made For? — contar los silencios', 'obra'),
        (8, 'HALLOWEEN · 16 Arabesque y 3 Poema: leer el menor', 'especial'),
    ]),
    ('Noviembre', [
        (9, '4 · What Was I Made For? — a tempo', 'obra'),
        (10, '5 · Thinking Out Loud — sostener', 'obra'),
        (11, '5 · Thinking Out Loud — entrar a contratiempo', 'obra'),
        (12, 'REPASO · las cinco primeras, seguidas', 'repaso'),
    ]),
    ('Diciembre', [
        (13, '6 · El Cisne — la escala escondida', 'obra'),
        (14, '6 · El Cisne — el fondo, igual 55 compases', 'obra'),
        (15, 'NAVIDAD · 13 Merry Little Christmas', 'especial'),
        (16, 'NAVIDAD · 14 Santa Tell Me y 15 It’s Beginning', 'especial'),
    ]),
    ('Enero', [
        (17, '7 · When I Was Your Man — el acorde desde el bajo', 'obra'),
        (18, '7 · When I Was Your Man — de memoria', 'obra'),
        (19, '8 · La Promesa — la derecha, que habla', 'obra'),
        (20, '8 · La Promesa — las dos capas con pedal', 'obra'),
    ]),
    ('Febrero', [
        (21, 'REPASO · de la 1 a la 8, media hoja cada una', 'repaso'),
        (22, '9 · Amiga Mía — las dos voces de una mano', 'obra'),
        (23, '9 · Amiga Mía — la frase entera sin cortar', 'obra'),
        (24, '10 · When We Were Young — el bajo del cifrado', 'obra'),
    ]),
    ('Marzo', [
        (25, '10 · When We Were Young — las cuatro páginas', 'obra'),
        (26, '11 · Soldadito de Hierro — el tresillo, sin la pieza', 'obra'),
        (27, '11 · Soldadito — con la izquierda puesta', 'obra'),
        (28, '12 · My Favourite Things — los golpes de arriba', 'obra'),
    ]),
    ('Abril', [
        (29, '12 · My Favourite Things — subir hasta ♩=160', 'obra'),
        (30, 'REPASO · elige tres y tócalas seguidas', 'repaso'),
        (31, '13 · Merry Little Christmas — el equilibrio', 'obra'),
        (32, '14 · Santa Tell Me — el recorrido, con lápiz', 'obra'),
    ]),
    ('Mayo', [
        (33, '14 · Santa Tell Me — las dos izquierdas', 'obra'),
        (34, '15 · It’s Beginning — las dos manos, sin eco', 'obra'),
        (35, '15 · It’s Beginning — a dúo con la profesora', 'obra'),
        (36, '16 · Arabesque — el ataque, comparando el sonido', 'obra'),
    ]),
    ('Junio', [
        (37, '16 · Arabesque — a dúo, entrando en el c. 3', 'obra'),
        (38, '17 · Bohemian Rhapsody — el recorrido y los compases raros', 'obra'),
        (39, '17 · Bohemian Rhapsody — el bajo que baja', 'obra'),
        (40, '17 · Bohemian Rhapsody — las dos texturas', 'obra'),
    ]),
    ('Julio', [
        (41, 'REPASO · las tres de Navidad, para no perderlas', 'repaso'),
        (42, 'Elegir el programa del concierto', 'repaso'),
        (43, 'ENSAYO GENERAL · el programa entero, sin parar', 'concierto'),
        (44, 'CONCIERTO DE FIN DE CURSO', 'concierto'),
    ]),
]

# los PDF de cada dosier, en orden
DOSIERES = [
    'Eva_01_CantHelp_CUADERNO.pdf',
    'Eva_02_SkyFullOfStars_CUADERNO.pdf',
    'Eva_03_PoemaDeAmor_CUADERNO.pdf',
    'Eva_04_WhatWasIMadeFor_CUADERNO.pdf',
    'Eva_05_ThinkingOutLoud_CUADERNO.pdf',
    'Eva_06_ElCisne_CUADERNO.pdf',
    'Eva_07_WhenIWasYourMan_CUADERNO.pdf',
    'Eva_08_LaPromesa_CUADERNO.pdf',
    'Eva_09_AmigaMia_CUADERNO.pdf',
    'Eva_10_WhenWeWereYoung_CUADERNO.pdf',
    'Eva_11_Soldadito_CUADERNO.pdf',
    'Eva_12_MyFavouriteThings_CUADERNO.pdf',
    'Eva_13_MerryLittleChristmas_CUADERNO.pdf',
    'Eva_14_SantaTellMe_CUADERNO.pdf',
    'Eva_15_BeginningChristmas_CUADERNO.pdf',
    'Eva_16_Arabesque_CUADERNO.pdf',
    'Eva_17_BohemianRhapsody_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Eva_Portada_Indice.pdf')
    c = canvas.Canvas(tapas, pagesize=(W, H))
    build_cover(c, os.path.join(ASSETS, 'asset_logo_tclas_v2.png'), ALUMNO, SUBTITULO, CURSO)
    pag = build_index(c, ALUMNO, ETAPAS)
    build_plan_curso(c, ALUMNO, PLAN, page_num=pag + 1)
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

    out = os.path.join(OUT_DIR, 'Eva_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    print('generado', out, '·', len(PdfReader(out).pages), 'paginas')


if __name__ == '__main__':
    main()
