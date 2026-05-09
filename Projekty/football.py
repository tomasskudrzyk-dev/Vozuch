import pygame
import sys
import random

pygame.init()# Inicializace pygame modulu
hodiny = pygame.time.Clock()
# Nastavení rozměrů okna
SIRKA, VYSKA = 1000, 800
# Vytvoření okna
okno = pygame.display.set_mode((SIRKA, VYSKA))
# Nastavení názvu okna
pygame.display.set_caption("Fotbal")
pismo = pygame.font.SysFont("Arial", 24)
#Nastavení barev
BILA = (255, 255, 255)
SEDA = (128, 128, 128)
CERNA = (0, 0, 0)
CERVENA = (255, 0, 0)
MODRA = (0, 0, 255)
ZELENA = (0, 255, 0)
TMAVE_ZELENA = (0, 100, 0)

#Nastavení pozadí
pozadi = pygame.Surface((SIRKA, VYSKA))
pozadi.fill(TMAVE_ZELENA)
    #aktualizace obrazovky
okno.blit(pozadi, (0, 0))

#Vykreslení hřiště
pygame.draw.rect(okno, BILA, (50, 50, 900, 700), 5) # Hřiště
pygame.draw.line(okno, BILA, (SIRKA // 2, 50), (SIRKA // 2, 750), 5) # Středová čára
pygame.draw.circle(okno, BILA, (SIRKA // 2, VYSKA // 2), 50, 5) # Středový kruh
pygame.draw.rect(okno, BILA, (50, 300, 50, 200), 5) # Levá branka
pygame.draw.rect(okno, BILA, (900, 300, 50, 200), 5) # Pravá branka

#Hlavní herní smyčka
bezi = True
while bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False
    #aktualizace obrazovky
    pygame.display.flip()# Aktualizace okna
    #regulace FPS
    hodiny.tick(60)
#ukončení pygame
pygame.quit()
