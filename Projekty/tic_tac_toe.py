import random
import pygame
import sys

#nastavení barev
BILA = (255, 255, 255)
CERNA = (0, 0, 0)

#nastavení herního pole
pole = [[None, None, None],
    [None, None, None],
    [None, None, None]]
#nastavení hráčů
HRAC_X = "X"
HRAC_O = "O"

pygame.init()#inicializace pygame modulu
#nastavení velikosti okna
SIRKA, VYSKA = 1000, 800
OKNO = pygame.display.set_mode((SIRKA, VYSKA))
#nastavení názvu okna
pygame.display.set_caption("Tic Tac Toe")
pismo = pygame.font.SysFont("Arial", 24)
bezi = True
hodiny = pygame.time.Clock()
while bezi:
 for udalost in pygame.event.get():
    if udalost.type == pygame.QUIT:
        bezi = False
    #nastavení velikosti políčka
    VELIKOST_POLICKA = 200
    #funkce pro vykreslení herního pole
    def vykresli_pole():
        OKNO.fill(BILA)
    for i in range(1, 3):
        pygame.draw.line(OKNO, CERNA, (i * VELIKOST_POLICKA, 0), (i * VELIKOST_POLICKA, VYSKA), 5)
        pygame.draw.line(OKNO, CERNA, (0, i * VELIKOST_POLICKA), (SIRKA, i * VELIKOST_POLICKA), 5)
    for radek in range(3):
        for sloupec in range(3):
            if pole[radek][sloupec] is not None:
                text = pismo.render(pole[radek][sloupec], True, CERNA)
                OKNO.blit(text, (sloupec * VELIKOST_POLICKA + 80, radek * VELIKOST_POLICKA + 80))
                OKNO.fill(BILA)
pygame.display.flip()
hodiny.tick(60)