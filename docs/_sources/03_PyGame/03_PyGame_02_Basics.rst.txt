Pisanje PyGame programa
=======================

Osnovna struktura PyGame programa
---------------------------------

Da bi programi koje pišemo mogli da koriste biblioteku (modul) PyGame, prva stvar koju treba da uradimo je da na početku programa priključimo našem programu modul PyGame. Time omogućavamo upotrebu svih funkcija i konstanti koje su definisane u modulu PyGame.

Svaki program koji koristi biblioteku PajGejm (PyGame), po priključivanju modula a pre pozivanja drugih gunkcija treba da izvrši nekoliko koraka da bi inicijalizovao biblioteku, zadao dimenzije prozora u kome će program da crta i postavio naslov tog prozora. Isto tako, na kraju programa ima nekoliko koraka koji govore programu da treba da čeka dok korisnik ne klikne na dugme za zatvaranje prozora, a zatim da zatvori prozor i isključi biblioteku PyGame.

Ti koraci na početku i na kraju rada su u svakom programu isti ili vrlo slični. Da bi korišćenje PyGame biblioteke bilo što jednostavnije za početnike, koristićemo i malu dodatnu biblioteku po imenu *PyGameBg*. Zahvaljujući ovoj biblioteci, umesto navođenja svih neophodnih koraka dovoljno je da i modul *pygamebg* priključimo našem programu, a zatim pozovemo samo po jednu funkciju iz modula *pygamebg* na početku i na kraju programa. Time programi postaju kraći i jednostavniji, što nam omogućava da se usredsredimo na deo programa koji je specifičan za dati zadatak. 

Programe koji koriste biblioteku *PyGameBg* možete da pokrenete i u svom lokalnom razvojnom okruženju (npr. *IDLE*). Potrebno je samo da pre toga instalirate i biblioteku *PyGameBg* na isti način kao što ste instalirali biblioteku *pygamebg*, kucanjem ``pip3 install pygamebg`` u komandnoj liniji. Kada instalirate i ovu biblioteku, možete da kopirate izabrani program u vaš editor i sačuvate ga na vašem računaru. Posle toga program možete da dorađujete i menjate po volji, da čuvate različite verzije programa i da ih isprobavate pokretanjem programa.

Evo kako izgleda jedan PajGejm program, koji crta jednu kosu duž i čeka da korisnik zatvori prozor. 

.. activecode:: pygame__basics_first_example
    :nocodelens:
    :modaloutput: 

    import pygame as pg
    import pygamebg
    prozor = pygamebg.open_window(400, 400, "Pygame")

    prozor.fill(pg.Color("white"))
    pg.draw.line(prozor, pg.Color("black"), (100, 100), (300, 300), 5)

    pygamebg.wait_loop()

Prođimo redom kroz naredbe ovog programa da bismo detaljnije objasnili čemu one služe. 

Najpre imamo grupu naredbi kakve će morati da se pojave na početku svakog programa:

- naredbom ``import pygame as pg`` priključujemo modul *pygame* našem programu. Ovde koristimo malo drugačiji oblik naredbe *import* od onog koji smo koristili ranije. Ovde ujedno modulu *pygame* dajemo skraćeno ime *pg* i to skraćeno ime onda koristimo nadalje u programu kao ime modula. Mogli smo ravnopravno da pišemo i samo ``import pygame`` i tada bi u nastavku programa umesto *pg.Color*, *pg.draw.line* i slično, trebalo da stoji *pygame.Color*, *pygame.draw.line* itd.
- naredbom ``import pygamebg`` priključujemo modul *pygamebg* našem programu. Ova naredba se zajedno sa prethodnom može spojiti u jednu: ``import pygame as pg, pygamebg``, a to ćemo često i činiti.
- Naredba ``prozor = pygamebg.open_window(400, 400, "Pygame")`` poziva fukciju ``open_window`` iz modula ``pygamebg``, koji smo dodali programu. U ovoj funkciji se obavljaju sve portebne pripremne radnje koje smo ranije pominjali. Parametri funkcije su širina, visina i naslov prozora koji se pozivom ove funkcije otvara. Promenljivu *prozor* koju ova funkcija vraća, kasnije koristimo u programu da bismo u tom prozoru crtali.

Sledi grupa naredbi koja je u svakom programu drugačija i određuje šta konkretan program zapravo radi. Naš prvi program crta crnu liniju na beloj pozadini, a to je postignuto pomoću ovog dela programa:

- naredba ``prozor.fill(pg.Color("white"))`` boji prozor u belo. Ovakvom naredbom se često započinje crtanje (boja može da bude i drugačija)
- naredba ``pg.draw.line(prozor, pg.Color("black"), (100, 100), (300, 300), 5)`` crta liniju.

Ovakve naredbe će uskoro biti detaljno objašnjene, ali ako ste nestrpljivi, možete da probate da u programu izmenite vrednosti parametara ili dodate nove, slične naredbe i sami otkrijete kako ove funkcije za crtanje rade.

Na kraju programa imamo poziv još jedne funkcije iz modula *pygamebg*: ``pygamebg.wait_loop()``. U ovoj funkciji se nalaze naredbe koje omogućavaju da se crtež pojavi na prozoru i da prozor ostane otvoren dok korisnik ne klikne na dugme za zatvaranje. Funkcija nakon zatvaranja prozora deaktivira sve pokrenute delove biblioteke PajGejm (isključuje ih). 

Svi naši PajGejm programi će se završavati pozivom funkcije ``pygamebg.wait_loop()`` ili neke slične funkcije. Posle izvršenja ove funkcije program može da nastavi da radi bez biblioteke *PyGame* u tekstualnom prozoru ako za time ima potrebe.


Koordinatni sistem
------------------

Koordinate su nam veoma važan pojam i sa njima ćemo se susretati u baš svakom PajGejm programu. Položaj svih objekata (tačaka, duži, krugova, teksta, gotovih slika itd.) na prozoru određuje se njihovim koordinatama u koordinatom sistemu prozora. 

Koordinatni sistem prozora je sličan, ali ipak malo drugačiji od onog koji se koristi u matematici. Položaj tačke je i u ovom slučaju određen uređenim parom njenih koordinata (koordinatom x tj. apscisom i koordinatom y tj. ordinatom). Jedinica mere je jedan piksel. 

U računarskoj grafici, koordinatni početak je u gornjem levom uglu prozora. Koordinata :math:`x` raste kada se krećemo na desno (kao i u matematici), ali koordinata :math:`y` opada kada se krećemo na gore, odnosno povećava se kada se krećemo na dole, što je drugačije od uobičajenog koordinatnog sistema iz matematike. Neka je data tačka :math:`A(5, 3)`. Ako bismo pomerili ovu tačku za 1 na gore i zadržali njenu :math:`x` koordinatu, tada bi nove koordinate tačke :math:`A` bile :math:`A(5, 2)`. Ako bismo tačku :math:`A` sa trenutne pozicije pomerili na dole za 2, nove koordinate bi joj bile :math:`A(5, 4)`. Dakle, **prva koordinata tačke određuje koliko je tačka udaljena od leve ivice prozora**, a **druga koordinata koliko je tačka udaljena od gornje ivice prozora**.


.. image:: ../../_images/PyGame/coordinate_system.png
   :width: 400px   
   :align: center 
      
U programskom jeziku Pajton par koordinata tačke možemo predstaviti bilo dvočlanom torkom ``(3, 5)`` bilo dvočlanom listom ``[3, 5]``.  U prethodnom primeru dve krajnje tačke duži bile su zadate pomoću dve dvočlane torke (``(100, 100)`` i ``(300, 300)``).

.. activecode:: pygame__basics_coordinates
   :passivecode: true
   
   pg.draw.line(prozor, pg.Color("black"), (100, 100), (300, 300), 5)

Često je potrebno zadati i pravougaonik, čije su stranice paralelne koordinatnim osama. Takav pravougaonik se zadaje pomoću torke ili liste od četiri broja: :code:`(x, y, w, h)` ili :code:`[x, y, w, h]`. Pri tome :math:`x` i :math:`y` predstavljaju koordinate gornjeg levog temena pravougaonika, a :math:`w` i :math:`h` predstavljaju redom širinu i visinu tog pravougaonika u pikselima. Tako na primer, pravougaonik na sledećoj slici bi mogao da se zada kao :code:`pygame.Rect(2, 1, 4, 3)`, ili prosto kao :code:`(2, 1, 4, 3)` ili :code:`[2, 1, 4, 3]`.

.. image:: ../../_images/PyGame/rect_coordinates.png
   :width: 400px   
   :align: center 

Naredni program može da vam pomogne da shvatite koordinate. Pokrenite program klikom na dugme "Prikaži primer", a zatim pomerajte miša i pratite kako se koordinate menjaju. Prozor po kom se miš kreće je veliičine 300 puta 300 piskela. Vrednosti koordinata *x* i *y* se pojavljuju i u naslovu prozora i pored pokazivača miša. Zapis pored miša u obliku uređenog para, kao što će biti i u programima kada zadajemo jednu tačku.

.. activecode:: pygame__basics_learn_coordinates
   :nocodelens:
   :modaloutput:
   :playtask:
   :includehsrc: src/PyGame/1_Drawing/1_BasicExamples/learn_coordinates.py

Proverite svoje znanje o koordinatama kroz narednih nekoliko pitanja.
                 
.. image:: ../../_images/PyGame/pygame_quiz_coordinates.png
    :width: 300px
    :align: center
   
.. dragndrop:: pygame__basics_quiz_coordinates_circles
    :feedback: Pokušajte ponovo!
    :match_1: crvena|||(30, 40)
    :match_2: zelena|||(50, 280)
    :match_3: plava|||(230, 20)
    :match_4: crna|||(150, 170)

    Povežite boju kružića sa koordinatama njegovog centra (dimenzije prozora su 300 puta 300 piksela).

.. fillintheblank:: pygame__basics_quiz_coordinates_vindow_center

    Ako je prozor širine 200 i visine 300 piksela, koje su koordinate njegove centralne tačke (rezultat napišite u obliku uređenog para)?

    - :\(100,[ ]*150\): Tačno!
      :\(100,[ ]*[0-9]+\): Pažljivije izračunaj koordinatu y.
      :\([0-9]+,[ ]*150\): Pažljivije izračunaj koordinatu x.
      :\([0-9]+,[ ]*[0-9]+\): Pažljivije izračunaj obe koordinate.
      :.*: Rezultat zapiši u obliku uređenog para.
   
.. mchoice:: pygame__basics_quiz_coordinates_dir
   :multiple_answers:
   :answer_a: Koordinata x raste sleva nadesno.
   :answer_b: Koordinata y opada od vrha ka dnu ekrana.
   :answer_c: Tačke na gornjoj ivici ekrana imaju koordinatu y jednaku 0.
   :answer_d: Tačke na desnoj ivici ekrana imaju koordinatu x jednaku 0.
   :answer_e: Tačka u donjem desnom uglu ekrana ima najveće obe koordinate. 
   :correct: a, c, e
   :feedback_a: Tačno.
   :feedback_b: Koordinata y raste od vrha ka dnu ekrana.
   :feedback_c: Tačno.
   :feedback_d: Tačke na desnoj ivici ekrana imaju najveću x koordinatu.
   :feedback_e: Tačno.

   Označite tačna tvrđenja.
   
.. dragndrop:: pygame__basics_quiz_coordinates_corners
    :feedback: Pokušajte ponovo!
    :match_1: gornje-levo|||(0, 0)
    :match_2: gornje-desno|||(s, 0)
    :match_3: donje-levo|||(0, v)
    :match_4: donje-desno|||(s, v)

    Ako je širina prozora `s`, a visina `v`, upari temena ekrana sa njihovim koordinatama.


Zadavanje boja
--------------

Pri crtanju se, naravno, mogu koristiti različite boje. Boju možemo zadati njenim imenom (na engleskom), koje se navodi kao parametar funkcije ``pg.Color``. Možete da koristite boje navođenjem odgovarajuće niske (stringa): ``'black'`` za crnu, ``'white'`` za belu, ``'gray'`` za sivu, ``'blue'`` za plavu, ``'green'`` za zelenu, ``'orange'`` za narandžastu, ``'yellow'`` za žutu i slično. Podsetimo se, niske se navode bilo između jednostrukih, bilo između dvostrukih navodnika (ravnopravno se, na primer, mogu koristiti``\'blue\'`` i ``"blue"``). Na primer, ako pozovete funkciju ``py.draw.line(prozor, pg.Color('blue'), (0, 0), (200, 200), 3)`` na prozoru će se prikazati duž debljine 3 piksela, plave boje, čija su temena tačke sa koordinatama :math:`(0, 0)` i :math:`(200, 200)`.

Neka od imena boja, koja se često koriste u programima su:

========================   ============
``pg.Color("black")``      Crna
``pg.Color("white")``      Bela
``pg.Color("red")``        Crvena
``pg.Color("green")``      Zelena
``pg.Color("blue")``       Plava
``pg.Color("cyan")``       Rezeda
``pg.Color("magenta")``    Ljubičasta
``pg.Color("yellow")``     Žuta
``pg.Color("orange")``     Narandžasta
========================   ============

Poigrajte se malo sa bojama u narednom programu i pokušajte da obojite prozor u neke ili sve od ovih boja.

.. activecode:: pygame__basics_colors
   :nocodelens:
   :enablecopy:
   :modaloutput:

   # -*- acsection: general-init -*-
   import pygame as pg, pygamebg

   # uključivanje rada biblioteke PyGame
   prozor = pygamebg.open_window(400, 400, "Boje - nazivi")
   # -*- acsection: main -*-

   # bojimo pozadinu prozora
   prozor.fill(pg.Color("???"))
   
    # -*- acsection: after-main -*-
    # zavrsavamo rad biblioteke PyGame
    pygamebg.wait_loop()
         
.. infonote::

    Jedna od grešaka koja se često dešava pri pisanju prvih PajGejm programa je da prilikom zadavanja boje napišete ``pg.color`` malim slovom, umesto velikim - ``pg.Color``. To pruzrokuje grešku sa porukom ``AttributeError: '' object has no attribute 'color'``. 
    
    Još jedna česta greška je da naziv boje ne navedete pod navodnicima (na primer, da navedete ``pg.Color(white)``). Tada uz grešku pojavljuje poruka ``NameError: name 'white' is not defined on line 8``.
  
Pored ovih boja, postoje i mnoge druge koje možete da koristie. Ukupan broj svih nijansi koje postoje u računarima je ogroman i iznosi oko 16 miliona. Od toga, pomoću imena možemo da zadamo nešto više od 600 različitih boja (kompletan spisak se nalazi u fajlu *colordict.py*, koji lako možete da nađete na internetu, a ako ste instalirali PajGejm, imate ga i na svom računaru).

Sve ove imenovane boje, a i sve ostale koje nemaju imena, možemo da zadamo pomoću brojeva. Za to se najviše koristi takozvani *RGB* model boja.  Naime, u računarskoj grafici svaka boja se dobija mešanjem određene količine crvene, zelene i plave, po čijim imenima na engleskom (*Red*, *Green*, *Blue*) je *RGB* model i dobio ime. Na primer, kombinovanjem crvenog i zelenog svetla dobija se žuto svetlo, kombinovanjem crvenog i plavog ljubičasto, a kombinovanjem plavog i zelenog rezeda. Kombinovanjem svetla sve tri osnovne boje dobija se belo svetlo dok se crno svetlo dobija kada se sva tri svetla isključe. Sivo svetlo se dobija kada se izmeša podjednaka količina, crvenog, zelenog i plavog svetla.

.. image:: ../../_images/PyGame/RGB.png
   :align: center
   :width: 200px

Boju tako možemo opisati navodeći tri broja (u ovom slučaju to su brojevi od 0 do 255), koji redom predstavljaju količinu crvene, zelene i plave komponente u boji koju definišemo. U programskom jeziku Pajton boju možemo da predstavimo i u obliku tročlane uređene torke (na pr. ``(123, 80, 56)``) ili tročlane liste (na pr. ``[123, 80, 56]``). Torku ili listu možete navesti direktno kao argument funkcije koji odgovara boji, a možete je upamtiti u promenljivoj i kasnije koristiti ime promenljive. Na primer, dodelom ``REZEDA = (0, 255, 255)`` definišemo rezeda boju navodeći odgovarajuće količine crvene, zelene i plave svetlosti koju ova boja sadrži (pošto je to mešavina plave i zelene boje u njoj nema nimalo crvene, a plava i zelena komponenta su na maksimumu). Nakon toga, tu boju možemo upotrebiti i u pozivu funkcije (na pr. ``prozor.fill(REZEDA)``). Imena tih promenljivih ne moraju biti napisana velikim slovima, ali to je postalo uobičajeno u pisanju Pajton programa. U programima koje budete čitali u nastavku, susretaćete se sa definicijama ovog oblika. 

Boju je moguće zadati i sa četiri broja, na primer ``REZEDA = (0, 255, 255, 10)``. Poslednji, četvrti parametar (takođe od 0 do 255) određuje prozirnost boje, tj. ovako zadata rezeda boja je blago providna.

Rezimirajmo sada RGB vrednosti nekih karakterističnih boja.

===================        ========= 
``(255, 0, 0)``            crvena
``(0, 255, 0)``            zelena
``(0, 0, 255)``            plava
``(255, 255, 0)``          žuta
``(0, 255, 255)``          rezeda
``(255, 0, 255)``          ljubičasta
``(255, 255, 255)``        bela
``(0, 0, 0)``              crna
``(128, 128, 128)``        siva
``(255, 128, 0)``          narandžasta
``(255, 128, 128)``        roze
===================        ========= 

Primetimo da su nijanse sive boje prepoznatljive po tome što su u njima količina crvene, zelene i plave jednake. Što je ta količina manja, nijansa sive je tamnija i obrnuto, veće jednake količine crvene, zelene i plave predstavljju svetlije nijanse sive (na osnovu *RGB* vrednosti, crnu i belu možemo da posmatramo kao najtamniju i najsvetliju nijansu sive).

U narednom programu možete da isprobate i zapise boja u RGB obliku. Pored bojenja prozora u neke ili sve od nabrojanih boja, možete da unesete i druge (bilo koje) trojke vrednosti između 0 i 255. 

.. infonote:: 

    Kada budete birali boje koje želite da koristite u svojim programima, može da vam pomogne alatka za biranje boja. Takvih alatki ima i na mnogim sajtovima (tražite *color picker*), a možete da koristite i onu iz programa *Paint*. Možete da isprobate već sada - izaberite boju i prepišite vrednosti *R*, *G*, *B* u program.

.. activecode:: pygame__basics_colors_rgb
   :nocodelens:
   :enablecopy:
   :modaloutput:

   # -*- acsection: general-init -*-
   import pygame as pg

   # uključivanje rada biblioteke PyGame
   pg.init()

   # postavljamo naslov prozora
   pg.display.set_caption("Boje - RGB")
   # određujemo dimenzije prozora
   (sirina, visina) = (400, 400)
   # prikazujemo prozor tih dimenzija
   prozor = pg.display.set_mode((sirina, visina))
   # -*- acsection: main -*-

   # bojimo pozadinu prozora
   prozor.fill([???, ???, ???])
   
   # -*- acsection: after-main -*-
   # osvežavamo sadržaj prozora i tako prikazujemo ono što smo nacrtali
   pg.display.update()

   # petlja obrade događaja - čekamo dok korisnik ne isključi prozor
   while pg.event.wait().type != pg.QUIT:
       pass

   # isključivanje rada biblioteke PyGame
   pg.quit()

Utvrdite svoje znanje o bojama tako što ćete odgovoriti na narednih nekoliko pitanja.

.. dragndrop:: pygame__basics_quiz_color_names
    :feedback: Pokušajte ponovo!
    :match_1: Crna|||pg.Color("black")
    :match_2: Plava|||pg.Color("blue")
    :match_3: Crvena|||pg.Color("red")
    :match_4: Zelena|||pg.Color("green")

    uparite boje.

.. dragndrop:: pygame__basics_quiz_color_values
    :feedback: Pokušajte ponovo!
    :match_1: Crna|||(0, 0, 0)
    :match_2: Plava|||(0, 0, 255)
    :match_3: Crvena|||(255, 0, 0)
    :match_4: Zelena|||(0, 255, 0)

    uparite boje.

.. mchoice:: pygame__basics_quiz_color_gray
   :answer_a: (1, 12, 123)
   :answer_b: (128, 0, 128)
   :answer_c: (0, 0, 128)
   :answer_d: (145, 145, 145)
   :correct: d
   :feedback_a: Pokušajte ponovo
   :feedback_b: Pokušajte ponovo
   :feedback_c: Pokušajte ponovo
   :feedback_d: Tačno

   Koja od narednih boja je neka nijansa sive?

.. mchoice:: pygame__basics_quiz_color_purple
   :answer_a: crvena i zelena
   :answer_b: plava i crvena
   :answer_c: zelena i plava
   :answer_d: crvena, zelena i plava
   :correct: b
   :feedback_a: Pokušajte ponovo
   :feedback_b: Tačno
   :feedback_c: Pokušajte ponovo
   :feedback_d: Pokušajte ponovo
   
   Koje boje se mešaju da bi se dobila ljubičasta boja?

.. mchoice:: pygame__basics_quiz_color_approx
   :answer_a: Plavkasta
   :answer_b: Crvenkasta
   :answer_c: Žućkasta
   :answer_d: Zelenkasta
   :correct: c
   :feedback_a: Pokušajte ponovo
   :feedback_b: Pokušajte ponovo
   :feedback_c: Tačno
   :feedback_d: Pokušajte ponovo

   Kako bi se boja [240, 230, 18] najbolje mogla nazvati?

Boje se dakle, predstavljaju sa tri, a koordinate tačaka sa dva broja.
Proveri da li ovo razumeš tako što ćeš odgovoriti na naredno pitanje.
   
.. dragndrop:: pygame__basics_quiz_colors_and_coordinates
    :feedback: Pokušajte ponovo!
    :match_1: Crna boja|||[0, 0, 0]
    :match_2: Gornje levo teme ekrana|||[0, 0]
    :match_3: Ljubičasta boja|||(255, 0, 255)
    :match_4: Donje desno teme ekrana|||(300, 200)

    uparite boje i koordinate, ako je ekran širine 300 i visine 200 piksela.
