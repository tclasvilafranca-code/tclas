# -*- coding: utf-8 -*-
"""Peça 12 · Piano Man (Billy Joel · versió fàcil «Simplified version from SimplyPiano», MuseScore).
   MESURAT sobre el PDF (2 pàgines, A4; notes pintades amb colorear_notas.py): sense armadura, 3/4, ♩ = 178,
   unes 62 compassos: pàg. 1 en 5 sistemes (cc. 1-11, 12-22, 23-34, 35-47, 48-59) i pàg. 2 en 1 sistema
   (cc. 60-62). Nota impresa al sistema 2: «10 real song compasses». Dreta: melodia de negres, blanques i
   negres amb puntet (motius Do Do Do, Do° Re, Re°, Mi Fa, Sol° Sol...). Esquerra: acords de dues notes de
   blanca amb puntet (Do3+Sol3, Fa3+La3) i silencis de compàs. Final: Fa Mi Do, Do (blanca amb puntet) i silenci."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}

SPEC = dict(
    num=12, slug='pianoman', pdf='pianoman.pdf', time_sig=(3, 4),
    titulo='Piano Man',
    autor='Billy Joel · versió fàcil (SimplyPiano)',
    kicker=kick(12, 'Piano Man'), mes=MESES[12],
    yt=yt('piano man billy joel piano easy'),
    credito='Partitura: versió simplificada (MuseScore). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense armadura'), ('Compàs', '3/4'), ('Tempo', '♩ = 178'),
               ('Figura curta', 'Corxera'), ('Compassos', '62')],
        total=62,
        secciones=[('A', 1, 11, 'Primera frase', AZUL),
                   ('B', 12, 34, 'Segona frase i repetició', OCRE),
                   ('C', 35, 47, 'Part central', AZUL),
                   ('D', 48, 62, 'Torna el tema i final', OCRE)],
        ideas=[('LA MELODIA', 'Notes repetides',
                'Moltes frases comencen amb la mateixa nota repetida (Do Do Do, Sol Sol…). Aprèn la frase i la repeteixes.'),
               ("L'ESQUERRA", 'Quasi sempre descansa',
                'Només toca un acord de tres temps de tant en tant: Do+Sol o Fa+La.'),
               ('EL TEMPO', 'Ràpid: 178 per minut',
                'La partitura diu ♩ = 178: molt ràpid, però la música és senzilla. Comença lent!'),
               ('LA LLARGADA', '62 compassos',
                'És la peça més llarga fins ara. Divideix-la en cinc parts i aprèn-ne una cada dia.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            'No hi ha armadura ni alteracions: només notes blanques del piano.',
            'Compàs de 3/4: «1-2-3». La partitura diu ♩ = 178 (negra = 178): molt ràpid; comença lent.',
            "Cap al c. 18 hi ha una nota escrita: «10 real song compasses». És un avís de l'edició, no s'ha de tocar.",
            "L'esquerra toca acords de dues notes (Do+Sol, Fa+La) i descansa quasi sempre.",
            'La peça és molt llarga: 62 compassos repartits en dues pàgines.'],
        reto='Toca els 62 compassos de memòria: el cervell és capaç de recordar totes les frases repetides!',
        truco="Divideix-la en parts: aprèn la frase, la repeteixes, i després la següent. Ja veuràs que són quasi iguals.",
        sabias="«Piano Man» és de Billy Joel (1973) i parla d'un pianista que toca en un bar cada vespre.",
        qr_texto='Escolta-la i canta amb la partitura al davant.',
        ts=(3, 4),
        cuenta_titulo='Com es compta el 3/4',
        cuenta_pie="Tres negres: «1, 2, 3». Una blanca + negra: «1-2, 3». Una blanca amb puntet: «1-2-3». Aquí només el ritme.",
        ritmos=[('TRES NEGRES', '3/4 · c. 6 · 1 · 2 · 3',
                 [_q('B4'), _q('B4'), _q('B4')], OCRE, 'treble', None),
                ('BLANCA + NEGRA', '3/4 · 1-2 · 3',
                 [{'pitch': 'B4', 'dur': 'h'}, _q('B4')], AZUL, 'treble', None),
                ("ACORD DE BLANCA AMB PUNTET", '3/4 · mà esquerra · 1-2-3',
                 [{'pitches': ['C3', 'G3'], 'dur': 'h.'}], VERDE, 'bass', None)]),
    manos=dict(
        izq=[('Do+Sol', 'Dos dits alhora (5 i 1): dura tot el compàs. Premeu i compteu 1-2-3.'),
             ('Fa+La', 'Un altre acord de dues notes: dit 5 al Fa i dit 2 a la La, tots dos alhora.'),
             ('Els silencis', 'Quan l\'esquerra descansa, deixa la mà sobre el teclat, relaxada.'),
             ('Una nota sola', 'En alguns compassos: La La o Fa Mi Re Do: baixa de pas.')],
        der=[('Fa, Sol, Sol Fa Mi', 'La frase del principi: negra amb puntet i dos temps llargs.'),
             ('Do Do Do', 'Tres negres iguals: dit 1 al Do, tres cops. Compta 1-2-3.'),
             ('Do° Re i Re°', 'Una blanca + negra i una blanca: compta 1-2 / 3.'),
             ('Les corxeres', 'Algunes frases tenen corxeres: Fa Mi. Són el doble de ràpides!')],
        tecnica=['Comença lent: ♩ = 90 i puja de mica en mica.',
                 'Canta la lletra: «Sing us a song, you\'re the piano man».',
                 "Quan hi hagi silencis, compta'ls: el cervell els recorda."]),
    bloques=[
        B(1, 'cc. 1-11', 'Sing us a song', (0, 0),
          D('cadena', 'Primera frase',
            [('cc. 1-4: Fa Sol Fa Mi', False), ('cc. 5-7: Do Do Do', False), ('cc. 8-11: Re Mi Fa Sol', True)]),
          [('IZQUIERDA', 'Do+Sol al c. 2, Fa+La al c. 6, Do+Sol al c. 10. Molt pocs acords!'),
           ('DERECHA', 'Cc. 1-4: Fa, Sol Sol, Sol Fa Mi. Cc. 5-7: Do Do Do. Cc. 8-11: Re i Mi Fa Sol.'),
           ('JUNTAS', 'Una mà després de l\'altra: la dreta fa la melodia, l\'esquerra només els acords.'),
           ('A TEMPO', 'Comença lent. Quan et surti, accelera de mica en mica fins al ♩ = 178.')]),
        B(2, 'cc. 12-34', 'La segona frase i la repetició', (1, 2),
          D('cadena', 'Frases iguals i diferents',
            [('cc. 12-22', False), ('cc. 23-34', True)]),
          [('IZQUIERDA', 'Do+Sol, La, La, Do+Sol, Fa+La... Acords i descans.'),
           ('DERECHA', 'Torna la mateixa melodia dels cc. 1-11 (cc. 12-22). Al c. 23: Do Do Do, Do° Re...'),
           ('JUNTAS', 'Quan canvia l\'acord, canvia la melodia: mira els colors.'),
           ('OJO', 'Hi ha un text escrit, «10 real song compasses»: és un avís de l\'edició, no s\'ha de tocar.')]),
        B(3, 'cc. 35-47', 'La part central', (3, 3),
          D('cadena', 'Una part nova',
            [('cc. 35-40: La La Si Do', False), ('cc. 41-47', True)]),
          [('IZQUIERDA', 'Quasi sempre silenci. Només Fa, Mi, Re, Do al final.'),
           ('DERECHA', 'Cc. 35-40: La° i La Si Do, Si La: nova melodia amb La i Si. Mira els colors!'),
           ('JUNTAS', 'Al final de la part, l\'esquerra baixa: Fa Mi Re Do.'),
           ('OJO', 'Aquí hi ha La i Si (lila i gris): notes noves per a la dreta.')]),
        B(4, 'cc. 48-62', 'Torna el tema i final', (4, 5),
          D('cadena', 'De tornada a casa',
            [('cc. 48-56', False), ('cc. 57-59', False), ('cc. 60-62: final', True)]),
          [('IZQUIERDA', 'Fa+La, Sol+Do, La La... i al final Do+Sol llarg.'),
           ('DERECHA', 'El tema del principi: Sol° Fa Mi, Fa Mi Do... Al final: Fa Mi Do i Do llarg.'),
           ('JUNTAS', 'Les dues mans fins al final. Deixa sonar el Do final tres temps.'),
           ('A TEMPO', 'Toca tota la peça: 62 compassos. Quan acabis, estàs de festa!')]),
    ],
    lista=['Toco la melodia del principi (cc. 1-11) de memòria.',
           'Sé on van els acords Do+Sol i Fa+La.',
           'Toco la part central (cc. 35-47) amb La i Si.',
           'Mantinc el pols de 3/4 sense parar.',
           'Toco els 62 compassos sencers.'],
    cortes={1: [215.0, 356.0, 497.0, 638.0], 2: []}, inicio={1: 81, 2: 45}, fin={1: 775, 2: 160},
    burb={
        0: [('arriba', 262, 'DER', 'La melodia comença amb Fa i Sol Sol. Compta «1-2-3».', 0.1),
            ('arriba', 262, 'IZQ', 'Do+Sol: l\'esquerra marca amb un acord de dues notes.', 0.3)],
        1: [('arriba', 262, 'AMB', 'Torna la mateixa música: ja la coneixes!', 0.2)],
        2: [('arriba', 262, 'OJO', '«10 real song compasses» és un text de l\'edició: no s\'ha de tocar ni llegir en veu alta.', 0.2)],
        3: [('arriba', 262, 'DER', 'Part nova: La i Si (lila i gris). Les notes pugen.', 0.15)],
        4: [('arriba', 262, 'DER', 'Torna el tema del principi. És el final!', 0.15),
            ('arriba', 262, 'IZQ', 'Al final, Do+Sol llarg: deixa que soni.', 0.85)],
        5: [('arriba', 262, 'OJO', 'Últims tres compassos: Fa Mi Do, Do llarg i silenci. Acabes!', 0.3)],
    },
    misol=dict(
        manos="Comença lent i no et rendeixis: les cançons llargues s'aprenen frase a frase.",
        guia="Si una frase es repeteix, no l'has d'aprendre dues vegades. Mira quins compassos són iguals!",
        pauta="Escriu a la pauta la frase 'Do Do Do' tres vegades, amb els colors."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu la frase Do Do Do amb el seu color")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_pianoman.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
