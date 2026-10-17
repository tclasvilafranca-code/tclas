# -*- coding: utf-8 -*-
"""Annexos del Quadern PEKES: glossari, teclat i targetes per retallar, pautes en blanc i banc de jocs per a la profe."""
from nens_t07 import *                                            # noqa: F401,F403
from nens_tclas import pagina, pauta, gran_pauta, cap
import nens_pla as pla

KICK = 'PEKES  ·  ANNEXOS'


def pg(titol, k):
    """Número de pàgina de la k-èsima pàgina dels annexos (0..7)."""
    return pla.ANNEX_PAG[0][1] + k


# ------------------------------------------------------------------ 1 · glossari
TERMES = [
    ('Acord', 'Tres notes que sonen alhora.', 29), ('Agut', 'So fi, com el d’un ocell.', 3),
    ('Atril', 'Suport on posem la partitura.', 1), ('Barra de compàs', 'Línia que separa un compàs d’un altre.', 18),
    ('Blanca', 'Figura que dura 2 temps.', 15), ('Calderó', 'Signe que allarga una nota una mica més.', 34),
    ('Clau de fa', 'Clau de la mà esquerra: notes greus.', 6), ('Clau de sol', 'Clau de la mà dreta: notes agudes.', 6),
    ('Compàs', 'Caixa de temps iguals: 4/4, 3/4 o 2/4.', 18), ('Corxera', 'Figura que dura mig temps.', 16),
    ('DO central', 'El DO que queda al mig del piano.', 4), ('Fort i suau', 'p = piano (suau) i f = forte (fort).', 31),
    ('Frase', 'Tros de música amb sentit, com una frase parlada.', 34), ('Greu', 'So gruixut, com el d’un ós.', 3),
    ('Lligadura', 'Línia que uneix dues notes iguals.', 19), ('Lligat i picat', 'Enllaçat o curt i separat.', 33),
    ('Melodia', 'La cançó feta de notes que pugen o baixen.', 13), ('Negra', 'Figura que dura 1 temps.', 15),
    ('Nota', 'Cada so amb nom: DO, RE, MI, FA, SOL, LA, SI.', 8), ('Octava', 'Vuit notes: del DO al següent DO.', 12),
    ('Pentagrama', 'Cinc línies i quatre espais on viuen les notes.', 5), ('Plica', 'El palet de la nota.', 22),
    ('Pols', 'El batec constant de la música.', 14), ('Puntet', 'Afegeix la meitat del valor d’una nota.', 19),
    ('Repetició', 'Dues barres amb punts: torna al principi.', 34), ('Rodona', 'Figura que dura 4 temps.', 15),
    ('Silenci', 'Moment sense so que també es compta.', 20), ('Tempo', 'La velocitat de la música: lent, moderat o ràpid.', 32),
]


def glossari(c, part):
    pagina(c, KICK, 'Glossari d’en Mussol', 'Annex 1 · %d/2' % (part + 1),
           'Totes les paraules importants, per ordre alfabètic.', pg('', part))
    ll = TERMES[part * 14:(part + 1) * 14]
    cw = (CW - 14) / 2.0
    for k, (t, d, tema) in enumerate(ll):
        col, fila = k // 7, k % 7
        x = M + col * (cw + 14)
        yt = Y(124) - fila * 92
        h = 80
        rr(c, x + 3, yt - h - 3, cw, h, 8, fill=SOMBRA, lw=0)
        rr(c, x, yt - h, cw, h, 8, fill=white, lw=1.6, col=NAVY)
        rr(c, x, yt - 24, cw, 24, 8, fill=NAVY, lw=1.6, col=NAVY)
        c.setFillColor(NAVY)
        c.rect(x + 1.5, yt - 24, cw - 3, 10, stroke=0, fill=1)
        txt(c, x + 12, yt - 17, t.upper(), 11.5, ETQ, white)
        txt(c, x + cw - 10, yt - 17, 'tema %d · pàg. %d' % (tema, pla.TEMES[tema]['pag']), 9.2, SANS, HexColor('#E0D6BD'), 'r')
        par(c, x + 12, yt - 44, d, 12.5, cw - 24, 15.5, SANS, INK)
    c.showPage()


# ------------------------------------------------------------------ 2 · teclat i targetes
def teclat_retallar(c):
    pagina(c, KICK, 'El meu teclat de paper', 'Annex 2 · 1/2', 'Retalla les tires, enganxa-les i toca sobre el paper com si fos un piano.', pg('', 2))
    caixa_t(c, M, Y(124), CW, 78, 'COM ES FA', 'Retalla per les línies de punts. Enganxa les tires a un cartró i posa-les davant teu. '
            'Mou els dits per sobre i digues el nom de cada nota!', 11.8)
    for k, (tit, kw_) in enumerate((('AMB NOMS', dict(noms='totes')), ('SENSE NOMS (TU LI POSES)', dict()),
                                    ('EN COLOR', dict(noms='resalta', color=True, resalta={i: NOTES7[i % 7] for i in range(14)})))):
        yt = Y(224) - k * 188
        txt(c, M, yt, tit, 10.5, ETQ, OCRE)
        rr(c, M - 4, yt - 164, CW + 8, 150, 4, fill=white, lw=1.2, col=MUTED, dash=(4, 3))
        teclat(c, M + 8, yt - 138, CW - 16, 96, nb=14, **kw_)
        txt(c, M + CW - 4, yt - 168, '✂', 14, 'DejaVuSans', MUTED, 'r')
    c.showPage()


def targetes(c):
    pagina(c, KICK, 'Targetes per retallar', 'Annex 2 · 2/2', 'Per jugar amb la profe: notes, figures, silencis i més.', pg('', 3))
    cw, chh = (CW - 3 * 10) / 4.0, 84
    cards = []
    for nm in NOTES7 + ['DO']:
        cards.append(('nota', nm))
    for t, nm, v in (('w', 'rodona', '4'), ('h', 'blanca', '2'), ('q', 'negra', '1'), ('e', 'corxera', '½')):
        cards.append(('fig', (t, nm, v)))
    for t, nm in (('w', 'silenci de rodona'), ('h', 'silenci de blanca'), ('q', 'silenci de negra'), ('e', 'silenci de corxera')):
        cards.append(('sil', (t, nm)))
    for s_, nm in (('p', 'suau'), ('mf', 'una mica fort'), ('f', 'fort'), ('ff', 'molt fort')):
        cards.append(('din', (s_, nm)))
    for t, nm, v in (('tortuga', 'lent', 'adagio'), ('petjades', 'moderat', 'andante'), ('coet', 'ràpid', 'allegro')):
        cards.append(('tem', (t, nm, v)))
    for k, (tp, d) in enumerate(cards):
        col, fila = k % 4, k // 4
        x = M + col * (cw + 10)
        yt = Y(124) - fila * (chh + 12)
        rr(c, x, yt - chh, cw, chh, 6, fill=white, lw=1.2, col=MUTED, dash=(4, 3))
        if tp == 'nota':
            hexc = HexColor(COL[d])
            rr(c, x + 6, yt - chh + 6, cw - 12, chh - 12, 5, fill=hexc, lw=1.4, col=NAVY)
            txt(c, x + cw / 2, yt - chh / 2 - 8, d, 26, SERIFB, INK if d == 'MI' else white, 'c')
        elif tp == 'fig':
            figura(c, d[0], x + cw / 2, yt - 46 if d[0] != 'w' else yt - 40, 7 if d[0] != 'w' else 9)
            txt(c, x + cw / 2, yt - 64, d[1], 11, SANSB, NAVY, 'c')
            txt(c, x + cw / 2, yt - 77, d[2] + ' temps', 10, SANS, MUTED, 'c')
        elif tp == 'sil':
            g = 7
            ytop = yt - 28
            yb = pauta(c, x + 14, ytop, cw - 28, g, None, final=False)
            nt.draw_rest(c, x + cw / 2, yb, ytop, g, d[0])
            txt(c, x + cw / 2, yt - 68, d[1], 10, SANSB, NAVY, 'c')
        elif tp == 'din':
            dinamica(c, x + cw / 2, yt - 42, d[0], 28)
            txt(c, x + cw / 2, yt - 70, d[1], 11, SANSB, NAVY, 'c')
        else:
            {'tortuga': tortuga, 'petjades': petjades, 'coet': coet}[d[0]](c, x + cw / 2, yt - 30 if d[0] != 'tortuga' else yt - 38, 0.34 if d[0] != 'petjades' else 0.5, color=False)
            txt(c, x + cw / 2, yt - 64, d[1] + ' · ' + d[2], 10.5, SANSB, NAVY, 'c')
    c.showPage()


# ------------------------------------------------------------------ 3 · pautes en blanc
def pautes_1(c):
    pagina(c, KICK, 'Pautes en blanc', 'Annex 3 · 1/2', 'Per escriure notes, inventar melodies i fer exercicis.', pg('', 4))
    for k in range(9):
        pauta(c, M + 6, Y(150) - k * 62, CW - 12, 8.4, 'treble' if k % 2 == 0 else 'bass', final=True)
    c.showPage()


def pautes_2(c):
    pagina(c, KICK, 'Pautes en blanc', 'Annex 3 · 2/2', 'Pentagrames grans, per a les dues mans.', pg('', 5))
    for k in range(5):
        gran_pauta(c, M + 24, Y(140) - k * 126, CW - 30, 8.2)
    c.showPage()


# ------------------------------------------------------------------ 4 · banc de jocs per a la profe
JOCS = [
    ('El semàfor musical', 'Notes de color (temes 8-11)', 'Targetes grans de colors (annex 2).',
     'Posa les targetes a terra. Toca una nota i l’alumne corre a trepitjar la targeta del seu color.'),
    ('El detectiu de notes', 'Notes (8-12)', 'Targetes de notes i una capsa.',
     'Amaga una targeta sota un mocador. Toca la nota al piano i l’alumne diu quina és abans de destapar-la.'),
    ('L’eco', 'Pols i ritme (14-17)', 'Només les mans.',
     'La profe pica un ritme curt (ta, ti-ti, ta). L’alumne el repeteix com un eco. Després canvien els papers.'),
    ('Estàtues musicals', 'Silencis (20-21)', 'Música gravada o piano.',
     'Mentre sona la música, l’alumne es mou. Quan ve un silenci, es queda quiet com una estàtua.'),
    ('El tren del compàs', 'El compàs (18)', 'Cadires o coixins.',
     'Els nens fan un tren: 4 vagons per al 4/4, 3 per al vals i 2 per a la marxa. El primer vagó té el temps fort.'),
    ('Bingo de notes', 'Les set notes (11)', 'Cartrons de 3×3 que dibuixes amb notes de colors.',
     'La profe toca una nota i els alumnes la cerquen al seu cartró. Qui té tot el cartró, canta Bingo!'),
    ('Memory de figures', 'Les figures (15-17)', 'Targetes de figures i de noms.',
     'Posa les targetes capgirades. Cada parella (figura i nom) que trobin, se la queden. Guanya qui en té més.'),
    ('El mussol dorm', 'Fort i suau (31)', 'Un peluix de mussol.',
     'El mussol dorm: l’alumne toca molt suau. Quan es desperta, toca fort. Es fan servir p, f i els passos entre mig.'),
    ('L’escala de colors', 'Les set notes (11-12)', 'Fulls de colors a terra.',
     'Posa set fulls de colors en fila. L’alumne puja i baixa l’escala caminant mentre diu el nom de cada nota.'),
    ('El dictat de la melodia', 'Direcció (13)', 'Només el piano.',
     'La profe toca tres notes: l’alumne mou la mà amunt si pugen, avall si baixen i la deixa quieta si són iguals.'),
    ('Passejada pel pols', 'Pols i tempo (14, 32)', 'Una cançó o el metrònom.',
     'Caminen pel pols de la música. Quan la profe accelera o alenteix, l’alumne canvia el pas: lent, moderat o ràpid.'),
    ('Lliscar o botar?', 'Lligat i picat (33)', 'Només el cos.',
     'La profe toca lligat i l’alumne llisca la mà; si toca picat, la mà bota. Després ho fa a l’inrevés!'),
]


def banc_jocs(c, part):
    pagina(c, KICK, 'Banc de jocs per a la profe', 'Annex 4 · %d/2' % (part + 1),
           'Dotze idees per jugar amb la música a la classe, sense gaires materials.', pg('', 6 + part))
    ll = JOCS[part * 6:(part + 1) * 6]
    cw = (CW - 14) / 2.0
    for k, (t, per, mat, com) in enumerate(ll):
        col, fila = k % 2, k // 2
        x = M + col * (cw + 14)
        yt = Y(124) - fila * 218
        h = 202
        rr(c, x + 3, yt - h - 3, cw, h, 8, fill=SOMBRA, lw=0)
        rr(c, x, yt - h, cw, h, 8, fill=white, lw=1.6, col=NAVY)
        rr(c, x, yt - 32, cw, 32, 8, fill=NAVY, lw=1.6, col=NAVY)
        c.setFillColor(NAVY)
        c.rect(x + 1.5, yt - 32, cw - 3, 12, stroke=0, fill=1)
        bola(c, x + 20, yt - 16, part * 6 + k + 1, 11)
        txt(c, x + 38, yt - 21, t, 13, ETQ, white)
        txt(c, x + 12, yt - 52, 'PER A', 9.2, ETQ, OCRE)
        txt(c, x + 56, yt - 52, per, 11, SANSB, NAVY)
        txt(c, x + 12, yt - 72, 'MATERIAL', 9.2, ETQ, OCRE)
        par(c, x + 74, yt - 72, mat, 11, cw - 86, 13.5, SANS, INK)
        txt(c, x + 12, yt - 98, 'COM ES JUGA', 9.2, ETQ, OCRE)
        par(c, x + 12, yt - 118, com, 12.5, cw - 24, 16, SANS, INK)
    c.showPage()
