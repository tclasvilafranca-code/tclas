# -*- coding: utf-8 -*-
"""Pieza 15 · Shallow (Lady Gaga y Bradley Cooper), arreglo de Campamento Musical Bye Bye Beethoven.
   MEDIDO sobre el PDF (3 paginas, tamano carta, 14 sistemas): 55 compases (5 sistemas de 4 en la
   pagina 1, 4+4+4+4+3 en la 2, 4+4+4+4 en la 3), armadura de un sostenido (Sol mayor), 4/4,
   negra = 96, sin matices escritos ni alteraciones, semicorchea como figura mas corta (cc. 20, 24,
   43), dobles barras tras los cc. 16, 24, 32, 39 y 47; izquierda en parejas de notas (casi todas
   quintas vacias), acaba en Mi (c. 55: derecha si, izquierda mi-si)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=15, slug='shallow', pdf='shallow.pdf', time_sig=(4, 4),
    titulo="Shallow", autor="Lady Gaga i Bradley Cooper · arr. Bye Bye Beethoven",
    kicker="Sharifa · peça 15 · Shallow", mes="Juliol · 2.a quinzena",
    yt='https://www.youtube.com/results?search_query=lady+gaga+bradley+cooper+shallow',
    credito="Partitura: Shallow, arranjament de Campamento Musical Bye Bye Beethoven "
            "(byebyebeethoven.es). Anotacions: T-Clas.",
    ficha=FICHA(
        datos=[("Tonalitat", "Sol major"), ("Compàs", "4/4"), ("Tempo", "Negra = 96"),
               ("Figura curta", "Semicorxera"), ("Compassos", "55")],
        total=55,
        secciones=[("A", 1, 16, "Estrofa", AZUL),
                   ("B", 17, 24, "La melodia puja", OCRE),
                   ("C", 25, 32, "Nota repetida", AZUL),
                   ("D", 33, 39, "Frases curtes", OCRE),
                   ("E", 40, 47, "Torna la pujada", AZUL),
                   ("F", 48, 55, "Final en Mi", OCRE)],
        ideas_titulo="La peça en quatre idees",
        ideas=[("ESQUERRA", "Dues notes alhora",
                "Gairebé sempre una quinta buida (sol-re, la-mi, mi-si): dues notes que sonen "
                "buides i netes."),
               ("DRETA", "Nota repetida",
                "Repeteix una nota (do, sol, fa♯) en corxeres i després fa un pas. Cal comptar "
                "bé."),
               ("EL RITME", "Notes lligades",
                "Moltes notes comencen a mig temps i es lliguen al compàs següent: cc. 1-2, "
                "9-10…"),
               ("ELS ACORDS", "Mi · Re · Sol · Do",
                "Són els dels cc. 1-4. Després arriben La i Si. Un cop apresos, es van "
                "repetint.")],
        especial=[
            "Un sostingut a l'armadura (fa♯): Sol major. No hi ha més alteracions.",
            "Negra = 96. No porta matisos escrits: tu tries com sona.",
            "Els cc. 1-4 i 5-8 són idèntics: s'aprenen una sola vegada.",
            "Els cc. 17-24 i 40-47 són gairebé iguals: la melodia puja i torna.",
            "Hi ha semicorxeres als cc. 20, 24 i 43: sol-la molt ràpids.",
            "Comença i acaba en Mi: l'últim compàs és mi-si a l'esquerra i un si a la dreta."],
        reto="Comptar bé les notes repetides: la dreta repeteix i l'esquerra canvia d'acord enmig. "
             "Pots fer-ho sense perdre el pols?",
        truco="Aprèn les parelles de l'esquerra dels cc. 1-4 com un dibuix de la mà i toca la "
              "melodia a sobre.",
        sabias="«Shallow» és de la pel·lícula «A Star Is Born» (2018; en castellà, «Ha nacido una "
               "estrella») i va guanyar l'Oscar a la millor cançó original el 2019. La van "
               "escriure Lady Gaga, Mark Ronson, Anthony Rossomando i Andrew Wyatt.",
        qr_texto="Escolta-la i marca el pols (negra = 96) amb el peu.", ts=(4, 4),
        cuenta_titulo="Dos compassos de la peça",
        cuenta_pie="A dalt, la dreta (cc. 1-2). A baix, l'esquerra (cc. 1-2): parelles de notes. "
                   "Fixa't en la lligadura: el si es lliga al c. 2.",
        ritmos=[("MD", "cc. 1-2 · la melodia",
                 [{'rest': True, 'dur': 'q'}, {'pitch': 'E4', 'dur': 'e', 'beam': 0},
                  {'pitch': 'E4', 'dur': 'e', 'beam': 0}, {'pitch': 'E4', 'dur': 'e'},
                  {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'B3', 'dur': 'e', 'lig': True},
                  {'pitch': 'B3', 'dur': 'h'}, {'rest': True, 'dur': 'h'}],
                 AZUL, 'treble', 'Sol mayor'),
                ("ME", "cc. 1-2 · parelles de notes",
                 [{'pitches': ['E2', 'B2'], 'dur': 'h'}, {'pitches': ['F#2', 'D3'], 'dur': 'q.'},
                  {'pitches': ['G2', 'D3'], 'dur': 'e', 'lig': True},
                  {'pitches': ['G2', 'D3'], 'dur': 'w'}],
                 OCRE, 'bass', 'Sol mayor')]),
    manos=dict(
        izq=[("Parelles de notes", "L'esquerra gairebé sempre toca dues notes alhora (una quinta): "
                                   "mi-si, sol-re, do-sol, la-mi. Aprèn cada parella."),
             ("Els cc. 1-4", "Cc. 1-2: mi-si, fa♯-re, sol-re. Cc. 3-4: do-sol, sol-re, re-fa♯. "
                             "En bucle, amb el pols."),
             ("Notes lligades", "Moltes parelles s'allarguen amb una lligadura: es toquen una "
                                "vegada i s'aguanten."),
             ("Els cc. 38-39", "C. 38: quatre acords de negra (re-fa♯). C. 39: set corxeres amb "
                               "la-mi.")],
        der=[("Notes repetides", "Als cc. 3 i 17 la mateixa nota sona sis i cinc vegades. Prem "
                                 "lleuger, sense picar, i compta «1 i 2 i»."),
             ("L'estrofa", "Els cc. 1-16 es mouen entre sol i re. Toca-la sola fins que te la "
                           "sàpigues de memòria."),
             ("La pujada", "Al c. 17 la mà puja: do agut repetit i si. Al c. 19 arriba la nota "
                           "més aguda, re."),
             ("Semicorxeres", "Als cc. 20, 24 i 43: sol-la molt ràpids i un si llarg. El sol ve "
                              "lligat del compàs anterior.")],
        tecnica=["Canell solt: el pols se sent al braç, no als dits.",
                 "La melodia mana: l'esquerra, més suau i sempre igual.",
                 "Compta en veu alta «1 i 2 i 3 i 4 i»: quasi tot són corxeres."]),
    misol=dict(
        manos="Al principi sembla que repeteixes la mateixa nota mil cops. Tranquil·la! Compta "
              "«1 i 2 i» i els dits ja s'hi apanyen sols.",
        guia="Els cc. 1-4 i 5-8 són iguals, i els cc. 40-47 repeteixen els 17-24. Estudia menys i "
             "toca més: bona part de la peça ja la saps!",
        pauta="Escriu les parelles de l'esquerra dels cc. 1-2 (mi-si, fa♯-re, sol-re) o inventa "
              "una melodia amb una sola nota repetida!"),
    bloques=[
        B(1, 'cc. 1-8', "L'estrofa, dues vegades", (0, 1),
          D('cadena', "Es toca igual dues vegades",
            [("cc. 1-4", False), ("= cc. 5-8", True)]),
          [('IZQUIERDA', "Mi-si, fa♯-re, sol-re / do-sol, sol-re, re-fa♯. A poc a poc."),
           ('DERECHA', "Silenci de negra i entra: mi, mi, mi, re, si (lligat)."),
           ('JUNTAS', "Un compàs cada cop: 1, 2, 3, 4. Després els quatre, i repeteix."),
           ('A TEMPO', "Negra = 96. Comença més lenta i puja a poc a poc.")]),
        B(2, 'cc. 9-16', "Segona part de l'estrofa", (2, 3),
          D('cadena', "Què es repeteix",
            [("cc. 9-10 = 13-14", False), ("c. 11 = c. 15", False), ("c. 16 tanca", True)]),
          [('IZQUIERDA', "Les mateixes parelles dels cc. 1-4: ja les saps."),
           ('DERECHA', "Melodia més greu: sol, la, si. Al c. 11 puja a re."),
           ('JUNTAS', "Primer els cc. 9-12; després el 13-16, que és gairebé igual."),
           ('OJO', "Després del c. 16 hi ha doble barra: s'acaba l'estrofa. Respira!")]),
        B(3, 'cc. 17-24', "La melodia puja", (4, 5),
          D('cadena', "El dibuix de cada compàs",
            [("c. 17: do", False), ("c. 18: la", False), ("c. 19: re", False),
             ("c. 20: sol-la", True)]),
          [('IZQUIERDA', "Parelles noves: la-mi i la nota sol, sola (c. 17), fa♯-re (c. 18), mi-si "
                         "(c. 20)."),
           ('DERECHA', "C. 17: do repetit i si. C. 19: arriba al re, el més agut."),
           ('JUNTAS', "Els cc. 21-24 repeteixen els 17-20; el c. 22 afegeix un re."),
           ('OJO', "Semicorxeres del c. 20: sol-la ràpids i si llarg. Ho tens!")]),
        B(4, 'cc. 25-32', "Una nota, moltes vegades", (6, 7),
          D('cadena', "La nota que es repeteix",
            [("sol", False), ("fa♯", False), ("mi", True)]),
          [('IZQUIERDA', "Parelles noves: sol-mi (c. 25) i re-la (c. 27). Llegeix-les abans."),
           ('DERECHA', "Sol repetit (c. 25), fa♯ (c. 26) i mi (c. 28): baixa esglaó a esglaó."),
           ('JUNTAS', "Els cc. 29-32 repeteixen els 25-28; el final baixa a re i si."),
           ('OJO', "El c. 32 queda en un si llarg i arriba la doble barra.")]),
        B(5, 'cc. 33-39', "Frases curtes", (8, 9),
          D('cadena', "Es toca, es respira, es toca",
            [("frase", False), ("silenci", False), ("frase", False), ("si llarg", True)]),
          [('IZQUIERDA', "Parelles llargues: si-fa♯, re-fa♯, la-mi, mi-si. C. 38: negres. C. 39: "
                         "corxeres."),
           ('DERECHA', "Fa♯, sol, fa♯, mi. Compta els silencis i no correguis."),
           ('JUNTAS', "De quatre en quatre compassos: 33-36 i 37-39."),
           ('OJO', "Cc. 38-39: un si de set temps (rodona i blanca amb puntet lligades).")]),
        B(6, 'cc. 40-47', "Torna la pujada", (10, 11),
          D('cadena', "Què es repeteix",
            [("cc. 40-43 = 17-20", False), ("cc. 44-45 = 21-22", False),
             ("cc. 46-47 canvien", True)]),
          [('IZQUIERDA', "Igual que els cc. 17-24: la-mi, fa♯-re, sol-re, mi-si."),
           ('DERECHA', "Igual que els cc. 17-22. Al c. 46 canvia el final: sol, re, si."),
           ('JUNTAS', "Si ja saps els cc. 17-24, només has d'aprendre els cc. 46-47."),
           ('OJO', "El c. 47 acaba en si llarg i arriba la doble barra.")]),
        B(7, 'cc. 48-55', "El final", (12, 13),
          D('cadena', "Cap al final",
            [("cc. 48-51 ≈ 25-28", False), ("mi repetit", False), ("si llarg", True)]),
          [('IZQUIERDA', "Parelles dels cc. 25-28. L'últim compàs: mi-si, una rodona."),
           ('DERECHA', "Cc. 52-55: mi repetit, re-mi-fa♯, sol repetit i si final."),
           ('JUNTAS', "Toca els cc. 52-55 diverses vegades: és el que se sent al final."),
           ('A TEMPO', "Tota la peça, sense parar, negra = 96. Quan et surti, grava-la!")]),
    ],
    cortes={1: [242.5, 261.5, 368.5, 387.5, 497.0, 516.0, 626.5, 645.5],
            2: [153.4, 172.9, 278.4, 297.9, 405.4, 424.9, 532.0, 551.5],
            3: [153.0, 173.0, 277.1, 296.6, 401.5, 421.5]},
    corte_titulo=119.0,
    fin={1: 748.0},
    burb={
        0: [('arriba', 262, 'AMB', "Negra = 96. Comença amb un silenci de negra: compta «1» i "
                                   "entra al «2».", 0.1),
            ('abajo', 262, 'IZQ', "Parelles de notes alhora: mi-si, fa♯-re, sol-re. Mà quieta.",
             0.3)],
        2: [('arriba', 300, 'DER', "Melodia més greu: sol, la, si. Al c. 11 puja a re.", 0.5)],
        3: [('abajo', 500, 'OJO', "Doble barra després del c. 16: s'acaba l'estrofa. Respira!",
             0.97)],
        4: [('arriba', 262, 'DER', "La melodia puja: do agut repetit. El c. 19 arriba al re, la "
                                   "nota més aguda.", 0.35),
            ('abajo', 262, 'IZQ', "Parelles noves: la-mi (c. 17), fa♯-re (c. 18).", 0.2)],
        6: [('arriba', 300, 'DER', "Sol repetit quatre vegades; després baixa: fa♯, mi.", 0.3)],
        8: [('arriba', 300, 'OJO', "Frases curtes amb silencis: compta'ls i no correguis!",
             0.3)],
        9: [('abajo', 300, 'AMB', "Un si de set temps: rodona i blanca amb puntet lligades. "
                                  "Esquerra: negres i corxeres.", 0.6)],
        10: [('arriba', 300, 'AMB', "Torna la pujada dels cc. 17-20. Ja la saps!", 0.4)],
        11: [('abajo', 300, 'OJO', "C. 46: canvia el final: sol repetit, re i si llarg. Compte!",
              0.7)],
        13: [('arriba', 300, 'AMB', "Final: mi repetit i un si llarg; mi-si a l'esquerra.",
              0.5)],
    },
    marcas=[],
    pie_pauta="la clau la poses tu · copia un compàs o escriu l'escala de Sol major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_shallow.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
