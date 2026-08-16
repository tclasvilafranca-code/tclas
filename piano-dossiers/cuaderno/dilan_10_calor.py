# -*- coding: utf-8 -*-
"""Al Calor del Amor en un Bar (Gabinete Caligari) — Dilan, avanzado.
   Ver TRANSCRIPCION_D09_11.md.

   Esta edicion es de las mejores del album: trae los CIFRADOS impresos en
   espanol Y ademas los NOMBRES DE LAS NOTAS del bajo escritos debajo del
   pentagrama. Las dos cosas son del editor, no analisis mio, asi que valen
   mas que cualquier cosa que yo dedujera.

   ATENCION con los numeros de compas: el recuento del lector no cuadra con
   los numeros impresos (el segno y las casillas le anaden barras), asi que
   aqui NO se cita ni un numero de compas. Se cita por CIFRADO, que es lo que
   la edicion imprime y no admite duda.

   Con armadura de Mi menor el Fa es sostenido por armadura y NO se escribe;
   el Do sostenido del acorde Fa#7 si, porque es alteracion accidental.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
MIm = 'Mi menor'
_B = [1800]


def n(p, d='q'):
    return {'pitch': p, 'dur': d}


def sil(d='e'):
    return {'rest': True, 'dur': d}


def corch(ps, agrupar=4):
    out = []
    for i, p in enumerate(ps):
        if i % agrupar == 0:
            _B[0] += 1
        out.append({'pitch': p, 'dur': 'e', 'beam': _B[0]})
    return out


def molde(fund, quinta, oct_):
    """El dibujo de la izquierda: fundamental · octava · quinta · octava."""
    return [n(fund), n(oct_), n(quinta), n(oct_)]


# --- lo medido, contrastado con los cifrados impresos ----------------------
MIM = molde('E2', 'B2', 'E3')            # cifrado Mim
FAS7 = molde('F2', 'C#3', 'F3')          # cifrado Fa#7 · el Do# va escrito
LAM = molde('A2', 'E3', 'A3')            # cifrado Lam
SOL = [n('G2'), n('G3'), n('B2'), n('G3')]   # cifrado Sol · aqui la 3a, no la 5a

# la melodia: el descenso que el lector encuentra dos veces, identico
BAJADA = [n('C5'), n('B4'), n('A4'), n('G4'), n('F4'), n('E4')]
# y la celula que sale CINCO veces
CELULA = [n('C5'), n('A4'), n('A4'), n('B4'), n('A4')]

CANCION = dict(
    alumno='Dilan', num=10, nivel='avanzado', slug='AlCalor',
    titulo_corto='Al Calor del Amor en un Bar', time_sig=(4, 4), key_sig=MIm,
    partitura=os.path.join(HERE, '..', 'students', 'dilan', 'source', 'DILAN',
                           'al-calor-del-amor-en-un-bar.pdf'),
    yt='https://www.youtube.com/results?search_query=gabinete+caligari+al+calor+del+amor+en+un+bar',

    ficha=dict(
        titulo='Al Calor del Amor en un Bar',
        autor='Gabinete Caligari (1986) · edición con cifrados en español',
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '4/4'), ('Tempo', 'Allegretto'),
               ('Mano izq.', 'Bajo alterno'), ('Extras', 'Cifrados')],
        armonia=dict(
            titulo='El molde de la mano izquierda',
            tarjetas=[
                ('CIFRADO Mim', 'Mi · Mi · Si · Mi',
                 'Fundamental, octava, quinta, octava. Cuatro negras, siempre igual.'),
                ('CIFRADO Fa♯7', 'Fa♯ · Fa♯ · Do♯ · Fa♯',
                 'El mismo molde movido. El Do♯ va escrito: no está en la armadura.'),
                ('CIFRADO Lam', 'La · La · Mi · La',
                 'Y otra vez igual. Es un molde, no cuatro notas que aprenderse.'),
                ('CIFRADO Sol', 'Sol · Sol · Si · Sol',
                 'Aquí el editor pone la TERCERA en vez de la quinta. Es la única excepción.'),
            ],
            pie='Esta edición te lo da todo hecho: encima del pentagrama están los cifrados en español '
                'y debajo del de la izquierda están escritos los nombres de las notas graves (MI, '
                'FA♯ MI DO♯ FA♯, MI SOL SI…). Eso lo ha puesto el editor, no yo, así que es más fiable '
                'que cualquier análisis. Si sabes colocar el molde, esta canción no hay que leerla.',
        ),
        ritmos=[
            ('MI · Mim', 'el molde: fundamental, octava, quinta, octava', MIM, OCRE, 'bass', MIm),
            ('MI · Fa♯7', 'el mismo molde movido, con el Do♯ escrito', FAS7, OCRE, 'bass', MIm),
            ('MD', 'la frase que más se repite: baja hasta la tónica',
             corch(['C5', 'B4', 'A4', 'G4', 'F4', 'E4']) + [n('E4')], AZUL, 'treble', MIm),
        ],
        especial=[
            'Armadura de un sostenido: todos los Fa son ♯. La tonalidad es Mi menor.',
            'Los cifrados vienen impresos y EN ESPAÑOL: Mim, Fa♯7, Si7, Lam, Solm, Sol.',
            'Debajo de la clave de fa están escritos los NOMBRES de las notas del bajo.',
            'Hay SEGNO y casillas 1.ª y 2.ª: el orden en que se toca no es el orden escrito.',
            'Más adelante CAMBIA LA ARMADURA a cuatro sostenidos. Míralo antes de llegar.',
            'Los cuatro primeros compases son introducción: la voz todavía no ha entrado.',
            'Hay TRESILLOS marcados con un 3 en la mano derecha.',
        ],
        reto='El recorrido de la hoja. Entre el segno, las dos casillas y el cambio de armadura, esta '
             'partitura se toca en un orden que no es el que está escrito, y con una tonalidad que '
             'cambia por el camino. Si eso no está claro, da igual lo bien que salgan las notas.',
        truco='Antes de tocar nada, sigue la partitura con el dedo y di en voz alta por dónde vas: '
              '"intro, segno, estrofa, casilla 1, vuelvo al segno, casilla 2". Y para la izquierda, lee '
              'solo los cifrados y coloca el molde: no mires el pentagrama de abajo.',
        sabias='Jaime Urrutia la escribió en 1986 pensando en los bares de Malasaña, y Gabinete Caligari '
               'la grabó con una trompeta que no estaba prevista: se la sugirió el productor en el '
               'estudio. Es de las pocas canciones de la Movida que hoy cantan igual tres generaciones.',
        qr=dict(titulo='Escucha la original',
                texto='Escucha el bajo: hace lo mismo que tu mano izquierda, sin parar.', png=None),
    ),

    calentamiento=dict(
        intro='Cinco minutos antes de abrir la partitura. La tonalidad es Mi menor y el gesto de la '
              'canción es un bajo alterno de cuatro negras. Aquí se trabaja ese molde por toda la '
              'tonalidad, no solo sobre los acordes que la pieza usa.',
        reglas=['ARMADURA DE MI MENOR: FA♯', 'EL PRIMER GOLPE PESA MÁS', 'MANOS SEPARADAS'],
        ejercicios=[
            dict(num=1, titulo='Escala de Mi menor · dos octavas', clef='bass',
                 pista='manos separadas · un solo sostenido, y el pulgar por debajo sin bache',
                 events=corch(['E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3']) +
                        corch(['F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'E4']) +
                        corch(['E4', 'D4', 'C4', 'B3', 'A3', 'G3', 'F3', 'E3']) +
                        corch(['D3', 'C3', 'B2', 'A2', 'G2', 'F2', 'E2', 'E2']),
                 bars_per_line=4),
            dict(num=2, titulo='El molde, por toda la tonalidad', clef='bass',
                 pista='fundamental · octava · quinta · octava, sobre los seis grados de Mi menor',
                 events=(molde('E2', 'B2', 'E3') + molde('F2', 'C3', 'F3') +
                         molde('G2', 'D3', 'G3') + molde('A2', 'E3', 'A3') +
                         molde('B2', 'F3', 'B3') + molde('E2', 'B2', 'E3')),
                 bars_per_line=3),
            dict(num=3, titulo='El molde al revés', clef='bass',
                 pista='octava · fundamental · octava · quinta · lo que la pieza nunca te hace practicar',
                 events=([n('E3'), n('E2'), n('E3'), n('B2')] +
                         [n('A3'), n('A2'), n('A3'), n('E3')] +
                         [n('G3'), n('G2'), n('G3'), n('D3')] +
                         [n('E3'), n('E2'), n('E3'), n('B2')]),
                 bars_per_line=4),
            dict(num=4, titulo='El Do sostenido que no está en la armadura',
                 pista='la nota del acorde Fa♯7 · va escrita a mano y es fácil comérsela',
                 events=[n('F4'), n('A4'), n('C#5'), n('E5'),
                         n('D5', 'h'), n('B4', 'h'),
                         n('E5'), n('C#5'), n('A4'), n('F4'),
                         n('E4', 'w')],
                 bars_per_line=3),
            dict(num=5, titulo='Notas repetidas, cambiando de dedo',
                 pista='dedos 3 · 2 · 1 · así empieza la canción, con la misma nota picoteada',
                 events=corch(['B4'] * 8) + corch(['A4'] * 8) +
                        corch(['G4'] * 8) + corch(['B4'] * 8),
                 bars_per_line=4),
        ],
    ),

    agudeza=dict(
        intro='Ni una nota al piano. Arriba se lee en voz alta, en las dos claves y con un sostenido. '
              'Abajo se escucha: lo dirige quien esté contigo y tú no miras el teclado.',
        sub_leer='di el nombre en voz alta · armadura de Mi menor: todos los Fa son ♯',
        chuleta_clef='bass',
        chuleta_titulo='EL REGISTRO DEL BAJO ALTERNO (CLAVE DE FA)',
        chuleta_pitches=['E2', 'G2', 'B2', 'E3', 'G3', 'B3', 'E4'],
        chuleta_nombres=['Mi', 'Sol', 'Si', 'Mi', 'Sol', 'Si', 'Mi'],
        ejercicios=[
            dict(num=1, titulo='Clave de Fa, registro grave', clef='bass',
                 pista='donde vive el bajo alterno · con líneas adicionales por abajo',
                 events=[n(p) for p in ('E2', 'B3', 'A2', 'E3', 'G2', 'D3', 'F2', 'B2',
                                        'C3', 'A3', 'E2', 'G3', 'D2', 'F3', 'B2', 'E3')]),
            dict(num=2, titulo='Clave de Sol',
                 pista='donde vive la melodía · orden irregular a propósito',
                 events=[n(p) for p in ('E4', 'B4', 'G4', 'E5', 'C5', 'A4', 'F4', 'D5',
                                        'G4', 'C5', 'B4', 'F5', 'A4', 'D4', 'E5', 'G4')]),
            dict(num=3, titulo='Con el Do sostenido',
                 pista='el del acorde Fa♯7 · una alteración suelta vale hasta la barra, no más',
                 events=[n('F4'), n('C#5', 'h'), n('A4'),
                         n('B4'), n('A4'), n('F4', 'h'),
                         n('E5'), n('C#5'), n('A4'), n('F4'),
                         n('E4', 'w')]),
        ],
        crono='¿Cuánto tardas en el ejercicio 1, sin fallos?',
        escucha=dict(
            sub='sin mirar el teclado · rodea con lápiz lo que oigas',
            profe=[
                ('A', 'Toca el molde de cuatro negras sobre un acorde. Que diga si la TERCERA nota fue '
                      'la quinta (lo normal) o la tercera (como en el Sol).'),
                ('B', 'Toca una tríada suelta: MAYOR o MENOR. La pieza alterna las dos.'),
                ('C', 'Toca dos acordes y acaba unas veces en Mi menor y otras en Si. Que diga si la '
                      'frase queda CERRADA o ABIERTA.'),
                ('+', 'Y sin escribir: toca el molde sobre Mi y que lo repita sobre La, de oído.'),
            ],
            filas=[
                dict(letra='A', titulo='¿Quinta o tercera?', pista='la tercera nota del molde',
                     n=10, opciones=['5ª', '3ª']),
                dict(letra='B', titulo='¿Mayor o menor?', pista='la tríada entera, de una vez',
                     n=8, opciones=['M', 'm']),
                dict(letra='C', titulo='¿Cerrada o abierta?', pista='acaba en la tónica, o se queda esperando',
                     n=6, opciones=['cerrada', 'abierta']),
            ],
        ),
    ),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 y 2 de 5',
        intro='Esta partitura te lo da casi todo hecho: el editor escribe los nombres de las notas '
              'graves debajo del pentagrama y los cifrados encima. Con eso se toca la izquierda entera '
              'sin leer una sola nota. Aquí no se cita ningún número de compás —con el segno y las '
              'casillas, contar da un número distinto según por dónde leas—: se cita por CIFRADO.',
        reglas=['SE CITA POR CIFRADO, NO POR COMPÁS', 'EL PRIMER GOLPE PESA MÁS', 'LEE LOS NOMBRES DEL BAJO'],
        bloques=[
            dict(num=1, titulo='El molde, y por dónde viaja', clef='bass',
                 pista='cifrado Mim · Mi · Mi · Si · Mi, medido y confirmado por los nombres impresos',
                 sistemas=[
                     dict(cap='a) cuatro negras sobre Mi menor · la primera pesa, las otras tres solo '
                              'acompañan',
                          events=MIM + MIM, bars=2, clef='bass'),
                     dict(cap='b) solo la fundamental de cada cifrado · Mi · Fa♯ · La · Sol · Mi: una '
                              'nota por compás y ya suena a la canción',
                          events=[n('E2', 'w'), n('F2', 'w'), n('A2', 'w'),
                                  n('G2', 'w'), n('E2', 'w')],
                          bars=5, clef='bass', show_time=False),
                     dict(cap='c) el molde sobre los cuatro cifrados: Mim · Fa♯7 · Lam · Sol · el Do♯ '
                              'del Fa♯7 va escrito a mano',
                          events=MIM + FAS7 + LAM + SOL, bars=4, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='ESTA PARTITURA TE LO DA TODO HECHO',
                 texto='Debajo del pentagrama de la izquierda el editor ha escrito los nombres de las '
                       'notas graves: “MI”, “FA♯ MI DO♯ FA♯”, “MI SOL SI”. Y encima están los cifrados. '
                       'Con eso puedes tocar la izquierda entera sin leer una sola nota: lees el cifrado, '
                       'colocas el molde y ya está. Los cifrados están impresos y no admiten discusión; '
                       'los números de compás, con el segno y las casillas, sí.'),
            dict(num=2, titulo='La derecha, en dos trozos que se repiten',
                 pista='alturas medidas · una bajada y una célula, y con eso tienes media canción',
                 sistemas=[
                     dict(cap='a) la frase que más se repite · Do · Si · La · Sol · Fa♯ · Mi: no la '
                              'leas nota a nota, léela como una bajada',
                          events=BAJADA + [n('E4', 'h')], bars=2),
                     dict(cap='b) la célula que sale cinco veces idéntica · Do · La · La · Si · La',
                          events=CELULA + [n('A4', 'h.')], bars=2, show_time=False),
                     dict(cap='c) y las dos seguidas, que es como aparecen en la canción',
                          events=BAJADA + [n('E4', 'h')] + CELULA + [n('A4', 'h.')],
                          bars=4, show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3, 4 y 5',
        intro='Las notas son lo de menos en esta canción: lo difícil es saber por dónde va la hoja. Hay '
              'segno, dos casillas y un cambio de armadura a mitad de partitura.',
        reglas=['PRIMERO EL RECORRIDO, LUEGO LAS NOTAS', 'OJO AL CAMBIO DE ARMADURA', 'ALLEGRETTO, NO CARRERA'],
        bloques=[
            dict(num=3, titulo='El recorrido, y la entrada', clef='treble',
                 pista='primero con el dedo y en voz alta, sin piano · después la introducción',
                 sistemas=[
                     dict(cap='a) los cuatro primeros compases van sobre una sola nota repetida · el '
                              'dedo cambia (3 · 2 · 1) pero la tecla no, y no se acelera',
                          events=corch(['E5'] * 8) + corch(['E5'] * 8) +
                                 corch(['E5'] * 8) + [n('E5', 'w')],
                          bars=4),
                     dict(cap='b) el bajo de la estrofa de un tirón · Mim · Fa♯7 · Si7 · Mim y vuelta: '
                              'así se oye la forma entera sin tocar casi nada',
                          events=[n('E2', 'w'), n('F2', 'w'), n('B2', 'w'), n('E2', 'w'),
                                  n('A2', 'w'), n('G2', 'w'), n('B2', 'w'), n('E2', 'w')],
                          bars=8, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE HACE EL PASO 3',
                 texto='1 · Cuatro compases de introducción, con la derecha picoteando la misma nota. '
                       '2 · Empieza la estrofa: ahí está el SEGNO, la marca a la que vas a volver. '
                       '3 · Llegas a la casilla 1.ª, la tocas y vuelves al segno. '
                       '4 · La segunda vez te saltas la 1.ª y entras por la 2.ª. '
                       'Sigue la partitura con el dedo y di en voz alta dónde estás antes de tocar nada.'),
            dict(num=4, titulo='El cambio de armadura',
                 pista='la misma bajada, escrita en la armadura nueva · mismas líneas, otras teclas',
                 sistemas=[
                     dict(cap='a) con cuatro sostenidos · en blancas, para colocar los dedos antes de '
                              'ponerle velocidad',
                          events=[n(e['pitch'], 'h') for e in BAJADA] + [n('E4', 'w')],
                          bars=4, key_sig='Mi mayor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE HACE EL PASO 4',
                 texto='A mitad de la partitura aparece una armadura nueva, de cuatro sostenidos. Eso '
                       'quiere decir que a partir de ahí los Fa, los Do, los Sol y los Re son todos '
                       'sostenidos, y que la mano se coloca en otro sitio aunque los cifrados se parezcan. '
                       'Busca ese cambio en tu hoja y márcalo con lápiz antes de estudiar nada: es el '
                       'punto donde más gente se cae.'),
            dict(tipo='escalera', valores=[70, 84, 96, 108, 116, 124],
                 regla='PASO 5 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
            dict(tipo='nota', etiqueta='LOS CINCO PASOS, PARA NO PERDERSE',
                 texto='1 · El molde, y por dónde viaja: solo cifrados, sin leer el pentagrama.   '
                       '2 · La derecha: la bajada y la célula.   '
                       '3 · El recorrido en voz alta, y la introducción.   '
                       '4 · El cambio de armadura, marcado con lápiz.   '
                       '5 · La escalera, y las dos manos del segno a la casilla 1.ª.'),
        ],
    ),

)

if __name__ == '__main__':
    print('generado', construir(CANCION))
