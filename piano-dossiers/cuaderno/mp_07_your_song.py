# -*- coding: utf-8 -*-
"""Pieza 7 · Your Song (Elton John), edicion de musicaparadisfrutar.com. MEDIDO sobre el PDF
   (2 paginas carta, 9 sistemas, 29 compases): tres bemoles (Mi bemol mayor), 4/4 con compases
   sueltos de 2/4 (cc. 11, 13, 22 y 27), negra = 66 impresa, sin matices, semicorchea la figura
   mas corta (con tresillos en los cc. 8, 9, 15 y 17), cifrado americano encima, signo de segno
   y barra de repeticion en el c. 3, casillas 1 (cc. 10-11) y 2 (c. 12), "D.S. al Coda" tras el
   c. 22, Coda (signo) en el c. 23 con repeticion y casillas 1 (cc. 26-27) y 2 (cc. 28-29),
   calderones en los cc. 19, 24 y 29. No imprime "To Coda"."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=7, slug='your_song', pdf='your_song_elton_john_mi_b_m.pdf', time_sig=(4, 4),
    titulo='Your Song', autor='Elton John · arranjament per a piano (musicaparadisfrutar.com)',
    kicker='Eva · peça 7 · Your Song', mes='Febrer · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=your+song+elton+john+piano+tutorial',
    credito='Partitura: Elton John, Your Song (musicaparadisfrutar.com). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Mi♭ major'), ('Compàs', '4/4 · algun 2/4'), ('Tempo', '♩ = 66'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '29')],
        total=29,
        secciones=[('A', 1, 12, 'Primera part · segno · caselles', AZUL),
                   ('B', 13, 22, 'Continua · D.S. al Coda', OCRE), ('C', 23, 29, 'Coda · final', AZUL)],
        ideas_titulo="Els acords, d'un cop d'ull",
        ideas=[('CC. 1-2', 'Mi♭ · La♭ · Mi♭ · La♭',
                'Mi♭ major (tònica) i La♭ major, alternant cada dos temps. A la teva partitura: '
                'E♭ i A♭.'),
               ('CC. 3-12', 'Mi♭ · La♭ · Si♭ · Do m',
                'Mi♭, La♭ amb sèptima major, Si♭, Sol menor, Do menor i Fa menor. Als cc. 5-6 '
                'el baix baixa: Do, Si♭, La, La♭ (xifrat).'),
               ('CC. 13-22', 'Do m · Fa m7 · La♭',
                'Do menor, Fa menor amb sèptima, La♭ amb sexta, i Si♭ i Mi♭ amb una altra nota al '
                'baix (Si♭/Re, Mi♭/Sol).'),
               ('CC. 23-29', 'La Coda · Mi♭',
                'Les mateixes notes dels cc. 18-21, amb el xifrat gairebé igual, i final en Mi♭ '
                '(c. 29).')],
        ideas_pie='Sobre la partitura els acords surten en xifrat americà (A = La, B = Si, '
                  'C = Do, D = Re, E = Mi, F = Fa, G = Sol; ♭ = bemoll; "m" = menor; la barra '
                  'indica la nota del baix). Aquí els diem pel nom de sempre.',
        especial=[
            'Posa ♩ = 66 (lent) i no porta cap matís imprès (ni p, ni f).',
            "Tres bemolls (si♭, mi♭, la♭) a l'inici de cada pentagrama: Mi♭ major.",
            'Segno i barra |: al c. 3; caseta 1 als cc. 10-11 i caseta 2 al c. 12.',
            'Després del c. 22 posa "D.S. al Coda"; la Coda són els cc. 23-29, amb la seva '
            'repetició.',
            "L'esquerra toca quasi sempre dues notes juntes, en blanques.",
            'Compassos de 2/4: cc. 11, 13, 22 i 27. Calderons: cc. 19, 24 i 29.'],
        reto="Entrar sense pressa després dels silencis de corxera, amb semicorxeres iguals, i no "
             "perdre't en el recorregut (segno, caselles, D.S. i Coda).",
        truco='Abans de tocar, segueix el recorregut amb el dit i digues-lo en veu alta. La partitura '
              'no imprimeix "To Coda": acorda amb la teva professora on es salta.',
        sabias='Elton John va publicar «Your Song» el 1970, amb lletra del seu company Bernie Taupin. Va ser el seu primer gran èxit.',
        qr_texto='Escolta-la amb la partitura al davant: segueix les repeticions amb el dit.',
        ts=(4, 4)),
    manos=dict(
        izq=[('Dues notes alhora', "L'esquerra toca quasi sempre dues notes juntes, llargues. "
                                   'Practica la parella: col·loca-la sense mirar i deixa-la anar '
                                   'a poc a poc.'),
             ('El xifrat et guia', 'La lletra de dalt (E♭ = Mi♭, A♭ = La♭) et diu en quin acord '
                                   'ets. Llegeix-la abans de cada canvi.'),
             ('Els becaires', "Als cc. 6, 8, 19 i 24 hi ha becaires a l'esquerra: aquesta nota va "
                              'sense bemoll. Llegeix-la dues vegades abans de tocar.'),
             ('Compassos de 2/4', 'Als cc. 11, 13, 22 i 27 només hi ha dos temps: compta 1-2 i '
                                  'continua.')],
        der=[('Entrar després del silenci', 'Moltes frases comencen amb silenci de corxera (cc. 3, 4 '
                                            'i 6): compta’l i no entris abans.'),
             ('Semicorxeres lligades', 'Compta quatre semicorxeres per cop. A cada lligadura toca '
                                       'la primera nota i mantén la segona.'),
             ('El tresillo', 'Als cc. 8, 9, 15 i 17 el "3" marca tres notes en el temps de '
                             'dues. Digues "tre-si-llo" mentre toques.'),
             ("Amb l'esquerra", "Uneix a poc a poc una frase amb l'esquerra ja segura. Si es "
                                'trenca, torna a una sola mà.')],
        tecnica=['Canell solt: les semicorxeres surten cantades, no apretades.',
                 'Compta 1-2-3-4 sense pressa: ♩ = 66 és lent.',
                 'Mira el recorregut (segno, caselles, Coda) abans de tocar.']),
    bloques=[
        B(1, 'cc. 1-2', "L'arrencada", (0, 0),
          D('cuenta', '4/4 en semicorxeres: quatre per cop', [('un compàs', 4, 4)]),
          [('IZQUIERDA', 'Dues blanques de dues notes per compàs: Mi♭ i La♭ segons el xifrat.'),
           ('DERECHA', 'Corxeres i semicorxeres lligades; entra ja al primer temps.'),
           ('JUNTAS', 'Compta 1-2-3-4 i toca només aquests dos compassos fins que no t’aturis.'),
           ('A TEMPO', '♩ = 66: comença més lent i puja a poc a poc.')]),
        B(2, 'cc. 3-5', 'Segno i repetició', (1, 1),
          D('cadena', 'Des del c. 3 es repeteix', [('segno i |: al c. 3', False),
                                                   ('toques fins a la caseta', True)]),
          [('IZQUIERDA', 'Mateixes blanques de dues notes: l’acord canvia cada dos temps.'),
           ('DERECHA', 'Entra després d’un silenci de corxera (cc. 3-4) o de corxera amb puntet '
                       '(c. 5).'),
           ('JUNTAS', 'Compta el silenci en veu alta i entra amb l’esquerra ja posada.'),
           ('OJO', 'La barra |: del c. 3 marca on es torna cada vegada.')]),
        B(3, 'cc. 6-8', 'Becaires i tresillo', (2, 2),
          D('fichas', 'Alteracions d’aquests compassos',
            ['c. 6: La natural (esq.)', 'c. 8: Si natural (esq.)', 'cc. 6 i 8: un bemoll solt (dta.)']),
          [('IZQUIERDA', 'Becaire al c. 6 (La) i al c. 8 (Si): sense el bemoll de l’armadura.'),
           ('DERECHA', 'Un bemoll solt als cc. 6 i 8; tresillo al c. 8: tres notes en el '
                       'temps de dues.'),
           ('JUNTAS', 'Primer només les notes alterades; després, el compàs sencer.'),
           ('OJO', 'El xifrat ja ho diu: Do m amb La al baix (c. 6) i Sol amb Si (c. 8).')]),
        B(4, 'cc. 9-12', 'Les caselles', (3, 3),
          D('cadena', 'Les dues voltes', [('caseta 1 (cc. 10-11)', False), ('↩ al c. 3', False),
                                         ('caseta 2 (c. 12)', True)]),
          [('IZQUIERDA', 'Blanques de dues notes; el c. 11 és de 2/4 i només en porta una.'),
           ('DERECHA', 'Tresillo al c. 9. Al c. 11 hi ha un compàs sencer de silenci.'),
           ('JUNTAS', '1.a vegada: cc. 9-11 i tornada al c. 3. 2.a vegada: c. 9 i salt al c. 12.'),
           ('OJO', 'La caseta 1 acaba amb :|; la caseta 2 continua al c. 13.')]),
        B(5, 'cc. 13-19', 'Més semicorxeres', (4, 5),
          D('capas', 'Dues capes alhora',
            [('Dreta: semicorxeres', 'puntos', AZUL, 8), ('Esquerra: blanques', 'barras', OCRE)]),
          [('IZQUIERDA', 'El c. 13 (2/4) porta una sola blanca; del c. 14 al 19, dues per compàs.'),
           ('DERECHA', 'Semicorxeres lligades des del c. 14; tresillo als cc. 15 i 17.'),
           ('JUNTAS', 'Dos trams en bucle: cc. 13-16 i cc. 17-19.'),
           ('OJO', 'c. 19: becaire a les dues mans i calderó sobre la negra del tercer temps.')]),
        B(6, 'cc. 20-22', 'D.S. al Coda', (6, 6),
          D('cadena', 'El salt', [('c. 22: D.S. al Coda', False), ('tornes al segno (c. 3)', False),
                                  ('Coda: c. 23', True)]),
          [('IZQUIERDA', 'Dues blanques per compàs; el c. 22 és de 2/4 i en porta una sola.'),
           ('DERECHA', 'Corxera amb puntet i semicorxera (cc. 20-21); bemoll solt en començar el '
                       'c. 21.'),
           ('JUNTAS', 'Toca els cc. 20-22 i torna al c. 3 sense parar: assaja el salt.'),
           ('OJO', 'No hi ha "To Coda" imprès: acordeu amb la professora on es salta.')]),
        B(7, 'cc. 23-29', 'La Coda i el final', (7, 8),
          D('cadena', 'La Coda', [('c. 23: |: i signe de Coda', False),
                                  ('caseta 1 (cc. 26-27)', False), ('caseta 2 (cc. 28-29)', True)]),
          [('IZQUIERDA', 'Els cc. 23-26 repeteixen les notes dels cc. 18-21; el c. 29, tres notes '
                         'en rodona.'),
           ('DERECHA', 'Les mateixes semicorxeres dels cc. 18-21; l’última nota ve lligada '
                       'del c. 28.'),
           ('JUNTAS', 'Primer cc. 23-27 i tornada al c. 23; després cc. 23-26 i caseta 2.'),
           ('A TEMPO', 'Calderons: c. 24 i c. 29 (en aquest últim, a les dues mans).')]),
    ],
    cortes={1: [269.8, 399.5, 519.0, 634.0], 2: [166.0, 285.8, 423.0]},
    corte_titulo=140.0,
    burb={
        0: [('arriba', 270, 'IZQ', 'Dues notes juntes, en blanques, i el xifrat a sobre: E♭ = Mi♭, '
                                   'A♭ = La♭.', 0.1),
            ('arriba', 270, 'AMB', 'Tres bemolls: Mi♭ major. ♩ = 66 i cap matís imprès.', 0.7)],
        1: [('arriba', 300, 'OJO', 'Segno i barra |: al c. 3: des d’aquí es repeteix. Entra després '
                                   'del silenci de corxera.', 0.05)],
        2: [('arriba', 270, 'IZQ', 'Becaires a l’esquerra (cc. 6 i 8): La i Si naturals, sense '
                                   'bemoll.', 0.1),
            ('arriba', 270, 'DER', 'Bemoll solt als cc. 6 i 8 i tresillo al c. 8.', 0.75)],
        3: [('arriba', 330, 'OJO', 'Caseta 1 (cc. 10-11) i tornada al c. 3; la 2.a vegada, caseta 2 '
                                   '(c. 12). Tresillo al c. 9.', 0.45)],
        5: [('arriba', 270, 'DER', 'Tresillo al c. 17 i silenci de semicorxera en començar el '
                                   'c. 18.', 0.2),
            ('arriba', 270, 'OJO', 'c. 19: becaire a les dues mans i calderó: aguanta aquesta '
                                   'negra.', 0.8)],
        6: [('arriba', 300, 'OJO', 'D.S. al Coda després del c. 22: tornes al segno del c. 3. No hi ha '
                                   '"To Coda" imprès.', 0.85)],
        7: [('arriba', 300, 'OJO', 'Signe de Coda i barra |: al c. 23. Aquests compassos són '
                                   'iguals als cc. 18-20.', 0.05)],
        8: [('arriba', 270, 'OJO', 'Caseta 1 (cc. 26-27) i tornada al c. 23; la 2.a vegada, caseta 2 '
                                   '(cc. 28-29).', 0.1),
            ('arriba', 270, 'AMB', 'Acord final: rodona amb calderó a les dues mans.', 0.85)],
    },
    marcas=[],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l’escala de Mi♭ major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_your_song.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
