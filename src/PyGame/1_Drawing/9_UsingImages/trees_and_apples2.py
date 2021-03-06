# -*- acsection: general-init -*-
import pygame as pg, pygamebg
prozor = pygamebg.open_window(800, 600, "Јабуке")
# -*- acsection: main -*-

drvo_slika = pg.image.load("tree.png")  # slika drveta
jabuka_slika = pg.image.load("apple_small.png")  # slika jabuke
jabuke_poz = ((43,191), (61, 158), (124, 145), (134, 175), (160, 180))

prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno
prozor.blit(drvo_slika, (0, 0))
for x, y in jabuke_poz:
    prozor.blit(jabuka_slika, (x, y))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
