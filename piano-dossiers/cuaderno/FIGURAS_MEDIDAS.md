# La figura impresa en cada partitura — medida sobre el PDF

Generado por `cuaderno/medir_figuras_todas.py`. Los datos vivos están en
`cuaderno/figuras_medidas.json`, que es lo que lee `auditar_figuras.py`.

**barras dobles** = pares de barras paralelas (semicorcheas) encontrados en el
PDF. **rabitos** = tramos cortos, ruidosos, que no deciden nada.

Esto es lo que faltaba: las transcripciones anotaban edición, tonalidad,
compás, tempo y páginas, pero nunca la figura más corta.

## Lo que este documento NO puede decir

**31 partituras salen como NO MEDIBLE.** No son PDF vectoriales: llevan dentro
una foto, a veces de 50 o 60 ppi, y a esa resolución las dos barras de una
semicorchea no se pueden separar. Hay que mirarlas a ojo.

Costó un error que conviene tener escrito: la primera versión daba **321
semicorcheas en el Flying Theme**, que va entero en corcheas.

## Las partituras que hay que mirar a ojo

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

## La tabla

| pieza | estado | barras dobles | rabitos | escribe | de ellas citadas | partitura |
|---|---|---|---|---|---|---|
| arnau_01_chopsticks | no medible | — | — | 0 | 0 | Chopsticks.pdf |
| arnau_02_clementine | no medible | — | — | 0 | 0 | Clementine.pdf |
| arnau_03_jolly | no medible | — | — | 0 | 0 | JOLLY OLD SAINT NICHOLAS.pdf |
| arnau_04_ears | no medible | — | — | 0 | 0 | Do Your Ears Hang Low?.pdf |
| arnau_05_wheels | no medible | — | — | 0 | 0 | The Wheels on the Bus.pdf |
| arnau_06_saints | no medible | — | — | 0 | 0 | Oh when the Saint.pdf |
| arnau_07_wewish | no medible | — | — | 0 | 0 | WE WISH A MERRY CRISTMAS.pdf |
| arnau_08_baabaa | no medible | — | — | 0 | 0 | Baa Baa Black Sheep.pdf |
| arnau_09_polly | no medible | — | — | 0 | 0 | Polly Put the Kettle On.pdf |
| arnau_10_muffet | no medible | — | — | 0 | 0 | Little Miss Muffet.pdf |
| arnau_11_eso | ok | 0 | 0 | 0 | 0 | Eso-que-tu-me-das. Jarabe de Palo.pdf |
| arnau_12_puff | ok | 0 | 0 | 0 | 0 | puff-the-magic-dragon.pdf |
| arnau_13_pantera | ok | 0 | 0 | 0 | 0 | La Pantera Rosa.pdf |
| arnau_14_bonnie | no medible | — | — | 0 | 0 | MyBonnie.pdf |
| arnau_15_largo | ok | 1 | 0 | 0 | 0 | Largo-Sinfonia 5 Dvorak.pdf |
| arnau_16_aloha | ok | 15 | 24 | 0 | 0 | Aloha oe.sib.pdf |
| arnau_17_popeye | ok | 0 | 1 | 0 | 0 | Popeye el marinerito.pdf |
| arnau_18_submarino | ok | 0 | 0 | 0 | 0 | ElSubmarinoAmarillo-.pdf |
| arnau_19_rain | no medible | — | — | 0 | 0 | rain-rain-away-easy-piano-4 manos.pdf |
| arnau_20_mulberry | no medible | — | — | 0 | 0 | the-mulberry-bush-185807.4 manos.pdf |
| dilan_01_cancion | ok | 0 | 21 | 0 | 0 | the-swan.pdf |
| dilan_02_cancion | ok | 0 | 5 | 0 | 0 |  cant-help-falling-in-love-.pdf |
| dilan_03_your_song | ok | 70 | 41 | 8 | 8 |  YOUR SONG _ Elton John_.pdf |
| dilan_04_thinking | ok | 1 | 2 | 0 | 0 |  THINKING OUT LOUD _ Ed Sheeran_.pdf |
| dilan_05_lucia | ok | 56 | 13 | 8 | 8 |  Lucia_.pdf |
| dilan_06_poema | ok | 0 | 8 | 0 | 0 |  poema-de-amor-joan-manuel-serrat_.pdf |
| dilan_07_amiga | ok | 106 | 1 | 32 | 32 | Amiga mia-alejandro Sanz.pdf |
| dilan_08_promesa | ok | 155 | 9 | 8 | 8 |  la-promesa-MELENDI.pdf |
| dilan_09_bruno | ok | 118 | 56 | 8 | 8 |  WHEN I WAS YOUR MAN _ Bruno Mars_.pdf |
| dilan_10_calor | no medible | — | — | 0 | 0 | al-calor-del-amor-en-un-bar.pdf |
| dilan_11_soldadito | ok | 44 | 28 | 24 | 24 |  SOLDADITO DE HIERRO _ Nil Moliner_.pdf |
| dilan_12_sky | ok | 23 | 54 | 8 | 8 |  a-sky-full-of-stars-coldplay.pdf |
| dilan_13_what | ok | 14 | 11 | 0 | 0 | what-was-i-made-for-billie-eilish.pdf |
| dilan_14_writings | ok | 19 | 10 | 0 | 0 | WRITING_S ON THE WALL _ Sam Smith_.pdf |
| dilan_15_favourite | ok | 6 | 6 | 0 | 0 | my-favourite-things-the-sound-.pdf |
| dilan_16_adagio | ok | 18 | 3 | 0 | 0 | Adagio en sol menor. Albinoni.pdf |
| dilan_17_arabesque | ok | 144 | 4 | 16 | 16 |  arabesque-burgmuller-( 4 manos).pdf |
| dilan_18_merry | ok | 9 | 9 | 0 | 0 | have-yourself-a-merry-little-NAVIDAD       ADhristmas_.pdf |
| dilan_19_santa | ok | 22 | 8 | 16 | 16 | Santa-tell-me-ariana-grande NAVIDAD.pdf |
| dilan_20_beginning | ok | 1 | 14 | 0 | 0 |  its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf |
| ed_01_romance | ok | 6 | 16 | 0 | 0 | Romance-Diabelli 4 manos.pdf |
| ed_02_america | no medible | — | — | 0 | 0 | himno America.pdf |
| ed_03_banner | no medible | — | — | 0 | 0 | Himno de Estados Unidos.pdf |
| ed_04_counting | ok | 8 | 0 | 0 | 0 | Counting-stars.pdf |
| ed_05_peaches | no medible | — | — | 0 | 0 | -PEACHES. |
| ed_06_someone | ok | 0 | 2 | 0 | 0 | SOMEONE YOU LOVED. |
| ed_07_deck | ok | 0 | 4 | 0 | 0 | Deck the Halls (with Boughs of Holly) NAVIDAD.pdf |
| ed_08_jailhouse | ok | 2 | 2 | 0 | 0 | jailhouse-rock-elvis-presley-.pdf |
| ed_09_clock | no medible | — | — | 0 | 0 | Grandfather's Clock.pdf |
| ed_10_shallow | ok | 3 | 68 | 0 | 0 | SHALLOW. |
| ed_11_canthelp | ok | 0 | 5 | 0 | 0 | cant-help-falling-in-love-elvis-presley. |
| ed_12_carol | ok | 4 | 17 | 0 | 0 | carol-of-the-bells   NAVIDAD. |
| ed_13_adagio | ok | 0 | 0 | 0 | 0 | ADAGIO. |
| ed_14_rasputin | ok | 0 | 1 | 0 | 0 | Rasputin.pdf |
| ed_15_toreador | no medible | — | — | 0 | 0 | Toreador. Bizet |
| ed_16_trouble | ok | 0 | 2 | 0 | 0 | Trouble. |
| ed_17_acomme | ok | 45 | 5 | 8 | 8 | A COMME AMOUR _ Richard Clayderman. |
| ed_18_interstellar | ok | 8 | 0 | 0 | 0 | Interstellar _ .pdf |
| ed_19_flying | no medible | — | — | 0 | 0 | Como entrenar a tu dragon. |
| eva_01_canthelp | ok | 0 | 5 | 0 | 0 | cant-help-falling-in-love-.pdf |
| eva_02_sky | ok | 23 | 54 | 12 | 8 | a-sky-full-of-stars-coldplay.pdf |
| eva_03_poema | ok | 0 | 8 | 0 | 0 | poema-de-amor-joan-manuel-serrat.pdf |
| eva_04_what | ok | 14 | 11 | 0 | 0 | what-was-i-made-for-billie-eilish.pdf |
| eva_05_thinking | ok | 1 | 2 | 0 | 0 | THINKING OUT LOUD _ Ed Sheeran .pdf |
| eva_06_cisne | ok | 0 | 21 | 0 | 0 | the-swan.pdf |
| eva_07_bruno | ok | 118 | 56 | 8 | 8 | WHEN I WAS YOUR MAN _ Bruno Mars.pdf |
| eva_08_promesa | ok | 155 | 9 | 8 | 8 | la-promesa-MELENDI.pdf |
| eva_09_amiga | ok | 106 | 1 | 16 | 16 | Amiga mia-alejandro Sanz.pdf |
| eva_10_young | ok | 93 | 88 | 20 | 4 | WHEN WE WERE YOUNG _ Adele Dm .pdf |
| eva_11_soldadito | ok | 44 | 28 | 0 | 0 | SOLDADITO DE HIERRO _ Nil Moliner.pdf |
| eva_12_favourite | ok | 6 | 6 | 0 | 0 | my-favourite-things-the-sound-.pdf |
| eva_13_merry | ok | 9 | 9 | 0 | 0 | have-yourself-a-merry-little-christmas.pdf |
| eva_14_santa | ok | 22 | 8 | 16 | 16 | Santa-tell-me-ariana-grande.pdf |
| eva_15_beginning | ok | 1 | 14 | 0 | 0 | its-beginning-to-look-a-lot-like (4 manos).pdf |
| eva_16_arabesque | ok | 144 | 4 | 8 | 8 | arabesque-burgmuller-( 4 manos).pdf |
| eva_17_bohemian | ok | 24 | 2 | 2 | 2 | bohemian-rhapsody.pdf |
| is_01_petite | ok | 1 | 21 | 0 | 0 | petite chanson(4 manos).pdf |
| is_02_saints | no medible | — | — | 0 | 0 | OH WHEN THE SAINT.pdf |
| is_03_puff | ok | 0 | 0 | 0 | 0 | Puff era un Drac Magic.pdf |
| is_04_beginner | ok | 0 | 3 | 0 | 0 | The Beginer le Debut(4 manos).pdf |
| is_05_wewishyou | ok | 0 | 6 | 0 | 0 | WE WISH YOU A MERRY CHRISTMAS.pdf |
| is_06_christmas | ok | 0 | 9 | 0 | 0 | christmas-songs-( 4 manos).pdf |
| is_07_silentnight | ok | 0 | 1 | 0 | 0 | SILENT NINGT.pdf |
| is_08_silentnight4h | ok | 0 | 2 | 3 | 0 | silent-night-(4 manos).pdf |
| is_09_panthere | ok | 0 | 0 | 0 | 0 | La Pantera Rosa.pdf |
| is_10_pianoman | ok | 0 | 5 | 0 | 0 | Piano Men.pdf |
| is_11_greensleeves | ok | 4 | 0 | 0 | 0 | -Greensleeves. |
| is_12_grandfather | no medible | — | — | 0 | 0 | Grandfather.pdf |
| is_13_doremi | ok | 0 | 1 | 4 | 0 | Sonrisas y Lagrimas.pdf |
| is_14_dream | ok | 1 | 7 | 4 | 0 | i-have-a-dream-abba-.pdf |
| is_15_gladiator | ok | 0 | 9 | 0 | 0 | Gladyator.pdf |
| is_16_rasputin | ok | 0 | 1 | 4 | 0 | Rasputin.pdf |
| is_17_jailhouse | ok | 2 | 2 | 0 | 0 | Jailhouse Elvis Presley.pdf |
| is_18_toreador | no medible | — | — | 4 | 0 | TOREADOR-BIZET.pdf |
| is_19_furelise | ok | 1 | 3 | 1 | 1 | Para Elisa.pdf |
| is_20_diabelli | ok | 19 | 14 | 0 | 0 | DIABELLI ( cuatro manos).pdf |
| jm_01_romance | ok | 6 | 16 | 0 | 0 | Romance-Diabelli 4 manos.pdf |
| jm_02_america | no medible | — | — | 0 | 0 | himno America.pdf |
| jm_03_banner | no medible | — | — | 0 | 0 | Himno de Estados Unidos.pdf |
| jm_04_counting | ok | 8 | 0 | 0 | 0 | Counting-stars.pdf |
| jm_05_peaches | no medible | — | — | 0 | 0 | -PEACHES. |
| jm_06_someone | ok | 0 | 2 | 0 | 0 | SOMEONE YOU LOVED. |
| jm_07_deck | ok | 0 | 4 | 0 | 0 | Deck the Halls (with Boughs of Holly) NAVIDAD.pdf |
| jm_08_jailhouse | ok | 2 | 2 | 0 | 0 | jailhouse-rock-elvis-presley-.pdf |
| jm_09_clock | no medible | — | — | 0 | 0 | Grandfather's Clock.pdf |
| jm_10_shallow | ok | 3 | 68 | 0 | 0 | SHALLOW. |
| jm_11_canthelp | ok | 0 | 5 | 0 | 0 | cant-help-falling-in-love-elvis-presley. |
| jm_12_carol | ok | 4 | 17 | 0 | 0 | carol-of-the-bells   NAVIDAD. |
| jm_13_adagio | ok | 0 | 0 | 0 | 0 | ADAGIO. |
| jm_14_rasputin | ok | 0 | 1 | 0 | 0 | Rasputin.pdf |
| jm_15_toreador | no medible | — | — | 0 | 0 | Toreador. Bizet |
| jm_16_trouble | ok | 0 | 2 | 0 | 0 | Trouble. |
| jm_17_acomme | ok | 45 | 5 | 8 | 8 | A COMME AMOUR _ Richard Clayderman. |
| jm_18_interstellar | ok | 8 | 0 | 0 | 0 | Interstellar _ .pdf |
| jm_19_flying | no medible | — | — | 0 | 0 | Como entrenar a tu dragon. |
| jp_01_romance | ok | 6 | 16 | 0 | 0 | Romance-Diabelli 4 manos.pdf |
| jp_02_petite | ok | 1 | 21 | 0 | 0 | Petite chanson.(4 MANOS) |
| jp_03_peaches | no medible | — | — | 8 | 8 | -PEACHES. |
| jp_04_counting | ok | 8 | 0 | 0 | 0 | Counting-stars.pdf |
| jp_05_what | ok | 14 | 11 | 0 | 0 | what-was-i-made-for-billie-eilish.pdf |
| jp_06_heart | ok | 0 | 5 | 0 | 0 | heart-and-soul-.pdf |
| jp_07_hittheroad | ok | 0 | 0 | 0 | 0 | hit-the-road-jack-ray-.pdf |
| jp_08_deck | ok | 0 | 4 | 4 | 0 | Deck the Halls  NAVIDAD.pdf |
| jp_09_jailhouse | ok | 2 | 2 | 0 | 0 | jailhouse-rock-elvis-presley-.pdf |
| jp_10_bellaciao | ok | 0 | 11 | 0 | 0 | bella-ciao-piano-(4 MANOS).pdf |
| jp_11_canthelp | ok | 0 | 5 | 0 | 0 | cant-help-falling-in-love-elvis-presley. |
| jp_12_lovely | no medible | — | — | 0 | 0 | -LOVELY.pdf |
| jp_13_rasputin | ok | 0 | 1 | 0 | 0 | Rasputin.pdf |
| jp_14_beginning | ok | 1 | 14 | 0 | 0 | its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf |
| jp_15_favourite | ok | 6 | 6 | 0 | 0 | my-favourite-things-the-sound-.pdf |
| jp_16_sweetchild | ok | 0 | 0 | 0 | 0 | sweet-child-o-mine-guns-n-roses-easy-piano.pdf |
| jp_17_unbeso | ok | 38 | 17 | 8 | 8 | Un beso-y-una-flor-nino-bravo.pdf |
| jp_18_merry | ok | 9 | 9 | 0 | 0 | merry-go-round-of-life.pdf |
| jp_19_acomme | ok | 45 | 5 | 8 | 8 | A COMME AMOUR _ Richard Clayderman. |
| lu_01_bambini | ok | 3 | 0 | 0 | 0 | bazzoni-maurizio-sonatina-per-bambini-(4 manos).pdf |
| lu_02_beginner | ok | 0 | 3 | 0 | 0 | The Beginner Le Debut.pdf |
| lu_03_sonatina2 | ok | 5 | 0 | 0 | 0 | _bazzoni-maurizio-sonatina-sol-maggiore (4 manos).pdf |
| lu_04_friend | ok | 0 | 0 | 0 | 0 | youve-got-a-friend-in-me-easy-piano-.pdf |
| lu_05_puff | ok | 0 | 0 | 0 | 0 | puff-the-magic-dragon. |
| lu_06_dream | ok | 1 | 7 | 0 | 0 | i-have-a-dream-abba-children-song.pdf |
| lu_07_christmas | ok | 0 | 9 | 0 | 0 | christmas-songs-(4 manos).pdf |
| lu_08_silent | ok | 0 | 1 | 0 | 0 | Silent-Night.easy |
| lu_09_spring | ok | 0 | 2 | 0 | 0 | LA PRIMAVERA.pdf easy |
| lu_10_titanic | ok | 6 | 3 | 0 | 0 | Titanic easy.pdf |
| lu_11_pianoman | ok | 0 | 5 | 0 | 0 | piano-man-easy. |
| lu_12_panthere | ok | 0 | 0 | 0 | 0 | la-panthere-rose-easy.pdf |
| lu_13_belaciao | ok | 0 | 0 | 0 | 0 | bela-ciao.easy |
| lu_14_heart | ok | 0 | 5 | 0 | 0 | heart-and-soul-hoagy-carmIchael easy.pdf |
| lu_15_greensleeves | ok | 4 | 0 | 0 | 0 | Copia de 1-----Greensleeves.pdf |
| lu_16_chimchim | ok | 0 | 3 | 0 | 0 | Mary Popins FACIL.pdf |
| lu_17_rasputin | ok | 0 | 1 | 0 | 0 | rasputin easy.pdf |
| lu_18_furelise | ok | 0 | 0 | 0 | 0 | Para  Elisa easy.pdf |
| lu_19_nocturne | ok | 0 | 7 | 0 | 0 | nocturne-op9-chopin. easy |
| me_01_bambini | ok | 3 | 0 | 0 | 0 | Maurizio Bazzoni sonatina para 4 manos.pdf |
| me_02_saints | no medible | — | — | 0 | 0 | OH WHEN THE SAINT.pdf |
| me_03_friend | ok | 0 | 0 | 0 | 0 | Hay un amigo en mi.pdf |
| me_04_puff | ok | 0 | 0 | 0 | 0 | Puff era un Drac Magic.pdf |
| me_05_sonatina2 | ok | 5 | 0 | 0 | 0 | bazzoni-maurizio-sonatia-sol-maggiore-174724. |
| me_06_avignon | no medible | — | — | 0 | 0 | SUR LE PONT D'AVIGNON.pdf |
| me_07_doremi | ok | 0 | 1 | 0 | 0 | Sonrisas y Lagrimas.pdf |
| me_08_christmas | ok | 0 | 9 | 0 | 0 | christmas-songs-for-four-little- 4 manos.pdf |
| me_09_silentnight | ok | 0 | 1 | 0 | 0 | SILENT NINGT.easy |
| me_10_wewishyou | ok | 0 | 6 | 0 | 0 | WE WISH YOU A MERRY CHRISTMAS.pdf |
| me_11_silentnight4h | ok | 0 | 2 | 0 | 0 | silent-night-4-hands. |
| me_12_panthere | ok | 0 | 0 | 0 | 0 | La Pantera Rosa.pdf |
| me_13_pianoman | ok | 0 | 5 | 0 | 0 | Piano Men.pdf |
| me_14_belaciao | ok | 0 | 0 | 0 | 0 | bela-ciao.pdf |
| me_15_spring | no medible | — | — | 0 | 0 | LAS CUATRO ESTACIONES.pdf |
| me_16_greensleeves | ok | 4 | 0 | 0 | 0 | -Greensleeves.pdf |
| me_17_countingstars | ok | 8 | 0 | 0 | 0 | counting-stars-.pdf |
| me_18_largodvorak | ok | 1 | 0 | 0 | 0 | -Largo-Sinfonia 5 Dvorak.pdf |
| me_19_grandfather | no medible | — | — | 0 | 0 | Grandfather.pdf |
| me_20_dream | ok | 1 | 7 | 0 | 0 | i-have-a-dream-abba-.pdf |
| me_21_beauty | no medible | — | — | 0 | 0 | BELLA Y BESTIA .pdf |
| me_22_gladiator | ok | 0 | 9 | 0 | 0 | Gladyator.pdf |
| me_23_rasputin | ok | 0 | 1 | 0 | 0 | Rasputin.pdf |
| me_24_jailhouse | ok | 2 | 2 | 0 | 0 | Jailhouse Elvis Presley.pdf |
| me_25_toreador | no medible | — | — | 0 | 0 | TOREADOR-BIZET. Bizet |
| me_26_furelise | ok | 1 | 3 | 1 | 1 | Para Elisa.pdf |
| me_27_nocturne | ok | 0 | 7 | 0 | 0 | nocturne-op9-chopin. |
| nl_01_petite | ok | 1 | 21 | 0 | 0 | petite chanson.(4 manos) |
| nl_02_counting | ok | 8 | 0 | 0 | 0 | Counting-stars-.pdf |
| nl_03_deck | ok | 0 | 4 | 0 | 0 | Deck the Halls (NAVIDAD).pdf |
| nl_04_heart | ok | 0 | 5 | 0 | 0 | heart-and-soul-.pdf |
| nl_05_hittheroad | ok | 0 | 0 | 0 | 0 | hit-the-road-jack-ray-.pdf |
| nl_06_jailhouse | ok | 2 | 2 | 0 | 0 | jailhouse-rock-elvis-presley-.pdf |
| nl_07_bellaciao | ok | 0 | 11 | 0 | 0 | bella-ciao-piano( 4 manos).pdf |
| nl_08_canthelp | ok | 0 | 5 | 0 | 0 | Cant-Falling-in-love-elvis-presley. |
| nl_09_toreador | no medible | — | — | 4 | 0 | Copia de Copia de Toreador. Bizet |
| nl_10_lovely | no medible | — | — | 0 | 0 | LOVELY. |
| nl_11_rasputin | ok | 0 | 1 | 0 | 0 | Rasputin.pdf |
| nl_12_diamonds | ok | 17 | 19 | 0 | 0 | rihanna-diamond-.pdf |
| nl_13_favourite | ok | 6 | 6 | 0 | 0 | my-favourite-things-the-sound-.pdf |
| nl_14_sweetchild | ok | 0 | 0 | 0 | 0 | sweet-child-o-mine-guns-n-roses-easy-piano.pdf |
| nl_15_merry | ok | 9 | 9 | 0 | 0 | Merry-go-round-of-life-easy-piano-excerpt.pdf |
| nl_16_acomme | ok | 45 | 5 | 8 | 8 | Copia de Copia de  A COMME AMOUR _ Richard Clayderman. |
| nl_17_dragon | no medible | — | — | 0 | 0 | Copia de Copia de Como entrenar a tu dragon. |
