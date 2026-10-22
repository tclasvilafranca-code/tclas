# -*- coding: utf-8 -*-
"""Peça 8 · You've Got a Friend in Me, versió fàcil (Randy Newman · arr. Megan Harper).
   MESURAT sobre el PDF (1 pàgina, carta; notes pintades amb colorear_notas.py): sense armadura,
   4/4, sense tempo ni matisos, 12 compassos en 3 sistemes de 4. Esquerra: UNA rodona per compàs:
   Do4 | Si♭3 | Fa3 | Mi3 | Fa3 | Sol♯3 | Fa3 | La3 | Fa3 | La3 | Re3 | Do3.
   Dreta: c. 1 Mi Sol♪Mi♪ La Sol; c. 2 Mi (rodona); c. 3 La Do♪La♪ Do La; c. 4 Sol (rodona);
   c. 5 silenci de corxera + notes de corxera/negra (La Fa Sol Do); c. 6 Si Si Do La Sol; c. 7 Do La Sol La Mi Do;
   c. 8 Mi Mi Mi; c. 9 silenci de corxera + escala de corxeres La Si Re Do Sol Mi Do; c. 10 Re♯ Mi Do La;
   c. 11 Do La♪Sol♪ Mi Do; c. 12 Do (rodona). Alteracions: Si♭ (esq. c. 2), Sol♯ (esq. c. 6), Re♯ (dta. c. 10)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}
_e = lambda g: {'pitch': 'B4', 'dur': 'e', 'beam': g}

SPEC = dict(
    num=8, slug='friend', pdf='friend.pdf', time_sig=(4, 4),
    titulo="You've Got a Friend in Me (fàcil)",
    autor='Randy Newman · arr. Megan Harper',
    kicker=kick(8, "You've Got a Friend in Me"), mes=MESES[8],
    yt=yt("you've got a friend in me piano easy toy story"),
    credito="Partitura: arr. Megan Harper (MuseScore). Notes pintades i anotacions: T-Clas.",
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense armadura'), ('Compàs', '4/4'), ('Tempo', 'No indicat'),
               ('Figura curta', 'Corxera'), ('Compassos', '12')],
        total=12,
        secciones=[('A', 1, 4, "«You've got a friend in me»", AZUL),
                   ('A', 5, 8, 'Segona frase', OCRE),
                   ('B', 9, 12, 'Final', AZUL)],
        ideas=[('LA MÀ ESQUERRA', 'Una rodona per compàs',
                'Una sola nota llarga cada compàs: Do, Si♭, Fa, Mi... Quatre temps cadascuna.'),
               ('LA MÀ DRETA', 'Negres i corxeres',
                'La melodia combina negres, corxeres i algun silenci. Mira els colors!'),
               ('ELS SILENCIS', 'Entra una mica tard',
                'Als cc. 5 i 9 hi ha un silenci de corxera: la melodia entra mig temps després.'),
               ('LES ALTERACIONS', 'Si♭, Sol♯ i Re♯',
                'Tres tecles negres: Si♭ a l\'esquerra (c. 2), Sol♯ a l\'esquerra (c. 6) i Re♯ a la dreta (c. 10).')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            'No hi ha armadura, però sí tres alteracions: Si♭ (c. 2), Sol♯ (c. 6) i Re♯ (c. 10).',
            "L'esquerra toca una rodona (quatre temps) a cada compàs.",
            'Hi ha silencis de corxera al principi dels cc. 5 i 9.',
            'Els compassos 2, 4 i 12 de la mà dreta són rodones: quatre temps.',
            'No hi ha tempo escrit: tria un pas alegre i constant.'],
        reto='Toca la cançó amb les dues mans: la dreta canta, l\'esquerra aguanta la nota llarga.',
        truco="Fixa't que cada compàs només té una nota a l'esquerra: aprèn-la com una escala de notes llargues.",
        sabias="Randy Newman va escriure aquesta cançó per a la pel·lícula Toy Story (1995). "
               "Woody la canta a Buzz Lightyear.",
        qr_texto='Escolta-la i canta amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo='Com es compta el c. 1 i el c. 5',
        cuenta_pie="Negra, dues corxeres, negra, negra: «1, 2-i, 3, 4». Silenci de corxera: la primera «i» és buida.",
        ritmos=[('EL COMPÀS 1', '4/4 · negra, dues corxeres, negra, negra',
                 [_q('B4'), _e(0), _e(0), _q('B4'), _q('B4')], OCRE, 'treble', None),
                ('SILENCI DE CORXERA', '4/4 · c. 9 · silenci + set corxeres',
                 [{'rest': True, 'dur': 'e'}] + [_e(0), _e(0), _e(0), _e(1), _e(1), _e(1), _e(1)],
                 AZUL, 'treble', None)]),
    manos=dict(
        izq=[('Una rodona per compàs', 'Una nota quatre temps. Prem la tecla i compta 1-2-3-4.'),
             ('Dos canvis de nota', 'Cc. 1-4: Do, Si♭, Fa, Mi. La mà baixa i puja com si fes escales.'),
             ('Sol♯ al c. 6', 'Una tecla negra. Mira el símbol ♯ abans de tocar-la.'),
             ('El final: Re i Do', 'Cc. 11-12: Re i Do. La mà descansa i acaba.')],
        der=[('Mi Sol Mi La Sol', 'C. 1: negra, dues corxeres, negra, negra. Mi, Sol-Mi, La, Sol.'),
             ('Rodones', 'Als cc. 2, 4 i 12: una nota per compàs. Aguanta i compta fins a 4.'),
             ('La corxera del c. 5', 'El silenci de corxera: entra mig temps tard. Compta «1-i-2».'),
             ('El Re♯ del c. 10', 'Una tecla negra: Re♯. Es toca amb el mateix dit que el Re i s\'ajusta a la tecla del costat.')],
        tecnica=['Compta 1-2-3-4 en veu alta, també quan hi ha rodones.',
                 "Mà esquerra suau: l'acompanyament no ha de tapar la melodia.",
                 'Les tres alteracions són tecles negres: mira-les abans.']),
    bloques=[
        B(1, 'cc. 1-4', "You've got a friend in me", (0, 0),
          D('cadena', 'Mi Sol Mi La Sol → Mi → La Do La Do La → Sol',
            [('c. 1', False), ('c. 2: Mi llarg', False), ('c. 3', False), ('c. 4: Sol llarg', True)]),
          [('IZQUIERDA', 'Do, Si♭, Fa, Mi: una rodona per compàs. Mira el Si♭ al c. 2.'),
           ('DERECHA', 'C. 1: Mi Sol Mi La Sol. C. 2: Mi llarg. C. 3: La Do La Do La. C. 4: Sol llarg.'),
           ('JUNTAS', 'Compàs a compàs: la dreta canta i l\'esquerra aguanta la nota.'),
           ('A TEMPO', 'Canta la cançó mentre toques. Alegre i sense córrer.')]),
        B(2, 'cc. 5-8', 'Segona frase', (1, 1),
          D('cadena', 'Silenci + melodia',
            [('c. 5', False), ('c. 6: Sol♯', False), ('c. 7', False), ('c. 8', True)]),
          [('IZQUIERDA', 'Fa, Sol♯, Fa, La: una rodona per compàs. El Sol♯ és una tecla negra.'),
           ('DERECHA', 'C. 5: silenci de corxera i notes. C. 6: Si Si Do La Sol. C. 7: Do La Sol La Mi Do. C. 8: Mi Mi Mi.'),
           ('JUNTAS', 'Dos compassos cada cop: mira el Sol♯ de l\'esquerra.'),
           ('OJO', 'Al c. 5 hi ha un silenci de corxera: entra mig temps tard.')]),
        B(3, 'cc. 9-12', 'Final: de corxera a rodona', (2, 2),
          D('cadena', 'Una escala de corxeres → Re♯ → Do final',
            [('c. 9: corxeres', False), ('c. 10: Re♯', False), ('c. 11', False), ('c. 12: Do', True)]),
          [('IZQUIERDA', 'Fa, La, Re, Do: una rodona per compàs.'),
           ('DERECHA', 'C. 9: La Si Re Do Sol Mi Do en corxeres. C. 10: Re♯ Mi Do La. C. 11: Do La Sol Mi Do. C. 12: Do llarg.'),
           ('JUNTAS', 'Quan la dreta corre amb corxeres, l\'esquerra aguanta la nota. No correguis!'),
           ('OJO', 'Les corxeres del c. 9 van el doble de ràpides: compta «1-i-2-i».')]),
        B(4, 'cc. 1-12', 'Tota la cançó', (0, 2),
          D('cadena', 'De dalt a baix',
            [('cc. 1-4', False), ('cc. 5-8', False), ('cc. 9-12', True)]),
          [('IZQUIERDA', 'Les dotze notes llargues de l\'esquerra, una després de l\'altra.'),
           ('DERECHA', 'La melodia sencera, cantant la lletra.'),
           ('JUNTAS', 'Les dues mans fins al Do final.'),
           ('A TEMPO', 'Alegre i sense córrer: com si fossis en Woody!')]),
    ],
    lista=["Toco l'esquerra: dotze notes llargues, una per compàs.",
           'Toco el Si♭, el Sol♯ i el Re♯ al seu lloc.',
           'Entro bé després del silenci de corxera (cc. 5 i 9).',
           'Toco la melodia de la dreta de memòria.',
           'Toco els 12 compassos sense parar.'],
    cortes={1: [214.5, 362.0]}, inicio={1: 95}, fin={1: 495},
    burb={
        0: [('arriba', 262, 'DER', 'Mi Sol Mi La Sol (c. 1) i La Do La Do La (c. 3). Rodones als cc. 2 i 4.', 0.15),
            ('arriba', 262, 'OJO', 'Si♭ a la mà esquerra (c. 2): tecla negra a l\'esquerra del Si.', 0.48)],
        1: [('arriba', 262, 'OJO', 'Silenci de corxera al c. 5: la dreta entra mig temps tard.', 0.05),
            ('arriba', 262, 'IZQ', 'Sol♯ a l\'esquerra al c. 6: tecla negra a la dreta del Sol.', 0.35)],
        2: [('arriba', 262, 'DER', 'Corxeres: la, si, re, do, sol, mi, do. Compta «1-i-2-i».', 0.1),
            ('arriba', 262, 'OJO', 'Re♯ a la dreta al c. 10.', 0.4)],
    },
    misol=dict(
        manos="Els silencis són música callada: compta'ls igual que les notes.",
        guia="L'esquerra només té una nota per compàs! Aprèn-la primer i la dreta anirà sola.",
        pauta="Escriu les dotze notes de la mà esquerra, una per compàs, amb els seus colors."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu les notes de l'esquerra: Do, Si♭, Fa, Mi")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_friend.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
