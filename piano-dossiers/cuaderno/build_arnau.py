# -*- coding: utf-8 -*-
"""Genera la portada + indice del cuaderno nuevo de Arnau."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.pdfgen import canvas
from portada import build_cover, build_index, W, H

HERE = os.path.dirname(__file__)
ASSETS = os.path.join(HERE, '..', 'assets')
OUT_DIR = os.path.join(HERE, '..', 'output')

ALUMNO = 'Arnau'
SUBTITULO = 'Nivel iniciación · 9 años'
CURSO = 'Curso 2026 · 2027'

# (num, titulo, autor, tonalidad, compas, QUE SE TRABAJA con esta pieza)
ETAPAS = [
    ('Primeros pasos', 'Do mayor · sin alteraciones', [
        dict(num=1, titulo='Chopsticks', autor='arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='3/4', trabaja='Las dos manos se turnan'),
        dict(num=2, titulo='Clementine', autor='arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='3/4', trabaja='La melodía, con la derecha sola'),
        dict(num=3, titulo='Baa Baa Black Sheep', autor='arr. Jim Paterson',
             tonalidad='Do mayor', compas='4/4', trabaja='Notas repetidas sin cansarse'),
        dict(num=4, titulo='Do Your Ears Hang Low?', autor='arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='4/4', trabaja='El salto grande, ligero'),
        dict(num=5, titulo='Oh, When the Saints', autor='arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='4/4', trabaja='El acorde desgranado (arpegio)'),
        dict(num=6, titulo='Jolly Old Saint Nicholas', autor='arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='4/4', trabaja='La escala, paso a paso'),
        dict(num=7, titulo='We Wish You a Merry Christmas', autor='arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='3/4', trabaja='Pregunta y respuesta entre manos'),
        dict(num=8, titulo='Puff the Magic Dragon', autor='Peter, Paul and Mary',
             tonalidad='Do mayor', compas='4/4', trabaja='Notas largas que no se cortan'),
        dict(num=9, titulo='Eso que tú me das', autor='Jarabe de Palo',
             tonalidad='Do mayor', compas='4/4', trabaja='Un ciclo de cuatro acordes'),
    ]),
    ('Primera armadura', 'Fa mayor · aparece el Si bemol', [
        dict(num=10, titulo='The Wheels on the Bus', autor='arr. Jim Paterson',
             tonalidad='Fa mayor', compas='4/4', trabaja='Leer con un bemol en la armadura'),
        dict(num=11, titulo='Polly Put the Kettle On', autor='arr. Jim Paterson',
             tonalidad='Fa mayor', compas='4/4', trabaja='Legato: unir sin cortar'),
        dict(num=12, titulo='Little Miss Muffet', autor='arr. Jim Paterson',
             tonalidad='Fa mayor', compas='6/8', trabaja='El 6/8: dos grupos de tres'),
    ]),
    ('Retos', 'piezas que piden algo más', [
        dict(num=13, titulo='Aloha Oe', autor='Reina Liliuokalani, arr. R. Pratley',
             tonalidad='Do mayor', compas='2/2', trabaja='Compás partido: contar a dos'),
        dict(num=14, titulo='La Pantera Rosa', autor='Henry Mancini',
             tonalidad='Do mayor', compas='4/4', trabaja='Notas cromáticas (teclas negras)'),
        dict(num=15, titulo='My Bonnie Lies Over the Ocean', autor='arr. Gilbert DeBenedetti',
             tonalidad='Do mayor', compas='3/4', trabaja='Cambiar la mano de posición'),
        dict(num=16, titulo='El Submarino Amarillo', autor='Lennon/McCartney, arr. Escobés',
             tonalidad='Sol mayor', compas='4/4', trabaja='Nueva armadura: el Fa sostenido'),
        dict(num=17, titulo='Popeye el marinerito', autor='arr. A. C. Escobés',
             tonalidad='Sol mayor', compas='3/4', trabaja='Sol mayor, ahora en vals'),
        dict(num=18, titulo='Largo · Sinfonía nº 5', autor='A. Dvořák, arr. Escobés',
             tonalidad='Do mayor', compas='4/4', trabaja='La frase larga, sin cortarla'),
    ]),
    ('A cuatro manos', 'con la profesora al lado', [
        dict(num=19, titulo='Rain Rain Go Away', autor='Tradicional, arr. R. Pratley',
             tonalidad='Do mayor', compas='4/4', trabaja='Entrar y seguir a la vez'),
        dict(num=20, titulo='The Mulberry Bush', autor='Tradicional, arr. R. Pratley',
             tonalidad='Do mayor', compas='6/8', trabaja='El 6/8, ahora a dúo'),
    ]),
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, 'Arnau_Cuaderno_Portada_Indice.pdf')
    c = canvas.Canvas(out, pagesize=(W, H))
    build_cover(c, os.path.join(ASSETS, 'asset_logo_tclas_v2.png'), ALUMNO, SUBTITULO, CURSO)
    build_index(c, ALUMNO, ETAPAS)
    c.save()
    print('generated', out)


if __name__ == '__main__':
    main()
