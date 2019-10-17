Očitavanje tastera miša
-----------------------

Informaciju o trenutno pritisnutim tasterima miša daje nam funkcija ``pg.mouse.get_pressed()``. Ova funkcija vraća torku od tri elementa (uređenu trojku), koji se koriste kao logičke vrednosti. Elementi torke redom odgovaraju levom, srednjem i desnom tasteru miša. Vrednost *True* označava da je taster pritisnut, a *False* da nije.

Primer naveden niže pokazuje kako se očitava koji tasteri miša su pritisnuti. Ovako izgleda deo programa u kome se to dešava:

.. activecode:: PyGame__interact_put_ball_into_box_part
    :passivecode: true

    pritisnut_taster_misa = pg.mouse.get_pressed()
    
    if pritisnut_taster_misa[2]: # desni taster - nova igra
        (x, y) = (sirina//2, visina//2) # vracamo lopticu u centar
        pobedio, izgubio = False, False # igrac nije ni pobedio ni izgubio
        
    if pritisnut_taster_misa[0]: # levi taster - pomeri lopticu
        (xm, ym) = pg.mouse.get_pos() # koordinate pozicije misa
        # loptica se pomera od misa za jos pola tog rastojanja
        x = x - 0.5 * (xm - x)
        y = y - 0.5 * (ym - y)

Torka *pritisnut_taster_misa* dobija tri vrednosti koje je vratila funkcija *pg.mouse.get_pressed()*. Te vrednosti kasnije tipično koristimo u *if* naredbama. Na primer, *if pritisnut_taster_misa[2]* znači "ako je pritisnut desni taster" (0 za levi, 1 za srednji, a 2 za desni).

Primeri i zadaci
''''''''''''''''

.. questionnote::

    **Primer - ubaci lopticu:** Dok je levi taster miša pritisnut, loptica se udaljava od miša. Cilj je pomeranjem miša i pritiskanjem levog tastera postići da loptica bude u crvenom okviru. Pritiskom na desni taster igra se vraća na početak.
    
Najpre pažljivo pogledajte funkciju *nov_frejm()*, a zatim i ostale delove programa. Isprobajte program i proverite da li on radi onako kako ste očekivali na osnovu čitanja.
    
.. activecode:: PyGame__interact_put_ball_into_box
    :nocodelens:
    :enablecopy:
    :modaloutput:
    :includesrc: src/PyGame/3_Interaction/3b_Mouse_readkey/put_ball_into_box.py    



.. questionnote::

    **Zadatak - ka i od miša:** Dovršite program, tako da radi kao u primeru (dugme "Prikaži primer").
    
    - Kada je levi taster miša pritisnut, loptica treba da se udaljava od miša, kao u primeru "ubaci lopticu" datom iznad, ali ne za po pola rastojanja, nego samo za po deseti deo rastojanja do miša. 
    - Kada levi taster miša nije pritisnut, loptica treba da se pibližava za po deseti deo rastojanja do miša (kao u zadatku "prema mišu" iz prethodne lekcije).
    
.. activecode:: PyGame__interact_to_and_from_mouse
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3b_Mouse_readkey/to_and_from_mouse.py
    
    import pygame as pg, pygamebg
    (sirina, visina) = (400, 400)
    prozor = pygamebg.open_window(sirina, visina, "Ka i od miša")

    (x, y) = (sirina // 2, visina // 2) # loptica krece iz centra

    def nov_frejm():
        global x, y
        
        # DODAJTE DEO KOJI NEDOSTAJE
        
        # crtamo zelenu lopticu na beloj pozadini
        prozor.fill(pg.Color("white")) 
        pg.draw.circle(prozor, pg.Color("green"), (int(x), int(y)), 10)

    pygamebg.frame_loop(50, nov_frejm)


.. questionnote::

    **Zadatak - laser:** Dovršite program tako da radi kao u primeru (dugme "Prikaži primer").
    
    Dok je levi taster miša pritisnut, "laser" je uključen, inače je isključen. Dok je laser uključen, energija mu se smanjuje za po 1 (ali ne ispod 0), a kad je isključen energija se povećava za po 2 (ali ne preko 100).
    

.. activecode:: PyGame__interact_laser
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/3_Interaction/3b_Mouse_readkey/laser.py

    import pygame as pg, pygamebg
    sirina, visina = 400, 400
    prozor = pygamebg.open_window(sirina, visina, "Laser")

    laser_ukljucen = False
    energija = 25 # koliko je laser pun od 0 do 100 

    def crtanje():
        prozor.fill(pg.Color("black")) # pozadina
        
        # indikator pokazuje koliko je laser pun
        pg.draw.rect(prozor, pg.Color("green"), (10, 10, 100, 10), 1)
        pg.draw.rect(prozor, pg.Color("green"), (10, 10, energija, 10))
        
        if laser_ukljucen:
            domet = (4 * energija, visina - 4 * energija)
            pg.draw.line(prozor, pg.Color("red"), (0, visina), domet, 5)

    def nov_frejm():
        global energija, laser_ukljucen
        
        # OCITAJTE STANJE LEVOG TASTERA MISA I POSTAVITE VREDNOSTI 
        # GLOBALNIH PROMENLJIVIH energija, laser_ukljucen

        crtanje()

    pygamebg.frame_loop(15, nov_frejm)


.. commented out

    .. questionnote::

        **Zadatak - boja pozadine:** Ovaj jednostavan primer samo ilustruje očitavanje stanja tastera miša. Dok je pritisnut levi taster pozadina postaje svetlija, a dok je pritisnut desni taster pozadina postaje tamnija.
        

    .. activecode:: PyGame__interact_bg_color
        :nocodelens:
        :modaloutput:
        :includesrc: src/PyGame/3_Interaction/3b_Mouse_readkey/bg_color.py




