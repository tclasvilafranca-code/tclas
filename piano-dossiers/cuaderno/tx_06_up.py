# -*- coding: utf-8 -*-
"""Pieza 6 · Up, tema principal (Giacchino), Easy version. MEDIDO sobre el PDF (1 pagina, imagen
   de baja resolucion, 35 compases en 4 sistemas de 8, 9, 10 y 8): un bemol (Fa mayor), 3/4, solo
   el matiz p en el c. 1, sin tempo, sin repeticiones, corchea como figura mas corta (sin
   semicorcheas), sin digitacion impresa. Izquierda: c. 1 en silencio y un acorde de tres o
   cuatro notas por compas (blanca con puntillo), con ligaduras entre compases (6-7, 8-9, 12-13,
   14-15, 16-17, 23-24, 25-26, 29-30, 31-32, 33-34) y becuadros en los cc. 6, 8, 11, 23, 25 y 28;
   desde el c. 18 la izquierda lee en clave de sol. Los cc. 18-27 repiten los cc. 1-10 una octava
   mas aguda y los cc. 28-35 los cc. 11-17 (+ Fa largo final)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=6, slug='up', pdf='copia_de_up.pdf', time_sig=(3, 4),
    titulo='Up · tema principal',
    autor='Michael Giacchino · música de la pel·lícula «Up» · Easy version',
    kicker='Txell · peça 6 · Up (tema principal)', mes='Febrer · 2.a quinzena',
    yt='https://www.youtube.com/results?search_query=up+pixar+main+theme+married+life+piano+easy',
    credito='Partitura: «Up - Main theme», Easy version (música de M. Giacchino). '
            'Anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Fa major'), ('Compàs', '3/4'), ('Tempo', 'Sense indicar'),
               ('Figura curta', 'Corxera'), ('Compassos', '35')],
        total=35,
        secciones=[('A', 1, 8, 'El tema', AZUL), ('B', 9, 17, 'Segona frase', OCRE),
                   ('C', 18, 27, 'El tema, més agut', AZUL), ('D', 28, 35, 'Final', OCRE)],
        ideas=[('ESQUERRA', 'Un acord per compàs',
                'Acords de tres o quatre notes, de compàs sencer. Alguns van lligats al compàs '
                'següent.'),
               ('DRETA', 'Frases amb respir',
                "Cada frase entra després d'un silenci i acaba en una nota llarga. Cal cantar-la."),
               ('ELS CANVIS', 'Un bemoll i becaires',
                "El Si és bemoll a tota la peça. A l'esquerra, algun becaire (cc. 6, 8, 11...)."),
               ('LA CLAU', 'Clau de sol a baix',
                'Des del c. 18 la mà esquerra llegeix en clau de sol: mira la clau.')],
        especial=[
            "Armadura d'un bemoll (Si♭): la peça està en Fa major.",
            'Compàs de 3/4: tres negres per compàs. No indica tempo.',
            'Només hi ha un matís: p (suau) al c. 1.',
            'La dreta entra a la «i» del 2n temps: silenci de negra i de corxera, i tres corxeres.',
            "L'esquerra calla al c. 1 i des del c. 18 llegeix en clau de sol.",
            'Els cc. 18-27 repeteixen els cc. 1-10, una octava més aguda.'],
        reto="Que l'esquerra no tapi la melodia: acords suaus (p) i la dreta cantant a sobre. "
             'Te\'n surts?',
        truco="Taral·leja la melodia abans de tocar-la. Les frases es repeteixen: n'aprens poques "
              'i valen per a tota la peça.',
        sabias="«Up» és una pel·lícula de Pixar del 2009. La seva música és de Michael Giacchino, "
               "que hi va guanyar l'Oscar a la millor banda sonora original.",
        qr_texto='Escolta-la: sents com cada frase acaba en una nota llarga?', ts=(3, 4)),
    manos=dict(
        izq=[('Un acord, un compàs', 'Cada acord dura el compàs sencer. Toca\'l, aguanta\'l i '
                                     'compta 1-2-3 sense deixar-lo anar.'),
             ('Els lligats', 'Si dos acords estan units per una lligadura (cc. 6-7), es toca el '
                             'primer i s\'aguanta.'),
             ('Els becaires', 'Als cc. 6, 8 i 11 hi ha un becaire: aquest Si no és bemoll, és '
                              'Si natural.'),
             ('Clau de sol', "Des del c. 18 l'esquerra llegeix en clau de sol. Mira la clau "
                             'abans de tocar.')],
        der=[('Cantar primer', 'Taral·leja els cc. 1-8: Fa-La-Fa i Mi llarg. Després toca\'ls a '
                               'poc a poc.'),
             ('Entrar a la «i»', 'Compta «1, 2-i, 3-i»: la melodia entra a la «i» del 2. Els '
                                 'silencis compten.'),
             ('Les frases', 'Cada frase acaba en una nota llarga (cc. 2, 10 i 17). Respira '
                            'allà.'),
             ('Una octava amunt', 'Al c. 18 torna el tema, igual però més agut: llegeix les '
                                  'notes altes amb calma.')],
        tecnica=['Braç solt i dits corbats: acords sense prémer.',
                 "L'esquerra sona suau (p) i la melodia mana.",
                 'Compta 1-2-3 sense córrer i sense parar.']),
    bloques=[
        B(1, 'cc. 1-8', 'El tema', (0, 0),
          D('cadena', 'El c. 1 de la dreta',
            [('silenci de negra', False), ('silenci de corxera', False), ('3 corxeres', True)]),
          [('IZQUIERDA', "El c. 1 en silenci. Del 2 al 7, un acord per compàs."),
           ('DERECHA', 'Fa-La-Fa i Mi llarg. Frases de dos compassos.'),
           ('JUNTAS', 'De dos en dos compassos: 1-2, 3-4, 5-6, 7-8.'),
           ('OJO', "Becaire a l'esquerra (cc. 6 i 8) i matís p al c. 1. Ho veus?")]),
        B(2, 'cc. 9-17', 'Segona frase', (1, 1),
          D('cadena', 'Tres frases amb nota llarga',
            [('cc. 9-10', False), ('cc. 11-13', False), ('cc. 14-17', True)]),
          [('IZQUIERDA', 'Un acord per compàs. Lligats: 12-13, 14-15 i 16-17. Becaire al 11.'),
           ('DERECHA', 'Cada frase acaba en nota llarga (cc. 10, 13 i 17).'),
           ('JUNTAS', 'Frase a frase: 9-10, 11-13 i 14-17.'),
           ('OJO', 'Des del c. 14 la melodia puja per graus fins a la nota llarga del c. 17.')]),
        B(3, 'cc. 18-27', 'El tema, més agut', (2, 2),
          D('cadena', 'La mateixa melodia',
            [('cc. 1-10', False), ('una octava amunt', True), ('cc. 18-27', False)]),
          [('IZQUIERDA', 'El c. 18 en silenci, amb canvi a clau de sol. Després, un acord per '
                         'compàs.'),
           ('DERECHA', 'És la melodia dels cc. 1-10, més aguda: línies addicionals a dalt.'),
           ('JUNTAS', 'Toca abans els cc. 1-10: és la mateixa música en un altre lloc.'),
           ('OJO', 'Becaires als cc. 23 i 25, lligats amb el compàs següent.')]),
        B(4, 'cc. 28-35', 'El final', (3, 3),
          D('cadena', 'Cap al final',
            [('cc. 28-33', False), ('Mi llarg', False), ('Fa llarg: FINAL', True)]),
          [('IZQUIERDA', 'Becaire al 28. Lligats: 29-30, 31-32 i 33-34. El 35, un acord.'),
           ('DERECHA', 'La frase torna i puja per graus: acaba en Mi llarg i Fa llarg.'),
           ('JUNTAS', 'Els quatre últims compassos en bucle, cantant.'),
           ('A TEMPO', 'La peça sencera seguida. Aguanta el Fa final el compàs sencer.')]),
    ],
    cortes={1: [264.0, 426.5, 592.0]},
    corte_titulo=122.2,
    burb={
        0: [('arriba', 250, 'DER', 'Entres a la «i» del 2n temps: silenci de negra, silenci de '
                                   'corxera i tres corxeres. Matís p.', 0.12),
            ('arriba', 250, 'IZQ', "El c. 1 és silenci. Al c. 2 entra el primer acord.", 0.3),
            ('abajo', 300, 'OJO', "Becaires a l'esquerra (cc. 6 i 8): aquest Si no és bemoll. "
                                  'Compte!', 0.8)],
        1: [('arriba', 300, 'AMB', 'Cada frase acaba en una nota llarga (cc. 10, 13 i 17): '
                                   'respira allà.', 0.2),
            ('abajo', 300, 'IZQ', "Lligats: 12-13, 14-15 i 16-17. Toca el primer i aguanta. "
                                  'Becaire al c. 11.', 0.6)],
        2: [('arriba', 250, 'DER', 'Torna el tema una octava més aguda: és la música dels cc. '
                                   '1-10.', 0.1),
            ('arriba', 250, 'IZQ', "Des d'aquí l'esquerra llegeix en clau de sol: mira la clau.",
             0.2),
            ('abajo', 300, 'OJO', 'Becaires als cc. 23 i 25, lligats amb el compàs següent. '
                                  'Aguanta!', 0.6)],
        3: [('arriba', 300, 'IZQ', 'Becaire al c. 28. Lligats: 29-30, 31-32 i 33-34.', 0.1),
            ('abajo', 300, 'OJO', "Fa llarg final (c. 35): aguanta'l el compàs sencer i deixa "
                                  'anar amb les dues mans. Bravo!', 0.9)],
    },
    marcas=[],
    misol=dict(manos='Truc: taral·leja la melodia mentre toques els acords. Si la cantes, la '
                     'mà dreta no es perd.',
               guia='Ànim! La peça només té quatre trossos i el tercer és el primer més agut. '
                    'Ja en saps la meitat!',
               pauta='Copia el c. 1 (dos silencis i tres corxeres) i inventa\'t tu la '
                     'continuació en Fa major!'),
    pie_pauta="la clau la poses tu · copia el c. 1 o escriu l'escala de Fa major")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_tx_up.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
