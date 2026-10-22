# -*- coding: utf-8 -*-
"""Peça 9 · La Panthère rose (Pink Panther, Henry Mancini · versió fàcil «Première année»).
   MESURAT sobre el PDF (1 pàgina, A4; notes pintades amb colorear_notas.py): sense armadura, 4/4,
   25 compassos en 3 sistemes (9 + 9 + 7). Cc. 1-3: silenci de compàs sencer a la dreta, l'esquerra
   toca Do3 i Sol3 llargs; c. 4: tres silencis de negra i Si3 (la melodia comença). La melodia puja
   cromàticament (sostenits ♯ a Do, Re, Fa, Sol) i hi ha molts silencis de negra. Esquerra: Do3, Sol3 i, a
   la fi, Re3, notes llargues (rodones i blanques). Final: Do rodona a les dues mans (c. 25).
   Digitació impresa als cc. 1-6 (5-1, 1-2-3-4)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403
from lo_comun import MESES, COLORS, kick, yt

_q = lambda p: {'pitch': p, 'dur': 'q'}

SPEC = dict(
    num=9, slug='panthere', pdf='panthere.pdf', time_sig=(4, 4),
    titulo='La Pantera Rosa',
    autor='Henry Mancini · versió fàcil «Première année»',
    kicker=kick(9, 'La Pantera Rosa'), mes=MESES[9],
    yt=yt('pink panther theme piano easy'),
    credito='Partitura: versió fàcil «Première année». Notes pintades i anotacions: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalitat', 'Sense armadura'), ('Compàs', '4/4'), ('Tempo', 'No indicat'),
               ('Figura curta', 'Negra'), ('Compassos', '25')],
        total=25,
        secciones=[('A', 1, 9, 'Introducció i primera frase', AZUL),
                   ('A', 10, 18, 'Segona frase', OCRE),
                   ('B', 19, 25, 'Frase final', AZUL)],
        ideas=[('LA INTRODUCCIÓ', 'Tres compassos de silenci',
                'La dreta descansa tres compassos sencers. La mà esquerra marca el pas amb Do i Sol.'),
               ('LA MELODIA', 'Sigil·losa, amb sostenits',
                'Puja de mig en mig to: hi ha moltes tecles negres (♯). Per això sona tan misteriosa.'),
               ('ELS SILENCIS', 'Cada pausa compta',
                'Silencis de negra entre les notes: compta-los i la melodia saltarà com una pantera.'),
               ("L'ESQUERRA", 'Do i Sol, i un Re',
                'Notes llargues: Do, Sol i, de tant en tant, Re. El pas fort de la cançó.')],
        ideas_titulo='La peça en quatre idees',
        ideas_pie=COLORS,
        especial=[
            "No hi ha armadura, però hi ha molts sostenits (♯) a la dreta: tecles negres.",
            "Els cc. 1-3 són tres silencis de compàs sencer a la dreta: compta-los!",
            'Al c. 4 entra la melodia després de tres silencis de negra.',
            "L'esquerra només toca Do, Sol i algun Re, amb notes llargues.",
            'Acaba amb un Do llarg a les dues mans.'],
        reto="Toca la melodia amb silencis ben comptats: el misteri de la pantera és que no es veu quan arriba!",
        truco="Primer toca només la dreta i marca els silencis amb un «shh» en veu baixa.",
        sabias="Henry Mancini va compondre aquest tema per a la pel·lícula La Pantera Rosa (1963). "
               "El dibuix animat de la pantera surt als crèdits de la pel·lícula.",
        qr_texto='Escolta-la i fes passos de pantera amb la partitura al davant.',
        ts=(4, 4),
        cuenta_titulo='Com es compta una frase amb silencis',
        cuenta_pie="Tres silencis de negra i una nota: «1 (sil.) 2 (sil.) 3 (sil.) 4». Aquí només el ritme.",
        ritmos=[('TRES SILENCIS I UNA NOTA', '4/4 · c. 4 · 1 · 2 · 3 · 4',
                 [{'rest': True, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, {'rest': True, 'dur': 'q'}, _q('B4')],
                 OCRE, 'treble', None),
                ('UN COMPÀS DE SILENCI', '4/4 · cc. 1-3',
                 [{'rest': True, 'dur': 'w'}], AZUL, 'treble', None)]),
    manos=dict(
        izq=[('Do i Sol llargs', 'Una nota quatre temps: prem i compta 1-2-3-4. El Do amb el dit 5 i el Sol amb el dit 1.'),
             ('Salta de Do a Sol', 'És un salt de cinc tecles blanques. Mira les posicions abans.'),
             ('Un Re al final', 'Als cc. 8-9, 17-18 apareix un Re: la mateixa mà, un pas més amunt.'),
             ('El Do final', 'Al c. 25: Do llarg, tots dos a l\'hora.')],
        der=[('Tres silencis', 'Cc. 1-3: compta 1-2-3-4 sense tocar. Els dits quiets!'),
             ('Si Do Re', "C. 4-5: la melodia arrenca amb Si i Do. Dits 1-2-3-4."),
             ('Els sostenits', "Tecles negres: sempre més amunt i a la dreta de la blanca. Mira el ♯ abans de tocar."),
             ('El final', 'Cc. 24-25: Fa Re Do Do i una nota llarga. Acaba i descansa.')],
        tecnica=['Compta els silencis igual que les notes.',
                 'Els sostenits (tecles negres): dits arrodonits.',
                 'Pas lent, com una pantera: sense córrer.']),
    bloques=[
        B(1, 'cc. 1-9', 'La pantera arriba', (0, 0),
          D('cadena', 'Silencis i la primera frase',
            [('cc. 1-3: silenci', False), ('c. 4: entra Si', False), ('cc. 5-9: melodia', True)]),
          [('IZQUIERDA', 'Do, Sol, Do, Sol: notes llargues. Mira-ho amb la dreta quieta.'),
           ('DERECHA', 'Tres compassos de silenci. Al c. 4, Si. Després Do, Re, Si, Do, Re, Sol...'),
           ('JUNTAS', 'Les dues mans sols als cc. 4-9: l\'esquerra marca, la dreta fa la melodia.'),
           ('OJO', 'Compta els tres primers compassos de silenci: «1-2-3-4» tres cops!')]),
        B(2, 'cc. 10-18', 'Segona frase', (1, 1),
          D('cadena', 'Igual i diferent',
            [('c. 10: Fa Re Do Do', False), ('c. 11: silenci', False), ('cc. 12-18', True)]),
          [('IZQUIERDA', 'Do, Sol i, al final, Re. Notes llargues, a la mateixa mà.'),
           ('DERECHA', 'C. 10: Fa Re Do Do. C. 11: silenci. Cc. 12-18: com els cc. 4-9.'),
           ('JUNTAS', 'Dues frases iguals: aprèn-te-les una vegada.'),
           ('OJO', 'Mira els sostenits (♯) de la dreta: tecles negres.')]),
        B(3, 'cc. 19-25', 'Frase final', (2, 2),
          D('cadena', 'De Do a Do',
            [('cc. 19-22', False), ('cc. 23-24', False), ('c. 25: Do llarg', True)]),
          [('IZQUIERDA', 'Do, Sol, Do, Sol, Sol i Do. Notes llargues.'),
           ('DERECHA', 'Cc. 19-22 com abans. Al final, Fa Re Do Do i el Do llarg del c. 25.'),
           ('JUNTAS', 'Quan arribis al Do final, aguanta els quatre temps i deixa anar.'),
           ('A TEMPO', 'Toca tota la cançó, lent i misteriós, com una pantera.')]),
    ],
    lista=['Compto els silencis dels cc. 1-3 sense equivocar-me.',
           'Toco la melodia dels cc. 4-9 amb la dreta.',
           "Toco l'esquerra: Do, Sol i Re.",
           'Toco els sostenits (♯) al seu lloc.',
           'Toco els 25 compassos sense parar.'],
    cortes={1: [222.0, 363.0]}, inicio={1: 102}, fin={1: 500},
    burb={
        0: [('arriba', 262, 'OJO', 'Tres compassos de silenci a la dreta (cc. 1-3). Compta-los!', 0.1),
            ('arriba', 262, 'IZQ', 'Do i Sol llargs: l\'esquerra marca el pas.', 0.45)],
        1: [('arriba', 262, 'DER', 'Fa Re Do Do (c. 10), després un compàs de silenci (c. 11).', 0.1),
            ('arriba', 262, 'OJO', 'Mira els ♯: tecles negres a la dreta.', 0.65)],
        2: [('arriba', 262, 'AMB', 'Última frase: com els cc. 4-9, però ara acaba.', 0.2),
            ('arriba', 262, 'DER', 'C. 25: Do llarg. Aguanta quatre temps.', 0.92)],
    },
    misol=dict(
        manos="Una pantera surt a caçar: pas lent i silenciós. Compta els silencis amb ella!",
        guia="La música és plena de ‘sostenits’: tecles negres. Els trobaràs a la dreta d'una blanca.",
        pauta="Escriu un compàs amb tres silencis de negra i una nota de color."),
    marcas=[],
    pie_pauta="la clau la poses tu · escriu tres silencis de negra i una nota")

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_lo_panthere.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
