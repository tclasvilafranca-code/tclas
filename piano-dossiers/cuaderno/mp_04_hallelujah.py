# -*- coding: utf-8 -*-
"""Pieza 4 · Hallelujah (Leonard Cohen), arreglo de sheetsfree. MEDIDO sobre el PDF (3 pags,
   tamano carta, 17 sistemas de 4 compases = 68 compases): 6/8, "Moderately slow, in 2", negra con
   puntillo = 60, mp, Do mayor sin armadura; barra de repeticion al empezar el c. 5 y casillas
   "1, 2." (c. 29) y "3." (cc. 30-32); doble barra y armadura de dos sostenidos (Re mayor) desde
   el c. 33; "rit." y calderon final; corchea la figura mas corta; izquierda en arpegios de seis
   corcheas por compas (Do, La menor...)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=4, slug='hallelujah', pdf='leonard_cohen_hallelujah.pdf', time_sig=(6, 8),
    titulo='Hallelujah', autor='Leonard Cohen · arranjament per a piano (sheetsfree)',
    kicker='Eva · peça 4 · Hallelujah', mes='Desembre · 2.ª quinzena (concert de Nadal)',
    yt='https://www.youtube.com/results?search_query=hallelujah+leonard+cohen+piano+tutorial',
    credito='Partitura: Leonard Cohen, Hallelujah (sheetsfree.com). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major → Re major'), ('Compàs', '6/8'), ('Tempo', '♩. = 60 lent'),
               ('Figura curta', 'Corxera'), ('Compassos', '68')],
        total=68,
        secciones=[('A', 1, 4, 'Introducció', AZUL), ('B', 5, 32, 'Do major · es repeteix', OCRE),
                   ('C', 33, 68, 'Re major · final', AZUL)],
        ideas=[('IZQUIERDA', 'Arpegi de sis corxeres',
                'Cada compàs, una figura que puja i baixa sobre l\'acord. Gairebé no canvia en '
                'tota la peça.'),
               ('DERECHA', 'Melodia i després acords',
                'Comença amb notes soltes i, en canviar de tonalitat, passa a notes dobles amb '
                'lligadures llargues.'),
               ('LA REPETICIÓ', 'Tres voltes, tres caselles',
                'Des del c. 5 es repeteix. Les dues primeres vegades vas a la casella 1, 2; la '
                'tercera, a la 3.'),
               ('EL CANVI', 'Do major → Re major',
                'Al c. 33 apareix una doble barra i dos sostinguts: puja un to.')],
        especial=[
            'Hi diu "Moderately slow, in 2" i negra amb punt = 60: lent i a dos.',
            'El compàs és 6/8: dos temps, cadascun de tres corxeres.',
            'Els cc. 5-28 es repeteixen: casella "1, 2." (c. 29) i casella "3." (cc. 30-32).',
            'Al c. 33 hi ha doble barra i dos sostinguts: Re major (fa♯ i do♯).',
            'L\'esquerra fa el mateix arpegi de sis corxeres quasi tot el temps.',
            'Acaba amb "rit." i un calderó a l\'últim acord.'],
        reto='Mantenir l\'arpegi de l\'esquerra sempre igual mentre la dreta canta, i '
             'recordar per on vas a les repeticions i les caselles.',
        truco='Abans de tocar, recorre la partitura amb el dit seguint les repeticions: '
              '5 → 29 → 5 → 29 → 5 → 30-32 → 33. Quan ho sàpigues, toca.',
        sabias='Leonard Cohen va publicar «Hallelujah» el 1984, al disc «Various Positions». Es va fer famosa amb la versió de Jeff Buckley, de 1994.',
        qr_texto='Escolta-la a poc a poc i compta "un-dos" amb el cap: és un 6/8 lent.',
        ts=(6, 8)),
    manos=dict(
        izq=[('Un arpegi, un compàs', 'Cada compàs són sis corxeres que pugen i baixen sobre '
                                      'l\'acord. Toca només el primer compàs, a poc a poc, deu '
                                      'vegades seguides sense fallar.'),
             ('Canviar d\'acord', 'El dibuix és el mateix i canvia la posició. Abans de tocar, '
                                  'mira quin acord ve i col·loca ja la mà.'),
             ('Regular i suau', 'Metrònom lent, sis corxeres iguals i en mp: la melodia mana.'),
             ('De memòria', 'Si saps el dibuix, només has de saber on canvia: aprèn-lo '
                            'sense partitura.')],
        der=[('Comptar a dos', 'En 6/8 lent comptes dos temps: 1-2-3, 4-5-6. La melodia '
                               'comença amb negres amb punt.'),
             ('Corxera i punt', 'Llegeix les notes soltes amb el seu ritme: digues-lo en veu '
                                'alta "ta-a-a ta-a-a" abans de tocar.'),
             ('Notes lligades i dobles', 'Des del c. 33 la dreta toca notes dobles amb '
                                         'lligadures: mantén la lligada, no la repeteixis.'),
             ('Amb l\'esquerra', 'Uneix a poc a poc un sistema amb l\'esquerra ja segura. Si es '
                                 'trenca, torna a una mà.')],
        tecnica=['Canell solt: l\'arpegi surt sol si no fas força.',
                 'Compta a dos, a poc a poc: 1-2-3, 4-5-6.',
                 'Mira on comença i on acaba cada repetició abans de tocar.']),
    bloques=[
        B(1, 'cc. 1-4', 'La introducció', (0, 0),
          D('cuenta', '6/8 lent: dos temps de tres corxeres', [('un compàs', 2, 3)]),
          [('IZQUIERDA', 'Arpegi de sis corxeres per compàs: Do, La menor, Do, La menor.'),
           ('DERECHA', 'Notes llargues amb punt; canta-les i compta-les senceres.'),
           ('JUNTAS', 'Compàs a compàs, i després els quatre.'),
           ('A TEMPO', 'negra amb punt = 60: molt a poc a poc, a dos.')]),
        B(2, 'cc. 5-12', 'Comença la repetició', (1, 2),
          D('cadena', 'Des d\'aquí es repeteix', [('barra |: al c. 5', False),
                                                 ('toques fins a la casella', True)]),
          [('IZQUIERDA', 'El mateix arpegi; l\'acord canvia a cada compàs.'),
           ('DERECHA', 'Apareixen corxeres i lligadures entre notes: llegeix-les a poc a poc.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 5-8 i cc. 9-12.'),
           ('OJO', 'La barra amb punts del c. 5 marca on es torna.')]),
        B(3, 'cc. 13-28', 'El que es repeteix', (3, 6),
          D('capas', 'Dues capes alhora',
            [('Dreta: melodia', 'barras', AZUL), ('Esquerra: arpegi', 'puntos', OCRE)]),
          [('IZQUIERDA', 'Segueix l\'arpegi: el difícil és no frenar en canviar d\'acord.'),
           ('DERECHA', 'Les frases acaben en notes llargues lligades: respira aquí.'),
           ('JUNTAS', 'Un sistema cada dia fins al c. 28.'),
           ('OJO', 'Això es toca tres vegades: cuida\'l, que l\'escoltaràs moltes vegades.')]),
        B(4, 'cc. 29-32', 'Les caselles', (7, 7),
          D('cadena', 'Les tres voltes',
            [('casella 1, 2 (c. 29)', False), ('↩ al c. 5', False), ('3.ª vegada: casella 3', True)]),
          [('IZQUIERDA', 'Segueix l\'arpegi a les dues caselles.'),
           ('DERECHA', 'A la casella 3 hi ha un compàs de silenci: compta\'l.'),
           ('JUNTAS', 'Recorre el camí amb el dit abans de tocar.'),
           ('OJO', 'Les dues primeres vegades, casella 1, 2 i torna al c. 5.')]),
        B(5, 'cc. 33-44', 'Canvi a Re major', (8, 10),
          D('cadena', 'L\'armadura canvia', [('Do major: sense alteracions', False),
                                             ('Re major: fa♯ i do♯', True)]),
          [('IZQUIERDA', 'La mateixa figura, però ara amb sostinguts: fa♯ i do♯.'),
           ('DERECHA', 'Notes dobles i lligadures llargues: toca-les pesades i cantades.'),
           ('JUNTAS', 'Un sistema cada dia, sense pressa.'),
           ('OJO', 'Dos sostinguts al principi de cada pentagrama: valen per a tota la peça.')]),
        B(6, 'cc. 45-60', 'Re major', (11, 14),
          D('capas', 'Dues capes alhora',
            [('Dreta: notes dobles', 'barras', AZUL), ('Esquerra: arpegi', 'puntos', OCRE)]),
          [('IZQUIERDA', 'L\'arpegi de sempre en Re major: cuida els sostinguts.'),
           ('DERECHA', 'Notes dobles amb lligadura: mantén la lligada i canvia l\'altra.'),
           ('JUNTAS', 'Dos sistemes cada vegada.'),
           ('OJO', 'És el tram més llarg: dividiu-lo per sistemes.')]),
        B(7, 'cc. 61-68', 'El final', (15, 16),
          D('cadena', 'Cap al final', [('notes llargues lligades', False), ('rit.', False),
                                       ('calderó', True)]),
          [('IZQUIERDA', 'Segueix l\'arpegi fins a l\'últim compàs.'),
           ('DERECHA', 'Notes llargues lligades: compta-les senceres.'),
           ('JUNTAS', 'Els dos últims sistemes en bucle.'),
           ('A TEMPO', 'rit.: frena a poc a poc. Allarga l\'últim acord.')]),
    ],
    cortes={1: [225.0, 344.8, 460.5, 583.2], 2: [162.0, 267.8, 387.0, 498.5, 612.5],
            3: [157.8, 266.0, 379.8, 488.8, 596.0]},
    corte_titulo=103.5, inicio={2: 47.0, 3: 44.5}, fin={1: 688.5},
    burb={
        0: [('arriba', 330, 'AMB', 'Moderately slow, in 2: lent i a dos. Negra amb punt = 60: '
                                   'dos temps per compàs, cadascun de tres corxeres.', 0.3),
            ('abajo', 300, 'IZQ', 'Un arpegi per compàs: sis corxeres que pugen i baixen. '
                                  'A poc a poc i regular.', 0.25)],
        1: [('arriba', 330, 'OJO', 'La barra amb punts a l\'inici d\'aquest sistema marca on es '
                                   'torna cada cop que es repeteix.', 0.05)],
        4: [('arriba', 300, 'DER', 'Les frases acaben en una nota llarga lligada: respira aquí, '
                                   'abans de començar la següent.', 0.5)],
        7: [('arriba', 330, 'OJO', 'Caselles: les dues primeres vegades toques la casella "1, 2." '
                                   'i tornes al c. 5. La tercera, la casella "3.".', 0.3)],
        8: [('arriba', 330, 'AMB', 'Doble barra i dos sostinguts: la tonalitat canvia a Re major '
                                   '(fa♯ i do♯ a tota la peça).', 0.05)],
        9: [('arriba', 330, 'DER', 'Ara la dreta toca notes dobles amb lligadures: mantén la '
                                   'lligada i no la repeteixis.', 0.3)],
        13: [('arriba', 300, 'IZQ', 'La mateixa figura de l\'esquerra, ara en Re major: cuida els '
                                    'sostinguts.', 0.2)],
        16: [('arriba', 330, 'AMB', 'rit. i calderó: frena a poc a poc i allarga l\'últim acord '
                                    'fins que s\'apagui.', 0.8)],
    },
    marcas=[],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Do major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_hallelujah.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
