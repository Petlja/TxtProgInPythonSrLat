Kretanje crteža
---------------

Animacije koje smo do sada videli rade tako što u svakom frejmu prikazuju neku drugu, unapred pripremljenu sliku. Sada ćemo slike koje prikazujemo i pomerati, tako da se ista slika pojavljuje na različitim mestima u prozoru, to jest kreće se.

Pogledajmo odmah primer:

.. image:: ../../_images/car.png
   :width: 50px

.. activecode:: PyGame__anim_car_oneway
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2b_Anim_Motion/car_rightwards_only.py

Kao i ranije, imamo funkciju *nov_frejm* koja u svakom frejmu prikazuje neku sliku. Ono što je novo u ovom primeru je da se položaj te slike menja iz frejma u frejm. 

Sliku prikazujemo tako da se njen gornji levi ugao pojavi u tački (*auto_x*, *auto_y*). Da bi se auto kretao na desno, u svakom frejmu povećavamo *x* koordinatu slike. Pri tome još samo vodimo računa da kada auto ode suviše desno, da vratimo auto tako da se njegov desni kraj poravna sa levom ivicom prozora. Na taj način auto počinje postepeno da se ponovo pojavljuje sa leve strane.

~~~~

Na sličan način možemo da pomeramo i crteže koje sami nacrtamo (a ne samo gotove slike). Pri tome sliku ili crtež možemo da pomeramo u bilo kom smeru. Evo jednog takvog primera:

.. activecode:: PyGame__anim_billiards
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2b_Anim_Motion/billiards.py

Obratite pažnju na to kako proveravamo da li je bilijarska kugla dotakla neku ivicu ekrana. Krajnja desna tačka kugle ima *x* koordinatu jednaku :math:`cx+r`. Ako bi ta vrednost postala jednaka širini prozora, to bi značilo da kugla dodiruje desnu ivicu prozora, a ako je :math:`cx + r > sirina`, znači da je je kugla bar delom već prošla desnu ivicu prozora. U tom slučaju naredbom  :math:`dx = -dx` postižemo da se od sledećeg frejma *x* koordinati kugle dodaje suprotna vrednost u odnosu na dosadašnju, odnosno da se ubuduće kugla pomera za po 3 piksela na levo. To će izgledati kao da se kugla odbila od desne ivice prozora. 

Primetimo još jedan detalj: umesto :math:`cx + r > sirina` mogli smo da koristimo i :math:`cx + r >= sirina` i program bi radio skoro isto. Međutim, pošto se kugla **ne pomera za po jedan piksel**, ne bi valjalo da smo koristili uslov :math:`cx + r == sirina`, jer bi tada moglo da se dogodi da kugla preskoči položaj koji proveravamo i prođe kroz ivicu prozora.

Detaljno smo analizirali slučaj desne ivice prozora, a isto razmišljanje je pri pisanju programa primenjeno i na ostale ivice. Ukupni efekat dveju *if* naredbi je utisak da se kugla odbija od svake ivice prozora.

Proverite da li ste ovo razumeli tako što ćete odgovoriti na sledeća pitanja.

Kretanje crteža - pitanja
'''''''''''''''''''''''''

.. dragndrop:: pygame__anim_quiz_bounce1
    :feedback: Pokušajte ponovo!
    :match_1: za levu ivicu ||| if cx - r < 0
    :match_2: za desnu ivicu ||| if cx + r > sirina
    :match_3: za gornju ivicu ||| if cy - r < 0
    :match_4: za donju ivicu ||| if cy + r > visina

    Povežite proveru da je kugla iz prethodnog primera prošla određenu ivicu sa odgovarajućom *if* naredbom.

.. mchoice:: pygame__anim_quiz_bounce2
    :answer_a: na desno
    :answer_b: na gore
    :answer_c: na levo
    :answer_d: na dole
    :correct: c
    :feedback_a: Pokušajte ponovo
    :feedback_b: Pokušajte ponovo
    :feedback_c: Tačno
    :feedback_d: Pokušajte ponovo

    Na koju stranu se pomera slika dodavanjem negativne vrednosti na njenu *x* koordinatu?

.. mchoice:: pygame__anim_quiz_bounce3
    :answer_a: if x + sl_sirina < 0:
    :answer_b: if y + sl_visina < 0:
    :answer_c: if x < 0:
    :answer_d: if y < 0:
    :correct: b
    :feedback_a: Pokušajte ponovo
    :feedback_b: Tačno
    :feedback_c: Pokušajte ponovo
    :feedback_d: Pokušajte ponovo

    Neka su dimenzije date slike *sl_sirina* i *sl_visina*, a njen gornji levi ugao (*x*, *y*). Kako proveravamo da li je slika u potpunosti prošla kroz gornju ivicu prozora i više se ne vidi ni jedan njen deo?
    
.. dragndrop:: pygame__anim_quiz_bounce4
    :feedback: Pokušajte ponovo!
    :match_1: slika je izašla kroz levu ivicu prozora ||| x + sl_sirina < 0
    :match_2: slika je počela da izlazi kroz levu ivicu prozora ||| x < 0
    :match_3: slika je izašla kroz desnu ivicu prozora ||| x > sirina
    :match_4: slika je počela da izlazi kroz desnu ivicu prozora ||| x + sl_sirina > sirina

    Neka je sirina širina prozora, sl_sirina širina slike, a (x, y) gornji levi ugao slike. Povežite logičke uslove sa značenjem.

.. mchoice:: pygame__anim_quiz_bounce5
    :answer_a: x = sirina; dx = -10
    :answer_b: x = sirina + sl_sirina; dx = -10
    :answer_c: x = sirina - sl_sirina; dx = -10
    :answer_d: x = sirina + sl_sirina; dx = 10
    :correct: a
    :feedback_a: Tačno
    :feedback_b: Ne, to je predaleko od desne ivice.
    :feedback_c: Ne, tako je cela slika već u prozoru.
    :feedback_d: Ne, slika je predaleko i još će nastaviti da se udaljava.

    Neka je *sirina* širina prozora, *sl_sirina* širina slike, (*x*, *y*) gornji levi ugao slike, a *dx* veličina za koju će se kasnije menjati *x* koordinata slike. Pomoću kojih naredbi će slika početi da se pojavljuje ulazeći u prozor kroz desnu ivicu?

Zadatak - auto koji ide levo - desno
''''''''''''''''''''''''''''''''''''

Pokušajte da prepravite prvi program, tako se auto kreće naizmenično na jednu pa na drugu stranu, kao u primeru (dugme "Pokreni primer"). Program već sadrži naredbe pomoću kojih se formira torka od dve slike. Slika auta koji ide nadesno se učitava, dok se slika auta okrenutog na drugu stranu dobija funkcijom *pg.transform.flip* koja od date slike pravi simetričnu.

.. activecode:: PyGame__anim_car_right_left
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2b_Anim_Motion/car_right_left.py
    
    auto_nadesno_slika = pg.image.load("car.png") 
    auto_nalevo_slika = pg.transform.flip(auto_nadesno_slika, True, False)
    auto_slike = (auto_nadesno_slika, auto_nalevo_slika)
