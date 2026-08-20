# -*- coding: utf-8 -*-
"""Material de apoyo para las hojas "al piano", derivado de la propia pieza.

   POR QUE EXISTE. Al escribir las dos manos en su sistema de piano —sol arriba,
   fa abajo, que es como se lee el piano— el bloque de manos juntas dejo de
   caber con los demas y el cliente decidio darle una segunda hoja. Eso dejo 88
   piezas con las dos hojas a medio llenar, y el estandar del proyecto es claro:
   una hoja a medias no se entrega, se llena.

   QUE NO ES. No es relleno. Estas funciones NO inventan una melodia: construyen
   escalas, arpegios y giros SOBRE LA TONALIDAD DE LA PIEZA, que es material de
   tecnica de toda la vida y lo que un profesor escribiria a mano en el margen.
   Los rotulos —lo que se le pide al alumno y por que— se escriben a mano en
   cada pieza; aqui solo viven las notas, para que no se cuele una nota que no
   pertenece a la tonalidad.

   COMO SE USA. En el archivo de la cancion:

       from relleno import escala, arpegio, giro

       dict(num=4, titulo='...', pista='andamio en Sol mayor · ...',
            sistemas=[dict(cap='a) ...', events=escala('Sol mayor', 'G4'), bars=2)])

   La regla de no repetirse entre alumnos sigue vigente y la comprueba
   `cruzar_<alumno>.py`: por eso todas admiten `desde`, `sentido` y `figura`,
   que es lo que separa la escala de un alumno de la del de al lado.
"""
import re

# Los siete grados de cada tonalidad, en orden, con su alteracion escrita como
# la escribe el motor ('Bb4', 'F#4'). No se deduce de la armadura al vuelo
# porque las menores armonicas alteran el septimo grado y eso hay que decidirlo,
# no adivinarlo: aqui van las escalas NATURALES, y si una pieza necesita la
# sensible alterada se escribe a mano en su archivo.
GRADOS = {
    'Do mayor':  ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'Sol mayor': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
    'Re mayor':  ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
    'La mayor':  ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
    'Mi mayor':  ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
    'Fa mayor':  ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
    'Sib mayor': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
    'Mib mayor': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],
    'Lab mayor': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],
    'La menor':  ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Mi menor':  ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
    'Si menor':  ['B', 'C#', 'D', 'E', 'F#', 'G', 'A'],
    'Re menor':  ['D', 'E', 'F', 'G', 'A', 'Bb', 'C'],
    'Sol menor': ['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F'],
    'Do menor':  ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
    'Fa menor':  ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb'],
    'Fa# menor': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E'],
    'Do# menor': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
    'Re dórico': ['D', 'E', 'F', 'G', 'A', 'B', 'C'],
}

_ORDEN = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


def _parte(p):
    m = re.match(r'^([A-G])([b#]?)(-?\d+)$', str(p))
    if not m:
        raise ValueError('altura rara: %r' % (p,))
    return m.group(1), m.group(2), int(m.group(3))


def _sube(letra, octava, pasos):
    """Sube `pasos` grados diatonicos desde una letra, llevando la octava."""
    i = _ORDEN.index(letra) + pasos
    return _ORDEN[i % 7], octava + i // 7


def _en_tono(tono, letra, octava):
    """La misma letra con la alteracion que le toca en esa tonalidad."""
    for g in GRADOS[tono]:
        if g[0] == letra:
            return '%s%d' % (g, octava)
    return '%s%d' % (letra, octava)


def cuantas(time_sig, figura='q'):
    """Cuantas notas de esa figura llenan compases ENTEROS.

       Una escala de ocho negras cabe en 4/4 y en 2/4, pero en 3/4 deja el
       ultimo compas a medias y el auditor de compases lo canta —con razon: un
       ejercicio que no cierra el compas es un ejercicio mal escrito. Aqui se
       elige el numero que cuadra en cada compas."""
    bpb = time_sig[0] * (4.0 / time_sig[1])
    paso = {'q': 1.0, 'e': 0.5, 'h': 2.0}.get(figura, 1.0)
    # se busca el numero de notas MAS CERCANO A OCHO que cierra compases
    # enteros. No vale dividir y redondear: la blanca no cabe un numero entero
    # de veces en un compas de tres, y por ahi salian sistemas de dieciseis
    # tiempos en 3/4 que el auditor de compases cantaba, con razon.
    mejor = None
    for n in range(1, 33):
        if abs((n * paso) % bpb) < 1e-9:
            d = abs(n - 8)
            if mejor is None or d < mejor[0]:
                mejor = (d, n)
    return mejor[1] if mejor else 8



def tonica(tono, registro):
    """La tonica del tono, en la octava de `registro`.

       Los rotulos generados dicen "la escala de Sol mayor", "el acorde de Sol
       mayor desplegado", "el giro sobre la tonica". Si la nota de partida se
       pasa a mano, basta equivocarse de octava o de grado para que el papel
       diga una cosa y dibuje otra: paso de verdad, con un rotulo que anunciaba
       el acorde de Do mayor encima de un arpegio de Mi menor. Asi que el grado
       lo pone el tono y lo unico que se elige por fuera es el registro."""
    letra, _alt, octava = _parte(registro)
    return _en_tono(tono, GRADOS[tono][0][0], octava)


def escala(tono, desde, notas=8, sentido='sube', figura='q', **extra):
    """Los grados de la tonalidad, seguidos, desde la nota que se le diga.

       Es el ejercicio mas viejo que hay y sigue siendo el que mas arregla:
       coloca la mano en el tono de la pieza antes de tocarla."""
    letra, _alt, octava = _parte(desde)
    fuera = []
    for k in range(notas):
        paso = k if sentido == 'sube' else -k
        l, o = _sube(letra, octava, paso)
        fuera.append(dict(pitch=_en_tono(tono, l, o), dur=figura, **extra))
    return fuera


def arpegio(tono, desde, figura='q', ida_vuelta=True, notas=None, **extra):
    """El acorde de la tonalidad desplegado: 1-3-5-8 y de vuelta 8-5-3-1.

       Ocho notas justas, o sea dos compases de cuatro por cuatro, y cierra en
       la nota de partida: un arpegio que acaba colgando en el aire hace que el
       alumno acelere para terminar cuanto antes."""
    letra, _alt, octava = _parte(desde)
    subida = [_en_tono(tono, *_sube(letra, octava, paso)) for paso in (0, 2, 4, 7)]
    camino = subida + list(reversed(subida)) if ida_vuelta else subida
    if notas and notas != len(camino):
        # se recorta por donde tiene sentido musical, no cortando por lo sano:
        # 1-3-5-8-5-3 para seis, y repitiendo el camino entero si piden mas
        if notas == 6:
            camino = subida + list(reversed(subida[1:3]))
        elif notas == 9:
            camino = subida + list(reversed(subida))[1:] + [subida[1], subida[0]]
        else:
            camino = (camino * 3)[:notas]
    return [dict(pitch=p, dur=figura, **extra) for p in camino]


def giro(tono, centro, figura='q', notas=None, **extra):
    """El giro de siempre alrededor de una nota: la de arriba, la de abajo, y
       vuelta. Es lo que suelta un dedo agarrotado sin cambiar de posicion."""
    letra, _alt, octava = _parte(centro)
    arriba = _en_tono(tono, *_sube(letra, octava, 1))
    abajo = _en_tono(tono, *_sube(letra, octava, -1))
    c = _en_tono(tono, letra, octava)
    camino = [c, arriba, c, abajo, c, arriba, c, c]
    if notas:
        camino = (camino * 3)[:notas]
    return [dict(pitch=p, dur=figura, **extra) for p in camino]


def figura_compas(time_sig):
    """La figura que llena un compas entero: redonda en 4/4, blanca con
       puntillo en 3/4 y en 6/8, blanca en 2/4. Poner una redonda en un compas
       de tres es el fallo mas tonto y el mas facil de colar."""
    bpb = time_sig[0] * (4.0 / time_sig[1])
    return {4.0: 'w', 3.0: 'h.', 2.0: 'h', 1.5: 'q.', 6.0: 'w'}.get(round(bpb, 2), 'w')


def cadencia(tono, bajo, figura='w'):
    """I - IV - V - I en la mano izquierda, en estado fundamental.

       Los tres acordes que sostienen casi todo el repertorio del cuaderno.
       Saberlos de memoria en el tono de la pieza es lo que permite acompanar
       sin leer, y es teoria que se toca, no que se estudia."""
    letra, _alt, octava = _parte(bajo)
    fuera = []
    for grado in (0, 3, 4, 0):
        raiz_l, raiz_o = _sube(letra, octava, grado)
        notas = []
        for paso in (0, 2, 4):
            l, o = _sube(raiz_l, raiz_o, paso)
            notas.append(_en_tono(tono, l, o))
        fuera.append(dict(pitches=notas, dur=figura))
    return fuera


# ---------------------------------------------------------------- recetas
#
# Los bloques que llenan la segunda hoja de "Como se estudia". Se montan aqui y
# no a mano pieza por pieza por una razon de calidad, no de prisa: el texto de
# cada rotulo se construye con los datos REALES de la tonalidad (que grado lleva
# alteracion y cual es), asi que dice la verdad siempre. Escribiendo doscientos
# rotulos a mano, la nota equivocada acaba colandose.
#
# Lo que si se escribe a mano en cada pieza es el FOCO: la dificultad concreta
# de esa cancion, que es lo unico que el codigo no puede saber.

def _alteradas(tono):
    """Los grados con alteracion, en nombre de solfeo: [('Si', 'bemol'), ...]."""
    nombres = {'C': 'Do', 'D': 'Re', 'E': 'Mi', 'F': 'Fa',
               'G': 'Sol', 'A': 'La', 'B': 'Si'}
    fuera = []
    for g in GRADOS[tono]:
        if len(g) > 1:
            fuera.append((nombres[g[0]], 'bemol' if g[1] == 'b' else 'sostenido'))
    return fuera


def _frase_alteraciones(tono):
    alt = _alteradas(tono)
    if not alt:
        return 'no hay ni un sostenido ni un bemol: todo teclas blancas'
    if len(alt) == 1:
        return 'el único que cambia es el %s, que es %s' % (alt[0][0], alt[0][1])
    tipo = 'bemoles' if alt[0][1] == 'bemol' else 'sostenidos'
    return 'los que cambian son %s y %s, todos %s' % (
        ', '.join(a[0] for a in alt[:-1]), alt[-1][0], tipo)


# Cada receta son dos bloques. Rotan con el numero de pieza para que dos
# semanas seguidas no traigan el mismo esqueleto, que es la norma de variedad
# del proyecto aplicada tambien aqui.
RECETAS = ('escalas', 'acorde', 'cadencia', 'corcheas', 'mixta')


def _tercero(tono, agudo):
    """La tercera del tono, en el registro de la mano derecha."""
    letra, _alt, octava = _parte(agudo)
    raiz = GRADOS[tono][0][0]
    l, o = _sube(raiz, octava, 2)
    return _en_tono(tono, l, o)


def _quinto(tono, agudo):
    """La dominante del tono, en el registro de la mano derecha."""
    letra, _alt, octava = _parte(agudo)
    raiz = GRADOS[tono][0][0]
    l, o = _sube(raiz, octava, 4)
    return _en_tono(tono, l, o)


def bloques_extra(tono, num, agudo, grave, foco, receta=None, desde=90,
                  time_sig=(4, 4)):
    """Los bloques de apoyo de una pieza, ya montados.

       tono   · la tonalidad de la pieza, tal cual ('Sol mayor')
       num    · el numero de la pieza, para rotar la receta
       agudo  · donde empieza la mano derecha ('G4')
       grave  · donde empieza la izquierda ('G2')
       foco   · UNA frase escrita a mano: la dificultad concreta de la cancion
       desde  · numero del primer bloque nuevo
    """
    r = receta or RECETAS[num % len(RECETAS)]
    alt = _frase_alteraciones(tono)
    arriba = agudo[0] + str(int(agudo[-1]) + 1) if agudo[-1].isdigit() else agudo
    # cuantas notas y que figura cuadran en ESTE compas: una escala de ocho
    # negras deja el ultimo compas a medias en 3/4, y una redonda no cabe en un
    # compas de tres. Se calcula, no se supone.
    agudo = tonica(tono, agudo)      # el rotulo dice la tonica: que lo sea
    nq = cuantas(time_sig, 'q')
    ne = cuantas(time_sig, 'e')
    fc = figura_compas(time_sig)
    bpb = time_sig[0] * (4.0 / time_sig[1])
    cq = max(1, int(round(nq / bpb)))
    ce = max(1, int(round(ne * 0.5 / bpb)))

    if r == 'escalas':
        return [
            dict(num=desde, titulo='La escala de %s, para colocar la mano' % tono,
                 pista='andamio en %s · %s' % (tono, alt),
                 sistemas=[
                     dict(cap='a) los siete grados y la octava · %s' % foco,
                          events=escala(tono, agudo, notas=nq), bars=cq),
                     dict(cap='b) y de vuelta abajo · si alguna alteración se te escapa, '
                              'es aquí donde pasa',
                          events=escala(tono, arriba, sentido='baja', notas=nq),
                          bars=cq, show_time=False),
                 ]),
            dict(num=desde + 1, titulo='Los tres acordes que la sostienen',
                 pista='andamio en %s · la armonía de la pieza, reducida a lo esencial' % tono,
                 sistemas=[
                     dict(cap='a) I - IV - V - I, una redonda cada uno · apréndelos de memoria '
                              'y luego búscalos en tu partitura',
                          events=cadencia(tono, grave, figura=fc), bars=4, clef='bass'),
                     dict(cap='b) y el de V desplegado, que es el que empuja de vuelta al primero '
                              '· tócalo y para: se oye solo que pide volver',
                          events=arpegio(tono, _quinto(tono, agudo), notas=nq),
                          bars=cq, show_time=False),
                 ]),
        ]
    if r == 'acorde':
        return [
            dict(num=desde, titulo='El acorde de %s, desplegado' % tono,
                 pista='andamio en %s · las notas del acorde, una detrás de otra' % tono,
                 sistemas=[
                     dict(cap='a) sube y baja sin pararse en la cima · %s' % foco,
                          events=arpegio(tono, agudo, notas=nq), bars=cq),
                     dict(cap='b) y el mismo acorde empezando por su tercera · las notas son las '
                              'mismas y la mano se coloca distinto, que es de lo que se trata',
                          events=arpegio(tono, _tercero(tono, agudo), notas=nq),
                          bars=cq, show_time=False),
                 ]),
            dict(num=desde + 1, titulo='El giro que suelta la mano',
                 pista='andamio en %s · sin mover la mano de sitio' % tono,
                 sistemas=[
                     dict(cap='a) alrededor de la tónica · las cuatro notas del mismo peso',
                          events=giro(tono, agudo, notas=nq), bars=cq),
                     dict(cap='b) y un grado más arriba · si la muñeca se levanta, estás '
                              'empujando en vez de dejar caer',
                          events=giro(tono, arriba, notas=nq), bars=cq, show_time=False),
                 ]),
        ]
    if r == 'cadencia':
        return [
            dict(num=desde, titulo='Los acordes, con la izquierda sola',
                 pista='andamio en %s · lo que hace la izquierda casi toda la pieza' % tono,
                 sistemas=[
                     dict(cap='a) I - IV - V - I · %s' % foco,
                          events=cadencia(tono, grave, figura=fc), bars=4, clef='bass'),
                     dict(cap='b) y el de V desplegado con la derecha · es el acorde que pide '
                              'volver al principio',
                          events=arpegio(tono, _quinto(tono, agudo), notas=nq),
                          bars=cq, show_time=False),
                 ]),
            dict(num=desde + 1, titulo='Y la escala por encima',
                 pista='andamio en %s · %s' % (tono, alt),
                 sistemas=[
                     dict(cap='a) bajando desde arriba, que es por donde se escapan',
                          events=escala(tono, arriba, sentido='baja', notas=nq), bars=cq),
                     dict(cap='b) y subiendo otra vez · es el mismo camino al revés, y no sale '
                              'igual de bien: por eso se hacen los dos',
                          events=escala(tono, agudo, notas=nq), bars=cq, show_time=False),
                 ]),
        ]
    if r == 'corcheas':
        return [
            dict(num=desde, titulo='La escala en corcheas, sin aflojar',
                 pista='andamio en %s · aquí lo que se trabaja es aguantar, no leer' % tono,
                 sistemas=[
                     dict(cap='a) ocho corcheas seguidas, todas del mismo peso · %s' % foco,
                          events=escala(tono, agudo, figura='e', notas=ne), bars=ce),
                     dict(cap='b) y bajando · si la última suena más floja, has empezado a '
                              'frenar antes de tiempo',
                          events=escala(tono, arriba, sentido='baja', figura='e', notas=ne),
                          bars=ce, show_time=False),
                 ]),
            dict(num=desde + 1, titulo='El acorde, para descansar la mano',
                 pista='andamio en %s · después de correr, abrir' % tono,
                 sistemas=[
                     dict(cap='a) el acorde desplegado, sube y baja',
                          events=arpegio(tono, agudo, notas=nq), bars=cq),
                 ]),
        ]
    # 'mixta'
    return [
        dict(num=desde, titulo='El acorde y el giro, seguidos',
             pista='andamio en %s · %s' % (tono, alt),
             sistemas=[
                 dict(cap='a) el acorde desplegado · %s' % foco,
                      events=arpegio(tono, agudo, notas=nq), bars=cq),
                 dict(cap='b) y el giro sobre la tónica, sin mover la mano',
                      events=giro(tono, agudo, notas=nq), bars=cq, show_time=False),
             ]),
        dict(num=desde + 1, titulo='Los acordes con la izquierda',
             pista='andamio en %s · la armonía de la pieza en cuatro acordes' % tono,
             sistemas=[
                 dict(cap='a) I - IV - V - I, una redonda cada uno',
                      events=cadencia(tono, grave, figura=fc), bars=4, clef='bass'),
                 dict(cap='b) y la escala bajando por encima, para unir las dos cosas',
                      events=escala(tono, arriba, sentido='baja', notas=nq),
                      bars=cq, show_time=False),
             ]),
    ]


def sistemas_extra(tono, agudo, grave, time_sig=(4, 4), variante=0,
                   letras=('c', 'd', 'c', 'd', 'c')):
    """El mismo material, pero como SISTEMAS sueltos en vez de bloques nuevos.

       Para Luisa, cuyo album esta disenado con TRES pasos al piano y una sola
       hoja de estudio (lo comprueba `auditar_luisa`): meterle bloques 4 y 5 le
       cambia el nivel, que es justo lo que el cliente no quiere para ella
       —"poquito pero bien"—. El material se anade dentro de los pasos que ya
       tiene, que es mas trabajo en la misma estructura y no un escalon mas.

       `letras` son las que continuan la serie de cada paso (a, b, c...):
       las pone quien llama, que es el unico que sabe cuantos sistemas hay ya.

       Devuelve (para_el_paso_1, para_el_paso_2)."""
    # La tonica manda sobre el rotulo (ver `tonica`), asi que la variedad entre
    # piezas del MISMO tono no puede venir de cambiar de nota: viene de cambiar
    # de registro, de direccion y de figura. Con doce piezas de Luisa en Do o La
    # menor —que son las mismas teclas— hacen falta los tres ejes o media docena
    # de semanas traen el mismo ejercicio, que es justo la norma de variedad.
    agudo = tonica(tono, agudo)
    if (variante // 3) % 2:
        agudo = agudo[:-1] + str(int(agudo[-1]) + 1)
    baja_primero = (variante // 6) % 2
    fig = 'h' if (variante // 12) % 2 else 'q'
    nq = cuantas(time_sig, fig)
    bpb = time_sig[0] * (4.0 / time_sig[1])
    cq = max(1, int(round(nq * (2.0 if fig == 'h' else 1.0) / bpb)))
    fc = figura_compas(time_sig)
    arriba = agudo[0] + str(int(agudo[-1]) + 1) if agudo[-1].isdigit() else agudo
    if baja_primero:
        agudo, arriba = arriba, agudo
    alt = _frase_alteraciones(tono)

    escalas = [
        dict(cap=letras[0] + ') la escala de %s entera · %s' % (tono, alt),
             events=escala(tono, agudo, notas=nq, figura=fig,
                           sentido='baja' if baja_primero else 'sube'),
             bars=cq, show_time=False),
        dict(cap=letras[1] + ') y de vuelta · es el mismo camino y no sale igual de bien',
             events=escala(tono, arriba, notas=nq, figura=fig,
                           sentido='sube' if baja_primero else 'baja'),
             bars=cq, show_time=False),
    ]
    acordes = [
        dict(cap=letras[2] + ') el acorde de %s desplegado, sube y baja' % tono,
             events=arpegio(tono, agudo, notas=nq, figura=fig), bars=cq, show_time=False),
        dict(cap=letras[3] + ') y los tres acordes que sostienen la pieza: I - IV - V - I',
             events=cadencia(tono, grave, figura=fc), bars=4, clef='bass',
             show_time=False),
    ]
    giros = [
        dict(cap=letras[0] + ') el giro sobre la tónica, sin mover la mano de sitio',
             events=giro(tono, agudo, notas=nq), bars=cq, show_time=False),
        dict(cap=letras[1] + ') y los tres acordes de la pieza con la izquierda',
             events=cadencia(tono, grave, figura=fc), bars=4, clef='bass',
             show_time=False),
    ]
    # Dos sistemas por paso: con uno solo la hoja se seguia quedando corta, y
    # el sitio da justo para esto. El reparto rota con la pieza para que dos
    # semanas seguidas no traigan lo mismo.
    juegos = (escalas, acordes, giros)
    uno = juegos[variante % 3]
    dos = juegos[(variante + 1) % 3]
    # y uno mas para el paso de las dos manos: los mismos tres acordes, pero
    # arriba. Saberlos con las dos manos es lo que permite acompanar sin leer,
    # y cierra el paso volviendo a la pieza en vez de a un ejercicio suelto.
    tres = [dict(cap=letras[4] + ') y los mismos tres acordes con la derecha, arriba · '
                                 'la izquierda solo la tónica',
                 events=cadencia(tono, agudo, figura=fc), bars=4, show_time=False)]
    return uno, dos, tres
