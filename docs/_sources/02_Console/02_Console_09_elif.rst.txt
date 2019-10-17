Složena grananja
================

Uzastopni uslovi
----------------

Ima zadataka u kojima, kada jedan uslov nije ispunjen, treba proveriti drugi, pa ako ni taj uslov ne važi onda se proverava treći itd. Da ne bismo pisali

.. activecode:: console__more_branching_elif1
    :passivecode: true
    
    if prvi_uslov:
        naredba1
    else:
        if drugi_uslov:
            naredba2
        else:
            if treci_uslov:
                naredba3
            else:
                if cetvrti_uslov:
                    naredba4
                else:
                    naredba5

u Pajtonu koristimo specijalnu reč ``elif``, koja stoji umesto *else:* i uvučenog *if* u sledećem redu. Tako dobijamo pregledniji zapis:

.. activecode:: console__more_branching_elif2
    :passivecode: true
    
    if prvi_uslov:
        naredba1
    elif drugi_uslov:
        naredba2
    elif treci_uslov:
        naredba3
    elif cetvrti_uslov:
        naredba4
    else:
        naredba5

Napomena 1: Bilo koji broj uzastopnih *elif* naredbi se može upotrebiti na ovaj način. 

Napomena 2: Deo 

.. activecode:: console__more_branching_elif3
    :passivecode: true

    else:
        naredba5

nije obavezan i može da se izostavi ako za njim nema potrebe.

Primeri i zadaci
''''''''''''''''

.. questionnote::
    
    **Primer - indeks telesne mase:** 
    
    Za brzu orijentaciju u vezi sa stepenom gojaznosti ili mršavosti koristi se indeks telesne mase (engl. body mass index, skraćeno bmi). Za izračunavanje indeksa telesne mase koristi se formula :math:`bmi = {m \over {h \times h}}`, gde je *m* masa u kilogramima, a *h* visina u metrima. Tumačenja vrednosti *bmi* su sledeća:

    - do 18.5: pothranjena osoba
    - od 18.5 do 25: osoba normalne telesne mase
    - od 25 do 30: osoba prekomerne telesne mase
    - preko 30: gojazna osoba
    
    Napisati program koji učitava telesnu masu i visinu osobe, a zatim ispisuje kojoj kategoriji pripada ta osoba (granične vrednosti priključiti nižoj kategoriji).

Jedno moguće rešenje je dato ispod. Razmislite o tome zašto nije neophodno koristiti složene uslove (reči *and*, *or*, *not*) u ovom rešenju.

.. activecode:: console__more_branching_bmi

    m = float(input('Telesna masa: '))
    h = float(input('Telesna visina: '))
    bmi = m / (h*h)
    if bmi <= 18.5:
        print('Pothranjena osoba.')
    elif bmi <= 25:
        print('Osoba normalne telesne mase.')
    elif bmi <= 30:
        print('Osoba prekomerne telesne mase.')
    else:
        print('Gojazna osoba.')



.. questionnote::
    
    **Zadatak - kategorije igrača:** 
    
    Mladi košarkaši se na početku košarkaške sezone registruju u jednoj od uzrasnih kategorija, prema tome koliko godina pune u kalendarskoj godini u kojoj sezona počinje. Pravila registrovanja su sledeća:

    - 10 i manje - bez kategorije
    - 11 ili 12 godina - mlađi pioniri
    - 13 ili 14 godina - pioniri
    - 15 ili 16 godina - kadeti
    - 17 ili 18 godina - juniori
    - 19 i više godina - seniori
    
    Napisati program koji učitava koliko godina košarkaš puni u godini u kojoj se registruje, a ispisuje njegovu uzrasnu kategoriju.

.. activecode:: console__more_branching_categories

    g = int(input("Koliko godina ima igrač: "))
    # dovrsite


        
.. questionnote::
    
    **Zadatak - redni broj:** 
    
    Napisati program koji učitava ceo broj od 1 do 6 (uključujući granice), a ispisuje odgovarajući redni broj slovima. Na primer, ako se učita broj 6, treba ispisati "šesti" (bez navodnika).

.. activecode:: console__more_branching_ordinal

    n = int(input("Unesite broj od 1 do 6: "))
    # dovrsite

Ugnežđena grananja
------------------

Ugnežđena grananja su *if* naredbe u granama drugih *if* naredbi. Ugnežđene (umetnute) *if* naredbe mogu da se nađu u jednoj, drugoj ili obe grane neke veće *if* naredbe. Ovakav način postavljanja *if* naredbi može ići do bilo koje dubine, ali treba imati na umu da programi na taj način mogu da postanu vrlo nepregledni i teški za tačno razumevanje i eventualne izmene kada je potrebno.

U prvom primeru namerno dajemo program sa tri nivoa gnežđenja *if* naredbi, da biste lakše zamislili kako može da izgleda program sa još dublje ugnežđenim i dužim *if* naredbama. U ostalim primerima i zadacima ćemo se ograničiti na jedan nivo umetanja *if* naredbi.

Primeri i zadaci
''''''''''''''''


.. questionnote::
    
    **Primer - nepoznato ime**
    
    U komšiluku ima osmoro dece koja su često zajedno. Njihova imena su: Ana, Bane, Vera, Goran, Dunja, Đorđe, Ema i Žarko. Ana, Bane, Vera i Goran idu na programersku sekciju, a Ana, Bane, Dunja i Đorđe na sportsku sekciju. Školska kuvarica je htela da pohvali jedno od dece, ali nije znala ime tog deteta.
    
    Napisati program koji postavlja tri pitanja, prihvata odgovore na ta pitanja (slovo 'd' za da, a svaki drugi odgovor za ne) i ispisuje ime deteta o kome je reč. Pitanja koja program postavlja su:

    - Da li je to devojčica
    - Da li ide na sportsku sekciju
    - Da li ide na programersku sekciju
    
.. activecode:: console__more_branching_guess_who1

    devojcica = input("Da li je to devojčica: ") == 'd'
    sportista = input("Da li ide na sportsku sekciju: ") == 'd'
    programer = input("Da li ide na programersku sekciju: ") == 'd'
    if programer:
        if sportista:
            if devojcica:
                print("Ana")
            else:
                print("Bane")
        else:
            if devojcica:
                print("Vera")
            else:
                print("Goran")
    else:
        if sportista:
            if devojcica:
                print("Dunja")
            else:
                print("Đorđe")
        else:
            if devojcica:
                print("Ema")
            else:
                print("Žarko")
            
Primetimo da programi sa ugnežđenim grananjima mogu da se preprave tako da koriste samo uzastopne uslove i oblik sa "elif", bez umetanja *if* naredbi u dubinu. Pri tome koristimo složene uslove, koje gradimo pomoću logičkih operacija *and*, *or* i *not*.
   
.. activecode:: console__more_branching_guess_who2

    devojcica = input("Da li je to devojčica: ") == 'd'
    sportista = input("Da li ide na sportsku sekciju: ") == 'd'
    programer = input("Da li ide na programersku sekciju: ") == 'd'
    if programer and sportista and devojcica:
        print("Ana")
    elif programer and sportista and not devojcica:
        print("Bane")
    elif programer and not sportista and devojcica:
        print("Vera")
    elif programer and not sportista and not devojcica:
        print("Goran")
    elif not programer and sportista and devojcica:
        print("Dunja")
    elif not programer and sportista and not devojcica:
        print("Đorđe")
    elif not programer and not sportista and devojcica:
        print("Ema")
    else:
        print("Žarko")



.. questionnote::
    
    **Zadatak - raskrsnica:** 
    
    U novom naselju nalazi se raskrsnica velikih ulica A i B. Brojevi u ulici A su parni sa desne strane a neparni sa leve. Na parnoj strani brojevi do raskrsnice su od 2 do 200, a posle raskrsnice su veći od 200. Na neparnoj strani brojevi do raskrsnice su od 1 do 177, a posle raskrsnice su od 179 nadalje. 

    Napisati program koji učitava jedan kućna broj u ulici A i odgovara da li je taj broj pre ili posle raskrsnice i sa koje strane ulice A. Na primer:
    
    - za broj 128 ispisati "sa desne strane, pre raskrsnice"
    - za broj 284 ispisati "sa desne strane, posle raskrsnice"
    - za broj 177 ispisati "sa leve strane, pre raskrsnice"
    - za broj 219 ispisati "sa leve strane, posle raskrsnice"

**Pomoć:** Nakon učitavanja, prvo treba proveriti da li je kućni broj *n* paran, to jest da li je :math:`n \% 2 == 0`.

.. activecode:: console__more_branching_quart

    n = int(input("Koji je kućni broj: "))
    # dovrsite




.. questionnote::
    
    **Zadatak - učenje:** 
    
    Jovanovi roditelji su rekli Jovanu da ako dobije četvorke ili petice iz matematike i engleskog, može da ide popodnevni fudbalski turnir, u protivnom mora da uči predmet ili predmete iz kojih dobije ocene manje od 4.

    Napisati program koji prvo učitava Jovanovu ocenu iz matematike a zatim iz engleskog i ispisuje poruku za Jovana. Na primer:
    
    - za ocene 2, 3 ispisati "uči i matematiku i engleski"
    - za ocene 3, 4 ispisati "uči matematiku"
    - za ocene 4, 2 ispisati "uči engleski"
    - za ocene 5, 4 ispisati "idi na turnir"

.. activecode:: console__more_branching_grades

    mat = int(input("Koja je ocena iz matematike: "))
    eng = int(input("Koja je ocena iz engleskog: "))
    # dovrsite


.. questionnote::
    
    **Zadatak - oblačenje:** 
    
    Igor pravi program koji sa sajta za vremensku prognozu očitava trenutnu temperaturu (u stepenima Celzijusa) i šanse za kišu (od 0 do 100), pa na osnovu tih podataka ispisuje preporuku da li treba poneti jaknu (koja ima kapuljaču) ili kišobran, ili nijedno od ta dva. Igor je izabrao ovakvo pravilo: 
        
    - kada je temperatura niža od 21, savet neka glasi: "ponesi jaknu"
    - kada je temperatura 21 ili viša a šanse za kišu preko 50, preporuka je: "ponesi kišobran"
    - kada je temperatura 21 ili viša a šanse za kišu do 50, savet neka bude "možeš samo u majici"

    Vi napišite program koji učitava prvo temperaturu pa šanse za kišu, a zatim ispisuje preporuku.
    
.. activecode:: console__more_branching_weather

    t = int(input("Koja je temperatura: "))
    sanse_kisa = int(input("Koje su šanse za kišu: "))
    # dovrsite







.. commented out

    .. questionnote::
        
        **Zadatak - raskrsnica:** 
        
        U novom naselju nalazi se raskrsnica velikih ulica A i B. Brojevi u ulici A do raskrsnice su manji od 200, a posle raskrsnice su veći ili jednaki 200. Pri tome su neparni brojevi sa leve strane ulice, a parni sa desne.

        Napisati program koji za dva kućna broja u ulici A odgovara koje velike ulice je potrebno preći da bi se došlo od jedne do druge adrese. Na primer:
        
        - za brojeve 128 i 64 ne treba preći ni jednu od tih ulica
        - za brojeve 208 i 225 treba preći ulicu A
        - za 207 i 91 treba preći ulicu B
        - za 133 i 210 treba preći obe ulice

    **Pomoć:** neka su *m* i *n* učitani kućni brojevi. Tada:

    - Brojevi *m* i *n* su sa iste strane ulice A ako su iste parnosti, odnosno ako imaju isti ostatak pri deljenju sa dva.
    - Brojevi *m* i *n* su sa iste strane ulice B ako su oba manja od 200 ili oba od 200 naviše, odnosno ako su logiči izrazi :math:`m < 200` i :math:`n < 200` oba tačna ili oba netačna, tj. ako je :math:`m < 200` jednako sa :math:`n < 200`.

    Zbog toga rešenje može da počne ovako:

    .. activecode:: console__more_branching_crossing1

        m = int(input("Prvi broj: "))
        n = int(input("Drugi broj: "))
        sa_ste_strane_a = (m % 2 == n % 2)
        sa_ste_strane_b = (m < 200 == n < 200)
        if sa_ste_strane_a and sa_ste_strane_b:
            print('Kućne brojeve', m, 'i', n, 'ne razdvaja ni jedna ulica.')
        elif # dovrsite


    .. commented out

        .. activecode:: console__more_branching_crossing1

            m = int(input("Prvi broj: "))
            n = int(input("Drugi broj: "))
            sa_ste_strane_a = (m % 2 == n % 2)
            sa_ste_strane_b = (m < 200 == n < 200)
            if sa_ste_strane_a and sa_ste_strane_b:
                print('Kućne brojeve', m, 'i', n, 'ne razdvaja ni jedna ulica.')
            elif sa_ste_strane_a:
                print('Kućne brojeve', m, 'i', n, 'razdvaja ulica B.')
            elif sa_ste_strane_b:
                print('Kućne brojeve', m, 'i', n, 'razdvaja ulica A.')
            else:
                print('Kućne brojeve', m, 'i', n, 'razdvajaju obe ulice.')

    Zadatak je mogao da bude rešen i umetanjem *if* naredbi jedne u drugu. U tom slučaju nam ne bi bila potrebna reč *elif*. 

    .. activecode:: console__more_branching_crossing2

        m = int(input("Prvi broj: "))
        n = int(input("Druge broj: "))
        sa_ste_strane_a = (m % 2 == n % 2)
        sa_ste_strane_b = (m < 200 == n < 200)
        if sa_ste_strane_a:
            if sa_ste_strane_b:
                print('Kućni brojevi', m, 'i', n, 'su u istom kvartu.')
            else:
                print('Kućne brojeve', m, 'i', n, 'razdvaja ulica B.')
        else:
            if sa_ste_strane_b:
                print('Kućne brojeve', m, 'i', n, 'razdvaja ulica A.')
            else:
                print('Kućne brojeve', m, 'i', n, 'razdvajaju obe ulice.')
