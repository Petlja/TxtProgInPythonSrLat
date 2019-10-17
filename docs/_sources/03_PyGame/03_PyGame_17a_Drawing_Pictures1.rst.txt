Prikazivanje gotovih slika
--------------------------

Crtanje osnovnih oblika može da bude zabavno, a ponekad je i izazovno. Ipak, bilo bi još zabavnije da možemo da kombinujemo svoje crtanje sa gotovim slikama ili fotografijama. U PyGame okruženju to se radi veoma jednostavno. Pogledajmo sledeći primer:

.. image:: ../../_images/tree.png
   :width: 50px

.. image:: ../../_images/apple_small.png
   :width: 50px

.. image:: ../../_images/basket.png
   :width: 50px

.. activecode:: PyGame__images_trees_and_apples1
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :includesrc: src\PyGame\1_Drawing\9_UsingImages\trees_and_apples1.py

U ovom programu nove su nam dve funkcije biblioteke PyGame:

- Funkcija :code:`pg.image.load` učitava sliku sa diska. Ovoj funkciji prosleđujemo ime fajla koji sadrži sliku (može se uključiti i putanja do fajla), a ona kao rezultat vraća sliku u obliku pogodnom za program. Taj rezultat treba da sačuvamo u nekoj promenljivoj (u primeru je to promenljiva *drvo_slika*);
- Funkcija :code:`prozor.blit` prikazuje sliku u datom prozoru. Ovoj funkciji prosleđujemo promenljivu koja sadrži sliku (rezultat funkcije *pg.image.load*) i poziciju :math:`(x, y)` u prozoru na kojoj želimo da se slika prikaže. Na poziciji koju smo zadali će se pojaviti gornji levi ugao slike. U primeru smo zadali poziciju :math:`(0, 0)`, pa se gornji levi ugao slike pojavljuje u gornjem levom uglu prozora.

Isprobajte upisivanje raznih vrednosti koordinata umesto :math:`(0, 0)` da biste bolje razumeli kako funkcioniše funkcija *blit*. Možemo da primetimo da je ovo iscrtavanje vrlo slično crtanju crteža iz više delova pomoću sidra.

Možete da isprobate i prikazivanje jedne slike na više mesta na ekranu, kao što smo to radili sa osnovnim oblicima. Dovoljno je da pozovete funkciju *blit* više puta, sa različitim vrednostima za mesto prikazivanja.

Kod prikazivanja slike na više mesta može doći do preklapanja slika. Zato treba voditi računa o redosledu prikazivanja. U našem slučaju, prvo treba prikazati drvo koje zamišljamo kao dalje, a zatim ono koje zamišljamo kao bliže. U protivnom konačna scena može izgledati nelogično, kao što pokazuje sledeća slika.

.. image:: ../../_images/PyGame/trees_and_apples_bad.png
   :width: 600px
   :align: center 
      
Objekti koje doživljavamo kao dalje su obično u gornjem delu slike, što znači da imaju manju :math:`y` koordinatu, mada ovo ne mora uvek da bude tačno. U ovom i u sličnim primerima će biti dovoljno da se držimo ovog jednostavnog pravila: **bolje je prvo prikazivati objekte sa manjom** :math:`y` **koordinatom**.

Zadaci za vežbu
'''''''''''''''

.. questionnote::

    **Zadatak - Drveće**

    U sledećem programu popravite redosled pozicija drveća u listi, tako da redosled iscrtavanja bude ispravan, a zatim dodajte u petlji naredbu za crtanje drveta na poziciji (*x*, *y*).

.. activecode:: PyGame__images_trees3
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\trees_and_apples3.py
    
    drvo_slika = pg.image.load("tree.png")  # slika drveta
    drvece_poz = [(240, 290), (400, 200), (550, 170), (120, 150), (200, 70)]
    
    prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno
    for x, y in drvece_poz:
        pass # dovrsite


.. questionnote::

    **Zadatak - Jabuke**

    Dovršite započeti program tako da crta drvo sa jabukama (kao u primeru).

.. activecode:: PyGame__images_trees2
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\trees_and_apples2.py
    
    drvo_slika = pg.image.load("tree.png")  # slika drveta
    jabuka_slika = pg.image.load("apple_small.png")  # slika jabuke
    jabuke_poz = ((43,191), (61, 158), (124, 145), (134, 175), (160, 180))
    
    # dovršite: obojte pozadinu u tamno zeleno, nacrtajte drvo i na njemu jabuke
    

Pokušajte da izmenite program tako da prikazuje drvo sa jabukama pomereno 100 piksela desno i 50 piksela niže.

.. questionnote::

    **Zadatak - Šah-mat**

    Napišite program koji crta šahovsku poziciju, kao u primeru. Nazivi fajlova sa slikama prazne table, belog kralja, belog topa i crnog kralja su redom "chess_table.png", "white_king.png", "white_rook.png", "black_king.png".

.. image:: ../../_images/chess_table.png
   :width: 50px

.. image:: ../../_images/white_king.png
   :width: 50px
    
.. image:: ../../_images/white_rook.png
   :width: 50px
   
.. image:: ../../_images/black_king.png
   :width: 50px

.. activecode:: PyGame__images_chess_mate
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\chess_mate.py
    


.. questionnote::

    **Zadatak - Voćnjak**


    U sledećem zadatku je započeto crtanje voćnjaka. Ako pokrenemo program (dugme "Pokreni program"), primetićemo neke nedoslednosti. Jedan problem je to što se jabuke nalaze samo na prvom drvetu, a treba da se nalaze na svakom drvetu, raspoređene na isti način. Osim toga, drugo drvo sleva (ispravno) preklapa krajnje levo drvo, ali ne preklapa njegove jabuke. Potrebno je da drvo koje prikazujemo ranije, prikažemo zajedno sa njegovim jabukama pre nego što pređemo na sledeće drvo.

    Ispravite program, tako da prikazuje sliku koja se dobija klikom na dugme "Prikaži primer".

.. activecode:: PyGame__images_trees_and_apples4
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :playtask:
    :includexsrc: src\PyGame\1_Drawing\9_UsingImages\trees_and_apples4.py
   
    drvo_slika = pg.image.load("tree.png")  # slika drveta
    jabuka_slika = pg.image.load("apple_small.png")  # slika jabuke
    jabuke_poz = ((43,191), (61, 158), (124, 145), (134, 175), (160, 180))
    
    prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno
    for drvo_x, drvo_y in ((0, 0), (200, 70), (120, 150), (240, 290), (550, 170), (400, 200)):
        prozor.blit(drvo_slika, (drvo_x, drvo_y))
        
    for jabuka_x, jabuka_y in jabuke_poz:
        prozor.blit(jabuka_slika, (jabuka_x, jabuka_y))


