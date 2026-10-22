# -*- coding: utf-8 -*-
"""Peça 4 · Melodische Übungsstücke n. 3, op. 149 (Diabelli), a quatre mans. MESURAT sobre el
   PDF (3 pàgines A4; Secondo a les pp. 1-2 i Primo a les pp. 2-3, 56 compassos cadascun):
   2/4, Moderato sense metrònom, sense armadura (Do major, amb alteracions). Repeticions: cc.
   1-17 i 18-32 (barres al final del c. 17 i del c. 32), igual al Primo i al Secondo. Matisos:
   p (c. 1), f (Secondo c. 9, Primo c. 8), sf (c. 21 Secondo / c. 23 Primo), p, mf, f, <, >, sf,
   calderó al c. 56 (dues parts); Primo amb 8va tot el temps; semicorxera (ritme amb puntet cc.
   45-52 del Primo) i nota d'adorn al c. 38 del Primo. Alteracions: Sol♯ (c. 21) i Sol becaire
   (c. 22) al Secondo, sostingut al c. 33."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=4, slug='melodische', pdf='melodishe_diabelli_4_manos.pdf', time_sig=(2, 4),
    titulo='Melodische Übungsstücke, n. 3', autor='Anton Diabelli · op. 149 · a quatre mans',
    kicker='Txell · peça 4 · Diabelli, op. 149 n. 3', mes='Gener',
    yt='https://www.youtube.com/results?search_query=diabelli+melodische+ubungsstucke+op+149+piano+4+hands',
    credito='Partitura: A. Diabelli, op. 149 n. 3 (Mutopia Project, BSD). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '2/4'), ('Tempo', 'Moderato'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '56')],
        total=56,
        secciones=[('A', 1, 17, 'Primera part (es repeteix)', AZUL),
                   ('B', 18, 32, 'Segona part (es repeteix)', OCRE),
                   ('C', 33, 56, 'Final', AZUL)],
        ideas=[('SECONDO', 'Acompanya',
                'Grups de corxeres lligades sobre notes soltes amb silencis: és '
                "l'acompanyament."),
               ('PRIMO', 'Canta',
                'Comença amb corxeres lligades i passa a «silenci de corxera + corxera» a cada '
                'temps.'),
               ('ELS MATISOS', 'p · f · mf · sf',
                'Alterna piano i forte, amb reguladors i algun sf (accent fort).'),
               ('EL FINAL', 'Calderó',
                "Els dos acaben amb un calderó a l'últim compàs.")],
        ideas_titulo='La peça en quatre idees',
        especial=[
            'Posa «Moderato» i el compàs és 2/4: dues negres per compàs.',
            "És a quatre mans: el Secondo (pp. 1-2) i el Primo (pp. 2-3) tenen cadascú la seva "
            "part completa.",
            'Hi ha dues repeticions: els cc. 1-17 i els cc. 18-32 es toquen dues vegades.',
            "El Primo va amb 8va: sona una octava més aguda del que hi ha escrit.",
            "El Primo porta ritme amb puntet (cc. 45-52) i una nota d'adorn (c. 38).",
            "Acaba amb un calderó a l'últim compàs."],
        reto="Que les dues parts encaixin: el Primo canta i el Secondo acompanya sense tapar-lo. "
             "Aconseguiu-ho?",
        truco="Estudieu per torns: una toca i l'altra compta «un-dos» en veu alta. Després "
              "canvieu. Quan sapigueu les dues parts, juntes!",
        sabias="És la n. 3 de les 28 peces melòdiques a quatre mans, op. 149, de Diabelli "
               "(1781-1858), l'editor vienès del vals sobre el qual Beethoven va escriure les "
               "33 variacions.",
        qr_texto='Escolta-la i segueix la teva part amb el dit: on respira el Primo?',
        ts=(2, 4),
        cuenta_titulo='Com es compta el c. 1',
        cuenta_pie='Un compàs de 2/4: dues negres, i cada negra són dues corxeres. Aquí només '
                   'el ritme.'),
    manos=dict(
        titulo='Secondo i Primo', sub="Cada part s'aprèn sola. Després, juntes i a poc a poc.",
        tit_izq='SECONDO · la part greu', tit_der='PRIMO · la part aguda',
        izq=[('Un grup cada cop', 'Aprèn un compàs de quatre corxeres lligades. Toca\'l a poc a '
                                  'poc, deu vegades seguides sense fallar.'),
             ('Les notes soltes', 'A baix hi ha notes soltes amb silencis. Toca només aquesta '
                                  'línia i compta «un-dos».'),
             ('Les dues línies', 'Ajunta-les: corxeres a dalt, notes soltes a baix, en p.'),
             ('Els canvis', 'Vigila els matisos: p, f, mf. Canvien de cop.')],
        der=[('Lligadures', "Al principi, corxeres lligades. Cada lligadura és un gest: so a la "
                            "primera, suau a la segona."),
             ('Silenci de corxera', 'Més endavant, cada compàs comença amb un silenci. Compta\'l: '
                                    'el silenci dura, no te\'l saltis.'),
             ('Puntet i adorn', "Als cc. 38 i 45-52 hi ha una nota d'adorn i ritmes amb puntet. "
                                "Estudia'ls sols i a poc a poc."),
             ('Amb el Secondo', 'Toqueu juntes a poc a poc. El Primo escolta el Secondo.')],
        tecnica=['Canells solts, dits corbats i so regular.',
                 'Compta «un-dos» en veu alta: cada compàs, dues negres.',
                 "Canvieu de part: així s'aprenen les dues."]),
    bloques=[
        B(1, 'Secondo cc. 1-8', "L'entrada", (0, 0),
          D('capas', 'Dues línies alhora',
            [('Corxeres lligades', 'puntos', OCRE, 6), ('Notes soltes', 'barras', OCRE)]),
          [('SECONDO', 'A dalt, quatre corxeres lligades. A baix, negra i silenci. En p.'),
           ('PRIMO', 'Escolta aquest bloc: la teva part el decorarà després.'),
           ('JUNTAS', 'Llegiu la partitura de l\'altre mentre toqueu la vostra.'),
           ('OJO', 'Compta «un-dos» abans d\'entrar.')]),
        B(2, 'Secondo cc. 9-17', 'Forte i repetició', (1, 1),
          D('cadena', 'El recorregut',
            [('cc. 1-17', False), ('↩ c. 1', False), ('cc. 18-32', True)]),
          [('SECONDO', 'Al c. 9 arriba el f. Als cc. 13-16, l\'esquerra toca dues notes juntes.'),
           ('PRIMO', 'Escolta com canvia el so.'),
           ('JUNTAS', 'Els cc. 9-17 en bucle i la barra de repetició.'),
           ('OJO', 'La barra del c. 17 et fa tornar al c. 1: els cc. 1-17 sonen dues vegades.')]),
        B(3, 'Secondo cc. 18-36', 'Segona part', (2, 3),
          D('cadena', 'Els matisos', [('p', False), ('sf', False), ('mf', False), ('f', True)]),
          [('SECONDO', "sf al c. 21; p al c. 22; mf al c. 23; f al c. 29. Puja i baixa amb els "
                       "reguladors."),
           ('PRIMO', 'Escolta com canvien els matisos.'),
           ('JUNTAS', 'Un sistema cada dia.'),
           ('OJO', 'Sol♯ al c. 21 i Sol becaire al c. 22: llegeix-los. Repetició al c. 32.')]),
        B(4, 'Secondo cc. 37-56', 'El final del Secondo', (4, 5),
          D('cadena', 'El final', [('p', False), ('regulador <', False), ('f', False),
                                  ('calderó', True)]),
          [('SECONDO', 'Acords a staccato (punts) i més so al f. Calderó al c. 56.'),
           ('PRIMO', 'El Primo acaba amb tu.'),
           ('JUNTAS', "Els dos últims compassos, en bucle."),
           ('A TEMPO', "El calderó: deixeu anar l'últim acord a l'hora.")]),
        B(5, 'Primo cc. 1-22', 'La melodia', (6, 7),
          D('cadena', 'Dos dibuixos',
            [('corxeres lligades', False), ('silenci + corxera', True)]),
          [('PRIMO', 'Canta la melodia lligada dels cc. 1-7. Des del c. 8, silenci + corxera.'),
           ('SECONDO', 'Acompanya molt fluix: p.'),
           ('JUNTAS', "Primer els cc. 1-11, després els cc. 12-22."),
           ('OJO', "L'8va del Primo: sona una octava més aguda.")]),
        B(6, 'Primo cc. 23-44', 'La part central', (8, 9),
          D('cadena', 'El que hi ha de nou',
            [('sf, p i mf', False), ('staccato i accents', False), ("nota d'adorn", True)]),
          [('PRIMO', "sf al c. 23, p al c. 24, mf al c. 25. Al c. 38, una nota d'adorn."),
           ('SECONDO', 'No tapis el Primo quan hi ha adorns.'),
           ('JUNTAS', 'Cada sistema per separat.'),
           ('OJO', 'Repetició al c. 32: els cc. 18-32 sonen dues vegades.')]),
        B(7, 'Primo cc. 45-56', 'El final', (10, 10),
          D('cadena', 'El final', [('< f', False), ('ritme amb puntet', False),
                                  ('calderó', True)]),
          [('PRIMO', 'Corxera amb puntet + semicorxera (cc. 45-52). f al c. 55; calderó al c. 56.'),
           ('SECONDO', "Espereu el Primo per a l'últim acord."),
           ('JUNTAS', 'La peça sencera, sense parar.'),
           ('A TEMPO', 'Tota la peça, un cop al dia.')]),
    ],
    sub_guia="Cada bloc: primer cada part sola, després juntes i a tempo.",
    lista=['Toco la meva part de memòria, almenys els primers blocs.',
           "Compto «un-dos» i comencem a l'hora.",
           'Sé on tornar a les dues repeticions (cc. 17 i 32).',
           'He tocat les dues parts, Primo i Secondo.',
           "La gravo amb el mòbil i me l'escolto."],
    cortes={1: [319.5, 468.2, 611.5], 2: [219.5, 373.2, 548.0], 3: [203.2, 344.2]},
    corte_titulo=163.0, inicio={1: 60.5, 2: 60.5, 3: 62.8},
    burb={
        0: [('arriba', 330, 'AMB', "Moderato, 2/4: dues negres per compàs. Comences en p; compta "
                                   "«un-dos» abans d'entrar.", 0.3)],
        1: [('arriba', 262, 'SEC', 'f al c. 9: a partir d\'aquí sona fort.', 0.08),
            ('arriba', 262, 'OJO', 'Barra de repetició al final del c. 17: tornes al c. 1 i '
                                   'toques els cc. 1-17 dues vegades.', 0.95)],
        2: [('arriba', 300, 'OJO', 'Sol♯ al c. 21 (amb sf) i Sol becaire al c. 22 (amb p): '
                                   'llegeix-los bé!', 0.55)],
        3: [('arriba', 262, 'SEC', 'Repetició al c. 32: repeteixes els cc. 18-32.', 0.45),
            ('arriba', 262, 'AMB', 'p al c. 33 i accents (>) als cc. 35-36: fes-los sonar una '
                                   'mica més.', 0.9)],
        5: [('arriba', 300, 'OJO', "Calderó final (c. 56): deixeu anar l'últim acord junts.",
             0.9)],
        6: [('arriba', 330, 'PRIMO', "Comences tu, amb 8va: llegeixes el que hi ha escrit i sona "
                                     "una octava més aguda. Lligat i cantat.", 0.2)],
        7: [('arriba', 262, 'PRIMO', "Cada compàs comença amb un silenci de corxera: compta'l, "
                                     "no te'l saltis.", 0.3),
            ('arriba', 262, 'OJO', 'Repetició al c. 17; el c. 18 comença una part nova en p.',
             0.8)],
        8: [('arriba', 262, 'AMB', 'sf al c. 23, p al c. 24 i mf al c. 25: tres matisos en tres '
                                   'compassos!', 0.05),
            ('arriba', 262, 'OJO', 'Repetició al c. 32: tornes al c. 18.', 0.85)],
        9: [('arriba', 330, 'PRIMO', "Punts (staccato), accents i una nota d'adorn al c. 38: "
                                     "lleugera i curta.", 0.35)],
        10: [('arriba', 262, 'PRIMO', 'Corxera amb puntet + semicorxera: practica-ho amb '
                                      'palmes.', 0.3),
             ('arriba', 262, 'OJO', 'Calderó al c. 56: deixeu anar junts.', 0.95)],
    },
    misol=dict(
        manos="Quatre mans, dos cervells: mireu-vos abans d'entrar i respireu junts. Així no "
              "us perdeu!",
        guia="Aprèn cada part per separat i canvieu: qui coneix les dues sent molt millor el "
             "conjunt.",
        pauta="Escriu un compàs de 2/4 amb corxeres lligades de dues en dues, com al c. 1 del "
              "Primo. Després canvia'n les notes!"),
    marcas=[],
    pie_pauta="la clau la poses tu · copia un compàs o escriu l'escala de Do major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_tx_melodische.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
