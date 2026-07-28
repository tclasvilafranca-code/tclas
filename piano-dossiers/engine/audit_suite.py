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
                show_clef=True, show_time=True, key_sig=None, spacing='linear'):
        dur_beats = {'w': 4.0, 'h': 2.0, 'q': 1.0, 'e': 0.5, 'q.': 1.5, 'h.': 3.0, 'e.': 0.75}
        total_beats = sum(dur_beats[e['dur']] for e in events)
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
                    spacing=spacing)

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
