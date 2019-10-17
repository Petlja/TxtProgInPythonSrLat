# -*- acsection: general-init -*-
import pygame as pg, pygamebg
prozor = pygamebg.open_window(800, 600, "Јабуке")
# -*- acsection: main -*-

drvo_slika = pg.image.load("tree.png")  # slika drveta

prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno
prozor.blit(drvo_slika, (0, 0))

# -*- acsection: after-main -*-
pygamebg.wait_loop()
