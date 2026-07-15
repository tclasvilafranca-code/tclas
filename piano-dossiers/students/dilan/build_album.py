"""Construye el cuaderno completo de Dilan: portada + los dosieres de cada
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

ALUMNO = 'Dilan'
SUBTITLE = 'Nivel medio-alto · Curso 2026-2027'

# (carpeta, modulo build.py, nombre del PDF de salida individual, fila de portada)
SONGS = [
    ('01_cant_help_falling_in_love', 'Dilan_01_Cant_Help_Falling_In_Love.pdf',
     dict(num=1, title="Can't Help Falling in Love", subtitle='Elvis Presley · arr. Seb Alejandro',
          tonalidad='Re mayor', dificultad=1)),
    ('02_the_swan', 'Dilan_02_The_Swan.pdf',
     dict(num=2, title='The Swan (El Cisne)', subtitle='Camille Saint-Saëns',
          tonalidad='Sol mayor', dificultad=1)),
    ('03_what_was_i_made_for', 'Dilan_03_What_Was_I_Made_For.pdf',
     dict(num=3, title='What Was I Made For?', subtitle='Billie Eilish',
          tonalidad='Do mayor', dificultad=1)),
    ('04_a_sky_full_of_stars', 'Dilan_04_A_Sky_Full_Of_Stars.pdf',
     dict(num=4, title='A Sky Full of Stars', subtitle='Coldplay · con Avicii',
          tonalidad='Fa mayor', dificultad=2)),
    ('05_soldadito_de_hierro', 'Dilan_05_Soldadito_De_Hierro.pdf',
     dict(num=5, title='Soldadito de Hierro', subtitle='Nil Moliner',
          tonalidad='La menor', dificultad=2)),
    ('06_merry_little_christmas', 'Dilan_06_Merry_Little_Christmas.pdf',
     dict(num=6, title='Have Yourself a Merry Little Christmas', subtitle='Ralph Blane · Hugh Martin',
          tonalidad='Do mayor', dificultad=2)),
    ('07_santa_tell_me', 'Dilan_07_Santa_Tell_Me.pdf',
     dict(num=7, title='Santa Tell Me', subtitle='Ariana Grande',
          tonalidad='Mi menor', dificultad=2)),
    ('08_beginning_to_look_like_christmas', 'Dilan_08_Beginning_To_Look_Like_Christmas.pdf',
     dict(num=8, title="It's Beginning to Look a Lot Like Christmas", subtitle='Piano Duet · a 4 manos',
          tonalidad='Do mayor', dificultad=3)),
    ('09_writings_on_the_wall', 'Dilan_09_Writings_On_The_Wall.pdf',
     dict(num=9, title="Writing's on the Wall", subtitle='Sam Smith · James Bond',
          tonalidad='Fa mayor', dificultad=2)),
    ('10_arabesque', 'Dilan_10_Arabesque.pdf',
     dict(num=10, title='Arabesque', subtitle='Burgmüller · a 4 manos',
          tonalidad='Do mayor', dificultad=3)),
    ('11_adagio_sol_menor', 'Dilan_11_Adagio_En_Sol_Menor.pdf',
     dict(num=11, title='Adagio en Sol menor', subtitle='Tomaso Albinoni',
          tonalidad='Sol menor', dificultad=3)),
    ('12_al_calor_del_amor_en_un_bar', 'Dilan_12_Al_Calor_Del_Amor_En_Un_Bar.pdf',
     dict(num=12, title='Al Calor del Amor en un Bar', subtitle='Gabinete Caligari',
          tonalidad='Mi menor', dificultad=2)),
    ('13_despacito', 'Dilan_13_Despacito.pdf',
     dict(num=13, title='Despacito', subtitle='Luis Fonsi & Daddy Yankee',
          tonalidad='La menor', dificultad=2)),
    ('14_when_i_was_your_man', 'Dilan_14_When_I_Was_Your_Man.pdf',
     dict(num=14, title='When I Was Your Man', subtitle='Bruno Mars',
          tonalidad='Do mayor', dificultad=2)),
    ('15_schindlers_list', 'Dilan_15_Schindlers_List.pdf',
     dict(num=15, title="Theme from Schindler's List", subtitle='John Williams',
          tonalidad='Sol menor', dificultad=3)),
    ('16_amiga_mia', 'Dilan_16_Amiga_Mia.pdf',
     dict(num=16, title='Amiga Mía', subtitle='Alejandro Sanz',
          tonalidad='Re mayor', dificultad=2)),
    ('17_la_promesa', 'Dilan_17_La_Promesa.pdf',
     dict(num=17, title='La Promesa', subtitle='Melendi',
          tonalidad='Sol mayor', dificultad=2)),
    ('18_lucia', 'Dilan_18_Lucia.pdf',
     dict(num=18, title='Lucía', subtitle='Joan Manuel Serrat',
          tonalidad='La menor', dificultad=3)),
    ('19_poema_de_amor', 'Dilan_19_Poema_De_Amor.pdf',
     dict(num=19, title='Poema de Amor', subtitle='Joan Manuel Serrat',
          tonalidad='Sol menor', dificultad=3)),
    ('20_when_we_were_young', 'Dilan_20_When_We_Were_Young.pdf',
     dict(num=20, title='When We Were Young', subtitle='Adele',
          tonalidad='Re menor', dificultad=3)),
    ('21_thinking_out_loud', 'Dilan_21_Thinking_Out_Loud.pdf',
     dict(num=21, title='Thinking Out Loud', subtitle='Ed Sheeran',
          tonalidad='Re mayor', dificultad=3)),
    ('22_my_favourite_things', 'Dilan_22_My_Favourite_Things.pdf',
     dict(num=22, title='My Favourite Things', subtitle='Sound of Music',
          tonalidad='Mi menor', dificultad=3)),
    ('23_bohemian_rhapsody', 'Dilan_23_Bohemian_Rhapsody.pdf',
     dict(num=23, title='Bohemian Rhapsody', subtitle='Queen',
          tonalidad='Sib mayor', dificultad=4)),
    ('24_your_song', 'Dilan_24_Your_Song.pdf',
     dict(num=24, title='Your Song', subtitle='Elton John · cierre de curso',
          tonalidad='Mib mayor', dificultad=4)),
]

MONTHS = [
    ('Septiembre', [SONGS[0][2], SONGS[1][2]]),
    ('Octubre', [SONGS[2][2], SONGS[3][2]]),
    ('Noviembre', [SONGS[4][2]]),
    ('Diciembre', [SONGS[5][2], SONGS[6][2], SONGS[7][2]]),
    ('Enero', [SONGS[8][2]]),
    ('Febrero', [SONGS[9][2]]),
    ('Marzo', [SONGS[10][2]]),
    ('Abril', [SONGS[11][2], SONGS[12][2], SONGS[13][2], SONGS[14][2]]),
    ('Mayo', [SONGS[15][2], SONGS[16][2], SONGS[17][2], SONGS[18][2], SONGS[19][2]]),
    ('Junio', [SONGS[20][2], SONGS[21][2], SONGS[22][2], SONGS[23][2]]),
]


def _run_song_build(folder):
    """Imports and runs students/dilan/<folder>/build.py's main(), regenerating
       that song's standalone dossier PDF in output/."""
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

    album_path = os.path.join(OUT_DIR, 'Dilan_Cuaderno_del_Pianista.pdf')
    with open(album_path, 'wb') as f:
        writer.write(f)
    os.remove(portada_path)
    print('generated', album_path)


if __name__ == '__main__':
    main()
