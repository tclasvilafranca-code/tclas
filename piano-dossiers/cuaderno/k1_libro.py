# -*- coding: utf-8 -*-
"""Monta «Mi cuaderno de piano · Nivel 1 KIDS» (diseño T-Clas para niños, adaptado a un alumno con TEA + TDAH).

   python3 k1_libro.py          -> entrega/CUADERNO_NIVEL1_KIDS.pdf
   BN=1 python3 k1_libro.py     -> version blanco y negro"""
import io
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if os.environ.get('BN') == '1':
    import bn
    bn.instalar()
from k1_base import *
from k1_comun import *
import k1_base as KB
import k1_sep, k1_oct, k1_nov, k1_dic, k1_ene_jun as ej
import n1_base
from dibujo_mano import ManoCanvas

MESES = [('Septiembre', k1_sep.construir, 'El pentagrama y las notas'), ('Octubre', k1_oct.construir, 'Líneas, espacios y dirección'),
         ('Noviembre', k1_nov.construir, 'El teclado y sus notas'), ('Diciembre', k1_dic.construir, 'Escala de Do mayor'),
         ('Enero', ej.enero, 'Los compases'), ('Febrero', ej.febrero, 'El ritmo y las palabras'), ('Marzo', ej.marzo, 'Las claves'),
         ('Abril', ej.abril, 'Los silencios'), ('Mayo', ej.mayo, 'La ligadura y el puntillo'), ('Junio', ej.junio, 'Repaso y concierto')]
ASSETS = os.path.join(HERE, '..', 'assets')


def portada(c):
    c.setFillColor(CREMA)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(NAVY)
    c.rect(0, H - 9, W, 9, stroke=0, fill=1)
    try:
        c.drawImage(os.path.join(ASSETS, 'asset_logo_tclas.png'), W / 2 - 45, H - 140, 90, 90, mask='auto', preserveAspectRatio=True)
    except Exception:
        pass
    mussol(c, W / 2, H - 330, 0.62, color=os.environ.get('BN') != '1', lw=3.2)
    txt(c, W / 2, H - 520, 'Mi cuaderno', 40, SERIFB, NAVY, 'c')
    txt(c, W / 2, H - 566, 'de piano', 40, SERIFB, NAVY, 'c')
    trac(c, 3, OCRE)
    c.line(W / 2 - 40, H - 584, W / 2 + 40, H - 584)
    rr(c, W / 2 - 110, H - 640, 220, 38, 19, fill=NAVY, lw=0)
    txt(c, W / 2, H - 627, 'NIVEL 1 · KIDS', 16, ETQ, white, 'c')
    txt(c, W / 2, H - 676, 'Aprendiz Pianístico · Curso 2026/27', 12.5, SANS, NAVY_SOFT, 'c')
    txt(c, M + 10, 92, 'Este cuaderno es de:', 12, SANSB, NAVY)
    trac(c, 1.2, NAVY_SOFT)
    c.line(M + 150, 90, W - M - 10, 90)
    c.showPage()


def como_funciona(d):
    d.nuevo('Cómo funciona')
    d.add(K_titulo('Empezamos', 'Cómo funciona mi cuaderno', 'Todas las páginas se parecen. Así sé siempre qué viene.'),
          K_mussol('Cada página tiene una sola tarea. Primero miro, después hago, y al final marco HECHO.'),
          K_panel('', 'LO QUE VOY A ENCONTRAR', [Blk(320, lambda c, x, y, w: [
              (c.setFillColor(OCRE), c.circle(x + 20, y - 24 - k * 62, 17, stroke=0, fill=1), txt(c, x + 20, y - 30 - k * 62, str(k + 1), 17, SANSB, white, 'c'),
               txt(c, x + 52, y - 21 - k * 62, t, 13.5, SANSB, NAVY), txt(c, x + 52, y - 40 - k * 62, s_, 12, SANS, INK))
              for k, (t, s_) in enumerate([('Título y Mussol Misol', 'Me dice qué voy a hacer en una frase.'), ('HAZLO ASÍ', 'Pasos numerados: hago un paso cada vez.'),
                                           ('¡HECHO!', 'Cuando termino, pinto el círculo.'), ('PAUSA ACTIVA', 'Cada pocas tareas muevo el cuerpo un momento.'),
                                           ('MIS LOGROS', 'Al final de cada mes pinto lo que ya sé.')])])]))
    d.add(K_cajita('RECUERDA', 'Si hoy no puedes terminar, no pasa nada. Marca hasta dónde has llegado y seguimos otro día.'))
    d.nuevo()
    d.add(K_titulo('Empezamos', 'Así es una clase', 'La clase siempre tiene los mismos pasos.'),
          K_mussol('Si sé qué viene después, me sale mejor. Estos son los pasos de la clase.'),
          K_panel('', 'MI HORARIO', [Blk(330, lambda c, x, y, w: [
              (rr(c, x, y - 52 - k * 58, w, 48, 12, fill=white if k % 2 == 0 else WARM, lw=1.4, col=NAVY), c.setFillColor(OCRE), c.circle(x + 28, y - 28 - k * 58, 15, stroke=0, fill=1),
               txt(c, x + 28, y - 34 - k * 58, str(k + 1), 15, SANSB, white, 'c'), txt(c, x + 56, y - 33 - k * 58, t, 13.5, SANSB, INK),
               trac(c, 1.8, OCRE), c.setFillColor(white), c.circle(x + w - 28, y - 28 - k * 58, 12, stroke=1, fill=1))
              for k, t in enumerate(['Saludo y respiración (1 minuto)', 'Repaso de lo que hice en casa', 'Tarea del cuaderno', 'Pausa activa', 'Al piano', 'Despedida: pinto mis logros'])])]))
    d.add(K_cajita('RECUERDA', 'Si cambia algo, el profesor te lo dirá antes de empezar.'))


def calendario(d, paginas):
    d.nuevo('Calendario')
    d.add(K_titulo('Calendario', 'Los 10 meses', 'Cada mes tiene un tema.'), K_mussol('Pinta el círculo cuando termines un mes.'))
    filas = []
    for mes, _, tema in MESES:
        filas.append((mes, tema, paginas.get(mes, '·')))

    def f(c, x, y, w):
        for k, (mes, tema, pg) in enumerate(filas):
            yy = y - k * 46
            rr(c, x, yy - 40, w, 40, 10, fill=white if k % 2 == 0 else WARM, lw=1.4, col=NAVY)
            txt(c, x + 14, yy - 26, mes, 13, SANSB, OCRE)
            txt(c, x + 112, yy - 26, tema, 13, SANS, INK)
            txt(c, x + w - 62, yy - 26, 'pág. %s' % pg, 11.5, SANS, MUTED, 'r')
            trac(c, 1.8, OCRE)
            c.setFillColor(white)
            c.circle(x + w - 26, yy - 20, 12, stroke=1, fill=1)
    d.add(Blk(len(filas) * 46 + 6, f))


def guia_adultos(d):
    d.nuevo('Para familia y profesorado')
    d.add(K_titulo('Anexo', 'Guía para familia y profesorado', 'Cómo está pensado este cuaderno y cómo sacarle partido.'),
          K_panel('', 'ESTE CUADERNO ES EL MISMO CONTENIDO, ADAPTADO', [
              K_par('El contenido es el del Nivel 1 KIDS: pentagrama, notas, teclado, escala de Do, compases, ritmo, claves, silencios, ligadura y puntillo. Lo que cambia es **cómo se presenta**, para que sea predecible, corto y con poco ruido visual.', 12, INK, 6),
              K_par('Estas adaptaciones se basan en recomendaciones generales de apoyo visual y estructura para alumnado con TEA y TDAH. No sustituyen la valoración de los profesionales que conocen al alumno: conviene ajustarlas con su familia y su equipo.', 11.5, NAVY_SOFT, 4)]))
    d.add(tabla_adapt())
    d.add(K_cajita('TRUCO', 'Si una actividad no sale, no la repitas igual: redúcela (una sola fila, una sola mano) y vuelve a subir. Las páginas de color de las notas sirven de apoyo; pueden retirarse poco a poco.'))
    d.nuevo()
    d.add(K_titulo('Anexo', 'Ideas para cada clase', 'Pequeñas decisiones que ayudan.'),
          K_panel('', 'ANTES, DURANTE Y DESPUÉS', [
              K_par('**Antes.** Mostrar el horario de la clase (página 3) y decir qué actividad toca. Evitar cambios de última hora; si los hay, avisar con tiempo.', 12, INK, 6),
              K_par('**Durante.** Una instrucción cada vez, en frases cortas y literales. Dejar tiempo para responder. Alternar actividad de mesa y movimiento (pausa activa) cada 5–8 minutos. '
                    'Ofrecer elegir entre dos opciones (por ejemplo, qué color usar) para dar sensación de control.', 12, INK, 6),
              K_par('**Si hay agobio.** Bajar el volumen del instrumento, reducir la tarea o pasar a una actividad que ya domine. Valorar el esfuerzo, no solo el acierto.', 12, INK, 6),
              K_par('**Después.** Pintar los logros del día. Terminar siempre con algo que el alumno sepa hacer bien.', 12, INK, 6)]))
    d.add(K_cajita('RECUERDA', 'Los juegos de sopa de letras, el test y el concierto son opcionales: se hacen solo si el alumno quiere y está tranquilo.'))


def tabla_adapt():
    filas = [('Una tarea por página', 'Menos distractores y un solo objetivo claro.'), ('Mismo orden en todas las páginas', 'Es predecible: título, ayuda, pasos, HECHO.'),
             ('Pasos numerados y frases cortas', 'Cada paso es una acción concreta; sin metáforas ni dobles sentidos.'),
             ('Casilla ¡HECHO! y tablero de logros', 'Ver el progreso motiva y permite parar sin perder el hilo.'), ('Pausa activa fija', 'Movimiento regulado cada pocas tareas.'),
             ('Color solo en las notas', 'El color significa algo siempre (cada nota, su color).'), ('Tareas opcionales marcadas con ★', 'Se pueden dejar sin que pase nada.')]
    h = 20 + len(filas) * 38

    def f(c, x, y, w):
        for k, (a, b) in enumerate(filas):
            yy = y - 8 - k * 38
            rr(c, x, yy - 34, w, 34, 8, fill=white if k % 2 == 0 else WARM, lw=1.2, col=NAVY)
            kpar(c, x + 10, yy - 14, a, 11, 214, 12.5, SANSB, NAVY)
            kpar(c, x + 230, yy - 14, b, 10, w - 236, 12, SANS, INK)
    return Blk(h, f)


def soluciones(d):
    d.nuevo('Soluciones')
    d.add(K_titulo('Anexo', 'Soluciones', 'Para el profesor o la familia.'))
    act = None
    for mes, num, tit, ls in n1_base.SOLUCIONES:
        if mes != act:
            act = mes
            d.add(K_par('**%s**' % mes.upper(), 12.5, OCRE, 3))
        d.add(K_par('**%s · %s:** %s' % (num if isinstance(num, str) else 'Act. %s' % num, tit, ' '.join(ls)), 10.5, INK, 4))


def pautas(d):
    d.nuevo('Papel pautado')
    d.add(K_titulo('Anexo', 'Papel pautado', 'Para dibujar, copiar y crear.'))
    for k in range(4):
        d.add(K_pauta_vacia('treble', 1, 11), K_pauta_vacia('bass', 1, 11))


def montar(c, prev, portada_=True):
    n1_base.SOLUCIONES.clear()
    if portada_:
        portada(c)
    d = Doc(c, 2 if portada_ else 1, prev)
    como_funciona(d)
    calendario(d, {m: prev.get('m:' + m, '·') for m, _, _ in MESES})
    for mes, fn, _ in MESES:
        d.marca('m:' + mes)
        fn(d)
    guia_adultos(d)
    soluciones(d)
    pautas(d)
    return d, d.fin()


def main():
    out = os.path.join(HERE, 'entrega')
    os.makedirs(out, exist_ok=True)
    bn = os.environ.get('BN') == '1'
    c1 = ManoCanvas(io.BytesIO(), pagesize=(W, H), seed=5, amp=0.0)
    d1, _ = montar(c1, {})
    c1.save()
    dst = os.path.join(out, 'CUADERNO_NIVEL1_KIDS%s.pdf' % ('_BN' if bn else ''))
    c2 = ManoCanvas(dst, pagesize=(W, H), seed=5, amp=0.0)
    c2.setTitle('Mi cuaderno de piano · Nivel 1 KIDS')
    c2.setAuthor('T-Clas')
    d2, fin = montar(c2, d1.marcas)
    c2.save()
    print('paginas:', fin - 1, '->', dst)


if __name__ == '__main__':
    main()
