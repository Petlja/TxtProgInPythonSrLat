# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(sirina, visina) = (800, 500)
prozor = pygamebg.open_window(sirina, visina, "Прекидач")

shema_slike = (pg.image.load('Shema1_Off.png'), pg.image.load('Shema1_On.png'))
prekidac_slike = (pg.image.load('SwitchOff.png'), pg.image.load('SwitchOn.png'))
sijalica_slike = (pg.image.load('BulbOff.png'), pg.image.load('BulbOn.png'))
prekidac_poz = (100, 200)
sijalica_poz = (500, 100)

def tacka_u_pravougaoniku(tacka, gornje_levo_teme, sirina, visina):
    x, y = tacka
    x0, y0 = gornje_levo_teme
    return x0 <= x and x <= x0 + sirina and y0 <= y and y <= y0 + visina
    
# -*- acsection: main -*-
ukljucen_prekidac = False
fps = 50

def nov_frejm():
    global ukljucen_prekidac
    pritisnut_taster_misa = pg.mouse.get_pressed()
    if pritisnut_taster_misa[0]:
        mis_tacka = pg.mouse.get_pos()
        if tacka_u_pravougaoniku(mis_tacka, prekidac_poz, 80, 80):
            ukljucen_prekidac = not ukljucen_prekidac
# -*- acsection: after-main -*-
 
    prozor.blit(shema_slike[ukljucen_prekidac], (0, 0))
    prozor.blit(prekidac_slike[ukljucen_prekidac], prekidac_poz)
    prozor.blit(sijalica_slike[ukljucen_prekidac], sijalica_poz)
    
pygamebg.frame_loop(fps, nov_frejm)
