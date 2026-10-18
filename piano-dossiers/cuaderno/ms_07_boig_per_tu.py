# -*- coding: utf-8 -*-
"""Pieza 7 · Boig per tu (Sau), arreglo de Pilar Sanz ("Arranj. Pilar Sanz" impreso). MEDIDO sobre
   el PDF (1 pagina, imagen de baja resolucion con marca de agua de solfejos que se ignora; 26
   compases en 6 sistemas de 5, 5, 5, 5, 3 y 3): sin armadura, 4/4, sin tempo ni matices, sin
   repeticiones, corchea como figura mas corta. Armonia leida sobre el papel: empieza y acaba en
   Sol-Si (Sol mayor), con Sol-Do y La-Do en la izquierda; c. 7 Fa-Do y Sol-Do; c. 8 cuatro negras
   La-Do bajo un acorde Re-Fa# (dominante); el Fa# va escrito como alteracion (cc. 8, 17, 18, 21,
   22) y el Fa es natural en el c. 7. La derecha entra en el «y» del 2 (silencio de negra con
   puntillo). Los cc. 9-10 y 11-12 repiten los cc. 1-2; 13-14 y 24-25 repiten 5-6."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from mayores_motor import *                                        # noqa: F401,F403

SPEC = dict(
    num=7, slug='boig_per_tu', pdf='boig_per_t.pdf', time_sig=(4, 4),
    titulo='Boig per tu', autor='Sau · canción catalana · arreglo de Pilar Sanz',
    kicker='Sharifa · pieza 7 · Boig per tu', mes='Marzo · 1.ª quincena',
    yt='https://www.youtube.com/results?search_query=sau+boig+per+tu',
    credito='Partitura: Sau, «Boig per tu», arranj. Pilar Sanz. Anotaciones: T-Clas.',
    ficha=FICHA(
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'), ('Tempo', 'Sin indicar'),
               ('Figura corta', 'Corchea'), ('Compases', '26')],
        total=26,
        secciones=[('A', 1, 8, 'La frase y su cierre', AZUL), ('B', 9, 15, 'Vuelve', OCRE),
                   ('C', 16, 23, 'Parte nueva · Fa♯', AZUL), ('D', 24, 26, 'Final', OCRE)],
        ideas=[('IZQUIERDA', 'Dos notas largas',
                'Una redonda de dos notas por compás: Sol-Si, Sol-Do o La-Do. Casi no se mueve.'),
               ('DERECHA', 'Entra en el «y»',
                'Empieza con un silencio de negra con puntillo y entra en el «y» del 2.º tiempo.'),
               ('EL RITMO', 'Notas largas y ligadas',
                'Negras con puntillo, notas ligadas y una negra que empieza a mitad de tiempo.'),
               ('EL FA♯', 'Una tecla negra',
                'No hay armadura: el Fa♯ va escrito cada vez (cc. 8, 17, 18, 21 y 22).')],
        especial=[
            'No lleva armadura ni tempo. Empieza y acaba con el acorde de Sol: Sol mayor.',
            'Compás de 4/4: cuatro negras por compás.',
            'La derecha entra en el «y» del 2: silencio de negra con puntillo y corchea.',
            'Fa♯ escrito en los cc. 8, 17, 18, 21 y 22. En el c. 7 el Fa es natural.',
            'No hay repeticiones ni casillas: se toca de seguido, hasta el c. 26.',
            'La izquierda cambia más en los cc. 7 y 8: dos acordes y luego cuatro negras.'],
        reto='Entrar en el «y» del 2 y mantener la negra que empieza a mitad de tiempo, sin '
             'atropellar.',
        truco='Canta la melodía en voz baja con la letra que conozcas: el ritmo de la canción '
              'es el de tu mano derecha.',
        sabias='«Boig per tu» significa «loco por ti». Es una de las canciones más conocidas de '
               'Sau, un grupo catalán de pop de los años 90; la escribió su cantante, Carles '
               'Sabater.',
        qr_texto='Escúchala y marca el pulso: ¿cuándo entra la melodía?', ts=(4, 4)),
    manos=dict(
        izq=[('Dos notas, una redonda', 'Toca Sol-Si y aguanta cuatro tiempos. Luego Sol-Do y '
                                        'La-Do. Cuenta 1-2-3-4.'),
             ('El orden', 'Cc. 1-4: Sol-Si, Sol-Do, Sol-Si, Sol-Do. Repítelo hasta que salga '
                          'sin mirar.'),
             ('Los cc. 7 y 8', 'C. 7: dos acordes de dos tiempos, Fa-Do y Sol-Do. C. 8: '
                               'cuatro negras, La-Do.'),
             ('De memoria', 'Aprende la izquierda de memoria: casi todo se repite.')],
        der=[('Cantar antes', 'Canta o tararea la melodía de los cc. 1-4 antes de tocarla.'),
             ('Entrar en el «y»', 'Silencio de negra con puntillo y entras en el «y» del 2: '
                                  'Sol-Si-Do-Re.'),
             ('Las notas largas', 'C. 2: Re largo, Mi ligado y Sol largo. Respira en las notas '
                                  'largas.'),
             ('Con la izquierda', 'Junta cuatro compases cada vez. Si te pierdes, vuelve a una '
                                  'sola mano.')],
        tecnica=['Muñeca suelta y dedos curvos: acordes sin apretar.',
                 'La izquierda suena suave y la derecha canta por encima.',
                 'Cuenta 1-2-3-4 en voz alta, también en los silencios.']),
    bloques=[
        B(1, 'cc. 1-5', 'La frase', (0, 0),
          D('cadena', 'Las notas del c. 1',
            [('silencio', False), ('Sol', False), ('Si', False), ('Do', False), ('Re', True)]),
          [('IZQUIERDA', 'Sol-Si, Sol-Do, Sol-Si, Sol-Do: una redonda por compás.'),
           ('DERECHA', 'Entras en el «y» del 2: Sol-Si-Do-Re. C. 2: Re largo, Mi ligado, Sol.'),
           ('JUNTAS', 'Los cc. 1-2 en bucle y luego los cc. 3-4: son iguales.'),
           ('OJO', 'El c. 5 cambia: La-Do en la izquierda y Do-Do-Do-Si en la derecha.')]),
        B(2, 'cc. 6-10', 'El cierre y la vuelta', (1, 1),
          D('cadena', 'La frase se cierra',
            [('c. 7', False), ('c. 8 · acorde con Fa♯', False), ('c. 9 · vuelve el inicio', True)]),
          [('IZQUIERDA', 'C. 6: Sol-Do larga. C. 7: Fa-Do y Sol-Do. C. 8: cuatro negras, La-Do.'),
           ('DERECHA', 'C. 6: La, Sol ligado, Mi-Sol. C. 7: dos notas a la vez. C. 8: acorde '
                       'y silencio.'),
           ('JUNTAS', 'Los cc. 5-8 como una sola frase; descansa en el silencio del c. 8.'),
           ('OJO', 'En el c. 8 aparece el Fa♯: una tecla negra. Los cc. 9-10 son los cc. 1-2.')]),
        B(3, 'cc. 11-15', 'Vuelve la frase', (2, 2),
          D('cadena', 'Es el principio',
            [('cc. 11-12 = 1-2', False), ('c. 13 = 5', False), ('c. 14 = 6', False),
             ('c. 15 · Sol largo', True)]),
          [('IZQUIERDA', 'Sol-Si, Sol-Do, La-Do, Sol-Do y Sol-Si: una redonda por compás.'),
           ('DERECHA', 'Repite los cc. 1, 2, 5 y 6. El c. 15 acaba en Sol largo.'),
           ('JUNTAS', 'Si sabes los cc. 1-6, ya sabes estos.'),
           ('OJO', 'El c. 15 es una redonda: cuéntala entera, 1-2-3-4.')]),
        B(4, 'cc. 16-20', 'La parte nueva', (3, 3),
          D('cadena', 'Los pasos de la derecha',
            [('Re-Si-Re-Si-Re', False), ('Mi-Mi-Fa♯', False), ('Sol-Fa♯-Mi-Re-Mi', False),
             ('Re largo', True)]),
          [('IZQUIERDA', 'Sol-Si en el c. 16, Sol-Do en los cc. 17-18 y Sol-Si en los cc. 19-20.'),
           ('DERECHA', 'Pasos pequeños: Re-Si-Re-Si-Re. Fa♯ en los cc. 17 y 18.'),
           ('JUNTAS', 'Los cc. 16-19 y luego el c. 20, que repite el 16.'),
           ('OJO', 'Mi-Fa♯-Sol sube y Sol-Fa♯-Mi baja: la tecla negra va entre medias.')]),
        B(5, 'cc. 21-23', 'Otra vez', (4, 4),
          D('cadena', 'Igual que antes',
            [('c. 21 = 17', False), ('c. 22 = 18', False), ('c. 23 · cierre', True)]),
          [('IZQUIERDA', 'Sol-Do en los cc. 21-22 y Sol-Si en el c. 23.'),
           ('DERECHA', 'Cc. 21-22 como 17-18. C. 23: Re largo, Sol, La, Re largo.'),
           ('JUNTAS', 'Los tres compases seguidos, sin parar.'),
           ('OJO', 'El c. 23 prepara el final: Sol-La y vuelve al Re.')]),
        B(6, 'cc. 24-26', 'El final', (5, 5),
          D('cadena', 'Como los cc. 5-6',
            [('c. 24 = 5', False), ('c. 25 = 6', False), ('c. 26 · Sol largo', True)]),
          [('IZQUIERDA', 'La-Do en el c. 24, Sol-Do en el 25 y Sol-Si en el 26, todas largas.'),
           ('DERECHA', 'Casi igual que los cc. 5-6. El c. 26 es un Sol largo.'),
           ('JUNTAS', 'Los tres compases seguidos.'),
           ('A TEMPO', 'La pieza entera, sin parar, una vez al día.')]),
    ],
    cortes={1: [209.8, 336.0, 452.5, 560.5, 668.5]},
    corte_titulo=100.2,
    burb={
        0: [('arriba', 300, 'DER', 'Entras en el «y» del 2.º tiempo: Sol-Si-Do-Re. Cuenta '
                                   '1-2-3-4 antes de entrar.', 0.15),
            ('abajo', 300, 'IZQ', 'Sol-Si, Sol-Do, Sol-Si, Sol-Do: una redonda por compás.',
             0.2)],
        1: [('arriba', 330, 'OJO', 'C. 7: dos acordes de dos tiempos. C. 8: cuatro negras a la '
                                   'izquierda y un acorde con Fa♯.', 0.6),
            ('abajo', 300, 'AMB', 'Los cc. 9-10 repiten los cc. 1-2: ya los conoces.', 0.85)],
        2: [('arriba', 300, 'AMB', 'Los cc. 11-12 son otra vez el inicio y los cc. 13-14 repiten '
                                   'los cc. 5-6.', 0.2)],
        3: [('arriba', 300, 'DER', 'Parte nueva: Re-Si-Re-Si-Re, pasos pequeños, sin saltos.',
             0.15),
            ('abajo', 300, 'OJO', 'Fa♯ en los cc. 17 y 18: la tecla negra a la derecha del Fa.',
             0.45)],
        4: [('arriba', 300, 'OJO', 'Los cc. 21-22 repiten los cc. 17-18: otra vez el Fa♯.', 0.3)],
        5: [('arriba', 330, 'AMB', 'Final: se parece a los cc. 5-6. El último Sol dura los '
                                   'cuatro tiempos: no sueltes antes.', 0.9)],
    },
    marcas=[],
    pie_pauta='la clave la pones tú · copia el c. 1 o escribe la escala de Sol mayor')

if __name__ == '__main__':
    wr, n = construir_pieza(SPEC, 1)
    dst = os.path.join(OUT, 'TEST_boig_per_tu.pdf')
    with open(dst, 'wb') as f:
        wr.write(f)
    print(n, 'paginas', dst)
