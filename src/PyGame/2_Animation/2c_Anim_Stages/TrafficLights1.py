import pygame as pg, pygamebg
(sirina, visina) = (100, 300)
prozor = pygamebg.open_window(sirina, visina, "Семафор")

# faze su: crveno, crveno_zuto, zeleno, zuto
trajanje_faze = (25, 10, 25, 10) # 25 frejmova za crveno, 10 za crveno_zuto itd.

kraj_faze = []
ukupno_frejmova = 0
for f in trajanje_faze:
    ukupno_frejmova += f
    kraj_faze.append(ukupno_frejmova)

x = 50             # x koordinata centara krugova
y = [50, 150, 250] # y koordinate centara krugova
r = 40             # poluprecnik (svih) krugova
crvena_uklj  = (255,   0, 0)
crvena_isklj = (128,   0, 0)
zuta_uklj    = (255, 255, 0)
zuta_isklj   = (128, 128, 0)
zelena_uklj  = (  0, 255, 0)
zelena_isklj = (  0, 128, 0)

i_frejm  = 0
fps = 10

def crtaj_semafor(boja_gore, boja_sredina, boja_dole):
    pg.draw.circle(prozor, boja_gore,    (x,  y[0]), r)
    pg.draw.circle(prozor, boja_sredina, (x,  y[1]), r)
    pg.draw.circle(prozor, boja_dole,    (x,  y[2]), r)
        
def nov_frejm():
    global i_frejm
    i_frejm = (i_frejm + 1) % ukupno_frejmova
    
    prozor.fill(pg.Color("darkgray")) # bojimo pozadinu prozora u sivo
    if i_frejm < kraj_faze[0]: # ako frejm pripada fazi 'crveno'
        crtaj_semafor(crvena_uklj, zuta_isklj, zelena_isklj)
    elif i_frejm < kraj_faze[1]: # ako frejm pripada fazi 'crveno_zuto'
        crtaj_semafor(crvena_uklj, zuta_uklj, zelena_isklj)
    elif i_frejm < kraj_faze[2]: # ako frejm pripada fazi 'zeleno'
        crtaj_semafor(crvena_isklj, zuta_isklj, zelena_uklj)
    else: # frejm pripada poslednjoj fazi ('zuto')
        crtaj_semafor(crvena_isklj, zuta_uklj, zelena_isklj)

pygamebg.frame_loop(fps, nov_frejm)
