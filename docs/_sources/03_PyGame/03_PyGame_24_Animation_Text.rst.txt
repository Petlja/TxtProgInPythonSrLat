Crtanje teksta
--------------

Programi koji crtaju, često uz slike ispisuju i razne poruke (verovatno ste i sami videli mnogo primera). Evo kako se to radi u PajGejmu:

.. activecode:: PyGame__anim_text
    :nocodelens:
    :modaloutput:
    :includesrc: src/PyGame/2_Animation/2d_Anim_Text/text_example.py

Kao što se vidi iz primera, da bi tekst mogao da bude prikazan, **prvo treba kreirati objekat koji predstavlja font**. Za to se koristi funkcija ``pg.font.SysFont``, kojoj zadajemo vrstu i veličinu slova. Možemo da napravimo i više ovakvih objekata u slučaju da nameravamo da pišemo slovima različitih veličina ili tipova, a često nam je dovoljan i samo jedan font. 

Nakon pravljenja fonta, svaki put kada želimo da prikažemo neki tekst, ponavljamo sledeća dva koraka:

- Prvi korak je **da se napravi slika koja sadrži željeni tekst.** To postižemo pomoću funkcije ``font.render``, gde je *font* objekat fonta kreiran na početku. Parametri funkcije *font.render* su redom tekst koji se prikazuje, logička vrednost koja određuje da li će se crtati lepšim linijama (tj. koristiti takozvana tehnika antialijasinga) i na kraju boja kojom će se tekst ispisivati.
- Drugi korak je isti kao kod prikazivanja bilo koje gotove slike - **prikazujemo sliku dobijenu u prethodnom koraku** na poziciji koju odaberemo. Pri tome za računanje pozicije možemo po potrebi (kao u primeru) da koristimo veličinu slike.

Zadaci - svetleće reklame
'''''''''''''''''''''''''

Sigurno ste viđali svetleće reklame sa neonskim cevima u obliku slova. One privlače pažnju tako što se različite grupe slova uključuju i isključuju nekim zadatim redosledom koji se ponavlja. Sledi nekoliko primera inspirisanih takvim svetlećim reklamama.


.. questionnote::

    **Trepereći tekst:** Napišite program koji prikazuje trepereći tekst, slično kao u primeru (dugme "Prikaži primer"). 
    
    Ako želite, možete da promenite tekst, njegovu boju i veličinu, font, učestalost uključivanja i isključivanja, ili bilo šta drugo. Ako želite da što približnije oponašate naš program, on koristi slova tipa "Arial" veličine 80, a prikazuje tekst u svakom drugom frejmu, centriran, pri brzini od 3 frejma u sekundi.
    
**Pomoć:** Od globalnih promenljivih koje opisuju scenu, dovoljna je jedna logička promenljiva koja govori da li treba prikazati dati tekst. Ovoj promenljivoj ćemo u funkciji *nov_frejm()* menjati vrednost, tako da ona ima vrednost *True* u svakom drugom frejmu.

.. activecode:: PyGame__anim_neon1
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2d_Anim_Text/neon_sign1.py

    import pygame as pg, pygamebg
    tekst = "PAJTON"
    (sirina, visina) = (len(tekst) * 70, 100)
    prozor = pygamebg.init(sirina, visina, "Reklama")
    
.. reveal:: PyGame__anim_neon1_reveal
   :showtitle: Prikaži rešenje
   :hidetitle: Sakrij rešenje

    .. activecode:: PyGame__anim_neon1_solution
        :nocodelens:
        :modaloutput:
        :includesrc: src/PyGame/2_Animation/2d_Anim_Text/neon_sign1.py

.. questionnote::

    **Dodavanje slova:** Probajte sada da imitirate ovaj primer. U prvom frejmu se prikazuje samo prvo slovo, a u svakom sledećem po jedno slovo više dok se ne prikažu sva slova. Nakon toga sledi jedan frejm u kome se ne prikazuje ništa, pa tri frejma sa svim uključenim slovima, a zatim se sve ponavlja. Brzina prikazivanja u našem programu je 2 frejma u sekundi.

**Pomoć:** evo nekih komentara koji mogu da pomognu pri rešavanju zadatka

- Iz opisa (i posmatranja primera) možemo da zaključimo da pun ciklus sadrži četiri frejma više nego što ima slova u tekstu. 
- Potrebnu veličinu prozora možemo da odredimo na osnovu dužine teksta, kao u prethodnom primeru.
- Tekst se uvek prikazuje na istoj poziciji (isti je gornji levi ugao teksta). Prema tome, poziciju možemo da izračunamo jednom, u glavnom delu programa.
- Možemo da koristimo brojač frejmova kao globalnu promenljivu, pa u funkciji *nov_frejm()* pomoću *if* naredbi da na osnovu vrednosti brojača ustanovimo da li i koji deo teksta treba prikazati.

.. activecode:: PyGame__anim_neon2
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2d_Anim_Text/neon_sign2.py

.. questionnote::

    **Pojedinačna slova:** U ovom primeru se prvo prikazuje svako slovo posebno, a zatim se sva slova 3 puta uključe i isključe. Možete li da ponovite ovo ponašanje?

**Pomoć:** pozicije prikazivanja pojedinih slova su redom (0, 0), (50, 0), (100, 0), (150, 0) itd. Broj frejmova u ciklusu je za 6 veći od broja slova u tekstu. Ostale ideje su vrlo slične onima iz prethodnih primera.

.. activecode:: PyGame__anim_neon3
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2d_Anim_Text/neon_sign3.py

.. questionnote::

    **Pokretna slova:** Ovaj primer je drugačiji po tome što se slova pomeraju. Pokušajte i njega da realizujete.
    
**Pomoć:** Jednom kada formirate sliku od datog teksta, zadatak postaje vrlo sličan zadatku sa autom koji se kreće.

.. activecode:: PyGame__anim_neon4
    :nocodelens:
    :modaloutput:
    :playtask:
    :includehsrc: src/PyGame/2_Animation/2d_Anim_Text/neon_sign4.py


Na kraju, ako želite, ovde možete da napravite svetleću reklamu po vašoj želji.

.. activecode:: PyGame__anim_neon5
    :nocodelens:
    :modaloutput:
