# La figura impresa en cada partitura — medida sobre el PDF

Medido con `cuaderno/medir_figuras.py` sobre el PDF real de la carpeta de cada
alumno. La columna **barras dobles** cuenta los pares de barras paralelas
(semicorcheas) que aparecen impresos; **rabitos** cuenta los tramos cortos, que
son ruidosos y NO se usan para decidir nada.

Esto es lo que faltaba: las transcripciones anotaban edición, tonalidad,
compás, tempo y páginas, pero nunca la figura más corta. Sin ese dato no había
forma de saber si un dosier estaba escondiendo una figura que la partitura
lleva impresa, y no lo detectaba ningún auditor.

## Lo que este documento NO puede decir

**31 partituras salen como NO MEDIBLE**, y hay que mirarlas a ojo. No son PDF
vectoriales: llevan dentro una foto de la partitura, a veces de 50 o 60 ppi. A
esa resolución las dos barras de una semicorchea ocupan menos de dos píxeles y
no se pueden separar — rasterizar el PDF más grande no añade información, solo
agranda el borrón.

Esto costó un error que conviene tener escrito: la primera versión de la
herramienta daba **321 semicorcheas en el Flying Theme**, que va entero en
corcheas. Al mirarlo a tamaño grande se ve una sola barra por grupo. Ahora la
herramienta mide el espacio de pentagrama en píxeles y, si no llega al mínimo,
dice NO MEDIBLE en vez de inventarse un número.

## Cómo se lee

- **≥ 20 barras dobles**: la semicorchea es un rasgo real y extendido. Si el
  dosier no la escribe, es un hueco.
- **1–19**: hay que mirarlo a ojo. En ese rango se cuelan falsos positivos: dos
  cabezas de acorde con puntillo dejan el mismo dibujo en una columna de
  píxeles que dos barras.
- **0**: la partitura no lleva semicorcheas.

Contrastado contra las partituras de `medir_figuras_patron.py`, miradas una a
una a tamaño grande.

## Los 12 huecos seguros

| barras dobles | pieza | partitura |
|---|---|---|
| 143 | dilan_17_arabesque | arabesque-burgmuller-( 4 manos).pdf |
| 106 | dilan_07_amiga | Amiga mia-alejandro Sanz.pdf |
| 106 | eva_09_amiga | Amiga mia-alejandro Sanz.pdf |
| 93 | eva_10_young | WHEN WE WERE YOUNG _ Adele Dm .pdf |
| 45 | jm_17_acomme | A COMME AMOUR _ Richard Clayderman. |
| 45 | ed_17_acomme | A COMME AMOUR _ Richard Clayderman. |
| 44 | dilan_11_soldadito | SOLDADITO DE HIERRO _ Nil Moliner_.pdf |
| 44 | eva_11_soldadito | SOLDADITO DE HIERRO _ Nil Moliner.pdf |
| 24 | eva_17_bohemian | bohemian-rhapsody.pdf |
| 22 | dilan_19_santa | Santa-tell-me-ariana-grande NAVIDAD.pdf |
| 22 | eva_14_santa | Santa-tell-me-ariana-grande.pdf |
| 20 | is_20_diabelli | DIABELLI ( cuatro manos).pdf |

## Las 31 partituras no medibles (hay que mirarlas)

- -LOVELY.pdf
- -PEACHES.
- BELLA Y BESTIA .pdf
- Baa Baa Black Sheep.pdf
- Chopsticks.pdf
- Clementine.pdf
- Como entrenar a tu dragon.
- Copia de Copia de Como entrenar a tu dragon.
- Copia de Copia de Toreador. Bizet
- Do Your Ears Hang Low?.pdf
- Grandfather's Clock.pdf
- Grandfather.pdf
- Himno de Estados Unidos.pdf
- JOLLY OLD SAINT NICHOLAS.pdf
- LAS CUATRO ESTACIONES.pdf
- LOVELY.
- Little Miss Muffet.pdf
- MyBonnie.pdf
- OH WHEN THE SAINT.pdf
- Oh when the Saint.pdf
- Polly Put the Kettle On.pdf
- SUR LE PONT D'AVIGNON.pdf
- TOREADOR-BIZET. Bizet
- TOREADOR-BIZET.pdf
- The Wheels on the Bus.pdf
- Toreador. Bizet
- WE WISH A MERRY CRISTMAS.pdf
- al-calor-del-amor-en-un-bar.pdf
- himno America.pdf
- rain-rain-away-easy-piano-4 manos.pdf
- the-mulberry-bush-185807.4 manos.pdf

## La tabla completa

| pieza | escribe | estado | barras dobles | rabitos | partitura |
|---|---|---|---|---|---|
| arnau_01_chopsticks | 0 | nomedible | 0 | 0 | Chopsticks.pdf |
| arnau_02_clementine | 0 | nomedible | 0 | 0 | Clementine.pdf |
| arnau_03_jolly | 0 | nomedible | 0 | 0 | JOLLY OLD SAINT NICHOLAS.pdf |
| arnau_04_ears | 0 | nomedible | 0 | 0 | Do Your Ears Hang Low?.pdf |
| arnau_05_wheels | 0 | nomedible | 0 | 0 | The Wheels on the Bus.pdf |
| arnau_06_saints | 0 | nomedible | 0 | 0 | Oh when the Saint.pdf |
| arnau_07_wewish | 0 | nomedible | 0 | 0 | WE WISH A MERRY CRISTMAS.pdf |
| arnau_08_baabaa | 0 | nomedible | 0 | 0 | Baa Baa Black Sheep.pdf |
| arnau_09_polly | 0 | nomedible | 0 | 0 | Polly Put the Kettle On.pdf |
| arnau_10_muffet | 0 | nomedible | 0 | 0 | Little Miss Muffet.pdf |
| arnau_11_eso | 0 | ok | 0 | 0 | Eso-que-tu-me-das. Jarabe de Palo.pdf |
| arnau_12_puff | 0 | ok | 0 | 0 | puff-the-magic-dragon.pdf |
| arnau_13_pantera | 0 | ok | 0 | 0 | La Pantera Rosa.pdf |
| arnau_14_bonnie | 0 | nomedible | 0 | 0 | MyBonnie.pdf |
| arnau_15_largo | 0 | ok | 1 | 0 | Largo-Sinfonia 5 Dvorak.pdf |
| arnau_16_aloha | 0 | ok | 15 | 24 | Aloha oe.sib.pdf |
| arnau_17_popeye | 0 | ok | 0 | 1 | Popeye el marinerito.pdf |
| arnau_18_submarino | 0 | ok | 0 | 0 | ElSubmarinoAmarillo-.pdf |
| arnau_19_rain | 0 | nomedible | 0 | 0 | rain-rain-away-easy-piano-4 manos.pdf |
| arnau_20_mulberry | 0 | nomedible | 0 | 0 | the-mulberry-bush-185807.4 manos.pdf |
| lu_01_bambini | 0 | ok | 3 | 0 | bazzoni-maurizio-sonatina-per-bambini-(4 manos).pdf |
| lu_02_beginner | 0 | ok | 0 | 3 | The Beginner Le Debut.pdf |
| lu_03_sonatina2 | 0 | ok | 5 | 0 | _bazzoni-maurizio-sonatina-sol-maggiore (4 manos).pdf |
| lu_04_friend | 0 | ok | 0 | 0 | youve-got-a-friend-in-me-easy-piano-.pdf |
| lu_05_puff | 0 | ok | 0 | 0 | puff-the-magic-dragon. |
| lu_06_dream | 0 | ok | 1 | 11 | i-have-a-dream-abba-children-song.pdf |
| lu_07_christmas | 0 | ok | 0 | 9 | christmas-songs-(4 manos).pdf |
| lu_08_silent | 0 | ok | 0 | 1 | Silent-Night.easy |
| lu_09_spring | 0 | ok | 0 | 2 | LA PRIMAVERA.pdf easy |
| lu_10_titanic | 0 | ok | 6 | 3 | Titanic easy.pdf |
| lu_11_pianoman | 0 | ok | 0 | 5 | piano-man-easy. |
| lu_12_panthere | 0 | ok | 0 | 0 | la-panthere-rose-easy.pdf |
| lu_13_belaciao | 0 | ok | 0 | 2 | bela-ciao.easy |
| lu_14_heart | 0 | ok | 1 | 10 | heart-and-soul-hoagy-carmIchael easy.pdf |
| lu_15_greensleeves | 0 | ok | 4 | 0 | Copia de 1-----Greensleeves.pdf |
| lu_16_chimchim | 0 | ok | 0 | 3 | Mary Popins FACIL.pdf |
| lu_17_rasputin | 0 | ok | 0 | 1 | rasputin easy.pdf |
| lu_18_furelise | 0 | ok | 0 | 0 | Para  Elisa easy.pdf |
| lu_19_nocturne | 0 | ok | 0 | 7 | nocturne-op9-chopin. easy |
| jm_01_romance | 0 | ok | 6 | 16 | Romance-Diabelli 4 manos.pdf |
| jm_02_america | 0 | nomedible | 0 | 0 | himno America.pdf |
| jm_03_banner | 0 | nomedible | 0 | 0 | Himno de Estados Unidos.pdf |
| jm_04_counting | 0 | ok | 8 | 0 | Counting-stars.pdf |
| jm_05_peaches | 0 | nomedible | 0 | 0 | -PEACHES. |
| jm_06_someone | 0 | ok | 0 | 2 | SOMEONE YOU LOVED. |
| jm_07_deck | 0 | ok | 0 | 10 | Deck the Halls (with Boughs of Holly) NAVIDAD.pdf |
| jm_08_jailhouse | 0 | ok | 2 | 2 | jailhouse-rock-elvis-presley-.pdf |
| jm_09_clock | 0 | nomedible | 0 | 0 | Grandfather's Clock.pdf |
| jm_10_shallow | 0 | ok | 3 | 68 | SHALLOW. |
| jm_11_canthelp | 0 | ok | 0 | 5 | cant-help-falling-in-love-elvis-presley. |
| jm_12_carol | 0 | ok | 4 | 17 | carol-of-the-bells   NAVIDAD. |
| jm_13_adagio | 0 | ok | 0 | 0 | ADAGIO. |
| jm_14_rasputin | 0 | ok | 0 | 1 | Rasputin.pdf |
| jm_15_toreador | 0 | nomedible | 0 | 0 | Toreador. Bizet |
| jm_16_trouble | 0 | ok | 0 | 2 | Trouble. |
| jm_17_acomme | 0 | ok | 45 | 5 | A COMME AMOUR _ Richard Clayderman. |
| jm_18_interstellar | 0 | ok | 8 | 0 | Interstellar _ .pdf |
| jm_19_flying | 0 | nomedible | 0 | 0 | Como entrenar a tu dragon. |
| ed_01_romance | 0 | ok | 6 | 16 | Romance-Diabelli 4 manos.pdf |
| ed_02_america | 0 | nomedible | 0 | 0 | himno America.pdf |
| ed_03_banner | 0 | nomedible | 0 | 0 | Himno de Estados Unidos.pdf |
| ed_04_counting | 0 | ok | 8 | 0 | Counting-stars.pdf |
| ed_05_peaches | 0 | nomedible | 0 | 0 | -PEACHES. |
| ed_06_someone | 0 | ok | 0 | 2 | SOMEONE YOU LOVED. |
| ed_07_deck | 0 | ok | 0 | 10 | Deck the Halls (with Boughs of Holly) NAVIDAD.pdf |
| ed_08_jailhouse | 0 | ok | 2 | 2 | jailhouse-rock-elvis-presley-.pdf |
| ed_09_clock | 0 | nomedible | 0 | 0 | Grandfather's Clock.pdf |
| ed_10_shallow | 0 | ok | 3 | 68 | SHALLOW. |
| ed_11_canthelp | 0 | ok | 0 | 5 | cant-help-falling-in-love-elvis-presley. |
| ed_12_carol | 0 | ok | 4 | 17 | carol-of-the-bells   NAVIDAD. |
| ed_13_adagio | 0 | ok | 0 | 0 | ADAGIO. |
| ed_14_rasputin | 0 | ok | 0 | 1 | Rasputin.pdf |
| ed_15_toreador | 0 | nomedible | 0 | 0 | Toreador. Bizet |
| ed_16_trouble | 0 | ok | 0 | 2 | Trouble. |
| ed_17_acomme | 0 | ok | 45 | 5 | A COMME AMOUR _ Richard Clayderman. |
| ed_18_interstellar | 0 | ok | 8 | 0 | Interstellar _ .pdf |
| ed_19_flying | 0 | nomedible | 0 | 0 | Como entrenar a tu dragon. |
| me_01_bambini | 0 | ok | 3 | 0 | Maurizio Bazzoni sonatina para 4 manos.pdf |
| me_02_saints | 0 | nomedible | 0 | 0 | OH WHEN THE SAINT.pdf |
| me_03_friend | 0 | ok | 0 | 0 | Hay un amigo en mi.pdf |
| me_04_puff | 0 | ok | 0 | 0 | Puff era un Drac Magic.pdf |
| me_05_sonatina2 | 0 | ok | 5 | 0 | bazzoni-maurizio-sonatia-sol-maggiore-174724. |
| me_06_avignon | 0 | nomedible | 0 | 0 | SUR LE PONT D'AVIGNON.pdf |
| me_07_doremi | 0 | ok | 0 | 1 | Sonrisas y Lagrimas.pdf |
| me_08_christmas | 0 | ok | 0 | 9 | christmas-songs-for-four-little- 4 manos.pdf |
| me_09_silentnight | 0 | ok | 0 | 1 | SILENT NINGT.easy |
| me_10_wewishyou | 0 | ok | 0 | 6 | WE WISH YOU A MERRY CHRISTMAS.pdf |
| me_11_silentnight4h | 0 | ok | 0 | 2 | silent-night-4-hands. |
| me_12_panthere | 0 | ok | 0 | 0 | La Pantera Rosa.pdf |
| me_13_pianoman | 0 | ok | 0 | 5 | Piano Men.pdf |
| me_14_belaciao | 0 | ok | 0 | 2 | bela-ciao.pdf |
| me_15_spring | 0 | nomedible | 0 | 0 | LAS CUATRO ESTACIONES.pdf |
| me_16_greensleeves | 0 | ok | 4 | 0 | -Greensleeves.pdf |
| me_17_countingstars | 0 | ok | 8 | 0 | counting-stars-.pdf |
| me_18_largodvorak | 0 | ok | 1 | 0 | -Largo-Sinfonia 5 Dvorak.pdf |
| me_19_grandfather | 0 | nomedible | 0 | 0 | Grandfather.pdf |
| me_20_dream | 0 | ok | 1 | 11 | i-have-a-dream-abba-.pdf |
| me_21_beauty | 0 | nomedible | 0 | 0 | BELLA Y BESTIA .pdf |
| me_22_gladiator | 0 | ok | 0 | 22 | Gladyator.pdf |
| me_23_rasputin | 0 | ok | 0 | 1 | Rasputin.pdf |
| me_24_jailhouse | 0 | ok | 2 | 2 | Jailhouse Elvis Presley.pdf |
| me_25_toreador | 0 | nomedible | 0 | 0 | TOREADOR-BIZET. Bizet |
| me_26_furelise | 0 | ok | 1 | 3 | Para Elisa.pdf |
| me_27_nocturne | 0 | ok | 0 | 7 | nocturne-op9-chopin. |
| is_01_petite | 0 | ok | 1 | 21 | petite chanson(4 manos).pdf |
| is_02_saints | 0 | nomedible | 0 | 0 | OH WHEN THE SAINT.pdf |
| is_03_puff | 0 | ok | 0 | 0 | Puff era un Drac Magic.pdf |
| is_04_beginner | 0 | ok | 0 | 3 | The Beginer le Debut(4 manos).pdf |
| is_05_wewishyou | 0 | ok | 0 | 6 | WE WISH YOU A MERRY CHRISTMAS.pdf |
| is_06_christmas | 0 | ok | 0 | 9 | christmas-songs-( 4 manos).pdf |
| is_07_silentnight | 0 | ok | 0 | 1 | SILENT NINGT.pdf |
| is_08_silentnight4h | 0 | ok | 0 | 2 | silent-night-(4 manos).pdf |
| is_09_panthere | 0 | ok | 0 | 0 | La Pantera Rosa.pdf |
| is_10_pianoman | 0 | ok | 0 | 5 | Piano Men.pdf |
| is_11_greensleeves | 0 | ok | 4 | 0 | -Greensleeves. |
| is_12_grandfather | 0 | nomedible | 0 | 0 | Grandfather.pdf |
| is_13_doremi | 0 | ok | 0 | 1 | Sonrisas y Lagrimas.pdf |
| is_14_dream | 0 | ok | 1 | 11 | i-have-a-dream-abba-.pdf |
| is_15_gladiator | 0 | ok | 0 | 22 | Gladyator.pdf |
| is_16_rasputin | 0 | ok | 0 | 1 | Rasputin.pdf |
| is_17_jailhouse | 0 | ok | 2 | 2 | Jailhouse Elvis Presley.pdf |
| is_18_toreador | 0 | nomedible | 0 | 0 | TOREADOR-BIZET.pdf |
| is_19_furelise | 16 | ok | 1 | 3 | Para Elisa.pdf |
| is_20_diabelli | 0 | ok | 20 | 14 | DIABELLI ( cuatro manos).pdf |
| jp_01_romance | 0 | ok | 6 | 16 | Romance-Diabelli 4 manos.pdf |
| jp_02_petite | 0 | ok | 1 | 21 | Petite chanson.(4 MANOS) |
| jp_03_peaches | 8 | nomedible | 0 | 0 | -PEACHES. |
| jp_04_counting | 0 | ok | 8 | 0 | Counting-stars.pdf |
| jp_05_what | 0 | ok | 14 | 21 | what-was-i-made-for-billie-eilish.pdf |
| jp_06_heart | 0 | ok | 1 | 10 | heart-and-soul-.pdf |
| jp_07_hittheroad | 0 | ok | 0 | 0 | hit-the-road-jack-ray-.pdf |
| jp_08_deck | 0 | ok | 0 | 10 | Deck the Halls  NAVIDAD.pdf |
| jp_09_jailhouse | 0 | ok | 2 | 2 | jailhouse-rock-elvis-presley-.pdf |
| jp_10_bellaciao | 0 | ok | 0 | 13 | bella-ciao-piano-(4 MANOS).pdf |
| jp_11_canthelp | 0 | ok | 0 | 5 | cant-help-falling-in-love-elvis-presley. |
| jp_12_lovely | 0 | nomedible | 0 | 0 | -LOVELY.pdf |
| jp_13_rasputin | 0 | ok | 0 | 1 | Rasputin.pdf |
| jp_14_beginning | 0 | ok | 1 | 29 | its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf |
| jp_15_favourite | 0 | ok | 5 | 7 | my-favourite-things-the-sound-.pdf |
| jp_16_sweetchild | 0 | ok | 0 | 0 | sweet-child-o-mine-guns-n-roses-easy-piano.pdf |
| jp_17_unbeso | 8 | ok | 38 | 22 | Un beso-y-una-flor-nino-bravo.pdf |
| jp_18_merry | 0 | ok | 9 | 9 | merry-go-round-of-life.pdf |
| jp_19_acomme | 8 | ok | 45 | 5 | A COMME AMOUR _ Richard Clayderman. |
| nl_01_petite | 0 | ok | 1 | 21 | petite chanson.(4 manos) |
| nl_02_counting | 0 | ok | 8 | 0 | Counting-stars-.pdf |
| nl_03_deck | 0 | ok | 0 | 10 | Deck the Halls (NAVIDAD).pdf |
| nl_04_heart | 0 | ok | 1 | 10 | heart-and-soul-.pdf |
| nl_05_hittheroad | 0 | ok | 0 | 0 | hit-the-road-jack-ray-.pdf |
| nl_06_jailhouse | 0 | ok | 2 | 2 | jailhouse-rock-elvis-presley-.pdf |
| nl_07_bellaciao | 0 | ok | 0 | 13 | bella-ciao-piano( 4 manos).pdf |
| nl_08_canthelp | 0 | ok | 0 | 5 | Cant-Falling-in-love-elvis-presley. |
| nl_09_toreador | 0 | nomedible | 0 | 0 | Copia de Copia de Toreador. Bizet |
| nl_10_lovely | 0 | nomedible | 0 | 0 | LOVELY. |
| nl_11_rasputin | 0 | ok | 0 | 1 | Rasputin.pdf |
| nl_12_diamonds | 0 | ok | 17 | 18 | rihanna-diamond-.pdf |
| nl_13_favourite | 0 | ok | 5 | 7 | my-favourite-things-the-sound-.pdf |
| nl_14_sweetchild | 0 | ok | 0 | 0 | sweet-child-o-mine-guns-n-roses-easy-piano.pdf |
| nl_15_merry | 0 | ok | 9 | 9 | Merry-go-round-of-life-easy-piano-excerpt.pdf |
| nl_16_acomme | 8 | ok | 45 | 5 | Copia de Copia de  A COMME AMOUR _ Richard Clayderman. |
| nl_17_dragon | 0 | nomedible | 0 | 0 | Copia de Copia de Como entrenar a tu dragon. |
| dilan_01_cancion | 0 | ok | 0 | 21 | the-swan.pdf |
| dilan_02_cancion | 0 | ok | 0 | 5 | cant-help-falling-in-love-.pdf |
| dilan_03_your_song | 8 | ok | 70 | 41 | YOUR SONG _ Elton John_.pdf |
| dilan_04_thinking | 0 | ok | 1 | 2 | THINKING OUT LOUD _ Ed Sheeran_.pdf |
| dilan_05_lucia | 8 | ok | 48 | 16 | Lucia_.pdf |
| dilan_06_poema | 0 | ok | 0 | 13 | poema-de-amor-joan-manuel-serrat_.pdf |
| dilan_07_amiga | 0 | ok | 106 | 1 | Amiga mia-alejandro Sanz.pdf |
| dilan_08_promesa | 8 | ok | 137 | 6 | la-promesa-MELENDI.pdf |
| dilan_09_bruno | 8 | ok | 118 | 56 | WHEN I WAS YOUR MAN _ Bruno Mars_.pdf |
| dilan_10_calor | 0 | nomedible | 0 | 0 | al-calor-del-amor-en-un-bar.pdf |
| dilan_11_soldadito | 0 | ok | 44 | 28 | SOLDADITO DE HIERRO _ Nil Moliner_.pdf |
| dilan_12_sky | 8 | ok | 28 | 58 | a-sky-full-of-stars-coldplay.pdf |
| dilan_13_what | 0 | ok | 14 | 21 | what-was-i-made-for-billie-eilish.pdf |
| dilan_14_writings | 0 | ok | 19 | 10 | WRITING_S ON THE WALL _ Sam Smith_.pdf |
| dilan_15_favourite | 0 | ok | 5 | 7 | my-favourite-things-the-sound-.pdf |
| dilan_16_adagio | 0 | ok | 18 | 3 | Adagio en sol menor. Albinoni.pdf |
| dilan_17_arabesque | 0 | ok | 143 | 3 | arabesque-burgmuller-( 4 manos).pdf |
| dilan_18_merry | 0 | ok | 9 | 9 | have-yourself-a-merry-little-NAVIDAD       ADhristmas_.pdf |
| dilan_19_santa | 0 | ok | 22 | 8 | Santa-tell-me-ariana-grande NAVIDAD.pdf |
| dilan_20_beginning | 0 | ok | 1 | 29 | its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf |
| eva_01_canthelp | 0 | ok | 0 | 5 | cant-help-falling-in-love-.pdf |
| eva_02_sky | 8 | ok | 28 | 58 | a-sky-full-of-stars-coldplay.pdf |
| eva_03_poema | 0 | ok | 0 | 13 | poema-de-amor-joan-manuel-serrat.pdf |
| eva_04_what | 0 | ok | 14 | 21 | what-was-i-made-for-billie-eilish.pdf |
| eva_05_thinking | 0 | ok | 1 | 2 | THINKING OUT LOUD _ Ed Sheeran .pdf |
| eva_06_cisne | 0 | ok | 0 | 21 | the-swan.pdf |
| eva_07_bruno | 8 | ok | 118 | 56 | WHEN I WAS YOUR MAN _ Bruno Mars.pdf |
| eva_08_promesa | 8 | ok | 137 | 6 | la-promesa-MELENDI.pdf |
| eva_09_amiga | 0 | ok | 106 | 1 | Amiga mia-alejandro Sanz.pdf |
| eva_10_young | 0 | ok | 93 | 88 | WHEN WE WERE YOUNG _ Adele Dm .pdf |
| eva_11_soldadito | 0 | ok | 44 | 28 | SOLDADITO DE HIERRO _ Nil Moliner.pdf |
| eva_12_favourite | 0 | ok | 5 | 7 | my-favourite-things-the-sound-.pdf |
| eva_13_merry | 0 | ok | 9 | 9 | have-yourself-a-merry-little-christmas.pdf |
| eva_14_santa | 0 | ok | 22 | 8 | Santa-tell-me-ariana-grande.pdf |
| eva_15_beginning | 0 | ok | 1 | 29 | its-beginning-to-look-a-lot-like (4 manos).pdf |
| eva_16_arabesque | 8 | ok | 143 | 3 | arabesque-burgmuller-( 4 manos).pdf |
| eva_17_bohemian | 0 | ok | 24 | 2 | bohemian-rhapsody.pdf |
