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

#nastavení velikosti políčka
VELIKOST_POLICKA = 200
aktualni_hrac = HRAC_X

#funkce pro vykreslení herního pole
def vykresli_pole():
    OKNO.fill(BILA)

    #zarovnání herního pole na střed okna
    SIRKA_POLICKA = VELIKOST_POLICKA * 3
    offset_x = (SIRKA - SIRKA_POLICKA) // 2
    offset_y = (VYSKA - SIRKA_POLICKA) // 2

    #Nakreslení svislých čar
    for i in range(1, 3):
        x = offset_x + i * VELIKOST_POLICKA
        pygame.draw.line(OKNO, CERNA, (x, offset_y), (x, offset_y + SIRKA_POLICKA), 5)

    #Nakreslení vodorovných čar
    for i in range(1, 3):
        y = offset_y + i * VELIKOST_POLICKA
        pygame.draw.line(OKNO, CERNA, (offset_x, y), (offset_x + SIRKA_POLICKA, y), 5)

        #Nakreslení postranních čar pro oddělení herního pole od zbytku okna
    pygame.draw.line(OKNO, CERNA, (offset_x - 5, offset_y), (offset_x - 5, offset_y + SIRKA_POLICKA), 5)
    pygame.draw.line(OKNO, CERNA, (offset_x + SIRKA_POLICKA + 5, offset_y), (offset_x + SIRKA_POLICKA + 5, offset_y + SIRKA_POLICKA), 5)
    pygame.draw.line(OKNO, CERNA, (offset_x, offset_y - 5), (offset_x + SIRKA_POLICKA, offset_y - 5), 5)
    pygame.draw.line(OKNO, CERNA, (offset_x, offset_y + SIRKA_POLICKA + 5), (offset_x + SIRKA_POLICKA, offset_y + SIRKA_POLICKA + 5), 5)
        
    #Nakreslení X a O vycentrované v každé buňce
    for radek in range(3):
        for sloupec in range(3):
            if pole[radek][sloupec] is not None:
                text = pismo.render(pole[radek][sloupec], True, CERNA)
                text_rect = text.get_rect()
                text_rect.center = (
                    offset_x + sloupec * VELIKOST_POLICKA + VELIKOST_POLICKA // 2,
                    offset_y + radek * VELIKOST_POLICKA + VELIKOST_POLICKA // 2,
                )
                OKNO.blit(text, text_rect)

while bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False
        elif udalost.type == pygame.MOUSEBUTTONDOWN and udalost.button == 1:
            mouse_x, mouse_y = udalost.pos
            SIRKA_POLICKA = VELIKOST_POLICKA * 3
            offset_x = (SIRKA - SIRKA_POLICKA) // 2
            offset_y = (VYSKA - SIRKA_POLICKA) // 2
            if offset_x <= mouse_x < offset_x + SIRKA_POLICKA and offset_y <= mouse_y < offset_y + SIRKA_POLICKA:
                sloupec = (mouse_x - offset_x) // VELIKOST_POLICKA
                radek = (mouse_y - offset_y) // VELIKOST_POLICKA
                if pole[radek][sloupec] is None:
                    pole[radek][sloupec] = aktualni_hrac
                    aktualni_hrac = HRAC_O if aktualni_hrac == HRAC_X else HRAC_X
    vykresli_pole()
    pygame.display.flip()
    hodiny.tick(60)