# -*- coding: utf-8 -*-
"""MI CUADERNO DE PIANO · NIVEL 1 · ADULTOS (castellano).

   Base del cuaderno: marco de pagina, flujo de bloques (cada bloque sabe cuanto mide), componentes
   (cajas «Tecla al dato» / «Tip musical», cabecera de ejercicio), filas de pentagrama para ejercicios
   (notas sueltas, compases con huecos, pautas vacias), teclados, sopa de letras y soluciones.

   Todo el material musical sale de datos explicitos: las soluciones del final se calculan a partir
   de los mismos datos que dibujan el ejercicio, asi no pueden contradecirse."""
import os
import sys
import random
HERE = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault('ALUMNA', 'alba')        # tema sobrio (adulto)
os.environ.setdefault('IDIOMA', 'es')          # sin traduccion automatica al catalan
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
sys.path.append(os.path.join(HERE, '..', 'cuaderno'))
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth
from mayores_motor import (W, H, MARGIN, CONTENT_W, NAVY, NAVY_SOFT, CREAM, INK, MUTED, PANEL, OCRE, AZUL,
                           VERDE, ROJO, BLANCO, GRIS, marco)
from notation import (draw_staff, draw_clef, draw_time_sig, draw_barline, draw_note, draw_rest, draw_notehead,
                      note_y, ledger_lines_needed, draw_ledger, draw_beam, draw_headless_note, _abs_idx)

GAP = 8.0
BOTTOM = 56.0
TOP = H - 64.0
RULE = HexColor('#C9CFD8')
CREMA2 = HexColor('#F3EEDF')
SOMBRA = HexColor('#E7E0CC')
KICKER = 'MI CUADERNO DE PIANO  ·  NIVEL 1  ·  ADULTOS'

NOMBRE = {'C': 'Do', 'D': 'Re', 'E': 'Mi', 'F': 'Fa', 'G': 'Sol', 'A': 'La', 'B': 'Si'}
LETRAS = 'CDEFGAB'


def nombre(p, octava=False):
    """'F#4' -> 'Fa♯'  ('Fa♯4' con octava)."""
    n = NOMBRE[p[0]]
    acc = ''
    rest = p[1:]
    if rest and rest[0] in '#bn':
        acc = {'#': '♯', 'b': '♭', 'n': '♮'}[rest[0]]
        rest = rest[1:]
    return n + acc + (rest if octava else '')


# ------------------------------------------------------------------ texto enriquecido
def _toks(txt):
    """Divide en palabras; cada palabra = lista de (trozo, negrita) (los trozos pegados, p. ej. '**Sol**,' ,
       forman una sola palabra para que no se separe el signo de puntuacion). **...** pone negrita."""
    import re
    words, cur, bold = [], [], False
    for k, parte in enumerate(txt.split('**')):
        if k:
            bold = not bold
        for m in re.finditer(r'\S+|\s+', parte):
            t = m.group(0)
            if t.isspace():
                if cur:
                    words.append(cur)
                    cur = []
            else:
                cur.append((t, bold))
    if cur:
        words.append(cur)
    return words


def _fuente(bold, size=None):
    return 'DejaVuSans-Bold' if bold else 'DejaVuSans'


def _wd_w(wd, size):
    return sum(stringWidth(t, _fuente(b), size) for t, b in wd)


def lineas(txt, w, size):
    """Lista de lineas; cada linea = lista de palabras (ver _toks). Respeta \\n como salto."""
    res = []
    sp = stringWidth(' ', 'DejaVuSans', size)
    for par in txt.split('\n'):
        cur, cw = [], 0.0
        for wd in _toks(par):
            ww = _wd_w(wd, size)
            if cur and cw + sp + ww > w:
                res.append(cur)
                cur, cw = [], 0.0
            cw += (sp if cur else 0) + ww
            cur.append(wd)
        res.append(cur)
    return res


def pinta_lineas(c, ls, x, y, size, lead, color=INK, centrado_w=None):
    """Dibuja las lineas con la primera baseline en y-size. Devuelve la y de debajo."""
    sp = stringWidth(' ', 'DejaVuSans', size)
    for ln in ls:
        yy = y - size
        xx = x
        if centrado_w is not None:
            tot = sum(_wd_w(wd, size) for wd in ln) + sp * (len(ln) - 1)
            xx = x + (centrado_w - tot) / 2.0
        for wd in ln:
            for t, b in wd:
                c.setFont(_fuente(b), size)
                c.setFillColor(color)
                c.drawString(xx, yy, t)
                xx += stringWidth(t, _fuente(b), size)
            xx += sp
        y -= lead
    return y


# ------------------------------------------------------------------ bloques
class Blk:
    """Un bloque = alto fijo + funcion de dibujo f(c, x, y_top, w)."""

    def __init__(self, h, f, keep_next=False):
        self.h = h
        self.f = f
        self.keep_next = keep_next


def espacio(h):
    return Blk(h, lambda c, x, y, w: None)


def par(txt, size=9.4, color=INK, lead=None, sangria=0, despues=6, centrado=False):
    lead = lead or size * 1.42

    def f(c, x, y, w):
        pinta_lineas(c, lineas(txt, w - sangria, size), x + sangria, y, size, lead, color,
                     centrado_w=(w - sangria) if centrado else None)
    h = len(lineas(txt, CONTENT_W - sangria, size)) * lead + despues
    return Blk(h, f)


def par_w(txt, w, size=9.4, color=INK, lead=None, despues=6):
    """Parrafo para un ancho distinto del de pagina (dentro de cajas/columnas)."""
    lead = lead or size * 1.42
    ls = lineas(txt, w, size)

    def f(c, x, y, ww):
        pinta_lineas(c, ls, x, y, size, lead, color)
    return Blk(len(ls) * lead + despues, f)


def lista(items, size=9.4, marca='•', color=INK, lead=None, sangria=14, despues=6, sep=2.4, col_marca=None):
    lead = lead or size * 1.42
    wi = CONTENT_W - sangria
    alt = [len(lineas(t, wi, size)) * lead + sep for t in items]

    def f(c, x, y, w):
        for t, hh in zip(items, alt):
            c.setFont('DejaVuSans-Bold', size)
            c.setFillColor(col_marca or NAVY_SOFT)
            c.drawString(x + 3, y - size, marca)
            pinta_lineas(c, lineas(t, w - sangria, size), x + sangria, y, size, lead, color)
            y -= hh
    return Blk(sum(alt) + despues, f)


def h2(txt, color=NAVY_SOFT, antes=4, despues=8):
    def f(c, x, y, w):
        yy = y - antes
        c.setFont('DejaVuSans-Bold', 8.4)
        c.setFillColor(color)
        c.drawString(x, yy - 8.4, txt.upper())
        tw = stringWidth(txt.upper(), 'DejaVuSans-Bold', 8.4)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.7)
        c.line(x + tw + 8, yy - 5.5, x + w, yy - 5.5)
    return Blk(antes + 12 + despues, f, keep_next=True)


def banda_mes(mes, trimestre, titulo, sub):
    """Cabecera de mes: etiqueta ocre, titulo serif grande, subtitulo."""
    lsub = lineas(sub, CONTENT_W, 10)
    h = 22 + 34 + len(lsub) * 14 + 14

    def f(c, x, y, w):
        c.setFillColor(OCRE)
        c.roundRect(x, y - 16, stringWidth(mes.upper(), 'DejaVuSans-Bold', 8.2) + 18, 16, 3, fill=1, stroke=0)
        c.setFillColor(BLANCO)
        c.setFont('DejaVuSans-Bold', 8.2)
        c.drawString(x + 9, y - 11.4, mes.upper())
        c.setFillColor(MUTED)
        c.setFont('DejaVuSans', 8.2)
        c.drawString(x + stringWidth(mes.upper(), 'DejaVuSans-Bold', 8.2) + 28, y - 11.4, trimestre)
        c.setFillColor(NAVY)
        c.setFont('DejaVuSerif-Bold', 25)
        c.drawString(x, y - 22 - 26, titulo)
        pinta_lineas(c, lsub, x, y - 22 - 34 - 2, 10, 14, MUTED)
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.4)
        c.line(x, y - h + 6, x + 44, y - h + 6)
    return Blk(h, f)


ICONOS = {'dato': ('!', OCRE, 'TECLA AL DATO'), 'tip': ('♪', NAVY, 'TIP MUSICAL'), 'ojo': ('!', ROJO, 'OJO'),
          'nota': ('i', AZUL, 'PARA SABER MÁS'), 'piano': ('♫', VERDE, 'AL PIANO')}


def caja(tipo, titulo, bloques, w=CONTENT_W, pad=13, keep=True):
    """Caja crema con filete de color a la izquierda, icono y rotulo."""
    sim, col, rot = ICONOS[tipo]
    if isinstance(bloques, str):
        bloques = [bloques]
    bl = []
    for b in bloques:
        bl.append(par_w(b, w - 2 * pad - 6, 9.1, INK, 12.9, 5) if isinstance(b, str) else b)
    cab = 30 if titulo else 22
    h = cab + sum(b.h for b in bl) + pad - 4

    def f(c, x, y, ww):
        c.setFillColor(SOMBRA)
        c.roundRect(x + 1.6, y - h - 1.6, w, h, 5, fill=1, stroke=0)
        c.setFillColor(PANEL)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.6)
        c.roundRect(x, y - h, w, h, 5, fill=1, stroke=1)
        c.setFillColor(col)
        c.roundRect(x, y - h, 4.5, h, 2, fill=1, stroke=0)
        c.setFillColor(col)
        c.circle(x + pad + 6, y - 15, 7, fill=1, stroke=0)
        c.setFillColor(BLANCO)
        c.setFont('DejaVuSans-Bold', 9.2)
        c.drawCentredString(x + pad + 6, y - 18.2, sim)
        c.setFillColor(col)
        c.setFont('DejaVuSans-Bold', 7.6)
        c.drawString(x + pad + 19, y - 12.6, rot)
        yy = y - 18
        if titulo:
            c.setFillColor(NAVY)
            c.setFont('DejaVuSerif-Bold', 11.2)
            c.drawString(x + pad + 19, y - 24.5, titulo)
            yy = y - 36
        else:
            yy = y - 26
        for b in bl:
            b.f(c, x + pad + 6, yy, w - 2 * pad - 6)
            yy -= b.h
    return Blk(h + 10, f, keep_next=keep)


def ejercicio(num, titulo, hacer, para=None, hecho_en=None):
    """Cabecera de ejercicio: circulo con el numero, titulo serif, instrucciones y para-que-sirve."""
    items = hacer if isinstance(hacer, list) else [hacer]
    w_i = CONTENT_W - 44
    ls_i = [lineas(t, w_i - 12, 9.1) for t in items]
    lp = lineas(para, w_i, 8.6) if para else []
    h = 30 + sum(len(l) for l in ls_i) * 12.6 + (len(items) * 2) + (len(lp) * 11.6 + 6 if lp else 0) + 6

    def f(c, x, y, w):
        c.setFillColor(NAVY)
        c.circle(x + 14, y - 16, 14, fill=1, stroke=0)
        c.setFillColor(BLANCO)
        c.setFont('DejaVuSerif-Bold', 15)
        c.drawCentredString(x + 14, y - 21.4, str(num))
        c.setFillColor(NAVY)
        c.setFont('DejaVuSerif-Bold', 13.2)
        c.drawString(x + 38, y - 14, titulo)
        c.setStrokeColor(OCRE)
        c.setLineWidth(1.1)
        c.line(x + 38, y - 21, x + 38 + 26, y - 21)
        yy = y - 28
        for ls in ls_i:
            c.setFillColor(OCRE)
            c.setFont('DejaVuSans-Bold', 9.1)
            c.drawString(x + 40, yy - 9.1, '›')
            yy = pinta_lineas(c, ls, x + 52, yy, 9.1, 12.6, INK) - 2
        if lp:
            yy -= 1
            c.setFillColor(OCRE)
            c.setFont('DejaVuSans-Bold', 7.6)
            c.drawString(x + 38, yy - 8, 'PARA QUÉ SIRVE')
            pinta_lineas(c, lp, x + 38 + 76, yy - 0.5, 8.6, 11.6, NAVY_SOFT)
    return Blk(h, f, keep_next=True)


def objetivo_inline(txt):
    return par(txt, 8.6, NAVY_SOFT, 11.6)


# ------------------------------------------------------------------ flujo de paginas
class Doc:
    """Acumula bloques y los reparte en paginas al final (fin()), para poder
       (1) no dejar cabeceras huerfanas (keep_next entre llamadas distintas),
       (2) repartir el aire sobrante entre los bloques cuando la pagina se cierra sola,
       (3) saber en que pagina cae cada marca (indice y calendario)."""

    def __init__(self, c, n0=1, marcas_prev=None):
        self.c = c
        self.n0 = n0
        self.items = []
        self.marcas = {}
        self.prev = marcas_prev or {}
        self.paginas = []
        self.estirar_max = 24.0

    def nuevo(self, derecha=None, estirar=False):
        self.items.append(('break', derecha, estirar))

    pagina = nuevo

    def seccion(self, derecha):
        self.items.append(('sec', derecha))

    def marca(self, nombre):
        self.items.append(('marca', nombre))

    def add(self, *bloques):
        for b in bloques:
            self.items.append(('blk', b))

    def _paginar(self):
        pages = []
        cur = None
        der = ''
        pend = []
        n = len(self.items)

        def abre():
            return {'der': der, 'blocks': [], 'y': TOP, 'est': True, 'marcas': []}
        i = 0
        while i < n:
            it = self.items[i]
            tipo = it[0]
            if tipo == 'sec':
                der = it[1]
                if cur is not None and not cur['blocks']:
                    cur['der'] = der
            elif tipo == 'break':
                if it[1] is not None:
                    der = it[1]
                if cur is not None and cur['blocks']:
                    cur['est'] = bool(it[2])
                    pages.append(cur)
                    cur = None
                if cur is not None and not cur['blocks']:
                    cur['der'] = der
            elif tipo == 'marca':
                pend.append(it[1])
            else:
                b = it[1]
                need = b.h
                j = i
                while self.items[j][0] == 'blk' and self.items[j][1].keep_next and j + 1 < n and self.items[j + 1][0] == 'blk':
                    j += 1
                    need += self.items[j][1].h
                if cur is None:
                    cur = abre()
                elif need > cur['y'] - BOTTOM and cur['blocks']:
                    pages.append(cur)
                    cur = abre()
                if b.h > TOP - BOTTOM + 0.1:
                    raise ValueError('bloque mas alto que la pagina (%.0f)' % b.h)
                cur['blocks'].append(b)
                cur['marcas'].extend(pend)
                pend = []
                cur['y'] -= b.h
            i += 1
        if cur is not None and cur['blocks']:
            cur['est'] = False
            pages.append(cur)
        return pages

    def fin(self):
        pages = self._paginar()
        for k, pg in enumerate(pages):
            num = self.n0 + k
            for m in pg['marcas']:
                self.marcas[m] = num
            marco(self.c, KICKER, pg['der'], num)
            bl = pg['blocks']
            libre = pg['y'] - BOTTOM
            extra = 0.0
            huecos = [i for i in range(len(bl) - 1) if not bl[i].keep_next]
            if pg['est'] and huecos and libre > 0:
                extra = min(self.estirar_max, libre / float(len(huecos)))
            y = TOP
            for i, b in enumerate(bl):
                b.f(self.c, MARGIN, y, CONTENT_W)
                y -= b.h + (extra if i in huecos else 0)
            # espacio sobrante: practica libre en pentagramas (solo en las paginas de los temas)
            resto = y - BOTTOM
            if resto >= 82 and 'Anexo' not in pg['der'] and 'Calendario' not in pg['der'] and 'Cómo usar' not in pg['der']:
                alto_p = 4 * GAP + GAP * 4.6
                n_p = int((resto - 24) // alto_p)
                if n_p >= 1:
                    self.c.setFont('DejaVuSans-Bold', 8.2)
                    self.c.setFillColor(OCRE)
                    self.c.drawString(MARGIN, y - 12, 'PRÁCTICA LIBRE · escribe, copia o inventa')
                    for j in range(min(n_p, 4)):
                        ys_ = draw_staff(self.c, MARGIN, y - 24 - j * alto_p - GAP * 1.6, CONTENT_W, GAP)
                        clef_ = 'treble' if j % 2 == 0 else 'bass'
                        draw_clef(self.c, MARGIN + 4, ys_[-1], GAP, clef_)
                        draw_barline(self.c, MARGIN, ys_[0], ys_[-1])
                        draw_barline(self.c, MARGIN + CONTENT_W - 4, ys_[0], ys_[-1], final=True)
            self.c.showPage()
            self.paginas.append((num, pg['der']))
        return self.n0 + len(pages)


# ------------------------------------------------------------------ pentagramas de ejercicio
def _extra_ledger(cy, bot, top, gap):
    return len(ledger_lines_needed(bot, top, cy, gap))


def fila_notas(clef, notas, dur='q', gap=GAP, bajo='linea', encima=None, caja_ancho=None, barras=0, ts=None,
               ancho=CONTENT_W, titulo=None, flechas=None, etiqueta_nota=None, claves_por_nota=None,
               plica=None, cabeza_sola=False, solucion_bajo=None):
    """Pentagrama con notas repartidas a igual distancia (ejercicios de lectura/nombres).
       notas: lista de alturas ('C4'), o None = hueco (el alumno escribe la nota).
       bajo: 'linea' (raya para escribir el nombre), 'nombres' (rotulo impreso), 'nada', o lista de textos.
       encima: textos sobre cada nota (digitos, etc.). barras: cada cuantas notas va una barra de compas.
       plica: lista 'up'/'down'/None por nota; cabeza_sola dibuja solo cabezas (para que el alumno ponga plicas)."""
    bot_off = 0
    n = len(notas)
    cys = []
    sup = inf = 0
    ref = 0
    for p in notas:
        if p is None:
            continue
        cy = note_y(0.0, gap, p, clef)
        cys.append(cy)
        sup = max(sup, cy - 4 * gap)
        inf = max(inf, -cy)
    pad_up = max(gap * 2.0, sup + gap * 1.4) + (gap * 2.0 if encima else 0)
    ydn = max(gap * 2.9, inf + gap * 1.9)
    pad_dn = ydn + (6 if bajo != 'nada' else 0)
    tit_h = 12 if titulo else 0
    h = tit_h + pad_up + 4 * gap + pad_dn

    def f(c, x, y, w):
        yy = y
        if titulo:
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, y - 8.5, titulo)
            yy = y - tit_h
        top_y = yy - pad_up
        ys = draw_staff(c, x, top_y, w, gap)
        top, bot = ys[0], ys[-1]
        draw_barline(c, x, top, bot)
        cur = x + 4
        draw_clef(c, cur, bot, gap, clef)
        cur += gap * (5.4 if clef == 'treble' else 4.6)
        if ts:
            draw_time_sig(c, cur, bot, gap, top=str(ts[0]), bottom=str(ts[1]))
            cur += gap * 3.0
        slot = (x + w - 8 - cur) / float(n)
        for k, p in enumerate(notas):
            cx = cur + slot * (k + 0.5)
            if p is not None:
                if cabeza_sola:
                    draw_headless_note(c, cx, bot, top, gap, p, clef)
                else:
                    sd = plica[k] if plica else None
                    draw_note(c, cx, bot, top, gap, p, dur=dur if isinstance(dur, str) else dur[k],
                              stem_dir=sd, clef=clef)
            if encima and encima[k]:
                c.setFont('DejaVuSans-Bold', 8.2)
                c.setFillColor(NAVY_SOFT)
                cyn = note_y(bot, gap, p, clef) if p else top
                c.drawCentredString(cx, (top + gap * 2.1) if cyn <= top + 1 else (cyn + gap * 2.1), str(encima[k]))
            if bajo == 'linea':
                c.setStrokeColor(NAVY_SOFT)
                c.setLineWidth(0.6)
                ww = min(slot * 0.78, caja_ancho or 34)
                yl = bot - ydn
                c.line(cx - ww / 2, yl, cx + ww / 2, yl)
            elif isinstance(bajo, list) and bajo[k]:
                c.setFont('DejaVuSans-Bold', 8.6)
                c.setFillColor(NAVY)
                c.drawCentredString(cx, bot - ydn + 2, bajo[k])
            if barras and (k + 1) % barras == 0 and k + 1 < n:
                draw_barline(c, cur + slot * (k + 1), top, bot)
        draw_barline(c, x + w - 4, top, bot, final=True)
    return Blk(h, f)


def pauta_vacia(clef='treble', compases=2, ts=None, gap=GAP, ancho=CONTENT_W, titulo=None, key=None, alto_extra=0):
    tit_h = 13 if titulo else 0
    pad_up, pad_dn = gap * 3.6 + alto_extra, gap * 3.4
    h = tit_h + pad_up + 4 * gap + pad_dn

    def f(c, x, y, w):
        if titulo:
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, y - 8.5, titulo)
        top_y = y - tit_h - pad_up
        ys = draw_staff(c, x, top_y, w, gap)
        top, bot = ys[0], ys[-1]
        draw_barline(c, x, top, bot)
        cur = x + 4
        draw_clef(c, cur, bot, gap, clef)
        cur += gap * (5.4 if clef == 'treble' else 4.6)
        if ts:
            draw_time_sig(c, cur, bot, gap, top=str(ts[0]), bottom=str(ts[1]))
            cur += gap * 3.0
        av = x + w - 8 - cur
        for i in range(1, compases):
            draw_barline(c, cur + av * i / compases, top, bot)
        draw_barline(c, x + w - 4, top, bot, final=True)
    return Blk(h, f)


def pauta_piano_vacia(compases=2, ts=None, gap=GAP, titulo=None):
    """Sistema de piano en blanco: sol + fa unidos por una llave."""
    tit_h = 13 if titulo else 0
    sep = gap * 6.4
    h = tit_h + gap * 3.0 + 4 * gap + sep + 4 * gap + gap * 2.6

    def f(c, x, y, w):
        if titulo:
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, y - 8.5, titulo)
        ty = y - tit_h - gap * 3.0
        by = ty - 4 * gap - sep
        for clef, top_y in (('treble', ty), ('bass', by)):
            ys = draw_staff(c, x, top_y, w, gap)
            draw_clef(c, x + 4, ys[-1], gap, clef)
            cur = x + 4 + gap * (5.4 if clef == 'treble' else 4.6)
            if ts:
                draw_time_sig(c, cur, ys[-1], gap, top=str(ts[0]), bottom=str(ts[1]))
                cur += gap * 3.0
            av = x + w - 8 - cur
            for i in range(1, compases):
                draw_barline(c, cur + av * i / compases, ys[0], ys[-1])
            draw_barline(c, x + w - 4, ys[0], ys[-1], final=True)
        c.setStrokeColor(INK)
        c.setLineWidth(1.6)
        c.line(x, ty, x, by - 4 * gap)
        c.setLineWidth(0.8)
        c.line(x, ty, x, by - 4 * gap)
    return Blk(h, f)


# ------------------------------------------------------------------ compases con huecos
BEATS = {'w': 4.0, 'h': 2.0, 'q': 1.0, 'e': 0.5, 's': 0.25, 'h.': 3.0, 'q.': 1.5, 'e.': 0.75, 'w.': 6.0}


def fila_compases(compases, ts=(4, 4), clef='treble', gap=GAP, titulo=None, final=True, pitch='B4',
                  contar=False, ancho_rel=None, nota_bajo=None, caja_hueco=True, rotulos=None):
    """Compases dibujados con figuras y/o silencios y/o huecos.
       compases: lista de compases; cada compas = lista de items:
         ('n', dur[, pitch])  nota          ('r', dur) silencio     ('x', beats)  hueco para que el alumno escriba
       Las corcheas seguidas dentro de un mismo tiempo se unen con barra.
       rotulos: texto bajo cada compas (p. ej. 'faltan 2 tiempos') o None."""
    tit_h = 12 if titulo else 0
    pad_up, pad_dn = gap * 3.8, gap * 3.2 + (11 if (rotulos or contar) else 0)
    h = tit_h + pad_up + 4 * gap + pad_dn
    bpb = ts[0] * 4.0 / ts[1] if ts else 4.0

    def f(c, x, y, w):
        if titulo:
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, y - 8.5, titulo)
        top_y = y - tit_h - pad_up
        ys = draw_staff(c, x, top_y, w, gap)
        top, bot = ys[0], ys[-1]
        draw_barline(c, x, top, bot)
        cur = x + 4
        draw_clef(c, cur, bot, gap, clef)
        cur += gap * (5.4 if clef == 'treble' else 4.6)
        if ts:
            draw_time_sig(c, cur, bot, gap, top=str(ts[0]), bottom=str(ts[1]))
            cur += gap * 3.0
        nco = len(compases)
        av = x + w - 6 - cur
        pesos = ancho_rel or [1.0] * nco
        tot = float(sum(pesos))
        x0 = cur
        for k, comp in enumerate(compases):
            wk = av * pesos[k] / tot
            xi, xf = x0, x0 + wk
            total_b = sum((it[1] if it[0] == 'x' else BEATS[it[1]]) for it in comp)
            inner0, inner1 = xi + gap * 1.0, xf - gap * 1.0
            span = max(total_b, bpb)
            # posiciones x de cada item (centro de su "casilla" proporcional al valor, con raiz para no deformar)
            beat = 0.0
            pos = []
            for it in comp:
                b = it[1] if it[0] == 'x' else BEATS[it[1]]
                pos.append((beat, b))
                beat += b
            def xb(bt):
                return inner0 + (inner1 - inner0) * (bt / span)
            grupos = {}
            for idx, it in enumerate(comp):
                b0, bb = pos[idx]
                cxm = (xb(b0) + xb(b0 + bb)) / 2.0
                if it[0] == 'n':
                    p = it[2] if len(it) > 2 else pitch
                    sd = 'up'
                    if it[1] in ('e', 's'):
                        grupos.setdefault(int(b0 + 1e-6), []).append((idx, cxm, p))
                    else:
                        cx, cy, _ = draw_note(c, min(cxm, xb(b0) + (xb(b0 + bb) - xb(b0)) * 0.5), bot, top, gap, p,
                                              dur=it[1], stem_dir=sd, clef=clef)
                elif it[0] == 'r':
                    draw_rest(c, min(cxm, xb(b0) + gap * 0.9) if it[1] in ('q', 'e') else cxm, bot, top, gap, it[1])
                elif it[0] == 'x':
                    ww = max(gap * 2.2, xb(b0 + bb) - xb(b0) - gap * 0.7)
                    c.setStrokeColor(OCRE)
                    c.setLineWidth(0.9)
                    c.setDash(2, 2)
                    c.roundRect(xb(b0) + gap * 0.2, bot - gap * 0.1, ww, 4 * gap + 0.2 * gap, 3, fill=0, stroke=1)
                    c.setDash()
            for bt, g in grupos.items():
                g.sort()
                if len(g) >= 2 and all(comp[i][1] in ('e', 's') for i, _, _ in g):
                    ys_ = [note_y(bot, gap, p, clef) for _, _, p in g]
                    endy = max(ys_) + gap * 3.4
                    for (i, cxm, p), cy in zip(g, ys_):
                        draw_note(c, cxm, bot, top, gap, p, dur=comp[i][1], stem_dir='up', beam_to=True, clef=clef,
                                  stem_end_y=endy)
                    draw_beam(c, g[0][1] + gap * 0.6, endy, g[-1][1] + gap * 0.6, endy, gap=gap)
                    if all(comp[i][1] == 's' for i, _, _ in g):
                        draw_beam(c, g[0][1] + gap * 0.6, endy - gap * 0.62, g[-1][1] + gap * 0.6, endy - gap * 0.62, gap=gap)
                else:
                    for i, cxm, p in g:
                        draw_note(c, cxm, bot, top, gap, p, dur=comp[i][1], stem_dir='up', clef=clef)
            if k + 1 < nco:
                draw_barline(c, xf, top, bot)
            if rotulos and rotulos[k]:
                c.setFont('DejaVuSans', 7.4)
                c.setFillColor(MUTED)
                c.drawCentredString((xi + xf) / 2.0, bot - gap * 2.3 - 6, rotulos[k])
            if contar:
                pass
            x0 = xf
        draw_barline(c, x + w - 4, top, bot, final=final)
    return Blk(h, f)


# ------------------------------------------------------------------ figuras sueltas (referencia)
FIG = {  # nombre: (banderas, cabeza llena, con plica, tiempos, texto del valor)
    'w': (0, False, False, 4.0, '4 tiempos'), 'h': (0, False, True, 2.0, '2 tiempos'),
    'q': (0, True, True, 1.0, '1 tiempo'), 'e': (1, True, True, 0.5, '½ tiempo'),
    's': (2, True, True, 0.25, '¼ de tiempo'), 'f': (3, True, True, 0.125, '⅛ de tiempo'),
    'g': (4, True, True, 0.0625, '1/16 de tiempo'),
}
NOM_FIG = {'w': 'Redonda', 'h': 'Blanca', 'q': 'Negra', 'e': 'Corchea', 's': 'Semicorchea', 'f': 'Fusa', 'g': 'Semifusa'}
NOM_SIL = {'w': 'Silencio de redonda', 'h': 'Silencio de blanca', 'q': 'Silencio de negra', 'e': 'Silencio de corchea',
           's': 'Silencio de semicorchea', 'f': 'Silencio de fusa', 'g': 'Silencio de semifusa'}


def figura(c, cx, cy, gap, d, linea=True, dot=False):
    """Una figura aislada sobre una raya de pentagrama (cabeza en la linea)."""
    nf, lleno, plica, _, _ = FIG[d.rstrip('.')]
    if linea:
        c.setStrokeColor(GRAY_L)
        c.setLineWidth(0.8)
        c.line(cx - gap * 1.6, cy, cx + gap * 1.6, cy)
    draw_notehead(c, cx, cy, gap, filled=lleno)
    if plica:
        sx = cx + gap * 0.6
        top = cy + gap * (3.4 + 0.95 * max(0, nf - 2))
        c.setStrokeColor(INK)
        c.setLineWidth(max(1.3, gap * 0.115))
        c.line(sx, cy, sx, top)
        for k in range(nf):
            fy = top - k * gap * 0.9
            c.setFillColor(INK)
            p = c.beginPath()
            p.moveTo(sx, fy)
            p.curveTo(sx + gap * 0.15, fy - gap * 0.25, sx + gap * 0.95, fy - gap * 0.05, sx + gap * 0.68, fy - gap * 1.25)
            p.curveTo(sx + gap * 0.62, fy - gap * 0.85, sx + gap * 0.22, fy - gap * 0.55, sx, fy - gap * 0.35)
            p.close()
            c.drawPath(p, fill=1, stroke=0)
    if dot:
        c.setFillColor(INK)
        c.circle(cx + gap * 1.05, cy + gap * 0.15 + (gap * 0.5 if False else 0), gap * 0.14, fill=1, stroke=0)


GRAY_L = HexColor('#9AA0AA')


def silencio(c, cx, cy, gap, d, linea=True):
    """Silencio aislado; cy = linea central del 'pentagrama' de referencia (5 lineas finas)."""
    if linea:
        c.setStrokeColor(GRAY_L)
        c.setLineWidth(0.7)
        for k in range(-2, 3):
            c.line(cx - gap * 1.7, cy + k * gap, cx + gap * 1.7, cy + k * gap)
    base = cy - 2 * gap
    if d in ('f', 'g'):
        c.setFillColor(INK)
        c.setFont('FreeSerif', gap * 2.6)
        c.drawCentredString(cx, cy - gap * 0.6 - (gap * 0.55 if d == 'f' else gap * 1.0),
                            '\U0001D140' if d == 'f' else '\U0001D141')
    else:
        draw_rest(c, cx, base, cy + 2 * gap, gap, d)


# ------------------------------------------------------------------ teclado
BLANCAS = 'CDEFGAB'
TIENE_NEGRA = {'C': 'C#', 'D': 'D#', 'F': 'F#', 'G': 'G#', 'A': 'A#'}


def teclado(c, x, y, w, h, desde=('C', 4), n_blancas=8, marcas=None, rotulos=None, cajas=None,
            etiqueta_blancas=False, do_central=False, tam_fuente=8.0, color_marca=None, negras_rotulo=None,
            contorno=NAVY, grosor=0.9):
    """Dibuja un teclado. y = borde de ABAJO. Las teclas se identifican por 'C4', 'C#4', 'D#4'...
       marcas: {tecla: color} pinta la tecla. rotulos: {tecla: texto} texto dentro de la tecla.
       cajas: set de teclas que llevan una casilla en blanco para escribir su nombre."""
    marcas = marcas or {}
    rotulos = rotulos or {}
    cajas = cajas or set()
    kw = w / float(n_blancas)
    letra0, oct0 = desde
    i0 = BLANCAS.index(letra0)
    teclas = []
    for i in range(n_blancas):
        L = BLANCAS[(i0 + i) % 7]
        o = oct0 + (i0 + i) // 7
        teclas.append((L, o, x + i * kw))
    for L, o, xx in teclas:
        k = '%s%d' % (L, o)
        c.setFillColor(marcas.get(k, BLANCO))
        c.setStrokeColor(contorno)
        c.setLineWidth(grosor)
        c.roundRect(xx, y, kw, h, 3, fill=1, stroke=1)
    for L, o, xx in teclas:
        k = '%s%d' % (L, o)
        if etiqueta_blancas:
            c.setFont('DejaVuSans-Bold', tam_fuente)
            c.setFillColor(INK)
            c.drawCentredString(xx + kw / 2, y + 6, NOMBRE[L])
        if k in rotulos:
            c.setFont('DejaVuSans-Bold', tam_fuente)
            c.setFillColor(INK)
            c.drawCentredString(xx + kw / 2, y + 6, rotulos[k])
        if k in cajas:
            c.setFillColor(BLANCO)
            c.setStrokeColor(NAVY_SOFT)
            c.setLineWidth(0.6)
            c.roundRect(xx + kw * 0.12, y + 4, kw * 0.76, 13, 2, fill=1, stroke=1)
    for L, o, xx in teclas[:-1] if n_blancas else []:
        pass
    for idx, (L, o, xx) in enumerate(teclas):
        if L in TIENE_NEGRA and idx + 1 < len(teclas):
            k = '%s#%d' % (L, o)
            bw, bh = kw * 0.58, h * 0.62
            bx = xx + kw - bw / 2
            c.setFillColor(marcas.get(k, INK))
            c.setStrokeColor(contorno)
            c.setLineWidth(0.7)
            c.roundRect(bx, y + h - bh, bw, bh, 2, fill=1, stroke=1)
            if k in rotulos:
                c.setFont('DejaVuSans-Bold', tam_fuente - 1.2)
                c.setFillColor(BLANCO if marcas.get(k) is None else INK)
                c.drawCentredString(bx + bw / 2, y + h - bh + 6, rotulos[k])
            if k in cajas:
                c.setFillColor(BLANCO)
                c.setStrokeColor(NAVY_SOFT)
                c.setLineWidth(0.6)
                c.roundRect(bx + bw * 0.1, y + h - bh + 5, bw * 0.8, 11, 2, fill=1, stroke=1)
    if do_central:
        for L, o, xx in teclas:
            if L == 'C' and o == 4:
                c.setFillColor(OCRE)
                c.circle(xx + kw / 2, y + 21, 3.4, fill=1, stroke=0)


def bloque_teclado(w=CONTENT_W, h=70, titulo=None, **kw):
    th = 12 if titulo else 0

    def f(c, x, y, ww):
        if titulo:
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, y - 8.5, titulo)
        teclado(c, x + (CONTENT_W - w) / 2.0, y - th - h - 4, w, h, **kw)
    return Blk(th + h + 12, f)


# ------------------------------------------------------------------ soluciones
SOLUCIONES = []           # (mes, num_ejercicio, titulo, [lineas])


def sol(mes, num, titulo, lineas_):
    SOLUCIONES.append((mes, num, titulo, lineas_ if isinstance(lineas_, list) else [lineas_]))


# ------------------------------------------------------------------ utilidades de azar reproducible
def rnd(sem):
    return random.Random(sem)


# ------------------------------------------------------------------ tablas, unir, casillas, lineas
def tabla(anchos, filas, cabecera=None, size=8.8, alto=19, zebra=True, alin=None, alto_cab=18, negrita_1=False):
    """Tabla sobria. anchos en puntos (suman <= CONTENT_W). Cada celda: str (admite **negrita**) o
       callable(c, cx, cy, w, h) para dibujar un simbolo. alin: lista 'c'/'l' por columna."""
    nf = len(filas)
    alin = alin or ['c'] * len(anchos)
    altos = []
    for fila in filas:
        hh = alto
        for ce, wc in zip(fila, anchos):
            if isinstance(ce, str):
                n = len(lineas(ce, wc - 10, size))
                hh = max(hh, n * size * 1.35 + 9)
        altos.append(hh)
    h = (alto_cab if cabecera else 0) + sum(altos) + 4

    def f(c, x, y, w):
        yy = y
        if cabecera:
            c.setFillColor(NAVY)
            c.roundRect(x, yy - alto_cab, sum(anchos), alto_cab, 3, fill=1, stroke=0)
            xx = x
            for tx, wc in zip(cabecera, anchos):
                c.setFillColor(BLANCO)
                c.setFont('DejaVuSans-Bold', 7.6)
                c.drawCentredString(xx + wc / 2, yy - alto_cab + 6, tx.upper())
                xx += wc
            yy -= alto_cab
        for r, (fila, hh) in enumerate(zip(filas, altos)):
            if zebra and r % 2 == 0:
                c.setFillColor(PANEL)
                c.rect(x, yy - hh, sum(anchos), hh, fill=1, stroke=0)
            c.setStrokeColor(RULE)
            c.setLineWidth(0.5)
            c.line(x, yy - hh, x + sum(anchos), yy - hh)
            xx = x
            for k, (ce, wc) in enumerate(zip(fila, anchos)):
                if callable(ce):
                    ce(c, xx + wc / 2, yy - hh / 2, wc, hh)
                elif ce:
                    ls = lineas(ce, wc - 10, size)
                    th = len(ls) * size * 1.35
                    if alin[k] == 'c':
                        pinta_lineas(c, ls, xx + 5, yy - (hh - th) / 2 + 0.6, size, size * 1.35, INK, centrado_w=wc - 10)
                    else:
                        pinta_lineas(c, ls, xx + 7, yy - (hh - th) / 2 + 0.6, size, size * 1.35, INK)
                xx += wc
            yy -= hh
    return Blk(h + 8, f)


def casillas(textos, cols=1, size=9.0):
    """Lista de comprobacion con casillas ☐."""
    filas = [textos[i:i + cols] for i in range(0, len(textos), cols)]
    cw = CONTENT_W / cols
    hs = []
    for fila in filas:
        hs.append(max(len(lineas(t, cw - 24, size)) for t in fila) * size * 1.4 + 6)

    def f(c, x, y, w):
        yy = y
        for fila, hh in zip(filas, hs):
            for k, t in enumerate(fila):
                xx = x + k * cw
                c.setStrokeColor(NAVY)
                c.setLineWidth(0.9)
                c.roundRect(xx + 2, yy - 11.5, 10, 10, 2, fill=0, stroke=1)
                pinta_lineas(c, lineas(t, cw - 24, size), xx + 20, yy, size, size * 1.4, INK)
            yy -= hh
    return Blk(sum(hs) + 6, f)


def lineas_escribir(n, etiqueta=None, sep=20, ancho=None):
    h = n * sep + (13 if etiqueta else 0) + 4

    def f(c, x, y, w):
        yy = y
        if etiqueta:
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, yy - 8.5, etiqueta)
            yy -= 13
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        for k in range(n):
            c.line(x, yy - (k + 1) * sep + 5, x + (ancho or w), yy - (k + 1) * sep + 5)
    return Blk(h, f)


def une(izq, der, alto=26, titulo=None, w=CONTENT_W, izq_w=110, der_w=210, sufijo=None, hueco=90):
    """Unir con lineas: izq y der son listas (str o callable(c,cx,cy,w,h)); dos columnas con punto.
       sufijo: texto tras la columna derecha (p. ej. 'tiempos') precedido de una raya para escribir."""
    n = len(izq)
    th = 13 if titulo else 0
    h = th + n * alto + 6

    def f(c, x, y, ww):
        if titulo:
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, y - 8.5, titulo)
        xl = x + 6
        xd_l = xl + izq_w + 6
        xd_r = xd_l + hueco
        for k in range(n):
            cy = y - th - k * alto - alto / 2.0
            it = izq[k]
            if callable(it):
                it(c, xl + izq_w / 2.0, cy, izq_w, alto)
            else:
                c.setFont('DejaVuSans', 9)
                c.setFillColor(INK)
                c.drawCentredString(xl + izq_w / 2.0, cy - 3, it)
            c.setFillColor(NAVY)
            c.circle(xd_l, cy, 3.1, fill=1, stroke=0)
            c.circle(xd_r, cy, 3.1, fill=1, stroke=0)
            it = der[k]
            if callable(it):
                it(c, xd_r + 10 + der_w / 2.0, cy, der_w, alto)
            else:
                c.setFont('DejaVuSans', 9.2)
                c.setFillColor(INK)
                c.drawString(xd_r + 10, cy - 3.2, it)
            if sufijo:
                xs = xd_r + 10 + der_w + 14
                c.setStrokeColor(NAVY_SOFT)
                c.setLineWidth(0.6)
                c.line(xs, cy - 4, xs + 40, cy - 4)
                c.setFont('DejaVuSans', 8.6)
                c.setFillColor(MUTED)
                c.drawString(xs + 46, cy - 3.2, sufijo)
    return Blk(h, f)


def posicion(p, clef='treble'):
    """Nombre del sitio que ocupa la nota en el pentagrama: '2.ª línea', '1.er espacio', ..."""
    ref = _abs_idx('E4') if clef == 'treble' else _abs_idx('G2')
    i = _abs_idx(p) - ref
    ordl = {1: '1.ª', 2: '2.ª', 3: '3.ª', 4: '4.ª', 5: '5.ª'}
    ords = {1: '1.er', 2: '2.º', 3: '3.er', 4: '4.º'}
    if 0 <= i <= 8:
        return ('%s línea' % ordl[i // 2 + 1]) if i % 2 == 0 else ('%s espacio' % ords[(i - 1) // 2 + 1])
    if i > 8:
        k = i - 8
        return ('espacio sobre la 5.ª línea' if k == 1 else '%s línea adicional superior' % ordl[(k + 1) // 2]
                if k % 2 == 0 else 'espacio sobre la %s adicional' % ordl[k // 2])
    k = -i
    return ('espacio bajo la 1.ª línea' if k == 1 else '%s línea adicional inferior' % ordl[k // 2]
            if k % 2 == 0 else 'espacio bajo la %s adicional' % ordl[k // 2])


# ------------------------------------------------------------------ utilidades musicales
def mover(p, k):
    """Altura k pasos diatonicos (naturales) por encima (k>0) o por debajo de p."""
    i = _abs_idx(p) + k
    return LETRAS[i % 7] + str(i // 7)


def fila_pares(clef, pares, gap=GAP, titulo=None):
    """Pares de notas (negras) seguidas; bajo cada par, una casilla para dibujar la flecha (↑ ↓ =)."""
    cys = [note_y(0.0, gap, p, clef) for par_ in pares for p in par_]
    sup = max([cy - 4 * gap for cy in cys] + [0])
    inf = max([-cy for cy in cys] + [0])
    pad_up = max(gap * 2.0, sup + gap * 1.4)
    pad_dn = max(gap * 2.6, inf + gap * 1.6) + 20
    tit = 12 if titulo else 0
    h = tit + pad_up + 4 * gap + pad_dn

    def f(c, x, y, w):
        if titulo:
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, y - 8.5, titulo)
        ys = draw_staff(c, x, y - tit - pad_up, w, gap)
        top, bot = ys[0], ys[-1]
        draw_barline(c, x, top, bot)
        draw_clef(c, x + 4, bot, gap, clef)
        cur = x + 4 + gap * (5.4 if clef == 'treble' else 4.6)
        slot = (x + w - 8 - cur) / float(len(pares))
        for k, (a, b) in enumerate(pares):
            cx = cur + slot * (k + 0.5)
            draw_note(c, cx - gap * 1.5, bot, top, gap, a, 'q', clef=clef)
            draw_note(c, cx + gap * 1.5, bot, top, gap, b, 'q', clef=clef)
            c.setStrokeColor(NAVY_SOFT)
            c.setLineWidth(0.7)
            c.roundRect(cx - 13, bot - pad_dn + 4, 26, 15, 3, fill=0, stroke=1)
            if k + 1 < len(pares):
                draw_barline(c, cur + slot * (k + 1), top, bot)
        draw_barline(c, x + w - 4, top, bot, final=True)
    return Blk(h, f)


def gran_pauta_notas(treble, bass, gap=GAP, titulo=None, nombres=None, linea_nombre=True, dur='w'):
    """Sistema de piano con una nota por columna en cada clave (None = hueco para dibujarla).
       Debajo del pentagrama de fa, una raya para escribir el nombre."""
    n = len(treble)
    sep = gap * 8.2
    tit = 12 if titulo else 0
    h = tit + gap * 3.2 + 4 * gap + sep + 4 * gap + gap * 5.4 + (10 if linea_nombre else 0)

    def f(c, x, y, w):
        if titulo:
            c.setFont('DejaVuSans-Bold', 8.2)
            c.setFillColor(NAVY_SOFT)
            c.drawString(x, y - 8.5, titulo)
        ty = y - tit - gap * 3.2
        by = ty - 4 * gap - sep
        cur0 = x + 4 + gap * 5.4
        slot = (x + w - 8 - cur0) / float(n)
        for clef, top_y, notas in (('treble', ty, treble), ('bass', by, bass)):
            ys = draw_staff(c, x, top_y, w, gap)
            draw_clef(c, x + 4, ys[-1], gap, clef)
            for k, p in enumerate(notas):
                cx = cur0 + slot * (k + 0.5)
                if p:
                    draw_note(c, cx, ys[-1], ys[0], gap, p, dur, clef=clef)
            draw_barline(c, x + w - 4, ys[0], ys[-1], final=True)
        c.setStrokeColor(INK)
        c.setLineWidth(1.4)
        c.line(x, ty, x, by - 4 * gap)
        if linea_nombre:
            for k in range(n):
                cx = cur0 + slot * (k + 0.5)
                c.setStrokeColor(NAVY_SOFT)
                c.setLineWidth(0.6)
                c.line(cx - 14, by - 4 * gap - gap * 4.4, cx + 14, by - 4 * gap - gap * 4.4)
    return Blk(h, f)
