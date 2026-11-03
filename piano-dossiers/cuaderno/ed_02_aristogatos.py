# -*- coding: utf-8 -*-
"""Los Aristogatos — pieza 2 de Eduard. Formato ADULTO.

   OJO CON EL NOMBRE DEL FICHERO. En su carpeta este PDF se llama "Escalas y
   Arpegios Facil progresando.pdf" y no es un cuaderno de escalas: dentro pone
   *Los aristogatos*, de Richard y Robert Sherman, arreglo de A. C. Escobes.
   Creerse el nombre habria puesto una hoja de tecnica donde hay una cancion.

   Medido sobre ESE PDF (vectorial, 1 pagina):

     - 4/4 y detras de la clave no hay nada: todo teclas blancas.
     - UN SOLO PENTAGRAMA otra vez. La izquierda sigue descansando.
     - Arriba pone **Adagio** y debajo **mf**.
     - La melodia del principio, medida a 300 ppp:

         c. 1   silencio de blanca · Sol4 · La4 · Si4 · Do5   (cuatro corcheas)
         c. 2   Si4 · Sol4 · Sol4                             (negra, negra, blanca)

     - Lo que la hace util aqui: **empieza callada**. Dos tiempos de silencio
       antes de la primera nota. Despues de la anacrusa de Clementine, esta es
       la otra mitad de la misma leccion — que el compas corre aunque no suene
       nada.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, sil, corch, plan, metronomo, objetivo, figuras,
                      rodear, escribir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1, medido. Cita literal.
ARRANQUE = [sil('h')] + corch(['G4', 'A4', 'B4', 'C5'])

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=2, nivel='iniciación',
    slug='Aristogatos', formato='adulto',
    titulo_corto='Los Aristogatos', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Los Aristogatos.pdf'),
    yt='https://www.youtube.com/results?search_query=aristogatos+piano+facil',

    ficha=dict(
        titulo='Los Aristogatos',
        autor='Richard y Robert Sherman · arreglo de A. C. Escobés',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Manos', 'Solo la derecha'), ('Carácter', 'Adagio'),
               ('Volumen', 'mf')],
        titulo_ritmos='Así empieza',
        pie_ritmos='El primer compás, medido en tu partitura. Fíjate en que las dos primeras '
                   'partes son de silencio.',
        armonia=dict(
            titulo='Empieza callada, y sube por escalones',
            tarjetas=[
                ('EL SILENCIO', 'Dos tiempos',
                 'La pieza empieza con un silencio de blanca: dos golpes en los que hay que '
                 'contar sin tocar. El compás corre igual aunque no suene nada.'),
                ('LA SUBIDA', 'Sol · La · Si · Do',
                 'Cuatro teclas seguidas, sin saltarse ninguna. La mano no se abre: los dedos '
                 'van uno detrás de otro.'),
                ('ADAGIO', 'Despacio',
                 'Es una palabra italiana y quiere decir lento. No es una cifra de metrónomo: '
                 'es un carácter, y aquí te viene de regalo.'),
                ('MF', 'Medio fuerte',
                 'Mezzo forte. Ni muy fuerte ni muy suave: el volumen de hablar normal.'),
            ],
            pie='Toda esta primera frase cabe en cinco teclas blancas seguidas. Lo único que hay '
                'que aprender de verdad es a contar los dos tiempos que no suenan.',
        ),
        ritmos=[
            ('LA DERECHA', 'el compás 1, medido · empieza callada',
             ARRANQUE, OCRE, 'treble', None),
            ('Y EL SIGUIENTE', 'el compás 2, medido · y se queda quieta',
             [n('B4'), n('G4'), n('G4', 'h')], AZUL, 'treble', None),
        ],
        especial=[
            'Un solo pentagrama: la izquierda todavía no toca.',
            'Empieza con un silencio de blanca: dos tiempos callado.',
            'Compás de 4/4: cuatro golpes por compás.',
            'No hay ni un sostenido ni un bemol.',
            'Arriba pone "Adagio": despacio.',
            'Debajo del pentagrama pone "mf": ni fuerte ni suave.',
        ],
        reto='Contar el silencio. Un silencio no es un descanso ni un hueco para pensar: dura lo '
             'que dura y hay que contarlo igual que si sonara.',
        truco='Toca los dos tiempos de silencio en la tapa del piano, con la mano izquierda, '
              'mientras cuentas. Cuando lo tengas, deja de dar los golpes pero sigue contándolos '
              'igual de fuerte por dentro.',
        sabias='Los hermanos Sherman escribieron también la música de Mary Poppins y de El libro '
               'de la selva. Trabajaban los dos en la misma habitación, uno al piano y otro con '
               'el lápiz, y discutían por cada compás.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuatro golpes con el pie desde el principio: verás que la primera '
                      'nota entra en el tres.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas, y ninguna es de dedos: un silencio que hay que contar y una '
              'subida de cuatro teclas seguidas. Se trabajan por separado.',
        reglas=['EL SILENCIO SE CUENTA', 'CUATRO GOLPES POR COMPÁS',
                'ADAGIO: NO HAY NINGUNA PRISA'],
        bloques=[
            dict(num=1, titulo='Contar cuatro, y callar dos',
                 pista='andamio en Do mayor · el silencio es la mitad del ejercicio',
                 sistemas=[
                     dict(cap='a) dos tiempos callado y dos tocando · cuenta en voz alta',
                          events=[sil('h'), n('C4'), n('D4'),
                                  sil('h'), n('E4'), n('D4')],
                          bars=2),
                     dict(cap='b) y ahora al revés: tocas primero y callas después',
                          events=[n('C4'), n('D4'), sil('h'),
                                  n('E4'), n('D4'), sil('h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ UN SILENCIO NO ES UN DESCANSO',
                 texto='Cuando el papel dice silencio, el compás sigue corriendo exactamente '
                       'igual: lo único que cambia es que no suena nada. Un silencio mal contado '
                       'estropea la pieza más que una nota mal tocada, porque descoloca todo lo '
                       'que viene detrás. Cuéntalos igual de alto que las notas.'),
            dict(num=2, titulo='La subida del principio',
                 pista='c. 1 · medido en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) primero las cuatro teclas en negras, para verlas · en mf, que es '
                              'lo que pide tu partitura',
                          events=[n('G4'), n('A4'), n('B4'), n('C5')],
                          matiz='mf',
                          bars=1),
                     dict(cap='b) y ahora en corcheas, de dos en dos, sin el silencio delante',
                          events=corch(['G4', 'A4']) + corch(['B4', 'C5']) + [n('C5', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Y lo que hace después',
                 pista='c. 2 · medido · la mano se queda donde estaba',
                 sistemas=[
                     dict(cap='a) baja de Si a Sol y se queda · repítelo cuatro veces seguidas',
                          events=[n('B4'), n('G4'), n('G4', 'h'),
                                  n('B4'), n('G4'), n('G4', 'h')],
                          bars=2),
                     dict(cap='b) y enlazado con la subida, que es la frase entera',
                          events=corch(['G4', 'A4']) + corch(['B4', 'C5']) +
                                 [n('B4'), n('G4'), n('G4', 'w')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Los Aristogatos · para casa',
            intro='Quince minutos al día. Esta semana lo que se aprende es a contar los silencios, '
                  'que es lo que más falta hace y lo que menos apetece.',
            bloques=[
                plan((4, 'Contar cuatro golpes en voz alta, con el pie, sin tocar'),
                     (4, 'El silencio de blanca: dos callados y dos tocando'),
                     (4, 'La subida Sol-La-Si-Do, despacio y con los dedos seguidos'),
                     (3, 'Los dos primeros compases enteros')),
                metronomo('Empieza a ♩ = 54, que es lo que pide un Adagio.',
                          'Aquí no hay que subir de velocidad: hay que contar bien.'),
                objetivo('Que los dos tiempos de silencio duren exactamente dos tiempos. Ni uno '
                         'más porque te lo piensas, ni uno menos porque tienes ganas de empezar.'),
                figuras(['Rh', 'e', 'q', 'h'],
                        titulo='Escribe cuánto vale cada una',
                        pista='en golpes · la primera es la que abre tu pieza'),
                rodear([[n('G4'), n('A4'), n('B4'), n('C5')],
                        [n('G4'), n('A4'), n('C5'), n('B4')],
                        [n('G4'), n('A4'), n('B4'), n('C5')],
                        [n('A4'), n('B4'), n('C5'), n('D5')]],
                       titulo='Rodea los dos grupos que son iguales',
                       pista='uno de ellos es la subida de tu compás 1'),
                escribir(titulo='Copia aquí el compás 1 de tu partitura',
                         pista='con su silencio delante · y luego tócalo cinco veces'),
                para_clase('Los dos primeros compases y, sobre todo, el silencio. Si se te hace '
                           'largo o corto, dilo en clase: es lo normal la primera semana.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 62, 'G4', 'C3',
    'la mano en Sol, que es donde arranca la melodía',
    desde=4, time_sig=(4, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
