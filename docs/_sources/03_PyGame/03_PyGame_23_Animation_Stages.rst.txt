Animacija po fazama
-------------------

Semafor
'''''''

Jedan od najpoznatijih primera uređaja koji radi po fazama je semafor koji reguliše saobraćaj. Na primeru semafora ćemo objasniti rad po fazama i kako možemo da animiramo na računaru događanja koja se odvijaju po fazama.

Postoji nekoliko stanja u kojima semafor može da se nađe. Na primer, može da svetli crveno, da svetli trepćuće žuto, da bude isključen itd. Period u toku kojeg semafor ne menja stanje zvaćemo faza. Pri normalnom radu semafora faze se ciklično smenjuju i svaka faza ima svoje trajanje. Uzmimo kao primer semafor na kome se smenjuju sledeće četiri faze: 1 - crveno svetlo, 2 - crveno i žuto svetlo, 3 - zeleno svetlo, i 4 - žuto svetlo.

Da bi animacija bila jednostavnija, trajanje svake faze ćemo izraziti brojem frejmova (umesto sekundama). Neka su trajanja pomenutih faza :math:`n_1`, :math:`n_2`, :math:`n_3` i :math:`n_4` frejmova redom. Tada ceo ciklus traje :math:`N = n_1 + n_2 + n_3 + n_4` frejmova. Od tih :math:`N` frejmova, prvih :math:`n_1` pripada prvoj fazi, sledećih :math:`n_2` drugoj itd.

Da bismo znali kojoj fazi pripada tekući frejm, možemo da uvedemo globalnu promenljivu koja broji frejmove. Pošto ceo ciklus traje :math:`N` frejmova, dovoljno je da brojimo po modulu :math:`N`. To znači da kada brojač frejmova dostigne vrednost :math:`N-1`, sledeća vrednost je nula (brojimo samo u okviru jednog ciklusa). Pri tome, za vrednosti od 0 do :math:`n_1 - 1`, frejm pripada prvoj fazi, za vrednosti od :math:`n_1` do :math:`n_1 + n_2 - 1`, drugoj fazi, za vrednosti od :math:`n_1 + n_2` do :math:`n_1 + n_2 + n_3 - 1` trećoj, a za vrednosti od :math:`n_1 + n_2 + n_3` do :math:`N-1` četvrtoj.

Evo kako može da izgleda program napisan na osnovu ovog razmatranja:

.. activecode:: PyGame__anim_stages_traffic_lights1
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2c_Anim_Stages/TrafficLights1.py

Zadaci
''''''

.. questionnote::

    **Peta faza:** Kopirajte prethodni program, pa ubacite fazu za trepćuće zeleno svetlo posle zelenog, a pre žutog svetla (kao u primeru - dugme "Prikaži primer").

.. activecode:: PyGame__anim_stages_traffic_lights1a
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2c_Anim_Stages/TrafficLights1a.py

**Pomoć:** U petoj fazi nećemo imati jedan poziv funkcije *crtaj_semafor*, nego deo koda koji otprilike izgleda ovako:

.. code::

        if i_frejm % 2 == 0:
            crtaj_semafor(...)
        else:
            crtaj_semafor(...)

.. questionnote::

    **Avion:** Napišite program koji radi kao u primeru (dugme "Prikaži primer"). 
    
    Opis kretanja: avion polazi sa sredine leve ivice prozora. Kreće se prvo 20 frejmova po 2 piksela desno i gore, zatim 20 frejmova po 2 piksela desno i dole. Kada izađe kroz desnu ivicu prozora, pojavljuje se na istoj visini sa leve strane. Brzina prikazivanja je 50 frejmova u sekundi.

.. image:: ../../_images/airplane.png
   :width: 50px
.. image:: ../../_images/sun.png
   :width: 50px

.. activecode:: PyGame__anim_stages_plane
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2c_Anim_Stages/airplane.py
    
    import pygame as pg, pygamebg
    (sirina, visina) = (800, 350)
    prozor = pygamebg.init(sirina, visina, "Avion")

    sunce_slika = pg.image.load("sun.png")      # slika sunca
    avion_slika = pg.image.load("airplane.png") # slika aviona
    avion_sirina = avion_slika.get_width()      # sirina slike aviona
    avion_visina = avion_slika.get_height()     # visina slike aviona
    # dovrsite


.. questionnote::

    **Krtica:** Napišite program koji radi kao u primeru (dugme "Prikaži primer"). 
    
    Učitava se 10 slika na kojima krtica redom sve više viri iz rupe. Ciklus ima četiri faze, koje zajedno traju 28 frejmova. 
    
    - Prva faza traje 10 frejmova i tokom nje krtica izlazi iz rupe (prikazuju se redom slike od prve do desete).
    - Druga faza traje 5 frejmova i tokom nje krtica je u najvišem položaju (prikazuje se deseta slika).
    - Treća faza traje 10 frejmova i tokom nje krtica ulazi u rupu (prikazuju se slike od desete do prve).
    - Četvrta faza traje 3 frejma i tokom nje krtica je u rupi (prikazuje se prva slika).

.. image:: ../../_images/mole1.png
   :width: 50px
.. image:: ../../_images/mole2.png
   :width: 50px
.. image:: ../../_images/mole3.png
   :width: 50px
.. image:: ../../_images/mole4.png
   :width: 50px
.. image:: ../../_images/mole5.png
   :width: 50px
.. image:: ../../_images/mole6.png
   :width: 50px
.. image:: ../../_images/mole7.png
   :width: 50px
.. image:: ../../_images/mole8.png
   :width: 50px
.. image:: ../../_images/mole9.png
   :width: 50px
.. image:: ../../_images/mole10.png
   :width: 50px

.. activecode:: PyGame__anim_stages_mole
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2c_Anim_Stages/mole.py

    import pygame as pg, pygamebg
    (sirina, visina) = (150, 150)
    prozor = pygamebg.init(sirina, visina, "Krtica")

    slike = []   # niz koji ce da sadrzi slike
    for i in range(1, 11): # učitavamo u listu slike mole1.png, ..., mole10.png
        naziv_slike = "mole" + str(i) + ".png"  # gradimo naziv slike od delova
        slike.append(pg.image.load(naziv_slike))

    braon = (60, 42, 3)
    Y_HORIZONT = 125
    ZEMLJA = (0, Y_HORIZONT, sirina, visina - Y_HORIZONT) # deo slike ispod horizonta
    i_frejm = 0 # redni broj frejma u sekvenci

    def nov_frejm():
        # dopunite - izracunajte koja slika se prikazuje u ovom frejmu

        prozor.fill(pg.Color("skyblue"))     # bojimo pozadinu prozora u nebo-plavo
        pg.draw.rect(prozor, braon, ZEMLJA)  # bojimo pravougaonik ZEMLJA u braon
        prozor.blit(slike[i_slika], (0, 0))  # prikazujemo sliku

    pygamebg.run(10, nov_frejm)
