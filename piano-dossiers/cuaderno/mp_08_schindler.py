# -*- coding: utf-8 -*-
"""Pieza 8 · Theme from Schindler's List (John Williams), descarga de Musescore. MEDIDO sobre el
   PDF (2 paginas carta, 9 sistemas, 27 compases numerados; el c. 1 es una sola negra con
   calderon): dos bemoles (Sol menor, con fa sostenido), 4/4, "Expressively" sin metronomo, mp,
   rit., a tempo, dim., cresc., rall., "a tempo, moving along", mf, "passionately", p; acordes
   arpegiados (linea ondulada), doble barra oblicua en el c. 11, clave de sol en la izquierda
   en el c. 26 y calderon final; semicorchea la figura mas corta (cc. 12, 13, 15, 23).
   La marca de agua de Musescore (primera linea de cada pagina) se excluye con `inicio`."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=8, slug='schindler', pdf='schindlers_list.pdf', time_sig=(4, 4),
    titulo="Theme from Schindler's List", autor='John Williams · arranjament per a piano',
    kicker="Eva · peça 8 · Schindler's List", mes='Febrer · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=schindler%27s+list+theme+piano+tutorial',
    credito="Partitura: J. Williams, Theme from Schindler's List (Musescore). Anotacions: T-Clas.",
    ficha=FICHA(
        datos=[('Tonalitat', 'Sol menor'), ('Compàs', '4/4'), ('Caràcter', 'Expressively'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '27')],
        total=27,
        secciones=[('A', 1, 3, 'Entrada · mp', AZUL), ('B', 4, 9, 'El tema · cresc.', OCRE),
                   ('C', 10, 15, 'dim. · rall. · a tempo', AZUL),
                   ('D', 16, 24, 'mf · passionately', OCRE), ('E', 25, 27, 'Final · p', AZUL)],
        ideas=[('ESQUERRA', 'Acords i baix',
                'Acords de dues o tres notes i notes soltes del baix, en negres i blanques. '
                'Molts acords porten una línia ondulada.'),
               ('DRETA', 'Melodia a dues notes',
                'Corxeres i negres que canten, sovint amb una segona nota a sota, tocades '
                'alhora.'),
               ('EL TEMPO', 'Respira tota l\'estona',
                'Hi ha rit., rall. i a tempo una vegada i una altra: la peça no va a una '
                'velocitat fixa.'),
               ('ELS MATISOS', 'mp → mf → p',
                'Comença en mp, arriba a mf i "passionately" al c. 18, i acaba en p amb dim.')],
        especial=[
            'Posa "Expressively" i no porta metrònom: el tempo el marca l\'expressió.',
            'Dos bemolls (si♭, mi♭) i fa♯ en uns quants compassos (cc. 3, 7, 10...): Sol menor.',
            'El c. 1 és una sola nota amb calderó; el tema comença al c. 2.',
            'La línia ondulada al costat d\'un acord: toca\'l de baix cap amunt, ràpid (arpegiat).',
            'rit./rall. (cc. 3, 11, 15, 24) i a tempo (cc. 4, 12, 16): vigila cada canvi.',
            'Al c. 26 l\'esquerra passa a clau de sol. L\'acord final (c. 27) porta '
            'calderó a les dues mans.'],
        reto='Cantar la melodia amb expressió mentre l\'esquerra canvia entre acords i notes '
             'soltes, i seguir tots els canvis de tempo i de matís.',
        truco='Marca amb llapis a la partitura cada rit., rall. i a tempo, i assaja cada canvi '
              'per separat, amb dos compassos abans i dos després.',
        sabias='John Williams va compondre el tema per a «La llista de Schindler» (1993), de Steven Spielberg, i va guanyar l\'Oscar a la millor banda sonora. A la pel·lícula, el violí el toca Itzhak Perlman.',
        qr_texto='Escolta-la amb la partitura al davant i segueix els rit. i els a tempo.',
        ts=(4, 4)),
    manos=dict(
        izq=[('Acords i notes soltes', 'Aprèn la successió de posicions: acord, nota sola, '
                                       'acord. Toca només el primer sistema, a poc a poc.'),
             ('Acords arpegiats', 'Amb la línia ondulada toca primer la nota més greu i '
                                  'puja ràpid; deixa sonar l\'última.'),
             ('Passatges que pugen', 'Al c. 11 hi ha corxeres que pugen i al c. 23, '
                                     'semicorxeres. Toca\'ls lents i iguals.'),
             ('Clau de sol a l\'esquerra', 'Al c. 26 les tres últimes notes de l\'esquerra '
                                           'es llegeixen en clau de sol: mira-ho abans.')],
        der=[('Cantar la melodia', 'Canta-la per dins i respira als silencis. Marca amb '
                                   'llapis els rit. i els a tempo.'),
             ('Dues notes alhora', 'Sovint la melodia porta una altra nota a sota: llegeix les dues '
                                   'juntes i toca amb la mà relaxada.'),
             ('Fa♯ i silencis', 'El fa♯ surt en uns quants compassos (cc. 3, 7, 10...). Als '
                                'cc. 12 i 14 comences després d\'un silenci de corxera: compta\'l.'),
             ('Amb l\'esquerra', 'Uneix a poc a poc un sistema amb l\'esquerra ja segura. Si es '
                                 'trenca, torna a una sola mà.')],
        tecnica=['Braç i canell solts: la melodia es canta, no es copeja.',
                 'Compta 1-2-3-4 i marca tu el rit. i el rall., no la pressa.',
                 'Estudia cada canvi de tempo per separat abans d\'unir-lo.']),
    bloques=[
        B(1, 'cc. 1-6', 'L\'entrada', (0, 1),
          D('cadena', 'Calderó → tema → rit. → a tempo', [('c. 1: calderó', False),
                                                         ('c. 2: el tema', False), ('c. 3: rit.', False),
                                                         ('c. 4: a tempo', True)]),
          [('IZQUIERDA', 'c. 2: acord llarg arpegiat i, a sobre, negres iguals; després acords.'),
           ('DERECHA', 'Nota amb calderó i corxeres que canten en mp; fa♯ al c. 3.'),
           ('JUNTAS', 'Dos trams: cc. 1-3 i cc. 4-6; en cada un, lent.'),
           ('OJO', 'rit. al c. 3, a tempo amb regulador creixent al c. 4, dim. al c. 6.')]),
        B(2, 'cc. 7-9', 'El tema creix', (2, 2),
          D('cadena', 'Els matisos', [('c. 7', False), ('cresc. (c. 8)', False),
                                      ('lligadures llargues (c. 9)', True)]),
          [('IZQUIERDA', 'Acords arpegiats i blanques; al c. 9 una lligadura llarga.'),
           ('DERECHA', 'Dues veus alhora al c. 7; fa♯ als cc. 7 i 9.'),
           ('JUNTAS', 'Un compàs cada cop, i després els tres.'),
           ('OJO', 'cresc. al c. 8; al c. 9 mantén les notes lligades, no les repeteixis.')]),
        B(3, 'cc. 10-12', 'Calma i tornada', (3, 3),
          D('cadena', 'Canvis de tempo', [('dim. (c. 10)', False), ('rall. (c. 11)', False),
                                          ('a tempo, moving along (c. 12)', True)]),
          [('IZQUIERDA', 'Corxeres que pugen al c. 11; al c. 12, silencis de corxera i '
                         'acords.'),
           ('DERECHA', 'c. 12: semicorxeres després d\'un silenci de corxera. Entra just.'),
           ('JUNTAS', 'Toca el c. 11 i el c. 12 seguits, amb el canvi de tempo.'),
           ('OJO', 'La doble barra obliqua (//) del c. 11 és una pausa curta.')]),
        B(4, 'cc. 13-15', 'Acords entre silencis', (4, 4),
          D('capas', 'Dues capes alhora',
            [('Dreta: melodia', 'barras', AZUL), ('Esquerra: acords', 'puntos', OCRE, 4)]),
          [('IZQUIERDA', 'Silenci de corxera i acord de tres notes, una vegada i una altra.'),
           ('DERECHA', 'Semicorxeres als cc. 13-15 i una lligadura llarga al c. 15.'),
           ('JUNTAS', 'Compta els silencis de l\'esquerra en veu alta.'),
           ('OJO', 'rit. al c. 15, just abans de l\'a tempo del c. 16.')]),
        B(5, 'cc. 16-21', 'Més força', (5, 6),
          D('cadena', 'Els matisos', [('mf (c. 16)', False), ('passionately (c. 18)', False),
                                      ('dim. (c. 19)', False), ('cresc. (c. 20)', True)]),
          [('IZQUIERDA', 'Molts acords arpegiats: puja ràpid i mantén el pols.'),
           ('DERECHA', 'Accent (>) al c. 16; corxeres amb acords de dues notes.'),
           ('JUNTAS', 'Dos trams: cc. 16-18 i cc. 19-21.'),
           ('OJO', 'mf amb regulador i "a tempo" al c. 16; "passionately" al c. 18.')]),
        B(6, 'cc. 22-24', 'L\'onada es calma', (7, 7),
          D('cadena', 'Cap al final', [('c. 23: semicorxeres (esq.)', False), ('dim.', False),
                                       ('rall. (c. 24)', True)]),
          [('IZQUIERDA', 'c. 23: semicorxeres que pugen fins a una nota llarga.'),
           ('DERECHA', 'Acords de dues i tres notes amb lligadures; fa♯ als cc. 22-24.'),
           ('JUNTAS', 'Toca els cc. 22-24 en bucle, sense accelerar.'),
           ('OJO', 'dim. i rall. al c. 24: més suau i més lent.')]),
        B(7, 'cc. 25-27', 'El final', (8, 8),
          D('cadena', 'Cap al final', [('p (c. 25)', False), ('dim. (c. 26)', False),
                                       ('calderó (c. 27)', True)]),
          [('IZQUIERDA', 'c. 26: les tres últimes notes, en clau de sol. c. 27: acord de tres '
                         'notes.'),
           ('DERECHA', 'c. 26: corxeres que pugen, amb ratlleta a sobre (tenuto); c. 27: acord de tres notes.'),
           ('JUNTAS', 'Els tres compassos en bucle.'),
           ('A TEMPO', 'p i dim.: gairebé sense so. Calderó a les dues mans: allarga.')]),
    ],
    cortes={1: [249.5, 410.8, 571.2], 2: [174.5, 319.5, 457.0, 583.5]},
    corte_titulo=89.2, inicio={1: 25.2, 2: 33.2},
    burb={
        0: [('arriba', 270, 'OJO', 'Calderó al c. 1: dura el que vulguis. Dos bemolls: Sol '
                                   'menor. Comença en mp.', 0.05),
            ('arriba', 270, 'IZQ', 'c. 2: a baix, acord llarg arpegiat (línia ondulada: de baix '
                                   'cap amunt); a dalt, negres iguals.', 0.55)],
        1: [('arriba', 330, 'AMB', 'a tempo i regulador creixent al c. 4; dim. al c. 6.',
             0.3)],
        3: [('arriba', 270, 'OJO', 'rall. al c. 11. La doble barra obliqua (//) és una pausa '
                                   'curta.', 0.35),
            ('arriba', 270, 'DER', 'c. 12: "a tempo, moving along" i semicorxeres després d\'un silenci '
                                   'de corxera.', 0.8)],
        4: [('arriba', 330, 'IZQ', 'Silenci de corxera i acord, una vegada i una altra (cc. 12-14): '
                                   'compta el silenci.', 0.1)],
        5: [('arriba', 270, 'AMB', 'c. 16: mf, a tempo i un accent (>). Al c. 18: regulador '
                                   'creixent i "passionately".', 0.1),
            ('arriba', 270, 'DER', 'Les corxeres porten acords de dues notes: toca les dues '
                                   'juntes, amb la melodia a dalt.', 0.7)],
        7: [('arriba', 270, 'IZQ', 'c. 23: semicorxeres que pugen a l\'esquerra.', 0.3),
            ('arriba', 270, 'OJO', 'c. 24: dim. i rall.: més suau i més lent.', 0.8)],
        8: [('arriba', 270, 'OJO', 'c. 26: les tres últimes notes de l\'esquerra van en clau de '
                                   'sol.', 0.5),
            ('arriba', 270, 'AMB', 'Acord final arpegiat, amb calderó a les dues mans.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Sol menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_schindler.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
