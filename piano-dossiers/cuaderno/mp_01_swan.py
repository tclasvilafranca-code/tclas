# -*- coding: utf-8 -*-
"""Pieza 1 · El cisne (Saint-Saens), edicion "Piano Collection for Beginners - Grade 3".
   MEDIDO sobre el PDF (5 paginas, tamano carta): una armadura de un sostenido (Sol mayor), 3/4,
   Andante negra = 96, termina en el c. 54 (numeracion impresa, que cuenta el primer compas vacio
   como 0); todo en corcheas (una barra), izquierda en seis corcheas por compas; matices pp, p,
   poco cresc., dim. e poco rit., a tempo, mf, dim., rit., lento, pp, rit.; sostenidos y becuadros
   en los cc. 14-15 y 32-33."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403



SPEC = dict(
    num=1, slug='cisne', pdf='the_swan.pdf', time_sig=(3, 4),
    titulo='El cigne', autor='Camille Saint-Saëns · edició per a principiants de Ricardo Boppré',
    kicker='Eva · peça 1 · El cigne', mes='Novembre · 1.a quinzena',
    yt='https://www.youtube.com/results?search_query=saint-saens+the+swan+le+cygne+piano',
    credito='Partitura: C. Saint-Saëns, revisió de Ricardo Boppré (theperfectscores.com). '
            'Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sol major'), ('Compàs', '3/4'), ('Tempo', 'Andante ♩=96'),
               ('Figura curta', 'Corxera'), ('Compassos', '54')],
        total=54,
        secciones=[('A', 1, 9, 'Entrada i primera frase', AZUL),
                   ('B', 10, 20, 'La melodia creix', OCRE),
                   ('C', 21, 31, 'Poco cresc.', AZUL),
                   ('D', 32, 43, 'Torna · clímax en mf', OCRE),
                   ('E', 44, 54, 'Final: dim., lento, rit.', AZUL)],
        ideas=[('ESQUERRA', 'Sis corxeres per compàs',
                'Un arpegi que puja i baixa, compàs rere compàs, sota una lligadura llarga. És el '
                'mar on neda el cigne.'),
               ('DRETA', 'Notes que canten',
                'La melodia va en negres i blanques, en frases lligades de tres o quatre compassos. '
                'S\'estudia cantant.'),
               ('ELS CANVIS', 'Sostinguts i becaires',
                'Quasi tota la peça fa servir les notes de Sol major. Les alteracions arriben als '
                'cc. 14-15 i 32-33.'),
               ('ELS MATISOS', 'pp → p → mf → pp',
                'Comença molt suau, creix fins al mf del c. 42 i s\'apaga amb rit. al final.')],
        especial=[
            'Hi diu "Andante" i negra = 96.',
            'Els dos primers compassos són de silenci a la dreta: comença l\'esquerra sola.',
            'L\'esquerra fa quasi sempre el mateix: sis corxeres per compàs.',
            'Les frases de la dreta van lligades: cada lligadura és una respiració.',
            'Hi ha "poco cresc." (cc. 28-31), "dim. e poco rit." (cc. 32-33) i "lento" (c. 49).',
            'El final porta "pp" i "rit.": acaba gairebé sense so.'],
        reto='Que l\'esquerra soni sempre igual i molt suau mentre la dreta canta. Si un '
             'compàs se t\'escapa, el normal és que l\'esquerra no estigui de memòria.',
        truco='Estudia l\'esquerra sola fins a tocar-la mirant la dreta de la partitura. Després '
              'afegeix només la primera nota llarga de cada frase, i la segona no fins que surti.',
        sabias='El cigne és el n.º 13 d\'«El carnaval dels animals» (1886), escrit per a violoncel i dos pianos. Saint-Saëns no va voler que aquesta obra es publiqués en vida, tret d\'aquesta peça.',
        qr_texto='Escolta-la amb la partitura al davant: segueix les lligadures amb el dit.',
        ts=(3, 4)),
    manos=dict(
        izq=[('Un compàs, un arc', 'A cada compàs l\'esquerra puja i baixa per sis corxeres. '
                                   'Toca només el primer compàs, a poc a poc, deu vegades '
                                   'seguides sense fallar.'),
             ('Regular i suau', 'Metrònom lent, sis corxeres iguals i molt suaus (pp). Si una '
                                'nota sobresurt, repeteix.'),
             ('Quan el dibuix canvia', 'Als cc. 13-15 el dibuix s\'aplana i canvien algunes '
                                       'notes (amb sostinguts). Al c. 16 torna el de '
                                       'sempre.'),
             ('De memòria', 'Aprèn l\'esquerra de memòria: la dreta necessita que ella vagi '
                            'sola.')],
        der=[('Cantar abans de tocar', 'La dreta quasi sempre toca notes llargues en una frase '
                                       'lligada. Canta-la per dins i respira on acaba la '
                                       'lligadura.'),
             ('Una frase, un gest', 'Toca cada frase lligada com un sol moviment del braç: '
                                    'baixa el braç a la primera nota i deixa pujar el canell al '
                                    'final.'),
             ('Les alteracions', 'Als cc. 14-15 la dreta puja per semitons, amb sostinguts '
                                 'i becaires. Toca-la a poc a poc i digues el nom de cada nota.'),
             ('Amb l\'esquerra', 'Uneix a poc a poc una frase amb l\'esquerra ja segura. Si es '
                                 'trenca, torna a una sola mà.')],
        tecnica=['Braç i canell solts: la melodia es canta, no es colpeja.',
                 'So petit i regular a l\'esquerra: la melodia mana.',
                 'Compta 1-2-3 a cada compàs, sense pressa (Andante).']),
    bloques=[
        B(1, 'cc. 1-5', 'L\'entrada', (0, 1), D('cuenta', 'L\'esquerra: sis corxeres per compàs',
                                                [('un compàs', 1, 6)]),
          [('IZQUIERDA', 'Comença sola: sis corxeres per compàs, puja i baixa. A poc a poc i '
                         'regular.'),
           ('DERECHA', 'Entra al c. 2 amb tres notes llargues lligades. Canta-les abans de '
                       'tocar-les.'),
           ('JUNTAS', 'Dos compassos d\'esquerra i, al tercer, entra la dreta.'),
           ('A TEMPO', 'Andante, negra = 96. Comença més lenta.')]),
        B(2, 'cc. 6-12', 'La melodia creix', (2, 3),
          D('capas', 'Dues capes que sonen alhora',
            [('Dreta: melodia', 'barras', AZUL), ('Esquerra: corxeres', 'puntos', OCRE)]),
          [('IZQUIERDA', 'Mateix arc de sis corxeres; al c. 12 la forma canvia: mira-ho abans de '
                         'tocar.'),
           ('DERECHA', 'La frase puja fins a la nota més alta de la pàgina: passa d\'una nota llarga '
                       'a l\'altra sense tallar.'),
           ('JUNTAS', 'Una frase de la dreta amb la seva esquerra, i respires.'),
           ('OJO', 'Al c. 12 acaba la lligadura llarga: aquí es respira.')]),
        B(3, 'cc. 13-20', 'Sostinguts i becaires', (4, 5),
          D('cadena', 'La pujada dels cc. 14-15',
            [('llegeix nota a nota', False), ('puja per semitons', False), ('acaba en nota llarga',
                                                                            True)]),
          [('IZQUIERDA', 'Als cc. 13-15 el dibuix s\'aplana i porta sostinguts. Al c. 16 '
                         'torna el de sempre.'),
           ('DERECHA', 'La pujada dels cc. 14-15 va per semitons. Digues cada nota en veu alta i '
                       'toca a poc a poc.'),
           ('JUNTAS', 'Primer només els cc. 13-16, en bucle.'),
           ('OJO', 'Els sostinguts i becaires valen només fins al final del seu compàs.')]),
        B(4, 'cc. 21-31', 'A poc a poc, més so', (6, 8),
          D('cadena', 'L\'arc de matisos',
            [('p', False), ('poco cresc.', False), ('més so', True)]),
          [('IZQUIERDA', 'Continua amb sis corxeres per compàs. Més so, però sense córrer.'),
           ('DERECHA', 'Les frases s\'assemblen a les d\'abans: reconeix les que ja saps.'),
           ('JUNTAS', 'Un sistema cada dia: cc. 21-23, 24-27, 28-31.'),
           ('OJO', 'Poco cresc.: puja el so a poc a poc, no de cop.')]),
        B(5, 'cc. 32-39', 'Torna el tema', (9, 10),
          D('cadena', 'Les indicacions d\'aquest bloc',
            [('dim. e poco rit.', False), ('a tempo', False), ('pp', True)]),
          [('IZQUIERDA', 'Als cc. 32-33 el dibuix porta alteracions; després tornen els '
                         'arcs de sempre.'),
           ('DERECHA', 'Al c. 34 torna la melodia del principi, altra vegada en pp.'),
           ('JUNTAS', 'Vigila el canvi: dim. e poco rit., i a tempo al c. 34.'),
           ('OJO', 'Al c. 34 torna el tempo: no et quedis lenta.')]),
        B(6, 'cc. 40-43', 'El punt més fort', (11, 11),
          D('cadena', 'El clímax', [('p', False), ('mf', True), ('torna a baixar', False)]),
          [('IZQUIERDA', 'Més so, però sempre regular: no acceleris amb la força.'),
           ('DERECHA', 'Aquí és la nota més aguda de la melodia: toca-la cantant.'),
           ('JUNTAS', 'Els quatre compassos en bucle, sense parar.'),
           ('A TEMPO', 'El mf és el punt més fort de tota la peça.')]),
        B(7, 'cc. 44-54', 'El final', (12, 14),
          D('cadena', 'Cap al silenci',
            [('dim.', False), ('p', False), ('rit.', False), ('lento', False), ('a tempo', False),
             ('pp', False), ('rit.', True)]),
          [('IZQUIERDA', 'Del c. 51 al 54 l\'esquerra passa a clau de sol: llegeix la clau abans de '
                         'tocar.'),
           ('DERECHA', 'Notes llargues al final: compta-les senceres.'),
           ('JUNTAS', 'Tres sistemes: cc. 44-47, 48-50 i 51-54.'),
           ('OJO', 'A poc a poc més suau i més lent: acaba gairebé sense so.')]),
    ],
    cortes={1: [333.5, 521.2], 2: [293.8, 502.5], 3: [303.0, 507.2], 4: [305.5, 503.5],
            5: [299.8, 509.2]},
    corte_titulo=151.8, inicio={2: 80, 3: 80, 4: 80, 5: 80},
    fin={1: 712.0, 2: 711.8, 3: 717.2, 4: 710.2, 5: 712.0},
    burb={
        0: [('abajo', 300, 'IZQ', 'Comences tu, sola: sis corxeres per compàs, puja i baixa com un '
                                  'arc. A poc a poc i regular.', 0.25)],
        1: [('arriba', 300, 'DER', 'Entra la melodia: tres notes llargues lligades. Canta-la per '
                                   'dins abans de tocar-la.', 0.15)],
        2: [('arriba', 330, 'AMB', 'Una frase llarga = un sol arc: toca les notes com una sola '
                                   'idea i respira on acaba la lligadura.', 0.2)],
        3: [('arriba', 300, 'IZQ', 'Al c. 12 l\'esquerra canvia de dibuix: sis corxeres '
                                   'seguides, sense arc.', 0.85)],
        4: [('arriba', 330, 'OJO', 'Sostinguts i becaires: la pujada dels cc. 14-15 va per '
                                   'semitons. Llegeix-la nota a nota.', 0.55)],
        5: [('arriba', 300, 'DER', 'Més suau (p): les notes llargues se senten sobre l\'esquerra. '
                                   'Pesa amb el braç, no amb el dit.', 0.1)],
        8: [('arriba', 300, 'AMB', 'Poco cresc.: puja el so a poc a poc, sense accelerar.', 0.5)],
        9: [('arriba', 330, 'OJO', 'dim. e poco rit.: baixa el so i afluixa el tempo; al c. 34 '
                                   'torna "a tempo" en pp.', 0.6)],
        11: [('arriba', 300, 'AMB', 'mf: el punt més fort de la peça. Que soni, però cantant.',
              0.6)],
        12: [('arriba', 300, 'OJO', 'dim., p i rit.: el so es va apagant fins al c. 47.', 0.3)],
        13: [('arriba', 330, 'OJO', 'lento al c. 49 i "a tempo" al c. 50.', 0.45)],
        14: [('arriba', 330, 'AMB', 'pp i rit.: acaba gairebé sense so i deixa que l\'últim compàs '
                                    's\'apagui.', 0.6)],
    },
    marcas=[],
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Sol major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_cisne.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
