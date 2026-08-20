# -*- coding: utf-8 -*-
"""Hojas de TRABAJO AL PIANO: la partitura desmontada y vuelta a montar.

   Las tres hojas anteriores preparan; esta es la única que trabaja la pieza:

   - El CALENTAMIENTO entrena la mano con secuencias inventadas a partir de
     la pieza. La AGUDEZA VISUAL entrena el ojo sin tocar. Ninguna de las dos
     toca la partitura de verdad.
   - Aquí el material NO se inventa: cada ejercicio es un trozo literal de la
     partitura, aislado. El método es el de cualquier profesor con oficio:

         AISLAR   -> sacar el trozo que falla, solo
         REDUCIR  -> quitarle el relleno y dejar la dificultad desnuda
         REINSERTAR -> devolverlo a su sitio y comprobar que ya está resuelto

   El error clásico de un cuaderno de ejercicios es quedarse en 'aislar'. Sin
   el paso de reinsertar, el alumno acaba tocando ejercicios muy bien y la
   pieza igual de mal. Por eso cada bloque acaba volviendo a la partitura.

   La velocidad no se trabaja tocando rápido, sino subiendo escalones con una
   regla: solo subes cuando sale dos veces seguidas sin parar. De ahí el
   bloque de la escalera de tempo, que es papel, no pentagrama, y es lo que
   de verdad se usa en casa entre semana.
"""
import sys, os, io
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from notation import draw_system
from page_layout_common import before_staff, after_system
from portada import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM,
                     INK, MUTED, ACCENT, _fit, _wrap)

BLUE = HexColor('#3E6E8F')
PANEL = HexColor('#F3F1EA')
WARM = HexColor('#F4EFE3')

# Pentagrama mas alto que en las hojas de lectura: aqui el alumno esta al
# piano, mirando de lejos y con las manos ocupadas, no con la hoja en la mano.
GAP = 7.4
BARS_PER_LINE = 4
# Una sola tabla de duraciones en todo el proyecto: la del motor. Esta copia
# local se quedo sin 'e.' y sin las semicorcheas, y una figura nueva reventaba
# aqui con un KeyError en vez de dibujarse.
from notation import DUR_BEATS as DUR, beats_de, INK


def _ej_heading(c, y, num, titulo, pista):
    c.setFillColor(ACCENT)
    c.roundRect(MARGIN, y - 13, 16, 16, 3, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 9)
    c.setFillColor(white)
    c.drawCentredString(MARGIN + 8, y - 9.5, str(num))
    c.setFont('DejaVuSans-Bold', 9.6)
    c.setFillColor(INK)
    c.drawString(MARGIN + 23, y - 9, titulo)
    tw = stringWidth(titulo, 'DejaVuSans-Bold', 9.6)
    hueco = CONTENT_W - 23 - tw - 12
    # 6.2 es el suelo de siempre: subirlo hace que pistas que llevaban veinte
    # canciones cabiendo al lado del titulo se bajen de linea, y ocho hojas se
    # salen por abajo. Solo se envuelve lo que no cabe ni asi.
    if stringWidth(pista, 'DejaVuSans', 6.2) <= hueco:
        psize = _fit(pista, 'DejaVuSans', 8.2, hueco, floor=6.2)
        c.setFont('DejaVuSans', psize)
        c.setFillColor(MUTED)
        c.drawString(MARGIN + 23 + tw + 12, y - 9, pista)
        return y - 21
    # No cabe: baja a su propia linea en vez de encogerse hasta ser ilegible o
    # salirse por la derecha, que es lo que hacia antes.
    y = _wrap(c, pista, MARGIN + 23, y - 20, 'DejaVuSans', 7.8,
              CONTENT_W - 23, 9.8, MUTED)
    return y - 3


# Contador de grupos de barrado. Los ids tienen que ser unicos DENTRO de un
# sistema; se lleva global y creciente para no chocar nunca con los `beam=` que
# algunas piezas ponen a mano.
_BEAM_AUTO = [9000]


def _autobeam(events, time_sig):
    """Barra las corcheas (y semicorcheas) seguidas, agrupando por golpe.

       Hasta ahora `draw_system` solo barraba lo que llevaba `beam=` escrito a
       mano, y el material de las hojas "al piano" casi nunca lo lleva: en
       produccion habia 74 sistemas imprimiendo corcheas seguidas con UN
       CORCHETE CADA UNA. Dieciseis seguidas en el Lovely de Josep. Ninguna
       edicion escribe eso —la corchea suelta lleva corchete, la seguida va
       barrada—, asi que el alumno miraba un pentagrama que no se parecia al
       suyo. Es la misma regla que el generador de lectura ya cumplia.

       Se agrupa POR GOLPE y sin cruzar la linea divisoria, que es como se
       barra de verdad: en 6/8 de tres en tres (la unidad es la negra con
       puntillo) y en los compases de negra, de dos en dos (o cuatro
       semicorcheas). Un silencio, una figura larga o el final del compas
       cierran el grupo.

       No toca lo que ya trae `beam=` a mano ni los acordes (el motor no sabe
       barrar acordes), y un grupo de uno se queda con su corchete, que es lo
       correcto."""
    corta = ('e', 'e.', 's', 's.')
    unidad = 1.5 if (time_sig[1] == 8 and time_sig[0] % 3 == 0) else 1.0
    bpb = time_sig[0] * (4.0 / time_sig[1])
    pos = 0.0            # posicion dentro del compas, en negras
    grupo = []

    def cerrar():
        if len(grupo) >= 2:
            _BEAM_AUTO[0] += 1
            for ev in grupo:
                ev['beam'] = _BEAM_AUTO[0]
        del grupo[:]

    for e in events:
        dur = e.get('dur')
        barrable = (dur in corta and not e.get('rest') and 'pitch' in e
                    and e.get('beam') is None and not e.get('tresillo'))
        if barrable:
            # el golpe al que pertenece esta nota; si cambia, el grupo anterior
            # se cierra aunque las figuras sigan siendo cortas
            if grupo and int(pos / unidad + 1e-9) != int(grupo[-1]['_golpe'] + 1e-9):
                cerrar()
            e['_golpe'] = pos / unidad
            grupo.append(e)
        else:
            cerrar()
        pos = (pos + beats_de(e)) % bpb
        if abs(pos) < 1e-9:          # cambio de compas: la barra no lo cruza
            cerrar()
    cerrar()
    for e in events:
        e.pop('_golpe', None)
    return events


def _partir_manos(events, time_sig, modo='dobla'):
    """Separa un sistema "las dos manos juntas" en sus dos pentagramas.

       El material de estos ejercicios viene escrito en UNA sola lista, con la
       izquierda metida dentro del mismo acorde que la melodia:

           [ac(('C3','E3','C4'))] + corch(['D4','E4','F4','G4','F4','E4'])

       Dibujado en un solo pentagrama de sol, ese Do3 cuelga de SEIS lineas
       adicionales. Habia 144 sistemas asi en produccion, uno o dos en cada
       pieza, siempre en el bloque de las dos manos. Un pianista no lee eso: la
       izquierda se escribe en clave de fa, en su pentagrama.

       El corte va en el Do central: lo que esta por debajo baja al pentagrama
       de fa y lo demas se queda arriba.

       QUE PASA CON LA DURACION de la izquierda depende de la pieza, y por eso
       NO se adivina: se declara en el sistema con `manos=`.

         'dobla' (lo normal, y lo que se hace si no se dice nada)
             la izquierda conserva la figura escrita y donde no toca hay
             silencio. Es lo correcto cuando las dos manos van a la vez, como
             en la Petite Chanson ("la izquierda dobla a la derecha").
         'sostiene'
             la izquierda se alarga hasta su siguiente acorde o hasta el final
             del compas. Es lo correcto cuando el bajo aguanta por debajo de
             una melodia que corre, como en Counting Stars ("la redonda
             sostiene bajo las corcheas"): ahi la nota esta escrita como negra
             solo porque iba metida en el mismo acorde que la melodia.

       Alargar siempre era comodo y estaba mal: en la Petite Chanson metia una
       blanca con puntillo que no habia escrito nadie."""
    bpb = time_sig[0] * (4.0 / time_sig[1])
    sostiene = modo == 'sostiene'
    arriba, abajo = [], []
    pos = 0.0
    pendiente = None          # (evento de fa, en que posicion empezo)

    def cerrar(hasta):
        """Cierra la nota de fa pendiente y rellena el hueco si hace falta."""
        if pendiente is None:
            return
        ev, ini = pendiente
        if sostiene:
            dur = _figura(hasta - ini)
            if dur:
                ev['dur'] = dur
                abajo.append(ev)
            return
        # modo 'dobla': la figura escrita se respeta y lo que sobra es silencio.
        # Alargarla seria inventar una duracion que no ha escrito nadie.
        abajo.append(ev)
        hueco = (hasta - ini) - beats_de(ev)
        while hueco > 1e-6:
            d = _figura(hueco)
            if not d:
                break
            abajo.append({'rest': True, 'dur': d})
            hueco -= DUR[d]

    for e in events:
        b = beats_de(e)
        ps = e.get('pitches') or ([e['pitch']] if 'pitch' in e else [])
        graves = [p for p in ps if _es_grave(p)]
        agudas = [p for p in ps if not _es_grave(p)]
        if e.get('rest') or not ps:
            arriba.append(dict(e))
        else:
            if agudas:
                ev = dict(e)
                ev.pop('pitches', None)
                if len(agudas) == 1:
                    ev['pitch'] = agudas[0]
                else:
                    ev.pop('pitch', None)
                    ev['pitches'] = agudas
                ev.pop('beam', None)
                arriba.append(ev)
            else:
                arriba.append({'rest': True, 'dur': e['dur']})
            if graves:
                cerrar(pos)
                ev = {k: v for k, v in e.items()
                      if k not in ('pitch', 'pitches', 'beam', 'lig', 'art',
                                   'matiz', 'cresc', 'dim', 'pedal', 'tresillo')}
                if len(graves) == 1:
                    ev['pitch'] = graves[0]
                else:
                    ev['pitches'] = graves
                pendiente = (ev, pos)
        pos += b
        if abs(pos % bpb) < 1e-9:       # fin de compas: la izquierda no lo cruza
            cerrar(pos)
            pendiente = None
    cerrar(pos)
    return arriba, abajo


def _es_grave(p):
    """Por debajo del Do central va al pentagrama de fa."""
    import re
    m = re.match(r'^([A-G])([b#]?)(-?\d+)$', str(p))
    return bool(m) and int(m.group(3)) < 4


# Que figura corresponde a un numero de tiempos. Solo las que el motor sabe
# dibujar: si el hueco no cae en ninguna (un 2.5, por ejemplo) se coge la mayor
# que quepa, que es preferible a inventar una figura que no existe.
_FIGURAS = [(4.0, 'w'), (3.0, 'h.'), (2.0, 'h'), (1.5, 'q.'), (1.0, 'q'),
            (0.75, 'e.'), (0.5, 'e'), (0.375, 's.'), (0.25, 's')]


def _figura(beats):
    for b, d in _FIGURAS:
        if beats >= b - 1e-9:
            return d
    return None


# Interruptor del sistema de piano (sol+fa) en los bloques de las dos manos.
# Ver el comentario de `_pide_dos_pentagramas`.
DOS_PENTAGRAMAS = [True]


def _pide_dos_pentagramas(events, clef):
    """True si el sistema mete las dos manos en un solo pentagrama de sol.

       Se detecta solo, sin tocar las 144 piezas afectadas: si un acorde lleva
       a la vez notas por debajo y por encima del Do central, es la izquierda
       metida dentro del acorde de la derecha y hay que abrir el pentagrama de
       fa. Un sistema que sea todo grave no entra aqui: ese solo necesita que
       le cambien la clave, y lo dice el auditor."""
    # DESACTIVADO a la espera de que el cliente decida la estructura: abrir el
    # pentagrama de fa anade unos 75 pt por sistema y estas hojas ya estan
    # llenas (el estandar es acabar entre 44 y 132). Medido sobre el album de
    # Nel: de 17 piezas, 8 se salen por abajo, la mayoria entre 60 y 80 pt. O
    # el bloque de las dos manos se va a una segunda hoja de "Como se estudia"
    # —y entonces cambia el numero de paginas de los diez albumes, que es
    # decision suya— o hay que quitar material medido, que la norma prohibe.
    if not DOS_PENTAGRAMAS[0]:
        return False
    if clef != 'treble':
        return False
    for e in events:
        ps = e.get('pitches') or []
        if len(ps) > 1 and any(_es_grave(p) for p in ps) and any(not _es_grave(p) for p in ps):
            return True
    return False


def _lineas(c, y, events, time_sig, bars_per_line, gap=GAP, show_time=True,
            clef='treble', key_sig=None, ottava=False, repetir=None, casilla=None,
            manos='dobla'):
    if _pide_dos_pentagramas(events, clef):
        return _lineas_dos_manos(c, y, events, time_sig, bars_per_line, gap,
                                 show_time, key_sig, manos=manos)
    _autobeam(events, time_sig)
    bpb = time_sig[0] * (4.0 / time_sig[1])
    line_beats = bpb * bars_per_line
    lines, cur, acc = [], [], 0.0
    for e in events:
        cur.append(e)
        acc += beats_de(e)
        if acc >= line_beats - 1e-6:
            lines.append(cur); cur, acc = [], 0.0
    if cur:
        lines.append(cur)
    for i, ln in enumerate(lines):
        # El 8va y la casilla van SOLO en la primera linea del sistema y la
        # barra que cierra la repeticion SOLO en la ultima: si se repartieran
        # por todas, un ejercicio de tres lineas saldria con tres 8va abiertos
        # y tres finales de repeticion, que en una edicion no significa nada.
        primera, ultima = i == 0, i == len(lines) - 1
        y -= before_staff(gap, ln, clef, ottava=bool(ottava) and primera,
                          casilla=casilla if primera else None)
        rep = None
        if repetir in ('abre', 'ambas') and primera:
            rep = 'abre'
        if repetir in ('cierra', 'ambas') and ultima:
            rep = 'ambas' if rep == 'abre' else 'cierra'
        top, bot = draw_system(c, MARGIN, y, CONTENT_W, gap, ln, clef=clef,
                               time_sig=time_sig, show_time=(i == 0 and show_time),
                               key_sig=key_sig, spacing='engraved',
                               ottava=bool(ottava) and primera,
                               repetir=rep, casilla=casilla if primera else None)
        # entre lineas hay que reservar tambien el sitio de las plicas y
        # barras que cuelgan: con un hueco fijo de 2*gap, un compas de
        # corcheas con la barra abajo se mete dentro del pentagrama siguiente
        last = i == len(lines) - 1
        y = bot - (after_system(gap, ln, clef) if last
                   else max(gap * 2.0, after_system(gap, ln, clef) * 0.85))
    return y


def _lineas_dos_manos(c, y, events, time_sig, bars_per_line, gap, show_time,
                      key_sig, manos='dobla'):
    """Un sistema de piano de verdad: sol arriba, fa abajo, unidos por su llave.

       El material llega en una sola lista con las dos manos mezcladas (ver
       `_partir_manos`). Se parte, se barra cada mano por su cuenta y se dibujan
       los dos pentagramas alineados, que es como se lee el piano."""
    arriba, abajo = _partir_manos(events, time_sig, modo=manos)
    _autobeam(arriba, time_sig)
    _autobeam(abajo, time_sig)
    y -= before_staff(gap, arriba, 'treble')
    t_top, t_bot = draw_system(c, MARGIN, y, CONTENT_W, gap, arriba, clef='treble',
                               time_sig=time_sig, show_time=show_time,
                               key_sig=key_sig, spacing='engraved')
    # 5.6 gaps entre pentagramas: es lo que necesita la clave de fa mas las
    # plicas que suben desde el pentagrama de abajo. Con menos se tocan.
    y2 = t_bot - gap * 5.6
    b_top, b_bot = draw_system(c, MARGIN, y2, CONTENT_W, gap, abajo, clef='bass',
                               time_sig=time_sig, show_time=show_time,
                               key_sig=key_sig, spacing='engraved')
    # la llave que une las dos manos: sin ella son dos ejercicios sueltos, no
    # un sistema de piano
    c.setStrokeColor(INK)
    c.setLineWidth(1.6)
    c.line(MARGIN, t_top, MARGIN, b_bot)
    return b_bot - after_system(gap, abajo, 'bass')


def _caption(c, y, texto):
    """Rotulo de un sistema concreto dentro de un ejercicio (a, b, c...)."""
    if not texto:
        return y
    size = _fit(texto, 'DejaVuSans-Bold', 7.8, CONTENT_W, floor=6.4)
    c.setFont('DejaVuSans-Bold', size)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y - 7, texto)
    return y - 12


def nota_clave(c, y, texto, etiqueta='LA CLAVE DE TODO'):
    """Caja destacada: la idea que hace que el ejercicio funcione. Va aparte
       de la 'pista' porque no es una instrucción, es el porqué."""
    size = 8.0
    inner = CONTENT_W - 26
    # medir cuantas lineas ocupa para dimensionar la caja antes de pintarla
    words, ln, count = texto.split(), '', 1
    for wd in words:
        t = (ln + ' ' + wd).strip()
        if stringWidth(t, 'DejaVuSans', size) > inner:
            count += 1; ln = wd
        else:
            ln = t
    h = 20 + count * 10.6
    c.setFillColor(WARM)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 7.2)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN + 13, y - 12, etiqueta)
    _wrap(c, texto, MARGIN + 13, y - 24, 'DejaVuSans', size, inner, 10.6, NAVY)
    return y - h - 10


def escalera_tempo(c, y, valores, regla, titulo='LA ESCALERA DE TEMPO'):
    """Los escalones de velocidad, con dos casillas por escalón. Subir de
       escalón solo cuando salga DOS veces seguidas sin parar: sin esa regla
       escrita, el alumno sube en cuanto le sale una vez y se atasca."""
    c.setFont('DejaVuSans-Bold', 8.2)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, titulo)
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.3)
    c.line(MARGIN, y - 5, MARGIN + 22, y - 5)
    y -= 14

    n = len(valores)
    rise, bh, sep = 8.5, 32, 5
    bw = (CONTENT_W - sep * (n - 1)) / n
    base = y - bh - (n - 1) * rise
    for i, v in enumerate(valores):
        bx = MARGIN + i * (bw + sep)
        by = base + i * rise
        c.setFillColor(PANEL)
        c.roundRect(bx, by, bw, bh, 3, fill=1, stroke=0)
        c.setFillColor(ACCENT)
        c.rect(bx, by + bh - 2.6, bw, 2.6, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 9.2)
        c.setFillColor(NAVY)
        c.drawCentredString(bx + bw / 2, by + 19, '♩=%d' % v)
        for k in range(2):
            sx = bx + bw / 2 - 10.5 + k * 13
            c.setStrokeColor(NAVY_SOFT)
            c.setLineWidth(0.9)
            c.setFillColor(white)
            c.rect(sx, by + 6, 8, 8, fill=1, stroke=1)
    y = base - 13
    size = _fit(regla, 'DejaVuSans-Bold', 8.0, CONTENT_W, floor=6.4)
    c.setFont('DejaVuSans-Bold', size)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN, y, regla)
    return y - 12


def tracker(c, y, titulo, pie, dias=('L', 'M', 'X', 'J', 'V', 'S', 'D')):
    """Registro de la semana: una casilla por día. Es lo que convierte la hoja
       en algo que se usa en casa y no solo en clase."""
    h = 46
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - h, CONTENT_W, h, 4, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.rect(MARGIN, y - h, 3, h, fill=1, stroke=0)
    c.setFont('DejaVuSans-Bold', 7.6)
    c.setFillColor(NAVY)
    c.drawString(MARGIN + 13, y - 14, titulo.upper())
    c.setFont('DejaVuSans', 7.2)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 13, y - 39, pie)

    bx = W - MARGIN - 13 - (len(dias) * 26 - 8)
    for d in dias:
        c.setFont('DejaVuSans-Bold', 6.8)
        c.setFillColor(MUTED)
        c.drawCentredString(bx + 9, y - 13, d)
        c.setStrokeColor(NAVY_SOFT)
        c.setLineWidth(0.9)
        c.setFillColor(white)
        c.rect(bx, y - 33, 18, 16, fill=1, stroke=1)
        bx += 26
    return y - h - 10


def _bloque(c, y, blq, cfg):
    """Dibuja UN bloque y devuelve la y de abajo.

       Sale del bucle de `build_piano` para poder MEDIRLO antes de
       dibujarlo: la hoja se pagina sola (ver `_paginar`) y para saber si
       un bloque cabe hay que saber cuanto ocupa, y eso solo se sabe
       dibujandolo."""
    tipo = blq.get('tipo', 'ej')
    if tipo == 'ej':
        y = _ej_heading(c, y, blq['num'], blq['titulo'], blq['pista'])
        for s in blq['sistemas']:
            y = _caption(c, y, s.get('cap'))
            # Un sistema puede declarar `matiz='p'` y se aplica a su primera
            # nota, que es donde va en cualquier edicion. Asi una pieza no
            # tiene que tocar su lista de notas solo para poner la dinamica.
            if s.get('matiz'):
                for _e in s['events']:
                    if not _e.get('rest'):
                        _e.setdefault('matiz', s['matiz'])
                        break
            # `ligar=True` arquea una ligadura de fraseo sobre TODO el
            # sistema (el "sempre legato" de tantas ediciones); `ligar=n`
            # la limita a las n primeras notas.
            if s.get('ligar'):
                _notas = [_e for _e in s['events'] if not _e.get('rest')]
                if len(_notas) >= 2:
                    _n = len(_notas) - 1 if s['ligar'] is True else int(s['ligar'])
                    _notas[0].setdefault('lig', max(1, min(_n, len(_notas) - 1)))
            # El resto del vocabulario de expresion, tambien declarable en
            # el sistema para no tener que tocar la lista de notas:
            #   staccato=True  -> punto en todas las notas
            #   acento=True    -> acento en la primera
            #   calderon=True  -> calderon en la ultima
            #   cresc/dim=n    -> regulador de n eventos desde la primera
            #   pedal=n        -> marca de pedal de n eventos
            _notas = [_e for _e in s['events'] if not _e.get('rest')]
            if _notas:
                if s.get('staccato'):
                    for _e in _notas:
                        _e.setdefault('art', 'staccato')
                if s.get('acento'):
                    _notas[0].setdefault('art', 'acento')
                if s.get('calderon'):
                    _notas[-1].setdefault('art', 'calderon')
                for _k in ('cresc', 'dim', 'pedal'):
                    if s.get(_k):
                        _notas[0].setdefault(_k, int(s[_k]))
            # un sistema puede llevar SU compas: hay piezas que cambian de
            # compas en un compas suelto (el c. 62 de When We Were Young)
            y = _lineas(c, y, s['events'], s.get('time_sig', cfg['time_sig']),
                        s.get('bars', BARS_PER_LINE),
                        gap=s.get('gap', cfg.get('gap', GAP)),
                        show_time=s.get('show_time', True),
                        clef=s.get('clef', 'treble'),
                        key_sig=s.get('key_sig', cfg.get('key_sig')),
                        ottava=s.get('ottava', False),
                        repetir=s.get('repetir'),
                        casilla=s.get('casilla'),
                        manos=s.get('manos', 'dobla'))
        y -= blq.get('extra_gap', 3)
    elif tipo == 'nota':
        y = nota_clave(c, y, blq['texto'], blq.get('etiqueta', 'LA CLAVE DE TODO'))
    elif tipo == 'escalera':
        y = escalera_tempo(c, y, blq['valores'], blq['regla'])
    elif tipo == 'tracker':
        y = tracker(c, y, blq['titulo'], blq['pie'])
    return y


# Hasta donde puede bajar el contenido antes de pisar el pie de pagina. El
# estandar del proyecto pide acabar entre 44 y 132; se pagina apuntando a la
# parte alta de esa horquilla para que la hoja siguiente no salga casi vacia.
SUELO = 48.0


# True mientras se esta MIDIENDO sobre un lienzo de prueba, no dibujando la
# hoja de verdad. Los escaneres que se enganchan a `draw_system` (los
# `cruzar_*.py`, que buscan material repetido entre alumnos) tienen que mirarlo
# y no anotar nada: si no, cada sistema se cuenta dos veces —una al medir y
# otra al dibujar— y encima con la etiqueta de la hoja anterior, porque al
# medir todavia no se ha empezado a dibujar esta. De ahi salian doce
# "coincidencias" del tipo `pieza_anterior/pauta + pieza_actual/piano 1` que no
# existian en ningun papel.
MIDIENDO = [False]


def _medir(cfg, blq, y):
    """Cuanto baja la y al dibujar este bloque, sin ensuciar nada.

       Se dibuja de verdad, sobre un lienzo que se tira: es la unica forma
       exacta de saber lo que ocupa un bloque, porque su altura depende del
       texto que envuelve, de las lineas adicionales de cada nota y de si el
       sistema abre o no el pentagrama de fa. Estimarlo "a ojo" es como se
       llego a tener hojas que se salian 80 pt por abajo."""
    import copy
    from reportlab.pdfgen.canvas import Canvas
    prueba = Canvas(io.BytesIO(), pagesize=(W, H))
    MIDIENDO[0] = True
    try:
        return _bloque(prueba, y, copy.deepcopy(blq), cfg)
    finally:
        MIDIENDO[0] = False


def _combinaciones(seq, k):
    from itertools import combinations
    return combinations(seq, k)


def _unidades(cfg):
    """Trocea los bloques en las piezas mas pequenas por las que se puede cortar.

       Un ejercicio de tres sistemas no tiene por que caber entero en una hoja:
       los metodos impresos parten por sistemas y repiten el titulo con un
       "(sigue)". Sin eso, la unica granularidad son bloques de 300 pt contra
       una horquilla de llenado de 84, y casi ninguna pieza tiene un corte
       legal: hay que ir retocando el material a mano pieza por pieza, que con
       88 piezas es exactamente lo que no se puede hacer.

       Devuelve una lista de unidades (idx_bloque, sistema, coste, coste_titulo).
       `coste_titulo` solo se paga cuando la unidad ABRE grupo en su hoja: si
       dos sistemas del mismo ejercicio caen seguidos, el titulo va una vez."""
    y0 = _ALTO_CABECERA(cfg)
    fuera = []
    for bi, blq in enumerate(cfg['bloques']):
        sis = blq.get('sistemas') if blq.get('tipo', 'ej') == 'ej' else None
        if not sis:
            fuera.append((bi, None, y0 - _medir(cfg, blq, y0), 0.0))
            continue
        solo_titulo = y0 - _medir(cfg, dict(blq, sistemas=[]), y0)
        prev = solo_titulo
        for s in sis:
            acum = y0 - _medir(cfg, dict(blq, sistemas=[s]), y0)
            fuera.append((bi, s, acum - solo_titulo, solo_titulo))
            prev = acum
    return fuera


def _titulo_sigue(t):
    return t if t.endswith('(sigue)') else t + ' (sigue)'


def _paginar(cfg):
    """Reparte los bloques en las hojas que hagan falta.

       Antes cabia todo en una hoja porque las dos manos se apretaban en un
       solo pentagrama de sol. Al abrir el pentagrama de fa —que es como se
       escribe el piano— el bloque de las dos manos ya no entra, y la decision
       del cliente fue darle su propia hoja en vez de quitar material medido.

       Se parte por bloques enteros: un ejercicio no se corta a la mitad.

       Y se reparte EQUILIBRANDO, no llenando la primera hasta que revienta.
       Llenar de forma codiciosa cumple el limite de abajo pero incumple el de
       arriba: la primera hoja sale a reventar y la ultima con media pagina en
       blanco, que el estandar cuenta —con razon— como hoja a medio hacer. Se
       buscan repartos donde TODAS las hojas caigan dentro de la horquilla, y
       entre ellos el mas parejo."""
    bloques = cfg['bloques']
    uds = _unidades(cfg)
    y0 = _ALTO_CABECERA(cfg)

    def alto(ini, fin):
        """Lo que ocupa el tramo de unidades [ini, fin) puesto en una hoja."""
        total, anterior = 0.0, None
        for bi, _s, coste, titulo in uds[ini:fin]:
            if bi != anterior:
                total += titulo
                anterior = bi
            total += coste
        return total

    def rehacer(ini, fin):
        """Los bloques dibujables de ese tramo, con su "(sigue)" si toca."""
        salida, anterior, sistemas = [], None, []

        def volcar():
            if anterior is None:
                return
            base = bloques[anterior]
            if sistemas is None or not sistemas:
                salida.append(base)
            else:
                corta = sistemas[0] is not (base.get('sistemas') or [None])[0]
                tit = _titulo_sigue(base['titulo']) if corta else base['titulo']
                salida.append(dict(base, sistemas=list(sistemas), titulo=tit))

        for bi, s, _c, _t in uds[ini:fin]:
            if bi != anterior:
                volcar()
                anterior, sistemas = bi, ([] if s is not None else None)
            if s is not None:
                sistemas.append(s)
        volcar()
        return salida
    # cuanto contenido admite una hoja para acabar dentro de la horquilla
    maximo = y0 - SUELO
    minimo = y0 - 132.0
    N = len(uds)

    def cortes_en(n):
        """Los n-1 cortes que dejan las hojas mas parejas, o None si no cabe.

           Fuerza bruta sobre los cortes posibles: son pocas unidades por hoja,
           asi que es exacto y sobra de rapido. Con una heuristica salian
           repartos legales pero feos, del tipo cinco ejercicios arriba y uno
           abajo."""
        mejor = None
        for corte in _combinaciones(range(1, N), n - 1):
            limites = [0] + list(corte) + [N]
            trozos = [alto(limites[k], limites[k + 1]) for k in range(n)]
            if any(t > maximo for t in trozos):
                continue
            # El minimo no se mide contra el contenido pelado: la hoja se
            # justifica y puede abrir hasta AIRE_MAX por hueco (ver
            # `build_piano`). Lo que hay que comprobar es si ESTIRADA llega
            # abajo. La ultima hoja puede quedarse corta igualmente, y entonces
            # lo canta el auditor: es la senal de que falta material escrito.
            corto = False
            for k in range(n - 1):
                huecos = limites[k + 1] - limites[k]
                if trozos[k] + huecos * AIRE_MAX < minimo:
                    corto = True
            if corto:
                continue
            coste = max(trozos) - min(trozos)      # lo mas parejo posible
            if mejor is None or coste < mejor[0]:
                mejor = (coste, limites)
        return None if mejor is None else mejor[1]

    for n in range(1, N + 1):
        limites = cortes_en(n)
        if limites is None:
            continue
        return [rehacer(limites[k], limites[k + 1]) for k in range(n)]

    # Ningun reparto deja TODAS las hojas dentro de la horquilla: a la pieza le
    # falta material para llenar lo que ocupa. Se reparte llenando sin pasarse
    # —una hoja corta se puede leer, una desbordada no— y el auditor lo dice con
    # su "falta material", que es la senal de que hay que escribir mas.
    limites, acc = [0], 0.0
    for i in range(N):
        paso = alto(limites[-1], i + 1)
        if paso > maximo and i > limites[-1]:
            limites.append(i)
    limites.append(N)
    return [rehacer(limites[k], limites[k + 1]) for k in range(len(limites) - 1)]


def _ALTO_CABECERA(cfg):
    """La y a la que empieza el primer bloque, medida igual que en build_piano."""
    from reportlab.pdfgen.canvas import Canvas
    return _cabecera(Canvas(io.BytesIO(), pagesize=(W, H)), cfg)


def _cabecera(c, cfg):
    """Fondo, titulo, intro y la banda de reglas. Devuelve la y del primer bloque.

       Esta suelta porque `_paginar` necesita saber a que altura empieza el
       contenido, y porque la dibujan igual la primera hoja y las siguientes:
       una segunda hoja de "Como se estudia" sin cabecera no se entiende."""
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    y = H - 44
    c.setFont('DejaVuSans-Bold', 8.4)
    c.setFillColor(NAVY_SOFT)
    c.drawString(MARGIN, y, cfg['kicker'].upper())
    c.setFont('DejaVuSans', 8.4)
    c.setFillColor(MUTED)
    c.drawRightString(W - MARGIN, y, cfg['esquina'])
    y -= 28

    c.setFont('DejaVuSerif-Bold', 24)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, y, cfg['titulo'])
    y -= 16
    y = _wrap(c, cfg['intro'], MARGIN, y, 'DejaVuSans', 9, CONTENT_W, 11.6, MUTED)
    y -= 8

    bh = 24
    c.setFillColor(PANEL)
    c.roundRect(MARGIN, y - bh, CONTENT_W, bh, 4, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(MARGIN, y - bh, 3, bh, fill=1, stroke=0)
    reglas = cfg['reglas']
    size = 8.2
    while size > 6.0 and (sum(stringWidth(r, 'DejaVuSans-Bold', size) for r in reglas)
                          + 24 * (len(reglas) - 1)) > CONTENT_W - 26:
        size -= 0.2
    rx = MARGIN + 13
    for i, r in enumerate(reglas):
        c.setFont('DejaVuSans-Bold', size)
        c.setFillColor(NAVY)
        c.drawString(rx, y - 15, r)
        rx += stringWidth(r, 'DejaVuSans-Bold', size)
        if i < len(reglas) - 1:
            c.setFillColor(ACCENT)
            c.circle(rx + 12, y - 12, 1.8, fill=1, stroke=0)
            rx += 24
    return y - (bh + 14)


def _pie(c, cfg):
    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()


def build_piano(c, cfg):
    """Dibuja UNA hoja: los bloques que le tocan a `cfg['bloques']`.

       El reparto en hojas lo hace `_paginar` y lo aplica `cancion.py`; aqui se
       dibuja lo que llegue, JUSTIFICADO: el aire que sobra se reparte entre los
       ejercicios en vez de quedarse todo junto al final.

       Es lo que hace cualquier metodo impreso y es lo que hacia falta aqui: los
       bloques miden entre 40 y 310 pt y la horquilla de llenado son 88, asi que
       casi ninguna pieza cae dentro por si sola. Sin justificar habia que ir
       retocando el material pieza a pieza hasta cuadrar el numero, que con 88
       piezas no es trabajo, es un bucle. El tope por hueco existe para que una
       hoja con poco material no acabe pareciendo un cartel."""
    y = _cabecera(c, cfg)
    bloques = cfg['bloques']
    aire = _aire(cfg, y, bloques)
    for blq in bloques:
        y = _bloque(c, y, blq, cfg) - aire
    _pie(c, cfg)
    return y


# Donde se quiere que acabe una hoja justificada. El estandar admite de 44 a
# 132; se apunta al centro para dejar margen a los dos lados.
OBJETIVO = 88.0
# Lo mas que se puede abrir un hueco entre ejercicios. Mas que esto ya no
# parece una hoja llena, parece una hoja con los ejercicios separados a la
# fuerza, y entonces lo honesto es decir que falta material.
AIRE_MAX = 26.0


def _aire(cfg, y0, bloques):
    """Cuanto se abre cada hueco para que la hoja acabe donde tiene que acabar."""
    if not bloques:
        return 0.0
    import copy
    from reportlab.pdfgen.canvas import Canvas
    prueba = Canvas(io.BytesIO(), pagesize=(W, H))
    y = y0
    MIDIENDO[0] = True
    try:
        for blq in bloques:
            y = _bloque(prueba, y, copy.deepcopy(blq), cfg)
    finally:
        MIDIENDO[0] = False
    sobra = y - OBJETIVO
    if sobra <= 0:
        return 0.0
    return min(sobra / len(bloques), AIRE_MAX)
