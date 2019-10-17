Događaji
--------

Kada očitavanje stanja nije dovoljno
''''''''''''''''''''''''''''''''''''

Na početku poglavlja o interakciji smo pomenuli da postoje dva osnovna načina da program dobije informacije o akcijama korisnika. Prvi način je očitavanje stanja miša i tastature, i taj način smo u međuvremenu upoznali.

Očitavanje stanja miša i tastature je jednostavno i dovoljno za mnoge primene. Ipak, u nekim situacijama ono nije najpogodniji način rada. Na primer, ako želimo da znamo kada je korisnik kliknuo mišem:

- pri čestom očitavanju stanja miša može se dogoditi da se u više uzastopnih očitavanja konstatuje da je taster miša dole, ali ne znamo da li je to sve isti klik ili više klikova.
- pri ređem očitavanju stanja miša može se dogoditi da nakon jednog očitavanja korisnik pritisne i otpusti taster pre sledećeg očitavanja. U takvom slučaju program neće dobiti informaciju o tom kliku.

.. commented out

    Još jedan slučaj kada očitavanje stanja nije najpogodniji način rada je kada nam je bitan redosled pritiskanja tastera. Recimo da upravljamo likom pomoću strelica. Očitavanje može da kaže da su pritisnute strelice desno i gore, ali ne može da kaže koja je pritisnuta prva. Tako ne znamo da li lik treba da ide prvo desno pa gore ili prvo gore pa desno (a desno je možda opasno polje).


Pogledajmo sledeći primer.

.. questionnote::

    **Primer - pokvareni prekidač:** 
    
    Sledeći program za svaki frejm iscrtava sliku električne šeme, a zatim preko nje slike prekidača i sijalice. Ideja je da se klikom na prekidač "uključuje i isključuje svetlo". 

Kada zadatak rešavamo tako što očitavamo stanje miša, zbog gore opisanih nedostataka bi se mogli dogoditi razni neželjeni efekti, kao što je nereagovanje na klik (suviše retko očitavanje) ili treperenje svetla (prečesto očitavanje). Čak i ako vi možete da izbegnete te neželjene efekte i normalno uključite ili isključite sijalicu, neko ko klikće brže ili sporije može da oseti problem. 

Isprobajte program klikćući različitom brzinom.

.. image:: ../../_images/Shema1_Off.png
   :width: 50px
.. image:: ../../_images/Shema1_On.png
   :width: 50px
.. image:: ../../_images/SwitchOff.png
   :width: 50px
.. image:: ../../_images/SwitchOn.png
   :width: 50px
.. image:: ../../_images/BulbOff.png
   :width: 50px
.. image:: ../../_images/BulbOn.png
   :width: 50px

.. activecode:: PyGame__interact_switch_read_state_bad
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3d_Mouse_events/Switch_read_state.py    

Informacije o promeni stanja
''''''''''''''''''''''''''''

Kao što smo u uvodu u ovo poglavlje spomenuli, akcije korisnika možemo da pratimo i na drugi način, a to je korišćenje sistemskih događaja. Događaje kojima ćemo se ovde baviti možemo da shvatimo kao **promene stanja miša i tastature** (mada ima i drugih događaja, kao što su oni generisani pomoću sistemskog časovnika). Na primer, u trenutku kada se neki taster na tastaturi ili mišu spusti, operativni sistem računara dobija signal od ulaznog uređaja i registruje to kao događaj. Slično se dešava i u trenutku otpuštanja (podizanja) tastera, promene položaja miša itd.

Svi događaji ostaju registrovani i zapamćeni, tako da se ne može dogoditi da neku akciju korisnika propustimo, kao što je slučaj kada samo očitavamo stanje.

Pajgejm biblioteka nam omogućava da za svaki događaj redom dobijemo po jedan objekat sa informacijama o tom događaju, da ispitamo o kakvom događaju se radi i da po potrebi programski reagujemo na taj događaj.

Upotreba događaja u programima
''''''''''''''''''''''''''''''

U programima koji koriste događaje pisaćemo posebnu funkciju ``obradi_dogadjaj(dogadjaj)`` (možete joj dati i drugačije ime). Ova funkcija kao argument dobija Pajgejm objekat *dogadjaj*, koji sadrži sve potrebne informacije o događaju. Ime naše funkcije za obradu događaja dodajemo kao treći argument u pozivu funkcije *pygamebg.frame_loop*. Time smo omogućili da naša funkcija *obradi_dogadjaj* bude pozvana za svaki događaj koji nastupi tokom rada programa.

Pogledajmo sada i kako konkretno obrađujemo događaj. 

U funkciji *obradi_dogadjaj* proveravamo da li je taj događaj tipa "spuštanje nekog dugmeta miša". To radimo tako što tip događaja, zapisan u ``dogadjaj.type`` poredimo sa Pajgejm konstantom ``pg.MOUSEBUTTONDOWN``, koja ima opisano značenje. 

Ako događaj jeste tipa koji nas interesuje (spuštanje tastera miša, to jest početak klika), naredbom ``mis_tacka = dogadjaj.pos`` u promenljivu *mis_tacka* smeštamo koordinate tačke na kojoj je bio miš u trenutku nastupanja događaja, jer nas zanima na šta je korisnik kliknuo.

Naredbama koje slede proveravamo dalje da li je korisnik kliknuo na prekidač, pa ako jeste menjamo vrednost logičke promenljive *ukljucen_prekidac* koja predstavlja stanje prekidača.

.. questionnote::

    **Primer - prekidač:** Ovaj program radi isto što i prethodni, ali koristi događaj spuštanja tastera miša pa nema neželjenih efekata. 
   
.. activecode:: PyGame__interact_Switch
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3d_Mouse_events/Switch.py

