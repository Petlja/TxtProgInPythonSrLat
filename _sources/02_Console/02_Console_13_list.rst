Liste
=====

Od kolekcija smo do sada pomenuli torku i opseg, a videli smo da i string može da se koristi kao kolekcija. Još jedna veoma važna i često korišćena vrsta kolekcija je lista.

Liste i torke
-------------

Liste, kao i torke, mogu da se zadaju nabrajanjem elemenata, uz razliku da se elementi liste pišu između uglastih zagrada:

.. activecode:: console__collections_list1

    for x in [2, 5, 8, 3]:
        print(x)
        
Liste su po mnogo čemu slične torkama. Sve što smo od osobina torki pomenuli u poglavlju o kolekcijama, važi i za liste:

- Lista se takođe može smestiti u promenljivu i obrnuto - elementi liste se mogu dodeliti odgovarajućem broju promenljivih (drugim rečima, lista se može spakovati i raspakovati)
- elementima liste se može pristupiti pomoću imena liste i rednog broja (indeksa) elementa napisanog u uglastim zagradama
- dužina liste se dobija funkcijom *len*

.. activecode:: console__collections_list2

    imena = ["Dragan", "Branko", "Svetlana", "Mirko"]
    a, b, c, d = imena
    print("b =", b)
    print("imena[0] =", imena[0])
    print("len(imena) =", len(imena))
    
Liste imaju i neke osobine koje ih razlikuju od torki. Na primer, liste se mogu produžavati pomoću funkcije *append*:
    
.. activecode:: console__collections_list_append

    a = []
    a.append(3)
    a.append(7)
    a.append(2)
    
    for x in a:
        print(x)
    
Takođe, elementi liste mogu da menjaju svoje vrednosti i mogu da se izbacuju iz liste:

.. activecode:: console__collections_list_mutable

    a = [3, 7, 2]
    print("Početna lista:")
    for x in a:
        print(x)
        
    a[0] = 5
    print("Izmenjena lista:")
    for x in a:
        print(x)

    del a[1]
    print("Skraćena lista:")
    for x in a:
        print(x)

Ovakve operacije sa torkama nisu moguće. Jednom napravljena torka ostaje takva dok postoji. Torka kao vrednost ne može da se modifikuje - ne može menjati svoju dužinu niti vrednosti pojedinih elemenata. Promenljiva koja sadrži torku može samo da dobije celu novu torku kao vrednost, ali time prethodna torka nije modifikovana, nego je prestala da postoji. Zato za torke kažemo da su nepromenljive (imutabilne).

Torke možemo da koristimo za kolekcije podataka koje ne nameravamo da menjamo tokom izvršavanja programa (mada ih možemo menjati ručno pre izvršavanja programa). Upotrebom torki obezbeđujemo da se podaci neće promeniti slučajno, a i program će raditi nešto efikasnije sa torkom nego što bi radio sa listom.

U toku rada programa torka *t* se može konvertovati u listu *a* i obrnuto: ``a = list(t)`` odnosno ``t = tuple(a)``, ali ovakve konverzije su veoma retko potrebne i bolje ih je izbegavati (ako se često primenjuju na velikim kolekcijama, ovakve konverzije mogu značajno da uspore program).


.. commented out 

    Prednost listi u odnosu na torke je očigledna, liste su fleksibilnije jer mogu da se menjaju. Ipak, i torke imaju svojih prednosti i razlog postojanja. Ovde se ne možemo upuštati u detalje, ali pomenimo za sada da je rad sa torkama nešto efikasniji nego rad sa listama, a postoje i primene u kojima liste ne mogu da se koriste umesto torki. 

    Možemo se zapitati kako da izaberemo da li da u nekom zadatku koristimo torku ili listu. Radi odluke je za sada dovoljno znati ovo:

    - Za kolekciju koja će u toku rada programa menjati dužinu ili vrednosti pojedinih elemenata, moramo da koristimo listu. 
    - Za kolekciju koja se nakon formiranja ne menja u programu, možemo da biramo listu ili torku (malu prednost možemo da damo torkama)
    - U svakom trenutku je moguća konverzija torke *t* u listu *a* i obrnuto: ``a = list(t)`` odnosno ``t = tuple(a)`` (u slučaju veoma dugačkih kolekcija treba izbegavati ovakve konverzije).


Formiranje liste
----------------

Kao što smo već videli, liste možemo jednostavno i efikasno da postepeno gradimo u programu. Na primer, ako je data torka brojeva iz koje želimo da u listu prebacimo one koji su veći od nule (da bismo sa njima nastavili da računamo), to možemo da uradimo ovako:

.. activecode:: console__collections_list_create

    brojevi  = (2, 5, -2, 1, -3, 4, -7, 3)
    pozitivni = []
    for x in brojevi:
        if x > 0:
            pozitivni.append(x)
            
    for x in pozitivni:
        print(x)

Na početku imamo praznu listu, a onda u petlji koristimo funkciju *append* da bismo dodali u listu elemente koje želimo.


Učitavanje liste
----------------

Na potpuno isti način možemo da formiramo listu od podataka koji se učitavaju: 

.. activecode:: console__collections_list_read1

    a = []
    n = int(input("Koliko elemenata treba učitati: "))
    for i in range(n):
        x = float(input("Unesite element: "))
        a.append(x)

    print("Elementi liste su:")
    for x in a:
        print(x)

Drugi način da učitamo listu je da prvo formiramo listu potrebne dužine, a onda da u petlji učitane vrednosti dodeljujemo direktno elementima liste. 

.. activecode:: console__collections_list_read2

    n = int(input("Koliko elemenata treba učitati: "))
    a = [0] * n
    for i in range(n):
        a[i] = float(input("Unesite element: "))

    print("Elementi liste su:")
    for x in a:
        print(x)

Koristili smo naredbu ``a = [0] * n`` kojom se formira lista od *n* elemenata. Operacija ``[0] * n`` se naziva umnožavanje (multipliciranje) liste. Rezultat umnožavanja liste je *n* nadovezanih datih listi. Na primer [0] * 5 je lista [0, 0, 0, 0, 0], a [2, 7] * 3 je lista [2, 7, 2, 7, 2, 7].


Ako korisnik unosi sve elemente liste u jednom redu razdvojene razmacima, program pišemo ovako:

.. activecode:: console__collections_list_read_line

    a_str = input("Unesite sve elemente: ")
    a = []
    for s in a_str.split():
        a.append(s)

    print("Elementi liste su:")
    for x in a:
        print(x)

Za rastavljanje unetog teksta na kraće stringove koji sadrže pojedinačne brojeve upotrebili smo funkciju *split()*. 

.. infonote::

    **Funkcija** *split()*:
    
    Parametar funkcije *split()* je znak ili tekst koji želimo da koristimo kao razdvajač (separator). Ako ne navedemo separator, podrazumeva se razmak.
    
    :code:`"1234 56".split() -> ["1234", "56"]`
    
    :code:`"1234,56".split(',') -> ["1234", "56"]`
    
    Rezultat funkcije  *split()* je lista stringova. Broj kraćih stringova koje ćemo kao rezultat dobiti, zavisi od broja i rasporeda znakova - razdvajača u polaznom stringu. Na primer, ako tekst sadrži samo jedan znak za razdvajanje negde u sredini, dobićemo dva kraća stringa. Svaki novi znak za razdvajanje može proizvesti string više u rezultatu (ako zaista odvaja neki deo polaznog stringa od ostatka teksta).
    
    :code:`"1;23;456;7".split(';') -> ["1", "23", "456", "7"]`
    
    :code:`" 1  234    56 7 ".split() -> ["1", "234", "56", "7"]`
    


Primeri i zadaci
''''''''''''''''

.. questionnote::

    **Primer - prodaje**
    
    Na početku skripte su date vrednosti nekoliko prodaja u jednoj prodavnici. Izdvojiti u listu prodaje koje su po vrednosti veće od 1000, a manje ili jednake 4000, a zatim ih ispisati.

.. activecode:: console__collections_list_sales

    prodaje = (241, 5372, 1278, 9335, 2438, 127, 529, 6027)
    donja_granica = 1000
    gornja_granica = 4000
    # dovrsite program

Zadatak rešavamo ovako:

.. activecode:: console__collections_list_sales_sol

    prodaje = (241, 5372, 1278, 9335, 2438, 127, 529, 6027)
    donja_granica = 1000
    gornja_granica = 4000

    trazene_prodaje = []
    for vrednost in prodaje:
        if vrednost > donja_granica and vrednost <= gornja_granica:
            trazene_prodaje.append(vrednost)

    print('Tražene prodaje:')
    for vrednost in trazene_prodaje:
        print(vrednost)


.. questionnote::

    **Primer - Nagle promene**
    
    Data je torka brojeva. Izdvojiti u listu brojeve koji se od svojih prethodnika razlikuju bar za 10, a zatim ih ispisati.

.. activecode:: console__collections_list_increasing

    brojevi = (5, 7, 9, 11, 22, 18, 15, 13, 36, 31, 27, 14, 13, 20)
    # dovrsite program

Jedno moguće rešenje je:

.. activecode:: console__collections_list_increasing_sol

    brojevi = (5, 7, 9, 11, 22, 18, 15, 13, 36, 31, 27, 14, 13, 20)
    nagle_promene = []
    
    for i in range(1, len(brojevi)):
        if abs(brojevi[i] - brojevi[i-1]) >= 10:
            nagle_promene.append(brojevi[i])

    print('Nagle promene:')
    for x in nagle_promene:
        print(x)





.. questionnote::

    **Zadatak - parni brojevi**
    
    Data je torka brojeva. Izdvojiti u listu brojeve koji su parni, a zatim ih ispisati.
    
    Podsetimo se, broj *x* je paran ako je :math:`x \% 2 == 0`

.. activecode:: console__collections_list_even

    a = (35, 12, 32, 17, 64, 98, 77, 46, 9)
    parni = []
    
.. commented out

    for x in a:
        if x % 2 == 0:
            parni.append(x)

    print('Parni brojevi:')
    for x in parni:
        print(x)




.. questionnote::

    **Zadatak - svaka treća reč**
    
    Data je torka stringova. Izdvojiti u listu stringove **čiji indeksi** su deljivi sa 3, a zatim ih ispisati.
    
.. activecode:: console__collections_list_every_third

    reci = ('Preko', 'ograde', 'od', 'trnja', 'pogled', 'ide', 'do', 'plainina', 'i', 'zvezda', 'na', 'nebu')
    svaka_treca = []
    
.. commented out

    for i in range(len(reci)):
        if i % 3 == 0:
            svaka_treca.append(reci[i])

    print('Svaka treća reč:')
    for rec in svaka_treca:
        print(rec)




.. questionnote::

    **Zadatak - ispod nule**
    
    Data je torka brojeva. Izdvojiti u listu brojeve koji su negativni, a njihovi prethodnici pozitivni, a zatim ispisati izdvojene brojeve.
    
.. activecode:: console__collections_list_neg_after_pos

    a = (1, -2, 3, 5, -4, -1, -3, 2, -7)
    izdvojeni = []
    
.. commented out

    for i in range(1, len(a)):
        if a[i] < 0 and a[i - 1] > 0:
            izdvojeni.append(a[i])

    for x in izdvojeni:
        print(x)
