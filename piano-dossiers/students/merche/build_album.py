"""Construye el cuaderno completo de Mercè: portada + los dosieres de cada
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

ALUMNO = 'Mercè'
SUBTITLE = 'Nivel básico, sólido · Curso 2026-2027'

SONGS = [
    ('01_oh_when_the_saints', 'Merce_01_Oh_When_The_Saints.pdf',
     dict(num=1, title='Oh, When the Saints', subtitle='Primer Level · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('02_christmas_songs_4manos', 'Merce_02_Christmas_Songs_4manos.pdf',
     dict(num=2, title='Christmas Songs for Four Little Hands', subtitle='Jingle Bells + We Wish You · Mindy Liang (a 4 manos)',
          tonalidad='Do mayor', dificultad=1)),
    ('03_beauty_and_beast', 'Merce_03_Beauty_And_Beast.pdf',
     dict(num=3, title='Beauty and Beast', subtitle='La Bella y la Bestia, arr. Naf',
          tonalidad='Fa mayor', dificultad=2)),
    ('04_bela_ciao', 'Merce_04_Bela_Ciao.pdf',
     dict(num=4, title='Bela Ciao', subtitle='La Casa de Papel · arr. Anderson Miranda Fernandes',
          tonalidad='Mi menor', dificultad=2)),
    ('05_counting_stars', 'Merce_05_Counting_Stars.pdf',
     dict(num=5, title='Counting Stars', subtitle='OneRepublic · arr. Becky Messer (Easy Version)',
          tonalidad='Do mayor', dificultad=2)),
    ('06_i_have_a_dream', 'Merce_06_I_Have_A_Dream.pdf',
     dict(num=6, title='I Have a Dream', subtitle='Abba',
          tonalidad='Do mayor', dificultad=2)),
    ('07_nocturne_chopin', 'Merce_07_Nocturne_Chopin.pdf',
     dict(num=7, title='Nocturne Op.9', subtitle='Frédéric Chopin, arr. Benny Chaw',
          tonalidad='Do mayor', dificultad=2)),
    ('08_silent_night_4manos', 'Merce_08_Silent_Night_4manos.pdf',
     dict(num=8, title='Silent Night', subtitle='Villancico tradicional (a 4 manos)',
          tonalidad='Do mayor', dificultad=2)),
    ('09_largo_dvorak', 'Merce_09_Largo_Dvorak.pdf',
     dict(num=9, title='Largo - Sinfonía nº5 Op. 95', subtitle='"Sinfonía del Nuevo Mundo" · A. Dvořák',
          tonalidad='Do mayor', dificultad=2)),
    ('10_mama_mia_son_stufa', 'Merce_10_Mama_Mia_Son_Stufa.pdf',
     dict(num=10, title='Mama Mia, Mi Son Stufa', subtitle='Canción popular italiana (a 4 manos)',
          tonalidad='Do mayor', dificultad=2)),
    ('11_gladiator', 'Merce_11_Gladiator.pdf',
     dict(num=11, title='Honor Him - Gladiator (Easy Version)', subtitle='Hans Zimmer',
          tonalidad='Re mayor', dificultad=2)),
    ('12_hay_un_amigo_en_mi', 'Merce_12_Hay_Un_Amigo_En_Mi.pdf',
     dict(num=12, title="You've Got a Friend in Me", subtitle='Toy Story · arr. Megan Harper',
          tonalidad='Do mayor', dificultad=2)),
    ('13_spring_vivaldi', 'Merce_13_Spring_Vivaldi.pdf',
     dict(num=13, title="'Spring' from the Four Seasons", subtitle='Antonio Vivaldi',
          tonalidad='Do mayor', dificultad=2)),
    ('14_sonatina_per_bambini', 'Merce_14_Sonatina_Per_Bambini.pdf',
     dict(num=14, title='Sonatina per bambini', subtitle='Maurizio Bazzoni (a 4 manos)',
          tonalidad='La menor', dificultad=2)),
    ('15_piano_man', 'Merce_15_Piano_Man.pdf',
     dict(num=15, title='Piano Man (Easy)', subtitle='Billy Joel',
          tonalidad='Do mayor', dificultad=2)),
    ('16_puff_the_magic_dragon', 'Merce_16_Puff_The_Magic_Dragon.pdf',
     dict(num=16, title='Puff the Magic Dragon', subtitle='Peter, Paul and Mary · arr. Eric Moore',
          tonalidad='Do mayor', dificultad=2)),
    ('17_rasputin', 'Merce_17_Rasputin.pdf',
     dict(num=17, title='Rasputin A (Easy Piano)', subtitle='Boney M.',
          tonalidad='Si menor', dificultad=2)),
    ('18_sur_le_pont_davignon', 'Merce_18_Sur_Le_Pont_Davignon.pdf',
     dict(num=18, title="Sur le Pont d'Avignon", subtitle='Deuxième Niveau · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=2)),
    ('19_we_wish_you_merry_christmas', 'Merce_19_We_Wish_You_A_Merry_Christmas.pdf',
     dict(num=19, title='We Wish You a Merry Christmas', subtitle='Villancico tradicional · arr. Gilbert DeBenedetti',
          tonalidad='Sol mayor', dificultad=2)),
    ('20_sonatina_sol_maggiore', 'Merce_20_Sonatina_Sol_Maggiore.pdf',
     dict(num=20, title='Sonatina N.2', subtitle='Maurizio Bazzoni (a 4 manos)',
          tonalidad='Sol mayor', dificultad=2)),
    ('21_greensleeves', 'Merce_21_Greensleeves.pdf',
     dict(num=21, title='Greensleeves', subtitle='Canción tradicional inglesa',
          tonalidad='La menor', dificultad=3)),
    ('22_grandfathers_clock', 'Merce_22_Grandfathers_Clock.pdf',
     dict(num=22, title="My Grandfather's Clock", subtitle='Level Three · Henry Clay Work',
          tonalidad='Sol mayor', dificultad=3)),
    ('23_jailhouse_rock', 'Merce_23_Jailhouse_Rock.pdf',
     dict(num=23, title='Jailhouse Rock', subtitle='Elvis Presley · arr. Sadie King',
          tonalidad='Do mayor', dificultad=3)),
    ('24_la_pantera_rosa', 'Merce_24_La_Pantera_Rosa.pdf',
     dict(num=24, title='La Pantera Rosa', subtitle='Henry Mancini',
          tonalidad='Do mayor', dificultad=3)),
    ('25_para_elisa', 'Merce_25_Para_Elisa.pdf',
     dict(num=25, title='Für Elise', subtitle='Ludwig van Beethoven',
          tonalidad='La menor', dificultad=3)),
    ('26_silent_night_solo', 'Merce_26_Silent_Night_Solo.pdf',
     dict(num=26, title='Silent Night (solo)', subtitle='Franz X. Gruber',
          tonalidad='Do mayor', dificultad=3)),
    ('27_sonrisas_y_lagrimas', 'Merce_27_Sonrisas_Y_Lagrimas.pdf',
     dict(num=27, title='Do Re Mi', subtitle='Sonrisas y Lágrimas · Richard Rodgers',
          tonalidad='Do mayor', dificultad=3)),
    ('28_toreador', 'Merce_28_Toreador.pdf',
     dict(num=28, title='Toreador', subtitle='de Carmen · Georges Bizet (reto final)',
          tonalidad='Fa mayor', dificultad=4)),
]

MONTHS = [
    ('Septiembre', [SONGS[0][2], SONGS[1][2], SONGS[2][2]]),
    ('Octubre', [SONGS[3][2], SONGS[4][2], SONGS[5][2]]),
    ('Noviembre', [SONGS[6][2], SONGS[7][2], SONGS[8][2]]),
    ('Diciembre', [SONGS[9][2], SONGS[10][2], SONGS[11][2]]),
    ('Enero', [SONGS[12][2], SONGS[13][2]]),
    ('Febrero', [SONGS[14][2], SONGS[15][2]]),
    ('Marzo', [SONGS[16][2], SONGS[17][2]]),
    ('Abril', [SONGS[18][2], SONGS[19][2]]),
    ('Mayo', [SONGS[20][2], SONGS[21][2]]),
    ('Junio', [SONGS[22][2], SONGS[23][2], SONGS[24][2], SONGS[25][2], SONGS[26][2], SONGS[27][2]]),
]


def _run_song_build(folder):
    """Importa y ejecuta students/merche/<folder>/build.py's main(), regenerando
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

    album_path = os.path.join(OUT_DIR, 'Merce_Cuaderno_del_Pianista.pdf')
    with open(album_path, 'wb') as f:
        writer.write(f)
    os.remove(portada_path)
    print('generated', album_path)


if __name__ == '__main__':
    main()
