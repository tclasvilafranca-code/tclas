# -*- coding: utf-8 -*-
"""Peça 4 · Greensleeves (cançó tradicional anglesa, versió a dues mans amb xifrat).
   MESURAT sobre el PDF (2 pàgines, A4, 8 sistemes de 4 compassos): sense armadura (La menor, amb Fa♯ i Sol♯
   puntuals), 3/4, «Moderato», mp a l'anacrusi, f als cc. 17 i 25, reguladors de crescendo als cc. 23 i 30-31,
   «con pedale» al c. 4-5 (impres). Anacrusi d'una negra (La, dit 1) i 32 compassos; l'últim (c. 32, blanca) completa
   l'anacrusi. Xifrat: Am, G, F, E, C, G/D, Am/E. Esquerra: tres negres que pugen per compàs (La-Do-Mi, Sol-Si-Re,
   Fa-La-Do, Mi-Sol♯-Si, Do-Mi-Sol, Re-Sol-Si) i un acord final (La-Do-Mi). Dreta: melodia amb negra amb puntet + corxera
   (cc. 2, 4, 6, 14, 18, 22, 26, 30...). Una gran lligadura per frase. Figura curta: corxera."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES

_q = lambda p: {'pitch': p, 'dur': 'q'}

SPEC = dict(
    num=4, slug='greensleeves', pdf='greensleeves.pdf', time_sig=(3, 4),
    titulo='Greensleeves',
    autor='Cançó tradicional anglesa · versió amb xifrat',
    kicker='Alba · peça 4 · Greensleeves', mes=MESES[4],
    yt='https://www.youtube.com/results?search_query=greensleeves+piano+easy',
    credito='Partitura: Greensleeves (MuseScore). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'La menor'), ('Compàs', '3/4'), ('Tempo', '«Moderato»'),
               ('Figura curta', 'Corxera'), ('Compassos', '32 + anacrusi')],
        total=32,
        secciones=[('A', 1, 8, '«Alas, my love…»', AZUL),
                   ('A', 9, 16, 'Segona frase', OCRE),
                   ('B', 17, 24, 'El cor, en f', AZUL),
                   ('B', 25, 32, 'El cor torna i acaba', OCRE)],
        ideas=[('EL GEST DE LA MÀ ESQUERRA', 'Tres negres que pugen',
                'A cada compàs, la nota greu de l\'acord, la mitjana i l\'aguda: La-Do-Mi, Sol-Si-Re, Fa-La-Do…'),
               ('LA MELODIA', 'Negra amb puntet + corxera',
                'Un balanceig que torna a moltes frases (cc. 2, 4, 6…): tres temps de vals i un petit gir.'),
               ('LA TONALITAT', 'La menor, amb Fa♯ i Sol♯',
                'No hi ha armadura, però la melodia porta Sol♯ i Fa♯ puntuals: el so «antic» de la peça.'),
               ('EL VOLUM', 'mp → f',
                'Comença fluix (mp), al c. 17 arriba al fort (f) i hi ha reguladors (crescendo) al final.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie='La partitura imprimeix xifrats: Am = La menor, G = Sol, F = Fa, E = Mi, C = Do, G/D = Sol amb Re al baix, Am/E = La menor amb Mi al baix.',
        especial=[
            'Sense armadura: La menor. Hi ha alteracions puntuals: Sol♯ i Fa♯.',
            'Comença amb anacrusi: una negra (La) abans del c. 1. L\'últim compàs només dura dues negres i la completa.',
            '«Moderato», mp al principi, f als cc. 17 i 25, reguladors als cc. 23 i 30-31.',
            'A la partitura hi diu «con pedale» (amb pedal): es pot tocar sense pedal.',
            'Cada frase té una gran lligadura: es toca lligada, com una sola respiració.'],
        reto='Toca les dues mans a la vegada, amb la dreta lligada i l\'esquerra suau i regular.',
        truco="Aprèn l'esquerra com una escala de tres notes que puja. Si la tens automàtica, la dreta s'hi adaptarà.",
        sabias="«Greensleeves» és una cançó anglesa de fa més de 400 anys. Shakespeare ja la cita a «Les alegres comares de Windsor».",
        qr_texto='Escolta-la i segueix el compàs de vals amb el peu.',
        ts=(3, 4),
        cuenta_titulo='Com es compta el 3/4',
        cuenta_pie="Tres negres: «1, 2, 3». Negra amb puntet + corxera + negra: «1-2, 3-i, 3». Aquí només el ritme.",
        ritmos=[('EL GEST DE L\'ESQUERRA', '3/4 · tres negres · 1 · 2 · 3',
                 [_q('B4'), _q('B4'), _q('B4')], OCRE, 'bass', None),
                ('MELODIA: NEGRA AMB PUNTET', '3/4 · c. 2 · 1-2 · i · 3',
                 [{'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e'}, _q('B4')], AZUL, 'treble', None)]),
    manos=dict(
        izq=[('La-Do-Mi', 'Els tres primers: negres suaus, amb el dit 5 al La greu, el 3 al Do i el 1 al Mi.'),
             ('Canvis d\'acord', 'Cada dos compassos canvia la forma: Sol-Si-Re, Fa-La-Do, Mi-Sol♯-Si… La mà es mou com un bloc.'),
             ('Sol♯ de l\'acord de Mi', 'Els cc. 7, 15, 23 i 31: Mi-Sol♯-Si. El Sol♯ és una tecla negra: mira-ho abans.'),
             ('Acord final', "L'últim acord és La-Do-Mi, tres notes juntes que duren tres temps.")],
        der=[('L\'anacrusi', 'La (dit 1) abans del c. 1. Compta «3» i entra.'),
             ('Do, Re, Mi, Fa', 'Cc. 1-2: blanca + negra, i després negra amb puntet + corxera + negra. El tema comença aquí.'),
             ('Sol♯ i Fa♯', 'Cc. 6, 7 i 15: tecles negres puntuals. Mira el ♯ abans de cada nota.'),
             ('El cor (cc. 17-24)', 'En f: més fort i més ple. Una frase lligada de principi a fi.')],
        tecnica=['Un so lligat: no aixequis el dit abans de tocar el següent.',
                 'La mà esquerra sempre més suau que la dreta (la melodia canta).',
                 'Compta «1-2-3» sense pressa, com un vals lent.']),
    bloques=[
        B(1, 'anacrusi + cc. 1-8', 'Alas, my love, you do me wrong', (0, 1),
          D('cadena', 'De la frase cap a Mi',
            [('anacrusi: La', False), ('cc. 1-4: Am-G', False), ('cc. 5-8: F-E', True)]),
          [('IZQUIERDA', 'Tres negres que pugen: La-Do-Mi (cc. 1-2), Sol-Si-Re (3-4), Fa-La-Do (5-6), Mi-Sol♯-Si (7).'),
           ('DERECHA', 'Anacrusi: La. Cc. 1-4: Do Re, Mi Fa Mi, Re Si, Sol La Si. Cc. 5-8: Do La, La Sol♯ La, Si Sol♯, Mi.'),
           ('JUNTAS', 'De dos en dos compassos: primer l\'esquerra, després la dreta, i juntes.'),
           ('OJO', 'Sol♯ als cc. 6-7: tecla negra. L\'acord de Mi (c. 7-8) és la tensió de la frase.')]),
        B(2, 'cc. 9-16', 'La segona frase', (2, 3),
          D('cadena', 'Igual i diferent',
            [('cc. 9-12 = cc. 1-4', False), ('cc. 13-16: final de frase', True)]),
          [('IZQUIERDA', 'Cc. 9-12 com els cc. 1-4. Cc. 13-16: Fa-La-Do, Mi-Sol♯-Si, Mi-La-Do, acord La-Do-Mi.'),
           ('DERECHA', 'Cc. 9-12 com abans. Cc. 13-16: Do. Si La, Sol♯. Fa♯ Sol, La llarga.'),
           ('JUNTAS', 'Quan coneguis la primera frase, aquesta és gairebé una còpia.'),
           ('OJO', 'Cc. 13-14: un Sol♯ i un Fa♯ (dues tecles negres). Mira-ho!')]),
        B(3, 'cc. 17-24', 'El cor: en f', (4, 5),
          D('cadena', 'Més fort i més ple',
            [('cc. 17-20: C-G/D', False), ('cc. 21-24: Am/E-E', True)]),
          [('IZQUIERDA', 'Do-Mi-Sol (cc. 17-18), Re-Sol-Si (19-20), Mi-La-Do (21-22), Mi-Sol♯-Si (23) i acord.'),
           ('DERECHA', 'Cc. 17-20: Sol llarg, Sol Fa♯ Mi, Re Si, Sol La Si. Cc. 21-24: com els cc. 5-8.'),
           ('JUNTAS', 'Més fort (f), amb tota la frase lligada.'),
           ('OJO', 'Regulador al c. 23: va creixent cap al final de la frase.')]),
        B(4, 'cc. 25-32', 'El cor torna i acaba', (6, 7),
          D('cadena', 'Fins al final',
            [('cc. 25-28 = cc. 17-20', False), ('cc. 29-32: final', True)]),
          [('IZQUIERDA', 'Els mateixos acords. Final: La-Do-Mi, acord de tres notes.'),
           ('DERECHA', 'Cc. 25-28 com els cc. 17-20. Cc. 29-32: Do. Si La, Sol♯. Fa♯ Sol, La llarga i La final.'),
           ('JUNTAS', 'Tota la peça. Aguanta el La final tres temps i deixa que s\'esvaeixi.'),
           ('A TEMPO', 'Moderato: ni lent ni ràpid. Un vals tranquil.')]),
    ],
    lista=["Toco el gest de l'esquerra sense mirar.",
           'Toco la melodia dels cc. 1-8 lligada.',
           'Faig bé el Sol♯ i el Fa♯.',
           'Faig el canvi de mp a f al c. 17.',
           'Toco els 32 compassos sense parar.'],
    cortes={1: [260.8, 450.0, 621.8], 2: [192.0, 387.8, 585.5]}, inicio={1: 95, 2: 30}, fin={1: 790, 2: 760},
    burb={
        0: [('arriba', 262, 'IZQ', 'Tres negres que pugen: La-Do-Mi (la nota greu, la mitjana i l\'aguda).', 0.2),
            ('arriba', 262, 'DER', 'Anacrusi: La (dit 1) abans del c. 1. Compta «3» i entra.', 0.05)],
        1: [('arriba', 262, 'OJO', 'Sol♯ al c. 6 i al c. 7 (tecla negra). L\'acord de Mi crea tensió.', 0.5)],
        2: [('arriba', 262, 'AMB', 'Els cc. 9-12 repeteixen els cc. 1-4.', 0.2)],
        3: [('arriba', 262, 'OJO', 'Sol♯ i Fa♯: dues tecles negres als cc. 13-14.', 0.4)],
        4: [('arriba', 262, 'OJO', 'f: el cor, més fort i ple. Cc. 17-20: Do i Sol/Re.', 0.1)],
        5: [('arriba', 262, 'OJO', 'Regulador (crescendo) al c. 23.', 0.55)],
        6: [('arriba', 262, 'AMB', 'El cor torna: mateixa música que els cc. 17-20.', 0.1)],
        7: [('arriba', 262, 'OJO', 'Final: La llarga i acord La-Do-Mi. Deixa sonar.', 0.85)],
    },
    misol=dict(manos='', guia='', pauta=''),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu els acords d'Am, G, F i E")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ba_greensleeves.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
