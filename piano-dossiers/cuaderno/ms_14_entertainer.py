# -*- coding: utf-8 -*-
"""Pieza 14 · The Entertainer (Scott Joplin, arr. Gilbert DeBenedetti, nivel 3, gradimi.com).
   MEDIDO sobre el PDF (2 paginas, tamano carta, 9 sistemas): 40 compases (4+4+4+5 en la pagina 1,
   4+5+4+5+5 en la 2), sin armadura (Do mayor), 2/2 (¢), "Not fast" sin metronomo, figura mas corta
   la negra, 8va en la derecha de los cc. 1-2, izquierda en silencio hasta el c. 8, calderon sobre el
   silencio del c. 8, matices p (c. 1), f (c. 8), p (c. 8), f (c. 12), p (c. 16), f (c. 20), p (c. 24),
   f (c. 28); alteraciones: la bemol (c. 6), re sostenido (cc. 8, 12, 16, 24, 28), fa sostenido (c. 21),
   si bemol (izquierda cc. 10, 18, 34) y la bemol (izquierda c. 36); final en staccato."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=14, slug='entertainer', pdf='el_golpe.pdf', time_sig=(2, 2),
    titulo="The Entertainer", autor="Scott Joplin · arr. Gilbert DeBenedetti",
    kicker="Sharifa · peça 14 · The Entertainer", mes="Juliol · 1.a quinzena",
    yt='https://www.youtube.com/results?search_query=scott+joplin+the+entertainer+piano',
    credito="Partitura: S. Joplin, arr. G. DeBenedetti, nivell 3 (gradimi.com). Anotacions: T-Clas.",
    ficha=FICHA(
        datos=[("Tonalitat", "Do major"), ("Compàs", "2/2 (¢)"), ("Caràcter", "Not fast: sense pressa"),
               ("Figura curta", "Negra"), ("Compassos", "40")],
        total=40,
        secciones=[("A", 1, 8, "Entrada", AZUL),
                   ("B", 9, 17, "Entra l'esquerra", OCRE),
                   ("C", 18, 26, "Fa♯ i torna el tema", AZUL),
                   ("D", 27, 35, "Tema i baixada", OCRE),
                   ("E", 36, 40, "Final", AZUL)],
        ideas_titulo="La peça en quatre idees",
        ideas=[("ESQUERRA", "Baix i acord",
                "Des del c. 9: una nota greu, un silenci, un acord i un altre silenci. És el pas de "
                "marxa del ragtime."),
               ("DRETA", "Notes lligades",
                "Moltes notes es lliguen per sobre de la barra i cauen entre temps. Això és el "
                "ragtime: temps «trencat»."),
               ("ELS ACORDS", "Do · Fa · Sol",
                "Do major; Do amb sèptima (el si♭ del c. 10); Fa major (c. 11); Sol amb sèptima, "
                "la dominant (c. 8)."),
               ("ELS MATISOS", "p ↔ f",
                "p al c. 1, f al c. 8 i després p i f cada quatre compassos: cc. 12, 16, 20, 24 "
                "i 28.")],
        especial=[
            "Posa «Not fast»: sense pressa. No porta metrònom.",
            "És 2/2 (¢): dos temps per compàs, cadascun de blanca.",
            "L'esquerra no toca fins al c. 8; abans, la dreta va sola.",
            "Els cc. 1-2 porten 8va: sonen una octava més aguda del que està escrit.",
            "Alteracions: la♭ (c. 6), re♯ (cc. 8, 12, 16, 24 i 28), fa♯ (c. 21) i, a l'esquerra, "
            "si♭ i la♭.",
            "Hi ha un calderó sobre el silenci del c. 8 i acaba amb notes curtes (staccato)."],
        reto="Mantenir l'esquerra «baix-acord» ferma i regular mentre la dreta juga amb les "
             "lligadures. Ho aconseguiràs sense mirar-te les mans?",
        truco="Aprèn-te l'esquerra dels cc. 9-12 de memòria. Compta «un-dos» (una blanca cada "
              "número) i toca la dreta a sobre.",
        sabias="Scott Joplin, el «rei del ragtime», va publicar The Entertainer el 1902. Es va fer "
               "famosa a tot el món el 1973 amb la pel·lícula «The Sting» (en castellà, «El golpe»). "
               "Joplin avisava: «mai no és correcte tocar ragtime de pressa».",
        qr_texto="Escolta-la i busca el «baix-acord» de l'esquerra.", ts=(2, 2),
        cuenta_titulo="Dos compassos de la peça",
        cuenta_pie="A dalt, la dreta (c. 1): quatre negres. A baix, l'esquerra (c. 9): baix, "
                   "silenci, acord, silenci. En 2/2 hi ha dos temps de blanca.",
        ritmos=[("MD", "c. 1 · el motiu",
                 [{'pitch': 'D5', 'dur': 'q'}, {'pitch': 'E5', 'dur': 'q'},
                  {'pitch': 'C5', 'dur': 'q'}, {'pitch': 'A4', 'dur': 'q'}],
                 AZUL, 'treble', None),
                ("ME", "c. 9 · baix i acord",
                 [{'pitch': 'C3', 'dur': 'q'}, {'rest': True, 'dur': 'q'},
                  {'pitches': ['E3', 'G3'], 'dur': 'q'}, {'rest': True, 'dur': 'q'}],
                 OCRE, 'bass', None)]),
    manos=dict(
        izq=[("Compta abans d'entrar", "L'esquerra calla fins al c. 8. Compta «un-dos» en veu alta "
                                       "set compassos i entra amb el Sol greu."),
             ("Baix i acord", "Cc. 9-12: nota greu, silenci, acord, silenci. Primer només el baix; "
                              "després, l'acord."),
             ("Els acords canvien", "C. 10: l'acord porta un si♭ (Do amb sèptima). C. 11: Fa major. "
                                    "C. 12: Do major."),
             ("La baixada", "Als cc. 34-37 la nota de dalt baixa per semitons: si♭, la, la♭, sol, "
                            "sobre un do que no canvia.")],
        der=[("El motiu", "Cc. 1-4: re, mi, do, la / la, si, sol. Toca'l a poc a poc: amb l'8va "
                          "sona una octava més aguda."),
             ("La lligadura", "El la del c. 1 està lligat al c. 2: es toca una vegada i "
                              "s'aguanta. Compta «un-dos» sense parar."),
             ("Re, re♯, mi", "Cc. 8, 12 i 16: la mà puja per semitons (re, re♯) i arriba al mi. "
                             "Lleugera i a poc a poc."),
             ("Amb l'esquerra", "Ajunta els cc. 9-12 a dues mans, molt a poc a poc. Si et perds, "
                                "torna a una mà.")],
        tecnica=["Canell solt: el ragtime es toca lleuger, sense picar.",
                 "L'esquerra marca el pols: el baix, una mica més fort que l'acord.",
                 "No correguis: posa «Not fast»."]),
    misol=dict(
        manos="Aquí el ritme és «bum-ts»: baix, silenci, acord, silenci. Digues-ho en veu alta "
              "abans de tocar-ho i et sortirà molt millor!",
        guia="Els cc. 27-30 són els mateixos que els cc. 11-14: aprofita-ho! Només has d'estudiar "
             "bé la part nova, a partir del c. 31.",
        pauta="Inventa un compàs de ragtime: nota greu, silenci, acord, silenci a l'esquerra. O "
              "copia el motiu del c. 1: re, mi, do, la!"),
    bloques=[
        B(1, 'cc. 1-4', "L'entrada", (0, 0),
          D('cuenta', "Un compàs de 2/2: dos temps de blanca",
            [("un compàs", 2, 2)]),
          [('IZQUIERDA', "Calla. Compta «un-dos» en veu alta amb ella."),
           ('DERECHA', "Re, mi, do, la. El la es lliga al c. 2. Després la, si, sol."),
           ('OJO', "Psst! L'8va: el llegeixes on és, però sona una octava més aguda."),
           ('A TEMPO', "«Not fast»: pols tranquil, sense pressa.")]),
        B(2, 'cc. 5-8', "La♭ i calderó", (1, 1),
          D('cadena', "Del silenci al tema",
            [("f", False), ("calderó", False), ("p: re, re♯", True)]),
          [('IZQUIERDA', "Per fi entra: Sol greu amb accent, a la vegada que l'acord."),
           ('DERECHA', "Com el c. 1; al c. 6 surt un la♭. El c. 8, acord amb f."),
           ('OJO', "El calderó és sobre el silenci: espera i continua en p."),
           ('JUNTAS', "Toca només el c. 8 moltes vegades: acord, silenci, re, re♯.")]),
        B(3, 'cc. 9-12', "Entra el tema", (2, 2),
          D('cadena', "Esquerra, compàs a compàs",
            [("baix", False), ("silenci", False), ("acord", False), ("silenci", True)]),
          [('IZQUIERDA', "Baix, silenci, acord, silenci. Al c. 10 l'acord porta si♭."),
           ('DERECHA', "Mi, do (llarga), mi. Do (llarga), mi, do lligat. Do, re, re♯ amb f."),
           ('JUNTAS', "Dos compassos cada cop: 9-10, 11-12 i després els quatre."),
           ('OJO', "Al c. 11 l'acord és de Fa, amb el do a baix. C. 12: acord curt.")]),
        B(4, 'cc. 13-17', "Segona frase", (3, 3),
          D('cadena', "El camí de la frase",
            [("cc. 13-15", False), ("c. 16: p", False), ("c. 17 = c. 9", True)]),
          [('IZQUIERDA', "Do i acord (c. 13); Sol llarg (c. 14); do i sol curts (c. 15)."),
           ('DERECHA', "Mi, do, re, mi lligat; mi, si, re. Al c. 15, un do llarg."),
           ('JUNTAS', "Cc. 13-14 i 15-16 per separat; després els cinc compassos."),
           ('OJO', "C. 16: p, altra vegada re, re♯. Al c. 17 torna el tema!")]),
        B(5, 'cc. 18-21', "Apareix el fa♯", (4, 4),
          D('cadena', "L'esquerra, compàs a compàs",
            [("Do amb si♭", False), ("Fa", False), ("Do", False), ("Re", True)]),
          [('IZQUIERDA', "Do amb si♭, Fa i Do. Al c. 21: Re greu i acord amb fa♯."),
           ('DERECHA', "Com els cc. 10-11. Després la, sol amb f; i fa♯, la, do, mi al c. 21."),
           ('JUNTAS', "Fes el c. 21 sol: és nou. Després, del c. 18 al 21."),
           ('OJO', "El fa♯ del c. 21 és nou a les dues mans: llegeix-lo abans de tocar.")]),
        B(6, 'cc. 22-26', "Torna el tema", (5, 5),
          D('cadena', "Cap al tema",
            [("Re i Sol", False), ("p: re, re♯", False), ("la, si, do", False), ("tema", True)]),
          [('IZQUIERDA', "Re (c. 22), Sol agut i Sol greu (c. 23); puja la, si, do (cc. 24-25)."),
           ('DERECHA', "Mi, re, do, la; re llarga; al c. 24, p: re, re♯."),
           ('JUNTAS', "Toca la pujada la-si-do de l'esquerra i entra al tema."),
           ('OJO', "Els cc. 25-26 són com els cc. 9-10: ja els saps!")]),
        B(7, 'cc. 27-35', "El tema i la baixada", (6, 7),
          D('cadena', "Què es repeteix",
            [("cc. 27-30 = 11-14", False), ("c. 32: do, re", False), ("mi, do, re", True)]),
          [('IZQUIERDA', "Cc. 27-32 com els cc. 11-16. Des del c. 33, acords llargs."),
           ('DERECHA', "Cc. 27-30 = cc. 11-14. Al c. 32, només do-re (sense re♯)."),
           ('JUNTAS', "Estudia els cc. 27-30; després 31-35 en dues meitats."),
           ('OJO', "«Mi, do, re, mi» es repeteix als cc. 33 a 37: no perdis el compte!")]),
        B(8, 'cc. 36-40', "El final", (8, 8),
          D('cadena', "L'esquerra al final",
            [("Do + la♭", False), ("Do + sol", False), ("Sol llarg", False),
             ("do, sol, do", True)]),
          [('IZQUIERDA', "Do + la♭, Do + sol, Sol llarg; i do, sol, do greu curts."),
           ('DERECHA', "Dues frases «mi, do, re»; mi, si, re (c. 38); do curt (c. 39)."),
           ('JUNTAS', "Cc. 36-38 a dues mans; després, els dos últims compassos."),
           ('A TEMPO', "Acaba curt (staccato). El c. 40 és només l'esquerra.")]),
    ],
    cortes={1: [259.5, 293.5, 417.4, 442.9, 574.0, 592.0],
            2: [180.5, 196.5, 326.9, 345.4, 474.5, 489.5, 608.0, 619.5]},
    corte_titulo=154.8,
    fin={1: 717.8, 2: 750.0},
    burb={
        0: [('abajo', 262, 'DER', "8va als cc. 1-2: sonen una octava més aguda del que està "
                                  "escrit. El la del c. 1 es lliga al c. 2.", 0.3),
            ('abajo', 262, 'IZQ', "L'esquerra no toca fins al c. 8: compta «un-dos» amb ella.",
             0.6)],
        1: [('arriba', 470, 'OJO', "Psst! Calderó sobre el silenci del c. 8: espera i continua "
                                   "en p, re, re♯.", 0.85),
            ('abajo', 262, 'IZQ', "Entra amb un Sol greu (accent) a la vegada que l'acord.",
             0.9)],
        2: [('abajo', 300, 'IZQ', "Baix, silenci, acord, silenci. Al c. 10 porta si♭ (Do amb "
                                  "sèptima); al c. 11, Fa.", 0.4)],
        3: [('abajo', 300, 'IZQ', "C. 14: Sol greu llarg. C. 15: do i sol curts (staccato).",
             0.5)],
        4: [('arriba', 480, 'OJO', "Fixa-t'hi: fa♯ al c. 21, nou a les dues mans. A l'esquerra, "
                                   "Re major.", 0.9)],
        5: [('abajo', 300, 'IZQ', "Cc. 24-25: la, si, do pugen fins al tema.", 0.45)],
        6: [('arriba', 300, 'AMB', "Cc. 27-30 = cc. 11-14: ja ho saps! La f és al c. 28.",
             0.3)],
        7: [('abajo', 440, 'IZQ', "La nota de dalt baixa: si♭ (c. 34), la (c. 35), la♭ i sol "
                                  "(cc. 36-37).", 0.7)],
        8: [('abajo', 440, 'AMB', "Final curt: do, sol i do greu. L'últim compàs és només "
                                  "l'esquerra.", 0.7)],
    },
    marcas=[],
    pie_pauta="la clau la poses tu · copia un compàs o escriu l'escala de Do major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_entertainer.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
