# -*- coding: utf-8 -*-
"""Peça 2 · Silent Night (Gruber), versió fàcil de sheetmusic-free.com. MESURAT sobre el PDF
   (2 pàgines A4, 7 sistemes): sense armadura (Do major), 3/4, «Gently», mp; 26 compassos
   impresos (cc. 1-22 i les caselles: 1.a cc. 23-24 amb barra de repetició cap al c. 1, 2.a
   cc. 25-26); dues lletres (2 versos); calderó al c. 20 (dues mans) i a l'últim; «rit. e dim.» a
   la casella 2; figura més curta: corxera. Alteracions només a l'esquerra: Si bemoll (c. 8),
   Fa# (cc. 10, 14, 20), Sol# (c. 18), La bemoll i Sol becaire (c. 19), La becaire (c. 20)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=3, slug='silent_night', pdf='silent_night.pdf', time_sig=(3, 4),
    titulo='Silent Night', autor='Franz X. Gruber (música) · Joseph Mohr (lletra) · versió fàcil',
    kicker='Abril · peça 3 · Silent Night', mes='Desembre · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=silent+night+piano+easy',
    credito='Partitura: F. X. Gruber, versió fàcil (sheetmusic-free.com). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '3/4'), ('Tempo', 'Gently · mp'),
               ('Figura curta', 'Corxera'), ('Compassos', '26')],
        total=26,
        secciones=[('A', 1, 8, 'Silent night… all is bright', AZUL),
                   ('B', 9, 16, 'Round yon Virgin…', OCRE),
                   ('C', 17, 22, 'Sleep in heavenly peace', AZUL),
                   ('D', 23, 26, 'Caselles 1 i 2', OCRE)],
        ideas=[('LA MELODIA', 'Ritme de bressol',
                'Negra amb puntet, corxera i negra: un balanceig que torna a moltes frases.'),
               ("L'ESQUERRA", 'Camina en negres',
                'Tres negres, o una negra i una blanca. Al final, notes llargues.'),
               ('LES ALTERACIONS', "Només a l'esquerra",
                'Si♭ (c. 8), Fa♯ (cc. 10, 14, 20), Sol♯ (c. 18) i La♭ (c. 19).'),
               ('EL FINAL', 'Calderons i rit.',
                "Calderó al c. 20 i a l'últim. A la casella 2: rit. e dim.")],
        ideas_titulo='La peça en quatre idees',
        ideas_pie='Xifrats de la partitura: C = Do, F = Fa, G = Sol, E = Mi, Am = La menor, '
                  'Bm = Si menor. G/B = Sol amb Si al baix (inversió). dim = disminuït; '
                  '7 = amb sèptima.',
        especial=[
            'Sense armadura: Do major. Posa «Gently» (suau) i mp.',
            'Dues lletres: la de dalt, 1.a vegada; la de baix, 2.a vegada.',
            'Repetició: al final del c. 24 tornes al c. 1. La 2.a vegada saltes a la casella 2 '
            '(cc. 25-26).',
            "Calderó al c. 20 (les dues mans) i a l'últim compàs.",
            'La casella 2 porta «rit. e dim.»: més lenta i més suau.',
            "Les alteracions són a l'esquerra: mira-les abans de tocar."],
        reto="Fes que la melodia canti lligada mentre l'esquerra camina regular, també als "
             "cc. 19-20. Repte acceptat?",
        truco="Toca l'esquerra sola fins que et surti mirant la dreta. Després afegeix la "
              "melodia frase a frase.",
        sabias="«Stille Nacht» es va estrenar la nit de Nadal de 1818 a l'església de Sant "
               "Nicolau d'Oberndorf, a Àustria. La lletra és del sacerdot Joseph Mohr i la "
               "música, del mestre Franz Xaver Gruber.",
        qr_texto='Escolta-la i segueix la partitura amb el dit.',
        ts=(3, 4),
        cuenta_titulo='Com es compta el c. 1',
        cuenta_pie='Negra amb puntet, corxera i negra: «1, 2, i, 3». Aquí només el ritme; les '
                   'notes, a la teva partitura.',
        ritmos=[('EL COMPTE', '3/4 · balanceig de bressol',
                 [{'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e'},
                  {'pitch': 'B4', 'dur': 'q'}], OCRE, 'treble', None)]),
    manos=dict(
        izq=[('Tres pulsos', 'Gairebé tot són negres. Toca els cc. 1-4 i compta 1-2-3.'),
             ('Baixar de pas', 'Als cc. 5 i 6 baixa de pas: Si-La-Sol i Fa-Mi-Re. Digues-ho '
                               'en veu alta.'),
             ('Les alteracions', 'Si♭ (c. 8), Fa♯ (cc. 10, 14) i Sol♯ (c. 18). Digues-les '
                                 'abans de tocar.'),
             ('Els cc. 19-20', 'Sis notes amb alteracions, una per pols. Acaben al Do '
                               'central, amb calderó.')],
        der=[('Canta-la', 'És una cançó de bressol. Canta-la per dins i respira on acaba '
                          'cada frase.'),
             ('El balanceig', 'Compta «1, 2, i, 3»: la corxera cau a la «i» i la negra, al '
                              '3.'),
             ('Notes llargues', 'Els cc. 2, 4, 6, 12 i 16 són una blanca amb puntet: tres '
                                'temps sencers.'),
             ('Calderó i rit.', 'Al c. 20 i al final allarga la nota. A la casella 2, més '
                                'lenta i més suau.')],
        tecnica=['Braç solt: la melodia es canta, no es toca a cops.',
                 "L'esquerra, sempre més fluixa que la melodia.",
                 'Compta 1-2-3 a poc a poc: és una cançó de bressol.']),
    bloques=[
        B(1, 'cc. 1-3', 'La cançó de bressol', (0, 0),
          D('cadena', 'El ritme de la melodia (c. 1)',
            [('negra amb puntet', False), ('corxera', False), ('negra', True)]),
          [('IZQUIERDA', 'Cc. 1 i 3: Do i Mi (blanca). C. 2: Do-La-Sol.'),
           ('DERECHA', 'Sol amb puntet, La i Sol. Després una nota llarga, lligada.'),
           ('JUNTAS', 'Un compàs cada cop; després els tres.'),
           ('A TEMPO', 'Gently: a poc a poc i suau (mp).')]),
        B(2, 'cc. 4-7', 'Dos acords amb inversió', (1, 1),
          D('cadena', 'Acords dels cc. 5 i 7 (amb una altra nota al baix)',
            [('Sol / Si baix', False), ('La menor / Do baix', True)]),
          [('IZQUIERDA', 'Do-La-Sol, Si-La-Sol, Fa-Mi-Re i Do-Mi-Sol.'),
           ('DERECHA', 'C. 4: Mi llarg. Cc. 5-7: blanca i negra, nota llarga, blanca i negra.'),
           ('JUNTAS', 'Els quatre compassos en bucle, comptant 1-2-3.'),
           ('OJO', 'Sol/Si i La menor/Do: el mateix acord amb una altra nota al baix '
                   '(inversió).')]),
        B(3, 'cc. 8-10', 'Primeres alteracions', (2, 2),
          D('cadena', 'Acords del bloc',
            [('Do7 / Si♭', False), ('Fa', False), ('Fa♯ dim.', True)]),
          [('IZQUIERDA', 'Si♭ al c. 8 i Fa♯ al c. 10. Digues-ho en veu alta.'),
           ('DERECHA', 'C. 10: negra amb puntet, corxera i negra, lligades.'),
           ('JUNTAS', 'Primer els cc. 8-9; després el 10.'),
           ('OJO', 'Cada alteració val només al seu compàs.')]),
        B(4, 'cc. 11-14', 'Torna la melodia', (3, 3),
          D('cadena', 'La melodia es repeteix',
            [('c. 11 = c. 1', False), ('c. 12 = c. 2', False), ('cc. 13-14 = 9-10', True)]),
          [('IZQUIERDA', 'El c. 11 comença en Mi. El c. 12 és com el c. 2. Fa♯ al c. 14.'),
           ('DERECHA', 'La melodia dels cc. 1-2 i 9-10: ja la saps.'),
           ('JUNTAS', 'Els quatre compassos en bucle.'),
           ('OJO', 'El Fa♯ del c. 14 és el mateix del c. 10.')]),
        B(5, 'cc. 15-18', 'Puja amb Si menor', (4, 4),
          D('cadena', 'Acords del bloc',
            [('Do', False), ('Si menor', False), ('Mi / Sol♯ baix', True)]),
          [('IZQUIERDA', "C. 15 com l'11. C. 17: Si-La-Sol. C. 18: Sol♯ i Si."),
           ('DERECHA', 'Cc. 15-16 repeteixen el principi. Al c. 18 puja: «heav-».'),
           ('JUNTAS', 'Dos compassos cada cop: 15-16 i 17-18.'),
           ('OJO', 'Sol♯ (c. 18): sostingut només en aquest compàs.')]),
        B(6, 'cc. 19-22', 'Calderó i pausa', (5, 5),
          D('cadena', "L'esquerra, cc. 19-20",
            [('La', False), ('La♭', False), ('Sol', False), ('Fa♯', False), ('La', False),
             ('Do', True)]),
          [('IZQUIERDA', 'Cc. 19-20: sis notes amb alteracions. Cc. 21-22: Sol i Fa llargs.'),
           ('DERECHA', 'Cc. 19-20: dues notes llargues lligades. C. 21: tres negres. C. 22: '
                       'bressol.'),
           ('JUNTAS', 'Cc. 19-20 en bucle, a poc a poc.'),
           ('OJO', 'Calderó (c. 20): la nota dura més del que està escrit.')]),
        B(7, 'cc. 23-26', 'Caselles i final', (6, 6),
          D('cadena', 'El recorregut',
            [('cc. 1-22', False), ('casella 1', False), ('↩ c. 1', False), ('cc. 1-22', False),
             ('casella 2', True)]),
          [('IZQUIERDA', 'Casella 1: Sol-Si-La, Sol-Fa-Re. Casella 2: Mi-Fa-Re i Do llarg.'),
           ('DERECHA', 'Do llarg lligat. A la casella 2, al final, nota aguda amb calderó.'),
           ('JUNTAS', 'Toca la peça amb repetició: 1.a vegada casella 1, 2.a vegada casella 2.'),
           ('A TEMPO', 'rit. e dim.: més lenta i més suau fins al calderó.')]),
    ],
    lista=['Toco la melodia lligada i cantant per dins.',
           "L'esquerra em surt sense mirar, també als cc. 19-20.",
           'Sé quan torno al c. 1 i quan salto a la casella 2.',
           'Faig bé els dos calderons.',
           "La gravo amb el mòbil i me l'escolto."],
    inicio={1: 71.5},
    cortes={1: [238, 320, 473, 545], 2: [186, 225, 384, 416, 586, 610]},
    burb={
        0: [('arriba', 262, 'AMB', 'Gently i mp: suau i a poc a poc. Compàs de 3/4: compta '
                                   '1-2-3.', 0.06),
            ('arriba', 262, 'IZQ', 'Cc. 1 i 3: Do i Mi (blanca). C. 2: tres negres, '
                                   'Do-La-Sol.', 0.45)],
        1: [('arriba', 262, 'IZQ', 'Cc. 5 i 6 baixen de pas: Si-La-Sol i Fa-Mi-Re. Digues-ho '
                                   'en veu alta.', 0.4),
            ('arriba', 262, 'OJO', 'Sol/Si i La menor/Do: el mateix acord amb una altra nota '
                                   'al baix. Això és una inversió!', 0.85)],
        2: [('arriba', 262, 'IZQ', 'Si♭ (c. 8) i Fa♯ (c. 10): alteracions, valen només al seu '
                                   'compàs.', 0.03),
            ('arriba', 262, 'DER', 'C. 10: negra amb puntet, corxera i negra: el ritme del c. '
                                   '1.', 0.8)],
        3: [('arriba', 262, 'IZQ', 'C. 11 comença en Mi, no en Do. Fa♯ al c. 14.', 0.04),
            ('arriba', 262, 'DER', 'La melodia repeteix els cc. 1-2 i 9-10: ja la saps.', 0.5)],
        4: [('arriba', 520, 'AMB', "C. 18: la melodia puja («heav-») i l'esquerra porta un "
                                   "Sol♯, sostingut només en aquest compàs.", 0.85)],
        5: [('arriba', 520, 'OJO', 'Cc. 19-20: sis notes amb alteracions fins al Do central. '
                                   "Calderó al c. 20: allarga-la tant com vulguis!", 0.3)],
        6: [('arriba', 520, 'OJO', "Al final de la casella 1 hi ha una repetició: tornes al c. "
                                   "1. La 2.a vegada, salta a la casella 2. No et perdis!",
             0.4),
            ('abajo', 520, 'AMB', "rit. e dim.: cada cop més lenta i més suau. L'últim compàs "
                                  "porta calderó.", 0.9)],
    },
    misol=dict(
        manos="Taral·leja-la abans de tocar: si la sents al cap, els dits ja saben cap on "
              "anar.",
        guia="Les alteracions fan por, però són poques i sempre a l'esquerra. Subratlla-les "
             "amb llapis!",
        pauta="Copia el ritme del bressol (negra amb puntet, corxera, negra) i inventa una "
              "melodia nova!"),
    marcas=[],
    pie_pauta="la clau la poses tu · copia un compàs o escriu l'escala de Do major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_silent_night.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
