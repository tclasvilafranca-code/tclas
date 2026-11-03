# -*- coding: utf-8 -*-
"""Peça 13 · Tetris (Korobeiniki). MEDIDO sobre el PDF de Drive de Sharifa: 3 paginas (la 3.ª en
   blanco), 24 compases en 6 sistemas de 4, sin armadura (La menor, con Sol sostenido en los
   cc. 10, 12 y 16), 4/4, sin tempo ni matices, corchea como figura mas corta.
   Derecha cc. 1-4: Mi5 | Si4 Do5 Re5 Do5 Si4 | La4 La4 Do5 Mi5 Re5 Do5 | Si4. Do5 Re5 Mi5 | Do5 La4 La4.
   Izquierda: nota grave + octava en corcheas; bajos Mi, La, Si, La | Re, Do, Si, La | La, Sol#, La, Si
   | La, Si, Do, Si. Los cc. 17-24 repiten los cc. 1-8 salvo el c. 24 (silencio de corchea, Do, La
   corchea, La, silencio)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403


def _e(p, d='q', b=None):
    ev = {'pitch': p, 'dur': d}
    if b is not None:
        ev['beam'] = b
    return ev


_MEL = [_e('E5'), _e('B4', 'e', 0), _e('C5', 'e', 0), _e('D5'), _e('C5', 'e', 1), _e('B4', 'e', 1),
        _e('A4'), _e('A4', 'e', 2), _e('C5', 'e', 2), _e('E5'), _e('D5', 'e', 3), _e('C5', 'e', 3)]
_IZQ = [_e(('E2', 'E3')[j % 2], 'e', j // 4) for j in range(8)]
_IZQ += [_e(('A1', 'A2')[j % 2], 'e', 2 + j // 4) for j in range(8)]

SPEC = dict(
    num=13, slug='tetris', pdf='copia_de_tetrix.pdf', time_sig=(4, 4),
    titulo='Tetris', autor='Korobeiniki · cançó popular russa · tema del videojoc',
    kicker='Txell · peça 13 · Tetris', mes='Juny · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=tetris+theme+korobeiniki+piano',
    credito='Partitura: Korobeiniki, tema de Tetris (Drive). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'La menor'), ('Compàs', '4/4'), ('Tempo', 'Sense indicar'),
               ('Figura curta', 'Corxera'), ('Compassos', '24')],
        total=24,
        secciones=[('A', 1, 8, 'La melodia', AZUL),
                   ('B', 9, 16, 'Notes llargues i pujada', OCRE),
                   ('A', 17, 24, 'Torna la melodia', AZUL)],
        ideas=[('LA MELODIA', 'Mi, Si, Do, Re',
                'Baixa i puja per notes veïnes. És la melodia que tothom reconeix.'),
               ('L\'ESQUERRA', 'Nota i octava',
                'Vuit corxeres per compàs: la nota greu i la mateixa, una octava més aguda, '
                'sense parar.'),
               ('LA BAIXADA', 'Re, Do, Si, La',
                'Als cc. 5-8 la nota greu baixa d\'una en una fins a arribar a La.'),
               ('SOL SOSTINGUT', 'Una tecla negra',
                'Surt als cc. 10, 12 i 16. És la nota que "demana" tornar a La menor.')],
        especial=[
            'No té armadura: és La menor, i el Sol sostingut va escrit dins el compàs.',
            'El compàs és 4/4. No porta tempo ni matisos.',
            'L\'esquerra toca vuit corxeres per compàs, del principi al final.',
            'La dreta barreja negres, corxeres, negres amb puntet (cc. 3, 6, 7), blanques '
            '(cc. 9-11, 13-14) i rodones (cc. 12 i 16).',
            'Els cc. 17-24 repeteixen els cc. 1-8; només canvia el final (c. 24).'],
        reto='Que l\'esquerra vagi com un rellotge, vuit corxeres per compàs, mentre la dreta '
             'canvia de ritme. Pots?',
        truco='Toca l\'esquerra sola fins que puguis parlar mentre toques. Després afegeix la '
              'dreta, un compàs cada vegada.',
        sabias='Korobeiniki vol dir "els buhoners" (venedors ambulants) i és una cançó popular '
               'russa sobre un poema de Nekrassov de 1861. El Tetris el va crear Aleksei '
               'Pajitnov el 1984 i la versió de Game Boy (1989) el va fer famós arreu.',
        qr_texto='Escolta-la amb la partitura davant i segueix l\'esquerra: no s\'atura mai.',
        ts=(4, 4), cuenta_titulo='La melodia i l\'esquerra, mesurades',
        cuenta_pie='A dalt, els cc. 1-2 de la dreta. A baix, els cc. 1-2 de l\'esquerra: '
                   'vuit corxeres per compàs.',
        ritmos=[('LA DRETA', 'cc. 1-2', _MEL, AZUL, 'treble', None),
                ('L\'ESQUERRA', 'cc. 1-2', _IZQ, OCRE, 'bass', None)]),
    manos=dict(
        titulo='Cada mà, per separat',
        sub='L\'esquerra mana i la dreta canta a sobre. Comença per l\'esquerra.',
        tit_izq='MÀ ESQUERRA', tit_der='MÀ DRETA',
        izq=[('Només la nota greu', 'Toca una nota per compàs, la greu: Mi, La, Si, La. '
                                    'Compta vuit corxeres.'),
             ('Nota i octava', 'Alterna la greu i la mateixa una octava més aguda. La mà '
                               'gairebé no es mou.'),
             ('Els vuit compassos', 'cc. 1-4: Mi, La, Si, La. cc. 5-8: Re, Do, Si, La. '
                                    'La nota greu baixa d\'una en una.'),
             ('Sense parar', 'Corxeres regulars, sense accelerar. Toca-ho de memòria.')],
        der=[('Canta-la', 'Mi, Si-Do, Re, Do-Si, La... Canta els noms abans de tocar.'),
             ('Llarg i curt', 'Dues corxeres valen una negra. Al c. 3, el Si dura un temps i '
                              'mig i el Do cau a la "i" del 2. Igual als cc. 6 i 7.'),
             ('El c. 5', 'Comença amb un silenci de corxera: entra a la "i" de l\'1.'),
             ('Notes llargues', 'Als cc. 9-16 hi ha blanques i rodones. Compta-les senceres i '
                                'vigila el Sol sostingut.')],
        tecnica=['Canell solt: les corxeres de l\'esquerra es toquen lleugeres.',
                 'Compta "1-i-2-i-3-i-4-i" en veu alta.',
                 'L\'esquerra és el rellotge: no s\'accelera quan la dreta canvia.']),
    bloques=[
        B(1, 'cc. 1-4', 'La melodia', (0, 0),
          D('grupos', 'Un compàs de 4/4 = 4 temps de 2 corxeres', (4, 2, ['1', '2', '3', '4'])),
          [('IZQUIERDA', 'Mi, La, Si, La: nota greu i octava, vuit corxeres per compàs.'),
           ('DERECHA', 'Mi, Si-Do, Re, Do-Si | La, La-Do, Mi, Re-Do | Si., Do, Re, Mi | Do, La, La.'),
           ('JUNTAS', 'Un compàs cada vegada; després els quatre.'),
           ('OJO', 'Al c. 3, el Si dura un temps i mig. Compta-ho bé!')]),
        B(2, 'cc. 5-8', 'La nota greu baixa', (1, 1),
          D('cadena', 'El baix, compàs a compàs', [('Re', False), ('Do', False), ('Si', False),
                                                   ('La', True)]),
          [('IZQUIERDA', 'Re, Do, Si, La: baixa d\'una en una. La mà segueix amb octaves.'),
           ('DERECHA', 'Silenci de corxera, Re, Fa, La, Sol-Fa | Mi., Do, Mi, Re-Do | Si., Do, Re, Mi | Do, La, La.'),
           ('JUNTAS', 'Els cc. 5-6, després els cc. 7-8.'),
           ('OJO', 'El c. 5 comença amb un silenci de corxera: no t\'avancis!')]),
        B(3, 'cc. 9-12', 'Notes llargues', (2, 2),
          D('cadena', 'Les blanques, per compàs',
            [('Mi-Do', False), ('Re-Si', False), ('Do-La', False), ('Sol#', True)]),
          [('IZQUIERDA', 'La, Sol sostingut, La, Si. El c. 10 sencer porta Sol sostingut.'),
           ('DERECHA', 'Dues blanques per compàs. El c. 12 és una rodona: Sol sostingut.'),
           ('JUNTAS', 'La dreta aguanta i l\'esquerra segueix en corxeres. Compta.'),
           ('OJO', 'Sol sostingut = tecla negra, a la dreta del Sol.')]),
        B(4, 'cc. 13-16', 'La pujada', (3, 3),
          D('cadena', 'El camí', [('cc. 13-14 = cc. 9-10', False), ('Do Mi La La', False),
                                  ('Sol# agut', True)]),
          [('IZQUIERDA', 'La, Si, Do, Si. Puja una mica i torna.'),
           ('DERECHA', 'Els cc. 13-14 són els cc. 9-10. Al c. 15: Do, Mi, La, La.'),
           ('JUNTAS', 'El c. 15 és el més difícil: les dues mans es mouen alhora.'),
           ('OJO', 'El c. 16 és una rodona de Sol sostingut agut.')]),
        B(5, 'cc. 17-20', 'Torna el principi', (4, 4),
          D('cadena', 'És el bloc 1', [('cc. 17-20', True), ('= cc. 1-4', False)]),
          [('IZQUIERDA', 'Mi, La, Si, La, com al principi.'),
           ('DERECHA', 'La mateixa melodia dels cc. 1-4. Toca-la de memòria.'),
           ('JUNTAS', 'Els quatre compassos seguits, sense parar.'),
           ('A TEMPO', 'Del c. 1 al c. 20, sense aturar-te al c. 16.')]),
        B(6, 'cc. 21-24', 'Final', (5, 5),
          D('cadena', 'Gairebé igual que els cc. 5-8', [('cc. 21-23 = 5-7', False),
                                                        ('c. 24 diferent', True)]),
          [('IZQUIERDA', 'Re, Do, Si, La, com als cc. 5-8.'),
           ('DERECHA', 'c. 24: silenci de corxera, Do, La corxera, La i silenci.'),
           ('JUNTAS', 'Atura\'t al final amb calma, sobre La.'),
           ('A TEMPO', 'Tota la peça, del principi al final.')]),
    ],
    cortes={1: [244.8, 391.2, 541.8, 684.2]}, corte_titulo=96.5,
    fin={1: 822},
    burb={
        0: [('arriba', 280, 'DER', 'Comença en Mi: una negra, dues corxeres juntes, una altra negra '
                                   'i dues corxeres. Canta-la abans de tocar.', 0.1),
            ('abajo', 270, 'IZQ', 'Vuit corxeres per compàs: la nota greu i la seva octava. Mi, La, '
                                  'Si, La.', 0.2)],
        1: [('arriba', 270, 'OJO', 'El c. 5 comença amb un silenci de corxera: entra a la '
                                   '"i" de l\'1. Compta!', 0.05),
            ('abajo', 280, 'IZQ', 'La nota greu baixa d\'una en una: Re, Do, Si, La.', 0.5)],
        2: [('arriba', 270, 'DER', 'Blanques: dos temps cadascuna. La dreta canta llarg.', 0.1),
            ('abajo', 280, 'OJO', 'Sol sostingut (tecla negra): a l\'esquerra del c. 10 i '
                                  'a la dreta del c. 12. No te\'l descuidis!', 0.55)],
        3: [('arriba', 270, 'DER', 'Els cc. 13-14 repeteixen els cc. 9-10. Al c. 15 puja: Do, '
                                   'Mi, La, La.', 0.55),
            ('abajo', 270, 'OJO', 'c. 16: una rodona de Sol sostingut agut. Compta quatre '
                                  'temps i no tinguis pressa.', 0.9)],
        4: [('arriba', 300, 'AMB', 'Són els cc. 1-4 un altre cop: ja la saps. Toca-la de memòria.',
             0.1)],
        5: [('arriba', 300, 'OJO', 'El c. 24 és diferent: silenci de corxera, Do, La corxera, '
                                   'La i silenci. Acaba amb calma!', 0.8)],
    },
    marcas=[],
    misol=dict(
        manos='Comença sempre per l\'esquerra: és el rellotge de la peça. Si ella va fina, la '
              'dreta et surt sola.',
        guia='Fes-ho per blocs de quatre compassos. Quan en dominis un, passa al següent. '
             'Els cc. 17-20 ja els saps!',
        pauta='Inventa dos compassos de 4/4 amb una nota greu i la seva octava, com l\'esquerra '
              'del Tetris. O copia el c. 1!'),
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de La menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_tx_tetris.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
