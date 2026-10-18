# -*- coding: utf-8 -*-
"""Dosier de Sharifa (12 anys): tema en CATALA, mes alegre, amb en Mussol Misol.

   Es activa quan ALUMNA != 'eva' (`mayores_motor` el carrega abans de res).  Fa dues coses:
   1) canvia la paleta (indigo, taronja, turquesa, rosa...) respectant la mateixa estructura;
   2) tradueix les cadenes FIXES del motor (capcaleres, etiquetes, textos per defecte) al
      catala en el moment de dibuixar: coincidencia exacta o per prefix. El text propi de cada
      peca (`ms_NN_*.py`) ja s'escriu en catala i passa sense canvis.
   Eva no es toca: amb ALUMNA='eva' aquest modul no fa res.
"""
import os
import re

ACTIU = os.environ.get('ALUMNA', 'eva') != 'eva'

# ------------------------------------------------------------------ paleta
PAL = dict(
    NAVY='#2F2B5C', NAVY_SOFT='#6E69C4', CREAM='#FFFCF6', RULE='#D7D2EE', INK='#26233A',
    MUTED='#7B7791', ACCENT='#D9731F', BLUE='#3F8FD2', PANEL='#F2EFFC', WARM='#FFF1D6',
    OCRE='#E8704F', AZUL='#3F8FD2', VERDE='#2FA39A', ROJO='#E04F6B', MORADO='#8A63D2',
    GRIS='#D8D3EE')
BLOQUES = ['#3F8FD2', '#E8704F', '#8A63D2', '#2FA39A', '#E04F6B', '#E09A1F', '#4C6FD1',
           '#C45AA0', '#5BA55B']

# ------------------------------------------------------------------ traduccio
EXACTES = {
    'El Cuaderno del Pianista  ·  T-Clas': 'El Quadern del Pianista  ·  T-Clas',
    'Ficha de la partitura': 'Fitxa de la partitura',
    'Cómo estudiarla': 'Com estudiar-la',
    'Guía por bloques': 'Guia per blocs',
    'Papel pautado': 'Paper pautat',
    'Para escribir': 'Per escriure',
    'Mano izquierda y mano derecha': 'Mà esquerra i mà dreta',
    'Cada mano se aprende sola. Las dos juntas llegan al final, despacio.':
        "Cada mà s'aprèn sola. Les dues juntes arriben al final, a poc a poc.",
    'MANO IZQUIERDA': 'MÀ ESQUERRA', 'MANO DERECHA': 'MÀ DRETA', 'LAS DOS': 'LES DUES',
    'LOS DOS': 'ELS DOS', 'ESCUCHA': 'ESCOLTA', 'OJO': 'MUSSOL MISOL', 'SECONDO': 'SECONDO',
    'IZQUIERDA': 'ESQUERRA', 'DERECHA': 'DRETA', 'JUNTAS': 'JUNTES', 'A TEMPO': 'A TEMPO',
    'Muñeca suelta y hombros bajos: si te cansas, estás apretando.':
        'Canell solt i espatlles baixes: si et cansa, estàs fent força.',
    'Dedos curvos, cerca de las teclas, sonido ligero y parejo.':
        'Dits corbats, a prop de les tecles, so lleuger i regular.',
    'Cuenta en voz alta los golpes y no pares cuando cambie algo.':
        'Compta els temps en veu alta i no paris quan canviï alguna cosa.',
    'Cómo tocar cada bloque': 'Com tocar cada bloc',
    'Cada bloque, en el mismo orden: izquierda, derecha, juntas y a tempo.':
        'Cada bloc, en el mateix ordre: esquerra, dreta, juntes i a tempo.',
    'ANTES DE DECIR «YA LA SÉ»': 'ABANS DE DIR «JA ME LA SÉ»',
    'Toco de memoria la mano izquierda de los primeros bloques.':
        'Toco de memòria la mà esquerra dels primers blocs.',
    'Cuento los golpes y no me pierdo cuando algo cambia.':
        'Compto els temps i no em perdo quan alguna cosa canvia.',
    'Sé por dónde voy en la partitura, también en las repeticiones.':
        'Sé per on vaig a la partitura, també a les repeticions.',
    'Toco la pieza entera, de principio a fin, sin parar.':
        'Toco la peça sencera, del principi al final, sense parar.',
    'La grabo con el móvil y la escucho.': 'La gravo amb el mòbil i me l\'escolto.',
    'la clave la pones tú · copia un compás o inventa algo':
        'la clau la poses tu · copia un compàs o inventa alguna cosa',
    'la clave la pones tú · para copiar un compás, escribir la escala o inventarte algo':
        'la clau la poses tu · copia un compàs, escriu l\'escala o inventa alguna cosa',
    'LA CUENTA': 'EL COMPTE', 'Mapa de la pieza': 'Mapa de la peça',
    'Lo especial de esta partitura': 'Què té de especial aquesta partitura',
    'El reto': 'El repte', 'El truco': 'El truc d\'en Mussol Misol',
    '¿Sabías que…?': 'Sabies que…?', 'La pieza en cuatro ideas': 'La peça en quatre idees',
    'Un compás de cada mano': 'Un compàs de cada mà',
    'Un solo compás de ejemplo, para ver de un vistazo qué hace cada mano en esta pieza. '
    'MI = mano izquierda, MD = mano derecha.':
        'Un sol compàs d\'exemple, per veure d\'un cop d\'ull què fa cada mà. '
        'ME = mà esquerra, MD = mà dreta.',
    'Escúchala': 'Escolta-la', 'El Cuaderno': 'El Quadern',
    'T-CLAS  ·  DESPIERTA TU SONIDO INTERIOR': 'T-CLAS  ·  DESPERTA EL TEU SO INTERIOR',
    # llibre
    'Cómo usar el dosier': 'Com fer servir el dossier',
    'Cómo usar este dosier': 'Com fer servir aquest dossier',
    'Pensado para clases de media hora: una pieza cada dos semanas, de la más fácil a la más '
    'difícil.': 'Pensat per a classes de mitja hora: una peça cada dues setmanes, de la més fàcil '
                'a la més difícil.',
    'LAS HOJAS DE CADA PIEZA': 'LES FULLES DE CADA PEÇA',
    'UNA CLASE DE 30 MINUTOS': 'UNA CLASSE DE 30 MINUTS',
    'CÓMO LEER LA PARTITURA ANOTADA': 'COM LLEGIR LA PARTITURA ANOTADA',
    'Manos': 'Mans', 'La partitura': 'La partitura',
    'Los datos medidos (tonalidad, compás, tempo), el mapa de la pieza, el reto, el truco y un QR '
    'para escucharla.': 'Les dades mesurades (tonalitat, compàs, tempo), el mapa de la peça, el '
                        'repte, el truc i un QR per escoltar-la.',
    'Cuatro pasos para la mano izquierda y cuatro para la derecha, y la técnica en tres frases.':
        'Quatre passos per a la mà esquerra i quatre per a la dreta, i la tècnica en tres frases.',
    'La pieza partida en bloques: qué tocar, en qué orden y cómo juntar las manos.':
        'La peça partida en blocs: què tocar, en quin ordre i com ajuntar les mans.',
    'Tu partitura con los bloques en color y burbujas que explican qué practicar en cada sitio.':
        'La teva partitura amb els blocs en color i bombolles que expliquen què practicar a cada lloc.',
    'Para copiar un compás, escribir la escala o inventar.':
        'Per copiar un compàs, escriure l\'escala o inventar.',
    'Calentar': 'Escalfar', 'Bloque nuevo': 'Bloc nou', 'Tocar lo ya sabido': 'Tocar el que ja saps',
    'Deberes': 'Deures',
    'La mano izquierda del bloque de hoy, sola y despacio.':
        'La mà esquerra del bloc d\'avui, sola i a poc a poc.',
    'Izquierda, derecha y juntas, siguiendo la guía de bloques.':
        'Esquerra, dreta i juntes, seguint la guia de blocs.',
    'Los bloques anteriores y, si se puede, la pieza entera.':
        'Els blocs anteriors i, si es pot, la peça sencera.',
    'Una sola tarea para casa: la que marca la tarjeta del bloque.':
        'Una sola tasca per a casa: la que marca la targeta del bloc.',
    'El curso de un vistazo': 'El curs d\'un cop d\'ull',
    'Quince piezas de noviembre a julio, de menos a más dificultad. Una pieza cada dos semanas; '
    'las más largas pueden llevar un poco más.':
        'Quinze peces de novembre a juliol, de menys a més dificultat. Una peça cada dues '
        'setmanes; les més llargues poden portar una mica més.',
    'Mi registro': 'El meu registre',
    'Marca cada pieza cuando la tengas: por bloques, entera y a tempo.':
        'Marca cada peça quan la tinguis: per blocs, sencera i a tempo.',
    'Quince piezas · de menos a más · 30 minutos por clase':
        'Quinze peces · de menys a més · 30 minuts per classe',
    'Curso de noviembre a julio': 'Curs de novembre a juliol',
    'PIEZA': 'PEÇA', 'CUÁNDO': 'QUAN', 'NIVEL': 'NIVELL', 'PÁG.': 'PÀG.',
    'Bloques': 'Blocs', 'Entera': 'Sencera', 'Grabada': 'Gravada', 'Fecha': 'Data',
    'Nº': 'Nº', 'Cómo estudiarla ': 'Com estudiar-la',
}

# prefix llarg -> traduccio completa (paragrafs fixos)
PREFIXOS = [
    ('El paréntesis de color del margen izquierdo',
     'El parèntesi de color del marge esquerre i el seu número diuen en quin bloc ets. Les '
     'bombolles expliquen què practicar: «mà esquerra» i «mà dreta» (taronja i blau), «les dues», '
     '«Mussol Misol» (el seu consell, per no passar res per alt) i, als duets, «Primo» i '
     '«Secondo». Els requadres fins amb número emmarquen el més important: ratlla el número amb '
     'llapis quan el tinguis. Els acords es diuen com sempre (La menor, Sol major…); a sobre de '
     'algunes partitures surten en xifrat americà (A = La, B = Si, C = Do, D = Re, E = Mi, '
     'F = Fa, G = Sol).'),
]

_UP = {k.upper(): v.upper() for k, v in EXACTES.items() if k != k.upper()}

MESOS = {'Noviembre': 'Novembre', 'Diciembre': 'Desembre', 'Enero': 'Gener', 'Febrero': 'Febrer',
         'Marzo': 'Març', 'Abril': 'Abril', 'Mayo': 'Maig', 'Junio': 'Juny', 'Julio': 'Juliol'}


def tr(s):
    """Tradueix una cadena fixa; si no la coneix, la torna igual."""
    if not ACTIU or not isinstance(s, str) or not s:
        return s
    r = EXACTES.get(s)
    if r is not None:
        return r
    r = _UP.get(s)
    if r is not None:
        return r
    for pre, t in PREFIXOS:
        if s.startswith(pre):
            return t
    m = re.match(r'^LA TÉCNICA, EN (\w+) FRASES?$', s)
    if m:
        n = {'DOS': 'DUES', 'TRES': 'TRES', 'CUATRO': 'QUATRE', 'UNA': 'UNA'}.get(m.group(1), m.group(1))
        return 'LA TÈCNICA, EN %s FRASE%s' % (n, '' if m.group(1) == 'UNA' else 'S')
    m = re.match(r'^Cómo se cuenta el (\d+/\d+)$', s)
    if m:
        return 'Com es compta el %s' % m.group(1)
    m = re.match(r'^Un compás de (\d+/\d+) contado en corcheas', s)
    if m:
        return ('Un compàs de %s comptat en corxeres. Aquí només el ritme, sobre una nota qualsevol: '
                'les altures, a la teva partitura.' % m.group(1))
    m = re.match(r'^DOSIER DE (\w+) · CURSO NOVIEMBRE - JULIO$', s)
    if m:
        return 'DOSSIER DE %s · CURS NOVEMBRE - JULIOL' % m.group(1)
    m = re.match(r'^(\w+) · (.*)$', s)           # 'Marzo · 1.ª quincena'
    if m and m.group(1) in MESOS:
        return '%s · %s' % (MESOS[m.group(1)], m.group(2).replace('.ª quincena', '.a quinzena'))
    if s in MESOS:
        return MESOS[s]
    u = EXACTES.get(s.capitalize())
    if u is not None and s.isupper():
        return u.upper()
    return s


def _tr_up(s):
    """Versio per a textos que el motor posa en majuscules (kicker, titulo.upper())."""
    return s


def instalar():
    """Parcheja el canvas i el _wrap de portada. Es crida una sola vegada, abans dels imports."""
    if not ACTIU:
        return
    from reportlab.pdfgen import canvas as _cv
    import portada
    from reportlab.lib.colors import HexColor

    for nom in ('NAVY', 'NAVY_SOFT', 'CREAM', 'RULE', 'INK', 'MUTED', 'ACCENT', 'PANEL'):
        setattr(portada, nom, HexColor(PAL[nom]))
    portada.BLUE = HexColor(PAL['BLUE'])

    for m in ('drawString', 'drawCentredString', 'drawRightString'):
        orig = getattr(_cv.Canvas, m)

        def nou(self, x, y, text, *a, _o=orig, **k):
            t = tr(text)
            return _o(self, x, y, t, *a, **k)
        setattr(_cv.Canvas, m, nou)

    w0 = portada._wrap

    def wrap(c, text, *a, **k):
        return w0(c, tr(text), *a, **k)
    portada._wrap = wrap


def post_imports():
    """Colors dels moduls que els redefineixen (ficha_info, hoja_pauta) un cop importats."""
    if not ACTIU:
        return
    from reportlab.lib.colors import HexColor
    import ficha_info
    for nom, k in (('BLUE', 'BLUE'), ('WARM', 'WARM'), ('PANEL', 'PANEL')):
        setattr(ficha_info, nom, HexColor(PAL[k]))
    for nom in ('NAVY', 'NAVY_SOFT', 'CREAM', 'INK', 'MUTED', 'ACCENT'):
        if hasattr(ficha_info, nom):
            setattr(ficha_info, nom, HexColor(PAL[nom]))
    if hasattr(ficha_info, '_wrap'):
        import portada
        ficha_info._wrap = portada._wrap
    try:
        import hoja_pauta
        for nom in ('NAVY', 'NAVY_SOFT', 'CREAM', 'INK', 'MUTED', 'ACCENT', 'PANEL'):
            if hasattr(hoja_pauta, nom):
                setattr(hoja_pauta, nom, HexColor(PAL[nom]))
        if hasattr(hoja_pauta, '_wrap'):
            import portada
            hoja_pauta._wrap = portada._wrap
    except ImportError:
        pass


# ------------------------------------------------------------------ en Mussol Misol
_IMG = {}
_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'pekes_owl')


def buho(c, x, y, alto, pose='normal'):
    """El mussol amb la cantonada inferior esquerra a (x, y). Torna l'amplada."""
    from reportlab.lib.utils import ImageReader
    if pose not in _IMG:
        _IMG[pose] = ImageReader(os.path.join(_DIR, 'owl_%s_color.png' % pose))
    iw, ih = _IMG[pose].getSize()
    amp = alto * iw / float(ih)
    c.drawImage(_IMG[pose], x, y, amp, alto, mask='auto')
    return amp


def _linies(txt, w, font, size):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    out, cur = [], ''
    for p in txt.split():
        t = (cur + ' ' + p).strip()
        if stringWidth(t, font, size) > w and cur:
            out.append(cur)
            cur = p
        else:
            cur = t
    if cur:
        out.append(cur)
    return out


def alto_caixa_misol(w, txt, alto_buho=46.0, size=8.8):
    amp = alto_buho * 0.82
    n = len(_linies(txt, w - amp - 44, 'DejaVuSans', size))
    return max(alto_buho + 14, 26 + 11.6 * n)


def caixa_misol(c, x, y, w, txt, pose='normal', alto_buho=46.0, size=8.8):
    """Bombolla d'en Mussol Misol: mussol a l'esquerra, consell dins d'un globus. y = part
       superior. Torna la y de la base."""
    from reportlab.lib.colors import HexColor, white
    amp = alto_buho * 0.82
    h = alto_caixa_misol(w, txt, alto_buho, size)
    c.setFillColor(HexColor(PAL['WARM']))
    c.setStrokeColor(HexColor(PAL['ACCENT']))
    c.setLineWidth(1.1)
    c.roundRect(x, y - h, w, h, 9, fill=1, stroke=1)
    buho(c, x + 10, y - h + (h - alto_buho) / 2.0, alto_buho, pose)
    tx = x + 10 + amp + 16
    # cua del globus cap al mussol
    p = c.beginPath()
    p.moveTo(tx - 4, y - h / 2.0 + 6)
    p.lineTo(tx - 12, y - h / 2.0)
    p.lineTo(tx - 4, y - h / 2.0 - 6)
    c.setFillColor(HexColor(PAL['WARM']))
    c.setStrokeColor(HexColor(PAL['WARM']))
    c.drawPath(p, fill=1, stroke=1)
    c.setFillColor(HexColor(PAL['ACCENT']))
    c.setFont('DejaVuSans-Bold', 7.8)
    c.drawString(tx, y - 16, "EN MUSSOL MISOL DIU")
    c.setFont('DejaVuSans', size)
    c.setFillColor(HexColor(PAL['NAVY']))
    yy = y - 29
    for l in _linies(txt, w - amp - 44, 'DejaVuSans', size):
        c.drawString(tx, yy, l)
        yy -= 11.6
    return y - h
