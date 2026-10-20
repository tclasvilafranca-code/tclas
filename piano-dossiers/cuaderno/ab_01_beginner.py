# -*- coding: utf-8 -*-
"""Peça 1 · The Beginner (Le Début, Der Anfänger), Cornelius Gurlitt, op. 211 n.º 3, a quatre mans.
   MESURAT sobre el PDF de Drive (1 pàgina A4, vectorial; 16 compassos en 2 sistemes de 8): sense
   armadura (Do major), 3/4, «Allegretto» (sense metrònom), sense repeticions. Corxera com a figura
   més curta (c. 3, 6, 11 i 14; cap semicorxera). PRIMO: dues pautes de clau de sol amb la mateixa
   melodia (Do-Re-Mi-Fa-Sol, només 5 notes); la de dalt porta «8» amb línia de punts (una octava més
   amunt); mf al c. 1, crescendo al c. 1 i diminuendo al c. 2 (també cc. 9-10). SECONDO: clau de sol
   (silenci de negra, una nota i un acord de dues notes lligats, a cada compàs) i clau de fa (una
   blanca amb puntet per compàs); p als cc. 1 i 9. Única alteració: un Fa♯ al Secondo (c. 6). Els cc.
   9-12 repeteixen els cc. 1-4; lligadura de frase als cc. 7-8 i 8-9 i lligadura de valor Fa-Fa als cc.
   14-15. Final amb Sol (c. 15) cap a Do major (c. 16).
   El PDF original té 2 sistemes de 8 compassos: es recol·loca en 4 files de 4 (vectorial, sense tocar
   cap nota) perquè cada bloc sigui una fila: veure preparar()."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
import pymupdf

STAVES1 = (214.22, 266.72, 341.73, 394.23)           # línia superior de les 4 pautes, sistema 1


def preparar(origen, destino):
    """Recol·loca els 2 sistemes de 8 compassos en 4 files de 4 (vectorial, sense reescalar) i
       acosta el Secondo al Primo (la línia de connexió es manté contínua)."""
    if not os.path.exists(origen):
        return
    src = pymupdf.open(origen)
    out = pymupdf.open()
    PW, RH, GAPR, ACOSTA = 520.0, 219.0, 14.0, 24.0
    pg = out.new_page(width=PW, height=40 + 4 * (RH + GAPR) + 40)
    BR = 66.0
    R = pymupdf.Rect
    sh = BR - 89.7

    def put(x0, y0, x1, y1, dx, dy):
        pg.show_pdf_page(R(x0 + dx, y0 + dy, x1 + dx, y1 + dy), src, 0, clip=R(x0, y0, x1, y1))

    def doble(x0, x1, dx, top, o):
        """Primo (part de dalt) i Secondo (part de baix, acostat) d'una columna x0-x1."""
        dy = top - (195.0 + o)
        put(x0, 195.0 + o, x1, 300.0 + o, dx, dy)
        put(x0, 312.0 + o, x1, 438.0 + o, dx, dy - ACOSTA)

    def gap(x0, x1, top, o, base):
        for k, y0 in enumerate(STAVES1):
            dy = top - (195.0 + o) - (ACOSTA if k >= 2 else 0)
            for j in range(5):
                y = y0 + o * (300.02 / 295.0) + 5 * j + dy
                pg.draw_line((x0, y), (x1, y), color=(0, 0, 0), width=0.4)

    for i in range(4):
        top = 40 + i * (RH + GAPR)
        s2 = i >= 2
        o = 295.0 if s2 else 0.0
        dye = top - 195.0
        put(41, 240, 84, 260, sh, dye)                       # etiqueta Primo
        put(27, 368, 84, 388, sh, dye - ACOSTA)              # etiqueta Secondo
        if i == 0:
            doble(88, 346, sh, top, 0.0)                     # claus, compàs i cc. 1-4
        elif i == 1:
            doble(88, 116.5, sh, top, 0.0)                   # clau + claus
            xg = 88 + sh + (116.5 - 88)
            gap(xg, xg + 8, top, 0.0, 0)
            doble(346.3, 568, xg + 8 - 346.3, top, 0.0)      # cc. 5-8
            put(135.2, 197, 146.4, 209.5, xg + 0.5 - 135.2, dye)      # el «8»
            pg.insert_text((xg - 10, top + 6), '5', fontname='tiro', fontsize=8)
        elif i == 2:
            doble(29, 310, BR - 30.4, top, o)                # sistema 2, cc. 9-12
        else:
            dx = BR - 30.4
            dy = top - (195.0 + o)
            put(29, 507, 54.3, 300.0 + o, dx, dy)
            put(29, 312.0 + o, 54.3, 438.0 + o, dx, dy - ACOSTA)
            xg = 54.3 + dx
            gap(xg, xg + 8, top, o, 0)
            doble(310.7, 568, xg + 8 - 310.7, top, o)        # cc. 13-16
            put(135.2, 197, 146.4, 209.5, xg + 0.5 - 135.2, dye)
            pg.insert_text((xg - 14, top + 6), '13', fontname='tiro', fontsize=8)
    out.save(destino)


preparar(os.path.join(SRCDIR, 'the_beginer_4_manos.pdf'),
         os.path.join(SRCDIR, 'beginner_recto.pdf'))

SPEC = dict(
    num=1, slug='beginner', pdf='beginner_recto.pdf', time_sig=(3, 4),
    titulo='The Beginner',
    autor='Cornelius Gurlitt · op. 211, n.º 3 · a quatre mans (Primo i Secondo)',
    kicker='Abril · peça 1 · The Beginner', mes='Novembre · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=gurlitt+the+beginner+op+211+piano+four+hands',
    credito='Partitura: Gurlitt, The Beginner, op. 211 n.º 3 (free-scores.com), recol·locada en '
            'files de 4 compassos. Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '3/4'), ('Caràcter', 'Allegretto'),
               ('Figura curta', 'Corxera'), ('Compassos', '16')],
        total=16,
        secciones=[('A', 1, 4, 'El tema', AZUL), ('B', 5, 8, 'Segona frase', OCRE),
                   ('A', 9, 12, 'Torna el tema', AZUL), ('C', 13, 16, 'Cap a casa', OCRE)],
        ideas=[('EL PRIMO', 'Cinc notes: Do-Sol',
                'Dues pautes amb la mateixa melodia. Només Do, Re, Mi, Fa i Sol.'),
               ('EL SECONDO', 'Nota, acord i baix',
                'A dalt, una nota i un acord a cada compàs. A baix, una nota llarga.'),
               ('EL POLS', 'Tres temps: 1-2-3',
                'Cada compàs té tres temps. Compteu-los junts, en veu alta.'),
               ('EL FINAL', 'Dominant → tònica',
                'El c. 15 (Sol) porta al c. 16 (Do major): sona a final.')],
        ideas_titulo='La peça en quatre idees',
        especial=[
            "Sense armadura: Do major. L'única alteració és un Fa♯ al Secondo (c. 6).",
            'Compàs de 3/4: tres negres per compàs. Surt «Allegretto»: animat, sense córrer.',
            "A quatre mans: tu pots fer el Primo (la melodia) i l'altra persona, el Secondo.",
            'Primo: dues pautes amb la mateixa melodia. El «8» de dalt vol dir una octava més '
            'amunt.',
            'Matisos: mf (mig fort) al Primo i p (suau) al Secondo. Crescendo al c. 1 i '
            'diminuendo al c. 2 (també als cc. 9-10).',
            'No hi ha repeticions: 16 compassos seguits. Els cc. 9-12 són com els cc. 1-4.'],
        reto="Toqueu els 16 compassos sense aturar-vos, començant i acabant junts. "
             "Us en sortireu?",
        truco="Compteu «1-2-3» en veu alta i entreu a l'hora. Escolta l'altra part mentre "
              "toques.",
        sabias="Cornelius Gurlitt (1820-1901) va ser un compositor alemany i va escriure moltes "
               "peces per ensenyar piano. El títol surt en anglès, francès i alemany: The "
               "Beginner, Le Début, Der Anfänger.",
        qr_texto='Escolta-la i compta 1-2-3 amb la partitura al davant.',
        ts=(3, 4),
        cuenta_titulo='Com es compten el c. 3 i el c. 1',
        cuenta_pie="Primo (c. 3): negra amb puntet, corxera i negra: «1, 2-i, 3». Secondo (c. 1): "
                   "silenci al 1, una nota al 2 i un acord al 3.",
        ritmos=[('PRIMO', 'c. 3 · «1, 2-i, 3»',
                 [{'pitch': 'E5', 'dur': 'q.'}, {'pitch': 'D5', 'dur': 'e'},
                  {'pitch': 'C5', 'dur': 'q'}], AZUL, 'treble', None),
                ('SECONDO', 'c. 1 · silenci, nota, acord',
                 [{'rest': True, 'dur': 'q'}, {'pitch': 'G3', 'dur': 'q'},
                  {'pitches': ['C4', 'E4'], 'dur': 'q'}], OCRE, 'treble', None)]),
    manos=dict(
        titulo='Les dues mans del Primo',
        sub="Primer cada mà sola. Després les dues juntes i, al final, amb l'altra persona.",
        tit_izq='MÀ ESQUERRA', tit_der='MÀ DRETA',
        izq=[('Cinc tecles, un dit per tecla', 'Troba el Do central i puja fins al Do següent. '
                                               'Posa la mà de Do a Sol.'),
             ('Una nota, un temps', 'Cc. 1-3: Mi-Mi-Mi. Una nota a cada temps. Compta 1-2-3.'),
             ('Blanca i negra', 'C. 2: Sol (blanca, 2 temps) i Fa (negra, 1 temps). '
                                'Compta 1-2 i 3.'),
             ('Un Re llarg', 'Al c. 4, Re de tres temps: prem-lo i aguanta fins a 3.')],
        der=[('La mateixa melodia', "Igual que l'esquerra, una octava més amunt (el «8» de "
                                    "la pauta de dalt)."),
             ('Troba el Do', "Posa la mà una octava més amunt que l'esquerra: de Do a Sol, un "
                             "dit per tecla."),
             ('Punt i corxera', 'C. 3: Mi (negra amb puntet), Re (corxera) i Do. Digues «1, '
                                '2-i, 3».'),
             ('Les lligadures', "Cc. 7-8: Re, Sol i Fa, lligats. Toca'ls sense talls, com si "
                                "cantessis.")],
        tecnica=['Canell solt i espatlles baixes.',
                 'Dits corbats, com si tinguessis una pilota petita a la mà.',
                 "Compta 1-2-3 en veu alta i no t'aturis si t'equivoques: continua."]),
    bloques=[
        B(1, 'cc. 1-4', 'La primera frase', (0, 0),
          D('fichas', 'Les cinc notes del Primo', ['Do', 'Re', 'Mi', 'Fa', 'Sol']),
          [('IZQUIERDA', 'Mi-Mi-Mi, Sol-Fa, Mi-Re-Do i Re llarg. Compta 1-2-3.'),
           ('DERECHA', 'La mateixa melodia, una octava més amunt (el «8»).'),
           ('JUNTAS', 'Les dues mans alhora, en octaves. Un compàs cada cop.'),
           ('A TEMPO', 'Amb el Secondo: compteu 1-2-3 i entreu junts, suaus.')]),
        B(2, 'cc. 5-8', 'La segona frase', (1, 1),
          D('cadena', 'El camí del bloc',
            [('c. 5: Do Do Do', False), ('c. 6: Do Mi Re', False), ('cc. 7-8: lligats', True)]),
          [('IZQUIERDA', 'C. 5: Do-Do-Do. C. 6: Do, Mi, Re. Cc. 7-8: Re, Sol, Fa.'),
           ('DERECHA', 'Igual, una octava més amunt. Lliga el Re del c. 7 amb el Sol.'),
           ('JUNTAS', 'De dos en dos compassos: 5-6 i 7-8. Sense córrer.'),
           ('OJO', 'Una lligadura és una línia corba: toca les notes sense tallar el so.')]),
        B(3, 'cc. 9-12', 'Torna el tema', (2, 2),
          D('cadena', 'Una música coneguda',
            [('cc. 1-4', False), ('igual', False), ('cc. 9-12', True)]),
          [('IZQUIERDA', 'És la música dels cc. 1-4. Toca-la de memòria!'),
           ('DERECHA', 'Igual que els cc. 1-4. El c. 9 comença lligat al Fa del c. 8.'),
           ('JUNTAS', 'Cc. 9-12 amb les dues mans. Un compàs cada cop, si cal.'),
           ('A TEMPO', 'Amb el Secondo: crescendo al c. 9 i diminuendo al c. 10.')]),
        B(4, 'cc. 13-16', 'Cap a casa', (3, 3),
          D('cadena', 'Baixant cap al Do',
            [('Fa', False), ('Mi', False), ('Re', False), ('Do: FINAL', True)]),
          [('IZQUIERDA', 'C. 13: Do-Do-Do. C. 14: Re, Mi, Fa. C. 15: Fa, Mi, Re. C. 16: Do.'),
           ('DERECHA', 'Igual, una octava més amunt. El Fa dels cc. 14-15 és una sola nota.'),
           ('JUNTAS', 'Cc. 15-16 en bucle: baixen Fa-Mi-Re i arriben al Do.'),
           ('OJO', "Final: Do de 3 temps. Aguanta'l i deixeu anar tots dos a l'hora.")]),
        B(5, 'cc. 1-8', 'La primera meitat', (0, 1),
          D('cadena', 'Dos blocs seguits', [('bloc 1', False), ('bloc 2', True)]),
          [('IZQUIERDA', 'Els dos blocs seguits, de memòria.'),
           ('DERECHA', 'Els dos blocs seguits, sense mirar les mans.'),
           ('JUNTAS', 'Del c. 1 al c. 8 sense parar, amb les dues mans.'),
           ('A TEMPO', 'Amb el Secondo: Primo mf i Secondo p.')]),
        B(6, 'cc. 9-16', 'La segona meitat', (2, 3),
          D('cadena', 'Dos blocs seguits', [('bloc 3', False), ('bloc 4', True)]),
          [('IZQUIERDA', 'Del c. 9 al c. 16, de memòria.'),
           ('DERECHA', 'Del c. 9 al c. 16, sense mirar les mans.'),
           ('JUNTAS', "Les dues mans, sense parar fins al Do final."),
           ('OJO', 'Compta els tres temps del Do final abans de deixar-lo anar.')]),
        B(7, 'cc. 1-16', 'Tota la peça', (0, 3),
          D('cadena', 'Tota la peça',
            [('tema', False), ('frase', False), ('tema', False), ('final', True)]),
          [('IZQUIERDA', "Repte: tota la peça només amb l'esquerra."),
           ('DERECHA', 'Ara sencera només amb la dreta, sense parar.'),
           ('JUNTAS', 'Sencera amb les dues mans, a pas tranquil.'),
           ('A TEMPO', 'Sencera amb el Secondo: compteu 1-2-3 i acabeu junts.')]),
    ],
    sub_guia="Cada bloc: mà esquerra, mà dreta, les dues juntes i amb l'altra persona.",
    lista=['Toco la melodia amb la dreta, de memòria.',
           "Toco la melodia amb l'esquerra, de memòria.",
           'Compto 1-2-3 en veu alta i entro a temps.',
           "Toco els 16 compassos amb l'altra persona, sense parar.",
           "La gravo amb el mòbil i me l'escolto."],
    cortes={1: [266.0, 499.0, 732.0]},
    burb={
        0: [('arriba', 262, 'DER', 'Pauta de dalt: mà dreta. El «8» i la línia de punts diuen: '
                                   'una octava més amunt.', 150),
            ('arriba', 262, 'IZQ', 'Pauta de baix: mà esquerra, la mateixa melodia: Mi-Mi-Mi, '
                                   'Sol-Fa.', 150),
            ('abajo', 262, 'SEC', "Silenci, una nota i un acord, i una nota llarga a baix. "
                                  'Tot suau (p).', 120),
            ('abajo', 262, 'AMB', 'Primo mf (mig fort), Secondo p (suau). Les cunyes: crescendo '
                                  'al c. 1 i diminuendo al c. 2.', 190)],
        1: [('arriba', 262, 'OJO', 'Lligadures! Cc. 7-8: Re, Sol i Fa van lligats. Toca sense '
                                   'tallar el so.', 285),
            ('abajo', 262, 'PRIMO', 'C. 6: Do amb puntet, Mi i Re. Compta 1, 2-i, 3.', 190),
            ('abajo', 262, 'SEC', "C. 6: hi surt un Fa♯, la tecla negra que va just després del "
                                  'Fa. Només en aquest compàs.', 202)],
        2: [('arriba', 262, 'AMB', "Torna el tema dels cc. 1-4. Crescendo al c. 9 i diminuendo al "
                                   'c. 10, i el Secondo en p.', 130),
            ('abajo', 262, 'DER', 'El Mi del c. 9 va lligat al Fa del c. 8: la frase no es talla.',
             90)],
        3: [('arriba', 262, 'PRIMO', 'Cc. 14-15: Re, Mi, Fa i Fa, Mi, Re. Els dos Fa lligats són '
                                     'una sola nota de 2 temps.', 200),
            ('abajo', 262, 'AMB', 'Cc. 15-16: Sol (dominant) → Do major (tònica). Sona a final!',
             280),
            ('abajo', 262, 'OJO', "Final: Do de 3 temps. Aguanteu i deixeu anar junts. Molt "
                                  'bé!', 330)],
    },
    misol=dict(
        manos="Un dit per tecla i un temps per nota. Si vas a poc a poc, sonarà bé. Compta "
              "sempre en veu alta!",
        guia="Cada bloc és com un nivell d'un joc: no passis al següent fins que et surti tres "
             "cops seguits!",
        pauta="Escriu aquí Do, Re, Mi, Fa i Sol. Després inventa una melodia curta amb aquestes "
              "cinc notes!"),
    marcas=[],
    pie_pauta='la clau la poses tu · escriu Do-Re-Mi-Fa-Sol i inventa una melodia')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_beginner.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
