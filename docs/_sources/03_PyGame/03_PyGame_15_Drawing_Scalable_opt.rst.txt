Promena veličine crteža
-----------------------

Kada smo govorili o pomeranju crteža, pomenuli smo da je bolje da se sva računanja obave u programu, jer je tako jednostavnije da se po potrebi ceo crtež pomeri ili nacrta na više mesta. Slična je situacija ako je potrebno da crtež bude manji, ili veći, ili da se nacrta na više mesta u različitim veličinama. Umesto računanja svih koordinata ispočetka, pri programskom računanju može biti dovoljno da se promeni jedan jedini broj, pa da dobijemo crtež druge veličine.

Da bismo naučili kako da pravimo crteže kojima veličina može lako da se menja, hajde prvo da vidimo šta sve treba da se promeni u nekom programu za crtanje, pa da crtež bude neke druge određene veličine. Na primer, ako smo nacrtali oblak pomoću ovih naredbi:

.. code::

    def     oblak(x, y, siva):
        # crtamo oblak od tri kruga
        boja = (siva, siva, siva)
        pg.draw.circle(prozor, boja, (x,      y), 50)
        pg.draw.circle(prozor, boja, (x - 50, y), 30)
        pg.draw.circle(prozor, boja, (x + 50, y), 30)

    oblak(200, 200, 180)

i sada želimo da oblak bude dvostruko manji, a da mu sredina i dalje bude u tački (200, 200), onda bismo funkciju datu gore izmenili u:

.. code::

    def oblak(x, y, siva):
        # crtamo oblak od tri kruga
        boja = (siva, siva, siva)
        pg.draw.circle(prozor, boja, (x,      y), 25)
        pg.draw.circle(prozor, boja, (x - 25, y), 15)
        pg.draw.circle(prozor, boja, (x + 25, y), 15)
    
Treba smanjiti poluprečnike sva tri kruga na pola prethodne veličine (25 piksela umesto 50, a 15 umesto 30), ali to nije dovoljno. Ako bi centri malih krugova ostali gde su bili, dobili bismo tri razdvojena kruga (isprobajte). Da bi crtež i dalje ličio na oblak, potrebno je i da krugove međusobno približimo. Preciznije rečeno, rastojanja centara manjih krugova od centra velikog kruga treba takođe da budu dva puta manja nego pre, to jest po 25 umesto po 50 piksela.

U opštem slučaju ne želimo uvek dvostruko manji oblak nego da oblaci mogu da budu različitih veličina. Osim toga, ne želimo da za svaku veličinu oblaka pravimo posebnu funkciju, nego da imamo jednu funkciju koja može da crta oblak zadate veličine. Najudobnije bi bilo da možemo veličinu oblaka da zadajemo samo jednim brojem i da promenom tog jednog broja menjamo veličinu oblaka. Da bismo to postigli, potrebno je da sve veličine koje se menjaju sa promenom veličine oblaka (a to su rastojanja između centara krugova i poluprečnici tih krugova) izrazimo pomoću jedne veličine. Možemo na primer za tu jednu veličinu da uzmemo poluprečnik srednjeg kruga, koji ćemo da označimo sa :math:`r`. Rastojanja centara manjih krugova do centra većeg kruga su jednaka upravo po :math:`r`, a poluprečnik manjih krugova je jednak :math:`{3 \over 5} r` bez obzira na veličinu oblaka. Kada iskoristimo sve ove veze koje smo uočili, funkcija dobija sledeći izgled:

.. code::

    def oblak(x, y, r, siva):
        # crtamo oblak od tri kruga
        boja = (siva, siva, siva)
        r_malo = round(3 * r / 5)
        pg.draw.circle(prozor, boja, (x,     y), r)
        pg.draw.circle(prozor, boja, (x - r, y), r_malo)
        pg.draw.circle(prozor, boja, (x + r, y), r_malo)

Funkcija ima jedan parametar više, tako da osim položaja i nijanse sive boje, ovoj funkciji zadajemo i veličinu oblaka. Sada možemo da pravimo i ovakve crteže:

.. activecode:: PyGame__drawing_clouds_scalable
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\6_Scalable\clouds_scalable.py

Hajde da sada nabrojimo korake za uopšteni postupak, kojim bismo prepravili crtanje bilo kog pomičnog crteža tako da mu se može menjati i veličina:

- Treba da odredimo jednu dužinu na crtežu, koja će da se zadaje direktno. Ovu izabranu dužinu možemo da nazovemo **osnovna dužina** ili **jedinica mere**. U primeru oblaka, osnovna dužina je poluprečnik srednjeg kruga.
- Sve poluprečnike krugova od kojih se crtež sastoji izražavamo srazmerno osnovnoj dužini. To znači da, ako je naša osnovna dužina označena sa :math:`a`, sve druge dužine u programu će biti neki broj pomnožen sa :math:`a`, na primer :math:`2a` ili :math:`5a`. Ovaj broj određujemo iz odnosa tražene dužine i izabrane osnovne dužine na početnom crtežu (taj odnos ostaje isti i kada se veličina crteža promeni). U primeru sa oblakom, poluprečnik malog kruga je uvek :math:`{3 \over 5}` izabrane osnovne dužine :math:`r`. Ako se na crtežu pojavljuju i pravougaonici ili elipse, dužine i širine tih pravougaonika i elipsi takođe treba da izrazimo srazmerno osnovnoj dužini, na isti način kao i poluprečnike krugova. 
- Koordinate svih tačaka određujemo u odnosu na glavnu tačku, tako što :math:`x` i :math:`y` koordinati glavne tačke dodajemo ili oduzimamo određeni broj osnovnih dužina. Potreban broj osnovnih dužina se i u ovom slučaju određuje iz odnosa na početnom crtežu. U primeru sa oblakom, da bismo dobili :math:`x` koordinatu centra levog kruga, od :math:`x` koordinate glavne tačke (centra srednjeg kruga) oduzimamo **jednu** osnovnu dužinu, jer je odnos razlike :math:`x` koordinata i osnovne dužine jednak jedan. Isti postupak se u principu primenjuje i na :math:`y` koordinate, mada je u ovom slučaju to posebno jednostano. Kako su :math:`y` koordinate centara krugova iste, odnos razlike :math:`y` koordinata i osnovne dužine je nula, pa na :math:`y` koordinatu sidra treba dodati nula osnovnih dužina da bismo dobili :math:`y` koordinatu centra manjeg kruga.

Da bismo bolje razumeli postupak promene veličine crteža, primenićemo ga i na primeru medvedića.

Meda - veličina
'''''''''''''''

Dat je sledeći program, koji prikazuje glavu medvedića igračke, tako da se ona lako može premeštati:

.. activecode:: PyGame__drawing_bear_movable
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\teddy-bear_movable1a.py

Da bismo mogli da menjamo veličinu crteža, uvedimo osnovnu dužinu, na primer :math:`a = 5`. Sada sve poluprečnike možemo da izrazimo pomoću :math:`a` ovako:

.. code::

    uokviren_krug(prozor, pg.Color("yellow"), (cx - 60,  cy - 70),  9*a) # levo uvo
    uokviren_krug(prozor, pg.Color("yellow"), (cx + 60,  cy - 70),  9*a) # desno uvo
    uokviren_krug(prozor, pg.Color("yellow"), (cx,       cy)     , 20*a) # glava
    uokviren_krug(prozor, pg.Color("yellow"), (cx,       cy + 50), 10*a) # njuska
    uokviren_krug(prozor, pg.Color("black"),  (cx - 50,  cy - 30),  3*a) # levo oko
    uokviren_krug(prozor, pg.Color("black"),  (cx + 50,  cy - 30),  3*a) # desno oko
    uokviren_krug(prozor, pg.Color("black"),  (cx,       cy + 20),  3*a) # vrh njuske
    
Kao osnovna dužina se može izabrati bilo koji broj, a izborom osnovne dužine od 5 piksela, postigli smo da ne moramo da koristimo realne brojeve - svi poluprečnici su celobrojni umnošci od :math:`a` i možemo lako da ih izračunamo napamet. Na primer, poluprečnik od 45 pikesla izražavamo kao :math:`45=9 \cdot 5 = 9 \cdot a`, i tako dalje.

Sada je potrebno da koordinate centara svih ostalih krugova izrazimo polazeći od glavne tačke :math:`(cx, cy)`, pomerajući se za potreban broj dužina :math:`a` u smeru :math:`x` i :math:`y` ose. Uzmimo kao primer desno uvo medvedića.

:math:`x` koordinata centra desnog uveta je :math:`cx + 60 = cx + 12 a`, dok je :math:`y` koordinata :math:`cy - 70 = cy - 14 a`. Kada ovo uradimo za sve centre krugova, dolazimo do sledećeg oblika programa:

.. activecode:: PyGame__drawing_bear_tmp2
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\6_Scalable\teddy-bear_scalable1a.py
    
Sada možemo ne samo da premeštamo ili kopiramo medvedića po ekranu, nego i da ga prikazujemo u raznim veličinama. Kao potvrdu da menjanje veličine zaista radi, možete poziv funkcije

.. code::

    crtaj_medu(sirina // 2, visina // 2, 6)
    
koja crta medvedića sa glavnom tačkom u centru prozora, da zamenite sa sledećih pet:

.. code::

    crtaj_medu(85, 100, 4)
    crtaj_medu(235, 100, 3)
    crtaj_medu(50, 250, 2)
    crtaj_medu(150, 250, 2)
    crtaj_medu(250, 250, 2)

Iskopirajte ili prepišite ovih pet linija koda u program i isprobajte! Razmislite koliko bi posla bilo da se ovih pet medvedića prikažu bez računanja u programu.


Pokušajte sada da dovršite jedan započeti primer.

Zadatak - veličina kuće
'''''''''''''''''''''''

Počećemo od programa koji crta četiri kućice na zadatim mestima na ekranu:

.. activecode:: PyGame__drawing_house_detailed1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\5_Movable\house2D_detailed_movable.py

Dovršite prepravku programa u polju ispod, tako da kućice mogu jednostavno da se povećavaju i smanjuju. Za osnovnu veličinu možete da uzmete na primer 10 piksela, jer je u tom slučaju izražavanje svih dužina pomoću osnovne dužine vrlo jednostavno. Kada potvrdite da program nakon prepravke prikazuje istu sliku kao i polazni program koji je dat gore, zamenite date pozive funkcije *kuca* sa sledeća 4, i tako proverite da li promena veličine kuće radi kako treba (treba da dobijete sliku kao pri kliku na dugme "Prikaži primer"):

.. code::

    kuca(150,  90,  8, pg.Color(220, 220, 220))
    kuca(250, 130,  9, pg.Color("white"))
    kuca(350, 160, 10, (255,255,150))
    kuca( 50, 150, 10, pg.Color("khaki"))

.. activecode:: PyGame__drawing_house_scalable1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask: 
    :includexsrc: src\PyGame\1_Drawing\6_Scalable\house2D_detailed_scalable1.py
   
    prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno

    def kuca(x, y, a, boja_zidova):
        pg.draw.polygon(prozor, pg.Color("red"), [(x, y), (x + ???*a, y - ???*a), (x+14*a, y)]) # krov
        pg.draw.rect(prozor, boja_zidova,       (x,       y,      14*a, 10*a)) # kuca
        pg.draw.rect(prozor, pg.Color("brown"), (x + ???, y + ???, 3*a,  3*a)) # levi prozor
        pg.draw.rect(prozor, pg.Color("brown"), (x + ???, y + ???, ???,  ???)) # desni prozor
        pg.draw.rect(prozor, pg.Color("brown"), (x + ???, y + ???, ???,  ???)) # vrata
        
    kuca(150,  90, 10, (220, 220, 220))
    kuca(220, 130, 10, pg.Color("white"))
    kuca(350, 160, 10, (255, 255, 150))
    kuca( 50, 150, 10, pg.Color("khaki"))

Nakon što ste uspešno izmenili funkciju *kuca*, isprobajte razne rasporede, boje i veličine kuća, na primer ovaj ispod, ili neki koji sami izaberete:

.. code::

    kuca(278, 110, 1, (211, 207, 169))
    kuca(231, 119, 2, (217, 211, 164))
    kuca(174, 130, 3, (228, 221, 152))
    kuca(112, 142, 4, (231, 222, 150))
    kuca( 18, 160, 6, (240, 230, 140))
