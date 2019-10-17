Definisanje funkcija
====================

U delu posvećenom upravljanju Karelom smo pomenuli da grupu naredbi možemo da izdvojimo u zasebnu celinu, koja se zove funkcija. Podsetimo se kako u opštem slučaju izgleda funkcija napisana na Pajtonu:


.. activecode:: Console__functions__function_def
    :passivecode: true

    def ime_funkcije(lista_argumenata):
        naredba_1
        ...
        naredba_k
        
Za pisanje funkcija na Pajtonu važe sledeća pravila:

.. infonote::

    **Pravila pisanja funkcije:**

    - Defniicija funkcije počinje rečju ``def``, iza koje sledi ime funkcije, lista argumenata u zagradama i znak ``:`` (dvotačka) na kraju reda.
    - Kao *ime_funkcije* može da se pojavi bilo koje pravilno napisano ime (pravila su ista kao za imena promenljivih).
    - Kao *lista_argumenata* može da se pojavi prazna lista (ništa) ako funkcija ne koristi argumente, ili jedan ili više argumenata razdvojenih zarezima.
    - U telu funkcije (*naredba_1*, ... *naredba_k*) mogu da se pojave bilo koje naredbe jezika Pajton. Ove naredbe se pišu uvučeno u odnosu na red koji sadrži ime i argumente funkcije.
    
Funkcije mogu a ne moraju da vrate neku vrednost. Do sada smo imali prilike da vidimo i jednu i drugu vrstu funkcija. Na primer, funkcije pomoću kojih se robot Karel pomera napred, okreće, uzima i ostavlja loptice su sve funkcije koje ne vraćaju vrednost. Sa druge strane, matematičke funkcije poput *abs* ili *round*, kao i funkcije pomoću kojih proveravamo da li Karel ima loptica kod sebe, da li ima loptica na polju i da li Karel može da ide napred su funkcije koje vraćaju vrednost.

Pisanje funkcija koje vraćaju vrednost
--------------------------------------

Da bi neka funkcija vratila vrednost, potrebno je da se u telu funkcije bar jednom navede naredba ``return``. Naredba ``return`` se sastoji od reči *return* iza koje sledi izraz čiju vrednost funkcija treba da vrati. 

.. activecode:: console__functions_return_example

    def kvadrat(x):
        return x * x
    
    print(kvadrat(3))

Naredba *return* može da se pojavi na više mesta u funkciji (obično sa različitim vrednostima), a obavezno se navodi na kraju tela funkcije. Funkcija *abs*, da nije ugrađena, mogla je biti definisana ovako:

.. activecode:: console__functions_def_abs
    :passivecode: true

    def abs(x):
        if x > 0:
            return x
        else:
            return -x
    

Funkcija može da vrati i više od jedne vrednosti. Takva je, na primer, ugrađena funkcija *divmod*, koja vraća dva broja - rezultat celobrojnog deljenja i ostatak. Funkciju *divmod* koristimo isto kao i funkcije koje vraćaju jednu vrednost, samo vraćene vrednosti smeštamo u više promenljivih:

.. activecode:: console__functions_divmod_example

    kol, ost = divmod(813, 10)
    print('Količnik je', kol, 'a ostatak', ost)

Kada pišemo funkcije koje vraćaju više vrednosti, dovoljno je da posle reči *return* navedemo vrednosti koje vraćamo, razdvojene zarezima. Kada bi trebalo da sami definišemo funkciju *divmod*, mogli bismo da je napišemo ovako:

.. activecode:: console__functions_divmod_def
    :passivecode: true

    def divmod(a, b):
        return a // b, a % b

Primer
''''''

.. questionnote::

    **Primer - krečenje:** 
    
    Za krečenje :math:`1m^{2}` zida potrebno je oko :math:`0.5kg` boje. Napisati funkciju koja kao argumente prihvata sledeća 4 argumenta:

    - dužinu sobe
    - širinu sobe
    - visinu sobe
    - dužinu koja se ne kreči (zbirna širina vrata, prozora, plakara i slično)

    Funkcija treba da vrati količinu boje (u kilogramima), potrebne za krečenje zidova i plafona.
    
    Posle funckcije napisati i program koji učitava podatke za 5 različitih prostorija, a zatim koristeći napisanu funkciju izračunava i ispisuje ukupnu količinu potrebne boje za krečenje svih pet prostorija.
    
.. activecode:: console__functions_paint2


    def kolicina_boje(a, b, h, ne_boji_se):
        pokrivnost = 0.5 # koliko kilograma za kvadratni metar
        plafon = a*b
        zidovi = h * (2*a + 2*b - ne_boji_se)
        za_krecenje = plafon + zidovi
        return za_krecenje * pokrivnost
        
    ukupno_boje = 0
    for i in range(5):
        s = input('Unesite dužinu, širinu i visinu sobe, i dužinu koja se ne kreči').split()
        ukupno_boje += kolicina_boje(float(s[0]), float(s[1]), float(s[2]), float(s[3]))

    print("Potrebno je ukupno", ukupno_boje, "kilograma boje.")  


Zadaci za vežbu:
''''''''''''''''

.. questionnote::

    **Zadatak - Geografske koordinate u obliku za GPS**
    
    Našli ste staru mapu zakopanog blaga i sa nje očitali koordinate blaga u stepenima, minutima i sekundama, ali vaš GPS uređaj podržava samo geografske koordinate kao realne brojeve stepeni. 
    
    Napišite program koji za datu koordinatu u stepenima, minutima i sekundama ispisuje realan broj stepeni.

Program je skoro sasvim napisan. Potrebno je još dodati izraz za računanje realnog broja stepeni. Da bismo (uglovne) minute pretvorili u stepene, delimo ih sa :math:`60`, a sekunde pretvaramo u stepene deljenjem sa :math:`60 \cdot 60 = 3600`.

.. activecode:: console__functions_GPS_1

   stepeni = int(input())
   minuti = int(input())
   sekunde = int(input())
   
   def st_min_sek_u_stepene(st, min, sek):
        # dovrsite funkciju
   
   realni_stepeni = st_min_sek_u_stepene(stepeni, minuti, sekunde)
   print(realni_stepeni)



.. questionnote::

    **Zadatak - Geografske koordinate u obliku za staru mapu**
    
    Pošto ste shvatili da je stara mapa iz prethodnog zadatka bila nečija šala, rešili ste da i vi nekome priredite sličnu šalu. Izabrali ste mesto u blizini i očitali koordinate sa vašeg GPS uređaja. Sada vam je potrebno da koordinate sa uređaja u realnim stepenima pretvorite u cele stepene, minute i sekunde, da biste napravili odgovarajuću "staru" mapu. 
    
    Dovršite započeti program koji obavlja ovo pretvaranje.


.. activecode:: console__functions_GPS_2

    realni_st = float(input())
    def st_min_sek(realni_stepeni):
        # dopunite funkciju tako sto cete izracunati tri vrednosti
        # koje funkcija vraca (i nakon toga uklonite komentar is sledece linije koda)
        # return celi_stepeni, celi_minuti, cele_sekunde

    celi_st, celi_min, cele_sek = st_min_sek(realni_st)
    print(celi_st, celi_min, cele_sek)


.. commented out

    .. reveal:: console__functions_GPS_2_reveal
       :showtitle: Prikaži rešenje
       :hidetitle: Sakrij rešenje

       Evo jednog mogućeg rešenja:
               
       .. activecode:: console__functions_GPS_2_solution

            realni_st = float(input())
            def st_min_sek(realni_stepeni):
                celi_stepeni = int(realni_stepeni)
                realni_minuti = (realni_stepeni - celi_stepeni) * 60
                celi_minuti = int(realni_minuti)
                realne_sekunde = (realni_minuti - celi_minuti) * 60
                cele_sekunde = round(realne_sekunde)
                return celi_stepeni, celi_minuti, cele_sekunde

            celi_st, celi_min, cele_sek = st_min_sek(realni_st)
            print(celi_st, celi_min, cele_sek)




.. questionnote::

    **Zadatak - Vodoinstalater:** 
    
    Petar je vodoinstalater i za danas ima planirane tri intervencije. Petar će za svaku intervenciju zabeležiti kada je počela i kada se završila, a na osnovu tih podataka treba izračunati koliko vremena je Petar ukupno proveo u intervencijama.
    
    Dat je delimično napisan program koji učitava vreme početka i završetka u satima i minutima za svaku Petrovu intervenciju, a zatim određuje i ispisuje ukupno vreme trajanja svih intervencija. 
    
    **Dopunite program** tako što ćete napisati funkciju *trajanje(h1, m1, h2, m2)*, koja izračunava koliko ukupno minuta protekne od *h1* sati i *m1* minuta do *h2* sati i *m2* minuta;
    
.. activecode:: console__functions_plumber

    # napisite funkciju trajanje

    def obradi_jednu_intervenciju():
        uputstvo = "Unesite sat i minut početka i sat i minut završetka intervencije "
        s1, s2, s3, s4 = input(uputstvo).split()
        h1, m1, h2, m2 = int(s1), int(s2), int(s3), int(s4)
        return trajanje(h1, m1, h2, m2)
        
    t1 = obradi_jednu_intervenciju()
    t2 = obradi_jednu_intervenciju()
    t3 = obradi_jednu_intervenciju()
    ukupno_minuta = t1 + t2 + t3
    broj_sati = ukupno_minuta // 60
    broj_minuta = ukupno_minuta % 60
    print ("Intervencije su trajale ukupno", broj_sati, "sati i", broj_minuta, "minuta")


Funkcije koje ne vraćaju vrednost
---------------------------------

Funkcije koje ne vraćaju vrednost samo obavljaju neki posao i koristimo ih kao naredbe. Takve su na primer bile funkcije *nazad()* ili *uzmi_na_susednom_polju()*, koje smo pisali u delu posvećenom Karelu. Slede primeri takvih funkcija u programu sa tekstualnim interfejsom.

.. questionnote::

    **Primer - prevoz:** 
    
    Članovima četvoročlane porodice je potrebno redom 55, 35, 40 i 20 minuta da stignu kući sa mesta na kojima se nalaze, pod uslovom da krenu kući pre 16 časova. U protivnom im treba 15 minuta više. 
    
    Napisati program koji učitava vreme polaska u satima i minutima za svakog člana porodice i ispisuje vreme stizanja kući.
    
Funkcija *obradi_clana_porodice* obavlja sve potrebne radnje za jednog člana porodice: učitava vreme polaska, na osnovu tog vremena produžava trajanje puta ako je potrebno, izračunava i ispisuje vreme stizanja kući. U glavnom programu je preostalo samo da se ova funkcija pozove za svakog člana porodice.

.. activecode:: console__functions_transport

    def obradi_clana_porodice(kojeg, trajanje_puta):
        uputstvo = 'Unesite sat i minut polaska ' + kojeg + ' člana poorodice '
        s_sat, s_min = input(uputstvo).split()
        sat_polaska, minut_polaska = int(s_sat), int(s_min)
        if sat_polaska >= 16:
            trajanje_puta = trajanje_puta + 15
        dolazak_u_minutima = sat_polaska * 60 + minut_polaska + trajanje_puta
        sat_dolaska = dolazak_u_minutima // 60
        minut_dolaska = dolazak_u_minutima % 60
        print("Vreme dolaska", kojeg, "člana kući je", sat_dolaska, "sati i", minut_dolaska, "minuta.")
        
    obradi_clana_porodice("prvog", 55)
    obradi_clana_porodice("drugog", 35)
    obradi_clana_porodice("trećeg", 40)
    obradi_clana_porodice("četvrog", 20)




Zadaci za vežbu:
''''''''''''''''

.. questionnote::

    **Zadatak - popust:** 
    
    Jedan proizvođač nudi robu po ceni od 100 dinara za komad, a za porudžbine od 50 i više komada odobrava popust od 10%. Nekoliko kupaca se najavilo da dolaze da kupe određeni broj komada. Imena kupaca i tražene količine su dati na početku programa.

    Napisati funkciju koja za dato ime kupca i količinu robe ispisuje koliko taj kupac treba da plati.

Ime kupca se ovde prosleđuje funkciji samo radi ispisivanja. Cena robe se računa na osnovu količine, koja se prosleđuje fuknciji kao drugi argument. 

.. activecode:: console__functions_discount

    # definisite funkciju ispisi_cenu

    kupci = ('Goran', 'Zdravko', 'Maja', 'Radomir')
    kolicine = (70, 28, 150, 6)
    n = len(kupci)
    for i in range(n):
        ispisi_cenu(kupci[i], kolicine[i])

.. commented out

    # ovo je bila funkcija sa vise naredbi return (ovde takav primer nedostaje)

    def ispisi_cenu(ime, kolicina):
        cena_za_komad = 100.0
        if kolicina < 50:
            cena = cena_za_komad * kolicina
        else:
            cena = 0.90 * cena_za_komad * kolicina
        print(ime, 'treba da plati', cena)

.. questionnote::

    **Zadatak - podvlačenje teksta:**

    Napisati funkciju *podvuci(tekst)*, koja zadati tekst prikazuje podvučeno. 
    
**Pomoć:** Funkcija *podvuci* treba da se sastoji od samo dve *print* naredbe. U prvoj se ispisuje dati tekst, a u drugoj linija. String koji sadrži liniju možete da dobijete množenjem stringa ``'-'`` dužinom datog stringa.


.. activecode:: console__functions_underlined_text

    # napisite funkciju podvuci
    
    podvuci("Iz Celzijusa u Farenhajte:")
    for c in range(15, 46, 5):
        print(c, '°C =', round(c * 9 / 5 + 32, 1), '°F.')
    print()
    
    podvuci("Iz Farenhajta u Celzijuse:")
    for f in range(50, 111, 10):
        print(f, '°F =', round((f-32) * 5 / 9, 1), '°C.')

.. commented out

    def podvuci(tekst):
        print(tekst)
        print('-' * len(tekst))

~~~~

Pomenimo na kraju neke od koristi koje imamo od pisanja funkcija, koje ovde zbog kratkoće naših primera i zadataka nisu mogle da dođu do izražaja:

- Funkcije se u dugačkim programima često koriste da rasterete glavni deo programa i učine ga kraćim i lakšim za razumevanje. Naši programi nisu toliko dugački da bi bilo potrebno rasterećivati glavni deo prorama, ali pokazuju kako bi to moglo da se uradi i sa dužim programima.
- Funkcije mogu da nam pomognu da izbegnemo ponavljanje istog ili sličnog koda u programima. Ponavljanje koda treba izbegavati jer se takav kod teže održava - svaku izmenu treba uneti na više mesta, što je zamorno i podložno greškama i propustima.
- Kada pišemo funkcije, omogućavamo drugima da lakše upotrebe delove našeg koda. Napisane funkcije se mogu izdvojiti u poseban modul, koji drugi programeri lako uključuju u svoje programe.
- Kod veoma velikih programa, formiranjem funkcija omogućavamo da se program rasporedi u više fajlova, umesto jednog ogromnog i nepreglednog fajla.

