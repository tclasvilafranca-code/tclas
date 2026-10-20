# -*- coding: utf-8 -*-
"""Pieza 15 · The Heart Asks Pleasure First (Michael Nyman). Medido sobre el PDF de Drive:
   3 paginas, 28 compases, sin armadura (La menor), 12/8 con 9/8 y 6/8 en los cc. 5, 6, 10, 11;
   "Con moto" y, desde el c. 3, "Piu mosso (corchea = 180)"; semicorchea como figura mas corta;
   repeticion desde el c. 15 con casillas en los cc. 23 y 25; 8va en la izquierda de los cc. 15-16."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
import build_mayores_demo as demo
import mayores_guia as g

_C = COLORES_BLOQUE

_CFG = demo.CFG
FICHA_CA = dict(_CFG)
FICHA_CA.update(
    datos=[('Tonalitat', 'La menor'), ('Compàs', '12/8 · canvia'), ('Tempo', 'Con moto'),
           ('Figura curta', 'Semicorxera'), ('Compassos', '28')],
    secciones=[
        ('A', 1, 2, 'Entrada · Con moto', AZUL),
        ('B', 3, 12, 'Più mosso · canvia el compàs', OCRE),
        ('A', 13, 14, "Torna l'entrada", AZUL),
        ('C', 15, 22, 'Es repeteix · octaves greus', OCRE),
        ('D', 23, 28, '1a i 2a vegada · final', AZUL),
    ],
    armonia=dict(
        titulo='Els acords, d\'un cop d\'ull',
        tarjetas=[
            ('CC. 1-2', 'Baix: Mi · Re · Do',
             'La menor, Sol major i La menor en inversió (la nota greu no és la fonamental), '
             'i Re major. A la teva partitura: Am/E, G/D, Am/C, D.'),
            ('CC. 3-8', 'La m · Fa · Sol · Mi',
             'La menor, Fa major, Sol major i la cadència: Mi amb quarta suspesa → Mi major → '
             'La menor (dominant → tònica). A la teva partitura: Esus4, E, Am.'),
            ('CC. 9-12', 'El mateix camí',
             'Repeteix Fa, Sol, La menor i la mateixa cadència sobre la dominant. El 9/8 i el 6/8 '
             'escurcen el camí de tornada.'),
            ('CC. 13-28', "Torna l'entrada",
             'Els mateixos acords dels cc. 1-2 als cc. 13-14 i a tot el final: el que '
             'aprens al principi es fa servir diverses vegades.'),
        ],
        pie='A sobre de la partitura els acords surten en xifrat americà (A = La, C = Do, '
            'D = Re, E = Mi, F = Fa, G = Sol; "m" = menor; la barra indica la nota del baix). '
            'Aquí els diem com sempre.'),
    titulo_ritmos='Com es compta el 12/8',
    pie_ritmos='Un compàs de 12/8: quatre temps de tres corxeres (1 2 3 · 4 5 6 · 7 8 9 · '
               '10 11 12). La teva peça parteix cada corxera en dues semicorxeres: sis per temps. '
               'Aquí només el ritme, sobre una nota qualsevol.',
    ritmos=[('EL COMPTE', '12/8 · quatre temps') + tuple(_CFG['ritmos'][0][2:])],
    especial=[
        'Diu "Con moto" i, al c. 3, "Più mosso" amb la corxera a 180.',
        'El compàs canvia: 12/8 quasi sempre, i 9/8 i 6/8 als cc. 5-6 i 10-11.',
        'Hi ha semicorxeres de principi a fi: sis per cada temps.',
        'La repetició comença al c. 15, amb 1a casella (c. 23) i 2a casella (c. 25).',
        "Als cc. 15-16 l'esquerra va escrita amb 8va (ottava bassa): sona una octava més greu."],
    reto='Els canvis de 12/8 a 9/8 i a 6/8. Les semicorxeres no frenen: el que canvia és '
         'quantes en caben abans de tornar a començar. Si comptes "un" a cada temps sense '
         'parar, surt sol.',
    truco='Toca només l\'esquerra dels cc. 5-6 amb el metrònom a una corxera per temps, '
          'compta en veu alta 1-2-3 / 1-2-3 / 1-2-3 i 1-2-3 / 1-2-3, i no deixis anar el '
          'compte encara que canviï el compàs. La dreta, quan l\'esquerra no et demani atenció.',
    sabias='El títol és el primer vers d\'un poema d\'Emily Dickinson, i Michael Nyman la '
           'va compondre per a la pel·lícula "El piano" (1993) de Jane Campion. És música '
           'minimalista: una mateixa figura que es repeteix amb petits canvis. L\'entrada torna '
           'als cc. 13-14 i 23-28.',
    qr=dict(_CFG['qr'], titulo='Escolta-la',
            texto='Escolta el primer minut amb la partitura al davant i segueix els canvis de '
                  'compàs amb el dit.'))
FICHA_CA.pop('kicker', None)
FICHA_CA['autor'] = 'Michael Nyman · de la pel·lícula "El piano" · transcripció de David Jůna'

IZQ_CA = [
    ('Un temps cada cop',
     'Cada temps són sis notes. Toca només el primer, a poc a poc, deu cops seguits sense '
     'fallar. Després, el següent.'),
    ('Regular i a poc a poc',
     'Metrònom lent, totes les notes iguals i la primera de cada temps una mica més forta.'),
    ('De memòria',
     'Mira la partitura per aprendre el dibuix i després toca sense mirar la mà.'),
    ('Uneix a poc a poc',
     'Dos temps, un compàs, dos compassos. Puja el metrònom un punt quan et surti tres '
     'cops seguits.'),
]
DER_CA = [
    ('Dues veus',
     'Al principi la dreta fa dues coses: a dalt, notes llargues que canten; a sota, '
     'semicorxeres. Aprèn cada veu per separat.'),
    ('Canta la melodia',
     'Toca només la veu de dalt i canta-la per dins. Les notes amb > van una mica més fortes.'),
    ('Les semicorxeres, més suaus',
     'Afegeix les de sota amb menys so que la melodia: la melodia mana, elles acompanyen.'),
    ("Amb l'esquerra",
     "Quan l'esquerra vagi sola, ajunta-les a poc a poc. Si es trenca, torna a una sola mà."),
]
TEC_CA = ['Canell solt i espatlles baixes: si et cansa, estàs fent força.',
          'Dits corbats, a prop de les tecles, so lleuger i regular.',
          'Compta els temps en veu alta (1-2-3, 4-5-6…) i no paris quan canviï el compàs.']

# (bloc, compassos, [(pas, text)] x4)
GUIA_CA = [
    (1, 'cc. 1-2', [
        ('IZQUIERDA', 'Només les 6 notes del primer temps. Quan surtin, el segon, fins a '
                      'quatre temps seguits.'),
        ('DERECHA', 'Primer la veu de dalt sola (notes llargues); després les semicorxeres '
                    'de sota.'),
        ('JUNTAS', 'Un temps cada cop: esquerra amb melodia, i al final tot.'),
        ('A TEMPO', 'Els dos compassos seguits, sense parar, tres cops.')]),
    (2, 'cc. 3-4', [
        ('IZQUIERDA', 'El mateix tipus de dibuix, però més de pressa: comença molt per sota de '
                      'la velocitat final.'),
        ('DERECHA', 'Els accents (>) marquen la melodia: toca\'ls una mica més forts.'),
        ('JUNTAS', 'Primer el c. 3, després el c. 4, després els dos.'),
        ('A TEMPO', 'Meta: la corxera a 180, que diu la teva partitura. Puja a poc a poc.')]),
    (3, 'cc. 5-6', [
        ('IZQUIERDA', 'Compta en veu alta mentre toques: 1-2-3 / 1-2-3 / 1-2-3 (9/8) i '
                      '1-2-3 / 1-2-3 (6/8).'),
        ('DERECHA', 'Igual, comptant. Cada grup de tres és un temps: no frenis en canviar.'),
        ('JUNTAS', 'Els tres compassos en bucle: c. 5, c. 6 i la tornada a 12/8 del c. 7.'),
        ('OJO', 'El que canvia és quants temps caben al compàs, no la velocitat.')]),
    (4, 'cc. 7-12', [
        ('IZQUIERDA', 'Al c. 7 hi ha notes lligades al baix: es mantenen, no es tornen '
                      'a tocar.'),
        ('DERECHA', 'Els cc. 9-12 segueixen el camí dels cc. 3-8: té oberta aquella pàgina.'),
        ('JUNTAS', 'Un compàs amb el seu compte: c. 9 en 12/8, c. 10 en 9/8, c. 11 en 6/8, '
                   'c. 12 en 12/8.'),
        ('OJO', 'El c. 12 tanca la frase: acaba amb calma.')]),
    (5, 'cc. 13-14', [
        ('IZQUIERDA', 'És el bloc 1: toca-la de memòria.'),
        ('DERECHA', 'Igual: sense partitura.'),
        ('JUNTAS', 'Dues passades seguides sense parar.'),
        ('OJO', 'Si falles, torna a la pàgina del bloc 1.')]),
    (6, 'cc. 15-22', [
        ('IZQUIERDA', 'Als cc. 15-16 porta 8va: llegeixes el que hi ha escrit i el toques una '
                      'octava més greu.'),
        ('DERECHA', 'Entren acords nous (Do major i quintes buides de Mi i de Re): llegeix la '
                    'lletra que hi ha a sobre.'),
        ('JUNTAS', 'Un sistema al dia: cc. 15-16, 17-18, 19-20, 21-22.'),
        ('OJO', 'Recorda la barra de repetició del c. 15.')]),
    (7, 'cc. 23-28', [
        ('IZQUIERDA', 'Les cases 1a (cc. 23-24) i 2a (cc. 25-26) són quasi iguals: '
                      'mira quina toques.'),
        ('DERECHA', 'Igual que l\'esquerra: el difícil és recordar per on vas.'),
        ('JUNTAS', 'Recorre el camí amb el dit sobre la partitura abans de tocar.'),
        ('A TEMPO', 'La peça sencera, de principi a fi, un cop al dia.')]),
]


def _b(num, cc, nombre, sist, diag, pasos):
    return dict(num=num, cc=cc, nombre=nombre, sist=sist, diag=diag, pasos=pasos,
                color=_C[(num - 1) % len(_C)])


def _diag(num):
    return {
        1: ('grupos', 'Un compàs de 12/8 = 4 temps · cada temps, 6 notes',
            (4, 6, ['temps 1', 'temps 2', 'temps 3', 'temps 4'])),
        2: ('capas', 'Més ràpid · tres capes que sonen alhora',
            [('MD melodia', 'barras', AZUL), ('MD semicorxeres', 'puntos', AZUL),
             ('ME semicorxeres', 'puntos', OCRE)]),
        3: ('cuenta', 'El compte no es trenca · cada grup de tres = un temps',
            [('c. 5 · 9/8', 3, 3), ('c. 6 · 6/8', 2, 3), ('c. 7 · 12/8', 4, 3)]),
        4: ('cadena', 'La cadència (cc. 7-8 i 12)',
            [('Mi amb 4.a', False), ('Mi major', False), ('La menor', True)]),
        5: ('cadena', 'És el bloc 1', [('cc. 13-14', True), ('= cc. 1-2', False)]),
        6: ('cadena', 'L\'8va · el que està escrit i el que sona (mà esquerra)',
            [('nota escrita', False), ('sona una octava més greu', True)]),
        7: ('cadena', 'El recorregut',
            [('1-22', False), ('1a: 23-24', True), ('↩ 15-22', False), ('2a: 25-26', True),
             ('27-28', False), ('FIN', True)]),
    }[num]


_NOM = {1: "L'entrada", 2: 'Més ràpid: Più mosso', 3: 'Canvia el compàs',
        4: 'Tancament de la frase i tornada', 5: "Torna l'entrada", 6: 'La repetició',
        7: 'Primera i segona vegada'}
_SIST = {1: (0, 0), 2: (1, 1), 3: (2, 2), 4: (3, 5), 5: (6, 6), 6: (7, 10), 7: (11, 13)}

SPEC = dict(
    num=15, slug='heart', pdf='michael_nyman_the_heart_asks.pdf',
    titulo=demo.CFG['titulo'], autor=demo.CFG['autor'], time_sig=(12, 8),
    kicker='Eva · peça 15 · The Heart Asks Pleasure First', mes='Juny-juliol',
    yt=demo.YT, ficha=FICHA_CA,
    credito="Partitura: Michael Nyman, transcripció de David Jůna (DJ's Sheet Music Archive). "
            "Anotacions: T-Clas.",
    manos=dict(izq=IZQ_CA, der=DER_CA, tecnica=TEC_CA),
    bloques=[_b(n, cc, _NOM[n], _SIST[n], _diag(n), pasos) for (n, cc, pasos) in GUIA_CA],
    cortes={1: [322.5, 482, 620.2], 2: [193.2, 339.2, 481.2, 638.5], 3: [199.2, 348, 498.5, 639]},
    corte_titulo=137.5,
    burb={
        0: [('arriba', 300, 'DER', 'Al principi fa dues coses: a dalt, notes llargues que canten; '
                                    'a sota, semicorxeres. Estudia cada veu sola.', 250),
            ('abajo', 238, 'IZQ', 'Comença per aquí, tu sola: cada temps són 6 notes. A poc a poc i '
                                  'regular.', 150),
            ('abajo', 238, 'AMB', 'Compta 4 temps per compàs: 1-2-3, 4-5-6, 7-8-9, 10-11-12.', 430)],
        1: [('arriba', 300, 'DER', 'Els accents (>) marquen la melodia: toca\'ls una mica més forts '
                                   'que el de sota.', 190)],
        2: [('arriba', 330, 'OJO', 'El compàs canvia: 9/8 són 3 temps, 6/8 són 2. Compta 1-2-3 a '
                                   'cada temps i no frenis.', 350)],
        3: [('arriba', 300, 'AMB', 'Tancament de la frase: la tensió de Mi es resol en La menor. '
                                    'Afluixa la mà en arribar.', 150),
            ('abajo', 270, 'IZQ', 'Les notes lligades del baix es mantenen: no es tornen a tocar.',
             130)],
        4: [('arriba', 300, 'AMB', 'Mateix camí que els cc. 3-8: ja el coneixes. Fixa\'t en els '
                                   'canvis a 9/8 i a 6/8.', 344)],
        5: [('arriba', 300, 'OJO', 'c. 11: 6/8 i després 12/8. Compta 1-2-3 / 1-2-3 i després quatre '
                                    'grups de tres.', 75)],
        6: [('arriba', 300, 'AMB', 'cc. 13-14: un altre cop l\'entrada. Toca-la de memòria, és el '
                                   'bloc 1.', 120)],
        7: [('arriba', 330, 'AMB', 'Comença la repetició. Acords nous: C = Do, G = Sol, '
                                   'Am = La menor, E = Mi.', 60),
            ('abajo', 300, 'IZQ', '8va: toca l\'esquerra una octava més greu mentre duri la '
                                  'línia de punts.', 230)],
        11: [('arriba', 330, 'OJO', 'La primera vegada, en arribar a la casella 1 tornes al signe de '
                                    'repetició del c. 15.', 80)],
        12: [('arriba', 330, 'OJO', 'La segona vegada NO repeteixis: salta a la casella 2 (cc. 25-26) i '
                                    'continua fins al final.', 80)],
        13: [('arriba', 300, 'AMB', 'Els dos últims compassos: baixa el volum i acaba amb calma '
                                    'sobre la doble barra.', 540)],
    },
    lista=['Toco de memòria l\'esquerra dels blocs 1, 2 i 3.',
           'Compto els temps als canvis de compàs sense parar-me.',
           'Sé per on passo la primera vegada i per on la segona.',
           'Toco la peça sencera, de principi a fi, sense parar.',
           'La gravo amb el mòbil i me l\'escolto.'],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de La menor',
    marcas=[(1, 76, 517, 17, 26, 3, 1, 'caja'), (1, 351, 516, 17, 26, 3, 2, 'caja'),
            (1, 545, 516, 19, 26, 3, 3, 'caja'),
            (2, 344, 93, 17, 26, 4, 1, 'caja'), (2, 72, 227, 17, 26, 4, 2, 'caja'),
            (2, 252, 227, 19, 26, 4, 3, 'caja'),
            (2, 50, 564, 12, 76, 6, 1, 'caja'), (2, 76, 621, 24, 14, 6, 2, 'ovalo'),
            (3, 72, 359, 15, 14, 7, 1, 'caja'), (3, 75, 507, 15, 14, 7, 2, 'caja'),
            (3, 555, 715, 14, 82, 7, 3, 'caja')],
)

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_heart.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
