"""Construye el cuaderno completo de Luisa: portada + los dosieres de cada
   cancion, en un unico PDF. Vuelve a generar cada dosier (llamando a su
   build.py) para asegurarse de que el album refleja siempre la ultima
   version, y luego los une con la portada delante."""
import sys, os, importlib.util

HERE = os.path.dirname(__file__)
ENGINE = os.path.join(HERE, '..', '..', 'engine')
ASSETS = os.path.join(HERE, '..', '..', 'assets')
OUT_DIR = os.path.join(HERE, '..', '..', 'output')
sys.path.insert(0, ENGINE)

from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_portada_generic import build_portada, W, H

ALUMNO = 'Luisa'
SUBTITLE = 'Nivel hobby, sin agobios · Curso 2026-2027'

SONGS = [
    ('01_bela_ciao', 'Luisa_01_Bela_Ciao.pdf',
     dict(num=1, title='Bela Ciao', subtitle='La Casa de Papel · arr. Anderson Miranda Fernandes',
          tonalidad='Sol mayor', dificultad=1)),
    ('02_we_wish_you_merry_christmas', 'Luisa_02_We_Wish_You_A_Merry_Christmas.pdf',
     dict(num=2, title='We Wish You a Merry Christmas', subtitle='Villancico tradicional · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('03_spring_vivaldi', 'Luisa_03_Spring_Vivaldi.pdf',
     dict(num=3, title='Spring (easy)', subtitle='From the Four Seasons · Antonio Vivaldi',
          tonalidad='Do mayor', dificultad=1)),
    ('04_christmas_songs_4manos', 'Luisa_04_Christmas_Songs_4manos.pdf',
     dict(num=4, title='Christmas Songs for Four Little Hands', subtitle='Jingle Bells + We Wish You · Mindy Liang (a 4 manos)',
          tonalidad='Do mayor', dificultad=1)),
    ('05_rasputin', 'Luisa_05_Rasputin.pdf',
     dict(num=5, title='Rasputin A (Easy Piano)', subtitle='Boney M.',
          tonalidad='Si menor', dificultad=1)),
    ('06_the_beginner_gurlitt', 'Luisa_06_The_Beginner_Gurlitt.pdf',
     dict(num=6, title='The Beginner, Le Début', subtitle='Op.211 No.3 · Cornelius Gurlitt (a 4 manos)',
          tonalidad='Do mayor', dificultad=1)),
    ('07_nocturne_chopin', 'Luisa_07_Nocturne_Chopin.pdf',
     dict(num=7, title='Nocturne Op.9 (easy)', subtitle='Frédéric Chopin, arr. Benny Chaw',
          tonalidad='Do mayor', dificultad=1)),
    ('08_largo_dvorak', 'Luisa_08_Largo_Dvorak.pdf',
     dict(num=8, title='Largo - Sinfonía nº5 Op. 95', subtitle='"Sinfonía del Nuevo Mundo" · A. Dvořák',
          tonalidad='Do mayor', dificultad=1)),
    ('09_silent_night_solo', 'Luisa_09_Silent_Night_Solo.pdf',
     dict(num=9, title='Silent Night (solo)', subtitle='Franz X. Gruber · palabras de Joseph Mohr',
          tonalidad='Do mayor', dificultad=1)),
    ('10_supercalifragilistico', 'Luisa_10_Supercalifragilistico.pdf',
     dict(num=10, title='Supercalifragilísticoexpialidoso', subtitle='Mary Poppins · R. y R. Sherman',
          tonalidad='Do mayor → Fa mayor', dificultad=2)),
    ('11_i_have_a_dream', 'Luisa_11_I_Have_A_Dream.pdf',
     dict(num=11, title='I Have a Dream', subtitle='Abba',
          tonalidad='Do mayor', dificultad=1)),
    ('12_youve_got_a_friend_in_me', 'Luisa_12_Youve_Got_A_Friend_In_Me.pdf',
     dict(num=12, title="You've Got a Friend in Me", subtitle='Toy Story',
          tonalidad='Do mayor', dificultad=1)),
    ('13_mama_mia_son_stufa', 'Luisa_13_Mama_Mia_Son_Stufa.pdf',
     dict(num=13, title='Mama Mia, Mi Son Stufa', subtitle='Canción popular italiana (a 4 manos)',
          tonalidad='Do mayor', dificultad=1)),
    ('14_greensleeves', 'Luisa_14_Greensleeves.pdf',
     dict(num=14, title='Greensleeves', subtitle='Canción tradicional inglesa',
          tonalidad='La menor', dificultad=2)),
    ('15_danubio_azul', 'Luisa_15_El_Danubio_Azul.pdf',
     dict(num=15, title='El Danubio Azul', subtitle='Johann Strauss II',
          tonalidad='Do mayor', dificultad=2)),
    ('16_titanic', 'Luisa_16_Titanic.pdf',
     dict(num=16, title='Titanic (Mi Corazón Sigue)', subtitle='James Horner',
          tonalidad='Do mayor', dificultad=2)),
    ('17_bazzoni_sonatina_sol', 'Luisa_17_Sonatina_Sol_Maggiore.pdf',
     dict(num=17, title='Sonatina N.2', subtitle='Maurizio Bazzoni (a 4 manos)',
          tonalidad='Sol mayor', dificultad=2)),
    ('18_bazzoni_sonatina_bambini', 'Luisa_18_Sonatina_Per_Bambini.pdf',
     dict(num=18, title='Sonatina per bambini', subtitle='Maurizio Bazzoni (a 4 manos)',
          tonalidad='La menor', dificultad=2)),
    ('19_piano_man', 'Luisa_19_Piano_Man.pdf',
     dict(num=19, title='Piano Man (Easy)', subtitle='Billy Joel',
          tonalidad='Do mayor', dificultad=2)),
    ('20_puff_the_magic_dragon', 'Luisa_20_Puff_The_Magic_Dragon.pdf',
     dict(num=20, title='Puff the Magic Dragon', subtitle='Peter, Paul and Mary · arr. Eric Moore',
          tonalidad='Do mayor', dificultad=2)),
    ('21_heart_and_soul', 'Luisa_21_Heart_And_Soul.pdf',
     dict(num=21, title='Heart and Soul', subtitle='Hoagy Carmichael',
          tonalidad='Do mayor', dificultad=2)),
    ('22_para_elisa', 'Luisa_22_Para_Elisa.pdf',
     dict(num=22, title='Para Elisa', subtitle='Ludwig van Beethoven · versión fácil',
          tonalidad='La menor', dificultad=2)),
    ('23_perfect', 'Luisa_23_Perfect.pdf',
     dict(num=23, title='Perfect', subtitle='Ed Sheeran, arr. Nicki Allan',
          tonalidad='Do mayor', dificultad=2)),
    ('24_mary_poppins_chim_chim', 'Luisa_24_Chim_Chim_Cheree.pdf',
     dict(num=24, title='Chim Chim Cher-ee', subtitle='Mary Poppins · Richard M. Sherman',
          tonalidad='Do mayor', dificultad=3)),
    ('25_la_pantera_rosa', 'Luisa_25_La_Pantera_Rosa.pdf',
     dict(num=25, title='La Pantera Rosa', subtitle='Henry Mancini',
          tonalidad='Do mayor', dificultad=3)),
    ('26_sound_of_silence', 'Luisa_26_The_Sound_Of_Silence.pdf',
     dict(num=26, title='The Sound of Silence', subtitle='Simon & Garfunkel',
          tonalidad='Re menor', dificultad=3)),
    ('27_gladiator', 'Luisa_27_Gladiator.pdf',
     dict(num=27, title='Gladiator (Honor Him)', subtitle='Hans Zimmer',
          tonalidad='Re mayor', dificultad=3)),
    ('28_jingle_bell_rock', 'Luisa_28_Jingle_Bell_Rock.pdf',
     dict(num=28, title='Jingle Bell Rock', subtitle='Boothe, arr. GC (a 4 manos, reto final)',
          tonalidad='Do mayor', dificultad=3)),
]

MONTHS = [
    ('Septiembre', [SONGS[0][2], SONGS[1][2], SONGS[2][2], SONGS[3][2]]),
    ('Octubre', [SONGS[4][2], SONGS[5][2], SONGS[6][2], SONGS[7][2]]),
    ('Noviembre', [SONGS[8][2], SONGS[9][2], SONGS[10][2]]),
    ('Diciembre', [SONGS[11][2], SONGS[12][2], SONGS[13][2]]),
    ('Enero', [SONGS[14][2], SONGS[15][2]]),
    ('Febrero', [SONGS[16][2], SONGS[17][2]]),
    ('Marzo', [SONGS[18][2], SONGS[19][2]]),
    ('Abril', [SONGS[20][2], SONGS[21][2]]),
    ('Mayo', [SONGS[22][2], SONGS[23][2]]),
    ('Junio', [SONGS[24][2], SONGS[25][2], SONGS[26][2], SONGS[27][2]]),
]


def _run_song_build(folder):
    """Importa y ejecuta students/luisa/<folder>/build.py's main(), regenerando
       el dosier individual de esa cancion en output/."""
    song_dir = os.path.join(HERE, folder)
    sys.path.insert(0, song_dir)
    for mod in ('build', 'page_exercises'):
        if mod in sys.modules:
            del sys.modules[mod]
    spec = importlib.util.spec_from_file_location('build', os.path.join(song_dir, 'build.py'))
    build_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(build_mod)
    build_mod.main()
    sys.path.pop(0)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    for folder, _out_name, _row in SONGS:
        _run_song_build(folder)

    portada_path = os.path.join(HERE, '_portada.pdf')
    c = canvas.Canvas(portada_path, pagesize=(W, H))
    build_portada(c, os.path.join(ASSETS, 'asset_logo_tclas.png'), ALUMNO, SUBTITLE, MONTHS)
    c.save()

    writer = PdfWriter()
    for p in PdfReader(portada_path).pages:
        writer.add_page(p)
    for _folder, out_name, _row in SONGS:
        dossier_path = os.path.join(OUT_DIR, out_name)
        for p in PdfReader(dossier_path).pages:
            writer.add_page(p)

    album_path = os.path.join(OUT_DIR, 'Luisa_Cuaderno_del_Pianista.pdf')
    with open(album_path, 'wb') as f:
        writer.write(f)
    os.remove(portada_path)
    print('generated', album_path)


if __name__ == '__main__':
    main()
