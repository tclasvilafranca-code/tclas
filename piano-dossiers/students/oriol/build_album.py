"""Construye el cuaderno completo de Oriol: portada + los dosieres de cada
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

ALUMNO = 'Oriol'
SUBTITLE = 'Nivel medio, sin agobios · Curso 2026-2027'

SONGS = [
    ('01_chopsticks', 'Oriol_01_Chopsticks.pdf',
     dict(num=1, title='Chopsticks', subtitle='Level One · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('02_la_primavera', 'Oriol_02_La_Primavera.pdf',
     dict(num=2, title='La Primavera', subtitle='Antonio Vivaldi (easy)',
          tonalidad='Do mayor', dificultad=2)),
    ('03_easy_on_me', 'Oriol_03_Easy_On_Me.pdf',
     dict(num=3, title='Easy on Me', subtitle='Adele, arr. Holmes',
          tonalidad='Fa mayor', dificultad=2)),
    ('04_heart_and_soul', 'Oriol_04_Heart_And_Soul.pdf',
     dict(num=4, title='Heart and Soul', subtitle='Hoagy Carmichael',
          tonalidad='Do mayor', dificultad=2)),
    ('05_gladiator', 'Oriol_05_Gladiator.pdf',
     dict(num=5, title='Gladiator (Honor Him)', subtitle='Hans Zimmer, easy version',
          tonalidad='Re mayor', dificultad=2)),
    ('06_i_have_a_dream', 'Oriol_06_I_Have_A_Dream.pdf',
     dict(num=6, title='I Have a Dream', subtitle='Abba',
          tonalidad='Do mayor', dificultad=1)),
    ('07_jingle_bell_rock', 'Oriol_07_Jingle_Bell_Rock.pdf',
     dict(num=7, title='Jingle Bell Rock', subtitle='Arr. Sadie King',
          tonalidad='Do mayor', dificultad=2)),
    ('08_la_pantera_rosa', 'Oriol_08_La_Pantera_Rosa.pdf',
     dict(num=8, title='La Pantera Rosa', subtitle='Henry Mancini',
          tonalidad='Do mayor', dificultad=2)),
    ('09_nocturne_chopin', 'Oriol_09_Nocturne_Chopin.pdf',
     dict(num=9, title='Nocturne Op.9', subtitle='Frédéric Chopin, arr. Benny Chaw',
          tonalidad='Do mayor', dificultad=2)),
    ('10_oh_when_the_saints', 'Oriol_10_Oh_When_The_Saints.pdf',
     dict(num=10, title='Oh, When the Saints', subtitle='Primer Level · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('11_perfect', 'Oriol_11_Perfect.pdf',
     dict(num=11, title='Perfect', subtitle='Ed Sheeran',
          tonalidad='Do mayor', dificultad=2)),
    ('12_piano_man', 'Oriol_12_Piano_Man.pdf',
     dict(num=12, title='Piano Man', subtitle='Billy Joel',
          tonalidad='Do mayor', dificultad=2)),
    ('13_puff_the_magic_dragon', 'Oriol_13_Puff_The_Magic_Dragon.pdf',
     dict(num=13, title='Puff the Magic Dragon', subtitle='Peter, Paul and Mary · arr. Eric Moore',
          tonalidad='Do mayor', dificultad=2)),
    ('14_blue_danube', 'Oriol_14_El_Danubio_Azul.pdf',
     dict(num=14, title='El Danubio Azul', subtitle='Johann Strauss II',
          tonalidad='Do mayor', dificultad=2)),
    ('15_youve_got_a_friend_in_me', 'Oriol_15_Youve_Got_A_Friend_In_Me.pdf',
     dict(num=15, title="You've Got a Friend in Me", subtitle='Randy Newman · Toy Story',
          tonalidad='Do mayor', dificultad=2)),
]

MONTHS = [
    ('Septiembre', [SONGS[0][2], SONGS[1][2]]),
    ('Octubre', [SONGS[2][2], SONGS[3][2]]),
    ('Noviembre', [SONGS[4][2], SONGS[5][2]]),
    ('Diciembre', [SONGS[6][2], SONGS[7][2]]),
    ('Enero', [SONGS[8][2], SONGS[9][2]]),
    ('Febrero', [SONGS[10][2], SONGS[11][2]]),
    ('Marzo', [SONGS[12][2], SONGS[13][2], SONGS[14][2]]),
]


def _run_song_build(folder):
    """Importa y ejecuta students/oriol/<folder>/build.py's main(), regenerando
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

    album_path = os.path.join(OUT_DIR, 'Oriol_Cuaderno_del_Pianista.pdf')
    with open(album_path, 'wb') as f:
        writer.write(f)
    os.remove(portada_path)
    print('generated', album_path)


if __name__ == '__main__':
    main()
