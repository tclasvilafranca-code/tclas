# -*- coding: utf-8 -*-
"""I Have a Dream, de Abba — pieza 6 de Luisa. Formato adulto, iniciación.

   Lo comprobado sobre el PDF de su carpeta de Drive (INeVENT Music Academy,
   2 páginas, con la letra debajo):

     - Detrás de la clave no hay nada: Do mayor.
     - 4/4, y pone "TEMPO-120".
     - La izquierda hace redondas, unas de una nota y otras de dos.
     - La derecha lleva la melodía con negras, negras con puntillo y redondas,
       y entra DESPUÉS de un silencio de negra en casi todas las frases.
     - Lleva la letra escrita debajo del pentagrama, sílaba a sílaba.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import sistemas_extra
from lu_comun import n, ac, sil

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=6, nivel='iniciación', slug='IHaveADream',
    formato='adulto',
    titulo_corto='I Have a Dream', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source',
                           'i-have-a-dream-abba-children-song.pdf'),
    yt='https://www.youtube.com/results?search_query=i+have+a+dream+abba+piano+easy',

    ficha=dict(
        titulo='I Have a Dream',
        autor='Abba · edición de INeVENT Music Academy',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 120'), ('Izquierda', 'Redondas'),
               ('Páginas', 'Dos')],
        titulo_ritmos='La melodía entra tarde',
        pie_ritmos='Andamio en Do mayor. Lo literal es la forma: silencio de negra y después la '
                   'melodía, con redondas abajo. Las notas exactas están en tu partitura.',
        armonia=dict(
            titulo='Lo nuevo: no se entra en el uno',
            tarjetas=[
                ('EL SILENCIO', 'Del primer golpe',
                 'Casi todas las frases empiezan con un silencio de negra: el compás arranca y tú '
                 'todavía no tocas. Hay que contar el uno igual, aunque esté callado.'),
                ('LA LETRA', 'Debajo',
                 'La canción viene con la letra escrita, sílaba a sílaba. Cántala mientras miras la '
                 'partitura: te dice sola dónde entra cada nota.'),
                ('LA IZQUIERDA', 'Redondas',
                 'Sigue haciendo redondas, unas de una nota y otras de dos. Ya lo has hecho las dos '
                 'semanas anteriores.'),
                ('♩ = 120', 'Con número',
                 'Esta sí trae velocidad escrita. No hay que empezar ahí: hay que llegar.'),
            ],
            pie='La izquierda es la de siempre y la derecha tiene una cosa nueva, entrar tarde. Es '
                'el reparto de trabajo que mejor funciona: una mano hace lo conocido y la otra '
                'aprende una cosa sola.',
        ),
        ritmos=[
            ('MANO DERECHA', 'silencio, y entonces la melodía · literal',
             [sil('q'), n('C4'), n('E4', 'q.'), n('D4', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una redonda por compás · andamio',
             [n('C3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4 y "TEMPO-120" escrito arriba.',
            'Casi todas las frases empiezan con un silencio de negra.',
            'La izquierda hace redondas, unas de una nota y otras de dos.',
            'La letra está escrita debajo del pentagrama, sílaba a sílaba.',
            'La canción ocupa dos páginas.',
        ],
        reto='Entrar después del silencio, en el segundo golpe y no en el primero. Cuando una mano '
             'no toca en el uno, lo normal es adelantarse.',
        truco='Cuenta los cuatro golpes en voz alta con las manos quietas, dos compases enteros, y '
              'entra al tercero. Si cuentas en voz alta no te vas a adelantar: la voz no miente.',
        sabias='Abba grabó esta canción en 1979 con un coro de niños de un colegio de Estocolmo. La '
               'usaron porque el estudio estaba al lado y les salía más barato que traer un coro '
               'profesional.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que la voz entra un poquito después de que empiece el compás. Ese '
                      'huequito es tu silencio de negra.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana todo es contar. Las notas ya las sabes leer; lo que hay que aprender es '
              'cuándo entra cada una.',
        reglas=['CUENTA EN VOZ ALTA, SIEMPRE', 'EL SILENCIO TAMBIÉN SE CUENTA',
                'CANTA LA LETRA MIENTRAS MIRAS'],
        bloques=[
            dict(num=1, titulo='Entrar después del silencio',
                 pista='andamio en Do mayor · el silencio del primer golpe es literal',
                 sistemas=[
                     dict(cap='a) cuenta "un" con la mano quieta y entra en el "dos"',
                          events=[sil('q'), n('C4'), n('E4'), n('D4'),
                                  sil('q'), n('E4'), n('G4'), n('E4')],
                          bars=2),
                     dict(cap='b) y con la nota larga al final · el silencio vuelve a estar en el uno',
                          events=[sil('q'), n('G4'), n('F4'), n('E4'), n('D4', 'w')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='UN SILENCIO NO ES UN DESCANSO',
                 texto='El silencio dura exactamente lo mismo que la nota que ocuparía su sitio: un '
                       'silencio de negra dura un golpe. No es "esperar un poco", es contar uno. '
                       'Si lo cuentas, entras bien siempre; si lo esperas a ojo, cada vez entras en '
                       'un sitio distinto.'),
            dict(num=2, titulo='La izquierda, que ya sabes', clef='bass',
                 pista='andamio · redondas, unas de una nota y otras de dos',
                 sistemas=[
                     dict(cap='a) de una nota, como en la pieza 4',
                          events=[n('C3', 'w'), n('A2', 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) y de dos notas, como en la pieza 5 · en esta canción salen las dos',
                          events=[ac(('F2', 'C3'), 'w'), ac(('G2', 'D3'), 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, con el silencio en su sitio',
                 pista='andamio · la izquierda entra en el uno y la derecha en el dos',
                 sistemas=[
                     dict(cap='a) abajo se toca en el uno, arriba no · esa es toda la dificultad',
                          events=[n('C3', 'q'), ac(('C3', 'C4')), n('E4'), n('D4'),
                                  n('A2'), ac(('A2', 'E4')), n('G4'), n('E4')],
                          bars=2),
                     dict(cap='b) y con la izquierda aguantando la redonda entera por debajo',
                          events=[ac(('F2', 'C3'), 'q'), n('A4'), n('G4'), n('F4'),
                                  ac(('G2', 'D3'), 'q'), n('E4'), n('D4', 'h')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('Do mayor', 'C4', 'G2', time_sig=(4, 4), variante=15,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
