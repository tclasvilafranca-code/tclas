# -*- coding: utf-8 -*-
"""Que figuras, silencios y recursos puede ver cada alumno.

   Decision del cliente tras revisar los diez albumes: la dificultad tiene que
   subir DE VERDAD segun el alumno, no solo en el texto. Hasta ahora los diez
   compartian exactamente el mismo techo de figura (la corchea) porque el motor
   no sabia dibujar la semicorchea; un nino de diez anos en su primer curso y
   una alumna avanzada de varios anos escribian, sobre el papel, la misma figura
   mas corta.

   Aqui viven los cinco escalones. Cada uno ANADE a los anteriores y nunca
   quita. Lo comprueba `auditar_niveles.py`, que entra en el auditor de cada
   alumno: si a Arnau le cuela una semicorchea, la auditoria falla.

   REGLA QUE MANDA SOBRE ESTA TABLA: todo sale de la partitura. Si la pieza real
   de un alumno lleva una figura que su escalon no contempla, la figura se
   escribe igual (es su partitura) y se anota la excepcion en EXCEPCIONES, con
   el motivo. Lo que este archivo impide es INVENTAR dificultad en el andamio
   por encima del nivel del alumno, que es cosa distinta.

   La digitacion NO se imprime en ningun escalon: decision del cliente, los
   numeros de dedo los escribe el alumno.
"""

# Duraciones ordenadas de larga a corta, para poder decir "hasta aqui".
ORDEN = ['w', 'h.', 'h', 'q.', 'q', 'e.', 'e', 's.', 's']


# Lo que de verdad separa un escalon de otro NO es prohibir la corchea —las
# partituras de iniciacion la traen desde el primer mes—, sino tres cosas:
#   1. hasta que figura se llega (el techo);
#   2. cuantas notas cortas seguidas se toleran (la RESISTENCIA, que es donde
#      se nota de verdad el nivel de un alumno);
#   3. que recursos de expresion se le piden.
#
# OJO con el punto 3: las marcas de expresion (matiz, ligadura, staccato,
# acento, calderon, reguladores) NO son dificultad de lectura, y las partituras
# de iniciacion las traen impresas desde el primer dia -- restringirlas por
# nivel era irreal. Lo que si escala de verdad es la FIGURA (la semicorchea),
# la DENSIDAD (max_corcheas_seguidas) y, en menor medida, el tresillo y el
# pedal. El Adagio de Albinoni lleva tresillos y es la pieza 13 de un adulto
# que empezo hace poco: por eso el tresillo entra ya en el escalon 2. Los
# reguladores entran en el 1 (The Beginner de Gurlitt los trae impresos) y el
# pedal en el 3 (Nel tiene doce anos pero lleva anos de clase).
# `max_corcheas_seguidas` cuenta corcheas Y semicorcheas consecutivas dentro de
# un mismo sistema: es la comprobacion que captura la norma de Luisa ("nunca
# corcheas seguidas") y la que impide que a un principiante le caiga un pasaje
# de resistencia disfrazado de ejercicio corto.
NIVELES = {
    1: dict(
        nombre='Lo básico, sin prisa',
        figuras={'w', 'h.', 'h', 'q.', 'q', 'e'},
        silencios={'w', 'h.', 'h', 'q.', 'q', 'e'},
        max_notas_acorde=3,
        max_corcheas_seguidas=8,
        recursos={'lig', 'matiz', 'art', 'cresc', 'dim'},
        desde={},
        nota='Hasta la corchea. Puede haber un compás seguido de corcheas en '
             'UNA mano (sus piezas lo traen), pero nunca más, y nunca en las '
             'dos manos a la vez. Ni semicorchea, ni tresillo, ni expresión.',
    ),
    2: dict(
        nombre='La corchea se asienta',
        figuras={'w', 'h.', 'h', 'q.', 'q', 'e.', 'e'},
        silencios={'w', 'h.', 'h', 'q.', 'q', 'e'},
        max_notas_acorde=3,
        max_corcheas_seguidas=12,
        recursos={'lig', 'matiz', 'art', 'cresc', 'dim', 'tresillo'},
        desde={},
        nota='Corcheas seguidas en una mano (hasta un compás entero), corchea '
             'con puntillo, ligaduras y matices. Todavía sin semicorchea.',
    ),
    3: dict(
        nombre='Empieza a correr',
        figuras={'w', 'h.', 'h', 'q.', 'q', 'e.', 'e', 's'},
        silencios={'w', 'h.', 'h', 'q.', 'q', 'e', 's'},
        max_notas_acorde=4,
        max_corcheas_seguidas=16,
        recursos={'lig', 'matiz', 'art', 'cresc', 'dim', 'tresillo', 'pedal'},
        desde={'s': 6},
        nota='Primeras semicorcheas, por parejas y en pasajes cortos, no antes '
             'de la pieza 6. Articulación y acordes de cuatro notas.',
    ),
    4: dict(
        nombre='El exigente',
        figuras={'w', 'h.', 'h', 'q.', 'q', 'e.', 'e', 's.', 's'},
        silencios={'w', 'h.', 'h', 'q.', 'q', 'e', 's'},
        max_notas_acorde=4,
        max_corcheas_seguidas=24,
        recursos={'lig', 'matiz', 'art', 'tresillo', 'cresc', 'dim', 'pedal'},
        desde={},
        nota='Grupos de cuatro semicorcheas, tresillos, staccato y matices '
             'impresos. Las dos manos en movimiento a la vez.',
    ),
    5: dict(
        nombre='Los avanzados',
        figuras={'w', 'h.', 'h', 'q.', 'q', 'e.', 'e', 's.', 's'},
        silencios={'w', 'h.', 'h', 'q.', 'q', 'e', 's'},
        max_notas_acorde=5,
        max_corcheas_seguidas=99,
        recursos={'lig', 'matiz', 'art', 'tresillo', 'cresc', 'dim', 'pedal'},
        desde={},
        nota='Todo: semicorcheas continuas, tresillos habituales, reguladores '
             'y pedal dibujados.',
    ),
}


# A que escalon va cada alumno. La clave es `CANCION['alumno']` en minusculas.
ESCALON = {
    'arnau': 1,          # 10 anos, media hora de clase, primer curso
    'luisa': 1,          # adulta, empezo hace nada: "poquito pero bien, sencillo"
    'josé maría': 2,
    'jose maria': 2,
    'eduard': 2,         # mismo nivel y repertorio que Jose Maria
    'mercè': 2,
    'merce': 2,
    'isaac': 3,          # nivel medio "con cana": sube mas rapido, techo mas bajo
    'nel': 3,            # doce anos, mismo repertorio que Josep
    'josep': 4,          # la edad de Jose Maria y mas anos de clase; le gustan los retos
    'dilan': 5,
    'eva': 5,
}


# Excepciones justificadas: (archivo, figura) -> motivo. Se usan cuando la
# partitura REAL del alumno trae una figura por encima de su escalon. La regla
# "todo sale de la partitura" manda sobre la tabla de niveles.
EXCEPCIONES = {
    ('arnau_10_muffet', 'q.'): 'la pieza real está en 6/8 y su unidad es la negra con puntillo',
    ('arnau_15_largo', 'q.'): 'el Largo de Dvorak lleva la figura con puntillo impresa',
    # Su edicion de The Wheels on the Bus lleva impresa una CORCHEA CON PUNTILLO
    # seguida de SEMICORCHEA en los cc. 1 y 5: es el balanceo del "round and
    # round" y es lo que hace reconocible la cancion. Comprobado a zoom sobre el
    # PDF (la barra secundaria corta se ve sin ninguna duda). El escalon 1 no
    # llega a la semicorchea, pero la regla que manda es que todo sale de la
    # partitura: si el nino la va a tocar, la tiene que ver escrita.
    ('arnau_05_wheels', 'e.'): 'su edicion lleva impreso el ritmo largo-corto en los cc. 1 y 5',
    ('arnau_05_wheels', 's'): 'la nota corta de ese mismo ritmo, impresa en su partitura',
    # Su Für Elise es la edición real: va en corcheas casi entera, pero en el
    # c. 20 lleva UNA semicorchea impresa, como nota corta de una figura
    # larga-corta. Es su partitura, así que se escribe. Comprobado a zoom sobre
    # el PDF: la última nota de ese grupo lleva una barra más que las otras.
    ('me_26_furelise', 's'): 'el c. 20 de su edición lleva una semicorchea impresa',
    # A comme amour va en semicorcheas de principio a fin (45 pares de barras
    # dobles medidos sobre el PDF) y esta en el bloque de los retos justo por
    # eso. Escribirlas en corcheas "porque el motor no llega" era la excusa
    # vieja; el motor llega, y la partitura es la suya.
    ('jm_17_acomme', 's'): 'su partitura va en semicorcheas continuas, medidas sobre el PDF',
    ('ed_17_acomme', 's'): 'la misma partitura de José María, con las mismas semicorcheas',
}

# Rachas de notas cortas por encima del tope del escalon que SI se aceptan,
# porque la partitura real las trae. modulo -> motivo.
RACHAS_JUSTIFICADAS = {
    'jm_17_acomme': 'la pieza va en semicorcheas continuas; aqui se escriben en '
                    'corcheas al doble de lento, que es como se estudian',
    'ed_17_acomme': 'idem que Jose Maria: misma partitura, mismas semicorcheas',
    'arnau_09_polly': 'la edicion va en 2/4 y su melodia es de notas cortas casi '
                      'todo el rato: medido sobre el PDF, no es andamio inventado',
    'arnau_10_muffet': 'la pieza esta en 6/8 y la corchea ES la unidad del compas: '
                       'seis por compas, agrupadas de tres en tres',
}


def escalon_de(alumno):
    return ESCALON.get(str(alumno).strip().lower())


def permitido(alumno, dur, es_silencio=False):
    """True si esa figura entra en el escalon del alumno."""
    n = escalon_de(alumno)
    if n is None:
        return True
    nivel = NIVELES[n]
    return dur in (nivel['silencios'] if es_silencio else nivel['figuras'])
