Crtanje mnogouglova pomoću petlji
---------------------------------

Podsetimo se primera programa koji crta ogradu:

.. activecode:: PyGame_loops_fence_fixed
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7b_Loops_polygons\fence_fixed.py

Kao što smo u međuvremenu naučili, crtanje svake pritke posebnom naredbom nije najbolji način da se nacrta ovaj crtež. Fleksibilniji program bi se dobio kada bismo pritke crtali u petlji. Pogledajmo zato kako treba da crtamo mnogougao (pritka je pretstavljena petouglom), da bi bilo jednostavno nacrtati isti taj mnogougao i na drugim mestima.

Svakako je korisno da se uvede glavna tačka (sidro), u odnosu na koju bi bila izražena sva temena mnogougla. U slučaju ograde, temena prve pritke su [(20, 80), (30, 70), (40, 80), (40, 270), (20, 270)]. Možemo da izaberemo prvu navedenu tačku (20, 80) za sidro, a ostala temena da izrazimo pomoću koordinata prve tačke. Tako dobijamo da su temena jedne pritke [(x, y), (x+10, y-10), (x+20, y), (x+20, y+190), (x, y+190)]. Zadavanjem *x* = 20, *y* = 80 dobijamo koordinate prve pritke u ogradi, a povećavanjem *x* za po 40 možemo da dobijemo i ostale pritke.

.. code:: 

    y = 80
    for x in range(20, 300, 40):
        pg.draw.polygon(prozor, pg.Color('brown'), [(x, y), (x + 10, y-10), (x + 20, y), (x + 20, y+190), (x, y+190)])

Pošto su sve pritke na istoj visini, *y* koordinata sidra se ne menja pa ne moramo ni da je uvodimo (uvođenje *y* koordinate bi nam bilo potrebno kada bi neke pritke bile iznad drugih). To znači da u ovom slučaju prethodni kod možemo da napišemo i nešto jednostavnije.

.. code:: 

    for x in range(20, 300, 40):
        pg.draw.polygon(prozor, pg.Color('brown'), [(x, 80), (x + 10, 70), (x + 20, 80), (x + 20, 270), (x, 270)])

Moguće su razne varijante ove osnovne ideje. Na primer, ako na početku formiramo listu temena mnogougla (prve pritke), možemo da formiramo listu pomerenih temena na nekoliko načina.

Možemo da izračunamo koordinate pomerenih temena u dodatnoj petlji:

.. code::

    pritka = [(0, 0), (10, -10), (20, 0), (20, 190), (0, 190)]
    y0 = 80
    for x0 in range(20, 300, 40):
        pomerena_temena = []
        for x, y in temena:
            pomerena_temena.append((x+x0, y+y0))
        pg.draw.polygon(prozor, boja, pomerena_temena)

.. commented out

    Možemo da koristimo sažeto zadavanje liste za pomereni mnogougao koji crtamo:

    .. code:: 

        y0 = 80
        pritka = [(0, 0), (10, -10), (20, 0), (20, 190), (0, 190)]
        for x0 in range(20, 300, 40):
            pg.draw.polygon(prozor, pg.Color('brown'), [(x + x0, y + y0) for (x,y) in pritka])

Možemo da uvedemo funkciju za crtanje zadatog mnogougla na zadatom mestu, pa da listu pomerenih temena formiramo u funkciji:

.. code::

    def crtaj_mnogougao(temena, boja, x0, y0):
        pomerena_temena = []
        for x, y in temena:
            pomerena_temena.append((x+x0, y+y0))
        pg.draw.polygon(prozor, boja, pomerena_temena)

    pritka = [(0, 0), (10, -10), (20, 0), (20, 190), (0, 190)]
    for x0 in range(20, 300, 40):
        crtaj_mnogougao(pritka, pg.Color('brown'), x0, 80)

.. commented out

    Isto to koristeći sažeto zadavanje liste:

    .. code::

        def crtaj_mnogougao(temena, boja, x0, y0):
            pomerena_temena = [(x+x0, y+y0) for x, y in temena]
            pg.draw.polygon(prozor, boja, pomerena_temena)

        pritka = [(0, 0), (10, -10), (20, 0), (20, 190), (0, 190)]
        for x0 in range(20, 300, 40):
            crtaj_mnogougao(pritka, pg.Color('brown'), x0, 80)


Svaki od ova dva načina može da zameni sedam poziva funkcije *pg.draw.polygon* iz datog početnog primera, i svaki od njih je bolji nego crtanje pritki zasebnim naredbama. Upotreba funkcije daje nešto duži kod, ali ima tu prednost da se potpuno ista funkcija može bez izmene upotrebiti za crtanje bilo kog mnogougla na novoj poziciji.

Isprobajte jednu ili obe predložene izmene u programu gore, a zatim upotrebite neki od ovih načina da rešite sledeće zadatke.

        
Zadaci za vežbu
'''''''''''''''

.. questionnote::

    **Zadatak - osmouglovi** 
    
    Napisati program koji ctra osmouglove kao u primeru (kliknite na dugme "Prikaži primer").

Funkcija za crtanje mnogougla je slična prethodnoj. Razlika je samo u tome što se u njoj funkcija *pg.draw.polygon* poziva dva puta: jednom za unutrašnjost mnogougla, a drugi put za ivice.

Date su i koordinate temena osmougla, ostalo je da se doda poziv funkcije za crtanje u dvostrukoj petlji. I *x* i *y* startuju od nule i povećava ju se za po 48 (48 je "visina" i "širina" osmougla).
    
.. activecode:: PyGame_loops_octagons
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7b_Loops_polygons\octagons.py
    
    def crtaj_uokviren_mnogougao(temena, boja, boja_okvir, x0, y0):
        pomerena_temena = []
        for x, y in temena:
            pomerena_temena.append((x+x0, y+y0))
        pg.draw.polygon(prozor, boja, pomerena_temena)
        pg.draw.polygon(prozor, boja_okvir, pomerena_temena, 2)
    
    osmougao = [(14, 0), (34, 0), (48, 14), (48, 34), (34, 48), (14, 48), (0, 34), (0, 14)]
    # dovrsite
    


.. questionnote::

    **Zadatak - Strelice**

    Dopunite sledeći program tako da crta zadatu sliku (sliku možete da vidite klikom na dugme "Prikaži primer"). 

Na slici se pojavljuju bele strelice usmerene na levo i crne, usmerene na desno. Kako crne i bele strelice zajedno potpuno pokrivaju sliku, primetite da je dovoljno nacrtati samo crne strelice (na beloj pozadini).

.. activecode:: PyGame_loops_arrows
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7b_Loops_polygons\arrows.py
   
    strelica = [(0, 10), (40, 10), (40, 0), (60, 20), (40, 40), (40, 30), (0, 30)]
    prozor.fill(pg.Color("white"))
    ??? # dovrsite


.. questionnote::

    **Zadatak - krdo žirafa**

    Date su koordinate temena mnogougla koji predstavlja žirafu. Dovršite program tako da (koristeći funkciju *crtaj_mnogougao*) iscrtava nekoliko žirafa. Listu položaja žirafe napravite po želji.


.. activecode:: PyGame_loops_herd
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src\PyGame\1_Drawing\7b_Loops_polygons\giraffe_herd.py
