# -*- acsection: general-init -*-
import pygame as pg, pygamebg
prozor = pygamebg.open_window(300, 300, "Мрав")

# -*- acsection: main -*-
prozor.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo

pg.draw.ellipse(prozor, pg.Color("limegreen"), (75, 100, 150, 180))    # glava
pg.draw.line(prozor, pg.Color("limegreen"), (130, 110), (120, 20), 6)  # leva antenica
pg.draw.line(prozor, pg.Color("limegreen"), (170, 110), (180, 20), 6)  # desna antenica
pg.draw.circle(prozor, pg.Color("limegreen"), (120, 20), 10)           # vrh leve antenice
pg.draw.circle(prozor, pg.Color("limegreen"), (180, 20), 10)           # vrh desne antenice
pg.draw.ellipse(prozor, pg.Color("black"), (110, 140, 30, 50))         # levo oko
pg.draw.ellipse(prozor, pg.Color("black"), (160, 140, 30, 50))         # desno oko

# -*- acsection: after-main -*-
pygamebg.wait_loop()
