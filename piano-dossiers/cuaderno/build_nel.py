# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Nel.

   Formato ADULTO estándar (seis hojas por pieza), el mismo esquema que José
   María, Josep, Luisa y Mercè — sin los bloques de la versión exigente de
   Josep. Nel tiene doce años, es muy listo y lleva años viniendo a clase,
   pero se desconcentra rápido; el encargo del cliente fue subirle el nivel
   de verdad y darle contenido para aplicarse. Eso se hace con la curva de
   lectura (`cancion.CURVA['nel']`, al ritmo de los avanzados) y con lo
   exigente del repertorio y del andamio escrito, no añadiendo bloques nuevos
   que no se han pedido.

   16 de las 17 partituras son el mismo archivo, byte a byte, que las de
   otros alumnos — ver TRANSCRIPCION_NEL_FUENTES.md. La única propia es
   Diamonds (Rihanna). El andamio inventado no coincide con el de nadie: lo
   comprueba `cruzar_nel.py` (con dos citas literales aceptadas a propósito,
   documentadas en el propio script).

   Antes de ejecutarlo tiene que salir TODO OK en auditar_nel.py y 0 solapes
   inesperados en cruzar_nel.py.
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

ALUMNO = 'Nel'
SUBTITULO = 'Diecisiete piezas, a por todas'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('Empezar fuerte', 'un dueto de entrada y una digitación que no perdona', [
        dict(num=1, titulo='Petite Chanson', autor='Riccardo Collu · a cuatro manos',
             tonalidad='Do mayor', compas='4/4', trabaja='La anacrusa de dos corcheas, entre dos'),
        dict(num=2, titulo='Counting Stars', autor='OneRepublic · arr. Becky Messer',
             tonalidad='Do mayor', compas='4/4', trabaja='La digitación impresa, nota a nota, sin fallar'),
    ]),
    ('La izquierda se pone a trabajar', 'del acompañamiento que aguanta al que corre', [
        dict(num=3, titulo='Heart and Soul', autor='Hoagy Carmichael · easy piano',
             tonalidad='Fa mayor', compas='4/4', trabaja='El swing y el bajo con acorde, sin mirarse la mano'),
        dict(num=4, titulo='Hit the Road Jack', autor='Popularizada por Ray Charles',
             tonalidad='Do mayor', compas='4/4', trabaja='La primera armadura, con dos texturas distintas'),
        dict(num=5, titulo='Jailhouse Rock', autor='Elvis Presley · arr. Sadie King',
             tonalidad='Fa mayor · blues', compas='4/4', trabaja='Subir a ♩ = 150 sin perder ni un fallo por el camino'),
    ]),
    ('El primer tono menor, y villancico', 'diciembre, con dos texturas que no se parecen', [
        dict(num=6, titulo='Bella Ciao', autor='popular italiana · a cuatro manos',
             tonalidad='Do mayor', compas='4/4', trabaja='Una sensible que va y viene, con metrónomo siempre'),
        dict(num=7, titulo='Deck the Halls', autor='villancico · arr. Jim Paterson',
             tonalidad='Sol menor', compas='4/4', trabaja='Acordes de dos notas en las dos manos a la vez'),
    ]),
    ('Tonalidades nuevas, y una marcha de verdad', 'sostenidos, bemoles y el nivel más alto del cuaderno', [
        dict(num=8, titulo="Can't Help Falling in Love", autor='Elvis Presley · arr. Seb Alejandro',
             tonalidad='Re mayor', compas='3/4', trabaja='Una izquierda que no se para, de memoria'),
        dict(num=9, titulo='Toreador · Carmen', autor='Bizet · Level Four',
             tonalidad='Fa mayor', compas='4/4', trabaja='El pulso de marcha, que no se mueve nunca'),
        dict(num=10, titulo='Lovely', autor='Billie Eilish con Khalid · arr. Amy Kieran',
             tonalidad='Mi menor', compas='4/4', trabaja='Corcheas sin parar: resistencia, no dificultad'),
        dict(num=11, titulo='Rasputin', autor='Boney M · easy piano',
             tonalidad='Si menor', compas='4/4', trabaja='Contar los compases callados a ♩ = 124'),
    ]),
    ('La que es solo tuya', 'la única partitura de tu carpeta que nadie más tiene', [
        dict(num=12, titulo='Diamonds', autor='Rihanna · easy piano, short form',
             tonalidad='Re mayor', compas='4/4', trabaja='La anacrusa corta, y una izquierda que cambia de textura'),
    ]),
    ('Los cinco retos del final', 'aquí el cuaderno deja de ser cómodo, y a propósito', [
        dict(num=13, titulo='My Favourite Things', autor='Rodgers y Hammerstein · arr. Kaitlin',
             tonalidad='Mi menor', compas='3/4', trabaja='55 compases a ♩ = 160 sin perder el sitio'),
        dict(num=14, titulo="Sweet Child O' Mine", autor="Guns N' Roses · arr. Sadie King",
             tonalidad='Si bemol', compas='4/4', trabaja='El pedal, escrito compás a compás'),
        dict(num=15, titulo='Merry Go Round of Life', autor='Joe Hisaishi · piano solo',
             tonalidad='Si bemol', compas='3/4', trabaja='Terceras en corcheas, y dos velocidades escritas'),
        dict(num=16, titulo='A comme amour', autor='Richard Clayderman',
             tonalidad='Mi m → La m', compas='4/4', trabaja='El único cambio de armadura de tu álbum'),
        dict(num=17, titulo='Flying Theme', autor='Cómo entrenar a tu dragón · John Powell',
             tonalidad='Do → Re', compas='4/4', trabaja='Un cambio de tonalidad a mitad de la pieza'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# Dale caña: la mayoría de piezas llevan dos semanas, y las siete más
# exigentes (Jailhouse Rock, Toreador, Diamonds, My Favourite Things, Sweet
# Child O'Mine, Merry Go Round y Flying Theme) llevan tres. Con Deck the
# Halls adelantado a diciembre y dos semanas de repaso, salen 44 semanas
# justas.
PLAN = [
    ('Septiembre', [
        (1, '1 · Petite Chanson — la anacrusa, entre dos', 'obra'),
        (2, '1 · Petite Chanson — a ♩ = 80, con la profesora', 'obra'),
        (3, '2 · Counting Stars — la digitación impresa, toda', 'obra'),
        (4, '2 · Counting Stars — las dos manos, ligadas incluidas', 'obra'),
    ]),
    ('Octubre', [
        (5, '3 · Heart and Soul — el bajo con acorde, a ciegas', 'obra'),
        (6, '3 · Heart and Soul — el swing, y las dos manos', 'obra'),
        (7, '4 · Hit the Road Jack — marcar todos los Si', 'obra'),
        (8, '4 · Hit the Road Jack — la intro y la melodía', 'obra'),
    ]),
    ('Noviembre', [
        (9, '5 · Jailhouse Rock — la entrada y el Si bemol', 'obra'),
        (10, '5 · Jailhouse Rock — subir por escalones a 150', 'obra'),
        (11, '5 · Jailhouse Rock — la izquierda del c. 12', 'obra'),
        (12, '6 · Bella Ciao — el primer tono menor', 'obra'),
    ]),
    ('Diciembre', [
        (13, '6 · Bella Ciao — el dueto, con metrónomo', 'obra'),
        (14, 'NAVIDAD · 7 Deck the Halls — el bemol y el salto', 'especial'),
        (15, 'NAVIDAD · 7 Deck the Halls — acordes en las dos manos', 'especial'),
        (16, 'REPASO · elige tres piezas y tócalas seguidas', 'repaso'),
    ]),
    ('Enero', [
        (17, "8 · Can't Help Falling — la izquierda sin pararse", 'obra'),
        (18, "8 · Can't Help Falling — los acordes, de memoria", 'obra'),
        (19, '9 · Toreador — el ritmo de marcha', 'obra'),
        (20, '9 · Toreador — el paso firme de la izquierda', 'obra'),
    ]),
    ('Febrero', [
        (21, '9 · Toreador — las dos manos, a paso de marcha', 'obra'),
        (22, '10 · Lovely — cuatro compases y parar', 'obra'),
        (23, '10 · Lovely — veinte compases con las corcheas iguales', 'obra'),
        (24, '11 · Rasputin — contar los compases callados', 'obra'),
    ]),
    ('Marzo', [
        (25, '11 · Rasputin — subir a ♩ = 124', 'obra'),
        (26, '12 · Diamonds — la anacrusa corta, aislada', 'obra'),
        (27, '12 · Diamonds — la izquierda que cambia de textura', 'obra'),
        (28, '12 · Diamonds — entera, con la letra', 'obra'),
    ]),
    ('Abril', [
        (29, '13 · My Favourite Things — marcar las frases a lápiz', 'obra'),
        (30, '13 · My Favourite Things — leer por acordes', 'obra'),
        (31, '13 · My Favourite Things — la página entera a 160', 'obra'),
        (32, 'REPASO · elige tres piezas y tócalas seguidas', 'repaso'),
    ]),
    ('Mayo', [
        (33, "14 · Sweet Child O' Mine — el pedal, con la izquierda sola", 'obra'),
        (34, "14 · Sweet Child O' Mine — el riff, con la mano quieta", 'obra'),
        (35, "14 · Sweet Child O' Mine — las dos manos y el pie", 'obra'),
        (36, '15 · Merry Go Round — las terceras, pareja a pareja', 'obra'),
    ]),
    ('Junio', [
        (37, '15 · Merry Go Round — el vals del c. 27, a 152', 'obra'),
        (38, '15 · Merry Go Round — las dos manos en el vals', 'obra'),
        (39, '16 · A comme amour — el cambio de armadura del c. 10', 'obra'),
        (40, '16 · A comme amour — entera, a ♩ = 69', 'obra'),
    ]),
    ('Julio', [
        (41, '17 · Flying Theme — las dos manos moviéndose a la vez', 'obra'),
        (42, '17 · Flying Theme — el cambio de tono, aislado', 'obra'),
        (43, '17 · Flying Theme — los acordes de la derecha', 'obra'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]

NOTA_PLAN = ('Las 44 semanas del curso, repartidas. La mayoría de piezas llevan dos semanas, y las '
             'siete más exigentes llevan tres. De cada una te llevas la hoja de calentamiento, la de '
             'agudeza visual, la de cómo se estudia y la de relajación, con el recuadro de deberes al '
             'pie. Es una propuesta, no una obligación: si una pieza pide más tiempo, se le da.')

DOSIERES = [
    'Nel_01_PetiteChanson_CUADERNO.pdf',
    'Nel_02_CountingStars_CUADERNO.pdf',
    'Nel_03_DeckTheHalls_CUADERNO.pdf',
    'Nel_04_HeartAndSoul_CUADERNO.pdf',
    'Nel_05_HitTheRoadJack_CUADERNO.pdf',
    'Nel_06_JailhouseRock_CUADERNO.pdf',
    'Nel_07_BellaCiao_CUADERNO.pdf',
    'Nel_08_CantHelpFalling_CUADERNO.pdf',
    'Nel_09_Toreador_CUADERNO.pdf',
    'Nel_10_Lovely_CUADERNO.pdf',
    'Nel_11_Rasputin_CUADERNO.pdf',
    'Nel_12_Diamonds_CUADERNO.pdf',
    'Nel_13_MyFavouriteThings_CUADERNO.pdf',
    'Nel_14_SweetChildOMine_CUADERNO.pdf',
    'Nel_15_MerryGoRoundOfLife_CUADERNO.pdf',
    'Nel_16_AcommeAmour_CUADERNO.pdf',
    'Nel_17_FlyingTheme_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Nel_Portada_Indice.pdf')
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
    out = os.path.join(OUT_DIR, 'Nel_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
