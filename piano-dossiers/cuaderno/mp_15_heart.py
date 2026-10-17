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


def _b(num, cc, nombre, sist, diag, pasos):
    return dict(num=num, cc=cc, nombre=nombre, sist=sist, diag=diag, pasos=pasos,
                color=_C[(num - 1) % len(_C)])


def _diag(num):
    return {
        1: ('grupos', 'Un compás de 12/8 = 4 golpes · cada golpe, 6 notas',
            (4, 6, ['golpe 1', 'golpe 2', 'golpe 3', 'golpe 4'])),
        2: ('capas', 'Más rápido · tres capas que suenan a la vez',
            [('MD melodía', 'barras', AZUL), ('MD semicorcheas', 'puntos', AZUL),
             ('MI semicorcheas', 'puntos', OCRE)]),
        3: ('cuenta', 'La cuenta no se rompe · cada grupo de tres = un golpe',
            [('c. 5 · 9/8', 3, 3), ('c. 6 · 6/8', 2, 3), ('c. 7 · 12/8', 4, 3)]),
        4: ('cadena', 'La cadencia (cc. 7-8 y 12)',
            [('Mi con 4.ª', False), ('Mi mayor', False), ('La menor', True)]),
        5: ('cadena', 'Es el bloque 1', [('cc. 13-14', True), ('= cc. 1-2', False)]),
        6: ('cadena', 'El 8va · lo escrito y lo que suena (mano izquierda)',
            [('nota escrita', False), ('suena una octava más grave', True)]),
        7: ('cadena', 'El recorrido',
            [('1-22', False), ('1ª: 23-24', True), ('↩ 15-22', False), ('2ª: 25-26', True),
             ('27-28', False), ('FIN', True)]),
    }[num]


_NOM = {1: 'La entrada', 2: 'Más rápido: Più mosso', 3: 'Cambia el compás',
        4: 'Cierre de la frase y vuelta', 5: 'Vuelve la entrada', 6: 'La repetición',
        7: 'Primera y segunda vez'}
_SIST = {1: (0, 0), 2: (1, 1), 3: (2, 2), 4: (3, 5), 5: (6, 6), 6: (7, 10), 7: (11, 13)}

SPEC = dict(
    num=15, slug='heart', pdf='michael_nyman_the_heart_asks.pdf',
    titulo=demo.CFG['titulo'], autor=demo.CFG['autor'], time_sig=(12, 8),
    kicker='Eva · pieza 15 · The Heart Asks Pleasure First', mes='Junio-julio',
    yt=demo.YT, ficha=dict(demo.CFG),
    credito="Partitura: Michael Nyman, transcripción de David Jůna (DJ's Sheet Music Archive). "
            "Anotaciones: T-Clas.",
    manos=dict(izq=g.IZQ, der=g.DER),
    bloques=[_b(n, cc, _NOM[n], _SIST[n], _diag(n), pasos)
             for (n, cc, nom, pasos) in [(b[0], b[1], b[2], b[3]) for b in g.GUIA]],
    cortes={1: [322.5, 482, 620.2], 2: [193.2, 339.2, 481.2, 638.5], 3: [199.2, 348, 498.5, 639]},
    corte_titulo=137.5,
    burb={
        0: [('arriba', 300, 'DER', 'Al principio hace dos cosas: arriba, notas largas que cantan; '
                                    'debajo, semicorcheas. Estudia cada voz sola.', 250),
            ('abajo', 238, 'IZQ', 'Empieza por aquí, tú sola: cada golpe son 6 notas. Despacio y '
                                  'parejo.', 150),
            ('abajo', 238, 'AMB', 'Cuenta 4 golpes por compás: 1-2-3, 4-5-6, 7-8-9, 10-11-12.', 430)],
        1: [('arriba', 300, 'DER', 'Los acentos (>) marcan la melodía: tócalos un poco más fuertes '
                                   'que lo de debajo.', 190)],
        2: [('arriba', 330, 'OJO', 'El compás cambia: 9/8 son 3 golpes, 6/8 son 2. Cuenta 1-2-3 en '
                                   'cada golpe y no frenes.', 350)],
        3: [('arriba', 300, 'AMB', 'Cierre de la frase: la tensión de Mi se resuelve en La menor. '
                                   'Afloja la mano al llegar.', 150),
            ('abajo', 270, 'IZQ', 'Las notas ligadas del bajo se mantienen: no se vuelven a tocar.',
             130)],
        4: [('arriba', 300, 'AMB', 'Mismo camino que los cc. 3-8: ya lo conoces. Fíjate en los '
                                   'cambios a 9/8 y a 6/8.', 344)],
        5: [('arriba', 300, 'OJO', 'c. 11: 6/8 y luego 12/8. Cuenta 1-2-3 / 1-2-3 y después cuatro '
                                   'grupos de tres.', 75)],
        6: [('arriba', 300, 'AMB', 'cc. 13-14: otra vez la entrada. Tócala de memoria, es el '
                                   'bloque 1.', 120)],
        7: [('arriba', 330, 'AMB', 'Empieza la repetición. Acordes nuevos: C = Do, G = Sol, '
                                   'Am = La menor, E = Mi.', 60),
            ('abajo', 300, 'IZQ', '8va: toca la izquierda una octava más grave mientras dure la '
                                  'línea de puntos.', 230)],
        11: [('arriba', 330, 'OJO', 'La primera vez, al llegar a la casilla 1 vuelves al signo de '
                                    'repetición del c. 15.', 80)],
        12: [('arriba', 330, 'OJO', 'La segunda vez NO repitas: salta a la casilla 2 (cc. 25-26) y '
                                    'sigue hasta el final.', 80)],
        13: [('arriba', 300, 'AMB', 'Los dos últimos compases: baja el volumen y acaba con calma '
                                    'sobre la doble barra.', 540)],
    },
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
