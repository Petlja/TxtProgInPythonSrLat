# -*- acsection: general-init -*-
import pygame as pg, pygamebg
prozor = pygamebg.open_window(300, 300, "Дрвеће")

# -*- acsection: main -*-
prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno

for i in range(3):
    pg.draw.rect(prozor, pg.Color("brown"), (100*i + 40, 180, 20, 100))        # stablo
    pg.draw.ellipse(prozor, pg.Color("darkgreen"), (100*i + 10, 50, 80, 150))  # krosnja

# -*- acsection: after-main -*-
pygamebg.wait_loop()
