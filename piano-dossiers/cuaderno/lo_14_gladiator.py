# -*- coding: utf-8 -*-
"""Peça 14 · Honor Him (Gladiator, Hans Zimmer · versió fàcil, MuseScore).
   MESURAT sobre el PDF (1 pàgina, A4; notes pintades amb colorear_notas.py): armadura de TRES SOSTENITS
   (Fa♯, Do♯, Sol♯), 3/4, ♩ = 70, mp al c. 1, mf al c. 16 i mp al c. 25; regulador (crescendo) als cc. 15-16 i
   un altre al c. 24; 26 compassos en 5 sistemes (6+5+5+5+5). Cc. 1-2: silenci de compàs sencer a la dreta;
   l'esquerra aguanta Fa♯2 (blanca amb puntet lligada). La melodia entra al c. 3 (Do♯ Fa♯ La, tres negres).
   Esquerra: blanques amb puntet i lligadures; arcs de fraseig als cc. 15-19. Final: Fa♯ a les dues mans (Fa♯ menor).
   Figura curta: negra. Notes pintades per lletra: Do, Fa i Sol sonen amb ♯ per l'armadura."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}

SPEC = dict(
    num=14, slug='gladiator', pdf='gladiator.pdf', time_sig=(3, 4),
    titulo='Honor Him (Gladiator)',
    autor='Hans Zimmer · versió fàcil',
    kicker=kick(14, 'Honor Him (Gladiator)'), mes=MESES[14],
    yt=yt('honor him gladiator hans zimmer piano easy'),
    credito='Partitura: versió fàcil (MuseScore). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', '3 sostenits'), ('Compàs', '3/4'), ('Tempo', '♩ = 70'),
               ('Figura curta', 'Negra'), ('Compassos', '26')],
        total=26,
        secciones=[('A', 1, 6, 'Introducció: la veu entra', AZUL),
                   ('B', 7, 11, 'La melodia, més oberta', OCRE),
                   ('C', 12, 16, 'Creix fins al mf', AZUL),
                   ('D', 17, 26, 'Torna i s\'apaga', OCRE)],
        ideas=[('LES ALTERACIONS', 'Tres sostenits sempre',
                "Al començament de cada línia hi ha tres ♯: Fa♯, Do♯ i Sol♯. Tots els Fa, Do i Sol d'aquesta peça són tecles negres."),
               ('LA MELODIA', 'Lenta i cantable',
                'Notes llargues (blanques i blanques amb puntet) i petits salts. Canta-la mentre toques.'),
               ('LA MÀ ESQUERRA', 'Notes molt llargues',
                "Una nota per compàs, sovint lligada al compàs següent: el so s'allarga com una ona."),
               ('ELS MATISOS', 'Fluix i fort',
                'Comença fluix (mp), arriba a fort (mf) al c. 16 amb un crescendo, i acaba fluix (mp).')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie='Atenció: en aquesta peça els colors de Do, Fa i Sol són tecles NEGRES (♯). ' + COLORS,
        especial=[
            'Armadura de tres sostenits: tots els Fa, Do i Sol són Fa♯, Do♯ i Sol♯.',
            "La peça acaba en Fa♯, per això és en Fa♯ menor (el relatiu menor de La major).",
            "Tempo: negra = 70, lent i solemne. Compàs de 3/4.",
            'Matisos: mp al c. 1 i al c. 25, mf al c. 16, amb un crescendo als cc. 15-16.',
            "Cc. 1-2: la mà dreta descansa dos compassos sencers: l'esquerra comença sola."],
        reto='Toca la peça tota seguida, mantenint la veu lenta i els matisos: mp, crescendo, mf, mp.',
        truco="Posa les mans sobre les tecles negres abans de començar: sentiràs la forma de la tonalitat (3 sostenits).",
        sabias="És de la banda sonora de Gladiator (2000), de Hans Zimmer. «Honor Him» vol dir «honra'l».",
        qr_texto='Escolta-la en silenci, com si fos al cinema.',
        ts=(3, 4),
        cuenta_titulo='Com es compta el 3/4',
        cuenta_pie="Una blanca amb puntet dura tot el compàs: «1-2-3». Tres negres: «1, 2, 3». Aquí només el ritme.",
        ritmos=[('TRES NEGRES', '3/4 · 1 · 2 · 3',
                 [_q('B4'), _q('B4'), _q('B4')], OCRE, 'treble', None),
                ('BLANCA AMB PUNTET', '3/4 · 1-2-3',
                 [{'pitch': 'B4', 'dur': 'h.'}], AZUL, 'treble', None),
                ('BLANCA + NEGRA', '3/4 · 1-2 · 3',
                 [{'pitch': 'B4', 'dur': 'h'}, _q('B4')], VERDE, 'treble', None)]),
    manos=dict(
        izq=[('Fa♯ llarg', "Cc. 1-2: el Fa♯ greu (tecla negra) lligat, tres temps més tres temps. Una sola nota!"),
             ('Re i Mi', 'Cc. 3-6: Re, Mi... notes llargues, una per compàs. Compta «1-2-3».'),
             ('Lligadures', "Els arcs que uneixen dues notes: la segona no es torna a tocar, només s'aguanta."),
             ('Arcs llargs', 'Als cc. 15-19 hi ha arcs de fraseig: toca amb una sola idea musical.')],
        der=[('Silenci de compàs', 'Cc. 1-2: no toques res, compta «1-2-3» dos cops.'),
             ('Do♯ Fa♯ La', 'C. 3: tres negres que pugen: vermell, verd, lila (amb ♯ als dos primers).'),
             ('La i Si', "Cc. 4-6: la melodia baixa i torna a pujar: Si, La, Sol, Si Do Mi."),
             ('El regulador', "Al c. 15: el sentit puja: crescendo fins al mf del c. 16.")],
        tecnica=['Pes del braç, no cop de dit: el so ha de ser ple i dolç.',
                 'Els tres sostenits: primer toca la tecla negra i després la resta.',
                 'Respira cada dues bars: com si cantessis.']),
    bloques=[
        B(1, 'cc. 1-6', 'La veu entra', (0, 0),
          D('cadena', 'Silenci → melodia',
            [('cc. 1-2: només esq.', False), ('c. 3: Do♯ Fa♯ La', False), ('cc. 4-6', True)]),
          [('IZQUIERDA', 'Fa♯ greu lligat (cc. 1-2), després Re i Mi. Notes llargues, mp.'),
           ('DERECHA', 'Cc. 1-2 silenci. C. 3: Do♯ Fa♯ La. Cc. 4-6: Si, La, Sol i Si Do Mi.'),
           ('JUNTAS', 'Entra la dreta al c. 3, amb l\'esquerra aguantant. Compta «1-2-3».'),
           ('OJO', "Tres sostenits (Fa♯, Do♯, Sol♯): tots els Fa, Do i Sol són tecles negres.")]),
        B(2, 'cc. 7-11', 'La melodia, més oberta', (1, 1),
          D('cadena', 'Notes llargues',
            [('cc. 7-8', False), ('cc. 9-10', False), ('c. 11', True)]),
          [('IZQUIERDA', 'Fa♯ amb puntet i, després, notes llargues lligades.'),
           ('DERECHA', 'Cc. 7-11: una melodia lenta, amb Si, La, Mi, Fa♯. Mira els colors i els ♯.'),
           ('JUNTAS', 'Una nota de l\'esquerra per cada dues de la dreta. Compta sempre 1-2-3.'),
           ('A TEMPO', 'Negra = 70: ni més ràpid, ni més lent.')]),
        B(3, 'cc. 12-16', 'Creix fins al mf', (2, 2),
          D('cadena', 'Cap al mf',
            [('cc. 12-14', False), ('cc. 15-16: crescendo', False), ('c. 16: mf', True)]),
          [('IZQUIERDA', 'Notes llargues amb arcs. Al c. 15 puja, de Do♯ a La.'),
           ('DERECHA', 'Cc. 12-14: notes llargues. C. 15: Do♯ Fa♯ La amb crescendo. C. 16: Mi, La i Si (mf).'),
           ('JUNTAS', 'Les dues mans pugen juntes: més so cada cop, fins al mf.'),
           ('OJO', 'Crescendo (<): fort poc a poc. Mf vol dir «mig fort».')]),
        B(4, 'cc. 17-26', 'Torna i s\'apaga', (3, 4),
          D('cadena', 'Del mf al final',
            [('cc. 17-21', False), ('cc. 22-24', False), ('cc. 25-26: mp → final', True)]),
          [('IZQUIERDA', 'Notes llargues, lligades. Al final: Fa♯ i descansa.'),
           ('DERECHA', 'Cc. 17-21: la melodia torna. Cc. 22-24: Fa♯, La, Si. Cc. 25-26: Fa♯ llarg.'),
           ('JUNTAS', 'Les dues mans fins al Fa♯ final. Deixa que soni fins a quedar en silenci.'),
           ('OJO', 'Al c. 25 hi ha mp (mig fluix): vas baixant el volum fins a acabar.')]),
    ],
    lista=['Sé que els tres sostenits afecten Fa, Do i Sol.',
           "Toco l'esquerra sola amb les lligadures ben fetes.",
           'Faig el crescendo dels cc. 15-16 i arribo al mf.',
           'Mantinc el tempo (negra = 70) tota la peça.',
           'Toco els 26 compassos sense parar.'],
    cortes={1: [233.5, 371.0, 516.0, 654.5]}, inicio={1: 97}, fin={1: 790},
    burb={
        0: [('arriba', 262, 'OJO', 'Tres sostenits: Fa♯, Do♯ i Sol♯. Tots els Fa, Do i Sol són tecles negres!', 0.1),
            ('arriba', 262, 'DER', 'La dreta entra al c. 3: Do♯ Fa♯ La, tres negres que pugen.', 0.38)],
        1: [('arriba', 262, 'IZQ', 'Notes llargues lligades: el so s\'allarga com una ona.', 0.2)],
        2: [('arriba', 262, 'OJO', 'Crescendo als cc. 15-16: tocar cada cop més fort fins al mf.', 0.7)],
        3: [('arriba', 262, 'AMB', 'Torna la melodia: mateixes notes, un altre caràcter.', 0.3)],
        4: [('arriba', 262, 'OJO', 'Al final, mp i Fa♯ llarg: deixa que el so s\'esvaeixi.', 0.7)],
    },
    misol=dict(
        manos="Una nota llarga és com respirar: entra l'aire (prem) i surt a poc a poc (aguanta).",
        guia="Els tres sostenits són com tres «candaus» a l'armadura: ja saps què has de recordar!",
        pauta="Dibuixa un crescendo («<») i un diminuendo («>») sota dues notes que tu triïs."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu els tres sostenits i pinta les notes")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_gladiator.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
