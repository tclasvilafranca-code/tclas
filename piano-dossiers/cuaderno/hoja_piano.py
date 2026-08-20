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
import sys, os
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


def _partir_manos(events, time_sig):
    """Separa un sistema "las dos manos juntas" en sus dos pentagramas.

       El material de estos ejercicios viene escrito en UNA sola lista, con la
       izquierda metida dentro del mismo acorde que la melodia:

           [ac(('C3','E3','C4'))] + corch(['D4','E4','F4','G4','F4','E4'])

       Dibujado en un solo pentagrama de sol, ese Do3 cuelga de SEIS lineas
       adicionales. Habia 144 sistemas asi en produccion, uno o dos en cada
       pieza, siempre en el bloque de las dos manos. Un pianista no lee eso: la
       izquierda se escribe en clave de fa, en su pentagrama.

       El corte va en el Do central: lo que esta por debajo baja al pentagrama
       de fa y lo demas se queda arriba. Y la nota de la izquierda se ALARGA
       hasta el siguiente acorde suyo (o hasta el final del compas), que es lo
       que dicen los propios rotulos de estos ejercicios ("la redonda sostiene
       bajo las corcheas") y lo que se toca de verdad: escrita como negra, la
       izquierda parecia soltar en el segundo golpe."""
    bpb = time_sig[0] * (4.0 / time_sig[1])
    arriba, abajo = [], []
    pos = 0.0
    pendiente = None          # (evento de fa, en que posicion empezo)

    def cerrar(hasta):
        if pendiente is None:
            return
        ev, ini = pendiente
        dur = _figura(hasta - ini)
        if dur:
            ev['dur'] = dur
            abajo.append(ev)

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
DOS_PENTAGRAMAS = [False]


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
            clef='treble', key_sig=None, ottava=False, repetir=None, casilla=None):
    if _pide_dos_pentagramas(events, clef):
        return _lineas_dos_manos(c, y, events, time_sig, bars_per_line, gap,
                                 show_time, key_sig)
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


def _lineas_dos_manos(c, y, events, time_sig, bars_per_line, gap, show_time, key_sig):
    """Un sistema de piano de verdad: sol arriba, fa abajo, unidos por su llave.

       El material llega en una sola lista con las dos manos mezcladas (ver
       `_partir_manos`). Se parte, se barra cada mano por su cuenta y se dibujan
       los dos pentagramas alineados, que es como se lee el piano."""
    arriba, abajo = _partir_manos(events, time_sig)
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


def build_piano(c, cfg):
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
    y -= bh + 14

    for blq in cfg['bloques']:
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
                            casilla=s.get('casilla'))
            y -= blq.get('extra_gap', 3)
        elif tipo == 'nota':
            y = nota_clave(c, y, blq['texto'], blq.get('etiqueta', 'LA CLAVE DE TODO'))
        elif tipo == 'escalera':
            y = escalera_tempo(c, y, blq['valores'], blq['regla'])
        elif tipo == 'tracker':
            y = tracker(c, y, blq['titulo'], blq['pie'])

    c.setFont('DejaVuSans', 7.4)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, 26, 'El Cuaderno del Pianista  ·  T-Clas')
    c.drawRightString(W - MARGIN, 26, str(cfg.get('page_num', '')))
    c.showPage()
    return y
