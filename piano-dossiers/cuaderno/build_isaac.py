# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Isaac.

   Formato ADULTO estándar (seis hojas por pieza), el mismo esquema que José
   María, Josep, Luisa, Mercè y Nel. Isaac es de nivel medio y el cliente
   pidió "dale caña": su curva de lectura (`cancion.CURVA['isaac']`) sube más
   rápido que la de José María o Mercè (cada 5 piezas en vez de cada 7-8),
   aunque su techo se queda en nivel 2, no en 3 como los alumnos avanzados.

   19 de las 20 partituras son el mismo archivo, byte a byte, que las de
   otros alumnos — sobre todo Mercè — ver TRANSCRIPCION_ISAAC_FUENTES.md. La
   única propia es el estudio de Diabelli, Op. 149 nº 3, medido de cero. El
   andamio inventado no coincide con el de nadie: lo comprueba
   `cruzar_isaac.py`.

   Antes de ejecutarlo tiene que salir TODO OK en auditar_isaac.py y 0
   solapes en cruzar_isaac.py.
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

ALUMNO = 'Isaac'
SUBTITULO = 'Veinte piezas, nivel medio con caña'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('Empezar con confianza', 'duetos y melodías sencillas, para entrar sin agobios', [
        dict(num=1, titulo='Petite Chanson', autor='Riccardo Collu · a cuatro manos',
             tonalidad='Do mayor', compas='4/4', trabaja='La anacrusa de dos corcheas, entre dos'),
        dict(num=2, titulo='Oh, When the Saints', autor='Primer nivel · arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='4/4', trabaja='El silencio de la izquierda que se repite'),
        dict(num=3, titulo='Puff the Magic Dragon', autor='arr. Eric Moore',
             tonalidad='Do mayor', compas='4/4', trabaja='Dos notas a la vez, sostenidas juntas'),
        dict(num=4, titulo='The Beginner', autor='C. Gurlitt · a cuatro manos',
             tonalidad='Do mayor', compas='3/4', trabaja='El primer compás de tres, con reguladores'),
    ]),
    ('Espera y precisión', 'contar compases callados y seguir la digitación exacta', [
        dict(num=5, titulo='La Panthère rose', autor='H. Mancini · Première année',
             tonalidad='Sol mayor', compas='3/4', trabaja='Tres compases callados, y entrar a tiempo'),
        dict(num=6, titulo='Piano Man', autor='Billy Joel · SimplyPiano',
             tonalidad='Do mayor', compas='4/4', trabaja='Contar los compases donde la izquierda no toca'),
    ]),
    ('Villancicos, dos veces cada uno', 'diciembre, con dos versiones de Silent Night', [
        dict(num=7, titulo='We Wish You a Merry Christmas', autor='arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='3/4', trabaja='La anacrusa, y las primeras letras de acorde'),
        dict(num=8, titulo='Christmas Songs', autor='M. Liang · a cuatro manos',
             tonalidad='Do mayor', compas='3/4', trabaja='La izquierda cambia de nota a mitad de compás'),
        dict(num=9, titulo='Silent Night', autor='F. X. Gruber · con letra y dedos',
             tonalidad='Do mayor', compas='4/4', trabaja='Dos ritmos a la vez, uno en cada mano'),
        dict(num=10, titulo='Silent Night · a cuatro manos', autor='Piano 1 + Piano 2',
             tonalidad='Do mayor', compas='3/4', trabaja='Sostener mientras se escucha a la otra parte'),
    ]),
    ('Teclas negras y digitación en las dos manos', 'entradas retrasadas y precisión de verdad', [
        dict(num=11, titulo='Greensleeves', autor='tradicional inglesa · con cifrado',
             tonalidad='La menor', compas='3/4', trabaja='Entrar antes del compás, con la izquierda caminando'),
        dict(num=12, titulo="My Grandfather's Clock", autor='H. C. Work · Nivel tres',
             tonalidad='Sol mayor', compas='4/4', trabaja='Digitación exacta en las dos manos'),
    ]),
    ('Ritmos que respiran', 'carrerillas, puntillos y el primer tono mayor de tres sostenidos', [
        dict(num=13, titulo='Do Re Mi', autor='R. Rodgers · Sonrisas y Lágrimas',
             tonalidad='Do mayor', compas='4/4', trabaja='El bajo que camina y una carrerilla de corcheas'),
        dict(num=14, titulo='I Have a Dream', autor='ABBA',
             tonalidad='Do mayor', compas='4/4', trabaja='El primer puntillo del álbum, contado en corcheas'),
    ]),
    ('Los seis retos del final', 'sostenidos, blues, marcha firme y las dos piezas más exigentes', [
        dict(num=15, titulo='Honor Him · Gladiator', autor='Hans Zimmer',
             tonalidad='La mayor', compas='3/4', trabaja='Tres sostenidos, y dos compases de espera'),
        dict(num=16, titulo='Rasputin', autor='Boney M · easy piano',
             tonalidad='Si menor', compas='4/4', trabaja='Dos sostenidos que valen para toda la pieza'),
        dict(num=17, titulo='Jailhouse Rock', autor='Elvis Presley · arr. Sadie King',
             tonalidad='Do · blues', compas='4/4', trabaja='El color de blues, y un silencio inicial largo'),
        dict(num=18, titulo='Toreador · Carmen', autor='Bizet · Nivel cuatro',
             tonalidad='Fa mayor', compas='4/4', trabaja='La figura de marcha, con paso firme y constante'),
        dict(num=19, titulo='Für Elise', autor='Beethoven · edición real',
             tonalidad='La menor', compas='3/4', trabaja='El arranque de una pieza exigente de verdad'),
        dict(num=20, titulo='Diabelli · Op. 149 nº 3', autor='28 melodische Übungsstücke · a cuatro manos',
             tonalidad='Do mayor', compas='2/4', trabaja='Staccato de verdad: la nota y el silencio, iguales'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# Dale caña: la mayoría de piezas llevan dos semanas, y las dos más
# exigentes del final (Für Elise y el Diabelli) llevan tres. Los villancicos
# se agrupan en diciembre aunque no sigan el orden numérico de las piezas,
# y hay una sola semana de repaso: con solo una semana de sobra en todo el
# curso, no da para más sin recortar las piezas del final.
PLAN = [
    ('Septiembre', [
        (1, '1 · Petite Chanson — la anacrusa, entre dos', 'obra'),
        (2, '1 · Petite Chanson — a ♩ = 80, con la profesora', 'obra'),
        (3, '2 · Oh When the Saints — el silencio que se repite', 'obra'),
        (4, '2 · Oh When the Saints — entera, con la letra', 'obra'),
    ]),
    ('Octubre', [
        (5, '3 · Puff the Magic Dragon — dos notas a la vez', 'obra'),
        (6, '3 · Puff the Magic Dragon — entera, muy suave', 'obra'),
        (7, '4 · The Beginner — el compás de tres, contado', 'obra'),
        (8, '4 · The Beginner — con los reguladores', 'obra'),
    ]),
    ('Noviembre', [
        (9, '5 · La Panthère rose — tres compases de espera', 'obra'),
        (10, '5 · La Panthère rose — entrar justo a tiempo', 'obra'),
        (11, '6 · Piano Man — contar los compases callados', 'obra'),
        (12, '6 · Piano Man — entera, sin correr', 'obra'),
    ]),
    ('Diciembre', [
        (13, 'NAVIDAD · 7 We Wish You — la anacrusa de un tiempo', 'especial'),
        (14, 'NAVIDAD · 7 We Wish You — las letras de acorde', 'especial'),
        (15, 'NAVIDAD · 8 Christmas Songs — la izquierda a mitad de compás', 'especial'),
        (16, 'NAVIDAD · 8 Christmas Songs — los dos villancicos', 'especial'),
    ]),
    ('Enero', [
        (17, '9 · Silent Night — dos ritmos a la vez', 'obra'),
        (18, '9 · Silent Night — entera, con la letra', 'obra'),
        (19, '10 · Silent Night a cuatro manos — sostener y escuchar', 'obra'),
        (20, '10 · Silent Night a cuatro manos — con la profesora', 'obra'),
    ]),
    ('Febrero', [
        (21, '11 · Greensleeves — la izquierda que camina', 'obra'),
        (22, '11 · Greensleeves — entrar antes del compás', 'obra'),
        (23, "12 · Grandfather's Clock — precisión en las dos manos", 'obra'),
        (24, "12 · Grandfather's Clock — entera, con la letra", 'obra'),
    ]),
    ('Marzo', [
        (25, '13 · Do Re Mi — el bajo que camina', 'obra'),
        (26, '13 · Do Re Mi — la carrerilla de corcheas', 'obra'),
        (27, '14 · I Have a Dream — el primer puntillo', 'obra'),
        (28, '14 · I Have a Dream — entera, a ♩ = 120', 'obra'),
    ]),
    ('Abril', [
        (29, 'REPASO · elige tres piezas y tócalas seguidas', 'repaso'),
        (30, '15 · Honor Him — los tres sostenidos, sueltos', 'obra'),
        (31, '15 · Honor Him — los dos compases de espera', 'obra'),
        (32, '16 · Rasputin — los dos sostenidos de la armadura', 'obra'),
    ]),
    ('Mayo', [
        (33, '16 · Rasputin — entera, con el pulso firme', 'obra'),
        (34, '17 · Jailhouse Rock — el color de blues', 'obra'),
        (35, '17 · Jailhouse Rock — el silencio inicial, contado', 'obra'),
        (36, '18 · Toreador — la figura de marcha', 'obra'),
    ]),
    ('Junio', [
        (37, '18 · Toreador — el paso firme, con las dos manos', 'obra'),
        (38, '19 · Für Elise — el dibujo del arranque, muy despacio', 'obra'),
        (39, '19 · Für Elise — el mismo dibujo, con la izquierda', 'obra'),
        (40, '19 · Für Elise — con ayuda de la profesora en clase', 'obra'),
    ]),
    ('Julio', [
        (41, '20 · Diabelli — el staccato con silencio real', 'obra'),
        (42, '20 · Diabelli — las dos manos en clave de sol', 'obra'),
        (43, '20 · Diabelli — entero, para la audición', 'obra'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]

NOTA_PLAN = ('Las 44 semanas del curso, repartidas. La mayoría de piezas llevan dos semanas, y las '
             'dos más exigentes del final —Für Elise y el estudio de Diabelli— llevan tres. De cada '
             'semana te llevas la hoja de calentamiento, la de agudeza visual, la de cómo se estudia '
             'y la de relajación, con el recuadro de deberes al pie. Es una propuesta, no una '
             'obligación: si una pieza pide más tiempo, se le da.')

DOSIERES = [
    'Isaac_01_PetiteChanson_CUADERNO.pdf',
    'Isaac_02_OhWhenTheSaints_CUADERNO.pdf',
    'Isaac_03_PuffTheMagicDragon_CUADERNO.pdf',
    'Isaac_04_TheBeginner_CUADERNO.pdf',
    'Isaac_05_WeWishYou_CUADERNO.pdf',
    'Isaac_06_ChristmasSongs_CUADERNO.pdf',
    'Isaac_07_SilentNight_CUADERNO.pdf',
    'Isaac_08_SilentNight4Hands_CUADERNO.pdf',
    'Isaac_09_PanthereRose_CUADERNO.pdf',
    'Isaac_10_PianoMan_CUADERNO.pdf',
    'Isaac_11_Greensleeves_CUADERNO.pdf',
    'Isaac_12_GrandfathersClock_CUADERNO.pdf',
    'Isaac_13_DoReMi_CUADERNO.pdf',
    'Isaac_14_IHaveADream_CUADERNO.pdf',
    'Isaac_15_HonorHim_CUADERNO.pdf',
    'Isaac_16_Rasputin_CUADERNO.pdf',
    'Isaac_17_JailhouseRock_CUADERNO.pdf',
    'Isaac_18_Toreador_CUADERNO.pdf',
    'Isaac_19_FurElise_CUADERNO.pdf',
    'Isaac_20_Diabelli_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Isaac_Portada_Indice.pdf')
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
    out = os.path.join(OUT_DIR, 'Isaac_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
