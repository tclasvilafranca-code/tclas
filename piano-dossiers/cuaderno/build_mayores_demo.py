# -*- coding: utf-8 -*-
"""DEMO del dosier para alumnos de 12-20 anos (clases de media hora).

   Pieza: The Heart Asks Pleasure First (Michael Nyman), de la carpeta de Eva
   en Drive. Todo lo que afirma la ficha esta MEDIDO sobre ese PDF (3 paginas,
   28 compases, A4), mirado a 110 y 300 dpi:

     - sin armadura, acordes de La menor (Am) y, a mitad, Mi mayor (E);
     - 12/8 y, en los cc. 5, 6, 10 y 11, 9/8 y 6/8;
     - "Con moto" y, desde el c. 3, "Piu mosso (corchea = 180)";
     - figura mas corta: SEMICORCHEA (dos barras); seis por pulso;
     - barra de repeticion que empieza en el c. 15, 1a casilla en el c. 23 y
       2a en el c. 25; 8va en la izquierda de los cc. 15-16.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import segno
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from portada import W, H
from ficha_info import build_ficha

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, 'entrega')
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

YT = ('https://www.youtube.com/results?search_query='
      'the+heart+asks+pleasure+first+nyman+piano')


def corcheas_12_8(pitch='B3'):
    """Un compás de 12/8 contado: cuatro golpes de tres corcheas."""
    return [{'pitch': pitch, 'dur': 'e', 'beam': g} for g in range(4) for _ in range(3)]


CFG = dict(
    kicker='Demo · pieza 1 · nivel intermedio',
    titulo='The Heart Asks Pleasure First',
    autor='Michael Nyman · de la película "El piano" · transcripción de David Jůna',
    page_num=2, time_sig=(12, 8),
    datos=[('Tonalidad', 'La menor'), ('Compás', '12/8 · cambia'),
           ('Tempo', 'Con moto'), ('Figura corta', 'Semicorchea'),
           ('Compases', '28')],
    total_compases=28,
    secciones=[
        ('A', 1, 2, 'Entrada · Con moto', AZUL),
        ('B', 3, 12, 'Più mosso · cambia el compás', OCRE),
        ('A', 13, 14, 'Vuelve la entrada', AZUL),
        ('C', 15, 22, 'Se repite · octavas graves', OCRE),
        ('D', 23, 28, '1ª y 2ª vez · final', AZUL),
    ],
    armonia=dict(
        titulo='Los acordes, de un vistazo',
        tarjetas=[
            ('CC. 1-2', 'Bajo: Mi · Re · Do',
             'La menor, Sol mayor y La menor en inversión (la nota grave no es la fundamental), '
             'y Re mayor. En tu partitura: Am/E, G/D, Am/C, D.'),
            ('CC. 3-8', 'La m · Fa · Sol · Mi',
             'La menor, Fa mayor, Sol mayor y la cadencia: Mi con cuarta suspendida → Mi mayor → '
             'La menor (dominante → tónica). En tu partitura: Esus4, E, Am.'),
            ('CC. 9-12', 'El mismo camino',
             'Repite Fa, Sol, La menor y la misma cadencia sobre la dominante. El 9/8 y el 6/8 '
             'acortan el camino de vuelta.'),
            ('CC. 13-28', 'Vuelve la entrada',
             'Los mismos acordes de los cc. 1-2 en los cc. 13-14 y en todo el final: lo que '
             'aprendes al principio se usa varias veces.'),
        ],
        pie='Encima de la partitura los acordes vienen en cifrado americano (A = La, C = Do, '
            'D = Re, E = Mi, F = Fa, G = Sol; "m" = menor; la barra indica la nota del bajo). '
            'Aquí los llamamos como siempre.',
    ),
    titulo_ritmos='Cómo se cuenta el 12/8',
    pie_ritmos='Un compás de 12/8: cuatro golpes de tres corcheas (1 2 3 · 4 5 6 · 7 8 9 · '
               '10 11 12). Tu pieza parte cada corchea en dos semicorcheas: seis por golpe. '
               'Aquí solo el ritmo, sobre una nota cualquiera.',
    ritmos=[
        ('LA CUENTA', '12/8 · cuatro golpes', corcheas_12_8(), OCRE, 'bass', None),
    ],
    especial=[
        'Pone "Con moto" y, en el c. 3, "Più mosso" con la corchea a 180.',
        'El compás cambia: 12/8 casi siempre, y 9/8 y 6/8 en los cc. 5-6 y 10-11.',
        'Hay semicorcheas de principio a fin: seis por cada golpe.',
        'La izquierda lleva "con Ped." (pedal) al principio.',
        'La repetición empieza en el c. 15, con 1ª casilla (c. 23) y 2ª casilla (c. 25).',
        'En los cc. 15-16 la izquierda va escrita con 8va (ottava bassa): suena una octava más grave.',
    ],
    reto='Los cambios de 12/8 a 9/8 y a 6/8. Las semicorcheas no se frenan: lo que cambia es '
         'cuántas caben antes de volver a empezar. Si cuentas "uno" en cada golpe sin '
         'pararte, sale solo.',
    truco='Toca solo la izquierda de los cc. 5-6 con el metrónomo en una corchea por golpe, '
          'cuenta en voz alta 1-2-3 / 1-2-3 / 1-2-3 y 1-2-3 / 1-2-3, y no sueltes la '
          'cuenta aunque cambie el compás. La derecha, cuando la izquierda no te pida atención.',
    sabias='El título es el primer verso de un poema de Emily Dickinson, y Michael Nyman la '
           'compuso para la película "El piano" (1993) de Jane Campion. Es música minimalista: '
           'una misma figura que se repite con pequeños cambios. La entrada vuelve '
           'en los cc. 13-14 y 23-28.',
    qr=dict(titulo='Escúchala',
            texto='Escucha el primer minuto con la partitura delante y sigue los cambios de '
                  'compás con el dedo.'),
)


def main():
    os.makedirs(OUT, exist_ok=True)
    qr = os.path.join(OUT, '_qr_demo.png')
    segno.make(YT, error='m').save(qr, scale=10, border=2, dark='#1A2332', light='#F3F1EA')
    cfg = dict(CFG)
    cfg['qr'] = dict(cfg['qr'], png=qr)
    dst = os.path.join(OUT, 'DEMO_Ficha_Heart.pdf')
    c = canvas.Canvas(dst, pagesize=(W, H))
    y = build_ficha(c, cfg)
    c.save()
    os.remove(qr)
    print('y final', y, '->', dst)


if __name__ == '__main__':
    main()
