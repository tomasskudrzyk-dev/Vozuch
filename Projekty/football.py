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

def draw_goal(surface, x, y, width, height, frame_color, net_color):
    pygame.draw.rect(surface, frame_color, (x, y, width, height), 5)
    # síť v brance
    for i in range(1, 6):
        x_offset = i * (width // 6)
        y_offset = i * (height // 6)
        pygame.draw.line(surface, net_color, (x + x_offset, y), (x + x_offset, y + height), 1)
        pygame.draw.line(surface, net_color, (x, y + y_offset), (x + width, y + y_offset), 1)

#Vykreslení hřiště
pygame.draw.rect(okno, BILA, (50, 50, 900, 700), 5) # Hřiště
pygame.draw.line(okno, BILA, (SIRKA // 2, 50), (SIRKA // 2, 750), 5) # Středová čára
pygame.draw.circle(okno, BILA, (SIRKA // 2, VYSKA // 2), 50, 5) # Středový kruh
#Vykreslení vápna
pygame.draw.rect(okno, BILA, (50, 250, 150, 300), 5) # Levé vápno
pygame.draw.rect(okno, BILA, (800, 250, 150, 300), 5) # Pravé vápno
#Vykreslení malého vápna
pygame.draw.rect(okno, BILA, (50, 325, 75, 150), 5) # Levé malé vápno
pygame.draw.rect(okno, BILA, (875, 325, 75, 150), 5) # Pravé malé vápno

# Brankové konstrukce
draw_goal(okno, 50, 300, 50, 200, BILA, SEDA)   # Levá branka
draw_goal(okno, 900, 300, 50, 200, BILA, SEDA)  # Pravá branka

#Vykreslení 6 fotbalistů, kteří budou rozestaveni na levé polovině hřiště
for i in range(6):
    x = random.randint(50, SIRKA // 2 - 50)
    y = random.randint(100, VYSKA - 100)
    pygame.draw.circle(okno, CERVENA, (x, y), 20) # Fotbalista jako červený kruh
    pygame.draw.circle(okno, CERNA, (x, y), 20, 2) # Obrys fotbalisty

    #Každý fotbalista bude mít na sobě napsané jekékoliv číslo od 1 do 99
    cislo = random.randint(1, 99)
    text = pismo.render(str(cislo), True, BILA)
    text_rect = text.get_rect(center=(x, y))
    okno.blit(text, text_rect)

#Vykreslení 6 fotbalistů, kteří budou rozestaveni na pravé polovině hřiště
for i in range(6):
    x = random.randint(SIRKA // 2 + 50, SIRKA - 50)
    y = random.randint(100, VYSKA - 100)
    pygame.draw.circle(okno, BILA, (x, y), 20) # Fotbalista jako modrý kruh
    pygame.draw.circle(okno, CERNA, (x, y), 20, 2) # Obrys fotbalisty

    #Každý fotbalista bude mít na sobě napsané jekékoliv číslo od 1 do 99
    cislo = random.randint(1, 99)
    text = pismo.render(str(cislo), True, CERVENA)
    text_rect = text.get_rect(center=(x, y))
    okno.blit(text, text_rect)

    #přidání scoreboardu
scoreboard_text = pismo.render("Skóre: 0 - 0", True, BILA)
scoreboard_rect = scoreboard_text.get_rect(center=(SIRKA // 2, 30))
okno.blit(scoreboard_text, scoreboard_rect)

#Vykreslení míče uprostřed hřiště
pygame.draw.circle(okno, BILA, (SIRKA // 2, VYSKA // 2), 15) # Míč jako bílý kruh
pygame.draw.circle(okno, CERNA, (SIRKA // 2, VYSKA // 2), 15, 2) # Obrys míče

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
