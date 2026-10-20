# -*- coding: utf-8 -*-
"""Pieza 3 · Jingle Bell Rock a cuatro manos (Primo = parte I, Secondo = parte II).
   MEDIDO sobre el PDF (4 paginas A4, 7 sistemas de 4 compases = 28): una armadura de un
   sostenido (Sol mayor), 4/4, sin tempo impreso; «Suonare entrambe le mani un ottava sopra»
   sobre la parte I; la parte II va entera en clave de fa. Repeticion al final del c. 8 hacia el
   c. 1: casilla 1 = cc. 7-8, casilla 2 = cc. 9-10. Matices: mf (I) y mp (II) en el c. 1; f (I) c.
   10; mf (II) c. 11; mf (I) y mp (II) c. 19; cc. 25-27: f-p-f (I) y mf-pp-mf (II). Figura mas
   corta: semicorchea (corchea con puntillo + semicorchea). Tresillo de corcheas en el Secondo,
   c. 24. Alteraciones: D# (I, c. 7), Sib (I, c. 8), G#/becuadro/C# y otras en el Secondo."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_p = lambda d, b=None: ({'pitch': 'B4', 'dur': d} if b is None else
                        {'pitch': 'B4', 'dur': d, 'beam': b})
_r = lambda d: {'rest': True, 'dur': d}

SPEC = dict(
    num=4, slug='jingle', pdf='jingle_bell_4_manos.pdf', time_sig=(4, 4),
    titulo='Jingle Bell Rock', autor='Joe Beal i Jim Boothe · a quatre mans (Primo i Secondo)',
    kicker='Abril · peça 4 · Jingle Bell Rock', mes='Desembre · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=bobby+helms+jingle+bell+rock',
    credito='Partitura: Jingle Bell Rock a 4 mans, arr. O. Litvichko (musescore.com). '
            'Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sol major'), ('Compàs', '4/4'), ('Tempo', 'No indicat'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '28')],
        total=28,
        secciones=[('A', 1, 8, 'El tema i la repetició', AZUL),
                   ('B', 9, 16, 'Casella 2 · f', OCRE),
                   ('C', 17, 24, 'Torna el tema · tresset', AZUL),
                   ('D', 25, 28, 'f · p · f i final', OCRE)],
        ideas=[('PRIMO · PART I', 'La melodia',
                'Corxera amb puntet, semicorxera i negra. Demana les dues mans una octava més '
                'aguda del que hi ha escrit.'),
               ('SECONDO · PART II', 'Acords i baix',
                'Tota en clau de fa. A dalt, acords als temps 2 i 4; a baix, el baix.'),
               ('ELS MATISOS', 'Molt contrast',
                'Comença en mf (Primo) i mp (Secondo). Als cc. 25-27: f, p, f.'),
               ('LA REPETICIÓ', 'Caselles 1 i 2',
                'Al final del c. 8 tornes al c. 1. La 2.a vegada, del c. 6 salts al c. 9.')],
        ideas_titulo='La peça en quatre idees',
        especial=[
            "Armadura d'un sostingut (Fa♯): Sol major. Compàs 4/4, sense tempo escrit.",
            'Dues parts: I (Primo, melodia) i II (Secondo, acords i baix). Cadascuna fa servir '
            'les dues mans.',
            'Primo: «Suonare entrambe le mani un ottava sopra» = les dues mans una octava més '
            'aguda.',
            'Casella 1 = cc. 7-8; casella 2 = cc. 9-10. Al final de la casella 1, de tornada '
            'al c. 1.',
            'Hi ha alteracions (♯, ♭ i becaires), sobretot al Secondo.',
            'Semicorxeres a tot el tema i un tresset al Secondo (c. 24).'],
        reto="Toqueu juntes: que el Primo no s'avanci ni el Secondo es retardi. Bateu igual!",
        truco="Compteu «1-2-3-4» en veu alta i comenceu a l'hora. Canvieu de part per aprendre'n "
              "les dues.",
        sabias="«Jingle Bell Rock» és de 1957: la va gravar Bobby Helms i la van compondre Joe "
               "Beal i Jim Boothe. No és «Jingle Bells», una altra cançó molt més antiga (1857).",
        qr_texto='Escolta-la i compta 1-2-3-4 amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo='Com es compten els cc. 1 i 2',
        cuenta_pie="Primo: corxera amb puntet, semicorxera i negra. Secondo: silenci i acord "
                   "al 2 i al 4. Aquí només el ritme.",
        ritmos=[('PRIMO', 'c. 1 · «jin-gle BELL»',
                 [_p('e.', 0), _p('s', 0), _p('q'), _p('e.', 1), _p('s', 1), _p('q')], AZUL,
                 'treble', None),
                ('SECONDO', 'c. 1 · acord al 2 i al 4',
                 [_r('q'), {'pitch': 'B3', 'dur': 'q'}, _r('q'), {'pitch': 'B3', 'dur': 'q'}],
                 OCRE, 'bass', None)]),
    manos=dict(
        titulo='Secondo i Primo',
        sub="Cada part s'aprèn sola. Després juntes, a poc a poc, i canvieu de part.",
        tit_izq='SECONDO · la part II', tit_der='PRIMO · la part I',
        izq=[('El baix', 'Quasi tot són blanques. Toca només aquesta línia i compta 1-2-3-4.'),
             ('Acords al 2 i al 4', 'A dalt, acord al temps 2 i al 4. A l\'1 i al 3, silenci.'),
             ('Les dues línies', 'Uneix baix i acords als cc. 1-4, fluix (mp).'),
             ('Més moviment', 'Des del c. 11 els acords són llargs i el baix va en negres.')],
        der=[('El ritme del tema', 'Corxera amb puntet, semicorxera i negra. Fes-ho primer amb '
                                   'palmes.'),
             ('Melodia sola', 'Toca els cc. 1-4 amb la dreta. Els cc. 2, 3 i 4 són iguals.'),
             ("L'esquerra del Primo", "Als cc. 1-4 toca quasi només blanques. Afegeix-la a la "
                                      "dreta."),
             ("L'8va", "Toca les dues mans una octava més aguda del que hi ha escrit. Busca la "
                       "posició abans de començar.")],
        tecnica=["Compteu 1-2-3-4 en veu alta i comenceu a l'hora.",
                 'El Secondo, més fluix que el Primo: la melodia mana.',
                 'Mireu-vos i canvieu de part.']),
    bloques=[
        B(1, 'cc. 1-4', 'El tema', (0, 0),
          D('capas', 'Tres capes alhora',
            [('Primo: melodia', 'puntos', AZUL, 6), ('Secondo: acords', 'barras', OCRE),
             ('Secondo: baix', 'barras', OCRE)]),
          [('SECONDO', 'Blanques a baix i acords al 2 i al 4. Tot en mp.'),
           ('PRIMO', 'Corxera amb puntet, semicorxera i negra (c. 1). Cc. 2-4 iguals. En mf.'),
           ('JUNTAS', "Compteu 1-2-3-4 i comenceu a l'hora."),
           ('OJO', 'Primo: les dues mans una octava més aguda. El Secondo, més fluix.')]),
        B(2, 'cc. 5-8', 'La repetició', (1, 1),
          D('cadena', 'El recorregut',
            [('cc. 1-6', False), ('casella 1: 7-8', False), ('↩ c. 1', False),
             ('cc. 1-6', False), ('casella 2: 9-10', True)]),
          [('SECONDO', 'Cc. 5-6 com el c. 4. Casella 1: acord llarg (c. 7) i baix en '
                       'moviment (c. 8).'),
           ('PRIMO', 'Cc. 5-6: silenci i frase curta. Casella 1: Re♯ (c. 7) i Si♭ (c. 8).'),
           ('JUNTAS', 'Toqueu els cc. 1-8; al final del c. 8, al c. 1!'),
           ('OJO', 'La 2.a vegada salteu del c. 6 a la casella 2 (c. 9).')]),
        B(3, 'cc. 9-12', 'Casella 2 i puja el so', (2, 2),
          D('cadena', 'Els matisos del bloc',
            [('mf', False), ('f · Primo c. 10', False), ('mf · Secondo c. 11', True)]),
          [('SECONDO', 'Acords amb ♯ i becaire (cc. 9-10). Des del c. 11, acords llargs i '
                       'baix en negres.'),
           ('PRIMO', "C. 10: puja a f. C. 11: un acord de dues notes a la dreta."),
           ('JUNTAS', 'Els quatre compassos en bucle, amb el canvi de matís.'),
           ('OJO', 'Les alteracions valen només al seu compàs.')]),
        B(4, 'cc. 13-16', 'Acords llargs', (3, 3),
          D('cadena', 'La melodia del c. 13',
            [('Sol', False), ('Fa♯', False), ('Mi', False), ('Re', True)]),
          [('SECONDO', 'Acords llargs i baix en negres. C. 16: blanca i dues negres.'),
           ('PRIMO', 'C. 13: quatre negres que baixen. C. 16: dues blanques.'),
           ('JUNTAS', 'Cc. 13-16 seguits, sense parar.'),
           ('OJO', 'Do♯ al final del baix del c. 16 (Secondo).')]),
        B(5, 'cc. 17-20', 'Torna el tema', (4, 4),
          D('cadena', 'Els matisos del c. 19',
            [('Primo mf', False), ('Secondo mp', True)]),
          [('SECONDO', 'Cc. 17-18: acords seguits i baix que puja. C. 19: torna mp.'),
           ('PRIMO', "Cc. 17-18: semicorxeres també a l'esquerra. C. 19: el tema, en mf."),
           ('JUNTAS', 'Dos compassos cada cop: 17-18 i 19-20.'),
           ('OJO', 'Els cc. 19-20 són com els cc. 1-2.')]),
        B(6, 'cc. 21-24', 'Cap al final', (5, 5),
          D('cuenta', 'Tresset: tres notes iguals en un temps', [('c. 24 · temps 4', 1, 3)]),
          [('SECONDO', 'Cc. 21-22: acords llargs amb ♭ i ♯. C. 24: tresset al 4t temps.'),
           ('PRIMO', 'C. 21: tema curt. C. 22: rodona (4 temps). C. 24: una alteració.'),
           ('JUNTAS', 'Practiqueu només el tresset del c. 24, i després el compàs sencer.'),
           ('OJO', 'Tresset = tres notes iguals en el temps d\'una negra.')]),
        B(7, 'cc. 25-28', 'Final: f, p, f', (6, 6),
          D('cadena', 'Primo · Secondo als cc. 25, 26 i 27',
            [('f · mf', False), ('p · pp', False), ('f · mf', True)]),
          [('SECONDO', 'Acords al 2 i al 4 amb ♯ i becaire. Baix en blanques i negres.'),
           ('PRIMO', 'Cc. 25-27: el mateix dibuix amb tres matisos. C. 28: Sol, Fa♯, Sol.'),
           ('JUNTAS', 'El c. 26 molt fluix: els dos alhora.'),
           ('A TEMPO', 'Tota la peça amb la repetició, sense parar.')]),
    ],
    sub_guia='Cada bloc: primer cada part sola, després juntes i a tempo.',
    lista=['Toco la meva part de memòria, almenys els primers blocs.',
           "Compto 1-2-3-4 i comencem a l'hora.",
           'Sé quan torno al c. 1 i quan salto a la casella 2.',
           'He tocat el tresset del c. 24 sense ensopegar.',
           "He tocat les dues parts (Primo i Secondo)."],
    inicio={1: 87, 2: 48, 3: 48, 4: 48},
    cortes={1: [390, 438], 2: [340, 390], 3: [342, 390]},
    fin={1: 735, 2: 690, 3: 678, 4: 354},
    burb={
        0: [('arriba', 262, 'AMB', 'mf (Primo) i mp (Secondo): la melodia sona una mica més. '
                                   'Compteu 1-2-3-4.', 0.05),
            ('arriba', 262, 'PRIMO', "Les dues mans, una octava més aguda. Els cc. 2, 3 i 4 són "
                                     "iguals.", 0.45),
            ('abajo', 262, 'SEC', 'Acords al 2 i al 4; a baix, blanques.', 0.3)],
        1: [('arriba', 520, 'OJO', 'Casella 1 (cc. 7-8): al final tornes al c. 1. La 2.a vegada '
                                   'salta del c. 6 a la casella 2 (c. 9). Apunta-ho amb llapis!',
             0.65),
            ('abajo', 520, 'PRIMO', 'C. 7: Re♯. C. 8: Si♭ a l\'esquerra.', 0.72)],
        2: [('arriba', 262, 'AMB', 'Casella 2 (cc. 9-10). C. 10: f al Primo.', 0.4),
            ('arriba', 262, 'SEC', 'C. 11: mf. Acords llargs i baix en negres.', 0.75)],
        3: [('arriba', 262, 'PRIMO', 'C. 13: quatre negres que baixen: Sol-Fa♯-Mi-Re.', 0.05),
            ('arriba', 262, 'SEC', 'C. 16: Do♯ al final del baix.', 0.95)],
        4: [('arriba', 262, 'SEC', 'C. 18: el baix puja en negres.', 0.42),
            ('arriba', 262, 'AMB', 'C. 19: torna el tema del c. 1. Primo mf, Secondo mp.',
             0.65)],
        5: [('arriba', 262, 'PRIMO', 'C. 22: rodona, quatre temps sencers.', 0.3),
            ('arriba', 262, 'OJO', 'C. 24: tresset! Tres notes iguals en un temps: fes-ho a '
                                   'poc a poc.', 0.95)],
        6: [('arriba', 520, 'AMB', 'Cc. 25-27: f, p, f al Primo i mf, pp, mf al Secondo. '
                                   'Contrasteu bé.', 0.3),
            ('abajo', 520, 'OJO', 'Final: Sol, Fa♯, Sol al Primo. Deixeu anar a l\'hora i '
                                  'somriu!', 0.97)],
    },
    misol=dict(
        manos="Poseu-hi veu: digues «jin-gle BELL» mentre toques el ritme. Si ho dius, ho "
              "toques!",
        guia="Si us perdeu a la repetició, recordeu: 1.a vegada casella 1, 2.a vegada casella "
             "2. Apunteu-ho amb llapis!",
        pauta="Inventa un ritme nou amb corxera amb puntet + semicorxera + negra, com al c. 1, "
              "i escriu-lo aquí."),
    marcas=[],
    pie_pauta="la clau la poses tu · copia un compàs o escriu l'escala de Sol major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_jingle.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
