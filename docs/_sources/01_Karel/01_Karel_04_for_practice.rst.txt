Naredba *for* - vežbanje
========================

U ovom delu ćemo samo uvežbavati upotrebu *for* naredbe.

Zadaci
------

Tri puta gore-dole
''''''''''''''''''

.. questionnote::

  Karel se nalazi na pravougaonoj tabli od 5 redova i 7 kolona i treba da stigne do donjeg desnog polja.


Karel treba tri puta da ponovi jednu složenu radnju, a to je: da pređe u sledeću (desnu) kolonu, ode do njenog vrha, ode još jednu kolonu desno, siđe do prvog reda i na kraju da se okrene ka poslednjoj koloni da bi se pripremio za sledeće ponavljanje. 

Dopunite program, vodeći računa da se brojač u *for* naredbama koje dodajete ne zove ``i`` (to ime je već upotrebljeno u spoljnoj petlji).

.. karel:: Karel_for_up_col_down_col_constant
   :blockly:

   {
      setup:function() {

         var X2 = 3;
         var Y = 5;
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
                     "for i in range(3):              # tri puta ponovi sve sto sledi",
                     "    napred(); levo()             #    udji u sledecu kolonu i okreni se na sever",
                     "    # upotrebite for naredbu da kazete Karelu da ode do gornje ivice",
                     "    ",
                     "    desno(); napred(); desno()   #    predji u sledecu kolonu i okreni se na jug",
                     "    # upotrebite for naredbu da kazete Karelu da ode do donje ivice",
                     "    ",
                     "    levo()                       #    okreni se na istok",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_up_col_down_col_constant_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_for_up_col_down_col_constant_solution
      :passivecode: true
      
      from karel import *
      for i_vodoravno in range(3):     # 3 puta ponovi sve sto sledi
          napred(); levo()             #     udji u sledecu kolonu i okreni se na sever
          for i_uspravno in range(4):  #     idi do gornje ivice
              napred()

          desno(); napred(); desno()   #     predji u sledecu kolonu i okreni se na jug
          for i_uspravno in range(4):  #     idi do donje ivice
              napred()

          levo()                       #     okreni se na istok


Donesi sve sa table
'''''''''''''''''''

.. questionnote::

  Karel treba da donese svih 12 loptica na polazno polje.


Karel treba četiri puta da pređe u sledeću kolonu i isprazni je, a na kraju da dođe na polazno polje i ostavi sve loptice. Karel će isprazniti kolonu ako tri puta ponovi korak napred i uzimanje, a zatim se vrati na početak kolone u isti položaj.

Dopunite program.

.. karel:: Karel_for_fetch_from_matrix
   :blockly:

   {
      setup:function() {
         var X = 5;
         var Y = 4;
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");

         world.addEWWall(1, 1, 1);
         world.addNSWall(1, 2, Y - 1);
         
         for (var col = 2; col <= X; col++) {
            for (var row = 2; row <= Y; row++) {
               world.putBall(col, row);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "for i_kolona in range(4):      # cetiri puta ponovi ciscenje kolone",
                     "    napred()                   #     udji u sledecu kolonu",
                     "    levo()                     #     okreni se na sever",
                     "    #for ...                   #     3 puta ponovi korak napred i uzimanje",
                     "",
                     "    desno(); desno()           #     okreni se na jug",
                     "    #for ...                   #     3 koraka napred do donje ivice",
                     "",
                     "    levo()                     #     okreni se na istok",
                     "    ",
                     "                               # sada smo prosli sva polja",
                     "levo()                         #     okreni se na zapad",
                     "levo()",
                     "#for ...                       # vrati se na pocetno polje",
                     "    ",
                     "for i_loptica in range(12):",
                     "    ostavi()",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return world.getBalls(1, 1) == 12 &&
            robot.getAvenue() == 1 &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_fetch_from_matrix_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_for_fetch_from_matrix_solution
      :passivecode: true
      
      from karel import *
      for i_kolona in range(4):     # cetiri puta ponovi ciscenje kolone
          napred()                  #     udji u sledecu kolonu
          levo()                    #     okreni se na sever
          for i_red in range(3):    #     idi do gornje ivice i usput pokupi
              napred()
              uzmi()

          desno(); desno()          #     okreni se na jug
          for i_red in range(3):    #     idi do donje ivice
              napred()

          levo()                    #     okreni se na istok
         
      levo()                        # okreni se na zapad
      levo()
      for i_kolona in range(4):     # vrati se na pocetno polje
          napred()
         
      for i_loptica in range(12):   # ostavi sve loptice
          ostavi()


Trostruka petlja
''''''''''''''''

.. questionnote::

  Sada se na svakom od 6 polja nalazi po 4 loptice, slično prethodnom zadatku. Karel treba da donese sve 24 loptice na polazno polje.


Ovaj program se od prethodnog razlikuje po tome što naredba *uzmi()* treba da stoji u dodatnoj petlji, trećoj u dubinu. Takođe, razlikuje se i broj loptica koje Karel na kraju programa ostavlja na polazno polje. Možete da iskopirate prethodni program i prepravite ga.

.. karel:: Karel_for_fetch_60_from_matrix
   :blockly:

   {
      setup:function() {
         var X = 3;
         var Y = 4;
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");

         world.addEWWall(1, 1, 1);
         world.addNSWall(1, 2, Y - 1);
         
         for (var col = 2; col <= X; col++) {
            for (var row = 2; row <= Y; row++) {
               world.putBalls(col, row, 4);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dopunite program",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return world.getBalls(1, 1) == 24 &&
            robot.getAvenue() == 1 &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_fetch_24_from_matrix_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_for_fetch_24_from_matrix_solution
      :passivecode: true
      
      from karel import *
      for i_kolona in range(2):         # cetiri puta ponovi ciscenje kolone
          napred()                      #     udji u sledecu kolonu
          levo()                        #     okreni se na sever
          for i_red in range(3):        #     idi do gornje ivice i usput pokupi
              napred()                   
              for i_loptica in range(4): 
                  uzmi()                  

          desno(); desno()              #     okreni se na jug
          for i_red in range(3):        #     idi do donje ivice
              napred()                   

          levo()                        #     okreni se na istok

      levo()                            #     okreni se na zapad
      levo()                           
      for i_kolona in range(2):         # vrati se na pocetno polje
          napred()

      for i_loptica in range(24):       # ostavi sve loptice
          ostavi()


Popni se pa siđi
''''''''''''''''

.. questionnote::

  Karel treba da se popne uz prve stepenice, a zatim da siđe niz druge i završi u donjem desnom uglu.

Sada nam trebaju samo dve petlje jedna za drugom (ne ugnežđene). U prvoj petlji Karel treba da se popne uz prve, a u drugoj da siđe niz druge stepenice. U svakoj petlji Karel treba da obavi po 4 radnje koje predstavljaju jedan korak uz ili niz stepenice.

.. karel:: Karel_for_stairs_constant
   :blockly:

   {
      setup:function() {

         var Y = 4;
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
                     "levo()                                 # ka severu",
                     "for i_stepenik in range(3):            # 3 puta ponovi",
                     "    # recite Karelu da se popne jedan stepenik ",
                     "",
                     "desno(); desno()                       # ka jugu",
                     "",
                     "# recite Karelu da sidje 3 stepenika",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_stairs_constant_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_for_stairs_constant_solution
      :passivecode: true
      
      from karel import *
      levo()                                  # ka severu
      for i_stepenik in range(3):             # 3 puta ponovi
          napred(); desno(); napred(); levo() #     popni se jedan stepenik 

      desno(); desno()                        # ka jugu
      
      for i_stepenik in range(3):             # 3 puta ponovi
          napred(); levo(); napred(); desno() #     sidji jedan stepenik 



Sakupi loptice na stepenicama
'''''''''''''''''''''''''''''

.. questionnote::

  Karel ponovo treba da završi u donjem desnom uglu, a usput treba da uzme sve loptice.

Dobar način da se reši ovaj zadatak je da se počne od rešenja prethodnog zadatka. Preporuka: iskopirajte rešenje prethodnog zadatka ovde, a zatim ubacite petlje za uzimanje loptica.


.. karel:: Karel_for_stairs_and_balls_constant
   :blockly:

   {
      setup:function() {

         var Y = 4;
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
         
         // Balls
         for (let y = 2; y <= Y; y++) {
            world.putBalls(y - 1, y, 3);
            world.putBalls(y, y, 4);
         }
         for (let y = 1; y < Y; y++) {
            world.putBalls(X - y, y, 2);
            world.putBalls(X + 1 - y, y, 3);
         }

         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# napisite program",
                     ""];
    
         return {robot:robot, world:world, code:code};
      },
    
      isSuccess: function(robot, world) {
         return robot.getBalls() == 36 &&
            robot.getAvenue() == world.getAvenues() &&
            robot.getStreet() == 1;
      },
   }

.. reveal:: Karel_for_stairs_and_balls_constant_reveal
   :showtitle: Rešenje
   :hidetitle: Sakrij rešenje

   .. activecode:: Karel_for_stairs_and_balls_constant_solution
      :passivecode: true
      
      from karel import *
      levo()                                 # ka severu
      for i_stepenik in range(3):            # 3 puta ponovi
          napred(); desno()
          for i_loptica in range(3):
              uzmi()
          napred(); levo() #    popni se jedan stepenik 
          for i_loptica in range(4):
              uzmi()
      
      desno(); desno()                       # ka jugu
      
      for i_stepenik in range(3):            # 3 puta ponovi
          napred(); levo()
          for i_loptica in range(2):
              uzmi()
          napred(); desno() #    sidji jedan stepenik 
          for i_loptica in range(3):
              uzmi()

