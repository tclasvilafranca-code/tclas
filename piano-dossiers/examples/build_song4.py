from reportlab.pdfgen import canvas
from page_theory_generic import build_theory_page, W, H
from page_exercises_song4 import page1, page2
from page_worksheet_generic import build_worksheet

song4 = dict(
  num=4, title='Do Your Ears Hang Low?', subtitle='Canción tradicional · arr. Gilbert DeBenedetti',
  tonalidad='Do mayor', compas='4/4', tempo='Gracioso ♩≈108', forma='A–B',
  dificultad='Muy fácil', manos='Melodía + acordes',
  la_cancion='Una canción divertida y un poco tonta sobre unas orejas que cuelgan. Se toca con ganas de reír, ligera y saltarina.',
  difficult_cc='cc. 1–4', difficult_title='Notas repetidas',
  reto='repetir la misma nota sin que se atasque el dedo.',
  truco='cambia de dedo al repetir (3-2-1) para que suene ágil.',
  sabias_que='Esta canción usa una melodía muy antigua que también sirve para "Auld Lang Syne" en algunas versiones populares infantiles. ¡La misma tonada, letras distintas!',
  mini_staff_events=[{'pitch':p,'dur':'q','number':n} for p,n in [('C4',1),('D4',2),('E4',3),('F4',4),('G4',5),('F4',4)]] + [{'pitch':'C4','dur':'h','number':1}],
)
cfg4 = {
 'kicker': 'NIVEL 1 · EMPIEZO · DO YOUR EARS HANG LOW?',
 'sec1_treble': ['Do', 'Si', 'La', 'Sol', 'Fa', 'Mi', 'Re', 'Do'],
 'sec1_bass': ['Sol', 'Fa', 'Mi', 'Re', 'Do', 'Si', 'La', 'Sol'],
 'sec1_alto': ['Fa', 'Mi', 'Re', 'Do', 'Si', 'La', 'Sol', 'Fa'],
 'sec2_title': 'Marca las notas repetidas y dibuja la plica',
 'sec2_desc': 'Rodea cada nota que se repite justo después de sí misma. Luego dibújales la plica en la dirección correcta.',
 'sec2_pitches': ['E4','E4','D4','C4','C4','D4','G4','G4','F4','E4','E4','C4'],
 'sec3_title': 'Colorea solo las notas MI (la que más se repite)',
 'sec3_desc': 'Repasa cada nota y pinta de naranja únicamente las que sean MI. Las demás, déjalas en blanco.',
 'sec3_treble': ['E4','E4','D4','C4','E4','E4','G4','F4','E4','D4','C4','E4'],
 'sec3_bass': ['E3','E3','D3','C3','E3','E3','G3','F3','E3','D3','C3','E3'],
 'pista_text': 'en clave de Sol, MI está en la primera línea (la de abajo); en clave de Fa, MI está en el tercer espacio.',
 'quiz_pitches': ['G4','E4','C4','D4','F4','A4','E4'],
}

c = canvas.Canvas('/home/claude/work/song4_generated.pdf', pagesize=(W, H))
build_theory_page(c, '/home/claude/work/asset_qr_real.png', song4)
c.showPage()
page1(c)
page2(c)
build_worksheet(c, cfg4)
c.save()
print('generated')
