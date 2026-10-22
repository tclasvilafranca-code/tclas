# -*- coding: utf-8 -*-
"""Annex del Quadern PEKES: pautes en blanc."""
from nens_t07 import *                                            # noqa: F401,F403
from nens_tclas import pagina, pauta, gran_pauta
import nens_pla as pla

KICK = 'PEKES  ·  ANNEX'


def pautes_1(c):
    pagina(c, KICK, 'Pautes en blanc', 'Annex · 1/2', 'Per escriure notes, inventar melodies i fer exercicis.', pla.ANNEX_PAG[0][1])
    for k in range(9):
        pauta(c, M + 6, Y(150) - k * 62, CW - 12, 8.4, 'treble' if k % 2 == 0 else 'bass', final=True)
    c.showPage()


def pautes_2(c):
    pagina(c, KICK, 'Pautes en blanc', 'Annex · 2/2', 'Pentagrames grans, per a les dues mans.', pla.ANNEX_PAG[0][1] + 1)
    for k in range(5):
        gran_pauta(c, M + 24, Y(140) - k * 126, CW - 30, 8.2)
    c.showPage()
