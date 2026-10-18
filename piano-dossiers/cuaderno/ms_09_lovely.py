# -*- coding: utf-8 -*-
"""Pieza 9 · Lovely (Billie Eilish y Khalid), arreglo de Amy Kieran. MEDIDO sobre el PDF de Drive:
   2 paginas A4, 44 compases (numeracion impresa, 5 sistemas + 4), una armadura de un sostenido
   (Mi menor: la melodia empieza y acaba en Mi-Sol), 4/4, negra = 115, sin matices impresos,
   barra de repeticion al abrir el c. 11 y al cerrar el c. 44, semicorchea como figura mas corta
   (cc. 35-37 y 39-40), izquierda en acordes de tres notas (c. 3: Do-Mi-Sol)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=9, slug='lovely', pdf='copia_de_lovely.pdf', time_sig=(4, 4),
    titulo='Lovely', autor='Billie Eilish amb Khalid · arranjament d\'Amy Kieran',
    kicker='Sharifa · peça 9 · Lovely', mes='Abril · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=billie+eilish+khalid+lovely+piano+tutorial',
    credito='Partitura: arranjament d\'Amy Kieran (còpia de Drive). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Mi menor'), ('Compàs', '4/4'), ('Tempo', '♩ = 115'),
               ('Figura curta', 'Semicorxera'), ('Compassos', '44')],
        total=44,
        secciones=[('A', 1, 10, 'Introducció', AZUL),
                   ('B', 11, 18, 'Primera part (es repeteix)', OCRE),
                   ('C', 19, 25, 'La melodia puja', AZUL),
                   ('D', 26, 34, 'Segona part', OCRE),
                   ('E', 35, 44, 'Final i tornada', AZUL)],
        ideas_titulo='La peça en quatre idees',
        ideas=[('DRETA', 'Mi-Sol sense parar',
                'A la intro la dreta repeteix Mi-Sol, Mi-Sol… És el «rellotge» de la cançó.'),
               ('ESQUERRA', 'Acords llargs',
                'L\'esquerra toca acords de tres notes, quasi sempre rodones o blanques. '
                'Entra al c. 3.'),
               ('LA MELODIA', 'Notes que canten',
                'Des del c. 11 la dreta canta amb negres i blanques. Cap al final hi ha notes '
                'ràpides (semicorxeres, cc. 35-40).'),
               ('LA REPETICIÓ', 'Dues vegades',
                'Una barra de repetició obre el c. 11 i una altra tanca el c. 44.')],
        especial=[
            'Posa negra = 115: un pols tranquil i constant.',
            'L\'armadura porta un sostingut (Fa♯): la peça és en Mi menor.',
            'Els cc. 1 i 2 són només dreta; l\'esquerra entra al c. 3.',
            'Hi ha lligadures d\'unió entre compassos: la nota llarga no es torna a tocar.',
            'Hi ha una repetició: cc. 11-44 (barres de repetició al c. 11 i al c. 44).',
            'No hi ha matisos escrits: tria tu on sona més suau i on més fort.'],
        reto='Aconsegueix que la dreta de la intro soni igual, com un rellotge, i que l\'esquerra '
             'entri al c. 3 sense ensopegar. Repte superat!',
        truco='Aprèn-te la intro de memòria (cc. 1-2). Amb ella segura, l\'esquerra i les notes '
              'llargues són l\'única cosa nova.',
        sabias='«Lovely» es va publicar el 2018 dins la banda sonora de la sèrie «Por trece '
               'razones» (13 Reasons Why). Billie Eilish la va escriure amb el seu germà Finneas.',
        qr_texto='Escolta-la amb la partitura al davant: segueix la dreta amb el dit.',
        ts=(4, 4), cuenta_titulo='Com es compta el 4/4',
        cuenta_pie='Un compàs de 4/4 comptat en corxeres. Aquí només el ritme, sobre una nota '
                   'qualsevol: les altures, a la teva partitura.', cuenta_rotulo='EL COMPTE'),
    manos=dict(
        izq=[('Només acords', 'L\'esquerra toca acords de tres notes. Comença al c. 3 amb una '
                              'rodona lligada: compta 1-2-3-4.'),
             ('Un acord, un cop', 'Cada acord es toca amb les tres notes alhora. Posa la mà en '
                                  'forma i baixa-les juntes.'),
             ('Lligadures', 'Si hi ha una lligadura entre dos acords iguals, no es toca el '
                            'segon: es deixa sonar.'),
             ('De memòria', 'Quasi tots els compassos tenen un sol acord. Aprèn-te\'ls sense '
                            'mirar.')],
        der=[('Mi-Sol, Mi-Sol', 'Als cc. 1-2 la dreta alterna dues notes, en corxeres. Toca-les '
                                'sense pressa i totes iguals.'),
             ('Una nota més alta', 'Als cc. 4-5 apareix una nota més alta dins el dibuix. '
                                   'Mira-ho abans de tocar.'),
             ('La melodia', 'Des del c. 11, notes llargues lligades. Canta-les per dins i '
                            'compta-les senceres.'),
             ('Notes ràpides', 'Als cc. 35-37 i 39-40 hi ha semicorxeres: toca-les a poc a poc '
                               'abans d\'anar a tempo.')],
        tecnica=['Canell solt: a les corxeres de la intro el so surt igual, nota rere nota.',
                 'Pols de 115 per minut: fes servir el metrònom i comença més lenta.',
                 'Mira les barres de repetició: la peça es toca dues vegades des del c. 11.']),
    bloques=[
        B(1, 'cc. 1-5', 'La introducció', (0, 0),
          D('cuenta', 'Un compàs de 4/4: 8 corxeres', [('dreta', 4, 2)]),
          [('DERECHA', 'Mi-Sol alternant, en corxeres. Al c. 4 apareix una nota més alta.'),
           ('IZQUIERDA', 'Silenci als cc. 1-2. Al c. 3 entra un acord de rodona.'),
           ('JUNTAS', 'Compta 1-2-3-4 i entra l\'esquerra al c. 3, sense parar.'),
           ('A TEMPO', 'Negra = 115. Comença molt més lenta.')]),
        B(2, 'cc. 6-10', 'Segueix el balanceig', (1, 1),
          D('cadena', 'L\'esquerra', [('acord llarg', False), ('lligat', False),
                                      ('acord nou', True)]),
          [('DERECHA', 'El mateix dibuix d\'abans: ja el coneixes. Fixa\'t quan puja.'),
           ('IZQUIERDA', 'Un acord per compàs, alguns lligats al següent.'),
           ('JUNTAS', 'Els cinc compassos en bucle, sense parar.'),
           ('OJO', 'En acabar el c. 10 comença la part que es repeteix. Prepara\'t!')]),
        B(3, 'cc. 11-18', 'Entra la melodia', (2, 3),
          D('cadena', 'La repetició', [('c. 11', False), ('... c. 44', False),
                                       ('torna al c. 11', True)]),
          [('DERECHA', 'Quatre corxeres i una blanca lligada. Canta abans de tocar.'),
           ('IZQUIERDA', 'Un acord de rodona per compàs, alguns lligats.'),
           ('JUNTAS', 'Una frase de quatre compassos cada cop: cc. 11-14, després 15-18.'),
           ('OJO', 'La barra de repetició del c. 11 obre la part que es toca dues vegades.')]),
        B(4, 'cc. 19-25', 'La melodia puja', (4, 4),
          D('cadena', 'La melodia', [('blanques', False), ('puja', False),
                                     ('nota més alta', True)]),
          [('DERECHA', 'Blanques i negres. Les notes més altes de la frase són al c. 21.'),
           ('IZQUIERDA', 'Acords de dues blanques per compàs. Als cc. 21 i 25 pugen una mica.'),
           ('JUNTAS', 'Un compàs cada cop, i després la frase sencera.'),
           ('A TEMPO', 'Compta 1-2-3-4: dues blanques per compàs.')]),
        B(5, 'cc. 26-36', 'Segona part', (5, 6),
          D('cadena', 'Mateix camí', [('c. 26', False), ('semblant a 19-25', False),
                                      ('c. 35 canvia', True)]),
          [('DERECHA', 'Les frases s\'assemblen a les dels cc. 19-25. Reconeix el que ja saps.'),
           ('IZQUIERDA', 'Acords de blanques i de rodona, com a la frase anterior.'),
           ('JUNTAS', 'Dos trams: cc. 26-30 i cc. 31-36.'),
           ('OJO', 'Al c. 35 arriba la part nova, amb notes més ràpides.')]),
        B(6, 'cc. 37-40', 'Notes ràpides', (7, 7),
          D('cadena', 'Dins el compàs', [('nota llarga', False), ('semicorxeres', True),
                                         ('lligadura', False)]),
          [('DERECHA', 'Hi ha semicorxeres (dues barres). Toca primer només el dibuix, a poc a poc.'),
           ('IZQUIERDA', 'Un acord de rodona per compàs, de vegades lligat.'),
           ('JUNTAS', 'Dos compassos cada cop i després els quatre.'),
           ('OJO', 'Les lligadures d\'unió: la nota lligada no es toca un altre cop.')]),
        B(7, 'cc. 41-44', 'Final i tornada', (8, 8),
          D('cadena', 'El recorregut', [('cc. 41-42', False), ('torna la intro', False),
                                        ('repeteix des del c. 11', True)]),
          [('DERECHA', 'Als cc. 43-44 torna el dibuix del principi.'),
           ('IZQUIERDA', 'Silenci als cc. 43-44: només sona la dreta.'),
           ('JUNTAS', 'Toca els cc. 41-44 i salta un altre cop al c. 11.'),
           ('A TEMPO', 'Després de la segona vegada, acabes al c. 44.')]),
    ],
    cortes={1: [244.0, 386.0, 527.8, 673.2], 2: [209.2, 375.0, 525.8]},
    corte_titulo=112.8, fin={1: 818.0},
    burb={
        0: [('arriba', 330, 'DER', 'Mi-Sol alternant: vuit corxeres per compàs. Iguals i suaus; '
                                   'al c. 4 apareix una nota més alta.', 0.25),
            ('abajo', 330, 'IZQ', 'L\'esquerra entra al c. 3 amb un acord llarg lligat: '
                                  'compta 1-2-3-4.', 0.6)],
        1: [('arriba', 330, 'AMB', 'Un acord per compàs a l\'esquerra i el mateix balanceig a la '
                                   'dreta.', 0.4)],
        2: [('arriba', 330, 'OJO', 'Compte! La barra de repetició obre el c. 11: d\'aquí al c. 44 '
                                   'es toca dues vegades.', 0.1),
            ('abajo', 270, 'IZQ', 'Acord de rodona lligat entre els cc. 11 i 12.', 0.2)],
        3: [('arriba', 330, 'DER', 'Frase de quatre compassos: compta les notes llargues senceres.',
             0.3)],
        4: [('arriba', 330, 'AMB', 'Blanques i negres: dos temps per compàs a l\'esquerra. '
                                   'La melodia arriba al més alt al c. 21.', 0.4)],
        5: [('arriba', 330, 'DER', 'S\'assembla a la frase dels cc. 19-25: reconeix el que ja '
                                   'saps.', 0.2)],
        6: [('arriba', 330, 'OJO', 'Mira! Al c. 35 la dreta puja i baixa amb notes ràpides. '
                                   'Estudia-ho sola i a poc a poc.', 0.65)],
        7: [('arriba', 330, 'DER', 'Semicorxeres un altre cop (dues barres): com al c. 35.', 0.1)],
        8: [('arriba', 330, 'OJO', 'La barra del c. 44 mana tornar al c. 11. Després de la '
                                   'segona vegada, acabes aquí.', 0.9)],
    },
    marcas=[],
    misol=dict(
        manos='Aprèn la intro de memòria: dues notes que es balancegen. Amb això a les mans, '
              'la resta és més fàcil.',
        guia='Un bloc cada dia i res més. Si el compàs et surt 3 cops seguits, passa al següent.',
        pauta='Inventa un compàs de 4/4 amb Mi i Sol en corxeres, com la intro de Lovely.'),
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Mi menor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lovely.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
