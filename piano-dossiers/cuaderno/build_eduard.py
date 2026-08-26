# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Eduard.

   Formato ADULTO (seis hojas por pieza). **Rehecho de arriba abajo en agosto
   de 2026**: la versión anterior era una copia del cuaderno de José María y le
   quedaba muy por encima del nivel. El cliente lo dijo claro —"un señor de
   unos 65 años con un nivel bajo, que necesita aprender con buena teoría y
   explicaciones"— y pasó su carpeta de Drive.

   De ahí salen dieciséis partituras nuevas. Las otras cuatro se rescataron del
   dosier antiguo porque encajan en su nivel (el Romance de Diabelli, America,
   el Star-Spangled Banner y Deck the Halls), tal y como pidió el cliente: "si
   de paso ves alguna partitura del dosier antiguo que cuadra con el nivel, la
   puedes añadir también". Veinte piezas y 44 semanas.

   EL ORDEN NO ES EL DE SIEMPRE, y esa es la decisión de fondo del álbum. Las
   tres primeras piezas se tocan con UNA SOLA MANO, y las dos manos no aparecen
   hasta la cuarta —y al unísono—. Cada mano no va a lo suyo hasta la séptima.
   La armadura no llega hasta la duodécima. Los dos retos del final —el
   Grandfather's Clock y el Toreador— están ahí porque el cliente los quiso
   como reto de fin de curso, no porque toquen antes.

   Antes de ejecutarlo tiene que salir TODO OK en `auditar_eduard.py` y, en
   `cruzar_eduard.py`, cero andamio inventado repetido: siete de sus veinte
   partituras son el mismo fichero que las de otro alumno.
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

ALUMNO = 'Eduard'
SUBTITULO = 'Empezar de cero, a los sesenta y cinco'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('Una sola mano, y aprender a contar', 'lo primero no son los dedos: es el compás', [
        dict(num=1, titulo='Clementine', autor='popular · arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='3/4', trabaja='Un solo pentagrama, y entrar en anacrusa'),
        dict(num=2, titulo='Los Aristogatos', autor='hermanos Sherman · arr. A. C. Escobés',
             tonalidad='Do mayor', compas='4/4', trabaja='Contar dos tiempos de silencio antes de tocar'),
        dict(num=3, titulo='Eso que tú me das', autor='Jarabe de Palo · Pau Donés',
             tonalidad='Do mayor', compas='4/4', trabaja='Un salto de quinta, y qué son las letras de acorde'),
    ]),
    ('Entran las dos manos, haciendo lo mismo', 'dos manos, pero una sola cosa que leer', [
        dict(num=4, titulo='Romance', autor='Anton Diabelli · Primo, a cuatro manos',
             tonalidad='Do mayor', compas='¢', trabaja='Posición fija de cinco dedos, y las dos manos al unísono'),
        dict(num=5, titulo='America', autor="My Country, 'Tis of Thee · arr. G. DeBenedetti",
             tonalidad='Do mayor', compas='3/4', trabaja='La primera melodía, y la negra con puntillo'),
        dict(num=6, titulo='The Star-Spangled Banner', autor='F. S. Key · arr. G. DeBenedetti',
             tonalidad='Do mayor', compas='3/4', trabaja='Entrar después de un silencio'),
    ]),
    ('Cada mano a lo suyo', 'el reparto de trabajo más común del piano', [
        dict(num=7, titulo='La Pantera Rosa', autor='Henry Mancini · arreglo fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='La izquierda empieza sola y la derecha calla tres compases'),
        dict(num=8, titulo='Nocturno op. 9 nº 2', autor='Chopin · versión muy simplificada',
             tonalidad='Do mayor', compas='3/4', trabaja='Notas largas: aguantar el sonido sin correr'),
        dict(num=9, titulo='The Beginner', autor='Cornelius Gurlitt · a cuatro manos',
             tonalidad='Do mayor', compas='3/4', trabaja='Otra vez al unísono, y los primeros reguladores'),
        dict(num=10, titulo='Heart and Soul', autor='Carmichael y Loesser · arreglo fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='Cuatro acordes en la izquierda, sin parar'),
        dict(num=11, titulo='I Have a Dream', autor='ABBA · arreglo fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='La negra con puntillo dentro de la frase'),
    ]),
    ('La primera armadura', 'mirar el principio del pentagrama antes de tocar', [
        dict(num=12, titulo='Deck the Halls', autor='villancico · arr. Jim Paterson',
             tonalidad='Fa mayor', compas='4/4', trabaja='Un bemol, y las dos manos con acordes'),
        dict(num=13, titulo='Villancicos a cuatro manos', autor='Jingle Bells + We Wish You a Merry Christmas',
             tonalidad='Do mayor', compas='4/4', trabaja='Las dos manos en clave de sol, y tocar con otra persona'),
        dict(num=14, titulo='Greensleeves', autor='canción inglesa del siglo XVI',
             tonalidad='La menor', compas='3/4', trabaja='El primer tono menor, y el acorde roto'),
        dict(num=15, titulo='Honor Him', autor='Hans Zimmer · Gladiator',
             tonalidad='Fa# menor', compas='3/4', trabaja='Tres sostenidos, y una nota que dura tres compases'),
    ]),
    ('Corcheas, silencios y velocidad', 'lo mismo de siempre, pero sin tiempo para pensar', [
        dict(num=16, titulo='Rasputin', autor='Boney M · easy piano',
             tonalidad='Si menor', compas='4/4', trabaja='Dos sostenidos, y contar los compases callados'),
        dict(num=17, titulo='Jingle Bell Rock', autor='Beal y Boothe · arreglo fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='Cuatro corcheas seguidas y una ligadura de unión'),
        dict(num=18, titulo='Piano Man', autor='Billy Joel · arreglo fácil',
             tonalidad='Do mayor', compas='3/4', trabaja='Un vals con más silencios que notas'),
    ]),
    ('Los dos retos del final', 'están aquí porque son el reto, no porque toquen antes', [
        dict(num=19, titulo="My Grandfather's Clock", autor='H. C. Work · arr. G. DeBenedetti',
             tonalidad='Sol mayor', compas='4/4', trabaja='El primer sostenido, y tocar a tiempo exacto'),
        dict(num=20, titulo='Toreador', autor='Bizet · Carmen · arr. G. DeBenedetti',
             tonalidad='Fa mayor', compas='4/4', trabaja='Level Four: la vara de medir del curso'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# Dos semanas por pieza, las veinte, y cuatro semanas sueltas al final para
# repasar y preparar la audición. Las tres piezas de Navidad —Deck the Halls,
# los villancicos a cuatro manos y Jingle Bell Rock— se adelantan a noviembre y
# diciembre aunque en el álbum vayan en otro sitio: en enero ya no sirven.
PLAN = [
    ('Septiembre', [
        (1, '1 · Clementine — contar tres, y entrar antes del compás', 'obra'),
        (2, '1 · Clementine — la pieza entera, con la mano quieta', 'obra'),
        (3, '2 · Los Aristogatos — contar dos tiempos sin tocar', 'obra'),
        (4, '2 · Los Aristogatos — la subida Sol-La-Si-Do', 'obra'),
    ]),
    ('Octubre', [
        (5, '3 · Eso que tú me das — el salto de Do a Sol', 'obra'),
        (6, '3 · Eso que tú me das — la página entera, con la letra', 'obra'),
        (7, '4 · Romance — colocar la mano y no moverla', 'obra'),
        (8, '4 · Romance — las dos manos a la vez', 'obra'),
    ]),
    ('Noviembre', [
        (9, '5 · America — la melodía, sin el puntillo', 'obra'),
        (10, '5 · America — con el ritmo de verdad', 'obra'),
        (11, 'NAVIDAD · 12 Deck the Halls — el primer bemol', 'especial'),
        (12, 'NAVIDAD · 12 Deck the Halls — entera', 'especial'),
    ]),
    ('Diciembre', [
        (13, 'NAVIDAD · 13 Villancicos — la izquierda, que no cambia', 'especial'),
        (14, 'NAVIDAD · 13 Villancicos — con la profesora, a cuatro manos', 'especial'),
        (15, 'NAVIDAD · 17 Jingle Bell Rock — corta, corta, larga', 'especial'),
        (16, 'NAVIDAD · 17 Jingle Bell Rock — las cuatro corcheas y la ligadura', 'especial'),
    ]),
    ('Enero', [
        (17, '6 · Star-Spangled Banner — entrar tras el silencio', 'obra'),
        (18, '6 · Star-Spangled Banner — las dos manos', 'obra'),
        (19, '7 · La Pantera Rosa — la izquierda sola, y contar', 'obra'),
        (20, '7 · La Pantera Rosa — la entrada de la derecha', 'obra'),
    ]),
    ('Febrero', [
        (21, '8 · Nocturno — que una nota larga dure lo que dura', 'obra'),
        (22, '8 · Nocturno — la primera línea, con las dos manos', 'obra'),
        (23, '9 · The Beginner — la melodía, con cada mano por separado', 'obra'),
        (24, '9 · The Beginner — las dos juntas, que suenen a un golpe', 'obra'),
    ]),
    ('Marzo', [
        (25, '10 · Heart and Soul — la izquierda, de memoria', 'obra'),
        (26, '10 · Heart and Soul — las dos manos', 'obra'),
        (27, '11 · I Have a Dream — la negra con puntillo, aparte', 'obra'),
        (28, '11 · I Have a Dream — la frase entera, con la letra', 'obra'),
    ]),
    ('Abril', [
        (29, '14 · Greensleeves — el acorde roto de la izquierda', 'obra'),
        (30, '14 · Greensleeves — la melodía, con su anacrusa', 'obra'),
        (31, '15 · Honor Him — las tres teclas de la armadura', 'obra'),
        (32, '15 · Honor Him — los tres primeros compases, con las dos manos', 'obra'),
    ]),
    ('Mayo', [
        (33, '16 · Rasputin — contar los compases callados', 'obra'),
        (34, '16 · Rasputin — subir a ♩ = 124', 'obra'),
        (35, '18 · Piano Man — el compás en el que la izquierda calla', 'obra'),
        (36, '18 · Piano Man — los tres primeros compases seguidos', 'obra'),
    ]),
    ('Junio', [
        (37, "19 · Grandfather's Clock — el primer sostenido", 'obra'),
        (38, "19 · Grandfather's Clock — a tiempo exacto", 'obra'),
        (39, '20 · Toreador — el ritmo de marcha, despacio', 'obra'),
        (40, '20 · Toreador — entera, comparándola con America', 'obra'),
    ]),
    ('Julio', [
        (41, 'REPASO · las tres primeras, una detrás de otra', 'repaso'),
        (42, 'REPASO · elige tres del resto y tócalas seguidas', 'repaso'),
        (43, 'ENSAYO · las tres elegidas, sin parar y sin repetir', 'concierto'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]
NOTA_PLAN = ('Las 44 semanas del curso, repartidas. Cada pieza tiene dos semanas y de cada una te '
             'llevas la hoja de trabajo con el plan de minutos. Las tres de Navidad se adelantan a '
             'noviembre y diciembre aunque en el cuaderno estén en otro sitio. Es una propuesta, no '
             'una obligación: si una pieza pide una semana más, se le da, y si sale antes, se pasa a '
             'la siguiente.')

DOSIERES = [
    'Eduard_01_Clementine_CUADERNO.pdf',
    'Eduard_02_Aristogatos_CUADERNO.pdf',
    'Eduard_03_EsoQueTuMeDas_CUADERNO.pdf',
    'Eduard_04_RomanceDiabelli_CUADERNO.pdf',
    'Eduard_05_America_CUADERNO.pdf',
    'Eduard_06_StarSpangledBanner_CUADERNO.pdf',
    'Eduard_07_PanteraRosa_CUADERNO.pdf',
    'Eduard_08_NocturnoChopin_CUADERNO.pdf',
    'Eduard_09_TheBeginner_CUADERNO.pdf',
    'Eduard_10_HeartAndSoul_CUADERNO.pdf',
    'Eduard_11_IHaveADream_CUADERNO.pdf',
    'Eduard_12_DeckTheHalls_CUADERNO.pdf',
    'Eduard_13_VillancicosCuatroManos_CUADERNO.pdf',
    'Eduard_14_Greensleeves_CUADERNO.pdf',
    'Eduard_15_HonorHim_CUADERNO.pdf',
    'Eduard_16_Rasputin_CUADERNO.pdf',
    'Eduard_17_JingleBellRock_CUADERNO.pdf',
    'Eduard_18_PianoMan_CUADERNO.pdf',
    'Eduard_19_GrandfathersClock_CUADERNO.pdf',
    'Eduard_20_Toreador_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Eduard_Portada_Indice.pdf')
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
    out = os.path.join(OUT_DIR, 'Eduard_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
