# -*- coding: utf-8 -*-
"""Música escrita en text per al Quadern PEKES: 'E4 D4 C4:h | R:q [C4+E4+G4]:w'.
   Marques després de la durada:  ~ lligadura de valor · ! calderó · * picat (staccato).
   Les corxeres se sumen sols en parelles per temps (com cal)."""
import nens_tclas as nk
from nens_tclas import nt

DUR_B = {'w': 4, 'h.': 3, 'h': 2, 'q.': 1.5, 'q': 1, 'e.': 0.75, 'e': 0.5, 's': 0.25}


def mus(text):
    out = []
    pos = 0.0
    beam_id = 0
    for tok in text.split():
        if tok == '|':
            continue
        p, _, d = tok.partition(':')
        d = d or 'q'
        marques = ''
        while d and d[-1] in '~!*':
            marques += d[-1]
            d = d[:-1]
        d = d or 'q'
        if p == 'R':
            ev = {'rest': True, 'dur': d}
        elif p.startswith('['):
            ev = {'pitches': p.strip('[]').split('+'), 'dur': d}
        else:
            ev = {'pitch': p, 'dur': d}
        if '~' in marques:
            ev['lig'] = True
        if '!' in marques:
            ev['art'] = 'calderon'
        if '*' in marques:
            ev['art'] = 'staccato'
        if d == 'e' and not ev.get('rest'):
            ev['beam'] = int(pos)          # dues corxeres al mateix temps
        out.append(ev)
        pos += DUR_B[d]
    # una corxera sola dins del seu temps no es barra
    from collections import Counter
    cnt = Counter(e['beam'] for e in out if 'beam' in e)
    for e in out:
        if 'beam' in e and cnt[e['beam']] < 2:
            del e['beam']
    return out


def beats(text):
    return sum(DUR_B[(tok.partition(':')[2].rstrip('~!*') or 'q')] for tok in text.split() if tok != '|')


def sist(c, x, ytop, w, gap, text, clau='treble', compas=(4, 4), show_time=True, show_clef=True, final=True, **kw):
    """Un sistema de pentagrama del motor, amb el text musical. Retorna (top, bot)."""
    ev = mus(text) if isinstance(text, str) else text
    top, bot = nt.draw_system(c, x, ytop, w, gap, ev, clau, compas, show_clef=show_clef, show_time=show_time, **kw)
    return top, bot
