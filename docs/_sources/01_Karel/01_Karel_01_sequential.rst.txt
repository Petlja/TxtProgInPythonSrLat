Odmakni

~~~~

Upravljanje Karelom
===================

Da biste videli kako programiranje izgleda, upoznaćemo vas sa Karelom. Karel je animirani robot, koji se kreće po tabeli nalik lavirintu tako što prati naša uputstva u obliku programa. Kroz upravljanje Karelom usvojićemo logiku koja je veoma bitna za pisanje bilo kakvih programa, a možemo se usput i zabaviti.

.. infonote::

    Ideja o učenju programiranja kroz upravljanje robotom potiče još iz sedamdesetih godina 20-tog veka, kada je Ričard Patis (Richard E. Pattis) kao postdiplomac na univerzitetu Stenford napravio prvo takvo okruženje i osmislio specijalan jezik za tu svrhu. Jezik je, kao i robot, nazvan Karel, po Karelu Čapeku, češkom piscu koji je prvi počeo da koristi reč robot. Patisova knjiga *Robot Karel: laki uvod u umetnost programiranja* (*Karel The Robot: A Gentle Introduction to the Art of Programming*) je objavljena 1981. godine i brzo je postala najbolje prodavana uvodna knjiga u programerske kurseve.


Za upravljanje Karelom možemo koristiti ove funkcije:

- ``napred()`` - pomeri se jedno polje napred,
- ``levo()`` - okreni se 90 stepeni nalevo (u smeru suprotnom kazaljki na satu),
- ``desno()`` - okreni se 90 stepeni nadesno (u smeru kazaljke na satu),
- ``uzmi()`` - pokupi lopticu sa polja na kojem se nalaziš,
- ``ostavi()`` - spusti lopticu na polje na kojem se nalaziš.

Ovih pet funkcija koristimo kao komande upućene Karelu. Karel razume još pet nešto drukčijih funkcija, koje ćemo videti uskoro. Pored ovih komandi upućenih direktno Karelu, možemo da koristimo i sve naredbe programskog jezika Pajton, koji ćemo usput upoznavati. 

Pogledajmo kroz primere kako gore navedene naredbe možemo da koristimo da bismo vodili Karela kroz njegov svet:

Primeri
-------

Pomeri se jedno polje napred i uzmi lopticu
'''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Napišite program na osnovu kojega će se Karel pomeriti na polje (2, 1) i pokupiti lopticu.

Ovaj program se sastoji od samo dve naredbe. Prva kaže Karelu da se pomeri jedno polje napred, a druga da uzme lopticu.
   
.. karel:: Karel_intro_two_squares_one_ball
   :blockly:

   {
        setup:function() {
            var world = new World(2, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(2, 1);

        var robot = new Robot();

        var code = ["from karel import *",
                    "napred()",
                    "uzmi()"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 1;
        },
   }

**Priključivanje biblioteke** *karel*
'''''''''''''''''''''''''''''''''''''

.. infonote::

    Naredbe pomoću kojih upravljamo Karelom nalaze se u biblioteci *karel*. Zato na početku programa treba da kažemo računaru (tačnije programu koji izvršava naš program) da prvo priključi definicije komandi za upravljanje Karelom. To se postiže prvom linijom programa: ``from karel import *``. Svaki naš program koji se bavi Karelom, treba da počne ovako.
   
    Imajte na umu da biblioteka *karel* za sada može da se koristi samo u ovom okruženju. Ostale programe koje budete pisali možete pokretati i na druge načine, ali na to ćemo vas podsetiti kada za to bude vreme.

Na jednom polju može biti i više loptica, a naš zadatak može biti da kažemo Karelu da ih uzme nekoliko ili sve.

Pomeri se jedno polje napred i uzmi tri loptice
'''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Napišite program na osnovu kojega će se Karel pomeriti na polje (2, 1) i pokupiti tri od pet loptica koje se tamo nalaze.

U ovom programu nakon naredbe ``napred()``, naredbu ``uzmi()`` treba navesti tri puta, jer treba pokupiti tri loptice. Obratite pažnju na broj koji se pojavljuje na loptici. On pokazuje koliko loptica ima na tom polju. Osim toga, broj levo od Karelove glave (koji ste možda primetili i u prethodnom primeru), govori koliko loptica Karel ima kod sebe.
   
.. karel:: Karel_intro_two_squares_five_balls
   :blockly:

   {
        setup:function() {
            var world = new World(2, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBalls(2, 1, 5);

        var robot = new Robot();

        var code = ["from karel import *",
                    "napred()",
                    "uzmi()",
                    "uzmi()",
                    "uzmi()"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 3;
        },
   }
   

Sledi sličan, ali nešto teži zadatak.
   
Dođi do loptice i uzmi je 
'''''''''''''''''''''''''

.. questionnote::

   Napišite program na osnovu kojega će Karel doći na polje (4, 1) i pokupiti lopticu.

Zadatak se suštinski ne razlikuje od prethodnog. I sada je potrebno navesti Karela do ciljnog polja i reći mu da uzme lopticu. Razlika je u tome što je sada putanja do ciljnog polja duža, a time i naš program:
   
.. karel:: Karel_intro_take_ball_on_square_4_1
   :blockly:

   {
        setup:function() {
            var world = new World(5,5);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(4, 1);
            world.addEWWall(1, 1, 2);
            world.addNSWall(2, 2, 2);
            world.addEWWall(2, 3, 3);
            world.addNSWall(3, 1, 2);
            world.addNSWall(3, 4, 1);
            world.addNSWall(1, 5, 1);
            world.addEWWall(4, 1, 1);
            
        var robot = new Robot();

        var code = ["from karel import *",
                    "napred()      # idi na (2, 1)",
                    "napred()      # idi na (3, 1)",
                    "levo()        # okreni se na sever (^)",
                    "napred()      # idi na (3, 2)",
                    "napred()      # idi na (3, 3)",
                    "desno()       # okreni se na istok (>)",
                    "napred()      # idi na (4, 3)",
                    "napred()      # idi na (5, 3)",
                    "desno()       # okreni se na jug   (v)",
                    "napred()      # idi na (5, 2)",
                    "napred()      # idi na (5, 1)",
                    "desno()       # okreni se na zapad (<)",
                    "napred()      # idi na (4, 1)",
                    "uzmi()        # uzmi lopticu na (4, 1)"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 1;
        },
   }

Čitajući ovaj program, postaje teško da se prati koja naredba dokle dovodi Karela. To nije tako samo sa početnicima, to je stvarno teško, jer svaka naredba napred() izgleda isto. Da bismo pomogli sebi (i vama), iza svake naredbe smo dodali znak # i neki tekst koji nam pomaže da pratimo "dokle smo stigli". 

**Komentari**
'''''''''''''

.. infonote::

    Deo bilo kog Pajton programa od znaka ``#`` do kraja reda se zove ``komentar``. Komentari ne utiču na izvršavanje programa, program radi isto sa ili bez njih. Komentari su namenjeni samo ljudima koji čitaju i pišu programe, da bi bolje razumeli te programe i lakše se u njima snalazili.
    
    Kada razmišljamo o pisanju komentara u programu, treba da ih pišemo i zbog sebe i zbog drugih ljudi koji će čitati naš program. Isto tako, komentari koje drugi ljudi napišu u svojim programima pomoći će nama da razumemo njihove programe.
    
    Za pisanje komentara ne postoje precizna pravila. Pišite u komentare ono što smatrate da bi pomoglo razumevanju vašeg programa.

   
Pokupi sve loptice 
''''''''''''''''''

U ovom primeru, loptice se nalaze na raznim poljima i potrebno je da dovedemo Karela do svake od tih loptica.

.. questionnote::

   Napišite program na osnovu kojega će Karel pokupiti sve četiri loptice.

Putanju možemo birati na više načina, ali što kraću putanju izaberemo, kraći će biti i program. Možemo na primer prvo da uzmemo lopticu na polju (5, 2), zatim dve loptice na polju (5, 5) i na kraju lopticu na polju (4, 4).

.. karel:: Karel_intro_collect_three_balls
   :blockly:

   {
        setup:function() {
            var world = new World(5,5);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(5, 2);
            world.putBalls(5, 5, 2);
            world.putBall(4, 4);
            world.addEWWall(1, 1, 2);
            world.addNSWall(2, 2, 2);
            world.addEWWall(2, 3, 3);
            world.addNSWall(3, 1, 2);
            world.addNSWall(3, 4, 1);
            world.addNSWall(1, 5, 1);
            world.addEWWall(4, 1, 1);
            
        var robot = new Robot();

        var code = ["from karel import *",
                    "napred(); napred(); levo()         # idi do polja (3, 1) i okreni se na sever",
                    "napred(); napred(); desno()        # idi do polja (3, 3) i okreni se na istok",
                    "napred(); napred(); desno()        # idi do polja (5, 3) i okreni se na jug",
                    "napred(); uzmi()                   # dodji na polje (5, 2) i uzmi lopticu",
                    "levo(); levo()                     # okreni se na sever",
                    "napred(); napred(); napred()       # dodji na polje (5, 5)",
                    "uzmi(); uzmi()                     # uzmi dve loptice",
                    "levo(); napred(); levo(); napred() # idi na polje (4, 4)",
                    "uzmi()                             # uzmi poslednju lopticu na polju (4, 4)"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 4;
        },
   }

**Grupisanje naredbi**
''''''''''''''''''''''

Pošto je ovaj program još duži od prethodnog, da bismo se lakše orijentisali u programu i pratili dokle smo doveli Karela, grupisali smo po nekoliko naredbi koje čine jednu etapu putovanja u jedan red programa. Na kraju svakog reda je komentar koji objašnjava grupu naredbi u tom redu.

Primetite da je pri ovakvom pisanju programa potrebno između naredbi pisati znak ``;`` (iza poslednje naredbe u redu, ovaj znak se ne piše).

Naredbe mogu da se grupišu i drugačije, na primer tako što se grupa naredbi (napisanih jedna ispod druge) razdvoji praznim redom od sledeće grupe. Ovakav način grupisanja je mnogo češće u upotrebi, jer naredbe obično nisu tako tako kratke kao ove za upravljanje Karelom. Evo kako bi to izgledalo: 

.. code::

    from karel import *
    
    # idi do polja (3, 1) i okreni se na sever"
    napred()
    napred()
    levo()
    
    # idi do polja (3, 3) i okreni se na istok
    napred()
    napred()
    desno()
    
    # idi do polja (5, 3) i okreni se na jug
    napred()
    napred()
    desno()
    
    # dodji na polje (5, 2) i uzmi lopticu
    napred()
    uzmi()
    
    # okreni se na sever
    levo()
    levo()
    
    # dodji na polje (5, 5)
    napred()
    napred()
    napred()
    
    # uzmi dve loptice
    uzmi()
    uzmi()
    
    # idi na polje (4, 4)
    levo()
    napred()
    levo()
    napred()
    
    # uzmi poslednju lopticu na polju (4, 4)
    uzmi()
    
~~~~

Karel može i da ostavlja loptice na pojedina polja. Evo kako on to može da uradi.

Premesti lopticu
''''''''''''''''

.. questionnote::

   Napišite program na osnovu kojega će se Karel premestiti lopticu na polje (2, 2) (primetite da Karel na početku **nije** okrenut kako treba).
   

.. karel:: Karel_intro_move_ball_in_2x2
   :blockly:

   {
        setup:function() {
            var world = new World(2, 2);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("S");
            world.putBall(2, 1);
            world.addEWWall(2, 1, 1);

        var robot = new Robot();

        var code = ["from karel import *",
                    "levo(); napred(); uzmi();  # uzmi lopticu na (2, 1)",
                    "desno(); desno(); napred() # vrati se na (1, 1)",
                    "desno(); napred()          # idi na (1, 2)",
                    "desno(); napred()          # idi na (2, 2)",
                    "ostavi()                   # ostavi lopticu na (2, 2)"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return world.getBalls(2, 2) === 1;
        },
   }

**Greške pri izvršavanju**
''''''''''''''''''''''''''

.. infonote::

    Imajte na umu da **Karel ne može u svakom trenutku da izvrši svaku naredbu koju mu zadamo**. Konkretnije, Karel ne može da ide napred ako je ispred njega zid, ne može da uzme lopticu tamo gde je nema, i ne može da je ostavi ako nema loptica kod sebe.

    Probajte da obrišete prvu naredbu ``levo()`` u prethodnom programu, pa pokrenite program i vidite šta se dešava. 
    
    Kada program koji izvršava naš program dođe do naredbe koju nije moguće izvršiti, izvršavanje našeg programa se prekida i dobijamo poruku o grešci pri izvršavanju. Takve poruke su normalna stvar i viđaćemo ih kada god Karel nije u mogućnosti "da nas posluša", ili kada je neka naredba nejasna (tačnije, kada nije napisana kako treba). U takvim situacijama treba da se potrudimo da razumemo u čemu je problem, pa da popravimo program i ponovo ga pokrenemo.


U nastavku je dato nekoliko zadatka za samostalan rad. Uz svaki zadatak ponuđeno je rešenje, koje možete da vidite kada kliknete na dugme "rešenje". Prikazano rešenje možte da iskopirate u prostor za rešavanje i isprobate ga pokretanjem programa. Vaše rešenje može da bude sasvim dobro iako je drukčije od našeg.

Zadaci za vežbu
---------------

Dođi do polja (3, 3)
''''''''''''''''''''

.. questionnote::

   U ovom zadatku nema loptica, potrebno je samo da dovedete Karela do polja (3, 3).
   
.. karel:: Karel_intro_task_go_to_3_3
   :blockly:

   {
        setup:function() {
            var world = new World(3, 3);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("N");
            world.addNSWall(1, 1, 2);
            world.addNSWall(2, 2, 2);

        var robot = new Robot();

        var code = ["from karel import *",
                    "# dodajte naredbe koje nedostaju"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getStreet() === 3 &&
           robot.getAvenue() === 3;
        },
   }
   
.. reveal:: Karel_intro_task_go_to_3_3_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_intro_task_go_to_3_3_solution
      :passivecode: true
      
      from karel import *
      napred(); napred()          # do polja (1, 3)
      desno(); napred()           # do polja (2, 3)
      desno(); napred(); napred() # do polja (2, 1)
      levo(); napred()            # do polja (3, 1)
      levo(); napred(); napred()  # do polja (3, 3)

Pokupi loptice
''''''''''''''

.. questionnote::

   Napišite program na osnovu kojega će se Karel pokupiti loptice.
   
.. karel:: Karel_intro_task_collect_balls_in_2x2
   :blockly:

   {
        setup:function() {
            var world = new World(2, 2);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.putBall(2, 1);
            world.putBall(2, 2);
            world.putBall(1, 2);
            world.addEWWall(2, 1, 1);

        var robot = new Robot();

        var code = ["from karel import *",
                    "# dodajte naredbe koje nedostaju",
                    "uzmi()"];
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() === 3;
        },
   }
   
.. reveal:: Karel_intro_task_collect_balls_in_2x2_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje
  
   .. activecode:: Karel_intro_task_collect_balls_in_2x2_solution
      :passivecode: true
       
      from karel import *
      napred(); uzmi()            # uzmi na polju (2, 1)
      desno(); desno(); napred()  # vrati se na polje (1, 1)
      desno(); napred(); uzmi()   # uzmi na polju (1, 2)
      desno(); napred(); uzmi()   # uzmi na polju (2, 2)

Krivudanje
''''''''''

.. questionnote::

  Karel treba da stigne do polja (5, 1).

.. karel:: Karel_intro_task_stairs_fixed
   :blockly:

   {
      setup:function() {

         var Y = 3;
         var X = 2 * Y - 1;
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");

         // Vertical walls
         for (let y = 1; y < Y; y++) world.addNSWall(y, y, 1); // low left
         for (let y = 1; y < Y; y++) world.addNSWall(X - 1 - y, y, 1); // low right
         for (let y = 3; y <= Y; y++) world.addNSWall(y - 2, y, 1); // high left
         for (let y = 2; y <= Y; y++) world.addNSWall(X + 1 - y, y, 1); // high right
         
         // Horizontal walls
         for (let y = 1; y < Y - 1; y++) world.addEWWall(y + 1, y, 1); // low left
         for (let y = 2; y < Y; y++) world.addEWWall(y - 1, y, 1); // high left
         for (let y = 1; y < Y - 1; y++) world.addEWWall(X - 1 - y, y, 1); // low right
         for (let y = 1; y < Y; y++) world.addEWWall(X + 1 - y, y, 1); // high right

         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dodajte naredbe ",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_intro_task_stairs_fixed_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_intro_task_stairs_fixed_solution
      :passivecode: true
      
      from karel import *
      levo(); napred()     # na (1, 2)
      desno(); napred()    # na (2, 2)
      levo(); napred()     # na (2, 3)
      desno(); napred()    # na (3, 3)
      desno(); napred()    # na (3, 2)
      levo(); napred()     # na (4, 2)
      desno(); napred()    # na (4, 1)
      levo(); napred()     # na (5, 1)


Pravo pa levo, pa opet
''''''''''''''''''''''

.. questionnote::

  Karel treba da stigne do polja (2, 3).
   
.. karel:: Karel_intro_task_spiral_left_fixed
   :blockly:

   {
      setup:function() {

         var N = 4;
         var world = new World(N, N);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         
         var i = 1;
         for (let d = N - 1; d > 0; d -= 2) { world.addEWWall(i, i, d); i++; }
         i = 2;
         for (let d = N - 2; d > 0; d -= 2) { world.addEWWall(i, N+1-i, d); i++; }
         i = 2;
         for (let d = N - 2; d > 0; d -= 2) { world.addNSWall(N+1-i, i, d); i++; }
         i = 1;
         for (let d = N - 3; d > 0; d -= 2) { world.addNSWall(i, i+2, d); i++; }
   
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "# dodajte naredbe ",
                     ""];
      
         return {robot:robot, world:world, code:code};
      },
 
      isSuccess: function(robot, world) {
         var N = world.getAvenues();
         return robot.getStreet() === Math.floor((N+2)/2) &&
           robot.getAvenue() === Math.floor((N+1)/2);
     },
   }

.. reveal:: Karel_intro_task_spiral_left_fixed_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_intro_task_spiral_left_fixed_solution
      :passivecode: true
      
      from karel import *
      napred(); napred(); napred(); levo() # do (4, 1)
      napred(); napred(); napred(); levo() # do (4, 4)
      napred(); napred(); napred(); levo() # do (1, 4)
      napred(); napred(); levo()           # do (1, 2)
      napred(); napred(); levo()           # do (3, 2)
      napred(); levo()                     # do (3, 3)
      napred();                            # do (2, 3)

