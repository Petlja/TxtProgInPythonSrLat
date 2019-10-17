Matematičke funkcije
====================

U programiranju stalno koristimo funkcije. Na primer, *print()*, *input()*, *int()*, *float()* i *str()* su funkcije jezika Pajton, koje smo do sada već koristili. U pajtonu postoje i mnoge druge funkcije, a među njima i veliki broj onih koje se koriste u matematici. Neke od jednostavnijih matematičkih funkcija ćemo videti u nastavku.

Funkcije *abs()*, *min()* i *max()*
-----------------------------------

Funkcije *abs()*, *min()* i *max()* se često koriste u računskim zadacima. Verovatno ste ih negde već koristili, pa ćemo ih objasniti samo ukratko:

- funkcija *abs()* vraća apsolutnu vrednost brojčanog izraza koji joj se prosledi kao argument (apsolutna vrednost broja se dobija kada se odbaci znak broja, videti primer ispod);
- funkcija *min()* može imati dva ili više brojčanih argumenata, a vraća vrednost najmanjeg od njih;
- funkcija *max()* može imati dva ili više brojčanih argumenata, a vraća vrednost najvećeg od njih;

Evo kako izgleda upotreba ovih funkcija u programu:

.. activecode:: console__numberfunc_absminmax_example

    print("abs(3) =", abs(3))
    print("abs(-7) =", abs(-7))
    print("abs(-5 - -2) =", abs(-5 - -2))
    print("min(5, 2, 7, 3) =", min(5, 2, 7, 3))
    print("max(5, 2, 7, 3) =", max(5, 2, 7, 3))

Funkcije *abs()*, *min()* i *max()* - pitanja
---------------------------------------------

Proverite razumevanje gore pomenutih funkcija:

.. mchoice:: console__numberfunc_min
   :answer_a: 10
   :answer_b: 20
   :answer_c: 30
   :correct: a
   :feedback_a: Tačno!
   :feedback_b: Funkcija min vraća najmanju od vrednosti koje joj se proslede kao argumenti.
   :feedback_c: Funkcija min vraća najmanju od vrednosti koje joj se proslede kao argumenti.
		
   Koja je vrednost izraza ``min(10, 20, 30)``?

.. mchoice:: console__numberfunc_max
   :answer_a: 10
   :answer_b: 20
   :answer_c: 30
   :correct: c
   :feedback_a: Funkcija max vraća najveću od vrednosti koje joj se proslede kao argumenti.
   :feedback_b: Funkcija max vraća najveću od vrednosti koje joj se proslede kao argumenti.
   :feedback_c: Tačno!
		
   Koja je vrednost izraza ``max(10, 20, 30)``?

.. dragndrop:: console__numberfunc_max_0x100
    :feedback: Pokušajte ponovo!
    :match_1: vrednost izraza je 0 ||| ako je x manje od nule
    :match_2: vrednost izraza je x ||| ako je x između 0 i 100
    :match_3: vrednost izraza je 100 ||| ako je x veće od 100
    
    Uparite vrednosti izraza ``min(100, max(0, x))`` sa uslovima za x.

.. dragndrop:: console__numberfunc_max_0x
    :feedback: Pokušajte ponovo!
    :match_1: abs(x)||| x ako je x pozitivno, a suprotan broj inače
    :match_2: max(0, x)||| x ako je x pozitivno, a nula inače
    :match_3: min(0, x)||| x ako je x negativno, a nula inače
    :match_4: min(0, abs(x))||| uvek nula
		
    Uparite izraze sa njihovim vrednostima.

Funkcije za zaokruživanje vrednosti
-----------------------------------

Zaokruživanje realne vrednosti na ceo broj je operacija koja nam je takođe često potrebna. Već smo videli da konverzijom realnog broja u ceo vršimo zaokruživanje ka nuli. Postoji još nekoliko funkcija pomoću kojih u Pajtonu možemo da zakoružimo realan broj na razlikite načine:

- funkcija *round()* vraća ceo broj najbliži vrednosti argumenta (reztultat je celobrojnog tipa);
- funkcija *floor()* vraća najbliži ceo broj, manji ili jednak vrednosti argumenta (reztultat je realnog tipa);
- funkcija *ceil()* vraća najbliži ceo broj, veći ili jednak vrednosti argumenta (reztultat je realnog tipa);

Pokrenite sledeći program da biste videli kako rade ove funkcije i da biste ih uporedili.

.. activecode:: console__numberfunc_rounding_example

    import math
    
    print("round(56.234) =", round(56.234))
    print("round(56.789) =", round(56.789))

    print("math.floor(56.234) =", math.floor(56.234))
    print("math.floor(56.789) =", math.floor(56.789))

    print("math.ceil(56.234) =", math.ceil(56.234))
    print("math.ceil(56.789) =", math.ceil(56.789))


Primećujemo da su funkcije *floor* i *ceil* po nečemu različite od funkcije *round* i svih prethodnih funkcija - ispred njihovog imena u programu piše ``math.``. To je zato što su ove funkcije definisane u modulu koji se zove *math*. Moduli su programske celine koje sadrže razne funkcije, konstante i druge delove koda koje možemo da koristimo u našim programima. Tako i modul *math* pored funkcija *floor* i *ceil* sadrži i mnoge druge funkcije. Na primer, poznata konstanta pi se može koristiti kao *math.pi*, a funkcija kvadratni koren kao *math.sqrt* (ovde ih nećemo koristiti).

Da bismo mogli da koristimo funkcije modula *math*, potrebno je da ovaj modul priključimo našem programu. To smo uradili pišući ``import math`` na početku programa. Time smo naravno omogućili korišćenje i svih drugih matematičkih funkcija i svega drugog što je definisano u ovom modulu.

Za fukciju *round* i sve prethodne funkcije nije potrebno priključivati nikakav poseban modul, jer su te funkcije ugrađene u sam jezik Pajton, tako da su nam uvek direktno na raspolaganju.

Funkcije za zaokruživanje vrednosti - pitanja
---------------------------------------------

Proverite razumevanje funkcija objašnjenih u ovoj lekciji:

.. mchoice:: console__numberfunc_abs_round
   :answer_a: -2
   :answer_b: 2
   :answer_c: -3
   :answer_d: 3
   :correct: d
   :feedback_a: Pročitajte ponovo objašnjenja funkcija abs i round.
   :feedback_b: Funkcija round vraća najbliži ceo broj.
   :feedback_c: Funkcija abs vraća apsolutnu vrednost broja, koja je uvek veća ili jednaka nuli.
   :feedback_d: Tačno!
		
   Koja je vrednost izraza ``abs(round(-2.7))``?
   
.. mchoice:: console__numberfunc_max_abs
   :answer_a: max(x, round(x))
   :answer_b: max(x)
   :answer_c: round(x)
   :answer_d: abs(x)
   :correct: a
   :feedback_a: Tačno!
   :feedback_b: Funkcija max treba da ima bar dva argumenta.
   :feedback_c: Na ovaj način iznos može i da se smanji.
   :feedback_d: Iznos je već pozitivan, funkcijom abs se ovde ništa ne postiže.
		
   Jedan kasir zaokružuje račun na najbliži ceo broj samo ako se time iznos povećava, u protivnom prijavljuje iznos kakav jeste. Koju formulu primenjuje taj kasir (x je polazna vrednost računa)?

.. dragndrop:: console__numberfunc_rounding
    :feedback: Pokušajte ponovo!
    :match_1: ka nuli|||int()
    :match_2: ka bližem celom broju|||round()
    :match_3: ka manjem celom broju|||floor()
    :match_4: ka većem celom broju|||ceil()

    Uparite funkcije za zaokruživanje sa načinom zaokruživanja.

.. questionnote::

    **Zadatak za radoznale** - funkcija *round*
    
    Funkcija *round* može da se pozove i sa dva argumenta (mi je inače nećemo tako koristiti), gde je drugi argument obično mali ceo broj. Proverite na primer koliko je :math:`round(123.23456, 2)`, :math:`round(123.23456, 3)` i :math:`round(123.23456, -1)`. Možete da koristite prostor ispod za pomoćni program.
    
    Pokušajte da objasnite čemu služi drugi argument funkcije *round*, kada se funkcija pozove sa dva argumenta.
    
.. activecode:: console__givenfunc_round


