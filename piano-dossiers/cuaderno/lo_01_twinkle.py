# -*- coding: utf-8 -*-
"""Peça 1 · Twinkle, Twinkle, Little Star (arr. Gilbert DeBenedetti, Gradimi).
   MESURAT sobre el PDF (1 pàgina, carta; notes pintades per color amb colorear_notas.py):
   sense armadura, 4/4 («C»), sense tempo ni matisos, 12 compassos en 3 sistemes de 4.
   Cada mà toca una part de la melodia: c. 1 Sol Sol (esq., dit 4) + Re Re (dta., dit 2);
   c. 2 Mi Mi Re(blanca) (dta.); c. 3 Do Do Si Si (esq.); c. 4 La La Sol(blanca) (esq.);
   c. 5 Re Re Do Do (dta.); c. 6 Si Si La(blanca) (esq.); c. 7 = c. 5; c. 8 = c. 6; c. 9-12 = c. 1-4.
   «Thumbs share C»: els dos polzes comparteixen el Do central. Només negres i blanques."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_q = lambda p: {'pitch': p, 'dur': 'q'}

SPEC = dict(
    num=1, slug='twinkle', pdf='twinkle.pdf', time_sig=(4, 4),
    titulo='Twinkle, Twinkle, Little Star',
    autor='Cançó tradicional · arr. Gilbert DeBenedetti',
    kicker='Lola · peça 1 · Twinkle, Twinkle, Little Star', mes='Novembre · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=twinkle+twinkle+little+star+piano+easy',
    credito='Partitura: arr. Gilbert DeBenedetti (gradimi.com). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense alteracions'), ('Compàs', '4/4'), ('Tempo', 'No indicat'),
               ('Figura curta', 'Negra'), ('Compassos', '12')],
        total=12,
        secciones=[('A', 1, 4, 'Twinkle, twinkle…', AZUL),
                   ('B', 5, 8, 'Up above the world…', OCRE),
                   ('A', 9, 12, 'Torna a començar', AZUL)],
        ideas=[('LES MANS', 'Es passen la melodia',
                "L'esquerra toca Sol Sol, la dreta Re Re Mi Mi Re, l'esquerra torna amb Do Do Si Si…"),
               ('ELS COLORS', 'Cada nota, un color',
                'Do vermell, Re taronja, Mi groc, Sol blau, La lila, Si gris. Segueix els colors!'),
               ('ELS DITS', 'Dos polzes al Do',
                'Els dos polzes (dit 1) comparteixen el Do del mig. La resta de dits van caient al costat.'),
               ('EL RITME', 'Només dues figures',
                'Negres (un temps) i blanques (dos temps). Cap compàs porta res més.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie='Do = vermell · Re = taronja · Mi = groc · Fa = verd · Sol = blau · La = lila · Si = gris.',
        especial=[
            'No hi ha cap alteració: només notes blanques del piano.',
            'Cada mà toca només una part de la melodia: es van passant la cançó.',
            'Els dos polzes comparteixen el Do del mig del piano.',
            'No hi ha tempo escrit: tria un pas tranquil i constant.',
            'Els compassos 5-8 i 9-12 són una repetició de la mateixa música.'],
        reto='Toca tota la cançó i canta la lletra a la vegada, sense aturar-te!',
        truco="Canta la lletra amb el nom de les notes i els colors. Les paraules t'ajuden a no perdre't.",
        sabias="La música d'aquesta cançó és antiga: Mozart la va fer servir per escriure 12 "
               "variacions. És la mateixa melodia que la de l'abecedari en anglès!",
        qr_texto="Escolta-la i canta amb la partitura al davant.",
        ts=(4, 4),
        cuenta_titulo='Com es compta cada compàs',
        cuenta_pie='Quatre negres: «1, 2, 3, 4». Una blanca i dues negres: «1-2, 3, 4». Aquí només el ritme.',
        ritmos=[('QUATRE NEGRES', '4/4 · 1 · 2 · 3 · 4',
                 [_q('B4'), _q('B4'), _q('B4'), _q('B4')], OCRE, 'treble', None),
                ('BLANCA + DUES NEGRES', '4/4 · 1-2 · 3 · 4',
                 [{'pitch': 'B4', 'dur': 'h'}, _q('B4'), _q('B4')], AZUL, 'treble', None)]),
    manos=dict(
        izq=[('Sol Sol amb el dit 4', 'Posa el dit 4 al Sol blau i toca dues vegades. Després el Do vermell: dit 1.'),
             ('Do Do Si Si', 'Als compassos 3 i 11: Do Do Si Si. Fixa\'t en els colors: vermell, vermell, gris, gris.'),
             ('La La Sol', "Al final de la frase: La lila dues vegades i Sol blau llarg (blanca). Compta 1-2."),
             ('Silenci a la mà', 'Mentre toca l\'altra mà, la teva descansa sobre les tecles. Compta les negres!')],
        der=[('Re Re amb el dit 2', 'Dit 2 al Re taronja. Toca dues vegades: «Twin-kle». El polze és al Do.'),
             ('Mi Mi Re', 'Dit 3 al Mi groc dues vegades i torna al Re (blanca): «lit-tle star».'),
             ('Re Re Do Do', 'Als compassos 5 i 7: dues notes taronges i dues vermelles. Baixa un escaló.'),
             ('Entra a temps', 'La dreta comença després de l\'esquerra. Compta 1-2 en silenci i entra al 3.')],
        tecnica=['Dits arrodonits, com si portessis una pilota petita a la mà.',
                 'Polze al costat: no el deixis caure pla.',
                 'Compta 1-2-3-4 en veu alta: el compte és el teu metrònom.']),
    bloques=[
        B(1, 'cc. 1-4', 'Twinkle, twinkle', (0, 0),
          D('cadena', 'Qui toca què',
            [('esq.: Sol Sol', False), ('dta.: Re Re Mi Mi Re', False), ('esq.: Do Do Si Si La La Sol', True)]),
          [('IZQUIERDA', 'Sol Sol (dit 4) i, més tard, Do Do Si Si i La La Sol. Compassos 1, 3 i 4.'),
           ('DERECHA', 'Re Re al c. 1 i Mi Mi Re al c. 2 (dits 2 i 3). Compta les negres.'),
           ('JUNTAS', 'Una mà després de l\'altra: esq., dreta, esq., esq. Sense aturar-te.'),
           ('A TEMPO', 'Canta la lletra mentre toques. Deixa que les blanques durin dos temps.')]),
        B(2, 'cc. 5-8', 'Up above the world', (1, 1),
          D('cadena', 'Els dos tornen',
            [('dta.: Re Re Do Do', False), ('esq.: Si Si La', False), ('dta.: Re Re Do Do', False), ('esq.: Si Si La', True)]),
          [('IZQUIERDA', 'Si Si La als compassos 6 i 8: gris, gris i lila llarg.'),
           ('DERECHA', 'Re Re Do Do als compassos 5 i 7: taronja, taronja, vermell, vermell.'),
           ('JUNTAS', 'Les mans es toquen per torns: dreta, esquerra, dreta, esquerra.'),
           ('OJO', "Al c. 6 la nota llarga és la lila (La): compta 1-2 abans de tornar a tocar.")]),
        B(3, 'cc. 9-12', 'Torna a començar', (2, 2),
          D('cadena', 'Com al principi',
            [('Re Re Mi Mi Re', False), ('Do Do Si Si', False), ('La La Sol', True)]),
          [('IZQUIERDA', 'Sol Sol, Do Do Si Si i La La Sol: igual que als compassos 1-4.'),
           ('DERECHA', 'Re Re i Mi Mi Re: igual que al principi.'),
           ('JUNTAS', 'Els quatre compassos amb les dues mans per torns.'),
           ('OJO', 'És l\'últim compàs: la blanca final dura 2 temps. Deixa anar les mans.')]),
        B(4, 'cc. 1-12', 'Tota la cançó', (0, 2),
          D('cadena', 'De dalt a baix',
            [('A', False), ('B', False), ('A', True)]),
          [('IZQUIERDA', 'Només les notes de l\'esquerra, saltant els silencis.'),
           ('DERECHA', 'Només les notes de la dreta, saltant els silencis.'),
           ('JUNTAS', 'Tota la cançó, per torns, sense aturar-te.'),
           ('A TEMPO', 'Canta-la mentre la toques, a pas constant.')]),
    ],
    lista=['Sé on va cada dit: dit 1 al Do dels dos polzes.',
           'Toco la dreta de memòria, cantant.',
           "Toco l'esquerra de memòria, cantant.",
           'Toco els 12 compassos sense parar.',
           'Sé dir el nom i el color de totes les notes.'],
    cortes={1: [347.5, 501.5]}, inicio={1: 190}, fin={1: 648},
    burb={
        0: [('arriba', 262, 'IZQ', 'Sol Sol amb el dit 4 (blau, blau). Després, per torns, la dreta.', 0.17),
            ('arriba', 262, 'DER', 'Re Re al c. 1 i Mi Mi Re al c. 2. Compta fins a 4.', 0.42)],
        1: [('arriba', 262, 'DER', 'Re Re Do Do: taronja, taronja, vermell, vermell.', 0.18),
            ('arriba', 262, 'IZQ', 'Si Si La: gris, gris i lila llarg. Compta 1-2.', 0.50)],
        2: [('arriba', 262, 'AMB', 'Torna a començar: repeteix els compassos 1-4. Mira que els colors són els mateixos!', 0.2),
            ('arriba', 262, 'OJO', 'L\'últim compàs: Sol blau llarg. Deixa que soni dos temps i acaba.', 0.9)],
    },
    misol=dict(
        manos="Canta els noms de les notes: Sol, Sol, Re, Re... Si les cantes, els dits les troben més fàcil!",
        guia="Si et perds, torna a mirar el color de la nota. Vermell, taronja, groc... els colors són el teu mapa!",
        pauta="Dibuixa aquí una estrella i, a sota, escriu les notes de Twinkle amb els seus colors!"),
    marcas=[],
    pie_pauta="la clau la poses tu · copia un compàs de Twinkle i pinta les notes")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_twinkle.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
