# -*- coding: utf-8 -*-
"""Pieza 10 · Perfect (Ed Sheeran), arreglo de Elaine Kelkel (Musescore, marzo de 2021). MEDIDO sobre
   el PDF de Drive: 2 paginas A4, 54 compases (el c. 1 es una anacrusa de tres corcheas), una
   armadura de un sostenido (Sol mayor), 6/8, negra con puntillo = 70, sin matices ni repeticiones,
   cifrados impresos G, Em, C, D y D/F#; izquierda en seis corcheas por compas (arpegio de tres
   notas dos veces) hasta el c. 45, acordes de blanca con puntillo en los cc. 46-49 y notas
   sueltas en los cc. 50-53; corchea como figura mas corta."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=10, slug='perfect', pdf='perfect.pdf', time_sig=(6, 8),
    titulo='Perfect', autor='Ed Sheeran · arranjament d\'Elaine Kelkel',
    kicker='Sharifa · peça 10 · Perfect', mes='Maig · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=ed+sheeran+perfect+piano+tutorial',
    credito='Partitura: arranjament d\'Elaine Kelkel (Musescore, 2021). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sol major'), ('Compàs', '6/8'), ('Tempo', '♩. = 70'),
               ('Figura curta', 'Corxera'), ('Compassos', '54')],
        total=54,
        secciones=[('A', 1, 17, 'Primera part', AZUL),
                   ('B', 18, 33, 'Segona part', OCRE),
                   ('C', 34, 45, 'Un acord per compàs', AZUL),
                   ('D', 46, 54, 'Final', OCRE)],
        ideas_titulo='La peça en quatre idees',
        ideas=[('ELS ACORDS', 'Quatre, en bucle',
                'Sol major, Mi menor, Do major i Re major (la partitura els imprimeix com G, Em, '
                'C i D). Gairebé tota la peça gira entre ells.'),
               ('ESQUERRA', 'Un arpegi per compàs',
                'Tres notes de l\'acord, de baix a dalt, dues vegades per compàs: sis corxeres.'),
               ('DRETA', 'Melodia amb puntets',
                'Notes llargues amb puntet i algunes corxeres. Comença abans del compàs '
                '(anacrusa).'),
               ('EL FINAL', 'Canvia l\'esquerra',
                'Als cc. 46-49 l\'esquerra toca acords llargs i als cc. 50-53, notes soltes.')],
        especial=[
            'Posa negra amb puntet = 70: dos pulsos per compàs.',
            'El c. 1 és una anacrusa: tres corxeres que comencen abans del primer compàs.',
            'Cifrats impresos: G = Sol major, Em = Mi menor, C = Do major, D = Re major.',
            'Al c. 50 apareix D/F♯: Re major amb Fa♯ al baix (primera inversió).',
            'No hi ha repeticions ni matisos escrits: tria tu on sona més suau.',
            'Als cc. 46-49 l\'esquerra toca acords de tres notes.'],
        reto='Mantén les sis corxeres de l\'esquerra ben iguals mentre la dreta canta notes '
             'llargues per sobre. Pots amb això?',
        truco='Estudia l\'esquerra en bucle: quatre compassos (Sol, Mi menor, Do, Re). Quan et surti '
              'sola, afegeix la dreta de dos en dos compassos.',
        sabias='«Perfect» (2017) és una balada d\'Ed Sheeran de l\'àlbum «÷» (Divide). Va ser el '
               'número 1 de Nadal del 2017 al Regne Unit i parla de la seva parella, Cherry Seaborn.',
        qr_texto='Escolta-la i compta dos pulsos per compàs amb la partitura al davant.',
        ts=(6, 8), cuenta_titulo='Com es compta el 6/8',
        cuenta_pie='Un compàs de 6/8: dos temps, cadascun amb tres corxeres. Aquí només el ritme, '
                   'sobre una nota qualsevol.', cuenta_rotulo='EL COMPTE'),
    manos=dict(
        izq=[('Tres notes que pugen', 'A cada compàs l\'esquerra toca tres notes de l\'acord, de '
                                      'baix a dalt, i repeteix. Fes només el primer compàs, deu '
                                      'cops.'),
             ('Quatre compassos', 'Sol, Mi menor, Do, Re: quatre dibuixos quasi iguals. Canvia\'ls '
                                  'sense aturar el pols.'),
             ('Igual i suau', 'Les sis corxeres iguals i molt suaus. Compta 1-2-3, 4-5-6.'),
             ('Els acords del final', 'Cc. 46-49: acords de tres notes amb blanca amb puntet. '
                                      'Les tres juntes, sense trencar-les.')],
        der=[('Abans del compàs', 'La peça comença amb tres corxeres d\'anacrusa. Canta-les i '
                                  'entra a l\'última corxera del compàs.'),
             ('Notes amb puntet', 'La melodia va en negres amb puntet i blanques amb puntet. '
                                  'Compta 1-2-3 per cadascuna.'),
             ('Les corxeres', 'Hi ha grups de corxeres entre les notes llargues. Toca-les '
                              'tranquil·les, sense córrer.'),
             ('Amb l\'esquerra', 'Uneix els cc. 2-5 a poc a poc, amb metrònom. Si es trenca, '
                                  'torna a una sola mà.')],
        tecnica=['Canell solt: l\'arpegi de l\'esquerra puja i baixa sense cops.',
                 'Compta dos temps llargs per compàs (1-2-3, 4-5-6), no sis de ràpids.',
                 'Comença a la meitat de la velocitat i puja a poc a poc.']),
    bloques=[
        B(1, 'cc. 1-5', 'Anacrusa i primera frase', (0, 0),
          D('grupos', 'Un compàs de 6/8 = 2 temps · 3 corxeres cadascun',
            (2, 3, ['temps 1', 'temps 2'])),
          [('DERECHA', 'Tres corxeres d\'anacrusa i notes llargues. Canta-les abans de tocar.'),
           ('IZQUIERDA', 'Silenci al c. 1. Des del c. 2 l\'arpegi de Sol i, al c. 4, de Mi menor.'),
           ('JUNTAS', 'Cc. 2-5 en bucle, amb l\'anacrusa d\'entrada.'),
           ('A TEMPO', 'Negra amb puntet = 70. Comença a la meitat.')]),
        B(2, 'cc. 6-9', 'Do i Re', (1, 1),
          D('cadena', 'Els acords del bloc', [('Do major', False), ('Re major', True)]),
          [('DERECHA', 'Corxeres i notes llargues. Compta bé les notes llargues dels cc. 8-9.'),
           ('IZQUIERDA', 'Dos compassos d\'arpegi de Do i dos de Re.'),
           ('JUNTAS', 'De dos en dos compassos, i després els quatre.'),
           ('OJO', 'Al final dels cc. 5, 9 i 13 hi ha corxeres que porten al compàs següent.')]),
        B(3, 'cc. 10-13', 'Torna la primera frase', (2, 2),
          D('cadena', 'El camí', [('Sol', False), ('Mi menor', True)]),
          [('DERECHA', 'Sol major i Mi menor un altre cop. La melodia és nova: llegeix-la abans.'),
           ('IZQUIERDA', 'Quatre compassos d\'arpegis, com als cc. 2-5.'),
           ('JUNTAS', 'Els quatre compassos i l\'última corxera, que porta al següent.'),
           ('OJO', 'Compara amb els cc. 2-5: semblants, però no iguals.')]),
        B(4, 'cc. 14-17', 'Do, Re i amunt', (3, 3),
          D('cadena', 'El camí', [('Do major', False), ('Re major', False),
                                  ('sis corxeres', True)]),
          [('DERECHA', 'Al c. 17 hi ha sis corxeres seguides. Compta-les de tres en tres.'),
           ('IZQUIERDA', 'Arpegis de Do i de Re, igual que al bloc 2.'),
           ('JUNTAS', 'Dos compassos i després quatre, sense parar.'),
           ('A TEMPO', 'Prepara\'t per al canvi de Re a Sol al c. 18.')]),
        B(5, 'cc. 18-25', 'Segona vegada', (4, 5),
          D('cadena', 'Mateix camí', [('Sol', False), ('Mi m.', False), ('Do', False),
                                      ('Re', True)]),
          [('DERECHA', 'La melodia és nova: llegeix amb cura abans de tocar.'),
           ('IZQUIERDA', 'Els mateixos quatre arpegis: Sol, Mi menor, Do, Re.'),
           ('JUNTAS', 'Un sistema cada cop: cc. 18-21 i 22-25.'),
           ('OJO', 'L\'esquerra no canvia: tota l\'atenció és per a la dreta.')]),
        B(6, 'cc. 26-33', 'Tercera vegada', (6, 7),
          D('cadena', 'Mateix camí', [('Sol', False), ('Mi m.', False), ('Do', False),
                                      ('Re', True)]),
          [('DERECHA', 'Mateixos acords; la melodia s\'assembla a la dels cc. 18-25.'),
           ('IZQUIERDA', 'Els mateixos arpegis: ja te\'ls saps de memòria.'),
           ('JUNTAS', 'Els cc. 26-29 i 30-33, un cada dia.'),
           ('A TEMPO', 'Toca els cc. 18-33 seguits.')]),
        B(7, 'cc. 34-45', 'Un acord per compàs', (8, 10),
          D('cadena', 'L\'acord canvia a cada compàs',
            [('Mi menor', False), ('Do', False), ('Sol', False), ('Re', True)]),
          [('DERECHA', 'Notes més agudes, amb notes llargues i corxeres. Els dibuixos canvien.'),
           ('IZQUIERDA', 'Un arpegi diferent per compàs: Mi menor, Do, Sol, Re.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 34-37, 38-41 i 42-45.'),
           ('OJO', 'L\'ordre dels acords es repeteix cada quatre compassos.')]),
        B(8, 'cc. 46-54', 'Final', (11, 12),
          D('cadena', 'Cap al final',
            [('acords llargs', False), ('notes soltes', False), ('Sol', True)]),
          [('DERECHA', 'Notes llargues, cada cop més tranquil·les. L\'últim compàs és Sol.'),
           ('IZQUIERDA', 'Cc. 46-49: acords de tres notes. Cc. 50-53: notes soltes, amb Fa♯ '
                         'al c. 50.'),
           ('JUNTAS', 'Cc. 46-49 i 50-54 per separat, i després junts.'),
           ('OJO', 'L\'acord de l\'últim compàs és de Sol major: deixa\'l sonar.')]),
    ],
    cortes={1: [206.5, 319.5, 437.5, 555.5, 672.5],
            2: [154.2, 256.8, 357.0, 459.8, 574.0, 682.0]},
    corte_titulo=93.0, inicio={1: 30, 2: 52},
    burb={
        0: [('arriba', 330, 'DER', 'Tres corxeres d\'anacrusa: entres abans del compàs, a l\'última '
                                   'corxera. Canta-les.', 0.1),
            ('abajo', 330, 'IZQ', 'Silenci al c. 1. Des del c. 2: tres notes de Sol, dues vegades '
                                  'per compàs.', 0.4)],
        1: [('arriba', 330, 'AMB', 'Do major (C) i Re major (D): l\'esquerra canvia de dibuix '
                                   'cada dos compassos.', 0.3)],
        2: [('arriba', 330, 'OJO', 'Torna la primera frase: Sol major (G) i Mi menor (Em). '
                                   'Ja l\'has sentida, oi?', 0.3)],
        3: [('arriba', 330, 'AMB', 'Compta 1-2-3, 4-5-6. Al c. 17 hi ha sis corxeres seguides: '
                                   'compta-les de tres en tres.', 0.5)],
        4: [('arriba', 330, 'AMB', 'Segona vegada: l\'esquerra repeteix Sol, Mi menor, Do i Re.',
             0.2)],
        7: [('arriba', 330, 'OJO', 'Tercera vegada! Compara amb els cc. 18-25: el que canvia és '
                                   'la dreta.', 0.3)],
        8: [('arriba', 330, 'AMB', 'Ara l\'acord canvia a cada compàs: Mi menor, Do, Sol, Re.',
             0.2)],
        11: [('arriba', 330, 'IZQ', 'Cc. 46-49: l\'esquerra toca acords de tres notes, de blanca '
                                    'amb puntet.', 0.2)],
        12: [('arriba', 330, 'IZQ', 'Cc. 50-53: notes soltes. Al c. 50, D/F♯ = Re major amb '
                                    'Fa♯ al baix.', 0.1),
             ('abajo', 330, 'OJO', 'Últim compàs: acord de Sol major. Deixa\'l sonar i somriu!',
              0.9)],
    },
    marcas=[],
    misol=dict(
        manos='Toca l\'esquerra en bucle: Sol, Mi menor, Do, Re. Quan et surti sola, la dreta '
              'serà un joc.',
        guia='Compta dos temps llargs, 1-2-3 i 4-5-6, no sis de ràpids. El 6/8 és com un gronxador.',
        pauta='Escriu un compàs de 6/8 amb sis corxeres, tres amunt i tres avall, com a Perfect.'),
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Sol major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_perfect.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
