Proverite pa odlučite
=====================

Naredba while se pokazala kao vrlo korisna, jer smo upotrebljavajući je mogli da rešavamo mnogo raznovrsnije zadatke. Ipak, sledeći primer pokazuje da postoje jednostavni zadaci koje sa ovim što do sada znamo i dalje ne možemo da rešimo. 

Recimo da vam je u nekoj situaciji potrebno da pomerite Karela samo za jedno polje ako je moguće (ako nije moguće, Karel treba da ostane tamo gde je). 

- Ako napišemo samo naredbu *napred()*, rizikujemo poruku o grešci u slučaju da je Karel pred zidom.
- Ako naredbu *napred()* smestimo ispod *while moze_napred():*, rizikujemo da odemo dalje nego što smo želeli.
- Ako ne koristimo naredbu *napred()*, rizkujemo da se ne pomerimo ni onda kada je to moguće (i potrebno).

Očigledno, potrebna nam je neka nova naredba, koja će Karelu reći "ako možeš napred, pomeri se za jedno mesto". 

Naredba if
----------

Naredba koja nam je potrebna u opisanom slučaju je naredba ``if``, koja takođe postoji u skoro svim programskim jezicima. Na pajtonu se ona (u svom jednostavnijem obliku) piše ovako:

.. activecode:: Karel_if__syntax
   :passivecode: true

   if uslov:
       naredba_1
       ...
       naredba_k


.. infonote::

   Vidimo da je pisanje ``if`` naredbe veoma slično pisanju *while* naredbe. Pod ``if`` naredbom se takođe može naći jedna ili više drugih naredbi, koje čine ``telo if naredbe``. Pri tome važe ista pravila za pisanje dvotačke posle uslova i uvlačenje naredbi koje se izvršavaju ako je uslov ispunjen. Razlika je u tome što se naredbe u telu *if* naredbe neće ponavljati - ako je uslov ispunjen one će se izvršiti samo jedanput.

   Naredba ``if`` se zove i *naredba grananja* zato što se tok izvršavanja programa kod ove naredbe grana: sledeća naredba koja će se izvršiti zavisi od odgovora na pitanje iz uslova.


U pomenutom primeru, trebalo bi pisati:


.. activecode:: Karel_if__example
   :passivecode: true

   if moze_napred():
       napred()


Slede zadaci u kojima se (pored ranije upoznatih) koristi ``if`` naredba.


Uzmi jednu lopticu ako ih ima
'''''''''''''''''''''''''''''

.. questionnote::

   Ispred Karela je jedno polje, na kome se nalazi nula ili više loptica. Napišite program na osnovu koga će Karel preći na to polje, a zatim uzeti tačno jednu lopticu ako na polju ima bar jedna loptica.
   
   Pokrenite program više puta da biste ga testirali na različitim primerima.
   

U našem slučaju, uslov će biti ``ima_loptica_na_polju()``, a naredba koja se uslovno izvršava je ``uzmi()``.

.. karel:: Karel_if__take_one_if_any
   :blockly:

   {
      setup:function() {
          var world = new World(2, 1);
          world.setRobotStartAvenue(1);
          world.setRobotStartStreet(1);
          world.setRobotStartDirection("E");
          if (Math.random() > 0.5)
             world.putBalls(2, 1, 1 + Math.floor(7 *  Math.random()));
      
      var robot = new Robot();
      
      var code = ["from karel import *",
                  "napred()",
                  "if ...         # dopunite",
                  "    uzmi()",
                  ""];
          return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return world.getBalls(1, 1) === 0 &&
            (robot.getBalls() === 1 ||
            (robot.getBalls() === 0 && world.getBalls(2, 1) === 0));
      }
   }

.. commented out
   .. reveal:: Karel_if__take_one_if_any_reveal
       :showtitle: Rešenje
       :hidetitle: Sakrij rešenje
       
       Rešenje:
   
       .. activecode:: Karel_if__take_one_if_any_solution
           :passivecode: true
         
           from karel import *
           napred()
           if ima_loptica_na_polju():
               uzmi()


Idi do kraja i pokupi po jednu lopticu gde ih ima
'''''''''''''''''''''''''''''''''''''''''''''''''

.. questionnote::

  Ispred Karela je bar jedno polje, a može ih biti bilo koliko. Na svakom polju ima nula ili više loptica. Karel treba da pokupi po tačno jednu lopticu sa svakog polja na kome ima loptica.
  
  Pokrenite program više puta da biste ga testirali na različitim primerima.

Ovde je potrebno koristiti while naredbu za napredovanje, a posle svakog napredovanja u telu while petlje treba koristiti if naredbu za proveru da li Karel stoji na polju sa lopticom.
  
.. karel:: Karel_if__many_squares_take_one_if_any
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var N = 2 + random(8);
         var world = new World(N, 1);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("E");
          for (var k = 2; k <= N; k++)
             if (Math.random() > 0.5)
                world.putBalls(k, 1, 2 + random(3)); // need initial world to replace '2'->'1'
      
         var robot = new Robot();
      
         var code = ["from karel import *",
                     "while moze_napred():",
                     "    napred()",
                     "    if ... # dopunite",
                     "       ... # dopunite",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         var N = world.getAvenues();
         var nonEmpty = 0;
         for (var k = 1; k <= N; k++)
            if (world.getBalls(k, 1) > 0)
               nonEmpty++;
               
         return robot.getBalls() === nonEmpty;
      }
   }

.. commented out
   .. reveal:: Karel_if__many_squares_take_one_if_any_reveal
       :showtitle: Rešenje
       :hidetitle: Sakrij rešenje
       
       Rešenje:
   
       .. activecode:: Karel_if__many_squares_take_one_if_any_solution
           :passivecode: true
         
           from karel import *
           while moze_napred():
               napred()
               if ima_loptica_na_polju():
                   uzmi()


Ako ne radiš to, uradi ovo (if-else)
------------------------------------

U nekim zadacima treba uraditi jednu stvar ako je neki uslov ispunjen, a neku drugu stvar ako nije ispunjen. U tom slučaju možemo da koristimo prošireni oblik  *if* naredbe, koji izgleda ovako:

.. activecode:: Karel_if__else_syntax
    :passivecode: true

    if uslov:
        naredba_a1
        ...
        naredba_ak
    else:
        naredba_b1
        ...
        naredba_bm


.. infonote::

   U proširenom obliku ``if`` naredbe prvi deo (do reči ``else``) ima isti izgled i značenje kao i do sada. U nastavku se piše reč ``else`` jednako uvučena kao i reč ``if``, zatim se piše dvotačka, a ispod sledi jedna ili više drugih naredbi, koje čine ``telo else grane``. Ova druga grupa naredbi se piše uvučeno u odnosu na reč ``else``, a izvršava se ako uslov naveden u ``if`` naredbi nije ispunjen.

    
Primer - uzimanje i ostavljanje loptica
'''''''''''''''''''''''''''''''''''''''

.. questionnote::

   Ispred Karela su 3 polja, a na svakom od njih može da bude po jedna ili nijedna loptica. Karel treba da uzme loptice sa onih polja na kojima se nalaze i da ih postavi na ona polja na kojima se ne nalaze. Karel na početku ima dovoljno loptica kod sebe.

Pomoću novog, proširenog oblika ``if`` naredbe, Karelu možemo da kažemo: "Ako je na polju loptica, onda uzmi tu lopticu, inače ostavi jednu lopticu", tako da se zadatak lako rešava:

.. karel:: Karel_if__take_else_put
    :blockly:
   
    {
      setup: function() {
       var world = new World(4, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
       world.balls = [];
       for (var k = 2; k <= world.getAvenues(); k++) {
          var ball = Math.random() > 0.5;
          world.balls.push(ball);
          if (ball)
                  world.putBall(k, 1);
           }
           var robot = new Robot();
       robot.setInfiniteBalls(true);
       var code = ["from karel import *",
        "for i in range(3):",
        "    napred()",
        "    if ima_loptica_na_polju():",
        "        uzmi()",
        "    else:",
        "        ostavi()"
       ]
       return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
       for (var k = 2; k <= world.getAvenues(); k++)
              if (world.getBalls(k, 1) == world.balls[k-2])
             return false;
       return true;
      }
    }


Pokupi loptice do kojih možeš da dođeš
''''''''''''''''''''''''''''''''''''''


.. questionnote::

   Lavirint se sastoji od dva reda. Karel se nalazi u gornjem redu, koji je prohodan do kraja. U donjem redu mogu da se nalaze prepreke ili polja sa po jednom lopticom. Karelov zadatak je da pokupi sve loptice.
   
.. karel:: Karel_if__take_all_from_lower_row
    :blockly:
   
    {
      setup: function() {

         function random(n) {
             return Math.floor(n * Math.random());
         }

         var world = new World(4 + random(4), 2);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(2);
         world.setRobotStartDirection("E");

         world.addEWWall(1, 1, 1);
         var balls = 0;
         var prevBall = false;
         for (var i = 2; i <= world.getAvenues(); i++) {
             if (random(2) == 0 || (balls == 0 && i == world.getAvenues() - 1)) {
                 balls++;
                 if (!prevBall)
                    world.addNSWall(i-1, 1, 1);
                 world.putBall(i, 1);
                 prevBall = true;
             } else {
                 if (prevBall)
                    world.addNSWall(i-1, 1, 1);
                 world.addEWWall(i, 1, 1);
                 prevBall = false;
             }
         }

         var robot = new Robot();
         var code = ["from karel import *",
            "while moze_napred():",
            "    napred() # sledece polje",
            "",
            "    # proveri donji red",
            "    desno()             # okreni se prema jugu",
            "    if moze_napred():   # ako postoji polje u donjem redu",
            "        # recite Karelu da ode po lopticu  uzme je, ",
            "        # da se vrati na sadasnje polje i okrene se ka istoku",
            "    # recite Karelu, ako nije mogao da predje na donji red,",
            "    # da se ponovo okrene ka istoku radi nastavka",
         ]
         return {world: world, robot: robot, code: code};
      },

      isSuccess: function(robot, world) {
           for (var i = 1; i <= world.getAvenues(); i++)
              for (var j = 1; j <= world.getStreets(); j++)
                 if (world.getBalls(i, j) != 0)
                    return false;
          return true;
      }
    }
   
.. commented out
   .. reveal:: Karel_if__take_all_from_lower_row_reveal
       :showtitle: Prikaži rešenje
       :hidetitle: Sakrij rešenje
   
       Jedno moguće rešenje (ne i jedino) je sledeće.               
   
       .. activecode:: Karel_if__take_all_from_lower_row_solution
           :passivecode: true
                       
           from karel import *
           while moze_napred():
               napred() # sledece polje
               
               # proveri donji red
               desno()  # okreni se prema jugu
               if moze_napred(): # ako postoji polje u donjem redu
                   napred(); uzmi() # idi po lopticu i uzmi je
                   levo(); levo(); napred(); desno() # u gornji red, ka istoku
               else:
                   levo() # ka istoku


Radi samo kad nešto nije
------------------------

Neka je potrebno da se Karel okrene levo ako **ne može** da ide napred (ako može da ide napred, ne treba da radi ništa).

Prema pravilima pisanja *if* naredbe, posle uslova (u telu prve grane) mora da postoji bar jedna naredba, a prema logici zadatka nam nije potrebna ni jedna naredba na tom mestu. U takvim situacijama možemo da pišemo:

.. activecode:: Karel_if__else_only
    :passivecode: true

    if moze_napred():
        pass
    else:
        levo()

ili 

.. activecode:: Karel_if__not
    :passivecode: true

    if not moze_napred():
        levo()

U prvom slučaju koristimo specijalnu naredbu ``pass`` koja ne radi ništa. Time je zadovoljena i sintaksa (pravila pisanja), a dobili smo i program koji radi kako želimo.

U drugom slučaju, pomoću reči ``not`` pravimo suprotan uslov, što znači da je uslov *if* naredbe ispunjen kada Karel ne može da ide napred. U ovom slučaju grane menjaju uloge i onda nam *else* grana više nije potrebna.

Sledi par sličnih zadataka, u kojima takođe treba nešto uraditi samo kada uslov nije ispunjen.

Okreni se ka praznom polju
''''''''''''''''''''''''''


.. questionnote::

   Karel može da bude okrenut na bilo koju stranu, ali samo u jednom smeru može da započne kretanje. Potrebno je da se Karel okrene ka slobodnom polju i da napravi jedan korak.
   
.. karel:: Karel_if__turn_to_free_square
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████',
               '█N.0█',
               '█████'
            ],
            [
               '█████',
               '█S.0█',
               '█████'
            ],
            [
               '█████',
               '█E.0█',
               '█████'
            ],
            [
               '█████',
               '█W.0█',
               '█████'
            ],
            [
               '███',
               '█0█',
               '█.█',
               '█E█',
               '███'
            ],
            [
               '███',
               '█0█',
               '█.█',
               '█W█',
               '███'
            ],
            [
               '███',
               '█0█',
               '█.█',
               '█S█',
               '███'
            ],
            [
               '███',
               '█0█',
               '█.█',
               '█N█',
               '███'
            ],
            [
               '███████',
               '█0.0.N█',
               '███████'
            ],
            [
               '███████',
               '█0.0.S█',
               '███████'
            ],
            [
               '███████',
               '█0.0.W█',
               '███████'
            ],
            [
               '███████',
               '█0.0.E█',
               '███████'
            ],
            [
               '█████',
               '█0█N█',
               '█.█.█',
               '█0.0█',
               '█████'
            ],
            [
               '█████',
               '█0█S█',
               '█.█.█',
               '█0.0█',
               '█████'
            ],
            [
               '█████',
               '█0█W█',
               '█.█.█',
               '█0.0█',
               '█████'
            ],
            [
               '█████',
               '█0█E█',
               '█.█.█',
               '█0.0█',
               '█████'
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
         var X = world.getAvenues();
         var Y = world.getStreets();
         if (X == 2 && Y == 1) return robot.getAvenue() == 2 && robot.getStreet() == 1 && robot.getDirection() == "E";
         if (X == 1 && Y == 2) return robot.getAvenue() == 1 && robot.getStreet() == 2 && robot.getDirection() == "N";
         if (X == 3 && Y == 1) return robot.getAvenue() == 2 && robot.getStreet() == 1 && robot.getDirection() == "W";
         if (X == 2 && Y == 2) return robot.getAvenue() == 2 && robot.getStreet() == 1 && robot.getDirection() == "S";
         return false;
      }
   }

.. reveal:: Karel_if__turn_to_free_square_reveal
    :showtitle: Rešenje
    :hidetitle: Sakrij rešenje

    Nudimo vam dva kratka rešenja:
   
    .. activecode:: Karel_if__turn_to_free_square_solution1
        :passivecode: true
      
        from karel import *
        while not moze_napred():
            levo()
        napred()

    .. activecode:: Karel_if__turn_to_free_square_solution2
        :passivecode: true
      
        from karel import *
        for i in range(3):
            if not moze_napred():
                levo()
        napred()
                
Dodaj loptice gde ih nema
'''''''''''''''''''''''''

.. questionnote::

   Ispred Karela je nepoznat broj polja, a na svakom od njih može da bude po jedna ili ni jedna loptica. Karel ima dovoljno loptica kod sebe, a treba da stavi po jednu lopticu na svako polje na kome nema loptice.

.. karel:: Karel_if__fill_the_empty_squares
    :blockly:
   
    {
        setup: function() {
            function random(n) {
                return Math.floor(n * Math.random());
            }
            var N = 2 + random(5);
            var world = new World(N, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            world.balls = [];
            world.putBall(1, 1);
            for (var k = 2; k <= world.getAvenues(); k++) {
                var ball = Math.random() > 0.5;
                world.balls.push(ball);
                if (ball)
                    world.putBall(k, 1);
            }
            var robot = new Robot();
            robot.setInfiniteBalls(true);
            var code = ["from karel import *",
                        "# dopunite"
                        ]
            return {world: world, robot: robot, code: code};
        },

        isSuccess: function(robot, world) {
            for (var k = 1; k <= world.getAvenues(); k++)
                if (world.getBalls(k, 1) != 1)
                    return false;
            return true;
        }
    }
