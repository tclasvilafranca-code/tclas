# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Aída.

   Formato ADULTO en su versión exigente (la de Josep): seis hojas por pieza,
   con `reto`, `escalera`, `cifrado` y `cuatro_manos` en la hoja semanal.

   EL ENCARGO, literal: "una mujer de cuarenta años aprox y había hecho piano
   así que tiene cierto nivel digamos algo como Josep, pero quiero que vaya
   asentando bases antes de correr". Las dos mitades de esa frase tiran en
   direcciones opuestas y hay que resolverlas sin rebajar ninguna:

     - **el nivel es el de Josep** (escalón 4, hasta la semicorchea). Bajarle
       el listón a una adulta que ya tocaba sería tratarla de principiante, y
       además sus propias partituras no lo permiten: A comme amour va en
       semicorcheas de principio a fin.
     - **asentar bases** no se hace con piezas más fáciles: se hace con el
       ORDEN. Por eso el álbum empieza por los dos Diabelli a cuatro manos
       —cuya portada dice, impreso, "Primo part for 5 fingers with stationary
       hand position"— y termina por el Canon de Pachelbel, el Preludio nº 1 de
       Bach y A comme amour, que son las tres que piden la mano abierta y la
       velocidad. Entre medias, cada etapa añade UNA cosa.

   Diecinueve piezas, todas de su carpeta de Drive, medidas sobre el PDF antes
   de escribir una sola hoja. Diez de las diecinueve son el mismo archivo que
   las de otro alumno (comprobado por md5): es la alumna que más comparte del
   proyecto, y por eso `cruzar_aida.py` no es opcional.

   UNA COSA QUE NO ES LO QUE PARECE, y está explicada en la hoja: el archivo
   que en su Drive se llama "Ave Maria de Bach" trae impreso "Book 1, Prelude
   1" y **no lleva la melodía de Gounod**. Es el Preludio nº 1 en Do mayor,
   BWV 846. El cuaderno lo llama por su nombre y cuenta de dónde sale el Ave
   María, que es teoría de verdad y además responde a la pregunta que ella va a
   hacerse al abrir la hoja.

   Antes de ejecutarlo tiene que salir TODO OK en `auditar_aida.py` y, en
   `cruzar_aida.py`, cero andamio inventado repetido.
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

ALUMNO = 'Aída'
SUBTITULO = 'Volver al piano, y esta vez por los cimientos'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('La mano quieta', 'cinco dedos, un solo sitio, y todo el trabajo en el oído', [
        dict(num=1, titulo='Romance', autor='Anton Diabelli · Primo, a cuatro manos',
             tonalidad='Do mayor', compas='¢', trabaja='Posición fija de cinco dedos, escrita en la partitura'),
        dict(num=2, titulo='Scherzo', autor='Anton Diabelli · op. 149 nº 6 · a cuatro manos',
             tonalidad='Do mayor', compas='3/4', trabaja='La misma posición, y un tempo que ya empuja'),
        dict(num=3, titulo='We Wish You a Merry Christmas', autor='villancico · arr. G. DeBenedetti',
             tonalidad='Sol mayor', compas='3/4', trabaja='La primera armadura, y el cifrado impreso'),
    ]),
    ('Cada mano con su papel', 'la izquierda deja de acompañar a ciegas', [
        dict(num=4, titulo="Can't Help Falling in Love", autor='Elvis Presley · piano, acordes y letra',
             tonalidad='Re mayor', compas='3/4', trabaja='Dos sostenidos, y el vals que no se acelera'),
        dict(num=5, titulo='What Was I Made For?', autor='Billie Eilish · easy piano',
             tonalidad='Do mayor', compas='4/4', trabaja='Tempo impreso (78) y una melodía que casi no se mueve'),
        dict(num=6, titulo='Counting Stars', autor='OneRepublic · arr. Becky Messer',
             tonalidad='Do mayor', compas='4/4', trabaja='La izquierda repitiendo sin parar bajo la melodía'),
    ]),
    ('Los acordes escritos con letras', 'leer el cifrado y no depender de la nota escrita', [
        dict(num=7, titulo='Perfect', autor='Ed Sheeran · Campamento Bye Bye Beethoven',
             tonalidad='Sol mayor', compas='12/8', trabaja='Un compás que se cuenta de cuatro en tres'),
        dict(num=8, titulo='Boig per tu', autor='Sau · Carles Sabater i Pep Sala',
             tonalidad='Do mayor', compas='4/4', trabaja='Entrar a contratiempo, después del silencio'),
        dict(num=9, titulo='Kiss the Rain', autor='Yiruma',
             tonalidad='Do mayor', compas='4/4', trabaja='Tres tiempos callada antes de la primera nota'),
    ]),
    ('El compás que se cuenta de otra manera', 'no todo se cuenta de cuatro', [
        dict(num=10, titulo="It's Beginning to Look a Lot Like Christmas", autor='Meredith Willson · a cuatro manos',
             tonalidad='Do mayor', compas='6/8', trabaja='Seis corcheas que son dos golpes, y con otra persona'),
        dict(num=11, titulo='Titanic', autor='James Horner · arr. A. C. Escobés',
             tonalidad='Do mayor', compas='2/4', trabaja='Dos tiempos por compás, y el puntillo dentro'),
        dict(num=12, titulo='Hijo de la Luna', autor='Mecano · arr. Unai Karam',
             tonalidad='Re menor', compas='6/8', trabaja='El 6/8 en modo menor, y un tempo muy lento escrito'),
    ]),
    ('El modo menor', 'la misma técnica, otro color', [
        dict(num=13, titulo='Carol of the Bells', autor='Mykola Leontovych · arr. J. Paterson',
             tonalidad='Sol menor', compas='3/4', trabaja='Dos bemoles, y una célula de tres notas que no para'),
        dict(num=14, titulo='The Sound of Silence', autor='Simon & Garfunkel',
             tonalidad='Re menor', compas='4/4', trabaja='Un bemol, y la melodía que baja y vuelve'),
        dict(num=15, titulo='Gladiator', autor='Hans Zimmer · arr. A. C. Escobés',
             tonalidad='Mi menor', compas='4/4', trabaja='Tresillos, calderón y casillas de 1ª y 2ª vez'),
    ]),
    ('La mano abierta y la semicorchea', 'las cuatro que piden todo lo anterior junto', [
        dict(num=16, titulo='Un beso y una flor', autor='Nino Bravo · piano, acordes y letra',
             tonalidad='Fa mayor', compas='4/4', trabaja='El cifrado impreso, ya con la mano abierta'),
        dict(num=17, titulo='Canon de Pachelbel', autor='Johann Pachelbel · Canon in D',
             tonalidad='Re mayor', compas='4/4', trabaja='El bajo de ocho notas que sostiene la pieza entera'),
        dict(num=18, titulo='Preludio nº 1', autor='J. S. Bach · BWV 846 · el del Ave María',
             tonalidad='Do mayor', compas='4/4', trabaja='Un solo dibujo de mano, repetido treinta y cinco veces'),
        dict(num=19, titulo='A comme amour', autor='Richard Clayderman · Paul de Senneville',
             tonalidad='Mi menor', compas='4/4', trabaja='Semicorcheas de principio a fin: el reto del curso'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# Dos semanas por pieza, las diecinueve (38), y seis sueltas: dos en diciembre
# para tocar los dos de Navidad seguidos y repasar el otoño, y las cuatro de
# julio para el repaso y la audición. Las dos piezas de Navidad —el We Wish You
# y el It's Beginning to Look a Lot Like Christmas— se adelantan a noviembre y
# diciembre aunque en el álbum vayan en otro sitio: en enero ya no sirven.
#
# Y una decisión de fondo: las tres últimas (Pachelbel, el Preludio de Bach y A
# comme amour) van seguidas en mayo y junio a propósito. Las tres trabajan lo
# mismo —la mano abierta en arpegio— y en ese orden cada una prepara la
# siguiente. Separarlas por el calendario sería tirar el trabajo de la anterior.
PLAN = [
    ('Septiembre', [
        (1, '1 · Romance de Diabelli — colocar la mano y no moverla', 'obra'),
        (2, '1 · Romance de Diabelli — con la profesora, a cuatro manos', 'obra'),
        (3, '2 · Scherzo de Diabelli — la misma posición, más deprisa', 'obra'),
        (4, '2 · Scherzo de Diabelli — el Primo entero, sin parar', 'obra'),
    ]),
    ('Octubre', [
        (5, "4 · Can't Help Falling in Love — los dos sostenidos", 'obra'),
        (6, "4 · Can't Help Falling in Love — el vals, sin acelerar", 'obra'),
        (7, '5 · What Was I Made For — la melodía, a ♩ = 78', 'obra'),
        (8, '5 · What Was I Made For — las dos manos, con el cifrado', 'obra'),
    ]),
    ('Noviembre', [
        (9, '6 · Counting Stars — la izquierda sola, de memoria', 'obra'),
        (10, '6 · Counting Stars — las dos manos', 'obra'),
        (11, 'NAVIDAD · 3 We Wish You a Merry Christmas — la anacrusa', 'especial'),
        (12, 'NAVIDAD · 3 We Wish You — entera, con el cifrado', 'especial'),
    ]),
    ('Diciembre', [
        (13, "NAVIDAD · 10 It's Beginning — contar el 6/8 en dos golpes", 'especial'),
        (14, "NAVIDAD · 10 It's Beginning — con la profesora, a cuatro manos", 'especial'),
        (15, 'NAVIDAD · los dos villancicos seguidos, para tocarlos en casa', 'especial'),
        (16, 'REPASO · las cuatro primeras, una detrás de otra', 'repaso'),
    ]),
    ('Enero', [
        (17, '7 · Perfect — contar doce corcheas como cuatro golpes', 'obra'),
        (18, '7 · Perfect — la primera página, a ♩. = 94', 'obra'),
        (19, '8 · Boig per tu — entrar después del silencio', 'obra'),
        (20, '8 · Boig per tu — las dos manos, sin perder la entrada', 'obra'),
    ]),
    ('Febrero', [
        (21, '9 · Kiss the Rain — contar tres tiempos callada', 'obra'),
        (22, '9 · Kiss the Rain — la primera línea, con pedal', 'obra'),
        (23, '11 · Titanic — el 2/4, y el puntillo del primer compás', 'obra'),
        (24, '11 · Titanic — la melodía entera', 'obra'),
    ]),
    ('Marzo', [
        (25, '12 · Hijo de la Luna — el 6/8 lento, contado en dos', 'obra'),
        (26, '12 · Hijo de la Luna — la primera página', 'obra'),
        (27, '13 · Carol of the Bells — la célula de tres notas', 'obra'),
        (28, '13 · Carol of the Bells — subir de velocidad sin perderla', 'obra'),
    ]),
    ('Abril', [
        (29, '14 · The Sound of Silence — la melodía, con su bemol', 'obra'),
        (30, '14 · The Sound of Silence — las dos manos', 'obra'),
        (31, '15 · Gladiator — los tresillos, contados aparte', 'obra'),
        (32, '15 · Gladiator — con las casillas de 1ª y 2ª vez', 'obra'),
    ]),
    ('Mayo', [
        (33, '16 · Un beso y una flor — leer el cifrado y tocarlo', 'obra'),
        (34, '16 · Un beso y una flor — la primera página entera', 'obra'),
        (35, '17 · Canon de Pachelbel — el bajo de ocho notas, de memoria', 'obra'),
        (36, '17 · Canon de Pachelbel — la melodía encima del bajo', 'obra'),
    ]),
    ('Junio', [
        (37, '18 · Preludio nº 1 de Bach — un compás, y la mano quieta', 'obra'),
        (38, '18 · Preludio nº 1 de Bach — los ocho primeros, seguidos', 'obra'),
        (39, '19 · A comme amour — las semicorcheas, muy despacio', 'obra'),
        (40, '19 · A comme amour — subir a ♩ = 69', 'obra'),
    ]),
    ('Julio', [
        (41, 'REPASO · Pachelbel y el Preludio, uno detrás de otro', 'repaso'),
        (42, 'REPASO · elige tres del resto y tócalas seguidas', 'repaso'),
        (43, 'ENSAYO · las tres elegidas, sin parar y sin repetir', 'concierto'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]
NOTA_PLAN = ('Las 44 semanas del curso, repartidas. Cada pieza tiene dos semanas y de cada una te '
             'llevas la hoja de trabajo con el plan de minutos. Las dos de Navidad se adelantan a '
             'noviembre y diciembre aunque en el cuaderno estén en otro sitio, y las tres de '
             'arpegio (Pachelbel, el Preludio de Bach y A comme amour) van seguidas al final '
             'porque cada una prepara la siguiente. Es una propuesta, no una obligación.')

DOSIERES = [
    'Aida_01_RomanceDiabelli_CUADERNO.pdf',
    'Aida_02_ScherzoDiabelli_CUADERNO.pdf',
    'Aida_03_WeWishYouAMerryChristmas_CUADERNO.pdf',
    'Aida_04_CantHelpFallingInLove_CUADERNO.pdf',
    'Aida_05_WhatWasIMadeFor_CUADERNO.pdf',
    'Aida_06_CountingStars_CUADERNO.pdf',
    'Aida_07_Perfect_CUADERNO.pdf',
    'Aida_08_BoigPerTu_CUADERNO.pdf',
    'Aida_09_KissTheRain_CUADERNO.pdf',
    'Aida_10_ItsBeginningToLook_CUADERNO.pdf',
    'Aida_11_Titanic_CUADERNO.pdf',
    'Aida_12_HijoDeLaLuna_CUADERNO.pdf',
    'Aida_13_CarolOfTheBells_CUADERNO.pdf',
    'Aida_14_TheSoundOfSilence_CUADERNO.pdf',
    'Aida_15_Gladiator_CUADERNO.pdf',
    'Aida_16_UnBesoYUnaFlor_CUADERNO.pdf',
    'Aida_17_CanonPachelbel_CUADERNO.pdf',
    'Aida_18_PreludioBach_CUADERNO.pdf',
    'Aida_19_ACommeAmour_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Aida_Portada_Indice.pdf')
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
    out = os.path.join(OUT_DIR, 'Aida_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
