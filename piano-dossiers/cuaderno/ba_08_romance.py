# -*- coding: utf-8 -*-
"""Peça 8 · Romance (Diabelli, op. 163 n.º 1, mov. 2), a quatre mans. MESURAT sobre el PDF de
   free-scores (2 pàgines A4, 24 compassos en 6 sistemes de 4): sense armadura i en LA MENOR (el
   Secondo comença en La, passa per Sol♯ i Mi i acaba en un acord La-Do-Mi amb calderó), 2/2 (¢),
   Andantino sense metrònom, Primo en dues files (la de dalt, per a cinc dits, amb 8va), barra de
   repetició al final del c. 8, notes d'adorn (cc. 3, 7, 19, 20, 21), matisos p dolce, sf, cresc.,
   f, p, mf, mp, p, pp i calderó final; semicorxera."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_c = lambda n: {'pitch': 'B4', 'dur': 'e', 'beam': n // 4}
SPEC = dict(
    num=8, slug='romance', pdf='romance_4_manos.pdf', time_sig=(2, 2),
    titulo="Romance", autor="Anton Diabelli · op. 163 n.º 1, 2n mov. · a quatre mans",
    kicker="Alba · peça 8 · Romance (Diabelli)", mes='Març · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=diabelli+romance+op+163+piano+4+hands',
    credito="Partitura: A. Diabelli, op. 163 n.º 1 (free-scores.com). Anotacions: T-Clas.",
    ficha=FICHA(
        datos=[("Tonalitat", "La menor"), ("Compàs", "2/2 (¢)"), ("Caràcter", "Andantino"),
               ("Figura curta", "Semicorxera"), ("Compassos", "24")],
        total=24,
        secciones=[("A", 1, 8, "Primera part (es repeteix)", AZUL),
                   ("B", 9, 16, "Cresc. i f", OCRE),
                   ("C", 17, 24, "mf → pp i calderó", AZUL)],
        ideas_titulo="La peça en quatre idees",
        ideas=[("PRIMO", "La melodia, a dalt",
                "Notes llargues lligades i alguna noteta d'adorn. Va amb 8va: sona una octava més "
                "aguda del que està escrit."),
               ("SECONDO", "Corxeres i baix",
                "A baix hi ha una nota llarga i, a sobre, vuit corxeres per compàs que pugen i "
                "baixen suaus i lligades."),
               ("L'HARMONIA", "La menor → Mi → La",
                "Als cc. 1-4: La menor, Mi amb sèptima (dominant) i torna a La menor. "
                "Dominant → tònica."),
               ("ELS MATISOS", "p dolce → f → pp",
                "Comença suau i dolç, creix fins a la f i acaba en pp amb un calderó.")],
        especial=[
            "Posa «Andantino» (pas tranquil) i «p dolce»: suau i dolç. No porta metrònom.",
            "El compàs és 2/2 (¢): dos temps per compàs, cadascun de blanca.",
            "És a quatre mans: Primo a dalt i Secondo a baix.",
            "El Primo ve en dues files: la de dalt és la versió per a cinc dits.",
            "Els cc. 1-8 es toquen dues vegades (barra de repetició al c. 8).",
            "Hi ha notes d'adorn (notetes petites) als cc. 3, 7, 19, 20 i 21, i un calderó al "
            "final."],
        reto="Tocar a dues com si fóssiu una sola persona: respirar juntes, créixer juntes al "
             "cresc. i entrar juntes després de cada nota llarga!",
        truco="Abans de començar, compteu en veu alta «un-dos» les dues i mireu la primera nota "
              "de l'altra. Al final de cada frase, respireu a l'hora.",
        sabias="Anton Diabelli (1781-1858) va ser editor de música a Viena. Beethoven va escriure "
               "les seves 33 variacions, op. 120, sobre un vals seu. Aquesta peça és d'una de les "
               "seves sis sonates a quatre mans, op. 163.",
        qr_texto="Escolta-la i fixa't en com el Secondo sosté el Primo.", ts=(2, 2),
        cuenta_titulo="Com es compta el 2/2",
        cuenta_pie="Un compàs de 2/2: dos temps de blanca, cadascun amb quatre corxeres. Aquí "
                   "només el ritme, sobre una nota qualsevol.",
        ritmos=[("EL COMPTE", "2/2 · dos temps", [_c(i) for i in range(8)], OCRE, 'treble',
                 None)]),
    manos=dict(
        titulo="Secondo i Primo",
        sub="Cada part s'aprèn sola. Després us canvieu de part i toqueu juntes, a poc a poc.",
        tit_izq="SECONDO · la part greu", tit_der="PRIMO · la part aguda",
        izq=[("El baix, primer", "A baix hi ha notes llargues (rodones i blanques). Toca només "
                                 "aquesta línia comptant «un-dos» per compàs."),
             ("Les corxeres que roden", "A sobre, vuit corxeres per compàs, lligades i suaus. "
                                        "Estudia-les soles, a poc a poc i ben regulars."),
             ("Les dues línies juntes", "Quan cada línia et surti sola, ajunta-les: les corxeres "
                                        "a sobre de la nota llarga."),
             ("Matisos", "Comença p dolce i «sempre legato» (tot lligat). Al c. 7 arriba la f: "
                         "no perdis la qualitat del so.")],
        der=[("Cantar la melodia", "La melodia va en blanques i negres amb lligadures. "
                                   "Canta-la per dins abans de tocar-la."),
             ("Els adorns", "Als cc. 3 i 7 hi ha una notica petita enganxada a la principal: "
                            "ràpida i lleugera, just abans del pols."),
             ("El 8va", "Tot el Primo va amb 8va: llegeixes el que hi ha escrit, però sona una "
                        "octava més aguda."),
             ("Amb el Secondo", "Toqueu juntes a poc a poc. El Primo escolta el Secondo: la "
                                "melodia canta sobre l'acompanyament.")],
        tecnica=["Braços solts i esquena recta: dues persones en un banc necessiten lloc.",
                 "Compteu en veu alta «un-dos» abans de començar, juntes.",
                 "Canvieu de part: així s'aprenen les dues."]),
    misol=dict(
        manos="A quatre mans, qui escolta mana! Mira la mà de l'altra i respireu juntes: "
              "sonareu com una sola persona.",
        guia="Primer cadascuna la seva part, després canvieu: així entens què fa l'altra i us "
             "ajunteu molt millor!",
        pauta="Copia el c. 1 del Secondo (vuit corxeres) o inventa un compàs en La menor. "
              "Ensenya'l a la profe!"),
    bloques=[
        B(1, 'cc. 1-4', "La frase d'entrada", (0, 0),
          D('capas', "Tres capes a la vegada (un compàs)",
            [("Primo: melodia", 'barras', AZUL), ("Secondo: corxeres", 'puntos', OCRE, 8),
             ("Secondo: baix", 'barras', OCRE)]),
          [('SECONDO', "Baix llarg i vuit corxeres per compàs, p dolce i tot lligat."),
           ('PRIMO', "La melodia, en p dolce. Notes llargues: compta-les senceres."),
           ('JUNTAS', "Comenceu a l'hora i respireu juntes al final del c. 4."),
           ('OJO', "Al c. 3 hi ha una noteta d'adorn: lleugera i enganxada.")]),
        B(2, 'cc. 5-8', "Es repeteix: dolce → f", (1, 1),
          D('cadena', "El recorregut",
            [("cc. 1-8", False), ("repeteix", False), ("després cc. 9-24", True)]),
          [('SECONDO', "Cresc.: més so a poc a poc fins a la f del c. 7."),
           ('PRIMO', "Al c. 7, f i una noteta d'adorn abans de la nota principal."),
           ('JUNTAS', "Cc. 5-8 i la barra de repetició: torneu al c. 1!"),
           ('OJO', "La barra del final del c. 8 mana tornar al principi. No te la saltis!")]),
        B(3, 'cc. 9-12', "Torna en p i creix", (2, 2),
          D('cadena', "Els matisos", [("p", False), ("cresc.", False), ("més so", True)]),
          [('SECONDO', "Torna el p. Al c. 10 comença el cresc."),
           ('PRIMO', "Ritme com el dels cc. 1-4, però amb notes diferents: llegeix-la amb "
                     "compte."),
           ('JUNTAS', "Dos compassos cada cop i després els quatre."),
           ('OJO', "El cresc. és a poc a poc: no arribis a la f abans d'hora!")]),
        B(4, 'cc. 13-16', "Cresc. i f", (3, 3),
          D('cadena', "De fort a suau", [("cresc.", False), ("f", True), ("p", False)]),
          [('SECONDO', "f al c. 15 i p al c. 16: el canvi és de cop."),
           ('PRIMO', "Cresc. fins a la f (c. 15). Al c. 16, una nota llarga i un silenci."),
           ('JUNTAS', "Toqueu en bucle el c. 15 i el c. 16: de la f a la p."),
           ('OJO', "Compte amb els si: si♭ al c. 14 i bequadre (♮) al c. 15!")]),
        B(5, 'cc. 17-20', "So mitjà", (4, 4),
          D('cadena', "Els matisos", [("mf", True), ("mp", False)]),
          [('SECONDO', "mf: so mig-fort; al c. 20 baixa a mp."),
           ('PRIMO', "Notes d'adorn als cc. 19 i 20: lleugeres."),
           ('JUNTAS', "Dos compassos cada cop, amb el matís."),
           ('OJO', "Els reguladors (< >) pugen i baixen el so dins del compàs. Fes-los "
                   "petits!")]),
        B(6, 'cc. 21-24', "Final: p, pp i calderó", (5, 5),
          D('cadena', "El final", [("p", False), ("pp", False), ("calderó", True)]),
          [('SECONDO', "Cc. 22-23: baix, silenci, acord, silenci. L'últim compàs, acord llarg."),
           ('PRIMO', "L'últim compàs és una nota llarga amb calderó."),
           ('JUNTAS', "Mireu-vos per deixar anar l'últim acord a l'hora."),
           ('A TEMPO', "Toqueu tota la peça, amb la repetició, sense parar.")]),
    ],
    cortes={1: [324.8, 574.8], 2: [299.5, 547.0]}, corte_titulo=105.2,
    fin={1: 798, 2: 798},
    burb={
        0: [('arriba', 330, 'AMB', "Andantino, p dolce: tranquil·la i dolça. El compàs és 2/2: "
                                   "compta un temps per blanca.", 0.2),
            ('abajo', 300, 'SEC', "Vuit corxeres per compàs sobre una nota llarga, lligat i "
                                  "suau.", 0.3)],
        1: [('arriba', 470, 'OJO', "Psst! La barra de repetició del c. 8 mana tornar al c. 1: "
                                   "toqueu dues vegades els cc. 1-8.", 0.95),
            ('abajo', 300, 'PRIMO', "La noteta petita del c. 7 (adorn) va enganxada a la "
                                    "principal: lleugera.", 0.6)],
        2: [('arriba', 300, 'AMB', "p i, des del c. 10, cresc.: més so a poc a poc.", 0.5)],
        3: [('arriba', 330, 'OJO', "f al c. 15 i p al c. 16: el canvi és de cop, no a poc a "
                                   "poc!", 0.65)],
        4: [('arriba', 300, 'AMB', "mf als cc. 17 i 19, i mp al c. 20.", 0.5)],
        5: [('arriba', 470, 'OJO', "p, pp i calderó: l'últim acord s'allarga i s'apaga sol.",
             0.9)],
    },
    marcas=[],
    pie_pauta="la clau la poses tu · copia un compàs o escriu l'escala de La menor")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ba_romance.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
