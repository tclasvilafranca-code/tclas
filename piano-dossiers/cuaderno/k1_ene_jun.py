# -*- coding: utf-8 -*-
"""ENERO a JUNIO del cuaderno KIDS: compases, ritmo, claves, silencios, ligadura y puntillo, repaso."""
from k1_base import *
from k1_comun import *
from n1_base import fila_compases, figura as fig_n1, silencio as sil_n1, NOM_SIL, FIG, BEATS

N = lambda dd, p=None: ('n', dd) if p is None else ('n', dd, p)
R = lambda dd: ('r', dd)


def comp(compases, ts, titulo=None, rot=None, final=True):
    return fila_compases(compases, ts=ts, gap=10.0, titulo=titulo, rotulos=rot)


def fin_mes(d, mes, items):
    d.nuevo()
    d.add(K_titulo(mes, 'Mis logros', 'Mira todo lo que has hecho este mes.'), K_mussol('Pinta una casilla por cada cosa que ya sabes.'),
          K_panel('', 'TABLERO', [K_tablero(mes.lower(), items)]))


def pausa(d, mes, k):
    d.nuevo(mes)
    d.add(K_titulo(mes, 'Pausa', 'Es momento de mover el cuerpo.'), K_mussol('Hacemos una pausa.'), K_pausa(k))


def plan(d, mes, titulo, frase, mus, items):
    KB.MES_ACTUAL[0] = mes
    d.nuevo(mes)
    d.add(K_titulo(mes, titulo, frase), K_mussol(mus), K_panel('', 'MI PLAN DEL MES', [K_plan(items)]))


# ============================================================== ENERO
def enero(d):
    M_ = 'Enero'
    plan(d, M_, 'Los compases', 'Este mes aprendo a llenar compases con figuras.', 'Un compás es como una caja. Tiene un número exacto de tiempos.',
         ['Sé qué es un compás.', 'Completo compases de 2, 3 y 4 tiempos.', 'Pongo las barras de compás.', 'Encuentro la figura que sobra.'])
    d.nuevo()
    d.add(K_titulo(M_, 'El compás', 'Las dos cifras del principio dicen cómo es la caja.'),
          K_mussol('El número de arriba dice cuántos tiempos caben. El de abajo es 4: la negra vale 1 tiempo. La línea que separa compases es la barra de compás.'),
          K_panel('', 'MIRA', [comp([[N('q'), N('q')], [N('h')]], (2, 4), '2/4 · caben 2 tiempos', ['1 2', '1 — 2']),
                               comp([[N('q'), N('q'), N('q')], [N('h'), N('q')]], (3, 4), '3/4 · caben 3 tiempos', ['1 2 3', '1 — 2 3']),
                               comp([[N('q')] * 4, [N('h'), N('h')]], (4, 4), '4/4 · caben 4 tiempos', ['1 2 3 4', '1 — 2 3 — 4'])]))
    actividad(d, 1, 'Completo el compás', 'Falta una figura en cada compás. Haz que sume.',
              ['Suma los tiempos que ya hay.', 'Mira cuántos faltan.', 'Dibuja una figura que los complete.'],
              [comp([[N('q'), ('x', 1)], [N('e'), N('e'), ('x', 1)]], (2, 4), 'A) 2/4'), comp([[N('q'), N('q'), ('x', 2)], [N('h.'), ('x', 1)]], (4, 4), 'B) 4/4')])
    sol(M_, 1, 'Completo el compás', ['A) falta 1 tiempo (negra) y 1 tiempo (dos corcheas) · B) faltan 2 (blanca o dos negras) y 1 (negra)'])
    pausa(d, M_, 4)
    actividad(d, 2, 'Compases secretos', 'Estos compases no tienen cifra. Descubre cuál es.',
              ['Suma los tiempos de cada compás.', 'Si suma 2, es 2/4. Si suma 3, es 3/4. Si suma 4, es 4/4.', 'Escribe la cifra en la casilla.'],
              [comp([[N('h'), N('q')], [N('q'), N('q')], [N('e'), N('e'), N('q'), N('q')]], None, 'A)', ['____', '____', '____']),
               comp([[N('h'), N('h')], [N('h.')], [N('q'), N('q'), R('q'), N('q')]], None, 'B)', ['____', '____', '____'])])
    sol(M_, 2, 'Compases secretos', ['A) 3/4 · 2/4 · 3/4 · B) 4/4 · 3/4 · 4/4'])
    actividad(d, 3, 'Pongo las barras', 'La música llega sin barras de compás. Ponlas tú.',
              ['Mira la cifra del principio.', 'Cuenta los tiempos.', 'Dibuja una barra cada vez que llegues al total.'],
              [comp([[N('q'), N('q'), N('q'), N('q'), N('h'), N('q'), N('q')]], (4, 4), 'A) 4/4: pon 1 barra'), comp([[N('q'), N('q'), N('q'), N('h'), N('q')]], (3, 4), 'B) 3/4: pon 1 barra')])
    sol(M_, 3, 'Pongo las barras', ['A) después de la 4.ª negra (4 tiempos) · B) después de la 3.ª negra (3 tiempos)'])
    actividad(d, 4, 'La figura intrusa', 'En cada compás sobra una figura.',
              ['Suma los tiempos.', 'Tacha la figura que hace que sobre.', 'Comprueba que ahora suma lo que dice la cifra.'],
              [comp([[N('h'), N('q'), N('q')], [N('q'), N('h')]], (2, 4), 'A) 2/4'), comp([[N('h'), N('q'), N('e'), N('e')], [N('h.'), N('q')]], (3, 4), 'B) 3/4')])
    sol(M_, 4, 'La figura intrusa', ['A) sobra una negra en cada compás · B) sobra una negra en cada compás'])
    fin_mes(d, M_, ['Sé qué es un compás.', 'Sé completar un compás.', 'Sé poner las barras de compás.', 'Sé encontrar la figura que sobra.'])


# ============================================================== FEBRERO
def febrero(d):
    M_ = 'Febrero'
    plan(d, M_, 'El ritmo y las palabras', 'Este mes juego con el ritmo.', 'El ritmo es cuánto dura cada sonido. Podemos sentirlo con las palabras y con las palmas.',
         ['Pongo ritmo a las palabras.', 'Ordeno las figuras de la que dura menos a la que dura más.', 'Leo ritmos con palmas.', 'Sé unir dos corcheas con una barra.'])
    d.nuevo()
    d.add(K_titulo(M_, 'Las sílabas son sonidos', 'Cada sílaba de una palabra es un sonido.'),
          K_mussol('Dos sílabas son dos sonidos. Ma-ri-po-sa tiene cuatro sílabas: cuatro sonidos.'),
          K_panel('', 'MIRA', [comp([[N('q')], [N('e'), N('e'), N('q')], [N('e'), N('e'), N('e'), N('e')]], (4, 4), None, ['sol', 'pla-ta-no', 'ma-ri-po-sa'], ), K_espacio(4)]),
          K_cajita('RECUERDA', 'Dos corcheas se unen con una barra. Una sola sílaba larga es una negra.'))
    actividad(d, 1, 'Ritmo de mi nombre', 'Tu nombre tiene un ritmo.',
              ['Di tu nombre en voz alta y aplaude cada sílaba.', 'Cuenta cuántas sílabas tiene.', 'Escribe el ritmo con negras y corcheas.'],
              [K_pauta_vacia('treble', 2, ts=(4, 4), titulo='Mi nombre es: ______________')])
    sol(M_, 1, 'Ritmo de mi nombre', ['Libre. Cada sílaba lleva un sonido: una negra (sílaba larga) o dos corcheas (sílabas rápidas).'])
    actividad(d, 2, 'Ritmos de cada día', 'Hay ritmos en la vida normal: un reloj, unos pasos, la lluvia.',
              ['Piensa en tres cosas que suenen de forma repetida.', 'Escribe su nombre en la línea.', 'Escribe su ritmo con negras y corcheas.'],
              [K_lineas(1, '1) ______________', 26), K_pauta_vacia('treble', 1, ts=(4, 4)), K_lineas(1, '2) ______________', 26), K_pauta_vacia('treble', 1, ts=(4, 4))])
    sol(M_, 2, 'Ritmos de cada día', ['Libre. Ejemplo: un reloj = cuatro negras; una pelota que bota deprisa = corcheas.'])
    pausa(d, M_, 1)
    d.nuevo()
    d.add(K_titulo_act(3, 'Ordeno las figuras'), K_mussol('La que dura menos va abajo. La que dura más, arriba.'),
          K_panel('', 'ESCALERA', [K_pasos(['Mira las figuras de abajo.', 'Escribe 1 en la que dura menos y 4 en la que dura más.']),
                                  Blk(130, lambda c, x, y, w: [(K.figura(c, d_, x + 60 + k * 100, y - 70, 9.0), K.caseta(c, x + 36 + k * 100, y - 118, 46, 34)) for k, d_ in enumerate(['h', 'e', 'w', 'q'])]), K_hecho()]))
    sol(M_, 3, 'Ordeno las figuras', ['Corchea 1 · negra 2 · blanca 3 · redonda 4 (de menos a más tiempo).'])
    actividad(d, 4, 'Ritmo y palmas', 'Lee el ritmo y aplaude sus tiempos.',
              ['Di el nombre de cada figura.', 'Aplaude: la negra, un golpe; dos corcheas, dos golpes rápidos.', 'Mantén el mismo pulso todo el tiempo.'],
              [comp([[N('q'), N('q'), N('e'), N('e'), N('q')], [N('h'), N('q'), N('q')]], (4, 4), 'A) 4/4'), comp([[N('q'), N('e'), N('e')], [N('q'), N('q')]], (2, 4), 'B) 2/4')])
    sol(M_, 4, 'Ritmo y palmas', ['Todos los compases suman 4 tiempos (A) o 2 tiempos (B).'])
    fin_mes(d, M_, ['Sé poner ritmo a una palabra.', 'Sé ordenar las figuras por duración.', 'Sé leer un ritmo con palmas.', 'Sé unir dos corcheas.'])


# ============================================================== MARZO
def marzo(d):
    M_ = 'Marzo'
    plan(d, M_, 'Las claves', 'Este mes conozco las claves de sol, de fa y de do.', 'La clave dice cómo se llaman las notas. Hay tres: sol, fa y do.',
         ['Dibujo la clave de sol y la clave de fa.', 'Conozco la clave de do.', 'Sé qué mano lee cada clave.', 'Leo notas en clave de fa.'])
    d.nuevo()
    d.add(K_titulo(M_, 'Tres claves', 'Cada clave rodea una línea y le da nombre.'),
          K_mussol('Clave de sol: la línea 2 es SOL. Clave de fa: la línea 4 es FA. Clave de do: la línea del centro es DO.'),
          K_panel('', 'MIRA', [Blk(150, lambda c, x, y, w: [(K.pauta(c, x + k * (w / 3.0) + 4, y - 40, w / 3.0 - 16, 10, clef), None) for k, clef in enumerate(['treble', 'bass'])]
                                  + [txt(c, x + w / 6.0, y - 108, 'CLAVE DE SOL', 11, ETQ, NAVY, 'c'), txt(c, x + w / 2.0, y - 108, 'CLAVE DE FA', 11, ETQ, NAVY, 'c'),
                                     txt(c, x + w * 5 / 6.0, y - 108, 'CLAVE DE DO', 11, ETQ, NAVY, 'c'),
                                     (K.pauta(c, x + 2 * (w / 3.0) + 4, y - 40, w / 3.0 - 16, 10, 'alto'), None),
                                     txt(c, x + w / 6.0, y - 128, 'mano derecha', 10.5, SANS, MUTED, 'c'), txt(c, x + w / 2.0, y - 128, 'mano izquierda', 10.5, SANS, MUTED, 'c'),
                                     txt(c, x + w * 5 / 6.0, y - 128, 'viola', 10.5, SANS, MUTED, 'c')])]),
          K_cajita('RECUERDA', 'En el piano usamos la clave de sol (mano derecha) y la clave de fa (mano izquierda).'))
    actividad(d, 1, 'Dibujo la clave de sol', 'Dibujar con calma ayuda a recordarla.',
              ['Repasa las claves punteadas.', 'Dibuja tú una clave de sol.'],
              [K_clave_fantasma('treble', titulo='Repasa'), K_pauta_vacia('treble', 1, titulo='Ahora tú')])
    actividad(d, 2, 'Dibujo la clave de fa', 'La clave de fa tiene dos puntos. Rodean la línea 4.',
              ['Repasa las claves punteadas.', 'Dibuja tú una clave de fa.'],
              [K_clave_fantasma('bass', titulo='Repasa'), K_pauta_vacia('bass', 1, titulo='Ahora tú')])
    pausa(d, M_, 5)
    actividad(d, 3, '¿Qué clave es?', 'Cada clave tiene su nombre.',
              ['Mira las claves de la izquierda.', 'Une cada clave con su nombre.', 'Rodea la clave que se usa con la mano derecha.'],
              [K_une([(lambda c, cx, cy, w, h, cl=cl: (K.pauta(c, cx - 50, cy + 10, 100, 4.6, cl))) for cl in ['bass', 'treble']], ['CLAVE DE SOL', 'CLAVE DE FA'], alto=66, ancho_izq=110)])
    sol(M_, 3, '¿Qué clave es?', ['La primera es la clave de fa; la segunda es la clave de sol. Con la mano derecha: clave de sol.'])
    actividad(d, 4, 'Leo en clave de fa', 'La primera nota es FA. Cuenta desde ella.',
              ['FA está en la línea 4.', 'Escribe el nombre de las otras notas.'],
              [K_notas('bass', ['F3', 'G3', 'A3', 'E3', 'D3', 'C3', 'B2'], rotulos='caja', color=False, gap=12), K_notas('bass', ['F3', 'E3', 'D3', 'C3', 'D3', 'E3', 'F3'], rotulos='caja', color=False, gap=12)])
    sol(M_, 4, 'Leo en clave de fa', ['A) FA SOL LA MI RE DO SI · B) FA MI RE DO RE MI FA'])
    actividad(d, 5, 'Escribo el mismo sonido', 'Una nota suena igual escrita en sol o en fa si es la misma tecla.',
              ['Mira las notas en clave de sol.', 'Escríbelas en clave de fa, una octava más grave: baja siete posiciones.', 'Comprueba en el piano que suena parecido pero más grave.'],
              [K_notas('treble', ['E4', 'F4', 'G4', 'E4'], rotulos='nombre', color=False, gap=12), K_notas('bass', [None] * 4, nombres=['MI', 'FA', 'SOL', 'MI'], color=False, gap=12)])
    sol(M_, 5, 'Escribo el mismo sonido', ['Una octava más grave: MI (3.er espacio), FA (4.ª línea), SOL (4.º espacio), MI (3.er espacio) en clave de fa.'])
    fin_mes(d, M_, ['Sé dibujar la clave de sol.', 'Sé dibujar la clave de fa.', 'Sé qué mano lee cada clave.', 'Sé leer notas en clave de fa.'])


# ============================================================== ABRIL
def abril(d):
    M_ = 'Abril'
    plan(d, M_, 'Los silencios', 'Este mes aprendo las pausas de la música.', 'Un silencio es un tiempo en que no se toca. Dura lo mismo que su figura.',
         ['Conozco los 4 silencios.', 'Los coloco en un compás.', 'Cuento los silencios con el pulso.', 'Invento un ritmo con silencios.'])
    d.nuevo()
    d.add(K_titulo(M_, 'Los 4 silencios', 'Cada figura tiene su silencio.'),
          K_mussol('El silencio de redonda cuelga de la línea 4. El de blanca se apoya en la línea 3.'),
          K_panel('', 'MIRA', [Blk(110, lambda c, x, y, w: [(K.pauta(c, x, y - 26, w, 11, 'treble'), None)] + [
              (nt.draw_rest(c, x + 70 + k * ((w - 90) / 4.0), y - 26 - 44, y - 26, 11, d_), txt(c, x + 70 + k * ((w - 90) / 4.0), y - 100, ['REDONDA · 4', 'BLANCA · 2', 'NEGRA · 1', 'CORCHEA · ½'][k], 10.5, SANSB, NAVY, 'c')) for k, d_ in enumerate(['w', 'h', 'q', 'e'])][0:0] + [
              (nt.draw_rest(c, x + 70 + k * ((w - 90) / 4.0), y - 26 - 44, y - 26, 11, d_), txt(c, x + 70 + k * ((w - 90) / 4.0), y - 100, ['REDONDA · 4', 'BLANCA · 2', 'NEGRA · 1', 'CORCHEA · ½'][k], 10.5, SANSB, NAVY, 'c')) for k, d_ in enumerate(['w', 'h', 'q', 'e'])])]),
          K_cajita('RECUERDA', 'El silencio vale lo mismo que su figura: la negra dura 1 tiempo y su silencio también.'))
    actividad(d, 1, 'Une cada silencio', 'Une cada silencio con su nombre.',
              ['Mira el silencio.', 'Busca su nombre.', 'Une con una línea.'],
              [K_une([(lambda c, cx, cy, w, h, d_=d_: nt.draw_rest(c, cx, cy - 12, cy + 12, 5.5, d_)) for d_ in ['q', 'w', 'e', 'h']], ['REDONDA · 4 tiempos', 'NEGRA · 1 tiempo', 'BLANCA · 2 tiempos', 'CORCHEA · ½ tiempo'], alto=62, ancho_izq=100, ancho_der=240)])
    sol(M_, 1, 'Une cada silencio', ['Negra=1 tiempo; redonda=4 tiempos; corchea=½ tiempo; blanca=2 tiempos.'])
    actividad(d, 2, 'Silencios que faltan', 'Faltan silencios en cada compás.',
              ['Suma lo que ya hay.', 'Mira cuántos tiempos faltan.', 'Dibuja el silencio que corresponde.'],
              [comp([[N('q'), ('x', 1), N('h')], [N('h'), ('x', 2)]], (4, 4), 'A) 4/4'), comp([[N('q'), ('x', 1), N('q')], [N('h'), ('x', 1)]], (3, 4), 'B) 3/4')])
    sol(M_, 2, 'Silencios que faltan', ['A) silencio de negra (1) y silencio de blanca (2) · B) silencio de negra (1) y silencio de negra (1)'])
    pausa(d, M_, 2)
    actividad(d, 3, '¿Suena o calla?', 'Las notas suenan. Los silencios callan.',
              ['Rodea de verde las notas.', 'Rodea de gris los silencios.', 'Escribe cuántos hay de cada.'],
              [comp([[N('q'), R('q'), N('h')], [R('h'), N('q'), N('q')]], (4, 4), 'A)', ['suenan __ callan __', 'suenan __ callan __']), comp([[N('h'), R('q')], [R('q'), N('q'), N('q')]], (3, 4), 'B)', ['suenan __ callan __', 'suenan __ callan __'])])
    sol(M_, 3, '¿Suena o calla?', ['A) c.1: suenan 2, callan 1 · c.2: suenan 2, callan 1 · B) c.1: suenan 1, callan 1 · c.2: suenan 2, callan 1'])
    actividad(d, 4, 'Mi ritmo con silencios', 'Ahora creas tú.',
              ['Escribe un compás de 4/4 con notas y silencios.', 'Suma 4 tiempos.', 'Aplaúdelo. En los silencios abre las manos.'],
              [K_pauta_vacia('treble', 2, ts=(4, 4), titulo='Mi compás')])
    sol(M_, 4, 'Mi ritmo con silencios', ['Libre. Cada compás tiene que sumar 4 tiempos.'])
    fin_mes(d, M_, ['Sé los 4 silencios.', 'Sé completar un compás con silencios.', 'Sé contar los silencios.', 'Sé inventar un ritmo con silencios.'])


# ============================================================== MAYO
def mayo(d):
    M_ = 'Mayo'
    plan(d, M_, 'La ligadura y el puntillo', 'Este mes aprendo dos formas de alargar las notas.', 'La ligadura une dos notas iguales. El puntillo suma la mitad.',
         ['Sé qué es la ligadura.', 'Sé qué es el puntillo.', 'Calculo cuánto dura una nota con puntillo.', 'Aplaudo un ritmo con puntillo.'])
    d.nuevo()
    d.add(K_titulo(M_, 'Ligadura y puntillo', 'Dos formas de hacer una nota más larga.'),
          K_mussol('Ligadura: una línea curva une dos notas iguales y suenan como una sola. Puntillo: un punto suma la mitad.'),
          K_panel('', 'MIRA', [sistema('Ligadura: 2 + 1 = 3 tiempos', [{'pitch': 'G4', 'dur': 'h', 'lig': True}, {'pitch': 'G4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'h'}, {'pitch': 'C4', 'dur': 'h'}], alto=100, gap=10),
                               tabla_pun()]))
    actividad(d, 1, '¿Ligadura o no?', 'La ligadura une dos notas del mismo nombre.',
              ['Mira las parejas de notas.', 'Si las dos notas son iguales, dibuja la ligadura.', 'Si son distintas, no se liga.'],
              [sistema('A)', [{'pitch': 'E4', 'dur': 'q'}, {'pitch': 'E4', 'dur': 'q'}, {'pitch': 'D4', 'dur': 'q'}, {'pitch': 'F4', 'dur': 'q'}], alto=96, gap=10),
               sistema('B)', [{'pitch': 'G4', 'dur': 'h'}, {'pitch': 'G4', 'dur': 'h'}, {'pitch': 'A4', 'dur': 'q'}, {'pitch': 'B4', 'dur': 'q'}], alto=96, gap=10)])
    sol(M_, 1, '¿Ligadura o no?', ['A) se liga Mi–Mi; Re–Fa no · B) se liga Sol–Sol; La–Si no'])
    pausa(d, M_, 0)
    actividad(d, 2, 'Puntillos', 'Calcula cuánto dura cada figura con puntillo.',
              ['Mira la figura.', 'Suma la mitad.', 'Escribe el resultado.'],
              [K_vf(['Blanca con puntillo = ___ tiempos', 'Negra con puntillo = ___ tiempos', 'Redonda con puntillo = ___ tiempos', 'Corchea con puntillo = ___ tiempo'], 14)])
    sol(M_, 2, 'Puntillos', ['3 · 1 ½ · 6 · ¾'])
    actividad(d, 3, 'Ligo y sumo', 'Dos notas ligadas suman sus tiempos.',
              ['Mira las dos figuras ligadas.', 'Suma sus tiempos.', 'Escribe el total.'],
              [K_vf(['Blanca + negra = ___', 'Negra + negra = ___', 'Redonda + blanca = ___', 'Blanca + blanca = ___'], 14)])
    sol(M_, 3, 'Ligo y sumo', ['3 · 2 · 6 · 4'])
    actividad(d, 4, 'El ritmo del puntillo', 'Negra con puntillo y corchea suenan «larga-corta».',
              ['Di «ta-i ti»: ta dura más, i dura menos.', 'Aplaude el ritmo.', 'Colorea los puntillos.'],
              [comp([[N('q.'), N('e'), N('q.'), N('e')], [N('q.'), N('e'), N('h')]], (4, 4), 'A)'), comp([[N('h.'), N('q')], [N('q.'), N('e'), N('q'), N('q')]], (4, 4), 'B)')])
    sol(M_, 4, 'El ritmo del puntillo', ['Cada compás suma 4 tiempos: negra con puntillo + corchea = 2 tiempos.'])
    fin_mes(d, M_, ['Sé qué es una ligadura.', 'Sé qué es un puntillo.', 'Sé sumar tiempos con puntillo.', 'Sé aplaudir un ritmo con puntillo.'])


def tabla_pun():
    RH = 40

    def f(c, x, y, w):
        for k, (d_, tx) in enumerate((('h', 'BLANCA con puntillo = 2 + 1 = 3 tiempos'), ('q', 'NEGRA con puntillo = 1 + ½ = 1 ½ tiempos'))):
            rr(c, x, y - (k + 1) * RH + 4, w, RH - 6, 12, fill=white, lw=1.4, col=NAVY)
            K.figura(c, d_, x + 34, y - k * RH - 26, 6.6)
            c.setFillColor(NAVY)
            c.circle(x + 52, y - k * RH - 24, 2.6, stroke=0, fill=1)
            txt(c, x + 72, y - k * RH - 25, tx, 12.5, SANSB, INK)
    return Blk(2 * RH + 6, f)


def sistema(titulo, ev, alto=110, gap=10, ts=(4, 4)):
    from n1_base import sistema as S
    return S(titulo, ev, ts=ts, alto=alto, gap=gap)


# ============================================================== JUNIO
def junio(d):
    M_ = 'Junio'
    plan(d, M_, 'Repaso y concierto', 'Este mes repaso todo y toco para otras personas.', 'Hemos llegado al final del curso. Repasamos y celebramos.',
         ['Elijo una canción que me guste.', 'Repaso lo aprendido.', 'Toco mi canción a alguien.', 'Celebro lo que he aprendido.'])
    actividad(d, 1, 'Mi canción', 'Elige la canción que más te ha gustado.',
              ['Escribe el nombre de la canción.', 'Practica un trozo de dos compases.', 'Tócala con calma.', 'Escribe qué te gusta de ella.'],
              [K_lineas(1, 'Mi canción es:', 28), K_lineas(2, 'Lo que más me gusta de ella:', 30)])
    sol(M_, 1, 'Mi canción', ['Libre.'])
    pausa(d, M_, 3)
    TEST = [
        ('Septiembre', '¿Cuánto dura la negra?', ['1 tiempo', '2 tiempos', '4 tiempos'], 'A'),
        ('Octubre', 'Si una nota sube en el pentagrama, suena…', ['más grave', 'más aguda', 'igual'], 'B'),
        ('Noviembre', 'En el piano, los sonidos graves están…', ['a la derecha', 'a la izquierda', 'en el centro'], 'B'),
        ('Diciembre', '¿Cuántas notas tiene la escala de DO (de un DO al siguiente)?', ['5', '7', '8'], 'C'),
        ('Enero', 'En un compás de 3/4 caben…', ['3 tiempos', '4 tiempos', '2 tiempos'], 'A'),
        ('Febrero', 'Dos corcheas duran lo mismo que…', ['una negra', 'una blanca', 'una redonda'], 'A'),
        ('Marzo', 'La clave de fa rodea la línea…', ['2', '4', '5'], 'B'),
        ('Abril', 'Un silencio de negra dura…', ['1 tiempo', '2 tiempos', '4 tiempos'], 'A'),
        ('Mayo', 'Una blanca con puntillo dura…', ['2 tiempos', '3 tiempos', '4 tiempos'], 'B'),
    ]
    d.nuevo(M_)
    d.add(K_titulo_act(2, 'Test de repaso'), K_mussol('Contesta sin prisa. Si no sabes una, sigue con la siguiente.'))
    resp = []
    for k, (mes, preg, ops, r_) in enumerate(TEST):
        d.add(K_panel('', mes.upper(), [K_opciones(preg, ops, 12.5)]))
        resp.append('%d) %s' % (k + 1, r_))
    sol(M_, 2, 'Test de repaso', ['  ·  '.join(resp)])
    d.nuevo()
    d.add(K_titulo_act(3, 'Mi dibujo musical'), K_mussol('Dibuja lo que quieras sobre música. Puede ser un instrumento, notas de colores o un concierto.'),
          K_panel('', 'DIBUJA', [K_pasos(['Usa los colores que quieras.', 'Puedes pegar un dibujo si prefieres.']), K_caja_dibujo('Mi dibujo musical', 300), K_hecho()]))
    sol(M_, 3, 'Mi dibujo musical', ['Libre.'])
    d.nuevo()
    d.add(K_titulo(M_, 'El concierto', 'Hoy toco para otras personas.'),
          K_mussol('Antes de tocar: respira tres veces. Después toca despacio. Si te equivocas, sigue.'),
          K_panel('', 'MI PROGRAMA', [K_pasos(['Digo el nombre de mi canción.', 'Toco.', 'Hago una reverencia.']), K_lineas(2, 'Mi canción:', 30)]),
          K_cajita('RECUERDA', 'Equivocarse es normal. Lo importante es seguir tocando.'))
    d.nuevo()
    d.add(K_titulo(M_, 'Mi diploma', 'Has terminado el nivel 1.'), diploma_k())
    fin_mes(d, M_, ['Elegí una canción y la practiqué.', 'Contesté el test de repaso.', 'Hice mi dibujo musical.', 'Toqué para otras personas.'])


def diploma_k():
    h = 320

    def f(c, x, y, w):
        trac(c, 2.2, NAVY)
        c.setFillColor(white)
        c.roundRect(x, y - h, w, h, 10, stroke=1, fill=1)
        trac(c, 1.0, OCRE)
        c.roundRect(x + 8, y - h + 8, w - 16, h - 16, 7, stroke=1, fill=0)
        mussol(c, x + w / 2, y - 150, 0.36, color=False, lw=2.6)
        txt(c, x + w / 2, y - 40, 'DIPLOMA', 28, SERIFB, NAVY, 'c')
        txt(c, x + w / 2, y - 62, 'Aprendiz Pianístico · Nivel 1', 13, SANSB, OCRE, 'c')
        txt(c, x + w / 2, y - 230, 'Este diploma es para', 12, SANS, INK, 'c')
        trac(c, 1.0, NAVY_SOFT)
        c.line(x + 80, y - 262, x + w - 80, y - 262)
        txt(c, x + w / 2, y - 290, 'Por todo lo que has aprendido. ¡Muy bien!', 12, SANS, INK, 'c')
    return Blk(h + 8, f)
