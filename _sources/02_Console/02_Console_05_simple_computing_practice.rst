Programi sa računanjem - vežbanje
=================================

Do sada smo naučili kako da u programima učitavamo brojeve, kako da obavljamo računske operacije nad njima i kako da ispisujemo rezulatate.

Sada možemo da provežbamo naučeno na nekoliko jednostavnih matematičkih zadataka.

Zadaci bez učitavanja podataka
------------------------------

Primer
''''''

.. questionnote::

    **Primer - Proslava**

    Mira i Nikola organizuju proslavu. Zakupljeni prostor prima 100 osoba, Mira je do sada pozvala 43, a Nikola 28. 
    
    Napisati program koji izračunava koliko još mesta imaju na raspolaganju.
    
Zadatak možemo da rešimo ovako:

.. activecode:: console__computing_party1
    
    print(100-43-28)

ili ovako:

.. activecode:: console__computing_party2

    ukupno_mesta = 100
    pozvala_mira = 43
    pozvao_nikola = 28
    ostalo_mesta = ukupno_mesta - pozvala_mira - pozvao_nikola
    print(ostalo_mesta)


.. infonote::

    Iako vam to možda ovde izgleda nepotrebno, rešenje sa promenljivama vredi uvežbati. Programi koji koriste promenljive mogu da urade mnogo više nego oni bez promenljivih. Na primer, ako učitavamo vrednosti u program, promenljive su nam neophodne. Takođe, složenija računanja bi bila vrlo nepregledna kada ne bi mogla da se razlože na prostije korake, a za vrednosti međurezulata su nam opet potrebne promenljive.
    
    Ranije smo pomenuli da treba da se trudimo da promenljivama dajemo smislena imena. Računaru to nije bitno (on radi jednako dobro sa bilo kakvim imenima), ali kada izračunavamo nešto što nam je važno, korišćenje promenljivih sa smislenim imenima će nam pomoći da taj program razumemo i posle dužeg vremena. Takođe, takav program će lakše da razumeju i drugi ljudi koji ga budu čitali.


Zadaci za vežbu
'''''''''''''''

.. questionnote::

    **Zadatak - Kupovina za sve pare**
    
    Koliko stvari od 756 dinara može da se kupi za 5000 dinara i koliko novca će ostati, ako se kupi najviše što može?

Kraća (i manje jasna) verzija rešenja je

    .. activecode:: console__computing_divmod_sol1
        :passivecode: true
        
        print(5000 // 756, 5000 % 756)

Napišite jasnije rešenje koristeći promenljive.

.. activecode:: console__computing_divmod





.. questionnote::

    **Zadatak - Datum**

    Ako je danas 15-ti u mesecu i mesec ima 31 dan, koliko ima dana do 11-tog sledećeg meseca (u isto vreme)?

Vaš zadatak je da napišete rešenje u kome su polazne i izračunate vrednosti dodeljene promenljivama. Klikom na dugme "kratko rešenje" možete kao pomoć da vidite kratko rešenje.

.. reveal:: console__computing_divmod_reveal
    :showtitle: Kratko rešenje
    :hidetitle: Sakrij kratko rešenje

    .. activecode:: console__computing_buying3_simple_sol1
        :passivecode: true
        
        print(11+31-15)

.. activecode:: console__computing_date


.. commented out

    .. reveal:: console__computing_date_reveal
        :showtitle: Rešenje
        :hidetitle: Sakrij rešenje

        Program možemo da napišemo ovako:    

            .. activecode:: console__computing_date_sol1
                :passivecode: true
                
                print(11+31-15)

        ili ovako:

            .. activecode:: console__computing_date_sol2
                :passivecode: true
                
                danasnji_datum = 15
                krajnji_datum = 11
                br_dana_u_mesecu = 31
                br_dana_do_roka = krajnji_datum + br_dana_u_mesecu - danasnji_datum        
                print(br_dana_do_roka)

        Možete da iskopirate jedan ili drugi program u prostor predviđen za rešavanje i da ga tamo izvršite.


.. questionnote::

    **Zadatak - Kupovina 3 komada**

    Pera ima 2000 dinara i hoće da kupi 3 svetiljke za bicikl po 158 dinara. Koliko novca će da mu ostane?
    
Napišite program koji koristi promenljive za polazne i izračunate vrednosti.

.. activecode:: console__computing_buying3_simple

.. commented out

    Vaš zadatak je da napišete rešenje u kome su sve polazne i izračunate vrednosti dodeljene promenljivama. Klikom na dugme "kratko rešenje" možete kao pomoć da vidite kratko rešenje.

    .. reveal:: console__computing_divmod_reveal
        :showtitle: Kratko rešenje
        :hidetitle: Sakrij kratko rešenje

        .. activecode:: console__computing_buying3_simple_sol1
            :passivecode: true
            
            print(2000 - 3*158)

            
Zadaci sa učitavanjem podataka
------------------------------

Primer
''''''

.. questionnote::

    **Primer - Krečenje** 
    
    Filip se sprema da okreči plafon u jednoj prostoriji. Da bi zano koliko boje da kupi, potrebno mu je da zna dimenzije prostorije i koliko kvadratnih metara pokriva jedan kilogram boje. Napisati program koji učitava redom dužinu sobe, širinu sobe, površinu koji pokriva jedan kilogram boje, a ispisuje potreban broj kilograma boje.

Rešenje:

.. activecode:: console__computing_painting

    duzina = float(input("Unesite dužinu sobe: "))
    sirina = float(input("Unesite širinu sobe: "))
    pov_po_kg = float(input("Unesite površinu koju pokriva 1 kg boje: "))
    potrebno_kg = duzina * sirina / pov_po_kg
    print("Potrebno je", potrebno_kg, "kg boje")


Zadaci za vežbu
'''''''''''''''

.. questionnote::

    **Zadatak - Zečevi** 
    
    Populacija zečeva se na jednom ostrvu svake godine udvostručava. Napisati program koji učitava sadašnji broj zečeva na ostrvu i broj godina, a ispisuje koliko bi zečeva bilo na ostrvu za zadati broj godina ako nastave da se razmnožavaju istim tempom.

.. activecode:: console__computing_rabbits

.. commented out

    .. activecode:: console__computing_rabbits

        br_zeceva_sada = int(input("Unesite sadašnji broj zečeva: "))
        br_godina = int(input("Unesite broj godina: "))
        br_zeceva_posle = br_zeceva_sada * (2 ** br_godina)
        print("Broj zečeva bi porastao na", br_zeceva_posle)

    Primetimo da zagrade u izrazu ``br_zeceva_sada * (2 ** br_godina)`` nisu bile neophodne (program bi isto radio i bez njih). Zagrade su ddoate samo radi bolje čitljivosti programa.



.. questionnote::

    **Zadatak - Kupovina auta**

    Dragan kupuje auto na rate. Napisati program koji redom učitava cenu iz ugovora, visinu jedne rate i broj rata, a ispisuje koliko će Dragan ukupno platiti više od cene iz ugovora.
    
.. activecode:: console__computing_buying_car
