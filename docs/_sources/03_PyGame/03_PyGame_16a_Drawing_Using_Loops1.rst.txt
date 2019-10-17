Izrada crteža pomoću petlji
---------------------------

Razmotrimo sledeći zadatak: neka je potrebno nacrtati 6 krugova, kao na ovoj slici:

.. image:: ../../_images/PyGame/target.png
   :width: 300px
   :align: center 

Gledajući u sliku možemo da pretpostavimo (a moglo je da bude i rečeno u postavci) da su krugovi jednako razmaknuti. Ovo znači da je razlika poluprečnika svaka dva susedna kruga ista.

Veličinu krugova biramo tako da budu što veći, ali da mogu da stanu u dati prostor za crtanje od 300x300 piksela. Pošto je širina prozora 300 piksela, poluprečnik najvećeg kruga je 150. Kao razliku poluprečnika dva susedna kruga možemo da uzmemo :math:`{150 \over 6} = 25`. Tako dobijamo poluprečnike 25, 50, 75, 100, 125, 150.

Na osnovu izračunatih vrednosti, mogli bismo da napišemo ovakav program:

.. activecode:: PyGame_loop__target_fixed
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Examples\circles_target_fixed.py

Zamislimo da smo posle ovoga dobili novi zadatak da napravimo isti takav crtež, ali sa 5 krugova. Ovo je vrlo mala promena, zar ne? Trebalo bi da možemo da iskoristimo nešto od prethodno rešenog zadatka.

Kada započnemo rad na crtežu od 5 krugova, vidimo da vrlo malo od prethodnog programa možemo da iskoristimo. U stvari, možemo da iskoristimo samo ideju, a veličine krugova treba da izračunamo ispočetka.

Da smo program pisali drugačije, prilagođavanje bi bilo mnogo jednostavnije. Mogli smo na primer da broj krugova upišemo u promenljivu, a zatim da u svim potrebnim računanjima koristimo tu promeljivu. Taj program bi izgledao ovako:

.. activecode:: PyGame_loop__target_flexible
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Examples\circles_target_flexible.py

U ovom programu je dovoljno da se izmeni samo jedan broj, pa da on crta bilo koji zadati broj krugova.

Kao što smo već pomenuli, kod mnogih crteža postoji neka pravilnost, kao što je simetrija ili neki deo koji se ponavlja (i mnoge druge, složenije pravilnosti). Ako shvatimo pravilnost na takvim crtežima i izrazimo je matematički, moći ćemo da je iskoristimo pri pisanju programa za crtanje takvih crteža, kao što smo uradili u prethodnom primeru. Na taj način dobijamo program koji je mnogo lakše izmeniti da bi se dobio neki drugi, sličan crtež. Kod crteža sa velikim brojem ponavljanja nekog dela (istovetnog ili malo izmenjenog), program koji koristi pravilnost će biti i dosta kraći.

.. infonote::

    Mnogi programi koje koriste milioni ljudi se stalno usavršavaju i dorađuju. Stalno se objavljuju nove verzije u kojima je nešto urađeno bolje. Prema tome, izmene programa su nešto potpuno normalno i nešto što se stalno dešava. Situacija je slična i sa programima koje sami pišemo. Kada napišemo neki program, lako može da se dogodi da se kasnije setimo nečega, zbog čega ćemo hteti da izmenimo deo programa koji je već napisan.
    
    Zato, kada pišemo programe, treba da imamo na umu mogućnost da će neko (moguće i mi sami) hteti da napravi neki sličan program i da će možda želeti da upotrebi naš program kao početnu verziju.

Pogledajmo još jedan primer kako možemo da iskoristimo pravilnosti na crtežu za pisanje fleksibilnijeg programa (programa koji je lakše prilagoditi malo drugačijoj nameni).

Primer - antena
'''''''''''''''

Ranije smo već imali program koji crta ovakvu antenu. Sada je program napisan tako da nije suviše teško izmeniti broj poprečnih segmenata, razmak između njih, razliku dužina uzastopnih segmenata i slično.

.. activecode:: PyGame_loop__antenna
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Examples\antenna1.py

Deo programa koji crta poprečne segmente antene je mogao da bude napisan i ovako:

.. code::

    for i in range(6):
        pg.draw.line(prozor, pg.Color('darkgray'), (120 - 10 * i,  75 + 25 * i), (180 +  10 * i,  75 + 25 * i), 1 + i//2)

Ovako napisan program bi bio nešto kraći, ali prvi je jasniji, tako da svaki ima svoje prednosti. Istaknimo samo da su oba ova programa bolja od direktnog crtanja 6 linija za poprečne segmente (kao što smo to radili raije). Kada bi se ovaj deo programa sastojao od šest poziva funkcije za crtanje linije, bilo bi teže izmeniti i prilagoditi program crtanju drugačije antene.

Pravilno raspoređeni brojevi
''''''''''''''''''''''''''''

U oba prethodna primera bilo je potrebno da nabrojimo neki niz ili nizove pravilno raspoređenih brojeva. U zadatku sa krugovima to su bili brojevi 25, 50, 75, 100, 125, 150 (poluprečnici krugova), a u zadatku sa antenom bile su nam potrebne čak četiri serije brojeva - *x* i *y* koordinate levih i desnih krajeva poprečnih segmenata antene. Konkretno, ti brojevi su:

- *x* koordinate levih krajeva: 120, 110, 100, 90, 80, 70
- *y* koordinate levih krajeva: 75, 100, 125, 150, 175, 200
- *x* koordinate desnih krajeva: 180, 190, 200, 210, 220, 230
- *y* koordinate desnih krajeva: 75, 100, 125, 150, 175, 200

Videli smo da postoje različiti načini da dobijemo potrebne vrednosti. Na primer, u zadatku sa koncentričnim krugovima, vrednosti 25, 50, 75, 100, 125, 150 mogli smo da dobijemo na bilo koji od sledećih (jednako dobrih) načina:

..  code::

    for r in range(25, 151, 25):
        pg.draw.circle(prozor, pg.Color("red"), centar, r, 2)

..  code::

    for i in range(br_krugova):
        pg.draw.circle(prozor, pg.Color("red"), centar, round(25 + i * 25), 2)

..  code::

    r = 25
    for _ in range(br_krugova):
        pg.draw.circle(prozor, pg.Color("red"), centar, r, 2)
        r += 25

U opštem slučaju, ako treba dobiti seriju vrednosti *a*, *a+d*, *a+2d*, ... *a+(n-1)d*, prethodna tri načina možemo da koristimo ovako:

..  code::

    for x in range(a, a + n*d, d):
        print(x)

..  code::

    for i in range(n):
        print(a+i*d)

..  code::

    x = a
    for _ in range(n):
        print(x)
        x += d


Videćemo da se veliki broj zadataka sa crtanjem pravilno raspoređenih oblika može rešiti primenom ovakvih petlji.

Naglasimo još i da funkcija ``range`` sa korakom (sa tri argumenta) prima obavezno celobrojne argumente, pa u situacijama kada korak nije
celobrojan njeno korišćenje nije moguće.

Kada nam je potrebno (kao u zadatku sa antenom) da napravimo nekoliko serija u jednoj petlji, prvi način je manje pogodan, pa treba birati neki od ostalih načina.

Sledeća pitanja će vam pomoći da utvrdite znanje o formiranju serija pravilno raspoređenih brojeva.

.. dragndrop:: pygame__loop_quiz_match_series
    :feedback: Pokušajte ponovo!
    :match_1: 100, 200, 300, 400, 500|||for i in range(100, 600, 100)
    :match_2: 100, 300, 500|||for i in range(100, 601, 200)
    :match_3: 100, 200, 300, 400, 500, 600|||for i in range(100, 601, 100)
    :match_4: 200, 300, 400, 500, 600|||for i in range(200, 601, 100)

    Upari niz brojeva sa petljom koja ga generiše.
     
.. dragndrop:: pygame__loop_quiz_match_series2
    :feedback: Pokušajte ponovo!
    :match_1: 100, 150, 200, 250, 300|||x = 100 + i*50
    :match_2: 50, 150, 250, 350, 450|||x = 50 + i*100
    :match_3: 0, 100, 200, 300, 400|||x = i*100
    :match_4: 100, 200, 300, 400, 500|||x = 100+i*100

    Upari brojeve koji se dobijaju sa izrazom u petlji "for i in range(5):" koji ih generiše.
     

.. mchoice:: pygame__loop_quiz_range01
    :answer_a: x = 25 * i + 50
    :answer_b: x = (25 + i) * 50
    :answer_c: x = 25 * 2*i+1
    :answer_d: x = 25 + 50 * i
    :correct: d
    :feedback_a: Ne.
    :feedback_b: Ne.
    :feedback_c: Ne.
    :feedback_d: Tačno!
    
    Koji izraz treba koristiti u petlji 
    
    .. code::
    
        for i in range(19):
            x = ???
            ...
            
    da bi *x* imalo iste vrednosti kao u petlji

    .. code::
    
        for x in range(25, 500, 50):
            ...
            
Slede zadaci za vežbu.

Merdevine
'''''''''

Izmenite program tako da se prečage merdevina crtaju u petlji.

.. activecode:: PyGame_loop__ladder
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\ladder.py

    prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno

    pg.draw.line(prozor, pg.Color("brown"), (100, 10), (100, visina - 10), 10)    # leva strana
    pg.draw.line(prozor, pg.Color("brown"), (200, 10), (200, visina - 10), 10)    # desna strana

    # ovaj deo prepraviti
    pg.draw.line(prozor, pg.Color("brown"), (100,  50), (200, 50), 10) # precaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 100), (200, 100), 10) # precaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 150), (200, 150), 10) # precaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 200), (200, 200), 10) # precaga
    pg.draw.line(prozor, pg.Color("brown"), (100, 250), (200, 250), 10) # precaga

   
.. reveal:: PyGame_loop__ladder_reveal
    :showtitle: Pomoć
    :hidetitle: Sakrij pomoć

    Umesto 5 naredbi za crtanje linija, možete da upotrebite petlju sledećeg oblika:
    
    .. code::
    
        for y in ???:
            pg.draw.line(prozor, pg.Color("brown"), (100, y), (200, y), 10)
            
    Da biste na pravi način kompletirali petlju, treba da odgovorite na sledeće pitanje:
    
    .. mchoice:: pygame__loop_quiz_range1
        :answer_a: range(0, 50, 250)
        :answer_b: range(250, 50)
        :answer_c: range(50, 251, 50)
        :answer_d: range(50, 250, 50)
        :correct: c
        :feedback_a: Ne, za taj opseg prvi broj nije odgovarajući.
        :feedback_b: Ne, pokušajte ponovo.
        :feedback_c: Tačno!
        :feedback_d: Ne, za taj opseg poslednji broj nije odgovarajući.
        
        Koji od ponuđenih opsega daje vrednosti 50, 100, 150, 200, 250?


.. commented out

    .. reveal:: PyGame_loop__ladder_reveal
        :showtitle: Prikaži rešenje
        :hidetitle: Sakrij rešenje
        
        Jedno moguće rešenje je:
        
        .. activecode:: PyGame_loop__ladder_solution
            :nocodelens:
            :enablecopy:
            :modaloutput:
            :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\ladder.py
          
Drveće
''''''

Izmenite program tako da se u tri prolaska kroz petlju crta po jedno drvo.

.. activecode:: PyGame_loop__trees
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\trees.py
   
    prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno

    pg.draw.rect(prozor, pg.Color("brown"), (40, 180, 20, 100))        # prvo stablo
    pg.draw.ellipse(prozor, pg.Color("darkgreen"), (10, 50, 80, 150))  # prva krosnja
    pg.draw.rect(prozor, pg.Color("brown"), (140, 180, 20, 100))       # drugo stablo
    pg.draw.ellipse(prozor, pg.Color("darkgreen"), (110, 50, 80, 150)) # druga krosnja
    pg.draw.rect(prozor, pg.Color("brown"), (240, 180, 20, 100))       # trece stablo
    pg.draw.ellipse(prozor, pg.Color("darkgreen"), (210, 50, 80, 150)) # treca krosnja

.. reveal:: PyGame_loop__trees_reveal
    :showtitle: Prikaži rešenje
    :hidetitle: Sakrij rešenje

    Program može da izgleda ovako:
    
    .. activecode:: PyGame_loop__trees_solution
        :nocodelens:
        :enablecopy:
        :modaloutput:
        :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\trees.py

        prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno


        for i in range(3):
            pg.draw.rect(prozor, pg.Color("brown"), (???, 180, 20, 100))        # stablo
            pg.draw.ellipse(prozor, pg.Color("darkgreen"), (???, 50, 80, 150))  # krosnja

    
    pri čemu umesto upitnika treba staviti odgovarajuće izraze za *x* koordinatu. Kada *i* uzima redom vrednosti 0, 1, 2, potrebno je da izraz u prvoj naredbi uzima redom vrednosti 40, 140, 240, a u drugoj 10, 110, 210.
    
.. commented out::    

        pg.draw.rect(prozor, pg.Color("brown"), (40, 180, 20, 100))        # prvo stablo
        pg.draw.ellipse(prozor, pg.Color("darkgreen"), (10, 50, 80, 150))  # prva krosnja
        pg.draw.rect(prozor, pg.Color("brown"), (140, 180, 20, 100))       # drugo stablo
        pg.draw.ellipse(prozor, pg.Color("darkgreen"), (110, 50, 80, 150)) # druga krosnja
        pg.draw.rect(prozor, pg.Color("brown"), (240, 180, 20, 100))       # trece stablo
        pg.draw.ellipse(prozor, pg.Color("darkgreen"), (210, 50, 80, 150)) # treca krosnja
        
        
Rešetka
'''''''

Izmenite program tako da se u jednoj petlji isrtavaju uspravne linije, a nakon toga u drugoj petlji vodoravne linije.

.. activecode:: PyGame_loop__grid
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\grid.py
    
    pg.draw.line(prozor, pg.Color("black"), (10, 10), (10, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (30, 10), (30, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (50, 10), (50, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (70, 10), (70, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (90, 10), (90, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (110, 10), (110, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (130, 10), (130, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (150, 10), (150, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (170, 10), (170, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (190, 10), (190, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (210, 10), (210, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (230, 10), (230, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (250, 10), (250, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (270, 10), (270, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (290, 10), (290, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (310, 10), (310, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (330, 10), (330, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (350, 10), (350, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (370, 10), (370, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (390, 10), (390, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (410, 10), (410, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (430, 10), (430, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (450, 10), (450, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (470, 10), (470, visina - 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (490, 10), (490, visina - 10), 1)
    
    pg.draw.line(prozor, pg.Color("black"), (10, 10), (sirina - 10, 10), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 30), (sirina - 10, 30), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 50), (sirina - 10, 50), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 70), (sirina - 10, 70), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 90), (sirina - 10, 90), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 110), (sirina - 10, 110), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 130), (sirina - 10, 130), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 150), (sirina - 10, 150), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 170), (sirina - 10, 170), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 190), (sirina - 10, 190), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 210), (sirina - 10, 210), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 230), (sirina - 10, 230), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 250), (sirina - 10, 250), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 270), (sirina - 10, 270), 1)
    pg.draw.line(prozor, pg.Color("black"), (10, 290), (sirina - 10, 290), 1)

.. commented out::

    .. reveal:: PyGame_loop__grid_reveal
        :showtitle: Prikaži rešenje
        :hidetitle: Sakrij rešenje

        Jedno moguće rešenje je:
       
        .. activecode:: PyGame_loop__grid_solution
            :nocodelens:
            :enablecopy:
            :modaloutput:
            :includesrc: src\PyGame\1_Drawing\7a_UsingLoops\Tasks\grid.py
