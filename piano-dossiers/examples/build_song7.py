from reportlab.pdfgen import canvas
from page_theory_generic import build_theory_page, W, H
from page_exercises_song7 import page1, page2
from page_worksheet_generic import build_worksheet

song7 = dict(
  num=7, title='Chopsticks', subtitle='Canción tradicional · arr. Gilbert DeBenedetti',
  tonalidad='Do mayor', compas='3/4', tempo='Vals divertido ♩≈120', forma='Se repite',
  dificultad='Muy fácil', manos='Un dedo de cada mano',
  la_cancion='¡El clásico «Chopsticks»! Se toca con un solo dedo de cada mano y suena divertidísimo. Es un vals: cuenta 1-2-3.',
  difficult_cc='cc. 1–4', difficult_title='Las dos manos a la vez',
  reto='que las dos manos toquen justo al mismo tiempo.',
  truco='cuenta 1-2-3 en voz alta y baja los dos dedos en el «1».',
  sabias_que='"Chopsticks" lo compuso en 1877 una joven de 16 años, Euphemia Allen, bajo el seudónimo "Arthur de Lulli". ¡Nunca imaginó que se haría tan famosa!',
  mini_staff_events=[{'pitch':p,'dur':'q','number':2} for p in ['D4','D4','E4','D4','D4','E4']],
  time_sig=(3,4),
  ritmo_texto='Ritmo: compás de 3/4, un vals — cuenta 1-2-3 en cada compás, con el "1" bien marcado.',
)
cfg7 = {
 'kicker': 'NIVEL 1 · EMPIEZO · CHOPSTICKS',
 'sec1_treble': ['Do', 'Mi', 'Sol', 'Do', 'Re', 'Fa', 'La', 'Do'],
 'sec1_bass': ['Sol', 'Si', 'Re', 'Sol', 'La', 'Do', 'Mi', 'Sol'],
 'sec1_alto': ['Fa', 'La', 'Do', 'Fa', 'Sol', 'Si', 'Re', 'Fa'],
 'sec2_title': 'Marca el patrón Re-Re-Mi y dibuja la plica',
 'sec2_desc': 'Rodea cada grupo de tres notas Re-Re-Mi. Luego dibújales la plica en la dirección correcta.',
 'sec2_pitches': ['D4','D4','E4','D4','D4','E4','F4','F4','G4','F4','F4','G4'],
 'sec3_title': 'Colorea solo las notas RE (donde empieza el patrón)',
 'sec3_desc': 'Repasa cada nota y pinta de morado únicamente las que sean RE. Las demás, déjalas en blanco.',
 'sec3_treble': ['D4','D4','E4','D4','D4','E4','C4','D4','D4','F4','D4','G4'],
 'sec3_bass': ['G2','C3','C3','G2','C3','C3','G2','C3','C3','G2','C3','C3'],
 'pista_text': 'en clave de Sol, RE está justo debajo de la primera línea (sin rayita); en clave de Fa, RE está en la tercera línea, la del medio.',
 'quiz_pitches': ['D4','E4','C4','F4','G4','D4','E4'],
}

c = canvas.Canvas('/home/claude/work/song7_generated.pdf', pagesize=(W, H))
build_theory_page(c, '/home/claude/work/asset_qr_real.png', song7)
c.showPage()
page1(c)
page2(c)
build_worksheet(c, cfg7)
c.save()
print('generated')
