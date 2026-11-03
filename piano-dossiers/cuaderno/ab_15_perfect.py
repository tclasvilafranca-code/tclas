# -*- coding: utf-8 -*-
"""Peça 15 · Perfect (Ed Sheeran), edició del campament «Bye Bye Beethoven» (byebyebeethoven.es).
   MEDIDO sobre el PDF de Drive (EDICIÓ DIFERENT de la de ms_10_perfect: 1 pàgina CARTA, vectorial):
   una anacrusi de tres corxeres (Re-Mi-Sol) i 27 compassos en 7 sistemes (4 + sis de 4 + un de 3; numeració
   impresa 5, 9, 13, 17, 21, 25), una armadura d'un sostingut (Sol major), 12/8, «♩. = 94» (negra amb
   puntet), sense matisos ni repeticions, barres dobles al final dels cc. 8, 16 i 24, corxera com a
   figura més curta, digitació impresa per l'edició (números 1-5). Xifrats impresos: G, Em, C, D i D/F♯
   (c. 25). Esquerra: dues blanques amb puntet per compàs (Sol, Mi, Do, Re als cc. 1-16; Mi-Do i Sol-Re
   als cc. 17-24), c. 25 Sol-Fa♯-Mi-Re (negres amb puntet), c. 26 Do-Re, c. 27 Sol (rodona amb puntet).
   Dreta: ambit Re4-Sol5 (Sol5 als cc. 17, 19 i 21); c. 12 amb lligadura entre un Si de negra amb
   puntet i un Si de corxera; c. 25 Si-La-Sol-Fa♯, c. 26 Mi-Fa♯, c. 27 Sol."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=15, slug='ab_perfect', pdf='perfect_ed_sheeran.pdf', time_sig=(12, 8),
    titulo='Perfect', autor="Ed Sheeran · edició del campament Bye Bye Beethoven",
    kicker='Abril · peça 15 · Perfect', mes='Juny · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=ed+sheeran+perfect+piano+easy+tutorial',
    credito='Partitura: edició del campament Bye Bye Beethoven (byebyebeethoven.es). '
            'Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sol major'), ('Compàs', '12/8'), ('Tempo', '♩. = 94'),
               ('Figura curta', 'Corxera'), ('Compassos', '27 + anacrusi')],
        total=27,
        secciones=[('A', 1, 8, 'Primera part', AZUL), ('B', 9, 16, 'Segona part', OCRE),
                   ('C', 17, 24, 'Tercera part', AZUL), ('D', 25, 27, 'Final', OCRE)],
        ideas_titulo='La peça en quatre idees',
        ideas=[('ELS ACORDS', 'Quatre, en bucle',
                'Sol, Mi menor, Do i Re: un per compàs, sempre en aquest ordre als cc. 1-16.'),
               ("L'ESQUERRA", 'Dues notes llargues',
                'Dues notes per compàs, cadascuna de dos temps: Sol, Mi, Do i Re. Es mou molt '
                'poc.'),
               ('LA DRETA', 'Llarga i tres corxeres',
                'Notes llargues amb puntet i grups de tres corxeres. Entra amb una anacrusi.'),
               ('EL FINAL', 'Baixada de pas',
                'Al c. 25 les dues mans baixen de pas: dreta Si-La-Sol-Fa♯, esquerra '
                'Sol-Fa♯-Mi-Re.')],
        ideas_pie='La partitura imprimeix xifrats: G = Sol major, Em = Mi menor, C = Do major, '
                  'D = Re major, D/F♯ = Re major amb Fa♯ al baix (primera inversió).',
        especial=[
            'Posa ♩. = 94: la negra amb puntet és el pols, quatre per compàs.',
            'Compàs de 12/8: dotze corxeres en quatre grups de tres.',
            "Armadura d'un sostingut (Fa♯): Sol major.",
            "Comença amb una anacrusi de tres corxeres: Re, Mi, Sol, abans del c. 1.",
            "Els números de dit són de l'edició del campament, no nostres.",
            'Sense matisos ni repeticions. Barres dobles als cc. 8, 16 i 24: tres parts i un final.'],
        reto="Mantén l'esquerra tranquil·la (dues notes llargues per compàs) mentre la dreta fa les "
             "corxeres. Pots?",
        truco="L'esquerra són només quatre notes (Sol, Mi, Do, Re) i es repeteixen als cc. 1-16: "
              "aprèn-les de memòria i només et queda la dreta.",
        sabias="«Perfect» és d'Ed Sheeran i surt a l'àlbum «÷» (Divide, 2017). Va ser el número 1 "
               "de Nadal del 2017 al Regne Unit. La va escriure per a la seva parella, Cherry "
               "Seaborn.",
        qr_texto='Escolta-la i compta quatre temps grans per compàs.',
        ts=(12, 8), cuenta_titulo='Dos compassos de la peça',
        cuenta_pie='Compta 1-2-3-4: quatre temps, cadascun amb tres corxeres. A dalt, el c. 9 de '
                   "la dreta; a baix, el c. 1 de l'esquerra.",
        ritmos=[('DRETA c. 9', '3 notes llargues + 3 corxeres',
                 [{'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'q.'},
                  {'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e', 'beam': 0},
                  {'pitch': 'A4', 'dur': 'e', 'beam': 0}, {'pitch': 'G4', 'dur': 'e', 'beam': 0}],
                 AZUL, 'treble', None),
                ('ESQUERRA c. 1', 'dues notes de dos temps',
                 [{'pitch': 'G3', 'dur': 'h.'}, {'pitch': 'G3', 'dur': 'h.'}], OCRE, 'bass',
                 None)]),
    manos=dict(
        izq=[('Dues notes llargues', 'Cada compàs, dues notes de dos temps (sis corxeres cada '
                                     'una). Compta 1-2, 3-4.'),
             ('Quatre notes', 'Sol, Mi, Do, Re. Toca-les en bucle, sense mirar, fins que surtin '
                              'soles.'),
             ('Canvia a mig compàs', 'Als cc. 17-24 les dues notes del compàs són diferents: '
                                     'Mi-Do, Sol-Re.'),
             ('La baixada final', 'Al c. 25: Sol, Fa♯, Mi, Re, una per temps. Al c. 27, un Sol de '
                                  'quatre temps.')],
        der=[("L'anacrusi", "Tres corxeres: Re, Mi, Sol. Entra a l'últim temps abans del c. 1. "
                            'Compta 1-2-3-4.'),
             ('Notes llargues', 'Una negra amb puntet dura tres corxeres: compta «1-2-3» sense '
                                'córrer.'),
             ('Tres corxeres', "Grups de tres: Si-La-Sol. Toca'ls com un gronxador, tots iguals."),
             ('Llarga-curta', 'Als cc. 17-19 i 21-22: una negra i una corxera. Canta-ho primer: '
                              '«1-2, 3».')],
        tecnica=["Canell solt: l'esquerra aguanta i la dreta canta, sense picar.",
                 'Compta quatre temps grans (1-2-3-4), cadascun de tres corxeres.',
                 'Comença més lent i ves pujant fins a ♩. = 94, a poc a poc.']),
    bloques=[
        B(1, 'anacrusi + cc. 1-4', "L'entrada i el primer bucle", (0, 0),
          D('grupos', 'Un compàs de 12/8 = 4 temps · 3 corxeres cadascun',
            (4, 3, ['temps 1', 'temps 2', 'temps 3', 'temps 4'])),
          [('IZQUIERDA', "Silenci a l'anacrusi. Dues notes per compàs: Sol, Mi, Do, Re."),
           ('DERECHA', "Anacrusi: Re-Mi-Sol. Després una nota llarga i grups de corxeres."),
           ('JUNTAS', "Entra amb l'anacrusi i compta 1-2-3-4: cada nota de l'esquerra, dos "
                      "temps."),
           ('A TEMPO', '♩. = 94. Comença a la meitat. Un temps = tres corxeres.')]),
        B(2, 'cc. 5-8', 'Segona frase', (1, 1),
          D('cadena', 'El mateix bucle',
            [('Sol', False), ('Mi menor', False), ('Do', False), ('Re', True)]),
          [('IZQUIERDA', 'Sol, Mi, Do, Re un altre cop: el mateix bucle dels cc. 1-4.'),
           ('DERECHA', 'Negres i corxeres. Al c. 8: tres Re iguals (corxeres) i baixa.'),
           ('JUNTAS', 'De dos en dos compassos i, després, els quatre junts.'),
           ('OJO', "Barra doble al c. 8: s'acaba la primera part.")]),
        B(3, 'cc. 9-12', 'Tres notes llargues', (2, 2),
          D('cadena', 'El mateix bucle',
            [('Sol', False), ('Mi menor', False), ('Do', False), ('Re', True)]),
          [('IZQUIERDA', 'Sol, Mi, Do, Re: el mateix bucle, una altra vegada.'),
           ('DERECHA', 'Tres notes llargues iguals (Si-Si-Si) i després Si-La-Sol.'),
           ('JUNTAS', 'Un compàs cada cop: compta 1-2-3-4 i canvia a temps.'),
           ('OJO', 'Al c. 12, lligadura: el Si llarg i el Si curt es toquen com una sola nota.')]),
        B(4, 'cc. 13-16', 'Tanca la segona part', (3, 3),
          D('cadena', 'El mateix bucle',
            [('Sol', False), ('Mi menor', False), ('Do', False), ('Re', True)]),
          [('IZQUIERDA', 'Sol, Mi, Do, Re: quarta vegada. Ja te\'l saps!'),
           ('DERECHA', 'Cc. 13-14 com els cc. 9-10. Al c. 15 canvia el final: Re-La-Sol.'),
           ('JUNTAS', 'Cc. 13-16 de dos en dos, i després els quatre.'),
           ('OJO', 'Al c. 16: silenci de negra, Re agut i Si-La-Sol. Barra doble al final.')]),
        B(5, 'cc. 17-20', "Canvia l'ordre dels acords", (4, 4),
          D('cadena', 'Un ordre nou',
            [('Mi menor', False), ('Do', False), ('Sol', False), ('Re', True)]),
          [('IZQUIERDA', 'Dues notes per compàs: Mi-Do, Sol-Re, Mi-Do, Sol-Re.'),
           ('DERECHA', 'Ritme nou: negra i corxera. Al c. 17, un Sol agut.'),
           ('JUNTAS', "Cada compàs, dues vegades: l'esquerra canvia a mig compàs."),
           ('OJO', 'Al c. 17: Sol agut, Fa♯, Mi, Fa♯. El Fa és sostingut (armadura).')]),
        B(6, 'cc. 21-27', 'La baixada final', (5, 6),
          D('cadena', 'Cap al Sol final',
            [('cc. 21-24', False), ('c. 25: baixa de pas', False), ('c. 27: Sol llarg', True)]),
          [('IZQUIERDA', 'Cc. 21-24: Mi-Do i Sol-Re. Cc. 25-27: Sol-Fa♯-Mi-Re, Do-Re i Sol.'),
           ('DERECHA', 'Al c. 25, Si-La-Sol-Fa♯ (una per temps). Al c. 27, Sol.'),
           ('JUNTAS', 'Al c. 25 les dues mans baixen juntes, de pas.'),
           ('OJO', 'El c. 27 és un Sol de quatre temps: aguanta i deixa anar.')]),
        B(7, 'anacrusi + cc. 1-27', 'Tota la peça', (0, 6),
          D('cadena', 'Les quatre parts',
            [('cc. 1-8', False), ('cc. 9-16', False), ('cc. 17-24', False), ('cc. 25-27', True)]),
          [('IZQUIERDA', 'Tot el bucle (Sol, Mi, Do, Re) i després els acords de la 3a part.'),
           ('DERECHA', "De l'anacrusi al c. 27, per parts: 1-8, 9-16, 17-24 i 25-27."),
           ('JUNTAS', 'Cada part per separat i, després, totes seguides.'),
           ('A TEMPO', '♩. = 94 amb metrònom: comença més lent i ves pujant.')]),
    ],
    lista=["Toco l'esquerra (Sol, Mi, Do, Re) de memòria.",
           'Compto els quatre temps del 12/8 sense córrer.',
           "Entro bé amb l'anacrusi (Re, Mi, Sol).",
           'Toco els 27 compassos sense parar.',
           "La gravo amb el mòbil i me l'escolto."],
    cortes={1: [209.0, 299.8, 390.2, 480.8, 571.2, 661.0]},
    corte_titulo=114.5, fin={1: 749.0},
    burb={
        0: [('arriba', 262, 'DER', "Anacrusi: tres corxeres (Re-Mi-Sol), un temps abans del c. 1. "
                                   "L'esquerra hi calla.", 0.08),
            ('arriba', 262, 'IZQ', 'Des del c. 1: Sol, Sol, Mi, Mi, Do, Do, Re, Re. Dues notes '
                                   'llargues per compàs.', 0.55)],
        1: [('abajo', 330, 'OJO', "Barra doble al c. 8: s'acaba la primera part. Al c. 8, tres Re "
                                  'iguals i baixa.', 0.85)],
        2: [('arriba', 262, 'DER', 'Tres notes llargues iguals (Si-Si-Si) i després Si-La-Sol. '
                                   'Canta-ho!', 0.3),
            ('abajo', 330, 'OJO', 'Al c. 12, lligadura entre dos Si: toca el primer i deixa-lo '
                                  'sonar.', 0.85)],
        3: [('arriba', 330, 'AMB', 'Cc. 13-14 com els cc. 9-10. Al c. 15 canvia el final: '
                                   'Re-La-Sol.', 0.7)],
        4: [('arriba', 330, 'DER', 'Nou: un Sol agut (c. 17) i ritme de negra i corxera. Acords: '
                                   'Mi menor, Do, Sol, Re.', 0.2)],
        5: [('arriba', 330, 'DER', 'Cc. 21-22: la melodia puja fins al Sol agut. Cc. 23-24: '
                                   'tres notes llargues per compàs.', 0.3),
            ('abajo', 300, 'OJO', "Barra doble al c. 24: s'acaba la tercera part. Només en "
                                  'queden tres!', 0.85)],
        6: [('arriba', 330, 'AMB', 'Les dues mans baixen de pas: dreta Si-La-Sol-Fa♯, esquerra '
                                   'Sol-Fa♯-Mi-Re.', 0.2),
            ('abajo', 330, 'OJO', "Últim compàs: un Sol de quatre temps a les dues mans. "
                                  "Aguanta'l i somriu!", 0.85)],
    },
    marcas=[],
    misol=dict(
        manos="Aprèn l'esquerra de memòria: Sol, Mi, Do, Re. Només són quatre notes i la tens a "
              "mig camí!",
        guia="El 12/8 és un gronxador: quatre balanceigs per compàs, de tres corxeres cadascun. "
             "Compta 1-2-3-4 i deixa't bressolar.",
        pauta="Escriu un compàs de 12/8 amb quatre grups de tres corxeres. Pots fer-lo amb Sol, "
              "La i Si?"),
    pie_pauta="la clau la poses tu · copia un compàs o escriu l'escala de Sol major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ab_perfect.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
