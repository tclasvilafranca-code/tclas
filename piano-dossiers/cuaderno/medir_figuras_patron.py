# -*- coding: utf-8 -*-
"""Banco de pruebas del detector de barras dobles.

   Las 16 partituras de abajo estan comprobadas MIRANDOLAS, una a una, a
   tamano grande. Sirven de patron: el detector tiene que separar las doce
   que llevan semicorchea impresa de las cuatro que no.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

S = '/home/user/tclas/piano-dossiers/students'

CON = [
    ('Fur Elise real', S + '/isaac/source/Para Elisa.pdf'),
    ('Un beso y una flor', S + '/josep/source/Un beso-y-una-flor-nino-bravo.pdf'),
    ('A comme amour', S + '/josep/source/A COMME AMOUR _ Richard Clayderman.'),
    ('Peaches', S + '/josep/source/-PEACHES.'),
    ('Your Song', S + '/dilan/source/DILAN/ YOUR SONG _ Elton John_.pdf'),
    ('Lucia', S + '/dilan/source/DILAN/ Lucia_.pdf'),
    ('La Promesa', S + '/dilan/source/DILAN/ la-promesa-MELENDI.pdf'),
    ('Sky Full of Stars', S + '/dilan/source/DILAN/ a-sky-full-of-stars-coldplay.pdf'),
    ('When I Was Your Man', S + '/dilan/source/DILAN/ WHEN I WAS YOUR MAN _ Bruno Mars_.pdf'),
    ('Arabesque', S + '/eva/source/EVA/arabesque-burgmuller-( 4 manos).pdf'),
    ('Soldadito de Hierro', S + '/dilan/source/DILAN/ SOLDADITO DE HIERRO _ Nil Moliner_.pdf'),
]

SIN = [
    ('Deck the Halls', S + '/jose_maria/source/Deck the Halls (with Boughs of Holly) NAVIDAD.pdf'),
    ('When the Saints', S + '/isaac/source/OH WHEN THE SAINT.pdf'),
    ('Fur Elise easy', S + '/luisa/source/Para  Elisa easy.pdf'),
    ('Nocturne easy', S + '/luisa/source/nocturne-op9-chopin. easy'),
]


def main(modulo):
    import importlib
    bd = importlib.import_module(modulo)
    print('%-24s %8s %8s' % ('partitura', 'largas', 'cortas'))
    for etiqueta, lista in (('CON semicorchea', CON), ('SIN semicorchea', SIN)):
        print('\n--- ' + etiqueta)
        for nombre, ruta in lista:
            if not os.path.exists(ruta):
                print('%-24s  FALTA %s' % (nombre, ruta))
                continue
            try:
                largas, cortas = bd.contar(ruta)
            except Exception as exc:                     # noqa: BLE001
                print('%-24s  ERROR %s' % (nombre, exc))
                continue
            print('%-24s %8d %8d' % (nombre, largas, cortas))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'medir_figuras')
