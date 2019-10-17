Kretanje više objekata
----------------------

Do sada smo pravili animacije u kojima su se kretali razni objekti (auto, bilijarska kugla, avion, tekst), ali u svakom takvom programu kretao se samo jedan objekat. Kao globalne promenljive koje opisuju scenu koristili smo koordinate tog pokretnog objekta, a ponekad i druge veličine, na primer pomeraj, smer kretanja i slično.

Kretanje više objekata se suštinski ne razlikuje od kretanja jednog objekta, samo će biti potrebno da se prate veličine koje opisuju kretanje svih objekata. Na primer, možemo svaki objekat da predstavimo torkom vrednosti koje ga opisuju, a sve takve torke da držimo u listi.

Lopte
'''''

U sledećem primeru videćemo animirano kretanje nekoliko lopti. Svaka lopta je predstavljena torkom :math:`(x, y, dx, dy, r, boja)`, gde su :math:`x, y` koordinate centra lopte, :math:`dx, dy` su pomeraji lopte po koordinatama, :math:`r` je poluprečnik, a :math:`boja` je boja lopte. Sve takve torke su smeštene u listu *lopte*. 

Prilikom raspakivanja torke iz jednog elementa liste (naredba ``x, y, dx, dy, r, boja = lopte[i]``), kao i prilikom vraćanja u listu (naredba ``lopte[i] = (x, y, dx, dy, r, boja)``), vodimo računa o redosledu promenljivih.

U primeru se za kreiranje lopti koristi modul ``random``, koji omogućava slučajne izbore (uvezen pomoću naredbe *import*). Funkcija ``random.randint(a, b)`` vraća slučajan ceo broj između *a* i *b* (uključujući i granice), a Funkcija ``random.choice(a)`` vraća slučajan element kolekcije *a*.

.. activecode:: PyGame__anim_balls_bouncing
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2e_Anim_Multiple/balls_bouncing.py

Ako uporedimo ovaj program sa animacijom kretanja bilijarske kugle, primetićemo veliku sličnost. Funkcija *nov_frejm* se u suštini razlikuje samo po tome što se sada sve radnje (pomeranje, odbijanje, crtanje) obavljaju u petlji, pošto ih treba obaviti za svaku loptu. Zadavanje početnog stanja je takođe nešto složenije, jer ima više objekata i za svaki od njih pamtimo više podataka, a uz to koristimo i slučajne izbore.

~~~~

U prethodnom primeru svi objekti (lopte) su prisutni od početka do kraja programa. Ima situacija kada želimo da neki objekti prestanu da postoje tokom rada programa, ili da se pojave novi (ili i jedno i drugo). U takvim slučajevima možemo u funkciji *nov_frejm* da koristimo pomoćnu listu, u koju stavljamo veličine koje opisuju novo stanje. Tipičan redosled aktivnosti je sledeći:

- na početku funkcije *nov_frejm* napravimo novu praznu listu
- prolazimo kroz listu postojećih torki, menjamo ih, i one koje nam i dalje trebaju dodajemo u novu listu
- ako je potrebno, dopunimo listu novim torkama
- na kraju ažuriramo globalnu listu tako što ona dobija vrednosti iz nove, pomoćne liste

Pogledajmo primer.

Zvezde
''''''

U ovom primeru simuliramo kretanje kroz svemir. Zvezde na koje nailazimo, predstavljene su kao beli krugovi i određene su položajem i poluprečnikom. 

Za svaki frejm izračunavamo novu, pomoćnu listu koja opisuje sledeće stanje. Zvezde pomeramo po nekom pravilu, a one koje nisu potpuno izašle iz prozora prepisujemo u listu sledećeg stanja. Nakon obrade postojećih zvezda, u listu sledećeg stanja dodajemo nove zvezde da se njihov broj ukupan broj ne bi smanjivao. Na kraju sve zvezde prebacimo u globalnu listu, da bismo kasnije mogli da izračunamo i sledeći frejm.

.. activecode:: PyGame__anim_trough_stars
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2e_Anim_Multiple/trough_stars.py

Ovaj primer je dat pre svega zato da bismo na njemu pokazali drugačiji način baratanja listom torki koje opisuju scenu. Time su neki zanimljivi detalji ostali u drugom planu. Osvrnimo se malo i na te, u ovom kontekstu sporedne detalje. Da bismo dobili efekat kao da se približavamo, zvezde ispred nas treba da se razmiču i povećavaju. Zbog toga se u programu vrednosti *x* i *y* menjaju tako da se zvezde kreću u smeru od centra prozora, pri tome sve brže što su dalje od centra. 

Za učenje programiranja nije naročito važno da potpuno razumete naredbe u kojima se menjaju vrednosti *x*, *y* i *r*, ali možete da isprobate kako se animacija menja kada malo promenite koeficijente u tim naredbama (na primer, zvezde mogu da se kreću sporije, ili da rastu brže).


Zadaci
''''''

.. questionnote::

    **Pahulje:** Dovršite program tako da radi kao u primeru (dugme "Prikaži primer"). 
    
    Svaka pahulja je opisana sa samo dva broja, a to su njene koordinate, tako da su torke koje ćemo koristiti u stvari parovi :math:`(x, y)`. 
    
    Pahulje padaju za po 1 piksel, a one koje izađu iz prozora, zamenjuju se novim pahuljama. Formiranje novog stanja je slično kao u programu "zvezde", samo su pravila pomeranja pahulja jednostavnija. 
    
    Pahulje iz početnog skupa se biraju bilo gde u prozoru, a one koje se kasnije dodaju kao dopuna, biraju se negde na gornjoj ivici prozora.
    
.. image:: ../../_images/snowflake.png
   :width: 50px
    
.. activecode:: PyGame__anim_snowflakes
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2e_Anim_Multiple/snowflakes.py

    import random, pygame as pg, pygamebg
    (sirina, visina) = (800, 400)
    prozor = pygamebg.init(sirina, visina, "Pahuljice")

    pahulja_slika = pg.image.load("snowflake.png")  # slika pahuljice
    visina_slike_pahulje = pahulja_slika.get_height()
    broj_pahulja = 10                               # ukupan broj pahuljica

.. questionnote::

    **Odlazeće lopte:** Iskopirajte ovde prvi program (lopte), pa ga izmenite tako da se lopte ne odbijaju nego nastavljaju da se udaljavaju, a one koje odu zamenjuju se novim loptama. Ovaj program je kombinacija dva data primera (lopte i zvezde), pa pokušajte zato da iskoristite delove iz oba ova programa.

.. activecode:: PyGame__anim_balls_passing
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2e_Anim_Multiple/balls_passing.py


.. questionnote::

    **Klizeći tekst:** Isprobajte program i probajte da razumete kako on radi. Probajte da izmenite nešto u programu (tekst koji se prikazuje, boju kojom se tekst prikazuje, brzinu kretanja teksta, ili neki drugi detalj).
    
    Izazov: pokušajte da izmenite program tako da tekst klizi na dole umesto na gore.

.. activecode:: PyGame__anim_gliding_text
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2e_Anim_Multiple/gliding_text.py
