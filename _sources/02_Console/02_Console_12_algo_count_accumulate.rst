Brojanje i sumiranje
====================

Vrlo je čest slučaj da nas iz kolekcije podataka interesuju samo neki. Ovde ćemo vežbati kako da prebrojimo i po potrebi saberemo podatke koji nas interesuju, odnosno koji ispunjavaju neki uslov.

Brojanje
--------

Program (algoritam) pomoću koga prebrojavamo elemente kolekcije koji ispunjavaju dati uslov u opštem obliku izgleda ovako:

.. code::

    br = 0
    for x in kolekcija:
        if (x ispunjava uslov):
            br += 1
    print(br)
    
.. infonote::

    Naredba ``x += a`` povećava vrednost promenljive *x* za *a*. To je u stvari skraćeni zapis naredbe :code:`x = x + a`, koja promenljivoj *x* dodeljuje vrednost *x + a*. 

    Naredba ``x -= a`` smanjuje vrednost promenljive *x* za *a*. To je skraćeni zapis naredbe :code:`x = x - a`, koja promenljivoj *x* dodeljuje vrednost *x - a*. 
    
U našem primeru, naredba *br += 1* povećava vrednost promenljive *br* za 1.

Primeri i zadaci
''''''''''''''''

.. questionnote::

    **Primer - sastanak:** 
    
    Vođa tima je ponudio dva termina za sastanak koji treba da se održi sutra. Svaki član tima je upisao u tabelu koji termin bi mu više odgovarao (1 za prvi termin, 2 za drugi). Ti podaci su prebačeni u prvi red programa.

    Dovršiti program - skriptu, tako da za date podatke o glasanju članova tima odgovara koliko ih je glasalo za prvi, a koliko za drugi termin.
    
.. activecode:: console__counting_meeting

    termini = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)
    
Možemo na primer da prebrojimo koliko članova tima je glasalo za prvi termin, a ostale da izračunamo na kraju.

.. activecode:: console__counting_meeting_sol1

    termini = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)

    br_prvi_termin = 0
    for t in termini:
        if t == 1:
            br_prvi_termin += 1
            
    br_drugi_termin = len(termini) - br_prvi_termin

    print('Za prvi termin je glasalo', br_prvi_termin, 'a za drugi', br_drugi_termin, 'članova tima.')

Drugi način je da brojimo uporedo glasove i za prvi i za drugi termin.

.. activecode:: console__counting_meeting_sol2

    termini = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)

    br_prvi_termin = 0
    br_drugi_termin = 0
    for t in termini:
        if t == 1:
            br_prvi_termin += 1
        if t == 2:
            br_drugi_termin += 1
    print('Za prvi termin je glasalo', br_prvi_termin, 'a za drugi', br_drugi_termin, 'članova tima.')

ili, ako pretpostavimo da su podaci "čisti", to jest da nema drugih vrednsoti osim 1 i 2:

.. activecode:: console__counting_meeting_sol3

    termini = (1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1)

    br_prvi_termin = 0
    br_drugi_termin = 0
    for t in termini:
        if t == 1:
            br_prvi_termin += 1
        else:
            br_drugi_termin += 1
            
    print('Za prvi termin je glasalo', br_prvi_termin, 'a za drugi', br_drugi_termin, 'članova tima.')

U slučaju da podaci nisu poznati unapred nego ih treba unositi, mogli bismo da napišemo ovakav program:

.. activecode:: console__counting_meeting_sol4

    n = int(input("Koliko članova tima je glasalo: "))
    br_prvi_termin = 0
    for i in range(n):
        t = int(input("Unesite jedan glas: "))
        if t == 1:
            br_prvi_termin += 1
            
    br_drugi_termin = n - br_prvi_termin
    print('Za prvi termin je glasalo', br_prvi_termin, 'a za drugi', br_drugi_termin, 'članova tima.')

Na početku ovog programa učitavamo broj glasova *n*, a zatim koristimo *for* petlju da *n* puta ponovimo učitavanje i brojanje jednog glasa.




.. questionnote::

    **Zadatak - testiranje:** 
    
    Nekoliko ljudi je rešavalo test poznavanja saobraćajnih propisa, što je uslov za izlazak na praktični deo ispita. Test se smatra položenim ako je je broj netačnih odgovora manji ili jednak 3. 
    
    Na početku programa - skripte su dati rezultati testiranja jedne grupe kandidata (broj netačnih odgovora za svaku osobu koja je rešavala test). Dovršite skriptu tako da ispisuje koliko kandidata je položilo test.

.. activecode:: console__counting_test

    netacnih = (2, 5, 1, 0, 4, 2, 7, 1)
    polozilo = 0

    # ovde dodajte naredbe koje nedostaju
    
    print(polozilo)
    
.. commented out
    
    polozilo = 0
    for x in netacnih:
        if x <= 3:
            polozilo += 1
    print(polozilo)



.. questionnote::

    **Zadatak - bazen** 
    
    Priprema se poseta bazenu za grupu dece. Svi koji su niži od 160 santimetara mogu da idu samo u manji u bazen. Organizatora interesuje koliko dece je niže od 160 santimetara, da bi mogao da planira grupe.

    Na početku programa su date visine dece. Dopuniti program tako da ispisuje broj dece niže od 160 santimetara.
    
.. activecode:: console__counting_swimmingpool

    visine = (160, 161, 174, 149, 153, 160, 158, 182, 144)
    
    


.. questionnote::

    **Zadatak - vlažnost** 
    
    U botaničkoj bašti se kod retkih i osetljivih vrsta jednom dnevno meri vlažnost zemljišta. Vlažnost se izražava brojem od 0 do 1, a smatra se da su uslovi za razvoj bialjaka dobri kada je vlažnost između 0.3 i 0.7 (uključujući i granice). 
    
    Na početku programa - skripte su date vlažnosti izmerene tokom nekog perioda. Dovršiti skriptu tako da ispisuje broj dana kada vlažnost nije bila dobra.

.. activecode:: console__counting_humidity

    vlaznosti = (0.2, 0.5, 0.61, 0.40, 0.72, 0.51, 0.43, 0.35, 0.28)
    


Sumiranje
---------

U jednoj velikoj grupi praktičnih problema do rezultata dolazimo tako što ga postepeno gradimo (nakupljamo) tokom prolaženja kroz podatke. Na primer, ako nam je potreban zbir nekih brojeva, do njega možemo da dođemo na ovaj uopšteni način:

.. code::

    zbir = 0
    for podatak in kolekcija:
        zbir += podatak
    print(zbir)

Kada nam treba zbir svih elemenata kolekcije, isti rezultat dobijamo i pozivom funkcije *sum*:

.. code::

    print(sum(kolekcija))

Postepeno formiranje rezultata ćemo koristiti kada nam od elemenata iz kolekcije trebaju samo neki, to jest oni koji ispunjavaju zadati uslov. U tom slučaju, postupak za računanje zbira bi uopšteno izgledao ovako:

.. code::

    zbir = 0
    for podatak in kolekcija:
        if (podatak ispunjava uslov):
            zbir += podatak
    print(zbir)

Da bismo dobili srednju vrednost podataka koji ispunjavaju neki uslov, potrebno je prebrojati i sabrati takve podatke, a onda njihov zbir podeliti njihovim brojem. U opštem slučaju to izgleda ovako:

.. code::

    zbir = 0
    brojac = 0
    for podatak in kolekcija:
        if (podatak ispunjava uslov):
            zbir += podatak
            brojac += 1
    print(zbir / brojac)

Napominjemo da se u Pajtonu zbir i srednja vrednost izabranih elemenata kolekcije može dobiti i na kraći i efikasniji način. Ovde smo se odlučili za navedeni način, jer on izgleda skoro isto kao u drugim programskim jezicima.

Primeri i zadaci
''''''''''''''''

.. questionnote::

    **Primer - Prosečan rezultat IQ testa:** 
    
    Dati su rezultati IQ testa za grupu ljudi. Rezultat -1 znači da osoba nije radila test. Dovršiti program tako da ispisuje srednju vrednost dobijenu na testiranju.

.. activecode:: console__accumulate_IQ

    iq_rezultati = (-1, 98, 115, -1, 83, 130, 101, 122, -1, 108)

Program možemo da napišemo ovako:

.. activecode:: console__accumulate_IQ_sol

    iq_rezultati = (-1, 98, 115, -1, 83, 130, 101, 122, -1, 108)
    broj_testiranih = 0
    zbir_rezultata = 0
    
    for rez in iq_rezultati:
        if rez != -1:
            zbir_rezultata += rez
            broj_testiranih += 1

    if broj_testiranih > 0:
        srednji_iq = zbir_rezultata / broj_testiranih
        print('Srednji IQ je', srednji_iq)
    else:
        print('Niko nije testiran.')


.. questionnote::

    **Zadatak - dežurstva:**  
    
    U preduzeću H svi zaposleni povremeno ostaju na dežurstvu. Norma za prethodni period je 20 sati dežurstva. Svaki sat dežurstva preko norme se plaća po posebnom cenovniku. Dat je broj sati dežurstva za svakog zaposlenog, a direktor želi da zna koliko je ukupno bilo sati dežurstva preko norme.
    
    Dovršiti program tako da ispisuje ukupan broj prekovremenih sati dežurstva.
    
Ako sto dobro rešili zadatak, za date podatke treba da dobijete rezultat 25, jer je :math:`(21-20)+(23-20)+(34-20)+(25-20)+(22-20)=25`.

.. activecode:: console__accumulate_overtime

    norma = 20
    radni_sati = (21, 23, 19, 34, 25, 22, 17)
    ukupno_preko = 0
    # dovrsite program
    
    print('Ukupan broj prekovremenih sati je', ukupno_preko)
    
.. commented out
    
    norma = 20
    radni_sati = (21, 23, 19, 34, 25, 22, 17)
    ukupno_preko = 0
    for sati in radni_sati:
        if sati > norma:
            ukupno_preko += (sati - norma)
    print('Ukupan broj prekovremenih sati je', ukupno_preko)






.. questionnote::

    **Zadatak - prosečan prinos:**  
    
    U jednom voćnjaku posle treće godine se prati prinos šljive po stablu. Stabla sa prinosom ispod 3 kilograma se smatraju oštećenim ili obolelim i biće izvađena. 
    
    Dat je prinos svih stabala u voćnjaku. Dovršiti program tako da izračunava i ispisuje prosečan prinos zdravih stabala (sa prinosom od 3 i više kilograma).
    
Za date podatke treba da dobijete reultat približno 14.757 .
    
.. activecode:: console__accumulate_yield

    prinosi = (11.3, 15.8, 9.5, 2.6, 21.1, 13.4, 17.9, 0.7, 14.3)
    
    # dovrsite program
