# -*- coding: utf-8 -*-
"""Cruza la figura IMPRESA en la partitura con la que el dosier DIBUJA.

   Es la comprobacion que faltaba, y la que dejo pasar el fallo mas gordo del
   proyecto: durante meses varias piezas se escribieron en corcheas "porque el
   motor no sabe dibujar la semicorchea", y cuando el motor aprendio a
   dibujarla esas frases se quedaron en el papel. El alumno leia una hoja que
   le contaba una figura que su partitura no tiene, o —peor— no veia nunca la
   figura que si tiene.

   `auditar_vocabulario.py` comprueba que no se HABLE de lo que no se dibuja.
   Esto comprueba lo otro: que se DIBUJE lo que la partitura trae.

   Lee `figuras_medidas.json`, que genera `medir_figuras_todas.py` (medir tarda
   varios minutos y no puede colgar de cada auditoria).

   Uso:  python3 auditar_figuras.py [prefijo ...]
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(HERE, 'figuras_medidas.json')

# A partir de cuantas barras dobles medidas se considera que la semicorchea es
# un rasgo REAL de la pieza y no ruido del detector. Por debajo hay falsos
# positivos (cabezas de acorde, lineas adicionales) y hay que mirarlo a ojo.
UMBRAL = 20

# Partituras NO MEDIBLES (una foto de baja resolucion dentro de un PDF) que ya
# se han mirado a ojo, a tamano grande, y lo que se vio. Sin esta lista el
# auditor no puede decir nada de ellas, y callarse no vale.
MIRADAS = {
    'Como entrenar a tu dragon.': 'corcheas · una sola barra por grupo en toda la pieza',
    'Copia de Copia de Como entrenar a tu dragon.': 'la misma edicion del Flying Theme: corcheas',
    '-PEACHES.': 'CORCHEAS hasta el c. 12 y SEMICORCHEAS del 13 en adelante',
    'OH WHEN THE SAINT.pdf': 'corcheas · sin barras dobles',
    'Oh when the Saint.pdf': 'la misma edicion: corcheas',
}


def cargar():
    if not os.path.exists(JSON):
        print('falta %s · ejecuta antes medir_figuras_todas.py' % os.path.basename(JSON))
        sys.exit(2)
    with open(JSON) as fh:
        return json.load(fh)


def main(prefijos=None):
    datos = cargar()
    if prefijos:
        datos = {m: d for m, d in datos.items()
                 if m.split('_')[0] in prefijos}

    huecos, sobra, mirar = [], [], []
    for m in sorted(datos):
        d = datos[m]
        estado = d.get('estado')
        escribe = d.get('escribe', 0)
        if estado == 'ok':
            largas = d.get('largas', 0)
            if largas >= UMBRAL and not escribe:
                huecos.append((m, largas, d['partitura']))
            elif largas == 0 and d.get('escribe_a_mano'):
                # Solo lo escrito A MANO: el material de apoyo de `relleno` es
                # tecnica generica sobre la tonalidad, va marcado como tal y
                # puede llevar una figura que la pieza no tenga.
                sobra.append((m, d['escribe_a_mano'], d['partitura']))
        elif estado == 'no medible':
            if d.get('partitura') not in MIRADAS:
                mirar.append((m, d['partitura'], d.get('motivo', '')))

    print('piezas comprobadas: %d (umbral: %d barras dobles)' % (len(datos), UMBRAL))

    print('\nLA PARTITURA LA LLEVA Y EL DOSIER NO LA DIBUJA: %d' % len(huecos))
    for m, largas, p in sorted(huecos, key=lambda x: -x[1]):
        print('   %4d barras dobles · %-22s %s' % (largas, m, p[:44]))

    print('\nEL DOSIER LA DIBUJA Y LA PARTITURA NO LA LLEVA: %d' % len(sobra))
    for m, escribe, p in sobra:
        print('   escribe %2d · %-22s %s' % (escribe, m, p[:44]))

    print('\nSin mirar (partitura de baja resolucion y no anotada en MIRADAS): %d'
          % len(mirar))
    for m, p, motivo in mirar:
        print('   %-22s %-40s %s' % (m, p[:40], motivo))

    if huecos or sobra or mirar:
        print('\n%d COSAS QUE MIRAR' % (len(huecos) + len(sobra) + len(mirar)))
        return 1
    print('\nFIGURAS OK — lo que la partitura trae impreso, el cuaderno lo dibuja.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or None))
