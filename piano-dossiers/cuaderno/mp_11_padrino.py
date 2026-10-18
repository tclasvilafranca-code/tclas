# -*- coding: utf-8 -*-
"""Pieza 11 · El Padrino (Nino Rota), arreglo para piano (escaneado a ~60 ppi). MEDIDO sobre el PDF
   a zoom (3 pags, A4, 14 sistemas, 51 compases numerados en el margen): 4/4 sin cambios de compas,
   armadura de tres bemoles y, tras la doble barra del c.33, seis bemoles; negra = 83 (c.1) y
   negra = 140 (c.32); letras A (c.1), A' (c.10), B (c.18), A (c.22), A'' (c.34); izquierda en
   silencio en los cc.1 y 10; tresillos de corcheas en la izquierda (cc.5-6 y 25-26); subida de
   semicorcheas ligadas en la izquierda (c.14); acordes arpegiados (linea ondulada); matices mp,
   mf, f, p, sf; "accelerando poco a poco" (c.29); calderon (c.32); semicorchea la figura corta.
   El credito del arreglista se lee 'ANDRE JAHJAH' pero el escaneo es borroso: no se imprime."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=11, slug='padrino', pdf='el_padrino.pdf', time_sig=(4, 4),
    titulo='El Padrí', autor='Nino Rota · arranjament per a piano',
    kicker='Eva · peça 11 · El Padrí', mes='Abril · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=el+padrino+the+godfather+nino+rota+piano+tutorial',
    credito='Partitura: N. Rota, El Padrí (arranjament per a piano). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do menor → 6 bemolls'), ('Compàs', '4/4'),
               ('Tempo', '♩=83 → ♩=140'), ('Figura curta', 'Semicorxera'), ('Compassos', '51')],
        total=51,
        secciones=[('A', 1, 9, 'El tema', AZUL), ('A\'', 10, 17, 'Acords arpegiats', OCRE),
                   ('B', 18, 21, 'Nova', AZUL), ('A', 22, 33, 'Torna i accelera', OCRE),
                   ('A\'\'', 34, 51, 'Sis bemolls · ♩=140', AZUL)],
        ideas=[('IZQUIERDA', 'Baix i tresquiàlteres',
                'Calla al c. 1; després, baix i acords curts. Tresquiàlteres de corxeres als '
                'cc. 5-6 i 25-26.'),
               ('DERECHA', 'El tema, entre silencis',
                'Entra després d\'un silenci, en corxeres, i més endavant duu acords amb línia '
                'ondulada (arpegi).'),
               ('EL CANVI', 'Més ràpid',
                '"accelerando poco a poco" al c. 29, ♩=140 al c. 32 i sis bemolls des del '
                'c. 34.'),
               ('ELS MATISOS', 'mp · mf · f · p · sf',
                'Comença en mp, creix a mf i f, baixa a p a la lletra B i torna a pujar.')],
        especial=[
            'Posa negra = 83 al principi i negra = 140 al c. 32.',
            'És 4/4 d\'un cap a l\'altre: no hi ha canvis de compàs.',
            'Tres bemolls (si♭, mi♭, la♭); després de la doble barra del c. 33 passa a sis.',
            'Lletres: A (c. 1), A\' (c. 10), B (c. 18), A (c. 22) i A\'\' (c. 34).',
            'L\'esquerra calla als cc. 1 i 10 i fa tresquiàlteres als cc. 5-6 i 25-26.',
            'Hi ha acords amb línia ondulada (arpegi), "accelerando" al c. 29 i calderó al '
            'c. 32.'],
        reto='Controlar el canvi de ritme: de ♩=83 a l\'acceleració del c. 29 i al ♩=140 sense que '
             'se t\'escapi la mà.',
        truco='Estudia per lletres, una per dia: A (cc. 1-9), A\' (cc. 10-17), B (cc. 18-21)... '
              'Les tresquiàlteres, soles i a poc a poc, dient "tri-o-la".',
        sabias='Nino Rota va compondre la música d\'«El Padrí» (1972), i també la de moltes pel·lícules de Fellini.',
        qr_texto='Escolta-ho amb la partitura al davant: notes on accelera?', ts=(4, 4)),
    manos=dict(
        izq=[('Calla i entra', 'Als cc. 1 i 10 l\'esquerra no toca. Del c. 2: baix i acords '
                               'curts; al c. 3 puja en quatre corxeres fins a una blanca.'),
             ('Les tresquiàlteres', 'Als cc. 5-6 hi ha dues tresquiàlteres de corxeres (tres notes per '
                               'temps) i una blanca. Digues "tri-o-la" i puja amb el regulador.'),
             ('La pujada del c. 14', 'Vuit semicorxeres lligades que pugen fins a una blanca. '
                                     'Estudia-les soles, molt a poc a poc, i accelera de mica en mica.'),
             ('Acords i calderó', 'Als cc. 29-33 són acords. Al c. 32 baixa en vuit '
                                    'corxeres amb calderó a la primera nota.')],
        der=[('Entrar a contratemps', 'Al c. 1 hi ha silenci de blanca i de corxera, i entren tres '
                                    'corxeres. Compta 1-2-3-i i entra a la "i".'),
             ('Tres corxeres al final', 'Als cc. 5-7 cada compàs acaba amb tres corxeres que '
                                        'pugen: és el mateix gest, après un cop.'),
             ('Acords arpegiats', 'Als cc. 10-17 hi ha acords amb línia ondulada: toca les '
                                    'notes de baix a dalt, ràpid, i continua amb les corxeres.'),
             ('L\'acceleració', 'Els cc. 29-30 són semicorxeres de mp a f. Comença lenta i puja '
                                'la velocitat de mica en mica.')],
        tecnica=['Compta 1-2-3-4 i no et saltis els silencis.',
                 'Accelera de mica en mica, no de cop: primer lent, després ràpid.',
                 'Els acords arpegiats, amb el canell solt i sense fer força.']),
    bloques=[
        B(1, 'cc. 1-4', 'El tema en mp', (0, 0),
          D('cadena', 'Primer de tot', [('♩=83', False), ('mp', False), ('regulador < a mf (c. 3)', True)]),
          [('IZQUIERDA', 'Calla al c. 1. Baix i acords curts; al c. 3 puja en 4 corxeres.'),
           ('DERECHA', 'Silenci de blanca i de corxera, i entren tres corxeres. Compta 1-2-3-i.'),
           ('JUNTAS', 'Compta 1-2-3-i i entra la dreta; l\'esquerra no toca fins al c. 2.'),
           ('A TEMPO', 'Negra = 83: lent. Comença en mp i creix cap a mf.')]),
        B(2, 'cc. 5-8', 'Les tresquiàlteres', (1, 1),
          D('grupos', 'Tresquiàltera: 3 notes en un temps', (2, 3, ['tri-o-la', 'tri-o-la'])),
          [('IZQUIERDA', 'Cc. 5-6: dues tresquiàlteres de corxeres i una blanca. Cc. 7-8: sis '
                         'corxeres i quatre negres.'),
           ('DERECHA', 'Cada compàs es tanca amb tres corxeres que pugen (cc. 5-7).'),
           ('JUNTAS', 'Una mà compta "tri-o-la" mentre l\'altra toca les tres corxeres.'),
           ('OJO', 'mp al c. 5 i mf al c. 6: puja el so amb el regulador.')]),
        B(3, 'cc. 9-12', 'Acords arpegiats (A\')', (2, 2),
          D('cadena', 'La lletra A\'', [('f i mp (c. 9)', False), ('A\' al c. 10', False),
                                      ('acord arpegiat', True)]),
          [('IZQUIERDA', 'Nota llarga al c. 9, silenci al c. 10, i després negra i blanca.'),
           ('DERECHA', 'Dues veus: a dalt corxeres, a baix negres, amb arpegis.'),
           ('JUNTAS', 'Només el c. 9 i el c. 10; després el c. 11.'),
           ('OJO', 'La línia ondulada: toca les notes de baix a dalt, ràpid.')]),
        B(4, 'cc. 13-16', 'La pujada del c. 14', (3, 3),
          D('cadena', 'Els cc. 13-16', [('acords (c. 13)', False), ('pujada en semicorxeres', False),
                                        ('f i acords (c. 15)', True)]),
          [('IZQUIERDA', 'C. 14: vuit semicorxeres lligades que pugen a una blanca. A poc a poc.'),
           ('DERECHA', 'Acords arpegiats i tres corxeres al final de cada compàs.'),
           ('JUNTAS', 'Un compàs cada cop, i els quatre seguits.'),
           ('OJO', 'f al c. 15 i acords amb sostinguts a l\'esquerra.')]),
        B(5, 'cc. 17-24', 'La part B i tornada d\'A', (4, 5),
          D('cadena', 'El canvi', [('doble barra: B en p (c. 18)', False),
                                    ('torna A en mf (c. 22)', True)]),
          [('IZQUIERDA', 'A la B puja i baixa en vuit corxeres per compàs. Al c. 22 torna el '
                         'baix del tema.'),
           ('DERECHA', 'La B comença amb una blanca i corxeres en p; llegeix-la a poc a poc.'),
           ('JUNTAS', 'La B compàs a compàs; l\'A ja la coneixes.'),
           ('OJO', 'Sostinguts al c. 20 (dues semicorxeres a l\'esquerra).')]),
        B(6, 'cc. 25-33', 'S\'accelera', (6, 8),
          D('cadena', 'Cap al canvi', [('tresquiàlteres (cc. 25-26)', False),
                                          ('accelerando (c. 29)', False),
                                          ('♩=140 i calderó (c. 32)', True)]),
          [('IZQUIERDA', 'Tresquiàlteres als cc. 25-26, després acords i al c. 32 vuit corxeres '
                         'que baixen.'),
           ('DERECHA', 'Semicorxeres als cc. 29-30, de mp a f; sf als cc. 31-33.'),
           ('JUNTAS', 'Comença lent i ves accelerant a poc a poc.'),
           ('A TEMPO', 'Calderó al c. 32; després, negra = 140.')]),
        B(7, 'cc. 34-41', 'Sis bemolls (A\'\')', (9, 10),
          D('cadena', 'El que canvia', [('doble barra', False), ('sis bemolls', False),
                                         ('♩=140 en f', True)]),
          [('IZQUIERDA', 'El mateix baix del tema, ara amb sis bemolls.'),
           ('DERECHA', 'El tema en f, en corxeres; acords i blanques entre les frases.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 34-37 i cc. 38-41.'),
           ('OJO', 'Sis bemolls al principi de cada pentagrama; mp al c. 41.')]),
        B(8, 'cc. 42-51', 'El final', (11, 13),
          D('cadena', 'Cap al final', [('mp (c. 45)', False), ('mf (c. 48)', False),
                                         ('mp (c. 49)', False), ('acord final', True)]),
          [('IZQUIERDA', 'Mateix baix; als cc. 50-51 només blanques.'),
           ('DERECHA', 'Corxeres sota una lligadura llarga i acords arpegiats al final.'),
           ('JUNTAS', 'Tres sistemes: cc. 42-45, 46-49 i 50-51.'),
           ('A TEMPO', 'Doble barra final: aguanta l\'últim acord.')]),
    ],
    cortes={1: [320.0, 452.0, 600.0], 2: [212.5, 333.0, 454.5, 588.2],
            3: [225.5, 351.5, 475.5, 605.0]},
    corte_titulo=184.5, fin={2: 730.0, 3: 736.0},
    burb={
        0: [('arriba', 330, 'AMB', 'Negra = 83, 4/4 i tres bemolls. Comença en mp: l\'esquerra '
                                   'calla i la dreta entra amb tres corxeres.', 0.12)],
        1: [('arriba', 330, 'IZQ', 'Tresquiàlteres als cc. 5-6: tres notes a cada temps, i puja '
                                   'amb el regulador fins a mf.', 0.12)],
        2: [('arriba', 330, 'DER', 'Lletra A\': acords amb línia ondulada, toca de baix a dalt. '
                                   'L\'esquerra calla al c. 10.', 0.32)],
        3: [('arriba', 330, 'IZQ', 'C. 14: pujada de vuit semicorxeres lligades, a poc a poc i '
                                   'regulars. Al c. 15 arriba f.', 0.35)],
        4: [('arriba', 300, 'AMB', 'Doble barra: comença la B en p (c. 18). L\'esquerra puja i '
                                   'baixa en corxeres.', 0.35)],
        6: [('arriba', 300, 'IZQ', 'Altra vegada les tresquiàlteres (cc. 25-26), com als cc. 5-6.',
             0.12)],
        7: [('arriba', 330, 'OJO', '"accelerando poco a poco": semicorxeres de mp a f; puja la '
                                   'velocitat a poc a poc.', 0.2)],
        8: [('arriba', 330, 'AMB', 'C. 32: calderó i ♩=140. Després de la doble barra del c. 33, '
                                   'sis bemolls.', 0.5)],
        9: [('arriba', 330, 'AMB', 'Lletra A\'\' en f: sis bemolls i ♩=140. És el tema una altra vegada.',
             0.1)],
        12: [('arriba', 330, 'OJO', 'mf al c. 48 i mp al c. 49: el so baixa de cop.',
              0.5)],
        13: [('arriba', 330, 'AMB', 'Corxeres sota una lligadura llarga i acords arpegiats. Fi.',
              0.4)],
    },
    marcas=[],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Do menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_padrino.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
