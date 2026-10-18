# -*- coding: utf-8 -*-
"""Pieza 5 · Gymnopedie n.º 1 (Satie). MEDIDO a zoom (150 dpi) sobre el PDF (imagen escaneada de 3
   paginas, 64 ppi, 15 sistemas con el numero de compas impreso al inicio: 1,6,11,16,21,26,31,36,
   41,46,52,57,63,68,74): 12 sistemas de 5 compases y 3 de 6 (46, 57 y 68) = 78 compases.
   3/4, dos sostenidos (Re mayor), "Lent et douloureux". Todo son negras, blancas con puntillo y
   compases enteros de silencio: no hay figuras mas rapidas que la negra. Derecha en silencio en los
   cc. 1-4 y 40-43 (entra en el 2.º tiempo de los cc. 5, 13, 44 y 52). Matices: pp cc. 1, 5, 13, 40,
   44 y 52; f cc. 9 y 48; p cc. 22 y 61. Nota larga ligada: cc. 9-12, 19-21, 29-31, 48-51, 58-60.
   Becuadros en la melodia: cc. 27, 28, 38, 61, 63, 66, 67, 72, 73.
   La copia escaneada trae una franja gris a un lado: se blanquea en una copia limpia
   (students/eva_sc/source_limpia/, que no se versiona)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403


def _limpiar():
    """Copia de la partitura escaneada sin la franja gris lateral (no se toca el original)."""
    import io
    import numpy as np
    import pymupdf
    from PIL import Image
    src = os.path.join(SRCDIR, 'gymnopedie_e_satie.pdf')
    dst_dir = os.path.join(SRCDIR, '..', 'source_limpia')
    dst = os.path.abspath(os.path.join(dst_dir, 'gymnopedie_limpia.pdf'))
    if os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(src):
        return dst
    os.makedirs(dst_dir, exist_ok=True)
    d = pymupdf.open(src)
    out = pymupdf.open()
    for pg in d:
        xref = pg.get_images(full=True)[0][0]
        rect = pg.get_image_rects(xref)[0]
        pix = pymupdf.Pixmap(d, xref)
        if pix.n > 3:
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        arr = np.frombuffer(pix.samples, np.uint8).reshape(pix.h, pix.w, pix.n)[:, :, :3].copy()
        g = arr.mean(2)
        panel = (g > 222) & (g < 250)
        cols = panel.mean(0) > 0.30
        arr[panel & cols[None, :]] = 255
        buf = io.BytesIO()
        Image.fromarray(arr).save(buf, 'PNG')
        npg = out.new_page(width=pg.rect.width, height=pg.rect.height)
        npg.insert_image(rect, stream=buf.getvalue())
    out.save(dst)
    return dst


SPEC = dict(
    num=5, slug='gymnopedie', pdf=_limpiar(), time_sig=(3, 4),
    titulo='Gymnopédie n.º 1', autor='Erik Satie · de les Trois Gymnopédies',
    kicker='Eva · peça 5 · Gymnopédie n.º 1', mes='Gener · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=satie+gymnopedie+no+1+piano',
    credito='Partitura: Erik Satie, Gymnopédie n.º 1 (còpia escanejada). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Re major'), ('Compàs', '3/4'), ('Tempo', 'Lent et douloureux'),
               ('Figura curta', 'Negra'), ('Compassos', '78')],
        total=78,
        secciones=[('A', 1, 12, 'Entrada i 1.a frase', AZUL), ('B', 13, 39, 'La melodia segueix', OCRE),
                   ('C', 40, 51, 'Silenci i tornada', AZUL), ('D', 52, 78, 'Última melodia · final', OCRE)],
        ideas=[('IZQUIERDA', 'Baix i acord',
                'Quasi cada compàs: nota greu al temps 1 i acord al 2. És el balanceig de tota la '
                'peça.'),
               ('DERECHA', 'Notes lentes',
                'Només negres i notes llargues, amb lligadures llargues. No hi ha cap nota més '
                'ràpida.'),
               ('EL SILENCI', 'La dreta calla',
                'Als cc. 1-4 i 40-43 només toca l\'esquerra. Cal comptar aquests compassos.'),
               ('ELS MATISOS', 'pp, p i f',
                'Quasi tot és pp. Hi ha f als cc. 9 i 48, i p als cc. 22 i 61.')],
        especial=[
            'Hi diu "Lent et douloureux" (en francès: lent i dolorós).',
            'Dos sostinguts al principi: Re major (fa♯ i do♯). Compàs de 3/4.',
            'La dreta comença en silenci i entra al c. 5, al segon temps.',
            'Hi ha becaires a la melodia (cc. 27, 28, 61, 63, 66 i 67, entre d\'altres).',
            'Una mateixa nota llarga va lligada de compàs en compàs (cc. 9-12 i 48-51).',
            'Acaba al c. 78 amb dos acords llargs i la barra final.'],
        reto='Tocar molt lent i molt suau sense afanyar-te: que l\'acord caigui sempre al '
             'segon temps i que la melodia canti per sobre.',
        truco='Compta 1-2-3 en veu baixa. Primer l\'esquerra sola, mirant la partitura; després '
              'afegeix només la primera nota llarga de cada frase de la dreta.',
        sabias='Satie va compondre les tres Gymnopédies el 1888. El nom ve de les Gymnopèdies, festes de l\'antiga Esparta amb danses i cants. Aquesta és la primera i la més coneguda.',
        qr_texto='Escolta-la seguint la partitura amb el dit: compta els tres temps.',
        ts=(3, 4),
        cuenta_pie='Un compàs de 3/4 en negres: tres temps iguals, lents. Aquí només el ritme; '
                   'les notes, a la teva partitura.',
        ritmos=[('EL COMPTE', '3/4 · tres negres',
                 [{'pitch': 'B4', 'dur': 'q'} for _ in range(3)], OCRE, 'treble', None)]),
    manos=dict(
        izq=[('Baix i acord', 'Cada compàs: nota greu al temps 1 i acord al 2. Toca només un '
                              'compàs, a poc a poc, fins que surti sense mirar les mans.'),
             ('Compta 1-2-3', 'Compta en veu baixa i sense pressa: el baix cau a l\'1 i l\'acord '
                              'al 2. Tot molt suau (pp).'),
             ('Canvia la nota greu', 'El baix alterna entre notes greus diferents. Abans de '
                                     'cada compàs, mira quina toca.'),
             ('Quan canvia el dibuix', 'Als cc. 37-39 i 76-78 l\'esquerra és diferent '
                                       '(negres o acords llargs). Mira-ho abans de tocar.')],
        der=[('Cantar abans de tocar', 'La melodia va en negres i notes llargues amb lligadures '
                                       'llargues. Canta-la per dins i respira on acaba cada '
                                       'lligadura.'),
             ('Entrar a temps', 'Al c. 5 hi ha un silenci de negra i entres al segon '
                                'temps. Abans, compta els quatre compassos de silenci.'),
             ('Notes llargues lligades', 'Als cc. 48-51 la mateixa nota va lligada de compàs en '
                                         'compàs: prem una vegada i compta fins al final.'),
             ('Els becaires', 'Als cc. 27 i 28 hi ha becaires. Digues el nom de cada nota '
                              'abans de tocar-la.')],
        tecnica=['Braç i canell solts: el so es deixa caure, no es colpeja.',
                 'Acord de l\'esquerra més suau que la melodia.',
                 'Tempo molt lent: compta 1-2-3 sense accelerar.']),
    bloques=[
        B(1, 'cc. 1-5', 'L\'entrada', (0, 0),
          D('cuenta', 'Un compàs de 3/4: tres temps', [('un compàs', 1, 3)]),
          [('IZQUIERDA', 'Baix al temps 1 i acord al 2, en pp. Quatre compassos iguals: toca\'ls '
                         'fins que surtin sols.'),
           ('DERECHA', 'Silenci de negra i entres al 2.º temps del c. 5 amb dues negres, en '
                       'pp.'),
           ('JUNTAS', 'L\'esquerra toca sola quatre compassos i la dreta entra al c. 5, sense '
                      'dubtar.'),
           ('A TEMPO', 'Lent et douloureux (lent i dolorós): tres negres iguals i molt lentes.')]),
        B(2, 'cc. 6-15', 'La primera frase', (1, 2),
          D('grupos', 'La nota lligada dels cc. 9-12: 4 compassos, 12 temps',
            (4, 3, ['c. 9', 'c. 10', 'c. 11', 'c. 12'])),
          [('IZQUIERDA', 'Igual que abans. Al c. 9 hi ha f: baix i acord una mica més forts, sense '
                         'colpejar.'),
           ('DERECHA', 'Cc. 6-8: tres negres per compàs sota una lligadura llarga. Cc. 9-12: una '
                       'sola nota llarga lligada.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 6-10 i cc. 11-15.'),
           ('OJO', 'Al c. 13 torna el pp i entres un altre cop al segon temps.')]),
        B(3, 'cc. 16-25', 'La melodia segueix', (3, 4),
          D('capas', 'Dues capes alhora',
            [('Dreta: melodia', 'barras', AZUL), ('Esquerra: baix i acord', 'puntos', OCRE)]),
          [('IZQUIERDA', 'El mateix dibuix a tots els compassos: aprèn-lo de memòria.'),
           ('DERECHA', 'Notes llargues als cc. 16-21 (lligades del 19 al 21) i tres negres per '
                       'compàs als cc. 22-24.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 16-20 i cc. 21-25.'),
           ('OJO', 'Al c. 22 hi ha p: una mica més fort que el pp d\'abans.')]),
        B(4, 'cc. 26-35', 'Els becaires', (5, 6),
          D('fichas', 'El que cal vigilar',
            ['becaires als cc. 27-28', 'notes llargues als cc. 32-33']),
          [('IZQUIERDA', 'Als cc. 27 i 28 l\'acord duu un becaire: mira-ho abans de '
                         'tocar.'),
           ('DERECHA', 'Becaires a la melodia dels cc. 27 i 28. Cc. 32-33: una nota llarga '
                       'per compàs.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 26-30 i cc. 31-35.'),
           ('OJO', 'Un becaire val només fins al final del seu compàs.')]),
        B(5, 'cc. 36-45', 'El silenci de la dreta', (7, 8),
          D('cadena', 'El que passa en aquest bloc',
            [('cc. 38-39: acords', False), ('c. 40: pp, la dreta calla', False),
             ('c. 44: entra', True)]),
          [('IZQUIERDA', 'Al c. 37 hi ha dues negres i als cc. 38-39 un acord llarg: mira-ho '
                         'abans de tocar.'),
           ('DERECHA', 'Als cc. 38-39 toca acords llargs i al c. 40 calla. Entra al '
                       'c. 44.'),
           ('JUNTAS', 'Compta els quatre compassos de silenci (cc. 40-43) mentre l\'esquerra '
                      'segueix.'),
           ('OJO', 'Al c. 44 entres al segon temps i en pp, com al c. 5.')]),
        B(6, 'cc. 46-56', 'De la f al pp', (9, 10),
          D('cadena', 'Cap al final de la frase',
            [('c. 48: f', False), ('lligades cc. 48-51', False), ('c. 52: pp', True)]),
          [('IZQUIERDA', 'Baix i acord com sempre, també durant les notes lligades.'),
           ('DERECHA', 'Del c. 48 al c. 51 la mateixa nota llarga va lligada: prem només la '
                       'primera vegada.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 46-51 i cc. 52-56.'),
           ('OJO', 'Al c. 52 torna el pp i l\'entrada dels cc. 5 i 44.')]),
        B(7, 'cc. 57-67', 'Lligadures i becaires', (11, 12),
          D('grupos', 'La nota lligada dels cc. 58-60: 3 compassos, 9 temps',
            (3, 3, ['c. 58', 'c. 59', 'c. 60'])),
          [('IZQUIERDA', 'El mateix balanceig. Alguns acords duen becaires, com el del c. 61.'),
           ('DERECHA', 'Cc. 58-60: nota lligada. Al c. 61 hi ha p; becaires als cc. 61, 63, '
                       '66 i 67.'),
           ('JUNTAS', 'Dos dies: cc. 57-62 i cc. 63-67.'),
           ('OJO', 'Els reguladors < > demanen pujar i baixar el so molt a poc a poc.')]),
        B(8, 'cc. 68-78', 'El final', (13, 14),
          D('cadena', 'Cap al final',
            [('cc. 68-73: melodia', False), ('cc. 74-76: negres', False),
             ('cc. 77-78: acords', True)]),
          [('IZQUIERDA', 'Al c. 76 hi ha dues negres i als cc. 77-78 acords llargs.'),
           ('DERECHA', 'Becaires als cc. 72 i 73. Als cc. 77 i 78 toca acords llargs.'),
           ('JUNTAS', 'Els dos últims sistemes, en bucle.'),
           ('A TEMPO', 'Deixa sonar l\'últim acord i compta els tres temps sencers.')]),
    ],
    cortes={1: [256.0, 387.5, 511.2, 638.0], 2: [233.0, 359.8, 489.0, 606.0],
            3: [230.0, 362.0, 489.5, 625.8]},
    corte_titulo=149.2, inicio={1: 85.0}, fin={2: 731.2, 3: 762.8},
    burb={
        0: [('arriba', 250, 'OJO', 'Lent et douloureux: lent i dolorós. Tres negres per compàs, '
                                   'molt suaus (pp).', 150),
            ('arriba', 250, 'DER', 'Silenci de negra i entres al segon temps del c. 5.', 485),
            ('abajo', 330, 'IZQ', 'Baix al temps 1 i acord al 2. Els quatre primers compassos '
                                  'són per a l\'esquerra sola.', 142)],
        1: [('arriba', 270, 'DER', 'Una sola lligadura llarga cobreix els cc. 6-8: toca\'ls com una '
                                   'frase i respira al final.', 200),
            ('arriba', 270, 'AMB', 'f al c. 9. Des d\'aquí la mateixa nota va lligada fins al c. '
                                   '12.', 398)],
        2: [('arriba', 330, 'AMB', 'cc. 11-12: segueix la nota lligada (no la premis un altre cop). '
                                   'Al c. 13, pp i entra al 2.º temps.', 120)],
        4: [('arriba', 300, 'AMB', 'p al c. 22: una mica més fort que el pp. Tres negres per '
                                   'compàs, regulars.', 185)],
        5: [('arriba', 330, 'OJO', 'Becaires als cc. 27 i 28, a la melodia i a l\'acord '
                                   'de l\'esquerra.', 226)],
        7: [('arriba', 270, 'IZQ', 'Des del c. 37 l\'esquerra canvia: dues negres i després '
                                   'acords llargs.', 240),
            ('arriba', 270, 'AMB', 'c. 40: pp i la dreta calla. Compta fins al c. 44.', 487)],
        9: [('arriba', 300, 'AMB', 'f al c. 48. La mateixa nota llarga va lligada fins al c. 51.',
             282)],
        11: [('arriba', 380, 'DER', 'Lligades als cc. 58-60 i p al c. 61, amb un becaire a '
                                    'la melodia.', 372)],
        14: [('arriba', 470, 'AMB', 'Final: dos acords llargs. Deixa que sonin i compta els '
                                    'tres temps.', 480)],
    },
    marcas=[(1, 485, 180, 70, 30, 1, 1, 'caja'), (1, 399.5, 327.5, 17, 17, 2, 1, 'caja'),
            (1, 284, 443, 22, 16, 2, 2, 'caja'), (2, 282.5, 671, 19, 18, 6, 1, 'caja'),
            (3, 374, 291, 16, 18, 7, 1, 'caja')],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Re major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_gymnopedie.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
