# -*- coding: utf-8 -*-
"""Los datos del CURSO PEKES — un curso entero (44 semanas, Septiembre a Junio)
   de iniciacion musical para ninos de 6-8 anos en su primer ano de piano,
   media hora de clase.

   De donde sale esto
   -------------------
   Reconstruido a partir del dosier "NIVEL PEKES" que el cliente ya tenia en
   Canva (138 paginas: 44 "CLASES" de 3 hojas cada una -- Teoria, Ejercicio,
   Juego Musical). El contenido es bueno y el recorrido pedagogico tambien
   (piano -> manos -> pentagrama -> clave de Sol -> las 7 notas con su color
   -> figuras -> compas -> silencios -> plicas -> repaso y concierto final),
   pero el archivo tenia bugs reales que se corrigen aqui:

   - Numeracion de clase rota: "Pilla al RE", "Pilla al MI" y "Pilla al FA"
     estaban los tres etiquetados "CLASE 13" en vez de 14, 15, 16/17.
   - El juego "El ninja del silencio" se repetia CUATRO veces casi palabra
     por palabra (una por cada silencio). Aqui es un solo texto por semana,
     sin relleno.
   - Las clases de Fa, Sol y Si (17, 18, 23) y la 41 no estaban completas en
     el original: se completan aqui siguiendo EXACTAMENTE el mismo patron ya
     usado en Do/Re/Mi/La (color + posicion en el pentagrama + "Pilla al X"),
     con los colores ya fijados por el cliente en otro material de esta
     sesion (Do rojo, Re naranja, Mi amarillo, Fa verde, Sol azul, La lila,
     Si gris -- ver `juego_escala_colores.py`).

   Cada CLASE es UNA hoja (lo que pidio el cliente: comprimir de 3 a 1 hoja
   por semana), con tres bloques dentro de esa misma hoja: Teoria, Ejercicio,
   Juego Musical. El curso entero sigue siendo 44 semanas -- una por semana de
   clase real -- pero agrupadas visualmente en 7 BLOQUES tematicos para que
   el peke vea el avance.
"""
from reportlab.lib.colors import HexColor

# --------------------------------------------------------------------------
# Los 7 bloques tematicos. `color` tinta la banda superior y el indicador de
# avance de cada semana que cae dentro de ese bloque.
# --------------------------------------------------------------------------
BLOQUES = [
    dict(n=1, nombre='EL PIANO Y LAS MANOS', desde=1,  hasta=4,  color=HexColor('#B4462F')),
    dict(n=2, nombre='EL PENTAGRAMA',        desde=5,  hasta=12, color=HexColor('#2C4C6B')),
    dict(n=3, nombre='LAS SIETE NOTAS',      desde=13, hasta=24, color=HexColor('#4A6741')),
    dict(n=4, nombre='LAS FIGURAS Y EL COMPÁS', desde=25, hasta=32, color=HexColor('#A9762F')),
    dict(n=5, nombre='LOS SILENCIOS',        desde=33, hasta=36, color=HexColor('#7A2E35')),
    dict(n=6, nombre='LAS PLICAS',           desde=37, hasta=40, color=HexColor('#5B4B8A')),
    dict(n=7, nombre='EL GRAN REPASO Y EL CONCIERTO', desde=41, hasta=44, color=HexColor('#B98A2E')),
]


def bloque_de(n):
    for b in BLOQUES:
        if b['desde'] <= n <= b['hasta']:
            return b
    raise ValueError('semana fuera de rango: %r' % n)


# Las 7 notas, en el orden y color que ya usa el proyecto (ver
# `juego_escala_colores.py`, pedido explicito del cliente).
NOTAS_COLOR = {
    'DO':  ('C4', HexColor('#D2483C')),
    'RE':  ('D4', HexColor('#E8862B')),
    'MI':  ('E4', HexColor('#E5C230')),
    'FA':  ('F4', HexColor('#4E9B4E')),
    'SOL': ('G4', HexColor('#3B72B4')),
    'LA':  ('A4', HexColor('#8C6BC1')),
    'SI':  ('B4', HexColor('#7D7D7D')),
}
ORDEN_NOTAS = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']


def _juego(titulo, texto):
    return dict(titulo=titulo, texto=texto)


# Los juegos que se repiten semana a semana (mismo juego, cambia solo lo que
# se esta entrenando): UN texto cada uno, no cuatro copias casi iguales.
J_PILLA = _juego(
    'PILLA LA NOTA',
    'La profe toca notas mezcladas en el piano. Cada vez que suena la nota de '
    'esta semana, el peke salta y la grita en voz alta. La profe va cada vez '
    'más rápido y mete trampas con notas parecidas para despistarle.')
J_NINJA = _juego(
    'EL NINJA DEL SILENCIO',
    'La profe toca el piano mezclando notas y silencios. Mientras suena, el '
    'peke baila libremente. En cuanto llega el silencio se convierte en un '
    'ninja: inmóvil y sin hacer ruido hasta que vuelve a sonar la música.')

# --------------------------------------------------------------------------
# Las 44 semanas.
# --------------------------------------------------------------------------
CLASES = []


def _c(n, teoria_titulo, teoria_texto, dibujo, ejercicio, juego):
    CLASES.append(dict(
        n=n,
        bloque=bloque_de(n)['n'],
        teoria=dict(titulo=teoria_titulo, texto=teoria_texto, dibujo=dibujo),
        ejercicio=ejercicio,
        juego=juego,
    ))


def _ej(tipo, instrucciones, **datos):
    d = dict(tipo=tipo, instrucciones=instrucciones)
    d.update(datos)
    return d


# ---- BLOQUE 1 · EL PIANO Y LAS MANOS ------------------------------------
_c(1, 'Las partes del piano',
   'El piano tiene muchas partes. ¡Vamos a conocerlas todas!',
   ('piano_partes', {}),
   _ej('numera', 'Numera cada parte del piano y escribe su nombre en la lista.',
       items=['Teclas blancas', 'Teclas negras', 'Tapa', 'Atril', 'Pedal',
              'Patas', 'Caja de resonancia']),
   _juego('EL PIANO BAILÓN',
          'La profe pone una canción que le guste al peke. Mientras suena, '
          'el peke baila libremente por la sala. Cuando la música se para de '
          'golpe, tiene que quedarse congelado como una estatua: el que se '
          'mueve, pierde.'))

_c(2, 'Mis manitas en el piano',
   'Para tocar el piano hay que poner las manos como si tuviéramos una '
   'pelota pequeña dentro, con los dedos numerados del 1 al 5.',
   ('manos_dedos', {}),
   _ej('escribe_letra', 'Escribe el número correcto dentro de cada dedo, en las dos manos.',
       filas=['Mano izquierda: 1-2-3-4-5', 'Mano derecha: 1-2-3-4-5']),
   _juego('EL VOLCÁN DE DEDOS',
          'Las dos manos sobre la tapa cerrada del piano. La profe dice un '
          'número del 1 al 5 y el peke tiene que levantar ese dedo antes de '
          'que la profe lo toque. Si no llega a tiempo, ¡el volcán explota! '
          'Después se cambian los papeles.'))

_c(3, 'Dos manos, dos mundos',
   'En el piano cada mano tiene su sitio: la izquierda vive en lo grave '
   '(como un oso), la derecha en lo agudo (como un pajarito).',
   ('grave_agudo', {}),
   _ej('rodea', 'Rodea con un círculo las manos derechas y pon una cruz en las izquierdas.',
       items=['Agudo (pajarito) · mano derecha', 'Grave (oso) · mano izquierda',
              'Grave (oso) · mano izquierda', 'Agudo (pajarito) · mano derecha']),
   _juego('EL OSO Y EL PAJARITO',
          'La profe toca notas muy graves y muy agudas en el piano. Cuando '
          'suenan graves, el peke gruñe como un oso y camina pesado. Cuando '
          'suenan agudas, vuela por la sala como un pajarito. La profe puede '
          'cambiar de golpe para pillarle descolocado.'))

_c(4, '¡Hola Do, eres nuestro amigo!',
   'El Do central es la nota más importante: nuestra casa en el piano. '
   'Siempre está justo a la izquierda de las dos teclas negras juntas.',
   ('do_central', {}),
   _ej('rodea', 'Encuentra el Do en el teclado y dibuja una estrella encima.',
       items=['Do central']),
   _juego('EL DO ESCONDIDO',
          'La profe tapa casi todo el teclado, dejando asomar solo un '
          'trocito de teclas negras. El peke tiene que adivinar dónde está '
          'el Do mirando solo las negras que se ven. Si acierta, la profe '
          'toca el Do fuerte para celebrarlo.'))

# ---- BLOQUE 2 · EL PENTAGRAMA -------------------------------------------
_c(5, '¡La casa de la música!',
   'El pentagrama es donde viven las notas. Tiene 5 líneas y 4 espacios, y '
   'se cuentan siempre desde abajo hacia arriba.',
   ('pentagrama_lineas', {}),
   _ej('numera', 'Escribe el número correcto al lado de cada línea, y colorea los espacios.',
       items=['Línea 1', 'Línea 2', 'Línea 3', 'Línea 4', 'Línea 5']),
   _juego('LA RAYUELA MUSICAL',
          'Cinco tiras de cinta en el suelo forman un pentagrama gigante. El '
          'peke salta de línea en línea contando en voz alta, primero de '
          'abajo arriba y luego al revés. Con música: cuando para, el peke '
          'dice en qué línea se ha quedado.'))

_c(6, 'Líneas y espacios',
   'Las notas viven o bien en una línea, o bien en un espacio entre dos '
   'líneas. Nunca en los dos sitios a la vez.',
   ('linea_espacio', {}),
   _ej('escribe_letra', 'Debajo de cada nota escribe una L si está en línea o una E si está en espacio.',
       filas=['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Nota 5', 'Nota 6']),
   _juego('SALTAR O PARAR',
          'Con el pentagrama gigante del suelo: la profe grita "¡LÍNEA!" y '
          'el peke salta encima de una cinta; grita "¡ESPACIO!" y salta '
          'entre dos. Cada vez más rápido, hasta que se confunde y se ríe.'))

_c(7, 'Arriba vuelan los pajaritos, abajo duermen los osos',
   'Cuanto más arriba está la nota en el pentagrama, más agudo suena. '
   'Cuanto más abajo, más grave.',
   ('agudo_grave_pentagrama', {}),
   _ej('rodea', 'Rodea con un círculo las notas agudas y con un cuadrado las más graves.',
       items=['Nota aguda', 'Nota grave', 'Nota aguda', 'Nota grave', 'Nota grave']),
   _juego('EL ASCENSOR LOCO',
          'La profe toca notas subiendo poco a poco de graves a agudas. El '
          'peke se agacha cuando bajan y se estira de puntillas cuando '
          'suben, como un ascensor. Si la profe salta de golpe de muy agudo '
          'a muy grave, el peke se tira al suelo rápido.'))

_c(8, '¡Ya sé todo del pentagrama!',
   'Repaso: 5 líneas y 4 espacios, y las notas viven arriba o abajo según '
   'lo agudas o graves que sean.',
   ('repaso_pentagrama1', {}),
   _ej('escribe_letra', 'Escribe el número de línea o espacio de cada nota, y si es aguda (A) o grave (G).',
       filas=['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']),
   _juego('EL DIRECTOR LOCO',
          'El peke dirige una orquesta imaginaria: brazos arriba, la profe '
          'toca agudo; brazos abajo, toca grave; brazos cruzados, silencio '
          'total. Después se cambian los papeles.'))

_c(9, '¡Aprendo a dibujar la clave de Sol!',
   'La clave de Sol se dibuja en 3 pasos: un círculo alrededor de la nota '
   'Sol, una subida que gira por el medio, y se cierra al final.',
   ('clave_sol_pasos', {}),
   _ej('crea', 'Practica la clave de Sol tantas veces como quieras, con el color que más te guste.',
       compases=6),
   _juego('LA CLAVE GIGANTE',
          'En un mural grande en el suelo, el peke dibuja la clave de Sol lo '
          'más grande posible, pero solo puede mover el rotulador mientras '
          'suena la música. Cuando para la música, para el lápiz.'))

_c(10, 'La clave de Sol, la guardiana del pentagrama',
   'La clave de Sol va siempre al principio del pentagrama. Sin ella, nadie '
   'sabe cómo se llaman las notas que hay dentro.',
   ('clave_guardiana', {}),
   _ej('escribe_letra', 'Dibuja la clave de Sol al principio de cada pentagrama.',
       filas=['Pentagrama 1', 'Pentagrama 2', 'Pentagrama 3']),
   _juego('MISOL DICE...',
          'Como el "Simón dice": la profe ordena "Misol dice... toca algo '
          'grave" y el peke obedece. Pero si la profe no dice "Misol dice" '
          'primero y el peke obedece igual, pierde y hace un reto gracioso.'))

_c(11, '¡La casa está lista!',
   'Cuando el pentagrama tiene su clave de Sol, la casa de la música está '
   'completa y lista para recibir notas.',
   ('pentagrama_completo', {}),
   _ej('crea', 'Construye tu pentagrama desde cero: 1) las 5 líneas, 2) la clave de Sol, 3) una nota donde quieras.',
       compases=3),
   _juego('LA ORQUESTA DE LOS ANIMALES',
          'Oso = grave, pajarito = agudo, perro = medio. La profe toca una '
          'nota y el peke imita al animal correspondiente con todo el '
          'cuerpo. La profe puede encadenar animales cada vez más rápido.'))

_c(12, '¡Soy un experto del pentagrama!',
   'Repaso final del bloque: 5 líneas y 4 espacios, clave de Sol, y oso '
   'grave / pajarito agudo.',
   ('repaso_pentagrama2', {}),
   _ej('vf', 'Responde verdadero o falso.',
       items=['El pentagrama tiene 5 líneas.',
              'El pentagrama tiene 3 espacios.',
              'La clave de Sol va al final del pentagrama.',
              'Las notas graves están arriba.',
              'Entre las líneas hay espacios.']),
   _juego('EL KARAOKE DEL PIANO',
          'La profe pone una canción que le guste al peke. Canta a todo '
          'volumen mientras toca cualquier tecla siguiendo el ritmo, sin '
          'preocuparse de si suena bien. Al final, aplauden los dos como si '
          'hubieran dado un concierto.'))

# ---- BLOQUE 3 · LAS SIETE NOTAS -----------------------------------------
def _c_nota(n, nombre):
    pitch, color = NOTAS_COLOR[nombre]
    orden = ORDEN_NOTAS.index(nombre)
    posiciones = ['en el primer espacio, debajo de la primera línea',
                  'en el primer espacio',
                  'en la primera línea',
                  'en el primer espacio por encima de la primera línea',
                  'en la segunda línea',
                  'en el segundo espacio',
                  'en la tercera línea']
    _c(n, '¡Hola %s, eres %s!' % (nombre.capitalize(), _nombre_color(color)),
       '%s vive %s del pentagrama. ¡Ya conoces %d nota%s!' % (
           nombre.capitalize(), posiciones[orden], orden + 1,
           's' if orden else ''),
       ('nota_color', dict(nombre=nombre)),
       _ej('colorea', 'Encuentra la tecla y la nota %s, y pinta las dos del mismo color.' % nombre.capitalize(),
           nombre=nombre),
       J_PILLA)


def _nombre_color(hexcolor):
    return {HexColor('#D2483C'): 'rojo', HexColor('#E8862B'): 'naranja',
            HexColor('#E5C230'): 'amarillo', HexColor('#4E9B4E'): 'verde',
            HexColor('#3B72B4'): 'azul', HexColor('#8C6BC1'): 'lila',
            HexColor('#7D7D7D'): 'gris'}[hexcolor]


_c_nota(13, 'DO')
_c_nota(14, 'RE')
_c_nota(15, 'MI')

_c(16, '¡Ya sé tres notas! DO-RE-MI',
   'Do, Re y Mi son nuestros tres primeros amigos. Cada uno tiene su color '
   'y su casa fija en el pentagrama.',
   ('mapa_notas', dict(hasta='MI')),
   _ej('escribe_letra', 'Escribe D, R o M debajo de cada nota según corresponda, y pinta cada una de su color.',
       filas=['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Nota 5', 'Nota 6']),
   _juego('EL TREN DO-RE-MI',
          'El peke es un tren que solo puede avanzar un vagón (un escalón) '
          'cada vez: Do, luego Re, luego Mi, y vuelta atrás. La profe toca '
          'las notas en el piano mientras el peke "viaja" cantando cada '
          'parada.'))

_c_nota(17, 'FA')
_c_nota(18, 'SOL')

_c(19, '¡Hola La, eres lila!',
   'El La está un escalón más arriba que el Sol. En el pentagrama vive en '
   'el segundo espacio.',
   ('nota_color', dict(nombre='LA')),
   _ej('colorea', 'Encuentra la tecla y la nota La, y pinta las dos de color lila.', nombre='LA'),
   _juego('LA CAJA DE LOS SONIDOS',
          'Dentro de una caja hay objetos que suenan: una cuchara, un vaso, '
          'unas llaves. El peke saca uno sin mirar y hace música con él '
          'durante 30 segundos mientras la profe le acompaña al piano.'))

_c_nota(20, 'SI')

_c(21, '¡Ya sé seis notas!',
   'Do, Re, Mi, Fa, Sol y La ya son viejos amigos. Solo falta una nota para '
   'completar la escalera entera.',
   ('mapa_notas', dict(hasta='LA')),
   _ej('rodea', 'Rodea solo las notas que ya sabes nombrar (todas menos el Si).',
       items=ORDEN_NOTAS[:-1]),
   J_PILLA)

_c(22, 'El piano y el pentagrama son el mismo mapa',
   'Cada tecla blanca tiene su sitio exacto en el pentagrama. Si sabes '
   'dónde vive una nota en el piano, ya sabes dónde dibujarla en el papel.',
   ('mapa_notas', dict(hasta='SI')),
   _ej('numera', 'Une cada tecla del piano con su nota en el pentagrama.',
       items=ORDEN_NOTAS),
   _juego('EL ECO DEL PIANO',
          'La profe toca una nota y dice su nombre. El peke la repite en el '
          'piano haciendo eco, y luego le toca a él elegir la nota y a la '
          'profe hacer de eco.'))

_c(23, 'Mi primer examen de notas',
   'Siete notas, siete colores. Antes del gran mapa final, vamos a '
   'comprobar que ya se conocen todas de memoria.',
   ('mapa_notas', dict(hasta='SI')),
   _ej('escribe_letra', 'Escribe el nombre de cada nota debajo, sin mirar la lista.',
       filas=ORDEN_NOTAS),
   _juego('EL CONCURSO DE LAS 7 NOTAS',
          'La profe señala teclas o notas en el pentagrama al azar y pone un '
          'cronómetro de 30 segundos. El peke tiene que nombrar tantas como '
          'pueda antes de que suene la alarma, intentando superar su propio '
          'récord cada semana.'))

_c(24, '¡Mi mapa musical!',
   'Todas las notas tienen ya su lugar. ¡Vamos a construir el mapa '
   'completo, de Do a Si!',
   ('mapa_notas', dict(hasta='SI')),
   _ej('vf', 'Responde verdadero o falso sobre los colores de las notas.',
       items=['El Do es rojo.', 'El Sol es verde.', 'El Mi es amarillo.',
              'El La es gris.', 'El Si es lila.']),
   _juego('EL GLOBO DE 4',
          'La profe toca una nota muy larga en el piano mientras el peke '
          'mantiene un globo en el aire a golpecitos, contando 1-2-3-4 en '
          'voz alta. Cuando la cuenta llega a 4, atrapa el globo justo '
          'cuando la nota termina.'))

# ---- BLOQUE 4 · LAS FIGURAS Y EL COMPÁS ---------------------------------
_c(25, '¡Hola redonda, duras 4 tiempos!',
   'La redonda es la figura más larga que conocemos: una cabeza hueca, sin '
   'plica, que dura 4 tiempos completos.',
   ('figura_intro', dict(clave='w')),
   _ej('cuenta', 'Cuenta en voz alta hasta 4 cada vez que veas una redonda, dando una palmada por número.',
       figuras=['w', 'w', 'w']),
   _juego('EL GLOBO DE 4 (OTRA VEZ)',
          'Igual que la semana pasada, pero ahora el peke sabe que esa nota '
          'larga se llama redonda y dura exactamente 4 tiempos: cuenta en '
          'voz alta mientras mantiene el globo en el aire.'))

_c(26, '¡La blanca dura la mitad que la redonda!',
   'La blanca es una figura con un palito (la plica). Dura 2 tiempos: la '
   'mitad que la redonda.',
   ('figura_intro', dict(clave='h')),
   _ej('colorea', 'Colorea las redondas de verde y las blancas de naranja. Después cuenta los tiempos dando palmas.',
       figuras=['w', 'h', 'h', 'w', 'h']),
   _juego('CONGELADOS A MEDIAS',
          'La profe toca redondas y blancas mezcladas. Si suena una '
          'redonda, el peke se congela contando hasta 4; si suena una '
          'blanca, se congela contando solo hasta 2 y vuelve a moverse.'))

_c(27, '¡La negra es la más corta de las tres!',
   'La negra es una figura con su plica, y dura solo 1 tiempo: la más '
   'corta de las que ya conocemos.',
   ('figura_intro', dict(clave='q')),
   _ej('colorea', 'Colorea las redondas de verde, las blancas de naranja y las negras de azul. Cuenta los tiempos.',
       figuras=['w', 'h', 'q', 'q', 'h', 'q']),
   _juego('EL SEMÁFORO DE FIGURAS',
          'Tres tarjetas en la pared: redonda, blanca y negra. La profe '
          'levanta una y el peke da el número de palmas correcto (4, 2 o 1) '
          'lo más rápido posible.'))

_c(28, '¡Las 3 figuras son amigas!',
   'Redonda, blanca y negra son las tres figuras que ya conocemos. Cada una '
   'dura un tiempo distinto, y las tres pueden convivir en la misma canción.',
   ('tres_figuras', {}),
   _ej('cuenta', 'Resuelve: ¿cuántos tiempos suman estas figuras juntas?',
       figuras=['w', 'h', 'q', 'q']),
   _juego('EL CHEF MUSICAL',
          'Restaurante imaginario: el plato redonda tarda 4 minutos, el '
          'blanca 2 y el negra 1. La profe pide un plato y el peke cuenta '
          'el tiempo correcto en voz alta antes de "servirlo".'))

_c(29, '¡Las figuras suenan en el piano!',
   'Cada figura dura un tiempo diferente también al tocar: el dedo tiene '
   'que quedarse apoyado en la tecla hasta que se acaben sus tiempos.',
   ('tres_figuras', {}),
   _ej('escribe_letra', 'Escribe debajo de cada figura el nombre de la nota y cuánto dura.',
       filas=['Figura 1', 'Figura 2', 'Figura 3', 'Figura 4']),
   _juego('EL ROBOT Y EL DIRECTOR',
          'El peke es un robot que solo entiende tres órdenes: "redonda" (4 '
          'pasos), "blanca" (2 pasos) y "negra" (1 paso y parar). La profe '
          'da las órdenes tocando el piano.'))

_c(30, '¡El compás ordena la música!',
   'La partitura se divide en compases. Dentro de cada compás, las figuras '
   'tienen que sumar exactamente el tiempo que marca el compás.',
   ('compas', {}),
   _ej('crea', 'Coloca la línea divisoria entre compás y compás, y añade la barra final.',
       compases=4),
   _juego('LA CALLE DE LAS CAJITAS',
          'Cuatro cajitas de cinta adhesiva en el suelo, en fila, como '
          'compases. La profe da palmas con un ritmo y el peke salta de '
          'cajita en cajita; una palmada más fuerte marca línea divisoria.'))

_c(31, '¡Ya sé todo de las figuras!',
   'Redonda, blanca y negra viven dentro de los compases. Repasamos todo '
   'antes de componer nuestra primera melodía.',
   ('repaso_figuras', {}),
   _ej('vf', 'Responde verdadero o falso.',
       items=['La negra dura 1 tiempo.', 'La redonda tiene plica.',
              'Dos blancas duran lo mismo que una redonda.',
              'La barra de compás es una línea vertical.',
              'Cuatro negras duran lo mismo que una redonda.']),
   _juego('EL ARTISTA LOCO',
          'Papel grande en el suelo y pintura de dedos. La profe toca el '
          'piano y el peke dibuja libremente lo que siente: trazos grandes '
          'y lentos en lo grave, pequeños y rápidos en lo agudo.'))

_c(32, '¡Soy compositor!',
   'Una melodía es un grupo de notas que suenan una detrás de otra. Hoy '
   'compones tu primera melodía de verdad.',
   ('compositor', {}),
   _ej('crea', 'Crea una canción de 8 compases: usa al menos 3 notas distintas, las figuras que ya conoces, y respeta el tiempo de cada compás.',
       compases=8),
   _juego('EL CONCIERTO DE LAS ESTRELLAS',
          'El peke toca su melodía por primera vez en el piano mientras la '
          'profe lo grava para los papás, actuando como el mayor concertista '
          'del mundo. Termina con una reverencia.'))

# ---- BLOQUE 5 · LOS SILENCIOS -------------------------------------------
_c(33, '¡El silencio también es música!',
   'El silencio de redonda dura 4 tiempos: paras de tocar, pero sigues '
   'contando por dentro exactamente igual que con la nota.',
   ('silencio_intro', dict(clave='Rw')),
   _ej('escribe_letra', 'Escribe S (sonido) o SIL (silencio) debajo de cada figura.',
       filas=['Figura 1', 'Figura 2', 'Figura 3', 'Figura 4']),
   J_NINJA)

_c(34, 'El silencio de blanca',
   'El silencio de blanca dura 2 tiempos, la mitad que el de redonda. Se '
   'apoya sobre la línea, en vez de colgar de ella.',
   ('silencio_intro', dict(clave='Rh')),
   _ej('escribe_letra', 'Escribe S o SIL debajo de cada figura.',
       filas=['Figura 1', 'Figura 2', 'Figura 3', 'Figura 4']),
   J_NINJA)

_c(35, 'El silencio de negra',
   'El silencio de negra dura solo 1 tiempo: el más corto de los tres que '
   'ya conocemos.',
   ('silencio_intro', dict(clave='Rq')),
   _ej('escribe_letra', 'Escribe S o SIL debajo de cada figura.',
       filas=['Figura 1', 'Figura 2', 'Figura 3', 'Figura 4']),
   J_NINJA)

_c(36, '¡Ya sé los tres silencios!',
   'Redonda, blanca y negra tienen cada una su silencio. El de redonda '
   'cuelga de la línea; el de blanca se apoya encima; el de negra es el '
   'garabato pequeño.',
   ('silencio_repaso', {}),
   _ej('escribe_letra', 'Escribe S o SIL debajo de cada figura, mezclando los tres silencios.',
       filas=['Figura 1', 'Figura 2', 'Figura 3', 'Figura 4', 'Figura 5', 'Figura 6']),
   J_NINJA)

# ---- BLOQUE 6 · LAS PLICAS -----------------------------------------------
_c(37, '¡La nota tiene cola!',
   'La plica es el palito que llevan la blanca y la negra. La redonda no '
   'tiene, porque es la figura más gordota y tranquila de todas.',
   ('plica_cola', {}),
   _ej('rodea', 'Pon un círculo rojo en las notas que tienen plica, y escribe debajo qué nota es.',
       items=['Redonda', 'Blanca', 'Negra', 'Redonda', 'Negra']),
   _juego('EL ESPÍA MUSICAL',
          'Ocho tarjetas escondidas por la sala, con figuras bien y mal '
          'dibujadas. El peke es un espía que solo puede quedarse con las '
          'que tienen la plica bien colocada: tiene 3 vidas si se equivoca.'))

_c(38, '¿Plica arriba o abajo?',
   'La plica no va siempre en el mismo sitio: por debajo de la tercera '
   'línea se coloca hacia arriba y a la derecha; en la tercera línea o por '
   'encima, hacia abajo y a la izquierda.',
   ('plica_arriba_abajo', {}),
   _ej('rodea', 'Dibuja la plica hacia arriba o hacia abajo según corresponda, en cada nota.',
       items=['Nota baja', 'Nota alta', 'Nota baja', 'Nota alta']),
   _juego('ARRIBA O ABAJO CON EL GLOBO',
          'La profe dibuja una nota en el pentagrama gigante. Si la plica va '
          'arriba, el peke lanza un globo hacia el techo; si va abajo, lo '
          'lanza hacia el suelo.'))

_c(39, '¡Dibujo notas perfectas!',
   'Para dibujar una figura perfecta hacen falta dos cosas: la cabeza en la '
   'posición correcta del pentagrama, y la plica en la dirección correcta.',
   ('plica_dibujo_pasos', {}),
   _ej('crea', 'Dibuja 4 notas siguiendo los 3 pasos: 1) la cabeza en su sitio, 2) decide arriba o abajo, 3) dibuja la plica.',
       compases=4),
   _juego('EL JUEZ MUSICAL',
          'La profe muestra tarjetas con notas, algunas con la plica '
          'correcta y otras no. El peke es el juez y levanta una tarjeta '
          'verde (✓) o roja (✗) lo más rápido posible. 5 aciertos seguidos '
          'gana el caso.'))

_c(40, '¡Ya sé todo de las plicas!',
   'Redonda sin plica; blanca y negra con plica, arriba o abajo según su '
   'altura en el pentagrama. Repasamos antes del gran examen final.',
   ('plica_cola', {}),
   _ej('vf', 'Responde verdadero o falso.',
       items=['La redonda tiene plica.', 'La plica siempre va hacia arriba.',
              'Por debajo de la tercera línea la plica va hacia arriba.',
              'La negra no tiene plica.']),
   _juego('EL JUEZ MUSICAL (RÉCORD)',
          'Repite el juego de la semana pasada, pero ahora intentando '
          'superar su propio récord de aciertos seguidos.'))

# ---- BLOQUE 7 · EL GRAN REPASO Y EL CONCIERTO ---------------------------
_c(41, '¡Lo sé casi todo!',
   'Piano, pentagrama, las 7 notas con su color, las figuras, el compás, '
   'los silencios y las plicas. Repasamos todo antes del gran test.',
   ('repaso_total', {}),
   _ej('numera', 'Une cada palabra con su dibujo: redonda, blanca, negra, silencio, plica, clave de Sol.',
       items=['Redonda', 'Blanca', 'Negra', 'Silencio', 'Plica', 'Clave de Sol']),
   _juego('EL REPASO EN EQUIPO',
          'La profe y el peke se hacen preguntas por turnos sobre todo lo '
          'aprendido este curso, cada uno intentando pillar al otro con una '
          'pregunta difícil.'))

_c(42, 'El gran test final',
   'Un repaso completo de todo el curso: colores, figuras, silencios y '
   'plicas, todo mezclado.',
   None,
   _ej('test', 'Responde a las tres partes del gran test final.',
       partes=[
           dict(tipo='elige', pregunta='¿De qué color es cada nota?',
                items=['Do', 'Sol', 'Mi', 'La', 'Si']),
           dict(tipo='vf', pregunta='Verdadero o falso.',
                items=['El pentagrama tiene 5 líneas.',
                       'La negra dura 4 tiempos.',
                       'El Fa es de color verde.',
                       'La clave de Sol va al principio.',
                       'La plica siempre va hacia arriba.',
                       'Dos negras duran lo mismo que una blanca.',
                       'El Si es de color gris.']),
       ]),
   _juego('EL PROGRAMA DE RADIO',
          'El peke es el locutor estrella de una radio imaginaria y explica '
          'en voz alta, muy exagerado, todo lo que ha aprendido este curso. '
          'La profe llama por "teléfono" haciendo preguntas graciosas.'))

_c(43, '¡Mi primer concierto de piano!',
   'Antes del diploma, un recuerdo de verdad: la ficha de tu primer '
   'concierto, para guardar para siempre.',
   ('concierto', {}),
   _ej('crea', 'Completa la ficha de tu concierto: nombre del pianista, fecha, partitura, dedicatoria y una foto.',
       compases=0),
   _juego('EL ENSAYO GENERAL',
          'El peke toca su pieza del concierto de principio a fin, sin '
          'pararse aunque se equivoque, practicando cómo saludar al público '
          'antes y después de tocar.'))

_c(44, 'Felicidades, gran pianista',
   'Has terminado el curso entero: piano, pentagrama, notas, figuras, '
   'compás, silencios y plicas. ¡Es hora del diploma!',
   ('diploma', {}),
   _ej('diploma', 'Encuentra el diploma escondido superando las 5 pruebas musicales.',
       pruebas=['Toca el Do en el piano.', '¿Cuánto dura una redonda?',
               'Dibuja una nota con la plica bien colocada.',
               '¿De qué color es el Sol?', 'Canta la escalera de Do a Si.']),
   _juego('LA BÚSQUEDA DEL DIPLOMA PERDIDO',
          'La profe esconde el diploma en la sala. Para encontrarlo, el peke '
          'supera 5 pruebas musicales en forma de pistas. Al encontrarlo: '
          'música festiva, entrega solemne, ¡y un abrazo de felicitación!'))


assert len(CLASES) == 44, 'faltan o sobran semanas: %d' % len(CLASES)
assert [c['n'] for c in CLASES] == list(range(1, 45))
