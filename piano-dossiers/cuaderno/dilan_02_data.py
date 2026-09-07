# -*- coding: utf-8 -*-
"""Material verificado de Can't Help Falling in Love (arr. Seb Alejandro).

   Todo medido; ver TRANSCRIPCION_D02_CANT_HELP.md. Con armadura de Re mayor
   los Fa y los Do se escriben SIN sostenido: la armadura ya los altera.

   El dibujo de la mano izquierda es siempre el mismo acorde roto:
   fundamental · 3a · 5a · 8a · 5a · 3a. Cambia el acorde, no el gesto.
"""
TONALIDAD = 'Re mayor'
COMPAS = (3, 4)

_B = [0]


def arpegio(fund, tercera, quinta, octava, n=1):
    """Un compas del acompanamiento: seis corcheas bajo una sola barra."""
    out = []
    for _ in range(n):
        _B[0] += 1
        for p in (fund, tercera, quinta, octava, quinta, tercera):
            out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


# --- los acordes reales de la pieza, medidos y contrastados con el cifrado --
RE      = ('D3', 'F3', 'A3', 'D4')      # c. 1   · cifrado D
FAm     = ('F3', 'A3', 'C4', 'E4')      # c. 2   · cifrado F#m
SIm     = ('B2', 'D3', 'F3', 'B3')      # c. 3   · cifrado Bm
LA      = ('A2', 'C3', 'E3', 'A3')      # cc. 5-6 · La mayor

# la melodia medida de los tres primeros compases
MELODIA_1_3 = [{'pitch': 'D4', 'dur': 'h.'},
               {'pitch': 'A4', 'dur': 'h.'},
               {'pitch': 'D4', 'dur': 'h.'}]
