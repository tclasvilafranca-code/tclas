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


def semi(ps, agrupar=4, **extra):
    """Semicorcheas unidas de cuatro en cuatro (un golpe de negra).

       Solo para los escalones 3 y superiores (ver niveles.py): a un alumno de
       iniciacion no se le escribe una semicorchea, y el auditor de niveles lo
       comprueba. Se agrupa de cuatro porque es la agrupacion por tiempo en los
       compases de x/4, que es como se graba de verdad."""
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        ev = {'pitch': p, 'dur': 's', 'beam': _B[0]}
        ev.update(extra)
        out.append(ev)
    return out


# --------------------------------------------------------------------------
# Fabricas de bloques de deberes
#
# Los ejercicios se numeran solos en `hoja_deberes.build_deberes`, asi que
# aqui NO se pone `num`: el orden de los bloques puede cambiar cada semana (lo
# pide la norma de variedad) y con los numeros escritos a mano habia que
# renumerar la hoja entera cada vez.
# --------------------------------------------------------------------------
def rutina(*tareas):
    return dict(tipo='rutina', titulo='Lo que hay que tocar cada día',
                pista='pon una cruz cuando lo hagas · cinco minutos bastan',
                tareas=list(tareas))


def juego(texto, pista='no hace falta que sepa música'):
    return dict(tipo='escucha', titulo='UN JUEGO, CON ALGUIEN DE CASA',
                pista=pista, texto=texto)


def acuerdate(texto, etiqueta='ACUÉRDATE'):
    return dict(tipo='nota', etiqueta=etiqueta, texto=texto)


def escribir(titulo='Copia aquí el compás que más te cueste',
             pista='cópialo tal cual y luego tócalo cinco veces', lineas=1):
    return dict(tipo='escribe', titulo=titulo, pista=pista, lineas=lineas)


def nombres(notas, titulo='¿Cómo se llama cada nota?',
            pista='escríbelas en la cajita de debajo'):
    return dict(tipo='nombres', titulo=titulo, pista=pista, notas=list(notas))


def dibujar(nombres_notas, titulo='Ahora al revés: dibuja tú las notas',
            pista='solo el óvalo, sin el palito'):
    return dict(tipo='dibuja', titulo=titulo, pista=pista,
                nombres=list(nombres_notas))


def figuras(items, titulo='¿Cuántos golpes dura cada una?',
            pista='escribe el número en la caja'):
    return dict(tipo='figuras', titulo=titulo, pista=pista, figuras=list(items))


def unir(pares, titulo='Une cada cosa con la que le toca',
         pista='una raya de un punto al otro', derecha=None):
    return dict(tipo='une', titulo=titulo, pista=pista, pares=list(pares),
                derecha=derecha)


def rodear(compases, titulo='Rodea los dos compases que son iguales',
           pista='fíjate en las notas de una en una'):
    return dict(tipo='rodea', titulo=titulo, pista=pista, compases=compases)


def colorear(eventos, leyenda, titulo='Colorea las notas',
             pista='cada figura de un color'):
    return dict(tipo='colorea', titulo=titulo, pista=pista, eventos=eventos,
                leyenda=list(leyenda))


def sopa(palabras, semilla, titulo='Sopa de letras',
         pista='están tumbadas, de pie o en diagonal', filas=9, columnas=22):
    return dict(tipo='sopa', titulo=titulo, pista=pista, semilla=semilla,
                palabras=list(palabras), filas=filas, columnas=columnas)


def adivinar(items, titulo='Adivina quién soy',
             pista='una letra en cada casilla'):
    return dict(tipo='adivina', titulo=titulo, pista=pista, items=list(items))


def crucigrama(clave, palabras, cierre, titulo='Crucigrama',
               pista='las casillas grises, de arriba abajo, dicen una palabra'):
    return dict(tipo='crucigrama', titulo=titulo, pista=pista, clave=clave,
                palabras=list(palabras), cierre=cierre)


def camino(filas, titulo='El camino correcto', pista='colorea solo esas casillas'):
    return dict(tipo='camino', titulo=titulo, pista=pista, filas=filas)


def verdadero_falso(frases, titulo='Verdadero o falso',
                    pista='marca la casilla que toca'):
    return dict(tipo='vf', titulo=titulo, pista=pista, frases=list(frases))


def ordenar(pasos, titulo='Pon los pasos en orden',
            pista='escribe 1, 2, 3… en las casillas'):
    return dict(tipo='ordena', titulo=titulo, pista=pista, pasos=list(pasos))


def diferencias(a, b, cuantas, titulo='Busca las diferencias', pista=None):
    return dict(tipo='diferencias', titulo=titulo, cuantas=cuantas,
                pista=pista or ('hay %d cosas cambiadas en el de abajo · rodéalas' % cuantas),
                a=a, b=b)


def contar(eventos, preguntas, titulo='Cuenta y escribe',
           pista='mira el pentagrama y escribe el número en la caja'):
    return dict(tipo='cuenta', titulo=titulo, pista=pista, eventos=eventos,
                preguntas=list(preguntas))


def teclado(senales, preguntas, titulo='En el teclado', pista=None, teclas=15):
    return dict(tipo='teclado', titulo=titulo, pista=pista, teclas=teclas,
                senales=senales, preguntas=list(preguntas))


def palmas(palabras, titulo='El ritmo de las palabras',
           pista='dilo en voz alta, cuenta las sílabas y escríbelo con figuras'):
    return dict(tipo='palmas', titulo=titulo, pista=pista,
                palabras=list(palabras))


def inventa(condiciones, time_sig, clef='treble', lineas=1,
            titulo='Inventa tú', pista='tiene que cumplir todo esto'):
    return dict(tipo='inventa', titulo=titulo, pista=pista, clef=clef,
                lineas=lineas, time_sig=time_sig,
                condiciones=list(condiciones))
