# -*- coding: utf-8 -*-
"""Pieza 6 · La vie en rose (Louiguy / Edith Piaf), arreglo de nephele.kulichki.com. MEDIDO a zoom
   (170-250 dpi) sobre el PDF (2 paginas A4, 8 sistemas): compas C (4/4), sin armadura, "Slowly".
   Empieza con un compas incompleto de un tiempo (anacrusa, no numerado: el sistema 2 empieza en el
   "4" tras anacrusa + cc. 1-3); numeros impresos 4,7,11,15,19,23,26 -> 27 compases numerados.
   Doble barra al final del c. 6; fermatas en los cc. 2, 22 y 27; "rit." c. 6; barra de repeticion
   |: al empezar el c. 7 ("a tempo", mp - mf) y :| al final del c. 26; casilla "1." (c. 26) y "2."
   (c. 27: "rall.", p, acordes arpegiados, sextillo de semicorcheas en la izquierda, barra final).
   Tonalidad: armadura vacia; bajo y acorde de Do en los cc. 7-8 y 26-27 (Do mayor, deducida por los
   acordes). Figura mas corta: semicorchea (sextillo del c. 27); en el resto, corchea."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=6, slug='vie_en_rose', pdf='edith_piaf_la_vie_en_rose_pdf.pdf', time_sig=(4, 4),
    titulo='La vie en rose', autor='Louiguy · lletra original d\'Édith Piaf',
    kicker='Eva · peça 6 · La vie en rose', mes='Gener · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=la+vie+en+rose+piano+tutorial',
    credito='Partitura: Louiguy, La vie en rose (nephele.kulichki.com). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '4/4'), ('Tempo', 'Slowly (lent)'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '27 + anacrusi')],
        total=27,
        secciones=[('A', 1, 6, 'Introducció', AZUL), ('B', 7, 18, 'El tema · es repeteix', OCRE),
                   ('C', 19, 27, 'Canvi, caselles i final', AZUL)],
        ideas=[('IZQUIERDA', 'Notes llargues i acords',
                'Al tema, quasi sempre dues notes llargues per compàs: baix greu i acord.'),
               ('DERECHA', 'Corxeres i acords',
                'La melodia va en corxeres lligades, amb acords de dues i tres notes a sota.'),
               ('LA REPETICIÓ', 'Dos finals',
                'Del c. 7 al c. 26 es repeteix: casella 1 (c. 26) la 1.a vegada; casella 2 (c. 27) la 2.a.'),
               ('LES PAUSES', 'Fermates, rit. i rall.',
                'Fermates als cc. 2, 22 i 27. "rit." al c. 6 i "rall." al c. 27.')],
        especial=[
            'Hi diu "Slowly" (lent). El compàs és C, és a dir, 4/4.',
            'No hi ha armadura: ni sostinguts ni bemolls fixos. És Do major: els baixos dels cc. '
            '7-8 i 26-27 són de Do.',
            'Comença amb un compàs incomplet d\'un temps (anacrusi), que no es numera.',
            'Les dues ratlletes // dels cc. 2-5 marquen una pausa breu.',
            'Al c. 7 hi ha barra de repetició, "a tempo" i mp - mf. Acaba al c. 26.',
            'El c. 27 duu acords arpegiats (línia ondulada), "rall.", p i sis notes ràpides '
            '(sextolet) a l\'esquerra.'],
        reto='Comptar bé les pauses i les fermates, i recordar per on es torna a la '
             'repetició i quina casella toca cada vegada.',
        truco='Abans de tocar, recorre la partitura amb el dit: 1-6, després 7-26, tornada al 7, '
              'fins al 25 i salt a la casella 2 (c. 27).',
        sabias='La música és de Louiguy, escrita el 1945, i la lletra original en francès és d\'Édith Piaf, que la va gravar el 1947. Mack David va fer la lletra en anglès.',
        qr_texto='Escolta-la amb la partitura al davant: marca les fermates i el rit.',
        ts=(4, 4)),
    manos=dict(
        izq=[('Notes llargues', 'Al tema l\'esquerra toca dues notes llargues per compàs. Toca '
                                'només els cc. 7-10, a poc a poc, fins que surtin sense mirar.'),
             ('Canvi d\'acord', 'Abans de cada compàs mira quin acord ve i col·loca la mà '
                                'abans de tocar.'),
             ('Quan canvia el dibuix', 'Als cc. 19-22 l\'esquerra va en negres amb notes '
                                       'llargues a sota, i al c. 27 hi ha sis notes ràpides.'),
             ('Amb fermata', 'Als cc. 2 i 22 hi ha fermata: aguanta la nota i compta.')],
        der=[('Cantar la melodia', 'Les corxeres van lligades en frases curtes. Canta-les per '
                                   'dins i respira en acabar cada lligadura.'),
             ('Els acords', 'Sota la melodia hi ha notes de dos i tres sons. Toca-les '
                            'juntes, sense que en sobresurti cap.'),
             ('Alteracions', 'Als cc. 19-22 cada compàs comença amb una alteració: ♭, ♮, ♯ '
                             'i ♮. Digues cada nota a poc a poc.'),
             ('Amb l\'esquerra', 'Uneix a poc a poc quatre compassos amb l\'esquerra ja segura.')],
        tecnica=['Canell solt: les corxeres lligades surten cantades.',
                 'Compta 1-2-3-4 a poc a poc, també a les pauses.',
                 'Mira on comença i acaba la repetició abans de tocar.']),
    bloques=[
        B(1, 'cc. 0-3', 'L\'anacrusi', (0, 0),
          D('cuenta', 'Una anacrusi d\'1 temps i un compàs de 4',
            [('anac.', 1, 2), ('c. 1', 4, 2)]),
          [('IZQUIERDA', 'Un sol acord a l\'anacrusi i quatre acords de negra al c. 1.'),
           ('DERECHA', 'Dues corxeres lligades a l\'anacrusi. Al c. 2, nota amb fermata.'),
           ('JUNTAS', 'Compta 1-2-3 en silenci i entra al 4. Aguanta la fermata del c. 2.'),
           ('A TEMPO', 'Slowly: lent. Les ratlletes // demanen una pausa breu.')]),
        B(2, 'cc. 4-6', 'Es frena', (1, 1),
          D('cadena', 'Cap a la doble barra',
            [('cc. 4-5: frases amb //', False), ('c. 6: rit.', False), ('doble barra', True)]),
          [('IZQUIERDA', 'Blanques lligades, silenci de corxera i acords: mira on cau cadascun.'),
           ('DERECHA', 'Frases curtes de corxeres lligades. Respira a les ratlletes //.'),
           ('JUNTAS', 'Primer la dreta cantant; després afegeix l\'esquerra.'),
           ('OJO', 'rit. al c. 6: frena a poc a poc fins a la doble barra.')]),
        B(3, 'cc. 7-10', 'Comença el tema', (2, 2),
          D('cadena', 'Des d\'aquí es repeteix',
            [('barra |: al c. 7', False), ('a tempo · mp - mf', True)]),
          [('IZQUIERDA', 'Dues blanques per compàs als cc. 7-8 (baix i acord). Al c. 9, '
                         'blanca i dues negres.'),
           ('DERECHA', 'Corxeres lligades amb acords. Al c. 9 hi ha un regulador <, al c. 10 '
                       'un >.'),
           ('JUNTAS', 'Un compàs cada vegada (7, 8, 9, 10) i després els quatre en bucle.'),
           ('A TEMPO', 'a tempo i mp - mf: so mitjà, sense córrer.')]),
        B(4, 'cc. 11-18', 'El tema segueix', (3, 4),
          D('capas', 'Dues capes alhora',
            [('Dreta: melodia', 'barras', AZUL), ('Esquerra: notes llargues', 'puntos', OCRE)]),
          [('IZQUIERDA', 'Al c. 14 hi ha quatre negres amb un sostingut i un becaire: mira-les '
                         'abans.'),
           ('DERECHA', 'Cc. 15-16 molt semblants als 7-8. Al c. 17 hi ha un bemoll i el c. 18 '
                       'acaba en un acord llarg.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 11-14 i cc. 15-18.'),
           ('OJO', 'Reguladors als cc. 13-14 i 17-18: puja i baixa el so sense accentuar.')]),
        B(5, 'cc. 19-22', 'Canvia el dibuix', (5, 5),
          D('cadena', 'El que canvia',
            [('dreta: corxeres repetides', False), ('esquerra en negres', False),
             ('fermata c. 22', True)]),
          [('IZQUIERDA', 'Quatre negres a dalt i notes llargues greus a sota. Alteracions: ♭ al '
                         '19, ♯ al 21.'),
           ('DERECHA', 'Notes repetides, corxeres i negres, regulars i suaus. Un regulador a '
                       'cada compàs.'),
           ('JUNTAS', 'Compàs a compàs, a poc a poc, fins a unir-los sense parar.'),
           ('OJO', 'Fermata al c. 22 (a les dues mans): aguanta i compta abans de seguir.')]),
        B(6, 'cc. 23-25', 'Torna el tema', (6, 6),
          D('cadena', 'Cap a les caselles',
            [('c. 23: tema', False), ('c. 25: lligadura', False), ('casella 1 o 2', True)]),
          [('IZQUIERDA', 'Dues blanques per compàs als cc. 23-24. Al c. 25: blanca, dues '
                         'corxeres i negra.'),
           ('DERECHA', 'Frase semblant a la dels cc. 7-9. El c. 25 acaba amb una lligadura cap '
                       'al compàs següent.'),
           ('JUNTAS', 'Els tres compassos en bucle.'),
           ('OJO', 'La nota lligada del c. 25 continua a la casella 1 i a la casella 2: no la '
                   'premis un altre cop.')]),
        B(7, 'cc. 26-27', 'Caselles i final', (7, 7),
          D('cadena', 'Les dues voltes',
            [('1.a vegada: casella 1', False), ('↩ al c. 7', False), ('2.a vegada: casella 2', True)]),
          [('IZQUIERDA', 'Casella 1: negres i acords. Casella 2: sis notes ràpides que pugen '
                         '(sextolet).'),
           ('DERECHA', 'Casella 1: corxeres amb ♭ i ♮. Casella 2: acords arpegiats i fermata.'),
           ('JUNTAS', 'Recorre-ho amb el dit: 7→26, tornada al 7, fins al 25 i salt al 27.'),
           ('A TEMPO', 'rall.: frena a poc a poc i acaba en p. Aguanta la fermata.')]),
    ],
    cortes={1: [273.2, 420.2, 588.8], 2: [223.2, 396.8, 547.5]},
    corte_titulo=125.5, inicio={2: 56.0},
    burb={
        0: [('arriba', 250, 'OJO', 'Slowly: lent. Compàs C (4/4), sense sostinguts ni bemolls '
                                   'fixos.', 130),
            ('arriba', 250, 'AMB', 'Fermata del c. 2: aguanta la nota. Les ratlletes // són una '
                                   'pausa breu.', 330),
            ('abajo', 330, 'IZQ', 'Anacrusi: el compàs comença incomplet, amb un sol acord d\'un '
                                  'temps. No es numera.', 135)],
        1: [('arriba', 480, 'OJO', 'rit. al c. 6: frena a poc a poc fins a la doble barra.',
             481)],
        2: [('arriba', 300, 'AMB', 'Barra |: del c. 7, "a tempo" i mp - mf. Des d\'aquí es '
                                   'repeteix.', 88)],
        3: [('arriba', 500, 'OJO', 'c. 14: sostingut i becaire a les quatre negres, a les dues '
                                   'mans.', 500)],
        5: [('arriba', 540, 'OJO', 'Fermata del c. 22, a les dues mans: aguanta i compta.', 546),
            ('abajo', 330, 'AMB', 'Cada compàs comença amb una alteració: ♭ (c. 19), ♮ (c. 20), '
                                  '♯ (c. 21) i ♮ (c. 22).', 300)],
        6: [('arriba', 520, 'AMB', 'c. 25: la lligadura del final uneix amb la primera nota de la '
                                   'casella. No la premis un altre cop.', 530)],
        7: [('arriba', 250, 'OJO', 'Casella 1 (c. 26): la primera vegada. Acaba en :| i tornes al '
                                   'c. 7.', 110),
            ('arriba', 250, 'AMB', 'Casella 2 (c. 27): la segona vegada. "rall." i p, amb acords '
                                   'arpegiats.', 350),
            ('abajo', 400, 'IZQ', 'Sis notes ràpides que pugen (sextolet): estudia-les a part, '
                                  'a poc a poc.', 470)],
    },
    marcas=[(1, 323.5, 151, 21, 16, 1, 1, 'caja'), (1, 483, 357, 26, 16, 2, 1, 'caja'),
            (1, 113, 506, 74, 34, 3, 1, 'caja'), (2, 547, 244, 26, 16, 5, 1, 'caja'),
            (2, 179, 561, 210, 16, 7, 1, 'caja'), (2, 417, 561, 258, 16, 7, 2, 'caja')],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Do major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_vie_en_rose.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
