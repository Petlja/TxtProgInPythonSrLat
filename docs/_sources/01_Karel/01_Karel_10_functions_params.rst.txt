Dodatna uputstva funkciji
=========================

Pomenuli smo da postoji nekoliko načina pisanja funkcija u Pajtonu, a da su funkcije koje smo do sada pisali i koristili najprostijeg oblika. Takve su na primer funkcije *napred()*, *levo()*, *desno()* , *uzmi()* i *ostavi()* iz biblioteke Karel, kao i funkcije *nazad()*, *uzmi_na_susednom_polju()* i *na_neprazno_susedno_polje()*, koje smo sami pisali. Sve ove funkcije obavljaju neki konkretan posao, uvek na isti način. 

Funkcije mogu da se pišu i tako da u različitim izvršavanjima ne rade uvek sasvim istu stvar, nego da obavljaju malo opštiji zadatak. Za takve funkcije mi pri njihovom pozivanju preciznije navodimo kako tačno želimo da se zadatak obavi. Na primer, često bi mogla da nam bude korisna funkcija koja bi pomerila Karela za neki broj polja napred ili nazad. Za tu funkciju želimo da pri njenom pozivanju preciziramo zahtev - za koliko polja Karel treba da se pomeri i na koju stranu.

Funkcije sa parametrima
-----------------------

.. infonote::
    Dodatne informacije koje dajemo funkciji pišu se između zagrada posle imena funkcije, u prvom redu njene definicije. Između zagrada možemo da navedemo jednu vrednost, ili više vrednosti razdvojenih zarezima. Te vrednosti se nazivaju **argumenti** funkcije, ili **parametri** funkcije. Reči "argumenti" i "parametri" su u programiranju sinonimi i koristićemo ih ravnopravno.
    
.. activecode:: Karel_functions__function_with_args_def
    :passivecode: true

    def ime_funkcije(parametar1, ... parametarN):
        naredba_1
        ...
        naredba_k

Funkcija koja pomera Karela za zadati broj polja napred ili nazad, mogla bi da se zove *idi* i da ima jedan parametar, čija vrednost je ceo broj. Ako je taj parametar pozitivan, Karel bi se pomerio toliko polja napred, a ako je negativan, Karel bi išao odgovarajući (suprotan) broj polja nazad. Na primer, poziv *idi(5)* bi značio "idi 5 polja napred", dok bi *idi(-2)* značio "idi 2 polja nazad". Evo kako možemo da napišemo takvu funkciju:

.. activecode:: Karel_functions__function_go_def
    :passivecode: true

    def idi(n):
        if n > 0:
            for i in range(n):
                napred()
        else:
            levo();levo()
            for i in range(-n):
                napred()
            levo();levo()
 
Ova funkcija može da pojednostavi mnoge programe u kojima Karel treba da više puta ide duž jednog hodnika na jednu i drugu stranu. Sledi primer.


Obavi zadata premeštanja
''''''''''''''''''''''''

.. questionnote::

    Karel se nalazi na početnom polju hodnika dovoljne dužine, a treba da obavi sledeća premeštanja loptica:

    - 3 loptice sa polja 3 na polje 4
    - 4 loptice sa polja 5 na polje 1

Pri rešavanju ovog zadatka koristićemo opisanu funkciju *idi*. Da bismo dodatno pojednostavili program, možemo da uvedemo i funkciju *premesti*, koja premešta zadati broj loptica za zadati broj polja napred ili nazad. Iz ovog opisa se vidi da funkcija *premesti* treba da ima dva argumenta. 

Da bi bilo jasnije čemu služi koji argument, daćemo im imena koja opisuju njihovu ulogu:

.. activecode:: Karel_functions__function_displace_def
    :passivecode: true

    def premesti(br_loptica, br_polja):
        for i in range(br_loptica):
            uzmi()
        idi(br_polja)
        for i in range(br_loptica):
            ostavi()
            
Funkcija *premesti* koristi pri svom izvršavanju ranije napisanu funkciju *idi*. Ovakvi pozivi funkcije iz druge funkcije mogu ići u dubinu koliko god nam je potrebno. Važno je jedino da da svaka funkcija bude definisana pre nego što je pozovemo na izvršenje.

Sada, kada imamo na raspolaganju ove dve funkcije, rešavanje polaznog zadatka je vrlo lako:

.. karel:: Karel_functions__displace_balls
    :blockly:

    {
        setup:function() {
            function random(n) {
                return Math.floor(n * Math.random());
        }
         
        var ww = [
            [
               '███████████',
               '█E.0.4.0.6█',
               '███████████'
            ],
            [
               '█████████████',
               '█E.1.3.0.4.0█',
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
                  world.setRobotStartDirection(c);
               }
               let d = w[wy].charCodeAt(wx);
               if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
            }
         }
         
            var robot = new Robot();
         
            var code = ["from karel import *",
                     "# umesto reci 'pass', kopirajte tela funkcija 'idi' i 'premesti'",
                     "",
                     "def idi(n):",
                     "    pass",
                     "",
                     "def premesti(br_loptica, br_polja):",
                     "    pass",
                     "",
                     "idi(2) # na polje 3",
                     "premesti(3, 1) # premesti 3 loptice jedno polje napred",
                     "idi(1) # na polje 5",
                     "premesti(4, -4) # premesti 4 loptice 4 polja nazad",
                     ""];
                     
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
            var X = world.getAvenues();
            if (X == 5) {var tagret_layout = [4,0,1,3,2]}
            if (X == 6) {var tagret_layout = [4,1,0,3,0,0]}
           
            for (let x = 1; x <= X; x++)
                if (world.getBalls(x, 1) != tagret_layout[x-1]) return false;
           
            if (robot.getBalls() > 0)
                return false;
                 
            return true;
        }
    }

Zadaci za vežbu
---------------

Uzmi zadati broj loptica
''''''''''''''''''''''''

.. questionnote::
    Napisati funkciju *uzmi_do(n)*, kojom Karel sa polja na kome se nalazi uzima najviše *n* loptica. Preciznije, ako je na polju *n* ili više loptica, Karel ih uzima *n*, a ako ima manje loptica, Karel uzima onoliko loptica koliko ih ima.
    
    Potrebno je da Karel, koji se nalazi na prvom polju, uzme sa drugog polja do 4 loptice, sa trećeg do 2, a sa četvrtog do 3 loptice, a zatim da sve prikupljene loptice donese na prvo polje. Naravno, za to treba koristiti funkciju *uzmi_do(n)*, napisanu u prvom delu zadatka.
    
.. karel:: Karel_functions__take_balls_up_to
    :blockly:

    {
        setup:function() {
            function random(n) {
                return Math.floor(n * Math.random());
        }
         
        var ww = [
            [
               '███████████',
               '█E.3.4.1.2█',
               '███████████'
            ],
            [
               '█████████',
               '█E.2.5.3█',
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
                  world.setRobotStartDirection(c);
               }
               let d = w[wy].charCodeAt(wx);
               if (d >= 48 && d < 58) world.putBalls(x, y, d - 48);
            }
         }
         
            var robot = new Robot();
         
            var code = ["from karel import *",
                     "def uzmi_do(n):",
                     "    pass # napisite funkciju",
                     "",
                     "napred(); uzmi_do(4)",
                     "# dovrsite uzimanje loptica",
                     "",
                     "levo(); levo() # vrati se",
                     "# dovrsite povratak i ostavljanje loptica",
                     ""];
                     
            // from karel import *
            // def uzmi_do(n):
            //     for i in range(n):
            //         if ima_loptica_na_polju():
            //             uzmi()
            // 
            // napred(); uzmi_do(4)
            // napred(); uzmi_do(2)
            // napred(); uzmi_do(3)
            //
            // levo(); levo()
            // napred();napred();napred()
            // while ima_loptica_kod_sebe():
            //     ostavi()
                     
            return {robot:robot, world:world, code:code};
        },
      
        isSuccess: function(robot, world) {
            var X = world.getAvenues();
            if (X == 5) {var tagret_layout = [6,0,2,0,2]} // = 0,3,4,1,2 - *,4,2,3
            if (X == 4) {var tagret_layout = [7,0,3,0]}   // = 0,2,5,3   - *,4,2,3
           
            for (let x = 1; x <= X; x++)
                if (world.getBalls(x, 1) != tagret_layout[x-1]) return false;
           
            if (robot.getBalls() > 0)
                return false;
                 
            return true;
        }
    }
    

Vožnja po uputstvima
''''''''''''''''''''

.. questionnote::
    Date su funkcije *na_raskrsnici_nalevo()* i *skreni_levo(n)*. 
    
    - Funkcija *na_raskrsnici_nalevo()* postavlja Karela da gleda u prvu ulicu sa leve strane na koju naiđe. Pri izvršavanju ove funkcije, Karel ide napred dok ne dođe do polja na kome može da ide levo, i ostaje na tom polju okrenut na levo. Ako pre poziva funkcije sa Karelove leve srane postoji polje, on se tokom rada ove funkcije neće ni pomerati sa svog polja, nego će se samo okrenuti na levo;
    - Funkcija *skreni_levo(n)* uvodi Karela jedno polje u *n*-tu ulicu sa leve strane. Ako je Karel već u raskrsnici, ulica levo od njega se broji kao prva;
    
    Napisati funkcije *na_raskrsnici_nadesno()* i *skreni_desno(n)* po ugledu na date. 
    
    Napisati program koji (pomoću datih i napisanih funkcija) vodi Karela u treću ulicu levo, zatim drugu desno, i na kraju drugu levo. Karel treba da dođe do kraja te ulice i da uzme jedinu lopticu na tabeli.

.. karel:: Karel_functions__travel_instructions_1
   :blockly:

   {
      setup:function() {
         function random(n) {
            return Math.floor(n * Math.random());
         }
         
         var ww = [
            [
               '█████████████',
               '█0.0.0█0█1█0█',
               '█████.█.█.█.█',
               '█0.0█0.0.0.0█',
               '███.█.███████',
               '█0█0█0.0.0.0█',
               '█.█.█.█████.█',
               '█E.0.0.0.0.0█',
               '█████████████'
            ],
            [
               '███████████████',
               '█0.0.0.0.0.0█1█',
               '███████.█████.█',
               '█0.0.0.0.0.0█0█',
               '███████.███.█.█',
               '█0.0█0.0.0.0.0█',
               '███.███.███████',
               '█0█0█0.0.0.0█0█',
               '█.█.███.█████.█',
               '█E.0.0.0.0.0.0█',
               '███████████████'
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
                     "def na_raskrsnici_nalevo():",
                     "    levo()",
                     "    while not moze_napred():",
                     "        desno()",
                     "        napred()",
                     "        levo()",
                     "    ",
                     "def skreni_levo(n):",
                     "    for i in range(n-1):",
                     "        na_raskrsnici_nalevo()",
                     "        desno()",
                     "        napred()",
                     "    na_raskrsnici_nalevo()",
                     "    napred()",
                     "",
                     "def na_raskrsnici_nadesno():",
                     "    # ...",
                     "    ",
                     "def skreni_desno(n):",
                     "    # ...",
                     "",
                     
                     "skreni_levo(3) # treca levo",
                     "# druga desno",
                     "# druga levo",
                     "# idi do kraja ulice",
                     "# uzmi lopticu",
                     ""];
                     
         //var code = ["from karel import *",
         //            "def na_raskrsnici_nalevo():",
         //            "    levo()",
         //            "    while not moze_napred():",
         //            "        desno()",
         //            "        napred()",
         //            "        levo()",
         //            "    ",
         //            "def skreni_levo(n):",
         //            "    for i in range(n-1):",
         //            "        na_raskrsnici_nalevo()",
         //            "        desno()",
         //            "        napred()",
         //            "    na_raskrsnici_nalevo()",
         //            "    napred()",
         //            "",
         //            "def na_raskrsnici_nadesno():",
         //            "    desno()",
         //            "    while not moze_napred():",
         //            "        levo()",
         //            "        napred()",
         //            "        desno()",
         //            "    ",
         //            "def skreni_desno(n):",
         //            "    for i in range(n-1):",
         //            "        na_raskrsnici_nadesno()",
         //            "        levo()",
         //            "        napred()",
         //            "    na_raskrsnici_nadesno()",
         //            "    napred()",
         //            "",
         //            
         //            "skreni_levo(3)",
         //            "skreni_desno(2)",
         //            "skreni_levo(2)",
         //            "while moze_napred():",
         //            "    napred()",
         //            "if ima_loptica_na_polju():",
         //            "    uzmi()",
         //            ""];
                     
         return {robot:robot, world:world, code:code};
      },
      
      isSuccess: function(robot, world) {
         return robot.getBalls() > 0;
      }
   }
