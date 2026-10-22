# -*- coding: utf-8 -*-
"""Pieza 12 · Arabesque (Burgmuller, op. 100 n.º 2), a cuatro manos. MEDIDO sobre el PDF a zoom
   (4 pags, A4, 9 sistemas, 40 compases numerados): 2/4, Allegro scherzando sin metronomo, sin
   armadura; "Piano" (Primo: DOS pentagramas de sol con la misma melodia, el de arriba una octava
   mas aguda, con 8va) y "Piano 2" (Secondo: sol + fa); Primo en silencio en los cc.1-2; p (c.1),
   f (cc.6, 14, 30, 39), mf (cc.7 y 15), acentos (cc.8, 10, 16), barra de repeticion al empezar el
   c.19, casilla 1. (c.34) y 2. (c.35), "dim. e poco rit." (c.25), "a tempo" con p (c.27),
   "risoluto" (c.39), calderon con acento en el Primo (c.40), final sobre La-Mi; semicorchea."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=12, slug='arabesque', pdf='arabesque_burgmuller_4_manos.pdf', time_sig=(2, 4),
    titulo='Arabesque', autor='J. F. F. Burgmüller · op. 100 núm. 2 · a quatre mans',
    kicker='Eva · peça 12 · Arabesque (Burgmüller)', mes='Abril · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=burgmuller+arabesque+op+100+piano+4+hands',
    credito='Partitura: J. F. F. Burgmüller, Arabesque op. 100 (arr. a quatre mans). '
            'Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'La menor'), ('Compàs', '2/4'), ('Tempo', 'Allegro scherzando'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '40')],
        total=40,
        secciones=[('A', 1, 18, 'El tema', AZUL), ('B', 19, 26, 'Repetició · notes llargues', OCRE),
                   ('C', 27, 35, 'a tempo · caselles', AZUL), ('D', 36, 40, 'Final', OCRE)],
        ideas=[('SECONDO', 'Acords picats',
                'Comença sol, amb dos acords curts per compàs. Més endavant toca semicorxeres '
                'lligades a les dues claus.'),
               ('PRIMO', 'Semicorxeres lleugeres',
                'Entra al c. 3 amb quatre semicorxeres lligades i una corxera curta. Dos '
                'pentagrames amb la mateixa melodia.'),
               ('LA REPETICIÓ', 'Del c. 19 al c. 34',
                'Barra de repetició a l\'inici del c. 19; casella 1 al c. 34 i casella 2 al '
                'c. 35.'),
               ('ELS MATISOS', 'p · f · mf · risoluto',
                'Comença en p; f i mf s\'alternen; "risoluto" al c. 39 i calderó al final.')],
        especial=[
            'Posa "Allegro scherzando" i el compàs és 2/4: dues negres per compàs. Sense armadura.',
            'És a quatre mans: el Primo ("Piano") a dalt i el Secondo ("Piano 2") a baix.',
            'El Primo calla als cc. 1-2 i entra al c. 3. Duu dos pentagrames de sol: el '
            'de dalt sona una octava més aguda (8va).',
            'Barra de repetició a l\'inici del c. 19 i caselles 1. i 2. als cc. 34-35.',
            'Al c. 25 posa "dim. e poco rit." i al c. 27 "a tempo" (p).',
            'Al c. 39 posa "risoluto" (f) i l\'últim compàs duu calderó i acord final '
            'sobre La i Mi.'],
        reto='Que les semicorxeres i els acords picats sonin lleugers i alhora sense córrer: és '
             'un scherzando, juganer. Al c. 19 es canvien els papers: melodia llarga al '
             'Primo i semicorxeres al Secondo.',
        truco='Estudieu per torns i compteu "un-dos" en veu alta. Abans de tocar, recorreu amb '
              'el dit: 19 → 34 → 19 → 35 → 36.',
        sabias='Burgmüller va escriure 25 estudis fàcils i progressius, op. 100, pensats per a alumnes. L\'«Arabesque» és el núm. 2.',
        qr_texto='Escolta-la i compta "un-dos": notes el caràcter juganer?', ts=(2, 4)),
    manos=dict(
        titulo='Secondo i Primo', sub='Cada part s\'aprèn sola. Després, juntes i a poc a poc.',
        tit_izq='SECONDO · la part greu', tit_der='PRIMO · la part aguda',
        izq=[('Acords picats', 'Al principi, dos acords curts per compàs: tres notes en sol '
                                 'i dues en fa. Lleugers, comptant "un-dos".'),
             ('Les semicorxeres', 'Als cc. 19-24 i 27-28 les dues mans toquen la mateixa figura '
                                  'a una octava de distància. A poc a poc i regulars.'),
             ('Els canvis de so', 'f als cc. 6, 14 i 30; mf als cc. 7 i 15; p al '
                                       'c. 27. Toca\'ls abans per separat.'),
             ('Amb el Primo', 'Juntes, a poc a poc. El Secondo acompanya i escolta el Primo.')],
        der=[('Entrar al c. 3', 'Els dos primers compassos són de silenci: compta\'ls i entra '
                                   'a temps.'),
             ('Semicorxeres lligades', 'Quatre semicorxeres lligades i una corxera curta, lleuger. '
                                      'Una sola idea per compàs.'),
             ('L\'octava', 'Els dos pentagrames del Primo duen la mateixa melodia; el de dalt '
                           'sona una octava més aguda (8va).'),
             ('Notes llargues', 'Als cc. 19-24 canta notes llargues lligades; als cc. 27-28 '
                              'toca acords curts.')],
        tecnica=['Canell solt: lleuger i juganer.',
                 'Compta "un-dos" a cada compàs, sense córrer.',
                 'Mireu primer el camí de les repeticions.']),
    bloques=[
        B(1, 'cc. 1-4', 'Entra el Secondo', (0, 0),
          D('cadena', 'Els primers compassos', [('Secondo sol (cc. 1-2)', False),
                                                ('entra el Primo (c. 3)', True)]),
          [('SECONDO', 'Dos acords curts per compàs, en p. Comença sol.'),
           ('PRIMO', 'Compta dos compassos i entra al c. 3: quatre semicorxeres i una corxera.'),
           ('JUNTAS', 'Compteu "un-dos" i mireu la primera nota de l\'altre.'),
           ('OJO', 'Allegro scherzando: viu i juganer, sense córrer.')]),
        B(2, 'cc. 5-9', 'f i mf', (1, 1),
          D('cadena', 'Els matisos', [('f (c. 6)', False), ('mf (c. 7)', False), ('accent (c. 8)', True)]),
          [('SECONDO', 'Els acords segueixen picats; al c. 7 canvien les notes del baix.'),
           ('PRIMO', 'Comença el 8va. Semicorxeres als cc. 5-6 i corxeres lligades als cc. 7-9.'),
           ('JUNTAS', 'f al c. 6 i mf al c. 7: el so baixa de cop.'),
           ('OJO', 'L\'accent (>) del c. 8 va sobre la nota lligada.')]),
        B(3, 'cc. 10-18', 'f i mf una altra vegada', (2, 3),
          D('cadena', 'Com els cc. 5-9', [('accent (c. 10)', False), ('f (c. 14)', False),
                                           ('mf (c. 15)', True)]),
          [('SECONDO', 'Acords picats; al c. 18 acaba en un acord llarg amb puntet.'),
           ('PRIMO', 'Semicorxeres lleugeres i silencis; accent als cc. 10 i 16.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 10-13 i cc. 14-18.'),
           ('OJO', 'f al c. 14 i mf al c. 15, com als cc. 6-7.')]),
        B(4, 'cc. 19-22', 'Comença la repetició', (4, 4),
          D('capas', 'Dues capes alhora',
            [('Primo: notes llargues', 'barras', AZUL), ('Secondo: semicorxeres', 'puntos', OCRE)]),
          [('SECONDO', 'Ara toques semicorxeres lligades, les dues mans a una octava.'),
           ('PRIMO', 'Notes llargues lligades amb 8va: canta-les, que el Secondo no les tapi.'),
           ('JUNTAS', 'Quatre compassos cada cop, en bucle.'),
           ('OJO', 'Barra de repetició a l\'inici del c. 19; hi ha un sostingut al Secondo.')]),
        B(5, 'cc. 23-26', 'dim. e poco rit.', (5, 5),
          D('cadena', 'El final de la frase', [('notes llargues', False), ('dim. e poco rit. (c. 25)', False),
                                               ('corxeres que baixen', True)]),
          [('SECONDO', 'Semicorxeres als cc. 23-24 i corxeres que baixen als cc. 25-26.'),
           ('PRIMO', 'Notes llargues i, al c. 25, quatre corxeres que baixen.'),
           ('JUNTAS', 'Baixeu el so i freneu una mica alhora.'),
           ('OJO', 'Hi ha sostinguts solts: llegeix-los abans de tocar.')]),
        B(6, 'cc. 27-30', 'a tempo', (6, 6),
          D('cadena', 'Les indicacions', [('a tempo i p (c. 27)', False), ('semicorxeres (c. 29)', False),
                                           ('f (c. 30)', True)]),
          [('SECONDO', 'Duu les semicorxeres en p (cc. 27-28) i torna als acords (cc. 29-30).'),
           ('PRIMO', 'Només el pentagrama de dalt, amb acords curts (cc. 27-28); després semicorxeres.'),
           ('JUNTAS', 'Recupereu el tempo juntes al c. 27.'),
           ('A TEMPO', 'f al c. 30.')]),
        B(7, 'cc. 31-35', 'Les caselles', (7, 7),
          D('cadena', 'El camí', [('c. 34: casella 1', False), ('↩ al c. 19', False),
                                    ('c. 35: casella 2', True)]),
          [('SECONDO', 'Acords picats, igual a les dues caselles.'),
           ('PRIMO', 'Corxeres lligades i accent al c. 32; a la casella 1 una blanca.'),
           ('JUNTAS', 'Recorreu el camí amb el dit abans de tocar.'),
           ('OJO', '1a vegada: casella 1 i tornada al c. 19. 2a vegada: casella 2, i segueixes al c. 36.')]),
        B(8, 'cc. 36-40', 'El final', (8, 8),
          D('cadena', 'Cap al final', [('semicorxeres que pugen', False), ('risoluto en f (c. 39)', False),
                                         ('calderó (c. 40)', True)]),
          [('SECONDO', 'Acords picats i, al c. 39, semicorxeres que baixen en f.'),
           ('PRIMO', 'Semicorxeres que pugen; al c. 39 baixen, amb f i "risoluto".'),
           ('JUNTAS', 'Els cinc compassos seguits, sense parar.'),
           ('A TEMPO', 'L\'últim compàs: acord final i calderó; deixeu-lo anar alhora.')]),
    ],
    cortes={1: [385.0], 2: [267.0, 534.0], 3: [264.0, 538.0]},
    corte_titulo=143.0, fin={2: 765.0, 3: 758.0},
    burb={
        0: [('arriba', 330, 'AMB', 'Allegro scherzando, 2/4 i p. Als cc. 1-2 toca sol el Secondo: '
                                   'acords curts.', 0.3),
            ('abajo', 330, 'PRIMO', 'Entres al c. 3: quatre semicorxeres lligades i una '
                                    'corxera curta.', 0.62)],
        1: [('arriba', 330, 'PRIMO', 'Aquí comença el 8va. f al c. 6 i mf al c. 7: el '
                                     'so baixa de cop.', 0.4)],
        3: [('arriba', 330, 'AMB', 'f al c. 14 i mf al c. 15, com als cc. 6-7. Accent '
                                   'al c. 16.', 0.3)],
        4: [('arriba', 330, 'OJO', 'Barra de repetició a l\'inici del c. 19. El Primo canta '
                                   'notes llargues i el Secondo toca semicorxeres.', 0.1)],
        5: [('arriba', 300, 'OJO', '"dim. e poco rit." al c. 25: baixa el so i frena una '
                                   'mica.', 0.62)],
        6: [('arriba', 330, 'OJO', 'a tempo i p al c. 27: ara el Secondo duu les '
                                   'semicorxeres i el Primo, acords a dalt.', 0.1)],
        7: [('arriba', 330, 'OJO', 'Casella 1 (c. 34): tornes al c. 19. Casella 2 (c. 35): '
                                   'segueixes al c. 36.', 0.62)],
        8: [('arriba', 300, 'AMB', 'risoluto i f al c. 39. Al c. 40, acord final amb '
                                   'calderó.', 0.6)],
    },
    marcas=[],
    pie_pauta='la clau la poses tu · copia un compàs o inventa dos compassos en 2/4')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_arabesque.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
