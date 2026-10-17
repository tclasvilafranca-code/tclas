# -*- coding: utf-8 -*-
"""El Quadern del Pianista · PEKES — pla del llibre: capítols, temes i numeració de pàgines.

   Pàgines 1-4: portada, en Mussol, com s'usa el llibre, índex. Després, cada tema té una
   pàgina de TEORIA ("APRENC") i una de JOCS ("JUGUEM"); algun tema en té més (`pags`).
   Al final, els annexos. La numeració surt d'aquí, de manera que l'índex és sempre correcte.
"""

CAPITOLS = {
    1: 'Abans de tocar',
    2: 'El pentagrama',
    3: 'Les notes i els seus colors',
    4: 'El ritme',
    5: 'Els silencis',
    6: 'Les plicas',
    7: 'Toquem!',
    8: 'Expressem la música',
}

# (n, capítol, títol, píndola del mapa, pàgines)
_T = [
    (1, 1, 'El piano i les seves parts', 'EL PIANO', 2),
    (2, 1, 'Com m’assec i els meus dits', 'POSTURA I DITS', 2),
    (3, 1, 'Greu i agut', 'GREU I AGUT', 2),
    (4, 1, 'El teclat: blanques i negres', 'EL TECLAT', 2),
    (5, 2, 'Línies i espais', 'LÍNIES I ESPAIS', 2),
    (6, 2, 'Clau de sol i clau de fa', 'LES CLAUS', 2),
    (7, 2, 'El pentagrama gran i el Do central', 'DO CENTRAL', 2),
    (8, 3, 'Do, Re i Mi', 'DO · RE · MI', 2),
    (9, 3, 'Fa i Sol', 'FA · SOL', 2),
    (10, 3, 'La i Si', 'LA · SI', 2),
    (11, 3, 'Les set notes', '7 NOTES', 2),
    (12, 3, 'L’octava', 'OCTAVA', 2),
    (13, 3, 'La melodia puja i baixa', 'MELODIA', 2),
    (14, 4, 'El pols', 'EL POLS', 2),
    (15, 4, 'Rodona, blanca i negra', 'RODONA · BLANCA · NEGRA', 2),
    (16, 4, 'La corxera', 'LA CORXERA', 2),
    (17, 4, 'Els temps i sumar figures', 'SUMAR FIGURES', 2),
    (18, 4, 'El compàs: 4/4, 3/4 i 2/4', 'EL COMPÀS', 2),
    (19, 4, 'Allargar notes: puntet i lligadura', 'PUNTET I LLIGADURA', 2),
    (20, 5, 'Silenci de rodona i de blanca', 'RODONA · BLANCA', 2),
    (21, 5, 'Silenci de negra i de corxera', 'NEGRA · CORXERA', 2),
    (22, 6, 'Plica amunt o avall', 'PLICA', 2),
    (23, 6, 'Dibuixo notes perfectes', 'NOTES PERFECTES', 2),
    (24, 7, 'Posició de Do: mà dreta', 'MÀ DRETA', 2),
    (25, 7, 'Mà esquerra i clau de fa', 'MÀ ESQUERRA', 2),
    (26, 7, 'Les dues mans juntes', 'DUES MANS', 2),
    (27, 7, 'Les primeres cançons', 'CANÇONS', 3),
    (28, 7, 'Llegir a primer cop d’ull', 'LLEGIR', 2),
    (29, 7, 'L’acord de Do', 'ACORD DE DO', 2),
    (30, 7, 'Com estudio una cançó', 'ESTUDIAR', 2),
    (31, 8, 'Fort i suau', 'FORT I SUAU', 2),
    (32, 8, 'Ràpid i lent', 'RÀPID I LENT', 2),
    (33, 8, 'Lligat i picat', 'LLIGAT I PICAT', 2),
    (34, 8, 'Repeticions, frases i calderó', 'FRASES', 2),
]
ANNEXOS = [('Glossari d’en Mussol', 2), ('Targetes i teclat per retallar', 2),
           ('Pautes en blanc', 2), ('Banc de jocs per a la profe', 2)]

TEMES = {}
_p = 5
for (n, cap, titol, pill, pags) in _T:
    TEMES[n] = dict(n=n, cap=cap, titol=titol, pill=pill, pags=pags, pag=_p)
    _p += pags
ANNEX_PAG = []
for (t, k) in ANNEXOS:
    ANNEX_PAG.append((t, _p, k))
    _p += k
TOTAL = _p - 1


def temes_del_cap(cap):
    return [TEMES[n] for n in sorted(TEMES) if TEMES[n]['cap'] == cap]


def pagines_cap(n):
    """Píndoles del mapa 'ET TROBES AQUÍ' per al capítol del tema `n` i l'índex actiu."""
    t = TEMES[n]
    ll = temes_del_cap(t['cap'])
    return [x['pill'] for x in ll], [x['n'] for x in ll].index(n)


def kicker(n):
    t = TEMES[n]
    return 'PEKES  ·  CAPÍTOL %d  ·  %s' % (t['cap'], CAPITOLS[t['cap']].upper())


if __name__ == '__main__':
    print(TOTAL, TEMES[8]['pag'], TEMES[27]['pag'], TEMES[34]['pag'])
