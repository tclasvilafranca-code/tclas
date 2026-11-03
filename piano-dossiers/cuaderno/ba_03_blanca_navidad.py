# -*- coding: utf-8 -*-
"""Peça 3 · White Christmas (Irving Berlin; versió a dues mans amb xifrat, MuseScore).
   MESURAT sobre el PDF (1 pàgina, A4): sense armadura, 4/4, sense tempo ni matisos, 31 compassos en 4 sistemes
   (cc. 1-7, 8-16, 17-23, 24-31). Xifrat imprès: C, D-, G, F, F-, G7, C7, F7. Lletra impresa. Figures: rodones,
   blanques, blanca amb puntet, negres (la més curta); cap corxera. Esquerra: un acord de tres notes en rodona per compàs
   (Do+Mi+Sol, Fa+La+Do, Sol+Si+Re, Re+Fa+La...). Dreta: c. 1 Mi (rodona); c. 2 Fa Mi Mi♭ Mi♮; c. 3 Fa; c. 4 Fa♯ Sol (puntet);
   c. 5 silenci + La Si Do; c. 6 Re Do Si La; c. 7 Sol (rodona); cc. 8-16: silenci de blanca + Do Re, Mi Mi, Mi La Sol, Do Do,
   Do Sol Fa, Mi, Fa Mi Re Do, Re, Re; cc. 17-23 = cc. 1-7; cc. 24-31: silenci + Do Re, Mi Mi, Mi La Sol, Do5, silenci + Do Re,
   Mi Mi, La i tres notes baixes, Do (rodona). Alteracions: Mi♭/Mi♮ (c. 2, 18), Fa♯ (c. 4, 20); a l'esquerra La♭ (c. 12),
   Si♭ (c. 26), Mi♭ (c. 28)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES

_q = lambda p: {'pitch': p, 'dur': 'q'}

SPEC = dict(
    num=3, slug='blanca_navidad', pdf='blanca_navidad.pdf', time_sig=(4, 4),
    titulo='White Christmas',
    autor='Irving Berlin · versió amb xifrat',
    kicker='Alba · peça 3 · White Christmas', mes=MESES[3],
    yt='https://www.youtube.com/results?search_query=white+christmas+piano+easy',
    credito='Partitura: White Christmas, I. Berlin (MuseScore). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '4/4'), ('Tempo', 'No indicat'),
               ('Figura curta', 'Negra'), ('Compassos', '31')],
        total=31,
        secciones=[('A', 1, 7, "«I'm dreaming of a white Christmas»", AZUL),
                   ('B', 8, 16, '«Where the treetops glisten»', OCRE),
                   ('A', 17, 23, 'Torna la primera frase', AZUL),
                   ('C', 24, 31, '«May your days be merry and bright»', OCRE)],
        ideas=[('LA MELODIA', 'Notes llargues',
                'La dreta toca rodones, blanques i negres, sense ritmes complicats. Es canta de seguida.'),
               ("L'ESQUERRA", 'Un acord per compàs',
                'Tres notes alhora, en rodona: quatre temps. El canvi d\'acord és el gest principal.'),
               ('EL XIFRAT', 'Les lletres sobre la pauta',
                "C = Do, D- = Re menor, F = Fa, G = Sol, F- = Fa menor, G7 = Sol amb sèptima. Diuen l'acord d'aquest compàs."),
               ('LES ALTERACIONS', 'Tecles negres puntuals',
                'Mi♭ i Mi♮ (c. 2), Fa♯ (c. 4), La♭ (c. 12), Si♭ (c. 26), Mi♭ (c. 28). Cadascun val només fins a la barra de compàs.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie='La partitura imprimeix xifrats: C = Do, D = Re, E = Mi, F = Fa, G = Sol, A = La, B = Si; «-» = menor; «7» = sèptima.',
        especial=[
            'No hi ha armadura: Do major. Però hi ha alteracions puntuals (♭, ♮, ♯) en alguns compassos.',
            'Les dues mans toquen quasi sempre notes llargues: rodones i blanques. Compta sempre quatre temps.',
            'Als cc. 1-7 i 17-23 la música és la mateixa: aprèn-la una vegada.',
            "A l'esquerra hi ha acords de tres notes; alguns porten un ♭ (cc. 12, 26 i 28).",
            'La lletra és impresa sota la melodia: pots cantar-la mentre toques.'],
        reto="Toca la melodia i l'acord alhora en cada compàs, sense perdre el pols de quatre temps.",
        truco="Aprèn primer els acords de l'esquerra com si fossin una cançó a part (Do, Do, Re menor, Sol…): la melodia et semblarà més fàcil.",
        sabias="Irving Berlin va compondre «White Christmas» perquè la cantés Bing Crosby a la pel·lícula Holiday Inn (1942). "
               "El disc de Crosby és un dels més venuts de la història.",
        qr_texto='Escolta-la i canta amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo='Com es compta el c. 1 i el c. 2',
        cuenta_pie="Una rodona: «1-2-3-4». Quatre negres: «1, 2, 3, 4». Aquí només el ritme.",
        ritmos=[('EL COMPÀS 1', '4/4 · rodona (melodia i acord)',
                 [{'pitch': 'B4', 'dur': 'w'}], OCRE, 'treble', None),
                ('EL COMPÀS 2', '4/4 · quatre negres',
                 [_q('B4'), _q('B4'), _q('B4'), _q('B4')], AZUL, 'treble', None)]),
    manos=dict(
        izq=[('Un acord de tres notes', "Dits 5, 3 i 1 (o 5, 2 i 1) alhora sobre Do-Mi-Sol. Premeu-les juntes, aguanteu quatre temps."),
             ('Canviar d\'acord', 'Els acords canvien cada compàs: mira el xifrat (C, F, G...) i mou la mà d\'un salt, sense aixecar-la molt.'),
             ('Els acords amb ♭', 'Als cc. 12, 26 i 28 hi ha una nota amb ♭: una tecla negra a l\'acord. Mira-ho abans.'),
             ('El pols', "Quan la melodia té notes curtes, l'esquerra no s'acorta: segueix una rodona per compàs.")],
        der=[('Mi, rodona', 'C. 1: un Mi de quatre temps. Compta «1-2-3-4» sense tocar res més.'),
             ('Fa Mi Mi♭ Mi♮', "C. 2: quatre negres que baixen i tornen. El Mi♭ i el Mi♮ són el truc del compàs."),
             ('Fa♯ i Sol llarg', 'C. 4: Fa♯ (tecla negra) i Sol amb puntet. Tres temps de Sol.'),
             ('La Si Do · Re Do Si La', 'Cc. 5-6: quatre negres que pugen i quatre que baixen, per graons.')],
        tecnica=['Dits arrodonits també a les notes llargues.',
                 'Canta la lletra mentre toques: la melodia ja la saps.',
                 "Mira l'acord un compàs abans de tocar-lo."]),
    bloques=[
        B(1, 'cc. 1-7', "I'm dreaming of a white Christmas", (0, 0),
          D('cadena', 'Primera frase',
            [('c. 1: Mi', False), ('c. 2: Fa Mi Mi♭ Mi♮', False), ('c. 4: Fa♯ Sol', False), ('cc. 5-7', True)]),
          [('IZQUIERDA', 'Do, Do, Re menor, Sol, Fa, Sol, Do: un acord per compàs.'),
           ('DERECHA', 'C. 1: Mi. C. 2: Fa Mi Mi♭ Mi♮. C. 3: Fa. C. 4: Fa♯ Sol. Cc. 5-7: La Si Do, Re Do Si La, Sol.'),
           ('JUNTAS', 'Compàs a compàs: acord a l\'esquerra i nota a la dreta alhora.'),
           ('OJO', 'Mi♭ i Mi♮ (c. 2) i Fa♯ (c. 4): tecles negres. Mira-les.')]),
        B(2, 'cc. 8-16', 'Where the treetops glisten', (1, 1),
          D('cadena', 'La part central',
            [('cc. 8-10', False), ('cc. 11-13', False), ('cc. 14-16', True)]),
          [('IZQUIERDA', 'Acords: Sol, Do, Do, Fa, Fa menor (La♭, c. 12), Do, Re menor, Sol, Sol7.'),
           ('DERECHA', 'Cada compàs comença amb un silenci de blanca o una nota. Mira el xifrat: G, C, F.'),
           ('JUNTAS', 'Dos o tres compassos cada cop. Compta els silencis!'),
           ('OJO', 'Al c. 12 l\'acord té un La♭ (Fa menor): tecla negra a l\'esquerra.')]),
        B(3, 'cc. 17-23', 'Torna la primera frase', (2, 2),
          D('cadena', 'Igual que els cc. 1-7',
            [('cc. 17-23', False), ('= cc. 1-7', True)]),
          [('IZQUIERDA', 'Els mateixos acords que els cc. 1-7.'),
           ('DERECHA', 'La mateixa melodia: només canvia la lletra («With every Christmas card I write»).'),
           ('JUNTAS', 'Toca-ho de memòria si pots.'),
           ('A TEMPO', 'Una mica més fort que la primera vegada: ja saps on vas.')]),
        B(4, 'cc. 24-31', 'May your days be merry and bright', (3, 3),
          D('cadena', 'El final',
            [('cc. 24-27', False), ('cc. 28-30', False), ('c. 31: Do', True)]),
          [('IZQUIERDA', 'Sol, Do, Do7 (Si♭), Fa, Fa7 (Mi♭), Do, Sol, Do.'),
           ('DERECHA', 'Cc. 24-27: Do Re, Mi Mi, Mi La Sol, Do agut. Cc. 28-31: com abans i Do final.'),
           ('JUNTAS', 'Les dues mans fins al Do final. Aguanta els quatre temps.'),
           ('OJO', 'Si♭ al c. 26 i Mi♭ al c. 28: dues tecles negres a l\'esquerra.')]),
    ],
    lista=['Sé tocar els acords de tres notes a la mà esquerra.',
           'Toco la melodia dels cc. 1-7 de memòria.',
           'Faig bé les alteracions (Mi♭, Fa♯, La♭, Si♭).',
           'Canto la lletra mentre toco.',
           'Toco els 31 compassos sense parar.'],
    cortes={1: [249.0, 404.0, 559.0]}, inicio={1: 110}, fin={1: 712},
    burb={
        0: [('arriba', 262, 'DER', "Mi (rodona), després Fa Mi Mi♭ Mi♮. «I'm dreaming of a white Christmas».", 0.1),
            ('arriba', 262, 'OJO', 'Fa♯ al c. 4: tecla negra. Mi♭ i Mi♮ al c. 2.', 0.45)],
        1: [('arriba', 262, 'AMB', 'Cada compàs comença amb un silenci de blanca i una frase curta.', 0.15),
            ('arriba', 262, 'OJO', 'La♭ a l\'esquerra al c. 12 (acord de Fa menor).', 0.55)],
        2: [('arriba', 262, 'AMB', 'Tornen els cc. 1-7. Només canvia la lletra.', 0.2)],
        3: [('arriba', 262, 'OJO', 'Si♭ al c. 26 i Mi♭ al c. 28 a l\'esquerra.', 0.4),
            ('arriba', 262, 'DER', 'Final: Do (rodona). Deixa sonar.', 0.9)],
    },
    misol=dict(manos='', guia='', pauta=''),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu els acords de Do, Fa i Sol")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ba_blanca_navidad.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
