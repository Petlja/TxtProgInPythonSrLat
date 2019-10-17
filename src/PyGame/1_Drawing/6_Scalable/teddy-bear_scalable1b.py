# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(sirina, visina) = (300, 300)
prozor = pygamebg.open_window(sirina, visina, "Медведић")
# -*- acsection: main -*-
# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

def uokviren_krug(prozor, boja, centar, poluprecnik):
    pg.draw.circle(prozor, boja, centar, poluprecnik)
    pg.draw.circle(prozor, pg.Color("black"), centar, poluprecnik, 1)

def crtaj_medu(cx, cy, a):
    uokviren_krug(prozor, pg.Color("yellow"), (cx - 12*a,  cy - 14*a),  9*a) # levo uvo
    uokviren_krug(prozor, pg.Color("yellow"), (cx + 12*a,  cy - 14*a),  9*a) # desno uvo
    uokviren_krug(prozor, pg.Color("yellow"), (cx,         cy),        20*a) # glava
    uokviren_krug(prozor, pg.Color("yellow"), (cx,         cy + 10*a), 10*a) # njuska
    uokviren_krug(prozor, pg.Color("black"),  (cx - 10*a,  cy - 6*a),   3*a) # levo oko
    uokviren_krug(prozor, pg.Color("black"),  (cx + 10*a,  cy - 6*a),   3*a) # desno oko
    uokviren_krug(prozor, pg.Color("black"),  (cx,         cy + 4*a),   3*a) # vrh njuske

crtaj_medu(85, 100, 4)
crtaj_medu(235, 100, 3)
crtaj_medu(50, 250, 2)
crtaj_medu(150, 250, 2)
crtaj_medu(250, 250, 2)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
