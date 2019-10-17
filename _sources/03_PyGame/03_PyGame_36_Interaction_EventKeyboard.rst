Događaji tastature
------------------

Od događaja koji nastaju upotrebom tastature najvažniji je događaj spuštanja tastera, pa ćemo se njime najviše i baviti. Prilikom spuštanja tastera na tastaturi, u objektu *dogadjaj* koji predstavlja događaj u našim programima, vrednost *dogadjaj.type* će biti ``pg.KEYDOWN``.

Kada konstatujemo da je neki taster na tastaturi pritisnut, skoro uvek nas interesuje koji je to taster. Ovo možemo saznati ispitivanjem vrednosti ``dogadjaj.key``. U lekciji o očitavanju stanja tastature već smo pomenuli da za svaki taster postoji imenovana konstanta koja odgovara tom tasteru. Podsetimo se imena ovih konstanti za neke često proveravane tastere (kompletan spisak ovih konstanti možete da vidite `ovde <https://www.pygame.org/docs/ref/key.html>`__ ):

============ ==============
konstanta    taster
============ ==============
pg.K_LEFT    strelica levo
pg.K_RIGHT   strelica desno
pg.K_UP      strelica gore
pg.K_DOWN    strelica dole
pg.K_SPACE   razmak
pg.K_a       taster *a*
pg.K_b       taster *b*
pg.K_c       taster *c*
============ ==============

Vrednost polja *dogadjaj.key* govori o kom se fizičkom tasteru radi i ta vrednost je pogodna za tastere poput strelica, *Ctrl*, *Shift*, *Alt*, *Home*, *End* i sličnih. Kada se radi o tekstu, može da bude zgodnije da koristimo vrednost polja ``dogadjaj.unicode``, koja sadrži upravo otkucani znak (kao string od jednog karaktera).

Sledeći primer ilustruje kako može da se ispituje pritisak na taster, odnosno događaj tipa *pg.KEYDOWN*.

.. questionnote::

    **Primer - ukrštenica** 
    
    U ovom primeru korisnik može pomoću strelica na tastaturi da premešta okvir i da unosi slova u kvadratiće. 
    
Obratite pažnju na funkciju  *obradi_dogadjaj* u kojoj se dešava provera tipa događaja, a zatim, ako se radi o pritisku na taster, proveravaju se dodatne informacije o događaju, zapisane u poljima *dogadjaj.key* i *dogadjaj.unicode*.

Usput možete da pokušate da sastavite neke zanimljive ukrštene reči.

.. activecode:: PyGame__interact_crossword
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3e_Keyboard_events/crossword.py
    
Uporedimo ovaj program sa programom "Navigacija" iz lekcije o očitavanju stanja tastature:

=========================================================== =============================================================
U programu "Navigacija"                                     U programu "Ukrštenica"
=========================================================== =============================================================
žuti krug se kretao za po jedan piksel - klizio je          okvir se kreće za po jedno polje - skače
nismo imali preciznu kontrolu gde će se krug zaustaviti     precizno kontrolišemo gde će se okvir zaustaviti
nije nam ni bilo važno gde će se tačno krug zaustaviti      važno nam je gde će se tačno okvir zaustaviti
očitavali smo stanje tastera na tastaturi (dole ili gore)    koristimo događaj (spuštanje tastera)
=========================================================== =============================================================


.. questionnote::

    **Zadatak - navigacija po poljima** 
    
    Napišite program koji radi kao u primeru (dugme "Prikaži primer"). 
    
    Korisnik pomoću strelica na tastaturi može da vodi lika predstavljenog žutim krugom. Lik se kreće po poljima na kojima se nalaze bele tačke.
    

.. activecode:: PyGame__interact_pacman1
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3e_Keyboard_events/pacman1.py
    
    import pygame as pg, pygamebg
    br_redova, br_kolona = 10, 10
    a = 50 # velicina polja
    (sirina, visina) = (a* br_kolona, a * br_redova)
    prozor = pygamebg.open_window(sirina, visina, "Pakmen")

    (lik_red, lik_kol) = (br_redova // 2, br_kolona // 2)

    def nov_frejm():
        prozor.fill(pg.Color("black"))   # bojimo prozor u crno

        # bele kuglice
        for x in range(a // 2, sirina, a):
            for y in range(a // 2, visina, a):
                pg.draw.circle(prozor, pg.Color("white"), (x, y), 3)
       
        # OVDE DODAJTE NAREDBE ZA CRTANJE ZUTOG KRUGA
        
    def obradi_dogadjaj(dogadjaj):
        global lik_red, lik_kol
        # OVDE DODAJTE NAREDBE ZA OBRADU DOGADJAJA
        
    pygamebg.frame_loop(30, nov_frejm, obradi_dogadjaj)





.. questionnote::

    **Zadatak - pravljenje lavirinta** 
    
    Napišite program koji pravi lavitint. Crveni okvir treba da se pomera pomoću strelica, a pritiskom na razmak da se menja boja polja (iz crne u belu i obrnuto).
    
Kada rešite zadatak, isprobajte sledeće:

- kliknite na dugme "Prikaži primer" (ovaj put program iz primera radi više od onoga što je bio vaš zadatak)
- napravite lavirint kakav želite
- pritisnite (latinično) *S* za start i posmatrajte
- pritisnite (latinično) *P* za pauzu, tj. zaustavljanje ili nastavak traganja
    
.. commented out

    Ovde bi bilo idealno da učenici ne mogu da probaju pretragu pre nego što reše zadatak

.. activecode:: PyGame__interact_labyrinth
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includehsrc: src/PyGame/3_Interaction/3e_Keyboard_events/labyrinth_edit_and_search.py
    
    import pygame as pg, pygamebg, random
    a = 50 # velicina polja
    br_redova = 12
    br_kolona = 20
    (sirina, visina) = (br_kolona * a, br_redova * a)
    prozor = pygamebg.open_window(sirina, visina, "Lavirint")

    def nov_frejm():
        prozor.fill(pg.Color('white')) # bela pozadina
        for red in range(br_redova):
            for kol in range(br_kolona):
                if tabla[red][kol] == 1: # zid
                    pg.draw.rect(prozor, pg.Color('black'), (kol * a, red * a, a, a))

        # okvir
        pg.draw.rect(prozor, pg.Color('red'), (okvir_kol * a, okvir_red * a, a, a), 3)
        
    def obradi_dogadjaj(dogadjaj):
        global tabla, okvir_red, okvir_kol
        
        # OVDE DODAJTE NAREDBE ZA OBRADU PRITISAKA NA RAZMAK I STRELICE

    tabla = []
    for j in range(br_redova):
        tabla.append([])
        for i in range(br_kolona):
            tabla[-1].append(random.randint(0, 1))
            
    (okvir_red, okvir_kol) = (0, 0)
    pygamebg.frame_loop(10, nov_frejm, obradi_dogadjaj)


Bonus - program za vežbanje kucanja
'''''''''''''''''''''''''''''''''''

Program koji sledi, služi za vežbanje kucanja. Program jeste dugačak, ali trebalo bi da možete da razumete njegov veliki deo. 

Možda ćete želeti (bez obaveze) da prilagodite program svojim potrebama, naročito u početku korišćenja. Na primer:

- da usporite (ili kasnije da ubrzate) padanje slova
- da ne gubite poene kad pogrešite
- kada dobro uvežbate slova koja prva padaju, da ih izbacite iz liste slova za vežbu
- da znaci koji padaju budu samo cifre i znaci operacija (ako želite da vežbate kucanje samo na numeričkoj tastaturi desno)
- da pritisak na razmak briše najniže slovo (uz neko smanjivanje poena) 

ili bilo šta drugo čega se setite.
    
Kada budete imali vremena, svakako pokušajte i da napravite što bolji rezultat (bez varanja).

.. activecode:: PyGame__interact_typing_tutor
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3e_Keyboard_events/typing_tutor.py
