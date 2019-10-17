Naredbe grananja
================

U lekcijama o Karelu smo redovno proveravali na primer da li robot može da ide napred. Ove provere su nam bile portebne, jer ukoliko bismo pokušali da pomerimo robota napred kada polje ispred njega ne postoji, program bi prijavio grešku i prekinuo rad. Isto tako, trebalo je pre uzimanja loptice provravati da li postoji loptica na polju, a pre ostavnjanja loptica provreavati da il Karel ima loptica kod sebe.

Slično tome, u programima u kojima računamo često nam je potrebno da poredimo dve vrednosti, to jest da ustanovimo da li su one jednake, da li je jedna manja od druge, različita od druge i slično. U zavisnosti od ishoda poređenja, program može da nastavi sa izvršavanjem na različite načine.

Neki od simbola koji se koriste za poređenje su isti kao u matematici (na primer ``<`` i ``>``), a neki nisu. U sledećoj tabeli su zato date oznake svih standardnih poređenja koje se koriste u matematici i u programskom jeziku Pajton (kao i u mnogim drugim programskim jezicima).

====================   ==================== ========================================
Matematika             Pajton               Značenje
====================   ==================== ========================================
:math:`a < b`          a < b                a je manje od b
:math:`a \leq b`       a <= b               a je manje ili jednako b
:math:`a > b`          a > b                a je veće od b
:math:`a \geq b`       a >= b               a je veće ili jednako b
:math:`a = b`          a == b               a je jednako b
:math:`a \neq b`       a != b               a nije jednako b
====================   ==================== ========================================

Zapis :math:`a < b` možemo da shvatimo kao izraz čija je vrednost u svakom konkretnom slučaju "tačno" ili "netačno". Ove vrednosti se u Pajtonu pišu redom kao *True* i *False* i to su **logičke konstante**, odnosno konstante tipa ``bool`` koji zovemo logički tip. Izraze čija je vrednost tipa *bool* (logičkog tipa) zovemo **logički izrazi**. Svi izrazi u gornjoj tabeli su logički izrazi (kasnije ćemo videti i drugačije logičke izraze).

Naredba if
----------

Naredbu *if* smo već upoznali u lekcijama o Karelu, podsetimo se:

Naredba *if* služi za donošenje odluke koja grupa od dve grupe naredbi treba da se izvrši. Na pajtonu se ona piše ovako:

.. activecode:: console__if_else_syntax
   :passivecode: true

   if uslov:
       naredba_a1
       ...
       naredba_ak
   else:
       naredba_b1
       ...
       naredba_bm

.. infonote::

    **Značenje (semantika) naredbe if:** 
    
    Naredba napisana gore znači: ako je uslov ispunjen, izvrši naredbe *naredba_a1*, ... *naredba_ak*, a ako nije ispunjen, onda izvrši naredbe *naredba_b1*, ... *naredba_bm*.
    
    **Pravila pisanja (sintaksa) naredbe if**
    
    - Posle reči ``if`` se piše logički izraz i na kraju reda obavezno znak ``:`` (dvotačka).
    - U sledećim redovima, uvučeno za isti broj razmaka (uobičajeno je 4), pišu se naredbe koje treba da budu izvršene ako logički izraz ima vrednost *True*. Ovih naredbi može biti jedna ili više.
    - Nakon naredbi koje se izvršavaju ako je uslov ispunjen piše se reč ``else`` i ponovo znak ``:`` (dvotačka). Reč *else* je jednako uvučena kao i reč *if*.
    - U sledećim redovima, ponovo uvučeno za isti broj razmaka, pišu se naredbe koje treba da budu izvršene ako logički izraz ima vrednost *False*. I ovih naredbi može biti jedna ili više.
    
    Naredba ``if`` se zove i *naredba grananja* zato što se tok izvršavanja programa kod ove naredbe grana: sledeća naredba koja će se izvršiti zavisi od vrednosti logičkog izraza u uslovu. Grupe naredbi posle reči *if*, odnosno *else* ze zato nazivaju i granama *if* naredbe.

U slučaju da program ne treba da uradi ništa kada uslov *if* naredbe nije ispunjen, to jest kada nam druga grana naredbe *if* nije potrebna, možemo da je izostavimo:

.. activecode:: console__if_syntax
   :passivecode: true

   if uslov:
       naredba_a1
       ...
       naredba_ak

Ovakav, skraćeni oblik *if* naredbe ćemo koristiti kasnije.

Naredba if - primeri i zadaci
'''''''''''''''''''''''''''''

.. questionnote::
    
    **Primer - ko je mlađi:** 
    
    Petar i Miloš treba da odigraju partiju bilijara. Dogovorili su se da prvi igra onaj ko je mlađi. Napisati program koji učitava broj godina Petra i Miloša (koji nisu jednaki) i ispisuje ko će izvesti prvi potez.

.. activecode:: console__branching_younger

    petar = int(input("Koliko godina ima Petar: "))
    milos = int(input("Koliko godina ima Miloš: "))
    if petar < milos:
        print('Petar igra prvi.')
    else:
        print('Miloš igra prvi.')





.. questionnote::
    
    **Primer - pakovanje:** 
    
    Jaja se na farmi pakuju u kutije od po 10 komada i pune kutije se šalju u prodavnicu. Napisati program koji učitava broj jaja spremnih za pakovanje, a ispisuje da li sva jaja mogu da se spakuju i pošalju u prodavnicu, ili će nekoliko jaja privremeno ostati neupakovano.

Ovde treba proveriti da li je broj jaja deljiv sa 10. Radi toga koristimo operator % koji daje ostatak pri deljenju. Ako je ostatak pri deljenju broja jaja sa 10 jednak nuli, sva jaja mogu da se pošalju.

.. activecode:: console__branching_eggs

    broj_jaja = int(input("Koliko ima jaja: "))
    if broj_jaja % 10 == 0:
        print('Sva jaja mogu da se pošalju.')
    else:
        print('Neka jaja će ostati.')





.. questionnote::
    
    **Zadatak - Strana ulice:** 
    
    Parni brojevi se nalaze sa desne strane ulice, a neparni sa leve. Napisati program koji učitava traženi broj i ispisuje sa koje strane ulice se nalazi taj broj.

Ovde treba proveriti da li je traženi broj deljiv sa 2. Zadatak je sličan prethodnom - ako je ostatak pri deljenju traženog broja sa 2 jednak nuli, broj je sa desne strane, inače je sa leve strane.

.. activecode:: console__branching_home_number

    broj = int(input("Koji je kućni broj: "))
    # dovrsite




.. questionnote::
    
    **Zadatak - bioskop:** 
    
    Imate kod sebe 700 dinara. Napišite program koji učitava cenu bioskopske karte i cenu kokica, a zatim ispisuje da li imate dovoljno novca za kartu i kokice.
    

.. activecode:: console__branching_cinema

    cena_karte = int(input("Pošto je karta: "))
    cena_kokica = int(input("Pošto su kokice: "))
    # dovrsite


Složeni uslovi
--------------

U nekim zadacima je potrebno da iskažemo uslove koji su složeniji od prostog poređenja dve vrednosti. Za povezivanje jednostavnijih uslova se koriste reči **i**, **ili** i **ne**, a u Pajtonu se za to koriste upravo iste te reči na engleskom: **and**, **or**, **not**. Pri tome, ako su *a* i *b* neki uslovi, tada:

- uslov *a and b* će biti ispunjen ako su oba uslova *a* i *b* ispunjena;
- uslov *a or b* će biti ispunjen ako je bar jedan od uslova *a* i *b* ispunjen;
- uslov *not a* će biti ispunjen ako uslov *a* nije ispunjen (što smo već pominjali i u poglavljima o Karelu);

Ovi uslovi se mogu dalje kombinovati u još složenije, prema potrebama zadatka. U složenim uslovima možemo da koristimo zagrade da bismo uticali na redosled računanja uslova (ili ako nismo sigurni koji je podrazumevani redosled), a i da bi program bio jasniji drugim ljudima koji ga čitaju. Ako u složenom uslovu nema zagrada, prvo se primenjuje *not*, zatim *and*, i na kraju *or*.

Složeni uslovi - primeri
''''''''''''''''''''''''

.. questionnote::
    
    **Primer - prestupna godina:**

    Napisati program koji odgovara da li je zadata godina (između 1800-te i 2200-te, uključujući granice) prestupna ili prosta.
    
    Po gregorijanskom kalendaru, za određivanje da li je godina prosta ili prestupna, koriste se sledeća pravila:
    
    - godine koje nisu deljive sa 4 (npr. 1923, 1070, 2017) su proste;
    - godine koje su deljive sa 100 a nisu sa 400 (npr. 1700, 1800, 1900, 2100, 2200) su takođe proste;
    - sve ostale godine (npr. 1984, 2000, 2012) su prestupne. To su godine koje su deljive sa 4 a nisu sa 100, ili su deljive sa 400.

Zapisujući data pravila u obliku logičkog uslova, dobijamo:
    
.. activecode:: console__branching_leap_year1

    godina = int(input())
    if (godina % 4 > 0) or (godina % 100 == 0 and godina % 400 > 0):
        print("Godina", godina, "je prosta.")
    else:
        print("Godina", godina, "je prestupna.")

Ravnopravno rešenje dobijamo ako iskoristimo opis za prestupne godine, dat u trećem pravilu (uverite se razmišljanjem i isprobavanjem oba programa da se dobija isti rezultat):
    
.. activecode:: console__branching_leap_year2

    godina = int(input())
    if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0:
        print("Godina", godina, "je prestupna.")
    else:
        print("Godina", godina, "je prosta.")


.. questionnote::

    **Primer - radno vreme:** 
    
    Radno vreme jedne prodavnice suvenira je od 7 do 11 ujutro i od 17 do 22 uveče (smatrati da tačno u 7:00 i u 17:00 radi, a u 11:00 i u 22:00 ne radi). Petar je naišao na prodavnicu u *H* časova i *M* minuta. Napisati program koji učitava broj *H* (od 0 do 23) i odgovara da li je Petar naišao u toku radnog vremena prodavnice.
    
.. activecode:: console__branching_working_hours1

    h = int(input())
    if (7 <= h and h < 11) or (17 <= h and h < 22):
        print("Petar je naišao u toku radnog vremena.")
    else:
        print("Petar je naišao van radnog vremena.")
    
Do rešenja možemo dođi i postupnim računanjem logočkih vrednosti, koristeći logičke promenljive:

.. activecode:: console__branching_working_hours2

    h = int(input())
    u_radno_vr_ujutro = 7 <= h and h < 11
    u_radno_vr_uvece = 17 <= h and h < 22
    u_radno_vr = u_radno_vr_ujutro or u_radno_vr_uvece
    if u_radno_vr:
        print("Petar je naišao u toku radnog vremena.")
    else:
        print("Petar je naišao van radnog vremena.")

U ovom rešenju samo *h* je celobrojna promenljiva, a sve ostale (*u_radno_vr_ujutro*, *u_radno_vr_uvece*, *u_radno_vr*) su logičke, što znači da će tokom izvršavanja programa dobiti vrednosti *True* ili *False*.

Složeni uslovi - pitanja
''''''''''''''''''''''''

.. dragndrop:: console__branching_quiz_compare
    :feedback: Pokušajte ponovo!
    :match_1: a <= b ||| a < b or a == b
    :match_2: a >= b ||| b <= a
    :match_3: not (a == b) ||| a < b or a > b
    :match_4: not (a != b) ||| a == b

    Uparite ravnopravne uslove

.. mchoice:: console__branching_quiz_interval
   :multiple_answers:
   :answer_a: h < 7 and 11 <= h
   :answer_b: h < 7 or 11 <= h
   :answer_c: not(7 <= h) or not(h < 11)
   :answer_d: h <= 7 or 11 < h
   :correct: b, c
   :feedback_a: Ne, taj uslov nije ispunjen ni za jedno h.
   :feedback_b: Tačno
   :feedback_c: Tačno
   :feedback_d: Ne, vrednost uslova se razlikuje u slučaju da je h jednako baš 7 ili 11.

   Koji sve uslovi su ravnopravni sa **not(7 <= h and h < 11)** ?

.. dragndrop:: console__branching_quiz_abc_sign
    :feedback: Pokušajte ponovo!
    :match_1: Bar jedan od a, b, c je pozitivan ||| a > 0 or b > 0 or c > 0
    :match_2: Ni jedan od a, b, c nije pozitivan||| a <= 0 and b <= 0 and c <= 0
    :match_3: a, b, c nisu svi pozitivni ||| a <= 0 or b <= 0 or c <= 0
    :match_4: a, b, c su svi pozitivni ||| a > 0 and b > 0 and c > 0

    Uparite uslove i opise

.. mchoice:: console__branching_quiz_sport_center
   :multiple_answers:
   :answer_a: (stanovnika <= 10000) or (stanovnika > 10000 and prihod <= 2000)
   :answer_b: stanovnika <= 10000 or prihod <= 2000
   :answer_c: stanovnika <= 10000 and prihod <= 2000
   :answer_d: (prihod <= 2000) or (prihod > 2000 and stanovnika <= 10000)
   :correct: a, b, d
   :feedback_a: Tačno
   :feedback_b: Tačno
   :feedback_c: Pogrešno
   :feedback_d: Tačno

   Državna vlada nudi pomoć za izgradnju sportskog centra. Naseljena mesta do 10000 stanovnika mogu sva da konkurišu, a od mesta sa više od 10000 stanovnika, mogu da konkurišu ona u kojima je prosečan prihod do 2000. Koji od uslova ispravno proveravaju da li neko mesto može da konkuriše?

Složeni uslovi - zadaci
'''''''''''''''''''''''

.. questionnote::

    **Zadatak - brojevi po redu:** 
    
    Napisati program koji učitava cele brojeve *a*, *b*, *c* i odgovara na pitanje da li su ti brojevi dati po veličini od najmanjeg do najvećeg.

    
.. activecode:: console__branching_increasing3

    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    # dovrsite




.. questionnote::

    **Zadatak - srednji broj:** 
    
    Napisati program koji učitava cele brojeve *a*, *b*, *c* i odgovara na pitanje da li je *b* srednji po veličini od njih.

    
.. activecode:: console__branching_middlenum

    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    # dovrsite
    
    
.. questionnote::

    **Zadatak - čuvanje psa:** 
    
    Sa Anom i Markom živi još samo njihov pas Bobi. Njih dvoje imaju zakazana putovanja istog meseca, Ana od datuma *a1* do *a2*, a Marko od *m1* do *m2*. Oboje na put polaze ujutro, a vraćaju se uveče. Pošto ne žele da ostavljaju Bobija samog, interesuje ih da li im se putovanja preklapaju.
    
    Napisati program koji učitava cele brojeve *a1*, *a2*, *m1* i *m2*, i odgovara na pitanje da li  se Anino i Markovo putovanje preklapaju.
    
**Pomoć:** putovanja se preklapaju ako Marko odlazi pre nego što se Ana vrati (dan Markovog odlaska je manji ili jednak danu Aninog povratka) ili obrnuto, ako Ana odlazi pre nego što se Marko vrati.
    
.. activecode:: console__branching_intervals

    a1 = int(input("a1 = "))
    a2 = int(input("a2 = "))
    m1 = int(input("m1 = "))
    m2 = int(input("m2 = "))
    # dovrsite
    
    
