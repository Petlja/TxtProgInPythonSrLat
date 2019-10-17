Očitavanje pozicije miša
------------------------

U PajGejmu postoji jednostavan način da saznamo, to jest očitamo trenutno stanje miša. Podaci koji nas često najviše interesuju su pozicija miša i pritisnuti tasteri. U ovoj lekciji ćemo koristiiti očitavnje pozicije miša, a u sledećoj tastere miša. Osim pozicije i pritisnutih tastera, postoje i druge informacije o mišu koje možemo da dobijemo, ali to ovde nećemo raditi. Zainteresovani mogu da nađu više detalja na primer  `ovde <https://www.pygame.org/docs/ref/mouse.html>`__ .

Poziciju miša možemo dobiti pozivom funkcije ``pg.mouse.get_pos()``, koja vraća uređeni par koordinata tačke na kojoj se trenutno nalazi pokazivač miša. 

Kao što ćemo videti u primerima i zadacima koji slede, upotreba ove funkcije je vrlo jednostavna, a očitanu poziciju miša možemo dalje da koristimo na različite načine.

Primeri i zadaci
''''''''''''''''

.. questionnote::

    **Primer - leptir prati miša:** 
    
    U ovom primeru učitavamo dve slike leptira i prikazujemo ih naizmenično, kao što smo to radili u animacijama. Novo je to da se mesto na kome prikazujemo leptira određuje na osnovu pozicije miša, koju smo dobili pomoću funkcije *pg.mouse.get_pos()*.

.. image:: ../../_images/butterfly1.png
   :width: 50px
.. image:: ../../_images/butterfly2.png
   :width: 50px

.. activecode:: PyGame__interact_butterfly1
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3a_Mouse_readpos/butterfly1.py

Verovatno ste primetili da kada brže pomerate miša, leptir malo kasni za njim. Ovo se dešava zato što se prikazuje samo 5 frejmova u sekundi, pa kašnjenje može bude i do 0.2 sekunde. 

Ovo kašnjenje se lako eliminiše tako što povećamo učestalost prikazivanja (prikazujemo veći broj frejmova u sekundi), međutim tada se slike smenjuju previše često i dejuje da leptir suviše brzo maše krilima. Rešenje je da povećamo učestalost prikazivanja, a da svaku sliku prikazujemo tokom više frejmova.

.. questionnote::

    **Zadatak - brzo kretanje, sporo mahanje:** Iskopirajte ovde prethodni program, a zatim ga izmenite tako da leptir ne kasni za mišem, ali da brzina mahanja krilima ostane ista.

**Pomoć:** da leptir ne bi kasnio, svakako nam treba više frejmova u sekundi, na primer *n* puta više. To znači da se funkcija *nov_frejm* poziva *n* puta češće nego ranije. Da bi se pri tome zadržala ista brzina mahanja krilima, potrebno je da se svaka slika prikazuje *n* puta duže, to jest tokom *n* uzastopnih frejmova.
 
.. activecode:: PyGame__interact_butterfly2
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3a_Mouse_readpos/butterfly2.py

.. questionnote::

    **Zadatak - prema mišu:** Napišite program u kome se zelena loptica kreće ka mišu, kao u primeru (dugme "Prikaži primer"). 
    
**Pomoć:** U ovom zadatku je ključno kako se menjaju koordinate :math:`(x, y)` centra loptice. U situaciji kao na slici, želimo da *x* povećamo za *dx*, a *y* da povećamo za *dy*. U zavisnosti od toga kako želimo da se loptica kreće, veličine *dx*, *dy* mogu da se izračunaju na razne načine. Jedan jednostavan način je da izaberemo :math:`dx = {1 \over 10} (xm - x), dy = {1 \over 10} (ym - y)`.

.. image:: ../../_images/PyGame/towards_mouse.png
   :width: 300px   
   :align: center     

.. activecode:: PyGame__interact_towards_mouse
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3a_Mouse_readpos/towards_mouse.py



.. questionnote::

    **Zadatak - prema mišu sa tragom:** Iskopirajte prethodni program, a zatim ga prepravite tako da loptica ostavlja sivi trag, kao u primeru (dugme "Prikaži primer"). 
    
**Pomoć:** Kretanje loptice je isto kao u prethodnom primeru. Da bismo napravili trag, potrebno je pamtiti listu nekoliko (mi smo koristili 20) prethodnih položaja loptice. 

Pri izračunavanju novog stanja, na listu dodajemo najnoviji položaj, a ako je lista postala preduga, izbacujemo najstariji položaj. 

Pri crtanju traga, za svaki krug koristimo boju  *(nijansa, nijansa, nijansa)*, gde je nijansa pre petlje jednaka 255 (bela), a u petlji se smanjuje za određenu vrednost, tako da u poslednjem prolazu kroz petlju postane nula, ili što bliže nuli (crna).

Dakle, ako se lista na primer zove *trag*, u vašem programu treba da se pojave ovakve ili slične naredbe:

.. code::

    trag = []
    ...
    
    def nov_frejm():
        
        ...
        trag.append((x, y))
        ...
        if ...
            trag = trag[1:]


.. activecode:: PyGame__interact_towards_mouse_with_trace
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3a_Mouse_readpos/towards_mouse_with_trace.py

~~~~

Na kraju, možete da isprobate sledeća dva programa i da se poigrate sa njima. 

Da bi se napravili ovakvi programi, pored ovde prikazanih tehnika programiranja potrebno je i malo znanja fizike (elastična sila, drugi Njutnov zakon) i matematike (Pitagorina teorema). Pogledajte programe, bez obaveze da ih potpuno razumete. Ako želite, probajte da malo izmenite neke konstante, pa vidite kako to utiče na rad programa.

.. questionnote::

    **Primer: Jo-jo**
    
.. activecode:: PyGame__interact_yoyo
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3a_Mouse_readpos/yoyo.py

.. questionnote::

    **Primer: Oči** 

Ovaj program takođe zahteva malo više znanja matematike, pa se nećemo upuštati u detalje. Ako vas interesuje kako ovaj program radi, a matematika vam dobro ide, pokušajte da razumete detalje uz nečiju pomoć.

.. activecode:: PyGame__interact_eyes
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3a_Mouse_readpos/eyes.py