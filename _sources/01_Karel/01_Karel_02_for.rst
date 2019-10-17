Skratite pisanje programa
=========================

U prethodnom poglavlju je bilo zadataka u kojima bi nam bilo zgodno da imamo skraćeni zapis za neke akcije koje se ponavljaju. Na primer, bilo je potrebno da Karel ide tri koraka napred. U slučaju samo tri koraka nije problem da napišemo naredbu ``napred()`` tri puta, međutim kada Karel treba da napravi dvanaest koraka napred, ako pišemo:

.. activecode:: Karel_for_12_steps_manual
   :passivecode: true
   
   napred(); napred(); napred(); napred(); napred()
   napred(); napred(); napred(); napred(); napred()
   napred(); napred()

u takvom načinu pisanja lakše se pogreši, a nije ni dovoljno pregledno. Ako vam izgleda da ni dvanaest nije neki problem, pomislite da u svetu programiranja nije retko da se neka naredba ponavlja i po milion puta.

Naredba for
-----------

Bolji način zadavanja ovakvog kretanja bi bio da kažemo: "dvanaest puta idi napred". Da bismo neku naredbu (ili grupu naredbi) ponovili određeni broj puta, koristimo naredbu ``for``. Najčešće korišćeni oblik ove naredbe U Pajtonu izgleda ovako:

.. activecode:: Karel_for_syntax
   :passivecode: true
   
   for i in range(n):
       naredba_1
       ...
       naredba_k

Kasnije ćemo se upoznati sa još nekim oblicima naredbe ``for``. 

Naš primer sa dvanaest ponavljanja jednog koraka napred se pomoću ``for`` naredbe može zapisati ovako:
      
.. activecode:: Karel_for_12_steps_loop
   :passivecode: true
   
   for i in range(12):
       napred()


Ovde dajemo i nešto detaljniji opis ``for`` naredbe. Ne morate ga potpuno razumeti u ovom trenutku, upotreba i pravila pisanja će postati jasniji uz primere koji slede. Kada budete želeli malo više detalja o naredbi ``for``, možete se vratiti na ovo objašnjenje (mada ono ne opisuje druge oblike *for* naredbe).


.. infonote::

   Prema pravilima pisanja programa na Pajtonu, reči ``for`` i ``in``, kao i dvotačka (znak ``:``) na kraju reda, moraju se pojaviti u zapisu ove naredbe. 
   
   - Slovo ``i`` je ovde ime za mesto na kome brojimo dokle smo stigli sa ponavljanjem, pa umesto ``i`` može da stoji i neko drugo ime (vratićemo se na ovo kad nam zatreba). 
   - Zapis ``range(n)`` predstavlja opseg celih brojeva počevši od 0, a ``n`` govori koliko brojeva sadrži taj opseg. Na primer ``range(3)`` je opseg koji sadrži brojeve :code:`0, 1, 2`, a ``range(7)`` je opseg sa brojevima :code:`0, 1, 2, 3, 4, 5, 6`.
   - Naredbe u sledećim redovima čine takozvano **telo for naredbe**. To mogu biti bilo koje naredbe na Pajtonu, uključujući naredbe za kretanje Karela, druge naredbe ``for``, ili neke naredbe koje još nismo pomenuli. Može ih biti jedna ili više. 
   
   Zapis ``for i in range(3)`` bi trebalo čitati: "za ``i`` u opsegu [0, 1, 2]". To znači da će se naredbe u telu for naredbe izvršiti po jedanput za i=0, i=1, i=2, dakle ukupno tri puta. Mi u telu for naredbe za sada nećemo koristiti vrednost i, tako da nam je bitno samo koliko opseg ima vrednosti (broj iza ``range`` u zagradi), jer će se telo for naredbe toliko puta izvršiti.
   
   Da bi bilo jasno koje naredbe čine telo for naredbe, te naredbe se pišu uvučeno (pomereno u desno), i to sve za isti broj razmaka. Možemo sami da odaberemo koliko razmaka koristimo za uvlačenje naredbi u telu *for* naredbe. Bilo bi dobro da to uvek bude isti broj, jer ćemo tako navići da određeni izgled programa i lakše ga čitati. Najčešće je to 4 razmaka, pa ćemo i mi uvlačiti telo *for* naredbe za četiri mesta.


Naredba ``for`` se često zove i naredba ponavljanja. Takođe je poznata i kao petlja (engl. loop), jer kretanjem u programu po naredbama koje izvršavamo, kad naiđemo na naredbu ``for`` kružimo određeni broj puta po naredbama u njenom telu, to jest pravimo petlju. 
Izrazi "petlja" ili "naredba ponavljanja" su manje precizni, jer kao što ćemo uskoro videti, naredba for nije jedina petlja, odnosno naredba ponavljanja. Reč "petlja" obično koristimo kada je jasno (ili nebitno) o kojoj naredbi govorimo, jer lakše je reći na primer "telo petlje", nego "telo for naredbe".

Zadaci za vežbu
---------------

Pomeri se petnaest polja napred i uzmi lopticu
''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Napiši program na osnovu kojega će se Karel pomeriti na polje (16, 1) i pokupiti lopticu.

U prostoru za rešavanje vas čeka duži (i ružniji) program. Pokušajte da ga zamenite ``for`` naredbom. U slučaju da vam rešenje sa ``for`` naredbom ne proradi (što se u početku često dešava), rešenje možete da vidite kada kliknete na dugme "Rešenje" ispod.

.. karel:: Karel_for_15_steps_and_take
   :blockly:

   {
      setup:function() {
          var world = new World(16, 1);
          world.setRobotStartAvenue(1);
          world.setRobotStartStreet(1);
          world.setRobotStartDirection("E");
          world.putBall(16, 1);
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                  "napred(); napred(); napred(); napred(); napred()",
                  "napred(); napred(); napred(); napred(); napred()",
                  "napred(); napred(); napred(); napred(); napred()",
                  "uzmi()"];
                  
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() === 1;
      }
   }

.. reveal:: Karel_for_15_steps_and_take_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_for_15_steps_and_take_solution
      :passivecode: true
      
      from karel import *
      for i in range(15):
          napred()
      uzmi()

      
Idi jedno polje napred i pokupi 10 loptica
''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Ispred Karela je tačno jedno polje, a na njemu 14 loptica. Karel treba da ih pokupi tačno deset.
  
.. karel:: Karel_for_one_square_take_10_balls
   :blockly:

   {
        setup:function() {
           var world = new World(2, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           world.putBalls(2, 1, 14);

           var robot = new Robot();

           var code = ["from karel import *",
                       "napred()",
                       "# dovrsite program",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == 10;
        },
   }
   
.. reveal:: Karel_for_one_square_take_10_balls_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_for_one_square_take_10_balls_solution
      :passivecode: true
      
      from karel import *
      napred()
      for i in range(10):
          uzmi()


Uzimaj po jednu lopticu na narednih 8 polja
'''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Ispred Karela je osam polja, a na svakom od njih po jedna loptica. Karel treba da pokupi sve loptice.
  
Primetite da sada u for petlji treba uraditi dve stvari: koraknuti napred i uzeti lopticu.

.. karel:: Karel_for_EightSquaresOneBallEach_TakeAllBalls
   :blockly:

   {
        setup:function() {
           var numAvenues = 9;
           var world = new World(numAvenues, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
         for (var k = 2; k <= numAvenues; k++)
            world.putBall(k, 1);

           var robot = new Robot();

           var code = ["from karel import *",
                       "# dovrsite program",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == world.getAvenues() - 1;
        },
   }
   
.. reveal:: Karel_for_EightSquaresOneBallEach_TakeAllBalls_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_for_EightSquaresOneBallEach_TakeAllBalls_solution
      :passivecode: true
      
      from karel import *
      for i in range(8):
          napred()
          uzmi()


Pokupi po 5 loptica sa naredna tri polja
''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Ispred Karela su tri polja, a na svakom od njih po pet loptica. Karel treba da pokupi sve loptice.

  
.. karel:: Karel_for_Take_5_5_5
   :blockly:

   {
        setup:function() {
           var world = new World(4, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           world.putBalls(2, 1, 5);
           world.putBalls(3, 1, 5);
           world.putBalls(4, 1, 5);
           
           var robot = new Robot();

           var code = ["from karel import *",
                       "# dovrsite program",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == 15;
        },
   }
   
.. reveal:: Karel_for_Take_5_5_5_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje
   
   .. activecode:: Karel_for_Take_5_5_5_solution
      :passivecode: true
      
      from karel import *
      napred()
      for i in range(5):
          uzmi()
      napred()
      for i in range(5):
          uzmi()
      napred()
      for i in range(5):
          uzmi()

