Pomeranje crteža
----------------

U prethodnim primerima smo napravili nekoliko crteža sastavljenih od osnovnih oblika. Pri tome je za svaki od tih oblika bilo potrebno odrediti tačan položaj da bi se svi delovi uklopili u celinu. Za neke crteže je bilo moguće (a u pojedinim zadacima i potrebno) da se koordinate pojedinih tačaka izračunaju na osnovu poznatih koordinata drugih tačaka. To računanje se moglo obaviti i van programa, a zatim u program samo uneti izračunate koordinate. Bolje je, međutim, da se takva računanja obave u samom programu, i to iz više razloga:

- Možda nećemo iz prvog pokušaja izračunavati koordinate na ispravan način. U takvoj situaciji je lakše izmeniti uputstvo za računanje nego računati sve tačke ručno ponovo.
- Kada sami kreiramo crtež, može se dogoditi da nakon prve verzije programa poželimo da dodamo još nešto, na primer sa leve strane crteža, ali da nemamo dovoljno mesta. U takvom slučaju potrebno je ceo crtež pomeriti udesno, tako što se *x* koordinate svih tačaka povećaju za istu vrednost. Ako smo ručno računali koordinate tačaka, potrebno je izračunati ih sve ponovo. U dobro organizovanom programu za pomeranje crteža udesno dovoljno je promeniti jedan broj. Ovaj postupak će možda biti potrebno ponoviti nekoliko puta dok ne budemo zadovoljni položajem nacrtanog dela, tako da je isprobavanje mnogo lakše kada računa program a ne mi.
- Ako poželimo da nacrtamo isti crtež na više mesta u prozoru, prednosti programskog računanja ponovo dolaze do izražaja.

Sada ćemo još malo sistematizovati računanje koordinata i upotrebiti ga za jednostavnije pomeranje nacrtanih objekata. Pre nego što počnemo, bilo bi dobro da proverite potrebno predznanje i odgovorite na ova pitanja:

.. mchoice:: PyGame__drawing_quiz_point_left
   :answer_a: (50, 60)
   :answer_b: (50, 80)
   :answer_c: (40, 70)
   :answer_d: (60, 70)
   :answer_e: (40, 60)
   :correct: c
   :feedback_a: Pokušajte ponovo
   :feedback_b: Pokušajte ponovo
   :feedback_c: Tačno
   :feedback_d: Pokušajte ponovo
   :feedback_e: Pokušajte ponovo

    Koje su koordinate tačke koja se nalazi 10 piksela levo od tačke (50, 70)?

.. mchoice:: PyGame__drawing_quiz_point_down
   :answer_a: (50, 60)
   :answer_b: (50, 80)
   :answer_c: (40, 70)
   :answer_d: (60, 70)
   :answer_e: (40, 60)
   :correct: b
   :feedback_a: Pokušajte ponovo
   :feedback_b: Tačno
   :feedback_c: Pokušajte ponovo
   :feedback_d: Pokušajte ponovo
   :feedback_e: Pokušajte ponovo

    Koje su koordinate tačke koja se nalazi 10 piksela ispod tačke (50, 70)?

.. mchoice:: PyGame__drawing_quiz_rect_up_left
   :answer_a: pg.draw.rect(prozor, boja, (70, 120, 50, 60))
   :answer_b: pg.draw.rect(prozor, boja, (100, 150, 110, 120))
   :answer_c: pg.draw.rect(prozor, boja, (100, 150, 50, 60))
   :answer_d: pg.draw.rect(prozor, boja, (70, 120, 80, 90))
   :answer_e: pg.draw.rect(prozor, boja, (70, 180, 80, 90))
   :correct: d
   :feedback_a: Pokušajte ponovo
   :feedback_b: Pokušajte ponovo
   :feedback_c: Pokušajte ponovo
   :feedback_d: Tačno
   :feedback_e: Pokušajte ponovo

   Pravougaonik je nacrtan pomoću ``pg.draw.rect(prozor, boja, (100, 150, 80, 90))``. Kako se može nacrtati pravougaonik iste veličine koji se nalazi 30 piksela levo i 30 piksela iznad ovog pravougaonika?
          
.. mchoice:: PyGame__drawing_quiz_circle_above
   :answer_a: pg.draw.circle(prozor, boja, (100, 120), 40)
   :answer_b: pg.draw.circle(prozor, boja, (100, 160), 40)
   :answer_c: pg.draw.circle(prozor, boja, (120, 100), 40)
   :answer_d: pg.draw.circle(prozor, boja, (160, 100), 40)
   :answer_e: pg.draw.circle(prozor, boja, (20, 120), 40)
   :correct: a
   :feedback_a: Tačno
   :feedback_b: Pokušajte ponovo
   :feedback_c: Pokušajte ponovo
   :feedback_d: Pokušajte ponovo
   :feedback_e: Pokušajte ponovo

   Krug je nacrtan pomoću ``pg.draw.circle(prozor, boja, (100, 200), 40)``. Kako se može nacrtati krug iste veličine koji se nalazi iznad ovog kruga i dodiruje ga?


Prepravljanje nepomičnog crteža u pomični
'''''''''''''''''''''''''''''''''''''''''

Pogledajmo kako je nacrtan oblak u sledećem primeru:

.. activecode:: PyGame__drawing_cloud_fixed
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\cloud_fixed.py

Oblak smo predstavili pomoću tri kruga, jednog većeg u sredini i dva manja oko njega:

.. code::

    pg.draw.circle(prozor, pg.Color("white"), (200, 200), 50)
    pg.draw.circle(prozor, pg.Color("white"), (150, 200), 30)
    pg.draw.circle(prozor, pg.Color("white"), (250, 200), 30)

Ako bismo hteli da taj oblak nacrtamo na različitim visinama, mogli bismo da ponavljamo ove tri naredbe, svaki put sa nekom novom vrednošću za :math:`y` koordinatu centara ova tri kruga umesto 200, koliko je na početku. Na primer:

.. code::

    pg.draw.circle(prozor, pg.Color("white"), (200, 200), 50)
    pg.draw.circle(prozor, pg.Color("white"), (150, 200), 30)
    pg.draw.circle(prozor, pg.Color("white"), (250, 200), 30)

    pg.draw.circle(prozor, pg.Color("white"), (200, 80), 50)
    pg.draw.circle(prozor, pg.Color("white"), (150, 80), 30)
    pg.draw.circle(prozor, pg.Color("white"), (250, 80), 30)
    
    pg.draw.circle(prozor, pg.Color("white"), (200, 320), 50)
    pg.draw.circle(prozor, pg.Color("white"), (150, 320), 30)
    pg.draw.circle(prozor, pg.Color("white"), (250, 320), 30)

.. image:: ../../_images/PyGame/clouds.png
    :width: 400px
    :align: center

Na ovaj način, ne samo da program raste brže nego što mora, nego i svaku promenu treba da napravimo na tri mesta (na primer, ako umesto 320 želimo da probamo 330, tu promenu treba napraviti na tri mesta). Tri izmene nije mnogo, ali ako usvojimo takav način rada, na složenijim crtežima (i složenijim programima uopšte) bismo imali sve više problema. 

Umesto ovoga, bolje je da napravimo funkciju i da :math:`y` koordinatu centara prosleđujemo kao parametar:

.. code::

    def oblak(yc):
        pg.draw.circle(prozor, pg.Color("white"), (200, yc), 50)
        pg.draw.circle(prozor, pg.Color("white"), (150, yc), 30)
        pg.draw.circle(prozor, pg.Color("white"), (250, yc), 30)

    oblak(200)
    oblak(80)
    oblak(320)

Novi program je pregledniji i lakši za dalje menjanje i isprobavanje. Za više oblaka, ili složenije oblake, prednost ovakvog pristupa bi bila još veća.

A kako bi izgledalo pomeranje oblaka na levo ili desno? Trebalo bi :math:`x` koordinate 200, 150, 250 centara krugova sve povećati ili smanjiti za istu vrednost. Na primer, ako bismo kao :math:`x` koordinate upisali 260, 210, 310, ceo oblak bi bio pomeren za 60 piksela desno. 

Bilo bi dobro da možemo da pomoću samo jednog broja zadamo i vodoravni položaj oblaka. Da bismo to postigli, primetimo da su centri manjih krugova udaljeni po 50 piksela od centra srednjeg kruga na levo i desno. Ova rastojanja se ne menjaju pri pomeranju oblaka. To znači da ako sa :math:`X_c` označimo :math:`x` koordinatu centra srednjeg kruga, onda centri manjih krugova imaju :math:`x` koordinate :math:`X_c - 50` i :math:`X_c + 50`. Zahvaljujući ovoj stalnoj vezi (koja ne zavisi od položaja oblaka), sada možemo u funkciju za crtanje oblaka da uvedemo i parametar :math:`x`:

.. code::

    def oblak(xc, yc):
        pg.draw.circle(prozor, pg.Color("white"), (xc, yc), 50)
        pg.draw.circle(prozor, pg.Color("white"), (xc - 50, yc), 30)
        pg.draw.circle(prozor, pg.Color("white"), (xc + 50, yc), 30)
        
    oblak(200, 200)
    oblak(200, 80)
    oblak(200, 320)

Bilo koji od ova tri oblaka bismo sada lako mogli da pomerimo na primer 60 piksela na desno, tako što u pozivu funkcije na mestu :math:`x` koordinate (prvog parametra) umesto 200 upišemo 260. Jednako lako je i napraviti crtež sa nekoliko oblaka. Boja, odnosno nijansa sive, takođe može da bude parametar funkcije. Na taj način neki oblaci mogu da budu tamniji, a neki svetliji.

Kada iskoristimo sve pomenuto, možemo da napravmo program koji crta nekoliko oblaka raznih nijansi, na primer:

.. activecode:: PyGame__drawing_cloud_movable
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\clouds_movable.py

Rezimirajmo, uz mala uopštenja, šta je potrebno da se uradi da bismo mogli da prkazujemo jedan crtež na raznim mestima: 

- Treba da izaberemo jednu tačku čije se koordinate zadaju direktno. Ovu izabranu tačku zvaćemo **glavna tačka**, (ponekad se ova tačka naziva i **sidro**, engl. anchor). U primeru oblaka, glavna tačka je centar srednjeg kruga.
- Nakon izbora glavne tačke, koordinate svih ostalih bitnih tačaka određujemo u odnosu na nju, tako što na koordinate glavne tačke dodajemo ili oduzimamo određeni pomeraj. U primeru sa oblakom, da bismo dobili :math:`x` koordinatu centra levog kruga, od :math:`x` koordinate glavne tačke tačke (centra srednjeg kruga) oduzimamo 50 piksela, a za desni krug dodajemo 50 piksela. 

U opštem slučaju, na crtežu može biti i drugih oblika osim krugova. Tačke koje određuju položaje tih oblika su: 

- za duž: njeni krajevi 
- za mnogougao: njegova temena
- za krug: njegov centar
- za pravougaonik: njegovo gornje levo teme
- za elipsu: gornje levo teme pravougaonika u koji je upisana ta elipsa

Sve ove tačke treba zadati u odnosu na glavnu tačku, to jest izraziti njihove koordinate kao koordinate glavne tačke uvećane ili umanjene za neku vrednost.

Proverite koliko ste razumeli prethodna objašnjenja i odgorovite na pitanja.

.. mchoice:: PyGame__drawing_quiz_anchor_introduction1
   :answer_a: pg.draw.circle(prozor, pg.Color("red"), (x, y), 50, 1)
   :answer_b: pg.draw.circle(prozor, pg.Color("red"), (x+120, y+90), 50, 1)
   :answer_c: pg.draw.circle(prozor, pg.Color("red"), (x+20, y-10), 50, 1)
   :answer_d: pg.draw.circle(prozor, pg.Color("red"), (x-20, y+10), 50, 1)
   :correct: c
   :feedback_a: Pokušajte ponovo
   :feedback_b: Pokušajte ponovo
   :feedback_c: Tačno
   :feedback_d: Pokušajte ponovo

   Želimo da prilagodimo crtež koji se sastoji od nekoliko oblika, tako da se sve crta u odnosu na sidro sa koordinatama `x=100`, `y=100`. Jedna od naredbi koje formiraju crtež je
                
   .. activecode:: PyGame__drawing_quiz_anchor_introduction_code1
      :passivecode: true
                    
      pg.draw.circle(prozor, pg.Color("red"), (120, 90), 50, 1)

   Koja naredba treba da zameni datu?
      
.. mchoice:: PyGame__drawing_quiz_anchor_introduction2
   :answer_a: pg.draw.line(prozor, pg.Color("red"), (x-50, y-50), (150, 150))
   :answer_b: pg.draw.line(prozor, pg.Color("red"), (x-50, y-50), (x+50, y+50))
   :answer_c: pg.draw.line(prozor, pg.Color("red"), (x-50, x+50), (y-50, y+50))
   :answer_d: pg.draw.line(prozor, pg.Color("red"), (x+50, y+50), (x+150, y+150))
   :correct: b
   :feedback_a: Pokušajte ponovo
   :feedback_b: Tačno
   :feedback_c: Pokušajte ponovo
   :feedback_d: Pokušajte ponovo

   Želimo da prilagodimo crtež koji se sastoji od nekoliko oblika, tako da se sve crta u odnosu na sidro sa koordinatama `x=100`, `y=100`. Jedna od naredbi koje formiraju crtež je
                
   .. activecode:: PyGame__drawing_quiz_anchor_introduction_code2
      :passivecode: true
                    
      pg.draw.line(prozor, pg.Color("red"), (50, 50), (150, 150))

   Koja naredba treba da zameni datu?
      
.. mchoice:: PyGame__drawing_quiz_anchor_introduction3
   :answer_a: pg.draw.rect(prozor, pg.Color("red"), (x-50, y-50, x, y))
   :answer_b: pg.draw.rect(prozor, pg.Color("red"), (x, y, 100, 100))
   :answer_c: pg.draw.rect(prozor, pg.Color("red"), (x+50, y+50, 100, 100))
   :answer_d: pg.draw.rect(prozor, pg.Color("red"), (x-50, y-50, 100, 100))
   :correct: d
   :feedback_a: Pokušajte ponovo
   :feedback_b: Pokušajte ponovo
   :feedback_c: Pokušajte ponovo
   :feedback_d: Tačno

   Želimo da prilagodimo crtež koji se sastoji od nekoliko oblika, tako da se sve crta u odnosu na sidro sa koordinatama `x=100`, `y=100`. Jedna od naredbi koje formiraju crtež je
                
   .. activecode:: PyGame__drawing_quiz_anchor_introduction_code3
      :passivecode: true
                    
      pg.draw.rect(prozor, pg.Color("red"), (50, 50, 100, 100))

   Koja naredba treba da zameni datu?
      
.. mchoice:: PyGame__drawing_quiz_move_to_the_right
   :multiple_answers:
   :answer_a: Umesto pg.draw.circle(prozor, boja, (x, y), r, d) pozvaćemo pg.draw.circle(prozor, boja, (x+100, y), r, d).
   :answer_b: Umesto pg.draw.circle(prozor, boja, (x, y), r, d) pozvaćemo pg.draw.circle(prozor, boja, (x-100, y-100), r, d).
   :answer_c: Umesto pg.draw.rect(prozor, boja, (x, y, w, h), d) pozvaćemo pg.draw.circle(prozor, boja, (x+100, y, w+100, h), d).
   :answer_d: Umesto pg.draw.rect(prozor, boja, (x, y, w, h), d) pozvaćemo pg.draw.rect(prozor, boja, (x+100, y, w, h), d).
   :answer_e: Umesto pg.draw.rect(prozor, boja, (x, y, w, h), d) pozvaćemo pg.draw.rect(prozor, boja, (x-100, y, w, h), d).
   :correct: a, d
   :feedback_a: Tačno
   :feedback_b: Pokušajte ponovo
   :feedback_c: Pokušajte ponovo
   :feedback_d: Tačno
   :feedback_e: Pokušajte ponovo

   Želimo da pomerimo crtež koji se sastoji od nekoliko oblika nadesno za 100 piksela. Označite tačna tvrđenja.

Slede još neki primeri pretvaranja fiksnog crteža u pomični.

Meda - položaj
''''''''''''''

Dat je sledeći program, koji prikazuje glavu medvedića igračke:

.. activecode:: PyGame__drawing_bear_fixed
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\teddy-bear_fixed.py

U programu se sedam puta poziva funkcija *uokviren_krug*, koja zadati krug uokviruje crnom bojom (mada je za tri mala crna kruga mogla je da bude pozvana i samo funkcija *circle*). Da bismo mogli da menjamo položaj crteža, izaberimo glavnu tačku (sidro). Neka to bude centar velikog kruga, to jest glave medvedića. Koordinate ove tačke su (250, 150). Sada je potrebno da koordinate centara svih ostalih krugova izrazimo polazeći od glavne tačke, pomerajući se za potreban broj piksela u smeru :math:`x` i :math:`y` ose. Uzmimo kao primer desno uvo medvedića.

:math:`x` koordinata centra desnog uveta je :math:`310 = 250 + 60`, dok je :math:`y` koordinata :math:`80 = 150 - 70`. Odavde se vidi da koordinate centra desnog uveta možemo u programu da napišemo kao :code:`(cx + 60,  cy - 70)`, gde su :code:`(cx, cy)` koordinate glavne tačke. Sprovedite isti postupak za ostale krugove i dovršite funkciju *crtaj_medu*.

.. activecode:: PyGame__drawing_bear_movable1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\5_Movable\teddy-bear_movable1b.py

   
    # bojimo pozadinu prozora u belo
    prozor.fill(pg.Color("white"))
    
    def uokviren_krug(prozor, boja, centar, poluprecnik):
        pg.draw.circle(prozor, boja, centar, poluprecnik)
        pg.draw.circle(prozor, pg.Color("black"), centar, poluprecnik, 1)
    
    def crtaj_medu(cx, cy):
        uokviren_krug(prozor, pg.Color("yellow"), (cx - 60,  cy - 70),  45) # levo uvo
        # dovrsite
        
    crtaj_medu(sirina // 2, visina // 2)

Ovako napisan program nam omogućava da jednostavno prikazujemo medvediće na raznim mestima na ekranu. Na primer, možete da poziv funkcije

.. code::

    crtaj_medu(sirina // 2, visina // 2)
    
koja crta medvedića sa glavnom tačkom u centru prozora (kao što je i bio), zamenite sa sledeća dva:

.. code::

    crtaj_medu(sirina // 2 - 120, visina // 2)
    crtaj_medu(sirina // 2 + 120, visina // 2)

Isprobajte ovo! Bilo bi znatno teže nacrtati drugog medevedića da nismo početni program prilagodili za ovakvu upotrebu.

Kuća - položaj
''''''''''''''

Recimo da ste napisali ovaj program, a cilj vam je da prepravite program tako da kućica može jednostavno da se premešta:

.. activecode:: PyGame__drawing_house_detailed_fixed
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\house2D_detailed_fixed.py

Neka je glavna tačka :code:`(x, y) = (50, 150)`. Dovršite započeto prepravljanje programa u polju ispod, u kome se crtanje obavlja u funkciji :code:`kuca(x, y, boja_zidova)`. Kada se uverite da crteži u dva programa izgledaju isto (osim što su prozori u kojima se crta različite veličine), zamenite poziv :code:`kuca( 50, 150, pg.Color("khaki"))` sa sledeća 4, da biste dobili sliku kao kad se klikne na dugme "Prikaži primer":

.. code::

    kuca(150,  90, pg.Color(220, 220, 220))
    kuca(220, 130, pg.Color("white"))
    kuca(350, 160, (255,255,150))
    kuca( 50, 150, pg.Color("khaki"))

.. activecode:: PyGame__drawing_house_detailed_movable
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask: 
    :includexsrc: src\PyGame\1_Drawing\5_Movable\house2D_detailed_movable.py
   
    prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno

    def kuca(x, y, boja_zidova):
        pg.draw.polygon(prozor, pg.Color("red"), [(x, y), (x+???, y-???), (x+140, y)]) # krov
        pg.draw.rect(prozor, boja_zidova,       (x,       y,     140, 100))   # kuca
        pg.draw.rect(prozor, pg.Color("brown"), (x + ???, y + ???,  30,  30)) # levi prozor
        pg.draw.rect(prozor, pg.Color("brown"), (x + ???, y + ???, ???, ???)) # desni prozor
        pg.draw.rect(prozor, pg.Color("brown"), (x + ???, y + ???, ???, ???)) # vrata
        
    kuca( 50, 150, pg.Color("khaki"))
    
.. commented out

    Zadatak je nekativan (u komentaru) dok se ne reši povezano tehničko pitanje 

    Zadatak - crtež koji se stalno pomera
    '''''''''''''''''''''''''''''''''''''

    Sledeća funkcija iscrtava neki crtež. 
       
    .. activecode:: PyGame__drawing_movable_scalable_given

       def crtanje():
           prozor.fill(pg.Color("white"))
           pg.draw.circle(prozor, pg.Color("blue"), (100, 100), 60)
           pg.draw.circle(prozor, pg.Color("yellow"), (75, 75), 15)
           pg.draw.circle(prozor, pg.Color("black"), (80, 80), 5)
           pg.draw.circle(prozor, pg.Color("yellow"), (125, 75), 15)
           pg.draw.circle(prozor, pg.Color("black"), (120, 80), 5)
           pg.draw.ellipse(prozor, pg.Color("red"), (75, 110, 50, 10))

    U programu koji sledi funkcija koja crta je samo započeta. Dovršite je tako da crta isti crtež, ali da pri tome koristi sidro :math:`(x, y)`, koje se nalazi u centru plavog kruga (u početku je to tačka :math:`(100, 100)`). 

    Kada završite funkciju, proverite da li radi isto kao kada kliknete na dugme "Prikaži primer".

    .. activecode:: PyGame__drawing_movable
       :nocodelens:
       :enablecopy:
       :modaloutput:
       :playtask:
       :includexsrc: src\PyGame\1_Drawing\5_Movable\movable_scalable.py
       
                     
       def crtanje():
           prozor.fill(pg.Color("white"))

.. commented out

    .. reveal:: PyGame__drawing_movable_reveal
       :showtitle: Prikaži rešenje
       :hidetitle: Sakrij rešenje

       .. activecode:: PyGame_movable_code
          :passivecode:

          def crtanje():
              prozor.fill(pg.Color("white"))
              pg.draw.circle(prozor, pg.Color("blue"), (x, y), 60)
              pg.draw.circle(prozor, pg.Color("yellow"), (x-25, y-25), 15)
              pg.draw.circle(prozor, pg.Color("black"), (x-20, y-20), 5)
              pg.draw.circle(prozor, pg.Color("yellow"), (x+25, y-25), 15)
              pg.draw.circle(prozor, pg.Color("black"), (x+20, y-20), 5)
              pg.draw.ellipse(prozor, pg.Color("red"), (x-25, y+10, 50, 10))
           

