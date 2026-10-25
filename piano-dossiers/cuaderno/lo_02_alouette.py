# -*- coding: utf-8 -*-
"""Peça 2 · Alouette (arr. Gilbert DeBenedetti, Gradimi, «Debutant / Primer Level»).
   MESURAT sobre el PDF (1 pàgina, carta; notes pintades amb colorear_notas.py): sense armadura,
   4/4 («C»), «Assez vite / Rather fast» al c. 1, «Plus lentement / Slower» al c. 8 (calderó
   al Re final), «Comme auparavant / As before» al c. 9. 12 compassos en 4 sistemes (2+3+3+4).
   Dreta: c. 1 Do. Re♪ Mi Mi; c. 2 Re♪ Do♪ Re♪ Mi♪ Do; c. 3 = c. 1; c. 4 = c. 2 amb Do blanca;
   c. 5 Do Re Mi Fa Sol Sol (corxeres) Sol; c. 7 Sol Sol Sol (dit 5); c. 8 Sol Fa Mi Re (calderó).
   Esquerra: c. 2 Sol3 al darrer temps (dit 1, unit a la dreta amb una línia); c. 6 Sol Fa Mi Re
   Do Do Do (baixant); c. 7 Sol Sol Sol; c. 8 Sol3 rodona; c. 10 Sol3. Els cc. 9-12 repeteixen 1-4."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

_q = lambda p: {'pitch': p, 'dur': 'q'}
_e = lambda g: {'pitch': 'B4', 'dur': 'e', 'beam': g}

SPEC = dict(
    num=2, slug='alouette', pdf='alouette.pdf', time_sig=(4, 4),
    titulo='Alouette',
    autor='Cançó tradicional francesa · arr. Gilbert DeBenedetti',
    kicker='Lola · peça 2 · Alouette', mes='Novembre · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=alouette+gentille+alouette+piano+easy',
    credito='Partitura: arr. Gilbert DeBenedetti (gradimi.com). Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense alteracions'), ('Compàs', '4/4'), ('Tempo', '«Assez vite» (ràpid)'),
               ('Figura curta', 'Corxera'), ('Compassos', '12')],
        total=12,
        secciones=[('A', 1, 5, 'Alouette, gentille…', AZUL),
                   ('B', 6, 8, 'Més lent: baixem', OCRE),
                   ('A', 9, 12, 'Com abans', AZUL)],
        ideas=[('LA DRETA', 'Per escales',
                'Do Re Mi, Re Do Re Mi, i una escala que puja fins al Sol (compàs 5).'),
               ("L'ESQUERRA", 'Un Sol que respon',
                "Sol al compàs 2 i, al 6, baixa Sol Fa Mi Re Do. Poques notes, ben triades."),
               ('EL TEMPO', 'Ràpid, lent, ràpid',
                'Comença ràpid, al compàs 8 va «més lent» (amb un calderó) i al 9 torna com abans.'),
               ('LES REPETICIONS', 'Meitat repetida',
                'Els compassos 1-4 i 9-12 són la mateixa música: només cal aprendre-la una vegada.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie='Do = vermell · Re = taronja · Mi = groc · Fa = verd · Sol = blau · La = lila · Si = gris.',
        especial=[
            'No hi ha cap alteració: només notes blanques del piano.',
            'Comença ràpid («Assez vite»), al c. 8 va més lent i al c. 9 torna «com abans».',
            'Al c. 8, el Re final té un calderó: es pot allargar a gust.',
            'La mà esquerra baixa Sol Fa Mi Re Do al c. 6 i se sent com si «baixés una escala».',
            'Els cc. 9-12 són una còpia dels cc. 1-4.'],
        reto='Toca la cançó i fes el canvi de ràpid a lent al c. 8 sense equivocar-te.',
        truco="Pinta amb llapis de colors les notes que se't resisteixin i toca-les dient el nom: Do, Re, Mi...",
        sabias='«Alouette» vol dir «alosa» en francès, un ocellet. És una cançó popular del Canadà francès '
               "que es canta mentre es fa un joc de noms de parts del cos. (Dada no verificada.)",
        qr_texto='Escolta-la i canta amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo='Com es compta el c. 1 i el c. 2',
        cuenta_pie='Negra amb puntet + corxera: «1-2-3, i, 4». Quatre corxeres: «1-i, 2-i». Aquí només el ritme.',
        ritmos=[('EL COMPÀS 1', '4/4 · negra amb puntet, corxera, negra, negra',
                 [{'pitch': 'B4', 'dur': 'q.'}, {'pitch': 'B4', 'dur': 'e'}, _q('B4'), _q('B4')],
                 OCRE, 'treble', None),
                ('EL COMPÀS 2', '4/4 · quatre corxeres + dues negres',
                 [_e(0), _e(0), _e(0), _e(0), _q('B4'), _q('B4')], AZUL, 'treble', None)]),
    manos=dict(
        izq=[('Sol amb el dit 1', "Al c. 2 el polze esquerre toca un Sol, a l'últim temps. Un sol cop i ja està."),
             ('Baixa Sol, Fa, Mi, Re, Do', "Al c. 6 la mà esquerra baixa de cinc en cinc: dits 1-2-3-4-5. Dits arrodonits!"),
             ('Tres soles seguits', 'Al c. 7: compta 1-2 en silenci i toca Sol, Sol, Sol als temps 3 i 4 (dit 1).'),
             ('Sol llarg', 'Al c. 8, una rodona: Sol durant quatre temps. Prem la tecla i compta 1-2-3-4.')],
        der=[("Do. Re Mi Mi", "C. 1: Do amb el dit 1. Dues notes juntes: Do llarg (negra amb puntet) i Re curt."),
             ('Corxeres de quatre en quatre', 'Al c. 2 i al c. 4: Re Do Re Mi i una nota més. Compta «1-i-2-i».'),
             ('Escala cap amunt', 'Al c. 5: Do Re Mi Fa Sol, una nota per tecla blanca, sense saltar-ne cap.'),
             ('Sol Sol Sol amb el dit 5', 'Al c. 7 la dreta toca Sol Sol Sol amb el dit 5 als temps 1-2 i descansa. Al c. 8 baixa Sol Fa Mi Re.')],
        tecnica=['Dits arrodonits, mà relaxada.',
                 'Quan una mà descansa, reposa sobre les tecles.',
                 "Compta 1-2-3-4 en veu alta, també al lent."]),
    bloques=[
        B(1, 'cc. 1-2', 'Alouette, gentille alouette', (0, 0),
          D('cadena', 'Qui toca què',
            [('dta.: Do Re Mi Mi', False), ('dta.: Re Do Re Mi Do', False), ('esq.: Sol', True)]),
          [('IZQUIERDA', 'Només un Sol (dit 1) a l\'últim temps del c. 2. Troba\'l amb els ulls.'),
           ('DERECHA', 'C. 1: Do. Re Mi Mi. C. 2: Re Do Re Mi i Do. Compta en veu alta.'),
           ('JUNTAS', 'Dreta tota la frase i, en acabar, el Sol de la mà esquerra.'),
           ('A TEMPO', 'Ràpid, com diu «Assez vite», però sense córrer.')]),
        B(2, 'cc. 3-5', 'Es repeteix i puja', (1, 1),
          D('cadena', 'Del Do al Sol',
            [('c. 3 = c. 1', False), ('c. 4: Do llarg', False), ('c. 5: escala', True)]),
          [('IZQUIERDA', 'Aquí descansa: només mira i compta les pauses.'),
           ('DERECHA', 'C. 3 com el c. 1. C. 4 acaba amb un Do llarg (blanca). C. 5: Do Re Mi Fa Sol i tres Sol.'),
           ('JUNTAS', 'La dreta sola, de principi a fi: és la part més llarga!'),
           ('OJO', 'Al c. 5 les notes van de cinc en cinc dits: 1-2-3-4-5 i tres Sol.')]),
        B(3, 'cc. 6-8', 'Més lent (Plus lentement)', (2, 2),
          D('cadena', 'Les mans es passen la cançó',
            [('esq. baixa', False), ('dta.: Sol Sol Sol', False), ('dta. baixa + calderó', True)]),
          [('IZQUIERDA', 'C. 6: Sol Fa Mi Re Do Do Do. C. 7: Sol Sol Sol. C. 8: Sol llarg.'),
           ('DERECHA', 'C. 7: Sol Sol Sol (dit 5). C. 8: Sol Fa Mi Re, el Re amb calderó.'),
           ('JUNTAS', 'Una mà després de l\'altra: esq. (c. 6), dta. (c. 7), tots dos (c. 8).'),
           ('OJO', 'Al c. 8 el calderó (♩ amb un arc) vol dir: allarga la nota. Compta fins a 5 o 6.')]),
        B(4, 'cc. 9-12', 'Com abans i tota la cançó', (3, 3),
          D('cadena', 'Torna el principi',
            [('c. 9 = c. 1', False), ('c. 10 = c. 2', False), ('c. 11-12', True)]),
          [('IZQUIERDA', 'Només un Sol al c. 10, igual que al c. 2.'),
           ('DERECHA', 'Els cc. 9-12 són els cc. 1-4: la mateixa melodia.'),
           ('JUNTAS', "Toca els quatre compassos com si fossin els del principi."),
           ('A TEMPO', 'Torna al ràpid i toca tota la cançó, de principi a fi. Fes que es noti el canvi lent!')]),
    ],
    lista=['Sé la dreta de memòria.',
           'Toco bé la baixada Sol-Fa-Mi-Re-Do de la mà esquerra.',
           'Allargo el calderó del c. 8.',
           'Faig el canvi ràpid – lent – ràpid.',
           'Toco els 12 compassos sense parar.'],
    cortes={1: [250.2, 381.5, 534.0]}, inicio={1: 96}, fin={1: 660},
    burb={
        0: [('arriba', 262, 'DER', 'Do. Re Mi Mi (c. 1) i Re Do Re Mi Do (c. 2). Compta 1-i-2-i.', 0.17),
            ('arriba', 262, 'IZQ', 'Aquest Sol blau de la mà esquerra (dit 1) arriba al darrer temps.', 0.88)],
        1: [('arriba', 262, 'DER', 'C. 3 igual que el c. 1. C. 4 acaba amb un Do llarg.', 0.28),
            ('arriba', 262, 'AMB', 'C. 5: Do Re Mi Fa Sol, cinc notes seguides i tres Sol.', 0.8)],
        2: [('arriba', 262, 'IZQ', 'Baixa Sol Fa Mi Re Do. Després tres Do i tres Sol.', 0.2),
            ('arriba', 262, 'OJO', 'Més lent! El calderó del c. 8 allarga el Re final.', 0.92)],
        3: [('arriba', 262, 'DER', 'Com abans: la mateixa música que els cc. 1-4.', 0.2),
            ('arriba', 262, 'IZQ', 'Un Sol esquerre al c. 10, igual que al c. 2.', 0.38)],
    },
    misol=dict(
        manos="Aprèn-te la cançó cantant el nom de les notes i els seus colors: Do vermell, Re taronja...",
        guia="Mira els compassos 1-4 i 9-12: són iguals! Ja saps la meitat de la cançó sense fer res més.",
        pauta="Escriu aquí els noms de les notes del c. 5 amb els seus colors: Do, Re, Mi, Fa, Sol!"),
    marcas=[],
    pie_pauta="la clau la poses tu · copia un compàs i pinta les notes del seu color")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_alouette.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
