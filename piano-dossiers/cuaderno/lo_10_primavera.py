# -*- coding: utf-8 -*-
"""Peça 10 · La Primavera (Vivaldi, Les quatre estacions · versió fàcil de la Profª Vera Lucia).
   MESURAT sobre el PDF (1 pàgina, carta; notes pintades amb colorear_notas.py): sense armadura,
   4/4, sense tempo ni matisos, 21 compassos en 5 sistemes (4+4+4+5+4). Repetició: «|:» al c. 14, «:|» al c. 20,
   amb casella 1 (c. 20) i casella 2 (c. 21). Comença amb una anacrusi d'un temps (Do, dit de dreta) al c. 1
   (silenci de blanca i de negra + Do). Esquerra: rodones de quinta buida Do3+Sol3 (c. 2-6, 8-13) amb Si2+Sol3
   al c. 7; als cc. 15-19 acords de tres notes (Do+Fa+La / Do+Mi+Sol) i als cc. 20-21 Do+Mi+Sol.
   Dreta: tema Do Mi Mi Mi Re♪Do♪, Sol blanca lligada, etc. Figures: negra, blanca, rodona, negra amb puntet, corxera."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}
_e = lambda g: {'pitch': 'B4', 'dur': 'e', 'beam': g}

SPEC = dict(
    num=10, slug='primavera', pdf='primavera.pdf', time_sig=(4, 4),
    titulo='La Primavera (Vivaldi)',
    autor='Antonio Vivaldi · versió fàcil de la Profª Vera Lucia',
    kicker=kick(10, 'La Primavera'), mes=MESES[10],
    yt=yt('vivaldi spring primavera easy piano'),
    credito='Partitura: versió fàcil de la Profª Vera Lucia. Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense armadura'), ('Compàs', '4/4'), ('Tempo', 'No indicat'),
               ('Figura curta', 'Corxera'), ('Compassos', '21 + repetició')],
        total=21,
        secciones=[('A', 1, 13, 'El tema de la primavera', AZUL),
                   ('B', 14, 20, 'Part repetida, amb acords', OCRE),
                   ('C', 21, 21, 'Segona vegada: final', AZUL)],
        ideas=[('LA MELODIA', 'Una nota repetida i un salt',
                'Tres notes iguals (Mi Mi Mi) i dues corxeres que baixen: és l\'imitació del cant dels ocells.'),
               ("L'ESQUERRA", 'Quintes llargues',
                'Do i Sol junts, una rodona per compàs. Més endavant, acords de tres notes (Do+Fa+La, Do+Mi+Sol).'),
               ('LA REPETICIÓ', 'Una part que es toca dues vegades',
                'Els signes «|:» i «:|» marquen la part que es repeteix. La primera vegada acabes a la casella 1; la segona, a la 2.'),
               ("L'ANACRUSI", 'Entra a l\'últim temps',
                'Comença amb dos silencis i un Do, al darrer temps del primer compàs.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            'No hi ha armadura ni alteracions: només notes blanques.',
            'Hi ha un signe de repetició: toca de «|:» (c. 14) a «:|» (c. 20) i repeteix.',
            "Primera casella (1.) al c. 20, segona casella (2.) al c. 21: la segona vegada, salta al final.",
            "Les notes de l'esquerra són rodones: quatre temps cadascuna.",
            'Comença amb dos silencis i una nota (Do) al darrer temps.'],
        reto='Toca la part repetida (cc. 14-20) i torna al «|:» sense aturar-te, i acaba a la casella 2.',
        truco="Ja saps el tema: Mi Mi Mi Re Do. Els ocells de Vivaldi sonen igual: pensa en un ocellet!",
        sabias="«La Primavera» és el primer concert de Les quatre estacions de Vivaldi, de fa uns tres-cents anys. "
               "Els violins imiten el cant dels ocells.",
        qr_texto='Escolta-la i imagina els ocellets amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo='Com es compta el tema',
        cuenta_pie="Tres negres i dues corxeres: «1, 2, 3, 4-i». Una blanca + dues corxeres: «1-2, 3-i». Aquí només el ritme.",
        ritmos=[('TRES NEGRES + 2 CORXERES', '4/4 · 1 · 2 · 3 · 4-i',
                 [_q('B4'), _q('B4'), _q('B4'), _e(0), _e(0)], OCRE, 'treble', None),
                ('UNA RODONA', '4/4 · mà esquerra · 1-2-3-4',
                 [{'pitches': ['C3', 'G3'], 'dur': 'w'}], AZUL, 'bass', None)]),
    manos=dict(
        izq=[('Do+Sol junts', 'Dos dits alhora: dit 5 al Do greu i dit 1 al Sol. Premeu i compteu 1-2-3-4.'),
             ('Acords de tres notes', "Als cc. 15-19: Do+Fa+La i Do+Mi+Sol. Tres dits alhora: 5-2-1."),
             ('Un canvi: Si+Sol', 'Al c. 7 la nota baixa a Si: gris. És l\'únic canvi del primer bloc.'),
             ('La repetició', 'Quan toca repetir (:|), torna al c. 14 sense parar.')],
        der=[('Do (anacrusi)', "Dos silencis i un Do: entra al darrer temps del c. 1."),
             ('Mi Mi Mi Re Do', 'C. 2: tres negres iguals (groc, groc, groc) i dues corxeres Re Do.'),
             ('Sol lligat', 'Al c. 3 i al c. 5: Sol llarg que es repeteix lligat. Una sola nota.'),
             ('Les dues cases', 'Cc. 20 i 21: la primera vegada, Do i Do. La segona, la nota final.')],
        tecnica=['Comença suau, com un ocell que desperta.',
                 'Corxeres: dues notes petites, rapides i lleugeres.',
                 'La mà esquerra es mou de pressa però sense sorolls.']),
    bloques=[
        B(1, 'cc. 1-8', 'El tema de la primavera', (0, 1),
          D('cadena', 'L\'ocell canta',
            [('anacrusi: Do', False), ('Mi Mi Mi Re Do', False), ('Sol lligat', False), ('cc. 5-8', True)]),
          [('IZQUIERDA', 'Do+Sol: una rodona per compàs durant els cc. 2-8. Al c. 7: Si+Sol.'),
           ('DERECHA', 'Anacrusi: Do. C. 2: Mi Mi Mi Re Do. C. 3: Sol lligat... Cc. 5-8: la mateixa idea.'),
           ('JUNTAS', 'Una nota de la dreta per cada acord de l\'esquerra. Compta 1-2-3-4.'),
           ('A TEMPO', 'Alegre i lleuger, com un ocell. Sense córrer.')]),
        B(2, 'cc. 9-12', 'El tema torna', (2, 2),
          D('cadena', 'Mateix tema, mateixa mà',
            [('c. 9: Sol lligat', False), ('c. 10: Mi Mi Mi', False), ('cc. 11-12', True)]),
          [('IZQUIERDA', 'Do+Sol: quatre rodones seguides. No et moguis de lloc.'),
           ('DERECHA', 'Cc. 9-12: Sol lligat, Mi Mi Mi Re Do, Sol lligat, Mi Fa Sol Fa Mi. Compta les corxeres.'),
           ('JUNTAS', 'La dreta canta, l\'esquerra és el fons: no el tapis.'),
           ('OJO', 'Les corxeres són el doble de ràpides que les negres: compta «1-i-2-i».')]),
        B(3, 'cc. 13-17', 'La part repetida, amb acords', (3, 3),
          D('cadena', '|: comença la repetició',
            [('c. 13: final del bloc', False), ('c. 14: |:', False), ('cc. 15-17: acords', True)]),
          [('IZQUIERDA', 'Acords de tres notes: Do+Fa+La i Do+Mi+Sol als cc. 15-17. Mira els colors.'),
           ('DERECHA', 'Cc. 14-17: Sol, Fa Mi Fa Sol, La lila, Sol, Mi... Una melodia més oberta.'),
           ('JUNTAS', 'Acord + nota: cada acord de l\'esquerra té una nota de la dreta damunt.'),
           ('OJO', 'Al c. 14 hi ha el signe «|:» (inici de repetició). Compta-hi bé.')]),
        B(4, 'cc. 18-21', 'Casella 1 i casella 2', (4, 4),
          D('cadena', 'Primera i segona vegada',
            [('cc. 18-19', False), ('c. 20: casella 1 → :|', False), ('c. 21: casella 2', True)]),
          [('IZQUIERDA', 'Acords: Do+Fa+La, Do+Mi+Sol. Al final, Do+Mi+Sol de rodona.'),
           ('DERECHA', 'Cc. 18-19: La Sol Fa, Mi Re Do Re. C. 20: Do. C. 21: Do llarg.'),
           ('JUNTAS', 'La primera vegada, toca la casella 1 i torna al «|:». La segona, salta a la 2.'),
           ('OJO', 'Casella 1: tornes enrere. Casella 2: acabes.')]),
    ],
    lista=["Toco l'anacrusi (Do) i entro a temps.",
           "Toco l'esquerra: Do+Sol, Si+Sol i els acords de tres notes.",
           'Faig bé la repetició (|: i :|).',
           'Toco les corxeres del tema amb claredat.',
           'Toco la peça sencera amb la repetició.'],
    cortes={1: [221.2, 345.2, 469.2, 597.0]}, inicio={1: 120}, fin={1: 725},
    burb={
        0: [('arriba', 262, 'DER', 'Anacrusi: dos silencis i un Do al darrer temps. Compta «1-2-3» i entra al 4.', 0.1),
            ('arriba', 262, 'IZQ', 'Do+Sol (quinta): una rodona per compàs.', 0.55)],
        1: [('arriba', 262, 'DER', 'Sol llarg i les dues corxeres que baixen.', 0.15),
            ('arriba', 262, 'OJO', 'Si+Sol a la mà esquerra al c. 7: la nota baixa al gris.', 0.62)],
        2: [('arriba', 262, 'DER', 'Mateix tema: Mi Mi Mi i corxeres. Aquí ja el coneixes!', 0.3)],
        3: [('arriba', 262, 'OJO', 'Signe «|:» al c. 14: aquí comença la part que es repeteix.', 0.3),
            ('arriba', 262, 'IZQ', 'Acords de tres notes: Do+Fa+La i Do+Mi+Sol.', 0.7)],
        4: [('arriba', 262, 'OJO', 'Casella 1 → torna al «|:». Casella 2 → final.', 0.65)],
    },
    misol=dict(
        manos="Un signe de repetició és com una porta: quan arribes a «:|», tornes enrere fins al «|:».",
        guia="Les dues caselles (1. i 2.) són dues sortides: la primera vegada surts per la 1, la segona per la 2!",
        pauta="Dibuixa un signe de repetició «|:» i «:|» i entre els dos escriu un compàs de la peça."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu el signe de repetició i un compàs entre mig")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_primavera.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
