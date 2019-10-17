Napravite paket naredbi
=======================

Podsetimo se zadatka *Uzmi lopticu na susednom polju*. Zadatak je bio da Karel u svakom smeru pokuša da ode na susedno polje i (ako uspe da ode na susedno polje) da pokuša da uzme lopticu tamo. Naravno, da bi Karel mogao da pokuša u sledećem smeru, bilo je potrebno i da se posle svakog pokušaja vrati na polazno polje.

Program koji rešava zadatak može da izgleda ovako:

.. activecode:: Karel_functions__take_neighboring_ball_1
    :passivecode: true

    from karel import *
    for i in range(4):          # u svakom od 4 smera
        if moze_napred():       # potrazi polje u tom smeru
            napred()
            if ima_loptica_na_polju():
                uzmi()
            levo()              # vrati se na polazno polje
            levo()
            napred()
            levo()              # okreni se ka polju koje si probao
            levo()
        levo()                  # sledeci smer

Verovatno vam je deo programa od sedme do jedanaeste linije malo teži za praćenje. U tom delu možda zamišljate Karela kako izvršava naredbu po naredbu da biste sasvim razumeli šta se tu dešava.

Komentari donekle pomažu da se ovaj deo programa lakše razume. Pored komentara, još bolje bi bilo kada bi postojala funkcija *nazad()*, pomoću koje bi Karel napravio korak unazad. Tada bi program bio kraći i jasniji:

.. activecode:: Karel_functions__take_neighboring_ball_2
    :passivecode: true

    from karel import *
    for i in range(4):          # u svakom od 4 smera
        if moze_napred():       # potrazi polje u tom smeru
            napred()
            if ima_loptica_na_polju():
                uzmi()
            nazad()             # vrati se na polazno polje
        levo()                  # sledeci smer
        
Funkcija *nazad()* nije deo Karel biblioteke, ali možemo vrlo jednostavno da sami napravimo tu funkciju. Kada je napravimo, funkciju *nazad()* moći ćemo da je koristimo ravnopravno sa funkcijama biblioteke *Karel* kao što su *napred()*, *desno()* i ostale.

Kako se pišu funkcije
---------------------

Za sada ćemo se upoznati samo sa najjednostavnijim načinom pisanja funkcije u Pajtonu, a ostale, složenije oblike ćemo upoznavati kasnije.

.. activecode:: Karel_functions__function_def
    :passivecode: true

    def ime_funkcije():
        naredba_1
        ...
        naredba_k

.. infonote::
      
   Pri pisanju bilo koje funkcije na Pajtonu, reč ``def`` na početku, zagrade ``()`` i dvotačka ``:`` na kraju prvog reda su obvavezni. Kao *ime_funkcije* može se pojaviti bilo koje pravilno napisano ime koje mi izaberemo. Naredbe koje slede, pišu se uvučeno i čine telo funkcije (ako se piše više naredbi u jednom redu, onda se te naredbe razdvajaju znakom tačka-zarez). Naredbe u telu funkcije će se izvršiti svaki put kada se pri izvršavanju programa naiđe na ime funkcije, to jest kada ta funkcija bude pozvana.

U skladu sa ovim pravilima, funkciju *nazad()* možemo da napišemo ovako:

.. activecode:: Karel_functions__backwards_def
    :passivecode: true

    def nazad():
        levo(); levo()
        napred()
        levo(); levo()

Tada bi ceo program izgledao ovako:
   
.. karel:: Karel_functions__take_neighboring_ball_final
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
                     "def nazad():",
                     "    levo(); levo()",
                     "    napred()",
                     "    levo(); levo()",
                     "",    
                     "for i in range(4):",
                     "    if moze_napred():",
                     "        napred()",
                     "        if ima_loptica_na_polju():",
                     "            uzmi()",
                     "        nazad()",
                     "    levo()  # sledeci smer",
                     ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }

.. infonote::
    Kada neku logičku celinu izdvojimo u funkciju, možemo da pišemo programe koji su kraći i jasniji, jer smo problem razložili na delove koji su manje složeni.
    
    Još jedna prednost od pisanja funkcija je da ih lako možemo iskoristiti u drugim programima (ovde ćemo napisane funkcije povremeno kopirati, ali u realnom programiranju postoji bolji i jednostavniji način).


Izlazak iz funkcije ili petlje pre njenog kraja
-----------------------------------------------

U primeru traženja loptice na susednom polju, radi jednostavnosti programa smo odlučili da Karel i kad nađe lopticu, on nastavlja da je traži u preostalim smerovima. Postoji način da izbegnemo ovo nepotrebno izvršavanje preostalih naredbi. 

.. infonote::
    **Kada želimo da prekinemo izvršavanje petlje**, pišemo specijalnu naredbu ``break``. Efekat naredbe *break* je da "iskočimo" iz petlje i nastavimo izvršavanje programa od prve naredbe posle petlje.
    
    Naredbom *break* ćemo iskočiti iz najbliže (najuže) *for* ili *while* petlje koja sadrži ovu naredbu. Ako se *break* naredba nalazi u dve ili više ugnežđenih petlji, izvršavanje se nastavlja naredbom koja sledi posle unutrašnje (najuže) petlje. 
    
Koristeći naredbu *break*, mogli bismo glavni deo programa 

.. activecode:: Karel_functions__break_intro_1
    :passivecode: true

    for i in range(4):
        if moze_napred():
            napred()
            if ima_loptica_na_polju():
                uzmi()
            nazad()
        levo()  # sledeci smer

da prepravimo u:

.. activecode:: Karel_functions__break_intro_2
    :passivecode: true

    for i in range(4):
        if moze_napred():
            napred()
            if ima_loptica_na_polju():
                uzmi()
                break
            nazad()
        levo()  # sledeci smer

Na taj način se iz petlje izlazi čim je loptica pronađena i uzeta. Pošto posle ove petlje nema drugih naredbi, u ovom slučaju se izvršavanjem naredbe *break* završava i rad programa.

~~~~

Vrlo slično izlasku iz petlje, iz funkcije takođe možemo da izađemo pre nego što se sve njene naredbe izvrše.

.. infonote::
    **Kada želimo da prekinemo izvršavanje funkcije**, pišemo specijalnu naredbu ``return``. Efekat naredbe *return* je da "iskočimo" iz funkcije i nastavimo izvršavanje programa od prve naredbe posle mesta odakle je funkcija pozvana.
    
    Naredbom *return* iskačemo iz funkcije bez obzira na to koliko petlji okružuje naredbu *return*.

Od programa za uzimanje loptice na susednom polju možemo da napravimo funkciju. U tom slučaju bismo mogli da pišemo:

.. activecode:: Karel_functions__return_intro
    :passivecode: true

    def uzmi_na_susednom_polju():
        for i in range(4):
            if moze_napred():
                napred()
                if ima_loptica_na_polju():
                    uzmi()
                    return # izlazak iz funkcije
                nazad()
            levo()  # sledeci smer
            
    uzmi_na_susednom_polju()
    
Zadaci za vežbu
---------------

Ostavljaj loptice dok ima loptica i polja
'''''''''''''''''''''''''''''''''''''''''

.. questionnote::

    Karel na početku ima nekoliko loptica i treba da ih rasporedi duž puta po jednu na svako polje (počevši od polja na kome stoji) dokle je moguće. Karel prekida sa postavljanjem loptica kada naiđe na prepreku ili kada ostane bez loptica (šta god se pre dogodi). Pri tome nije važno da li će se Karel zaustaviti na poslednjem popunjenom, ili na prvom praznom polju.
    
Predlog: Stavite jedan od ova dva uslova u *while* petlju, tako da se petlja završi kada uslov ne bude više ispunjen. Koristite *break* naredbu da izađete iz petlje ako drugi uslov nije ispunjen.
    
.. karel:: Karel_functions__put_balls_until_wall_or_no_more_balls
   :blockly:

    {
        setup:function() {
            function random(n) {
                return Math.floor(n * Math.random());
            }
            var choice = random(3); // need initial world to get rid of 'choice'
            var N = [3, 4, 5];
            var world = new World(N[choice], 1);
            world.setRobotStartAvenue(1);
            world.setRobotStartStreet(1);
            world.setRobotStartDirection("E");
            
            var robot = new Robot();
            if (choice == 0) robot.setBalls(3);
            if (choice == 1) robot.setBalls(6);
            if (choice == 2) robot.setBalls(2);
           
            var code = ["from karel import *",
                        " # dopunite",
                        ""];
                        
            //var code = ["from karel import *",
            //            "while ima_loptica_kod_sebe():",
            //            "    ostavi()",
            //            "    if not moze_napred():",
            //            "        break",
            //            "    napred()",
            //            ""];
                        
            return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
            var X = world.getAvenues();
            var zeroBallsFound = false;
            for (var x = 1; x <= X; x++) {
                var b = world.getBalls(x, 1);
                if (b > 1) return false;
                if (b == 1 && zeroBallsFound) return false;
                if (b == 0) zeroBallsFound = true;
            }
           
           if (robot.getBalls() > 0 && zeroBallsFound)
               return false;
                 
           return true;
        },
    }

Pomeri sve loptice unazad
'''''''''''''''''''''''''

.. questionnote::

    Ispred Karela je prav put nepoznate dužine. Na početnom polju nema loptica. Karel treba da svaku lopticu premesti za jedno polje ka levoj strani ekrana.
  
Ovaj zadatak možete da rešite tako što, dok god ima polja ispred Karela, ponavljate sledeće korake:

- pređi na sledeće polje
- uzmi sve loptice sa tog polja
- idi korak nazad (to jest, okreni se dva puta i idi napred)
- ostavi sve loptice
- vrati se na polje sa kojeg si uzeo loptice

Pri tome, za vraćanje na polje na koje Karel premešta loptice možete da koristite ranije napisanu funkciju *nazad()*. Treba samo da je iskopirate ili prepišete u prostor za rešavanje.

.. karel:: Karel_functions__all_balls_one_square_back
   :blockly:

    {
        setup:function() {
           function random(n) {
              return Math.floor(n * Math.random());
           }
           var choice = random(3); // need initial world to get rid of 'choice'
           var N = [3, 4, 5];
           var world = new World(N[choice], 1);
           world.setRobotStartAvenue(1);
           world.setRobotStartStreet(1);
           world.setRobotStartDirection("E");
           
           var B = 0;
           if (Math.random() > 0.8) B = random(3);
           if (choice == 0) {
              world.putBalls(2, 1, B);
              world.putBalls(3, 1, B + 2);
           }
           if (choice == 1) {
              world.putBalls(2, 1, B);
              world.putBalls(3, 1, B + 3);
              world.putBalls(4, 1, B + 1);
           }
           if (choice == 2) {
              world.putBalls(2, 1, B);
              world.putBalls(3, 1, B + 2);
              world.putBalls(4, 1, B + 1);
              world.putBalls(5, 1, B + 0);
           }

           var robot = new Robot();

           var code = ["from karel import *",
                       "",
                       "# kopirajte funkciju 'nazad'()",
                       "",
                       "while moze_napred():   # dok ima polja ispred Karela, ponavljaj",
                       "    napred();              # idi napred",
                       "    # dopunite             # pokupi sve loptice sa polja",
                       "    # dopunite             # idi jedno polje nazad",
                       "    # dopunite             # ostavi sve loptice",
                       "    # dopunite             # vrati se napred na ispraznjeno polje",
                       ""];
                       
           return {robot:robot, world:world, code:code};
        },
    
        isSuccess: function(robot, world) {
           var N = world.getAvenues();
           var B = world.getBalls(1, 1);
           if (N == 3) {
              if (world.getBalls(2, 1) != B + 2)
                return false;              
           }
           if (N == 4) {
              if (world.getBalls(2, 1) != B + 3)
                return false;
              if (world.getBalls(3, 1) != B + 1)
                return false;              
           }
           if (N == 5) {
              if (world.getBalls(2, 1) != B + 2)
                return false;
              if (world.getBalls(3, 1) != B + 1)
                return false;
              if (world.getBalls(4, 1) != B + 0)
                return false;
           }
           
           if (world.getBalls(N, 1) != 0) 
              return false;

           if (robot.getBalls() > 0)
                 return false;
                 
           return true;
        },
    }
   
.. reveal:: Karel_functions__all_balls_one_square_back_reveal
    :showtitle: Rešenje
    :hidetitle: Sakrij rešenje

    .. activecode:: Karel_functions__all_balls_one_square_back_solution
        :passivecode: true
      
        from karel import *
        def nazad():     # idi jedno polje nazad, ostani isto okrenut
            levo(); levo();
            napred(); 
            levo(); levo();

        while moze_napred():   # dok ima polja ispred Karela, ponavljaj
            napred();                     # idi na novo polje
            while ima_loptica_na_polju(): # uzmi sve loptice na polju
                uzmi()            
            nazad()                       # korak nazad
            while ima_loptica_kod_sebe(): # ostavi sve loptice
                ostavi()
            napred()                      # idi na polje koje si ispraznio


Prati loptice
'''''''''''''

.. questionnote::

    Na svakom polju se nalazi po jedna ili nijedna loptica. Polja sa lopticama formiraju put, koji počinje na polju pored Karela. Karel treba da prati taj put i da pokupi sve loptice.

Predlog: radi rešavanja ovog zadatka možete da napišete funkciju *na_neprazno_susedno_polje()*, koja treba samo da premesti Karela na susedno polje na kome postoji loptica (pri tome naredba *return* može da bude korisna). Funkcija *na_neprazno_susedno_polje* treba da se razlikuje od ranije napisane funkcije *uzmi_na_susednom_polju()* samo po tome što ne uzima lopticu.

Kada Karel pokupi sve loptice, sledeći poziv ove funkcije će ostaviti Karela na nekom praznom polju (to će biti polje na kome je Karel uzeo poslednju lopticu). Po tome što nema loptice na polju na kome se nalazi Karel, znaćemo da je Karel već uzeo sve loptice.

.. karel:: Karel_functions__follow_the_balls
   :blockly:

    {
        setup:function() {
            function random(n) {
                return Math.floor(n * Math.random());
            }
         
            var ww = [
                [
                   '███████████',
                   '█0.0.1.1.0█',
                   '█.........█',
                   '█0.N.0.1.0█',
                   '█.........█',
                   '█0.1.1.1.0█',
                   '███████████'
                ],
                [
                   '███████████',
                   '█1.1.1.1.1█',
                   '█.........█',
                   '█1.0.0.0.1█',
                   '██........█',
                   '█S.1.1.1.1█',
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
                        "def nazad():",
                        "    levo(); levo()",
                        "    napred()",
                        "    levo(); levo()",
                        "",    
                        "def na_neprazno_susedno_polje():",
                        "    # napisite funkciju",
                        "",
                        "na_neprazno_susedno_polje()",
                        "while ??? # dodajte uslov",
                        "    uzmi()",
                        "    ??? # dopunite",
                        ""];
                     
            //var code = ["from karel import *",
            //            "def nazad():",
            //            "    levo(); levo()",
            //            "    napred()",
            //            "    levo(); levo()",
            //            "",
            //            "def na_neprazno_susedno_polje():",
            //            "    for i in range(4):",
            //            "        if moze_napred():",
            //            "            napred()",
            //            "            if ima_loptica_na_polju():",
            //            "                return",
            //            "            nazad()",
            //            "        levo()  # sledeci smer",
            //            "",
            //            "na_neprazno_susedno_polje()",
            //            "while ima_loptica_na_polju():",
            //            "    uzmi()",
            //            "    na_neprazno_susedno_polje()",
            //            ""];
            
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
            var X = world.getAvenues();
            var Y = world.getStreets();
            for (var y = 1; y <= Y; y++)
                for (var x = 1; x <= X; x++)
                    if (world.getBalls(x, y) > 0)
                        return false;
               
            return true;
        },
    }



Uzmi sve loptice sa cele table
''''''''''''''''''''''''''''''

.. questionnote::

  Karel je na početku okrenut ka severu (gore), a nalazi se u donjem levom uglu pravougaone table nepoznate veličine, bez unutrašnjih zidova. Na svakom polju može biti bilo koliko loptica. Karel treba da uzme sve loptice sa svih polja table.

Predlog: Napišite funkciju *isprazni_red()*, pomoću koje Karel:

- okreće se na levo (na istoku, tj. desnoj strani ekrana, gledajući duž reda na čijem je početku)
- prolazi ceo red tabele i usput uzima sve loptice sa svakog polja iz tog reda, uključujući i prvo polje u redu, sa koga je krenuo
- okreće se ka početku reda (ka zapadu, tj. ka desnoj strani ekrana)
- vraća se na početak reda i okreće se na severu (gore), kao što je stajao pre poziva funkcije

Program koji rešava zadatak pomoću ove funkcije nije dugačak. Potrebno je:

- isprazniti prvi red
- dok ima redova ispred Karela, ići na sledeći red i isprazniti ga

.. karel:: Karel_functions_take_all_balls_2D
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }

         var sizes = [1, 2, 3, 3, 4, 4, 4];
         var numBalls = [0, 0, 1, 1, 1, 3];
         var X = sizes[random(sizes.length)];
         var Y = sizes[random(sizes.length)];
         var world = new World(X, Y);
         world.setRobotStartAvenue(1);
         world.setRobotStartStreet(1);
         world.setRobotStartDirection("N");
         
         for (var col = 1; col <= X; col++) {
             for (var row = 1; row <= Y; row++) {
                 let B = numBalls[random(numBalls.length)];
                 world.putBalls(col, row, B);
             }
         }
      
         var robot = new Robot();
         
         var code = ["from karel import *",
                     "# dopunite",
                     ""];
        //var code = ["from karel import *
        //            "def isprazni_red():",
        //            "    desno()                            # okreni se ka kraju reda (ka istoku)",
        //            "    while ima_loptica_na_polju():      # isprazni prvo polje u redu",
        //            "        uzmi()",
        //            "    while moze_napred():               # dok ima jos polja u redu",
        //            "        napred()                           # predji na novo polje",
        //            "        while ima_loptica_na_polju():      # isprazni novo polje",
        //            "            uzmi()",
        //            "        ",
        //            "    desno(); desno()                   # okreni se ka pocetku reda (ka zapadu)",
        //            "    while moze_napred():               # vrati se na pocetak reda",
        //            "        napred()",
        //            "    desno()                            # okreni se ka sledecem redu (ka severu)",
        //            "",
        //            "isprazni_red()                 # pokupi loptice iz prvog reda",
        //            "while moze_napred():           # dok ima jos redova",
        //            "    napred(); isprazni_red()   #     predji u sledeci red i isprazni ga",
        //            ""];

         return {robot:robot, world:world, code:code};
        },

        isSuccess: function(robot, world) {
           var X = world.getAvenues();
           var Y = world.getStreets();
           for (var col = 1; col <= X; col++) {
              for (var row = 1; row <= Y; row++) {
                 if (world.getBalls(col, row) > 0)   
                    return false;
              }
           }
                 
           return true;
      },
   }
