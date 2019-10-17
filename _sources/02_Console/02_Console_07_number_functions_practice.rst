Matematičke funkcije - vežbanje
===============================

Provežbajmo upotrebu matematičkih funkcija koje smo naučili.


.. questionnote::
    
    **Zadatak - reklamni paketi:** 
    
    Jovan deli reklamne pakete u kojima se nalazi po jedan kalendar, privezak za ključeve i hemijska olovka. Napisati program koji učitava koliko Jovan ima kalendara, privezaka i olovaka, a zatim ispisuje koliko reklamnih paketa može da napravi.

Iskoristite jednu od matematičkih funkcija koje ste naučili i dovršite program.

.. activecode:: console__mathfunc_promo_material

    kalendara = int(input("Koliko ima kalendara?"))
    privezaka = int(input("Koliko ima privezaka?"))
    olovaka = int(input("Koliko ima olovaka?"))
    cega_je_najmanje = 0 # dopunite ovu naredbu
    print("Može da se napravi", cega_je_najmanje, "paketa.")
            

.. questionnote::

    **Zadatak - limunada:** 
    
    Grupa ljudi polazi na put i Dara je napravila limunadu za sve. Napisati program koji učitava koliko litara limunade je Dara napravila (kao realan broj), a zatim ispisuje koliko flašica od pola litra može da se napuni sa toliko limunade i koliko je ukupno flašica potrebno za svu limunadu (ova dva broja mogu da se razlikuju najviše za jedan).
    
  
.. activecode:: console__mathfunc_lemonade

.. reveal:: console__mathfunc_lemonade_reveal
   :showtitle: Prikaži pomoć
   :hidetitle: Sakrij pomoć
   
   Da biste dovršili ovaj program, koristite neke od funkcija za zaokruživanje.
   
   .. activecode:: console__mathfunc_lemonade_solution
   
        litara = float(input())
        punih_flasica = 0 # dopunite ovu naredbu
        ukupno_flasica = 0 # dopunite ovu naredbu
        print("Može da se napuni", punih_flasica, "flašica.")
        print("Potrebno je ukupno", ukupno_flasica, "flašica.")



.. questionnote::

    **Zadatak - utakmica:** 
    
    Šest drugara se dogovorilo da se nađu na igralištu u određeno vreme i odigraju utakmicu. Napisati program koji učitava vreme kašnjenja svakog od igrača u minutima (kao cele brojeve), a ispisuje sa koliko minuta zakašnjenja je utakmica mogla da počne.
    
.. activecode:: console__mathfunc_late_game

.. reveal:: console__mathfunc_late_game_reveal
   :showtitle: Prikaži pomoć
   :hidetitle: Sakrij pomoć
   
   Jedno od mogućih rešenja je delimično napisano u nastavku. Pokušajte da ga dovršite.
   
   .. activecode:: console__mathfunc_late_game_help

        t1 = int(input("Koliko minuta je kasnio prvi: "))
        # ucitajte ostale podatke na isti nacin
        kasnjenje_utakmice = 0 # dopunite ovu naredbu
        print("Utakmica je mogla da počne sa", kasnjenje_utakmice, "minuta zakašnjenja.")

.. commented out

   .. activecode:: console__mathfunc_late_game_solution

        t1 = int(input("Koliko minuta je kasnio prvi: "))
        t2 = int(input("Koliko minuta je kasnio drugi: "))
        t3 = int(input("Koliko minuta je kasnio treći: "))
        t4 = int(input("Koliko minuta je kasnio četvrti: "))
        t5 = int(input("Koliko minuta je kasnio peti: "))
        t6 = int(input("Koliko minuta je kasnio šesti: "))
        kasnjenje_utakmice = 0 # dopunite ovu naredbu
        print("Utakmica je mogla da počne sa", kasnjenje_utakmice, "minuta zakašnjenja.")


.. questionnote::

    **Zadatak - dva autobusa:** 
    
    Marko i Goran putuju istim autoputem u dva različita autobusa i razgovaraju telefonom. Jedan od njih je upravo primetio oznaku :math:`x` kilometraže puta, a drugi :math:`y`. Napisati program koji učitava cele brojeve :math:`x` i :math:`y` i ispisuje koliko kilometara su Marko i Goran udaljeni jedan od drugog.

.. activecode:: console__mathfunc_buses

.. commented out
        
    .. reveal:: console__mathfunc_buses_reveal
       :showtitle: Prikaži pomoć
       :hidetitle: Sakrij pomoć
       
       Da biste dovršili sledeći program, koristite jednu od matematičkih funkcija koje ste naučili.
       
       .. activecode:: console__mathfunc_buses_solution

            x = int(input("Koliko je x: "))
            y = int(input("Koliko je y: "))
            rastojanje = 0 # dopunite ovu naredbu
            print("Rastojanje je", rastojanje)

    
.. questionnote::

    **Zadatak - Video lekcije**

    Kurs se sastoji iz nekoliko video lekcija koje sve jednako traju. Odlučili ste da tom kursu posvetitie svakog dana po 90 minuta i interesuje vas koliko dana će vam biti potrebno za ceo kurs. Napišite program koji učitava redom broj lekcija i trajanje jedne lekcije u minutima, a ispisuje potreban broj dana, zaokružen na najbliži ceo broj.
    
.. activecode:: console__mathfunc_videolessons
