"""Construye el cuaderno completo de Josep: portada + los dosieres de cada
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

ALUMNO = 'Josep'
SUBTITLE = 'Nivel medio-alto · Curso 2026-2027'

SONGS = [
    ('01_cant_help_falling_in_love', 'Josep_01_Cant_Help_Falling_In_Love.pdf',
     dict(num=1, title="Can't Help Falling in Love", subtitle='Elvis Presley · arr. Seb Alejandro',
          tonalidad='Re mayor', dificultad=1)),
    ('02_counting_stars', 'Josep_02_Counting_Stars.pdf',
     dict(num=2, title='Counting Stars', subtitle='OneRepublic · arr. Becky Messer (Easy Version)',
          tonalidad='Do mayor', dificultad=1)),
    ('03_boig_per_tu', 'Josep_03_Boig_Per_Tu.pdf',
     dict(num=3, title='Boig per tu', subtitle='Sau · arr. Pilar Sanz',
          tonalidad='La menor', dificultad=2)),
    ('04_un_beso_y_una_flor', 'Josep_04_Un_Beso_Y_Una_Flor.pdf',
     dict(num=4, title='Un Beso y una Flor', subtitle='Nino Bravo',
          tonalidad='Fa mayor', dificultad=2)),
    ('05_rasputin', 'Josep_05_Rasputin.pdf',
     dict(num=5, title='Rasputin', subtitle='Boney M.',
          tonalidad='Si menor', dificultad=2)),
    ('06_jailhouse_rock', 'Josep_06_Jailhouse_Rock.pdf',
     dict(num=6, title='Jailhouse Rock', subtitle='Elvis Presley · arr. Sadie King',
          tonalidad='Do mayor', dificultad=2)),
    ('07_romance_diabelli', 'Josep_07_Romance_Diabelli.pdf',
     dict(num=7, title='Romance', subtitle='Anton Diabelli · a 4 manos',
          tonalidad='Do mayor', dificultad=2)),
    ('08_bella_ciao', 'Josep_08_Bella_Ciao.pdf',
     dict(num=8, title='Bella Ciao', subtitle='Tradicional italiana (a 4 manos)',
          tonalidad='Sol menor', dificultad=2)),
    ('09_what_was_i_made_for', 'Josep_09_What_Was_I_Made_For.pdf',
     dict(num=9, title='What Was I Made For?', subtitle='Billie Eilish',
          tonalidad='Do mayor', dificultad=2)),
    ('10_petite_chanson', 'Josep_10_Petite_Chanson.pdf',
     dict(num=10, title='Petite Chanson', subtitle='Riccardo Collu (a 4 manos)',
          tonalidad='Do mayor', dificultad=3)),
    ('11_kiss_the_rain', 'Josep_11_Kiss_The_Rain.pdf',
     dict(num=11, title='Kiss the Rain', subtitle='Yiruma',
          tonalidad='Do mayor', dificultad=3)),
    ('12_a_comme_amour', 'Josep_12_A_Comme_Amour.pdf',
     dict(num=12, title='A comme Amour', subtitle='Richard Clayderman · Paul de Senneville',
          tonalidad='Mi menor', dificultad=3)),
    ('13_nuovo_cinema_paradiso', 'Josep_13_Nuovo_Cinema_Paradiso.pdf',
     dict(num=13, title='Nuovo Cinema Paradiso', subtitle='Ennio Morricone',
          tonalidad='Sib mayor', dificultad=3)),
    ('14_si_tu_no_estas_aqui', 'Josep_14_Si_Tu_No_Estas_Aqui.pdf',
     dict(num=14, title='Si tú no estás aquí', subtitle='Rosana',
          tonalidad='Do mayor', dificultad=3)),
    ('15_y_si_fuera_ella', 'Josep_15_Y_Si_Fuera_Ella.pdf',
     dict(num=15, title='Y si fuera ella', subtitle='Alejandro Sanz',
          tonalidad='Fa mayor', dificultad=3)),
    ('16_your_song', 'Josep_16_Your_Song.pdf',
     dict(num=16, title='Your Song', subtitle='Elton John',
          tonalidad='Fa mayor', dificultad=3)),
    ('17_bob_esponja', 'Josep_17_Bob_Esponja.pdf',
     dict(num=17, title='Bob Esponja (canción inicial)', subtitle='Tema de la serie animada',
          tonalidad='Mi mayor', dificultad=3)),
    ('18_beginning_to_look_like_christmas', 'Josep_18_Beginning_To_Look_Like_Christmas.pdf',
     dict(num=18, title="It's Beginning to Look a Lot Like Christmas", subtitle='Meredith Willson (a 4 manos)',
          tonalidad='Do mayor', dificultad=3)),
    ('19_despacito', 'Josep_19_Despacito.pdf',
     dict(num=19, title='Despacito', subtitle='Luis Fonsi & Daddy Yankee · arr. Unai Karam',
          tonalidad='Do mayor', dificultad=3)),
    ('20_sweet_child_o_mine', 'Josep_20_Sweet_Child_O_Mine.pdf',
     dict(num=20, title="Sweet Child O' Mine", subtitle="Guns N' Roses",
          tonalidad='Sib mayor', dificultad=3)),
    ('21_como_entrenar_a_tu_dragon', 'Josep_21_Como_Entrenar_A_Tu_Dragon.pdf',
     dict(num=21, title='Cómo entrenar a tu dragón (tema de vuelo)', subtitle='John Powell',
          tonalidad='Do mayor → Re mayor', dificultad=4)),
    ('22_bohemian_rhapsody', 'Josep_22_Bohemian_Rhapsody.pdf',
     dict(num=22, title='Bohemian Rhapsody', subtitle='Queen (apertura, piano solo)',
          tonalidad='Sib mayor', dificultad=4)),
]

MONTHS = [
    ('Septiembre', [SONGS[0][2], SONGS[1][2]]),
    ('Octubre', [SONGS[2][2], SONGS[3][2]]),
    ('Noviembre', [SONGS[4][2]]),
    ('Diciembre', [SONGS[5][2], SONGS[6][2], SONGS[7][2]]),
    ('Enero', [SONGS[8][2]]),
    ('Febrero', [SONGS[9][2]]),
    ('Marzo', [SONGS[10][2], SONGS[11][2]]),
    ('Abril', [SONGS[12][2], SONGS[13][2], SONGS[14][2]]),
    ('Mayo', [SONGS[15][2], SONGS[16][2], SONGS[17][2], SONGS[18][2]]),
    ('Junio', [SONGS[19][2], SONGS[20][2], SONGS[21][2]]),
]


def _run_song_build(folder):
    """Importa y ejecuta students/josep/<folder>/build.py's main(), regenerando
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

    album_path = os.path.join(OUT_DIR, 'Josep_Cuaderno_del_Pianista.pdf')
    with open(album_path, 'wb') as f:
        writer.write(f)
    os.remove(portada_path)
    print('generated', album_path)


if __name__ == '__main__':
    main()
