from reportlab.pdfgen import canvas
from page_theory_generic import build_theory_page, W, H
from page_exercises_song20 import page1, page2
from page_worksheet_generic import build_worksheet

song20 = dict(
  num=20, title='Here We Go Round the Mulberry Bush', subtitle='Canción tradicional · arr. Regina Pratley (4 manos)',
  tonalidad='Do mayor', compas='6/8', tempo='Balanceado ♩.≈60', forma='Se repite',
  dificultad='Fácil', manos='Melodía + acordes',
  la_cancion='«Damos la vuelta a la morera». Un juego en corro con un balanceo bonito en 6/8: se cuenta en dos grupos de tres.',
  difficult_cc='cc. 1–4', difficult_title='El balanceo de 6/8',
  reto='sentir los dos pulsos por compás, no seis golpes.',
  truco='cuenta «UN-dos-tres, DOS-dos-tres» marcando el UN y el DOS.',
  sabias_que='Esta canción de corro británica tiene siglos de antigüedad. Los niños se cogen de las manos y giran en círculo mientras la cantan, ¡como un tiovivo!',
  mini_staff_events=[{'pitch': p, 'dur': 'e', 'beam': i // 3} for i, p in enumerate(['C4', 'D4', 'E4', 'F4', 'G4', 'F4'])],
  time_sig=(6, 8),
  ritmo_texto='Ritmo: compás de 6/8 — se cuenta en dos grandes pulsos, «1-2-3 / 4-5-6», como un balanceo.',
)
cfg20 = {
 'kicker': 'NIVEL 2 · AVANZO · HERE WE GO ROUND THE MULBERRY BUSH',
 'sec1_treble': ['Do','Mi','Sol','Do','Fa','Do','Sol','Mi'],
 'sec1_bass': ['Sol','Si','Re','Sol','Do','Sol','Re','Si'],
 'sec1_alto': ['Fa','La','Do','Fa','Sib','Fa','Do','La'],
 'sec2_title': 'Marca los dos pulsos y dibuja la plica',
 'sec2_desc': 'Rodea cada grupo de tres notas (un pulso). Deberías encontrar dos grupos por línea. Luego dibuja la plica.',
 'sec2_pitches': ['C4','D4','E4','F4','G4','F4','G4','F4','E4','D4','C4','D4'],
 'sec3_title': 'Colorea solo las notas DO (la nota casa)',
 'sec3_desc': 'Repasa cada nota y pinta de verde únicamente las que sean DO. Las demás, déjalas en blanco.',
 'sec3_treble': ['C4','D4','E4','C4','F4','C4','G4','E4','C4','D4','E4','C4'],
 'sec3_bass': ['C3','D3','E3','C3','F3','C3','G3','E3','C3','D3','E3','C3'],
 'pista_text': 'en clave de Sol, DO está en la primera línea adicional bajo el pentagrama (con su rayita); en clave de Fa, DO está en el segundo espacio.',
 'quiz_pitches': ['C4','E4','G4','D4','F4','A4','C4'],
}

c = canvas.Canvas('/home/claude/work/song20_generated.pdf', pagesize=(W, H))
build_theory_page(c, '/home/claude/work/asset_qr_real.png', song20)
c.showPage()
page1(c)
page2(c)
build_worksheet(c, cfg20)
c.save()
print('generated')
