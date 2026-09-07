"""Construye el cuaderno completo de Jose Maria: portada + los dosieres de
   cada cancion, en un unico PDF. Vuelve a generar cada dosier (llamando a su
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

ALUMNO = 'José María'
SUBTITLE = 'A su ritmo · Curso 2026-2027'

SONGS = [
    ('01_grandfathers_clock', 'JoseMaria_01_Grandfathers_Clock.pdf',
     dict(num=1, title="My Grandfather's Clock", subtitle='Henry Clay Work',
          tonalidad='Sol mayor', dificultad=1)),
    ('02_counting_stars', 'JoseMaria_02_Counting_Stars.pdf',
     dict(num=2, title='Counting Stars', subtitle='OneRepublic (Easy Version)',
          tonalidad='Do mayor', dificultad=1)),
    ('03_america', 'JoseMaria_03_America.pdf',
     dict(num=3, title="America (My Country, 'Tis of Thee)", subtitle='Tradicional',
          tonalidad='Do mayor', dificultad=1)),
    ('04_a_comme_amour', 'JoseMaria_04_A_Comme_Amour.pdf',
     dict(num=4, title='A comme Amour', subtitle='Richard Clayderman',
          tonalidad='Mi menor', dificultad=2)),
    ('05_someone_you_loved', 'JoseMaria_05_Someone_You_Loved.pdf',
     dict(num=5, title='Someone You Loved', subtitle='Lewis Capaldi',
          tonalidad='Do mayor', dificultad=2)),
    ('06_interstellar', 'JoseMaria_06_Interstellar.pdf',
     dict(num=6, title='Interstellar (tema principal)', subtitle='Hans Zimmer',
          tonalidad='Do mayor', dificultad=2)),
    ('07_deck_the_halls', 'JoseMaria_07_Deck_The_Halls.pdf',
     dict(num=7, title='Deck the Halls', subtitle='Tradicional',
          tonalidad='Fa mayor', dificultad=2)),
    ('08_jingle_bells', 'JoseMaria_08_Jingle_Bells.pdf',
     dict(num=8, title='Jingle Bells', subtitle='James Lord Pierpont',
          tonalidad='Sol mayor', dificultad=2)),
    ('09_leise_rieselt', 'JoseMaria_09_Leise_Rieselt.pdf',
     dict(num=9, title='Leise rieselt der Schnee', subtitle='Villancico alemán (a 4 manos)',
          tonalidad='Do mayor', dificultad=1)),
    ('10_jailhouse_rock', 'JoseMaria_10_Jailhouse_Rock.pdf',
     dict(num=10, title='Jailhouse Rock', subtitle='Elvis Presley',
          tonalidad='Do mayor', dificultad=2)),
    ('11_peaches', 'JoseMaria_11_Peaches.pdf',
     dict(num=11, title='Peaches', subtitle='Jack Black · Super Mario Bros Movie',
          tonalidad='Do mayor', dificultad=2)),
    ('12_himno_estados_unidos', 'JoseMaria_12_Himno_Estados_Unidos.pdf',
     dict(num=12, title='Himno de Estados Unidos', subtitle='The Star-Spangled Banner',
          tonalidad='Do mayor', dificultad=2)),
    ('13_rasputin', 'JoseMaria_13_Rasputin.pdf',
     dict(num=13, title='Rasputin', subtitle='Boney M.',
          tonalidad='Si menor', dificultad=2)),
    ('14_romance_diabelli', 'JoseMaria_14_Romance_Diabelli.pdf',
     dict(num=14, title='Romance', subtitle='Anton Diabelli (a 4 manos)',
          tonalidad='Do mayor', dificultad=2)),
    ('15_shallow', 'JoseMaria_15_Shallow.pdf',
     dict(num=15, title='Shallow', subtitle='Lady Gaga & Bradley Cooper',
          tonalidad='Sol mayor', dificultad=2)),
    ('16_trouble', 'JoseMaria_16_Trouble.pdf',
     dict(num=16, title='Trouble', subtitle='Coldplay',
          tonalidad='Sol mayor', dificultad=2)),
    ('17_cant_help_falling_in_love', 'JoseMaria_17_Cant_Help_Falling_In_Love.pdf',
     dict(num=17, title="Can't Help Falling in Love", subtitle='Elvis Presley',
          tonalidad='Re mayor', dificultad=2)),
    ('18_carol_of_the_bells', 'JoseMaria_18_Carol_Of_The_Bells.pdf',
     dict(num=18, title='Carol of the Bells', subtitle='Villancico tradicional ucraniano',
          tonalidad='Sol menor', dificultad=3)),
    ('19_toreador', 'JoseMaria_19_Toreador.pdf',
     dict(num=19, title='Toreador', subtitle='Georges Bizet · Carmen',
          tonalidad='Fa mayor', dificultad=3)),
    ('20_adagio_albinoni', 'JoseMaria_20_Adagio_Albinoni.pdf',
     dict(num=20, title='Adagio', subtitle='Tomaso Albinoni',
          tonalidad='La menor', dificultad=3)),
    ('21_como_entrenar_a_tu_dragon', 'JoseMaria_21_Como_Entrenar_A_Tu_Dragon.pdf',
     dict(num=21, title='Cómo entrenar a tu dragón (tema de vuelo)', subtitle='John Powell',
          tonalidad='Do mayor → Re mayor', dificultad=3)),
]

MONTHS = [
    ('Septiembre', [SONGS[0][2], SONGS[1][2]]),
    ('Octubre', [SONGS[2][2], SONGS[3][2]]),
    ('Noviembre', [SONGS[4][2], SONGS[5][2]]),
    ('Diciembre', [SONGS[6][2], SONGS[7][2], SONGS[8][2], SONGS[9][2]]),
    ('Enero', [SONGS[10][2], SONGS[11][2]]),
    ('Febrero', [SONGS[12][2], SONGS[13][2]]),
    ('Marzo', [SONGS[14][2], SONGS[15][2]]),
    ('Abril', [SONGS[16][2]]),
    ('Mayo', [SONGS[17][2], SONGS[18][2]]),
    ('Junio', [SONGS[19][2], SONGS[20][2]]),
]


def _run_song_build(folder):
    """Importa y ejecuta students/jose_maria/<folder>/build.py's main(),
       regenerando el dosier individual de esa cancion en output/."""
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

    album_path = os.path.join(OUT_DIR, 'JoseMaria_Cuaderno_del_Pianista.pdf')
    with open(album_path, 'wb') as f:
        writer.write(f)
    os.remove(portada_path)
    print('generated', album_path)


if __name__ == '__main__':
    main()
