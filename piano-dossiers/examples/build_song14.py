from reportlab.pdfgen import canvas
from page_theory_generic import build_theory_page, W, H
from page_exercises_song14 import page1, page2
from page_worksheet_generic import build_worksheet

song14 = dict(
  num=14, title='Polly Put the Kettle On', subtitle='Canción tradicional · arr. Jim Paterson',
  tonalidad='Fa mayor', compas='4/4', tempo='Alegre ♩≈100', forma='Estrofa',
  dificultad='Fácil', manos='Melodía + acordes',
  la_cancion='«Polly pon la tetera», una cancioncita inglesa de la hora del té. Se toca en FA mayor: aparece una tecla negra, el Sib.',
  difficult_cc='cc. 1–4', difficult_title='Tocar el Sib (tecla negra)',
  reto='meter el dedo 4 en la tecla negra sin fallar.',
  truco='toca solo Fa-Sib-Fa varias veces, buscando la negra sin mirar.',
  sabias_que='Esta rima inglesa del siglo XVIII habla de poner la tetera para el té... ¡y luego quitarla otra vez porque las visitas se han ido! Una escena muy británica.',
  mini_staff_events=[{'pitch':p,'dur':'q','number':n} for p,n in [('F4',1),('G4',2),('A4',3),('Bb4',4),('C5',5),('Bb4',4)]] + [{'pitch':'F4','dur':'h','number':1}],
  tonic_solfege='Fa', quinta_solfege='Do',
  keyboard_notes=['Fa','Sol','La','Sib','Do','Re','Mi'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de Fa',
  posicion_texto='Mano derecha en posición de FA (un dedo por tecla, el 4 en el Sib); izquierda: acordes FA, SIb y DO.',
  estudiar_steps=['Busca FA y tócala 3 veces (tu nota casa).',
                   'Mano derecha sola, muy despacio, sintiendo el Sib con el dedo 4.',
                   'Acordes FA-SIb-DO con la izquierda, uno por compás.',
                   'Las dos manos juntas: lento primero, luego un poco más rápido.'],
  checklist_items=['Encuentro FA y pongo bien los dedos.', 'Toco el Sib con el dedo 4 sin fallar.',
                    'Hago los acordes FA, SIb y DO con la izquierda.', 'Junto las dos manos despacio.'],
)
cfg14 = {
 'kicker': 'NIVEL 2 · AVANZO · POLLY PUT THE KETTLE ON',
 'sec1_treble': ['Fa','Sol','La','Sib','Do','Sib','La','Sol'],
 'sec1_bass': ['Do','Re','Mi','Fa','Sol','Fa','Mi','Re'],
 'sec1_alto': ['Sib','Do','Re','Mi','Fa','Mi','Re','Do'],
 'sec2_title': 'Marca el Sib y dibuja la plica',
 'sec2_desc': 'Rodea cada nota Sib (con el símbolo de bemol ♭) que encuentres. Luego dibújales la plica en la dirección correcta.',
 'sec2_pitches': ['F4','Bb4','F4','A4','Bb4','G4','F4','Bb4','F4','A4','Bb4','C5'],
 'sec3_title': 'Colorea solo las notas FA (la nota casa)',
 'sec3_desc': 'Repasa cada nota y pinta de verde únicamente las que sean FA. Las demás, déjalas en blanco.',
 'sec3_treble': ['F4','Bb4','F4','A4','G4','F4','Bb4','C5','F4','A4','Bb4','F4'],
 'sec3_bass': ['F3','Bb3','F3','A3','G3','F3','Bb3','C4','F3','A3','Bb3','F3'],
 'pista_text': 'en clave de Sol, FA está en el primer espacio; en clave de Fa, FA está en la cuarta línea.',
 'quiz_pitches': ['F4','A4','C5','G4','Bb4','D5','F4'],
}

c = canvas.Canvas('/home/claude/work/song14_generated.pdf', pagesize=(W, H))
build_theory_page(c, '/home/claude/work/asset_qr_real.png', song14)
c.showPage()
page1(c)
page2(c)
build_worksheet(c, cfg14)
c.save()
print('generated')
