Tekstualne vrednosti
====================

Pored celih i realnih brojeva, jedan od osnovnih tipova podataka u programiranju je tekst. Tekstualni podaci se nazivaju **niske** ili **stringovi**. U njima pored slova mogu da se nađu i svi ostali znaci koji se koriste u tekstu: interpukcija, zagrade, cifre, znaci matematičkih operacija, razni specijalni znaci poput ``%``, ``$``, ``^``, ``&`` itd. Svi ovi znaci koji mogu da se pojave u tekstu nazivaju se **karakteri**.

Tekstualne vrednosti se pišu između navodnika. Tekst pod navodnicima zovemo **tekstualna konstanta** ili **literal**. U pajtonu mogu ravnopravno da se koriste jednostruki ``'...'`` i dvostruki ``"..."`` navodnici (važno je samo da su na početku i na kraju stringa navodnici iste vrste). Na primer:

.. code::

    s1 = 'Jedan tekst'
    s2 = "Drugi tekst"

U daljem tekstu reč string ćemo koristiti za tekstualni tip podataka, kao i za svaki izraz čija je vrednost tog tipa. Najvažniji primeri izraza tipa string su tekstualne konstante (literali) i promenljive koje sadrže tekst.

Ispisivanje teksta 
------------------

Stringovi se prikazuju na ekranu na isti način kao i brojčani podaci. String koji želimo da ispišemo jednostavno navodimo kao argument funkcije *print()*.

.. activecode:: console__text_hello

    print("Zdravo svete!")

Kada funkcija *print()* ima više argumenata, ti agrumenti mogu da budu različitog tipa:

.. activecode:: console__text_compute

    print('2+2 =', 2+2)

Kada navodimo više argumenata, pišemo ih razdvojene zarezima (kao kod svake funkcije). Vrednosti svih navedenih argumenata će biti prikazane jedna za drugom, i biće razdvojene po jednim razmakom.

Još o ispisivanju brojeva
-------------------------

Ponekad ispisani rezultat izgleda nepregledno:

.. activecode:: console__text_format1a

    print(5/3)

Najčešće nam nije važno da vidimo sve ove decimale. Pregledniji prikaz realnih vrednosti možemo da dobijemo koristeći funkciju *format*. Pomoću ove funkcije možemo na primer da zadamo koliko decimala želimo da bude prikazano:

.. activecode:: console__text_format1b

    x = 5/3
    s = format(x, '.2f')
    print(s)
    
Da bismo zadali broj decimala koje ćemo da prikažemo, funkciju *format* smo pozvali ovako: prvi agrument funkcije je vrednost koju ispisujemo, a drugi argument je opis prikaza. U ovom opisu deo '.2' znači da želimo dva decimalna mesta, a deo 'f', skraćeno od *float*, znači da dajemo opis za prikazivanje realanog broja (tip realnih brojeva se zove *float*). Funkcija vraća string u kome je broj *x* zapisan na traženi način.

Istaknimo da ovo podešavanje prikaza ne utiče na vrednost promenljive *x*, koja i dalje ima sve svoje decimale.

Primer smo razložili na korake da bi bio jasniji, mada je mogao da bude napisan i u jednoj liniji koda, na primer za ispis sa 4 decimale:

.. activecode:: console__text_format1c

    print(format(5/3, '.4f'))
    
~~~~

Kada prikazujemo više realnih brojeva jedan ispod drugog, da bi prikaz bio pregledniji poželjno je da decimalne tačke budu poravnate. Na primer, ovakav prikaz nije naročito pregledan:

.. activecode:: console__text_format2a

    print(-1.23)
    print(7251.7)
    print(84.15)
   
Da bismo dobili pregledniji prikaz, možemo funkciju *format* da upotrebimo ovako:

.. activecode:: console__text_format2b

    print(format(-1.23, '8.2f'))
    print(format(7251.7, '8.2f'))
    print(format(84.15, '8.2f'))

U opisu '8.2f' broj 8 znači da želimo da prikaz broja zauzme ukupno 8 mesta. U tih 8 mesta se broje cifre, decimalna tačka, eventualni znak broja i razmaci ispred broja. Delovi opisa '.2' i 'f' imaju isto značenje kao i ranije.

Funkcija *format* ima i mnoge druge mogućnosti, od kojih ćemo još neke upoznati usput.




Operacije sa stringovima
------------------------

Nadovezivanje stringova
'''''''''''''''''''''''

Stringovi se mogu nadovezivati jedan na drugi operacijom nadovezivanja stringova, koja poznata i pod imenom **konkatenacija stringova**. Ova operacija se označava znakom ``+``, isto kao i operacija sabiranja brojeva, pa se u programiranju ona često neformalno naziva i sabiranje stringova.

.. activecode:: console__text_concat1

    s = 'nast' + 'avak'
    print(s)

Povremeno se dešava da u stringu imamo zapis celog ili realnog broja, pa je važno je da razumemo kada se u programima znak ``+`` odnosi na sabiranje brojeva, a kada na nadovezivanje stringova. Na primer, u sledećem programu prvo *a + b* je sabiranje brojeva, a drugo je sabiranje (nadovezivanje) stringova. U skladu sa time se razlikuju i ispisani rezultati (isprobajte).

.. activecode:: console__text_concat2

    a = 14.2
    b = 1
    print(a + b)
    
    a = '14.2'
    b = '1'
    print(a + b)

Verovatno će se povremeno događati da kasnije pri izvršavanju nekog svog prorgama budete zbunjeni rezultatom. Rezultat može da bude različit od očekivanog iz mnogo razloga, a jedna mogućnost je i da ste slučajno sabirali stringove umesto brojeva.

Znak ``+`` može da stoji između dva brojčana izraza ili između dva stringa, ali ne i između stringa i broja. Ovakve kombinacije dovode do greške tipa (*TypeError*), bilo da se sabira broj sa stringom, ili string sa brojem (isprobajte).

.. activecode:: console__text_concat3

    print('2' + 2)

Umnožavanje stringova
'''''''''''''''''''''

Stringovi se mogu i umnožavati (multiplicirati). To znači da je dozvoljeno pomnožiti string celim brojem (bilo sleva ili sdesna), a rezultat je novi string, koji se dobija ponavljanjem datog stringa zadati broj puta.

U sledećem primeru, crta kojom podvlačimo sabirke je dobijena množenjem stringa '-' sa 12.

.. activecode:: console__text_str_mult

    a = 1.23958
    b = 5467251.707256
    c = 384.150576
    zbir = a + b + c
    print(format(a, '12.2f'))
    print(format(b, '12.2f'))
    print(format(c, '12.2f'))
    print(12 * '-')
    print(format(zbir, '12.2f'))

    
Pitanja i zadaci
----------------

.. dragndrop:: console__text_quiz_format
    :feedback: Pokušajte ponovo!
    :match_1: '12.34'|||format(12.34, '.2f')
    :match_2: '__12.34'|||format(12.34, '7.2f')
    :match_3: '_12.34'|||format(12.34, '6.2f')
    :match_4: '__12.3'|||format(12.34, '6.1f')
    :match_5: '12.3'|||format(12.34, '.1f')

    Uparite pozive funkcije *format* sa rezultatima. Razmaci su predstavljeni znakom '_' pošto inače ne bi bili vidljivi.

.. mchoice:: console__text_quiz_quotes
    :answer_a: s = 'a' + "b"
    :answer_b: s = 'ab"
    :answer_c: s = 'ab'
    :correct: b
    :feedback_a: Pokušajte ponovo
    :feedback_b: Tačno
    :feedback_c: Pokušajte ponovo
    
    Koja od naredbi je neispravna?

.. mchoice:: console__text_quiz_tralala
   :multiple_answers:
   :answer_a: print('tra' + 2 * '-la')
   :answer_b: print('tra-' + 2 * 'la-')
   :answer_c: print('tra-' + 'la-' + 'la')
   :answer_d: print('tra-' + 'la-la')
   :answer_e: print('tra-la-' + '-la')
   :correct: a, c, d

   Koja naredba ispisuje ``tra-la-la``? (Označite sve tačne odgovore)
       
.. dragndrop:: console__text_quiz_nanana
    :feedback: Pokušajte ponovo!
    :match_1: 'NA' * 3 ||| 'NANANA'
    :match_2: 'N' + 3 * 'A' ||| 'NAAA'
    :match_3: 'N' * 3 + 'A' ||| 'NNNA'
    :match_4: 'N' * 3 + 3 * 'A' |||'NNNAAA'

    Uparite izraze sa njihovim vrednostima.

.. fillintheblank:: console__text_quiz_N_A

    Šta ispisuje naredba ``print(('N' + 'A') * 2)``?
    
    - :NANA: Tačno!
      :NNAA: Prvo se izračunava deo u zagradi (kao u matematici)
      :.*: Pokušajte ponovo.

.. questionnote::

    **Zadatak - Deljenje zarade**

    Tri prijatelja su se dogovorila da zaradu od zajedničkog posla podele tako da prvom pripadne 2/7 zarade, drugom 1/3, a trećem preostala svota. Ukupna zarada je bila 40000. Dovršite program, koji će na dve decimale prikazati zaradu svakog od trojice prijatelja.

    
.. activecode:: console__computing_earnings

    ukupna_zarada = 40000
    prvi = ukupna_zarada * 2 / 7
    drugi = 0 # ispravite
    treci = ukupna_zarada - prvi - drugi
    # dodajte naredbe za ispisivanje

