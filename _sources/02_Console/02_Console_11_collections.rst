Kolekcije podataka
==================

U prethodnoj lekciji smo upotrebili torku vrednosti da bismo pomoću *for* petlje obavili neke naredbe (računanje i ispisivanje) nad svakom vrednošću iz torke. 

Torke su takođe tip podataka u Pajtonu, kao što su to brojevi, stringovi ili logičke vrednosti. Tipovi *int* (ceo broj), *float* (realan broj), *str* (string) i *bool* (logička vrednost) su **osnovni tipovi**. Razlika između torki i osnovnih tipova je u tome što se vrednost torke sastoji od više vrednosti jednostavnijeg tipa.

Svaku vrednost koja se sastoji od više vrednosti jednostavnijeg tipa zvaćemo **kolekcija**. Podatke od kojih se kolekcija sastoji zovemo **elementi kolekcije**. 

Jedine kolekcije koje smo do sada upozali su torke, koje ćemo sada upoznati detaljnije. U nastavku lekcije ćemo videti još neke vrste kolekcija.

Torka i njeni elementi
----------------------

Pakovanje i raspakivanje torki
''''''''''''''''''''''''''''''

Celu torku možemo da smestimo u promenljivu, kao što to radimo i sa vrednostima prostijeg tipa. U sledećem primeru, promenljiva *temperature* sadrži celu torku kao svoju vrednost.

.. activecode:: console__collections_tuple1
    
    temperature = (25, 24, 25, 23, 25, 25)
    for t in temperature:
        print(t)
        
Ovakvo dodeljivanje vrednosti (kao u prvoj liniji programa) zovemo i pakovanje torke. Moguća je i obrnuta dodela: kada znamo koliko torka ima elemenata, možemo da elemente torke dodelimo odgovarajućem broju promenljivih:

.. activecode:: console__collections_tuple2
    
    puno_ime = ("Milan", "Jovanović", "Batut")
    ime, prezime, nadimak = puno_ime
    print(ime)
    print(prezime)
    print(nadimak)
    
Kažemo da se u naredbi ``ime, prezime, nadimak = puno_ime`` vrši raspakivanje torke.

Isti efekat ima i srodna naredba 

.. code::
    
    ime, prezime, nadimak = "Milan", "Jovanović", "Batut"
    
U ovoj naredbi se torke i ne pojavljauju, pa ovde govorimo o višestrukom dodeljivnju vrednosti.

Elementi i indeksi torke
''''''''''''''''''''''''

Elemente torke možemo da dobijemo i tako što napišemo ime torke, a iza njega u uglastim zagradama redni broj elementa koji želimo. Ovde treba zapamtiti da brojanje elemenata bilo koje kolekcije počinje od nule. Na primer:

.. activecode:: console__collections_index

    osnovne_boje = ("Crvena", "Zelena", "Plava")
    print(osnovne_boje[0])
    print(osnovne_boje[1])
    print(osnovne_boje[2])

Redni broj elementa se još naziva i **indeks** elementa. Za torku od *n* elemenata kao indekse možemo da koristimo brojeve 0, 1, 2, ... *n-1*. U primeru gore je *n* = 3, pa su dozvoljeni indeksi 0, 1 i 2. Pokušaj da upotrebimo neki indeks van ovih granica prouzrokuje grešku (možete da isprobate ovo).


Dužina torke
''''''''''''

Broj elemenata torke možemo da dobijemo pomoću funkcije *len*. 

.. activecode:: console__collections_len1
    
    osnovne_boje = ["Crvena", "Zelena", "Plava"]
    n = len(osnovne_boje)
    print(n)
    
ili kraće:

.. activecode:: console__collections_len2
    
    print(len(("Crvena", "Zelena", "Plava")))
    
Obratite pažnju na dvostruke zagrade (jedne zbog funkcije, a druge zbog torke).

Kroz ove primere smo videli da elementi torke mogu da budu brojevi ili stringovi. U stvari, elementi torke mogu biti bilo kojeg tipa, osnovnog ili složenijeg.

Dozvoljeno je na primer praviti torku torki: 


.. activecode:: console__collections_len3
    
    t = ((11, 12, 13), (21, 22, 23))
    print(len(t))


.. commented out

    t2 = ((1, 2, 3), ) # poslednji zarez je bitan
    print(len(t2))
    
Torka *t* sadrži dve jednostavnije torke, zato je broj njenih elemenata 2.

U Pajtonu je dozvoljeno da elementi torke budu različitog tipa i kasnije ćemo videti i takve primere.

Opseg
-----

Opseg (engl. range) je još jedna vrsta kolekcije. Za razliku od torke, elementi ove kolekcije su uvek celi brojevi. 

Opseg može da se zada na više načina.

Opseg sa jednim argumentom
''''''''''''''''''''''''''

Najjednostavniji oblik zadavanja opsega je *range(n)*, gde je *n* neki ceo pozitivan broj. Opseg *range(n)* sadrži celobrojne vrednosti od 0 do *n*, ne uključujući *n*. Na primer, *range(5)* sadrži vrednosti 0, 1, 2, 3, 4. 

.. activecode:: console__collections_range_n_i
    
    for i in range(5):
        print(i)
        
Vidimo da u *for* naredbi možemo da koristimo opseg na isti način kao i torku. U stvari, na mestu torke ili opsega može da stoji bilo koja kolekcija.

Pošto opseg *range(n)* sadrži ukupno *n* vrednosti, ovako zadat opseg se često koristi kada neku naredbu treba samo ponoviti *n* puta na isti način:

.. activecode:: console__collections_range_n
    
    for i in range(5):
        print("Zdravo!")

Naredba *print* je izvršena za svaku vrednost *i* iz sekvence 0, 1, 2, 3, 4, ali u ovom primeru se te vrednosti ne koriste u telu petlje. Tako smo postigli da se naredba *print* izvrši 5 puta na potpuno isti način, to jest da se ponovi 5 puta. 

Druga česta upotreba ovakvog opsega je da pomoću njega prođemo kroz sve elemente torke. Ovakav način prolaženja kroz vrednosti torke je pogodan kada nam osim tih vrednosti u petlji trebaju i njihovi redni brojevi (ovakav način prolaženja kroz kolekciju je češći u drugim programskim jezicima nego u Pajtonu).

.. activecode:: console__collections_for_range_len
    
    boje = ["Crvena", "Zelena", "Plava", "Žuta", "Ciklama"]
    n = len(boje)
    for i in range(n):
        print('Boja br.', i, 'je', boje[i])




Opseg sa dva argumenta
''''''''''''''''''''''

Kada nam je potrebna sekvenca uzastopnih celih brojeva koja ne počinje nulom, opseg zadajemo kao *range(a, b)*, gde su *a* i *b* celi brojevi, takvi da je :math:`a<b`. Tada sekvencu čine celi brojevi od *a* do *b*, ne uključujući *b*. Na primer, opseg *range(1, 6)* daje sekvencu brojeva 1, 2, 3, 4, 5:

.. activecode:: console__collections_range_a_b
    
    for i in range(1, 6):
        print(i)

Opseg sa tri argumenta
''''''''''''''''''''''

Treći oblik zadavanja opsega ima tri argumenta:

.. activecode:: console__collections_range_a_b_c
    
    for i in range(2, 12, 2):
        print(i)

Vrednosti opsega zadatog sa *range(a, b, c)* idu od *a* do *b* (ne uključujući *b*) sa korakom *c*, tj. menjajući se za po *c*. Korak *c* može da bude i negativan:

.. activecode:: console__collections_range_a_b_cneg
    
    for i in range(12, 2, -2):
        print(i)


Opseg možemo da konvertujemo u torku (obrnuto nije moguće, niti je potrebno):

.. activecode:: console__collections_range_to_tuple
    
    a = tuple(range(2, 12, 2))
    print(len(a))


String kao kolekcija
--------------------

Stringove smo do sada koristili kao osnovni tip, ali stringovi mogu da se koriste i kao kolekcije pojedinačnih karaktera. Možemo da prolazimo kroz karaktere stringa pomoću petlje i da dohvatamo pojedine karatere koristeći indekse:

.. activecode:: console__collections_str_as_collection
    
    s = 'tekst'
    print(s[1], s[2])
    for c in s:
        print(c)



Funkcije nad kolekcijama
------------------------

U Pajtonu postoje mnoge funkcije koje kao argument prihvataju kolekciju. Jedna od njih je funkcija *len*, koju smo već upoznali. Još neke često korišćene funkcije koje se primenjuju nad kolekcijama su:

- *min*, koja daje najmanji element kolekcije
- *max*, koja daje najveći element kolekcije
- *sum*, koja daje zbir elemenata kolekcije

.. activecode:: console__collections_aggregation
    
    print('Torka:')
    t = (2, 8, 4, 15, 3)
    print('len(t) =', len(t))
    print('min(t) =', min(t))
    print('max(t) =', max(t))
    print('sum(t) =', sum(t))

    print('Opseg:')
    r = range(1, 10, 2)
    print('len(r) =', len(r))
    print('min(r) =', min(r))
    print('max(r) =', max(r))
    print('sum(r) =', sum(r))

    print('String:')
    s = 'Python'
    print('len(s) =', len(s))
    print('min(s) =', min(s))
    print('max(s) =', max(s))
    # elementi kolekcije s nisu brojevi, pa bi izvrsavanje sledece naredbe izazvalo gresku
    # print('sum(s) =', sum(s))

Vrednosti funkcija *len*, *min*, *max*, *sum* za opseg možemo da odredimo i iz parametara opsega. Takođe, funkcije *min* i *max* se obično ne primenjuju na stringove (one vraćaju redom karakter sa najmanjim i najvećim kodom). Ovde samo ističemo da sve pomenute funkcije prihvataju razne vrste kolekcija kao svoj argument (uključujući i opseg i string).

Pitanja
'''''''

.. mchoice:: console__collections_quiz_tuple_unpack
   :answer_a: dolazi do greške u programu
   :answer_b: 2
   :answer_c: 20
   :answer_d: 3
   :correct: c
   :feedback_a: Pokušajte ponovo
   :feedback_b: Pokušajte ponovo
   :feedback_c: Tačno
   :feedback_d: Pokušajte ponovo

   Šta ispisuje sledeći program?
   
   .. code::
   
       t = (32, 41, 20, 17)
       a, b, c, d = t
       print(c)

.. mchoice:: console__collections_quiz_tuple_index
   :answer_a: 1
   :answer_b: 2
   :answer_c: dolazi do greške u programu
   :answer_d: 3
   :correct: b
   :feedback_a: Pokušajte ponovo
   :feedback_b: Tačno
   :feedback_c: Pokušajte ponovo
   :feedback_d: Pokušajte ponovo

   Šta ispisuje sledeći program?
   
   .. code::
   
       a = (1, 2, 3)
       print(a[1])


.. mchoice:: console__collections_quiz_range1
   :answer_a: range(4)
   :answer_b: range(1, 4)
   :answer_c: range(3)
   :answer_d: range(1, 3)
   :correct: b
   :feedback_a: Pokušajte ponovo
   :feedback_b: Tačno
   :feedback_c: Pokušajte ponovo
   :feedback_d: Pokušajte ponovo

   Koji opseg sadrži samo vrednosti 1, 2, 3 ?

.. mchoice:: console__collections_quiz_range2
   :answer_a: 5
   :answer_b: 6
   :answer_c: 9
   :answer_d: 10
   :correct: a
   :feedback_a: Tačno
   :feedback_b: Pokušajte ponovo
   :feedback_c: Pokušajte ponovo
   :feedback_d: Pokušajte ponovo

   Koliko vrednosti sadrži opseg range(1, 10, 2) ?

.. dragndrop:: console__collections_quiz_range_len
    :feedback: Pokušajte ponovo!
    :match_1: 5|||range(5)
    :match_2: 0|||range(3, 3)
    :match_3: 3|||range(1, 4)
    :match_4: 1|||range(3, 6, 3)

    Uparite opsege sa brojem elemenata.


.. dragndrop:: console__collections_quiz_range_values
    :feedback: Pokušajte ponovo!
    :match_1: 3, 4, 5|||range(3, 6)
    :match_2: 0, 1, 2|||range(3)
    :match_3: 3, 1|||range(3, -1, -2)
    :match_4: 3, 2, 1, 0, -1|||range(3, -2, -1)
    :match_5: 3|||range(3, 6, 3)

    Uparite opsege sa vrednostima.
