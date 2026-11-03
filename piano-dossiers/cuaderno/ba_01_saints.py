# -*- coding: utf-8 -*-
"""Peça 1 · Oh, When the Saints (arr. Gilbert DeBenedetti, Gradimi, «Primer Level»).
   MESURAT sobre el PDF (1 pàgina, carta; original en blanc i negre): sense armadura,
   4/4, «Lively», 17 compassos escrits en 4 sistemes (4+4+4+5): una ANACRUSI de 3 negres (Do Mi Fa,
   dit 1-3-4) abans del c. 1, 16 compassos i un últim compàs d'un sol temps (Do esquerra) que
   completa l'anacrusi. Dreta: frase Do Mi Fa + Sol llarg (rodona) al principi; Do Mi Fa al c. 2,
   Sol blanca + Mi blanca; Do blanca + Mi blanca; Re rodona; Mi Re; Do blanques; Mi Sol Sol; Sol Fa;
   Mi Fa; Sol Mi; Re Re; Do rodona. Esquerra: Do3 repetit (dit 5) amb silencis de negra, Sol3 (dit 1)
   ×3 al c. 7, Sol3 blanca, Fa3 (dit 2), Sol3 rodones i Do Do Do Do final. Silencis de negra i blanca."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}

SPEC = dict(
    num=1, slug='saints', pdf='saints.pdf', time_sig=(4, 4),
    titulo='Oh, When the Saints',
    autor='Espiritual tradicional · arr. Gilbert DeBenedetti',
    kicker='Alba · peça 1 · Oh, When the Saints', mes=MESES[1],
    yt=yt('oh when the saints go marching in piano easy'),
    credito='Partitura: arr. Gilbert DeBenedetti (gradimi.com). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense alteracions'), ('Compàs', '4/4'), ('Caràcter', '«Lively» (viu)'),
               ('Figura curta', 'Negra'), ('Compassos', '16 + anacrusi')],
        total=16,
        secciones=[('A', 1, 7, '«Oh, when the saints…»', AZUL),
                   ('B', 8, 11, '«Lord, I want to be…»', OCRE),
                   ('A', 12, 16, '«When the saints…»', AZUL)],
        ideas=[('LA FRASE', 'Curtes i llarga',
                'La frase comença amb tres notes curtes (Do Mi Fa) i acaba amb una nota llarga.'),
               ('ELS SILENCIS', 'La música també calla',
                'Hi ha silencis de negra i de blanca. Compta-los: hi són per respirar.'),
               ("L'ESQUERRA", 'Do Do Do… i canvia',
                'Repeteix Do tres cops, després Sol, i al final Fa i altra vegada Do.'),
               ("L'ANACRUSI", 'Entra abans',
                "La cançó comença amb tres notes abans del primer compàs. L'últim compàs només té un temps.")],
        ideas_titulo='La peça en quatre idees',
        ideas_pie='',
        especial=[
            'No hi ha cap alteració: només notes blanques del piano.',
            "Comença amb anacrusi: tres negres (Do Mi Fa) abans del c. 1. L'últim compàs té un sol temps i la completa.",
            'Hi ha molts silencis de negra i de blanca: compta-los sempre.',
            'La partitura diu «Lively»: viu i alegre, però sense córrer.',
            "No hi ha repeticions escrites, però la frase d'entrada es repeteix quatre vegades."],
        reto='Toca tota la cançó comptant bé els silencis: en cada silenci, dius «1» en veu alta.',
        truco="Aprèn primer la frase d'entrada (Do Mi Fa Sol): apareix quatre cops en tota la cançó!",
        sabias="És un espiritual afroamericà que es va fer famós al jazz de Nova Orleans. "
               "Louis Armstrong la va gravar l'any 1938.",
        qr_texto='Escolta-la i canta amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo="Com es compta l'entrada i un compàs",
        cuenta_pie="Anacrusi: tres negres «2-3-4». Un compàs amb silenci: «1 (silenci), 2-3-4». Aquí només el ritme.",
        ritmos=[("L'ANACRUSI", '3 negres: 2 · 3 · 4',
                 [_q('B4'), _q('B4'), _q('B4')], OCRE, 'treble', None),
                ('SILENCI + 3 NEGRES', '4/4 · 1 (silenci) · 2 · 3 · 4',
                 [{'rest': True, 'dur': 'q'}, _q('B4'), _q('B4'), _q('B4')], AZUL, 'treble', None),
                ('DUES BLANQUES', '4/4 · 1-2 · 3-4',
                 [{'pitch': 'B4', 'dur': 'h'}, {'pitch': 'B4', 'dur': 'h'}], VERDE, 'treble', None)]),
    manos=dict(
        izq=[('Do, Do, Do (dit 5)', 'Posa el dit 5 al Do greu i toca tres cops, sense pressa. Descansa al primer temps.'),
             ('Sol, Sol, Sol (dit 1)', 'Al c. 7: tres Sol amb el polze. Només es mou el dit, no tot el braç.'),
             ('Les notes llargues', 'Sol i Do llargs (blanques i rodones): prem la tecla i compta, sense tallar-los abans d\'hora.'),
             ('Fa, dit 2', 'Al final del c. 11 i al c. 12 hi ha un Fa a l\'esquerra amb el dit 2.')],
        der=[('Do Mi Fa', 'Dits 1-3-4. Toca les tres notes curtes per començar la cançó.'),
             ('Sol llarg', 'Després, un Sol de quatre temps (rodona). Compta 1-2-3-4 sense moure el dit.'),
             ('Mi i Do blanques', 'Als cc. 5 i 6: dues notes de dos temps cadascuna. Compta 1-2 / 3-4.'),
             ('Mi Re Do', "A la part B baixa de pas: Mi Re, i dues Do. Els dits 3-2-1.")],
        tecnica=['Un dit per tecla: no els arrossegis.',
                 "Quan toca l'altra mà, la teva reposa sobre les tecles.",
                 'Compta 1-2-3-4 en veu alta, també dins els silencis.']),
    bloques=[
        B(1, 'anacrusi + cc. 1-3', 'Oh, when the saints', (0, 0),
          D('cadena', 'Entra abans',
            [('Do Mi Fa', False), ('Sol rodona', False), ('silenci + Do Mi Fa', False), ('Sol rodona', True)]),
          [('IZQUIERDA', 'Do Do Do (dit 5) sota la nota llarga i un Do sol al c. 2.'),
           ('DERECHA', 'Do Mi Fa (dits 1-3-4), un Sol llarg, després silenci i Do Mi Fa, Sol llarg.'),
           ('JUNTAS', 'Comença amb la dreta; entra l\'esquerra mentre aguanta el Sol llarg.'),
           ('OJO', "L'anacrusi: són tres notes soles. Compta «2-3-4» abans de començar.")]),
        B(2, 'cc. 4-7', 'Oh, when the saints go marching in', (1, 1),
          D('cadena', 'De Do Mi Fa cap al Re',
            [('Do Mi Fa', False), ('Sol Mi', False), ('Do Mi', False), ('Re rodona', True)]),
          [('IZQUIERDA', 'Do (c. 4), Do llarg (c. 5), silenci (c. 6) i Sol Sol Sol (c. 7).'),
           ('DERECHA', 'Do Mi Fa · Sol blanca + Mi blanca · Do blanca + Mi blanca · Re rodona.'),
           ('JUNTAS', 'Les dues mans entren i sortin per torns. Compta els silencis.'),
           ('OJO', 'Les blanques valen dos temps: compta 1-2 i 3-4. No les escurcis.')]),
        B(3, 'cc. 8-11', 'Lord, I want to be', (2, 2),
          D('cadena', 'Part nova',
            [('Mi Re', False), ('Do Do', False), ('Mi Sol Sol', False), ('Sol Fa', True)]),
          [('IZQUIERDA', 'Sol blanca (c. 8), Do rodona (c. 9) i Fa Fa (dit 2) al final del c. 11.'),
           ('DERECHA', 'C. 8: silenci i Mi Re. C. 9: Do blanca + Do blanca. C. 10: Mi, Sol Sol. C. 11: Sol Fa.'),
           ('JUNTAS', 'Quan una mà descansa, l\'altra canta. Mira qui toca.'),
           ('OJO', 'Part nova: les notes canvien. Mira bé la partitura!')]),
        B(4, 'cc. 12-16', 'When the saints go marching in', (3, 3),
          D('cadena', 'Tornem a casa',
            [('Mi Fa', False), ('Sol Mi', False), ('Re Re', False), ('Do rodona', True)]),
          [('IZQUIERDA', 'Fa blanca, Sol rodona, Sol rodona i Do Do Do Do per acabar.'),
           ('DERECHA', 'C. 12: Mi Fa. C. 13: Sol Mi. C. 14: Re Re. C. 15: Do rodona.'),
           ('JUNTAS', 'Les dues mans fins a la nota final. L\'últim compàs té un temps.'),
           ('A TEMPO', 'Toca tota la cançó, alegre i sense parar ni als silencis!')]),
    ],
    lista=['Sé tocar la frase Do Mi Fa Sol amb la mà dreta.',
           'Compto bé els silencis.',
           'Toco Do-Do-Do i Sol-Sol-Sol amb la mà esquerra.',
           'Entro amb l\'anacrusi (Do Mi Fa).',
           'Toco tota la cançó sense parar.'],
    cortes={1: [294.0, 423.2, 558.0]}, inicio={1: 158}, fin={1: 686},
    burb={
        0: [('arriba', 262, 'DER', "L'anacrusi: tres notes (Do Mi Fa) abans del primer compàs. Compta «2-3-4».", 0.15),
            ('arriba', 262, 'IZQ', 'Do Do Do (dit 5) sota el Sol llarg.', 0.55)],
        1: [('arriba', 262, 'DER', 'Do Mi Fa un altre cop. Després, dues blanques i un Re llarg.', 0.3),
            ('arriba', 262, 'IZQ', 'Sol Sol Sol (dit 1) al c. 7.', 0.88)],
        2: [('arriba', 262, 'DER', 'Part nova: «Lord, I want to be…». Mi Re, dues Do, Mi Sol Sol.', 0.3),
            ('arriba', 262, 'IZQ', 'Sol, Do rodona... i Fa Fa (dit 2) al final.', 0.9)],
        3: [('arriba', 262, 'AMB', 'Ja torna el final. L\'últim compàs té només un temps: el Do final de la mà esquerra.', 0.55),
            ('arriba', 262, 'OJO', 'El Do de la mà dreta és una rodona: quatre temps!', 0.45)],
    },
    misol=dict(
        manos="Dins dels silencis, compta en veu alta: el silenci també és música!",
        guia="La frase Do Mi Fa Sol surt quatre cops: aprèn-te-la molt bé i ja tens mitja cançó.",
        pauta="Escriu aquí la frase Do Mi Fa Sol amb la clau de sol."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu la frase Do Mi Fa Sol")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ba_lo_saints.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
