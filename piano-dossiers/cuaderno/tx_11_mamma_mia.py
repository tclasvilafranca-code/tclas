# -*- coding: utf-8 -*-
"""Pieza 10 · Mamma Mia (ABBA), arranjament d'Unai Karam. MEDIDO sobre el PDF (3 paginas A4
   apaisadas, vectorial; 44 compases en 11 sistemas de 4; barra final doble): sin armadura (Do
   mayor, empieza en Sol-La-Do-Mi y acaba en un acorde de Do), 4/4, «blanca = 68», sin matices,
   sin repeticiones, semicorchea como figura mas corta (solo el par del c. 21), sin digitacion.
   Cc. 1-4: ostinato de corcheas Do-Sol en las dos manos, con Sol sostenido y becuadros. Desde
   el c. 5 la izquierda toca un acorde de tres notas por compas (en los cc. 24, 26, 31, 35 y
   41-43 cambia dentro del compas) y la derecha una melodia con silencios y notas ligadas. Los
   cc. 13-16 repiten los cc. 9-12 y los cc. 33-36 los cc. 29-32; bemol en los cc. 31, 35 y 41.
   La pagina se recorta (vectorial) en los margenes para poder escalarla a una pagina vertical."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403


def _preparar(origen, destino, x0=40.0, x1=802.0):
    """Retalla els marges laterals de cada pagina apaisada (vectorial) perque el motor pugui
       escalar la partitura a l'amplada d'una pagina vertical sense empetitir-la de mes."""
    import pymupdf
    if os.path.exists(destino) or not os.path.exists(origen):
        return
    src = pymupdf.open(origen)
    out = pymupdf.open()
    h = 595.2756
    for i in range(len(src)):
        pg = out.new_page(width=x1 - x0, height=h)
        pg.show_pdf_page(pymupdf.Rect(0, 0, x1 - x0, h), src, i, clip=pymupdf.Rect(x0, 0, x1, h))
    out.save(destino)


_preparar(os.path.join(SRCDIR, 'mama_mia.pdf'), os.path.join(SRCDIR, 'mama_mia_recto.pdf'))

SPEC = dict(
    num=11, slug='mamma_mia', pdf='mama_mia_recto.pdf', time_sig=(4, 4),
    titulo='Mamma Mia',
    autor='ABBA · arranjament d\'Unai Karam',
    kicker='Txell · peça 11 · Mamma Mia', mes='Maig · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=abba+mamma+mia+piano+easy+tutorial',
    credito='Partitura: «Mamma Mia» (ABBA), arranjament d\'Unai Karam. Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '4/4'), ('Tempo', 'Blanca = 68'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '44')],
        total=44,
        secciones=[('A', 1, 4, 'El motor', AZUL), ('B', 5, 16, 'Entra la melodia', OCRE),
                   ('C', 17, 28, 'Silencis i frases', AZUL), ('D', 29, 44, 'El final', OCRE)],
        ideas=[('ESQUERRA', 'Corxeres, després acords',
                'Als cc. 1-4, corxeres Do-Sol. Des del c. 5, un acord de tres notes per compàs.'),
               ('DRETA', 'Melodia amb silencis',
                'Frases curtes, silencis i notes lligades. Cal comptar-los bé.'),
               ('ELS CANVIS', 'Sostinguts i becaires',
                'Sol♯ i becaires als cc. 1-8 i 17-20. Un bemoll als cc. 31, 35 i 41.'),
               ('EL RITME', 'Semicorxeres',
                'Només al c. 21: dues notes molt ràpides, juntes en un sol temps.')],
        ideas_pie='Els cc. 13-16 repeteixen els cc. 9-12, i els cc. 33-36, els cc. 29-32: '
                  'menys feina de la que sembla!',
        especial=[
            'Sense armadura: Do major. Comença amb Sol-La-Do-Mi i acaba en un acord de Do.',
            'Porta «blanca = 68»: dues negres per cada pulsació. No hi ha matisos escrits.',
            'Els cc. 1-4 són un motor de corxeres Do-Sol a les dues mans.',
            'Des del c. 5 l\'esquerra toca un acord per compàs, aguantat.',
            'La dreta té molts silencis i notes lligades que s\'han d\'aguantar.',
            'Al c. 44 la dreta calla i l\'esquerra tanca amb un acord de Do.'],
        reto="Que els cc. 1-4 sonin com una màquina: corxeres iguals, sense córrer, mans "
             'juntes. Quant temps aguantes?',
        truco="Canta «mamma mia» sobre les notes de la dreta. Els silencis són el moment de "
              'respirar!',
        sabias='«Mamma Mia» és d\'ABBA i va sortir el 1975. El 1999 va donar nom al musical '
               '«Mamma Mia!», estrenat a Londres.',
        qr_texto='Escolta-la: sents el motor de corxeres a l\'inici?', ts=(4, 4)),
    manos=dict(
        izq=[('El motor', 'Els cc. 1-4: corxeres Do-Sol-Do-Sol... Toca-les a poc a poc i iguals, '
                          'sense accelerar.'),
             ('Sol♯ i becaire', 'Al final dels cc. 1-4 canvia el Sol: mira on hi ha un sostingut '
                                '(♯) i on un becaire (♮).'),
             ('Un acord per compàs', 'Des del c. 5, tres notes juntes. Toca-les a la vegada i '
                                     'aguanta quatre temps.'),
             ('Acords que canvien', 'Als cc. 24 i 26, l\'acord canvia dins el compàs: mira que '
                                    'no et passi per alt.')],
        der=[('El motor, també', 'Els cc. 1-4 són el mateix dibuix que l\'esquerra, una octava '
                                 'més amunt.'),
             ('La primera frase', 'Cc. 5-6: Sol-La-Do-Mi lligat. Canta-la abans de tocar-la.'),
             ('Els silencis', 'Compta els silencis com si toquessis: 1-2-3-4, no et precipitis.'),
             ('Les dues ràpides', 'Al c. 21 hi ha dues notes molt ràpides (semicorxeres): fes-les '
                                  'a poc a poc primer.')],
        tecnica=['Canell solt: el motor sona lleuger, sense picar.',
                 'La dreta canta i l\'esquerra acompanya, més fluix.',
                 'Compta «1-i-2-i-3-i-4-i» en veu alta als cc. 1-4.']),
    bloques=[
        B(1, 'cc. 1-4', 'El motor', (0, 0),
          D('cadena', 'Corxeres Do-Sol',
            [('Do', False), ('Sol', False), ('Do', False), ('Sol♯ / Sol', True)]),
          [('IZQUIERDA', 'Corxeres Do-Sol, vuit a cada compàs, igual que la dreta.'),
           ('DERECHA', 'El mateix dibuix, una octava més amunt: Do-Sol-Do-Sol...'),
           ('JUNTAS', 'Compta «1-i-2-i-3-i-4-i» i toca un compàs cada vegada.'),
           ('OJO', 'El Sol canvia a ♯ o ♮ prop del final de cada compàs. Mira-ho!')]),
        B(2, 'cc. 5-8', 'Entra la melodia', (1, 1),
          D('cadena', 'De corxeres a melodia',
            [('motor (cc. 1-4)', False), ('un acord per compàs', False),
             ('melodia lligada', True)]),
          [('IZQUIERDA', 'Un acord de tres notes per compàs. Aguanta quatre temps.'),
           ('DERECHA', 'Sol-La-Do-Mi lligat a una blanca. Després, notes soltes.'),
           ('JUNTAS', 'Compàs a compàs: acord i melodia a la vegada.'),
           ('OJO', 'Sol♯ i becaire a l\'acord (cc. 6, 7 i 8): mira els signes.')]),
        B(3, 'cc. 9-16', 'La frase que torna', (2, 3),
          D('cadena', 'Una frase, dues vegades',
            [('cc. 9-12', False), ('torna igual', True), ('cc. 13-16', False)]),
          [('IZQUIERDA', 'Un acord per compàs. Els cc. 13-16 repeteixen els 9-12.'),
           ('DERECHA', 'Corxeres per graus, una nota llarga lligada, i un silenci de negra.'),
           ('JUNTAS', 'Si saps els cc. 9-12, ja saps els cc. 13-16.'),
           ('OJO', 'Entre el c. 12 i el 13 canvia de pàgina.')]),
        B(4, 'cc. 17-20', 'Torna una idea', (4, 4),
          D('cadena', 'Com als cc. 5-8',
            [('Sol-La-Do-Mi', False), ('lligat', False), ('silenci i frase', True)]),
          [('IZQUIERDA', 'Acords de compàs sencer. Sol♯ al c. 18 i al c. 20, becaire al 19.'),
           ('DERECHA', 'Torna Sol-La-Do-Mi lligat; ara la resposta és diferent.'),
           ('JUNTAS', 'Compara amb els cc. 5-8: què és igual i què canvia?'),
           ('OJO', 'Cada compàs parell comença amb un silenci de negra.')]),
        B(5, 'cc. 21-28', 'Silencis i dues ràpides', (5, 6),
          D('cadena', 'Compta tots els silencis',
            [('semicorxeres c. 21', False), ('silenci de blanca c. 23', False),
             ('cc. 24-28', True)]),
          [('IZQUIERDA', 'Acords de compàs sencer; als cc. 24 i 26 canvien dins el compàs.'),
           ('DERECHA', 'Al c. 21, dues semicorxeres. Al c. 23, un silenci de blanca.'),
           ('JUNTAS', 'Primer els cc. 21-24, després els cc. 25-28.'),
           ('OJO', 'No et precipitis als silencis: compta-los tots.')]),
        B(6, 'cc. 29-36', 'Un dibuix que es repeteix', (7, 8),
          D('cadena', 'Quatre compassos, dos cops',
            [('cc. 29-32', False), ('torna igual', True), ('cc. 33-36', False)]),
          [('IZQUIERDA', 'Acords de tres notes; als cc. 31 i 35 canvien dins el compàs.'),
           ('DERECHA', 'Silenci i corxeres per graus. Al final, una nota llarga lligada.'),
           ('JUNTAS', 'Aprèn els cc. 29-32: els cc. 33-36 són els mateixos.'),
           ('OJO', 'Un bemoll als cc. 31 i 35 a l\'acord de l\'esquerra.')]),
        B(7, 'cc. 37-40', 'Notes lligades', (9, 9),
          D('cadena', 'Aguanta i respira',
            [('nota lligada', False), ('corxera', False), ('silenci de corxera', True)]),
          [('IZQUIERDA', 'Acords que van baixant, compàs a compàs.'),
           ('DERECHA', 'Notes lligades: toca la primera i aguanta, no repeteixis.'),
           ('JUNTAS', 'Compta amb calma: la dreta té silencis de corxera.'),
           ('OJO', 'Cada frase acaba amb un silenci de corxera: no et passis!')]),
        B(8, 'cc. 41-44', 'El final', (10, 10),
          D('cadena', 'Cap al final',
            [('acords de negra', False), ('acord lligat', False), ('acord de Do: FINAL', True)]),
          [('IZQUIERDA', 'Acords de negra amb un bemoll al c. 41, després un acord lligat.'),
           ('DERECHA', 'Corxeres per graus i un silenci. Al c. 44, silenci de compàs sencer.'),
           ('JUNTAS', 'Els quatre compassos en bucle, comptant tots els silencis.'),
           ('A TEMPO', 'La peça sencera, a blanca = 68. Aguanta l\'últim acord de Do.')]),
    ],
    cortes={1: [286.2, 401.2], 2: [158.8, 276.0, 396.8], 3: [160.5, 275.8, 389.8]},
    corte_titulo=136.2, fin={2: 539.2, 3: 534.8},
    burb={
        0: [('arriba', 280, 'AMB', 'El motor: corxeres Do-Sol a les dues mans. Compta '
                                   '«1-i-2-i-3-i-4-i».', 0.1),
            ('abajo', 300, 'OJO', 'Sol♯ i becaire prop del final de cada compàs. Mira els '
                                  'signes!', 0.75)],
        1: [('arriba', 300, 'DER', 'Sol-La-Do-Mi lligat a una blanca. Canta-la abans de '
                                   'tocar-la.', 0.15),
            ('abajo', 300, 'IZQ', 'Un acord de tres notes per compàs: aguanta quatre temps.',
             0.6)],
        2: [('arriba', 300, 'AMB', 'Una frase de quatre compassos. Els cc. 13-16 la repeteixen.',
             0.15),
            ('abajo', 300, 'OJO', 'La dreta té silencis: compta-los com si toquessis.', 0.6)],
        3: [('arriba', 300, 'DER', 'Mateixa frase que els cc. 9-12: ja la tens!', 0.15),
            ('abajo', 300, 'IZQ', 'Acords de compàs sencer, sense pressa.', 0.6)],
        4: [('arriba', 300, 'AMB', 'Torna Sol-La-Do-Mi lligat, però la resposta és '
                                   'diferent.', 0.2),
            ('abajo', 300, 'OJO', 'Sol♯ als cc. 18 i 20, becaire al 19.', 0.6)],
        5: [('arriba', 300, 'DER', 'Al c. 21, dues semicorxeres. Al c. 23, silenci de blanca: '
                                   'compta 1-2-3-4.', 0.15),
            ('abajo', 300, 'IZQ', "Als cc. 24 i 26 l'acord canvia dins el compàs.", 0.6)],
        6: [('arriba', 300, 'AMB', 'Frase i resposta: dues idees que es contesten.', 0.2)],
        7: [('arriba', 300, 'DER', 'Silenci, corxeres per graus i nota llarga: és la frase '
                                   'que torna.', 0.15),
            ('abajo', 300, 'OJO', 'Un bemoll a l\'acord de l\'esquerra al c. 31.', 0.6)],
        8: [('arriba', 300, 'AMB', 'Els cc. 33-36 repeteixen els cc. 29-32.', 0.15)],
        9: [('arriba', 300, 'DER', 'Notes lligades: toca la primera i aguanta.', 0.15),
            ('abajo', 300, 'IZQ', 'Els acords van baixant a poc a poc.', 0.6)],
        10: [('arriba', 300, 'IZQ', 'Acords de negra i un de lligat. Un bemoll al c. 41.', 0.15),
             ('abajo', 300, 'OJO', "Aguanta l'últim acord de Do... i fes una reverència!",
              0.85)],
    },
    marcas=[],
    misol=dict(manos='Truc: aprèn primer el motor dels cc. 1-4. Només són dues notes, Do i Sol, '
                     'però has de ser constant!',
               guia='Ànim! Els cc. 13-16 i 33-36 ja els saps de la primera vegada: menys feina '
                    'de la que sembla.',
               pauta="Escriu els cc. 1-4 (Do-Sol en corxeres) i inventa'n dos més amb "
                     'altres notes!'),
    pie_pauta="la clau la poses tu · copia el motor Do-Sol o inventa un ritme propi")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_tx_mamma_mia.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
