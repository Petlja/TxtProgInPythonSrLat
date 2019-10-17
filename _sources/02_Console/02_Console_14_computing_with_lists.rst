Računanje sa listama
====================

Ovde ćemo još malo uvežbavati rad sa listama i kombinavanje tehnika koje smo do sada naučili.


.. questionnote::

    **Zadatak - najmanji pozitivan broj**
    
    Data je torka brojeva. Ispisati najmanji pozitivan broj iz te torke.

Ovaj zadatak je kombinacija zadataka kakve smo radili do sada. U prvom delu zadatka u listu kopiramo pozitivne brojeve iz torke, a u drugom delu primenjujemo funkciju *min* na listu pozitivnih brojeva. 

.. activecode:: console__list_min_positive

    a = (-4, 3, 4, -3, 5, 6, 2, -5)
    poz = []
    for x in a:
        if x > 0:
            poz.append(x)

    print(min(poz))

Pomenuli smo da funkcije *min*, *max*, *sum*, *len* mogu da se primene različite kolekcije i pokazali smo to na primerima torke, opsega i stringa (izuzev sume elemenata stringa). Sada vidimo da funkcija *min* prihvata i listu kao svoj argument. Isto važi i za funkcije *max*, *sum*, *len*.





.. questionnote::

    **Primer - kvarovi**
    
    U jednoj fabrici ima 10 mašina i one su predstavljene brojevima od 0 do 9. Za svaki kvar koji je nastao beleži se broj mašine koja se kvarila. Ovi brojevi su dati u torki na početku skripte.

    Napišite program koji ispisuje koliko je puta svaka od mašina neispravno funkcionisala, a zatim i brojeve mašina koje se nisu ni jednom pokvarile.

   
.. activecode:: console__list_malfunctions

    kvarovi = (0, 2, 1, 3, 2, 4, 2, 6, 4, 7, 4, 8)

Prvi deo zadatka zahteva da prebrojimo koliko puta se svaki broj pojavljuje u ulaznim podacima. Da bismo rešili taj deo zadatka, pravimo niz *br_kvarova* od 10 elemenata (koji su inicijalno nule), u kome svaki element odgovara jednoj mašini i broji njene kvarove.

.. code::
    
    br_kvarova = [0] * 10
    for masina in kvarovi:
        br_kvarova[masina] += 1

Nakon toga za svaku mašinu ispisujemo koliko je imala kvarova. Ovde koristimo opseg jer želimo da za svaku mašinu pored broja kvarova ispišemo i njen redni broj:

.. code::

    for masina in range(10):
        print('Mašina', masina, 'se kvarila', br_kvarova[masina], 'puta.')

U drugom delu zadatka se traži da ispišemo brojeve mašina koje se nisu kvarile. To su mašine kojima je broj kvarova jednak nuli. Prolazimo još jednom kroz listu *br_kvarova* i indekse elemenata jednakih nuli ubacujemo u listu *ispravne*:

.. code::

    ispravne = []
    for masina in range(10):
        if br_kvarova[masina] == 0:
            ispravne.append(masina)
            
Na kraju ispisujemo elemente liste *ispravne*:

.. code::

    print('Mašine koje se nisu kvarile:')
    for masina in ispravne:
        print(masina)

Evo kako izgleda ceo program:

.. activecode:: console__list_malfunctions_sol

    kvarovi = (0, 2, 1, 3, 2, 4, 2, 6, 4, 7, 4, 8)
    br_kvarova = [0] * 10
    for masina in kvarovi:
        br_kvarova[masina] += 1

    for masina in range(10):
        print('Mašina', masina, 'se kvarila', br_kvarova[masina], 'puta.')

    ispravne = []
    for masina in range(10):
        if br_kvarova[masina] == 0:
            ispravne.append(masina)
            
    print('Mašine koje se nisu kvarile:')
    for masina in ispravne:
        print(masina)


.. questionnote::

    **Zadatak - navijači**

    Navijači iz 8 zemalja dolaze na turnir u grad *X*. Organizatori turnira žele da znaju koliko navijača dolazi iz svake od zemalja.
    
    Svaka zemlja je predstavljena brojem od 0 do 7. Dati brojevi za svakog navijača govore iz koje zemlje on dolazi. Dopuniti program koji za svaku zemlju ispisuje koliko navijača dolazi iz nje.

U zadatku se traži da se za svaki broj od 0 to 7 prebroji koliko puta se taj broj pojavljuje mežu datim brojevima. Deo koji nedostaje je vrlo sličan brojanju kvarova iz datog primera.

.. activecode:: console__list_counters

    navijaci = (1, 2, 3, 2, 3, 0, 2, 4, 3, 5, 6, 4, 0, 5, 3, 7, 1, 6, 3)
    br_nav = [0] * 8
    for # dopunite
        # dopunite

    for zemlja in range(8):
        print('Iz zemlje', zemlja, 'dolazi', br_nav[zemlja], 'navijača.')

.. commented out

    navijaci = (1, 2, 3, 2, 3, 0, 2, 4, 3, 5, 6, 4, 0, 5, 3, 7, 1, 6, 3)
    br_nav = [0] * 8
    for x in navijaci:
        br_nav[x] += 1

    for zemlja in range(8):
        print('Iz zemlje', zemlja, 'dolazi', br_nav[zemlja], 'navijača.')




.. questionnote::

    **Zadatak - najviše navijača**
    
    Ovo je nastavak prethodnog zadatka. Organizatori sada dodatno žele da znaju iz koje zemlje dolazi najviše navijača.
    
    Iskopirajete prethodni program i dopunite ga tako da na kraju ispisuje broj zemlje iz koje dolazi najviše navijača.

Ako ispravno rešite zadatak, program treba da ispiše broj 3, jer se taj broj načešće pojavljuje među podacima.

.. activecode:: console__list_max_counter

    navijaci = (1, 2, 3, 2, 3, 0, 2, 4, 3, 5, 6, 4, 0, 5, 3, 7, 1, 6, 3)






.. questionnote::

    **Zadatak - Najveći negativan broj**

    Data je torka brojeva. Ispisati najveći negativan broj iz te torke.

.. activecode:: console__list_max_negative

    a = (-4, 3, 4, -3, 5, 6, 2, -5)







.. questionnote::

    **Zadatak - Male prodaje**

    Data torka sadrži iznose računa kupaca u jednoj prodajnoj mreži. Sve prodaje sa iznosom manjim od 500 se smatraju za male prodaje. Napisati program koji izračunava ukupan prihod od svih malih prodaja.

Ovaj zadatak možete da rešavate na dva načina. Jedan je izdvajanje malih iznosa u posebnu listu i primena funkcije *sum* na tu listu. Drugi način je postepeno građenje zbira, kao što smo to radili u lekciji o brojanju i sumiranju.

.. activecode:: console__list_sum_small_sales

    prodaje = (158, 681, 249, 1250, 335, 5400, 455)


