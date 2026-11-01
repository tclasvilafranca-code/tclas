# -*- coding: utf-8 -*-
"""NOVIEMBRE · Fundamentos: postura, dedos, teclado y pentagrama."""
from n1_base import *
from n1_base import _abs_idx
from n1_comun import *

MES = 'Noviembre'


def construir(d):
    d.nuevo('Noviembre · Fundamentos')
    d.add(banda_mes('Noviembre', 'Etapa 1', 'Fundamentos del piano',
                    'Colocación al piano, numeración de los dedos, organización del teclado y lectura de las primeras notas en las dos claves.'))
    d.add(caja('dato', 'Postura y colocación de las manos', [
        '▸ Siéntate en el borde delantero de la banqueta, con la espalda erguida pero sin rigidez y los pies apoyados en el suelo.',
        '▸ La altura debe dejar los antebrazos aproximadamente paralelos al suelo, con los codos a la altura del teclado.',
        '▸ Hombros y cuello relajados. El sonido se produce con el **peso del brazo**, no con la fuerza del dedo.',
        '▸ Dedos ligeramente curvados, en contacto con la tecla por la yema; muñeca a la altura de la mano, sin caer ni elevarse; uñas cortas.']))
    d.add(h2('Numeración de los dedos'))
    d.add(manos_dedos(),
          par('En ambas manos los dedos se numeran del **1 (pulgar)** al **5 (meñique)**. Estos números, la **digitación**, aparecen sobre las notas en las '
              'partituras y determinan la posición de la mano en cada pasaje.', 9.4))
    d.add(h2('Posición de cinco dedos sobre el Do'),
          cinco_dedos_teclas(),
          par('En la mano derecha, el pulgar (1) se sitúa en el **Do central**. En la izquierda, el meñique (5) se sitúa en el **Do una octava más grave** y '
              'el pulgar (1) en el Sol. Cada dedo corresponde a una tecla, sin desplazar la mano.', 9.4))

    # ---------------------------------------------------------------- teclado
    d.add(caja('dato', 'Organización del teclado', [
        'El teclado alterna **teclas blancas** (las siete notas naturales: Do, Re, Mi, Fa, Sol, La, Si) y **teclas negras**, agrupadas en conjuntos de dos y de tres. '
        'Este patrón se repite a lo largo de todo el teclado; cada repetición, de un Do al siguiente, es una **octava** (7 blancas y 5 negras). '
        'Un piano de 88 teclas abarca desde el La0 hasta el Do8, con 52 teclas blancas y 36 negras.',
        'Las negras funcionan como referencia visual: **Do** queda a la izquierda del grupo de dos negras; **Fa**, a la izquierda del grupo de tres; '
        '**Mi** y **Si** son las blancas que no tienen una negra a su derecha. Hacia la derecha del teclado los sonidos son más agudos; hacia la izquierda, más graves.']),
        diag_grupos(),
        caja('nota', 'Nombre completo de una nota', [
            'Para distinguir un Do de otro se añade el número de **octava**: el Do central es el **Do4** (C4); el Do una octava más grave es el Do3, y una más aguda, el Do5. '
            'La numeración cuenta las octavas desde el extremo grave del piano.']))
    d.add(ejercicio(1, 'Nombrar las teclas',
                    ['Escribe el nombre de cada tecla blanca, empezando por el Do central y acabando en el Do de dos octavas más arriba.',
                     'Dilo en voz alta mientras señalas la tecla en el piano.'],
                    'Automatizar la correspondencia entre el nombre y la posición de la tecla.'))
    blancas = {'%s%d' % (L, o) for o in (4, 5) for L in 'CDEFGAB'} | {'C6'}
    d.add(bloque_teclado(h=80, desde=('C', 4), n_blancas=15, cajas=blancas, do_central=True, titulo='Dos octavas desde el Do central'))
    sol(MES, 1, 'Nombrar las teclas', ['Do Re Mi Fa Sol La Si Do Re Mi Fa Sol La Si Do.'])
    d.add(ejercicio(2, 'Localizar teclas de referencia',
                    ['En el teclado de tres octavas, rodea todas las teclas **Do** y marca con una cruz todas las teclas **Fa**.',
                     'Después, escribe el nombre completo (con la octava) de las seis teclas numeradas.'],
                    'Reconocer en cualquier octava las teclas de referencia y nombrarlas con su octava.'))
    marc = {'F3': '①', 'A4': '②', 'C5': '③', 'E3': '④', 'G4': '⑤', 'B5': '⑥'}
    d.add(bloque_teclado(h=78, desde=('C', 3), n_blancas=21, rotulos=marc, marcas={k: CREMA_T for k in marc},
                         titulo='Tres octavas: del Do3 al Si5'))
    def lineas_num(c, x, y, w):
        for i, g_ in enumerate(['①', '②', '③', '④', '⑤', '⑥']):
            c.setFont('DejaVuSans-Bold', 9.4)
            c.setFillColor(NAVY)
            c.drawString(x + 2 + i * 82, y - 14, g_)
            c.setStrokeColor(NAVY_SOFT)
            c.setLineWidth(0.6)
            c.line(x + 18 + i * 82, y - 16, x + 74 + i * 82, y - 16)
    d.add(Blk(30, lineas_num))
    sol(MES, 2, 'Localizar teclas de referencia',
        ['Do: C3, C4, C5 (tres teclas).  Fa: F3, F4, F5 (tres teclas).  Numeradas: ① Fa3 · ② La4 · ③ Do5 · ④ Mi3 · ⑤ Sol4 · ⑥ Si5.'])

    # ---------------------------------------------------------------- pentagrama
    d.add(caja('dato', 'El pentagrama y las claves', [
        'La música se escribe sobre el **pentagrama**: cinco líneas y cuatro espacios que se numeran de abajo arriba. Cada posición corresponde a una altura; '
        'cuanto más arriba se sitúa una nota, más aguda es.',
        'La **clave** fija qué nota representa cada posición. La **clave de sol** indica que la 2.ª línea es Sol; la **clave de fa**, que la 4.ª línea es Fa. '
        'En el piano se leen las dos a la vez: sol para las notas agudas, normalmente de la mano derecha, y fa para las graves, de la izquierda. '
        'Unidas por una llave forman el **sistema de piano**.',
        'Los nombres siguen el orden **Do – Re – Mi – Fa – Sol – La – Si** y se repiten en cada octava.']),
        diag_pentagrama(), diag_claves(),
        tabla([110, 190, 191], [['Clave de sol', 'Mi · Sol · Si · Re · Fa', 'Fa · La · Do · Mi'], ['Clave de fa', 'Sol · Si · Re · Fa · La', 'La · Do · Mi · Sol']],
              ['Clave', 'Líneas (de abajo arriba)', 'Espacios (de abajo arriba)'], alto=20, size=8.8),
        caja('nota', 'El Do central en las dos claves', [
            'El **Do central** (Do4) es la nota de enlace entre las dos claves: en clave de sol se escribe en la **1.ª línea adicional inferior** y en clave de fa, '
            'en la **1.ª línea adicional superior**. Es la misma tecla del piano.']))
    d.add(ejercicio(3, 'Lectura desde el Do en clave de sol',
                    ['La primera nota de cada fila es el **Do central**, ya nombrado. Cuenta a partir de ella y escribe el nombre de las demás.',
                     'Si dudas, sube por el orden Do – Re – Mi – Fa – Sol – La – Si hasta llegar a la nota.'],
                    'Leer contando desde una referencia, que es como se lee al principio con rapidez.'))
    r = rnd(11)
    bl, s3 = bloque_lectura(r, 'treble', 3, 'Clave de sol')
    d.add(*bl)
    sol(MES, 3, 'Lectura desde el Do', s3)
    d.add(ejercicio(4, 'Lectura desde el Fa en clave de fa',
                    ['La primera nota de cada fila es el **Fa de la 4.ª línea**, ya nombrado. Cuenta a partir de ella y escribe el nombre de las demás.'],
                    'Fijar la clave de fa a partir de su nota de referencia.'))
    r = rnd(12)
    bl, s4 = bloque_lectura(r, 'bass', 3, 'Clave de fa')
    d.add(*bl)
    sol(MES, 4, 'Lectura desde el Fa', s4)
    d.add(ejercicio(5, 'Escribir notas desde la referencia',
                    ['Dibuja la nota que corresponde a cada nombre. La primera ya está escrita: sube o baja por orden, una posición cada vez.'],
                    'Pasar del nombre a la posición en el pentagrama, el camino inverso a la lectura.'))
    asc = [mover('C4', k) for k in range(8)]
    desc = [mover('F3', -k) for k in range(8)]
    desc_t = [mover('C5', -k) for k in range(8)]
    d.add(fila_notas('treble', [asc[0]] + [None] * 7, 'w', bajo=[nombre(p) for p in asc], titulo='a) Clave de sol: desde el Do central, subiendo'))
    d.add(fila_notas('treble', [desc_t[0]] + [None] * 7, 'w', bajo=[nombre(p) for p in desc_t], titulo='b) Clave de sol: desde el Do agudo, bajando'))
    d.add(fila_notas('bass', [desc[0]] + [None] * 7, 'w', bajo=[nombre(p) for p in desc], titulo='c) Clave de fa: desde el Fa, bajando'))
    sol(MES, 5, 'Escribir notas desde la referencia',
        ['a) ' + ' · '.join('%s (%s)' % (nombre(p), posicion(p)) for p in asc),
         'b) ' + ' · '.join('%s (%s)' % (nombre(p), posicion(p)) for p in desc_t),
         'c) ' + ' · '.join('%s (%s)' % (nombre(p, False), posicion(p, 'bass')) for p in desc)])

    # ---------------------------------------------------------------- al piano
    d.add(caja('piano', 'Primeros ejercicios: posición de cinco dedos', [
        'Cada mano en su posición sobre el Do. Toca despacio (aproximadamente un golpe por segundo), con la cuenta en voz alta y las notas de igual duración y volumen. '
        'Primero mano derecha sola, después izquierda sola.']))
    ev_d = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in zip(['C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4', 'D4'], [1, 2, 3, 4, 5, 4, 3, 2])] + [{'pitch': 'C4', 'dur': 'w', 'number': 1}]
    ev_i = [{'pitch': p, 'dur': 'q', 'number': n} for p, n in zip(['C3', 'D3', 'E3', 'F3', 'G3', 'F3', 'E3', 'D3'], [5, 4, 3, 2, 1, 2, 3, 4])] + [{'pitch': 'C3', 'dur': 'w', 'number': 5}]
    d.add(sistema('a) Mano derecha: subir y bajar por la posición de Do', ev_d), sistema('b) Mano izquierda: la misma posición, una octava más grave', ev_i, clef='bass'))
    au = [('C', 'q', 1), ('C', 'q', 1), ('C', 'q', 1), ('D', 'q', 2), ('E', 'h', 3), ('D', 'h', 2), ('C', 'q', 1), ('E', 'q', 3), ('D', 'q', 2), ('D', 'q', 2), ('C', 'w', 1)]
    d.add(sistema('Au clair de la lune (canción tradicional francesa) · primera frase · mano derecha',
                  [{'pitch': l + '4', 'dur': dd, 'number': n} for l, dd, n in au]))
    d.add(sistema('La misma frase con la mano izquierda, una octava más grave',
                  [{'pitch': l + '3', 'dur': dd, 'number': {1: 5, 2: 4, 3: 3}[n]} for l, dd, n in au], clef='bass'))
    d.add(caja('tip', 'Cómo practicar la primera semana', [
        'Pocas repeticiones, lentas y limpias, valen más que muchas rápidas. Antes de tocar, **lee en voz alta los nombres de las notas y la digitación**; '
        'después toca con la cuenta. Si te equivocas, retrocede un compás, no vuelvas al principio. Diez a quince minutos diarios son suficientes para empezar.']))
    sol(MES, 'Al piano', 'Posición de cinco dedos y Au clair de la lune',
        ['a) y b): Do Re Mi Fa Sol Fa Mi Re Do. Au clair de la lune: Do Do Do Re · Mi (blanca) Re (blanca) · Do Mi Re Re · Do (redonda). Cada compás suma 4 tiempos.'])
