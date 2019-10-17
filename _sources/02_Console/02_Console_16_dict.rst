Rečnici
=======

Sada ćemo upoznati još jednu vrstu složenih tipova podataka, odnosno kolekcija, koja je drugačija od onih koje smo do sada upoznali.

Pretpostavimo da treba da napišemo program koji odgovara na pitanja o starosti pojedinih osoba. Imena i starosti osoba su nam poznati, na primer Marija ima 14 godina, Mihajlo 15, Danijela takođe 15, a Nenad 16 (stvarni podaci bi bili mnogo obimniji, ali za ilustraciju je dovoljno i ovo). 

Zadatak možemo da rešimo tako što imena smestimo u jednu torku, a starosti u drugu. Sa ovako organizovanim podacima možemo pomoću petlje da tražimo zadato ime u torki imena, pa kada ga nađemo, ispisujemo odgovarajuću starost.

.. activecode:: dict__two_tuples

    imena = ('Marija', 'Mihajlo', 'Danijela', 'Nenad')
    godine = (14, 15, 15, 16)
    trazeno_ime = input('Unesite ime: ')
    ime_je_nadjeno = False
    for i in range(len(imena)):
        if trazeno_ime == imena[i]:
            print(trazeno_ime, 'ima', godine[i], 'godina.')
            ime_je_nadjeno = True
            break
    
    if not ime_je_nadjeno:
        print('Ime', trazeno_ime, 'nije nađeno.')

Kao što vidimo, kolekcije koje već poznajemo mogu i u ovom slučaju da nam posluže. Ipak, za ovakvu vrstu zadataka postoji kolekcija u kojoj se podaci zapisuju na pregledniji način, a potreban podatak se pronalazi jednostavnije i mnogo efikasnije. Pogledajmo drugo rešenje:

.. activecode:: dict__1st_example

    godine = {'Marija':14, 'Mihajlo':15, 'Danijela':15, 'Nenad':16}
    trazeno_ime = input('Unesite ime: ')
    if trazeno_ime in godine:
        print(trazeno_ime, 'ima', godine[trazeno_ime], 'godina.')
    else:
        print('Ime', trazeno_ime, 'nije nađeno.')

Kolekcija oblika {'Marija':14, 'Mihajlo':15, 'Danijela':15, 'Nenad':16} se zove **rečnik**. Vidimo da rečnik može da se zada slično kao i torka i lista - nabrajanjem elemenata razdvojenih zarezima. Elementi rečnika se zapisuju između vitičastih zagrada ``{ }``. Svaki element se sastoji od dva dela između kojih stoji znak dvotačka ``:``. Prvi deo elementa se naziva **ključ**, a drugi **vrednost**. Na primer, ključu 'Marija' odgovara vrednost 14 itd. 

Rečnike koristimo tako što za dati ključ brzo i lako dobijamo vrednost. U našem primeru smo za dato ime u rečniku pronalazili broj godina. U torkama i listama na sličan način pomoću rednog broja (indeksa) elementa dohvatamo vrednost elementa. Možemo da kažemo da ključ u rečniku ima onu ulogu koju indeks ima u torkama i listama. Suštinstka razlika rizmeđu rečnika sa jedne, i torki i listi sa druge strane, je u tome što u rečniku ključ može da bude bilo kojeg nepromenljivog tipa (ceo broj, realan broj, string, torka...) dok u torki ili listi indeksi moraju da budu celi brojevi redom od 0.

Formiranje rečnika
------------------

Rečnik možemo i da formiramo tokom rada programa. To radimo tako što u rečnik ubacujemo nove parove ključ - vrednost, a zatim po potrebi menjamo vrednost za dati ključ. 

U sledećem primeru polazna torka sadrži imena fudbalskih klubova koji su u periodu 1956-2019 osvajali Kup evropskih šampiona, odnosno UEFA Ligu prvaka. Na osnovu tih podataka ćemo formirati rečnik u kome ćemo za svaki klub pamtiti broj osvojenih šampionata. Evo kako to možemo da uradimo.

.. activecode:: dict__counting

    sampioni = (
        'Real Madrid',       'Real Madrid',       'Real Madrid',       'Real Madrid',
        'Real Madrid',       'Benfica',           'Benfica',           'Milan',
        'Internazionale',    'Internazionale',    'Real Madrid',       'Celtic',
        'Manchester United', 'Milan',             'Feyenoord',         'Ajax',
        'Ajax',              'Ajax',              'Bayern Munich',     'Bayern Munich',
        'Bayern Munich',     'Liverpool',         'Liverpool',         'Nottingham Forest',
        'Nottingham Forest', 'Liverpool',         'Aston Villa',       'Hamburg',
        'Liverpool',         'Juventus',          'Steaua București',  'Porto',
        'PSV Eindhoven',     'Milan',             'Milan',             'Red Star Belgrade',
        'Barcelona',         'Marseille',         'Milan',             'Ajax',
        'Juventus',          'Borussia Dortmund', 'Real Madrid',       'Manchester United',
        'Real Madrid',       'Bayern Munich',     'Real Madrid',       'Milan',
        'Porto',             'Liverpool',         'Barcelona',         'Milan',
        'Manchester United', 'Barcelona',         'Internazionale',    'Barcelona',
        'Chelsea',           'Bayern Munich',     'Real Madrid',       'Barcelona',
        'Real Madrid',       'Real Madrid',       'Real Madrid',       'Liverpool'
    )
    broj_titula = {} # prazan recnik
    for klub in sampioni:
        if klub in broj_titula:
            broj_titula[klub] += 1
        else:
            broj_titula[klub] = 1
    
    print('klub          broj titula')
    print('-' * 25)    
    for klub in broj_titula:
        s_br_titula = str(broj_titula[klub])
        razmak = ' ' * (25 - len(klub) - len(s_br_titula))
        print(klub + razmak + s_br_titula)

Na početku formiramo prazan rečnik *broj_titula*. Za svaki klub iz spiska šampiona prvo proverimo da li klub već postoji u rečniku *broj_titula*. Ako postoji, na broj titula tog kluba dodajemo jedan, a ako ne postoji, upisujemo klub u rečnik sa jednom osvojenom titulom. 

Po završetku prebrojavanja smo pomoću petlje prošli kroz rečnik i ispisali ključeve i vrednosti iz tog rečnika.

Jedan način da skratimo ovaj program je da koristimo funkciju (metodu) ``get``, koja je deo svakog rečnika i poziva se sa *ime_recnika.get(kljuc, podrazumevana_vrednost)*. Kao što vidimo, ova funkcija ima dva argumenta. Prvi argument je ključ za koji tražimo vrednost. U slučaju da taj ključ postoji u rečniku, funkcija *get* vraća vrednost koja odgovara tom ključu, a ako ključ nije u rečniku, funkcija vraća vrednost svog drugog argumenta. Tako na primer, umesto 

.. code::

    if klub in broj_titula:
        broj_titula[klub] += 1
    else:
        broj_titula[klub] = 1

možemo da pišemo

.. code::

    broj_titula[klub] = broj_titula.get(klub, 0) + 1
    
i efekat je isti. U ovom primeru *broj_titula.get(klub, 0)* vraća broj titula datog kluba ako je je on već u rečniku, odnosno 0 ako još nije. I u jednom i u drugom slučaju na tu vrednost treba da se doda 1 i da se nova vrednost sačuva u rečniku.


Zadaci za vežbu
'''''''''''''''

.. questionnote::

    **Zadatak - cene namirnica**
    
    Cene u jednoj prodavnici su: 
    
    - hleb: 1 (za veknu od pola kilograma)
    - mleko: 0.8 (za litar)
    - jaje: 0.08 (za komad)
    - pileća prsa: 7.3 (za kilogram)
    - jabuke: 2.2 (za kilogram)
    - paradajz: 1 (za kilogram)
    
    Smestiti ove podatke u rečnik, a zatim dopuniti program tako da učitava naziv namirnice i ispisuje cenu te namirnice, ili informaciju da ta namirnica nije na raspolaganju.
    
.. activecode:: console__dict__prices
    
.. reveal:: console__dict__prices_reveal
    :showtitle: Rešenje
    :hidetitle: Sakrij rešenje

    Rešenje:
    
    .. activecode:: console__dict__prices_sol1
        :passivecode: true
        
        cene = {
            "hleb": 1, "mleko": 0.8, "jaje": 0.08,
            "pileća prsa": 7.3, "jabuke": 2.2, "paradajz": 1 
        }
        namirnica = input()
        print(cene.get(namirnica, "nije na raspolaganju"))

.. questionnote::

    **Zadatak - izostanci**
    
    U torki su data imena učenika koji su izostajali sa nastave. Svako pojavljivanje jednog imena predstavlja izostanak sa jednog časa. Dovršiti program tako da izračunava i ispisuje sa koliko je časova koji učenik izostao.
    
    Da bismo vam pomogli da proverite program, dajemo i očekivani rezultat: za podatke date u torki *izostali*, treba da dobijete da Dragan ima 4 izostanka, Maja 3, Aleksandar 2, a Ljubica, Mirko, Ognjen, Petar, Rade i Olivera po jedan (ne nužno tim redom).
    
.. activecode:: console__dict__absence
    
    izostali = (
        'Maja', 'Dragan', 'Ljubica', 'Aleksandar', 'Dragan', 
        'Mirko', 'Maja', 'Ognjen', 'Dragan', 'Petar',
        'Rade', 'Olivera', 'Maja', 'Aleksandar', 'Dragan')

.. commented out

    izostanci = {}
    for ime in izostali:
        izostanci[ime] = izostanci.get(ime, 0) + 1
    for ime in izostanci:
        print(ime, izostanci[ime])
        
.. questionnote::

    **Zadatak - zalihe**
    
    Date su nabavke i prodaje robe u obliku torke parova. U svakom paru prvi element je naziv robe, a drugi promena stanja zaliha. Na primer, par *('sir', -1.5)* znači da se raspoloživa količina sira smanjila za 1.5 (toliko sira je prodato).
     
    Dovršiti program koji na osnovu datih promena stanja izračunava i ispisuje stanje nakon tih promena. Smatrati da na početku nema nikakvih zaliha.
    
    Proverite rezultat: za date podatke, treba da dobijete (u bilo kom redosledu)
    
    - sir 18.5
    - mleko 297
    - brašno 985
    - jaja 1988
    - riba 47
     
Ovde je najvažniji deo programa prolazak kroz sve parove. Radi jasnoće, svaki par iz torke promene odmah raspakujemo u promenljive *namirnica*, *promena*.
    
.. activecode:: console__dict__stock_status
    
        promene = (
            ('sir', 20), ('mleko', 300), ('sir', -1.5), ('brašno', 1000), 
            ('jaja', 2000), ('mleko', -2), ('brašno', -5), ('riba', 50), 
            ('jaja', -12), ('mleko', -1), ('brašno', -10), ('riba', -3)
        )
        
        stanje = {}
        for namirnica, promena in promene:
            # dovrsite
            
        for namirnica in stanje:
            print(namirnica, stanje[namirnica])