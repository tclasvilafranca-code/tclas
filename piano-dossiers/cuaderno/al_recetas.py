# -*- coding: utf-8 -*-
"""El reparto de la hoja de trabajo semanal en el cuaderno de Alan.

   Mismo mecanismo que `jau_recetas`. Alan tiene 23 piezas y por tanto 23 hojas
   de trabajo; la norma de variedad no deja repetir un esqueleto más de dos
   veces ni a menos de ocho hojas, y dos bloques solo caen donde la partitura
   los justifica:

     - **`cifrado`** solo donde la edición imprime de verdad las letras de
       acorde: White Christmas (7), Perfect (19) y What Was I Made For? (20).
       Comprobado sobre el PDF.
     - **`cuatro_manos`** solo en los cuatro duetos: Romance (2), Bella Ciao
       (10), The Beginner (15) y Scherzo (22).

   Por eso las recetas con esos bloques se usan una sola vez, salvo D1 (piezas
   2 y 22, veinte hojas de distancia). Las otras ocho se reparten en parejas
   separadas por diez hojas o más.

   Costes medidos (los mismos de Josep) para cuadrar el llenado:

     diferencias 143 · cuenta 142 · plan(4) 136 · vf(5) 132 · inventa 127
     escalera(4) 120 · teclado 118 · colorea 117 · figuras 114 · nombres 111
     cifrado 110 · une(4) 108 · dibuja 104 · ordena 104 · rodea 98
     metronomo 96 · escribe 84 · reto 66 · objetivo 60 · cuatro_manos 59
     escucha 48 · nota 41
"""

RECETAS = {
    # los tres duetos
    'D1': ['reto', 'plan', 'cuatro_manos', 'ordena', 'nombres', 'figuras', 'escucha'],
    'D2': ['plan', 'cuatro_manos', 'escalera', 'diferencias', 'nombres', 'escucha'],
    'D3': ['reto', 'plan', 'cuatro_manos', 'cuenta', 'une', 'vf', 'escucha'],
    # con cifrado impreso
    'C1': ['reto', 'plan', 'escalera', 'cifrado', 'colorea', 'escucha'],
    'C2': ['plan', 'escalera', 'cifrado', 'une', 'nombres', 'escucha'],
    'C3': ['reto', 'plan', 'cifrado', 'vf', 'figuras', 'escucha'],
    # las ocho que se usan dos veces
    'A': ['reto', 'plan', 'rodea', 'une', 'colorea', 'nota', 'escucha'],
    'B': ['plan', 'metronomo', 'vf', 'inventa', 'dibuja', 'escucha'],
    'C': ['plan', 'metronomo', 'ordena', 'cuenta', 'teclado', 'escucha'],
    'D': ['reto', 'plan', 'escalera', 'inventa', 'teclado', 'escucha'],
    'E': ['reto', 'plan', 'metronomo', 'escribe', 'diferencias', 'nota', 'escucha'],
    'F': ['plan', 'escalera', 'rodea', 'escribe', 'vf', 'escucha'],
    'G': ['reto', 'plan', 'ordena', 'une', 'inventa', 'nota', 'escucha'],
    'H': ['plan', 'metronomo', 'nombres', 'colorea', 'diferencias', 'escucha'],
}

#        pieza:  1    2     3    4    5    6     7     8    9    10    11   12
ORDEN = ['A', 'D1', 'B', 'C', 'D', 'E', 'C1', 'F', 'G', 'D2', 'H', 'A',
#                13   14   15    16   17   18   19    20    21   22    23
         'B', 'C', 'D3', 'D', 'E', 'F', 'C2', 'C3', 'G', 'D1', 'H']

CON_CIFRADO = {7, 19, 20}
A_CUATRO_MANOS = {2, 10, 15, 22}


def receta(num_pieza):
    return ORDEN[num_pieza - 1]


def esqueleto(num_pieza):
    return RECETAS[receta(num_pieza)]


def revisar_reparto(modulos, verbose=True):
    """Comprueba que cada hoja de trabajo lleva los bloques que le manda el
       reparto, en ese orden, y que `cifrado` y `cuatro_manos` solo caen donde
       la partitura los justifica."""
    fallos, n = [], 0
    for mod in modulos:
        cfg = __import__(mod).CANCION
        for hoja in cfg.get('trabajo') or []:
            n += 1
            num = cfg['num']
            quiere = esqueleto(num)
            tiene = [b['tipo'] for b in hoja['bloques']]
            if tiene != quiere:
                fallos.append('%02d (%s): lleva %s y el reparto pide %s'
                              % (num, receta(num), ' > '.join(tiene),
                                 ' > '.join(quiere)))
            if 'cifrado' in tiene and num not in CON_CIFRADO:
                fallos.append('%02d: lleva cifrado y su partitura no imprime '
                              'letras de acorde' % num)
            if 'cuatro_manos' in tiene and num not in A_CUATRO_MANOS:
                fallos.append('%02d: lleva el bloque de duetos y no es un dueto' % num)
    if verbose:
        print('  reparto · %d hojas comprobadas contra al_recetas · %s'
              % (n, 'ok' if not fallos else '%d fuera de sitio' % len(fallos)))
        for f in fallos:
            print('      %s' % f)
    return fallos
