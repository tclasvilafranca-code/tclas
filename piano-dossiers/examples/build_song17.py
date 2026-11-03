from reportlab.pdfgen import canvas
from page_theory_generic import build_theory_page, W, H
from page_exercises_song17 import page1, page2
from page_worksheet_generic import build_worksheet

song17 = dict(
  num=17, title='La Pantera Rosa', subtitle='Henry Mancini · arr. sencillo',
  tonalidad='La menor', compas='4/4', tempo='Misterioso ♩≈100', forma='Tema',
  dificultad='Un reto', manos='Melodía + acordes',
  la_cancion='¡El tema de la Pantera Rosa! Suena misterioso, como el gato que anda de puntillas. Se toca en LA menor.',
  difficult_cc='cc. 1–4', difficult_title='Notas y silencios',
  reto='respetar los silencios: ¡lo que no suena también cuenta!',
  truco='cuenta también los silencios, como si fueran notas mudas.',
  sabias_que='Henry Mancini compuso este tema en 1963 para la película "La Pantera Rosa". Ganó un Grammy y sigue siendo uno de los temas de cine más reconocibles del mundo.',
  mini_staff_events=[{'pitch':p,'dur':'q','number':n} for p,n in [('A4',1),('B4',2),('C5',3),('D5',4),('E5',5),('D5',4)]] + [{'pitch':'C5','dur':'h','number':3}],
  tonic_solfege='La', quinta_solfege='Mi',
  keyboard_notes=['La','Si','Do','Re','Mi','Fa','Sol'], keyboard_highlight=0,
  posicion_titulo='A tocar — posición de La',
  posicion_texto='Mano derecha en posición de LA menor (un dedo por tecla); izquierda: acordes La menor y MI.',
  ritmo_texto='Ritmo: compás de 4/4 — cuenta 1-2-3-4, y también cuenta los silencios.',
  estudiar_steps=['Busca LA y tócala 3 veces (tu nota casa).',
                   'Mano derecha sola, muy despacio, respetando los silencios.',
                   'Acordes La menor y MI con la izquierda, uno por compás.',
                   'Las dos manos juntas: lento primero, luego un poco más rápido.'],
  checklist_items=['Encuentro LA y pongo bien los dedos.', 'Toco la melodía con la mano derecha.',
                    'Hago los acordes La menor y MI con la izquierda.', 'Respeto los silencios sin adelantarme.'],
)
cfg17 = {
 'kicker': 'NIVEL 3 · YA TOCO · LA PANTERA ROSA',
 'sec1_treble': ['La','Do','Mi','La','Re','La','Mi','Do'],
 'sec1_bass': ['Mi','Sol','Si','Mi','La','Mi','Si','Sol'],
 'sec1_alto': ['Re','Fa','La','Re','Sol','Re','La','Fa'],
 'sec2_title': 'Marca dónde hay un silencio',
 'sec2_desc': 'Con una X, marca en el aire debajo de la línea dónde crees que iría un silencio en este patrón. Luego dibuja la plica de las notas.',
 'sec2_pitches': ['A4','C5','B4','A4','C5','B4','A4','C5','B4','A4','C5','B4'],
 'sec3_title': 'Colorea solo las notas LA (la nota casa)',
 'sec3_desc': 'Repasa cada nota y pinta de morado (¡misterioso!) únicamente las que sean LA. Las demás, déjalas en blanco.',
 'sec3_treble': ['A4','C5','E5','A4','D5','A4','B4','C5','A4','E5','D5','A4'],
 'sec3_bass': ['A3','C4','E4','A3','D4','A3','B3','C4','A3','E4','D4','A3'],
 'pista_text': 'en clave de Sol, LA está en el segundo espacio; en clave de Fa, LA está en el primer espacio.',
 'quiz_pitches': ['A4','C5','E5','B4','D5','F5','A4'],
}

c = canvas.Canvas('/home/claude/work/song17_generated.pdf', pagesize=(W, H))
build_theory_page(c, '/home/claude/work/asset_qr_real.png', song17)
c.showPage()
page1(c)
page2(c)
build_worksheet(c, cfg17)
c.save()
print('generated')
