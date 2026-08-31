# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Eduard.

   Formato ADULTO (seis hojas por pieza). **Rehecho de arriba abajo en agosto
   de 2026**: la versión anterior era una copia del cuaderno de José María y le
   quedaba muy por encima del nivel. El cliente lo dijo claro —"un señor de
   unos 65 años con un nivel bajo, que necesita aprender con buena teoría y
   explicaciones"— y pasó su carpeta de Drive.

   De ahí salen diecisiete partituras. Las otras dos se rescataron del dosier
   antiguo porque encajan en su nivel (America y el Star-Spangled Banner), tal
   y como pidió el cliente: "si de paso ves alguna partitura del dosier antiguo
   que cuadra con el nivel, la puedes añadir también".

   **Ajuste del 31 de agosto de 2026**, pedido por el cliente después de tocar
   su carpeta de Drive: entra *Puff, el dragón mágico* (que subió él mismo como
   "Copia de Puff era un Drac Magic.pdf") y salen el *Romance* de Diabelli y
   *Deck the Halls*. El álbum queda en **diecinueve piezas** y 44 semanas, y
   todo lo que iba detrás se corrió un número hacia arriba.

   EL ORDEN NO ES EL DE SIEMPRE, y esa es la decisión de fondo del álbum. Las
   tres primeras piezas se tocan con UNA SOLA MANO. La izquierda no aparece
   hasta la cuarta, y ahí solo apoya una vez por compás. Cada mano no va de
   verdad a lo suyo hasta la sexta, y la primera armadura no llega hasta la
   decimocuarta. Los dos retos del final —el Grandfather's Clock y el
   Toreador— están ahí porque el cliente los quiso como reto de fin de curso,
   no porque toquen antes.

   Antes de ejecutarlo tiene que salir TODO OK en `auditar_eduard.py` y, en
   `cruzar_eduard.py`, cero andamio inventado repetido: cinco de sus diecinueve
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
    ('La derecha canta y la izquierda apoya', 'una nota por compás abajo: con eso basta para empezar', [
        dict(num=4, titulo='America', autor="My Country, 'Tis of Thee · arr. G. DeBenedetti",
             tonalidad='Do mayor', compas='3/4', trabaja='La primera melodía, y la negra con puntillo'),
        dict(num=5, titulo='The Star-Spangled Banner', autor='F. S. Key · arr. G. DeBenedetti',
             tonalidad='Do mayor', compas='3/4', trabaja='Entrar después de un silencio'),
    ]),
    ('Cada mano a lo suyo', 'el reparto de trabajo más común del piano', [
        dict(num=6, titulo='La Pantera Rosa', autor='Henry Mancini · arreglo fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='La izquierda empieza sola y la derecha calla tres compases'),
        dict(num=7, titulo='Nocturno op. 9 nº 2', autor='Chopin · versión muy simplificada',
             tonalidad='Do mayor', compas='3/4', trabaja='Notas largas: aguantar el sonido sin correr'),
        dict(num=8, titulo='The Beginner', autor='Cornelius Gurlitt · a cuatro manos',
             tonalidad='Do mayor', compas='3/4', trabaja='Las dos manos al unísono, y los primeros reguladores'),
    ]),
    ('Un acompañamiento que aguanta, y un dueto', 'la izquierda coge su sitio y no lo suelta', [
        dict(num=9, titulo='Puff, el dragón mágico', autor='Yarrow y Lipton · arr. Eric Moore',
             tonalidad='Do mayor', compas='4/4', trabaja='Un acorde de dos notas que dura el compás entero'),
        dict(num=10, titulo='Heart and Soul', autor='Carmichael y Loesser · arreglo fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='Cuatro acordes en la izquierda, sin parar'),
        dict(num=11, titulo='I Have a Dream', autor='ABBA · arreglo fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='La negra con puntillo dentro de la frase'),
        dict(num=12, titulo='Villancicos a cuatro manos', autor='Jingle Bells + We Wish You a Merry Christmas',
             tonalidad='Do mayor', compas='4/4', trabaja='Las dos manos en clave de sol, y tocar con otra persona'),
    ]),
    ('El tono menor, y las armaduras', 'mirar el principio del pentagrama antes de tocar', [
        dict(num=13, titulo='Greensleeves', autor='canción inglesa del siglo XVI',
             tonalidad='La menor', compas='3/4', trabaja='El primer tono menor, y sin ninguna alteración'),
        dict(num=14, titulo='Honor Him', autor='Hans Zimmer · Gladiator',
             tonalidad='Fa# menor', compas='3/4', trabaja='Tres sostenidos, y una nota que dura tres compases'),
        dict(num=15, titulo='Rasputin', autor='Boney M · easy piano',
             tonalidad='Si menor', compas='4/4', trabaja='Dos sostenidos, y contar los compases callados'),
    ]),
    ('Velocidad, silencios y los dos retos del final', 'los dos últimos están aquí porque son el reto', [
        dict(num=16, titulo='Jingle Bell Rock', autor='Beal y Boothe · arreglo fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='Cuatro corcheas seguidas y una ligadura de unión'),
        dict(num=17, titulo='Piano Man', autor='Billy Joel · arreglo fácil',
             tonalidad='Do mayor', compas='3/4', trabaja='Un vals con más silencios que notas'),
        dict(num=18, titulo="My Grandfather's Clock", autor='H. C. Work · arr. G. DeBenedetti',
             tonalidad='Sol mayor', compas='4/4', trabaja='Un solo sostenido, y tocar a tiempo exacto'),
        dict(num=19, titulo='Toreador', autor='Bizet · Carmen · arr. G. DeBenedetti',
             tonalidad='Fa mayor', compas='4/4', trabaja='Level Four: la vara de medir del curso'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# Dos semanas por pieza, las diecinueve (38), y seis semanas sueltas: una en
# diciembre para tocar los dos de Navidad seguidos, otra para repasar el otoño,
# y las cuatro de julio para el repaso y la audición. Las dos piezas de Navidad
# —los villancicos a cuatro manos y el Jingle Bell Rock— se adelantan a
# noviembre y diciembre aunque en el álbum vayan en otro sitio: en enero ya no
# sirven.
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
        (7, '4 · America — la melodía, sin el puntillo', 'obra'),
        (8, '4 · America — con el ritmo de verdad, y la izquierda', 'obra'),
    ]),
    ('Noviembre', [
        (9, '5 · Star-Spangled Banner — entrar tras el silencio', 'obra'),
        (10, '5 · Star-Spangled Banner — las dos manos', 'obra'),
        (11, 'NAVIDAD · 12 Villancicos — la izquierda, que no cambia', 'especial'),
        (12, 'NAVIDAD · 12 Villancicos — con la profesora, a cuatro manos', 'especial'),
    ]),
    ('Diciembre', [
        (13, 'NAVIDAD · 16 Jingle Bell Rock — corta, corta, larga', 'especial'),
        (14, 'NAVIDAD · 16 Jingle Bell Rock — las cuatro corcheas y la ligadura', 'especial'),
        (15, 'NAVIDAD · los dos villancicos seguidos, para tocarlos en casa', 'especial'),
        (16, 'REPASO · las cinco primeras, una detrás de otra', 'repaso'),
    ]),
    ('Enero', [
        (17, '6 · La Pantera Rosa — la izquierda sola, y contar', 'obra'),
        (18, '6 · La Pantera Rosa — la entrada de la derecha', 'obra'),
        (19, '7 · Nocturno — que una nota larga dure lo que dura', 'obra'),
        (20, '7 · Nocturno — la primera línea, con las dos manos', 'obra'),
    ]),
    ('Febrero', [
        (21, '8 · The Beginner — la melodía, con cada mano por separado', 'obra'),
        (22, '8 · The Beginner — las dos juntas, que suenen a un golpe', 'obra'),
        (23, '9 · Puff — los tres acordes de la izquierda, aguantados', 'obra'),
        (24, '9 · Puff — el puntillo del compás 1, con las dos manos', 'obra'),
    ]),
    ('Marzo', [
        (25, '10 · Heart and Soul — la izquierda, de memoria', 'obra'),
        (26, '10 · Heart and Soul — las dos manos', 'obra'),
        (27, '11 · I Have a Dream — la negra con puntillo, aparte', 'obra'),
        (28, '11 · I Have a Dream — la frase entera, con la letra', 'obra'),
    ]),
    ('Abril', [
        (29, '13 · Greensleeves — el acorde roto de la izquierda', 'obra'),
        (30, '13 · Greensleeves — la melodía, con su anacrusa', 'obra'),
        (31, '14 · Honor Him — las tres teclas de la armadura', 'obra'),
        (32, '14 · Honor Him — los tres primeros compases, con las dos manos', 'obra'),
    ]),
    ('Mayo', [
        (33, '15 · Rasputin — contar los compases callados', 'obra'),
        (34, '15 · Rasputin — subir a ♩ = 124', 'obra'),
        (35, '17 · Piano Man — el compás en el que la izquierda calla', 'obra'),
        (36, '17 · Piano Man — los tres primeros compases seguidos', 'obra'),
    ]),
    ('Junio', [
        (37, "18 · Grandfather's Clock — el sostenido de la armadura", 'obra'),
        (38, "18 · Grandfather's Clock — a tiempo exacto", 'obra'),
        (39, '19 · Toreador — el ritmo de marcha, despacio', 'obra'),
        (40, '19 · Toreador — entera, comparándola con America', 'obra'),
    ]),
    ('Julio', [
        (41, 'REPASO · las tres primeras, una detrás de otra', 'repaso'),
        (42, 'REPASO · elige tres del resto y tócalas seguidas', 'repaso'),
        (43, 'ENSAYO · las tres elegidas, sin parar y sin repetir', 'concierto'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]
NOTA_PLAN = ('Las 44 semanas del curso, repartidas. Cada pieza tiene dos semanas y de cada una te '
             'llevas la hoja de trabajo con el plan de minutos. Las dos de Navidad se adelantan a '
             'noviembre y diciembre aunque en el cuaderno estén en otro sitio. Es una propuesta, no '
             'una obligación: si una pieza pide una semana más, se le da, y si sale antes, se pasa a '
             'la siguiente.')

DOSIERES = [
    'Eduard_01_Clementine_CUADERNO.pdf',
    'Eduard_02_Aristogatos_CUADERNO.pdf',
    'Eduard_03_EsoQueTuMeDas_CUADERNO.pdf',
    'Eduard_04_America_CUADERNO.pdf',
    'Eduard_05_StarSpangledBanner_CUADERNO.pdf',
    'Eduard_06_PanteraRosa_CUADERNO.pdf',
    'Eduard_07_NocturnoChopin_CUADERNO.pdf',
    'Eduard_08_TheBeginner_CUADERNO.pdf',
    'Eduard_09_PuffDragon_CUADERNO.pdf',
    'Eduard_10_HeartAndSoul_CUADERNO.pdf',
    'Eduard_11_IHaveADream_CUADERNO.pdf',
    'Eduard_12_VillancicosCuatroManos_CUADERNO.pdf',
    'Eduard_13_Greensleeves_CUADERNO.pdf',
    'Eduard_14_HonorHim_CUADERNO.pdf',
    'Eduard_15_Rasputin_CUADERNO.pdf',
    'Eduard_16_JingleBellRock_CUADERNO.pdf',
    'Eduard_17_PianoMan_CUADERNO.pdf',
    'Eduard_18_GrandfathersClock_CUADERNO.pdf',
    'Eduard_19_Toreador_CUADERNO.pdf',
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
