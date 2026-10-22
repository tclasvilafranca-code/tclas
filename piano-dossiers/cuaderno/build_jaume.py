# -*- coding: utf-8 -*-
"""Portada, índice, plan de curso y álbum completo del cuaderno de Jaume.

   Formato ADULTO (seis hojas por pieza), en su versión EXIGENTE: el mismo que el
   de Josep. Jaume tiene unos 60 años, nivel medio y base musical, y lleva 23
   piezas: sus 23 partituras de Drive, todas.

   Los duetos (Romance de Diabelli, Bella Ciao y It's Beginning to Look a Lot
   Like Christmas) se ven abiertos: `ensamblar.anadir_dosier` intercala una hoja
   de pauta delante cuando la partitura caería empezando en página impar.

   Antes de ejecutarlo tiene que salir TODO OK en auditar_jaume.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import build_cover, build_index, build_plan_curso, W, H
from ensamblar import anadir_dosier

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')
OUT_DIR = os.path.join(HERE, '..', 'output')

ALUMNO = 'Jaume'
SUBTITULO = 'Veintitrés piezas'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('Empezar con calma', 'repertorio conocido, mano quieta y un dueto para tocar con alguien', [
        dict(num=1, titulo='Himno de la alegría', autor='Beethoven · arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='4/4', trabaja='Redondas completas en la izquierda'),
        dict(num=2, titulo='Romance', autor='Anton Diabelli · Primo, a cuatro manos',
             tonalidad='Do mayor', compas='2/2', trabaja='Sonar como una sola mano con la otra persona'),
        dict(num=3, titulo='My Bonnie', autor='canción popular · arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='3/4', trabaja='Dos compases de silencio contados, y entrar a tiempo'),
        dict(num=4, titulo='Heart and Soul', autor='Hoagy Carmichael · versión fácil',
             tonalidad='Do mayor', compas='4/4', trabaja='El bajo con acorde, que ande solo'),
    ]),
    ('El cifrado, el modo menor y el swing', 'la izquierda deja de aguantar y empieza a acompañar', [
        dict(num=5, titulo='Greensleeves', autor='canción popular inglesa',
             tonalidad='La menor', compas='3/4', trabaja='Leer el cifrado y el arpegio a la vez'),
        dict(num=6, titulo='Bella Ciao', autor='popular italiana · a cuatro manos',
             tonalidad='Sol menor', compas='4/4', trabaja='Dejar de oír el acompañamiento como un metrónomo'),
        dict(num=7, titulo='Jailhouse Rock', autor='Elvis Presley · arr. Sadie King',
             tonalidad='Do · con blues', compas='4/4', trabaja='El compás de entrada a ♩ = 150'),
        dict(num=8, titulo='Hijo de la Luna', autor='Mecano · arr. Unai Karam',
             tonalidad='Re menor', compas='6/8', trabaja='Semicorcheas que no se atropellan en 6/8'),
    ]),
    ('Compases distintos y frases largas', 'cuando el compás deja de ser lo cómodo', [
        dict(num=9, titulo='Titanic', autor='James Horner · arr. Ana Cristina Escobés',
             tonalidad='Do mayor', compas='2/4', trabaja='Una línea que no se corta'),
        dict(num=10, titulo='El submarino amarillo', autor='Lennon y McCartney · arr. Ana Cristina Escobés',
             tonalidad='Sol mayor', compas='4/4', trabaja='Notas repetidas que no se aceleran'),
        dict(num=11, titulo='Largo', autor='Antonín Dvořák · arr. Ana Cristina Escobés',
             tonalidad='Do mayor', compas='4/4', trabaja='Cuatro frases iguales que no suenan iguales'),
        dict(num=12, titulo="It's Beginning to Look a Lot Like Christmas",
             autor='Meredith Willson · dúo de piano',
             tonalidad='Do mayor', compas='6/8', trabaja='El 6/8 se cuenta en dos, y el silencio abre el compás'),
    ]),
    ('Cifrado, 12/8 y silencios largos', 'canciones que se estudian por acordes y se tocan con el silencio', [
        dict(num=13, titulo='Perfect', autor='Ed Sheeran · arr. Bye Bye Beethoven',
             tonalidad='Sol mayor', compas='12/8', trabaja='Contar el 12/8 en cuatro y no en doce'),
        dict(num=14, titulo='What Was I Made For?', autor='Billie Eilish · versión de Musescore',
             tonalidad='Do mayor', compas='4/4', trabaja='Tres compases de silencio y la entrada a tiempo'),
        dict(num=15, titulo='Mamma Mia', autor='ABBA · arr. Unai Karam',
             tonalidad='Do mayor', compas='4/4', trabaja='Un ostinato de corcheas con un sostenido que se mueve'),
        dict(num=16, titulo='Shallow', autor='Lady Gaga y Bradley Cooper · Bye Bye Beethoven',
             tonalidad='Mi menor', compas='4/4', trabaja='Corcheas iguales sobre la misma nota, sin acortarlas'),
    ]),
    ('La escritura exigente', 'doble puntillo, notas de adorno, casillas: lo difícil es el papel', [
        dict(num=17, titulo='Gladiator', autor='Hans Zimmer · arr. A. C. Escobés',
             tonalidad='Mi menor', compas='4/4', trabaja='El doble puntillo y el tresillo'),
        dict(num=18, titulo='The Entertainer', autor='Scott Joplin · arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='2/2', trabaja='El 8va, el La♭ y el staccato'),
        dict(num=19, titulo='Toreador', autor='Georges Bizet · de Carmen · arr. Gilbert DeBenedetti',
             tonalidad='Fa mayor', compas='4/4', trabaja='El largo-corto de la marcha y la nota de adorno'),
        dict(num=20, titulo='Un beso y una flor', autor='Nino Bravo · versión de Musescore',
             tonalidad='Fa mayor', compas='4/4', trabaja='Semicorcheas sueltas y octavas en la izquierda'),
    ]),
    ('Los tres grandes del final', 'aquí el cuaderno deja de ser cómodo, y a propósito', [
        dict(num=21, titulo="Sweet Child O' Mine", autor="Guns N' Roses · arr. Sadie King",
             tonalidad='Si bemol mayor', compas='4/4', trabaja='El pedal escrito, que cambia después del acorde'),
        dict(num=22, titulo='La primavera', autor='Antonio Vivaldi · de Las cuatro estaciones',
             tonalidad='Do mayor', compas='4/4', trabaja='Intervalos dobles con la mano quieta'),
        dict(num=23, titulo='Para Elisa', autor='Ludwig van Beethoven',
             tonalidad='La menor', compas='3/4', trabaja='La oscilación del arranque, liviana y sin prisa'),
    ]),
]

# --- el curso repartido en 44 semanas -------------------------------------
#
# 23 piezas en 43 semanas más la audición: tres piezas de una semana (las más
# cortas y conocidas: el Himno, Heart and Soul y La primavera) y veinte de dos.
# It's Beginning to Look a Lot Like Christmas se adelanta a diciembre.
PLAN = [
    ('Septiembre', [
        (1, '1 · Himno de la alegría — redondas completas', 'obra'),
        (2, '2 · Romance — las dos manos exactamente juntas', 'obra'),
        (3, '2 · Romance — el dúo con la otra persona', 'obra'),
        (4, '3 · My Bonnie — los dos compases mudos', 'obra'),
    ]),
    ('Octubre', [
        (5, '3 · My Bonnie — el cruce final', 'obra'),
        (6, '4 · Heart and Soul — el bajo con acorde, y el swing', 'obra'),
        (7, '5 · Greensleeves — las letras del cifrado', 'obra'),
        (8, '5 · Greensleeves — el arpegio y la melodía', 'obra'),
    ]),
    ('Noviembre', [
        (9, '6 · Bella Ciao — el tono menor, con la profesora', 'obra'),
        (10, '6 · Bella Ciao — el dúo, con metrónomo', 'obra'),
        (11, '7 · Jailhouse Rock — la entrada y el Mi♭', 'obra'),
        (12, '7 · Jailhouse Rock — subir por escalones a 150', 'obra'),
    ]),
    ('Diciembre', [
        (13, "NAVIDAD · 12 It's Beginning — contar en dos", 'especial'),
        (14, "NAVIDAD · 12 It's Beginning — el dúo entero", 'especial'),
        (15, '8 · Hijo de la Luna — las semicorcheas del c. 5', 'obra'),
        (16, '8 · Hijo de la Luna — entera, con las tres páginas', 'obra'),
    ]),
    ('Enero', [
        (17, '9 · Titanic — la línea que no se corta', 'obra'),
        (18, '9 · Titanic — la ligadura de frase', 'obra'),
        (19, '10 · El submarino amarillo — las notas repetidas', 'obra'),
        (20, '10 · El submarino amarillo — la pieza entera', 'obra'),
    ]),
    ('Febrero', [
        (21, '11 · Largo — las cuatro frases', 'obra'),
        (22, '11 · Largo — que no suenen iguales', 'obra'),
        (23, '13 · Perfect — contar en cuatro', 'obra'),
        (24, '13 · Perfect — el cifrado y la anacrusa', 'obra'),
    ]),
    ('Marzo', [
        (25, '14 · What Was I Made For? — la entrada del c. 4', 'obra'),
        (26, '14 · What Was I Made For? — la figura con ligadura', 'obra'),
        (27, '15 · Mamma Mia — el ostinato', 'obra'),
        (28, '15 · Mamma Mia — la melodía de los cc. 5-6', 'obra'),
    ]),
    ('Abril', [
        (29, '16 · Shallow — las corcheas del c. 3', 'obra'),
        (30, '16 · Shallow — el estribillo y las semicorcheas', 'obra'),
        (31, '17 · Gladiator — contar el doble puntillo', 'obra'),
        (32, '17 · Gladiator — el tresillo y el calderón', 'obra'),
    ]),
    ('Mayo', [
        (33, '18 · The Entertainer — el 8va y el La♭', 'obra'),
        (34, '18 · The Entertainer — el bajo y el staccato', 'obra'),
        (35, '19 · Toreador — el largo-corto', 'obra'),
        (36, '19 · Toreador — la nota de adorno y las casillas', 'obra'),
    ]),
    ('Junio', [
        (37, '20 · Un beso y una flor — el c. 1 y las octavas', 'obra'),
        (38, '20 · Un beso y una flor — el cifrado y las casillas', 'obra'),
        (39, "21 · Sweet Child O' Mine — el pedal, con la izquierda sola", 'obra'),
        (40, "21 · Sweet Child O' Mine — el riff y el pie", 'obra'),
    ]),
    ('Julio', [
        (41, '22 · La primavera — los intervalos, con la mano quieta', 'obra'),
        (42, '23 · Para Elisa — el arranque liviano', 'obra'),
        (43, '23 · Para Elisa — la semicorchea del c. 20 y la pieza entera', 'obra'),
        (44, 'AUDICIÓN DE FIN DE CURSO', 'concierto'),
    ]),
]

NOTA_PLAN = ('Las 44 semanas del curso, repartidas. Las tres piezas más conocidas y cortas (el Himno, '
             'Heart and Soul y La primavera) tienen una semana; las demás, dos. De cada una te llevas '
             'la hoja de trabajo con el plan de minutos y, según la pieza, el reto de la semana, la '
             'escalera del metrónomo, el cifrado o lo que haya que acordar con la otra persona. Es '
             'una propuesta, no una obligación: si una pieza pide una semana más, se le da, y si '
             'sale antes, se pasa a la siguiente.')

DOSIERES = [
    'Jaume_01_HimnoAlegria_CUADERNO.pdf',
    'Jaume_02_RomanceDiabelli_CUADERNO.pdf',
    'Jaume_03_MyBonnie_CUADERNO.pdf',
    'Jaume_04_HeartAndSoul_CUADERNO.pdf',
    'Jaume_05_Greensleeves_CUADERNO.pdf',
    'Jaume_06_BellaCiao_CUADERNO.pdf',
    'Jaume_07_JailhouseRock_CUADERNO.pdf',
    'Jaume_08_HijoDeLaLuna_CUADERNO.pdf',
    'Jaume_09_Titanic_CUADERNO.pdf',
    'Jaume_10_SubmarinoAmarillo_CUADERNO.pdf',
    'Jaume_11_LargoDvorak_CUADERNO.pdf',
    'Jaume_12_ItsBeginningToLook_CUADERNO.pdf',
    'Jaume_13_Perfect_CUADERNO.pdf',
    'Jaume_14_WhatWasIMadeFor_CUADERNO.pdf',
    'Jaume_15_MammaMia_CUADERNO.pdf',
    'Jaume_16_Shallow_CUADERNO.pdf',
    'Jaume_17_Gladiator_CUADERNO.pdf',
    'Jaume_18_ElGolpe_CUADERNO.pdf',
    'Jaume_19_Toreador_CUADERNO.pdf',
    'Jaume_20_UnBesoYUnaFlor_CUADERNO.pdf',
    'Jaume_21_SweetChild_CUADERNO.pdf',
    'Jaume_22_Primavera_CUADERNO.pdf',
    'Jaume_23_ParaElisa_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Jaume_Portada_Indice.pdf')
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
        if anadir_dosier(wr, ruta):
            print('  %s: hoja de pauta intercalada para que el dúo se vea abierto' % nombre)
    out = os.path.join(OUT_DIR, 'Jaume_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    if faltan:
        print('OJO, faltan dosieres: %s' % ', '.join(faltan))
    print('generado %s · %d paginas' % (out, len(PdfReader(out).pages)))


if __name__ == '__main__':
    main()
