Kombinovanje petlji
===================

Videli smo da u telu *for* naredbe može da se nađe više različitih naredbi. Slično kao sa *for* naredbom, i u telu ``while`` naredbe može (pored ostalih naredbi) da se nađe i nova petlja, bilo *while* ili *for*. Tako možemo da gradimo različite kombinacije umetnutih (ugnežđenih) petlji.

Kada su dve petlje umetnute jedna u drugu, zovemo ih i dvostruka petlja, dok tri ugnežđene petlje zovemo trostruka petlja. Na sličan način možemo ugnezditi bilo koji broj petlji jednu u drugu, ali za velikim brojem ugnežđenih petlji vrlo retko imamo potrebu.

U ovoj lekciji ćemo vežbati pisanje kombinacija ugnežđenih *while* i *for* petlji.

Razne dvostruke i višestruke petlje - zadaci
--------------------------------------------

Uzimaj po četiri loptice do kraja
'''''''''''''''''''''''''''''''''

.. questionnote::

  Ispred Karela je jedno ili više polja, a na svakom od polja ispred Karela su po četiri loptice (na početnom polju nema loptica). Karel treba sve da ih pokupi.
  
Sada Karel, sve dok ne dođe do zida, treba da ponavlja korak napred i uzimanje 4 loptice. Pokušajte da dopunite program.

Podsetimo se, kao i u ranijim primerima ugnežđenih petlji, naredba u telu unutrašnje petlje (ovde će to biti naredba ``uzmi()``) treba da bude dodatno uvučena. 
  
.. karel:: Karel_while__many_squares_four_bals_per_square
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(9);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         for (var k = 2; k <= N; k++)
             world.putBalls(k, 1, 4);
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "while moze_napred():",
                     "    napred()",
                     "    # dodajte naredbe koje nedostaju",
                     ""];
                     //from karel import *
                     //while moze_napred():
                     //    napred()
                     //    for i in range(4):
                     //        uzmi()
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         var N = world.getAvenues();
         for (var k = 1; k <= N; k++)
            if (world.getBalls(k, 1) > 0)
               return false;
               
         return true;
      }
   }
   
..  commented out
    .. reveal:: Karel_while__many_squares_four_bals_per_square_reveal
       :showtitle: Rešenje
       :hidetitle: Sakrij rešenje
    
       .. activecode:: Karel_while__many_squares_two_bals_per_square_solution
          :passivecode: true
          
          from karel import *
          while moze_napred():
              napred()
              for i in range(4):
                  uzmi()
   
   
Pokupi sve loptice
''''''''''''''''''

.. questionnote::

  Ispred Karela je bar jedno polje, a može ih biti bilo koliko. Na svakom od polja **ispred** Karela ima nula ili više loptica (počteno polje je prazno). Karel treba da pokupi sve loptice.

Ovaj zadatak je uopštenje prethodnog, pa program koji rešava ovaj zadatak, može da se iskoristi i u prethodnom. Razlika je u tome što sada unutrašnja petlja mora da bude *while*, dok je u prethodnom zadatku mogla da bude i *for*. 

I u ovom programu naredba ``uzmi()`` treba da bude dodatno uvučena. Na taj način će se ona ponavljati dok je uslov unutrašnje ``while`` naredbe ispunjen, to jest dok ima loptica na polju na kome je Karel u tom trenutku, a uzimanje svih loptica se zajedno sa naredbom ``napred`` ponavlja u spoljašnjoj ``while`` naredbi dok ima polja ispred Karela. Ukupni efekat ugnežđenih petlji je da će biti uzete sve loptice sa svakog polja.


.. karel:: Karel_while__many_squares_many_balls
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(9);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         
         for (var k = 2; k <= N; k++) {
            let B = random(7);
            world.putBalls(k, 1, B);
         }
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "while moze_napred():",
                     "    # pomeri se napred",
                     "    while ... # dovrsite",
                     ""];
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         var N = world.getAvenues();
         for (var k = 1; k <= N; k++)
            if (world.getBalls(k, 1) > 0)
               return false;
               
         return true;
      }
   }

Donesi sve loptice
''''''''''''''''''

.. questionnote::

  Ispred Karela je prav put nepoznate dužine. Karel treba da prikupi sve loptice sa svih polja i donese ih na početno polje.

Program je komentarima razložen na sitnije celine. Dodajte delove koji nedostaju.

.. karel:: Karel_while__bring_all_balls
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(9);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
         
         for (var k = 1; k <= N; k++) {
            let B = random(7);
            world.putBalls(k, 1, B);
         }
      
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# koristite dvostruku while petlju za uzimanje svih loptica sa svih polja",
                     "",
                     "",
                     "levo(); levo()                # okreni se nazad",
                     "# kazite Karelu da se vrati na pocetno polje (to jest, da ide napred dok moze)",
                     "",
                     "while ima_loptica_kod_sebe(): # ostavi sve loptice",
                     "    # ostavi jednu lopticu",
                     ""];

           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           var N = world.getAvenues();
           for (var k = 2; k <= N; k++)
              if (world.getBalls(k, 1) > 0)
                 return false;
               
           if (robot.getBalls() > 0)
                 return false;
                 
           return true;
        },
   }

..  commented out
    .. reveal:: Karel_while__bring_all_balls_reveal
       :showtitle: Rešenje
       :hidetitle: Sakrij rešenje

       .. activecode:: Karel_while__bring_all_balls_solution
          :passivecode: true
          
          from karel import *
          while moze_napred():          # pokupi sve loptice sa svih polja
              napred()
              while ima_loptica_na_polju():
                  uzmi()
                
          levo(); levo()                # okreni se nazad
          
          while moze_napred():          # vrati se na pocetno polje
              napred()
              
          while ima_loptica_kod_sebe(): # ostavi sve loptice           
              ostavi()


Gore-dole
'''''''''

.. questionnote::

  Karel se nalazi na pravougaonoj tabli nepoznate veličine (broj kolona je uvek neparan), bez loptica. Cilj je da Karel stigne do donjeg desnog polja, a da bi to postigao, moraće da se kreće kroz kolone naizmenično gore-dole.
  
  Ovo su neki od mogućih izgleda lavirinta:

   .. image:: ../../_images/Karel/While_UpDown.jpg
      :width: 600px   
      :align: center

.. karel:: Karel_while__up_col_down_col
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var X2 = 1 + random(4);
         var Y = 2 + random(5);
         var world = new World(2*X2+1, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
            
         world.addEWWall(1, 1, 1);
         for (let x = 0; x < X2; x++) { 
            world.addNSWall(2*x + 1, 2, Y - 1);
            world.addNSWall(2*x + 2, 1, Y - 1);
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dodajte naredbe ",
                     ""];
                     //from karel import *
                     //while moze_napred():           # dok nismo u donjem desnom uglu
                     //    napred(); levo()           #     udji u sledecu kolonu i okreni se na sever
                     //    while moze_napred():       #     idi do gornje ivice
                     //        napred()
                     //
                     //    desno(); napred(); desno() #     predji u sledecu kolonu i okreni se na jug
                     //    while moze_napred():       #     idi do donje ivice
                     //        napred()
                     //
                     //    levo()                     #     okreni se na istok
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_while__up_col_down_col_reveal
   :showtitle: Pomoć
   :hidetitle: Sakrij pomoć

   .. activecode:: Karel_while__up_col_down_col_solution
      :passivecode: true
      
      from karel import *
      while moze_napred():           # dok nismo u donjem desnom uglu
          napred(); levo()           #     udji u sledecu kolonu i okreni se na sever
          ... # dovrsite             #     idi do gornje ivice

          desno(); napred(); desno() #     predji u sledecu kolonu i okreni se na jug
          ... # dovrsite             #     idi do donje ivice

          levo()                     #     okreni se na istok

Stepenice
'''''''''

.. questionnote::

  Karel treba da se popne uz prve stepenice, a zatim da siđe niz druge i završi u donjem desnom uglu. Veličina table nije poznata, ali broj kolona će uvek biti neparan. Tabla može da izgleda na primer ovako:
  

   .. image:: ../../_images/Karel/While_Stairs.jpg
      :width: 600px   
      :align: center

.. karel:: Karel_while__stairs
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var Y = 2 + random(6);
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
                     //from karel import *
                     //levo()                                  # ka severu
                     //while moze_napred():                    # dok ima uzbrdo
                     //    napred(); desno(); napred(); levo() #    popni se jedan stepenik 
                     //
                     //desno(); desno()                        # ka jugu
                     //
                     //while moze_napred():                    # dok ima nizbrdo
                     //    napred(); levo(); napred(); desno() #    sidji jedan stepenik 
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_while__stairs_reveal
   :showtitle: Pomoć
   :hidetitle: Sakrij pomoć

   .. activecode:: Karel_while__stairs_solution
      :passivecode: true
      
      from karel import *
      levo()                                  # ka severu
      while moze_napred():                    # dok ima stepenika uzbrdo
          napred(); desno(); napred(); levo() #    popni se jedan stepenik 

      desno(); desno()                        # ka jugu
      
      while ... # dovrsite uslov              # dok ima stepenika nizbrdo
          ... # dodajte jos 4 naredbe         #    sidji jedan stepenik 


Spirala ulevo
'''''''''''''

.. questionnote::

  Karel u svim prikazanim slučajevima treba da dođe do polja označenog crvenim krugom (ni u ovom zadatku nema loptica).
   
   .. image:: ../../_images/Karel/While_SpiralLeft.jpg
      :width: 600px   
      :align: center


.. karel:: Karel_while__spiral_left
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

      var N = 1 + random(7);
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
                  "# dopunite naredbe koje nisu kompletne",
                  "while moze_napred():",
                  "    while ... ",
                  "        ... ",
                  "    levo()",
                  ""];

        return {robot:robot, world:world, code:code};
     },
 
     isSuccess: function(robot, world) {
        var N = world.getAvenues();
        return robot.getStreet() === Math.floor((N+2)/2) &&
           robot.getAvenue() === Math.floor((N+1)/2);
     },
   }

.. reveal:: Karel_while__spiral_left_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_while__spiral_left_solution
      :passivecode: true
      
      from karel import *
      while moze_napred():
          while moze_napred():
              napred()
          levo()

