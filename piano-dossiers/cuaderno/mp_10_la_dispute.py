# -*- coding: utf-8 -*-
"""Pieza 10 · La dispute (Yann Tiersen, de «Amelie»; transcripcion de Michael Jordan). MEDIDO sobre
   el PDF (4 pag. carta; la 1 es portada, la partitura ocupa las pp. 2-4: 14 sistemas, 99 compases;
   el c. 1 es un compas de silencio): 3/4, «Rubato (negra = 120)», tres bemoles; acaba con calderon
   (rit. en el c. 96). Izquierda: nota grave larga y dos acordes (cc. 2-50), arpegios de seis corcheas
   desde el c. 51. Derecha: notas largas (cc. 2-26), dos notas a la vez (cc. 27-50), notas largas
   (51-74), seis corcheas por compas (75-96). Dobles barras tras los cc. 26, 50 y 74. Matices: mp
   cc. 2, 27, 49; mf cc. 11, 35, 67, 83; f cc. 19, 43, 91; p cc. 51, 74, 99. Semicorcheas en el
   c. 5. Sin repeticiones ni casillas. El pentagrama de abajo lleva el rotulo «Accordion»."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=10, slug='la_dispute', pdf='yann_tiersen_la_dispute_amelie_pdf.pdf', time_sig=(3, 4),
    titulo='La dispute', autor='Yann Tiersen · de la pel·lícula «Amélie» · transcr. M. Jordan',
    kicker='Eva · peça 10 · La dispute (Tiersen)', mes='Març · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=yann+tiersen+la+dispute+amelie+piano',
    credito='Partitura: Y. Tiersen, La dispute, transcr. M. Jordan. Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do menor'), ('Compàs', '3/4'), ('Tempo', 'Rubato'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '99')],
        total=99,
        secciones=[('A', 1, 26, 'Melodia i vals', AZUL),
                   ('B', 27, 50, 'Dues notes alhora', OCRE),
                   ('C', 51, 74, 'Arpegis', VERDE),
                   ('D', 75, 99, 'Corxeres i final', AZUL)],
        ideas=[('IZQUIERDA', 'Vals i arpegi',
                'Cc. 2-50: nota greu llarga i dos acords (al 2 i al 3). Des del c. 51: arpegis '
                'de sis corxeres.'),
               ('DERECHA', 'Melodia i acords',
                'Notes llargues lligades; dues notes alhora (cc. 27-50); corxeres (cc. 75-96).'),
               ('RUBATO', 'Negra = 120',
                'El pols és flexible: es frena i s\'accelera una mica. La base la marca '
                'l\'esquerra.'),
               ('ELS MATISOS', 'mp · mf · f · p',
                'mp cc. 2, 27, 49 · mf cc. 11, 35, 67, 83 · f cc. 19, 43, 91 · p cc. 51, 74, 99.')],
        especial=[
            'Posa "Rubato" amb la negra a 120, i el compàs és 3/4: tres negres per compàs.',
            'Tres bemolls a l\'armadura (si, mi i la bemoll); acaba en un acord de Do menor.',
            'El c. 1 és un compàs de silenci: compta\'l.',
            'Dobles barres després dels cc. 26, 50 i 74: canvia la textura.',
            'Becaires a la melodia i als acords; semicorxeres lligades al c. 5.',
            'Acaba amb rit. (c. 96) i un calderó al c. 99. No hi ha repeticions.'],
        reto='Tocar amb rubato sense perdre la base: l\'esquerra marca el pols i la dreta canta '
             'amb llibertat.',
        truco='Els cc. 33-48 duen a l\'esquerra el mateix que els cc. 9-24: aprèn-ne un i tindràs '
              'l\'altre. Estudia per sistemes, no compàs a compàs.',
        sabias='«La dispute» (en francès, «la disputa») és de Yann Tiersen i sona a la pel·lícula «Amélie» (2001).',
        qr_texto='Escolta-la i fixa\'t en com la melodia respira amb el rubato.', ts=(3, 4),
        cuenta_pie='Un compàs de 3/4: tres cops, cadascun amb dues corxeres. Aquí només el '
                   'ritme, sobre una nota qualsevol.'),
    manos=dict(
        titulo='Mà esquerra i mà dreta',
        sub='Cada mà sola, per blocs. Després juntes i a poc a poc.',
        izq=[('Nota llarga i dos acords', 'Cc. 2-50: una nota greu llarga al 1 i dos acords '
                                          'curts al 2 i al 3. Compta "un-dos-tres".'),
             ('Canviar de nota greu', 'La nota greu canvia cada dos compassos (Mi bemoll, Re, Fa, '
                                       'Do...). Mira la que ve i posa-hi ja la mà.'),
             ('L\'arpegi', 'Des del c. 51, sis corxeres lligades per compàs. Un compàs, '
                            'a poc a poc, deu cops seguits.'),
             ('Regular i suau', 'Totes les corxeres iguals i en p: la melodia mana.')],
        der=[('Cantar la melodia', 'Notes llargues amb lligadures: canta-les per dins abans de '
                                   'tocar-les.'),
             ('Dues notes alhora', 'Cc. 27-50: dues notes juntes. Toca-les totes dues amb el mateix '
                                    'pes i vigila els becaires.'),
             ('Les corxeres', 'Cc. 75-96: sis corxeres lligades per compàs, com l\'esquerra. '
                              'Primer sola i a poc a poc.'),
             ('Amb rubato', 'Quan surti amb l\'esquerra, deixa respirar la frase en acabar '
                            'cada lligadura.')],
        tecnica=['Canell solt: l\'arpegi surt sol si no fas força.',
                 'Compta "un-dos-tres" amb l\'esquerra abans d\'afegir la dreta.',
                 'Estudia per sistemes: hi ha molts compassos semblants.']),
    bloques=[
        B(1, 'cc. 1-8', 'Entrada en mp', (0, 0),
          D('cadena', 'Com comença', [('c. 1 silenci', False), ('c. 2 mp', False),
                                       ('c. 5 semicorxeres', True)]),
          [('IZQUIERDA', 'Nota greu llarga i dos acords curts per compàs. Compta 1-2-3.'),
           ('DERECHA', 'Notes llargues lligades. Al c. 5, becaire i semicorxeres lligades.'),
           ('JUNTAS', 'Compteu el compàs de silenci i entreu alhora, en mp.'),
           ('OJO', 'Becaires als acords de l\'esquerra (cc. 4-5).')]),
        B(2, 'cc. 9-24', 'mf i f', (1, 2),
          D('cadena', 'Els matisos', [('c. 11 mf', False), ('c. 19 f', True)]),
          [('IZQUIERDA', 'Mateixa figura. La nota greu puja a Fa als cc. 11-12 i 19-20.'),
           ('DERECHA', 'Frases de dos compassos amb lligadura: respira entre l\'una i l\'altra.'),
           ('JUNTAS', 'Un sistema cada dia, i després els dos seguits.'),
           ('OJO', 'El so creix: mf al c. 11 i f al c. 19.')]),
        B(3, 'cc. 25-32', 'Doble barra i mp', (3, 3),
          D('cadena', 'Canvia la textura', [('c. 26 doble barra', False), ('c. 27 mp', False),
                                            ('dues notes alhora', True)]),
          [('IZQUIERDA', 'Segueix el vals: nota greu llarga i dos acords.'),
           ('DERECHA', 'Des del c. 27 toca dues notes alhora; vigila els becaires.'),
           ('JUNTAS', 'Quatre compassos cada cop, en mp.'),
           ('OJO', 'La doble barra entre els cc. 26 i 27 marca una altra part.')]),
        B(4, 'cc. 33-48', 'Altra vegada mf i f', (4, 5),
          D('cadena', 'Els matisos', [('c. 35 mf', False), ('c. 43 f', True)]),
          [('IZQUIERDA', 'És la mateixa que als cc. 9-24: aprèn-ne una i tindràs l\'altra.'),
           ('DERECHA', 'Dues notes alhora, lligades; reguladors llargs als cc. 43-48.'),
           ('JUNTAS', 'Compareu amb els cc. 9-24: canvia la dreta.'),
           ('OJO', 'mf al c. 35 i f al c. 43.')]),
        B(5, 'cc. 49-69', 'Arriben els arpegis', (6, 8),
          D('capas', 'Dues capes alhora',
            [('Dreta: notes llargues', 'barras', AZUL),
             ('Esquerra: arpegi', 'puntos', OCRE, 6)]),
          [('IZQUIERDA', 'Des del c. 51, sis corxeres lligades per compàs. Un compàs, deu '
                         'cops.'),
           ('DERECHA', 'Notes llargues lligades sobre l\'arpegi: compta-les senceres.'),
           ('JUNTAS', 'Primer l\'arpegi sol; afegeix la melodia de dos en dos compassos.'),
           ('OJO', 'mp al c. 49, p al c. 51 i mf al c. 67.')]),
        B(6, 'cc. 70-88', 'Corxeres a les dues mans', (9, 11),
          D('capas', 'Dues capes alhora',
            [('Dreta: corxeres', 'puntos', AZUL, 6), ('Esquerra: arpegi', 'puntos', OCRE, 6)]),
          [('IZQUIERDA', 'L\'arpegi continua; canvia d\'acord cada un o dos compassos.'),
           ('DERECHA', 'Des del c. 75, sis corxeres lligades per compàs: de dues en dues, sense pressa.'),
           ('JUNTAS', 'Un sistema cada dia: no frenis en canviar de compàs.'),
           ('OJO', 'Doble barra després del c. 74 (p) i mf al c. 83.')]),
        B(7, 'cc. 89-99', 'f, rit. i calderó', (12, 13),
          D('cadena', 'El final', [('c. 91 f', False), ('c. 96 rit.', False),
                                   ('c. 99 p + calderó', True)]),
          [('IZQUIERDA', 'Arpegi fins al c. 96; als cc. 97-99, notes llargues lligades.'),
           ('DERECHA', 'Corxeres fins al c. 96; després notes llargues i un acord amb calderó.'),
           ('JUNTAS', 'Els quatre últims compassos, en bucle.'),
           ('A TEMPO', 'rit.: frena a poc a poc. Allarga l\'últim acord en p.')]),
    ],
    cortes={2: [278.8, 411.0, 543.0], 3: [184.5, 317.5, 450.0, 582.2],
            4: [177.2, 310.2, 442.5, 576.2]},
    inicio={1: 700, 2: 152.2, 4: 38},
    burb={
        0: [('arriba', 200, 'AMB', 'Rubato, negra = 120, en 3/4. El c. 1 és un compàs de '
                                   'silenci: compta\'l.', 120),
            ('arriba', 230, 'DER', 'c. 5: becaire i semicorxeres lligades, la figura més ràpida '
                                   'de la peça.', 421),
            ('abajo', 330, 'IZQ', 'Nota greu llarga a l\'1 i dos acords curts al 2 i al 3. '
                                  'Els acords, suaus.', 277)],
        1: [('arriba', 330, 'AMB', 'mf al c. 11 (i f al c. 19). Els reguladors < > fan '
                                   'pujar i baixar el so.', 213)],
        3: [('arriba', 250, 'OJO', 'Doble barra entre els cc. 26 i 27: una altra part, en mp.', 209),
            ('arriba', 300, 'DER', 'Des del c. 27 la dreta toca dues notes alhora: el mateix '
                                   'pes a les dues.', 332)],
        5: [('arriba', 330, 'AMB', 'f al c. 43 amb un regulador llarg: no t\'apressis en '
                                   'arribar al final del sistema.', 215)],
        6: [('arriba', 250, 'OJO', 'Doble barra després del c. 50 i p al c. 51: canvia la '
                                   'textura.', 209),
            ('abajo', 330, 'IZQ', 'Des del c. 51: sis corxeres lligades per compàs, en arpegi. '
                                  'Regular i suau.', 266)],
        7: [('arriba', 330, 'IZQ', 'Al c. 59 l\'arpegi canvia de posició i comença en Fa: '
                                   'mira abans on poses la mà.', 330)],
        9: [('arriba', 330, 'OJO', 'Doble barra després del c. 74, amb p: des del c. 75 la dreta '
                                   'toca corxeres.', 439)],
        10: [('arriba', 330, 'DER', 'Sis corxeres lligades per compàs, com l\'esquerra. '
                                    'De dues en dues i sense pressa.', 200)],
        12: [('arriba', 330, 'AMB', 'Regulador als cc. 89-90 i f al c. 91: el punt més '
                                    'fort del final.', 227)],
        13: [('arriba', 330, 'AMB', 'rit. al c. 96: frena a poc a poc. Al c. 99, p i '
                                    'calderó.', 90),
             ('abajo', 330, 'AMB', 'L\'últim acord s\'allarga: deixa\'l anar junts, amb calma.',
              532)],
    },
    marcas=[(2, 421, 186, 28, 22, 1, 1, 'ovalo'), (2, 210, 609, 14, 100, 3, 1, 'caja'),
            (3, 209, 383, 14, 95, 5, 1, 'caja'), (4, 439, 122, 14, 85, 6, 1, 'caja'),
            (4, 95, 658, 36, 11, 7, 1, 'caja'), (4, 532, 645, 80, 85, 7, 2, 'caja')],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Do menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_la_dispute.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
