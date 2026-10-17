"""Construye el cuaderno completo de Arnau: portada (SIN agrupar por mes,
   a peticion expresa) + los dosieres de cada cancion, en un unico PDF.
   Vuelve a generar cada dosier (llamando a su build.py) para asegurarse de
   que el album refleja siempre la ultima version, y luego los une con la
   portada delante."""
import sys, os, importlib.util

HERE = os.path.dirname(__file__)
ENGINE = os.path.join(HERE, '..', '..', 'engine')
ASSETS = os.path.join(HERE, '..', '..', 'assets')
OUT_DIR = os.path.join(HERE, '..', '..', 'output')
sys.path.insert(0, ENGINE)

from reportlab.pdfgen import canvas
from pypdf import PdfWriter, PdfReader
from page_portada_generic import build_portada, W, H

ALUMNO = 'Arnau'
SUBTITLE = 'Nivel iniciación · 9 años · Curso 2026-2027'

SONGS = [
    ('01_chopsticks', 'Arnau_01_Chopsticks.pdf',
     dict(num=1, title='Chopsticks', subtitle='Level One · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('02_clementine', 'Arnau_02_Clementine.pdf',
     dict(num=2, title='Clementine (Found a Peanut)', subtitle='Primer Level · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('03_baa_baa_black_sheep', 'Arnau_03_Baa_Baa_Black_Sheep.pdf',
     dict(num=3, title='Baa Baa Black Sheep', subtitle='Traditional · arr. Jim Paterson',
          tonalidad='Do mayor', dificultad=1)),
    ('04_do_your_ears_hang_low', 'Arnau_04_Do_Your_Ears_Hang_Low.pdf',
     dict(num=4, title='Do Your Ears Hang Low?', subtitle='Level One · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('05_oh_when_the_saints', 'Arnau_05_Oh_When_The_Saints.pdf',
     dict(num=5, title='Oh, When the Saints', subtitle='Primer Level · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('06_jolly_old_saint_nicholas', 'Arnau_06_Jolly_Old_Saint_Nicholas.pdf',
     dict(num=6, title='Jolly Old Saint Nicholas', subtitle='Level One · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('07_we_wish_you_merry_christmas', 'Arnau_07_We_Wish_You_A_Merry_Christmas.pdf',
     dict(num=7, title='We Wish You a Merry Christmas', subtitle='Primer Level · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=1)),
    ('08_puff_the_magic_dragon', 'Arnau_08_Puff_The_Magic_Dragon.pdf',
     dict(num=8, title='Puff the Magic Dragon', subtitle='Peter, Paul and Mary',
          tonalidad='Do mayor', dificultad=1)),
    ('09_eso_que_tu_me_das', 'Arnau_09_Eso_Que_Tu_Me_Das.pdf',
     dict(num=9, title='Eso que tú me das', subtitle='Jarabe de Palo',
          tonalidad='Do mayor', dificultad=1)),
    ('10_wheels_on_the_bus', 'Arnau_10_The_Wheels_On_The_Bus.pdf',
     dict(num=10, title='The Wheels on the Bus', subtitle='Canción infantil tradicional · arr. Jim Paterson',
          tonalidad='Fa mayor', dificultad=1)),
    ('11_polly_put_the_kettle_on', 'Arnau_11_Polly_Put_The_Kettle_On.pdf',
     dict(num=11, title='Polly Put the Kettle On', subtitle='Traditional · arr. Jim Paterson',
          tonalidad='Fa mayor', dificultad=1)),
    ('12_little_miss_muffet', 'Arnau_12_Little_Miss_Muffet.pdf',
     dict(num=12, title='Little Miss Muffet', subtitle='Traditional · arr. Jim Paterson',
          tonalidad='Fa mayor', dificultad=1)),
    ('13_aloha_oe', 'Arnau_13_Aloha_Oe.pdf',
     dict(num=13, title='Aloha Oe', subtitle='Música de la Reina Liliuokalani, arr. Regina Pratley',
          tonalidad='Do mayor', dificultad=1)),
    ('14_la_pantera_rosa', 'Arnau_14_La_Pantera_Rosa.pdf',
     dict(num=14, title='La Pantera Rosa', subtitle='Henry Mancini, arr. escolar',
          tonalidad='Do mayor', dificultad=1)),
    ('15_my_bonnie', 'Arnau_15_My_Bonnie.pdf',
     dict(num=15, title='My Bonnie Lies Over the Ocean', subtitle='Level Two · arr. Gilbert DeBenedetti',
          tonalidad='Do mayor', dificultad=2)),
    ('16_submarino_amarillo', 'Arnau_16_El_Submarino_Amarillo.pdf',
     dict(num=16, title='El Submarino Amarillo', subtitle='John Lennon y Paul McCartney, arr. A.C. Escobés',
          tonalidad='Sol mayor', dificultad=2)),
    ('17_popeye_marinerito', 'Arnau_17_Popeye_El_Marinerito.pdf',
     dict(num=17, title='Popeye el marinerito', subtitle='Arr. A.C. Escobés',
          tonalidad='Sol mayor', dificultad=2)),
    ('18_largo_dvorak', 'Arnau_18_Largo_Dvorak.pdf',
     dict(num=18, title='Largo - Sinfonía nº5 Op. 95', subtitle='"Sinfonía del Nuevo Mundo" · A. Dvořák',
          tonalidad='Do mayor', dificultad=2)),
    ('19_rain_rain_go_away', 'Arnau_19_Rain_Rain_Go_Away.pdf',
     dict(num=19, title='Rain Rain Go Away', subtitle='Tradicional, arr. Regina Pratley (a 4 manos)',
          tonalidad='Do mayor', dificultad=1)),
    ('20_the_mulberry_bush', 'Arnau_20_The_Mulberry_Bush.pdf',
     dict(num=20, title='The Mulberry Bush', subtitle='Tradicional, arr. Regina Pratley (a 4 manos)',
          tonalidad='Do mayor', dificultad=1)),
]

# Sin agrupacion por mes (a peticion expresa): un unico grupo con label vacio.
MONTHS = [
    ('', [row for _folder, _out, row in SONGS]),
]


def _run_song_build(folder):
    """Importa y ejecuta students/arnau/<folder>/build.py's main(), regenerando
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

    out_path = os.path.join(OUT_DIR, 'Arnau_Album_Completo.pdf')
    with open(out_path, 'wb') as f:
        writer.write(f)
    os.remove(portada_path)
    print('generated', out_path)


if __name__ == '__main__':
    main()
