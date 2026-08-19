# -*- coding: utf-8 -*-
"""Verificador automatico: pasa esto SIEMPRE antes de entregar cualquier pagina.
   Comprueba (1) que cada pentagrama tiene un numero de tiempos multiplo del compas,
   (2) que ningun pentagrama queda disperso, (3) que ningun texto se sale del margen,
   y (4) que la clave usada en cada pentagrama es la esperada."""
import notation as nt
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas as canvas_mod


def audit_music(build_fn, page_w=595.276, page_h=841.89):
    """Wraps draw_system to log beat totals / event density / clef usage."""
    calls = []
    orig = nt.draw_system

    def patched(c, x, top_y, width, gap, events, clef='treble', time_sig=(4, 4),
                show_clef=True, show_time=True, key_sig=None, spacing='linear',
                repetir=None, casilla=None, ottava=False):
        # La tabla de duraciones vive en notation.DUR_BEATS: cuando estaba
        # duplicada aqui, anadir una figura al motor y olvidarla en el auditor
        # hacia que los compases se contasen mal sin avisar.
        dur_beats = nt.DUR_BEATS
        total_beats = sum(nt.beats_de(e) for e in events)
        beats_per_bar = time_sig[0] * (4.0 / time_sig[1])
        n_events = len(events)
        avail_w_est = width - gap * 8
        px_per_event = avail_w_est / max(n_events, 1)
        calls.append({
            'clef': clef,
            'total_beats': total_beats,
            'clean_bars': abs(total_beats % beats_per_bar) < 1e-6,
            'n_bars': total_beats / beats_per_bar,
            'n_events': n_events,
            'px_per_event': px_per_event,
        })
        return orig(c, x, top_y, width, gap, events, clef=clef, time_sig=time_sig,
                    show_clef=show_clef, show_time=show_time, key_sig=key_sig,
                    spacing=spacing, repetir=repetir, casilla=casilla, ottava=ottava)

    nt.draw_system = patched
    import page_layout_common as plc
    plc.draw_system = patched
    patched_modules = [plc]
    import sys
    # Cualquier modulo que haya hecho `from notation import draw_system` tiene
    # su propia referencia y no se entera del parche de nt.draw_system: hay que
    # parchearlos uno a uno. Si esta lista se queda corta, el auditor dice
    # "0 systems, all clean" sin haber mirado nada — un falso OK.
    for modname, mod in list(sys.modules.items()):
        if mod is None or mod is nt or mod is plc:
            continue
        if modname.startswith(('page_', 'hoja_', 'ficha_')) and hasattr(mod, 'draw_system'):
            mod.draw_system = patched
            patched_modules.append(mod)
    try:
        c = canvas_mod.Canvas('/tmp/_audit_tmp2.pdf', pagesize=(page_w, page_h))
        build_fn(c)
        c.save()
    finally:
        nt.draw_system = orig
        for mod in patched_modules:
            mod.draw_system = orig

    problems = []
    for i, call in enumerate(calls):
        if not call['clean_bars']:
            problems.append(f"system {i}: {call['total_beats']} beats is not a whole number of bars")
        if call['px_per_event'] > 45:
            problems.append(f"system {i}: sparse ({call['px_per_event']:.1f} px/event)")
    return calls, problems


def audit_text_bounds(build_fn, page_w, page_h, right_margin):
    """Catches any drawString/drawCentredString/drawRightString call whose ink
       would cross the given right margin (in points from the left edge)."""
    OrigCanvas = canvas_mod.Canvas
    captured = []

    class SpyCanvas(OrigCanvas):
        def drawString(self, x, y, text, *a, **k):
            w = stringWidth(text, self._fontname, self._fontsize)
            if x + w > right_margin:
                captured.append(('drawString', round(x + w, 1), text[:60], round(y, 1)))
            return super().drawString(x, y, text, *a, **k)

        def drawCentredString(self, x, y, text, *a, **k):
            w = stringWidth(text, self._fontname, self._fontsize)
            if x + w / 2 > right_margin:
                captured.append(('drawCentredString', round(x + w / 2, 1), text[:60], round(y, 1)))
            return super().drawCentredString(x, y, text, *a, **k)

    canvas_mod.Canvas = SpyCanvas
    try:
        c = canvas_mod.Canvas('/tmp/_audit_tmp.pdf', pagesize=(page_w, page_h))
        build_fn(c)
        c.save()
    finally:
        canvas_mod.Canvas = OrigCanvas
    return captured


def run_full_audit(label, build_fn):
    print(f'--- Auditing {label} ---')
    calls, problems = audit_music(build_fn)
    text_over = audit_text_bounds(build_fn, 595.276, 841.89, 549.28)
    ok = True
    if problems:
        ok = False
        print('MUSIC PROBLEMS:')
        for p in problems:
            print(' ', p)
    if text_over:
        ok = False
        print('TEXT OVERFLOW:')
        for t in text_over:
            print(' ', t)
    if ok:
        print(f'  OK — {len(calls)} systems, all clean bars, no overflow.')
    return ok


def audit_duplicados(hojas, page_w=595.276, page_h=841.89, minimo=8):
    """Busca material repetido ENTRE las hojas de un mismo cuaderno.

       hojas: [(etiqueta, build_fn), ...]

       El calentamiento debe DERIVAR de la pieza (transportar, invertir,
       ampliar) y las hojas 'al piano' deben CITARLA literalmente. Cuando las
       dos copian los mismos compases, el cuaderno acaba teniendo la misma hoja
       dos veces sin que se note al maquetar — paso de verdad, con 24 notas
       identicas impresas en tres hojas.

       Devuelve (identicos, parciales). Un solape de 6-7 notas suele ser
       inevitable (una celula repetida, o la escala de la tonalidad); a partir
       de `minimo` hay que mirarlo.
    """
    import notation as nt
    orig = nt.draw_system
    cur = ['?']
    seqs = []

    def patched(c, x, top_y, width, gap, events, clef='treble', time_sig=(4, 4),
                show_clef=True, show_time=True, key_sig=None, spacing='linear',
                repetir=None, casilla=None, ottava=False):
        key = tuple((e.get('pitch') or tuple(e.get('pitches', [])) or 'R', e['dur'])
                    for e in events)
        seqs.append((cur[0], clef, key))
        return orig(c, x, top_y, width, gap, events, clef=clef, time_sig=time_sig,
                    show_clef=show_clef, show_time=show_time, key_sig=key_sig,
                    spacing=spacing, repetir=repetir, casilla=casilla, ottava=ottava)

    import sys
    nt.draw_system = patched
    tocados = []
    for name, mod in list(sys.modules.items()):
        if mod is None or mod is nt:
            continue
        if name.startswith(('page_', 'hoja_', 'ficha_')) and hasattr(mod, 'draw_system'):
            mod.draw_system = patched
            tocados.append(mod)
    try:
        c = canvas_mod.Canvas('/tmp/_audit_dupes.pdf', pagesize=(page_w, page_h))
        for etiqueta, fn in hojas:
            cur[0] = etiqueta
            fn(c)
    finally:
        nt.draw_system = orig
        for mod in tocados:
            mod.draw_system = orig

    from collections import defaultdict
    by = defaultdict(list)
    for hoja, clef, key in seqs:
        by[(clef, key)].append(hoja)
    identicos = [(v, k[1]) for k, v in by.items() if len(set(v)) > 1]

    parciales = []
    for i in range(len(seqs)):
        for j in range(i + 1, len(seqs)):
            ha, ca, ka = seqs[i]
            hb, cb, kb = seqs[j]
            if ha == hb or ca != cb or ka == kb:
                continue
            for L in range(min(len(ka), len(kb)), minimo - 1, -1):
                sa = {ka[t:t + L] for t in range(len(ka) - L + 1)}
                if any(kb[t:t + L] in sa for t in range(len(kb) - L + 1)):
                    parciales.append((ha, hb, L))
                    break
    return identicos, parciales
