Naredba *if* - vežbanje
=======================

U ovom delu ćemo samo uvežbavati upotrebu *if* naredbe i njeno kombinovanje sa petljama.

Zadaci za vežbu
---------------

Idi do kraja i uzmi samo jednu
''''''''''''''''''''''''''''''

.. questionnote::

   Karel treba da stigne do kraja hodnika, a da usput uzme samo prvu lopticu na koju naiđe. Polje sa koga Karel polazi nikad nema lopticu, a i Karel je na početku bez loptica.
   
.. karel:: Karel_if__take_first_ball_only
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████████████',
               '█E.0.1.0.3.0█',
               '█████████████'
            ],
            [
               '█████████',
               '█E.0.2.2█',
               '█████████'
            ],
            [
               '███████',
               '█E.1.0█',
               '███████'
            ]
         ];
         let choice = random(ww.length);
         var w = ww[choice];
         var ny = Math.floor(w.length / 2);
         var nx = Math.floor(w[0].length / 2);
         var world = new World(nx, ny);
         
         for (let y = 1; y <= ny; y++) {
            let wy = 2*(ny-y) + 1;
            for (let x = 1; x <= nx; x++) {
               let wx = 2*x - 1;
               if (y < ny && w[wy - 1].charAt(wx) == "█") world.addEWWall(x, y, 1);
               if (x < nx && w[wy].charAt(wx + 1) == "█") world.addNSWall(x, y, 1);
               let c = w[wy].charAt(wx);
               let pos = "SWEN".indexOf(c);
               if (pos > -1) {
                  world.setRobotStartAvenue(x);
                  world.setRobotStartStreet(y);
                  world.setRobotStartDirection("SWEN".charAt(pos));
               }
               let d = w[wy].charCodeAt(wx);
               if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dopunite",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. reveal:: Karel_if__take_first_ball_only_reveal
    :showtitle: Pomoć
    :hidetitle: Sakrij pomoć
    
    Ovde je započeto jedno rešenje, potrebno je dopuniti *if* naredbe odgovarajućim uslovima.
    
    Karel treba da uzme lopticu samo ako su ispunjena dva uslova:
    
    - jedan je uslov koji proveravamo pri svakom uzimanju loptice (bez tog uslova program bi mogao da se prekine zbog neizvodljive operacije).
    - drugi uslov je nametnut zahtevima ovog zadatka, a to je da Karel uzima lopticu samo ako pre toga nije već uzeo neku lopticu.
    
    Redosled ispitivanja ova dva uslova nije bitan, svakako oba treba da budu ispunjena da bi Karel uzeo lopticu.
    
    .. activecode:: Karel_if__take_first_ball_only_solution
        :passivecode: true
      
        from karel import *
        while moze_napred():  # dok ima polja ispred Karela
            napred()                    
            if ???
                if ???
                    uzmi()

Uzmi lopticu na susednom polju
''''''''''''''''''''''''''''''

.. questionnote::

   Na tabli se nalazi samo jedna loptica. Karel i loptica se nalaze na dva susedna polja, između kojih nema zida (Karela od loptice deli samo jedan korak, ako se pre toga okrene ka loptici). Između ostalih polja može a ne mora biti zidova. Karel treba da uzme lopticu i pri tome nije bitno na kojem polju će da ostane kada se program završi.
   
   Kao i obično, pokrenite program više puta da biste ga testirali na različitim primerima.   

Jedna od ideja je da u svakom od 4 smera pokušamo Karelom korak napred i uzimanje loptice. Pri svakom od 4 pokušaja mogu da nastupe razni slučajevi:

- moguće je da u tom smeru nema polja napred
- moguće je da postoji polje ispred Karela, ali da na njemu nema loptice
- moguće je da postoji polje i da je na njemu loptica

Pri pokušaju u sledećem smeru nam je mnogo jednostavnije ako ne moramo da vodimo računa o tome da li je Karel u prethodnom smeru našao polje bez loptice, ili nije našao ni polje. Radi toga je potrebno da Karel, kada završi pokušaj u jednom smeru, stane na isti način kada je bio na praznom polju, kao i kada polja nije ni bilo. Kada polja u datom smeru nema, Karel će ostati na početnom polju, okrenut u tom smeru. Najjednostavnije za nastavak traganja je da Karela ostavimo na istom polju i u istom položaju i kada se vrati sa praznog susednog polja. U stvari, neće smetati ako to uradimo i kada Karel uzme lopticu (može da dogoditi da Karel nepotrebno nastavi da traži, ali neće doći do greške). 

Zahvaljujući ovom dovođenju Karela na isto stanje (pozicija i orijentacija) posle bilo kog od tri gore nabrojana slučaja, za svaki sledeći pokušaj tačno znamo od kog Karelovog stanja počinjemo. Ostaje da nakon svakog pokušaja okrenemo Karela ka sledećem smeru u kojem ćemo pokušati da dođemo do loptice (na levo ili na desno).

.. karel:: Karel_if__take_neighboring_ball
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████',
               '█0.0█',
               '███.█',
               '█1.N█',
               '███.█',
               '█0.0█',
               '█████'
            ],
            [
               '█████',
               '█1.0█',
               '█...█',
               '█E.0█',
               '█████'
            ],
            [
               '███████',
               '█0█0█0█',
               '█.█.█.█',
               '█0.W.0█',
               '█.█.█.█',
               '█0█1█0█',
               '███████'
            ]
         ];
         let choice = random(ww.length);
         var w = ww[choice];
         var ny = Math.floor(w.length / 2);
         var nx = Math.floor(w[0].length / 2);
         var world = new World(nx, ny);
         
         for (let y = 1; y <= ny; y++) {
            let wy = 2*(ny-y) + 1;
            for (let x = 1; x <= nx; x++) {
               let wx = 2*x - 1;
               if (y < ny && w[wy - 1].charAt(wx) == "█") world.addEWWall(x, y, 1);
               if (x < nx && w[wy].charAt(wx + 1) == "█") world.addNSWall(x, y, 1);
               let c = w[wy].charAt(wx);
               let pos = "SWEN".indexOf(c);
               if (pos > -1) {
                  world.setRobotStartAvenue(x);
                  world.setRobotStartStreet(y);
                  world.setRobotStartDirection("SWEN".charAt(pos));
               }
               let d = w[wy].charCodeAt(wx);
               if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "for i in range(4):",
                     "    if moze_napred():",
                     "        napred()",
                     "        # recite Karelu da pokusa da uzme lopticu",
                     "        # recite Karelu da se vrati na pocetno polje",
                     "        # i okrene se ka polju na kome je upravo pokusao",
                     "        # (kao da nije ni isao na to polje)",
                     "    # recite Karelu da se pripremi za sledeci pokusaj",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. commented out
   .. reveal:: Karel_if__take_neighboring_ball_reveal
       :showtitle: Rešenje
       :hidetitle: Sakrij rešenje
       
       Rešenje može da izgleda ovako:
       
       .. activecode:: Karel_if__take_neighboring_ball_solution
           :passivecode: true
         
           from karel import *
           for i in range(4):          # u svakom od 4 smera
               if moze_napred():       # potrazi polje u tom smeru
                   napred()                    
                   if ima_loptica_na_polju():
                       uzmi()
                   levo()              # idi na polazno polje
                   levo()
                   napred()
                   levo()              # okreni se ka polju koje si probao
                   levo()
               levo()                  # sledeci smer

Prati put
'''''''''

.. questionnote::

  Postoji samo jedna loptica i Karel treba da je uzme. Put do loptice je krivudav, ali nema raskrsnica (uvek postoji samo jedan nastavak puta, čak i sa polaznog polja).


.. karel:: Karel_if__take_ball_no_branches
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '███████████',
               '█N█0.0.0.0█',
               '█.█.█████.█',
               '█0█0█0.1█0█',
               '█.█.█.███.█',
               '█0.0█0.0.0█',
               '███████████'
            ],
            [
               '█████████',
               '█0.0.0.0█',
               '█.█████.█',
               '█0█0.0.0█',
               '█.█.█████',
               '█0█E█0.0█',
               '█.███.█.█',
               '█0.0.0█1█',
               '█████████'
            ],
            [
               '█████████████',
               '█W.0.0█0.0.0█',
               '█████.█.███.█',
               '█0.0.0█0█0.0█',
               '█.█████.█.███',
               '█0.0.0.0█0.1█',
               '█████████████'
            ],
            [
               '███████████',
               '█0.0█0.0█S█',
               '█.█.█.█.█.█',
               '█0█0.0█0.0█',
               '█.█████████',
               '█0█0.0█0.0█',
               '█.█.█.█.█.█',
               '█0.0█0.0█1█',
               '███████████'
            ]
         ];
         let choice = random(ww.length);
         var w = ww[choice];
         var ny = Math.floor(w.length / 2);
         var nx = Math.floor(w[0].length / 2);
         var world = new World(nx, ny);
         
         for (let y = 1; y <= ny; y++) {
            let wy = 2*(ny-y) + 1;
            for (let x = 1; x <= nx; x++) {
               let wx = 2*x - 1;
               if (y < ny && w[wy - 1].charAt(wx) == "█") world.addEWWall(x, y, 1);
               if (x < nx && w[wy].charAt(wx + 1) == "█") world.addNSWall(x, y, 1);
               let c = w[wy].charAt(wx);
               let pos = "SWEN".indexOf(c);
               if (pos > -1) {
                  world.setRobotStartAvenue(x);
                  world.setRobotStartStreet(y);
                  world.setRobotStartDirection("SWEN".charAt(pos));
               }
               let d = w[wy].charCodeAt(wx);
               if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "... # dopunite",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. reveal:: Karel_if__take_ball_no_branches_reveal
    :showtitle: Pomoć
    :hidetitle: Sakrij pomoć
    
    Uputstva za jedno moguće rešenje:

    .. activecode:: Karel_if__take_ball_no_branches_solution
        :passivecode: true
      
        # prvo se okreni ka (jedinom) praznom polju
        dok ne mozes napred: 
            okreni se na levo
            
        dok mozes napred:
            idi napred            
            ako ispred tebe nije prazno polje: # ako ne mozes pravo
                okreni se na levo
                ako ispred tebe nije prazno polje: # ako ne mozes ni levo
                    okreni se dva puta na desno
        
        uzmi lopticu

.. commented out
   .. reveal:: Karel_if__take_ball_no_branches_reveal
       :showtitle: Rešenje
       :hidetitle: Sakrij rešenje
       
       Jedno moguće rešenje je:
   
       .. activecode:: Karel_if__take_ball_no_branches_solution
           :passivecode: true
         
           from karel import *
           while not moze_napred(): # okreni se ka (jedinom) praznom polju
               levo()
               
           while moze_napred():
               napred()
               
               # okreni se ka sledecem praznom polju
               if not moze_napred(): # ako ne moze pravo,
                   levo()                # probaj levo
               if not moze_napred(): # ako ne moze ni levo
                   desno(); desno()      # probaj desno
           
           if ima_loptica_na_polju():
               uzmi()

Skreći
''''''

.. questionnote::

  Postoji samo jedna loptica i Karel treba da je uzme. Da bi stigao do loptice, Karel treba da ide pravo samo kad ne može da skrene ni levo ni desno (neće se pojaviti raskrsnice na kojima se može skrenuti i levo i desno). 


.. karel:: Karel_if__p1_left_p2_right_p3_forward
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '███████████',
               '█1.0█0.0.0█',
               '███.█.█████',
               '█0.0.0█0.0█',
               '█████.███.█',
               '█S.0.0.0.0█',
               '███████████'
            ],
            [
               '███████████',
               '█0.0.0█0.0█',
               '█████.█.███',
               '█0.0.0█0.0█',
               '█.█.█.█.█.█',
               '█0█0█E█0█1█',
               '█.█.███.███',
               '█0█0.0.0.0█',
               '███████████'
            ],
            [
               '█████████████',
               '█E.0.0█0.0.0█',
               '███.█.█.█████',
               '█0.0█0█0.0.0█',
               '█.█.███.███.█',
               '█0█0█0.0.0█0█',
               '█.███.█████.█',
               '█0.0.0.0.0█1█',
               '█████████████'
            ],
            [
               '█████████',
               '█0.0.0█S█',
               '█.█████.█',
               '█0.0.0.0█',
               '███.███.█',
               '█0█0.0█0█',
               '█.█.█.███',
               '█0.0█0.1█',
               '█████████'
            ]
         ];
         let choice = random(ww.length);
         var w = ww[choice];
         var ny = Math.floor(w.length / 2);
         var nx = Math.floor(w[0].length / 2);
         var world = new World(nx, ny);
         
         for (let y = 1; y <= ny; y++) {
             let wy = 2*(ny-y) + 1;
             for (let x = 1; x <= nx; x++) {
                 let wx = 2*x - 1;
                 if (y < ny && w[wy - 1].charAt(wx) == "█") world.addEWWall(x, y, 1);
                 if (x < nx && w[wy].charAt(wx + 1) == "█") world.addNSWall(x, y, 1);
                 let c = w[wy].charAt(wx);
                 let pos = "SWEN".indexOf(c);
                 if (pos > -1) {
                     world.setRobotStartAvenue(x);
                     world.setRobotStartStreet(y);
                     world.setRobotStartDirection("SWEN".charAt(pos));
                 }
                 let d = w[wy].charCodeAt(wx);
                 if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
             }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "... # dopunite",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }
   
.. reveal:: Karel_if__p1_left_p2_right_p3_forward_reveal
    :showtitle: Pomoć
    :hidetitle: Sakrij pomoć

    Uputstva za jedno moguće rešenje:
    
    .. activecode:: Karel_if__p1_left_p2_right_p3_forward_solution
        :passivecode: true
      
        # okreni se ka (jedinom) praznom polju
        
        dok mozes da ides napred:
            idi napred
            # probaj da skrenes levo (okreni se na levo i probaj napred)
            # ako ne mozes levo
                # probaj da skrenes desno
                # ako ne mozes ni desno
                    # probaj pravo u sledecoj iteraciji
        
        uzmi lopticu

.. commented out
    .. reveal:: Karel_if__p1_left_p2_right_p3_forward_reveal
        :showtitle: Rešenje
        :hidetitle: Sakrij rešenje

        .. activecode:: Karel_if__p1_left_p2_right_p3_forward_solution
            :passivecode: true
          
            from karel import *
            for i in range(3):        # okreni se ka (jedinom) praznom polju
                if not moze_napred():
                    levo()
            
            while moze_napred():
                napred()
                levo()                # probaj da skrenes levo
                if not moze_napred(): # ako ne mozes levo
                    desno(); desno()     # probaj da skrenes desno
                if not moze_napred(): # ako ne mozes ni desno
                    levo()               # probaj pravo u sledecoj iteraciji
            
            uzmi()

Levo kad god može
'''''''''''''''''

.. questionnote::

  Postoji samo jedna loptica i Karel treba da je uzme. Karel će do loptice uvek stići tako što skrene levo kad god može, a inače ide pravo (kad ne može ni levo ni pravo, znači da je stigao). Karel je na početku okrenut kako treba i prvi korak mu je uvek pravo.


.. karel:: Karel_if_p1_left_p2_forward
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████████████',
               '█0.0.0.0.0.0█',
               '█.███████.█.█',
               '█0.0.0.1█0█0█',
               '█████.███...█',
               '█0.0.0.0█0.0█',
               '█████████.███',
               '█E.0.0.0.0.0█',
               '█████████████'
            ],
            [
               '█████████████',
               '█0.0.0.0.0█0█',
               '█..██████.█.█',
               '█0.0█0.0.0█0█',
               '█████..██.█.█',
               '█0.0.0.1█0█0█',
               '█████████..██',
               '█E.0.0.0.0.0█',
               '█████████████'
            ],
            [
               '█████████████',
               '█0.0.0.0.0█0█',
               '█.█.........█',
               '█0█0.0.0.0.0█',
               '█.█.███████.█',
               '█0█0.0.1█0█0█',
               '█.█.█████.█.█',
               '█0.0.0.0.0█N█',
               '█████████████'
            ],
            [
               '█████████████',
               '█S█0.0.0.0█0█',
               '█.███.███...█',
               '█0█0.1█0█..0█',
               '█.███████.█.█',
               '█0.0.0.0.0█0█',
               '█.███████████',
               '█0.0.0.0.0.0█',
               '█████████████'
            ]
         ];
         let choice = random(ww.length);
         var w = ww[choice];
         var ny = Math.floor(w.length / 2);
         var nx = Math.floor(w[0].length / 2);
         var world = new World(nx, ny);
         
         for (let y = 1; y <= ny; y++) {
            let wy = 2*(ny-y) + 1;
            for (let x = 1; x <= nx; x++) {
               let wx = 2*x - 1;
               if (y < ny && w[wy - 1].charAt(wx) == "█") world.addEWWall(x, y, 1);
               if (x < nx && w[wy].charAt(wx + 1) == "█") world.addNSWall(x, y, 1);
               let c = w[wy].charAt(wx);
               let pos = "SWEN".indexOf(c);
               if (pos > -1) {
                  world.setRobotStartAvenue(x);
                  world.setRobotStartStreet(y);
                  world.setRobotStartDirection("SWEN".charAt(pos));
               }
               let d = w[wy].charCodeAt(wx);
               if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
            }
         }
         
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "... # dopunite",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. reveal:: Karel_if_p1_left_p2_forward_reveal
    :showtitle: Pomoć
    :hidetitle: Sakrij pomoć

    Uputstva za jedno moguće rešenje:
    
    .. activecode:: Karel_if_p1_left_p2_forward_solution
        :passivecode: true
      
        dok mozes da ides napred:
            idi napred
            # ako ne postoji put na levo
                # ostani okrenut pravo

        uzmi lopticu

.. commented out
    .. reveal:: Karel_if_p1_left_p2_forward_reveal
        :showtitle: Rešenje
        :hidetitle: Sakrij rešenje

        .. activecode:: Karel_if_p1_left_p2_forward_solution
            :passivecode: true
          
            from karel import *
            while moze_napred():
                napred()
                levo()
                if not moze_napred():
                    desno()

            if ima_loptica_na_polju():
                uzmi()
