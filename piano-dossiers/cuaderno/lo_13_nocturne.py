# -*- coding: utf-8 -*-
"""Peça 13 · Nocturne Op. 9 n.º 2 (Frédéric Chopin · arr. Benny Chaw, versió fàcil, MuseScore).
   MESURAT sobre el PDF (1 pàgina, A4; notes pintades amb colorear_notas.py): sense armadura, 3/4, mp
   a les dues mans al c. 1 (sense tempo), 17 compassos en 4 sistemes (4+4+4+5). Anacrusi: silenci de negra
   a la dreta i Sol3 (dit 4) a l'esquerra. Dreta: notes llargues (blanques amb puntet i lligadura al c. 1-2)
   i petits motius de negres (Mi Re Mi, La Mi...). Dit 3 al c. 2, 5 al c. 7 i al c. 15, 1 al c. 12.
   Esquerra: gairebé només silencis; un compàs de corxeres La-Si♭-La-Sol♯-La (c. 6, amb ♭ i ♯);
   notes soltes (La, Si, Do...). Calderó al Do final de la mà esquerra (c. 17), lligat des del c. 16."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}
_e = lambda g: {'pitch': 'B4', 'dur': 'e', 'beam': g}

SPEC = dict(
    num=13, slug='nocturne', pdf='nocturne.pdf', time_sig=(3, 4),
    titulo='Nocturn Op. 9 (Chopin)',
    autor='Frédéric Chopin · arr. Benny Chaw',
    kicker=kick(13, 'Nocturn Op. 9'), mes=MESES[13],
    yt=yt('chopin nocturne op 9 no 2 easy piano'),
    credito='Partitura: arr. Benny Chaw (MuseScore). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense armadura'), ('Compàs', '3/4'), ('Tempo', 'No indicat (mp)'),
               ('Figura curta', 'Corxera'), ('Compassos', '17 + anacrusi')],
        total=17,
        secciones=[('A', 1, 4, 'El tema entra', AZUL),
                   ('B', 5, 8, 'El tema continua', OCRE),
                   ('C', 9, 12, 'El diàleg de les mans', AZUL),
                   ('D', 13, 17, 'Final amb calderó', OCRE)],
        ideas=[('LA MELODIA', 'Lenta i cantable',
                'Notes llargues, lligades i amb pocs salts. Cal tocar-la molt suau, com un cant.'),
               ('LES DUES MANS', 'Es passen la música',
                "Mentre una mà toca, l'altra descansa. Les mans parlen per torns."),
               ('LES ALTERACIONS', 'Si♭ i Sol♯ al c. 6',
                "Al c. 6 la mà esquerra fa corxeres i hi ha un Si♭ i un Sol♯: dues tecles negres."),
               ('EL FINAL', 'Calderó',
                "L'última nota té un calderó: s'allarga tant com vulguis, com un petit respir final.")],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            'Hi ha dues alteracions: Si♭ i Sol♯ a la mà esquerra (c. 6).',
            "Comença amb silenci de negra a la dreta i un Sol a l'esquerra (anacrusi).",
            'Matís mp (mig fluix) a les dues mans al principi.',
            "L'últim compàs té un calderó (𝄐): allarga la nota.",
            'No hi ha tempo escrit: tria un pas lent i tranquil.'],
        reto='Toca tota la peça tan suau com puguis, com si el piano fos de vidre.',
        truco="La mà que descansa no és una mà quieta: mantén-la preparada sobre la propera nota.",
        sabias="Chopin va escriure els nocturns per imitar la nit: la música calma que s'escolta abans d'adormir-se. "
               "Aquesta és una versió molt simplificada del famós Nocturn Op. 9 n.º 2.",
        qr_texto='Escolta-la amb els ulls tancats i la partitura al davant.',
        ts=(3, 4),
        cuenta_titulo='Com es compta el 3/4',
        cuenta_pie="Una blanca amb puntet dura tot el compàs: «1-2-3». Tres negres: «1, 2, 3». Les corxeres: «1-i-2-i-3-i».",
        ritmos=[('BLANCA AMB PUNTET', '3/4 · 1-2-3',
                 [{'pitch': 'B4', 'dur': 'h.'}], OCRE, 'treble', None),
                ('TRES NEGRES', '3/4 · 1 · 2 · 3',
                 [_q('B4'), _q('B4'), _q('B4')], AZUL, 'treble', None),
                ('CORXERES', '3/4 · c. 6 · 1-i-2-i-3-i',
                 [{'rest': True, 'dur': 'e'}] + [{'pitch': 'D3', 'dur': 'e', 'beam': g} for g in (0, 0, 1, 1, 1)], VERDE, 'bass', None)]),
    manos=dict(
        izq=[("Anacrusi: Sol", "Comença tu: un Sol (dit 4) abans del c. 1. Compta «3» i toca."),
             ('Gairebé tot són silencis', 'Compta 1-2-3 en cada compàs de silenci. No et distreguis!'),
             ('Les corxeres del c. 6', 'La, Si♭, La, Sol♯, La: suaus i iguals. Mira el ♭ i el ♯ abans de tocar.'),
             ('El calderó', "Al c. 17: Do llarg amb calderó, lligat des del c. 16. Aguanta tant com vulguis.")],
        der=[('Mi lligat', 'C. 1-2: un Mi (dit 3) que dura gairebé dos compassos. Només un so!'),
             ('Mi Re Mi', 'C. 2: tres negres suaus. Fixa\'t en l\'ordre: groc, taronja, groc.'),
             ('Notes llargues', 'Les blanques amb puntet duren tot el compàs: «1-2-3».'),
             ('El motiu final', "Cc. 14-15: La Sol (dit 5) i Fa: tres notes que baixen. Suau, com un suspir.")],
        tecnica=['Toca amb el pes del braç, no amb força de dit.',
                 "La mà que descansa roman relaxada, a prop de les tecles.",
                 'Respira cada dos compassos: la melodia canta.']),
    bloques=[
        B(1, 'anacrusi + cc. 1-4', 'El tema entra', (0, 0),
          D('cadena', 'Silenci + Mi lligat',
            [('esq.: Sol', False), ('cc. 1-2: Mi', False), ('c. 2: Mi Re Mi', False), ('cc. 3-4: Re, Do', True)]),
          [('IZQUIERDA', 'Anacrusi: un Sol (dit 4). Després quatre compassos de silenci.'),
           ('DERECHA', 'C. 1: Mi lligat. C. 2: Mi Re Mi. C. 3: Re llarg. C. 4: Do llarg (blanques amb puntet).'),
           ('JUNTAS', 'L\'esquerra comença; la dreta entra suaument, mp.'),
           ('OJO', 'La lligadura del c. 1 al c. 2: una sola nota, no la toquis dues vegades.')]),
        B(2, 'cc. 5-8', 'El tema continua', (1, 1),
          D('cadena', 'Corxeres a l\'esquerra',
            [('c. 5', False), ('c. 6: esquerra amb corxeres', False), ('cc. 7-8', True)]),
          [('IZQUIERDA', 'C. 6: La Si♭ La Sol♯ La en corxeres. Només aquest compàs té notes.'),
           ('DERECHA', 'C. 5: Mi llarg. C. 6: silenci. C. 7: La (dit 5), Mi. C. 8: Sol llarg.'),
           ('JUNTAS', 'Una mà després de l\'altra: dreta, esquerra, dreta, dreta.'),
           ('OJO', 'Al c. 6 hi ha un ♭ i un ♯: dues tecles negres a l\'esquerra.')]),
        B(3, 'cc. 9-12', 'El diàleg de les mans', (2, 2),
          D('cadena', 'Mi Fa → Re → Mi → Do',
            [('c. 9: Fa Mi', False), ('c. 10: Re llarg', False), ('c. 11: Mi', False), ('c. 12: Do (dit 1)', True)]),
          [('IZQUIERDA', 'Descansa quasi tots els compassos. Al c. 11, una nota (Si).'),
           ('DERECHA', 'C. 9: Fa Mi. C. 10: Re. C. 11: Mi. C. 12: Do (dit 1).'),
           ('JUNTAS', 'Dreta i esquerra no toquen alhora: una cada vegada.'),
           ('OJO', 'Aquí hi ha moltes notes llargues: compta «1-2-3» sempre.')]),
        B(4, 'cc. 13-17', 'Final amb calderó', (3, 3),
          D('cadena', 'Fins al calderó',
            [('cc. 13-14', False), ('cc. 15-16', False), ('c. 17: calderó', True)]),
          [('IZQUIERDA', 'C. 13: La. C. 14: Sol. C. 15: La i Si. Cc. 16-17: Do lligat, amb calderó.'),
           ('DERECHA', 'C. 14: La Sol (dit 5). C. 15: Fa. Cc. 16-17: silenci.'),
           ('JUNTAS', 'Les dues mans fins al Do final. Deixa que soni i respira.'),
           ('OJO', 'Calderó: allarga la nota fins que et sembli que el so s\'esvaeix.')]),
    ],
    lista=["Toco l'anacrusi (Sol) i començo bé.",
           'Faig la lligadura del c. 1-2 sense tornar a tocar.',
           'Toco els cc. 6 (corxeres amb ♭ i ♯).',
           'Respecto el matís mp: tot suau.',
           'Allargo el calderó final.'],
    cortes={1: [246.8, 386.2, 537.8]}, inicio={1: 105.5}, fin={1: 710},
    burb={
        0: [('arriba', 262, 'IZQ', "Anacrusi: Sol (dit 4) a l'esquerra. Compta «3» i entra.", 0.1),
            ('arriba', 262, 'DER', 'Mi lligat (cc. 1-2): una sola nota, no la repeteixis.', 0.35)],
        1: [('arriba', 262, 'OJO', 'C. 6: La Si♭ La Sol♯ La a l\'esquerra, amb ♭ i ♯.', 0.4)],
        2: [('arriba', 262, 'DER', 'Fa Mi · Re · Mi · Do: la melodia baixa pas a pas.', 0.3)],
        3: [('arriba', 262, 'OJO', 'Calderó al Do final: allarga la nota.', 0.88)],
    },
    misol=dict(
        manos="Un nocturn és música de nit: toca-la suau, com si algú dormís a l'habitació del costat.",
        guia="Hi ha molts compassos de silenci: compta-los sempre! Un silenci també forma part de la música.",
        pauta="Escriu un Sol a la pauta amb la clau de fa i pinta'l de blau."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu un Sol i un Do amb els seus colors")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_nocturne.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
