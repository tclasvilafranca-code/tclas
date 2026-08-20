# La figura impresa en cada partitura — medida sobre el PDF

Medido con `cuaderno/medir_figuras.py` sobre el PDF real de la carpeta de cada
alumno, a 200 dpi. La columna **barras dobles** cuenta los pares de barras
paralelas (semicorcheas) que aparecen impresos; **rabitos** cuenta los tramos
cortos, que son ruidosos y NO se usan para decidir nada.

Esto es lo que faltaba: las transcripciones anotaban edición, tonalidad,
compás, tempo y páginas, pero nunca la figura más corta. Sin ese dato no había
forma de saber si un dosier estaba escondiendo una figura que la partitura
lleva impresa, y no lo detectaba ningún auditor.

## Cómo se lee

- **≥ 20 barras dobles**: la semicorchea es un rasgo real y extendido de la
  pieza. Si el dosier no la escribe, es un hueco, no una decisión.
- **1–19**: hay que mirarlo a ojo antes de decidir. En ese rango se cuelan
  falsos positivos (dos cabezas de acorde con puntillo dan el mismo dibujo en
  una columna de píxeles que dos barras; pasa en el Jailhouse).
- **0**: la partitura no lleva semicorcheas. Comprobado a ojo en cuatro casos
  (Deck the Halls, When the Saints, Für Elise easy de Luisa y el Nocturno
  easy), y los cuatro dan 0 exacto.

El detector está contrastado contra quince partituras miradas una a una a
tamaño grande (`cuaderno/medir_figuras_patron.py`): las once que llevan
semicorchea dan entre 1 y 143, y las cuatro que no llevan dan 0.

## La tabla

| pieza | escribe | barras dobles | rabitos | partitura |
|---|---|---|---|---|
| arnau_01_chopsticks | 0 | 0 | 3 | Chopsticks.pdf |
| arnau_02_clementine | 0 | 0 | 0 | Clementine.pdf |
| arnau_03_jolly | 0 | 0 | 1 | JOLLY OLD SAINT NICHOLAS.pdf |
| arnau_04_ears | 0 | 0 | 0 | Do Your Ears Hang Low?.pdf |
| arnau_05_wheels | 0 | 3 | 19 | The Wheels on the Bus.pdf |
| arnau_06_saints | 0 | 0 | 0 | Oh when the Saint.pdf |
| arnau_07_wewish | 0 | 0 | 0 | WE WISH A MERRY CRISTMAS.pdf |
| arnau_08_baabaa | 0 | 0 | 0 | Baa Baa Black Sheep.pdf |
| arnau_09_polly | 0 | 0 | 0 | Polly Put the Kettle On.pdf |
| arnau_10_muffet | 0 | 0 | 2 | Little Miss Muffet.pdf |
| arnau_11_eso | 0 | 0 | 0 | Eso-que-tu-me-das. Jarabe de Palo.pdf |
| arnau_12_puff | 0 | 0 | 0 | puff-the-magic-dragon.pdf |
| arnau_13_pantera | 0 | 0 | 0 | La Pantera Rosa.pdf |
| arnau_14_bonnie | 0 | 0 | 0 | MyBonnie.pdf |
| arnau_15_largo | 0 | 1 | 0 | Largo-Sinfonia 5 Dvorak.pdf |
| arnau_16_aloha | 0 | 15 | 24 | Aloha oe.sib.pdf |
| arnau_17_popeye | 0 | 0 | 1 | Popeye el marinerito.pdf |
| arnau_18_submarino | 0 | 0 | 0 | ElSubmarinoAmarillo-.pdf |
| arnau_19_rain | 0 | 0 | 0 | rain-rain-away-easy-piano-4 manos.pdf |
| arnau_20_mulberry | 0 | 0 | 1 | the-mulberry-bush-185807.4 manos.pdf |
| lu_01_bambini | 0 | 3 | 0 | bazzoni-maurizio-sonatina-per-bambini-(4 man |
| lu_02_beginner | 0 | 0 | 3 | The Beginner Le Debut.pdf |
| lu_03_sonatina2 | 0 | 5 | 0 | _bazzoni-maurizio-sonatina-sol-maggiore (4 m |
| lu_04_friend | 0 | 0 | 0 | youve-got-a-friend-in-me-easy-piano-.pdf |
| lu_05_puff | 0 | 0 | 0 | puff-the-magic-dragon. |
| lu_06_dream | 0 | 1 | 12 | i-have-a-dream-abba-children-song.pdf |
| lu_07_christmas | 0 | 0 | 9 | christmas-songs-(4 manos).pdf |
| lu_08_silent | 0 | 0 | 1 | Silent-Night.easy |
| lu_09_spring | 0 | 0 | 2 | LA PRIMAVERA.pdf easy |
| lu_10_titanic | 0 | 6 | 3 | Titanic easy.pdf |
| lu_11_pianoman | 0 | 0 | 5 | piano-man-easy. |
| lu_12_panthere | 0 | 0 | 0 | la-panthere-rose-easy.pdf |
| lu_13_belaciao | 0 | 0 | 2 | bela-ciao.easy |
| lu_14_heart | 0 | 1 | 10 | heart-and-soul-hoagy-carmIchael easy.pdf |
| lu_15_greensleeves | 0 | 4 | 0 | Copia de 1-----Greensleeves.pdf |
| lu_16_chimchim | 0 | 0 | 4 | Mary Popins FACIL.pdf |
| lu_17_rasputin | 0 | 0 | 1 | rasputin easy.pdf |
| lu_18_furelise | 0 | 0 | 0 | Para  Elisa easy.pdf |
| lu_19_nocturne | 0 | 0 | 7 | nocturne-op9-chopin. easy |
| jm_01_romance | 0 | 6 | 21 | Romance-Diabelli 4 manos.pdf |
| jm_02_america | 0 | 0 | 6 | himno America.pdf |
| jm_03_banner | 0 | 0 | 8 | Himno de Estados Unidos.pdf |
| jm_04_counting | 0 | 8 | 0 | Counting-stars.pdf |
| jm_05_peaches | 0 | 153 | 17 | -PEACHES. |
| jm_06_someone | 0 | 0 | 2 | SOMEONE YOU LOVED. |
| jm_07_deck | 0 | 0 | 10 | Deck the Halls (with Boughs of Holly) NAVIDA |
| jm_08_jailhouse | 0 | 2 | 2 | jailhouse-rock-elvis-presley-.pdf |
| jm_09_clock | 0 | 0 | 1 | Grandfather's Clock.pdf |
| jm_10_shallow | 0 | 3 | 69 | SHALLOW. |
| jm_11_canthelp | 0 | 0 | 8 | cant-help-falling-in-love-elvis-presley. |
| jm_12_carol | 0 | 4 | 22 | carol-of-the-bells   NAVIDAD. |
| jm_13_adagio | 0 | 0 | 0 | ADAGIO. |
| jm_14_rasputin | 0 | 0 | 1 | Rasputin.pdf |
| jm_15_toreador | 0 | 6 | 14 | Toreador. Bizet |
| jm_16_trouble | 0 | 0 | 2 | Trouble. |
| jm_17_acomme | 0 | 45 | 5 | A COMME AMOUR _ Richard Clayderman. |
| jm_18_interstellar | 0 | 8 | 0 | Interstellar _ .pdf |
| jm_19_flying | 0 | 321 | 65 | Como entrenar a tu dragon. |
| ed_01_romance | 0 | 6 | 21 | Romance-Diabelli 4 manos.pdf |
| ed_02_america | 0 | 0 | 6 | himno America.pdf |
| ed_03_banner | 0 | 0 | 8 | Himno de Estados Unidos.pdf |
| ed_04_counting | 0 | 8 | 0 | Counting-stars.pdf |
| ed_05_peaches | 0 | 153 | 17 | -PEACHES. |
| ed_06_someone | 0 | 0 | 2 | SOMEONE YOU LOVED. |
| ed_07_deck | 0 | 0 | 10 | Deck the Halls (with Boughs of Holly) NAVIDA |
| ed_08_jailhouse | 0 | 2 | 2 | jailhouse-rock-elvis-presley-.pdf |
| ed_09_clock | 0 | 0 | 1 | Grandfather's Clock.pdf |
| ed_10_shallow | 0 | 3 | 69 | SHALLOW. |
| ed_11_canthelp | 0 | 0 | 8 | cant-help-falling-in-love-elvis-presley. |
| ed_12_carol | 0 | 4 | 22 | carol-of-the-bells   NAVIDAD. |
| ed_13_adagio | 0 | 0 | 0 | ADAGIO. |
| ed_14_rasputin | 0 | 0 | 1 | Rasputin.pdf |
| ed_15_toreador | 0 | 6 | 14 | Toreador. Bizet |
| ed_16_trouble | 0 | 0 | 2 | Trouble. |
| ed_17_acomme | 0 | 45 | 5 | A COMME AMOUR _ Richard Clayderman. |
| ed_18_interstellar | 0 | 8 | 0 | Interstellar _ .pdf |
| ed_19_flying | 0 | 321 | 65 | Como entrenar a tu dragon. |
| me_01_bambini | 0 | 3 | 0 | Maurizio Bazzoni sonatina para 4 manos.pdf |
| me_02_saints | 0 | 0 | 0 | OH WHEN THE SAINT.pdf |
| me_03_friend | 0 | 0 | 0 | Hay un amigo en mi.pdf |
| me_04_puff | 0 | 0 | 0 | Puff era un Drac Magic.pdf |
| me_05_sonatina2 | 0 | 5 | 0 | bazzoni-maurizio-sonatia-sol-maggiore-174724 |
| me_06_avignon | 0 | 0 | 1 | SUR LE PONT D'AVIGNON.pdf |
| me_07_doremi | 0 | 0 | 1 | Sonrisas y Lagrimas.pdf |
| me_08_christmas | 0 | 0 | 9 | christmas-songs-for-four-little- 4 manos.pdf |
| me_09_silentnight | 0 | 0 | 1 | SILENT NINGT.easy |
| me_10_wewishyou | 0 | 0 | 7 | WE WISH YOU A MERRY CHRISTMAS.pdf |
| me_11_silentnight4h | 0 | 0 | 2 | silent-night-4-hands. |
| me_12_panthere | 0 | 0 | 0 | La Pantera Rosa.pdf |
| me_13_pianoman | 0 | 0 | 5 | Piano Men.pdf |
| me_14_belaciao | 0 | 0 | 2 | bela-ciao.pdf |
| me_15_spring | 0 | 35 | 21 | LAS CUATRO ESTACIONES.pdf |
| me_16_greensleeves | 0 | 4 | 0 | -Greensleeves.pdf |
| me_17_countingstars | 0 | 8 | 0 | counting-stars-.pdf |
| me_18_largodvorak | 0 | 1 | 0 | -Largo-Sinfonia 5 Dvorak.pdf |
| me_19_grandfather | 0 | 0 | 1 | Grandfather.pdf |
| me_20_dream | 0 | 1 | 12 | i-have-a-dream-abba-.pdf |
| me_21_beauty | 0 | 151 | 4 | BELLA Y BESTIA .pdf |
| me_22_gladiator | 0 | 0 | 24 | Gladyator.pdf |
| me_23_rasputin | 0 | 0 | 1 | Rasputin.pdf |
| me_24_jailhouse | 0 | 2 | 2 | Jailhouse Elvis Presley.pdf |
| me_25_toreador | 0 | 6 | 14 | TOREADOR-BIZET. Bizet |
| me_26_furelise | 0 | 1 | 3 | Para Elisa.pdf |
| me_27_nocturne | 0 | 0 | 7 | nocturne-op9-chopin. |
| is_01_petite | 0 | 1 | 22 | petite chanson(4 manos).pdf |
| is_02_saints | 0 | 0 | 0 | OH WHEN THE SAINT.pdf |
| is_03_puff | 0 | 0 | 0 | Puff era un Drac Magic.pdf |
| is_04_beginner | 0 | 0 | 3 | The Beginer le Debut(4 manos).pdf |
| is_05_wewishyou | 0 | 0 | 7 | WE WISH YOU A MERRY CHRISTMAS.pdf |
| is_06_christmas | 0 | 0 | 9 | christmas-songs-( 4 manos).pdf |
| is_07_silentnight | 0 | 0 | 1 | SILENT NINGT.pdf |
| is_08_silentnight4h | 0 | 0 | 2 | silent-night-(4 manos).pdf |
| is_09_panthere | 0 | 0 | 0 | La Pantera Rosa.pdf |
| is_10_pianoman | 0 | 0 | 5 | Piano Men.pdf |
| is_11_greensleeves | 0 | 4 | 0 | -Greensleeves. |
| is_12_grandfather | 0 | 0 | 1 | Grandfather.pdf |
| is_13_doremi | 0 | 0 | 1 | Sonrisas y Lagrimas.pdf |
| is_14_dream | 0 | 1 | 12 | i-have-a-dream-abba-.pdf |
| is_15_gladiator | 0 | 0 | 24 | Gladyator.pdf |
| is_16_rasputin | 0 | 0 | 1 | Rasputin.pdf |
| is_17_jailhouse | 0 | 2 | 2 | Jailhouse Elvis Presley.pdf |
| is_18_toreador | 0 | 6 | 14 | TOREADOR-BIZET.pdf |
| is_19_furelise | 16 | 1 | 3 | Para Elisa.pdf |
| is_20_diabelli | 0 | 22 | 33 | DIABELLI ( cuatro manos).pdf |
| jp_01_romance | 0 | 6 | 21 | Romance-Diabelli 4 manos.pdf |
| jp_02_petite | 0 | 1 | 22 | Petite chanson.(4 MANOS) |
| jp_03_peaches | 8 | 153 | 17 | -PEACHES. |
| jp_04_counting | 0 | 8 | 0 | Counting-stars.pdf |
| jp_05_what | 0 | 52 | 39 | what-was-i-made-for-billie-eilish.pdf |
| jp_06_heart | 0 | 1 | 10 | heart-and-soul-.pdf |
| jp_07_hittheroad | 0 | 0 | 0 | hit-the-road-jack-ray-.pdf |
| jp_08_deck | 0 | 0 | 10 | Deck the Halls  NAVIDAD.pdf |
| jp_09_jailhouse | 0 | 2 | 2 | jailhouse-rock-elvis-presley-.pdf |
| jp_10_bellaciao | 0 | 0 | 13 | bella-ciao-piano-(4 MANOS).pdf |
| jp_11_canthelp | 0 | 0 | 8 | cant-help-falling-in-love-elvis-presley. |
| jp_12_lovely | 0 | 116 | 13 | -LOVELY.pdf |
| jp_13_rasputin | 0 | 0 | 1 | Rasputin.pdf |
| jp_14_beginning | 0 | 1 | 30 | its-beginning-to-look-a-lot-li ke (4 manos N |
| jp_15_favourite | 0 | 32 | 14 | my-favourite-things-the-sound-.pdf |
| jp_16_sweetchild | 0 | 0 | 0 | sweet-child-o-mine-guns-n-roses-easy-piano.p |
| jp_17_unbeso | 8 | 38 | 22 | Un beso-y-una-flor-nino-bravo.pdf |
| jp_18_merry | 0 | 9 | 11 | merry-go-round-of-life.pdf |
| jp_19_acomme | 8 | 45 | 5 | A COMME AMOUR _ Richard Clayderman. |
| nl_01_petite | 0 | 1 | 22 | petite chanson.(4 manos) |
| nl_02_counting | 0 | 8 | 0 | Counting-stars-.pdf |
| nl_03_deck | 0 | 0 | 10 | Deck the Halls (NAVIDAD).pdf |
| nl_04_heart | 0 | 1 | 10 | heart-and-soul-.pdf |
| nl_05_hittheroad | 0 | 0 | 0 | hit-the-road-jack-ray-.pdf |
| nl_06_jailhouse | 0 | 2 | 2 | jailhouse-rock-elvis-presley-.pdf |
| nl_07_bellaciao | 0 | 0 | 13 | bella-ciao-piano( 4 manos).pdf |
| nl_08_canthelp | 0 | 0 | 8 | Cant-Falling-in-love-elvis-presley. |
| nl_09_toreador | 0 | 6 | 14 | Copia de Copia de Toreador. Bizet |
| nl_10_lovely | 0 | 116 | 13 | LOVELY. |
| nl_11_rasputin | 0 | 0 | 1 | Rasputin.pdf |
| nl_12_diamonds | 0 | 17 | 27 | rihanna-diamond-.pdf |
| nl_13_favourite | 0 | 32 | 14 | my-favourite-things-the-sound-.pdf |
| nl_14_sweetchild | 0 | 0 | 0 | sweet-child-o-mine-guns-n-roses-easy-piano.p |
| nl_15_merry | 0 | 9 | 11 | Merry-go-round-of-life-easy-piano-excerpt.pd |
| nl_16_acomme | 8 | 45 | 5 | Copia de Copia de  A COMME AMOUR _ Richard C |
| nl_17_dragon | 0 | 321 | 65 | Copia de Copia de Como entrenar a tu dragon. |
| dilan_01_cancion | 0 | 0 | 24 | the-swan.pdf |
| dilan_02_cancion | 0 | 0 | 8 | cant-help-falling-in-love-.pdf |
| dilan_03_your_song | 8 | 70 | 43 | YOUR SONG _ Elton John_.pdf |
| dilan_04_thinking | 0 | 1 | 2 | THINKING OUT LOUD _ Ed Sheeran_.pdf |
| dilan_05_lucia | 8 | 68 | 17 | Lucia_.pdf |
| dilan_06_poema | 0 | 0 | 13 | poema-de-amor-joan-manuel-serrat_.pdf |
| dilan_07_amiga | 0 | 106 | 1 | Amiga mia-alejandro Sanz.pdf |
| dilan_08_promesa | 8 | 177 | 25 | la-promesa-MELENDI.pdf |
| dilan_09_bruno | 8 | 118 | 56 | WHEN I WAS YOUR MAN _ Bruno Mars_.pdf |
| dilan_10_calor | 0 | 14 | 13 | al-calor-del-amor-en-un-bar.pdf |
| dilan_11_soldadito | 0 | 44 | 30 | SOLDADITO DE HIERRO _ Nil Moliner_.pdf |
| dilan_12_sky | 8 | 36 | 58 | a-sky-full-of-stars-coldplay.pdf |
| dilan_13_what | 0 | 52 | 39 | what-was-i-made-for-billie-eilish.pdf |
| dilan_14_writings | 0 | 19 | 10 | WRITING_S ON THE WALL _ Sam Smith_.pdf |
| dilan_15_favourite | 0 | 32 | 14 | my-favourite-things-the-sound-.pdf |
| dilan_16_adagio | 0 | 18 | 5 | Adagio en sol menor. Albinoni.pdf |
| dilan_17_arabesque | 0 | 146 | 6 | arabesque-burgmuller-( 4 manos).pdf |
| dilan_18_merry | 0 | 10 | 9 | have-yourself-a-merry-little-NAVIDAD       A |
| dilan_19_santa | 0 | 22 | 8 | Santa-tell-me-ariana-grande NAVIDAD.pdf |
| dilan_20_beginning | 0 | 1 | 30 | its-beginning-to-look-a-lot-li ke (4 manos |
| eva_01_canthelp | 0 | 0 | 8 | cant-help-falling-in-love-.pdf |
| eva_02_sky | 8 | 36 | 58 | a-sky-full-of-stars-coldplay.pdf |
| eva_03_poema | 0 | 0 | 13 | poema-de-amor-joan-manuel-serrat.pdf |
| eva_04_what | 0 | 52 | 39 | what-was-i-made-for-billie-eilish.pdf |
| eva_05_thinking | 0 | 1 | 2 | THINKING OUT LOUD _ Ed Sheeran .pdf |
| eva_06_cisne | 0 | 0 | 24 | the-swan.pdf |
| eva_07_bruno | 8 | 118 | 56 | WHEN I WAS YOUR MAN _ Bruno Mars.pdf |
| eva_08_promesa | 8 | 177 | 25 | la-promesa-MELENDI.pdf |
| eva_09_amiga | 0 | 106 | 1 | Amiga mia-alejandro Sanz.pdf |
| eva_10_young | 0 | 93 | 90 | WHEN WE WERE YOUNG _ Adele Dm .pdf |
| eva_11_soldadito | 0 | 44 | 30 | SOLDADITO DE HIERRO _ Nil Moliner.pdf |
| eva_12_favourite | 0 | 32 | 14 | my-favourite-things-the-sound-.pdf |
| eva_13_merry | 0 | 10 | 9 | have-yourself-a-merry-little-christmas.pdf |
| eva_14_santa | 0 | 22 | 8 | Santa-tell-me-ariana-grande.pdf |
| eva_15_beginning | 0 | 1 | 30 | its-beginning-to-look-a-lot-like (4 manos).p |
| eva_16_arabesque | 8 | 146 | 6 | arabesque-burgmuller-( 4 manos).pdf |
| eva_17_bohemian | 0 | 24 | 4 | bohemian-rhapsody.pdf |
