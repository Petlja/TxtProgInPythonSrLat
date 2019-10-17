Očitavanje tastature
--------------------

Dobijanje informacije o pritisnutim tasterima na tastaturi je vrlo slično kao za tastere miša. Funkcija ``pg.key.get_pressed()`` vraća torku čiji se elementi koriste kao logičke vrednosti, a pokazuju za svaki taster na tastaturi da li je on trenutno pritisnut ili ne.

Pošto tastatura ima mnogo više tastera nego miš, korišćenje indeksa 0, 1, 2 itd. za pojedine tastere bi bilo nepraktično. Da ne bismo morali da znamo koji indeks u torci odgovara kojem tasteru, PajGejm biblioteka sadrži imenovane konstante koje koristimo kao indekse. Na primer, konstante ``pg.K_LEFT``, ``pg.K_RIGHT``, ``pg.K_UP``, ``pg.K_DOWN`` odgovaraju tasterima sa strelicama, koji se često očitavaju. Tasteru za razmak odgovara konstanta ``pg.K_SPACE``, dok tasterima slova na primer *a*, *b*, *c* odgovaraju konstante ``pg.K_a``, ``pg.K_b``, ``pg.K_c`` itd. kompletan spisak ovih konstanti možete da vidite `ovde <https://www.pygame.org/docs/ref/key.html>`__ .
 
Primeri i zadaci
''''''''''''''''

.. questionnote::

    **Primer - Svemirski brod:** U ovom primeru imamo sličicu svemirskog broda, koju pomeramo levo - desno u skladu sa pritisnutim strelicama. Osim toga, iz broda može da se puca pritiskom na razmak. 
    
Najpre obratite pažnju na istaknuti deo programa sa svetlijom pozadinom (linije 23-37). To je deo koji je ovde nov, i on je nešto detaljnije prokomentarisan i u samom kodu.

Ostali deo programa samo radi animaciju više objekata, a to je tehnika poznata od ranije.

.. image:: ../../_images/spaceship.png
   :width: 50px

.. activecode:: PyGame__interact_spaceship_arrow_keys
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3c_Keyboard_read/spaceship_arrow_keys.py

Dakle, nakon što očitamo stanje svih tastera i smestimo ga u torku *pritisnut*, u *if* naredbi jednostavno proveravamo stanje tastera koji nas interesuju.


.. questionnote::

    **Zadatak - navigacija:**  Dopunite sledeći program, tako da se pomoću 4 strelice upravlja žutim krugom, kao u primeru. Krug treba da se ne pomera ako nije pritisnuta ni jedna strelica, a da se kreće za po jedan piksel u smeru strelica koje su pritisnute (pritisnute suprotne strelice se međusobno poništavaju).
    

.. activecode:: PyGame__interact_navigtate1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src/PyGame/3_Interaction/3c_Keyboard_read/navigtate1.py

        pritisnut = pg.key.get_pressed()
        if pritisnut[pg.K_LEFT] and (x > 0):
            x -= 1
            
        # DOVRSITE



.. questionnote::

    **Zadatak - zmija:**  Dopunite sledeći program, tako da pomoću strelica može da se upravlja 'zmijom' koja se sastoji od nekoliko kvadratića, kao u primeru.
    
    Promenljive *d_red* i *d_kol* označavaju smer kretanja zmije. Dok ni jedna strelica nije pritisnuta, ove promenljive ne menjaju vrednost i zmija nastavlja da se kreće u istom smeru. Vaš zadatak je da dodate naredbe za očitavanje stanja tastature i izračunavanje novih vrednsti za *(d_red, d_kol)* na osnovu pritisnutih strelica, tako da se kretanje nastavi u izabranom smeru.

**Pomoć:** ako se glava zmije nalazila na polju *(red, kol)*, u novom frejmu će se nalaziti na polju *(red + d_red, kol + d_kol)*. Proverite da li razumete kako treba dodeliti vrednosti promenljivama *d_red*, *d_kol* za svaki od smerova:

.. mchoice:: pygame__interact_quiz_direction
   :answer_a: Gore
   :answer_b: Dole
   :answer_c: Levo
   :answer_d: Desno
   :correct: c
   :feedback_a: Ne, vrednosti za gore su (d_red, d_kol) = (-1, 0)
   :feedback_b: Ne, vrednosti za dole su (d_red, d_kol) = (1, 0)
   :feedback_c: Tačno
   :feedback_d: Ne, vrednosti za desno su (d_red, d_kol) = (0, 1)

   Ako se promenljivama (d_red, d_kol) dodele vrednosti (0, -1), u kom smeru se nastavlja kretanje?

.. activecode:: PyGame__interact_snake
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src/PyGame/3_Interaction/3c_Keyboard_read/snake.py
    
        # OVDE IZRACUNAJTE POMERAJ (d_red, d_kol)
        # NA OSNOVU PRITISNUTIH TASTERA

.. commented out
    
    import pygame as pg, pygamebg, random
    (sirina, visina) = (400, 400)
    prozor = pygamebg.open_window(sirina, visina, "Zmija")

    boja_zmije = (255, 0, 0)            # boja zmije
    a = 10                              # velicina jednog polja
    (br_redova, br_kolona) = (visina // a, sirina // a) # velicina table
    (d_red, d_kol) = (0, 1) # inicijalno po jednu kolonu udesno
    centar = (br_redova // 2, br_kolona // 2) # koordinate centra table
    zmija = [centar] * 10 # na pocetku je zmija sklupcana u centru
    i_glava = 0 # indeks kvadratica u listi koji predstavlja glavu zmije
    kraj = False

    def crtanje():
        prozor.fill(pg.Color("gray")) # bojimo prozor u sivo
        if kraj:
            # ispisujemo poruku da je kraj
            font = pg.font.SysFont("Arial", 60)
            sl_tekst = font.render("Kraj!", True, pg.Color("black"))
            x = (sirina - sl_tekst.get_width()) // 2
            y = (visina - sl_tekst.get_height()) // 2
            prozor.blit(sl_tekst, (x, y))
        else:
            # crtamo zmiju
            for red, kol in zmija:
                pg.draw.rect(prozor, boja_zmije, (kol*a, red*a, a, a))


    def nov_frejm():
        global zmija, i_glava, d_red, d_kol, kraj
        
        # OVDE IZRACUNAJTE POMERAJ (d_red, d_kol)
        # NA OSNOVU PRITISNUTIH TASTERA
        
        # izracunavamo nov polozaj glave zmije
        red, kol = zmija[i_glava]
        i_glava = (i_glava + 1) % len(zmija)
        zmija[i_glava] = (red + d_red, kol + d_kol)
        if kol < 0 or kol >= br_kolona or red < 0 or red >= br_redova:
            kraj = True  # zmija je izasla iz table
        
        crtanje()


    pygamebg.frame_loop(10, nov_frejm)


Pitanja
'''''''

Dok odgovarate na pitanja, vraćajte se po potrebi na program "zmija" i pogledajte deo koji vam je potreban za odgovor.

.. fillintheblank:: pygame__interact_quiz_snake_tablesize

    Koliko redova ima tabla?

    - :40: Tačno!
      :[0-9]+: Pogledajte početak programa pažljivije.
      :.*: Odgovor treba da bude zapisan ciframa.

.. mchoice:: pygame__interact_quiz_snake_rowcol_to_xy
   :answer_a: x = red*a + a, y = kol*a + a
   :answer_b: x = kol*a + a, y = red*a + a
   :answer_c: x = red*a, y = kol*a
   :answer_d: x = kol*a, y = red*a
   :correct: d
   :feedback_a: Pokušajte ponovo
   :feedback_b: Pokušajte ponovo
   :feedback_c: Pokušajte ponovo
   :feedback_d: Tačno

   Koje su koordinate gornjeg levog ugla kvadratića na mestu *(red, kol)*?

.. mchoice:: pygame__interact_quiz_snake_head
   :multiple_answers:
   :answer_a: Lista zmija se u svakom frejmu produžava za novi element koji predstavlja novi položaj glave zmije.
   :answer_b: Lista zmija tokom rada programa stalno ima isti broj elemenata.
   :answer_c: Iz liste zmija se u svakom frejmu izbacuje jedan element, koji predstavlja kraj repa zmije.
   :correct: b
   :feedback_a: Ne postoji takva naredba u programu
   :feedback_b: Tačno
   :feedback_c: Ne postoji takva naredba u programu.

   Koje rečenice su tačne?
    

.. commented out

    chase_and_avoid.py