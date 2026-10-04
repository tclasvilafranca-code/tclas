# -*- coding: utf-8 -*-
"""EL LLIBRE DE PEKES — contingut (en catala).

   Historia, perque no es repeteixi:
   - v1 (setmanes, una fulla per classe) i v2 (disseny propi en blanc i negre):
     rebutjades pel client ("todo el diseno en general es feo").
   - v3: el motor i l'aspecte dels albums d'alumne. Li agrada, pero demana:
     TOT EN CATALA, mes informacio i practica de la MA ESQUERRA, fitxes de
     casa mes dinamiques (relacionar, pintar, comptar, amb el codi de colors
     de les notes que ja coneixen) i la lletra MOLT mes gran.
   - v4 (aquesta): `pekes_hojas.py` posa tot aixo a mida de nen.

   Estructura: un llibre de teoria i exercicis, SENSE setmanes. Cada tema son
   quatre fulles: teoria, al piano i dues fitxes per a casa. L'ordre dels
   capitols es el de "La ruta musical" del Canva original del client.

   Les notes de la ma esquerra: en aquest punt del curs el nen nomes llegeix
   la clau de Sol, aixi que l'esquerra toca les MATEIXES notes (Do-Re-Mi del
   mig del piano) amb els dits 3-2-1. Escriure-la una octava avall demanaria
   la clau de Fa o sis linies addicionals, i cap de les dues coses es pot
   llegir encara.
"""

CAPITOLS = [
    ('Abans de tocar', 'conèixer el piano i les mans', [
        (1, 'El piano i les seves parts'),
        (2, 'Les meves mans i els meus dits'),
        (3, 'Greu i agut'),
        (4, 'El Do, casa nostra'),
    ]),
    ('El pentagrama i la clau de Sol', 'la casa on viuen les notes', [
        (5, 'La casa de les notes'),
        (6, 'Línies i espais'),
        (7, 'La clau de Sol'),
    ]),
    ('Les notes i els seus colors', 'una a una, al piano i al paper', [
        (8, 'Do, Re i Mi'),
        (9, 'Fa i Sol'),
        (10, 'La i Si'),
        (11, 'Les set notes'),
    ]),
    ('Les figures', 'el que dura cada nota', [
        (12, 'Rodona, blanca i negra'),
        (13, 'El compàs'),
    ]),
    ('Els silencis', 'quan no es toca, també es compta', [
        (14, 'Els tres silencis'),
    ]),
    ('Les pliques', 'el pal de les notes', [
        (15, 'Plica amunt, plica avall'),
    ]),
    ("L'escala musical", 'tot junt', [
        (16, 'De Do a Do'),
        (17, 'El gran repàs i el meu primer concert'),
    ]),
]

# Amb la lletra a mida de nen, cada part del tema ocupa dues fulles: retallar
# material per fer-lo cabre en una era justament el contrari del que es va
# demanar ("anadir info y practica").
FULLES_PER_TEMA = 6            # teoria ×2 · al piano ×2 · fitxa ×2
PRIMERA_PAGINA_TEMES = 3       # 1 portada · 2 index


def pagina_de(n_tema):
    return PRIMERA_PAGINA_TEMES + (n_tema - 1) * FULLES_PER_TEMA


def capitol_de(n_tema):
    for i, (nom, _sub, temes) in enumerate(CAPITOLS, 1):
        if any(n == n_tema for n, _t in temes):
            return i, nom
    raise ValueError(n_tema)


def q(p, d='q'):
    """Una nota. Sense numero de dit a sobre: norma del projecte, els dits
       no s'imprimeixen mai al pentagrama (els escriu l'alumne). On va cada
       dit ho diu el text i el teclat dibuixat."""
    return {'pitch': p, 'dur': d}


HOT_CROSS_BUNS = [q('E4'), q('D4'), q('C4', 'h'),
                  q('E4'), q('D4'), q('C4', 'h'),
                  q('C4'), q('C4'), q('D4'), q('D4'),
                  q('E4'), q('D4'), q('C4', 'h')]

TEMES = {
    8: dict(
        titol='Do, Re i Mi',
        teoria=dict(
            intro='Les nostres tres primeres notes. Viuen juntes al piano i juntes al '
                  'pentagrama: l’una al costat de l’altra, com tres esglaons.',
            regles=['DO · RE · MI', 'PUGEN COM UNA ESCALA', 'AMB LES DUES MANS'],
            fulles=[[
                dict(tipus='misol',
                     text='Hola! Avui coneixerem tres amigues que sempre van juntes: el Do, '
                          'el Re i el Mi. Si saps on viu el Do, les altres dues són just al '
                          'costat!'),
                dict(tipus='mans', titol='On van els dits',
                     esquerra={0: 3, 1: 2, 2: 1}, dreta={0: 1, 1: 2, 2: 3},
                     peu='Mira-ho bé: a la mà esquerra els dits van al revés. El dit 3 toca '
                         'el Do i el polze, que és el dit 1, toca el Mi.'),
                dict(tipus='pentagrama', titol='Al pentagrama',
                     notes=[('C4', 'Do'), ('D4', 'Re'), ('E4', 'Mi')],
                     peu='Cada nota és un esglaó més amunt que l’anterior: al paper pugen '
                         'igual que al piano.'),
            ], [
                dict(tipus='escala', titol='L’escala Do-Re-Mi',
                     notes=['Do', 'Re', 'Mi'],
                     peu='Pinta el cercle de cada esglaó del seu color. Quan toques Do-Re-Mi '
                         'puges l’escala, i quan toques Mi-Re-Do la baixes.'),
                dict(tipus='targetes', titol='Una a una', items=[
                    ('LA PRIMERA', 'Do',
                     'Porta una ratlleta que la travessa pel mig. Al piano, a l’esquerra '
                     'de les dues negres.'),
                    ('LA DEL MIG', 'Re',
                     'Penja just a sota del pentagrama, sense ratlleta. Al piano, entre '
                     'les dues negres.'),
                    ('LA TERCERA', 'Mi',
                     'La primera línia li passa per la panxa. Al piano, a la dreta de les '
                     'dues negres.'),
                ]),
                dict(tipus='nota', etiqueta='RECORDA',
                     text='El Do sempre és a l’esquerra de les dues tecles negres juntes. Si '
                          'trobes el Do, el Re i el Mi són just al costat!'),
                dict(tipus='sabies',
                     text='Els noms Do, Re i Mi vénen d’una cançó de fa més de mil anys: cada '
                          'nota començava amb una síl·laba d’una frase en llatí. I al principi '
                          'el Do no es deia Do, sinó «Ut»!'),
            ]],
        ),
        piano=dict(
            intro='Ara toquem de debò! Primer amb la mà dreta, després amb l’esquerra, i al '
                  'final les dues, l’una darrere l’altra.',
            regles=['MÀ DRETA: DITS 1-2-3', 'MÀ ESQUERRA: DITS 3-2-1', 'A POC A POC I CANTANT'],
            fulles=[[
                dict(tipus='misol',
                     text='Abans de tocar, posa els dits a casa: a la mà dreta, el dit 1 al Do. '
                          'A la mà esquerra, el dit 3 al Do. I no es mouen de casa en tota la '
                          'pàgina!'),
                dict(tipus='exercici', titol='La mà dreta puja i baixa',
                     pista='dits 1, 2 i 3 · canta el nom de cada nota mentre la toques',
                     sistemes=[dict(events=[q('C4'), q('D4'), q('E4'), q('D4'), q('C4', 'w')],
                                    compassos=2)]),
                dict(tipus='exercici', titol='Ara, la mà esquerra',
                     pista='dits 3, 2 i 1 · comença pel Mi, amb el polze',
                     sistemes=[dict(events=[q('E4'), q('D4'), q('C4'), q('D4'), q('E4', 'w')],
                                    compassos=2)]),
                dict(tipus='exercici', titol='Pregunta i resposta',
                     pista='un compàs amb la mà dreta, el següent amb l’esquerra',
                     sistemes=[dict(events=[q('C4'), q('D4'), q('E4', 'h'),
                                            q('E4'), q('D4'), q('C4', 'h'),
                                            q('C4'), q('D4'), q('E4', 'h'),
                                            q('E4'), q('D4'), q('C4', 'h')],
                                    compassos=4)]),
            ], [
                dict(tipus='misol', pose='happy', etiqueta='EN MUSSOL MISOL CANTA',
                     text='Ja saps tres notes amb les dues mans! Ara les posem juntes en una '
                          'cançó de veritat. Primer canta-la, i després toca-la.'),
                dict(tipus='exercici', titol='La meva primera cançó',
                     pista='Hot Cross Buns · cançó popular anglesa, simplificada',
                     sistemes=[
                         dict(cap='a) amb la mà dreta', events=HOT_CROSS_BUNS, compassos=4),
                         dict(cap='b) i ara amb la mà esquerra · són les mateixes notes!',
                              events=HOT_CROSS_BUNS, compassos=4, show_time=False),
                     ]),
                dict(tipus='nota', etiqueta='COM SABER SI HO FAS BÉ',
                     text='Si per tocar el Mi has de moure la mà, és que no estava ben posada. '
                          'Torna a deixar els dits a casa i comença de nou: a poc a poc surt '
                          'sol!'),
                dict(tipus='joc', etiqueta='UN JOC AMB LA PROFE: L’ECO',
                     text='La profe toca tres notes amb una mà i tu les repeteixes amb la '
                          'mateixa mà, com un eco. Després canvieu de mà!'),
                dict(tipus='estrelles',
                     etiqueta='CADA DIA QUE TOQUIS LA CANÇÓ, PINTA UNA ESTRELLA'),
            ]],
        ),
        fitxa=dict(
            intro='Agafa un llapis i els teus colors. Tot el que hi ha en aquestes fitxes és '
                  'del Do, el Re i el Mi.',
            fulles=[
                [
                    dict(tipus='misol',
                         text='En aquest llibre cada nota té el seu color: el Do és VERMELL, '
                              'el Re és TARONJA i el Mi és GROC. Primer pinta les rodonetes '
                              'de la llegenda!'),
                    dict(tipus='pinta', titol='Escriu el nom i pinta',
                         pista='escriu DO, RE o MI a la caixeta i pinta la nota del seu color',
                         llegenda=['DO', 'RE', 'MI'],
                         notes=['C4', 'E4', 'D4', 'C4', 'E4', 'D4', 'E4', 'C4']),
                    dict(tipus='relaciona', titol='Cada nota amb la seva tecla',
                         pista='uneix amb una ratlla cada nota amb la tecla que té el punt',
                         notes=['C4', 'D4', 'E4'], tecles=['E4', 'C4', 'D4']),
                ],
                [
                    dict(tipus='compta', titol='Compta i pinta',
                         pista='quantes n’hi ha de cada? Escriu el número i pinta el cercle '
                               'del seu color',
                         notes=['C4', 'E4', 'E4', 'D4', 'C4', 'E4', 'D4', 'E4', 'C4', 'E4'],
                         quines=['DO', 'RE', 'MI']),
                    dict(tipus='cami', titol='Ajuda en Mussol Misol',
                         pista='pinta el camí trepitjant les notes en ordre: DO, RE, MI, DO, '
                               'RE, MI... fins al piano',
                         files=4, columnes=7, cicle=['DO', 'RE', 'MI'],
                         cami=[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4),
                               (1, 4), (1, 5), (1, 6), (2, 6), (3, 6)]),
                    dict(tipus='teclat_pinta', titol='Busca-les al teclat',
                         pista='n’hi ha més d’un de cada!', pintar=['DO', 'RE', 'MI']),
                    dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                         text='Canta Do-Re-Mi pujant o Mi-Re-Do baixant, sense dir quin. Qui '
                              'està amb tu endevina si puges o baixes!'),
                ],
            ],
        ),
    ),
}
