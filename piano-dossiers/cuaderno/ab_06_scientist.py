# -*- coding: utf-8 -*-
"""Pieza 6 · The Scientist (Coldplay), versio facil. MEDIDO sobre el PDF de Musescore (2 paginas,
   43 compases en 9 sistemas de 7, 4, 4, 3, 4, 4, 4, 5 y 8): un bemol (Fa mayor), 4/4, sin tempo
   ni matices ni repeticiones, corchea como figura mas corta, sin digitacion impresa, letra
   impresa. Izquierda: una redonda por compas (Re, Si bemol, Fa, Do en los cc. 1-4, que se repiten
   en los cc. 5-8); derecha en los cc. 1-8: acordes de dos notas a cada tiempo (Fa-La sobre Re y
   Fa; Fa-Si bemol sobre Si bemol; Fa-Sol sobre Do = cuarta suspendida), con dos corcheas
   al final de los cc. 2 y 6. La melodia entra en el c. 9 (corcheas ligadas a notas largas) y
   los cc. 36-43 vuelven a los acordes del principio."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=6, slug='scientist', pdf='the_scientist.pdf', time_sig=(4, 4),
    titulo='The Scientist',
    autor='Coldplay · versió fàcil (Musescore)',
    kicker='Abril · peça 6 · The Scientist', mes='Febrer · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=coldplay+the+scientist+piano+easy+tutorial',
    credito='Partitura: «The Scientist» (Coldplay), versió fàcil de Musescore. Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Fa major'), ('Compàs', '4/4'), ('Tempo', 'Sense indicar'),
               ('Figura curta', 'Corxera'), ('Compassos', '43')],
        total=43,
        secciones=[('A', 1, 8, 'Els acords', AZUL), ('B', 9, 24, 'La melodia canta', OCRE),
                   ('C', 25, 35, 'El cor: puja', AZUL), ('D', 36, 43, 'Tornen els acords', OCRE)],
        ideas=[('ESQUERRA', 'Una rodona per compàs',
                'Una sola nota llarga a cada compàs: Re, Si♭, Fa i Do. Només cal comptar fins a '
                'quatre.'),
               ('DRETA', 'Acords de dues notes',
                'Als cc. 1-8, dues notes juntes a cada temps. Després, la melodia canta amb '
                'corxeres.'),
               ('ELS ACORDS', 'Re menor · Si♭ · Fa · Do',
                'Quatre acords que giren: Re menor, Si♭ major, Fa major i Do (dominant, amb '
                'quarta suspesa).'),
               ('EL FINAL', 'Torna el principi',
                'Els cc. 36-43 repeteixen els acords del començament i acaba en Fa major.')],
        ideas_pie='Els acords surten sempre en aquest ordre: quan te\'l sàpigues, tens mitja '
                  'cançó feta.',
        especial=[
            "Armadura d'un bemoll (Si♭): la peça està en Fa major.",
            'Compàs de 4/4: quatre negres per compàs. No porta tempo ni matisos escrits.',
            "L'esquerra toca una sola rodona a cada compàs, de principi a fi.",
            'Els cc. 5-8 repeteixen els cc. 1-4.',
            'La melodia entra al c. 9. Moltes notes van lligades a una nota llarga.',
            'La lletra va impresa sota la melodia: serveix per cantar mentre toques.',
            'No hi ha repeticions: 43 compassos seguits.'],
        reto='Que els acords de la dreta sonin tots iguals, sense accents, mentre '
             "l'esquerra aguanta la rodona. Pots fer-ho?",
        truco="Canta la cançó en veu alta i després toca el que has cantat. Si la saps de "
              'memòria, la melodia surt gairebé sola.',
        sabias='«The Scientist» és de Coldplay i surt al disc «A Rush of Blood to the Head» '
               '(2002). Al videoclip, el cantant, Chris Martin, va aprendre la lletra al revés '
               'per cantar «cap enrere».',
        qr_texto='Escolta-la: sents com giren els quatre acords?', ts=(4, 4)),
    manos=dict(
        izq=[('Una rodona, un compàs', 'Toca una nota i aguanta-la quatre temps. Compta '
                                       '1-2-3-4 sense deixar-la anar.'),
             ('Les quatre notes', 'Toca Re, Si♭, Fa, Do (cc. 1-4), una a cada compàs. '
                                  "Aquest és l'esquelet de la peça."),
             ('El Si♭', "El Si és bemoll a tota la peça: és la tecla negra just a l'esquerra "
                        'del Si.'),
             ('Seguir el camí', 'Amb el dit a la partitura, compta quatre temps a cada nota. '
                                'No cal que corris.')],
        der=[('Dos sons junts', 'Toca les dues notes del primer acord (Fa i La) alhora i '
                                'prem les dues tecles a la vegada.'),
             ('Quatre temps', 'Quatre acords per compàs, un a cada temps. Compta '
                              '1-2-3-4 en veu alta.'),
             ('Les dues corxeres', 'Al final dels cc. 2 i 6 hi ha dues corxeres soltes: '
                                   'compta «4-i».'),
             ('Cantar la melodia', 'Del c. 9 en endavant, canta la lletra i busca on '
                                   'comencen les notes lligades.')],
        tecnica=['Canell solt: els acords sonen suaus, sense picar.',
                 "L'esquerra aguanta i la dreta no té pressa.",
                 'Compta 1-2-3-4 en veu alta i no paris quan canviï el compàs.']),
    bloques=[
        B(1, 'cc. 1-7', 'Els acords del principi', (0, 0),
          D('cadena', 'Els quatre acords',
            [('Re menor', False), ('Si♭', False), ('Fa', False), ('Do', True)]),
          [('IZQUIERDA', 'Una rodona per compàs: Re, Si♭, Fa, Do. Els cc. 5-7 repeteixen.'),
           ('DERECHA', 'Dues notes juntes a cada temps. Quatre acords per compàs.'),
           ('JUNTAS', 'Compta 1-2-3-4: l\'esquerra aguanta i la dreta toca a cada temps.'),
           ('OJO', 'Al final dels cc. 2 i 6 hi ha dues corxeres: compta «4-i».')]),
        B(2, 'cc. 8-11', 'Entra la melodia', (1, 1),
          D('cadena', 'De acords a melodia',
            [('c. 8: acords', False), ('c. 9: acord llarg', False), ('cc. 9-11: melodia', True)]),
          [('IZQUIERDA', 'Una rodona per compàs, com abans.'),
           ('DERECHA', "El c. 8 encara són acords. Al c. 9 comença la melodia: canta-la primer."),
           ('JUNTAS', 'Compta amb calma: la melodia entra a la segona part del compàs 9.'),
           ('OJO', 'Les notes lligades: toca la primera i aguanta, no la repeteixis.')]),
        B(3, 'cc. 12-15', 'La melodia continua', (2, 2),
          D('cadena', 'Una idea que torna',
            [('corxeres', False), ('nota llarga', True), ('respirar', False)]),
          [('IZQUIERDA', 'Segueix una rodona per compàs: quatre temps cada nota.'),
           ('DERECHA', 'Frases de corxeres que acaben lligades a una nota llarga.'),
           ('JUNTAS', 'Frase a frase: 12-13 i 14-15.'),
           ('OJO', 'Cada frase té el mateix dibuix: busca què es repeteix.')]),
        B(4, 'cc. 16-22', 'Cap al cor', (3, 4),
          D('cadena', 'Dos sistemes seguits',
            [('cc. 16-18', False), ('canvi de pàgina', False), ('cc. 19-22', True)]),
          [('IZQUIERDA', 'Una rodona per compàs. Mira a cada compàs quina nota toca.'),
           ('DERECHA', 'La melodia va fent el mateix dibuix amb petites variacions.'),
           ('JUNTAS', 'Primer cc. 16-18, després 19-22. Després, tots junts.'),
           ('OJO', 'Entre cc. 18 i 19 canvia de pàgina: no et perdis.')]),
        B(5, 'cc. 23-26', 'El cor: puja!', (5, 5),
          D('cadena', 'La part més coneguda',
            [('Heads on a science...', False), ('No-bo-dy said', False), ('it was easy', True)]),
          [('IZQUIERDA', 'Mateixes rodones: una nota per compàs.'),
           ('DERECHA', 'La melodia puja i apareixen notes llargues amb puntet.'),
           ('JUNTAS', 'Canta «Nobody said it was easy» mentre toques.'),
           ('OJO', 'Negra amb puntet: dura un temps i mig. Compta «1-2-i».')]),
        B(6, 'cc. 27-30', 'El cor segueix', (6, 6),
          D('cadena', 'Una frase que torna',
            [('cc. 23-26', False), ('és igual', True), ('cc. 27-30', False)]),
          [('IZQUIERDA', 'Una rodona per compàs, sense pressa.'),
           ('DERECHA', 'La frase del «Nobody said it was easy» torna una altra vegada.'),
           ('JUNTAS', 'Si ja saps els cc. 23-26, aquests ja els tens a mitges.'),
           ('OJO', 'Mira la lletra: et diu on respirar.')]),
        B(7, 'cc. 31-35', 'Tornar al principi', (7, 7),
          D('cadena', 'Cap als acords',
            [('melodia', False), ('últimes notes', False), ('acords', True)]),
          [('IZQUIERDA', 'Una rodona per compàs fins al final del sistema.'),
           ('DERECHA', 'La melodia acaba i la dreta torna als acords de dues notes.'),
           ('JUNTAS', 'Compta amb calma el canvi de melodia a acords.'),
           ('OJO', 'Preparat per als acords: dues notes a la vegada.')]),
        B(8, 'cc. 36-43', 'El final', (8, 8),
          D('cadena', 'Com al principi',
            [('Re menor', False), ('Si♭', False), ('Fa', False), ('Do', False),
             ('acord final', True)]),
          [('IZQUIERDA', 'Les mateixes rodones del principi: Re, Si♭, Fa, Do...'),
           ('DERECHA', 'Els acords del principi, dues vegades seguides.'),
           ('JUNTAS', 'Com als cc. 1-8: si els saps, aquests surten sols.'),
           ('A TEMPO', 'La peça sencera. Aguanta l\'últim acord el compàs sencer.')]),
    ],
    cortes={1: [229.5, 390.0, 550.8], 2: [177.5, 317.5, 458.0, 598.5]},
    corte_titulo=103.8, inicio={1: 24.0, 2: 36.8}, fin={2: 730.8},
    burb={
        0: [('arriba', 250, 'DER', 'Dues notes juntes a cada temps (Fa-La). Compta 1-2-3-4. '
                                   'Dues corxeres al final dels cc. 2 i 6.', 0.12),
            ('arriba', 250, 'IZQ', 'Una rodona per compàs: Re, Si♭, Fa, Do. Aguanta-la!', 0.55),
            ('abajo', 300, 'OJO', "El Si és bemoll a tota la peça. Compte amb la tecla negra!",
             0.8)],
        1: [('arriba', 300, 'AMB', 'Aquí entra la melodia: la dreta passa dels acords a cantar '
                                   'notes soltes.', 0.25),
            ('abajo', 300, 'OJO', 'Notes lligades: toca la primera i aguanta, no la repeteixis.',
             0.6)],
        2: [('arriba', 300, 'DER', 'Mira com la frase torna: corxeres que acaben en una nota '
                                   'llarga.', 0.2),
            ('abajo', 300, 'IZQ', 'Una rodona per compàs: només cal comptar fins a quatre.',
             0.6)],
        3: [('arriba', 300, 'AMB', 'Cada frase acaba en una nota llarga: respira abans de la '
                                   'següent.', 0.2)],
        4: [('arriba', 300, 'DER', 'Segueix la lletra amb el dit: et diu què toca després.', 0.15),
            ('abajo', 300, 'OJO', "Has passat de pàgina! Aquesta és la mateixa cançó.", 0.7)],
        5: [('arriba', 300, 'DER', 'Aquí la melodia puja: és el cor de la cançó («Nobody said it '
                                   'was easy»).', 0.15),
            ('abajo', 300, 'OJO', 'Notes amb puntet: duren un temps i mig. Compta «1-2-i».', 0.6)],
        6: [('arriba', 300, 'AMB', 'La mateixa música torna: ja la coneixes!', 0.2)],
        7: [('arriba', 300, 'IZQ', "L'esquerra sempre igual: una rodona per compàs.", 0.15),
            ('abajo', 300, 'OJO', 'Cap al final, la dreta torna als acords de dues notes.', 0.7)],
        8: [('arriba', 300, 'AMB', 'Final: els mateixos acords del principi.', 0.1),
            ('abajo', 300, 'OJO', "Aguanta l'últim acord de Fa el compàs sencer i... bravo!",
             0.85)],
    },
    marcas=[],
    misol=dict(manos='Truc: aprèn primer els quatre bassos (Re, Si♭, Fa, Do). Amb aquests quatre '
                     'ja saps mitja cançó!',
               guia='Ànim! Només hi ha quatre acords que giren. Si te\'ls aprens, el 90 % de la '
                    'peça ja és teu.',
               pauta='Copia els quatre bassos (Re, Si♭, Fa, Do) en rodones i inventa una '
                     'melodia a sobre!'),
    pie_pauta="la clau la poses tu · copia els quatre bassos o inventa una melodia en Fa major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_scientist.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
