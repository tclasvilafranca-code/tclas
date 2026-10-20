# -*- coding: utf-8 -*-
"""Peça 12 · Per a Elisa (Für Elise), Beethoven, «Easy Ver.». MEDIDO sobre el PDF de Drive (1 pàgina
   A4, vectorial; al peu hi ha un bàner publicitari que el motor talla): 22 compassos en 5 sistemes
   (5, 5, 4, 4, 4; numeració impresa 1, 6, 11, 15, 19), 3/4, sense armadura (La menor), sense tempo
   ni caràcter escrits, sense repeticions, corxera com a figura més curta, sense digitació impresa.
   Matisos: mp (c. 1), mf (c. 10), p (c. 13), mp (c. 14), mf (c. 17), mp (c. 22); reguladors creixents
   als cc. 9 i 16 i decreixents als cc. 12 i 21. Alteracions: Re♯ (cc. 1-2, 5-6, 14-15, 18-19), becaire
   al Re (cc. 2, 6, 15, 19), Sol♯ (cc. 4, 17 a la dreta; c. 13 a l'esquerra). Dreta: c. 1 = silenci de
   blanca + 2 corxeres (Mi-Re♯); cc. 3-5, 7-8, 16-18, 20-21 = negra + silenci de corxera + 3 corxeres.
   Esquerra: silenci als cc. 1, 2, 6, 14, 15 i 19; blanca + silenci de negra als cc. 3-5, 7-13, 16-18
   i 20-21 (La, Mi, La, -, La, Mi, La, Do, Si, La, Sol♯); c. 22: acord La-Mi (blanca) + La molt greu
   (blanca amb puntet, tres línies addicionals). Els cc. 14-21 repeteixen els cc. 1-8."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=12, slug='ab_elisa', pdf='para_elisa.pdf', time_sig=(3, 4),
    titulo='Per a Elisa',
    autor='Ludwig van Beethoven · Für Elise · versió fàcil (Easy Ver.)',
    kicker='Abril · peça 12 · Per a Elisa', mes='Maig · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=fur+elise+beethoven+easy+piano+tutorial',
    credito='Partitura: «Fur Elise», Easy Ver. (còpia de Drive). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'La menor'), ('Compàs', '3/4'), ('Caràcter', 'Sense indicar'),
               ('Figura curta', 'Corxera'), ('Compassos', '22')],
        total=22,
        secciones=[('A', 1, 8, 'El tema', AZUL), ('B', 9, 13, 'La part nova', OCRE),
                   ('A', 14, 22, 'Torna el tema i final', AZUL)],
        ideas_titulo='La peça en quatre idees',
        ideas=[('EL MOTIU', 'Mi i Re♯ alternats',
                'Mi, Re♯, Mi, Re♯, Mi, Si, Re, Do: és la melodia que tothom coneix. '
                'Torna quatre cops.'),
               ('LA RESPOSTA', 'Negra i tres corxeres',
                'Un ritme que es repeteix: una negra, un silenci de corxera i tres corxeres. '
                'Surt als cc. 3, 4, 5, 7 i 8.'),
               ("L'ESQUERRA", 'Una nota i un silenci',
                'Una nota de dos temps i un silenci de negra: La, Mi, La. En sis compassos '
                'no toca.'),
               ('ELS ACORDS', 'La menor i Mi major',
                'Comença en La menor. Al c. 4 (i al 13) sona Mi major, amb Sol♯: dominant → '
                'tònica, torna a La.')],
        especial=[
            "Sense armadura: La menor. Les tecles negres surten com a alteracions (Re♯, Sol♯).",
            'Compàs de 3/4: tres negres per compàs. No hi ha tempo ni caràcter escrits.',
            "El c. 1 comença amb un silenci de blanca: la dreta entra al 3r temps.",
            "Matisos: mp, mf i p, amb reguladors als cc. 9, 12, 16 i 21.",
            "No hi ha repeticions: 22 compassos seguits. Els cc. 14-21 repeteixen els cc. 1-8.",
            "Al c. 22, l'esquerra toca un acord (La i Mi) i un La molt greu."],
        reto="Toca el motiu (Mi, Re♯, Mi, Re♯, Mi, Si, Re, Do) tres cops seguits, sense parar i "
             "sense córrer. Repte!",
        truco="Canta el motiu: «mi-re♯-mi-re♯-mi-si-re-do». Torna quatre cops: l'aprens una "
              "vegada i ja el tens quatre!",
        sabias="Beethoven la va escriure cap al 1810, però no es va publicar fins al 1867, "
               "quaranta anys després de morir ell (1827). Ningú no sap del cert qui era l'Elisa.",
        qr_texto="Escolta-la i segueix el motiu amb el dit sobre la partitura.",
        ts=(3, 4), cuenta_titulo='Dos compassos de la peça',
        cuenta_pie='Compta 1-2-3. A dalt, el c. 1 i el c. 3 de la dreta; a baix, el c. 3 de '
                   "l'esquerra.",
        ritmos=[('DRETA c. 1', 'silenci de blanca + 2 corxeres',
                 [{'rest': True, 'dur': 'h'}, {'pitch': 'E5', 'dur': 'e', 'beam': 0},
                  {'pitch': 'D#5', 'dur': 'e', 'beam': 0}], AZUL, 'treble', None),
                ('DRETA c. 3', 'negra, silenci i 3 corxeres',
                 [{'pitch': 'A4', 'dur': 'q'}, {'rest': True, 'dur': 'e'},
                  {'pitch': 'C4', 'dur': 'e'}, {'pitch': 'E4', 'dur': 'e', 'beam': 1},
                  {'pitch': 'A4', 'dur': 'e', 'beam': 1}], AZUL, 'treble', None),
                ('ESQUERRA c. 3', 'blanca + silenci de negra',
                 [{'pitch': 'A3', 'dur': 'h'}, {'rest': True, 'dur': 'q'}], OCRE, 'bass',
                 None)]),
    manos=dict(
        izq=[('Silenci i nota llarga', 'Als cc. 1-2 calla. Del 3 al 5: La, Mi, La, cada una de '
                                       'dos temps i un silenci de negra.'),
             ('Compta els silencis', "L'esquerra calla als cc. 1, 2, 6, 14, 15 i 19. Compta "
                                     '1-2-3 igualment.'),
             ('La, Mi, La, Do, Si...', 'Als cc. 7-13: La, Mi, La, Do, Si, La i Sol♯. Una nota '
                                       'per compàs. Toca-les soles.'),
             ('El final', 'Al c. 22: un acord de dues notes (La i Mi) i un La molt greu. '
                          "Aguanta'ls.")],
        der=[('El motiu', 'Mi, Re♯, Mi, Re♯, Mi, Si, Re, Do. Canta-ho i toca-ho nota a nota, '
                          'a poc a poc.'),
             ('Les tecles negres', 'Re♯ (cc. 1-2) i Sol♯ (c. 4) són tecles negres. Al c. 2 el '
                                   'Re és natural: mira el becaire.'),
             ('Negra i tres corxeres', 'Compta «1, 2-i, 3-i»: la negra, el silenci i tres '
                                       'corxeres. Surt als cc. 3, 4 i 5.'),
             ('La part nova', 'Cc. 9-12: el mateix ritme. Les negres són La, Mi, Re i Do: '
                              'llegeix-les amb calma.')],
        tecnica=['Canell solt i dits corbats: el Re♯ i el Sol♯ es toquen igual de lleugers.',
                 "La dreta canta (mp) i l'esquerra acompanya molt fluix.",
                 'Compta 1-2-3 en veu alta i no paris als silencis.']),
    bloques=[
        B(1, 'cc. 1-5', 'El tema, primera part', (0, 0),
          D('cadena', 'Del motiu a la resposta',
            [('cc. 1-2: el motiu', False), ('cc. 3-5: la resposta', True)]),
          [('IZQUIERDA', 'Silenci als cc. 1-2. Del 3 al 5: La, Mi, La, de dos temps.'),
           ('DERECHA', 'Primer els cc. 1-2: Mi, Re♯, Mi, Re♯, Mi, Si, Re, Do. Canta-ho!'),
           ('JUNTAS', "L'esquerra entra al c. 3: una nota per compàs, sense parar."),
           ('OJO', 'Al c. 1 la dreta calla dos temps i entra al tercer.')]),
        B(2, 'cc. 6-10', 'El tema torna i canvia', (1, 1),
          D('cadena', 'Cap a la part nova',
            [('motiu', False), ('resposta', False), ('part nova', True)]),
          [('IZQUIERDA', 'Silenci al c. 6. Després La, Mi, La i Do: una nota per compàs.'),
           ('DERECHA', 'Cc. 6-8: com abans. Cc. 9-10: La, Si, Do, Re i Mi, Sol, Fa, Mi.'),
           ('JUNTAS', "Cc. 6-8 junts i, després, els cc. 9-10: l'esquerra puja al Do."),
           ('OJO', 'Al c. 9, regulador creixent (<): puja cap al mf del c. 10.')]),
        B(3, 'cc. 11-14', 'La baixada', (2, 2),
          D('cadena', 'Baixa i descansa',
            [('cc. 11-12: baixa', False), ('c. 13: Si llarg', False), ('c. 14: torna', True)]),
          [('IZQUIERDA', 'Si, La i Sol♯: una nota per compàs, cada cop més greu. Al 14, silenci.'),
           ('DERECHA', 'Dos compassos que baixen i, al c. 13, un Si llarg de tres temps.'),
           ('JUNTAS', 'Cc. 11-13 junts i cada cop més fluix: arriba al p del c. 13.'),
           ('OJO', 'El c. 14 és com el c. 1: silenci de blanca i mp. Torna el tema!')]),
        B(4, 'cc. 15-18', 'Torna el tema', (3, 3),
          D('cadena', 'La mateixa música',
            [('cc. 2-5', False), ('es repeteix', False), ('cc. 15-18', True)]),
          [('IZQUIERDA', 'Silenci al c. 15. Després La, Mi, La, com als cc. 3-5.'),
           ('DERECHA', 'És la música dels cc. 2-5. Ja la saps!'),
           ('JUNTAS', 'Els quatre compassos en bucle, un compàs cada cop.'),
           ('OJO', 'Regulador creixent al c. 16 i mf al c. 17: aquí el tema sona més fort.')]),
        B(5, 'cc. 19-22', 'El final', (4, 4),
          D('cadena', 'Cap al final',
            [('cc. 19-21', False), ('La llarg', False), ('acord final', True)]),
          [('IZQUIERDA', 'Silenci al c. 19; La i Mi als cc. 20-21. Al 22, acord i La greu.'),
           ('DERECHA', 'Cc. 19-21: com els cc. 6-8. Al c. 22, un La llarg de tres temps.'),
           ('JUNTAS', 'Els cc. 19-22 junts, cada cop més suau, i acaba amb calma.'),
           ('OJO', 'Regulador decreixent al c. 21 i mp al c. 22: acaba suau.')]),
        B(6, 'cc. 1-13', 'La primera part sencera', (0, 2),
          D('cadena', 'Tres trossos seguits',
            [('cc. 1-5', False), ('cc. 6-10', False), ('cc. 11-13', True)]),
          [('IZQUIERDA', 'La, Mi, La, (silenci), La, Mi, La, Do, Si, La, Sol♯: de memòria.'),
           ('DERECHA', 'Del c. 1 al 13, cantant el motiu cada cop que torna.'),
           ('JUNTAS', 'Del c. 1 al c. 13 sense parar, a poc a poc.'),
           ('A TEMPO', 'Pas tranquil i regular: compta 1-2-3 en veu baixa.')]),
        B(7, 'cc. 1-22', 'Tota la peça', (0, 4),
          D('cadena', 'La peça sencera',
            [('cc. 1-13', False), ('cc. 14-21: el tema', False), ('c. 22: final', True)]),
          [('IZQUIERDA', 'Tota l\'esquerra. Compta els silencis: cc. 1, 2, 6, 14, 15 i 19.'),
           ('DERECHA', 'Tota la dreta, atenta als Re♯, als Sol♯ i al becaire del Re.'),
           ('JUNTAS', 'Per parts: cc. 1-13 i cc. 14-22. Després, les dues parts seguides.'),
           ('A TEMPO', 'Sencera, sense parar i amb els matisos: mp, mf i p.')]),
    ],
    lista=["Toco el motiu (Mi, Re♯, Mi, Re♯, Mi, Si, Re, Do) de memòria.",
           'Sé on van els Re♯, els Sol♯ i el becaire del Re.',
           "Compto els silencis de l'esquerra i entro a temps.",
           'Toco els 22 compassos sense parar.',
           "La gravo amb el mòbil i me l'escolto."],
    cortes={1: [213.0, 351.5, 487.2, 627.5]},
    corte_titulo=87.0, fin={1: 772.0},
    burb={
        0: [('arriba', 262, 'DER', 'El motiu: Mi, Re♯, Mi, Re♯, Mi, Si, Re, Do. Entres al 3r '
                                   'temps, després del silenci de blanca. Matís mp.', 0.15),
            ('arriba', 262, 'IZQ', 'Silenci als cc. 1-2. Al c. 3 entra el La: dos temps de nota '
                                   'i un de silenci.', 0.55)],
        1: [('arriba', 262, 'AMB', "Cc. 9-10: regulador creixent cap al mf. L'esquerra puja al "
                                   'Do.', 0.78),
            ('abajo', 300, 'OJO', 'Compte! Al c. 6 torna el motiu, amb un Re natural: fixa\'t '
                                  'en el becaire.', 0.05)],
        2: [('arriba', 262, 'DER', 'Cc. 11-12: la dreta baixa de pas. Al c. 13, un Si llarg '
                                   'de tres temps.', 0.2),
            ('arriba', 262, 'IZQ', 'Si, La i Sol♯: el Sol♯ del c. 13 és una tecla negra.', 0.7),
            ('abajo', 300, 'OJO', 'Diminuendo al c. 12 i p al c. 13. El c. 14 torna a començar '
                                  'amb mp.', 0.5)],
        3: [('arriba', 300, 'AMB', 'És la música dels cc. 2-5: ja la saps. Creix al c. 16 cap '
                                   'al mf del c. 17.', 0.4)],
        4: [('arriba', 262, 'DER', 'Cc. 19-21: com els cc. 6-8. Al c. 22, un La llarg de '
                                   'tres temps.', 0.4),
            ('abajo', 300, 'OJO', "Últim compàs: acord a l'esquerra i un La molt greu. "
                                  'Aguanta i deixa anar. Bravo!', 0.8)],
    },
    marcas=[],
    misol=dict(
        manos="Els cc. 14-21 són iguals que els cc. 1-8: aprèn-ne un tros i en tens dos!",
        guia="Un bloc cada dia. Si el motiu et surt tres cops seguits sense fallar, passa al "
             "següent. Ànim!",
        pauta="Escriu el motiu (Mi, Re♯, Mi, Re♯, Mi) a la pauta, amb el seu sostingut!"),
    pie_pauta="la clau la poses tu · copia el c. 1 o escriu l'escala de La menor")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ab_elisa.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
