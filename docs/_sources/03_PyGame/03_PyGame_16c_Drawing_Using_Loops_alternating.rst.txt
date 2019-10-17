Izrada složenijih crteža pomoću petlji
--------------------------------------

Pravilnost koju želimo da iskoristimo na crtežima može da bude i nešto složenija. Evo nekih primera:

.. image:: ../../_images/PyGame/repeat_alternating.png 
   :width: 800px
   :align: center 

U svim ovim slučajevima pravilnost i dalje postoji i može da se iskoristi pri pisanju programa. Osim toga, možemo da primetimo da primeri sa slike svi imaju nešto zajedničko, a to je da se naizmenično pojavljjuju dva pravila. Na primer, na crtežu sa ciglama prvi red počinje celom ciglom, drugi polovinom cigle, treći opet celom i tako dalje. Slično tome, na crtežu zgrade se naizimenično pojavljuju osvetljeni i zatamnjeni prozori.

Zbog naizmeničnog pojavljivanja dva pravila na crtežima, i programi koji ih crtaju će imati nekih sličnosti. Pogledajmo primere.

Primer - rajsferšlus
''''''''''''''''''''

Da bismo nacrtali ovakav rajsferšlus, linije ćemo svakako crtati u petlji. Sa crteža se vidi da je svaka sledeća linija za isti broj piksela niže od prethodne, tako da ne bi trebalo da bude problema sa računanjem :math:`y` koordinata. Nešto je teža situacija sa :math:`x` koordinatama, jer se one menjaju po malo složenijem pravilu.

Ovaj problem možemo da rešimo pomoću *if* naredbe u petlji. Nakon crtanja jedne linije, proveravamo koju od dve moguće vrednosti ima :math:`x` koordinata početka linije, pa ako ima prvu vrednost - dodeljujemo joj drugu i obrnuto. Evo kako to izgleda u programu:

.. activecode:: PyGame_drawing_loops_zipper1
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\zipper1.py

Druga mogućnost da rešimo problem sa :math:`x` koordinatama je da u jednom prolasku kroz petlju crtamo po dve linije, na primer ovako:

.. activecode:: PyGame_drawing_loops_zipper2
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\zipper2.py


Primer - Cigle
''''''''''''''

Već smo pomenuli da redovi cigala naizmenično počinju celom ciglom i polovinom cigle. Zato pri crtanju cigala možemo da iskoristimo iste dve ideje kao i u prethodnom primeru. 

Neka je dužina cigle označena sa :math:`a`, a njena visina sa :math:`h`. Celu ciglu na početku reda dobijamo tako što crtamo pravougaonik od tačke na datoj visini, sa :math:`x` koordinatom jednakom nuli. Polovinu cigle na početku reda možemo da dobijemo tako što nacrtamo celu ciglu pomerenu za :math:`a \over 2` ulevo, to jest tako što crtamo pravougaonik od tačke na istoj visini, ali sa :math:`x` koordinatom jednakom :code:`-a // 2`. Tako postižemo da se vidi samo desna polovina cigle. Ostaje da rešimo kada crtamo pomerenu ciglu a kada ne.

Jedno rešenje je da mesto početka reda cigala čuvamo u promenljivoj, nazovimo je *x_poc*. Posle svakog iscrtanog reda, proveravamo da li promenljiva *x_poc* ima vrednost nula ili :code:`-a // 2`. Kao i u prethodnom primeru, koju god od ove dve vrednosti promenljiva imala, dodelićemo joj onu drugu vrednost, da bi u sledećem redu crtanje cigala počelo drugačije.

Dovršite naredbe za dodeljivanje vrednosti promenljivoj *x_poc*.

.. activecode:: PyGame_drawing_loops_bricks1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\bricks1.py

    prozor.fill(pg.Color("red"))
    a_cigle, h_cigle = 80, 40
    x_poc = 0
    for y0 in range(0, visina, h_cigle): # Za svaki red cigala
        for x0 in range(x_poc, sirina, a_cigle): # Za svaku ciglu u redu
            pg.draw.rect(prozor, pg.Color("black"), (x0, y0, a_cigle, h_cigle), 1)
            
        if x_poc == ???: # dopunite
            x_poc = -a_cigle//2
        else:
            x_poc = ??? # dopunite

Druga ideja je da u svakom prolasku kroz dvostruku petlju crtramo ciglu koju smo crtali i u prvom rešenju, a osim nje i ciglu ispod i polu-levo od nje. Primetite da u tom slučaju petlja po *y0* ima dvostruko veći korak, jer unutrašnja petlja crta dva reda cigala.

Dovršite naredbe za crtanje pravougaonika u ovom programu.

.. activecode:: PyGame_drawing_loops_bricks2
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Examples\bricks2.py

    prozor.fill(pg.Color("red"))
    a_cigle, h_cigle = 80, 40
    for y0 in range(0, visina, 2 * h_cigle):
        for x0 in range(0, sirina, a_cigle):
            #crtamo prvu ciglu
            pg.draw.rect(???) # dopunite kao malopre
            
            # druga cigla je u sledecem redu, pomerena za pola sirine ulevo
            x1, y1 = x0 - a_cigle//2, y0 + h_cigle 
            pg.draw.rect(???) # dopunite crtanje druge cigle


Zadaci za vežbu
'''''''''''''''

.. questionnote::

    **Zadatak - šahovska tabla**

    Nacrtati šahovsku tablu preko celog prozora (polja table treba da budu veličine 50h50 piksela). Donje levo polje treba da bude tamne boje.

.. activecode:: PyGame_drawing_loops_chessboard
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Tasks\chessboard1.py
    
    # bojimo pozadinu prozora u sivo za svetla polja
    prozor.fill(pg.Color("gray"))   
    
    brojPolja = 8
    sirinaPolja = sirina / brojPolja
    visinaPolja = visina / brojPolja

    # prolazimo kroz sva polja
    for i in range(brojPolja):
        for j in range(brojPolja):
            # bojimo crna polja
            if (i + j) % 2 != 0:
            ... # dovrsite


.. questionnote::

    **Zadatak - Zgrada**

    Izmenite program tako da se prozori crtaju u dvostrukoj petlji.

Deo koji treba izmeniti, nakon izmene može da počinje ovako:

.. code::

    for y in range(5):     # sprat
        for x in range(2): # strana zgrade (0 - leva, 1 - desna)
            if (x+y) % 2 == 0:
                boja = ...


.. activecode:: PyGame_drawing_loops_building_alternating
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Tasks\building_alternating.py
    
    pg.draw.rect(prozor, pg.Color("darkgray"), (120, 50, 60, 140)) # zgrada

    # Ovaj deo izmeniti
    pg.draw.rect(prozor, pg.Color('yellow'), (130,  60, 15, 15))
    pg.draw.rect(prozor, pg.Color('black'), (155,  60, 15, 15))
    pg.draw.rect(prozor, pg.Color('black'), (130,  80, 15, 15))
    pg.draw.rect(prozor, pg.Color('yellow'), (155,  80, 15, 15))
    pg.draw.rect(prozor, pg.Color('yellow'), (130, 100, 15, 15))
    pg.draw.rect(prozor, pg.Color('black'), (155, 100, 15, 15))
    pg.draw.rect(prozor, pg.Color('black'), (130, 120, 15, 15))
    pg.draw.rect(prozor, pg.Color('yellow'), (155, 120, 15, 15))
    pg.draw.rect(prozor, pg.Color('yellow'), (130, 140, 15, 15))
    pg.draw.rect(prozor, pg.Color('black'), (155, 140, 15, 15))

    pg.draw.rect(prozor, pg.Color("black"),  (140, 160, 20, 30))   # kapija

~~~~

Ako sa svim ovim zadacima niste imali većih problema, pokušajte za kraj da rešite i jedan malo teži zadatak. 

.. questionnote::

    **Zadatak - izazov: Parket**

    Napišite program koji prikazuje parket (sliku parketa možete da vidite kada kliknete na dugme "Prikaži primer", a slika je ista kao na početku ove strane, desno). Cilj je, naravno, da se crtanje daščica parketa obavlja u višestrukoj petlji. Dimenzije daščice su 10h60, a boje su "goldenrod" i "brown".

Kostur programa ugrubo izgleda ovako:

.. code::

    for red ...
        for kol ...
            if ...
                for dascica in range(6):
                    pg.draw.rect(...)
            else:
                for dascica in range(6):
                    pg.draw.rect(...)

.. activecode:: PyGame_drawing_loops_parquet
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7c_Loops_alternating\Tasks\parquet.py
