# -*- coding: utf-8 -*-
"""La tarea escrita de la semana, para Dilan y Eva.

   Norma de variedad del cliente: la variedad es parte de la calidad, y vale
   para todos los alumnos. En el formato largo (Dilan y Eva) el sitio donde el
   alumno se lleva algo a casa es el recuadro del pie de la hoja de relajación,
   y hasta ahora era **el mismo recuadro en blanco en los 37 dosieres**: tres
   rayas para que la profesora escribiera algo al final de la clase.

   Ahora cada pieza trae **una tarea escrita distinta**, y sigue quedando una
   raya libre para que la profesora añada lo suyo. Las tareas rotan de manera
   que dos piezas seguidas nunca llevan la misma, y cada una vuelve doce
   piezas después.

   Todas las tareas son de las que **no necesitan un dato que no esté medido**:
   apuntan al alumno a SU partitura ("el compás que peor te sale", "los
   compases que se repiten iguales") en vez de citar números de compás que no
   se han comprobado pieza por pieza. Eso es a propósito: la norma de que nada
   se escribe sin medirlo manda también aquí.
"""

TAREAS = [
    ('ANÁLISIS',
     'Coge un lápiz y rodea en tu partitura todos los compases que se repiten '
     'iguales. Apunta al lado cuántos son de verdad nuevos: casi siempre son '
     'muchos menos de los que parecen, y eso es lo que tienes que aprender.'),
    ('DIGITACIÓN',
     'Elige el pasaje que peor te sale y escribe con lápiz el número de dedo de '
     'cada nota. Lo importante no es acertar a la primera: es no cambiarlo '
     'durante toda la semana, para que la mano se lo aprenda.'),
    ('METRÓNOMO',
     'Apunta cada día a qué velocidad te sale entera y sin pararte. Sube solo '
     'cuando te haya salido limpia tres veces seguidas, y si al subir empiezas '
     'a fallar, baja otra vez. Al final de la semana mira los números.'),
    ('DE MEMORIA',
     'Apréndete de memoria las cuatro primeras líneas y tócalas con los ojos '
     'cerrados. Cuando te pierdas, no vuelvas al principio: sigue desde donde '
     'te acuerdes, que eso es lo que hay que saber hacer en un concierto.'),
    ('ESCUCHAR',
     'Busca dos versiones distintas de esta pieza y escucha las dos seguidas. '
     'Escribe una diferencia concreta entre ellas: dónde una respira y la otra '
     'no, o dónde una va más lenta. Con una diferencia bien vista basta.'),
    ('RITMO SOLO',
     'Coge el compás que peor te sale y palméalo veinte veces, solo el ritmo, '
     'sin notas y sin piano. Después tócalo. Casi siempre el problema no eran '
     'las notas.'),
    ('DINÁMICA',
     'Marca con lápiz en tu partitura dónde crece el sonido y dónde baja, y '
     'escribe al lado por qué lo has decidido ahí. Tiene que haber una razón: '
     'la frase sube, la armonía cambia, se repite algo.'),
    ('TRANSPORTAR',
     'Copia las dos primeras líneas en la hoja de pentagrama vacío, un tono más '
     'arriba. Escríbelo primero y tócalo después: si lo tocas de oído no te '
     'enteras de nada.'),
    ('PRIMERA VISTA',
     'Cinco minutos al día leyendo una pieza nueva, más fácil que esta, sin '
     'pararte a corregir. Apunta cada día qué ha sido lo que más te ha fallado: '
     'las notas, el ritmo, o mirar las dos manos a la vez.'),
    ('COPIAR',
     'Copia en la hoja de pentagrama vacío el compás que peor te sale, tal cual, '
     'con su armadura y su compás. Copiar a mano obliga a mirar cosas que '
     'leyendo se pasan por alto.'),
    ('CANTAR',
     'Canta la melodía en voz alta mientras tocas solo la mano izquierda. Si no '
     'puedes cantarla, es que todavía no la tienes: te la sabes de dedos pero no '
     'de oído.'),
    ('EL PEDAL',
     'Si esta pieza lleva pedal, marca con lápiz dónde lo cambias. Si no lo '
     'lleva, marca dónde levantas las manos: los sitios donde el sonido se '
     'corta son decisiones tuyas y conviene tomarlas escribiéndolas.'),
]

# Cada alumno arranca la rotación en un sitio distinto para que dos alumnos que
# comparten pieza no se lleven la misma tarea la misma semana.
ARRANQUE = {'Dilan': 0, 'Eva': 5}


def tarea(alumno, num):
    """La tarea que le toca a la pieza `num` (1..N) de ese alumno."""
    i = (ARRANQUE.get(alumno, 0) + num - 1) % len(TAREAS)
    etiqueta, texto = TAREAS[i]
    return dict(etiqueta=etiqueta, texto=texto)


def revisar_variedad_tareas(alumno, numeros, verbose=True):
    """Comprueba que dos piezas seguidas no llevan la misma tarea y que ninguna
       se repite a menos de seis piezas de distancia."""
    fallos = []
    etiquetas = [tarea(alumno, n)['etiqueta'] for n in numeros]
    for i in range(1, len(etiquetas)):
        if etiquetas[i] == etiquetas[i - 1]:
            fallos.append('%s: las piezas %d y %d llevan la misma tarea (%s)'
                          % (alumno, numeros[i - 1], numeros[i], etiquetas[i]))
    donde = {}
    for i, e in enumerate(etiquetas):
        donde.setdefault(e, []).append(i)
    for e, idx in donde.items():
        for a, b in zip(idx, idx[1:]):
            if b - a < 6:
                fallos.append('%s: la tarea %s vuelve solo %d piezas después'
                              % (alumno, e, b - a))
    if verbose:
        print('  tarea de la semana · %d piezas · %d tareas distintas · %s'
              % (len(numeros), len(set(etiquetas)),
                 'ok' if not fallos else '%d fallos' % len(fallos)))
        for f in fallos:
            print('      %s' % f)
    return fallos
