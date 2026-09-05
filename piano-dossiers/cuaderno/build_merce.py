# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Mercè.

   Formato ADULTO, las mismas seis hojas que José María, Josep y Luisa. Mercè
   no tiene un nivel alto, pero bastante más que Luisa, y su clase de hora y
   media es la más larga del proyecto: por eso su curva de nivel
   (`cancion.CURVA['mercè']`) sube más rápido que la de Luisa, y su plan de
   curso reparte 27 piezas en vez de 19 o 20.

   17 de las 27 partituras son el mismo archivo, byte a byte, que las de
   otros alumnos — ver TRANSCRIPCION_MERCE_FUENTES.md. El andamio inventado
   no coincide con el de nadie: lo comprueba `cruzar_merce.py`.

   Antes de ejecutarlo tiene que salir TODO OK en auditar_merce.py y 0
   solapes en cruzar_merce.py.
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

ALUMNO = 'Mercè'
SUBTITULO = 'Veintisiete piezas, hora y media'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('Las manos que ya conoces', 'duetos y redondas, para entrar con confianza', [
        dict(num=1, titulo='Sonatina per bambini', autor='M. Bazzoni · a cuatro manos',
             tonalidad='La menor', compas='4/4', trabaja='Las dos manos al unísono, y solo negras'),
        dict(num=2, titulo='Oh, When the Saints', autor='Primer nivel · arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='4/4', trabaja='El silencio de la izquierda que se repite cada compás'),
        dict(num=3, titulo="You've Got a Friend in Me", autor='arr. Megan Harper',
             tonalidad='Do mayor', compas='4/4', trabaja='Sostener una redonda el compás entero'),
        dict(num=4, titulo='Puff the Magic Dragon', autor='arr. Eric Moore',
             tonalidad='Do mayor', compas='4/4', trabaja='Dos notas a la vez, sostenidas juntas'),
    ]),
    ('La primera armadura, y los acordes con nombre', 'Sol mayor, corcheas y letras de acorde', [
        dict(num=5, titulo='Sonatina nº 2', autor='M. Bazzoni · a cuatro manos',
             tonalidad='Sol mayor', compas='4/4', trabaja='El primer sostenido, con las manos al unísono'),
        dict(num=6, titulo="Sur le Pont d'Avignon", autor='Nivel dos · arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='4/4', trabaja='Corcheas en las dos manos, con staccato'),
        dict(num=7, titulo='Do Re Mi', autor='R. Rodgers · Sonrisas y Lágrimas',
             tonalidad='Do mayor', compas='4/4', trabaja='El bajo que camina y una carrerilla de corcheas'),
    ]),
    ('Villancicos, y la izquierda que se mueve', 'diciembre, con dos versiones de Silent Night', [
        dict(num=8, titulo='Christmas Songs', autor='M. Liang · a cuatro manos',
             tonalidad='Do mayor', compas='4/4', trabaja='La izquierda cambia de nota a mitad de compás'),
        dict(num=9, titulo='Silent Night', autor='F. X. Gruber · con letra y dedos',
             tonalidad='Do mayor', compas='3/4', trabaja='Dos ritmos a la vez, uno en cada mano'),
        dict(num=10, titulo='We Wish You a Merry Christmas', autor='arr. Gilbert DeBenedetti',
             tonalidad='Sol mayor', compas='3/4', trabaja='La anacrusa, y las primeras letras de acorde'),
        dict(num=11, titulo='Silent Night · a cuatro manos', autor='Piano 1 + Piano 2',
             tonalidad='Do mayor', compas='3/4', trabaja='Sostener mientras se escucha a la otra parte'),
    ]),
    ('Teclas negras y ritmos que respiran', 'entradas retrasadas y el primer puntillo', [
        dict(num=12, titulo='La Panthère rose', autor='H. Mancini · Première année',
             tonalidad='Do mayor', compas='4/4', trabaja='Tres compases callados, y sostenidos sueltos'),
        dict(num=13, titulo='Piano Man', autor='Billy Joel · SimplyPiano',
             tonalidad='Do mayor', compas='3/4', trabaja='Contar los compases donde la izquierda no toca'),
        dict(num=14, titulo='Bela Ciao', autor='popular italiana · La Casa de Papel',
             tonalidad='Mi menor', compas='2/4', trabaja='El primer tono menor, y entrar media parte tarde'),
    ]),
    ('Acordes dobles y compases nuevos', 'de las redondas ligadas a los intervalos repetidos', [
        dict(num=15, titulo='Spring', autor='Vivaldi · con intervalos dobles',
             tonalidad='Do mayor', compas='4/4', trabaja='Repetir un intervalo con los mismos dos dedos'),
        dict(num=16, titulo='Greensleeves', autor='tradicional inglesa · con cifrado',
             tonalidad='La menor', compas='3/4', trabaja='Entrar antes del compás, con la izquierda caminando'),
        dict(num=17, titulo='Counting Stars', autor='OneRepublic · arr. Becky Messer',
             tonalidad='Do mayor', compas='4/4', trabaja='Redondas ligadas, y la digitación impresa'),
        dict(num=18, titulo='Largo · Sinfonía del Nuevo Mundo', autor='Dvořák · arr. A. C. Escobés',
             tonalidad='Do mayor', compas='4/4', trabaja='Notas que cruzan de un compás a otro'),
        dict(num=19, titulo="My Grandfather's Clock", autor='H. C. Work · Nivel tres',
             tonalidad='Sol mayor', compas='4/4', trabaja='Digitación exacta en las dos manos'),
        dict(num=20, titulo='I Have a Dream', autor='ABBA',
             tonalidad='Do mayor', compas='4/4', trabaja='El primer puntillo del álbum, contado en corcheas'),
    ]),
    ('Los seis retos del final', 'bemoles, sostenidos y la pieza más exigente del cuaderno', [
        dict(num=21, titulo='Beauty and the Beast', autor='Alan Menken · arr. Naf',
             tonalidad='Fa mayor', compas='4/4', trabaja='Acordes de tres notas repetidos con el brazo'),
        dict(num=22, titulo='Honor Him · Gladiator', autor='Hans Zimmer',
             tonalidad='La mayor', compas='3/4', trabaja='Tres sostenidos, y dos compases de espera'),
        dict(num=23, titulo='Rasputin', autor='Boney M · easy piano',
             tonalidad='Si menor', compas='4/4', trabaja='Dos sostenidos que valen para toda la pieza'),
        dict(num=24, titulo='Jailhouse Rock', autor='Elvis Presley · arr. Sadie King',
             tonalidad='Do · blues', compas='4/4', trabaja='El color de blues, y un silencio inicial largo'),
        dict(num=25, titulo='Toreador · Carmen', autor='Bizet · Nivel cuatro',
             tonalidad='Fa mayor', compas='4/4', trabaja='La figura de marcha, con paso firme y constante'),
        dict(num=26, titulo='Für Elise', autor='Beethoven · edición real',
             tonalidad='La menor', compas='3/4', trabaja='El arranque de la pieza más exigente de tu carpeta'),
        dict(num=27, titulo='Nocturne op. 9', autor='Chopin · arr. Benny Chaw',
             tonalidad='Do mayor', compas='3/4', trabaja='Pocas notas: aquí lo que se trabaja es el sonido'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# 27 piezas para 44 semanas: la mayoría de piezas ya conocidas de otros
# álbumes (o parecidas) llevan una sola semana; las que traen algo realmente
# nuevo llevan dos; Für Elise, la más exigente de toda la carpeta, lleva
# tres, y hay dos semanas de repaso repartidas por el curso.
PLAN = [
    ('Septiembre', [
        (1, '1 · Sonatina per bambini — las dos manos al unísono', 'obra'),
        (2, '2 · Oh, When the Saints — el silencio que se repite', 'obra'),
        (3, "3 · You've Got a Friend in Me — sostener la redonda", 'obra'),
        (4, '4 · Puff the Magic Dragon — dos notas a la vez', 'obra'),
    ]),
    ('Octubre', [
        (5, '5 · Sonatina nº 2 — el primer sostenido', 'obra'),
        (6, "6 · Sur le Pont d'Avignon — corcheas y staccato", 'obra'),
        (7, '7 · Do Re Mi — el bajo que camina', 'obra'),
        (8, '8 · Christmas Songs — la izquierda cambia a mitad de compás', 'obra'),
    ]),
    ('Noviembre', [
        (9, '8 · Christmas Songs — los dos villancicos, con la profesora', 'obra'),
        (10, '9 · Silent Night — dos ritmos a la vez', 'obra'),
        (11, '10 · We Wish You a Merry Christmas — la anacrusa', 'obra'),
        (12, '11 · Silent Night a cuatro manos — sostener y escuchar', 'obra'),
    ]),
    ('Diciembre', [
        (13, '12 · La Panthère rose — tres compases de espera', 'obra'),
        (14, '13 · Piano Man — contar los compases callados', 'obra'),
        (15, '13 · Piano Man — entera, sin correr', 'obra'),
        (16, '14 · Bela Ciao — el primer tono menor', 'obra'),
    ]),
    ('Enero', [
        (17, '14 · Bela Ciao — entrar media parte tarde', 'obra'),
        (18, 'REPASO · elige tres piezas y tócalas seguidas', 'repaso'),
        (19, '15 · Spring — el intervalo repetido, muy despacio', 'obra'),
        (20, '15 · Spring — las dos manos juntas', 'obra'),
    ]),
    ('Febrero', [
        (21, '16 · Greensleeves — la izquierda que camina', 'obra'),
        (22, '16 · Greensleeves — entrar antes del compás', 'obra'),
        (23, '17 · Counting Stars — la digitación impresa', 'obra'),
        (24, '17 · Counting Stars — las redondas ligadas', 'obra'),
    ]),
    ('Marzo', [
        (25, '18 · Largo del Nuevo Mundo — notas que cruzan el compás', 'obra'),
        (26, "19 · My Grandfather's Clock — precisión en las dos manos", 'obra'),
        (27, "19 · My Grandfather's Clock — entera, con la letra", 'obra'),
        (28, '20 · I Have a Dream — el primer puntillo', 'obra'),
    ]),
    ('Abril', [
        (29, 'REPASO · elige tres piezas y tócalas seguidas', 'repaso'),
        (30, '21 · Beauty and the Beast — el acorde de tres notas', 'obra'),
        (31, '21 · Beauty and the Beast — entera, con el silencio inicial', 'obra'),
        (32, '22 · Honor Him — los tres sostenidos, sueltos', 'obra'),
    ]),
    ('Mayo', [
        (33, '22 · Honor Him — los dos compases de espera', 'obra'),
        (34, '23 · Rasputin — los dos sostenidos de la armadura', 'obra'),
        (35, '23 · Rasputin — entera, con el pulso firme', 'obra'),
        (36, '24 · Jailhouse Rock — el color de blues', 'obra'),
    ]),
    ('Junio', [
        (37, '24 · Jailhouse Rock — el silencio inicial, contado', 'obra'),
        (38, '25 · Toreador — la figura de marcha', 'obra'),
        (39, '26 · Für Elise — el dibujo del arranque, muy despacio', 'obra'),
        (40, '26 · Für Elise — el mismo dibujo, con la izquierda', 'obra'),
    ]),
    ('Julio', [
        (41, '26 · Für Elise — con ayuda de la profesora en clase', 'obra'),
        (42, '27 · Nocturne — las notas largas, escuchando el final', 'obra'),
        (43, '27 · Nocturne — entero, para la audición', 'obra'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]

NOTA_PLAN = ('Las 44 semanas del curso, repartidas. La mayoría de piezas llevan una semana y las '
             'que traen algo realmente nuevo, dos; Für Elise, la más exigente de la carpeta, lleva '
             'tres y sigue siendo un objetivo abierto más allá del curso. De cada semana te llevas '
             'la hoja de calentamiento, la de agudeza visual, la de cómo se estudia y la de '
             'relajación, con el recuadro donde se apuntan los deberes. Es una propuesta, no una '
             'obligación: si una pieza pide más tiempo, se le da.')

DOSIERES = [
    'Merce_01_SonatinaBambini_CUADERNO.pdf',
    'Merce_02_OhWhenTheSaints_CUADERNO.pdf',
    'Merce_03_FriendInMe_CUADERNO.pdf',
    'Merce_04_PuffTheMagicDragon_CUADERNO.pdf',
    'Merce_05_SonatinaSolMayor_CUADERNO.pdf',
    'Merce_06_SurLePontDAvignon_CUADERNO.pdf',
    'Merce_07_DoReMi_CUADERNO.pdf',
    'Merce_08_ChristmasSongs_CUADERNO.pdf',
    'Merce_09_SilentNight_CUADERNO.pdf',
    'Merce_10_WeWishYou_CUADERNO.pdf',
    'Merce_11_SilentNight4Hands_CUADERNO.pdf',
    'Merce_12_PanthereRose_CUADERNO.pdf',
    'Merce_13_PianoMan_CUADERNO.pdf',
    'Merce_14_BelaCiao_CUADERNO.pdf',
    'Merce_15_Spring_CUADERNO.pdf',
    'Merce_16_Greensleeves_CUADERNO.pdf',
    'Merce_17_CountingStars_CUADERNO.pdf',
    'Merce_18_LargoDvorak_CUADERNO.pdf',
    'Merce_19_GrandfathersClock_CUADERNO.pdf',
    'Merce_20_IHaveADream_CUADERNO.pdf',
    'Merce_21_BeautyAndTheBeast_CUADERNO.pdf',
    'Merce_22_HonorHim_CUADERNO.pdf',
    'Merce_23_Rasputin_CUADERNO.pdf',
    'Merce_24_JailhouseRock_CUADERNO.pdf',
    'Merce_25_Toreador_CUADERNO.pdf',
    'Merce_26_FurElise_CUADERNO.pdf',
    'Merce_27_Nocturne_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Merce_Portada_Indice.pdf')
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
    out = os.path.join(OUT_DIR, 'Merce_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
