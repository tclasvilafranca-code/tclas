# -*- coding: utf-8 -*-
"""SEPTIEMBRE · El pentagrama y las notas (plantilla de referencia del cuaderno KIDS)."""
from k1_base import *
from k1_comun import *

MES = 'Septiembre'
SEC = 'ABCDEF'
FRASES = {'ya': 'Ya sabes hacerlo. ¡Sigue!'}


def construir(d):
    KB.MES_ACTUAL[0] = MES
    # ---------------------------------------------------------------- 1. lo que voy a aprender
    d.nuevo('Septiembre')
    d.add(K_titulo('Septiembre', 'El pentagrama y las notas', 'Este mes aprendo dónde se escribe la música y cómo se llaman las siete notas.'),
          K_mussol('Hola. Cada página tiene una sola tarea. Cuando la termines, marca HECHO.'),
          K_panel('', 'MI PLAN DEL MES', [K_plan(['Conozco el pentagrama y la clave de sol.', 'Aprendo las 7 notas y sus colores.',
                                                    'Aprendo cómo se llaman las figuras y cuánto duran.', 'Pongo bien los palitos de las notas.'])]))
    # ---------------------------------------------------------------- 2. el pentagrama
    d.nuevo()
    d.add(K_titulo('Septiembre', 'El pentagrama', 'La música se escribe en el pentagrama.'),
          K_mussol('El pentagrama tiene 5 líneas y 4 espacios. Se cuentan de abajo hacia arriba.'),
          K_panel('', 'MIRA', [K_diag_pentagrama()]),
          K_cajita('RECUERDA', 'Al principio del pentagrama hay un dibujo que se llama clave. La clave dice cómo se llaman las notas.'))
    # ---------------------------------------------------------------- 3. las notas
    d.nuevo()
    d.add(K_titulo('Septiembre', 'Las 7 notas', 'Cada nota tiene un nombre y un color. El color es siempre el mismo.'),
          K_mussol('Las notas son siete: DO, RE, MI, FA, SOL, LA y SI. Después de SI vuelve DO.'),
          K_panel('', 'MIRA', [K_notas_colores(), K_espacio(6),
                               K_notas('treble', ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4'], titulo='Así se escriben, de la más grave a la más aguda')]),
          K_cajita('RECUERDA', 'SOL está en la línea 2: justo donde la clave hace su espiral.'))

    # ---------------------------------------------------------------- actividad 1: clave de sol
    actividad(d, 1, 'La clave de sol', 'Vamos a dibujar la clave de sol. Empieza en la línea 2, da la vuelta y sube.',
              ['Repasa con lápiz las claves punteadas.', 'Dibuja tú tu clave de sol en el pentagrama de abajo.', 'Coloréala del color que quieras.'],
              [K_clave_fantasma('treble', titulo='Repasa'), K_espacio(8), K_pauta_vacia('treble', 1, titulo='Ahora tú')])

    # ---------------------------------------------------------------- actividad 2: dibujo las notas
    actividad(d, 2, 'Dibujo las notas', 'Cada nota va en su lugar y lleva su color.',
              ['Repasa con lápiz las notas punteadas.', 'Píntalas de su color.', 'Dibuja tú las notas en la segunda fila.'],
              [K_notas('treble', ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4'], fantasma=True, color=True, titulo='Repasa y pinta'), K_espacio(10),
               K_notas('treble', [None] * 7, nombres=NOMBRES, titulo='Dibuja')])

    # ---------------------------------------------------------------- pausa
    d.nuevo()
    d.add(K_titulo('Septiembre', 'Pausa', 'Cuando te cansas, tu cuerpo necesita moverse.'), K_mussol('Hacemos una pausa. Después volvemos.'), K_pausa(0))

    # ---------------------------------------------------------------- actividad 3: leo las notas
    r = rnd(13)
    pool = ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
    f1 = ['C4'] + [r.choice(pool) for _ in range(5)]
    f2 = ['C4'] + [r.choice(pool) for _ in range(5)]
    actividad(d, 3, 'Leo las notas', 'La primera nota de cada fila es DO. Cuenta desde ella.',
              ['Mira la primera nota: es DO.', 'Escribe el nombre de las otras notas en las casillas.', 'La segunda fila no tiene colores.'],
              [K_notas('treble', f1, rotulos='caja', titulo='Con colores'), K_espacio(6), K_notas('treble', f2, rotulos='caja', color=False, titulo='Sin colores')])
    sol(MES, 3, 'Leo las notas', ['Fila 1: ' + ' · '.join(nom_nota(p) for p in f1), 'Fila 2: ' + ' · '.join(nom_nota(p) for p in f2)])

    # ---------------------------------------------------------------- actividad 4: figuras
    actividad(d, 4, 'Las figuras', 'Cada figura dura un número de tiempos. Cuenta los círculos azules.',
              ['Mira la tabla: figura, nombre y cuántos tiempos dura.', 'Une cada figura con su nombre.', 'Di en voz alta: redonda, blanca, negra, corchea.'],
              [K_tabla_figuras()])
    d.nuevo()
    ord_ = ['q', 'w', 'e', 'h']
    nombres = ['REDONDA · 4', 'NEGRA · 1', 'CORCHEA · ½', 'BLANCA · 2']
    d.add(K_titulo_act(5, 'Une las figuras'), K_mussol('Une cada figura con su nombre y su número de tiempos.'),
          K_panel('', 'UNE CON UNA LÍNEA', [K_pasos(['Mira la figura.', 'Busca su nombre a la derecha.', 'Dibuja una línea para unirlos.']), K_espacio(6),
                                           K_une([(lambda c, cx, cy, w, h, d_=d_: K.figura(c, d_, cx - 8, cy - 12, 9.4)) for d_ in ord_], nombres, alto=56), K_hecho()]))
    sol(MES, 5, 'Une las figuras', ['Negra = NEGRA · 1; redonda = REDONDA · 4; corchea = CORCHEA · ½; blanca = BLANCA · 2.'])

    # ---------------------------------------------------------------- actividad 6: los palitos
    actividad(d, 6, 'Los palitos', 'El palito se llama plica. Va hacia arriba o hacia abajo.',
              ['Mira el ejemplo.', 'Las notas por debajo de SI: la plica va hacia arriba, a la derecha.', 'Las notas por encima de SI: la plica va hacia abajo, a la izquierda.',
               'Dibuja la plica de cada nota.'],
              [K_notas('treble', ['E4', 'G4', 'B4', 'D5', 'F5'], rotulos=None, color=False, plica=True, titulo='Ejemplo'), K_espacio(8),
               K_notas('treble', ['F4', 'C5', 'A4', 'E5', 'D4', 'G4'], rotulos=None, color=False, titulo='Ahora tú')])
    sol(MES, 6, 'Los palitos', ['Hacia arriba (derecha): F4 (fa), A4 (la), D4 (re), G4 (sol). Hacia abajo (izquierda): C5 (do), E5 (mi). SI se puede hacia los dos lados.'])

    # ---------------------------------------------------------------- reto opcional: sopa
    g, pos = sopa_letras(NOMBRES, 9, 5)
    d.nuevo()
    d.add(K_titulo_act('★', 'Reto: sopa de letras'), K_mussol('Este juego es opcional. Si hoy no quieres, lo dejamos para otro día.'),
          K_panel('', 'BUSCA LAS 7 NOTAS', [K_pasos(['Busca cada nota: hacia la derecha o hacia abajo.', 'Rodéala con su color.']), K_sopa(g, NOMBRES, 30), K_hecho()]))
    sol(MES, 'Reto', 'Sopa de letras', ['  ·  '.join('%s (fila %d, col. %d, %s)' % (p, y0 + 1, x0 + 1, '→' if dx else '↓') for p, (y0, x0, dy, dx) in pos.items())])

    # ---------------------------------------------------------------- al piano
    d.nuevo()
    d.add(K_titulo('Septiembre', 'Al piano: mis manos', 'Antes de tocar, conocemos los dedos.'),
          K_mussol('Los dedos tienen número. El 1 es el pulgar. El 5 es el meñique.'),
          K_panel('', 'MIS DEDOS', [Blk(250, lambda c, x, y, w: (nens_dib.ma_real(c, x + w * 0.26, y - 130, 0.8, esq=True, dits=True, color=False),
                                                                    nens_dib.ma_real(c, x + w * 0.74, y - 130, 0.8, esq=False, dits=True, color=False),
                                                                    txt(c, x + w * 0.26, y - 244, 'MANO IZQUIERDA', 11.5, ETQ, NAVY, 'c'),
                                                                    txt(c, x + w * 0.74, y - 244, 'MANO DERECHA', 11.5, ETQ, NAVY, 'c')))]),
          K_cajita('PRUEBA', 'Pon las dos manos sobre las piernas. Levanta el dedo 1 de cada mano. Después el 2. Después el 3, el 4 y el 5.'))

    # ---------------------------------------------------------------- tablero
    d.nuevo()
    d.add(K_titulo('Septiembre', 'Mis logros', 'Mira todo lo que has hecho este mes.'), K_mussol('Pinta una casilla por cada cosa que ya sabes. ¡Muy bien!'),
          K_panel('', 'TABLERO', [K_tablero('septiembre', ['Sé qué es el pentagrama.', 'Sé dibujar la clave de sol.', 'Sé el nombre y el color de las 7 notas.',
                                                         'Sé el nombre de las 4 figuras.', 'Sé poner la plica a las notas.'])]))
