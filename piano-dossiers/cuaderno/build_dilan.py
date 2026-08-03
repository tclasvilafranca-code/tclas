# -*- coding: utf-8 -*-
"""Portada, indice y album completo del cuaderno de Dilan.

   Une la portada + el indice con los veinte dosieres, en orden. Cada dosier
   son seis paginas (la partitura, que puede ocupar varias, mas las cinco
   hojas), asi que el total sale de sumarlos.

   Antes de ejecutarlo tiene que salir TODO OK en auditar_dilan.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from portada import build_cover, build_index, W, H

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')
OUT_DIR = os.path.join(HERE, '..', 'output')

ALUMNO = 'Dilan'
SUBTITULO = 'Nivel avanzado'
CURSO = 'Curso 2026 · 2027'

ETAPAS = [
    ('Empezar por la izquierda', 'la mano que sostiene la pieza entera', [
        dict(num=1, titulo='El Cisne', autor='Saint-Saëns, rev. Ricardo Boppré',
             tonalidad='Sol mayor', compas='3/4', trabaja='Un arpegio que no para en 55 compases'),
        dict(num=2, titulo='Can’t Help Falling in Love', autor='Elvis Presley, arr. Seb Alejandro',
             tonalidad='Re mayor', compas='3/4', trabaja='El acorde roto, leído del cifrado'),
        dict(num=3, titulo='Your Song', autor='Elton John y Bernie Taupin',
             tonalidad='Mi♭ mayor', compas='4/4', trabaja='Una línea de bajo que baja por grados'),
        dict(num=4, titulo='Thinking Out Loud', autor='Ed Sheeran y Amy Wadge',
             tonalidad='Re mayor', compas='4/4', trabaja='Sostener, y entrar a contratiempo'),
    ]),
    ('El molde y el cifrado', 'cuando la izquierda deja de tener notas', [
        dict(num=5, titulo='Lucía', autor='Joan Manuel Serrat',
             tonalidad='La menor', compas='4/4', trabaja='Un bajo que oscila un semitono'),
        dict(num=6, titulo='Poema de Amor', autor='Joan Manuel Serrat',
             tonalidad='Sol menor', compas='4/4', trabaja='El bajo alterno: 1 · 8 · 5 · 8'),
        dict(num=7, titulo='Amiga Mía', autor='Alejandro Sanz',
             tonalidad='Re mayor', compas='4/4', trabaja='Dos voces con una sola mano'),
        dict(num=8, titulo='La Promesa', autor='Melendi',
             tonalidad='Sol mayor', compas='4/4', trabaja='Dos capas, sostenidas con el pedal'),
    ]),
    ('Acordes, quintas y arpegios', 'las cinco posiciones que hay que memorizar', [
        dict(num=9, titulo='When I Was Your Man', autor='Bruno Mars',
             tonalidad='Do mayor', compas='4/4', trabaja='Cinco acordes arpegiados, de memoria'),
        dict(num=10, titulo='Al Calor del Amor en un Bar', autor='Gabinete Caligari',
             tonalidad='Mi menor', compas='4/4', trabaja='Leer el cifrado en vez del pentagrama'),
        dict(num=11, titulo='Soldadito de Hierro', autor='Nil Moliner',
             tonalidad='Do mayor', compas='4/4', trabaja='Quintas vacías, y los tresillos'),
        dict(num=12, titulo='A Sky Full of Stars', autor='Coldplay y Avicii',
             tonalidad='Fa mayor', compas='4/4', trabaja='Aguantar un riff sin endurecerse'),
    ]),
    ('Contar, y leer la hoja', 'donde la dificultad no está en los dedos', [
        dict(num=13, titulo='What Was I Made For?', autor='Billie Eilish y Finneas',
             tonalidad='Do mayor', compas='4/4', trabaja='Contar cuando nada marca el pulso'),
        dict(num=14, titulo='Writing’s on the Wall', autor='Sam Smith y Jimmy Napes',
             tonalidad='Re menor', compas='4/4', trabaja='La nota larga que sostiene, y el 8va'),
        dict(num=15, titulo='My Favourite Things', autor='Rodgers y Hammerstein II',
             tonalidad='Sol mayor', compas='3/4', trabaja='El salto del vals, a ♩=160'),
        dict(num=16, titulo='Adagio en Sol menor', autor='Albinoni, arr. A. C. Escobés',
             tonalidad='Sol menor', compas='3/4', trabaja='Un bajo obstinado, medido entero'),
        dict(num=17, titulo='Arabesque', autor='Burgmüller op. 100 nº 2 · a 4 manos',
             tonalidad='La menor', compas='2/4', trabaja='Las dos manos igual, y entrar con otra persona'),
    ]),
    ('Navidad', 'para tocar en casa en diciembre', [
        dict(num=18, titulo='Have Yourself a Merry Little Christmas', autor='Martin y Blane',
             tonalidad='Do mayor', compas='4/4', trabaja='Repartir volumen entre tres voces'),
        dict(num=19, titulo='Santa Tell Me', autor='Ariana Grande, arr. Sadie King',
             tonalidad='Sol mayor', compas='4/4', trabaja='Segno, casillas, coda y cruce de manos'),
        dict(num=20, titulo='It’s Beginning to Look a Lot Like Christmas',
             autor='Meredith Willson · a 4 manos',
             tonalidad='Do mayor', compas='6/8', trabaja='El 6/8, contado en dos, y a dúo'),
    ]),
]

# los PDF de cada dosier, en orden
DOSIERES = [
    'Dilan_01_ElCisne_CUADERNO.pdf',
    'Dilan_02_CantHelp_CUADERNO.pdf',
    'Dilan_03_YourSong_CUADERNO.pdf',
    'Dilan_04_ThinkingOutLoud_CUADERNO.pdf',
    'Dilan_05_Lucia_CUADERNO.pdf',
    'Dilan_06_PoemaDeAmor_CUADERNO.pdf',
    'Dilan_07_AmigaMia_CUADERNO.pdf',
    'Dilan_08_LaPromesa_CUADERNO.pdf',
    'Dilan_09_WhenIWasYourMan_CUADERNO.pdf',
    'Dilan_10_AlCalor_CUADERNO.pdf',
    'Dilan_11_Soldadito_CUADERNO.pdf',
    'Dilan_12_SkyFullOfStars_CUADERNO.pdf',
    'Dilan_13_WhatWasIMadeFor_CUADERNO.pdf',
    'Dilan_14_WritingsOnTheWall_CUADERNO.pdf',
    'Dilan_15_MyFavouriteThings_CUADERNO.pdf',
    'Dilan_16_AdagioAlbinoni_CUADERNO.pdf',
    'Dilan_17_Arabesque_CUADERNO.pdf',
    'Dilan_18_MerryLittleChristmas_CUADERNO.pdf',
    'Dilan_19_SantaTellMe_CUADERNO.pdf',
    'Dilan_20_BeginningChristmas_CUADERNO.pdf',
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tapas = os.path.join(OUT_DIR, 'Dilan_Portada_Indice.pdf')
    c = canvas.Canvas(tapas, pagesize=(W, H))
    build_cover(c, os.path.join(ASSETS, 'asset_logo_tclas_v2.png'), ALUMNO, SUBTITULO, CURSO)
    build_index(c, ALUMNO, ETAPAS)
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

    out = os.path.join(OUT_DIR, 'Dilan_Cuaderno_del_Pianista_2026.pdf')
    with open(out, 'wb') as f:
        wr.write(f)
    print('generado', out, '·', len(PdfReader(out).pages), 'paginas')


if __name__ == '__main__':
    main()
