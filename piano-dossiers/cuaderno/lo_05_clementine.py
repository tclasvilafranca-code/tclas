# -*- coding: utf-8 -*-
"""Peça 5 · Oh My Darling, Clementine (arr. Gilbert DeBenedetti, Gradimi, «Primer Level», «Tongue in cheek»).
   MESURAT sobre el PDF (1 pàgina, carta; notes pintades amb colorear_notas.py): sense armadura,
   3/4, caràcter «Tongue in cheek», 3 sistemes de 3 compassos. Comença amb una ANACRUSI d'un temps
   (dues corxeres Do Do) i l'últim compàs (Do blanca) dura 2 temps: la completa. 8 compassos + anacrusi.
   Dreta: c. 1 Do q, Mi♪ Mi♪; c. 2 Mi q, Do q, Do♪ Mi♪; c. 3 Sol q, Sol q, Fa♪ Mi♪; c. 4 Re blanca, Re♪ Mi♪;
   c. 5 Fa q, Fa q, Mi♪ Re♪; c. 6 = c. 2 (Mi Do Do Mi); c. 7 Re q, Si♪ Re♪ («stretch!», polze al Si);
   c. 8 Do blanca. Esquerra: només dos Sol3 (c. 1 i c. 7), digitació impresa «1 or 4». Lletra: «Oh my darling,
   Clementine» / «Found a peanut»."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}
_e = lambda g: {'pitch': 'B4', 'dur': 'e', 'beam': g}

SPEC = dict(
    num=5, slug='clementine', pdf='clementine.pdf', time_sig=(3, 4),
    titulo='Oh My Darling, Clementine',
    autor='Cançó tradicional americana · arr. Gilbert DeBenedetti',
    kicker=kick(5, 'Clementine'), mes=MESES[5],
    yt=yt('oh my darling clementine piano easy'),
    credito='Partitura: arr. Gilbert DeBenedetti (gradimi.com). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense alteracions'), ('Compàs', '3/4'), ('Caràcter', '«Tongue in cheek»'),
               ('Figura curta', 'Corxera'), ('Compassos', '8 + anacrusi')],
        total=8,
        secciones=[('A', 1, 4, '«Oh my darling…»', AZUL),
                   ('B', 5, 8, '«…Clementine»', OCRE)],
        ideas=[('EL COMPÀS', 'Tres temps: un vals',
                "És la primera peça en 3/4: «1-2-3, 1-2-3». El primer temps és el més fort."),
               ("L'ANACRUSI", 'Entra abans',
                'Comença amb dues corxeres (Do Do) abans del c. 1. L\'últim compàs només dura 2 temps.'),
               ('LA MÀ ESQUERRA', 'Només dues notes!',
                'Un Sol greu al c. 1 i un altre al c. 7. La resta de la cançó és per a la dreta.'),
               ('EL CANVI DE POSICIÓ', 'El polze baixa',
                'Al c. 7 la partitura diu «stretch!»: el polze s\'estira cap avall fins al Si.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            "No hi ha cap alteració: només notes blanques del piano.",
            "Compàs de 3/4: tres temps per compàs.",
            "Comença amb anacrusi (dues corxeres, 1 temps); l'últim compàs té dos temps i la completa.",
            "Al c. 7 la partitura diu «stretch!»: la mà s'estira i el polze toca un Si.",
            "A l'esquerra només hi ha dos Sol. Compta els silencis!"],
        reto='Toca la cançó sencera comptant «1-2-3» en veu alta, també quan la mà esquerra descansa.',
        truco="Pinta en groc la frase «Oh my darling» i cantala. Les paraules ja porten el ritme.",
        sabias="Clementine és una cançó de l'Oest americà: un miner busca or i perd la seva filla Clementine. "
               "Aquesta versió diu «Tongue in cheek», que vol dir que es canta amb un puntet de broma.",
        qr_texto='Escolta-la i canta amb la partitura al davant.',
        ts=(3, 4),
        cuenta_titulo="Com es compta l'entrada i un compàs",
        cuenta_pie="L'anacrusi: «3-i» (dues corxeres). Un compàs: «1-2-3». Una blanca: «1-2» i la negra: «3».",
        ritmos=[("L'ANACRUSI", 'dues corxeres: 3-i',
                 [_e(0), _e(0)], OCRE, 'treble', None),
                ('NEGRA, NEGRA, DUES CORXERES', '3/4 · c. 2 · 1 · 2 · 3-i',
                 [_q('B4'), _q('B4'), _e(0), _e(0)], AZUL, 'treble', None),
                ('BLANCA + NEGRA', '3/4 · 1-2 · 3',
                 [{'pitch': 'B4', 'dur': 'h'}, _q('B4')], VERDE, 'treble', None)]),
    manos=dict(
        izq=[('Un Sol greu', 'Al c. 1: un sol Sol (dit 1 o dit 4, com prefereixis). És el primer cop de la cançó.'),
             ('Compta els silencis', "Entre els dos Sol hi ha moltes pauses: compta «1-2-3» i no et perdis."),
             ('El Sol de la baixada', 'Al c. 7 torna el Sol: el mateix color blau, la mateixa tecla.'),
             ('Mà relaxada', "Mentre descansa, la mà esquerra reposa sobre el teclat, sense apretar.")],
        der=[('Do Do (anacrusi)', 'Dues corxeres amb el dit 1: el començament de la cançó, abans del primer temps.'),
             ('Mi Do Do Mi', 'Cc. 2 i 6: negra, negra i dues corxeres. Cantar-ho: «dar-ling Oh my».'),
             ('Sol Sol Fa Mi', 'C. 3: Sol amb el dit 5 i després baixa, una nota cada cop.'),
             ('El Si del c. 7', "«Stretch!»: el polze baixa fins al Si, un pas per sota del Do. Després torna al Do final.")],
        tecnica=['Compta 1-2-3 sempre, com un vals.',
                 'Els dits cauen suaus a la tecla: no piquis.',
                 "El polze és el que s'estira al c. 7: la mà es mou, no el braç."]),
    bloques=[
        B(1, 'anacrusi + cc. 1-2', 'Oh my darling', (0, 0),
          D('cadena', 'Entra abans',
            [('Do Do', False), ('c. 1: Do Mi Mi', False), ('c. 2: Mi Do Do Mi', True)]),
          [('IZQUIERDA', 'Un Sol (dit 1 o dit 4) al c. 1. Només aquesta nota!'),
           ('DERECHA', 'Anacrusi: Do Do. C. 1: Do, Mi Mi. C. 2: Mi, Do, Do Mi.'),
           ('JUNTAS', 'La dreta canta i, quan toca, el Sol de l\'esquerra entra amb ella.'),
           ('OJO', "L'anacrusi són dues corxeres: compta «3-i» i comença.")]),
        B(2, 'cc. 3-5', '…dar-ling, Clementine', (1, 1),
          D('cadena', 'Mi → Sol → Fa → Re',
            [('c. 3: Sol Sol Fa Mi', False), ('c. 4: Re llarg', False), ('c. 5: Fa Fa Mi Re', True)]),
          [('IZQUIERDA', 'Aquí descansa: compta «1-2-3» en silenci.'),
           ('DERECHA', 'C. 3: Sol Sol Fa Mi. C. 4: Re blanca i Re Mi. C. 5: Fa Fa Mi Re.'),
           ('JUNTAS', 'Només la dreta: l\'esquerra mira com toques.'),
           ('OJO', 'Al c. 4 la blanca dura dos temps: «1-2» i després «3».')]),
        B(3, 'cc. 6-8', 'Thou art lost and gone forever', (2, 2),
          D('cadena', 'Final: stretch!',
            [('c. 6 = c. 2', False), ('c. 7: stretch!', False), ('c. 8: Do blanca', True)]),
          [('IZQUIERDA', 'Un Sol al c. 7, enmig. Torna a ser un sol so.'),
           ('DERECHA', 'C. 6: Mi Do Do Mi. C. 7: Re, Si Re (polze al Si). C. 8: Do blanca.'),
           ('JUNTAS', 'Al c. 7 la mà esquerra toca el Sol i la dreta fa el «stretch!».'),
           ('OJO', "«Stretch!»: al Si, el polze s'estira. Després torna al Do i acaba.")]),
        B(4, 'cc. 1-8', 'Tota la cançó', (0, 2),
          D('cadena', 'De dalt a baix',
            [('anacrusi + c. 1-2', False), ('cc. 3-5', False), ('cc. 6-8', True)]),
          [('IZQUIERDA', 'Els dos Sol (c. 1 i c. 7) i el silenci entre mig.'),
           ('DERECHA', 'Tota la melodia, de memòria si pots.'),
           ('JUNTAS', 'Compta «1-2-3» sense parar. Tot el vals!'),
           ('A TEMPO', 'Canta la lletra mentre toques. Amb ganes i una mica de broma!')]),
    ],
    lista=['Sé començar amb l\'anacrusi (Do Do).',
           'Compto «1-2-3» sense parar.',
           'Faig bé el «stretch!» del c. 7.',
           'Toco els dos Sol de la mà esquerra al seu lloc.',
           'Toco tota la cançó sense parar.'],
    cortes={1: [345.2, 488.8]}, inicio={1: 186}, fin={1: 640},
    burb={
        0: [('arriba', 262, 'DER', 'Anacrusi: dues corxeres Do Do. Compta «3-i» i entra.', 0.12),
            ('arriba', 262, 'IZQ', 'Un sol Sol (blau) al c. 1. Només una nota!', 0.4)],
        1: [('arriba', 262, 'DER', 'Sol amb el dit 5 al c. 3. Baixa fins al Re.', 0.1),
            ('arriba', 262, 'OJO', 'Re blanca al c. 4: dura dos temps.', 0.42)],
        2: [('arriba', 262, 'DER', 'Stretch! El polze baixa al Si al c. 7 (gris).', 0.5),
            ('arriba', 262, 'IZQ', 'Un Sol al c. 7: l\'últim de l\'esquerra.', 0.72)],
    },
    misol=dict(
        manos="La mà esquerra només té dues notes: no t'enganyis, és tota la teva feina! Compta els silencis.",
        guia="El vals fa «1-2-3, 1-2-3». El primer temps sempre és el més fort. Prova de tocar-lo amb un petit 'ballet'!",
        pauta="Escriu a la pauta un compàs de 3/4 amb tres negres i pinta-les amb els seus colors."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu un compàs de 3/4 amb tres negres")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_clementine.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
