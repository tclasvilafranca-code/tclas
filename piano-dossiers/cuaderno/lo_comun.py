# -*- coding: utf-8 -*-
"""Peces comunes dels dossiers de Lola (8 anys, nova al piano, necessita els colors de les notes)."""
MESES = {1: 'Novembre · 1.a quinzena', 2: 'Novembre · 2.a quinzena', 3: 'Desembre', 4: 'Gener',
         5: 'Febrer · 1.a quinzena', 6: 'Febrer · 2.a quinzena', 7: 'Març · 1.a quinzena',
         8: 'Març · 2.a quinzena', 9: 'Abril · 1.a quinzena', 10: 'Abril · 2.a quinzena',
         11: 'Maig · 1.a quinzena', 12: 'Maig · 2.a quinzena', 13: 'Juny · 1.a quinzena',
         14: 'Juny · 2.a quinzena', 15: 'Juliol'}
COLORS = 'Do = vermell · Re = taronja · Mi = groc · Fa = verd · Sol = blau · La = lila · Si = gris.'


def kick(num, titulo):
    return 'Lola · peça %d · %s' % (num, titulo)


def yt(q):
    return 'https://www.youtube.com/results?search_query=' + q.replace(' ', '+')
