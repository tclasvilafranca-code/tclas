# -*- coding: utf-8 -*-
"""Peça 11 · I Have a Dream (ABBA · versió fàcil «children song», MuseScore).
   MESURAT sobre el PDF (2 pàgines, A4; notes pintades amb colorear_notas.py): sense armadura, 4/4,
   «TEMPO-120» (♩ = 120 segons el títol), 29 compassos: pàg. 1 en 5 sistemes (cc. 1-6, 7-12, 13-17, 18-21,
   22-25) i pàg. 2 en 1 sistema (cc. 26-29). Anacrusi: silenci de negra al c. 1. Lletra impresa en anglès.
   Figures: negres, blanques, rodones, negra amb puntet, corxeres unides, lligadures i silencis.
   Esquerra: acords de dues notes mantinguts (Do3+Sol3, Si3+Sol3, Do3+Fa3, ...); final: Do3/Sol3 i silenci."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}
_e = lambda g: {'pitch': 'B4', 'dur': 'e', 'beam': g}

SPEC = dict(
    num=11, slug='dream', pdf='dream.pdf', time_sig=(4, 4),
    titulo='I Have a Dream',
    autor='ABBA · versió fàcil (children song)',
    kicker=kick(11, 'I Have a Dream'), mes=MESES[11],
    yt=yt('i have a dream abba piano easy'),
    credito='Partitura: versió fàcil (MuseScore). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense armadura'), ('Compàs', '4/4'), ('Tempo', '♩ = 120'),
               ('Figura curta', 'Corxera'), ('Compassos', '29')],
        total=29,
        secciones=[('A', 1, 12, '«I have a dream…»', AZUL),
                   ('B', 13, 17, '«You can take the future»', OCRE),
                   ('C', 18, 25, '«I believe in angels»', AZUL),
                   ('D', 26, 29, 'Final: «I have a dream»', OCRE)],
        ideas=[('LA MELODIA', 'Moltes notes lligades',
                'Hi ha notes que s\'allarguen de compàs a compàs (lligadures). Només es toquen una vegada.'),
               ("L'ESQUERRA", 'Acords de dues notes',
                'Dues notes alhora, mantingudes: Do+Sol, Si+Sol, Do+Fa… com un coixí per sota de la veu.'),
               ('EL RITME', 'Puntet i corxeres',
                'Combina notes llargues amb petits grups de corxeres que baixen o pugen.'),
               ('LA LLETRA', 'Cantada en anglès',
                'La partitura porta la lletra escrita: canta-la mentre toques per saber on respirar.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            'No hi ha armadura ni alteracions: només notes blanques.',
            'El títol diu «TEMPO-120»: unes 120 negres per minut (alegre, mig-ràpid).',
            'Comença amb un silenci de negra: compta-hi bé abans d\'entrar.',
            'Hi ha moltes lligadures: notes unides que s\'allarguen sobre la barra del compàs.',
            'És la peça més llarga de les que has tocat: 29 compassos, en dues pàgines.'],
        reto='Toca sencers els 29 compassos, sense aturar-te, cantant la lletra.',
        truco="Divideix-la en 4 frases (A, B, C, D). Aprèn-ne una cada setmana i, al final, junta-les.",
        sabias="«I Have a Dream» és de ABBA, un grup suec, i va sortir l'any 1979. "
               "La nena protagonista de la cançó somia que, amb una mica de màgia, tot pot sortir bé.",
        qr_texto='Escolta-la i canta amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo='Com es compta el c. 1',
        cuenta_pie="Silenci de negra + negra amb puntet + corxera: «(1) 2-3 i 4». Aquí només el ritme.",
        ritmos=[('EL COMPÀS 1', '4/4 · silenci, negra, negra amb puntet, corxera',
                 [{'rest': True, 'dur': 'q'}, _q('B4'), {'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e'}],
                 OCRE, 'treble', None),
                ('QUATRE CORXERES', '4/4 · 1-i-2-i',
                 [_e(0), _e(0), _e(0), _e(0)], AZUL, 'treble', None)]),
    manos=dict(
        izq=[('Dues notes juntes', 'Acords de dues notes mantingudes: Do+Sol, Si+Sol. Prem-les alhora i aguanta.'),
             ('Canvis lents', 'Els acords canvien cada un o dos compassos: mira el color de la nota més baixa.'),
             ('Els silencis', 'Hi ha compassos on l\'esquerra descansa: compta «1-2-3-4».'),
             ('El final', 'Al c. 28: Do, Sol, Sol: tres notes soltes. Torna a descansar.')],
        der=[('Sol Mi Re', 'La melodia comença amb Sol (greu), Mi, Re: dits 1-3-2 en posició de Do.'),
             ('Lligadures', 'Una nota unida a la següent: només es toca la primera, però dura els dos compassos.'),
             ('Corxeres que pugen', 'Cc. 8, 13, 19: grups de corxeres que pugen. Compta «1-i-2-i».'),
             ('Frase final', 'C. 29: Do llarg lligat, final tranquil.')],
        tecnica=['Respira entre frases, com cantant.',
                 'Les lligadures: el dit queda a la tecla mentre sona.',
                 "Si et perds, torna a l'inici de la frase, no al de la peça."]),
    bloques=[
        B(1, 'cc. 1-6', 'I have a dream, a song to sing', (0, 0),
          D('cadena', 'Frase 1',
            [('anacrusi', False), ('I have a dream', False), ('a song to sing', True)]),
          [('IZQUIERDA', 'Acords de dues notes: Do+Sol, Si+Sol... aguanta cada acord.'),
           ('DERECHA', 'Cc. 1-2: Sol Mi Re i Fa llarg. Cc. 3-4: Sol Do Si i Do llarg. Cc. 5-6: Sol Mi Re i Fa llarg.'),
           ('JUNTAS', 'Compta el silenci del c. 1 i entra amb l\'acord de l\'esquerra.'),
           ('A TEMPO', 'Canta «I have a dream, a song to sing»: la melodia ja la saps.')]),
        B(2, 'cc. 7-12', 'If you see the wonder of a fairy tale', (1, 1),
          D('cadena', 'Frase 2',
            [('cc. 7-8', False), ('cc. 9-10', False), ('cc. 11-12', True)]),
          [('IZQUIERDA', 'Acords de dues notes: Do+Sol, ... Cada acord dura dos o quatre temps.'),
           ('DERECHA', 'Cc. 7-8: Do lligat, Mi Fa Sol La... Corxeres que pugen. Cc. 9-12: segueix la lletra.'),
           ('JUNTAS', 'Quan la dreta fa corxeres, l\'esquerra aguanta.'),
           ('OJO', 'Lligadures: aquí hi ha dues notes unides per un arc. Una sola nota!')]),
        B(3, 'cc. 13-17', 'You can take the future', (2, 2),
          D('cadena', 'Frase 3',
            [('c. 13', False), ('c. 14-15', False), ('c. 16-17', True)]),
          [('IZQUIERDA', 'Do+Sol i Si+Sol, un parell de rodones lligades.'),
           ('DERECHA', 'Notes llargues i corxeres que pugen: Do Re Mi Fa Sol...'),
           ('JUNTAS', 'Mira els colors: les notes de la dreta pugen pas a pas.'),
           ('OJO', 'Aquesta frase té notes llargues lligades. Només toca la primera!')]),
        B(4, 'cc. 18-29', 'El cor i el final', (3, 5),
          D('cadena', 'Del cor al final',
            [('cc. 18-21: I believe in angels', False), ('cc. 22-25', False), ('cc. 26-29: final', True)]),
          [('IZQUIERDA', 'Acords mantinguts. Al c. 28: Do, Sol, Sol. Al c. 29, silenci.'),
           ('DERECHA', 'Cc. 18-25: «I believe in angels» i «When I know the time is right». C. 29: Do llarg lligat.'),
           ('JUNTAS', 'Quan canvia l\'acord, canvia la melodia. Lent i amb sentiment al final.'),
           ('A TEMPO', 'Toca tota la cançó des del principi: dues pàgines, sense parar.')]),
    ],
    lista=['Sé tocar les dues mans dels cc. 1-6 de memòria.',
           'Faig bé les lligadures (no repeteixo la segona nota).',
           'Toco les corxeres que pugen amb claredat.',
           'Canto la lletra mentre toco.',
           'Toco els 29 compassos sense parar.'],
    cortes={1: [220.5, 362.8, 492.2, 626.2], 2: []}, inicio={1: 98, 2: 47}, fin={1: 775, 2: 175},
    burb={
        0: [('arriba', 262, 'AMB', 'Anacrusi: un silenci de negra. Compta «1» i entra al 2.', 0.1),
            ('arriba', 262, 'DER', 'Sol Mi Re i Fa llarg: «I have a dream».', 0.25)],
        1: [('arriba', 262, 'IZQ', 'Acords de dues notes: Do+Sol, ... sense moure massa la mà.', 0.2),
            ('arriba', 262, 'OJO', 'Lligadura: la nota llarga no es torna a tocar.', 0.45)],
        2: [('arriba', 262, 'DER', 'Corxeres que pugen: «You can take the future».', 0.3)],
        3: [('arriba', 262, 'AMB', 'El cor: «I believe in angels». La part més coneguda.', 0.3)],
        4: [('arriba', 262, 'DER', 'Cc. 22-25: «When I know the time is right for me».', 0.3)],
        5: [('arriba', 262, 'OJO', 'Final: «I have a dream». Lent i amb la darrera nota llarga (Do).', 0.7)],
    },
    misol=dict(
        manos="Quan una nota té un arc a sobre (lligadura), la toques una vegada però la deixes sonar tot el temps!",
        guia="Aquesta peça és llarga: no ho facis tot d'una. Una frase per setmana i en un mes la tens.",
        pauta="Escriu a la pauta les primeres quatre notes de la melodia: Sol, Mi, Re, Fa."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu Sol Mi Re Fa i pinta les notes")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_dream.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
