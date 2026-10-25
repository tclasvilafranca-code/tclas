# -*- coding: utf-8 -*-
"""Peça 7 · Puff, the Magic Dragon (Peter Yarrow i Leonard Lipton · arr. Eric Moore, MuseScore).
   MESURAT sobre el PDF (1 pàgina, A4; notes pintades amb colorear_notas.py): sense armadura,
   4/4, sense tempo ni matisos, 16 compassos en 4 sistemes de 4. Una negra amb puntet + corxera
   (cc. 1 i 9) i dues corxeres unides (cc. 6 i 14). Esquerra: acords de dues notes (terceres) mantinguts:
   c. 1 Do+Mi, c. 2 Mi+Sol, c. 3 Fa+La, c. 4 Do+Mi, c. 5 Fa+La, c. 6 Mi+Sol; c. 7 Fa♯ (♯); c. 8 Sol, Fa;
   cc. 9-14 igual que 1-6; c. 15 Fa♯ i després Fa♮+Sol (♮); c. 16 acord final Do+Mi+Sol.
   Dreta: cc. 1-4 Do5 Do5 Do5 Do5 | Si4 Sol4 | La4 Do5 Do5 | Sol4 Sol4; cc. 5-8 Fa4 Fa4 Sol4 Fa4 | Mi4 Sol4 Do5 Do5♪Do5♪ |
   Do5 La4 Si4 Do5 | Re5; cc. 13-16 igual que 5-6 i després La4 Do5 Si4 Re5 | Do5 (rodona)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}

SPEC = dict(
    num=7, slug='puff', pdf='puff.pdf', time_sig=(4, 4),
    titulo='Puff, the Magic Dragon',
    autor='Peter Yarrow i Leonard Lipton · arr. Eric Moore',
    kicker=kick(7, 'Puff, the Magic Dragon'), mes=MESES[7],
    yt=yt('puff the magic dragon piano easy'),
    credito='Partitura: arr. Eric Moore (MuseScore). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense armadura'), ('Compàs', '4/4'), ('Tempo', 'No indicat'),
               ('Figura curta', 'Corxera'), ('Compassos', '16')],
        total=16,
        secciones=[('A', 1, 4, '«Puff, the magic dragon»', AZUL),
                   ('B', 5, 8, 'La melodia puja i baixa', OCRE),
                   ('A', 9, 12, 'Torna el principi', AZUL),
                   ('B', 13, 16, 'Final', OCRE)],
        ideas=[('LA MELODIA', 'Do agut repetit',
                "Comença amb quatre Do aguts seguits i baixa fins al Sol: «Puff the ma-gic dra-gon»."),
               ("L'ESQUERRA", 'Acords de dues notes',
                'Dues tecles a la vegada, mantingudes: Do+Mi, Mi+Sol, Fa+La. No és ràpid: és un coixí suau.'),
               ('EL RITME', 'Negra amb puntet',
                'Un temps i mig, i una corxera curta: «Puff the». Apareix al principi de cada frase.'),
               ('LES ALTERACIONS', 'Fa♯ i el becaire',
                "Al c. 7 i al c. 15 hi ha un Fa♯; al c. 15 un becaire (♮) torna el Fa natural.")],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            'No hi ha armadura: Do major, però amb dues alteracions (Fa♯ al c. 7 i al c. 15).',
            "Al c. 15 hi ha un becaire (♮) que cancel·la el sostingut: torna al Fa natural.",
            "No hi ha tempo escrit: tria un pas tranquil i constant.",
            'La mà esquerra toca acords de dues notes: premeu-les alhora.',
            'Els cc. 9-14 són una còpia dels cc. 1-6.'],
        reto='Toca els acords de dues notes amb la mà esquerra mentre la dreta canta la melodia.',
        truco="Aprèn els acords de l'esquerra com a «dues tecles juntes», sense pensar en notes: Do-Mi, Mi-Sol, Fa-La.",
        sabias="La cançó va néixer d'un poema que Leonard Lipton va escriure el 1959, quan tenia 19 anys. "
               "Peter Yarrow hi va afegir la música i el trio Peter, Paul and Mary la va fer famosa el 1963.",
        qr_texto='Escolta-la i canta amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo='Com es compta el c. 1 i el c. 6',
        cuenta_pie="Negra amb puntet + corxera: «1-2-3, i, 4». Dues corxeres: «1-i». Aquí només el ritme.",
        ritmos=[('EL COMPÀS 1', '4/4 · negra amb puntet, corxera, negra, negra',
                 [{'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e'}, _q('B4'), _q('B4')],
                 OCRE, 'treble', None),
                ('UN ACORD LLARG', '4/4 · mà esquerra · 1-2-3-4',
                 [{'pitches': ['C3', 'E3'], 'dur': 'w'}], AZUL, 'bass', None)]),
    manos=dict(
        izq=[('Dos Do i Mi junts', 'Posa els dits 5 i 3 sobre Do i Mi i prem-los alhora. Aguanta els quatre temps.'),
             ('Mi+Sol i Fa+La', 'Cada compàs porta un acord nou. Mou la mà sencera i mira els colors.'),
             ('Un Fa♯ (c. 7)', 'Una tecla negra: Fa♯. Només una nota, tota sola, al c. 7.'),
             ("L'acord final", 'Al c. 16, tres notes alhora: Do+Mi+Sol. Premeu-les ben juntes i deixeu-les sonar.')],
        der=[('Quatre Do', 'C. 1: Do agut (dit 5): negra amb puntet, corxera i dues negres.'),
             ('Baixant al Sol', 'Cc. 2-4: Si, Sol, La, Do, Sol. Mira els colors: gris, blau, lila, vermell, blau.'),
             ('Fa Fa Sol Fa', 'Cc. 5-8: baixa a la zona del Fa: verd, verd, blau, verd. Després puja al Do agut.'),
             ('El final', 'Cc. 15-16: La, Do, Si, Re i la nota llarga final, Do.')],
        tecnica=['Acord: tots els dits cauen alhora, com una sola mà.',
                 'La dreta canta: toca més fort que l\'esquerra.',
                 'Si et perds, torna a la primera nota de la frase.']),
    bloques=[
        B(1, 'cc. 1-4', 'Puff, the magic dragon', (0, 0),
          D('cadena', 'Do, Do, Do → Si → La → Sol',
            [('Do Do Do Do', False), ('Si Sol', False), ('La Do Do', False), ('Sol Sol', True)]),
          [('IZQUIERDA', 'Quatre acords de dues notes: Do+Mi, Mi+Sol, Fa+La, Do+Mi. Un per compàs.'),
           ('DERECHA', 'C. 1: quatre Do aguts (el primer, llarg). Cc. 2-4: baixa fins al Sol.'),
           ('JUNTAS', 'El Do+Mi de l\'esquerra entra amb el primer Do de la dreta.'),
           ('A TEMPO', 'Canta «Puff the ma-gic dra-gon» mentre toques. Compta 1-2-3-4.')]),
        B(2, 'cc. 5-8', 'La melodia puja i baixa', (1, 1),
          D('cadena', 'Fa Fa Sol Fa → Mi Sol Do → Do La Si Do → Re',
            [('c. 5', False), ('c. 6', False), ('c. 7', False), ('c. 8: Re', True)]),
          [('IZQUIERDA', 'Fa+La, Mi+Sol, Fa♯ (c. 7) i Sol, Fa (c. 8).'),
           ('DERECHA', 'C. 5: Fa Fa Sol Fa. C. 6: Mi Sol Do Do Do. C. 7: Do La Si Do. C. 8: Re llarg.'),
           ('JUNTAS', 'Compàs per compàs. Mira el Fa♯ de la mà esquerra al c. 7.'),
           ('OJO', 'Al c. 7 hi ha un Fa♯ (♯): tecla negra. Mira-ho abans de tocar.')]),
        B(3, 'cc. 9-12', 'Torna el principi', (2, 2),
          D('cadena', 'Igual que els cc. 1-4',
            [('cc. 9-12', False), ('= cc. 1-4', True)]),
          [('IZQUIERDA', 'Els mateixos acords: Do+Mi, Mi+Sol, Fa+La, Do+Mi.'),
           ('DERECHA', 'La mateixa melodia que els cc. 1-4. Si la saps, ja és teva!'),
           ('JUNTAS', 'Toca els quatre compassos de memòria.'),
           ('A TEMPO', 'Alegre i tranquil: sense córrer, amb el ritme de negra amb puntet.')]),
        B(4, 'cc. 13-16', 'El final', (3, 3),
          D('cadena', 'Fa♯ i el final',
            [('cc. 13-14 = cc. 5-6', False), ('c. 15: Fa♯ i ♮', False), ('c. 16: Do final', True)]),
          [('IZQUIERDA', 'Fa+La, Mi+Sol, després Fa♯ i Fa♮+Sol, i l\'acord final Do+Mi+Sol.'),
           ('DERECHA', 'Cc. 13-14 com els cc. 5-6. C. 15: La Do Si Re. C. 16: Do llarg.'),
           ('JUNTAS', 'Les dues mans fins al final: l\'últim acord sona amb la nota Do de la dreta.'),
           ('OJO', 'Al c. 15, Fa♯ i després Fa♮ (el becaire cancel·la el sostingut).')]),
    ],
    lista=["Toco els acords de dues notes de l'esquerra alhora.",
           'Toco la melodia dels cc. 1-4 de memòria.',
           'Toco el Fa♯ del c. 7.',
           'Faig la negra amb puntet + corxera.',
           'Toco els 16 compassos sense parar.'],
    cortes={1: [251.8, 427.0, 600.2]}, inicio={1: 120}, fin={1: 770},
    burb={
        0: [('arriba', 262, 'DER', 'Quatre Do aguts: negra amb puntet, corxera, negra, negra.', 0.15),
            ('arriba', 262, 'IZQ', 'Acords de dues notes: Do+Mi, Mi+Sol, Fa+La, Do+Mi.', 0.55)],
        1: [('arriba', 262, 'DER', 'Fa Fa Sol Fa (verd, verd, blau, verd): una nota per temps.', 0.15),
            ('arriba', 262, 'OJO', 'Fa♯ a la mà esquerra al c. 7: tecla negra.', 0.7)],
        2: [('arriba', 262, 'AMB', 'Els cc. 9-12 són iguals que els cc. 1-4. Repeteix!', 0.2)],
        3: [('arriba', 262, 'OJO', 'Al c. 15: Fa♯ i després un becaire (♮) que torna al Fa.', 0.65),
            ('arriba', 262, 'IZQ', "L'acord final, Do+Mi+Sol, amb tres dits alhora.", 0.95)],
    },
    misol=dict(
        manos="Un acord és com una abraçada: totes les notes alhora. Prova-ho amb la mà esquerra!",
        guia="Els cc. 9-12 són iguals que els cc. 1-4. Si t'ho saps bé, ja saps un altre quart de la cançó!",
        pauta="Escriu a la pauta l'acord Do+Mi+Sol amb els colors: vermell, groc i blau."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu l'acord Do-Mi-Sol amb els seus colors")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_puff.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
