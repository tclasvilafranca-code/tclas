# -*- coding: utf-8 -*-
"""Constructor generico de UN dosier de cancion: todas las hojas de una vez.

   Cada cancion pasa a ser un unico archivo de datos (`dilan_NN_*.py`) con un
   diccionario CANCION; aqui esta todo el fontanero. Asi el trabajo por
   cancion es medir la partitura, verificar a zoom y escribir el contenido,
   que es lo unico que no se puede automatizar.

   Estructura (rediseno pedido por el cliente):
       partitura · ficha · calentamiento de dedos · agudeza visual ·
       como se estudia (x2) · soltando dedos · papel pautado

   Dos de esas hojas ya no se escriben a mano: el calentamiento de dedos y la
   agudeza visual son hojas LLENAS de pentagramas generadas
   (engine/generador_lectura.py) a partir de la tonalidad de la pieza, con el
   numero de cancion como semilla y con el nivel subiendo a lo largo del
   curso. La hoja de la cancion 7 es siempre la misma, pero no se parece a la
   de la 6.

   La regla dura del proyecto sigue en pie: lo generado DERIVA (no lleva
   numeros de compas) y las hojas al piano CITAN compases literales con su
   numero. Nada puede estar en las dos. Se comprueba con audit_duplicados().
"""
import os
import random
import sys
import zlib

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'engine'))

import segno
from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader

import portada
from portada import W, H
from ficha_info import build_ficha
from hoja_calentamiento import build_calentamiento
from hoja_lectura import build_lectura
from hoja_piano import build_piano
from hoja_relax import build_relax
from hoja_pauta import build_pauta
from hoja_taller import build_taller
from hoja_deberes import build_deberes
from tareas_semana import tarea as tarea_semana
from audit_suite import run_full_audit, audit_text_bounds, audit_duplicados

HERE = os.path.dirname(__file__)
OUT_DIR = os.path.join(HERE, '..', 'output')

# Compases que el generador sabe escribir. Si la pieza va en otro, se usa 4/4
# de base y se juega con el resto igual.
COMPASES = [(4, 4), (3, 4), (2, 4), (6, 8)]

# Por donde entra cada alumno en las hojas generadas, segun su nivel. Un
# alumno avanzado no puede empezar el curso leyendo negras y blancas: se
# aburre en la primera hoja y no vuelve a mirarlas.
NIVEL_BASE = {'iniciación': 0, 'iniciacion': 0, 'intermedio': 1, 'avanzado': 1}


def _nivel_lectura(cfg):
    """El nivel de las hojas generadas sube a lo largo del curso.

       0 = negras y blancas · 1 = corcheas, puntillos y silencios ·
       2 = todo el repertorio y registro ancho, con lineas adicionales.
       Cada alumno entra por donde le toca (`nivel_base`) y sube cada siete
       canciones, que es mas o menos un trimestre."""
    if cfg.get('nivel_lectura') is not None:
        return cfg['nivel_lectura']
    base = cfg.get('nivel_base')
    if base is None:
        base = NIVEL_BASE.get(str(cfg.get('nivel', '')).lower(), 0)
    return min(2, base + (cfg['num'] - 1) // 7)


# Alumnos cuyo album YA esta entregado: su sal se congela para que reimprimir
# una hoja suelta siga dando exactamente la misma hoja que tienen impresa. Un
# alumno nuevo no entra aqui; se le calcula la sal y ya no se toca.
SAL_CONGELADA = {'dilan': 0}


def _sal_alumno(alumno):
    """Un desplazamiento fijo por alumno para las hojas generadas.

       Sin esto, dos alumnos que trabajan la misma cancion en el mismo numero
       reciben EXACTAMENTE la misma hoja de calentamiento y de agudeza — y eso
       pasa de verdad: Eva comparte quince partituras con Dilan, byte a byte.

       crc32 y no hash(), que en Python va con sal aleatoria por proceso: la
       hoja tiene que salir igual en cada ejecucion, porque la promesa del
       cuaderno es que se puede reimprimir una hoja suelta y el alumno se
       encuentra la misma."""
    clave = alumno.strip().lower()
    if clave in SAL_CONGELADA:
        return SAL_CONGELADA[clave]
    return zlib.crc32(clave.encode('utf-8')) % 90000


def _mezcla_compases(time_sig, semilla):
    """El compas de la pieza manda, pero no es el unico.

       De cada siete lineas, cuatro van en el compas de la pieza (que es el
       que hay que interiorizar) y tres en otros, rotando. Asi el alumno no se
       acostumbra a contar siempre hasta cuatro, que es el motivo por el que
       un 3/4 se le atraganta en marzo."""
    ts = tuple(time_sig)
    if ts not in COMPASES:
        ts = (4, 4)
    otros = [t for t in COMPASES if t != ts]
    random.Random(semilla).shuffle(otros)
    return [ts, ts, otros[0], ts, otros[1], ts, otros[2]]


def _hojas_corto(cfg, qr_png):
    """El dosier CORTO, para clases de media hora (Arnau, 10 anos).

       partitura · ficha · taller (dedos + leer en una hoja) · como se estudia
       (una hoja, o dos si la pieza lo pide) · deberes + pentagramas

       No es el formato largo recortado: el taller junta en una hoja lo que
       alli son dos, y la ultima hoja junta los deberes con el papel pautado.
       Con media hora de clase, ocho hojas por cancion no se miran."""
    kicker = '%s · canción %d · %s' % (cfg['alumno'], cfg['num'], cfg['titulo_corto'])
    nivel = '%s · canción %d · %s' % (cfg['alumno'], cfg['num'], cfg['nivel'])
    sem = cfg['num'] + _sal_alumno(cfg['alumno'])
    nl = _nivel_lectura(cfg)
    p0 = _paginas_partitura(cfg)

    ficha = dict(cfg['ficha'])
    ficha.update(kicker=nivel, page_num=p0 + 1, time_sig=cfg['time_sig'])
    ficha['qr'] = dict(ficha['qr']); ficha['qr']['png'] = qr_png

    tal = dict(cfg.get('taller') or {})
    tal.update(kicker=kicker, page_num=p0 + 2, time_sig=cfg['time_sig'],
               key_sig=cfg.get('key_sig'), gap=tal.get('gap', 6.6),
               semilla=sem, nivel_lectura=nl,
               compases_extra=cfg.get('compases_extra')
               or _mezcla_compases(cfg['time_sig'], 5000 + sem),
               compases_extra_leer=cfg.get('compases_extra_leer')
               or _mezcla_compases(cfg['time_sig'], 6000 + sem))

    hojas = [('ficha', lambda c: build_ficha(c, ficha)),
             ('taller', lambda c: build_taller(c, tal))]

    pag = p0 + 3
    pianos = [cfg['piano1']] + ([cfg['piano2']] if cfg.get('piano2') else [])
    for i, bruto in enumerate(pianos):
        p = dict(bruto)
        p.update(kicker=kicker, page_num=pag, time_sig=cfg['time_sig'],
                 key_sig=cfg.get('key_sig'), gap=p.get('gap', 7.0),
                 esquina=p.get('esquina', 'Cómo se aprende esta canción'),
                 titulo=p.get('titulo', 'Cómo se estudia'))
        hojas.append(('piano %d' % (i + 1), (lambda q: lambda c: build_piano(c, q))(p)))
        pag += 1

    # Los deberes van ESCRITOS y hay una hoja por semana: la pieza se trabaja
    # dos semanas, asi que salen dos hojas, cada una con sus ejercicios.
    for i, bruto in enumerate(cfg.get('deberes') or []):
        deb = dict(bruto)
        deb.update(kicker=kicker, page_num=pag)
        hojas.append(('deberes %d' % (i + 1),
                      (lambda q: lambda c: build_deberes(c, q))(deb)))
        pag += 1
    return hojas


def _hojas_adulto(cfg, qr_png):
    """El dosier de ADULTO, seis hojas (Jose Maria, unos 60 anos, empezo hace
       poco; viene a clase y practica en casa con su teclado).

       partitura · ficha · dedos · leer · como se estudia (una hoja, o dos si
       la pieza lo pide) · el trabajo de la semana · papel pautado

       Decision del cliente: dedos y lectura en hojas SEPARADAS, no fundidas
       como en el formato corto. Y nada infantil: los ejercicios son los
       mismos de siempre, pero la hoja de la semana lleva plan de minutos por
       dia y tabla de metronomo: es lo que se lleva de la clase para los dias
       que hay en medio."""
    kicker = '%s · pieza %d · %s' % (cfg['alumno'], cfg['num'], cfg['titulo_corto'])
    nivel = '%s · pieza %d · %s' % (cfg['alumno'], cfg['num'], cfg['nivel'])
    sem = cfg['num'] + _sal_alumno(cfg['alumno'])
    nl = _nivel_lectura(cfg)
    p0 = _paginas_partitura(cfg)

    ficha = dict(cfg['ficha'])
    ficha.update(kicker=nivel, page_num=p0 + 1, time_sig=cfg['time_sig'])
    ficha['qr'] = dict(ficha['qr']); ficha['qr']['png'] = qr_png

    cal = dict(cfg.get('calentamiento') or {})
    cal.update(kicker=kicker, page_num=p0 + 2, time_sig=cfg['time_sig'],
               key_sig=cfg.get('key_sig'), gap=cal.get('gap_lectura', 6.6),
               semilla=sem, nivel_lectura=nl,
               compases_extra=cfg.get('compases_extra')
               or _mezcla_compases(cfg['time_sig'], 5000 + sem))

    lec = dict(cfg.get('agudeza') or {})
    lec.update(kicker=kicker, page_num=p0 + 3, time_sig=cfg['time_sig'],
               key_sig=cfg.get('key_sig'), gap=lec.get('gap_lectura', 6.6),
               semilla=sem, nivel_lectura=nl,
               compases_extra=cfg.get('compases_extra_leer')
               or _mezcla_compases(cfg['time_sig'], 6000 + sem))

    hojas = [('ficha', lambda c: build_ficha(c, ficha)),
             ('dedos', lambda c: build_calentamiento(c, cal)),
             ('leer', lambda c: build_lectura(c, lec))]

    pag = p0 + 4
    pianos = [cfg['piano1']] + ([cfg['piano2']] if cfg.get('piano2') else [])
    for i, bruto in enumerate(pianos):
        p = dict(bruto)
        p.update(kicker=kicker, page_num=pag, time_sig=cfg['time_sig'],
                 key_sig=cfg.get('key_sig'), gap=p.get('gap', 7.0),
                 esquina=p.get('esquina', 'Al piano · el orden de estudio'),
                 titulo=p.get('titulo', 'Cómo se estudia'))
        hojas.append(('piano %d' % (i + 1), (lambda q: lambda c: build_piano(c, q))(p)))
        pag += 1

    for i, bruto in enumerate(cfg.get('trabajo') or []):
        tr = dict(bruto)
        tr.update(kicker=kicker, page_num=pag)
        hojas.append(('trabajo %d' % (i + 1),
                      (lambda q: lambda c: build_deberes(c, q))(tr)))
        pag += 1

    pau = dict(cfg.get('pauta') or {})
    pau.update(kicker=kicker, page_num=pag)
    hojas.append(('pauta', lambda c: build_pauta(c, pau)))
    return hojas


def _hojas(cfg, qr_png):
    """Las hojas del dosier, ya con el kicker y la numeracion puestos."""
    if cfg.get('formato') == 'corto':
        return _hojas_corto(cfg, qr_png)
    if cfg.get('formato') == 'adulto':
        return _hojas_adulto(cfg, qr_png)
    kicker = '%s · canción %d · %s' % (cfg['alumno'], cfg['num'], cfg['titulo_corto'])
    nivel = '%s · canción %d · nivel %s' % (cfg['alumno'], cfg['num'], cfg['nivel'])
    num = cfg['num']
    sem = num + _sal_alumno(cfg['alumno'])       # semilla propia de cada alumno
    nl = _nivel_lectura(cfg)
    p0 = _paginas_partitura(cfg)

    ficha = dict(cfg['ficha'])
    ficha.update(kicker=nivel, page_num=p0 + 1, time_sig=cfg['time_sig'])
    ficha['qr'] = dict(ficha['qr']); ficha['qr']['png'] = qr_png

    cal = dict(cfg['calentamiento'])
    cal.update(kicker=kicker, page_num=p0 + 2, time_sig=cfg['time_sig'],
               key_sig=cfg.get('key_sig'), gap=cal.get('gap_lectura', 6.6),
               semilla=sem, nivel_lectura=nl,
               compases_extra=cfg.get('compases_extra')
               or _mezcla_compases(cfg['time_sig'], 5000 + sem))

    lec = dict(cfg['agudeza'])
    lec.update(kicker=kicker, page_num=p0 + 3, time_sig=cfg['time_sig'],
               key_sig=cfg.get('key_sig'), gap=lec.get('gap_lectura', 6.6),
               semilla=sem, nivel_lectura=nl,
               compases_extra=cfg.get('compases_extra_leer')
               or _mezcla_compases(cfg['time_sig'], 6000 + sem))

    # El titulo y la esquina salen del archivo de la cancion si estan puestos:
    # el orden de estudio no es el mismo en todas las piezas y ponerle a todas
    # "por partes / montarla" era justo lo que no se entendia.
    p1 = dict(cfg['piano1'])
    p1.update(kicker=kicker, page_num=p0 + 4, time_sig=cfg['time_sig'],
              key_sig=cfg.get('key_sig'), gap=p1.get('gap', 7.0),
              esquina=p1.get('esquina', 'Al piano · el orden de estudio'),
              titulo=p1.get('titulo', 'Cómo se estudia'))

    p2 = dict(cfg['piano2'])
    p2.update(kicker=kicker, page_num=p0 + 5, time_sig=cfg['time_sig'],
              key_sig=cfg.get('key_sig'), gap=p2.get('gap', 7.0),
              esquina=p2.get('esquina', 'Al piano · el orden de estudio'),
              titulo=p2.get('titulo', 'Cómo se estudia (sigue)'))

    rlx = dict(cfg.get('relax') or {})
    rlx.update(kicker=kicker, page_num=p0 + 6, key_sig=cfg.get('key_sig'),
               semilla=sem)
    # La tarea escrita de la semana (norma de variedad): rota por pieza, asi
    # que el alumno no se encuentra el mismo recuadro las 20 semanas. Si la
    # cancion trae la suya escrita a mano, manda la suya.
    rlx.setdefault('tarea', tarea_semana(cfg['alumno'], cfg['num']))

    pau = dict(cfg.get('pauta') or {})
    pau.update(kicker=kicker, page_num=p0 + 7)

    return [('ficha', lambda c: build_ficha(c, ficha)),
            ('calentamiento', lambda c: build_calentamiento(c, cal)),
            ('agudeza', lambda c: build_lectura(c, lec)),
            ('piano 1', lambda c: build_piano(c, p1)),
            ('piano 2', lambda c: build_piano(c, p2)),
            ('relax', lambda c: build_relax(c, rlx)),
            ('pauta', lambda c: build_pauta(c, pau))]


_CACHE_PAGS = {}

# Dosieres montados sin su partitura original (el PDF del cliente no esta en
# el repositorio). Se anota para poder avisar al final en vez de fallar.
SIN_PARTITURA = []

SUELO_AUDIT = {'ficha': 33}


def _paginas_partitura(cfg):
    """Cuantas paginas ocupa la partitura original. La numeracion de las hojas
       arranca donde acaba ella; antes estaba escrita a mano (siempre 4) y en
       las piezas de dos paginas el numero no coincidia con la hoja."""
    if cfg.get('paginas_partitura'):
        return cfg['paginas_partitura']
    ruta = cfg.get('partitura')
    if not ruta:
        return 2
    if ruta not in _CACHE_PAGS:
        try:
            _CACHE_PAGS[ruta] = len(PdfReader(ruta).pages)
        except Exception:
            # Las partituras originales no estan en el repositorio (son del
            # cliente). Sin ellas se sigue pudiendo generar y auditar todo lo
            # que escribimos nosotros; solo el numero de pagina es aproximado.
            _CACHE_PAGS[ruta] = 2
    return _CACHE_PAGS[ruta]


def construir(cfg, verificar=True):
    """Genera el dosier completo (partitura + hojas) y devuelve su ruta."""
    os.makedirs(OUT_DIR, exist_ok=True)
    qr = os.path.join(OUT_DIR, '_qr_%s.png' % cfg['slug'])
    segno.make(cfg['yt'], error='m').save(qr, scale=10, border=2,
                                          dark='#1A2332', light='#F3F1EA')
    hojas = _hojas(cfg, qr)

    tmp = os.path.join(HERE, '_tmp_%s.pdf' % cfg['slug'])
    c = canvas.Canvas(tmp, pagesize=(W, H))
    for _, fn in hojas:
        fn(c)
    c.save()

    wr = PdfWriter()
    if os.path.exists(cfg['partitura']):
        for p in PdfReader(cfg['partitura']).pages:
            wr.add_page(p)
    else:
        SIN_PARTITURA.append(cfg['slug'])
    for p in PdfReader(tmp).pages:
        wr.add_page(p)
    # El nombre del archivo sale del alumno, y hay alumnos con espacios y
    # acentos ("José María"): se limpia, o el PDF acaba llamandose
    # "José María_01_...pdf" y no casa con los demas.
    quien = cfg.get('carpeta') or cfg['alumno']
    out = os.path.join(OUT_DIR, '%s_%02d_%s_CUADERNO.pdf'
                       % (quien, cfg['num'], cfg['slug']))
    with open(out, 'wb') as f:
        wr.write(f)
    os.remove(tmp)
    os.remove(qr)

    if verificar:
        auditar(cfg)
    return out


def auditar(cfg):
    """Las cuatro comprobaciones obligatorias. Imprime lo que falle."""
    qr = os.path.join(OUT_DIR, '_qr_a_%s.png' % cfg['slug'])
    segno.make(cfg['yt'], error='m').save(qr, scale=10, border=2,
                                          dark='#1A2332', light='#F3F1EA')
    hojas = _hojas(cfg, qr)
    fallos = _revisar(hojas, cfg['slug'])
    os.remove(qr)
    return fallos


def auditar_hojas(hojas, etiqueta):
    """La misma revision para cuadernos montados a mano (los que no pasan por
       construir(), como las dos primeras canciones de Dilan)."""
    return _revisar(hojas, etiqueta)


def _revisar(hojas, etiqueta):
    fallos = []
    for nombre, fn in hojas:
        ov = audit_text_bounds(fn, 595.276, 841.89, 549.28)
        if ov:
            fallos.append('%s: texto fuera del margen -> %s' % (nombre, ov[:2]))
        # Y el otro desbordamiento, el que no ve el auditor de margenes: un
        # texto que se sale de SU CAJA aunque este dentro de la pagina. Lo
        # apunta `_fit` cuando ni al tamano minimo cabe.
        del portada.NO_CABEN[:]
        fn(_lienzo())
        if portada.NO_CABEN:
            fallos.append('%s: texto que no cabe en su hueco -> %s'
                          % (nombre, portada.NO_CABEN[:3]))
        calls, probs = _music(fn)
        for p in probs:
            if 'not a whole number of bars' in p:
                fallos.append('%s: %s' % (nombre, p))
        y = _altura(fn)
        # El pie de pagina escribe con la base en 26 y sube unos 7 pt, asi que
        # 34 es el limite real. En las hojas de pentagrama se deja mas aire
        # (44) porque ahi lo que baja son plicas y lineas adicionales, que el
        # calculo de altura no siempre ve; en la ficha lo ultimo es un recuadro
        # con el borde medido, y ahi 34 es exacto.
        suelo = SUELO_AUDIT.get(nombre, 44)
        if y is not None and y < suelo:
            fallos.append('%s: la pagina se pasa por abajo (y=%.1f)' % (nombre, y))
        # Una hoja que acaba a media pagina esta a medio hacer. El auditor de
        # margenes la daba por buena y salian calentamientos con un tercio de
        # hoja en blanco: el listón es el de Arnau, que llena el 97-99%.
        if y is not None and y > 132:
            fallos.append('%s: la hoja se queda corta, sobran %.0f pt de hoja '
                          '(y=%.1f) -> falta material' % (nombre, y - 60, y))
    ident, parc = audit_duplicados(hojas)
    if ident:
        fallos.append('material IDENTICO entre hojas: %s' % (ident[:2],))
    if parc:
        fallos.append('solape >=8 notas entre hojas: %s' % (parc[:3],))
    print(('  %s: OK' % etiqueta) if not fallos else
          ('  %s: %d FALLOS\n    %s' % (etiqueta, len(fallos),
                                        '\n    '.join(fallos))))
    return fallos


def _music(fn):
    from audit_suite import audit_music
    return audit_music(fn)


def _lienzo():
    """Un lienzo de usar y tirar, para las comprobaciones que solo necesitan
       ejecutar el dibujo y mirar lo que quedo apuntado."""
    return canvas.Canvas(os.devnull, pagesize=(W, H))


def _altura(fn):
    """La y en la que acaba la hoja: por debajo de ~44 pisa el pie de pagina.
       build_ficha no devuelve y (su layout es en dos columnas), asi que ahi
       la comprobacion la hace el chequeo de pixeles."""
    c = canvas.Canvas(os.devnull, pagesize=(W, H))
    return fn(c)
