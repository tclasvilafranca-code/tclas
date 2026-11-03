# -*- coding: utf-8 -*-
"""Peça 5 · Bella ciao (cançó popular italiana; arranjament d'Anderson Miranda Fernandes, de la
   sèrie «La casa de papel»). MESURAT sobre el PDF (1 pàgina A4 vectorial, 25 compassos en 5
   sistemes de 5; el títol imprès és «BELA CIAO»): armadura d'un sostingut (Fa♯) i final en Mi:
   Mi menor; 2/4; sense caràcter ni matisos; corxera com a figura més curta (cap semicorxera).
   Barra de repetició a l'inici (c. 1) i al final del c. 16: es repeteixen els cc. 1-16 una sola
   vegada i es segueix al c. 17 (sense caselles). Dreta: melodia de corxeres i negres, silenci de
   corxera als cc. 1, 3, 5, 11, 13, 17, 19 i 21; lligadures de valor als cc. 2, 4, 10, 12, 18 i 20.
   Esquerra: silenci de compàs als cc. 1 i 17 i, la resta, dues negres per compàs en parelles
   (Mi-Si, La-Mi, Si-Fa♯; quinta o quarta segons si puja o baixa) o d'octava (Mi-Mi als cc. 13, 16 i 21); blanca final (c. 25).
   Úniques alteracions: Do♯ i Re♯ als cc. 23-24 (dreta)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_r = lambda d: {'rest': True, 'dur': d}
_n = lambda p, d, b=None: ({'pitch': p, 'dur': d} if b is None else {'pitch': p, 'dur': d, 'beam': b})

SPEC = dict(
    num=5, slug='bella_ciao', pdf='bela_ciao.pdf', time_sig=(2, 4),
    titulo='Bella ciao',
    autor="Cançó popular italiana · arranjament d'Anderson Miranda Fernandes · «La casa de papel»",
    kicker='Abril · peça 5 · Bella ciao', mes='Gener',
    yt='https://www.youtube.com/results?search_query=bella+ciao+la+casa+de+papel+piano+easy',
    credito='Partitura: «Bela Ciao», arr. Anderson Miranda Fernandes (musescore.com). '
            'Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Mi menor'), ('Compàs', '2/4'), ('Caràcter', 'No indicat'),
               ('Figura curta', 'Corxera'), ('Compassos', '25')],
        total=25,
        secciones=[('A', 1, 9, 'El tema', AZUL), ('B', 10, 16, 'Baixa i repeteix', OCRE),
                   ('C', 17, 25, 'Cap al final', AZUL)],
        ideas=[('LA DRETA', 'Frases curtes',
                'Moltes frases comencen amb un silenci de corxera i es repeteixen.'),
               ("L'ESQUERRA", 'Dues notes per compàs',
                'Parelles de notes: Mi-Si, La-Mi i Si-Fa♯. Una negra a cada temps.'),
               ('LA REPETICIÓ', 'Una barra al c. 16',
                'Toques els cc. 1-16 dues vegades i segueixes al c. 17.'),
               ('EL FINAL', 'Do♯ i Re♯',
                'Als cc. 23-24 surten dos sostinguts nous. Acaba en Mi.')],
        ideas_titulo='La peça en quatre idees',
        especial=[
            "Armadura d'un sostingut (Fa♯) i final en Mi: Mi menor.",
            'Compàs de 2/4: dos temps per compàs. No porta caràcter ni matisos.',
            'Només corxeres i negres, més unes lligadures i una blanca al final.',
            'Barra de repetició al final del c. 16: torna al c. 1 una sola vegada.',
            "L'esquerra calla un compàs sencer als cc. 1 i 17.",
            'Als cc. 23-24 surten Do♯ i Re♯: són les úniques alteracions.'],
        reto="Toca els cc. 1-16 dues vegades seguides, amb la repetició, sense aturar-te. "
             "I si la cantes alhora?",
        truco="Taral·leja la melodia abans de tocar-la. Les frases es repeteixen: n'aprens poques "
              "i valen per a tota la peça.",
        sabias="«Bella ciao» vol dir «adéu, bonica». Els partisans italians la cantaven entre "
               "1943 i 1945, i la sèrie «La casa de papel» la va fer famosa arreu del món.",
        qr_texto='Escolta-la i marca el pols amb el peu: 1-2, 1-2.',
        ts=(2, 4),
        cuenta_titulo='Com es compten el c. 1 i el c. 2',
        cuenta_pie="Dreta (c. 1): silenci de corxera i tres corxeres: «1-i-2-i». Esquerra (c. 2): "
                   "dues negres, una a cada temps.",
        ritmos=[('LA DRETA', 'c. 1 · silenci + 3 corxeres',
                 [_r('e'), _n('B3', 'e'), _n('E4', 'e', 0), _n('F#4', 'e', 0)], AZUL, 'treble',
                 'Mi menor'),
                ("L'ESQUERRA", 'c. 2 · dues negres',
                 [_n('E2', 'q'), _n('B2', 'q')], OCRE, 'bass', 'Mi menor')]),
    manos=dict(
        izq=[('Dues notes per compàs', 'Mi i Si, dues negres. Cc. 2-9: sempre Mi-Si. Compta '
                                       '«1, 2».'),
             ('Parelles de notes', 'Mi-Si, La-Mi i Si-Fa♯: a vegades puja i a vegades baixa. Mira on '
                                 'cau la mà.'),
             ('Canvis de notes', 'Cc. 10-11 i 18-19: La-Mi. Cc. 14-15 i 22-23: Si-Fa♯. La resta, '
                                 'Mi-Si.'),
             ('Els silencis', "Al c. 1 i al c. 17 l'esquerra no toca. Compta 1-2 en silenci.")],
        der=[('Taral·leja-la', 'La melodia es repeteix molt. Canta-la abans de tocar-la.'),
             ('Silenci de corxera', 'C. 1: silenci i Si-Mi-Fa♯. Compta «1-i-2-i» i entra a la '
                                    'primera «i».'),
             ('Notes lligades', 'Cc. 2 i 4: Sol i Mi lligat a Mi. El Mi es toca un sol cop i '
                                "s'aguanta."),
             ('Do♯ i Re♯', 'Cc. 23-24: dues tecles negres noves. Busca-les abans de tocar.')],
        tecnica=['Canell solt i dits corbats.',
                 "La dreta canta; l'esquerra acompanya més fluix.",
                 'Compta «1-i-2-i» en veu alta i no paris a la repetició.']),
    bloques=[
        B(1, 'cc. 1-5', 'El tema', (0, 0),
          D('grupos', 'Compta: 1-i-2-i', (2, 2, ['1 i', '2 i'])),
          [('IZQUIERDA', 'C. 1: silenci. Cc. 2-5: Mi i Si, una negra cada un.'),
           ('DERECHA', 'C. 1: silenci, Si, Mi, Fa♯. C. 2: Sol i Mi lligat a Mi.'),
           ('JUNTAS', 'Dos compassos cada cop: 1-2 i 3-4. Després el c. 5.'),
           ('OJO', "Armadura: un sostingut. Tots els Fa són Fa♯, també els de l'esquerra.")]),
        B(2, 'cc. 6-10', 'Baixa i puja', (1, 1),
          D('cadena', 'El camí del bloc',
            [('Sol Fa♯ Mi', False), ('Si Si', False), ('Do Do', True)]),
          [('IZQUIERDA', 'Cc. 6-9: Mi-Si. C. 10: canvia a La-Mi.'),
           ('DERECHA', 'Cc. 6-7: Sol, Fa♯, Mi. C. 8: Si, Si. C. 9: Si, Si, La, Si.'),
           ('JUNTAS', 'De dos en dos: 6-7 i 8-9. Després el c. 10.'),
           ('A TEMPO', 'Pols suau. El c. 8 són dues negres: una nota a cada temps.')]),
        B(3, 'cc. 11-15', 'La melodia baixa', (2, 2),
          D('cadena', 'Baixant per graus',
            [('Do Si La', False), ('Si La Sol', False), ('Fa♯', True)]),
          [('IZQUIERDA', 'Cc. 11-13: La-Mi, Mi-Si, Mi-Mi. Cc. 14-15: Si-Fa♯.'),
           ('DERECHA', 'Cc. 11 i 13: silenci i tres corxeres. Cc. 14-15: negres.'),
           ('JUNTAS', 'Primer els cc. 11-12, després el 13, i els cc. 14-15.'),
           ('OJO', "Fa♯ a les dues mans (cc. 14-15): l'armadura val per a totes dues.")]),
        B(4, 'cc. 16-20', 'La repetició', (3, 3),
          D('cadena', 'El recorregut',
            [('cc. 1-16', False), ('↩ c. 1', False), ('cc. 1-16', False), ('c. 17 →', True)]),
          [('IZQUIERDA', 'C. 16: Mi alt i Mi baix. C. 17: silenci. Cc. 18-19: La-Mi. C. 20: Mi-Si.'),
           ('DERECHA', 'C. 16: Mi de 2 temps. C. 17: silenci i Si-La-Si. C. 19: Mi-Re-Do.'),
           ('JUNTAS', 'Dos compassos cada cop: 17-18 i 19-20.'),
           ('OJO', 'Barra al final del c. 16: torna al c. 1 i toca els cc. 1-16 un cop més.')]),
        B(5, 'cc. 21-25', 'El final', (4, 4),
          D('cadena', 'Cap al Mi final',
            [('Do♯', False), ('Re♯', False), ('Mi: FINAL', True)]),
          [('IZQUIERDA', 'Cc. 21-23: Mi-Mi, Si-Fa♯, Si-Fa♯. C. 24: Mi-Si. C. 25: Mi.'),
           ('DERECHA', 'C. 23: Do♯, Re♯. C. 24: Mi, Si, Do♯, Re♯. C. 25: Mi llarg.'),
           ('JUNTAS', 'Cc. 23-25 en bucle: Do♯ i Re♯ pugen fins al Mi final.'),
           ('OJO', 'Do♯ i Re♯ són tecles negres noves. Valen fins al final del compàs.')]),
        B(6, 'cc. 1-16', 'La primera part, amb repetició', (0, 3),
          D('cadena', 'Amb la repetició',
            [('cc. 1-16', False), ('↩', False), ('cc. 1-16', True)]),
          [('IZQUIERDA', 'Del c. 1 al c. 16, de memòria.'),
           ('DERECHA', 'Del c. 1 al c. 16, sense mirar les mans.'),
           ('JUNTAS', 'Les dues mans fins a la barra de repetició i torna al c. 1.'),
           ('A TEMPO', 'Els cc. 1-16 dos cops, a pas constant i sense parar.')]),
        B(7, 'cc. 1-25', 'Tota la peça', (0, 4),
          D('cadena', 'Tota la peça',
            [('cc. 1-16', False), ('cc. 1-16', False), ('cc. 17-25', True)]),
          [('IZQUIERDA', "Repte: tota la peça només amb l'esquerra."),
           ('DERECHA', 'Tota la peça només amb la dreta, cantant-la.'),
           ('JUNTAS', 'Tota la peça amb la repetició, sense parar.'),
           ('A TEMPO', 'Pols constant i, al final, Mi llarg. Bravo!')]),
    ],
    lista=['Toco la dreta de memòria i la canto alhora.',
           'Entro bé després del silenci de corxera del c. 1.',
           'Sé quan torno al c. 1 i quan segueixo al c. 17.',
           'Toco bé els Fa♯, el Do♯ i el Re♯.',
           'Toco la peça sencera sense parar.'],
    cortes={1: [216.0, 357.0, 498.2, 639.5]}, inicio={1: 92.0},
    burb={
        0: [('arriba', 262, 'DER', 'C. 1: silenci de corxera i Si-Mi-Fa♯. Els cc. 3 i 5, igual. '
                                   'Compta «1-i-2-i».', 0.2),
            ('arriba', 262, 'IZQ', "L'esquerra calla al c. 1. Des del c. 2: Mi-Si, dues negres "
                                   'per compàs.', 0.4),
            ('abajo', 262, 'OJO', "Armadura: un sostingut. Tots els Fa són Fa♯, també els de "
                                  "l'esquerra.", 0.09)],
        1: [('arriba', 262, 'AMB', "Cc. 6-7: Sol, Fa♯, Mi a la dreta; Mi-Si a l'esquerra. C. 8: "
                                   'dues negres.', 0.2),
            ('abajo', 262, 'DER', 'C. 10: el 2n Do va lligat al 3r: es toca un cop i dura una '
                                  'corxera i una negra.', 0.88)],
        2: [('arriba', 262, 'DER', 'Cc. 11 i 13: silenci de corxera i tres corxeres que baixen: '
                                   'Do-Si-La i Si-La-Sol.', 0.15),
            ('abajo', 262, 'IZQ', 'Cc. 14-15: Si-Fa♯ a baix. Recorda: el Fa és Fa♯.', 0.72)],
        3: [('arriba', 262, 'AMB', 'Barra de repetició al final del c. 16: torna al c. 1 i '
                                   'repeteix-ho tot. Només un cop!', 0.23),
            ('abajo', 262, 'OJO', "C. 17: l'esquerra calla tot el compàs. Compta 1-2 i entra al "
                                  'c. 18.', 0.37)],
        4: [('arriba', 262, 'DER', 'Cc. 23-24: Do♯ i Re♯. Un sostingut val fins al final del '
                                   'compàs.', 0.5),
            ('abajo', 262, 'AMB', "C. 25: Mi llarg a les dues mans. Aguanta'l i deixa anar. "
                                  'Final!', 0.93)],
    },
    misol=dict(
        manos="Canta la melodia mentre toques: els dits la segueixen sols i l'esquerra no et "
              "distreu.",
        guia="Si t'equivoques, torna a l'inici del bloc, no al principi de la peça. Tu pots!",
        pauta="Escriu l'escala de Mi menor: Mi, Fa♯, Sol, La, Si, Do, Re, Mi. Només un "
              "sostingut!"),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu l'escala de Mi menor (amb el Fa♯)")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_bella_ciao.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
