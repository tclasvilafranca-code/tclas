# -*- coding: utf-8 -*-
"""Pieza 7 · Boig per tu (Sau), arreglo de Pilar Sanz ("Arranj. Pilar Sanz" impreso). MEDIDO sobre
   el PDF (1 pagina, imagen de baja resolucion con marca de agua de solfejos que se ignora; 26
   compases en 6 sistemas de 5, 5, 5, 5, 3 y 3): sin armadura, 4/4, sin tempo ni matices, sin
   repeticiones, corchea como figura mas corta. Armonia leida sobre el papel: empieza y acaba en
   Sol-Si (Sol mayor), con Sol-Do y La-Do en la izquierda; c. 7 Fa-Do y Sol-Do; c. 8 cuatro negras
   La-Do bajo un acorde Re-Fa# (dominante); el Fa# va escrito como alteracion (cc. 8, 17, 18, 21,
   22) y el Fa es natural en el c. 7. La derecha entra en el «y» del 2 (silencio de negra con
   puntillo). Los cc. 9-10 y 11-12 repiten los cc. 1-2; 13-14 y 24-25 repiten 5-6."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=12, slug='boig_per_tu', pdf='boig_per_t.pdf', time_sig=(4, 4),
    titulo='Boig per tu', autor='Sau · cançó catalana · arranjament de Pilar Sanz',
    kicker='Alba · peça 12 · Boig per tu', mes='Maig · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=sau+boig+per+tu',
    credito='Partitura: Sau, «Boig per tu», arranj. Pilar Sanz. Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sol major'), ('Compàs', '4/4'), ('Tempo', 'Sense indicar'),
               ('Figura curta', 'Corxera'), ('Compassos', '26')],
        total=26,
        secciones=[('A', 1, 8, 'La frase i el tancament', AZUL), ('B', 9, 15, 'Torna', OCRE),
                   ('C', 16, 23, 'Part nova · Fa♯', AZUL), ('D', 24, 26, 'Final', OCRE)],
        ideas=[('ESQUERRA', 'Dues notes llargues',
                'Una rodona de dues notes per compàs: Sol-Si, Sol-Do o La-Do. Gairebé no es '
                'mou.'),
               ('DRETA', 'Entra a la «i»',
                "Comença amb un silenci de negra amb puntet i entra a la «i» del 2n temps."),
               ('EL RITME', 'Notes llargues i lligades',
                "Negres amb puntet, notes lligades i una negra que comença a mig temps."),
               ('EL FA♯', 'Una tecla negra',
                "No hi ha armadura: el Fa♯ va escrit cada vegada (cc. 8, 17, 18, 21 i 22).")],
        especial=[
            "No porta armadura ni tempo. Comença i acaba amb l'acord de Sol: Sol major.",
            'Compàs de 4/4: quatre negres per compàs.',
            'La dreta entra a la «i» del 2: silenci de negra amb puntet i corxera.',
            'Fa♯ escrit als cc. 8, 17, 18, 21 i 22. Al c. 7 el Fa és natural.',
            "No hi ha repeticions ni cases: es toca seguit, fins al c. 26.",
            "L'esquerra canvia més als cc. 7 i 8: dos acords i després quatre negres."],
        reto="Entrar a la «i» del 2 i mantenir la negra que comença a mig temps, sense "
             'atropellar. Pots?',
        truco="Canta la melodia en veu baixa amb la lletra que coneguis: el ritme de la cançó és "
              'el de la teva mà dreta.',
        sabias="«Boig per tu» és una de les cançons més conegudes de Sau, un grup català de pop "
               'dels anys 90. La va escriure el seu cantant, Carles Sabater.',
        qr_texto='Escolta-la i marca el pols: quan entra la melodia?', ts=(4, 4)),
    manos=dict(
        izq=[('Dues notes, una rodona', 'Toca Sol-Si i aguanta quatre temps. Després Sol-Do i '
                                        'La-Do. Compta 1-2-3-4.'),
             ("L'ordre", 'Cc. 1-4: Sol-Si, Sol-Do, Sol-Si, Sol-Do. Repeteix-ho fins que et '
                         'surti sense mirar.'),
             ('Els cc. 7 i 8', 'C. 7: dos acords de dos temps, Fa-Do i Sol-Do. C. 8: quatre '
                               'negres, La-Do.'),
             ('De memòria', "Aprèn l'esquerra de memòria: gairebé tot es repeteix.")],
        der=[('Cantar abans', 'Canta o taral·leja la melodia dels cc. 1-4 abans de tocar-la.'),
             ('Entrar a la «i»', 'Silenci de negra amb puntet i entres a la «i» del 2: '
                                 'Sol-Si-Do-Re.'),
             ('Les notes llargues', 'C. 2: Re llarg, Mi lligat i Sol llarg. Respira a les '
                                    'notes llargues.'),
             ("Amb l'esquerra", 'Ajunta quatre compassos cada vegada. Si et perds, torna a una '
                                'sola mà.')],
        tecnica=['Canell solt i dits corbats: acords sense prémer.',
                 "L'esquerra sona suau i la dreta canta per sobre.",
                 'Compta 1-2-3-4 en veu alta, també als silencis.']),
    bloques=[
        B(1, 'cc. 1-5', 'La frase', (0, 0),
          D('cadena', 'Les notes del c. 1',
            [('silenci', False), ('Sol', False), ('Si', False), ('Do', False), ('Re', True)]),
          [('IZQUIERDA', 'Sol-Si, Sol-Do, Sol-Si, Sol-Do: una rodona per compàs.'),
           ('DERECHA', 'Entres a la «i» del 2: Sol-Si-Do-Re. C. 2: Re llarg, Mi lligat, Sol.'),
           ('JUNTAS', 'Els cc. 1-2 en bucle i després els cc. 3-4: són iguals.'),
           ('OJO', 'El c. 5 canvia: La-Do a l\'esquerra i Do-Do-Do-Si a la dreta. Atenció!')]),
        B(2, 'cc. 6-10', 'El tancament i la tornada', (1, 1),
          D('cadena', 'La frase es tanca',
            [('c. 7', False), ('c. 8 · acord amb Fa♯', False), ('c. 9 · torna el principi', True)]),
          [('IZQUIERDA', 'C. 6: Sol-Do llarg. C. 7: Fa-Do i Sol-Do. C. 8: quatre negres, La-Do.'),
           ('DERECHA', 'C. 6: La, Sol lligat, Mi-Sol. C. 7: dues notes alhora. C. 8: acord i '
                       'silenci.'),
           ('JUNTAS', 'Els cc. 5-8 com una sola frase; descansa al silenci del c. 8.'),
           ('OJO', 'Al c. 8 apareix el Fa♯: una tecla negra. Els cc. 9-10 són els cc. 1-2.')]),
        B(3, 'cc. 11-15', 'Torna la frase', (2, 2),
          D('cadena', "És el principi",
            [('cc. 11-12 = 1-2', False), ('c. 13 = 5', False), ('c. 14 = 6', False),
             ('c. 15 · Sol llarg', True)]),
          [('IZQUIERDA', 'Sol-Si, Sol-Do, La-Do, Sol-Do i Sol-Si: una rodona per compàs.'),
           ('DERECHA', 'Repeteix els cc. 1, 2, 5 i 6. El c. 15 acaba en Sol llarg.'),
           ('JUNTAS', 'Si saps els cc. 1-6, ja saps aquests.'),
           ('OJO', "El c. 15 és una rodona: compta-la sencera, 1-2-3-4!")]),
        B(4, 'cc. 16-20', 'La part nova', (3, 3),
          D('cadena', 'Els passos de la dreta',
            [('Re-Si-Re-Si-Re', False), ('Mi-Mi-Fa♯', False), ('Sol-Fa♯-Mi-Re-Mi', False),
             ('Re llarg', True)]),
          [('IZQUIERDA', 'Sol-Si al c. 16, Sol-Do als cc. 17-18 i Sol-Si als cc. 19-20.'),
           ('DERECHA', 'Passos petits: Re-Si-Re-Si-Re. Fa♯ als cc. 17 i 18.'),
           ('JUNTAS', 'Els cc. 16-19 i després el c. 20, que repeteix el 16.'),
           ('OJO', 'Mi-Fa♯-Sol puja i Sol-Fa♯-Mi baixa: la tecla negra va enmig.')]),
        B(5, 'cc. 21-23', 'Un altre cop', (4, 4),
          D('cadena', 'Igual que abans',
            [('c. 21 = 17', False), ('c. 22 = 18', False), ('c. 23 · tancament', True)]),
          [('IZQUIERDA', 'Sol-Do als cc. 21-22 i Sol-Si al c. 23.'),
           ('DERECHA', 'Cc. 21-22 com 17-18. C. 23: Re llarg, Sol, La, Re llarg.'),
           ('JUNTAS', 'Els tres compassos seguits, sense parar.'),
           ('OJO', 'El c. 23 prepara el final: Sol-La i torna al Re.')]),
        B(6, 'cc. 24-26', 'El final', (5, 5),
          D('cadena', 'Com els cc. 5-6',
            [('c. 24 = 5', False), ('c. 25 = 6', False), ('c. 26 · Sol llarg', True)]),
          [('IZQUIERDA', 'La-Do al c. 24, Sol-Do al 25 i Sol-Si al 26, totes llargues.'),
           ('DERECHA', 'Gairebé igual que els cc. 5-6. El c. 26 és un Sol llarg.'),
           ('JUNTAS', 'Els tres compassos seguits.'),
           ('A TEMPO', 'La peça sencera, sense parar, un cop al dia.')]),
    ],
    cortes={1: [209.8, 336.0, 452.5, 560.5, 668.5]},
    corte_titulo=100.2,
    burb={
        0: [('arriba', 300, 'DER', 'Entres a la «i» del 2n temps: Sol-Si-Do-Re. Compta '
                                   '1-2-3-4 abans d\'entrar.', 0.15),
            ('abajo', 300, 'IZQ', 'Sol-Si, Sol-Do, Sol-Si, Sol-Do: una rodona per compàs.',
             0.2)],
        1: [('arriba', 330, 'OJO', "C. 7: dos acords de dos temps. C. 8: quatre negres a "
                                   "l'esquerra i un acord amb Fa♯. Mira bé!", 0.6),
            ('abajo', 300, 'AMB', 'Els cc. 9-10 repeteixen els cc. 1-2: ja els coneixes.', 0.85)],
        2: [('arriba', 300, 'AMB', 'Els cc. 11-12 són un altre cop el principi i els cc. 13-14 '
                                   'repeteixen els cc. 5-6.', 0.2)],
        3: [('arriba', 300, 'DER', 'Part nova: Re-Si-Re-Si-Re, passos petits, sense salts.',
             0.15),
            ('abajo', 300, 'OJO', 'Fa♯ als cc. 17 i 18: la tecla negra a la dreta del Fa. '
                                  'No la oblidis!', 0.45)],
        4: [('arriba', 300, 'OJO', 'Els cc. 21-22 repeteixen els cc. 17-18: un altre cop el '
                                   'Fa♯. Ja el coneixes!', 0.3)],
        5: [('arriba', 330, 'OJO', "Final: s'assembla als cc. 5-6. L'últim Sol dura els quatre "
                                   'temps: no el deixis anar abans!', 0.9)],
    },
    marcas=[],
    misol=dict(manos="Truc: gairebé tot es repeteix. Aprèn els cc. 1-2 i ja en tens mitja peça!",
               guia="Ànim! Si canviar de bloc et costa, canta la lletra baixet: el ritme "
                    "ja el portes al cap.",
               pauta="Copia el c. 1 (Sol-Si-Do-Re) i inventa't un compàs nou en Sol major. "
                     "Pot ser el teu final!"),
    pie_pauta="la clau la poses tu · copia el c. 1 o escriu l'escala de Sol major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ba_boig_per_tu.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
