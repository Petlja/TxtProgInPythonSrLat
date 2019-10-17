Još kraći programi
==================

Podsetimo se poslednjeg programa prethodne lekcije. Trebalo je da Karel uzme po pet loptica sa svakog od tri naredna polja. 

.. image:: ../../_images/Karel/nested_for_3x5.png
    :width: 300px
    :align: center

Program koji rešava zadatak mogao je da izgleda ovako:

.. activecode:: Karel_nested_for__intro_1
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
        
Vidimo da se u ovom programu sledeća grupa naredbi ponavlja tri puta:

.. activecode:: Karel_nested_for__intro_2
   :passivecode: true

    napred()
    for i in range(5):
        uzmi()

To nam omogućava da dodatno skratimo program. Pri objašnjavanju *for* naredbe smo pomenuli da u telu petlje mogu da se nađu druge petlje. Sada imamo priliku da to iskoristimo.
 
Ugnežđene for naredbe
---------------------

Kada se u telu jedne petlje nalazi druga petlja, onda prvu petlju zovemo spoljna petlja, a drugu unutrašnja. Zajedno ih zovemo ugnežđene ili umetnute petlje. U sledećem primeru ćemo videti kako se pišu ugnežđene *for* naredbe.

Pokupi tri puta po 5 loptica
''''''''''''''''''''''''''''

.. questionnote::

  Ispred Karela su tri polja, a na njima po 5 loptica. Karel treba da pokupi sve loptice.

Zadatak je ponovljen, ali sada ćemo ga rešiti na drugačiji način. 

.. infonote::
   Ranije smo pomenuli da je sa ``i`` u dosadašnjim primerima *for* naredbe imenovano mesto na kome brojimo dokle smo stigli sa ponavljanjem. Sada prvi put treba da u toku brojanja jedne stvari (polja) prebrojimo drugu stvar (loptice). To znači da će na primer biti potrebno da znamo kada smo na trećem polju pri drugoj loptici. Zbog toga ne možemo da koristimo isto ime za oba brojača, pa smo umesto dosadašnjeg ``i`` uveli nova imena za brojače. U programu koji sledi brojač polja smo nazvali ``i_polje``, a za brojač loptica ``i_loptica``. 
   
.. karel:: Karel_for_TakeMxN
   :blockly:

   {
        setup:function() {
           var numAvenues = 4;
           var numBalls = 5;
           var world = new World(numAvenues, 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           for (var k = 2; k <= numAvenues; k++)
              world.putBalls(k, 1, numBalls);
           
           var robot = new Robot();

           var code = ["from karel import *",
                       "for i_polje in range(3):",
                       "    napred()",
                       "    for i_loptica in range(5):",
                       "        uzmi()",
                       ""];
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           return robot.getBalls() == 15; // 3 x 5 balls
        },
   }

U datom rešenju naredba *uzmi()* je dodatno uvučena, jer se ona izvršava po jednom za svako ``i_loptica`` iz opsega [0, 1, 2, 3, 4]. Osim toga, cela naredba ``for i_loptica in range(5):`` se (uz naredbu *napred()*, zajedno sa svojim telom) ponavlja 3 puta, po jednom za svako ``i_polje`` iz opsega [0, 1, 2]. To znači da se naredba *uzmi()* izvršava ukupno 3 x 5 = 15 puta (na svakom od tri polja po pet puta).
   
.. infonote::
   Kod umetnutih petlji je potrebno dodatno paziti na pravilno uvlačenje naredbi, jer ono postaje nešto malo komplikovanije. Pogrešno uvlačenje pojedinih naredbi može da dovede do pogrešnog rezultata, ili do programa koji uopšte ne radi.
  
Zadaci za vežbu
---------------

Preskok
'''''''

.. questionnote::

  Ispred Karela je na svakom trećem polju po jedna loptica, a on treba da ih obe pokupi.
  
Karel treba da ponovi 2 puta grupu naredbi: "tri puta idi napred, a zatim uzmi lopticu".

.. karel:: Karel_for_every_nth_square
    :blockly:

    {
        setup:function() {
            var everyNth = 3;
            var numRepetitions = 2;
            var numBalls = 1;
            var numAvenues = 1 + numRepetitions * everyNth;
            var world = new World(numAvenues, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
           
            for (var k = 1; k <= numRepetitions; k++)
                world.putBalls(1+k*everyNth, 1, numBalls);
            
            var robot = new Robot();
         
            var code = ["from karel import *",
                        "for i_pon in range(2):      # dva puta ponovi sve sto sledi",
                        "    # upotrebite for naredbu da kazete Karelu da ode 3 polja napred",
                        "    uzmi()              #    uzmi lopticu",
                        ""];
    
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
            return robot.getBalls() == 2; // number of repetitions
        },
    }

.. commented out
   .. reveal:: Karel_for_every_nth_square_reveal
       :showtitle: Rešenje
       :hidetitle: Sakrij rešenje
   
       .. activecode:: Karel_for_every_nth_square_solution
           :passivecode: true
         
           from karel import *
           for i_pon in range(2):     # dva puta ponovi sve sto sledi
               for i_polje in range(3):   # idi 3 polja napred
                   napred()
               uzmi()                     # uzmi lopticu

Na svakom trećem po 5
'''''''''''''''''''''

.. questionnote::

  Ispred Karela je na svakom trećem polju po pet loptica, a on treba da ih sve pokupi.
  
Zadatak je sličan prethodnom, treba samo ponavljati uzimanje loptice. Pazite da petlja za uzimanje loptica bude ispod petlje za kretanje napred, a ne u njoj.

.. karel:: Karel_for_every_nth_square_5
    :blockly:

    {
        setup:function() {
            var everyNth = 3;
            var numRepetitions = 2;
            var numBalls = 5;
            var numAvenues = 1 + numRepetitions * everyNth;
            var world = new World(numAvenues, 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
           
            for (var k = 1; k <= numRepetitions; k++)
                world.putBalls(1+k*everyNth, 1, numBalls);
            
            var robot = new Robot();
         
            var code = ["from karel import *",
                        "for i_pon in range(2):      # dva puta ponovi sve sto sledi",
                        "    # upotrebite for naredbu da kazete Karelu da ode 3 polja napred",
                        "    # upotrebite novu for naredbu da kazete Karelu da uzme 5 loptica",
                        ""];
    
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
            return robot.getBalls() == 10; // numRepetitions x numBalls
        },
    }

.. commented out
   .. reveal:: Karel_for_every_nth_square_5_reveal
       :showtitle: Rešenje
       :hidetitle: Sakrij rešenje
   
       .. activecode:: Karel_for_every_nth_square_5_solution
           :passivecode: true
         
           from karel import *
           for i_pon in range(2):     # dva puta ponovi sve sto sledi
               for i_polje in range(3):   # idi 3 polja napred
                   napred()
               for i_loptica in range(5): # uzmi 5 loptica
                   uzmi()


U krug
''''''

.. questionnote::

  Karel ponovo treba da pokupi sve loptice.
  
Spoljna petlja treba da se izvrši 3 puta, a u njoj Karel treba da uradi sledeće:

- Dva puta ponovi korake: "idi napred" i "uzmi lopticu"
- Okreni se levo

.. karel:: Karel_for_ring
    :blockly:

    {
        setup:function() {
            var w = [
               '███████',
               '█1.1.1█',
               '█.███.█',
               '█0.0█1█',
               '█████.█',
               '█E.1.1█',
               '███████'
            ];

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
           return robot.getBalls() == 6;
        }
    }

.. reveal:: Karel_for_ring_reveal_1
    :showtitle: Pomoć
    :hidetitle: Sakrij pomoć

    Uputstvo smo još malo približili programu, probajte da ga pretvorite u naredbe. Ako ipak želite da vidite program, kliknite na dugme "Rešenje".
    
    .. activecode:: Karel_for_ring_solution_1
        :passivecode: true
      
        za svaku od 3 strane:
            za svako od 2 polja:
                idi napred
                uzmi lopticu
            okreni se na levo

    .. reveal:: Karel_for_ring_reveal_2
       :showtitle: Rešenje
       :hidetitle: Sakrij rešenje
   
       .. activecode:: Karel_for_ring_solution_2
           :passivecode: true
         
           from karel import *
           for i_strana in range(3):     # tri puta ponovi sve sto sledi
               for i_polje in range(2):     # dva puta idi napred i uzmi
                   napred()
                   uzmi()
               levo()                       # okreni se duz sledece strane



U krug po 3 loptice
'''''''''''''''''''

.. questionnote::

  Napišite program pomoću koga će Karel da pokupi svih 18 loptica.
  
Razlika u odnosu na prethodni zadatak je u tome što sada uzimanje loptica treba da bude u dodatnoj petlji. To znači da ćemo imati tri ugnežđene petlje: jednu koja broji strane lavirinta, drugu koja broji polja duž jedne strane, i treću koja broji loptice na polju.

.. karel:: Karel_for_ring_3
    :blockly:

    {
        setup:function() {
            var w = [
               '███████',
               '█3.3.3█',
               '█.███.█',
               '█0.0█3█',
               '█████.█',
               '█E.3.3█',
               '███████'
            ];

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
           return robot.getBalls() == 18;
        }
    }

.. reveal:: Karel_for_ring_3_reveal
    :showtitle: Pomoć
    :hidetitle: Sakrij pomoć

    Ponovo dajemo uputstvo koje malo više liči na program (ovaj put bez rešenja).
    
    .. activecode:: Karel_for_ring_3_solution
        :passivecode: true
      
        za svaku od 3 strane:
            za svako od 2 polja:
                idi napred
                za svaku od 3 loptice:
                    uzmi lopticu
            okreni se na levo

.. commented out
   .. reveal:: Karel_for_ring_3_reveal
       :showtitle: Rešenje
       :hidetitle: Sakrij rešenje
   
       .. activecode:: Karel_for_ring_3_solution
           :passivecode: true
         
           from karel import *
           for i_strana in range(3):     # tri puta ponovi sve sto sledi
               for i_polje in range(2):     # dva puta idi napred i uzmi 3 loptice
                   napred()
                   for i_loptica in range(3):
                       uzmi()
               levo()                       # okreni se duz sledece strane


