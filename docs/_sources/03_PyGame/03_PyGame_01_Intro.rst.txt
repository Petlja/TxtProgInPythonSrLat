Biblioteka PyGame
=================

Pretpostavljamo da ste već upoznali Pajton kao jezik i da znate šta su izrazi (konstante, promenljive, operatori), naredbe (``if``, ``if-else``, ``if-elif-else``, ``for``), funkcije (one ugrađene poput ``min`` ili ``abs`` i one koje sami definišete pomoću ``def``), stringovi (``"Zdravo"`` tj. ``'Zdravo'``), liste (poput ``[1, 2, 3]``), torke (poput ``(3, 4)``) i slično. 

Pisanje programa na Pajtonu ćemo sada nastaviti da vežbamo koristeći grafičku biblioteku PyGame. Odabrali smo ovu biblioteku jer ona nudi mogućnost da se uz relativno malo programiranja dođe do zanimljivih rezultata, koji uključuju crtanje, animaciju i interakciju programa sa korsnikom. Prema tome, cilj našeg bavljenja bibliotekom PyGame je da nastavite da uvežbavate svoju veštinu programiranja na zabavan način. Takođe, čitaoci koji se više zainteresuju za programiranje, dobiće mnoge prilike da dorađuju date programe i inspiraciju za razne samostale projekte.

O biblioteci PyGame
-------------------

Biblioteka `PyGame <http://pygame.org>`__ se razvija još od ranih 2000. godina. Sami autori kažu da nije u pitanju najbolja biblioteka za programiranje igara (nije ni druga, pa ni treća po
kvalitetu), ali glavna prednost joj je to što je jednostavnja o ddrugih za korišćenje i pogodna je za učenje programiranja kroz interesantan svet računarske grafike i računarskih igara.


Korišćenje onlajn
-----------------

Da bismo vam olakšali prve korake, u priručniku koji upravo čitate spremili smo vam okruženje u kojem možete da pišete i testirate jednostavne PyGame programe. Spremili smo i pregršt primera i zadataka u kojima, kao i u prethodenim poglavljima, treba uglavnom da dovršite ili popravite započete programe da bi oni potpuno proradili. Da biste ovo okruženje mogli da koristite, nije potrebno da instalirate ništa dodatno na svoj računar.  Ipak, ako želite da s emalo ozbiljnije pozabavite programiranjem (na primer, želite da napravite svoju igricu), preporučujemo da biblioteku instalirate na svoj računar i koristite je iz okruženja za razvoj Python programa (na primer, IDLE), nezavisno od pregledača veba i ovog priručnika. Programiranje u pravom okruženju za razvoj je udobnije i efikasnije, lakše je pronalaziti greške u programu itd.

Instalacija
-----------

Da biste u vašem okruženju za razvoj programa mogli da pokrećete programe koji su napisani uz korišćenje biblioteke PyGame, potrebno je prethodno instalirati ovu biblioteku. Preduslov je, naravno, da na računaru imate instaliran Pajton (poželjno je verziju 3.6 ili noviju). Ako to do sada niste uradili, onda prvo posetite sajt `<https://www.python.org>`__ i sa njega preuzmite najnoviju verziju jezika Pajton i okruženja za rad sa njim (one se obično nalaze u sekciji Downloads, u podsekciji posvećenoj operativnom sistemu koji koristite).

Kada je na računar instaliran Pajton, možemo preći na instalaciju biblioteke PyGame. To je zaista veoma jednostavno. Dovoljno je da u komandnoj liniji otkucate ``pip3 install pygame``. Komandnu liniju pokrećete najlakše tako što držeći taster ``windows`` pritisnete taster ``r`` i onda otkucate ``cmd``. Ukoliko dobijete poruku da komanda ``pip3`` ne postoji, onda probajte sa ``py -3 -m pip install pygame``. 

Kada izvršite instalaciju, najbolje je da odmah testirate da je sve proteklo kako treba tako što ćete:

* pokrenuti Pajton razvojno okruženje IDLE koje je instalirano kao windows apkikacija

* u razvojnom okruženju IDLE otvoriti novi projekat (opcija File/New)

* u editoru koji se pojavi otkucati program koji je prikazan dalje u tekstu (možete odatle da ga iskopirate i samo nalepite u editor okruženja IDLE)

* snimiti program u fajl pre pokretanja (opcija File/Save as...)

* pokrenuti program (opcija Run/Run Module u meniju, ili taster F5)


Nakon pokretanja programa treba da se pojavi prozor u kojem je nacrtan jedan kvadrat i koji stoji prikazan tri sekunde.

.. activecode:: PyGame__check_install
   :nocodelens:
   :modaloutput: 
   :enablecopy:

   import pygame
   pygame.init()
   prozor = pygame.display.set_mode((200, 200))
   prozor.fill(pygame.Color("white"))
   pygame.draw.rect(prozor, pygame.Color("black"), (20, 20, 160, 160), 5)
   pygame.display.update()
   pygame.time.wait(3000)
   pygame.quit()

I ostale primere iz priručnika možete da izvršavate kod sebe na računaru, što i preporučujemo da uradite bar ponekad.

