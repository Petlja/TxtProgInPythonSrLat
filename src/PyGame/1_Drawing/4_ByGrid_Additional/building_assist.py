# -*- acsection: general-init -*-
import pygame as pg, pygamebg
prozor = pygamebg.open_window(300, 300, "Pygame")

# -*- acsection: main -*-
(sirina, visina) = (300, 300)
def crtanje():
    prozor.blit(platno, (0, 0))  # crtanje onoga sto je zadato
    
    # ose
    pg.draw.line(prozor, pg.Color("black"), (mis_x, 0), (mis_x, visina), 1) # uspravna linija misa
    pg.draw.line(prozor, pg.Color("black"), (0, mis_y), (sirina, mis_y), 1) # vodoravna linija misa

    # ispis koordinata
    str_x, str_y = str(mis_x), str(mis_y)
    xt_y, yt_y = (5, mis_y - 25) if 2 * mis_y > visina else (visina - 25, mis_y + 5)
    xt_x, yt_x = (mis_x - 50, 5) if 2 * mis_x > sirina else (mis_x + 5, sirina - 50)
    sl_x = font.render(str_x, True, pg.Color("black"))
    sl_y = font.render(str_y, True, pg.Color("black"))
    if mis_x <= 150:
        prozor.blit(sl_x, (xt_x, xt_y))
    if mis_y <= 60 or mis_y >= 135:
        prozor.blit(sl_y, (yt_x, yt_y))

def obradi_dogadjaj(dogadjaj):
    global mis_x, mis_y
    if dogadjaj.type == pg.MOUSEMOTION:   # miš je pomeren
        mis_x, mis_y = dogadjaj.pos
        return True                         # ponovo iscrtavamo scenu
    return False                            # nema potrebe da iscrtavamo scenu

################# crtez
platno = pg.Surface((sirina, visina)) # platno na kome je slika nacrtana
platno.fill(pg.Color("lightgray")) # bojimo pozadinu ekrana u svetlo sivo

pg.draw.rect(platno, pg.Color("darkgray"), (120, 50, 60, 140))   # zgrada
pg.draw.rect(platno, pg.Color("yellow"), (130, 60, 15, 15))      # levi prozor, prvi red
pg.draw.rect(platno, pg.Color("yellow"), (155, 60, 15, 15))      # desni prozor, prvi red
pg.draw.rect(platno, pg.Color("yellow"), (130, 80, 15, 15))      # levi prozor, drugi red
pg.draw.rect(platno, pg.Color("black"),  (155, 80, 15, 15))      # desni prozor, drugi red
pg.draw.rect(platno, pg.Color("black"),  (130, 100, 15, 15))     # levi prozor, treci red
pg.draw.rect(platno, pg.Color("yellow"), (155, 100, 15, 15))     # desni prozor, treci red
pg.draw.rect(platno, pg.Color("yellow"), (130, 120, 15, 15))     # levi prozor, cetvrti red
pg.draw.rect(platno, pg.Color("yellow"), (155, 120, 15, 15))     # desni prozor, cetvrti red
pg.draw.rect(platno, pg.Color("black"),  (130, 140, 15, 15))     # levi prozor, peti red
pg.draw.rect(platno, pg.Color("black"),  (155, 140, 15, 15))     # desni prozor, peti red
pg.draw.rect(platno, pg.Color("black"),  (140, 160, 20, 30))     # kapija
#################

font = pg.font.SysFont("Arial", 20)         # font kojim će biti prikazan tekst
font.set_bold(True)
mis_x, mis_y = 0, 0

treba_crtati = True
kraj = False
while not kraj:
    if treba_crtati:    # ako je potrebno nacrtati lopticu
        crtanje()
        pg.display.update()        # ažuriramo prikaz sadržaja prozora
        treba_crtati = False

    dogadjaj = pg.event.wait()     # čekamo naredni događaj
    if dogadjaj.type == pg.QUIT:   # isključivanje prozora
        kraj = True
    else:
        treba_crtati = obradi_dogadjaj(dogadjaj)

# Zavrsetak skrivenog programa, koji radi kao primer
pg.quit()
pg.time.set_timer(pg.QUIT,50)
pg.time.wait(70)
pg.time.set_timer(pg.QUIT,0)

# Zavrsetak korisnickog programa je posebnoj sekciji

# -*- acsection: after-main -*-
pygamebg.wait_loop()
