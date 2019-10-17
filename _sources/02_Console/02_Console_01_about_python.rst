Uvod u Pajton
=============

Pajton je veoma popularan programski jezik opšte namene. Postao je poznat po svojoj jednostavnosti, lakoći učenja i brzini programiranja. Mnogi profesionalni programeri koriste Pajton bar kao pomoćni jezik, jer pomoću njega brzo i lako automatizuju razne poslove. Zbog pomenutih dobrih osobina koristi ga i sve više ljudi drugih profesija koji se na svom poslu služe programiranjem u različitim oblastima. Programski jezik Pajton je besplatan za upotrebu, pa se oko njega formirala brojna zajednica koja doprinosi njegovom daljem razvoju i podršci na internetu.

Na primeru programskog jezika Pajton se jasno vidi da profesionalni programeri nisu jedini koji programiraju, kao što ni profesionalni pisci nisu jedini koji pišu. Sve je više poslova koje umereno poznavanje veštine programiranja može da učini nešto lakšim, uspešnijim ili produktivnijim. Zato i ovaj priručnik nije namenjen samo budućim profesionalcima u programiranju, već svima koji u svojim poslovima (i van njih) mogu imati koristi od programiranja.

Sada ćemo se upoznati sa osnovama rada u Pajtonu i videti kako se pišu naredbe i programi u ovom programskom jeziku.

Pajton interpreter
------------------

Za izvršavanje programa koje pišemo na Pajtonu, potreban nam je program koji se zove Pajton interpreter. Ovaj program tumači (interpretira), a zatim i izvršava Pajton naredbe. Pajton interpreteri mogu da prihvate cele programe i da ih izvrše, a mogu da rade i u **interaktivnom režimu**, u kome se svaka unesena naredba izvršava odmah.

Okruženje u kome se Pajton interpreter izvršava naziva se školjka (engl. shell). Postoje razne školjke u kojima odgovarajući Pajton interpreter može da se izvršava. Samim tim, imamo više načina da pokrenemo Pajton školjku.

**Školjka onlajn**

Veb strana https://www.python.org/shell sadrži jednu onljan školjku, koju možete da koristite odmah za interaktivan rad (dovoljno je da imate pristup internetu).

.. image:: ../../_images/Console/console_shell_online.png
   :width: 550px   
   :align: center 

**Instaliranje Pajtona i okruženje IDLE**

Za učenje programiranja na Pajtonu svakako je korisno da preuzmete Pajton sa adrese https://www.python.org/downloads/ i instalirate ga ako nije već instaliran na vašem računaru. Sa instalacijom Pajtona dobijate i program koji se zove *IDLE* (integrated development and learning environment - integrisano okruženje za razvoj i učenje). Ovo integrisano okruženje sadrži i školjku u kojoj možete da izvršavate Pajton programe. Kada pokrenete na vašem računaru program *IDLE*, dobijate sledeći prozor, u kome možete da radite interaktivno, ali i da pišete i izvršavate Pajton programe.

.. image:: ../../_images/Console/console_shell_idle.png
   :width: 550px   
   :align: center 

**Školjka u komandnom prozoru**

Još jedan način da pokrenete Pajton školjku je da otvorite komandni prozor (na *Windows* sistemima to se radi pokretanjem programa *cmd*), a zatim u komandnom prozoru otkucate *Python* (ovde podrazumevamo da je Pajton instaliran tako da je dostupan iz svakog foldera, u protivnom treba se prvo pozicionirati u folder u kome se nalazi Pajton interpreter).

.. image:: ../../_images/Console/console_shell_cmdwindow.png
   :width: 550px   
   :align: center 

U nastavku možete da odaberete školjku koju želite, u svakoj od njih se radi na isti način.

Interaktivan rad 
----------------

Pokrenite Pajton školjku. Znaci ``>>>`` koje vidite predstavljaju odzivnik (engl. prompt). Odzivnikom nam Pajton interpreter javlja da je spreman da primi komandu.

Kada radimo interaktivno, Pajton interpreter možemo da upotrebimo i kao kalkulator - otkucamo neki izraz i dobijamo njegovu vrednost:

.. code::

    >>> 3 + 2
    5
    >>> 3.25 + 2.25
    5.5
    >>> 3 - 2
    1
    >>> 4 * 2
    8
    >>> 4 / 2
    2.0
    
Za osnovne računske operacije u Pajtonu se (kao i u većini programskih jezika) koriste sledeći simboli: 

- sabiranje: ``+``
- oduzimanje: ``-``
- množenje: ``*``
- deljenje: ``/``

Osim ovih osnovnih i najčešće korišćenih, ponekad su nam potrebne još neke operacije, koje se koriste nešto ređe. To su:

- Celi deo količnika: ``//``, na primer vrednost izraza :math:`7 // 2` je :math:`3`.
- Ostatak pri deljenju celih brojeva: ``%``, na primer vrednost izraza :math:`7 \% 2` je :math:`1`.
- Stepenovanje: ``**``, na primer vrednost izraza :math:`2 ** 4` je :math:`2^4 = 16`.

.. code::

    >>> 7 // 2
    3
    >>> 7 % 2
    1
    >>> 2 ** 4
    16

Računari razlikuju cele i realne brojeve, različito ih zapisuju u svojoj memoriji i na različit način interno računaju sa njima. Tako u programiranju 2.0 nije sasvim isto što i 2, iako su vrednosti matematički jednake (znak ``==`` se koristi za poređenje dve vrednosti).

.. code::

    >>> 2.0 == 2
    True
    >>> type(2.0)
    <class 'float'>
    >>> type(2)
    <class 'int'>

Ovo što vidimo znači da je prvi broj realan, a drugi je ceo (reč *float* označava realne brojeve, a *int* cele).

U vezi sa time, primetimo da je u Pajtonu rezultat običnog deljenja ``/`` uvek realan broj, čak i kada se dele celi brojevi i nema ostatka. Kada nam je važno da rezultat deljenja celih brojeva bude ceo broj, treba da koristimo operaciju celobrojnog deljenja ``//``.

.. code::

    >>> 6/2
    3.0
    >>> 6//2
    3
    
.. commented out

    Koristeći ugrađene Pajtonove funkcije, realan broj možemo da pretvorimo u ceo, a ceo u realan.

    .. code::

        >>> float(3)
        3.0
        >>> int(3.0)
        3
        >>> int(6/2)
        3

Kod ostalih navedenih operacija rezulatat je ceo broj kada su oba operanda (brojevi na koje se primenjuje operacija) celi brojevi, a realan ako je bar jedan operand realan.

.. code::

    >>> 3 + 2
    5
    >>> 3.0 + 2
    5.0
    >>> 3 + 2.0
    5.0
    >>> 2.0 ** 4
    16.0


Pravila računanja vrednosti izraza su ista kao u matematici:

- Operacija stepenovanja se izvršava pre ostalih navedenih operacija. Ako ima više operacija stepenovanja u nizu, one se izvršavaju zdesna nalevo. 
- Operacije množenja, deljenja i ostatka se primenjuju pre sabiranja i oduzimanja. Kada ih ima više u nizu, izvršavaju se sleva nadesno.
- Kada nam je potreban drugačiji redosled računanja, koristimo zagrade (prvo se izračunava deo u zagradi).

.. code::

    >>> (5-3) * (2+2)
    8
    >>> 

Rad u Pajton školjci završvamo tako što otkucamo komandu ``quit()``.

.. code::

    >>> quit()

**Računanje - proverite razumevanje**

Proverite da li ste razumeli pravila računanja u Pajtonu tako što ćete odgovoriti na sledeća pitanja.

.. mchoice:: console__basics_expression_plustimes
   :answer_a: 15
   :answer_b: 30
   :answer_c: 50
   :answer_d: 125
   :correct: b
   :feedback_a: Znak + označava sabiranje, a znak * množenje.
   :feedback_b: Tačno!
   :feedback_c: Obratite pažnju i na prioritet operacija (isti je kao i u matematici).
   :feedback_d: Znak + označava sabiranje, a znak * množenje.
		
   Koja je vrednost izraza ``5 + 5 * 5``?

.. mchoice:: console__basics_expression_mode
   :answer_a: 3
   :answer_b: 0
   :answer_c: 5
   :answer_d: 6
   :correct: c
   :feedback_a: Pročitajte ponovo o računanju
   :feedback_b: Obratite pažnju i na prioritet operacija.
   :feedback_c: Tačno!
   :feedback_d: Znak % označava ostatak pri deljenju celih brojeva.
		
   Koja je vrednost izraza ``4 + 11 % 5``?

.. mchoice:: console__basics_expression_pow
   :answer_a: 60
   :answer_b: 100000000
   :answer_c: 1000000
   :answer_d: 300
   :correct: b
   :feedback_a: znaci ** predstavljaju stepenovanje
   :feedback_b: Tačno!
   :feedback_c: Operacije stepenovanja se izvršavaju sdesna nalevo, tako da je a**b**c isto što i a**(b**c).
   :feedback_d: Obe navedene operacije su operacije stepenovanja.
		
   Koja je vrednost izraza ``10 ** 2 ** 3``?

.. mchoice:: console__basics_expression_intdiv
   :answer_a: 1.666666
   :answer_b: 1
   :answer_c: 11.666666
   :answer_d: 12
   :correct: d
   :feedback_a: Pročitajte ponovo o označavanju i redosledu izvršavanja (prioritetu) operacija
   :feedback_b: Prvo se izvršava celobrojno deljenje
   :feedback_c: Oznaka // predstavlja celobrojno deljenje.
   :feedback_d: Tačno!
		
   Koja je vrednost izraza ``15 - 10 // 3``?

.. mchoice:: console__basics_expression_braces
   :answer_a: 5.0
   :answer_b: 5
   :answer_c: 1.0
   :answer_d: 1
   :correct: a
   :feedback_a: Tačno!
   :feedback_b: Rezultat ovog deljenja je uvek realan broj.
   :feedback_c: Prvo se izračunava deo u zagradi.
   :feedback_d: Prvo se izračunava deo u zagradi.
		
   Koja je vrednost izraza ``15 / (5 - 2)``?
