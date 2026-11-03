# -*- coding: utf-8 -*-
"""Peça 15 · Can't Stop the Feeling! (Justin Timberlake). MEDIDO sobre el PDF de Drive de Sharifa:
   1 pagina apaisada y girada 90 grados (imagen de 79 ppp) con 17 compases en 3 sistemas (6+6+5),
   sin armadura ni alteraciones, 4/4, sin tempo ni matices, corchea como figura mas corta.
   Derecha: solo Do4, Re4, Mi4 y un Sol4 (c. 6). Izquierda: La3, Sol3 y un Mi3 (c. 9); silencio de
   compas entero en los cc. 1, 4, 8 y 17. El PDF se gira con PyMuPDF y se recoloca en filas mas
   cortas (cc. 1-4, 5-6, 7-9, 10-12, 13-15, 16-17): ver _cs_prep.py (se genera solo)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
import _cs_prep

_cs_prep.preparar(os.path.join(SRCDIR, 'copia_de_can_t_stop_the_feeling.pdf'),
                  os.path.join(SRCDIR, 'cant_stop_recto.pdf'))


def _n(p, d='e', b=None):
    ev = {'pitch': p, 'dur': d}
    if b is not None:
        ev['beam'] = b
    return ev


def _r(d='e'):
    return {'rest': True, 'dur': d}


# cc. 10 medidos: derecha Do, silencio x3 + silencio de negra; izquierda silencio, La, ... La Sol La
_DER = [_n('C4'), _r(), _n('C4'), _r(), _n('C4'), _r(), _r('q')]
_IZQ = [_r(), _n('A3'), _r(), _n('A3'), _r(), _n('A3', 'e', 0), _n('G3', 'e', 0), _n('A3', 'e', 0)]

SPEC = dict(
    num=15, slug='cant_stop', pdf='cant_stop_recto.pdf', time_sig=(4, 4),
    titulo="Can't Stop the Feeling!", autor='Justin Timberlake · de la pel·lícula "Trolls" (2016)',
    kicker="Alba · peça 15 · Can't Stop the Feeling!", mes='Juliol',
    yt='https://www.youtube.com/results?search_query=cant+stop+the+feeling+piano+tutorial',
    credito="Partitura: Can't Stop the Feeling! (Drive), girada i recol·locada. Anotacions: T-Clas.",
    ficha=FICHA(
        datos=[('Tonalitat', 'Do major'), ('Compàs', '4/4'), ('Tempo', 'Sense indicar'),
               ('Figura curta', 'Corxera'), ('Compassos', '17')],
        total=17,
        secciones=[('A', 1, 4, 'La frase', AZUL), ('A', 5, 8, 'Torna i puja a Sol', AZUL),
                   ('B', 9, 17, 'Cops solts i final', OCRE)],
        ideas=[('LA DRETA', 'Do, Re, Mi i Sol',
                'Quatre notes veïnes, gairebé totes corxeres. Només tecles blanques.'),
               ('L\'ESQUERRA', 'La i Sol',
                'Entra a poc a poc: un La solt, i des del c. 9 La, Sol i (una vegada) Mi.'),
               ('ELS SILENCIS', 'Marquen el ritme',
                'Hi ha molts silencis. Compta\'ls en veu alta: també són música.'),
               ('EL VAIVÉ', 'Do · silenci · Do',
                'Als cc. 10, 12, 14 i 16 la dreta cau al pols i l\'esquerra, a la "i".')],
        especial=[
            'No té armadura ni alteracions: només tecles blanques.',
            'El compàs és 4/4. No porta tempo ni matisos.',
            'Les mans són a prop: la dreta al voltant del Do central i l\'esquerra al La de sota.',
            'L\'esquerra descansa un compàs sencer als cc. 1, 4, 8 i 17; la dreta, al c. 9.',
            'Acaba en Do (negra amb puntet) i silencis.'],
        reto='Que les mans es tornin sense trepitjar-se: la dreta al pols, l\'esquerra a la "i". '
             'Ets capaç de no perdre\'t?',
        truco='Compta "1-i-2-i-3-i-4-i" i fes picades de mans del c. 10: forta al pols, fluixa '
              'a la "i". Després, només la dreta.',
        sabias='Justin Timberlake la va escriure amb Max Martin i Shellback per a la pel·lícula '
               '"Trolls" (2016) i va ser nominada a l\'Oscar a la millor cançó original.',
        qr_texto='Escolta la tornada i marca el pols amb el peu: la dreta cau a sobre.',
        ts=(4, 4), cuenta_titulo='El vaivé del c. 10, mesurat',
        cuenta_pie='Un compàs de cada mà: la dreta toca al pols i l\'esquerra, a la "i" que hi '
                   'ha entre pols i pols.',
        ritmos=[('LA DRETA', 'c. 10', _DER, AZUL, 'treble', None),
                ('L\'ESQUERRA', 'c. 10', _IZQ, OCRE, 'bass', None)]),
    manos=dict(
        titulo='Cada mà, per separat',
        sub='Poques notes i molts silencis: compta bé i tot surt.',
        tit_izq='MÀ ESQUERRA', tit_der='MÀ DRETA',
        izq=[('Compta els silencis', 'Als cc. 1 i 4 no es toca res. Compta 1-2-3-4 en veu alta '
                                     'amb el compàs buit.'),
             ('Un sol La', 'Cc. 2-6: un La per compàs. Cau a l\'1 (cc. 3 i 5) o a la "i" '
                           'del 3 (cc. 2 i 6).'),
             ('La, Mi, Sol, La', 'El c. 9 és el més mogut. Aprèn només aquest compàs, a poc a '
                                 'poc.'),
             ('El vaivé', 'Cc. 10, 12, 14, 16: La, La, i La-Sol-La. Sempre a la "i".')],
        der=[('Quatre notes', 'Do, Re, Mi i Sol, amb la mà oberta i còmoda en una posició.'),
             ('Entrar tard', 'Els cc. 1, 3 i 5 comencen amb silenci: compta i entra a la "i" '
                             'del 3.'),
             ('L\'escaleta', 'Cc. 4 i 8: Mi, Re, Do, Re, Mi, Re, Do, Do. Vuit corxeres '
                              'regulars.'),
             ('Do, silenci', 'Cc. 10, 12, 14, 16: Do, silenci, tres vegades. El silenci val '
                             'el mateix que la nota.')],
        tecnica=['Canell solt: les corxeres, lleugeres, sense picar.',
                 'Compta "1-i-2-i-3-i-4-i" en veu alta, també als silencis.',
                 'Les mans gairebé no es mouen: queda\'t a prop del Do central.']),
    bloques=[
        B(1, 'cc. 1-4', 'La frase d\'entrada', (0, 0),
          D('grupos', 'Compta: 1-i-2-i-3-i-4-i', (4, 2, ['1 i', '2 i', '3 i', '4 i'])),
          [('IZQUIERDA', 'c. 1 i c. 4: silenci. Als cc. 2 i 3, un sol La.'),
           ('DERECHA', 'Dos temps i mig de silenci, i entren Mi, Re, Do. Al c. 4: '
                       'Mi, Re, Do, Re, Mi, Re, Do, Do.'),
           ('JUNTAS', 'Un compàs cada vegada; el c. 4, només amb la dreta.'),
           ('OJO', 'Al c. 3 la dreta entra amb Do, Do, Re. Compta abans d\'entrar!')]),
        B(2, 'cc. 5-6', 'Torna la frase i puja a Sol', (1, 1),
          D('cadena', 'Al c. 6', [('Mi', False), ('Sol', True)]),
          [('IZQUIERDA', 'Un La a l\'1 (c. 5) i un altre a la "i" del 3 (c. 6).'),
           ('DERECHA', 'c. 5 com el c. 1. Al c. 6: Mi i Sol (pugen), dos silencis i Do, Do.'),
           ('JUNTAS', 'Els dos compassos en bucle.'),
           ('OJO', 'El salt de Mi a Sol se salta el Fa: mira la mà!')]),
        B(3, 'cc. 7-9', 'L\'escaleta i el c. 9', (2, 2),
          D('cadena', 'Al c. 9', [('La', False), ('Mi', False), ('Sol', False),
                                  ('La', True)]),
          [('IZQUIERDA', 'c. 7: La i La. c. 8: silenci. c. 9: La, silenci, Mi, Sol, La.'),
           ('DERECHA', 'c. 7: Do, Re. c. 8: Mi, Re, Do, Re, Mi, Re, Do, Do. c. 9: silenci.'),
           ('JUNTAS', 'Primer el c. 7, després el c. 9, i al final els tres.'),
           ('OJO', 'Al c. 9 l\'esquerra es belluga i la dreta calla.')]),
        B(4, 'cc. 10-12', 'Do, silenci, Do', (3, 3),
          D('fichas', 'Un compàs de 4 temps: Do = dreta · La i Sol = esquerra',
            ['1 Do', 'i La', '2 Do', 'i La', '3 Do', 'i La', '4 Sol', 'i La']),
          [('IZQUIERDA', 'c. 10: silenci, La, silenci, La, silenci, La, Sol, La.'),
           ('DERECHA', 'c. 10: Do, silenci, tres vegades. c. 11: Do, Do, Do, Do, Mi.'),
           ('JUNTAS', 'Compta "1-i-2-i": la dreta al número, l\'esquerra a la "i".'),
           ('OJO', 'Al c. 11 l\'esquerra entra al final amb Sol i La.')]),
        B(5, 'cc. 13-15', 'Sol i La, i altre cop el vaivé', (4, 4),
          D('cadena', 'El camí', [('c. 13 Do solt', False), ('c. 14 vaivé', False),
                                  ('c. 15 amb Mi', True)]),
          [('IZQUIERDA', 'c. 13: silenci i, al final, Sol i La. c. 14 com el c. 10.'),
           ('DERECHA', 'c. 13: Do i dos temps de silenci. c. 15: Do, Do, Do, Mi.'),
           ('JUNTAS', 'Del c. 13 al c. 14: el Sol-La de l\'esquerra llança el vaivé.'),
           ('OJO', 'c. 15: l\'esquerra toca La a la "i" de l\'1 i acaba amb Sol i La.')]),
        B(6, 'cc. 16-17', 'El final', (5, 5),
          D('cadena', 'El final', [('c. 16 vaivé', False), ('Do llarg', True),
                                   ('silenci', False)]),
          [('IZQUIERDA', 'c. 16: el vaivé de sempre. c. 17: silenci.'),
           ('DERECHA', 'c. 16: Do, silenci, tres vegades. c. 17: Do (negra amb puntet).'),
           ('JUNTAS', 'Atura\'t al c. 17: deixa anar el Do i que s\'apagui.'),
           ('A TEMPO', 'Tota la peça, comptant els silencis.')]),
    ],
    cortes={1: [248.2, 392.2], 2: [168.2, 312.2]}, corte_titulo=98.2,
    burb={
        0: [('arriba', 290, 'DER', 'Dos temps i mig de silenci, i entren Mi, Re, Do. Compta '
                                   'abans d\'entrar.', 0.2),
            ('abajo', 270, 'IZQ', 'Els cc. 1 i 4 són silenci. Als cc. 2 i 3, un sol La.',
             0.44)],
        1: [('arriba', 250, 'DER', 'Al c. 6 la melodia puja de Mi a Sol.', 0.33),
            ('abajo', 270, 'IZQ', 'Un La a l\'1 (c. 5) i un altre a la "i" del 3 (c. 6).', 0.42)],
        2: [('arriba', 270, 'OJO', 'c. 8: vuit corxeres seguides, Mi Re Do Re, Mi Re Do Do. '
                                   'L\'esquerra calla. Vés a poc a poc!', 0.39),
            ('abajo', 340, 'IZQ', 'c. 9: La, silenci, Mi, Sol, La. La dreta calla.', 0.57)],
        3: [('arriba', 280, 'AMB', 'La dreta cau al pols i l\'esquerra a la "i": es tornen.',
             0.17),
            ('abajo', 270, 'OJO', 'c. 11: quatre Do i un Mi. L\'esquerra entra al final: Sol, '
                                  'La. Atenta!', 0.44)],
        4: [('arriba', 250, 'DER', 'c. 13: un Do i dos temps de silenci.', 0.09),
            ('abajo', 270, 'IZQ', 'c. 13: només Sol i La, al final del compàs.', 0.22)],
        5: [('arriba', 290, 'OJO', 'c. 17: l\'últim Do dura una negra amb puntet; després, '
                                   'silenci. Final! Molt bé!', 0.42)],
    },
    marcas=[],
    misol=dict(
        manos='Aquí els silencis manen: compta "1-i-2-i" en veu alta i les notes cauran soles al '
              'seu lloc.',
        guia='Fes un bloc cada dia i no passis al següent fins que et surti net. El vaivé del '
             'bloc 4 és el repte!',
        pauta='Inventa un vaivé teu: un compàs de 4/4 amb Do i silencis a la dreta i La a la '
              'esquerra. O copia el c. 10!'),
    pie_pauta='la clau la poses tu · copia un compàs o escriu l\'escala de Do major')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_ba_cant_stop.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
