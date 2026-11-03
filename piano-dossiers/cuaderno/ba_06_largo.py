# -*- coding: utf-8 -*-
"""Peça 6 · Largo de la Simfonia del Nou Món (A. Dvořák · arr. A. C. Escobés, elcuartodelpiano.com).
   MESURAT sobre el PDF (1 pàgina, A4): sense armadura, 4/4, «Largo», p al c. 1, mf al c. 9, p al c. 13, «cresc.» al c. 17,
   f al c. 18, mp al c. 20; 20 compassos en 5 sistemes de 4; repetició «|:» al c. 9 i «:|» al c. 12. Dreta: c. 1 Mi. Sol♪ Sol(blanca);
   c. 2 Mi. Re♪ Do(blanca); c. 3 Re. Mi♪ Sol. Mi♪; c. 4 Re (rodona); c. 5-6 = c. 1-2; c. 7 Re. Mi♪ Re. Do♪; c. 8 Do (rodona);
   cc. 9-12 La. Do♪ Do(blanca) | Si Sol La(blanca) | La Do Si Sol | La (rodona); c. 13-16 = c. 1-4; cc. 17-20: Mi. Sol♪ Sol |
   Do5. Re5♪ Mi5(blanca) | Re5. Do5♪ Re5 La | Do5. + silenci | Re. Do♪ Re La Do (rodona). Esquerra: acords i notes llargues
   (Do+Mi+Sol, Do, Fa+Sol lligats, Fa+Sol, Fa, La, Sol...). Lligadures llargues. Figura curta: corxera."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES

_q = lambda p: {'pitch': p, 'dur': 'q'}

SPEC = dict(
    num=6, slug='largo', pdf='largo.pdf', time_sig=(4, 4),
    titulo='Largo · Simfonia del Nou Món',
    autor='Antonín Dvořák · arr. A. C. Escobés',
    kicker='Alba · peça 6 · Largo (Dvořák)', mes=MESES[6],
    yt='https://www.youtube.com/results?search_query=dvorak+largo+new+world+piano+easy',
    credito='Partitura: arr. A. C. Escobés (elcuartodelpiano.com). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '4/4'), ('Tempo', '«Largo» (molt lent)'),
               ('Figura curta', 'Corxera'), ('Compassos', '20')],
        total=20,
        secciones=[('A', 1, 8, 'El tema, dues vegades', AZUL),
                   ('B', 9, 12, 'Part central (repetició)', OCRE),
                   ('A', 13, 16, 'Torna el tema', AZUL),
                   ('C', 17, 20, 'Final: crescendo i f', OCRE)],
        ideas=[('LA MELODIA', 'Lenta i cantable',
                'Negra amb puntet + corxera i blanques: un ritme de cant que torna a moltes frases.'),
               ("L'ESQUERRA", 'Notes i acords llargs',
                "Acords de tres notes i notes sostingudes. Gairebé mai al mateix temps que la melodia: l'acompanya."),
               ('LA REPETICIÓ', '«|:» i «:|» als cc. 9-12',
                'Els quatre compassos centrals es toquen dues vegades abans de seguir.'),
               ('ELS MATISOS', 'Fluix, fort, fluix',
                'p al principi, mf al c. 9, p al c. 13, «cresc.» al c. 17, f al c. 18 i mp al c. 20.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie='',
        especial=[
            'Sense armadura ni alteracions: només notes blanques.',
            '«Largo»: molt lent, amb un pols tranquil. Compta quatre temps amplis.',
            'Matisos: p (c. 1), mf (c. 9), p (c. 13), cresc. (c. 17), f (c. 18), mp (c. 20).',
            'Repetició: des del «|:» del c. 9 fins al «:|» del c. 12, i es torna a tocar.',
            'Lligadures llargues: cada frase es toca lligada, sense aixecar els dits entre notes.'],
        reto='Toca tota la peça com si la cantessis: llarga, lligada i sense pressa.',
        truco="Canta el tema mentre l'esquerra toca soleta: et fixaràs on respirar i on s'ha de moure la mà.",
        sabias="Aquest tema és del segon moviment de la Simfonia del Nou Món, que Dvořák va escriure el 1893 als Estats Units. "
               "La melodia va ser tan popular que es va convertir en una cançó, «Goin' Home».",
        qr_texto='Escolta-la en silenci, amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo='Com es compta el c. 1 i el c. 9',
        cuenta_pie="Negra amb puntet + corxera + blanca: «1-2-3, i, 4-5…» en lent: «1 (2-3), i, 3-4». Aquí només el ritme.",
        ritmos=[('EL COMPÀS 1', '4/4 · negra amb puntet, corxera, blanca',
                 [{'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e'}, {'pitch': 'B4', 'dur': 'h'}],
                 OCRE, 'treble', None),
                ('UN ACORD LLARG', '4/4 · mà esquerra · 1-2-3-4',
                 [{'pitches': ['C3', 'E3', 'G3'], 'dur': 'w'}], AZUL, 'bass', None)]),
    manos=dict(
        izq=[('Acord Do+Mi+Sol', "Tres notes alhora, dits 5-3-1. Prem-les juntes i deixa-les sonar quatre temps."),
             ('Notes llargues', 'Un Do greu de quatre temps al c. 2. Compta sense moure\'t.'),
             ('Fa+Sol lligats', 'Cc. 3-4: dues notes juntes que s\'allarguen dos compassos. Lligadura: no repeteixis.'),
             ('La part central', 'Cc. 9-12: Fa-La, Sol-Mi, Fa-Sol, Fa-La, Sol-Mi, Fa. La mà esquerra també canta.')],
        der=[('Mi. Sol♪ Sol', 'C. 1: negra amb puntet, corxera i blanca. Dits 3, 5, 5. Compta «1-2-3, i, 4».'),
             ('Mi. Re♪ Do', 'C. 2: la melodia baixa fins al Do. Blanca llarga: dos temps.'),
             ('Re. Mi♪ Sol. Mi♪', 'C. 3: dues vegades negra amb puntet + corxera. Respira al final del c. 4.'),
             ('El final (cc. 17-20)', 'Do agut, Re i Mi: la melodia puja. «cresc.», f al c. 18 i mp al c. 20.')],
        tecnica=['Pes de braç: la melodia ha de cantar, no picar.',
                 'La mà esquerra sempre més fluixa que la dreta.',
                 'Cada lligadura és una respiració: no aixequis els dits d\'hora.']),
    bloques=[
        B(1, 'cc. 1-4', 'El tema', (0, 0),
          D('cadena', 'Una frase de 4 compassos',
            [('c. 1: Mi. Sol♪ Sol', False), ('c. 2: Mi. Re♪ Do', False), ('c. 3: Re. Mi♪ Sol. Mi♪', False), ('c. 4: Re', True)]),
          [('IZQUIERDA', 'Acord Do+Mi+Sol (c. 1), Do (c. 2), Fa+Sol lligats (cc. 3-4).'),
           ('DERECHA', 'C. 1: Mi. Sol♪ Sol. C. 2: Mi. Re♪ Do. C. 3: Re. Mi♪ Sol. Mi♪. C. 4: Re (rodona).'),
           ('JUNTAS', 'Compta «1-2-3-4» en veu alta. L\'esquerra entra al temps 1 de cada compàs.'),
           ('A TEMPO', 'Largo: molt lent i amb la lligadura de tota la frase. p.')]),
        B(2, 'cc. 5-8', 'La segona vegada', (1, 1),
          D('cadena', 'Igual i amb un petit canvi',
            [('cc. 5-6 = cc. 1-2', False), ('c. 7: Re. Mi♪ Re. Do♪', False), ('c. 8: Do', True)]),
          [('IZQUIERDA', 'Els mateixos acords. Al c. 7: Fa i Sol. Al c. 8: acord Do+Mi+Sol.'),
           ('DERECHA', 'Cc. 5-6 com cc. 1-2. C. 7: Re. Mi♪ Re. Do♪. C. 8: Do (rodona).'),
           ('JUNTAS', 'Fins al Do final del c. 8 amb una sola lligadura.'),
           ('OJO', 'Només canvia el c. 7: baixa fins al Do en lloc de pujar.')]),
        B(3, 'cc. 9-12', 'Part central · repetició', (2, 2),
          D('cadena', '|: es repeteix :|',
            [('c. 9: La. Do♪ Do', False), ('c. 10: Si Sol La', False), ('c. 11: La Do Si Sol', False), ('c. 12: La (:|)', True)]),
          [('IZQUIERDA', 'Fa-La, Sol-Mi, Fa-Sol, Fa-La, Sol-Mi, Fa: notes de dues en dues.'),
           ('DERECHA', 'C. 9: La. Do♪ Do. C. 10: Si Sol La. C. 11: La Do Si Sol. C. 12: La llarg.'),
           ('JUNTAS', 'Mf: una mica més fort. Es repeteix: toca els quatre compassos dues vegades.'),
           ('OJO', 'Al c. 12 el signe «:|» et fa tornar al c. 9. La segona vegada, segueix al c. 13.')]),
        B(4, 'cc. 13-20', 'Torna el tema i final', (3, 4),
          D('cadena', 'El tema i el final en f',
            [('cc. 13-16 = cc. 1-4', False), ('cc. 17-18: cresc. → f', False), ('cc. 19-20: mp, Do', True)]),
          [('IZQUIERDA', 'Els mateixos acords. Al final: Do-Si-La-Sol… fins a l\'acord final Do+Mi+Sol.'),
           ('DERECHA', 'Cc. 13-16 com cc. 1-4. Cc. 17-20: Mi. Sol♪ Sol, Do5. Re5♪ Mi5, Re5. Do5♪ Re5 La, Re. Do♪ Re La, Do final.'),
           ('JUNTAS', 'Crescendo cap al c. 18 (f), després baixa a mp i acaba suaument.'),
           ('A TEMPO', 'Largo: sense pressa fins al Do final.')]),
    ],
    lista=['Toco el tema (cc. 1-4) de memòria, amb les dues mans.',
           'Faig la lligadura de cada frase.',
           'Faig bé la repetició dels cc. 9-12.',
           'Canvio els matisos: p, mf, p, cresc., f, mp.',
           'Toco els 20 compassos sense parar.'],
    cortes={1: [228.5, 368.5, 509.5, 648.5]}, inicio={1: 107}, fin={1: 768},
    burb={
        0: [('arriba', 262, 'DER', 'Mi. Sol♪ Sol: negra amb puntet, corxera i blanca. p, lligat.', 0.1),
            ('arriba', 262, 'IZQ', 'Acord Do+Mi+Sol (c. 1), Do llarg (c. 2), Fa+Sol lligats (cc. 3-4).', 0.5)],
        1: [('arriba', 262, 'OJO', 'Només canvia el c. 7: baixa fins al Do (Re. Mi♪ Re. Do♪).', 0.65)],
        2: [('arriba', 262, 'AMB', 'mf: més fort. Cc. 9-12 es repeteixen (|: :|).', 0.1)],
        3: [('arriba', 262, 'DER', 'Torna el tema en p (cc. 13-16).', 0.15)],
        4: [('arriba', 262, 'OJO', 'cresc. al c. 17, f al c. 18, mp al c. 20: puja i baixa.', 0.4)],
    },
    misol=dict(manos='', guia='', pauta=''),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu el tema dels cc. 1-2")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ba_largo.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
