# -*- coding: utf-8 -*-
"""EL LIBRO DE PEKES — contenido.

   Tercer intento, y el bueno en cuanto a forma: el cliente descarto los dos
   disenos propios ("todo el diseno en general es feo") y pidio usar EL MISMO
   MOTOR Y EL MISMO ASPECTO de los albumes de alumno, solo que "un poco mas
   infantil, resumido, didactico, y que realmente sea para ninos".

   Estructura (lo que pidio antes y sigue en pie):
   - un libro de teoria y ejercicios, SIN semanas ni dias pautados: la
     profesora lo va usando a su ritmo;
   - cada tema son TRES hojas: teoria, al piano y ficha;
   - Musol Misol, el buho del Canva original, sale en todas.

   El orden de los capitulos es el de "La ruta musical" del propio Canva del
   cliente (antes de tocar · pentagrama y clave de Sol · las notas y sus
   colores · las figuras · los silencios · las plicas · escalera musical),
   resumido a 17 temas en vez de las 44 clases del original.

   De momento solo esta escrito el tema de MUESTRA (Do, Re y Mi). El resto
   se escribe cuando el cliente apruebe la muestra.
"""

CAPITULOS = [
    ('Antes de tocar', 'conocer el piano y las manos', [
        (1, 'El piano y sus partes'),
        (2, 'Mis manos y mis dedos'),
        (3, 'Grave y agudo'),
        (4, 'El Do, nuestra casa'),
    ]),
    ('El pentagrama y la clave de Sol', 'la casa donde viven las notas', [
        (5, 'La casa de las notas'),
        (6, 'Líneas y espacios'),
        (7, 'La clave de Sol'),
    ]),
    ('Las notas y sus colores', 'una a una, en el piano y en el papel', [
        (8, 'Do, Re y Mi'),
        (9, 'Fa y Sol'),
        (10, 'La y Si'),
        (11, 'Las siete notas'),
    ]),
    ('Las figuras', 'lo que dura cada nota', [
        (12, 'Redonda, blanca y negra'),
        (13, 'El compás'),
    ]),
    ('Los silencios', 'cuando no se toca, también se cuenta', [
        (14, 'Los tres silencios'),
    ]),
    ('Las plicas', 'el palito de las notas', [
        (15, 'Plica arriba, plica abajo'),
    ]),
    ('La escalera musical', 'todo junto', [
        (16, 'De Do a Do'),
        (17, 'El gran repaso y mi primer concierto'),
    ]),
]

HOJAS_POR_TEMA = 3
PRIMERA_PAGINA_TEMAS = 3        # 1 portada · 2 indice


def pagina_de(n_tema):
    return PRIMERA_PAGINA_TEMAS + (n_tema - 1) * HOJAS_POR_TEMA


def capitulo_de(n_tema):
    for i, (nombre, _sub, temas) in enumerate(CAPITULOS, 1):
        if any(n == n_tema for n, _t in temas):
            return i, nombre
    raise ValueError(n_tema)


def m(p, d='q'):
    """Una nota de la mano derecha. Sin numero de dedo encima: norma del
       proyecto, los dedos no se imprimen nunca en el pentagrama (los escribe
       el alumno). Donde va cada dedo lo dice el texto y el teclado dibujado."""
    return {'pitch': p, 'dur': d}


TEMAS = {
    8: dict(
        titulo='Do, Re y Mi',
        teoria=dict(
            intro='Nuestras tres primeras notas. Viven juntas en el piano y juntas en el '
                  'pentagrama: una al lado de la otra, como tres escalones.',
            reglas=['DO · RE · MI', 'SUBEN COMO UNA ESCALERA', 'CADA UNA CON SU DEDO'],
            bloques=[
                dict(tipo='misol',
                     texto='¡Hola! Hoy conocemos a tres amigas que siempre van juntas: Do, Re '
                           'y Mi. Si sabes dónde vive el Do, las otras dos están justo al lado.'),
                dict(tipo='teclado', titulo='En el piano', teclas=10,
                     marcas={0: 'dedo 1', 1: 'dedo 2', 2: 'dedo 3'},
                     pie='El Do está justo a la izquierda de las dos teclas negras. El Re, entre '
                         'las dos negras. Y el Mi, justo a su derecha.'),
                dict(tipo='pentagrama', titulo='En el pentagrama',
                     notas=[('C4', 'Do'), ('D4', 'Re'), ('E4', 'Mi')],
                     pie='Cada nota está un escalón más arriba que la anterior: en el papel '
                         'suben igual que en el piano.'),
                dict(tipo='tarjetas', titulo='Las tres, una a una', items=[
                    ('DEDO 1', 'Do', 'Lleva una rayita que le cruza por la mitad. En el piano, a '
                                     'la izquierda de las dos negras.'),
                    ('DEDO 2', 'Re', 'Se cuelga justo debajo del pentagrama, sin rayita. En el '
                                     'piano, entre las dos negras.'),
                    ('DEDO 3', 'Mi', 'La primera línea le pasa por la barriga. En el piano, a '
                                     'la derecha de las dos negras.'),
                ]),
                dict(tipo='sabias',
                     texto='Los nombres Do, Re, Mi vienen de una canción de hace más de mil '
                           'años: cada nota empezaba con una sílaba de una frase en latín. ¡Y al '
                           'principio el Do no se llamaba Do, sino «Ut»!'),
            ],
        ),
        piano=dict(
            intro='Ahora a tocar de verdad. Mano derecha, y cada dedo encima de su tecla: el 1 '
                  'en el Do, el 2 en el Re y el 3 en el Mi.',
            reglas=['MANO DERECHA', 'DEDO 1 EN EL DO', 'DESPACITO Y CANTANDO'],
            bloques=[
                dict(tipo='misol',
                     texto='Antes de tocar, pon los tres dedos encima de sus teclas y déjalos '
                           'ahí. ¡Los dedos no se mueven de su casa en toda la hoja!'),
                dict(num=1, titulo='Subir y bajar la escalera',
                     pista='canta el nombre de cada nota mientras la tocas',
                     sistemas=[
                         dict(cap='a) subimos y bajamos, muy despacio',
                              events=[m('C4'), m('D4'), m('E4'), m('D4'), m('C4', 'w')],
                              bars=2),
                         dict(cap='b) y ahora con notas largas · las de cabeza hueca duran dos golpes',
                              events=[m('C4', 'h'), m('D4', 'h'), m('E4', 'h'), m('D4', 'h'),
                                      m('C4', 'w')],
                              bars=3, show_time=False),
                     ]),
                dict(tipo='nota', etiqueta='CÓMO SABER SI LO ESTÁS HACIENDO BIEN',
                     texto='Si para tocar el Mi tienes que mover la mano, es que no estaba bien '
                           'puesta: vuelve a dejar el dedo 1 en el Do y empieza otra vez.'),
                dict(num=2, titulo='Mi primera canción con tres notas',
                     pista='Hot Cross Buns · canción popular inglesa, simplificada',
                     sistemas=[
                         dict(cap='solo Do, Re y Mi · fíjate: empieza ARRIBA, en el Mi',
                              events=[m('E4'), m('D4'), m('C4', 'h'),
                                      m('E4'), m('D4'), m('C4', 'h'),
                                      m('C4'), m('C4'), m('D4'), m('D4'),
                                      m('E4'), m('D4'), m('C4', 'h')],
                              bars=4),
                     ]),
                dict(tipo='nota', etiqueta='UN JUEGO CON LA PROFE: EL ECO',
                     texto='La profe toca tres notas (solo Do, Re y Mi) y tú las repites como un '
                           'eco. Luego cambiáis: tocas tú y la profe hace de eco.'),
            ],
        ),
        ficha=dict(
            intro='Coge un lápiz y tus colores. Todo lo de esta hoja es de Do, Re y Mi.',
            bloques=[
                dict(tipo='misol',
                     texto='En este libro cada nota tiene su color: el Do es ROJO, el Re es '
                           'NARANJA y el Mi es AMARILLO. ¡Cuando veas una, píntala!'),
                dict(tipo='nombres', titulo='¿Cómo se llama cada nota?',
                     notas=['C4', 'E4', 'D4', 'C4', 'E4', 'D4', 'E4', 'C4'],
                     pista='escribe Do, Re o Mi en la cajita · y luego píntala de su color'),
                dict(tipo='teclado', titulo='Busca en el teclado', teclas=15,
                     pista='hay más de un Do, de un Re y de un Mi',
                     preguntas=['Pinta de ROJO todos los Do que encuentres.',
                                'Pinta de NARANJA todos los Re.',
                                'Pinta de AMARILLO todos los Mi.']),
                dict(tipo='une', titulo='Une cada nota con su sitio',
                     pares=[('Do', ''), ('Re', ''), ('Mi', '')],
                     derecha=['entre las dos teclas negras',
                              'a la derecha de las dos negras',
                              'a la izquierda de las dos negras']),
                dict(tipo='adivina', titulo='Adivina quién soy', items=[
                    ('Soy la primera de las tres y llevo una rayita.', 'DO'),
                    ('Vivo en medio, entre el Do y el Mi.', 'RE'),
                    ('La primera línea me pasa por la barriga.', 'MI'),
                ]),
                dict(tipo='escucha', titulo='UN JUEGO, CON ALGUIEN DE CASA',
                     texto='Canta Do-Re-Mi subiendo y Mi-Re-Do bajando, sin decir cuál haces. '
                           'Quien esté contigo dice si subes o bajas. ¡Cinco veces cada uno!'),
            ],
        ),
    ),
}
