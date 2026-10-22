# -*- coding: utf-8 -*-
"""Peça 6 · My Bonnie Lies Over the Ocean (arr. Gilbert DeBenedetti, Gradimi, «Level Two»).
   MESURAT sobre el PDF (1 pàgina, carta; notes pintades amb colorear_notas.py): sense armadura,
   3/4, «Slowly, longingly», 3 sistemes (anacrusi + 4 | 6 | 6 compassos) = 16 compassos + anacrusi.
   L'anacrusi és una negra a l'ESQUERRA (Sol3, dit 1) amb silenci de negra a la dreta. Una alteració:
   Fa♯3 (blanca amb puntet) a l'esquerra al c. 6. Marques impreses «shift» (canvi de posició de la mà) i,
   al final, «l. h. over»: l'esquerra creua per damunt i toca el Do5 final (c. 16). Figures: negres, blanques,
   blanques amb puntet i una lligadura (E3 al c. 11-12 i Re al c. 7-8). Dreta: c. 1 Mi Re Do; c. 2 Re Do;
   c. 3-4 silenci; c. 5 Mi Re Do; c. 6 Do Si Do; c. 7-8 Re lligat; c. 9 Mi Re Do; c. 10 Re Do; c. 11-12 silenci;
   c. 13 Re Do; c. 14 silenci; c. 15 Mi Sol; c. 16 Do5 (esq.). Cap corxera."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}

SPEC = dict(
    num=6, slug='bonnie', pdf='bonnie.pdf', time_sig=(3, 4),
    titulo='My Bonnie Lies Over the Ocean',
    autor='Cançó tradicional · arr. Gilbert DeBenedetti',
    kicker=kick(6, 'My Bonnie'), mes=MESES[6],
    yt=yt('my bonnie lies over the ocean piano easy'),
    credito='Partitura: arr. Gilbert DeBenedetti (gradimi.com). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense armadura'), ('Compàs', '3/4'), ('Caràcter', '«Slowly, longingly»'),
               ('Figura curta', 'Negra'), ('Compassos', '16 + anacrusi')],
        total=16,
        secciones=[('A', 1, 4, '«My Bonnie lies over the ocean»', AZUL),
                   ('A', 5, 10, '«…over the sea. My Bonnie…»', OCRE),
                   ('B', 11, 16, '«Oh, bring back my Bonnie to me»', AZUL)],
        ideas=[('LES DUES MANS', 'Per primera vegada, de debò',
                "L'esquerra no només acompanya: comença la cançó (anacrusi) i toca notes llargues pròpies."),
               ("LA POSICIÓ", 'Marques «shift»',
                'La partitura diu «shift» cada cop que la mà ha de canviar de lloc. Mira-ho abans!'),
               ('ELS SILENCIS', 'Compassos sencers',
                'Aquí hi ha silencis de compàs sencer a la dreta (cc. 3-4 i 11-12). L\'esquerra aguanta la música.'),
               ('EL FINAL', 'L\'esquerra creua',
                'Al c. 16, la partitura diu «l. h. over»: la mà esquerra passa per sobre de la dreta per tocar el Do agut.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            "La partitura diu «Slowly, longingly»: lent i amb sentiment.",
            "L'anacrusi la toca la mà esquerra (un Sol) abans del c. 1.",
            "Al c. 6 hi ha un Fa♯ a l'esquerra: l'única alteració de la peça.",
            'Cinc cops la partitura escriu «shift»: la mà canvia de lloc.',
            "Al c. 16, «l. h. over»: l'esquerra creua per sobre i toca el Do agut."],
        reto="Toca la cançó dues mans, fent bé els canvis de posició («shift») sense aturar-te.",
        truco="Toca primer la mà esquerra sola, que és la que té els canvis. Després suma la dreta.",
        sabias="«Bonnie» vol dir «bonic» en escocès. És una cançó popular del segle XIX que es canta "
               "a tot el món. (Dada no verificada.)",
        qr_texto='Escolta-la i canta amb la partitura al davant.',
        ts=(3, 4),
        cuenta_titulo='Com es compta cada compàs',
        cuenta_pie="Tres negres: «1-2-3». Una blanca amb puntet dura tot el compàs: «1-2-3». Aquí només el ritme.",
        ritmos=[('TRES NEGRES', '3/4 · 1 · 2 · 3',
                 [_q('B4'), _q('B4'), _q('B4')], OCRE, 'treble', None),
                ('BLANCA AMB PUNTET', '3/4 · 1-2-3',
                 [{'pitch': 'B4', 'dur': 'h.'}], AZUL, 'treble', None),
                ('SILENCI + DUES NEGRES', '3/4 · c. 13 · (1) · 2 · 3',
                 [{'rest': True, 'dur': 'q'}, _q('B4'), _q('B4')], VERDE, 'treble', None)]),
    manos=dict(
        izq=[("L'anacrusi: Sol", "Comença tu! Un Sol amb el dit 1, abans del c. 1. Compta «3» i toca."),
             ('Blanques amb puntet', "Al c. 1: Do durant tot el compàs (dit 5). Premem la tecla i comptem 1-2-3."),
             ('El Fa♯ del c. 6', "Una tecla negra: el Fa♯, just a la dreta del Fa. Fixa't en el símbol ♯."),
             ('«Shift»', "Quan la partitura diu «shift», la mà esquerra es mou a una altra posició. Mira-ho abans.")],
        der=[('Mi Re Do', 'C. 1: dits 3-2-1. Baixa de pas, tres notes, una per temps.'),
             ('Descans llarg', 'Als cc. 3-4 la dreta descansa: dos compassos de silenci. Compta-los!'),
             ('Do Si Do', 'C. 6: Do, Si (gris) i Do. El Si és la nota del costat.'),
             ('Mi Sol final', "C. 15: Mi i Sol amb els dits 3 i 5, i el Do final el toca l'altra mà.")],
        tecnica=['Quan una mà es mou («shift»), l\'altra es queda quieta.',
                 'Canta la melodia: és una cançó lenta que demana veu.',
                 'Compta 1-2-3 sense pressa.']),
    bloques=[
        B(1, 'anacrusi + cc. 1-4', 'My Bonnie lies over the ocean', (0, 0),
          D('cadena', 'L\'esquerra comença',
            [('anacrusi: Sol', False), ('c. 1: Mi Re Do', False), ('c. 2: Re Do', False), ('cc. 3-4: silenci', True)]),
          [('IZQUIERDA', 'Anacrusi: Sol (dit 1). C. 1: Do llarg (dit 5). C. 2: Fa i La. C. 3-4: Sol i Mi lligat.'),
           ('DERECHA', 'C. 1: Mi Re Do. C. 2: Re Do. Després dos compassos de silenci.'),
           ('JUNTAS', 'L\'esquerra comença, la dreta entra al c. 1. Compta «1-2-3».'),
           ('OJO', 'La marca «shift» indica que la mà esquerra canvia de lloc. Mira-ho abans de tocar.')]),
        B(2, 'cc. 5-10', '…over the sea. My Bonnie…', (1, 1),
          D('cadena', 'De Mi Re Do al Si',
            [('c. 5: Mi Re Do', False), ('c. 6: Do Si Do + Fa♯', False), ('cc. 7-8: Re lligat', False), ('cc. 9-10', True)]),
          [('IZQUIERDA', 'C. 5: Do llarg. C. 6: Fa♯ (la tecla negra). Cc. 7-8: notes llargues amb «shift».'),
           ('DERECHA', 'C. 5: Mi Re Do. C. 6: Do Si Do. Cc. 7-8: un Re que dura dos compassos (lligadura).'),
           ('JUNTAS', 'Mans juntes de cop: dreta melodia, esquerra notes llargues.'),
           ('OJO', 'Lligadura: el Re del c. 7 i el del c. 8 són la mateixa nota. No la toquis dues vegades.')]),
        B(3, 'cc. 11-16', 'Oh, bring back my Bonnie to me', (2, 2),
          D('cadena', 'El final: l. h. over',
            [('cc. 11-12: silenci', False), ('c. 13: Re Do', False), ('c. 15: Mi Sol', False), ('c. 16: Do agut', True)]),
          [('IZQUIERDA', 'Sol, Mi lligat, després acords. Al c. 16, creua per damunt de la dreta («l. h. over»).'),
           ('DERECHA', 'Cc. 11-12: silenci. C. 13: Re Do. C. 15: Mi Sol. C. 16: descansa.'),
           ('JUNTAS', 'Les dues mans fins al Mi Sol; després, la mà esquerra creua i toca el Do agut.'),
           ('OJO', "Al c. 16 la mà esquerra passa per sobre de la dreta: avança el braç esquerre sense moure el cos.")]),
        B(4, 'cc. 1-16', 'Tota la cançó', (0, 2),
          D('cadena', 'De dalt a baix',
            [('cc. 1-4', False), ('cc. 5-10', False), ('cc. 11-16', True)]),
          [('IZQUIERDA', 'Només l\'esquerra, amb tots els «shift» i el Fa♯.'),
           ('DERECHA', 'Només la dreta, amb els silencis ben comptats.'),
           ('JUNTAS', 'Les dues mans, tota la cançó, lenta i amb sentiment.'),
           ('A TEMPO', 'Canta-la mentre la toques: «Slowly, longingly». Sense pressa!')]),
    ],
    lista=["Toco l'anacrusi (Sol) i entro a temps.",
           "Toco la mà esquerra sola amb tots els «shift».",
           'Toco el Fa♯ del c. 6.',
           'Sé fer la lligadura dels cc. 7-8 i dels cc. 11-12.',
           'Faig el «l. h. over» final.'],
    cortes={1: [380.8, 537.8]}, inicio={1: 222}, fin={1: 689},
    burb={
        0: [('arriba', 262, 'IZQ', "Anacrusi: la mà esquerra toca el Sol (dit 1) abans del c. 1.", 0.12),
            ('arriba', 262, 'DER', 'Mi Re Do (c. 1), Re Do (c. 2). Dos compassos de silenci després.', 0.5)],
        1: [('arriba', 262, 'OJO', 'Fa♯ a la mà esquerra al c. 6: la tecla negra, a la dreta del Fa.', 0.22),
            ('arriba', 262, 'DER', 'Re lligat entre els cc. 7-8: una sola nota que dura dos compassos.', 0.55)],
        2: [('arriba', 262, 'DER', 'Cc. 11-12 silenci. C. 13: Re Do. C. 15: Mi Sol.', 0.45),
            ('arriba', 262, 'OJO', '«l. h. over»: l\'esquerra creua i toca el Do agut final.', 0.93)],
    },
    misol=dict(
        manos="Quan vegis «shift», la mà es mou: mira on cau el dit i no hi ha por!",
        guia="Les lligadures són notes unides: la segona no es toca, només s'aguanta. Només un so!",
        pauta="Escriu la nota Sol amb la clau de fa i pinta-la de blau."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu el Do i el Sol amb els seus colors")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_bonnie.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
