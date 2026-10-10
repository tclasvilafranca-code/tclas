# -*- coding: utf-8 -*-
"""EL LLIBRE DE PEKES — contingut (en catala).

   Historia, perque no es repeteixi:
   - v1 (setmanes, una fulla per classe) i v2 (disseny propi en blanc i negre):
     rebutjades pel client ("todo el diseno en general es feo").
   - v3: el motor i l'aspecte dels albums d'alumne. Li agrada, pero demana:
     TOT EN CATALA, mes informacio i practica de la MA ESQUERRA, fitxes de
     casa mes dinamiques (relacionar, pintar, comptar, amb el codi de colors
     de les notes que ja coneixen) i la lletra MOLT mes gran.
   - v4: `pekes_hojas.py` posa tot aixo a mida de nen. Mostra d'un tema.
   - v5 (aquesta): el llibre sencer, amb dues decisions del client:
       * LES DUES CLAUS DES DEL PRINCIPI: la ma dreta llegeix en clau de Sol i
         la ma esquerra en clau de Fa, a la teoria, al piano i a les fitxes.
         Per aixo el capitol 2 ensenya les dues claus i el gran pentagrama
         ABANS de les notes.
       * Una pagina de REPAS AMB MEDALLA al final de cada capitol.

   Estructura: un llibre de teoria i exercicis, SENSE setmanes: la profe va
   al ritme del nen. Cada tema te les seves fulles de teoria, d'al piano i de
   fitxa per a casa. L'ordre dels capitols es el de "La ruta musical" del
   Canva original del client, amb les claus avancades.

   Les posicions de les mans (les mateixes a tot el llibre):
     posicio de Do   ma dreta Do4-Sol4 (dits 1-5) · ma esquerra Do3-Sol3 (dits 5-1)
     posicio de Sol  ma dreta Sol4-Re5 (dits 1-5) · ma esquerra Sol2-Re3 (dits 5-1)
   Cap nota passa de dues linies addicionals (norma del projecte). Els numeros
   de dit no s'imprimeixen mai al pentagrama: els diu el text i el teclat.

   Les cancons son melodies populars verificades (Hot Cross Buns, Au clair de
   la lune, Mary Had a Little Lamb, l'Oda a l'alegria simplificada); la resta
   del material d'al piano son exercicis construits sobre la posicio.
"""

# --------------------------------------------------------------------------
# musica
# --------------------------------------------------------------------------
def m(text):
    """Una linia de musica escrita a ma: 'E4 D4 C4:h | R:q [C3+E4]:w'.
       La barra | nomes ajuda a llegir; la posa el motor tot sol."""
    out = []
    for tok in text.split():
        if tok == '|':
            continue
        p, _, d = tok.partition(':')
        d = d or 'q'
        if p == 'R':
            out.append({'rest': True, 'dur': d})
        elif p.startswith('['):
            out.append({'pitches': p.strip('[]').split('+'), 'dur': d})
        else:
            out.append({'pitch': p, 'dur': d})
    return out


def sis(text, compassos=4, clau='treble', cap=None, compas_visible=False, **kw):
    """Un sistema d'exercici. Fins al tema del compas (14) no es mostra la
       xifra 4/4: el nen encara no sap que vol dir."""
    d = dict(events=m(text), compassos=compassos, clau=clau, show_time=compas_visible)
    if cap:
        d['cap'] = cap
    d.update(kw)
    return d


TOTES = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']

DO_DRETA = dict(rotul='MÀ DRETA · posició de Do', inici=0, n=5,
                dits={0: 1, 1: 2, 2: 3, 3: 4, 4: 5})
DO_ESQUERRA = dict(rotul='MÀ ESQUERRA · posició de Do', inici=0, n=5,
                   dits={0: 5, 1: 4, 2: 3, 3: 2, 4: 1})
SOL_DRETA = dict(rotul='MÀ DRETA · posició de Sol', inici=4, n=5,
                 dits={0: 1, 1: 2, 2: 3, 3: 4, 4: 5})
SOL_ESQUERRA = dict(rotul='MÀ ESQUERRA · posició de Sol', inici=4, n=5,
                    dits={0: 5, 1: 4, 2: 3, 3: 2, 4: 1})

# --------------------------------------------------------------------------
# l'index
# --------------------------------------------------------------------------
CAPITOLS = [
    ('Abans de tocar', 'el piano, les mans i el Do', [
        (1, 'El piano i les seves parts'),
        (2, 'Les meves mans i els meus dits'),
        (3, 'Greu i agut'),
        (4, 'El Do i les seves germanes'),
    ]),
    ('El pentagrama i les claus', 'la casa on viuen les notes', [
        (5, 'La casa de les notes'),
        (6, 'La clau de Sol'),
        (7, 'La clau de Fa'),
        (8, 'El gran pentagrama'),
    ]),
    ('Les notes i els seus colors', 'una a una, amb les dues mans', [
        (9, 'Do, Re i Mi'),
        (10, 'Fa i Sol'),
        (11, 'La i Si'),
        (12, 'Les set notes'),
    ]),
    ('Les figures', 'el que dura cada nota', [
        (13, 'Rodona, blanca i negra'),
        (14, 'El compàs'),
    ]),
    ('Els silencis', 'quan no es toca, també es compta', [
        (15, 'Els tres silencis'),
    ]),
    ('Les pliques', 'el pal de les notes', [
        (16, 'Plica amunt, plica avall'),
    ]),
    ('Tot junt', 'les dues mans i el primer concert', [
        (17, 'Les dues mans alhora'),
        (18, 'El gran repàs i el meu primer concert'),
    ]),
]


def capitol_de(n_tema):
    for i, (nom, _sub, temes) in enumerate(CAPITOLS, 1):
        if any(n == n_tema for n, _t in temes):
            return i, nom
    raise ValueError(n_tema)


def fulles_de(tema):
    return sum(len(tema[s]['fulles']) for s in ('teoria', 'piano', 'fitxa'))


def paginacio():
    """{('tema', n): pagina, ('repas', capitol): pagina}. Es calcula de les
       dades: cada tema ocupa les fulles que te, i cada capitol acaba amb la
       seva pagina de repas."""
    pag = 3                                 # 1 portada · 2 index
    out = {}
    for i, (_nom, _sub, temes) in enumerate(CAPITOLS, 1):
        for n, _t in temes:
            out[('tema', n)] = pag
            pag += fulles_de(TEMES[n])
        out[('repas', i)] = pag
        pag += 1
    return out


# --------------------------------------------------------------------------
# els temes
# --------------------------------------------------------------------------
TEMES = {}

# ==========================================================================
# CAPITOL 1 · ABANS DE TOCAR
# ==========================================================================
TEMES[1] = dict(
    titol='El piano i les seves parts',
    teoria=dict(
        intro='Abans de tocar, coneixem el nostre instrument: què té per fora, què '
              'amaga per dins i com ens hi asseiem.',
        regles=['TECLES BLANQUES I NEGRES', 'MARTELLETS I CORDES', 'BEN ASSEGUTS'],
        fulles=[[
            dict(tipus='misol',
                 text='Hola! Sóc en Mussol Misol i t’acompanyaré per tot el llibre. Avui '
                      'et presento el meu millor amic: el piano. Té moltes tecles, però '
                      'no t’espantis: aviat les coneixeràs totes!'),
            dict(tipus='teclat', titol='Tecles blanques i tecles negres', tecles=15,
                 grups=True, alt=90,
                 peu='Fixa’t en les tecles negres: van en grups de DUES i de TRES, i '
                     'sempre en el mateix ordre. Això ens ajudarà a trobar totes les notes.'),
            dict(tipus='targetes', titol='Les parts del piano', items=[
                ('A FORA', 'Les tecles',
                 'On posem els dits. N’hi ha de blanques i de negres.'),
                ('A BAIX', 'Els pedals',
                 'Es toquen amb els peus. De moment, els deixem descansar!'),
                ('A DALT', 'La tapa',
                 'Protegeix les tecles. S’obre i es tanca a poc a poc.'),
            ]),
            dict(tipus='nota', etiqueta='RECORDA',
                 text='El piano no és una joguina: es toca amb els dits nets i amb '
                      'suavitat. Les tecles no es piquen, s’acaricien!'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Saps què passa quan toques una tecla? A dins del piano, un '
                      'martellet petit corre a picar una corda. La corda vibra… i sona '
                      'la música!'),
            dict(tipus='targetes', titol='Què hi ha a dins?', items=[
                ('1', 'La tecla', 'Tu l’apretes amb el dit.'),
                ('2', 'El martellet', 'Té un cap de feltre tou i pica la corda.'),
                ('3', 'La corda', 'Vibra i fa el so. N’hi ha més de dues-centes!'),
            ]),
            dict(tipus='targetes', titol='Com m’assec al piano', items=[
                ('L’ESQUENA', 'Dreta',
                 'Com un arbre, sense penjar-te cap endavant.'),
                ('ELS PEUS', 'A terra',
                 'Si no hi arriben, posa-hi un tamboret a sota.'),
                ('ELS BRAÇOS', 'Tous',
                 'Les espatlles avall i els colzes a l’altura de les tecles.'),
            ]),
            dict(tipus='sabies',
                 text='Un piano de cua pot pesar tant com un cotxe! I el primer piano '
                      'el va inventar un italià, en Bartolomeo Cristofori, fa més de '
                      'tres-cents anys.'),
        ]],
    ),
    piano=dict(
        intro='Primer contacte amb el piano. Avui no llegim res: escoltem, mirem i '
              'toquem amb molta suavitat.',
        regles=['ESQUENA DRETA', 'DITS RODONS', 'TOCAR AMB SUAVITAT'],
        fulles=[[
            dict(tipus='misol',
                 text='Abans de tocar, fem com els pianistes de veritat: seiem bé, '
                      'respirem i posem les mans a la falda. Ja estem preparats!'),
            dict(tipus='passos', titol='Em preparo per tocar',
                 pista='fes-ho cada dia abans de començar, com un petit ritual',
                 passos=['Seu al centre del banc, davant del nom del piano.',
                         'Posa els peus a terra i l’esquena ben dreta.',
                         'Fes la mà rodona, com si aguantessis una pilota petita.',
                         'Posa la mà sobre les tecles sense apretar-les. Shhh!']),
            dict(tipus='passos', titol='Els grups de negres',
                 pista='amb el dit 2 (l’índex), toca les tecles negres',
                 passos=['Toca els dos grups de DUES negres que trobis. Totes dues alhora!',
                         'Ara toca els grups de TRES negres. Totes tres alhora!',
                         'Ves de l’esquerra a la dreta del piano: dues, tres, dues, tres…']),
            dict(tipus='joc', etiqueta='UN JOC AMB LA PROFE: LA PLUJA',
                 text='Toca tecles negres molt fluix, com gotes de pluja petites. Quan '
                      'la profe diu «TRONS!», toca més fort. Quan diu «SOL!», t’atures.'),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara fem que el piano parli fluix i fort. Escolta bé: amb el '
                      'mateix dit i la mateixa tecla, pots fer sons molt diferents!'),
            dict(tipus='teclat', titol='Les tecles negres, de dues en dues', tecles=14,
                 grups=True, alt=80,
                 peu='Toca només els grups de DUES negres d’aquest teclat. Quants n’hi '
                     'ha? Compta’ls amb el dit!'),
            dict(tipus='passos', titol='Fluix i fort',
                 pista='amb el dit 3 (el del mig), sobre una tecla negra',
                 passos=['Toca tres vegades molt fluix, com un gatet que camina.',
                         'Toca tres vegades fort, com un elefant (però sense picar!).',
                         'Ara alterna: fluix, fort, fluix, fort.']),
            dict(tipus='estrelles',
                 etiqueta='CADA DIA QUE SEGUIS EL RITUAL AL PIANO, PINTA UNA ESTRELLA'),
        ]],
    ),
    fitxa=dict(
        intro='Ja coneixes el piano per fora i per dins. Demostra-ho amb aquestes fitxes!',
        fulles=[[
            dict(tipus='misol',
                 text='Uneix cada part del piano amb el que fa. Si no te’n recordes, '
                      'mira la teoria: no passa res!'),
            dict(tipus='uneix', titol='Cada part, amb la seva feina',
                 pista='uneix els punts amb una ratlla',
                 esquerra=['La tecla', 'El martellet', 'La corda', 'El pedal', 'La tapa'],
                 dreta=['es toca amb el peu', 'vibra i fa el so', 'l’apretem amb el dit',
                        'protegeix les tecles', 'pica la corda']),
            dict(tipus='endevina', titol='Endevina qui sóc',
                 pista='escriu una lletra a cada caixeta',
                 items=[('Sóc blanca o negra i em toques amb el dit.', 'TECLA'),
                        ('Tinc un cap de feltre i pico les cordes.', 'MARTELLET'),
                        ('Em toques amb el peu, a sota del piano.', 'PEDAL')]),
        ], [
            dict(tipus='sopa', titol='Sopa de lletres del piano',
                 pista='busca les paraules en horitzontal i en vertical, i marca la caixeta',
                 paraules=['PIANO', 'TECLA', 'CORDA', 'PEDAL', 'TAPA', 'MÚSICA'],
                 llavor=11),
            dict(tipus='quadre', etiqueta='DIBUIXA AQUÍ',
                 text='Dibuixa’t assegut al piano: amb '
                      'l’esquena dreta, els peus a terra i la mà rodona.'),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Explica a algú de casa com sona un piano per dins: tecla, '
                      'martellet i corda. Ho sabràs explicar millor que ningú!'),
        ]],
    ),
)

TEMES[2] = dict(
    titol='Les meves mans i els meus dits',
    teoria=dict(
        intro='Per tocar el piano tenim dues mans i deu dits. Cada dit té un número, i '
              'aquest número ens dirà quin dit toca cada nota.',
        regles=['DOS POLZES = DIT 1', 'DRETA I ESQUERRA', 'MÀ RODONA'],
        fulles=[[
            dict(tipus='misol',
                 text='Mira’t les mans. Els dos polzes són el dit 1. Després ve l’índex, '
                      'que és el 2, el del mig és el 3, l’anular el 4 i el petit, el 5. '
                      'A les dues mans igual!'),
            dict(tipus='mans', titol='Els números dels dits', alt=96,
                 teclats=[dict(DO_ESQUERRA, rotul='MÀ ESQUERRA'),
                          dict(DO_DRETA, rotul='MÀ DRETA')],
                 peu='Fixa’t: a la mà dreta el polze queda a l’esquerra, i a la mà '
                     'esquerra el polze queda a la dreta. Els dos polzes es miren!'),
            dict(tipus='targetes', titol='Cinc dits, cinc noms', items=[
                ('DIT 1', 'Polze', 'El més gruixut. Toca amb el costat.'),
                ('DIT 3', 'Del mig', 'El més llarg de tots.'),
                ('DIT 5', 'Petit', 'El més petit. Ha de fer-se fort!'),
            ]),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Al piano, la mà ha d’estar rodona, com si tinguessis una pilota '
                      'petita a dins. Els dits toquen amb la punta, com si caminessin!'),
            dict(tipus='targetes', titol='La mà de pianista', items=[
                ('LA MÀ', 'Rodona', 'Com una cúpula, o com un pont.'),
                ('ELS DITS', 'De puntetes', 'Toquen amb la punta, no amb el pla.'),
                ('EL CANELL', 'Tou', 'Ni amunt ni avall: recte i relaxat.'),
            ]),
            dict(tipus='nota', etiqueta='LA MÀ ESQUERRA TAMBÉ TOCA!',
                 text='Al piano les dues mans treballen igual. La dreta sol tocar les '
                      'notes agudes i l’esquerra, les greus. En aquest llibre totes dues '
                      'aprenen alhora: l’esquerra no és la germana petita!'),
            dict(tipus='joc', etiqueta='EL JOC DELS DITS BOJOS',
                 text='Algú diu un número i una mà: «Dit 3 de la mà esquerra!». Tu el '
                      'mous tan ràpid com puguis. Si t’equivoques de mà… torna a començar!'),
            dict(tipus='sabies',
                 text='El dit 4 és el més mandrós de tots, perquè va lligat al seu veí. '
                      'Fins i tot els pianistes famosos l’han d’entrenar cada dia!'),
        ]],
    ),
    piano=dict(
        intro='Fem caminar els dits per les tecles negres, primer amb una mà i després '
              'amb l’altra.',
        regles=['MÀ RODONA', 'DITS DE PUNTETES', 'LES DUES MANS'],
        fulles=[[
            dict(tipus='misol',
                 text='Les tecles negres són perfectes per començar: estan separades i '
                      'els dits les troben fàcilment. Comencem pels grups de tres!'),
            dict(tipus='teclat', titol='Els dits sobre un grup de tres negres', tecles=7,
                 inici=3, grups=True, alt=96,
                 peu='Posa els dits 2, 3 i 4 sobre les tres negres. Amb la mà dreta i '
                     'després amb l’esquerra: els dits del mig fan la mateixa feina!'),
            dict(tipus='passos', titol='Els dits caminen',
                 pista='primer la mà dreta, després la mà esquerra',
                 passos=['Toca 2, 3, 4 a poc a poc: un, dos, tres passos.',
                         'Torna enrere: 4, 3, 2.',
                         'Ara fes-ho amb l’altra mà. Els números són els mateixos!']),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara els polzes! El dit 1 toca amb el costat de l’ungla. Prova '
                      'de fer sonar una tecla blanca amb cada polze.'),
            dict(tipus='passos', titol='Dit a dit, de l’1 al 5',
                 pista='cinc tecles blanques seguides, un dit a cada una',
                 passos=['Mà dreta: toca 1, 2, 3, 4, 5, una tecla rere l’altra cap a la '
                         'dreta.',
                         'Mà esquerra: comença pel dit 5 i ves cap a la dreta: 5, 4, 3, 2, 1.',
                         'Escolta: totes dues mans pugen cap als sons aguts!']),
            dict(tipus='joc', etiqueta='UN JOC AMB LA PROFE: EL MIRALL',
                 text='La profe toca un dit d’una mà i tu el toques amb la mateixa mà i '
                      'el mateix número. Després, canvieu: tu fas de profe!'),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='Els números dels dits són molt importants. A veure si te’ls saps!',
        fulles=[[
            dict(tipus='misol',
                 text='Ajuda’m a arribar al piano! Només puc trepitjar els números en '
                      'ordre: 1, 2, 3, 4, 5, i torna a començar.'),
            dict(tipus='cami', titol='El camí dels dits',
                 pista='pinta les rodones del camí en ordre: 1, 2, 3, 4, 5, 1, 2…',
                 files=4, columnes=7, cicle=['1', '2', '3', '4', '5'],
                 coneguts=['1', '2', '3', '4', '5'], llavor=2,
                 cami=[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4),
                       (1, 4), (1, 5), (1, 6), (2, 6), (3, 6)]),
            dict(tipus='uneix', titol='Cada dit, amb el seu número',
                 pista='uneix el nom del dit amb el seu número',
                 esquerra=['Polze', 'Índex', 'Del mig', 'Anular', 'Petit'],
                 dreta=['dit 3', 'dit 5', 'dit 1', 'dit 4', 'dit 2']),
        ], [
            dict(tipus='vf', titol='Vertader o fals?',
                 pista='marca amb una creu la V si és vertader i la F si és fals',
                 frases=['El polze és el dit 1.',
                         'El dit petit és el dit 3.',
                         'La mà esquerra també té un dit 1.',
                         'Al piano, la mà ha d’estar plana com una taula.',
                         'Els dits toquen amb la punta.']),
            dict(tipus='quadre', etiqueta='DIBUIXA AQUÍ',
                 text='Ressegueix les teves dues mans aquí dins. Escriu el número a '
                      'cada dit: recorda que els dos polzes són el 1!'),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Algú de casa et toca un dit sense que miris. Endevina quin número '
                      'és i de quina mà!'),
        ]],
    ),
)

TEMES[3] = dict(
    titol='Greu i agut',
    teoria=dict(
        intro='El piano té sons greus, gruixuts com un ós, i sons aguts, primets com un '
              'ocellet. Depèn de cap on vagis!',
        regles=['ESQUERRA = GREU', 'DRETA = AGUT', 'PUJAR I BAIXAR'],
        fulles=[[
            dict(tipus='misol',
                 text='Quan vas cap a l’esquerra del piano, el so es fa greu i gruixut. '
                      'Quan vas cap a la dreta, es fa agut i primet. Prova-ho!'),
            dict(tipus='teclat', titol='Cap on va el so?', tecles=22, greu_agut=True,
                 alt=84,
                 peu='La mà esquerra viu a la banda dels greus i la mà dreta a la banda '
                     'dels aguts. Per això, normalment, l’esquerra fa els sons gruixuts.'),
            dict(tipus='targetes', titol='Animals greus i aguts', items=[
                ('GREU', 'L’ós', 'Fa un so gros i gruixut: grrr…'),
                ('AGUT', 'L’ocellet', 'Fa un so primet i brillant: piu, piu!'),
                ('GREU', 'L’elefant', 'Camina a poc a poc i fa un so gros.'),
            ]),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Quan toques una tecla i després la de la seva dreta, el so PUJA. '
                      'Quan vas cap a l’esquerra, el so BAIXA. Com una escala!'),
            dict(tipus='targetes', titol='Pujar i baixar', items=[
                ('CAP A LA DRETA', 'Puja', 'El so es fa més agut, pas a pas.'),
                ('CAP A L’ESQUERRA', 'Baixa', 'El so es fa més greu, pas a pas.'),
                ('LA MATEIXA', 'Es repeteix', 'Si toques la mateixa tecla, ni puja ni baixa.'),
            ]),
            dict(tipus='nota', etiqueta='RECORDA',
                 text='Greu i agut no vol dir fluix i fort! Una nota greu pot sonar molt '
                      'fluixa i una nota aguda pot sonar molt forta.'),
            dict(tipus='sabies',
                 text='Les cordes dels sons greus són llargues i gruixudes, i les dels '
                      'sons aguts són curtes i primes. Per això el piano de cua té forma '
                      'd’ala: s’escurça cap als aguts!'),
        ]],
    ),
    piano=dict(
        intro='Viatgem pel piano de punta a punta, de l’ós a l’ocellet, amb les dues mans.',
        regles=['ESQUERRA: GREUS', 'DRETA: AGUTS', 'ESCOLTA BÉ'],
        fulles=[[
            dict(tipus='misol',
                 text='Avui fem d’animals! La mà esquerra serà un ós que viu a baix, i la '
                      'mà dreta, un ocellet que viu a dalt del tot.'),
            dict(tipus='passos', titol='L’ós i l’ocellet',
                 pista='amb el dit 3 de cada mà, sobre els grups de dues negres',
                 passos=['Mà esquerra: toca els grups de dues negres més greus del piano. '
                         'Lent i pesat, com un ós!',
                         'Mà dreta: toca els grups de dues negres més aguts. Lleuger i '
                         'ràpid, com un ocellet!',
                         'L’ós i l’ocellet parlen: un grup cadascú, per torns.']),
            dict(tipus='passos', titol='L’ascensor',
                 pista='amb el dit 3, sobre els grups de dues negres',
                 passos=['Comença a baix de tot i puja grup a grup fins a dalt.',
                         'Ara baixa grup a grup fins a baix de tot.',
                         'Canvia de mà a la meitat del camí: l’esquerra fa els greus i la '
                         'dreta, els aguts.']),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara tanca els ulls i escolta. La profe tocarà sons i tu has '
                      'd’endevinar si són greus o aguts. Tens bones orelles?'),
            dict(tipus='joc', etiqueta='UN JOC AMB LA PROFE: ÓS O OCELLET?',
                 text='La profe toca una nota. Si és greu, fes l’ós amb els braços; si és '
                      'aguda, mou els braços com unes ales. Després, toca tu i ella '
                      'endevina!'),
            dict(tipus='joc', etiqueta='UN ALTRE JOC: PUJA O BAIXA?',
                 text='La profe toca dues notes. Si la segona és més aguda, aixeca la mà. '
                      'Si és més greu, abaixa-la. Si és la mateixa, queda’t quiet!'),
            dict(tipus='passos', titol='La tempesta',
                 pista='inventem una música amb greus i aguts',
                 passos=['Els trons: la mà esquerra toca greus, fort i a poc a poc.',
                         'La pluja: la mà dreta toca aguts, fluix i ràpid.',
                         'Surt el sol: toca les dues mans juntes, fluix, i atura’t.']),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='Greu o agut? Puja o baixa? Fes servir les teves orelles i el teu cap!',
        fulles=[[
            dict(tipus='misol',
                 text='Els animals grossos solen fer sons greus i els petits, sons aguts. '
                      'Endevina quin animal sóc!'),
            dict(tipus='endevina', titol='Endevina l’animal',
                 pista='escriu una lletra a cada caixeta',
                 items=[('Sóc gros i pelut, i faig un so molt greu.', 'OS'),
                        ('Sóc petit, tinc ales i faig piu, piu: molt agut!', 'OCELL'),
                        ('Tinc una trompa llarga i el meu so és greu.', 'ELEFANT'),
                        ('Sóc petitó, menjo formatge i faig un so agut.', 'RATOLI')]),
            dict(tipus='vf', titol='Vertader o fals?',
                 pista='marca amb una creu la V o la F',
                 frases=['Cap a la dreta del piano el so es fa més agut.',
                         'L’ós fa un so agut.',
                         'La mà esquerra sol tocar els sons greus.',
                         'Si toques la mateixa tecla, el so puja.']),
        ], [
            dict(tipus='sopa', titol='Sopa de lletres dels sons',
                 pista='busca les paraules i marca la caixeta quan les trobis',
                 paraules=['GREU', 'AGUT', 'PUJA', 'BAIXA', 'FORT', 'FLUIX'], llavor=5),
            dict(tipus='quadre', etiqueta='DIBUIXA AQUÍ',
                 text='Dibuixa un animal que faci un so GREU i '
                      'un altre que faci un so AGUT. Quins has triat?'),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Canta una nota greu o una nota aguda. Qui està amb tu ha de dir '
                      'quina és. Després, canvieu!'),
        ]],
    ),
)

TEMES[4] = dict(
    titol='El Do i les seves germanes',
    teoria=dict(
        intro='Les tecles blanques tenen nom: són set notes que es repeteixen per tot el '
              'piano. La primera, la que ho comença tot, és el Do.',
        regles=['DO · RE · MI · FA · SOL · LA · SI', 'EL DO, A L’ESQUERRA DE DUES NEGRES'],
        fulles=[[
            dict(tipus='misol',
                 text='Vols saber el truc per trobar el Do? Busca un grup de DUES tecles '
                      'negres. La tecla blanca que hi ha just a l’esquerra… és el Do!'),
            dict(tipus='teclat', titol='On viu el Do', tecles=15, grups=True,
                 ressalta=[0, 7, 14], etiquetes={0: 'DO', 7: 'DO', 14: 'DO'}, alt=88,
                 peu='Hi ha un Do a cada grup de dues negres. Al piano n’hi ha molts, i '
                     'tots es diuen igual!'),
            dict(tipus='escala', titol='Les set germanes, en ordre',
                 notes=['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'],
                 peu='Després del Si torna a venir el Do, i tot torna a començar. Pinta '
                     'cada cercle del color de la seva nota!'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Al mig del piano hi ha un Do molt important: el DO CENTRAL. És '
                      'la casa d’on surten les dues mans.'),
            dict(tipus='teclat', titol='El Do central', tecles=15, inici=0,
                 ressalta=[7], etiquetes={7: 'DO CENTRAL'}, alt=84,
                 peu='El Do central és el que tens just davant de la panxa quan seus al '
                     'mig del banc, davant del nom del piano.'),
            dict(tipus='nota', etiqueta='CADA NOTA, EL SEU COLOR',
                 text='En aquest llibre cada nota té un color: DO vermell, RE taronja, MI '
                      'groc, FA verd, SOL blau, LA lila i SI gris. Com un arc de Sant '
                      'Martí!'),
            dict(tipus='sabies',
                 text='En anglès i en alemany les notes no es diuen Do, Re, Mi, sinó amb '
                      'lletres: el Do és la C, el Re la D, el Mi la E… i el Sol és la G!'),
        ]],
    ),
    piano=dict(
        intro='Busquem el Do per tot el piano, i després hi posem les dues mans.',
        regles=['BUSCA LES DUES NEGRES', 'LA TECLA DE L’ESQUERRA', 'ÉS EL DO!'],
        fulles=[[
            dict(tipus='misol',
                 text='Som caçadors de Dos! Recorda el truc: dues negres, i el Do just a '
                      'l’esquerra. Quants en trobaràs?'),
            dict(tipus='passos', titol='La caça del Do',
                 pista='amb el dit 3 de cada mà',
                 passos=['Mà esquerra: toca tots els Do de la banda greu, de baix cap amunt.',
                         'Mà dreta: toca tots els Do de la banda aguda, cap amunt.',
                         'Canta «Do» cada vegada que en toquis un.']),
            dict(tipus='mans', titol='Les mans a casa: posició de Do',
                 teclats=[DO_ESQUERRA, DO_DRETA],
                 peu='La mà dreta posa el polze al Do central. La mà esquerra posa el dit '
                     '5 al Do de més avall. Cinc dits, cinc tecles: no se’n deixa cap!'),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara canta i toca l’ordre de les notes: Do, Re, Mi, Fa, Sol. Un dit '
                      'a cada tecla, sense saltar-ne cap!'),
            dict(tipus='passos', titol='Do-Re-Mi-Fa-Sol',
                 pista='amb les mans a la posició de Do',
                 passos=['Mà dreta: toca Do, Re, Mi, Fa, Sol amb els dits 1, 2, 3, 4, 5.',
                         'Mà esquerra: toca Do, Re, Mi, Fa, Sol amb els dits 5, 4, 3, 2, 1.',
                         'Ara de baixada: Sol, Fa, Mi, Re, Do. Canta el nom de cada nota!']),
            dict(tipus='joc', etiqueta='UN JOC AMB LA PROFE: LA NOTA AMAGADA',
                 text='La profe diu el nom d’una nota i tu la toques tan ràpid com puguis. '
                      'Primer amb la mà dreta, després amb l’esquerra!'),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='El Do és la nota més fàcil de trobar. Les altres sis venen darrere seu, en '
              'ordre!',
        fulles=[[
            dict(tipus='misol',
                 text='Primer, pinta la rodoneta del Do de color vermell. Després busca '
                      'tots els Do del teclat i pinta’ls també de vermell!'),
            dict(tipus='teclat_pinta', titol='Pinta tots els Do',
                 pista='recorda: a l’esquerra de les dues negres', pintar=['DO'],
                 tecles=15, alt=80),
            dict(tipus='cami', titol='El camí de les set germanes',
                 pista='pinta el camí seguint l’ordre: DO, RE, MI, FA, SOL, LA, SI, DO…',
                 files=5, columnes=7, cicle=TOTES, coneguts=TOTES, llavor=4, alt_fila=34,
                 cami=[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3),
                       (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6)]),
        ], [
            dict(tipus='uneix', titol='Quina ve després?',
                 pista='uneix cada nota amb la que va just després',
                 esquerra=['DO', 'MI', 'SOL', 'SI', 'RE'],
                 dreta=['LA', 'MI', 'DO', 'RE', 'FA']),
            dict(tipus='teclat_pinta', titol='Pinta i compta', tecles=15, alt=72,
                 pista='fes servir el color que diu cada consigna',
                 consignes=['Pinta de BLAU tots els grups de DUES tecles negres.',
                            'Encercla el Do central.',
                            'Quants Do hi ha en aquest teclat? Escriu-ho aquí: ____']),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Digues les set notes en ordre tan ràpid com puguis: Do, Re, Mi, Fa, '
                      'Sol, La, Si! Ara prova-ho al revés…'),
        ]],
    ),
)

# ==========================================================================
# CAPITOL 2 · EL PENTAGRAMA I LES CLAUS
# ==========================================================================
TEMES[5] = dict(
    titol='La casa de les notes',
    teoria=dict(
        intro='Les notes s’escriuen en una casa molt especial: el pentagrama. Té cinc '
              'línies i quatre espais, i es compten sempre de baix a dalt.',
        regles=['5 LÍNIES', '4 ESPAIS', 'DE BAIX A DALT'],
        fulles=[[
            dict(tipus='misol',
                 text='Aquesta és la casa de les notes! Com un edifici, té pisos: les '
                      'cinc línies i els quatre espais. I com als edificis, comptem des de '
                      'baix!'),
            dict(tipus='linies_espais', titol='Cinc línies i quatre espais',
                 peu='Una nota pot viure A UNA LÍNIA (la línia li passa per la panxa) o A '
                     'UN ESPAI (entre dues línies, ben encaixada).'),
            dict(tipus='targetes', titol='Dues maneres de viure', items=[
                ('A UNA LÍNIA', 'Travessada',
                 'La línia passa just pel mig de la nota.'),
                ('A UN ESPAI', 'Encaixada',
                 'La nota toca la línia de dalt i la de baix.'),
                ('DE BAIX A DALT', 'Comptem',
                 'La línia 1 és la de baix de tot.'),
            ]),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Al pentagrama, les notes que pugen sonen més agudes, i les que '
                      'baixen sonen més greus. Igual que al piano quan vas cap a la dreta!'),
            dict(tipus='pentagrama', titol='Pugen o baixen?', clau=None,
                 notes=[('E4', '1'), ('G4', '2'), ('B4', '3'), ('D5', '4'), ('F5', '5')],
                 peu='Aquestes notes viuen totes a les línies, de la 1 a la 5. Com més '
                     'amunt, més agut sona!'),
            dict(tipus='targetes', titol='Com es mouen les notes', items=[
                ('PUJA', 'Més amunt', 'Al piano, ves cap a la dreta.'),
                ('BAIXA', 'Més avall', 'Al piano, ves cap a l’esquerra.'),
                ('ES REPETEIX', 'Igual', 'Toca la mateixa tecla un altre cop.'),
            ]),
            dict(tipus='sabies',
                 text='«Penta» vol dir cinc, com les cinc puntes d’un pentàgon. Per això '
                      'la casa de cinc línies es diu PENTAgrama!'),
        ]],
    ),
    piano=dict(
        intro='Encara no sabem com es diuen les notes del pentagrama, però ja podem llegir '
              'si pugen, baixen o es repeteixen!',
        regles=['PUJA = DRETA', 'BAIXA = ESQUERRA', 'IGUAL = LA MATEIXA'],
        fulles=[[
            dict(tipus='misol',
                 text='Llegir música és com seguir un camí. No cal saber el nom de cada '
                      'nota: mira si va amunt, avall o es queda igual, i el teu dit la '
                      'segueix!'),
            dict(tipus='exercici', titol='Escales i escalons',
                 pista='mà dreta · comença al Do central amb el dit 1 · cada nota, un '
                       'escaló',
                 sistemes=[sis('C4 D4 E4 F4 | G4 F4 E4 D4 | C4 D4 E4 F4 | G4:w', 4)]),
            dict(tipus='exercici', titol='Iguals i diferents',
                 pista='mà dreta · comença al Do central · quan la nota es repeteix, '
                       'toques la mateixa tecla',
                 sistemes=[sis('C4 C4 D4 D4 | E4 E4 D4:h | C4 C4 D4 D4 | C4:w', 4)]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara la mà esquerra! Llegeix el camí de la mateixa manera: si puja, '
                      'ves a la dreta; si baixa, ves a l’esquerra.'),
            dict(tipus='exercici', titol='La mà esquerra puja i baixa',
                 pista='mà esquerra · comença al Do de baix amb el dit 5 · els escalons, '
                       'un a un',
                 sistemes=[sis('C3 D3 E3 F3 | G3 F3 E3 D3 | C3 D3 E3 D3 | C3:w', 4,
                               clau='bass')]),
            dict(tipus='exercici', titol='Un camí amb repeticions',
                 pista='mà esquerra · comença al Do de baix amb el dit 5',
                 sistemes=[sis('C3 C3 D3 E3 | E3 E3 D3:h | C3 D3 E3 E3 | D3 D3 C3:h', 4,
                               clau='bass')]),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='Línies i espais, de baix a dalt. Llapis a punt!',
        fulles=[[
            dict(tipus='misol',
                 text='Dibuixa una rodona a cada lloc que et diuen. Recorda: a la línia, la '
                      'línia la travessa; a l’espai, queda encaixada!'),
            dict(tipus='dibuixa', titol='Dibuixa la nota al seu lloc', clau=None,
                 pista='dibuixa una rodona just a sobre de cada etiqueta, al pis que diu',
                 noms=['línia 1', 'espai 2', 'línia 3', 'espai 4', 'línia 5', 'espai 1']),
            dict(tipus='encercla', titol='Encercla les notes que viuen a un espai',
                 clau=None, pista='les de les línies, deixa-les tranquil·les',
                 notes=['E4', 'F4', 'B4', 'C5', 'G4', 'A4', 'D5', 'E5', 'F5', 'D5']),
        ], [
            dict(tipus='vf', titol='Vertader o fals?',
                 pista='marca amb una creu la V o la F',
                 frases=['El pentagrama té cinc línies.',
                         'El pentagrama té cinc espais.',
                         'Les línies es compten de dalt a baix.',
                         'Si la nota puja, sona més aguda.',
                         'Una nota a un espai té una línia per la panxa.']),
            dict(tipus='quadre', etiqueta='DIBUIXA AQUÍ',
                 text='Dibuixa un edifici de cinc pisos i posa-hi una nota a cada finestra. '
                      'Quin pis és el més alt?'),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Amb els cinc dits d’una mà fes un pentagrama: cada dit és una línia. '
                      'Algú assenyala un dit o un forat i tu dius «línia 3» o «espai 2»!'),
        ]],
    ),
)

TEMES[6] = dict(
    titol='La clau de Sol',
    teoria=dict(
        intro='Al començament del pentagrama sempre hi ha una clau. La clau de Sol diu on '
              'viu el Sol, i és la clau de la mà dreta.',
        regles=['LA MÀ DRETA', 'EL SOL, A LA LÍNIA 2', 'S’ESCRIU DES DE LA LÍNIA 2'],
        fulles=[[
            dict(tipus='misol',
                 text='La clau de Sol té forma de caragol, i el seu caragol s’enrotlla a la '
                      'línia 2. Per això sap que el Sol viu a la línia 2!'),
            dict(tipus='clau', titol='La clau de Sol', clau='treble',
                 qui='la mà dreta',
                 com='Comença a la línia 2 i s’enrotlla al seu voltant. La nota d’aquesta '
                     'línia es diu Sol.'),
            dict(tipus='pentagrama', titol='El Sol de la mà dreta', clau='treble',
                 notes=[('G4', 'Sol'), ('G4', 'Sol'), ('G4', 'Sol')],
                 peu='Al piano, aquest Sol el toca el dit 5 de la mà dreta, a la posició de '
                     'Do. És la tecla blanca entre la primera i la segona negra del grup de '
                     'tres.'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='A la clau de Sol hi viuen les notes que toca la mà dreta: les més '
                      'agudes. La mà esquerra tindrà la seva pròpia clau. Ja ho veuràs!'),
            dict(tipus='teclat', titol='On és el Sol al piano', tecles=15, grups=True,
                 ressalta=[4, 11], etiquetes={4: 'SOL', 11: 'SOL'}, alt=84,
                 peu='Busca el grup de TRES negres: el Sol és la tecla blanca entre la '
                     'primera i la segona negra.'),
            dict(tipus='nota', etiqueta='COM ES DIBUIXA',
                 text='Comença al mig, a la línia 2, fes un caragol, puja fins dalt de tot i '
                      'baixa fent una línia llarga com un bastó. Prova-ho a l’aire amb el '
                      'dit!'),
            dict(tipus='sabies',
                 text='Fa molts anys, la clau de Sol era una lletra G (que vol dir Sol). A '
                      'base de dibuixar-la ràpid, es va anar enrotllant fins a fer-se el '
                      'caragol que veiem ara!'),
        ]],
    ),
    piano=dict(
        intro='La mà dreta toca el seu primer Sol llegint-lo al pentagrama.',
        regles=['MÀ DRETA A CASA', 'SOL = DIT 5', 'COMPTA EN VEU ALTA'],
        fulles=[[
            dict(tipus='misol',
                 text='Posa la mà dreta a la posició de Do: el polze al Do central. El dit 5 '
                      'ha caigut just a sobre del Sol. Quina sort!'),
            dict(tipus='exercici', titol='El Sol fa ta, ta, ta',
                 pista='mà dreta · dit 5 · una nota per cada «ta» · la nota buida '
                       'aguanta més',
                 sistemes=[sis('G4 G4 G4 G4 | G4 G4 G4:h | G4 G4 G4 G4 | G4:w', 4)]),
            dict(tipus='exercici', titol='Del Do al Sol',
                 pista='mà dreta · el dit 1 toca el Do i el dit 5 toca el Sol · un salt!',
                 sistemes=[sis('C4 C4 G4 G4 | C4 C4 G4:h | C4 G4 C4 G4 | C4:w', 4)]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ja llegeixes el Do i el Sol! Els reconeixes de seguida: el Do porta '
                      'una ratlleta i el Sol viu a la línia 2.'),
            dict(tipus='exercici', titol='Pujem pels escalons fins al Sol',
                 pista='mà dreta · dits 1, 2, 3, 4, 5 · i baixem',
                 sistemes=[sis('C4 D4 E4 F4 | G4:w | G4 F4 E4 D4 | C4:w', 4)]),
            dict(tipus='joc', etiqueta='UN JOC AMB LA PROFE: SOL O NO SOL?',
                 text='La profe toca notes amb la mà dreta. Cada vegada que sona el Sol, '
                      'pica de mans. Després, intenta-ho amb els ulls tancats!'),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='La clau de Sol i el seu Sol: troba’ls, compta’ls i encercla’ls.',
        fulles=[[
            dict(tipus='misol',
                 text='El Sol viu a la línia 2. Busca tots els Sol del pentagrama i '
                      'encercla’ls. Compte, que n’hi ha d’amagats!'),
            dict(tipus='encercla', titol='Encercla tots els Sol', clau='treble',
                 pista='la línia 2 passa per la panxa del Sol',
                 notes=['G4', 'E4', 'G4', 'B4', 'G4', 'F4', 'G4', 'A4', 'D5', 'G4']),
            dict(tipus='compta', titol='Compta els Sol i els Do', clau='treble',
                 pista='escriu el número i pinta el cercle del seu color',
                 notes=['G4', 'C4', 'G4', 'G4', 'C4', 'G4', 'C4', 'G4', 'G4', 'C4'],
                 quines=['SOL', 'DO']),
        ], [
            dict(tipus='endevina', titol='Endevina qui sóc',
                 pista='escriu una lletra a cada caixeta',
                 items=[('Sóc la clau de la mà dreta i tinc forma de caragol.', 'SOL'),
                        ('Tinc cinc línies i quatre espais.', 'PENTAGRAMA'),
                        ('Visc a la línia 2 de la clau de Sol.', 'SOL'),
                        ('Sóc la mà que llegeix en clau de Sol.', 'DRETA')]),
            dict(tipus='pauta_buida', etiqueta='DIBUIXA CLAUS DE SOL',
                 text='Fes tres claus de '
                      'Sol. Comença sempre a la línia 2!'),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Dibuixa una clau de Sol a l’esquena d’algú de casa amb el dit. '
                      'Endevina-ho? Ara canvieu!'),
        ]],
    ),
)

TEMES[7] = dict(
    titol='La clau de Fa',
    teoria=dict(
        intro='La mà esquerra també té la seva clau: la clau de Fa. Amb ella llegeix les '
              'notes greus, les de l’ós.',
        regles=['LA MÀ ESQUERRA', 'EL FA, A LA LÍNIA 4', 'ENTRE ELS DOS PUNTS'],
        fulles=[[
            dict(tipus='misol',
                 text='La clau de Fa sembla una orella amb dos punts. Els dos punts '
                      'abracen la línia 4: allà viu el Fa!'),
            dict(tipus='clau', titol='La clau de Fa', clau='bass',
                 qui='la mà esquerra',
                 com='Comença amb un punt gros a la línia 4 i té dos puntets, un a cada '
                     'banda de la línia. La nota d’aquesta línia es diu Fa.'),
            dict(tipus='pentagrama', titol='El Fa de la mà esquerra', clau='bass',
                 notes=[('F3', 'Fa'), ('F3', 'Fa'), ('F3', 'Fa')],
                 peu='Al piano, aquest Fa el toca el dit 2 de la mà esquerra, a la posició '
                     'de Do. És la tecla blanca a l’esquerra del grup de tres negres.'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara ja tens dues claus! La clau de Sol per a la mà dreta i la clau de '
                      'Fa per a la mà esquerra. Cada mà llegeix la seva!'),
            dict(tipus='teclat', titol='On és el Fa al piano', tecles=15, grups=True,
                 ressalta=[3, 10], etiquetes={3: 'FA', 10: 'FA'}, alt=84,
                 peu='Busca el grup de TRES negres: el Fa és la tecla blanca just a '
                     'l’esquerra.'),
            dict(tipus='targetes', titol='Dues claus, dues mans', items=[
                ('MÀ DRETA', 'Clau de Sol',
                 'Notes agudes. El Sol viu a la línia 2.'),
                ('MÀ ESQUERRA', 'Clau de Fa',
                 'Notes greus. El Fa viu a la línia 4.'),
                ('COMPTE!', 'No són iguals',
                 'La mateixa línia té un nom diferent a cada clau.'),
            ]),
            dict(tipus='sabies',
                 text='La clau de Fa també era una lletra: la F, que vol dir Fa. Si la mires '
                      'bé, encara s’hi veu una mica!'),
        ]],
    ),
    piano=dict(
        intro='La mà esquerra llegeix la seva primera nota en clau de Fa.',
        regles=['MÀ ESQUERRA A CASA', 'FA = DIT 2', 'DO = DIT 5'],
        fulles=[[
            dict(tipus='misol',
                 text='Posa la mà esquerra a la posició de Do: el dit 5 al Do de baix. El '
                      'dit 2 queda sobre el Fa. Ja el pots tocar!'),
            dict(tipus='exercici', titol='El Fa de la mà esquerra',
                 pista='mà esquerra · dit 2 · una nota per cada «ta»',
                 sistemes=[sis('F3 F3 F3 F3 | F3 F3 F3:h | F3 F3 F3 F3 | F3:w', 4,
                               clau='bass')]),
            dict(tipus='exercici', titol='Del Do al Fa',
                 pista='mà esquerra · el dit 5 toca el Do (a l’espai 2) i el dit 2 toca el '
                       'Fa (a la línia 4)',
                 sistemes=[sis('C3 C3 F3 F3 | C3 C3 F3:h | C3 F3 C3 F3 | C3:w', 4,
                               clau='bass')]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara les dues mans parlen per torns: la dreta toca el Sol i '
                      'l’esquerra li contesta amb el Fa. Pregunta i resposta!'),
            dict(tipus='exercici', titol='Pregunta i resposta',
                 pista='primer la mà dreta (a dalt), després la mà esquerra (a baix)',
                 sistemes=[sis('G4 G4 G4:h | G4 G4 G4:h', 2, cap='a) la mà dreta pregunta'),
                           sis('F3 F3 F3:h | F3 F3 F3:h', 2, clau='bass',
                               cap='b) la mà esquerra respon')]),
            dict(tipus='exercici', titol='La mà esquerra puja fins al Fa',
                 pista='mà esquerra · dits 5, 4, 3, 2 · i tornem a baixar',
                 sistemes=[sis('C3 D3 E3 F3 | F3 E3 D3 C3 | C3 D3 E3 F3 | C3:w', 4,
                               clau='bass')]),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='La clau de Fa és nova: dibuixa-la, troba el Fa i uneix cada clau amb la seva '
              'mà.',
        fulles=[[
            dict(tipus='misol',
                 text='El Fa viu a la línia 4, entre els dos puntets de la clau. Dibuixa una '
                      'rodona allà on et diuen!'),
            dict(tipus='dibuixa', titol='Dibuixa el Fa', clau='bass',
                 pista='dibuixa una rodona a la línia 4 a sobre de cada «Fa»',
                 noms=['Fa', 'Fa', 'Fa', 'Fa', 'Fa', 'Fa']),
            dict(tipus='uneix', titol='Cada clau, amb la seva mà',
                 pista='uneix els punts amb una ratlla',
                 esquerra=['Clau de Sol', 'Clau de Fa', 'Línia 2', 'Línia 4'],
                 dreta=['hi viu el Fa (clau de Fa)', 'mà dreta', 'mà esquerra',
                        'hi viu el Sol (clau de Sol)']),
        ], [
            dict(tipus='vf', titol='Vertader o fals?',
                 pista='marca amb una creu la V o la F',
                 frases=['La mà esquerra llegeix en clau de Fa.',
                         'La clau de Fa té dos puntets.',
                         'En clau de Fa, el Fa viu a la línia 2.',
                         'La clau de Sol és per a la mà dreta.',
                         'Les dues claus són iguals.']),
            dict(tipus='pauta_buida', etiqueta='DIBUIXA CLAUS DE FA',
                 text='Fes tres claus de '
                      'Fa. No t’oblidis dels dos puntets a banda i banda de la línia 4!'),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Algú diu «Sol!» o «Fa!». Si diu Sol, aixeca la mà dreta; si diu Fa, '
                      'aixeca l’esquerra. Cada vegada més ràpid!'),
        ]],
    ),
)

TEMES[8] = dict(
    titol='El gran pentagrama',
    teoria=dict(
        intro='La música de piano s’escriu en dos pentagrames units: a dalt, la clau de '
              'Sol per a la mà dreta; a baix, la clau de Fa per a l’esquerra.',
        regles=['DALT: MÀ DRETA', 'BAIX: MÀ ESQUERRA', 'AL MIG: EL DO CENTRAL'],
        fulles=[[
            dict(tipus='misol',
                 text='Mira quin pentagrama tan gran! Són dos pentagrames abraçats per una '
                      'clau llarga. Es llegeixen alhora, com dues mans que toquen juntes.'),
            dict(tipus='gran', titol='El gran pentagrama del piano',
                 notes=[('G4', 'treble', 'Sol'), ('C4', 'treble', 'Do central'),
                        ('F3', 'bass', 'Fa'), ('C3', 'bass', 'Do')],
                 peu='El Do central porta una ratlleta: és la nota que queda just al mig '
                     'dels dos pentagrames.'),
            dict(tipus='targetes', titol='Tres notes que ja coneixes', items=[
                ('MÀ DRETA', 'Sol', 'A la línia 2 de la clau de Sol.'),
                ('AL MIG', 'Do central', 'Amb una ratlleta, sota la clau de Sol.'),
                ('MÀ ESQUERRA', 'Fa', 'A la línia 4 de la clau de Fa.'),
            ]),
        ], [
            dict(tipus='misol', pose='happy',
                 text='A la posició de Do, la mà dreta posa el polze al Do central. La mà '
                      'esquerra posa el dit 5 al Do de baix, que viu a l’espai 2 de la clau '
                      'de Fa.'),
            dict(tipus='mans', titol='La posició de Do', teclats=[DO_ESQUERRA, DO_DRETA],
                 peu='Les dues mans miren cap al centre i entre elles queden dos Dos. El '
                     'de l’esquerra és més greu: és el Do de baix.'),
            dict(tipus='nota', etiqueta='RECORDA',
                 text='Al gran pentagrama, el que està escrit a dalt ho toca la mà dreta i '
                      'el que està escrit a baix ho toca la mà esquerra. Sempre!'),
            dict(tipus='sabies',
                 text='La clau llarga que uneix els dos pentagrames del piano s’anomena '
                      '«clau de sistema». Si la veus, ja saps que és música per a dues mans!'),
        ]],
    ),
    piano=dict(
        intro='Llegim les tres notes que ja sabem al gran pentagrama, i toquem per primer '
              'cop amb les dues mans alhora.',
        regles=['POSICIÓ DE DO', 'DALT DRETA · BAIX ESQUERRA', 'ESCOLTA LES DUES MANS'],
        fulles=[[
            dict(tipus='misol',
                 text='Les dues mans a la posició de Do. La dreta toca el Do central i el '
                      'Sol. L’esquerra toca el Do de baix i el Fa.'),
            dict(tipus='exercici', titol='La mà dreta: Do i Sol',
                 pista='mà dreta · dit 1 al Do central, dit 5 al Sol',
                 sistemes=[sis('C4 G4 C4 G4 | C4 C4 G4:h | G4 G4 C4 C4 | C4:w', 4)]),
            dict(tipus='exercici', titol='La mà esquerra: Do i Fa',
                 pista='mà esquerra · dit 5 al Do, dit 2 al Fa',
                 sistemes=[sis('C3 F3 C3 F3 | C3 C3 F3:h | F3 F3 C3 C3 | C3:w', 4,
                               clau='bass')]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara les dues mans alhora! Les dues toquen un Do: la dreta amb el '
                      'polze i l’esquerra amb el dit 5. Sona com una campana!'),
            dict(tipus='exercici', titol='La campana dels dos Dos',
                 pista='les dues mans alhora · la dreta toca el de dalt i l’esquerra el '
                       'de baix',
                 sistemes=[sis('[C3+C4]:h [C3+C4]:h | [C3+C4]:w | [C3+C4] [C3+C4] '
                               '[C3+C4]:h | [C3+C4]:w', 4)]),
            dict(tipus='joc', etiqueta='UN JOC AMB LA PROFE: DALT O BAIX?',
                 text='La profe assenyala una nota del gran pentagrama. Si és a dalt, la '
                      'toques amb la mà dreta; si és a baix, amb l’esquerra!'),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='Dalt la mà dreta, baix la mà esquerra. Relaciona, busca i pinta!',
        fulles=[[
            dict(tipus='misol',
                 text='Mira bé la clau de cada pentagrama abans de dir el nom de la nota. '
                      'La mateixa línia no es diu igual a les dues claus!'),
            dict(tipus='relaciona', titol='Cada nota amb la seva tecla',
                 pista='uneix cada nota amb la tecla que té el punt',
                 notes=[('G4', 'treble'), ('F3', 'bass'), ('C4', 'treble')],
                 tecles=['F3', 'C4', 'G4']),
            dict(tipus='teclat_pinta', titol='Pinta les notes que ja coneixes',
                 pista='pinta cada tecla del seu color', pintar=['DO', 'FA', 'SOL'],
                 tecles=15, alt=72),
        ], [
            dict(tipus='sopa', titol='Sopa de lletres de les claus',
                 pista='busca les paraules i marca la caixeta',
                 paraules=['CLAU', 'SOL', 'FA', 'DO', 'LÍNIA', 'ESPAI', 'NOTA'],
                 llavor=8),
            dict(tipus='quadre', etiqueta='DIBUIXA AQUÍ',
                 text='Dibuixa un gran pentagrama: dos pentagrames, '
                      'una clau de Sol a dalt, una clau de Fa a baix i la clau llarga que '
                      'els uneix.'),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Ensenya a algú de casa on viuen el Sol, el Fa i el Do central al gran '
                      'pentagrama. Ara ets tu el profe!'),
        ]],
    ),
)

# ==========================================================================
# CAPITOL 3 · LES NOTES I ELS SEUS COLORS
# ==========================================================================
HCB_DRETA = 'E4 D4 C4:h | E4 D4 C4:h | C4 C4 D4 D4 | E4 D4 C4:h'
HCB_ESQUERRA = 'E3 D3 C3:h | E3 D3 C3:h | C3 C3 D3 D3 | E3 D3 C3:h'

TEMES[9] = dict(
    titol='Do, Re i Mi',
    teoria=dict(
        intro='Les nostres tres primeres notes, i les dues mans les aprenen alhora: la '
              'dreta en clau de Sol i l’esquerra en clau de Fa.',
        regles=['DO · RE · MI', 'MÀ DRETA: DITS 1-2-3', 'MÀ ESQUERRA: DITS 5-4-3'],
        fulles=[[
            dict(tipus='misol',
                 text='Avui coneixerem tres amigues que sempre van juntes: el Do, el Re i '
                      'el Mi. Si saps on viu el Do, les altres dues són just al costat!'),
            dict(tipus='mans', titol='On van els dits',
                 teclats=[dict(DO_ESQUERRA, n=3, dits={0: 5, 1: 4, 2: 3}),
                          dict(DO_DRETA, n=3, dits={0: 1, 1: 2, 2: 3})],
                 peu='La dreta toca Do-Re-Mi amb els dits 1, 2, 3. L’esquerra, amb els '
                     'dits 5, 4, 3. Els números són diferents, però les notes són les '
                     'mateixes!'),
            dict(tipus='pentagrama', titol='A la clau de Sol (mà dreta)', clau='treble',
                 notes=[('C4', 'Do'), ('D4', 'Re'), ('E4', 'Mi')],
                 peu='El Do porta una ratlleta, el Re penja sota el pentagrama i el Mi '
                     'viu a la línia 1.'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='A la clau de Fa, les tres notes viuen més amunt del pentagrama, però '
                      'també van una darrere l’altra, com tres escalons!'),
            dict(tipus='pentagrama', titol='A la clau de Fa (mà esquerra)', clau='bass',
                 notes=[('C3', 'Do'), ('D3', 'Re'), ('E3', 'Mi')],
                 peu='El Do viu a l’espai 2, el Re a la línia del mig (la 3) i el Mi a '
                     'l’espai 3.'),
            dict(tipus='escala', titol='L’escala Do-Re-Mi', notes=['Do', 'Re', 'Mi'],
                 peu='Pinta el cercle de cada escaló del seu color: DO vermell, RE taronja '
                     'i MI groc.'),
            dict(tipus='sabies',
                 text='Els noms Do, Re i Mi vénen d’una cançó de fa més de mil anys: cada '
                      'nota començava amb una síl·laba d’una frase en llatí. I al principi '
                      'el Do no es deia Do, sinó «Ut»!'),
        ]],
    ),
    piano=dict(
        intro='Primer amb la mà dreta, després amb l’esquerra, i al final una cançó de '
              'veritat amb totes dues.',
        regles=['DRETA: 1-2-3', 'ESQUERRA: 5-4-3', 'A POC A POC I CANTANT'],
        fulles=[[
            dict(tipus='misol',
                 text='Abans de tocar, posa els dits a casa. A la mà dreta, el polze al Do '
                      'central. A la mà esquerra, el dit 5 al Do de baix. I no es mouen!'),
            dict(tipus='exercici', titol='La mà dreta puja i baixa',
                 pista='dits 1, 2 i 3 · canta el nom de cada nota mentre la toques',
                 sistemes=[sis('C4 D4 E4 D4 | C4 D4 E4:h | E4 D4 C4 D4 | C4:w', 4)]),
            dict(tipus='exercici', titol='La mà esquerra puja i baixa',
                 pista='dits 5, 4 i 3 · en clau de Fa · canta el nom de cada nota',
                 sistemes=[sis('C3 D3 E3 D3 | C3 D3 E3:h | E3 D3 C3 D3 | C3:w', 4,
                               clau='bass')]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy', etiqueta='EN MUSSOL MISOL CANTA',
                 text='Ja saps tres notes amb les dues mans! Ara les posem juntes en una '
                      'cançó de veritat. Primer canta-la, i després toca-la.'),
            dict(tipus='exercici', titol='La meva primera cançó',
                 pista='Hot Cross Buns · cançó popular anglesa',
                 sistemes=[sis(HCB_DRETA, 4, cap='a) amb la mà dreta, en clau de Sol'),
                           sis(HCB_ESQUERRA, 4, clau='bass',
                               cap='b) amb la mà esquerra, en clau de Fa')]),
            dict(tipus='joc', etiqueta='UN JOC AMB LA PROFE: L’ECO',
                 text='La profe toca tres notes amb una mà i tu les repeteixes amb la '
                      'mateixa mà, com un eco. Després canvieu de mà!'),
            dict(tipus='estrelles', etiqueta='CADA DIA QUE TOQUIS LA CANÇÓ, PINTA UNA '
                                             'ESTRELLA'),
        ]],
    ),
    fitxa=dict(
        intro='Agafa un llapis i els teus colors. Do vermell, Re taronja i Mi groc!',
        fulles=[[
            dict(tipus='misol',
                 text='Primer pinta les rodonetes de la llegenda. Després escriu el nom de '
                      'cada nota a la caixeta i pinta-la del seu color.'),
            dict(tipus='pinta', titol='La mà dreta: escriu i pinta', clau='treble',
                 pista='escriu DO, RE o MI a la caixeta i pinta la nota',
                 llegenda=['DO', 'RE', 'MI'],
                 notes=['C4', 'E4', 'D4', 'C4', 'E4', 'D4', 'E4', 'C4']),
            dict(tipus='pinta', titol='La mà esquerra: escriu i pinta', clau='bass',
                 pista='compte: és la clau de Fa! El Do viu a l’espai 2',
                 llegenda=['DO', 'RE', 'MI'],
                 notes=['D3', 'C3', 'E3', 'D3', 'C3', 'E3', 'C3', 'D3']),
        ], [
            dict(tipus='compta', titol='Compta i pinta', clau='bass',
                 pista='mà esquerra · quantes n’hi ha de cada? Escriu el número',
                 notes=['C3', 'E3', 'E3', 'D3', 'C3', 'E3', 'D3', 'E3', 'C3', 'E3'],
                 quines=['DO', 'RE', 'MI']),
            dict(tipus='cami', titol='Ajuda en Mussol Misol',
                 pista='pinta el camí trepitjant les notes en ordre: DO, RE, MI, DO, RE, '
                       'MI… fins al piano',
                 files=4, columnes=7, cicle=['DO', 'RE', 'MI'],
                 coneguts=['DO', 'RE', 'MI', 'FA', 'SOL'], llavor=9,
                 cami=[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4),
                       (1, 4), (1, 5), (1, 6), (2, 6), (3, 6)]),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Canta Do-Re-Mi pujant o Mi-Re-Do baixant, sense dir quin. Qui està '
                      'amb tu endevina si puges o baixes!'),
        ]],
    ),
)

ODA_DRETA = ('E4 E4 F4 G4 | G4 F4 E4 D4 | C4 C4 D4 E4 | E4 D4 D4:h | '
             'E4 E4 F4 G4 | G4 F4 E4 D4 | C4 C4 D4 E4 | D4 C4 C4:h')
ODA_ESQUERRA = ('E3 E3 F3 G3 | G3 F3 E3 D3 | C3 C3 D3 E3 | E3 D3 D3:h | '
                'E3 E3 F3 G3 | G3 F3 E3 D3 | C3 C3 D3 E3 | D3 C3 C3:h')

TEMES[10] = dict(
    titol='Fa i Sol',
    teoria=dict(
        intro='Dues notes més i ja tenim la mà sencera: Do, Re, Mi, Fa i Sol. Cinc dits, '
              'cinc notes!',
        regles=['DO · RE · MI · FA · SOL', 'UN DIT PER NOTA', 'LA POSICIÓ DE DO'],
        fulles=[[
            dict(tipus='misol',
                 text='El Fa i el Sol ja els coneixes de les claus! Ara els posem al costat '
                      'del Do, el Re i el Mi. Cinc notes seguides, una per a cada dit.'),
            dict(tipus='mans', titol='La posició de Do sencera',
                 teclats=[DO_ESQUERRA, DO_DRETA],
                 peu='Mà dreta: Do 1, Re 2, Mi 3, Fa 4, Sol 5. Mà esquerra: Do 5, Re 4, '
                     'Mi 3, Fa 2, Sol 1.'),
            dict(tipus='pentagrama', titol='Cinc notes a la clau de Sol', clau='treble',
                 notes=[('C4', 'Do'), ('D4', 'Re'), ('E4', 'Mi'), ('F4', 'Fa'),
                        ('G4', 'Sol')],
                 peu='El Fa viu a l’espai 1 i el Sol, a la línia 2.'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara a la clau de Fa. Mira com pugen: espai, línia, espai, línia, '
                      'espai. Línia i espai, línia i espai… com una escala!'),
            dict(tipus='pentagrama', titol='Cinc notes a la clau de Fa', clau='bass',
                 notes=[('C3', 'Do'), ('D3', 'Re'), ('E3', 'Mi'), ('F3', 'Fa'),
                        ('G3', 'Sol')],
                 peu='El Fa viu a la línia 4, entre els dos puntets de la clau, i el Sol, '
                     'a l’espai 4.'),
            dict(tipus='escala', titol='L’escala de la mà',
                 notes=['Do', 'Re', 'Mi', 'Fa', 'Sol'],
                 peu='Pinta cada escaló del seu color: el FA verd i el SOL blau.'),
            dict(tipus='nota', etiqueta='EL TRUC DE LA LÍNIA I L’ESPAI',
                 text='Quan les notes van seguides, sempre alternen: una a una línia, la '
                      'següent a un espai. Si te’n saltes una, vas de línia a línia!'),
        ]],
    ),
    piano=dict(
        intro='Cinc dits, cinc notes, dues mans. I una melodia famosa de veritat!',
        regles=['POSICIÓ DE DO', 'CADA DIT, LA SEVA NOTA', 'CANTA EL NOM'],
        fulles=[[
            dict(tipus='misol',
                 text='Les dues mans a la posició de Do. Cada dit té la seva tecla i no es '
                      'mou de casa en tota la pàgina!'),
            dict(tipus='exercici', titol='Cinc escalons amb la mà dreta',
                 pista='dits 1-2-3-4-5 i tornem a baixar',
                 sistemes=[sis('C4 D4 E4 F4 | G4 F4 E4 D4 | C4 E4 D4 F4 | E4 G4 G4:h', 4)]),
            dict(tipus='exercici', titol='Cinc escalons amb la mà esquerra',
                 pista='dits 5-4-3-2-1 · en clau de Fa',
                 sistemes=[sis('C3 D3 E3 F3 | G3 F3 E3 D3 | C3 E3 D3 F3 | E3 G3 G3:h', 4,
                               clau='bass')]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy', etiqueta='EN MUSSOL MISOL CANTA',
                 text='Aquesta melodia la va escriure en Beethoven fa dos-cents anys i tot '
                      'el món la coneix. I ara tu també la pots tocar!'),
            dict(tipus='exercici', titol='L’Oda a l’alegria',
                 pista='Beethoven · simplificada · primer la mà dreta, després l’esquerra',
                 sistemes=[sis(ODA_DRETA, 4, cap='a) mà dreta, en clau de Sol'),
                           sis(ODA_ESQUERRA, 4, clau='bass',
                               cap='b) mà esquerra, en clau de Fa · són les mateixes notes!')]),
            dict(tipus='estrelles', etiqueta='CADA DIA QUE TOQUIS L’ODA, PINTA UNA '
                                             'ESTRELLA'),
        ]],
    ),
    fitxa=dict(
        intro='Fa verd i Sol blau. Ja tens cinc colors!',
        fulles=[[
            dict(tipus='misol',
                 text='Mira la clau abans de començar! A la clau de Sol i a la de Fa, la '
                      'mateixa línia no és la mateixa nota.'),
            dict(tipus='relaciona', titol='Cada nota amb la seva tecla',
                 pista='uneix cada nota amb la tecla que té el punt · mira la clau!',
                 notes=[('F4', 'treble'), ('G3', 'bass'), ('E4', 'treble'), ('F3', 'bass')],
                 tecles=['E4', 'F3', 'G3', 'F4']),
            dict(tipus='encercla', titol='Encercla els Fa i els Sol', clau='bass',
                 pista='mà esquerra · pinta de verd els Fa i de blau els Sol',
                 notes=['F3', 'C3', 'G3', 'E3', 'F3', 'D3', 'G3', 'F3', 'C3', 'G3']),
        ], [
            dict(tipus='dibuixa', titol='Dibuixa la nota a la clau de Sol', clau='treble',
                 pista='dibuixa una rodona a sobre de cada nom, al seu lloc',
                 noms=['Do', 'Mi', 'Sol', 'Re', 'Fa', 'Sol', 'Mi']),
            dict(tipus='teclat_pinta', titol='Pinta la posició de Do',
                 pista='pinta les cinc tecles de la mà dreta del seu color',
                 pintar=['DO', 'RE', 'MI', 'FA', 'SOL'], tecles=12, alt=72),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Taral·leja l’Oda a l’alegria a algú de casa. Sap com es diu? Ara '
                      'canta-la amb els noms de les notes!'),
        ]],
    ),
)

AU_SOL_DRETA = 'G4 G4 G4 A4 | B4:h A4:h | G4 B4 A4 A4 | G4:w'
AU_SOL_ESQUERRA = 'G2 G2 G2 A2 | B2:h A2:h | G2 B2 A2 A2 | G2:w'

TEMES[11] = dict(
    titol='La i Si',
    teoria=dict(
        intro='Les dues últimes germanes! Per arribar-hi, la mà fa un viatge: passa de la '
              'posició de Do a la posició de Sol.',
        regles=['LA · SI', 'POSICIÓ DE SOL', 'DUES MANS, DUES CLAUS'],
        fulles=[[
            dict(tipus='misol',
                 text='Per tocar el La i el Si, movem la mà: el polze de la dreta se’n va '
                      'al Sol. És la posició de Sol, i té cinc notes noves per jugar!'),
            dict(tipus='mans', titol='La posició de Sol',
                 teclats=[SOL_ESQUERRA, SOL_DRETA],
                 peu='Mà dreta: Sol 1, La 2, Si 3, Do 4, Re 5. Mà esquerra: Sol 5, La 4, '
                     'Si 3, Do 2, Re 1.'),
            dict(tipus='pentagrama', titol='La i Si a la clau de Sol', clau='treble',
                 notes=[('G4', 'Sol'), ('A4', 'La'), ('B4', 'Si')],
                 peu='El La viu a l’espai 2 i el Si, a la línia del mig (la 3).'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='La mà esquerra baixa fins al Sol més greu. A la clau de Fa, aquest Sol '
                      'viu a la línia 1, a baix de tot!'),
            dict(tipus='pentagrama', titol='La i Si a la clau de Fa', clau='bass',
                 notes=[('G2', 'Sol'), ('A2', 'La'), ('B2', 'Si')],
                 peu='El Sol viu a la línia 1, el La a l’espai 1 i el Si a la línia 2.'),
            dict(tipus='targetes', titol='Les dues noves', items=[
                ('LILA', 'La', 'Al piano, entre la segona i la tercera negra del grup de '
                               'tres.'),
                ('GRIS', 'Si', 'Al piano, just a la dreta del grup de tres negres.'),
                ('I DESPRÉS?', 'Do', 'Després del Si, torna a començar el Do!'),
            ]),
            dict(tipus='sabies',
                 text='El Si va ser l’última nota a tenir nom: durant molts anys només n’hi '
                      'havia sis! El van anomenar amb les inicials de Sant Joan en llatí, '
                      '«Sancte Ioannes».'),
        ]],
    ),
    piano=dict(
        intro='Viatgem a la posició de Sol i toquem cançons que ja coneixem… en un altre '
              'lloc del piano!',
        regles=['DRETA: POLZE AL SOL', 'ESQUERRA: DIT 5 AL SOL', 'MANS A CASA NOVA'],
        fulles=[[
            dict(tipus='misol',
                 text='Mà dreta: el polze al Sol. Mà esquerra: el dit 5 al Sol més greu. Ja '
                      'esteu a la casa nova!'),
            dict(tipus='exercici', titol='Sol, La i Si amb la mà dreta',
                 pista='dits 1, 2 i 3 · en clau de Sol',
                 sistemes=[sis('G4 A4 B4 A4 | G4 A4 B4:h | B4 A4 G4 A4 | G4:w', 4)]),
            dict(tipus='exercici', titol='Sol, La i Si amb la mà esquerra',
                 pista='dits 5, 4 i 3 · en clau de Fa',
                 sistemes=[sis('G2 A2 B2 A2 | G2 A2 B2:h | B2 A2 G2 A2 | G2:w', 4,
                               clau='bass')]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy', etiqueta='EN MUSSOL MISOL CANTA',
                 text='Aquesta cançó francesa té més de dos-cents anys. Explica la història '
                      'd’en Pierrot, que demana una ploma sota la llum de la lluna.'),
            dict(tipus='exercici', titol='Au clair de la lune',
                 pista='cançó popular francesa · a la posició de Sol',
                 sistemes=[sis(AU_SOL_DRETA, 4, cap='a) mà dreta, en clau de Sol'),
                           sis(AU_SOL_ESQUERRA, 4, clau='bass',
                               cap='b) mà esquerra, en clau de Fa')]),
            dict(tipus='exercici', titol='Hot Cross Buns a la casa nova',
                 pista='la cançó del tema 9, ara a la posició de Sol · mà dreta',
                 sistemes=[sis('B4 A4 G4:h | B4 A4 G4:h | G4 G4 A4 A4 | B4 A4 G4:h', 4)]),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='La lila i Si gris. Ja tens els set colors de l’arc de Sant Martí musical!',
        fulles=[[
            dict(tipus='misol',
                 text='A la clau de Fa, el Sol de baix viu a la línia 1. Escriu el nom de '
                      'cada nota i pinta-la del seu color!'),
            dict(tipus='pinta', titol='La mà esquerra: escriu i pinta', clau='bass',
                 pista='escriu SOL, LA o SI a la caixeta i pinta la nota',
                 llegenda=['SOL', 'LA', 'SI'],
                 notes=['G2', 'B2', 'A2', 'G2', 'A2', 'B2', 'B2', 'G2']),
            dict(tipus='pinta', titol='La mà dreta: escriu i pinta', clau='treble',
                 pista='escriu SOL, LA o SI a la caixeta i pinta la nota',
                 llegenda=['SOL', 'LA', 'SI'],
                 notes=['A4', 'G4', 'B4', 'A4', 'G4', 'B4', 'A4', 'G4']),
        ], [
            dict(tipus='cami', titol='El camí de la posició de Sol',
                 pista='pinta el camí en ordre: SOL, LA, SI, SOL, LA, SI… fins al piano',
                 files=4, columnes=7, cicle=['SOL', 'LA', 'SI'], coneguts=TOTES,
                 llavor=12,
                 cami=[(3, 0), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (2, 3), (2, 4),
                       (2, 5), (1, 5), (0, 5), (0, 6)]),
            dict(tipus='endevina', titol='Endevina quina nota sóc',
                 pista='escriu el nom de la nota a les caixetes',
                 items=[('A la clau de Sol visc a la línia del mig.', 'SI'),
                        ('Sóc de color lila.', 'LA'),
                        ('A la clau de Fa visc a la línia 1.', 'SOL'),
                        ('Després de mi torna a començar el Do.', 'SI')]),
        ]],
    ),
)

TEMES[12] = dict(
    titol='Les set notes',
    teoria=dict(
        intro='Ja les coneixes totes! Set notes, set colors, i es repeteixen per tot el '
              'piano i per tot el pentagrama.',
        regles=['DO RE MI FA SOL LA SI', 'I TORNA EL DO', 'DUES POSICIONS'],
        fulles=[[
            dict(tipus='misol', pose='happy',
                 text='Felicitats! Ja saps les set notes de la música. Totes les cançons '
                      'del món, absolutament totes, es fan amb aquestes set notes.'),
            dict(tipus='escala', titol='L’escala de les set notes',
                 notes=['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'],
                 peu='Pinta cada escaló del seu color. És l’arc de Sant Martí de la música!'),
            dict(tipus='pentagrama', titol='Les set notes a la clau de Sol', clau='treble',
                 notes=[('C4', 'Do'), ('D4', 'Re'), ('E4', 'Mi'), ('F4', 'Fa'),
                        ('G4', 'Sol'), ('A4', 'La'), ('B4', 'Si')],
                 peu='Del Do central al Si: línia i espai, línia i espai… com una escala.'),
        ], [
            dict(tipus='misol',
                 text='A la clau de Fa també hi caben totes. Les dues posicions de la mà '
                      'esquerra, la de Sol i la de Do, juntes fan les set notes!'),
            dict(tipus='pentagrama', titol='Les set notes a la clau de Fa', clau='bass',
                 notes=[('G2', 'Sol'), ('A2', 'La'), ('B2', 'Si'), ('C3', 'Do'),
                        ('D3', 'Re'), ('E3', 'Mi'), ('F3', 'Fa')],
                 peu='Del Sol de la línia 1 fins al Fa de la línia 4. Totes set, en ordre.'),
            dict(tipus='gran', titol='Les dues mans a la posició de Do',
                 notes=[('C4', 'treble', 'Do'), ('E4', 'treble', 'Mi'),
                        ('G4', 'treble', 'Sol'), ('C3', 'bass', 'Do'),
                        ('E3', 'bass', 'Mi'), ('G3', 'bass', 'Sol')],
                 peu='Do, Mi i Sol, a les dues claus. Mira com es mouen igual: una línia o '
                     'un espai de distància.'),
        ]],
    ),
    piano=dict(
        intro='Juguem amb les set notes i les dues posicions. Les mans viatgen!',
        regles=['POSICIÓ DE DO', 'POSICIÓ DE SOL', 'EL VIATGE DE LA MÀ'],
        fulles=[[
            dict(tipus='misol',
                 text='Amb la mà dreta toquem de Do a Sol a la posició de Do. Després, la mà '
                      'salta: el polze se’n va al Sol, i continuem fins al Do de dalt!'),
            dict(tipus='exercici', titol='L’escala de la mà dreta, amb un salt',
                 pista='posició de Do fins al Sol · el polze salta al Sol · i fins al Do',
                 sistemes=[sis('C4 D4 E4 F4 | G4:w | G4 A4 B4 C5 | C5:w', 4)]),
            dict(tipus='exercici', titol='La mà esquerra fa el viatge al revés',
                 pista='posició de Sol (dit 5 al Sol de baix) · després, posició de Do',
                 sistemes=[sis('G2 A2 B2 C3 | D3:w | C3 D3 E3 F3 | G3:w', 4,
                               clau='bass')]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara llegeix amb atenció: les notes van i vénen! Mira bé si puja o '
                      'baixa, i si salta o va a l’escaló del costat.'),
            dict(tipus='exercici', titol='Escalons i salts',
                 pista='mà dreta · posició de Do',
                 sistemes=[sis('C4 E4 D4 F4 | E4 G4 G4:h | G4 E4 F4 D4 | E4 C4 C4:h', 4)]),
            dict(tipus='exercici', titol='Escalons i salts a l’esquerra',
                 pista='mà esquerra · posició de Do · en clau de Fa',
                 sistemes=[sis('C3 E3 D3 F3 | E3 G3 G3:h | G3 E3 F3 D3 | E3 C3 C3:h', 4,
                               clau='bass')]),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='Set notes, set colors i dues claus. És l’hora de demostrar-ho!',
        fulles=[[
            dict(tipus='misol',
                 text='Ja coneixes totes les notes. Mira bé la clau de cada pentagrama i '
                      'uneix cada nota amb la seva tecla!'),
            dict(tipus='relaciona', titol='Cada nota amb la seva tecla',
                 pista='uneix cada nota amb la tecla que té el punt',
                 notes=[('A4', 'treble'), ('B2', 'bass'), ('D4', 'treble')],
                 tecles=['D4', 'A4', 'B2']),
            dict(tipus='compta', titol='Compta i pinta', clau='treble',
                 pista='quantes n’hi ha de cada? Escriu el número',
                 notes=['C4', 'A4', 'F4', 'A4', 'C4', 'F4', 'A4', 'C4', 'A4', 'F4'],
                 quines=['DO', 'FA', 'LA']),
        ], [
            dict(tipus='dibuixa', titol='Dibuixa les notes a la clau de Fa', clau='bass',
                 pista='dibuixa una rodona a sobre de cada nom, al seu lloc',
                 noms=['Do', 'Sol', 'Mi', 'La', 'Fa', 'Re', 'Si']),
            dict(tipus='sopa', titol='Sopa de lletres de les notes',
                 pista='busca les set notes i marca la caixeta',
                 paraules=['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI'], files=6,
                 columnes=12, llavor=21),
        ]],
    ),
)

# ==========================================================================
# CAPITOL 4 · LES FIGURES
# ==========================================================================
TEMES[13] = dict(
    titol='Rodona, blanca i negra',
    teoria=dict(
        intro='Les notes no només diuen QUINA tecla toquem: també diuen QUANT de temps la '
              'deixem sonar. Cada forma de nota és una figura.',
        regles=['RODONA = 4', 'BLANCA = 2', 'NEGRA = 1'],
        fulles=[[
            dict(tipus='misol',
                 text='Fins ara has tocat notes curtes i notes llargues. Avui aprendràs com '
                      'es diuen i quants temps duren. Compta en veu alta: u, dos, tres, '
                      'quatre!'),
            dict(tipus='figures', titol='Les tres figures',
                 items=[('w', 'Rodona', '4 temps'), ('h', 'Blanca', '2 temps'),
                        ('q', 'Negra', '1 temps')],
                 peu='La rodona és buida i no té pal. La blanca és buida i té pal. La '
                     'negra és plena i té pal.'),
            dict(tipus='targetes', titol='Com sonen', items=[
                ('RODONA', 'Taaaa-a-a-a', 'Toques un cop i comptes u, dos, tres, quatre.'),
                ('BLANCA', 'Taa-a', 'Toques un cop i comptes u, dos.'),
                ('NEGRA', 'Ta', 'Toques un cop i comptes u.'),
            ]),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Les figures són com una pizza! Una rodona sencera és tota la pizza. '
                      'Dues blanques fan una rodona, i quatre negres també.'),
            dict(tipus='compas', titol='Quant val cada cosa',
                 compassos=[['q', 'q', 'q', 'q'], ['h', 'h'], ['w']],
                 peu='Quatre negres, dues blanques o una rodona: tot dura el mateix, quatre '
                     'temps!'),
            dict(tipus='nota', etiqueta='RECORDA',
                 text='Quan toques una blanca o una rodona, el dit es queda a la tecla '
                      'apretada fins que acabes de comptar. No l’aixequis abans d’hora!'),
            dict(tipus='sabies',
                 text='La rodona es diu així perquè és ben rodona. I la blanca i la negra, '
                      'pel color del seu cap: buit com un full en blanc, o ple de tinta!'),
        ]],
    ),
    piano=dict(
        intro='Toquem comptant en veu alta. El dit es queda a la tecla fins que s’acaba '
              'el compte!',
        regles=['COMPTA EN VEU ALTA', 'EL DIT ES QUEDA', 'DUES MANS'],
        fulles=[[
            dict(tipus='misol',
                 text='Compta sempre en veu alta: «u, dos, tres, quatre». A la rodona, toques '
                      'a l’u i aguantes fins al quatre.'),
            dict(tipus='exercici', titol='Rodones per a la mà esquerra',
                 pista='posició de Do · dits 5, 3 i 1 · aguanta les quatre!',
                 sistemes=[sis('C3:w | E3:w | G3:w | C3:w', 4, clau='bass')]),
            dict(tipus='exercici', titol='Blanques per a la mà dreta',
                 pista='posició de Do · compta «u, dos» a cada blanca',
                 sistemes=[sis('C4:h E4:h | G4:h E4:h | D4:h F4:h | E4:h C4:h', 4)]),
            dict(tipus='exercici', titol='Negres per a la mà esquerra',
                 pista='posició de Do · un temps cada una, com un rellotge',
                 sistemes=[sis('C3 D3 E3 F3 | G3 G3 G3 G3 | G3 F3 E3 D3 | C3 C3 C3 C3', 4,
                               clau='bass')]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy', etiqueta='EN MUSSOL MISOL CANTA',
                 text='Barregem les tres figures en una cançó. La saps? És la de l’ovelleta '
                      'de la Mary!'),
            dict(tipus='exercici', titol='Mary tenia una ovelleta',
                 pista='Mary Had a Little Lamb · cançó popular · mà dreta, posició de Do',
                 sistemes=[sis('E4 D4 C4 D4 | E4 E4 E4:h | D4 D4 D4:h | E4 G4 G4:h | '
                               'E4 D4 C4 D4 | E4 E4 E4 E4 | D4 D4 E4 D4 | C4:w', 4)]),
            dict(tipus='exercici', titol='I ara la mà esquerra',
                 pista='la mateixa cançó · posició de Do · en clau de Fa',
                 sistemes=[sis('E3 D3 C3 D3 | E3 E3 E3:h | D3 D3 D3:h | E3 G3 G3:h | '
                               'E3 D3 C3 D3 | E3 E3 E3 E3 | D3 D3 E3 D3 | C3:w', 4,
                               clau='bass')]),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='Rodones, blanques i negres: quant duren i com es diuen?',
        fulles=[[
            dict(tipus='misol',
                 text='Mira cada figura i escriu a la caixeta quants temps dura. Si dubtes, '
                      'pensa en la pizza!'),
            dict(tipus='quant_dura', titol='Quants temps dura?',
                 pista='escriu 1, 2 o 4 a la caixeta de cada figura',
                 figures=['h', 'q', 'w', 'q', 'h']),
            dict(tipus='uneix', titol='Cada figura amb el seu nom',
                 pista='uneix els punts amb una ratlla',
                 esquerra=['Rodona', 'Blanca', 'Negra', 'Dues blanques', 'Dues negres'],
                 dreta=['dura 1 temps', 'fan una blanca', 'dura 4 temps', 'dura 2 temps',
                        'fan una rodona']),
        ], [
            dict(tipus='vf', titol='Vertader o fals?',
                 pista='marca amb una creu la V o la F',
                 frases=['La rodona dura 4 temps.',
                         'La negra és buida.',
                         'Dues blanques duren el mateix que una rodona.',
                         'La blanca dura 1 temps.',
                         'La negra té el cap ple i un pal.']),
            dict(tipus='quant_dura', titol='Suma les pizzes',
                 pista='escriu quants temps dura cada figura… i al final, suma-ho tot!',
                 figures=['w', 'h', 'h', 'q', 'q']),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Picant de mans: una palmada i compta 4 és una rodona, una palmada i '
                      'compta 2 és una blanca. Algú pica i tu endevines la figura!'),
        ]],
    ),
)

TEMES[14] = dict(
    titol='El compàs',
    teoria=dict(
        intro='La música es divideix en caixetes iguals que es diuen compassos. Les separa '
              'una línia que es diu línia divisòria.',
        regles=['4/4 = 4 TEMPS', 'LÍNIA DIVISÒRIA', 'DOBLE BARRA: FINAL'],
        fulles=[[
            dict(tipus='misol',
                 text='Imagina un tren amb vagons. Cada vagó és un compàs, i a cada vagó hi '
                      'caben exactament quatre temps. Ni un més, ni un menys!'),
            dict(tipus='compas', titol='El compàs de quatre',
                 compassos=[['q', 'q', 'q', 'q'], ['h', 'q', 'q'], ['w']],
                 peu='El 4/4 del principi vol dir que a cada compàs hi caben quatre negres '
                     '(o el que duri el mateix).'),
            dict(tipus='targetes', titol='Els senyals del compàs', items=[
                ('AL PRINCIPI', 'El 4/4', 'Diu que cada compàs té 4 temps.'),
                ('ENTRE COMPASSOS', 'La línia', 'Separa un compàs del següent.'),
                ('AL FINAL', 'Doble barra', 'Una línia prima i una de gruixuda: fi!'),
            ]),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Per saber si un compàs està complet, suma els temps de les figures: '
                      'ha de donar quatre! La negra 1, la blanca 2 i la rodona 4.'),
            dict(tipus='figures', titol='Les peces del compàs',
                 items=[('w', 'Rodona', '4 temps'), ('h', 'Blanca', '2 temps'),
                        ('q', 'Negra', '1 temps')],
                 peu='Amb aquestes tres peces pots omplir qualsevol compàs de quatre.'),
            dict(tipus='nota', etiqueta='EL TRUC',
                 text='El primer temps de cada compàs és el més important: fes-lo una '
                      'miqueta més fort. U, dos, tres, quatre — U, dos, tres, quatre!'),
            dict(tipus='sabies',
                 text='Els músics d’una orquestra miren el director, que marca el compàs '
                      'amb la batuta: avall, a l’esquerra, a la dreta i amunt. Quatre '
                      'temps!'),
        ]],
    ),
    piano=dict(
        intro='Ara sí que veuràs el 4/4 al principi del pentagrama. Comptem compàs a '
              'compàs!',
        regles=['COMPTA 1-2-3-4', 'EL PRIMER, MÉS FORT', 'NO T’ATURIS A LA LÍNIA'],
        fulles=[[
            dict(tipus='misol',
                 text='A la línia divisòria no t’aturis: la música continua com un tren que '
                      'passa d’un vagó a l’altre sense frenar!'),
            dict(tipus='exercici', titol='El tren de les negres',
                 pista='mà dreta · posició de Do · el primer temps, una miqueta més fort',
                 sistemes=[sis('C4 D4 E4 F4 | G4 G4 G4 G4 | G4 F4 E4 D4 | C4:w', 4,
                               compas_visible=True)]),
            dict(tipus='exercici', titol='Vagons diferents',
                 pista='mà esquerra · posició de Do · cada compàs suma quatre',
                 sistemes=[sis('C3:h E3:h | G3 G3 G3:h | F3 E3 D3 E3 | C3:w', 4,
                               clau='bass', compas_visible=True)]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy', etiqueta='EN MUSSOL MISOL CANTA',
                 text='Aquesta cançó la coneixes del tema 10! Ara l’has de tocar comptant '
                      'els quatre temps de cada compàs.'),
            dict(tipus='exercici', titol='L’Oda a l’alegria, comptant',
                 pista='mà dreta · posició de Do · compta en veu alta',
                 sistemes=[sis(ODA_DRETA, 4, compas_visible=True)]),
            dict(tipus='exercici', titol='Blanques i negres a l’esquerra',
                 pista='mà esquerra · posició de Do · u, dos, tres, quatre',
                 sistemes=[sis('C3 C3 E3:h | D3 D3 F3:h | E3 E3 G3:h | C3:w', 4,
                               clau='bass', compas_visible=True)]),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='Comptar fins a quatre és la clau de tot. A veure com ho fas!',
        fulles=[[
            dict(tipus='misol',
                 text='A aquests pentagrames els falten les línies divisòries! Compta quatre '
                      'temps i dibuixa una línia. La primera ja te la poso jo.'),
            dict(tipus='divisories', titol='Dibuixa les línies divisòries',
                 pista='cada quatre temps, una línia de dalt a baix del pentagrama',
                 notes=[('C4', 'q'), ('D4', 'q'), ('E4', 'q'), ('C4', 'q'),
                        ('E4', 'h'), ('G4', 'h'), ('F4', 'q'), ('E4', 'q'), ('D4', 'h'),
                        ('C4', 'w')]),
            dict(tipus='divisories', titol='Ara a la clau de Fa', clau='bass',
                 pista='mà esquerra · aquí no hi ha cap línia d’exemple!', exemple=False,
                 notes=[('C3', 'h'), ('E3', 'h'), ('G3', 'q'), ('F3', 'q'), ('E3', 'q'),
                        ('D3', 'q'), ('C3', 'w')]),
        ], [
            dict(tipus='pinta', titol='Escriu i pinta, compàs a compàs', clau='treble',
                 pista='escriu el nom de cada nota a la caixeta i pinta-la del seu color',
                 llegenda=['DO', 'MI', 'SOL'],
                 notes=['C4', 'E4', 'G4', 'E4', 'C4', 'G4', 'E4', 'C4']),
            dict(tipus='endevina', titol='Endevina qui sóc',
                 pista='escriu una lletra a cada caixeta',
                 items=[('Separo un compàs de l’altre.', 'LINIA'),
                        ('Sóc la caixeta on caben quatre temps.', 'COMPAS'),
                        ('Duro quatre temps i sóc buida.', 'RODONA')]),
        ]],
    ),
)

# ==========================================================================
# CAPITOL 5 · ELS SILENCIS
# ==========================================================================
TEMES[15] = dict(
    titol='Els tres silencis',
    teoria=dict(
        intro='De vegades la música calla. Els silencis diuen quant de temps no toquem… '
              'però seguim comptant!',
        regles=['SILENCI DE RODONA = 4', 'DE BLANCA = 2', 'DE NEGRA = 1'],
        fulles=[[
            dict(tipus='misol',
                 text='Els silencis són com respirar. Quan en veus un, aixeca el dit de la '
                      'tecla, però continua comptant. La música no s’atura!'),
            dict(tipus='figures', titol='Els tres silencis',
                 items=[('Rw', 'De rodona', '4 temps'), ('Rh', 'De blanca', '2 temps'),
                        ('Rq', 'De negra', '1 temps')],
                 peu='El de rodona PENJA de la línia 4 com un barret. El de blanca SEU a '
                     'la línia 3 com un barret posat. El de negra fa ziga-zaga.'),
            dict(tipus='targetes', titol='Com els reconec', items=[
                ('4 TEMPS', 'Penja', 'Com un barret penjat del penja-robes.'),
                ('2 TEMPS', 'Seu', 'Com un barret posat al cap.'),
                ('1 TEMPS', 'Ziga-zaga', 'Com un llamp petit.'),
            ]),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Cada figura té el seu silenci, i duren el mateix: la rodona i el seu '
                      'silenci, quatre temps; la blanca i el seu, dos; la negra i el seu, u.'),
            dict(tipus='figures', titol='Cada figura, amb el seu silenci',
                 items=[('w', 'Rodona', '4'), ('Rw', 'Silenci', '4'),
                        ('h', 'Blanca', '2'), ('Rh', 'Silenci', '2'),
                        ('q', 'Negra', '1'), ('Rq', 'Silenci', '1')]),
            dict(tipus='nota', etiqueta='EL TRUC DELS BARRETS',
                 text='El silenci de rodona pesa més (dura 4!) i per això penja cap avall. '
                      'El de blanca és més lleuger i es queda assegut a sobre de la línia.'),
            dict(tipus='sabies',
                 text='Hi ha una obra famosa, d’en John Cage, en què el pianista no toca cap '
                      'nota durant més de quatre minuts. Només silencis!'),
        ]],
    ),
    piano=dict(
        intro='Toquem i callem. Al silenci, el dit s’aixeca però el compte continua.',
        regles=['AL SILENCI, DIT AMUNT', 'SEGUEIX COMPTANT', 'ESCOLTA EL SILENCI'],
        fulles=[[
            dict(tipus='misol',
                 text='Quan arribis a un silenci, aixeca el dit com si la tecla cremés, però '
                      'deixa’l a prop. I compta, compta, compta!'),
            dict(tipus='exercici', titol='Toca i calla',
                 pista='mà dreta · posició de Do · al silenci, dit amunt',
                 sistemes=[sis('C4 R:q C4 R:q | E4 R:q E4 R:q | G4 G4 R:h | C4:h R:h', 4,
                               compas_visible=True)]),
            dict(tipus='exercici', titol='La mà esquerra respira',
                 pista='mà esquerra · posició de Do · compta els silencis en veu alta',
                 sistemes=[sis('C3:h R:h | E3 E3 R:h | G3 F3 E3 R:q | C3:w', 4,
                               clau='bass', compas_visible=True)]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Mentre una mà toca, l’altra fa silenci. Una pregunta, l’altra '
                      'contesta. Ara ja saps escriure-ho!'),
            dict(tipus='exercici', titol='Pregunta i resposta amb silencis',
                 pista='quan una mà toca, l’altra fa silenci · posició de Do',
                 sistemes=[sis('C4 D4 E4 F4 | G4:h R:h | R:w | G4 F4 E4 D4 | C4:h R:h | R:w',
                               3, cap='a) la mà dreta', compas_visible=True),
                           sis('R:w | R:w | G3 F3 E3 D3 | R:w | R:w | C3:w', 3, clau='bass',
                               cap='b) la mà esquerra', compas_visible=True)]),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='Silencis que pengen, que seuen i que fan ziga-zaga!',
        fulles=[[
            dict(tipus='misol',
                 text='Escriu quants temps dura cada silenci. Recorda els barrets: el que '
                      'penja dura quatre i el que seu en dura dos.'),
            dict(tipus='quant_dura', titol='Quants temps calla?',
                 pista='escriu 1, 2 o 4 a la caixeta de cada silenci',
                 figures=['Rh', 'Rq', 'Rw', 'Rq', 'Rh']),
            dict(tipus='uneix', titol='Cada silenci amb la seva figura',
                 pista='uneix els que duren el mateix',
                 esquerra=['Silenci de rodona', 'Silenci de blanca', 'Silenci de negra'],
                 dreta=['negra · 1 temps', 'rodona · 4 temps', 'blanca · 2 temps']),
        ], [
            dict(tipus='sopa', titol='Sopa de lletres del silenci',
                 pista='busca les paraules i marca la caixeta',
                 paraules=['SILENCI', 'RODONA', 'BLANCA', 'NEGRA', 'PENJA', 'SEU'],
                 llavor=15),
            dict(tipus='pauta_buida', clau='treble', etiqueta='DIBUIXA SILENCIS',
                 text='Fes tres silencis de '
                      'rodona penjant de la línia 4 i tres de blanca asseguts a la línia 3.'),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='El joc de les estàtues musicals: algú canta i, quan s’atura, et '
                      'quedes quiet tants temps com digui: 1, 2 o 4!'),
        ]],
    ),
)

# ==========================================================================
# CAPITOL 6 · LES PLIQUES
# ==========================================================================
ODA_SOL = ('B4 B4 C5 D5 | D5 C5 B4 A4 | G4 G4 A4 B4 | B4 A4 A4:h | '
           'B4 B4 C5 D5 | D5 C5 B4 A4 | G4 G4 A4 B4 | A4 G4 G4:h')

TEMES[16] = dict(
    titol='Plica amunt, plica avall',
    teoria=dict(
        intro='El pal de les blanques i les negres es diu plica. A vegades va amunt i a '
              'vegades va avall: depèn d’on viu la nota.',
        regles=['SOTA LA LÍNIA DEL MIG: AMUNT', 'DE LA LÍNIA DEL MIG AMUNT: AVALL'],
        fulles=[[
            dict(tipus='misol',
                 text='La línia del mig del pentagrama és la frontera. Les notes de sota '
                      'porten la plica amunt, a la dreta. Les de dalt, avall, a l’esquerra!'),
            dict(tipus='pliques', titol='A la clau de Sol', clau='treble',
                 notes=[('E4', 'up'), ('G4', 'up'), ('B4', 'down'), ('D5', 'down')],
                 peu='El Si viu just a la línia del mig: la seva plica va avall.'),
            dict(tipus='targetes', titol='La norma de la plica', items=[
                ('A SOTA', 'Amunt', 'La plica surt per la DRETA i puja.'),
                ('A DALT', 'Avall', 'La plica surt per l’ESQUERRA i baixa.'),
                ('AL MIG', 'Avall', 'Les de la línia del mig, també avall.'),
            ]),
        ], [
            dict(tipus='misol', pose='happy',
                 text='A la clau de Fa passa el mateix! La línia del mig hi és igual, i a la '
                      'clau de Fa allà hi viu el Re.'),
            dict(tipus='pliques', titol='A la clau de Fa', clau='bass',
                 notes=[('G2', 'up'), ('B2', 'up'), ('D3', 'down'), ('F3', 'down')],
                 peu='El Re viu a la línia del mig de la clau de Fa: plica avall.'),
            dict(tipus='nota', etiqueta='PER QUÈ?',
                 text='Si les pliques anessin sempre amunt, les notes de dalt tindrien el '
                      'pal fora del pentagrama, molt lluny! Així tot queda endreçat i es '
                      'llegeix millor.'),
            dict(tipus='sabies',
                 text='La rodona és l’única figura que no té plica. És tan llarga que no li '
                      'cal cap pal per aguantar-se!'),
        ]],
    ),
    piano=dict(
        intro='Toquem melodies que pugen per sobre de la línia del mig: mira com giren les '
              'pliques!',
        regles=['POSICIÓ DE SOL', 'MIRA LES PLIQUES', 'COMPTA 1-2-3-4'],
        fulles=[[
            dict(tipus='misol',
                 text='A la posició de Sol, la mà dreta arriba fins al Re de dalt. Les notes '
                      'del Si cap amunt porten la plica avall. Fixa-t’hi!'),
            dict(tipus='exercici', titol='Pugem fins al Re',
                 pista='mà dreta · posició de Sol · dits 1-2-3-4-5',
                 sistemes=[sis('G4 A4 B4 C5 | D5:w | D5 C5 B4 A4 | G4:w', 4,
                               compas_visible=True)]),
            dict(tipus='exercici', titol='La mà esquerra a la posició de Sol',
                 pista='mà esquerra · dits 5-4-3-2-1 · el Re té la plica avall',
                 sistemes=[sis('G2 A2 B2 C3 | D3:w | D3 C3 B2 A2 | G2:w', 4, clau='bass',
                               compas_visible=True)]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy', etiqueta='EN MUSSOL MISOL CANTA',
                 text='L’Oda a l’alegria, però ara a la posició de Sol! Sona igual de bonica, '
                      'però més aguda. I quantes pliques avall!'),
            dict(tipus='exercici', titol='L’Oda a l’alegria a la casa de Sol',
                 pista='mà dreta · posició de Sol · Beethoven, simplificada',
                 sistemes=[sis(ODA_SOL, 4, compas_visible=True)]),
            dict(tipus='exercici', titol='La mà esquerra fa de baix',
                 pista='mà esquerra · posició de Sol · rodones i blanques',
                 sistemes=[sis('G2:w | D3:w | B2:h A2:h | G2:w', 4, clau='bass',
                               compas_visible=True)]),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='Plica amunt o plica avall? Mira bé la línia del mig!',
        fulles=[[
            dict(tipus='misol',
                 text='Aquestes notes s’han quedat sense pal! Dibuixa’ls la plica: amunt i a '
                      'la dreta si són a sota de la línia del mig, avall i a l’esquerra si no.'),
            dict(tipus='posa_pliques', titol='Posa les pliques a la clau de Sol',
                 clau='treble', pista='la línia de punts és la línia del mig',
                 notes=['E4', 'B4', 'G4', 'D5', 'F4', 'C5', 'A4', 'E5']),
            dict(tipus='posa_pliques', titol='Posa les pliques a la clau de Fa',
                 clau='bass', pista='la línia de punts és la línia del mig',
                 notes=['A2', 'E3', 'B2', 'F3', 'G2', 'D3', 'C3', 'A3']),
        ], [
            dict(tipus='encercla', titol='Encercla les notes de plica avall',
                 clau='treble',
                 pista='si haguessin de portar plica, quines la portarien avall?',
                 notes=['E4', 'C5', 'G4', 'B4', 'F4', 'D5', 'A4', 'E5', 'G4', 'B4']),
            dict(tipus='compta', titol='Compta i pinta', clau='treble',
                 pista='escriu quantes n’hi ha de cada nota',
                 notes=['G4', 'B4', 'D5', 'B4', 'G4', 'D5', 'B4', 'G4', 'B4', 'D5'],
                 quines=['SOL', 'SI', 'RE']),
        ]],
    ),
)

# ==========================================================================
# CAPITOL 7 · TOT JUNT
# ==========================================================================
TEMES[17] = dict(
    titol='Les dues mans alhora',
    teoria=dict(
        intro='Fins ara les mans tocaven per torns. Ara toquen juntes: la dreta fa la '
              'melodia i l’esquerra l’acompanya.',
        regles=['LLEGEIX DE DALT A BAIX', 'LES NOTES JUNTES, ALHORA', 'A POC A POC'],
        fulles=[[
            dict(tipus='misol',
                 text='Quan dues notes estan una a sobre de l’altra al gran pentagrama, es '
                      'toquen ALHORA. Com quan dues persones diuen una paraula juntes!'),
            dict(tipus='gran', titol='Dalt i baix, alhora',
                 notes=[('C4', 'treble', 'Do'), ('C3', 'bass', 'Do'),
                        ('E4', 'treble', 'Mi'), ('C3', 'bass', 'Do'),
                        ('G4', 'treble', 'Sol'), ('G3', 'bass', 'Sol')],
                 peu='Llegeix sempre en columna, de dalt a baix: primer mira la nota de la '
                     'dreta, després la de l’esquerra, i toca-les juntes.'),
            dict(tipus='targetes', titol='Com s’aprèn una peça a dues mans', items=[
                ('PRIMER', 'Mà dreta', 'Toca-la sola fins que surti fàcil.'),
                ('DESPRÉS', 'Mà esquerra', 'Toca-la sola també.'),
                ('AL FINAL', 'Juntes', 'Molt a poc a poc, compàs a compàs.'),
            ]),
        ], [
            dict(tipus='misol', pose='happy',
                 text='El truc més fàcil per començar: l’esquerra toca una nota llarga, una '
                      'rodona, i l’aguanta mentre la dreta canta la melodia.'),
            dict(tipus='mans', titol='Les dues mans a la posició de Do',
                 teclats=[DO_ESQUERRA, DO_DRETA],
                 peu='L’esquerra toca el Do amb el dit 5 i l’aguanta. La dreta canta amb els '
                     'cinc dits.'),
            dict(tipus='nota', etiqueta='EL TRUC DE L’ÀNCORA',
                 text='La rodona de l’esquerra és com una àncora: la deixes posada i no '
                      'l’aixeques fins al compàs següent, mentre la dreta va fent.'),
            dict(tipus='sabies',
                 text='El cervell ha de fer dues coses alhora quan toques amb les dues mans. '
                      'Per això és tan bo per al cap: és com un gimnàs per a les neurones!'),
        ]],
    ),
    piano=dict(
        intro='Primeres peces a dues mans: l’esquerra aguanta i la dreta canta.',
        regles=['ESQUERRA: ÀNCORA', 'DRETA: MELODIA', 'A POC A POC'],
        fulles=[[
            dict(tipus='misol',
                 text='Comencem amb la campana dels dos Dos, però ara la dreta es mou! '
                      'L’esquerra aguanta el seu Do quatre temps.'),
            dict(tipus='exercici', titol='L’àncora del Do',
                 pista='mà esquerra: rodona amb el dit 5 · mà dreta: posició de Do',
                 sistemes=[sis('[C3+C4] D4 E4 D4 | [C3+C4] D4 E4:h | [C3+E4] D4 C4 D4 | '
                               '[C3+C4]:w', 4, manos='sostiene', compas_visible=True)]),
            dict(tipus='exercici', titol='Hot Cross Buns a dues mans',
                 pista='la cançó del tema 9 · l’esquerra aguanta el Do a cada compàs',
                 sistemes=[sis('[C3+E4] D4 C4:h | [C3+E4] D4 C4:h | [C3+C4] C4 D4 D4 | '
                               '[C3+E4] D4 C4:h', 4, manos='sostiene',
                               compas_visible=True)]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol', pose='happy',
                 text='Ara l’esquerra canvia de nota! Fa Do i Sol, les dues notes que més '
                      'agraden a les cançons. Mira bé quan canvia.'),
            dict(tipus='exercici', titol='Do i Sol a l’esquerra',
                 pista='mà esquerra: Do amb el dit 5, Sol amb el dit 1 · mà dreta: posició '
                       'de Do',
                 sistemes=[sis('[C3+E4] E4 F4 G4 | [G3+G4] F4 E4 D4 | [C3+C4] C4 D4 E4 | '
                               '[C3+E4] D4 D4:h', 4, manos='sostiene',
                               compas_visible=True)]),
            dict(tipus='exercici', titol='La pluja de la dreta',
                 pista='l’esquerra aguanta · la dreta toca negres · posició de Do',
                 sistemes=[sis('[C3+G4] F4 E4 D4 | [C3+C4] D4 E4 C4 | [G3+D4] E4 F4 D4 | '
                               '[C3+C4]:w', 4, manos='sostiene', compas_visible=True)]),
            dict(tipus='estrelles'),
        ]],
    ),
    fitxa=dict(
        intro='Dues mans, dues claus, un sol cap. Llegeix-ho tot!',
        fulles=[[
            dict(tipus='misol',
                 text='Al gran pentagrama, la clau de Sol és per a la dreta i la de Fa per a '
                      'l’esquerra. Uneix cada nota amb la seva tecla, mirant la clau!'),
            dict(tipus='relaciona', titol='Cada nota amb la seva tecla',
                 pista='uneix cada nota amb la tecla que té el punt',
                 notes=[('G3', 'bass'), ('E4', 'treble'), ('C3', 'bass')],
                 tecles=['E4', 'C3', 'G3']),
            dict(tipus='pinta', titol='La mà esquerra: escriu i pinta', clau='bass',
                 pista='escriu el nom a la caixeta i pinta la nota del seu color',
                 llegenda=['DO', 'MI', 'SOL'],
                 notes=['C3', 'G3', 'E3', 'C3', 'G3', 'E3', 'G3', 'C3']),
        ], [
            dict(tipus='dibuixa', titol='Dibuixa les notes de l’esquerra', clau='bass',
                 pista='dibuixa una rodona a sobre de cada nom, a la clau de Fa',
                 noms=['Do', 'Sol', 'Do', 'Mi', 'Sol', 'Do']),
            dict(tipus='vf', titol='Vertader o fals?',
                 pista='marca amb una creu la V o la F',
                 frases=['Les notes una a sobre de l’altra es toquen alhora.',
                         'Una peça a dues mans s’aprèn primer amb les dues juntes.',
                         'La rodona de l’esquerra s’aguanta quatre temps.',
                         'La mà esquerra llegeix en clau de Sol.']),
            dict(tipus='joc', etiqueta='UN JOC AMB ALGÚ DE CASA',
                 text='Pica a la taula amb les dues mans: l’esquerra a poc a poc (u… dos…) i '
                      'la dreta el doble de ràpid. Ho aconsegueixes sense fer-te un embolic?'),
        ]],
    ),
)

TEMES[18] = dict(
    titol='El gran repàs i el meu primer concert',
    teoria=dict(
        intro='Has fet un viatge llarguíssim! Repassem tot el que saps i preparem el teu '
              'primer concert.',
        regles=['NOTES', 'FIGURES', 'SILENCIS', 'DUES MANS'],
        fulles=[[
            dict(tipus='misol', pose='happy',
                 text='Mira tot el que has après! Les set notes, dues claus, tres figures, '
                      'tres silencis i les dues mans alhora. Ets un pianista de veritat!'),
            dict(tipus='gran', titol='Les notes de les dues mans',
                 notes=[('C4', 'treble', 'Do'), ('D4', 'treble', 'Re'),
                        ('E4', 'treble', 'Mi'), ('F4', 'treble', 'Fa'),
                        ('G4', 'treble', 'Sol'), ('C3', 'bass', 'Do'),
                        ('D3', 'bass', 'Re'), ('E3', 'bass', 'Mi'), ('F3', 'bass', 'Fa'),
                        ('G3', 'bass', 'Sol')],
                 peu='La posició de Do a les dues claus: les mateixes cinc notes, una octava '
                     'de distància.'),
            dict(tipus='figures', titol='Figures i silencis',
                 items=[('w', 'Rodona', '4'), ('h', 'Blanca', '2'), ('q', 'Negra', '1'),
                        ('Rw', 'Silenci', '4'), ('Rh', 'Silenci', '2'),
                        ('Rq', 'Silenci', '1')]),
        ], [
            dict(tipus='misol',
                 text='Un concert no és només tocar: també és saludar, seure bé i escoltar '
                      'els altres. Aquí tens com es fa, pas a pas!'),
            dict(tipus='targetes', titol='El meu concert, pas a pas', items=[
                ('1', 'Saludo', 'Camino fins al piano, miro el públic i faig una '
                                'reverència.'),
                ('2', 'Respiro', 'Sec bé, poso les mans a casa i respiro fons.'),
                ('3', 'Toco', 'A poc a poc. Si m’equivoco, continuo sense aturar-me!'),
            ]),
            dict(tipus='targetes', titol='I quan acabo…', items=[
                ('4', 'Espero', 'Deixo sonar l’última nota fins al final.'),
                ('5', 'Saludo', 'M’aixeco i faig una altra reverència.'),
                ('6', 'Gaudeixo', 'Escolto els aplaudiments. M’ho he guanyat!'),
            ]),
            dict(tipus='nota', etiqueta='SI ESTIC NERVIÓS',
                 text='És normal! Fins i tot els pianistes famosos es posen nerviosos. Respira '
                      'a poc a poc tres vegades, mira la profe i pensa en la primera nota.'),
        ]],
    ),
    piano=dict(
        intro='Les peces del concert. Tria amb la profe quina tocaràs!',
        regles=['DUES MANS', 'COMPTA', 'GAUDEIX'],
        fulles=[[
            dict(tipus='misol', pose='happy', etiqueta='EN MUSSOL MISOL CANTA',
                 text='La peça més famosa del llibre, ara amb les dues mans! L’esquerra fa '
                      'Do i Sol, com al tema 17.'),
            dict(tipus='exercici', titol='L’Oda a l’alegria a dues mans',
                 pista='Beethoven · simplificada · posició de Do · l’esquerra aguanta',
                 sistemes=[sis('[C3+E4] E4 F4 G4 | [G3+G4] F4 E4 D4 | [C3+C4] C4 D4 E4 | '
                               '[G3+E4] D4 D4:h | [C3+E4] E4 F4 G4 | [G3+G4] F4 E4 D4 | '
                               '[C3+C4] C4 D4 E4 | [G3+D4] C4 C4:h', 4, manos='sostiene',
                               compas_visible=True)]),
            dict(tipus='apunts'),
        ], [
            dict(tipus='misol',
                 text='Una altra peça per al concert, a la posició de Sol. Primer cada mà '
                      'sola, i després totes dues juntes!'),
            dict(tipus='exercici', titol='Au clair de la lune a dues mans',
                 pista='cançó popular francesa · posició de Sol · l’esquerra aguanta el Sol',
                 sistemes=[sis('[G2+G4] G4 G4 A4 | [G2+B4]:h A4:h | [G2+G4] B4 A4 A4 | '
                               '[G2+G4]:w', 4, manos='sostiene', compas_visible=True)]),
            dict(tipus='exercici', titol='Mary tenia una ovelleta, amb l’àncora',
                 pista='posició de Do · l’esquerra aguanta el Do',
                 sistemes=[sis('[C3+E4] D4 C4 D4 | [C3+E4] E4 E4:h | [G3+D4] D4 D4:h | '
                               '[C3+E4] G4 G4:h', 4, manos='sostiene',
                               compas_visible=True)]),
            dict(tipus='estrelles', etiqueta='CADA DIA QUE ASSAGIS EL CONCERT, PINTA UNA '
                                             'ESTRELLA'),
        ]],
    ),
    fitxa=dict(
        intro='L’última fitxa del llibre! Fes-la amb calma: ho saps tot.',
        fulles=[[
            dict(tipus='misol',
                 text='El camí més difícil del llibre: Do, Mi, Sol! Saltem de dos en dos, '
                      'com un conill. Arribaràs al piano?'),
            dict(tipus='cami', titol='El camí del conill',
                 pista='pinta el camí saltant: DO, MI, SOL, DO, MI, SOL… fins al piano',
                 files=5, columnes=7, cicle=['DO', 'MI', 'SOL'], coneguts=TOTES,
                 llavor=18, alt_fila=34,
                 cami=[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3),
                       (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6)]),
            dict(tipus='quant_dura', titol='Figures i silencis',
                 pista='escriu quants temps dura cada un',
                 figures=['w', 'Rq', 'h', 'Rw', 'q', 'Rh']),
        ], [
            dict(tipus='endevina', titol='El gran endevinalles',
                 pista='escriu una lletra a cada caixeta',
                 items=[('Sóc la clau de la mà esquerra.', 'FA'),
                        ('Separo els compassos.', 'LINIA'),
                        ('Sóc el pal de les notes.', 'PLICA'),
                        ('Sóc la nota de color vermell.', 'DO'),
                        ('Calla dos temps i seu a la línia 3.', 'SILENCI')]),
            dict(tipus='nota', etiqueta='EL MEU CONCERT',
                 text='La peça que tocaré: ______________________. El dia: ___________. '
                      'Qui vindrà a escoltar-me: _______________________.'),
            dict(tipus='joc', etiqueta='UN ASSAIG A CASA',
                 text='Fes un concert a casa: prepara les cadires, presenta la teva peça, '
                      'toca-la i saluda. I demana que t’aplaudeixin molt fort!'),
        ]],
    ),
)

# --------------------------------------------------------------------------
# les pagines de repas, amb la medalla
# --------------------------------------------------------------------------
REPASSOS = {
    1: dict(
        intro='Has acabat el primer capítol! Abans de pintar la medalla, demostra que ho '
              'saps tot.',
        blocs=[
            dict(tipus='misol', pose='happy',
                 text='Ja coneixes el piano, els números dels dits, els sons greus i aguts, '
                      'i el Do. Quin gran començament!'),
            dict(tipus='vf', titol='Repàs ràpid',
                 pista='marca amb una creu la V o la F',
                 frases=['Els polzes són el dit 1.',
                         'Cap a l’esquerra del piano el so es fa més agut.',
                         'El Do és a l’esquerra de dues tecles negres.',
                         'Dins del piano, un martellet pica la corda.']),
            dict(tipus='medalla', capitol=1,
                 peu='Pinta la medalla i les estrelles: has acabat «Abans de tocar»!'),
        ]),
    2: dict(
        intro='Has acabat el segon capítol! Ja saps llegir a les dues claus.',
        blocs=[
            dict(tipus='misol', pose='happy',
                 text='Línies, espais, la clau de Sol, la clau de Fa i el gran pentagrama. '
                      'Ets un detectiu de la música!'),
            dict(tipus='uneix', titol='Repàs ràpid',
                 pista='uneix els punts amb una ratlla',
                 esquerra=['Clau de Sol', 'Clau de Fa', 'Pentagrama', 'Do central'],
                 dreta=['cinc línies i quatre espais', 'mà esquerra',
                        'entre els dos pentagrames', 'mà dreta']),
            dict(tipus='medalla', capitol=2,
                 peu='Pinta la medalla i les estrelles: has acabat «El pentagrama i les '
                     'claus»!'),
        ]),
    3: dict(
        intro='Has acabat el tercer capítol! Ja coneixes les set notes amb les dues mans.',
        blocs=[
            dict(tipus='misol', pose='happy',
                 text='Do, Re, Mi, Fa, Sol, La i Si, a la clau de Sol i a la clau de Fa. Quin '
                      'arc de Sant Martí tan bonic!'),
            dict(tipus='pinta', titol='Repàs ràpid', clau='bass',
                 pista='escriu el nom i pinta cada nota del seu color',
                 llegenda=['DO', 'MI', 'SOL'],
                 notes=['E3', 'C3', 'G3', 'E3', 'G3', 'C3']),
            dict(tipus='medalla', capitol=3,
                 peu='Pinta la medalla i les estrelles: has acabat «Les notes i els seus '
                     'colors»!'),
        ]),
    4: dict(
        intro='Has acabat el quart capítol! Ja saps quant dura cada nota.',
        blocs=[
            dict(tipus='misol', pose='happy',
                 text='Rodona, blanca, negra i el compàs de quatre temps. Ja comptes com un '
                      'director d’orquestra!'),
            dict(tipus='quant_dura', titol='Repàs ràpid',
                 pista='escriu quants temps dura cada figura',
                 figures=['q', 'w', 'h', 'q']),
            dict(tipus='medalla', capitol=4,
                 peu='Pinta la medalla i les estrelles: has acabat «Les figures»!'),
        ]),
    5: dict(
        intro='Has acabat el cinquè capítol! Ja saps fer silenci comptant.',
        blocs=[
            dict(tipus='misol', pose='happy',
                 text='El silenci que penja, el que seu i el de ziga-zaga. Ara la teva música '
                      'també sap respirar!'),
            dict(tipus='quant_dura', titol='Repàs ràpid',
                 pista='escriu quants temps calla cada silenci',
                 figures=['Rw', 'Rq', 'Rh']),
            dict(tipus='medalla', capitol=5,
                 peu='Pinta la medalla i les estrelles: has acabat «Els silencis»!'),
        ]),
    6: dict(
        intro='Has acabat el sisè capítol! Ja saps cap on va cada plica.',
        blocs=[
            dict(tipus='misol', pose='happy',
                 text='Per sota de la línia del mig, amunt. Per sobre, avall. Les teves notes '
                      'ja estan ben endreçades!'),
            dict(tipus='posa_pliques', titol='Repàs ràpid', clau='treble',
                 pista='dibuixa la plica de cada nota',
                 notes=['F4', 'C5', 'A4', 'E4', 'D5', 'G4']),
            dict(tipus='medalla', capitol=6,
                 peu='Pinta la medalla i les estrelles: has acabat «Les pliques»!'),
        ]),
    7: dict(
        intro='Has acabat el llibre! Ets un pianista de veritat.',
        blocs=[
            dict(tipus='misol', pose='happy', etiqueta='EN MUSSOL MISOL ET FELICITA',
                 text='Ha estat un viatge fantàstic, i l’hem fet junts. Estic molt orgullós de '
                      'tu! Ens veiem al següent llibre?'),
            dict(tipus='estrelles', etiqueta='PINTA UNA ESTRELLA PER CADA PEÇA QUE JA SAPS '
                                             'TOCAR'),
            dict(tipus='medalla', capitol=7,
                 peu='La medalla més gran: has acabat «El Quadern del Pianista · Pekes»!'),
        ]),
}
