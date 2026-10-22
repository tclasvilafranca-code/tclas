# -*- coding: utf-8 -*-
"""Peça 3 · Ode to Joy (Beethoven, arr. Gilbert DeBenedetti, Gradimi, «Primer Level»).
   MESURAT sobre el PDF (1 pàgina, carta; notes pintades amb colorear_notas.py): sense armadura,
   4/4 («C»), «C position», 16 compassos en 4 sistemes de 4, sense tempo ni matisos.
   Dreta (negres, c. 4/8 acaben en blanca): c. 1 Mi Mi Fa Sol; c. 2 Sol Fa Mi Re; c. 3 Do Do Re Mi;
   c. 4 Mi Re Re; c. 5-7 = c. 1-3; c. 8 Re Do Do; c. 9 Re Re Mi Do; c. 10 Re Mi♪Fa♪ Mi Do;
   c. 11 Re Mi♪Fa♪ Mi Re; c. 12 Do Re; c. 13-15 = c. 1-3; c. 16 = c. 8.
   Esquerra (rodones): c. 1 Do3, c. 2 Sol3, c. 3 Do3, c. 4 Sol3, c. 5-7 igual; c. 8 Sol3+Do3 (blanques);
   c. 9-11 Sol3; c. 12 Fa♯3+Sol3 (blanques; únic sostingut); c. 13-15 igual; c. 16 Sol3+Do3.
   Corxeres només als cc. 10 i 11 (Mi-Fa). Digitació impresa als compassos clau."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}
_e = lambda g: {'pitch': 'B4', 'dur': 'e', 'beam': g}

SPEC = dict(
    num=3, slug='ode', pdf='ode.pdf', time_sig=(4, 4),
    titulo='Oda a l\'alegria (Ode to Joy)',
    autor='Ludwig van Beethoven · arr. Gilbert DeBenedetti',
    kicker=kick(3, 'Ode to Joy'), mes=MESES[3],
    yt=yt('ode to joy beethoven piano easy'),
    credito='Partitura: arr. Gilbert DeBenedetti (gradimi.com). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense alteracions'), ('Compàs', '4/4'), ('Tempo', 'No indicat'),
               ('Figura curta', 'Corxera'), ('Compassos', '16')],
        total=16,
        secciones=[('A', 1, 8, 'La melodia coneguda', AZUL),
                   ('B', 9, 12, 'La part nova', OCRE),
                   ('A', 13, 16, 'Torna el principi', AZUL)],
        ideas=[('LA MELODIA', 'Pas a pas',
                'La dreta va de Do a Sol sense fer salts: cada nota és la veïna de l\'anterior.'),
               ("L'ESQUERRA", 'Una nota per compàs',
                'Nomes rodones, quatre temps cadascuna: Do, Sol, Do, Sol... Fàcil i fort com una columna.'),
               ('LA REPETICIÓ', 'Tres frases iguals',
                'Els compassos 1-4, 5-7 i 13-15 són quasi el mateix: aprens-ne una i en tens tres.'),
               ('EL FA SOSTINGUT', 'Una tecla negra',
                "Al c. 12, l'esquerra toca Fa♯, la tecla negra de la dreta del Fa. És l'única de tota la peça.")],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            'La partitura diu «C position»: la mà dreta té el polze (dit 1) al Do i un dit a cada nota fins al Sol.',
            'No hi ha cap tempo escrit: tria un pas tranquil i constant.',
            "L'esquerra toca rodones i blanques: durada llarga, compta fins a quatre.",
            'Només als cc. 10 i 11 hi ha corxeres (Mi-Fa): van el doble de ràpid.',
            'Al c. 12 hi ha un Fa♯ (única alteració).'],
        reto="Toca les dues mans juntes: la dreta canta i l'esquerra marca un pas ferm.",
        truco="Primer toca la dreta sola cantant «la la la»; l'esquerra només cal afegir-la quan la dreta et surti sola.",
        sabias="Beethoven va escriure aquesta melodia per a la seva Novena Simfonia (1824), quan ja era quasi sord. "
               "Avui és l'himne d'Europa.",
        qr_texto='Escolta-la i canta amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo='Com es compta un compàs de la cançó',
        cuenta_pie="Quatre negres: «1, 2, 3, 4». Una rodona dura els quatre temps. Només al c. 10 i al c. 11 hi ha corxeres.",
        ritmos=[('QUATRE NEGRES', '4/4 · mà dreta · 1 · 2 · 3 · 4',
                 [_q('B4'), _q('B4'), _q('B4'), _q('B4')], OCRE, 'treble', None),
                ('UNA RODONA', "4/4 · mà esquerra · 1-2-3-4",
                 [{'pitch': 'D3', 'dur': 'w'}], AZUL, 'bass', None),
                ('NEGRA, DUES CORXERES, DUES NEGRES', '4/4 · c. 10 · 1 · 2-i · 3 · 4',
                 [_q('B4'), _e(0), _e(0), _q('B4'), _q('B4')], VERDE, 'treble', None)]),
    manos=dict(
        izq=[('Do i Sol, rodones', "Compassos 1-4: Do (dit 5), Sol (dit 1), Do, Sol. Una nota per compàs, compta 1-2-3-4."),
             ('Dues blanques', "Als cc. 8 i 16: Sol i Do, dos temps cadascuna. Compta 1-2 / 3-4."),
             ('Sol, Sol, Sol', "Als cc. 9, 10 i 11 el mateix Sol: no et moguis, descansa."),
             ('Un Fa♯', "Al c. 12 hi ha una tecla negra: el Fa♯. Fixa't en el símbol ♯ abans de tocar.")],
        der=[('Do Re Mi Fa Sol', 'Posa els cinc dits sobre Do-Re-Mi-Fa-Sol: dit 1 al Do, 2 al Re, 3 al Mi, 4 al Fa i 5 al Sol.'),
             ('Mi Mi Fa Sol', 'C. 1: dits 3-3-4-5. «Mi Mi Fa Sol» és el començament que ja coneixes.'),
             ('Puja i baixa', "C. 2: Sol Fa Mi Re, tot baixant. C. 3: Do Do Re Mi, tot pujant."),
             ('El final de la frase', 'Cc. 4 i 8: Mi Re Re (o Re Do Do). Les dues últimes són blanques: dos temps cadascuna.')],
        tecnica=['Dits arrodonits, polze relaxat al costat.',
                 'Quan la dreta fa corxeres, no correguis: cada nota igual de clara.',
                 "Mans suaus: el pes del braç fa el so, no els dits."]),
    bloques=[
        B(1, 'cc. 1-4', 'La primera frase', (0, 0),
          D('cadena', 'Mi Mi Fa Sol → Sol Fa Mi Re → Do Do Re Mi',
            [('c. 1', False), ('c. 2', False), ('c. 3', False), ('c. 4', True)]),
          [('IZQUIERDA', 'Do (dit 5), Sol (dit 1), Do, Sol: una rodona per compàs.'),
           ('DERECHA', 'Mi Mi Fa Sol · Sol Fa Mi Re · Do Do Re Mi · Mi Re Re. Mira els colors.'),
           ('JUNTAS', 'Compta 1-2-3-4. Una nota de l\'esquerra aguanta tot el compàs.'),
           ('A TEMPO', 'Canta «la la la» mentre toques. Acaba amb les dues blanques del c. 4.')]),
        B(2, 'cc. 5-8', 'La mateixa frase, un altre final', (1, 1),
          D('cadena', 'Igual i diferent',
            [('cc. 5-7 = cc. 1-3', False), ('c. 8: Re Do Do', True)]),
          [('IZQUIERDA', 'Do, Sol, Do... i al c. 8, dues blanques: Sol i Do.'),
           ('DERECHA', 'Cc. 5-7 com abans. C. 8: Re Do Do. Dits 2-1-1.'),
           ('JUNTAS', 'Les dues mans fins al c. 8. Els dos últims temps de la mà esquerra són el Do.'),
           ('OJO', 'Al c. 8 acabes en Do: és un petit descans. Respira abans de la part nova!')]),
        B(3, 'cc. 9-12', 'La part nova', (2, 2),
          D('cadena', 'Corxeres i el Fa♯',
            [('c. 9', False), ('cc. 10-11: Mi-Fa corxeres', False), ('c. 12: Fa♯', True)]),
          [('IZQUIERDA', 'Tres compassos seguits amb Sol (rodona). Al c. 12: Fa♯ i Sol, dues blanques.'),
           ('DERECHA', 'C. 9: Re Re Mi Do. Cc. 10-11: Re, Mi-Fa (corxeres), Mi, Do / Re. C. 12: Do Re.'),
           ('JUNTAS', 'Quan la dreta fa corxeres, l\'esquerra manté la rodona.'),
           ('OJO', 'Les corxeres del c. 10-11 són més ràpides: compta «1, 2-i, 3, 4».')]),
        B(4, 'cc. 13-16', 'Torna el principi i fi', (3, 3),
          D('cadena', 'Com al principi',
            [('cc. 13-15 = cc. 1-3', False), ('c. 16: Re Do Do', True)]),
          [('IZQUIERDA', 'Do, Sol, Do i, al final, Sol i Do en blanques.'),
           ('DERECHA', 'Igual que els cc. 1-3 i el final del c. 8: Re Do Do.'),
           ('JUNTAS', 'Les dues mans al final: la dreta acaba amb Do blanca i l\'esquerra amb Do.'),
           ('A TEMPO', 'Toca tota l\'Oda a l\'alegria sense parar. Quan et surti: grava-la amb el mòbil!')]),
    ],
    lista=['Sé on va cada dit de la mà dreta (Do-Re-Mi-Fa-Sol).',
           "Toco l'esquerra de memòria: Do, Sol, Do, Sol...",
           'Toco el Fa♯ del c. 12.',
           'Faig bé les corxeres Mi-Fa dels cc. 10-11.',
           'Toco els 16 compassos sense parar.'],
    cortes={1: [300.8, 438.2, 573.8]}, inicio={1: 150}, fin={1: 703},
    burb={
        0: [('arriba', 262, 'DER', 'Mi Mi Fa Sol (dits 3-3-4-5): groc, groc, verd, blau.', 0.2),
            ('arriba', 262, 'IZQ', 'Una rodona per compàs: Do, Sol, Do, Sol. Compta fins a 4.', 0.52)],
        1: [('arriba', 262, 'DER', 'Cc. 5-7 són com els cc. 1-3. Al c. 8: Re Do Do.', 0.3),
            ('arriba', 262, 'IZQ', 'Dues blanques al c. 8: Sol i Do (dits 1 i 5).', 0.9)],
        2: [('arriba', 262, 'DER', 'Corxeres Mi-Fa als cc. 10-11: el doble de ràpid.', 0.5),
            ('arriba', 262, 'OJO', 'Fa♯ al c. 12: la tecla negra, just a la dreta del Fa.', 0.88)],
        3: [('arriba', 262, 'AMB', 'Torna el principi: cc. 13-15 = cc. 1-3. Al c. 16, final amb Do blanca.', 0.2)],
    },
    misol=dict(
        manos="Els colors són el teu mapa: groc-groc-verd-blau... Mira'ls i toca! Quan et surti, tapa'ls amb la mà.",
        guia="Aquesta melodia puja i baixa pels veïns: una tecla blanca a la vegada, sense saltar-ne cap.",
        pauta="Escriu aquí els noms de les primeres notes de l'Oda a l'alegria i pinta-les del seu color."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu l'escala de Do i pinta cada nota")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_ode.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
