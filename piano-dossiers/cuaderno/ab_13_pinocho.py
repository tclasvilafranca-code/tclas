# -*- coding: utf-8 -*-
"""Peça 13 · Cuando deseas una estrella / When You Wish Upon a Star (de «Pinotxo», Leigh Harline),
   arranjament d'A. C. Escobés (El Cuarto del Piano). MEDIDO sobre el PDF de Drive (1 pàgina A4,
   vectorial; el logotip del peu s'exclou): 17 compassos en 4 sistemes (4, 4, 5, 4; numeració impresa
   1, 5, 9, 14), 4/4, sense armadura (Do major), «Andantino» sense metrònom, matís p als cc. 1 i 9,
   negra com a figura més curta (cap corxera), sense digitació impresa. Barra de repetició al final
   del c. 16 (sense barra d'inici: torna al c. 1) i c. 17 final amb signe 8va a la dreta, línia ondulada
   (acord trencat) i canvi a clau de sol a l'esquerra (Do-Mi-Sol; la dreta, La-Do-Mi). Dreta: cc. 1 i 3 amb
   silenci de negra; c. 2 silenci de blanca + La; c. 5: quatre parelles de negres (Si-Re, La-Do, Sol-Si,
   Fa-La amb becaire). Esquerra: blanques (Sol-Do, Do♯-Re~Re, Si-Re, Re♯-Mi~Mi), c. 5 buit, c. 6 Re-Do-Si
   a partir del 2n temps, c. 7 La i Si, c. 8 Do amb puntet. Els cc. 9-16 repeteixen els cc. 1-8."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=13, slug='ab_pinocho', pdf='cuando_deseas_una_estrella_pinocho.pdf', time_sig=(4, 4),
    titulo='When You Wish Upon a Star',
    autor='Leigh Harline · de «Pinotxo» (Disney)',
    kicker='Abril · peça 13 · When You Wish Upon a Star', mes='Maig · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=when+you+wish+upon+a+star+pinocchio+piano+easy+tutorial',
    credito="Partitura: «Cuando deseas una estrella», arr. A. C. Escobés (El Cuarto del Piano). "
            'Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '4/4'), ('Caràcter', 'Andantino'),
               ('Figura curta', 'Negra'), ('Compassos', '17')],
        total=17,
        secciones=[('A', 1, 4, 'Primera frase', AZUL), ('B', 5, 8, 'Segona frase', OCRE),
                   ('A', 9, 12, 'Torna la primera', AZUL),
                   ('B', 13, 17, 'Torna la segona i final', OCRE)],
        ideas_titulo='La peça en quatre idees',
        ideas=[('LA MELODIA', 'Baixa de pas',
                'Sol-Fa-Mi, La, Si-La-Sol… Són negres i blanques. Cada frase acaba en una nota '
                'llarga.'),
               ("L'ESQUERRA", 'Notes de dos temps',
                'Blanques i negres, sempre amb calma. Als cc. 2, 4, 10 i 12 hi ha una '
                'lligadura.'),
               ('LES PARELLES', 'Dues notes juntes',
                'Als cc. 5 i 13 la dreta toca quatre parelles de negres que baixen de pas.'),
               ('EL FINAL', 'Acord trencat',
                "Al c. 17, un acord llarg: Do-Mi-Sol a l'esquerra i La-Do-Mi a la dreta, de baix "
                'a dalt.')],
        especial=[
            'Sense armadura: Do major. Hi ha alteracions: Do♯, Re♯, Fa♯ i un becaire (Fa).',
            'Compàs de 4/4. «Andantino» no té metrònom: tria un pas tranquil.',
            'Només hi ha un matís: p (suau), als cc. 1 i 9.',
            'Els cc. 1 i 3 comencen amb un silenci de negra: la dreta entra al 2n temps.',
            'Barra de repetició al final del c. 16: torna al c. 1. La 2a vegada, passa al c. 17.',
            "Al c. 17: signe 8va a la dreta, línia ondulada (acord trencat) i clau de sol a "
            "l'esquerra."],
        reto="Toca els cc. 5-8 amb les parelles de notes ben juntes: que sonin com una sola nota. "
             "Pots?",
        truco="Els cc. 9-16 són iguals que els cc. 1-8. Aprèn la meitat de la peça i ja te la saps "
              "tota!",
        sabias="Aquesta cançó surt de la pel·lícula «Pinotxo» (Disney, 1940). La música és de "
               "Leigh Harline i la lletra, de Ned Washington. Va guanyar l'Oscar a la millor "
               "cançó original.",
        qr_texto='Escolta-la i canta-la per dins amb la partitura al davant.',
        ts=(4, 4), cuenta_titulo='Un compàs de cada mà',
        cuenta_pie='Compta 1-2-3-4. A dalt, el c. 1 i el c. 5 de la dreta; a baix, el c. 1 '
                   "de l'esquerra.",
        ritmos=[('DRETA c. 1', 'silenci de negra + 3 negres',
                 [{'rest': True, 'dur': 'q'}, {'pitch': 'G4', 'dur': 'q'},
                  {'pitch': 'F4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}], AZUL, 'treble',
                 None),
                ('DRETA c. 5', 'quatre parelles de negres',
                 [{'pitches': ['B4', 'D5'], 'dur': 'q'}, {'pitches': ['A4', 'C5'], 'dur': 'q'},
                  {'pitches': ['G4', 'B4'], 'dur': 'q'}, {'pitches': ['F4', 'A4'], 'dur': 'q'}],
                 AZUL, 'treble', None),
                ('ESQUERRA c. 1', 'dues blanques',
                 [{'pitch': 'G3', 'dur': 'h'}, {'pitch': 'C4', 'dur': 'h'}], OCRE, 'bass',
                 None)]),
    manos=dict(
        izq=[('Blanques', 'Cc. 1 i 3: dues blanques (Sol-Do, Si-Re). Compta 1-2, 3-4. Els cc. 2 i '
                           '4 porten lligadura.'),
             ('Les lligadures', 'Als cc. 2 i 4 el Re i el Mi van lligats: es toquen un sol cop i '
                                'duren tres temps.'),
             ('Tecles negres', 'Do♯ (c. 2) i Re♯ (c. 4) són tecles negres. Cerca-les abans de '
                               'tocar.'),
             ('Tres negres', 'Al c. 6 calla al 1r temps i baixa: Re, Do, Si. Les mans baixen '
                             'juntes.')],
        der=[('Canta-la', 'Baixa de pas: Sol-Fa-Mi, La, Si-La-Sol. Canta-la per dins i després '
                          'toca-la.'),
             ('Entra al 2n temps', 'Els cc. 1 i 3 comencen amb un silenci de negra. Compta 1 en '
                                   'silenci.'),
             ('Parelles de notes', 'Al c. 5, dues notes juntes quatre cops. Prem-les alhora i '
                                   'baixa de pas.'),
             ('El final', 'Al c. 17, tres notes juntes (La-Do-Mi) amb 8va. Trenca l\'acord de '
                          'baix a dalt.')],
        tecnica=['Braç solt: les blanques de l\'esquerra sonen suaus, sense picar.',
                 "La dreta canta (p) i l'esquerra l'acompanya més fluix.",
                 'Compta 1-2-3-4 sense córrer: és un Andantino, un pas tranquil.']),
    bloques=[
        B(1, 'cc. 1-4', 'La primera frase', (0, 0),
          D('cadena', 'La dreta, compàs a compàs',
            [('Sol-Fa-Mi', False), ('La llarg', False), ('Si-La-Sol', False),
             ('Fa♯-Sol-Do', True)]),
          [('IZQUIERDA', 'Sol-Do, Do♯-Re, Si-Re, Re♯-Mi. Cc. 2 i 4: una negra i una nota lligada.'),
           ('DERECHA', 'Sol-Fa-Mi, La, Si-La-Sol i Fa♯-Sol-Do. Canta-ho abans!'),
           ('JUNTAS', 'Al c. 1 sona primer l\'esquerra; la dreta entra al 2n temps.'),
           ('OJO', 'Als cc. 2 i 4, el Re i el Mi lligats es toquen un sol cop.')]),
        B(2, 'cc. 5-8', 'Les parelles de notes', (1, 1),
          D('cadena', 'Cap al final de la frase',
            [('c. 5: parelles', False), ('c. 6: Sol-Fa-Mi-Re', False), ('cc. 7-8: llargues', True)]),
          [('IZQUIERDA', 'Silenci al c. 5. Al c. 6: Re-Do-Si. Cc. 7-8: La i Si, i Do llarg.'),
           ('DERECHA', 'C. 5: parelles que baixen. C. 6: Sol i Mi junts, Fa, Mi, Re.'),
           ('JUNTAS', 'Al c. 6 les mans baixen juntes: l\'esquerra entra al 2n temps.'),
           ('OJO', 'Al c. 5, el becaire del Fa: és Fa normal, sense sostingut.')]),
        B(3, 'cc. 9-13', 'Torna el principi', (2, 2),
          D('cadena', 'La mateixa música',
            [('cc. 9-12 = cc. 1-4', False), ('c. 13 = c. 5', True)]),
          [('IZQUIERDA', 'Cc. 9-12 com els cc. 1-4. Al c. 13, l\'esquerra no toca.'),
           ('DERECHA', 'La mateixa melodia i, al c. 13, les quatre parelles.'),
           ('JUNTAS', 'Toca els cc. 9-13 sense mirar els cc. 1-5. Si et perds, torna al 9.'),
           ('OJO', 'Torna el matís p (suau) al c. 9: baixa el volum un altre cop.')]),
        B(4, 'cc. 14-17', 'El final', (3, 3),
          D('cadena', 'Fins a l\'acord',
            [('cc. 14-16 = cc. 6-8', False), ('repetició', False), ('c. 17: acord', True)]),
          [('IZQUIERDA', "Cc. 14-16 com els cc. 6-8. Al c. 17: Do-Mi-Sol, en clau de sol."),
           ('DERECHA', 'Cc. 14-16 com els cc. 6-8. Al c. 17: La-Do-Mi amb el signe 8va.'),
           ('JUNTAS', 'Al c. 17, prem les notes de baix a dalt, molt ràpid, i aguanta.'),
           ('OJO', 'Barra de repetició al c. 16: torna al c. 1. La 2a vegada, passa al c. 17.')]),
        B(5, 'cc. 1-8', 'La meitat de la peça', (0, 1),
          D('cadena', 'Dues frases seguides',
            [('cc. 1-4', False), ('cc. 5-8', True)]),
          [('IZQUIERDA', 'Els cc. 1-8 de memòria: notes llargues i, al c. 6, tres negres.'),
           ('DERECHA', 'Els cc. 1-8 cantant. Que les parelles del c. 5 sonin juntes.'),
           ('JUNTAS', 'Del c. 1 al c. 8 sense parar, a poc a poc.'),
           ('A TEMPO', 'Pas tranquil i suau (p). Compta 1-2-3-4.')]),
        B(6, 'cc. 1-17', 'Tota la peça', (0, 3),
          D('cadena', 'El recorregut',
            [('cc. 1-8', False), ('cc. 9-16', False), ('torna al c. 1', False),
             ('c. 17: final', True)]),
          [('IZQUIERDA', 'Tota l\'esquerra: lligadures i acord final inclosos.'),
           ('DERECHA', 'Tota la dreta, cantant, amb les parelles i el final.'),
           ('JUNTAS', 'Els cc. 1-16, la repetició i, al final, el c. 17.'),
           ('A TEMPO', 'Sencera, amb la repetició, a pas tranquil i sense parar.')]),
    ],
    lista=['Toco la melodia de memòria, cantant-la per dins.',
           'Faig sonar juntes les parelles del c. 5.',
           'Sé que els cc. 9-16 són com els cc. 1-8.',
           'Toco els 17 compassos amb la repetició.',
           "La gravo amb el mòbil i me l'escolto."],
    cortes={1: [243.0, 262.0, 356.0, 375.0, 468.5, 487.5]},   # parelles de talls: s'omet el blanc entre sistemes
    corte_titulo=160.2, fin={1: 600.0},
    burb={
        0: [('arriba', 262, 'DER', 'Entres al 2n temps: silenci de negra i Sol-Fa-Mi. Matís p '
                                   '(suau). Andantino: pas tranquil.', 0.12),
            ('arriba', 262, 'IZQ', 'Notes de dos temps. Lligadura als cc. 2 i 4: el Re i el Mi '
                                   'es toquen un sol cop.', 0.55),
            ('abajo', 400, 'OJO', "Tecles negres: Do♯ i Re♯ a l'esquerra (cc. 2 i 4) i Fa♯ a la "
                                  'dreta (c. 4).', 0.68)],
        1: [('arriba', 262, 'DER', 'C. 5: quatre parelles de notes que baixen. Prem-les ben '
                                   'juntes!', 0.1),
            ('arriba', 262, 'AMB', "C. 6: dreta Sol-Fa-Mi-Re; l'esquerra entra al 2n temps "
                                   '(Re-Do-Si).', 0.35),
            ('abajo', 300, 'OJO', 'Becaire al Fa (c. 5): és Fa normal, no Fa♯.', 0.24)],
        2: [('arriba', 300, 'OJO', 'Torna el principi (p): els cc. 9-13 són com els cc. 1-5. '
                                   'Ja ho saps!', 0.08)],
        3: [('arriba', 440, 'OJO', 'Barra de repetició al c. 16: torna al c. 1. La 2a vegada, '
                                   'passa al c. 17.', 0.76),
            ('abajo', 470, 'AMB', 'C. 17: acord trencat (línia ondulada), de baix a dalt. 8va: '
                                  'la dreta, una octava més alta. Bravo!', 0.8)],
    },
    marcas=[],
    misol=dict(
        manos="Aquesta peça repeteix molt: els cc. 9-16 són com els cc. 1-8. Aprèn la meitat i ja "
              "la tens tota!",
        guia="Canta-la per dins mentre la toques: si la cantes, els dits troben el camí tot sols.",
        pauta="Escriu les tres primeres notes (Sol, Fa, Mi) a la pauta i inventa'n una melodia "
              "nova de 4 compassos!"),
    pie_pauta="la clau la poses tu · copia el c. 1 o escriu l'escala de Do major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ab_pinocho.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
