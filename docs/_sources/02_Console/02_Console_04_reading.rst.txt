Učitavanje podataka
===================

Učitavanje teksta
-----------------

Programi koje smo do sada naučili da pišemo sadrže sve potrebne podatke u sebi i rade uvek na isti način. Kada nam je potrebno da program radi istu stvar sa drugačijim podacima, morali bismo da izmenimo sam program. Ovaj način može da bude sasvim odgovarajući kada su izmene u podacima male i nisu česte.

Drugi način da postignemo da naš program rešava raznovrsnije zadatke je da omogućimo unošenje podataka. Unošenje podataka u program tokom njegovog rada se vrši pomoću funkcije *input()*. Ova funkcija radi tako što čeka da korisnik programa otkuca nešto (i pritisne taster *Enter*), a onda kao rezultat vraća otkucani tekst.

Kada pokrenete ovaj program, da biste videli kako on radi otkucajte nešto i pritisnite *Enter*. Isprobajte isti program i u okruženju *IDLE* ili na sajtu *repl.it*.

.. activecode:: console__text_input_first

    s = input()
    print("Napisali ste", s)

Program radi kako je opisano, ali ovakvo ponašanje programa može da bude i zbunjujuće. Kada bi neko pokrenuo ovakav program u okruženju *IDLE* ne znajući da program očekuje podatke, moglo bi da mu izgleda kao da se računar blokirao jer se ništa ne dešava, a u stvari program samo čeka na ulaz sa tastature.

Da bismo pomogli korisniku da razume šta se od njega očekuje, možemo da koristimo i oblik funkcije *input* sa jednim tekstualnim argumentom, koji će biti ispisan kao uputstvo korisniku. Na primer:

.. activecode:: console__text_input_prompt

    s = input("Napišite nešto: ")
    print("Napisali ste", s)

Izbor oblika funkcije *input* koji ćemo koristiti zavisi od namene programa. Kada pišemo program u koji će podatke da unose drugi ljudi, koristimo oblik sa argumentom - uputstvom. Kada pišemo program samo sa svoju kratkoročnu (možda čak jednokratnu) upotrebu, tada nemamo potrebe za uputstvima i možemo da koristimo i oblik bez argumenata.

Pomenimo i to da u nekim od okruženja u kojima se program izvršava možemo da podesimo da program umesto sa tastature, učitava podatke sa nekog drugog mesta na kome smo te podatke unapred pripremili. Tada nema čekanja da podaci budu uneti, oni se učitavaju automatski i nema potrebe da se nekome ispisuje uputstvo (ono čak može i da smeta). Zato se u programima predviđenim za ovakvu upotrebu takođe koristi *input* naredba bez argumenata.


Učitavanje brojeva
------------------

Videli smo da funkcija *input()* vraća string (otkucani tekst). To znači da ukoliko nam je potreban podatak drugog tipa, treba da promenimo tip unetog podatka iz stringa u željeni tip. Promena tipa podatka se zove još i **konverzija**. Na primer ako želimo ceo broj, onda dobijeni tekst treba da pretvorimo (konvertujemo) u ceo broj. Evo kako se to radi u Pajtonu:
    
.. activecode:: console__text_input_int1

    s = input("Unesite ceo broj: ")
    n = int(s)
    print(n+n)

Funkcija ``int()`` tekstualnu vrednost pretvara u brojčanu (celobrojnu). Tako, naredbom ``n = int(s)`` u promenljivu *n* smeštamo celobrojnu vrednost i zato znak + u programu označava sabiranje celih brojeva. Sabiranje je dodato u program kao dokaz da je *n* zaista celobrojna vrednost (po rezultatu vidimo da se vrednosti sabiraju kao brojevi).

Pošto funkcija *input* vraća string, rezultat njenog rada možemo i direktno da prosledimo funkciji *int*. Tako izbegavamo upotrebu promenljive *s* i dobijamo nešto kraći program koji radi istu stvar:

.. activecode:: console__text_input_int2

    n = int(input("Unesite ceo broj: "))
    print(n+n)

~~~~

Za realan broj samo umesto *int* treba pisati *float*, jer Funkcija ``float()`` tekstualnu vrednost pretvara u realan broj. Na primer, ako želimo da učitamo realan broj i ispišemo dvostruko veći broj, program može da izgleda ovako:

.. activecode:: console__text_input_float1

    s = input("Unesite realan broj: ")
    a = float(s)
    print(2*a)

ili

.. activecode:: console__text_input_float2

    a = float(input("Unesite realan broj: "))
    print(2*a)


Proverite šta se dešava u ova dva primera kada se ne unese broj nego tekst.

O konverzijama
--------------

Videli smo da kada se u stringu nalazi zapis celog ili realnog broja, taj string se može konvertovati u celobrojni, odnosno realni tip pomoću funkcija *int()*, odnosno *float()*. Obrnuto, celi i realni brojevi uvek mogu da se konvertuju u string. Za konverziju u string se koristi funkcija *str()*.

.. activecode:: console__text_convert_to_str

    a = 1
    a_str = str(a)
    print(a_str + a_str)

    b = 2.1
    b_str = str(b)
    print(b_str + b_str)

Konverzija celobrojne vrednosti u realnu se vrši automatski kada je to potrebno, mada je dozvoljeno i da to uradimo i pozivom funkcije *float*. 

.. activecode:: console__text_convert_int_to_float

    print(float(1))
    
Obrnuto, kada nam zatreba da konvertujemo realan broj u ceo, ta konverzija se ne dešava automatski (s razlogom) i nju treba da zadamo u programu pozivom funkcije *int()*. Prilikom konverzije realnog broja u ceo broj odbacuju se eventualne decimale realnog broja, što znači da je zaokruživanje uvek **ka nuli**. Drugim rečima, kada vrednost realnog broja *x* nije cela, *int(x)* je bliži nuli nego *x*.

.. activecode:: console__text_convert_int_float

    print(float(1))
    
    print(int(1.68))
    print(int(-1.68))
    
Pitanja
-------

.. mchoice:: console__text_quiz_1
    :answer_a: Program će ispisati 5
    :answer_b: Program će ispisati 23
    :answer_c: Doći će do greške zbog pokušaja sabiranja stringa i broja
    :correct: c
    :feedback_a: Pokušajte ponovo
    :feedback_b: Pokušajte ponovo
    :feedback_c: Tačno
    
    Šta će se dogoditi kada pokrenemo sledeći program i unesemo vrednost ``2`` ?
    
    .. code::
    
        a = input()
        print(a+3)

.. mchoice:: console__text_quiz_2
    :answer_a: Program će ispisati 5
    :answer_b: Program će ispisati 23
    :answer_c: Doći će do greške zbog pokušaja sabiranja stringa i broja
    :correct: b
    :feedback_a: Pokušajte ponovo
    :feedback_b: Tačno
    :feedback_c: Pokušajte ponovo
    
    Šta će se dogoditi kada pokrenemo sledeći program i unesemo vrednost ``2`` ?
    
    .. code::
    
        a = input()
        print(a+'3')

.. dragndrop:: console__text_quiz_4
    :feedback: Pokušajte ponovo!
    :match_1: '2.11'|||str(2.1) + '1'
    :match_2: 3.1|||float('2.1') + 1
    :match_3: greška pri računanju|||float('2.1') + '1'
    :match_4: 2.11|||float('2.1') + 1/100
    :match_5: '3.1'|||str(2.1 + int('1'))

    Uparite izraze sa rezultatima izračunavanja.


.. mchoice:: console__text_quiz_5
   :answer_a: Kada je prva decimala broja a veća ili jednaka 5
   :answer_b: Kada je broj a negativan
   :answer_c: Kada je broj a pozitivan
   :answer_d: Kada je broj a jednocifren
   :answer_e: Kada je razlika između a i int(a) veća od 0.5
   :correct: b
   :feedback_a: Pokušajte ponovo.
   :feedback_b: Tačno!
   :feedback_c: Pokušajte ponovo.
   :feedback_d: Pokušajte ponovo.
   :feedback_e: Pokušajte ponovo.

   Kada je ceo broj *int(a)* veći od realnog broja a?

