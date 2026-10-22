"""Construye el cuaderno completo de Julia: portada + los dosieres de cada
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

ALUMNO = 'Julia'
SUBTITLE = 'Nivel inicial · Curso 2026-2027'

SONGS = [
    ('01_wheels_on_the_bus', 'Julia_01_Wheels_On_The_Bus.pdf',
     dict(num=1, title='The Wheels on the Bus', subtitle='Canción infantil tradicional · arr. Jim Paterson',
          tonalidad='Fa mayor', dificultad=1)),
    ('02_chopsticks', 'Julia_02_Chopsticks.pdf',
     dict(num=2, title='Chopsticks', subtitle='Level One · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('03_do_your_ears_hang_low', 'Julia_03_Do_Your_Ears_Hang_Low.pdf',
     dict(num=3, title='Do Your Ears Hang Low?', subtitle='Level One · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('04_jolly_old_saint_nicholas', 'Julia_04_Jolly_Old_Saint_Nicholas.pdf',
     dict(num=4, title='Jolly Old Saint Nicholas', subtitle='Level One · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('05_oh_christmas_tree', 'Julia_05_Oh_Christmas_Tree.pdf',
     dict(num=5, title='O Christmas Tree', subtitle='Level One · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('06_oh_when_the_saints', 'Julia_06_Oh_When_The_Saints.pdf',
     dict(num=6, title='Oh, When the Saints', subtitle='Primer Level · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('07_eso_que_tu_me_das', 'Julia_07_Eso_Que_Tu_Me_Das.pdf',
     dict(num=7, title='Eso que tú me das', subtitle='Jarabe de Palo',
          tonalidad='Do mayor', dificultad=1)),
    ('08_this_old_man', 'Julia_08_This_Old_Man.pdf',
     dict(num=8, title='This Old Man', subtitle='Level 2 · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('09_mary_mary_quite_contrary', 'Julia_09_Mary_Mary_Quite_Contrary.pdf',
     dict(num=9, title='Mary Mary Quite Contrary', subtitle='Traditional · arr. Jim Paterson',
          tonalidad='Fa mayor', dificultad=1)),
    ('10_polly_put_the_kettle_on', 'Julia_10_Polly_Put_The_Kettle_On.pdf',
     dict(num=10, title='Polly Put the Kettle On', subtitle='Traditional · arr. Jim Paterson',
          tonalidad='Fa mayor', dificultad=1)),
    ('11_puff_the_magic_dragon', 'Julia_11_Puff_The_Magic_Dragon.pdf',
     dict(num=11, title='Puff the Magic Dragon', subtitle='Peter, Paul and Mary',
          tonalidad='Do mayor', dificultad=1)),
    ('12_youve_got_a_friend_in_me', 'Julia_12_Youve_Got_A_Friend_In_Me.pdf',
     dict(num=12, title="You've Got a Friend in Me", subtitle='Toy Story · Randy Newman',
          tonalidad='Do mayor', dificultad=1)),
    ('13_buttermilk_hill', 'Julia_13_Buttermilk_Hill.pdf',
     dict(num=13, title='Buttermilk Hill', subtitle='Johnny Has Gone for a Soldier · Tradicional (a 4 manos)',
          tonalidad='Do mayor', dificultad=1)),
    ('14_the_mulberry_bush', 'Julia_14_The_Mulberry_Bush.pdf',
     dict(num=14, title='The Mulberry Bush', subtitle='Tradicional, arr. Regina Pratley (a 4 manos)',
          tonalidad='Do mayor', dificultad=1)),
    ('15_i_have_a_dream', 'Julia_15_I_Have_A_Dream.pdf',
     dict(num=15, title='I Have a Dream', subtitle='Abba',
          tonalidad='Do mayor', dificultad=1)),
    ('16_supercalifragilistico', 'Julia_16_Supercalifragilistico.pdf',
     dict(num=16, title='Supercalifragilísticoexpialidoso', subtitle='Mary Poppins · R. y R. Sherman',
          tonalidad='Do mayor → Fa mayor', dificultad=2)),
    ('17_lullaby_brahms', 'Julia_17_Lullaby_Brahms.pdf',
     dict(num=17, title='Lullaby (Canción de cuna)', subtitle='Johannes Brahms, arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=2)),
    ('18_morning_song_grieg', 'Julia_18_Morning_Song_Grieg.pdf',
     dict(num=18, title='Morning Song', subtitle='Edvard Grieg, arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=2)),
    ('19_aloha_oe', 'Julia_19_Aloha_Oe.pdf',
     dict(num=19, title='Aloha Oe', subtitle='Música de la Reina Liliuokalani',
          tonalidad='Do mayor', dificultad=2)),
    ('20_beauty_and_beast', 'Julia_20_Beauty_And_Beast.pdf',
     dict(num=20, title='Beauty and Beast', subtitle='La Bella y la Bestia, arr. Naf',
          tonalidad='Fa mayor', dificultad=2)),
    ('21_la_pantera_rosa', 'Julia_21_La_Pantera_Rosa.pdf',
     dict(num=21, title='La Pantera Rosa', subtitle='Henry Mancini',
          tonalidad='Do mayor', dificultad=2)),
    ('22_largo_dvorak', 'Julia_22_Largo_Dvorak.pdf',
     dict(num=22, title='Largo - Sinfonía nº5 Op. 95', subtitle='"Sinfonía del Nuevo Mundo" · A. Dvořák',
          tonalidad='Do mayor', dificultad=2)),
    ('23_perfect', 'Julia_23_Perfect.pdf',
     dict(num=23, title='Perfect', subtitle='Ed Sheeran, arr. Nicki Allan',
          tonalidad='Do mayor', dificultad=2)),
    ('24_gladiator', 'Julia_24_Gladiator.pdf',
     dict(num=24, title='Honor Him - Gladiator (Easy Version)', subtitle='Hans Zimmer',
          tonalidad='Re mayor', dificultad=2)),
]

MONTHS = [
    ('Septiembre', [SONGS[0][2], SONGS[1][2], SONGS[2][2]]),
    ('Octubre', [SONGS[3][2], SONGS[4][2], SONGS[5][2]]),
    ('Noviembre', [SONGS[6][2], SONGS[7][2], SONGS[8][2]]),
    ('Diciembre', [SONGS[9][2], SONGS[10][2], SONGS[11][2]]),
    ('Enero', [SONGS[12][2], SONGS[13][2]]),
    ('Febrero', [SONGS[14][2], SONGS[15][2]]),
    ('Marzo', [SONGS[16][2], SONGS[17][2]]),
    ('Abril', [SONGS[18][2]]),
    ('Mayo', [SONGS[19][2], SONGS[20][2]]),
    ('Junio', [SONGS[21][2], SONGS[22][2], SONGS[23][2]]),
]


def _run_song_build(folder):
    """Importa y ejecuta students/julia/<folder>/build.py's main(), regenerando
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

    album_path = os.path.join(OUT_DIR, 'Julia_Cuaderno_del_Pianista.pdf')
    with open(album_path, 'wb') as f:
        writer.write(f)
    os.remove(portada_path)
    print('generated', album_path)


if __name__ == '__main__':
    main()
