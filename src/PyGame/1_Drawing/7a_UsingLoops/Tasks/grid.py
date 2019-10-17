# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(sirina, visina) = (500, 300)
prozor = pygamebg.open_window(sirina, visina, "Решетка")

# -*- acsection: main -*-
prozor.fill(pg.Color("gray"))

for x in range(10, sirina, 20):
    pg.draw.line(prozor, pg.Color("black"), (x, 10), (x, visina - 10), 1)

for y in range(10, visina, 20):
    pg.draw.line(prozor, pg.Color("black"), (10, y), (sirina - 10, y), 1)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
