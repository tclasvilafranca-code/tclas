# -*- coding: utf-8 -*-
"""Piezas sueltas que usan todas las canciones de Arnau.

   No hay material musical aqui: solo las tres funciones de siempre para
   escribir notas, acordes y silencios, y un contador de barras de corchea
   propio para que dos canciones distintas no compartan numero de barra.
"""
_B = [5000]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def ac(ps, d='q'):
    return {'pitches': list(ps), 'dur': d}


def sil(d='q'):
    return {'rest': True, 'dur': d}


def corch(ps, agrupar=2):
    """Corcheas unidas de dos en dos (o de tres en tres en 6/8)."""
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


def rutina(*tareas):
    return dict(tipo='rutina', titulo='Lo que hay que tocar cada día',
                pista='pon una cruz cuando lo hagas · cinco minutos bastan',
                tareas=list(tareas))


def juego(texto, pista='no hace falta que sepa música'):
    return dict(tipo='escucha', titulo='UN JUEGO, CON ALGUIEN DE CASA',
                pista=pista, texto=texto)


def escribir(num=3, titulo='Copia aquí el compás que más te cueste',
             pista='cópialo tal cual y luego tócalo cinco veces'):
    return dict(tipo='escribe', num=num, titulo=titulo, pista=pista, lineas=1)
