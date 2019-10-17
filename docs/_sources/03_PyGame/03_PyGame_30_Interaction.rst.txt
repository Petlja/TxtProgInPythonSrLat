Interakcija
===========

U PajGejm programima koje smo do sada videli korisnik nije mogao da utiče na njihov rad, osim da prekine program. Ovakve programe možemo da uporedimo sa gledanjem filmova - korisnik je u suštini gledalac.

U narednom poglavlju ćemo se baviti programima u kojima korisnik ima aktivnu ulogu i može da utiče na rad programa koristeći miša i tastaturu. Postoje dva osnovna načina da naš program "zna" kada je korisnik reagovao.

- Jedan način je **očitavanje stanja** miša i tastature. Iz programa možemo da pitamo koja je trenutna pozicija miša, da li je neki taster trenutno pritisnut i slično.
- Drugi način je korišćenje sistemskih **događaja.** Svaka akcija korisnika (pritisak na taster miša ili tastature, otpuštanje tastera, pomeranje miša i slično) je događaj, a mi u programima možemo da dobijemo informacije o takvim događajuma i da reagujemo na njih.

U nastavku ćemo upoznati oba ova načina koji omogućavaju našim programima da reaguju na akcije korisnika.

   .. toctree::
      :maxdepth: 1

      ./03_PyGame_31_Interaction_ReadMousePos.rst
      ./03_PyGame_32_Interaction_ReadMouseKey.rst
      ./03_PyGame_33_Interaction_ReadKeyboard.rst
      ./03_PyGame_34_Interaction_Events.rst
      ./03_PyGame_35_Interaction_EventMouse.rst
      ./03_PyGame_36_Interaction_EventKeyboard.rst
