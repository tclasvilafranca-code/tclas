"""Construye el cuaderno completo de Sandi: portada + los dosieres de cada
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

ALUMNO = 'Sandi'
SUBTITLE = 'Nivel avanzado, repertorio clásico · Curso 2026-2027'

SONGS = [
    ('01_soldadito_de_hierro', 'Sandi_01_Soldadito_De_Hierro.pdf',
     dict(num=1, title='Soldadito de Hierro', subtitle='Nil Moliner',
          tonalidad='La menor', dificultad=3)),
    ('02_my_way', 'Sandi_02_My_Way.pdf',
     dict(num=2, title='My Way', subtitle='Jacques Revaux',
          tonalidad='Do mayor', dificultad=3)),
    ('03_canon_pachelbel', 'Sandi_03_Canon_De_Pachelbel.pdf',
     dict(num=3, title='Canon en Re', subtitle='Johann Pachelbel',
          tonalidad='Re mayor', dificultad=3)),
    ('04_deck_the_halls', 'Sandi_04_Deck_The_Halls.pdf',
     dict(num=4, title='Deck the Halls', subtitle='Villancico tradicional galés',
          tonalidad='Fa mayor', dificultad=3)),
    ('05_el_condor_pasa', 'Sandi_05_El_Condor_Pasa.pdf',
     dict(num=5, title='El Cóndor Pasa', subtitle='Melodía tradicional andina',
          tonalidad='Re menor', dificultad=3)),
    ('06_carol_of_the_bells', 'Sandi_06_Carol_Of_The_Bells.pdf',
     dict(num=6, title='Carol of the Bells', subtitle='Mykola Leontovych',
          tonalidad='Sol menor', dificultad=3)),
    ('07_scarborough_fair', 'Sandi_07_Scarborough_Fair.pdf',
     dict(num=7, title='Scarborough Fair', subtitle='Balada tradicional inglesa',
          tonalidad='Re dórico', dificultad=4)),
    ('08_nuovo_cinema_paradiso', 'Sandi_08_Nuovo_Cinema_Paradiso.pdf',
     dict(num=8, title='Nuovo Cinema Paradiso', subtitle='Ennio Morricone',
          tonalidad='Re menor', dificultad=3)),
    ('09_hijo_de_la_luna', 'Sandi_09_Hijo_De_La_Luna.pdf',
     dict(num=9, title='Hijo de la Luna', subtitle='Mecano',
          tonalidad='Re menor', dificultad=3)),
    ('10_when_i_was_your_man', 'Sandi_10_When_I_Was_Your_Man.pdf',
     dict(num=10, title='When I Was Your Man', subtitle='Bruno Mars',
          tonalidad='Do mayor', dificultad=3)),
    ('11_hello_adele', 'Sandi_11_Hello.pdf',
     dict(num=11, title='Hello', subtitle='Adele',
          tonalidad='Mi menor', dificultad=3)),
    ('12_claro_de_luna', 'Sandi_12_Claro_De_Luna.pdf',
     dict(num=12, title='Claro de Luna', subtitle='"Moonlight" Sonata · Beethoven',
          tonalidad='La menor', dificultad=4)),
    ('13_diabelli_romance', 'Sandi_13_Romance_Diabelli.pdf',
     dict(num=13, title='Romance', subtitle='Anton Diabelli (a 4 manos)',
          tonalidad='Do mayor', dificultad=3)),
    ('14_diabelli_scherzo', 'Sandi_14_Scherzo_Diabelli.pdf',
     dict(num=14, title='Scherzo', subtitle='Anton Diabelli (a 4 manos)',
          tonalidad='Do mayor', dificultad=3)),
    ('15_arabesque_burgmuller', 'Sandi_15_Arabesque.pdf',
     dict(num=15, title='Arabesque', subtitle='J.F.F. Burgmüller (a 4 manos)',
          tonalidad='Do mayor', dificultad=4)),
    ('16_sinfonia_5_beethoven', 'Sandi_16_Sinfonia_5_Beethoven.pdf',
     dict(num=16, title='Sinfonía Nº5 (1er movimiento)', subtitle='Beethoven (reto final)',
          tonalidad='Do menor', dificultad=4)),
]

MONTHS = [
    ('Septiembre', [SONGS[0][2], SONGS[1][2]]),
    ('Octubre', [SONGS[2][2], SONGS[3][2]]),
    ('Noviembre', [SONGS[4][2], SONGS[5][2]]),
    ('Diciembre', [SONGS[6][2], SONGS[7][2]]),
    ('Enero', [SONGS[8][2], SONGS[9][2]]),
    ('Febrero', [SONGS[10][2], SONGS[11][2]]),
    ('Marzo', [SONGS[12][2], SONGS[13][2]]),
    ('Abril', [SONGS[14][2], SONGS[15][2]]),
]


def _run_song_build(folder):
    """Importa y ejecuta students/sandi/<folder>/build.py's main(), regenerando
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

    album_path = os.path.join(OUT_DIR, 'Sandi_Cuaderno_del_Pianista.pdf')
    with open(album_path, 'wb') as f:
        writer.write(f)
    os.remove(portada_path)
    print('generated', album_path)


if __name__ == '__main__':
    main()
