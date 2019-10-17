# -*- acsection: general-init -*-
import pygame as pg, pygamebg
prozor = pygamebg.open_window(300, 300, "Ограда")
# -*- acsection: main -*-

prozor.fill(pg.Color("skyblue")) # bojimo pozadinu ekrana u nebo-plavo
pg.draw.rect(prozor, pg.Color("green"), (0, 200, 300, 100))  # trava

boja = pg.Color('brown')
pg.draw.line(prozor, boja, ( 10, 100), (290, 100), 10) # gornja poprecna daska
pg.draw.line(prozor, boja, ( 10, 250), (290, 250), 10) # donja poprecna daska

# pritke
pg.draw.polygon(prozor, boja, [(20, 80), (30, 70), (40, 80), (40, 270), (20, 270)])
pg.draw.polygon(prozor, boja, [(60, 80), (70, 70), (80, 80), (80, 270), (60, 270)])
pg.draw.polygon(prozor, boja, [(100, 80), (110, 70), (120, 80), (120, 270), (100, 270)])
pg.draw.polygon(prozor, boja, [(140, 80), (150, 70), (160, 80), (160, 270), (140, 270)])
pg.draw.polygon(prozor, boja, [(180, 80), (190, 70), (200, 80), (200, 270), (180, 270)])
pg.draw.polygon(prozor, boja, [(220, 80), (230, 70), (240, 80), (240, 270), (220, 270)])
pg.draw.polygon(prozor, boja, [(260, 80), (270, 70), (280, 80), (280, 270), (260, 270)])

# -*- acsection: after-main -*-
pygamebg.wait_loop()
