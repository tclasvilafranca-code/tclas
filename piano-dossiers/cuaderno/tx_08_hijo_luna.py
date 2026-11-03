# -*- coding: utf-8 -*-
"""Peça 8 · Hijo de la Luna (Mecano), versio facil, arranjament d'Unai Karam. MESURAT sobre el PDF
   (3 pagines A4 APAISADES, vectorial; 34 compassos en 8 sistemes de 4, 4, 4, 4, 4, 4, 5 i 5):
   un bemoll (Si b) i acaba en acord de Re menor, 6/8, «negra amb puntet = 58», sense matisos,
   sense repeticions (totes les barres son simples; l'ultima, doble final), semicorxera com a
   figura mes curta (+ un tresillo de semicorxeres al c. 29), dits impresos nomes en alguns
   compassos (1, 5, 9-12, 17, 19-20, 29). Esquerra: negres amb puntet (cc. 1-16 i 30-33), octaves
   La-Sol/Fa-Mi als cc. 17-24 i octaves que baixen als cc. 27-29 (Mi, Re, Do, Si becaire, Si b, La);
   acord arpegiat final (Re2-La2-Re3 / Fa3-La3-Re4). Alteracions: La b (cc. 18, 22, 25), Si becaire
   (cc. 18-19, 22-23, 27-28), Sol # (cc. 27-28). Els cc. 13-16 repeteixen els cc. 9-12 i els
   cc. 30-33, els cc. 1-4. La pagina es gira a vertical retallant marges (_preparar), sense tocar
   cap nota (vectorial)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403


def _preparar(origen, destino, x0=36.0, x1=803.0):
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


_preparar(os.path.join(SRCDIR, 'hijo_de_la_luna_mecano.pdf'),
          os.path.join(SRCDIR, 'hijo_luna_recto.pdf'))

_DER_C1 = [{'rest': True, 'dur': 'e'}, {'pitch': 'A4', 'dur': 'e', 'beam': 0},
           {'pitch': 'G4', 'dur': 'e', 'beam': 0}, {'rest': True, 'dur': 'e'},
           {'pitch': 'E4', 'dur': 'e', 'beam': 1}, {'pitch': 'D4', 'dur': 'e', 'beam': 1}]
_IZQ_C1 = [{'pitch': 'D3', 'dur': 'q.'}, {'pitch': 'C3', 'dur': 'q.'}]

SPEC = dict(
    num=8, slug='hijo_luna', pdf='hijo_luna_recto.pdf', time_sig=(6, 8),
    titulo='Hijo de la Luna',
    autor="Mecano · versió fàcil · arranjament d'Unai Karam",
    kicker='Txell · peça 8 · Hijo de la Luna', mes='Març · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=mecano+hijo+de+la+luna+piano+easy',
    credito="Partitura: «Hijo de la Luna (easy)», arr. Unai Karam (còpia de Drive), girada. "
            "Anotacions: T-Clas.",
    ficha=FICHA(
        datos=[('Tonalitat', 'Re menor'), ('Compàs', '6/8'), ('Tempo', '♩. = 58'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '34')],
        total=34,
        secciones=[('A', 1, 4, 'Intro', AZUL), ('B', 5, 8, 'Ràpides', OCRE),
                   ('C', 9, 16, 'La frase puja', AZUL), ('D', 17, 24, 'Octaves', OCRE),
                   ('E', 25, 29, 'El pont', AZUL), ('F', 30, 34, 'Final', OCRE)],
        ideas_titulo='La peça en quatre idees',
        ideas=[('LA DRETA', 'Silenci, nota, nota',
                'Un dibuix de corxeres que torna sempre. Des del c. 5 hi ha semicorxeres.'),
               ("L'ESQUERRA", 'Notes llargues i octaves',
                'Una negra amb puntet per temps. Als cc. 17-24 sonen dues notes iguals alhora.'),
               ('LES ALTERACIONS', 'Si♮, La♭ i Sol♯',
                'Només als cc. 18-19, 22-23 i 25-28. Van sempre amb el seu signe.'),
               ('EL FINAL', 'Acord arpegiat',
                "L'últim compàs és un acord de Re menor amb una línia ondulada.")],
        ideas_pie='Negra amb puntet = 58: un pols per cada grup de tres corxeres.',
        especial=[
            "Armadura d'un bemoll (Si♭). La peça acaba en acord de Re menor.",
            'Compàs de 6/8: dos grups de tres corxeres. Tempo: negra amb puntet = 58.',
            'La partitura porta alguns dits impresos (cc. 1, 5, 9-12, 17, 19-20 i 29).',
            "Cc. 17-29: l'esquerra toca sovint dues notes iguals alhora (octava).",
            'Alteracions: La♭ (cc. 18, 22 i 25), Si♮ (cc. 18-19, 22-23 i 27-28) i Sol♯ (cc. 27-28).',
            'Al c. 29, tres semicorxeres en el temps d\'una corxera (tresillo).',
            'No hi ha matisos ni repeticions: 34 compassos seguits.'],
        reto="Que les octaves de l'esquerra (cc. 17-24) no et facin perdre el pols de la dreta. "
             "T'hi atreveixes?",
        truco="Reconeix els dibuixos que tornen: cc. 13-16 = cc. 9-12 i cc. 30-33 = cc. 1-4. "
              'Aprendràs menys del que sembla!',
        sabias="«Hijo de la Luna» és de Mecano (1986, àlbum «Entre el cielo y el suelo») i la va "
               'escriure José María Cano. La lletra explica una llegenda: la Lluna cria un nen '
               'de pell molt blanca.',
        qr_texto='Escolta-la i compta «1-2-3, 4-5-6» amb la partitura al davant.',
        ts=(6, 8), cuenta_titulo='Com es compta el c. 1',
        cuenta_pie="Compta 1-2-3, 4-5-6. Dreta: silenci a l'1, La-Sol al 2-3, silenci al 4, Mi-Re "
                   'al 5-6. Esquerra: dues notes llargues.',
        ritmos=[('LA DRETA', 'c. 1 · silenci, nota, nota', _DER_C1, AZUL, 'treble', 'Re menor'),
                ("L'ESQUERRA", 'c. 1 · dues negres amb puntet', _IZQ_C1, OCRE, 'bass',
                 'Re menor')]),
    manos=dict(
        izq=[('Dues notes llargues', 'Cc. 1-16: una negra amb puntet per temps. Re-Do, Si♭-Do. '
                                     'Compta 1-2-3, 4-5-6.'),
             ('Octaves', 'Cc. 17-24: dues notes iguals alhora, La-Sol i Fa-Mi. Prem-les juntes.'),
             ('Baixa de pas', 'Cc. 27-29: Mi, Re, Do, Si♮, Si♭, La. Algunes van sota la pauta, '
                              'amb ratlletes.'),
             ("L'acord final", 'C. 34: Re, La i Re, tocades de baix a dalt i aguantades.')],
        der=[('Silenci, nota, nota', 'Cc. 1-4: silenci, La-Sol, silenci, Mi-Re. Compta 1-2-3, '
                                     '4-5-6.'),
             ('Semicorxeres', 'Cc. 5 i 7: Re-Mi-Fa-La, quatre notes en el temps de dues corxeres. '
                              'Totes iguals.'),
             ('Alteracions', 'Cc. 18-19, 22-23 i 27-28: Si♮, La♭ i Sol♯. Mira el signe abans de '
                             'tocar.'),
             ('Notes de sota', "Als cc. 11 i 15 la mà baixa fins al La i al Do central, amb "
                               "ratlletes.")],
        tecnica=['Canell solt: les semicorxeres sonen lleugeres i iguals.',
                 "Compta 1-2-3, 4-5-6 en veu alta: l'esquerra marca el pols.",
                 'Pols de 58: comença molt més lenta i puja a poc a poc.']),
    bloques=[
        B(1, 'cc. 1-4', 'El motiu del principi', (0, 0),
          D('cuenta', 'Un compàs de 6/8: dos grups de tres', [('compta', 2, 3)]),
          [('IZQUIERDA', 'Dues negres amb puntet per compàs: Re-Do i Si♭-Do.'),
           ('DERECHA', 'C. 1: silenci, La, Sol, silenci, Mi, Re. C. 2: silenci, Fa, Sol, '
                       'silenci, Mi, Re.'),
           ('JUNTAS', 'Compta 1-2-3, 4-5-6. Un compàs cada cop i després de dos en dos.'),
           ('OJO', 'Pols: negra amb puntet = 58. Comença molt més lenta!')]),
        B(2, 'cc. 5-8', 'Entren les semicorxeres', (1, 1),
          D('cadena', 'El c. 5, en ordre',
            [('silenci', False), ('4 semicorxeres', False), ('negra', False),
             ('corxera', True)]),
          [('IZQUIERDA', "Igual que els cc. 1-4: Re-Do, Si♭-Do. Ja la saps de memòria!"),
           ('DERECHA', 'Cc. 5 i 7: Re-Mi-Fa-La, Mi, Re. Cc. 6 i 8: Re-Mi, Fa-Sol (amb silencis).'),
           ('JUNTAS', 'Cc. 5-6 i després cc. 7-8: és el mateix, dues vegades.'),
           ('OJO', 'Semicorxeres: dues barres. Toca Re-Mi-Fa-La a poc a poc, totes iguals.')]),
        B(3, 'cc. 9-16', 'La frase que puja', (2, 3),
          D('cadena', 'La mateixa frase, dues vegades',
            [('cc. 9-12', False), ('igual', False), ('cc. 13-16', True)]),
          [('IZQUIERDA', 'Fa-Do, Re-La, Si♭-Do i Re amb silenci. Es repeteix als cc. 13-16.'),
           ('DERECHA', 'C. 9: silenci i Fa-Sol-La-Do. C. 10, com el c. 5. Cc. 11-12: baixa i '
                       'puja.'),
           ('JUNTAS', 'Frase a frase: cc. 9-10 i 11-12. Els cc. 13-16 són la mateixa música.'),
           ('OJO', 'Als cc. 11 i 15 la dreta baixa fins al La i al Do central, amb ratlletes.')]),
        B(4, 'cc. 17-24', 'Octaves a baix', (4, 5),
          D('cadena', "L'esquerra baixa de pas",
            [('La', False), ('Sol', False), ('Fa', False), ('Mi', True)]),
          [('IZQUIERDA', 'Octaves: dues notes iguals alhora. La-Sol, Fa-Mi, La-Sol, Fa-Mi.'),
           ('DERECHA', 'C. 17: silenci, La-La i Sol-Mi-Sol. Cc. 18-20: Si♮, La♭ i La♮.'),
           ('JUNTAS', "Cc. 17-20 d'una tirada. Els cc. 21-24 són iguals, però el c. 21 comença "
                      'amb Mi.'),
           ('OJO', 'Si♮ i La♭ als cc. 18 i 22. El La♮ del final va lligat al compàs següent.')]),
        B(5, 'cc. 25-29', 'El pont', (6, 6),
          D('cadena', "L'esquerra als cc. 27-29",
            [('Mi', False), ('Re', False), ('Do', False), ('Si♮', False), ('Si♭', False),
             ('La', True)]),
          [('IZQUIERDA', 'Cc. 25-26: una nota (La, La♭, La, Fa). Cc. 27-29: octaves que baixen.'),
           ('DERECHA', 'Cc. 25-26: Mi, Re, Do-Re. Cc. 27-28: silenci, Sol♯ i Si♮-Mi. C. 29: '
                       'puja.'),
           ('JUNTAS', 'Cc. 25-26, després els cc. 27-28 (iguals) i, al final, el c. 29.'),
           ('OJO', 'Sol♯ i Si♮ valen fins al final del compàs. Al c. 29, tresillo de '
                   'semicorxeres.')]),
        B(6, 'cc. 30-34', 'Torna el principi i final', (7, 7),
          D('cadena', 'Cap al final',
            [('cc. 30-33', False), ('acord de Re menor', True)]),
          [('IZQUIERDA', 'Cc. 30-33: Re-Do, Si♭-Do, com al principi. C. 34: Re, La, Re.'),
           ('DERECHA', 'C. 30: Re-La-Sol, sense silenci. Cc. 31-33 com abans (c. 33: Mi-Do).'),
           ('JUNTAS', "Els cc. 30-33 i, tot seguit, l'acord final."),
           ('OJO', 'Acord arpegiat (línia ondulada): de baix a dalt, de pressa, i aguanta.')]),
        B(7, 'cc. 1-34', 'Tota la peça', (0, 7),
          D('cadena', 'Els trossos',
            [('cc. 1-8', False), ('cc. 9-16', False), ('cc. 17-29', False),
             ('cc. 30-34', True)]),
          [('IZQUIERDA', "Tota l'esquerra de memòria: negres amb puntet i, al mig, octaves."),
           ('DERECHA', 'Tota la dreta, bloc a bloc, mirant els dits de la partitura.'),
           ('JUNTAS', 'Tres trossos: cc. 1-16, cc. 17-29 i cc. 30-34.'),
           ('A TEMPO', 'Negra amb puntet = 58. Sense repeticions i sense parar!')]),
    ],
    lista=['Toco de memòria el principi (cc. 1-8).',
           'Toco les semicorxeres a poc a poc i netes.',
           'Llegeixo bé Si♮, La♭ i Sol♯.',
           "Toco les octaves de l'esquerra (cc. 17-29) amb seguretat.",
           'Toco els 34 compassos seguits, a negra amb puntet = 58.'],
    cortes={1: [279.0, 412.5], 2: [177.8, 329.5], 3: [206.0]}, corte_titulo=134.5,
    fin={1: 545.0, 2: 478.0, 3: 350.0},
    burb={
        0: [('arriba', 265, 'DER', 'Silenci, La, Sol, silenci, Mi, Re. Compta 1-2-3, 4-5-6.',
             0.1),
            ('arriba', 265, 'IZQ', 'Dues negres amb puntet per compàs: Re-Do i Si♭-Do.', 0.6)],
        1: [('arriba', 300, 'OJO', 'Cc. 5 i 7: quatre semicorxeres (dues barres): Re-Mi-Fa-La. '
                                   'A poc a poc!', 0.25)],
        2: [('arriba', 265, 'DER', 'C. 9: silenci i Fa-Sol-La-Do. Al c. 11 la dreta baixa fins '
                                   'al La, amb ratlletes.', 0.5),
            ('abajo', 265, 'IZQ', 'Una negra amb puntet per temps: Fa-Do, Re-La, Si♭-Do, Re.',
             0.2)],
        3: [('arriba', 300, 'AMB', 'Els cc. 13-16 són els cc. 9-12 un altre cop: ja ho saps!',
             0.4)],
        4: [('arriba', 265, 'IZQ', 'Octaves: dues notes iguals alhora. La, Sol, Fa, Mi.', 0.1),
            ('abajo', 265, 'OJO', 'Si♮ i La♭ (cc. 18-19). El La♮ final del c. 18 va lligat al '
                                  'c. 19.', 0.6)],
        5: [('arriba', 300, 'AMB', 'Igual que els cc. 17-20, però el c. 21 comença amb Mi '
                                   '(no hi ha silenci).', 0.25)],
        6: [('arriba', 265, 'OJO', 'Sol♯ i Si♮ (cc. 27-28) valen fins al final del compàs. C. 29: '
                                   'tresillo de semicorxeres.', 0.55),
            ('abajo', 265, 'IZQ', 'Cc. 27-29: octaves que baixen: Mi, Re, Do, Si♮, Si♭, La.',
             0.8)],
        7: [('arriba', 300, 'AMB', 'Cc. 30-33: com els cc. 1-4, a les dues mans.', 0.3),
            ('abajo', 265, 'OJO', 'Acord arpegiat (línia ondulada): de baix a dalt, de pressa, '
                                  'i aguanta. Bravo!', 0.93)],
    },
    marcas=[],
    misol=dict(
        manos="Aprèn el principi de memòria: «silenci, nota, nota». Amb això ja en saps mitja "
              "peça!",
        guia="La peça és plena de dibuixos que tornen. Cada cop que en reconeguis un, és un bloc "
             "que ja saps!",
        pauta="Escriu el c. 1: silenci, La, Sol, silenci, Mi, Re. Compta 1-2-3, 4-5-6 en veu "
              "alta!"),
    pie_pauta="la clau la poses tu · copia el c. 1 o escriu l'escala de Re menor")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_tx_hijo_luna.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
