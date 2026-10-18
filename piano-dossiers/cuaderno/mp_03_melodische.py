# -*- coding: utf-8 -*-
"""Pieza 3 · Melodische Uebungsstuecke n.º 3, op. 149 (Diabelli), a cuatro manos. MEDIDO: 3
   paginas (Secondo en las pp. 1-2, Primo en las pp. 2-3), 2/4, Moderato sin metronomo, sin
   armadura (Do mayor, con alteraciones), p, f, mf, sf, reguladores, barras de repeticion y un
   calderon final; semicorchea (ritmo con puntillo y notas de adorno en el Primo)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=3, slug='melodische', pdf='melodishe_diabelli_4_manos.pdf', time_sig=(2, 4),
    titulo='Melodische Übungsstücke n.º 3', autor='Anton Diabelli · op. 149 · a quatre mans',
    kicker='Eva · peça 3 · Diabelli, op. 149 n.º 3', mes='Desembre · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=diabelli+melodische+ubungsstucke+op+149+piano+4+hands',
    credito='Partitura: A. Diabelli, op. 149 n.º 3 (Mutopia Project, BSD). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '2/4'), ('Tempo', 'Moderato'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '56')],
        total=56,
        secciones=[('A', 1, 22, 'Primera part', AZUL), ('B', 23, 44, 'Part central', OCRE),
                   ('C', 45, 56, 'Final', AZUL)],
        ideas=[('SECONDO', 'Acompanya',
                'Grups de corxeres lligades sobre notes soltes amb silencis. És '
                'l\'acompanyament.'),
               ('PRIMO', 'Canta',
                'Comença amb corxeres lligades i passa a un disseny de silenci i dues corxeres '
                'per compàs.'),
               ('ELS MATISOS', 'p · f · mf · sf',
                'Alterna pianos i forts, amb reguladors i algun sf (accent fort).'),
               ('EL FINAL', 'Calderó',
                'Els dos acaben amb un calderó a l\'últim compàs.')],
        especial=[
            'Hi diu "Moderato" i el compàs és 2/4: dues negres per compàs.',
            'És a quatre mans: el Secondo (pp. 1-2) i el Primo (pp. 2-3) tenen cadascun la seva '
            'part completa.',
            'Hi ha barres de repetició: abans de tocar, localitza on comencen i on acaben.',
            'El Primo porta ritme amb puntet i alguna noteta d\'adorn.',
            'Els matisos canvien de cop (p, f, mf) i hi ha reguladors (< >).',
            'Acaba amb un calderó a l\'últim compàs.'],
        reto='Que les dues parts encaixin: el Primo canta i el Secondo acompanya sense tapar-lo. Si '
             'el Secondo sona fort, el Primo no se sent.',
        truco='Estudieu per torns: una toca i l\'altra compta "un-dos" en veu alta. Després '
              'canvieu. Només quan les dues sapigueu les dues parts, juntes.',
        sabias='És la n.º 3 de les 28 peces melòdiques a quatre mans, op. 149, de Diabelli (1781-1858), l\'editor vienès del vals sobre el qual Beethoven va escriure les seves 33 variacions.',
        qr_texto='Escolta-la i segueix la teva part amb el dit: on respira el Primo?', ts=(2, 4)),
    manos=dict(
        titulo='Secondo i Primo', sub='Cada part s\'aprèn sola. Després, juntes i a poc a poc.',
        tit_izq='SECONDO · la part greu', tit_der='PRIMO · la part aguda',
        izq=[('Un grup cada cop', 'Aprèn primer un compàs de corxeres lligades de tres en '
                                  'tres. Toca-ho a poc a poc, deu vegades seguides sense fallar.'),
             ('Les notes soltes', 'A baix hi ha notes soltes amb silencis. Toca només aquesta '
                                  'línia i compta "un-dos" en veu alta.'),
             ('Les dues línies', 'Ajunta-les: corxeres a sobre, notes soltes a sota, en p.'),
             ('Els canvis', 'Vigila els canvis de matís: p, f, mf. Canvien de cop.')],
        der=[('Lligadures', 'Al principi van corxeres lligades de dues en dues. Cada lligadura és un '
                            'gest: so a la primera, suau a la segona.'),
             ('Corxera-silenci', 'Més endavant cada compàs comença amb un silenci de corxera. '
                                 'Compta-lo: el silenci dura, no se salta.'),
             ('Puntet i adorns', 'Als cc. 34-50 apareixen ritmes amb puntet i notetes d\'adorn. '
                                 'Estudia-los sols i a poc a poc.'),
             ('Amb el Secondo', 'Toqueu juntes a poc a poc. El Primo escolta el Secondo.')],
        tecnica=['Canells solts, dits corbats i so regular.',
                 'Compta en veu alta "un-dos": cada compàs, dues negres.',
                 'Canvieu de part: així s\'aprenen les dues.']),
    bloques=[
        B(1, 'Secondo cc. 1-17', 'Primera part', (0, 1),
          D('capas', 'Dues línies alhora',
            [('Corxeres lligades', 'puntos', OCRE, 6), ('Notes soltes', 'barras', OCRE)]),
          [('SECONDO', 'Comença en p; al c. 9 arriba la f. Aprèn cada línia sola.'),
           ('PRIMO', 'Escolta aquest bloc: la teva part l\'adorna després.'),
           ('JUNTAS', 'Llegiu la partitura de l\'altra mentre toqueu la vostra.'),
           ('OJO', 'Hi ha barres de repetició: localitzeu-les abans de tocar.')]),
        B(2, 'Secondo cc. 18-36', 'Segona part', (2, 3),
          D('cadena', 'Els matisos', [('p', False), ('sf', False), ('mf', False), ('f', True)]),
          [('SECONDO', 'El sf (accent fort) del c. 21 i els reguladors: puja i baixa.'),
           ('PRIMO', 'Escolta com canvien els matisos.'),
           ('JUNTAS', 'Un sistema cada dia.'),
           ('OJO', 'Dos sostinguts i un becaire als cc. 21-22: llegeix-los.')]),
        B(3, 'Secondo cc. 37-56', 'Final del Secondo', (4, 5),
          D('cadena', 'El final', [('p', False), ('regulador <', False), ('f', False),
                                  ('calderó', True)]),
          [('SECONDO', 'Notes repetides i acords: més so a la f.'),
           ('PRIMO', 'El Primo acaba juntament amb tu.'),
           ('JUNTAS', 'Els dos últims compassos, en bucle.'),
           ('A TEMPO', 'El calderó: deixeu anar l\'últim acord alhora.')]),
        B(4, 'Primo cc. 1-22', 'La melodia', (6, 7),
          D('cadena', 'Dos dissenys', [('corxeres lligades', False), ('silenci + 2 corxeres', True)]),
          [('PRIMO', 'Canta la melodia lligada dels cc. 1-11 i després el disseny amb silenci.'),
           ('SECONDO', 'Acompanya molt suau: p.'),
           ('JUNTAS', 'Primer els cc. 1-11, després els cc. 12-22.'),
           ('OJO', 'El 8va del Primo: sona una octava més aguda.')]),
        B(5, 'Primo cc. 23-44', 'La part central', (8, 9),
          D('cadena', 'El que és nou', [('sf i mf', False), ('ritme amb puntet', False),
                                       ('noteta d\'adorn', True)]),
          [('PRIMO', 'Apareixen el puntet i les notetes d\'adorn: a poc a poc.'),
           ('SECONDO', 'No tapis el Primo quan hi hagi adorns.'),
           ('JUNTAS', 'Cada sistema per separat.'),
           ('OJO', 'Hi ha barres de repetició en aquest bloc.')]),
        B(6, 'Primo cc. 45-56', 'El final', (10, 10),
          D('cadena', 'El final', [('< f', False), ('sf', False), ('calderó', True)]),
          [('PRIMO', 'Notes llargues al final i calderó: compta-les senceres.'),
           ('SECONDO', 'Us espereu per a l\'últim acord.'),
           ('JUNTAS', 'La peça sencera, sense parar.'),
           ('A TEMPO', 'Tota la peça, una vegada al dia.')]),
    ],
    cortes={1: [319.5, 468.2, 611.5], 2: [219.5, 373.2, 548.0], 3: [203.2, 344.2]},
    corte_titulo=163.0, inicio={1: 60.5, 2: 60.5, 3: 62.8},
    burb={
        0: [('arriba', 330, 'AMB', 'Moderato, 2/4: dues negres per compàs. Comença en p; compta '
                                   '"un-dos" abans d\'entrar.', 0.3)],
        1: [('arriba', 300, 'SEC', 'f al c. 9. Fixa\'t en les barres de repetició d\'aquest '
                                   'sistema.', 0.1)],
        3: [('arriba', 300, 'OJO', 'sf (accent fort) i reguladors < >: el so puja i baixa '
                                   'dins del compàs.', 0.7)],
        5: [('arriba', 300, 'AMB', 'p, f i un calderó al final: l\'últim acord s\'allarga.',
             0.9)],
        6: [('arriba', 330, 'PRIMO', 'Comences tu, amb el 8va: llegeixes el que està escrit i sona una '
                                     'octava més aguda. Lligat i cantat.', 0.2)],
        7: [('arriba', 300, 'PRIMO', 'Cada compàs comença amb un silenci de corxera: compta\'l, '
                                     'no te\'l saltis.', 0.3)],
        9: [('arriba', 300, 'PRIMO', 'Ritme amb puntet i notetes d\'adorn: a poc a poc i lleuger.',
             0.5)],
        10: [('arriba', 300, 'AMB', 'Fi: calderó. Deixeu anar l\'últim acord juntes.', 0.95)],
    },
    marcas=[],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Do major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_melodische.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
