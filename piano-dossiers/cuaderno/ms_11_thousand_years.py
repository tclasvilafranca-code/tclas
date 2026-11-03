# -*- coding: utf-8 -*-
"""Pieza 11 · A Thousand Years (Christina Perri y David Hodges), arreglo de Piano Seeds STUDIO.
   MEDIDO sobre el PDF de Drive: 2 paginas A4, 33 compases, sin armadura (Do mayor: acaba en un
   acorde de Do), 6/8, sin tempo ni matices impresos, sin repeticiones, dedos impresos por el
   arreglista, corchea como figura mas corta (cc. 8, 10, 12-14, 16-19, 25-30). Derecha en
   intervalos de negra con puntillo los cc. 1-8, izquierda en acordes de tres notas desde el c. 9;
   las notas mas altas (lineas adicionales encima del pentagrama) estan en los cc. 22-24;
   ligadura de union de acorde entre los cc. 21 y 22."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=11, slug='thousand_years', pdf='copia_de_a_thousand_years.pdf', time_sig=(6, 8),
    titulo='A Thousand Years', autor='Christina Perri i David Hodges · arranjament de Piano Seeds STUDIO',
    kicker='Sharifa · peça 11 · A Thousand Years', mes='Maig · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=christina+perri+a+thousand+years+piano+tutorial',
    credito='Partitura: arranjament de Piano Seeds STUDIO (còpia de Drive). Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '6/8'), ('Caràcter', 'Sense tempo escrit'),
               ('Figura curta', 'Corxera'), ('Compassos', '33')],
        total=33,
        secciones=[('A', 1, 8, 'Introducció', AZUL),
                   ('B', 9, 17, 'Primera frase', OCRE),
                   ('C', 18, 24, 'La melodia puja', AZUL),
                   ('D', 25, 33, 'Final', OCRE)],
        ideas_titulo='La peça en quatre idees',
        ideas=[('INTRODUCCIÓ', 'Només dues notes',
                'Als cc. 1-8 la dreta toca dues notes alhora, dues vegades per compàs. '
                'L\'esquerra, una nota llarga.'),
               ('ESQUERRA', 'Acords de tres notes',
                'Des del c. 9 l\'esquerra toca acords, quasi sempre un per compàs.'),
               ('DRETA', 'Notes llargues',
                'Notes llargues amb puntet i grups de tres corxeres que baixen.'),
               ('EL MÉS ALT', 'Cc. 22-24',
                'Les notes més agudes són en aquests compassos, amb ratlletes damunt del '
                'pentagrama.')],
        especial=[
            'És 6/8: dos temps per compàs, cadascun amb tres corxeres.',
            'No hi ha armadura: ni sostinguts ni bemolls. Acaba en un acord de Do major.',
            'La partitura no posa tempo ni matisos: tria tu un pols lent i còmode.',
            'La teva partitura porta números de dit escrits per l\'arranjador; fes-los servir si '
            't\'ajuden.',
            'Hi ha una lligadura d\'acord entre els cc. 21 i 22: es toca un cop i es deixa sonar.',
            'No hi ha repeticions: són 33 compassos, del principi al final.'],
        reto='Toca les notes altes dels cc. 22-24 sense que se\'t tensi la mà, i que l\'esquerra '
             'no es despisti mentrestant. Tu pots!',
        truco='Aprèn-te la introducció (cc. 1-8) de memòria: són dues notes, i et deixa mirar la mà '
              'esquerra quan comença la melodia.',
        sabias='«A Thousand Years» (2011) la van escriure Christina Perri i David Hodges per a la '
               'banda sonora de la pel·lícula «The Twilight Saga: Breaking Dawn – Part 1».',
        qr_texto='Escolta-la amb la partitura al davant i compta dos temps per compàs.',
        ts=(6, 8), cuenta_titulo='Com es compta el 6/8',
        cuenta_pie='Un compàs de 6/8: dos temps, cadascun amb tres corxeres. Aquí només el ritme, '
                   'sobre una nota qualsevol.', cuenta_rotulo='EL COMPTE'),
    manos=dict(
        izq=[('Una nota llarga', 'Als cc. 1-8 l\'esquerra toca una sola nota llarga, de vegades '
                                 'lligada al compàs següent. Compta 1-2-3, 4-5-6.'),
             ('Un acord, un compàs', 'Des del c. 9 hi ha un acord de tres notes per compàs. '
                                     'Posa la mà en forma i baixa les tres alhora.'),
             ('Dos acords per compàs', 'Als cc. 25-33 l\'acord canvia a cada temps. '
                                       'Compta 1-2-3, 4-5-6.'),
             ('De memòria', 'Els acords es repeteixen molt: aprèn-te l\'esquerra sense mirar.')],
        der=[('Dues notes alhora', 'Als cc. 1-8 la dreta toca intervals de dues notes, dues '
                                   'vegades per compàs. Toca-les juntes i iguals.'),
             ('Notes amb puntet', 'La melodia va en negres amb puntet: cadascuna dura tres '
                                  'corxeres. Compta 1-2-3.'),
             ('Les corxeres', 'Els grups de tres corxeres baixen pas a pas. Toca-les '
                              'tranquil·les, sense córrer.'),
             ('Les notes altes', 'Als cc. 22-24 hi ha notes amb ratlletes damunt del pentagrama. '
                                 'Llegeix-les a poc a poc i digues-ne el nom.')],
        tecnica=['Canell solt i braç pesat: el so és dolç, no a cops.',
                 'Compta dos temps llargs per compàs (1-2-3, 4-5-6).',
                 'Comença molt lenta i puja el pols a poc a poc.']),
    bloques=[
        B(1, 'cc. 1-4', 'Introducció', (0, 0),
          D('grupos', 'Un compàs de 6/8 = 2 temps · 3 corxeres cadascun',
            (2, 3, ['temps 1', 'temps 2'])),
          [('DERECHA', 'Dues notes alhora, dues vegades per compàs. Compta 1-2-3, 4-5-6.'),
           ('IZQUIERDA', 'Una nota llarga per compàs, lligada a la següent.'),
           ('JUNTAS', 'Comença amb la dreta i l\'esquerra juntes: els quatre compassos.'),
           ('A TEMPO', 'Molt a poc a poc. Tria un pols que puguis mantenir.')]),
        B(2, 'cc. 5-8', 'La introducció continua', (1, 1),
          D('cadena', 'Per entrar a la melodia', [('dues notes', False), ('dues notes', False),
                                                  ('3 corxeres', True)]),
          [('DERECHA', 'Les mateixes dues notes i, al c. 8, tres corxeres que baixen.'),
           ('IZQUIERDA', 'Una nota llarga per compàs. Al c. 8 toca una nota i descansa el '
                         'segon temps.'),
           ('JUNTAS', 'Els quatre compassos en bucle.'),
           ('OJO', 'Al c. 8 l\'esquerra descansa al segon temps: compta-ho.')]),
        B(3, 'cc. 9-11', 'Entra la melodia', (2, 2),
          D('cadena', 'Dins el compàs', [('nota amb puntet', False), ('tres corxeres', True)]),
          [('DERECHA', 'Dues notes amb puntet i, al c. 10, tres corxeres que baixen.'),
           ('IZQUIERDA', 'Acord de tres notes, un per compàs, en clau de fa.'),
           ('JUNTAS', 'Compta 1-2-3, 4-5-6 i toca els tres compassos.'),
           ('OJO', 'Al c. 9 comença la melodia: abans només hi havia dues notes.')]),
        B(4, 'cc. 12-14', 'Segueix la frase', (3, 3),
          D('cadena', 'La frase', [('nota llarga', False), ('corxeres', False),
                                   ('nota llarga', True)]),
          [('DERECHA', 'Combina notes llargues amb grups de corxeres.'),
           ('IZQUIERDA', 'Un acord per compàs, igual que al bloc anterior.'),
           ('JUNTAS', 'Els tres compassos, a poc a poc, sense aturar-te.'),
           ('A TEMPO', 'Compta dos temps per compàs.')]),
        B(5, 'cc. 15-17', 'Es prepara el canvi', (4, 4),
          D('cadena', 'El camí', [('c. 15', False), ('c. 16', False), ('c. 17', True)]),
          [('DERECHA', 'Segueix amb notes llargues i corxeres. El c. 17 acaba la frase.'),
           ('IZQUIERDA', 'Un acord per compàs.'),
           ('JUNTAS', 'Els cc. 15-17 i l\'entrada del c. 18.'),
           ('OJO', 'Abans del c. 18 respira: comença una altra frase.')]),
        B(6, 'cc. 18-20', 'La frase continua', (5, 5),
          D('cadena', 'El camí', [('nota llarga', False), ('corxeres', False),
                                  ('nota llarga', True)]),
          [('DERECHA', 'Notes llargues i corxeres, semblant als cc. 12-14.'),
           ('IZQUIERDA', 'Un acord per compàs, igual que abans.'),
           ('JUNTAS', 'Compta 1-2-3, 4-5-6 a cada compàs.'),
           ('A TEMPO', 'Els cc. 15-20 seguits, sense parar.')]),
        B(7, 'cc. 21-24', 'La melodia puja', (6, 6),
          D('cadena', 'Cap al més alt', [('c. 21', False), ('c. 22', False),
                                         ('c. 23-24', True)]),
          [('DERECHA', 'Les notes pugen i arriben a les més altes de la peça (cc. 22-24).'),
           ('IZQUIERDA', 'Acord llarg lligat entre els cc. 21 i 22: es toca un cop.'),
           ('JUNTAS', 'Els quatre compassos, a poc a poc. Digues el nom de les notes altes.'),
           ('OJO', 'Les ratlletes damunt del pentagrama són notes molt agudes.')]),
        B(8, 'cc. 25-33', 'Final', (7, 9),
          D('cadena', 'Cap al final',
            [('6 corxeres', False), ('lligadures', False), ('notes llargues', False),
             ('Do', True)]),
          [('DERECHA', 'Sis corxeres per compàs als cc. 25-27. Al final, notes llargues que baixen.'),
           ('IZQUIERDA', 'Dos acords per compàs (un per temps) als cc. 25-33.'),
           ('JUNTAS', 'Tres trams: cc. 25-27, 28-30 i 31-33.'),
           ('A TEMPO', 'La peça sencera, sense parar, fins a l\'acord final de Do major.')]),
    ],
    cortes={1: [254.2, 388.8, 549.2, 679.5], 2: [211.0, 365.8, 522.2, 680.2]},
    corte_titulo=127.5, fin={1: 822.0, 2: 806.0},
    burb={
        0: [('abajo', 330, 'AMB', 'Introducció: la dreta toca dues notes alhora, dues vegades per '
                                  'compàs. L\'esquerra sosté una nota llarga.', 0.3)],
        1: [('abajo', 330, 'OJO', 'Al c. 8 arriben tres corxeres que baixen i porten a la '
                                  'melodia del c. 9. Escolta com et porten!', 0.9)],
        2: [('arriba', 330, 'IZQ', 'Des d\'aquí, un acord de tres notes per compàs. Baixa les tres '
                                   'alhora.', 0.1),
            ('abajo', 330, 'DER', 'Entra la melodia: dues notes llargues i, al c. 10, tres '
                                  'corxeres que baixen.', 0.5)],
        3: [('arriba', 330, 'DER', 'Notes llargues i grups de corxeres: compta 1-2-3, 4-5-6.',
             0.2)],
        4: [('arriba', 330, 'OJO', 'Final de la primera frase: respira abans del c. 18.', 0.3)],
        5: [('arriba', 330, 'AMB', 'Mateixa forma que als cc. 12-14: notes llargues i grups de '
                                   'tres corxeres.', 0.2)],
        6: [('arriba', 330, 'DER', 'Les notes pugen: les més altes de la peça són als cc. 22-24 '
                                   '(ratlletes damunt del pentagrama).', 0.3),
            ('abajo', 330, 'IZQ', 'Acord lligat entre els cc. 21 i 22: es toca un cop i es deixa '
                                  'sonar.', 0.15)],
        7: [('arriba', 330, 'DER', 'Sis corxeres per compàs. A l\'esquerra, dos acords per '
                                   'compàs.', 0.2)],
        8: [('arriba', 330, 'OJO', 'Les lligadures dels cc. 29-30 uneixen notes iguals: es '
                                   'toquen una sola vegada.', 0.5)],
        9: [('arriba', 330, 'AMB', 'Les notes baixen pas a pas. L\'últim acord, de Do major, es '
                                   'deixa sonar sencer.', 0.4)],
    },
    marcas=[],
    misol=dict(
        manos='Aprèn-te la intro de memòria: només dues notes. Així pots mirar l\'esquerra quan '
              'entri la melodia.',
        guia='Les notes altes dels cc. 22-24 fan por, però són poques. Digues-ne el nom i toca a poc a poc.',
        pauta='Inventa un compàs de 6/8 amb dues notes llargues amb puntet, com la intro.'),
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Do major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_thousand_years.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
