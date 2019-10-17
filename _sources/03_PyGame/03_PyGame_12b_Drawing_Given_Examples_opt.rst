Crtanje zadatih crteža - dodatni primeri
----------------------------------------

Pretpostavljamo da ste već stekli određenu veštinu očitavanja koordinata i pozivanja funkcija za crtanje osnovnih oblika. Zato će se u narednim zadacima pojaviti novi izazov. 

Na mnogim crtežima postoji neka pravilnost, na primer osna simetrija ili deo crteža koji se ponavlja. Ako poželite da sami napravite neki takav crtež, da bi on dobro izgedao, ne možete da izaberete sve tačke potpuno slobodno. Umesto toga, neke tačke treba da izaberete, a neke treba da izračunate. 

Da bismo se približili pravljenju slika koje samostalno osmišljamo, način zadavanja crteža je malo izmenjen. Crteži su i dalje zadati pomoću programa - primera koji crta sliku (postoji izreka da jedna slika vredi 1000 reči). Novo je to što na pojedinim delovima slike neće biti moguće da se očita jedna ili obe koordinate, već je potrebno da te koordinate izračunate na osnovu poznatih koordinata.

Osim toga što je potrebno i malo računanja, crteži u zadacima koji slede sadrže i više detalja pa je za njihovu izradu potrebno nešto više vremena. 

Ograda
''''''

U ovom zadatku očitavanje :math:`x` koordinata je ograničeno na prvu pritku ograde i prvi razmak. Sve ostale potrebne koordinate se mogu izračunati.

.. activecode:: PyGame__drawing_fence
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src\PyGame\1_Drawing\4_ByGrid_Additional\fence_assist.py
   
.. reveal:: PyGame__drawing_fence_reveal
   :showtitle: Prikaži rešenje
   :hidetitle: Sakrij rešenje

   Dat je kompletan program, možete da ga isprobate i ovde.
	       
   .. activecode:: PyGame__drawing_fence_solution
      :nocodelens:
      :enablecopy:
      :modaloutput:
      :includesrc: src\PyGame\1_Drawing\4_ByGrid_Additional\fence.py

Zgrada
''''''

Svi prozori zgrade su iste veličine, razmaci između spratova su jednaki, a leva i desna strana zgrade su simetrične jedna drugoj (osim što simetrični prozori ne moraju biti iste boje). Iskoristite ove podatke da biste izračunali koordinate koje ne možete da očitate.

.. activecode:: PyGame__drawing_building
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src\PyGame\1_Drawing\4_ByGrid_Additional\building_assist.py
   
.. commented out 

    .. reveal:: PyGame__drawing_building_reveal
       :showtitle: Prikaži rešenje
       :hidetitle: Sakrij rešenje

       Dat je kompletan program, možete da ga isprobate i ovde.
               
       .. activecode:: PyGame__drawing_building_solution
          :nocodelens:
          :enablecopy:
          :modaloutput:
          :includesrc: src\PyGame\1_Drawing\4_ByGrid_Additional\building.py

Čiča Gliša
''''''''''

U ovom primeru ne mogu da se očitaju koordinate tačaka na desnoj nozi, ali je ona simetrična levoj. Pošto je širina slike poznata (pogledajte početak programa), koordinate dveju nepoznatih tačaka na desnoj strani se mogu izračunati na osnovu poznatih simetričnih tačaka sa leve strane.

**Pomoć:** Neka je :math:`A` tačka na levoj strani slike, a :math:`B` tačka na desnoj strani slike, simetrična tački :math:`A`. Te dve tačke onda imaju istu :math:`y` koordinatu, a zbir :math:`x` koordinata tačaka :math:`A` i :math:`B` jednak je širini slike.

.. activecode:: PyGame__drawing_stickman
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src\PyGame\1_Drawing\4_ByGrid_Additional\stickman_assist.py
   
.. commented out 

    .. reveal:: PyGame__drawing_stickman_reveal
       :showtitle: Prikaži rešenje
       :hidetitle: Sakrij rešenje

       Dat je kompletan program, možete da ga isprobate i ovde.
               
       .. activecode:: PyGame__drawing_stickman_solution
          :nocodelens:
          :enablecopy:
          :modaloutput:
          :includesrc: src\PyGame\1_Drawing\4_ByGrid_Additional\stickman.py

Mačka
'''''

Uši ove mačke mogu da se prikažu kao popunjeni trouglovi. Kako se uši nadovezuju na glavu, po dva temena svakog trougla mogu da budu izabrana sa više slobode (dovoljno je da budu negde u glavi). Osim dva trougla koji predstavljaju uši, imamo još:

- dva kruga (glava i vrh njuške)
- šest elipsi (oči, zenice i delovi njuške)
- šest linija (brkovi)

:math:`x` koordinate na desnoj strani slike se ne mogu očitavati, ali se mogu izračunati koristeći simetriju (i poznatu širinu slike - pogledajte početak programa). 

**Napomena:** Postupak određivanja parametara elipse na desnoj strani malo se razlikuje od onog za krug ili duž. Treba voditi računa o tome da je gornje **levo** teme pravougaonika opisanog oko tražene elipse u stvari slika gornjeg **desnog** temena pravougaonika opisanog oko poznate elipse. To znači da kada odredimo parametre *(x, y, w, h)* elipse na levoj strani, parametri njoj simemtrične elipse na desnoj strani su *(sirina - x - w, y, w, h)*, gde je *sirina* širina prozora, *x*, *y* su koordinate gornjeg levog temena pravougaonika oko leve elipse, a *w* i *h* su širina i visina (obe) elipse.

.. activecode:: PyGame__drawing_cat
   :nocodelens:
   :enablecopy:
   :modaloutput:
   :playtask:
   :includexsrc: src\PyGame\1_Drawing\4_ByGrid_Additional\cat_assist.py

.. reveal:: PyGame__drawing_cat_reveal
   :showtitle: Prikaži rešenje
   :hidetitle: Sakrij rešenje

   Dat je kompletan program, možete da ga isprobate i ovde.
	       
   .. activecode:: PyGame__drawing_cat_solution
      :nocodelens:
      :enablecopy:
      :modaloutput:
      :includesrc: src\PyGame\1_Drawing\4_ByGrid_Additional\cat.py

