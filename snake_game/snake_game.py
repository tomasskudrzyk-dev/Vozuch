import pygame
import random
import sys

pygame.init() # inicializace pygame modulu
# nastavení rozměrů okna
SIRKA, VYSKA = 1000, 800
# nastavení barev
CERNA = (0, 0, 0)
BILA = (255, 255, 255)
ZELENA = (0, 255, 0)
CERVENA = (255, 0, 0)
VELIKOST_BLOKU = 20
rychlost = 4
VELIKOST_JIDLA = 10
had_x = SIRKA // 2
had_y = VYSKA // 2
# vytvoření okna
okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Snake game") #nastavení názvu okna
pismo = pygame.font.SysFont("Arial", 24) #nastavení fontu a velikosti písma
hra_zacala = False #nastavení proměnné pro kontrolu, zda hra začala
bezi = True
hodiny = pygame.time.Clock() #nastavení hodin pro regulaci FPS
while bezi:
    for udalost in pygame.event.get(): #zpracování událostí
        if udalost.type == pygame.QUIT: #kontrola, zda uživatel chce ukončit hru
            bezi = False
    klavesy = pygame.key.get_pressed() #získání stavu kláves
    if klavesy[pygame.K_w]: #had se pohybuje nahoru po stisknutí klávesy W
        had_y -= rychlost
    if klavesy[pygame.K_s]: #had se pohybuje dolů po stisknutí klávesy S
        had_y += rychlost
    if klavesy[pygame.K_a]: #had se pohybuje doleva po stisknutí klávesy A
        had_x -= rychlost
    if klavesy[pygame.K_d]: #had se pohybuje doprava po stisknutí klávesy D
        had_x += rychlost

    okno.fill(CERNA) #vyplnění pozadí černou barvou
    #had se vykreslí jako zelený obdélník
    pygame.draw.rect(okno, ZELENA, (had_x, had_y, VELIKOST_BLOKU, VELIKOST_BLOKU))




    pygame.display.update() #aktualizace obrazovky

    #regulace FPS
    hodiny.tick(60) #nastavení FPS na 60
pygame.quit() #ukončení pygame



