from random import random

import pygame
pygame.init() #inicializace pygame modulu
SIRKA, VYSKA = 1000, 800 #nastavení rozměrů okna
CERNA = (0, 0, 0) #Nastavení barev
BILA = (255, 255, 255)
velikost_ctverce1 = 50
ctverec1_x = SIRKA // 2 - velikost_ctverce1 // 2
ctverec1_y = VYSKA // 2 - velikost_ctverce1 // 2
rychlost = 5
velikost_ctverce2 = 50
ctverec2_x = SIRKA // 2 - velikost_ctverce2 // 2
ctverec2_y = VYSKA // 2 - velikost_ctverce2 // 2
rychlost2 = 5
micek_x = SIRKA // 2
micek_y = VYSKA // 2
rychlost_micek_x = 5
rychlost_micek_y = 5
body_hrace1 = 0
body_hrace2 = 0
okno = pygame.display.set_mode((SIRKA, VYSKA))
 #nastavení názvu okna velikosti okna
pygame.display.set_caption("Ping Pong") #nastavení názvu okna
pismo = pygame.font.SysFont("Arial", 24) #nastavení fontu a velikosti písma
bezi = True
hodiny = pygame.time.Clock() #nastavení hodin pro reulaci FPS
while bezi:
    for udalost in pygame.event.get(): #ziskani všech udalosti
        if udalost.type == pygame.QUIT: #pokud uživatel zavře okno
            bezi = False #ukončení smyčky
    klavesy = pygame.key.get_pressed() #ziskani stisknutých kláves
    if klavesy[pygame.K_w]: #pokud je stisknuta klavesa W
        ctverec1_y -= rychlost #posun čtverce nahoru
    if klavesy[pygame.K_s]: #pokud je stisknuta klavesa S
            ctverec1_y += rychlost #posun čtverce dolů

        #čtverec1 se bude nacházet v levé polovině okna
    if ctverec1_x < 0: #pokud je čtverec1 vlevo od levé hranice okna
        ctverec1_x = 0 #nastavení x souřadnice čtverce1 na 0
    if ctverec1_x > SIRKA // 2 - velikost_ctverce1: #pokud je čtverec1 vpravo od středu okna
        ctverec1_x = SIRKA // 10 - velikost_ctverce1 #nastavení x souřadnice čtverce1 na pravou hranici levé poloviny okna
        #čtverec se nemůže pohybovat mimo okno
    if ctverec1_y < 0: #pokud je čtverec1 nad horní hranicí okna
        ctverec1_y = 0 #nastavení y souřadnice čtverce1 na 0
    if ctverec1_y > VYSKA - velikost_ctverce1: #pokud je čtverec1 pod dolní hranicí okna
        ctverec1_y = VYSKA - velikost_ctverce1 #nastavení y souřadnice čtverce1 na dolní hranici okna
            
    klavesy2 = pygame.key.get_pressed() #ziskani stisknutých kláves pro druhý čtverec
    if klavesy2[pygame.K_UP]: #pokud je stisknuta klavesa UP
        ctverec2_y -= rychlost2 #posun druhého čtverce nahoru
    if klavesy2[pygame.K_DOWN]: #pokud je stisknuta klavesa DOWN
        ctverec2_y += rychlost2 #posun druhého čtverce dolů
        #čtverec se nemůže pohybovat mimo okno
    if ctverec2_y < 0: #pokud je čtverec2 nad horní hranicí okna
        ctverec2_y = 0 #nastavení y souřadnice čtverce2 na 0
    if ctverec2_y > VYSKA - velikost_ctverce2: #pokud je čtverec2 pod dolní hranicí okna
        ctverec2_y = VYSKA - velikost_ctverce2 #nastavení y souřadnice čtverce2 na dolní hranici okna

        #čtverec2 se bude nacházet v pravé polovině okna
    if ctverec2_x < SIRKA // 1: #pokud je čtverec2 vlevo od středu okna
        ctverec2_x = SIRKA // 1 #nastavení x souřadnice čtverce2 na střed okna
    if ctverec2_x > SIRKA - velikost_ctverce2: #pokud je čtverec2 vpravo od pravé hranice okna
        ctverec2_x = SIRKA - velikost_ctverce2 #nastavení x souřadnice čtverce2 na pravou hranici okna

        #míček se bude nacházet uprostřed okna
        micek_x += rychlost_micek_x #posun míčku v ose x
        micek_y += rychlost_micek_y #posun míčku v ose y
        pygame.draw.circle(okno, BILA, (micek_x, micek_y), 15) #vykreslení míčku jako kruhu s poloměrem 15
        #odraz míčku od horní a dolní hranice okna
        if micek_y < 0 or micek_y > VYSKA: #pokud je míček nad horní hranicí okna nebo pod dolní hranicí okna
            rychlost_micek_y = -rychlost_micek_y #změna směru pohybu míčku v ose y
            #když míček propadne do levé nebo pravé poloviny okna, míček se vrátí do středu okna a nebude se pohybovat
        if micek_x < 0 or micek_x > SIRKA: #pokud je míček vlevo od levé hranice okna nebo vpravo od pravé hranice okna
            if micek_x < 0: #pokud je míček vlevo od levé hranice okna
                body_hrace2 += 1 #přidání bodu hráči 2
            else: #pokud je míček vpravo od pravé hranice okna
                body_hrace1 += 1 #přidání bodu hráči 1
            micek_x = SIRKA // 2 #nastavení x souřadnice míčku na střed okna
            micek_y = VYSKA // 2 #nastavení y souřadnice míčku na střed okna
            rychlost_micek_x = 0 #nastavení rychlosti míčku v ose x na 0
            rychlost_micek_y = 0 #nastavení rychlosti míčku v ose y na 0

            #rozpohybování míčku, po jeho resetování pomocí klávesy space
        if klavesy[pygame.K_SPACE]: #pokud je stisknuta klavesa SPACE
            rychlost_micek_x = 5 #nastavení rychlosti míčku v ose x na 5
            rychlost_micek_y = 5 #nastavení rychlosti míčku v ose y na 5

            #míček se odrazí od čtverce1 a čtverce2
        if (ctverec1_x < micek_x < ctverec1_x + velikost_ctverce1 and ctverec1_y < micek_y < ctverec1_y + velikost_ctverce1) or (ctverec2_x < micek_x < ctverec2_x + velikost_ctverce2 and ctverec2_y < micek_y < ctverec2_y + velikost_ctverce2): #pokud je míček uvnitř čtverce1 nebo čtverce2
            rychlost_micek_x = -rychlost_micek_x #změna směru pohybu míčku v ose x

        #vytvoření skóre pro oba hráče s počáteční hodnotou 0
        skore1 = pismo.render(f"Hráč 1: {body_hrace1}", True, BILA) #vytvoření textu pro skóre hráče 1
        skore2 = pismo.render(f"Hráč 2: {body_hrace2}", True, BILA) #vytvoření textu pro skóre hráče 2
        okno.blit(skore1, (140, 10)) #vykreslení skóre hráče 1 na obrazovku
        okno.blit(skore2, (SIRKA - 240, 10)) #vykreslení skóre hráče 2 na obrazovku

        #po získání 20 bodů jedním z hráčů se zobrazí zpráva o vítězství a hra poté napíše "Stiskněte mezerník pro restartování hry"
        if body_hrace1 >= 20: #pokud hráč 1 získá 20 nebo více bodů
            vyhra1 = pismo.render("Hráč 1 vyhrál! Gratulujeme!", True, BILA) #vytvoření textu pro vítězství hráče 1
            restart = pismo.render("Stiskněte mezerník pro restartování hry", True, BILA) #vytvoření textu pro restartování hry
        if body_hrace2 >= 20: #pokud hráč 2 získá 20 nebo více bodů
            vyhra2 = pismo.render("Hráč 2 vyhrál! Gratulujeme!", True, BILA) #vytvoření textu pro vítězství hráče 2
            restart = pismo.render("Stiskněte mezerník pro restartování hry", True, BILA) #vytvoření textu pro restartování hry
        if body_hrace1 >= 20: #pokud hráč 1 získá 20 nebo více bodů
            okno.blit(vyhra1, (SIRKA // 2 - vyhra1.get_width() // 2, VYSKA // 2 - vyhra1.get_height() // 2 - 20)) #vykreslení zprávy o vítězství hráče 1 na obrazovku
            okno.blit(restart, (SIRKA // 2 - restart.get_width() // 2, VYSKA // 2 - restart.get_height() // 2 + 20)) #vykreslení zprávy o restartování hry na obrazovku
        if body_hrace2 >= 20: #pokud hráč 2 získá 20 nebo více bodů
            okno.blit(vyhra2, (SIRKA // 2 - vyhra2.get_width() // 2, VYSKA // 2 - vyhra2.get_height() // 2 - 20)) #vykreslení zprávy o vítězství hráče 2 na obrazovku
            okno.blit(restart, (SIRKA // 2 - restart.get_width() // 2, VYSKA // 2 - restart.get_height() // 2 + 20)) #vykreslení zprávy o restartování hry na obrazovku
            pygame.display.flip() #aktualizace obrazovky


        #vytvoření čáry uprostřed okna
        pygame.draw.line(okno, BILA, (SIRKA // 2, 0), (SIRKA // 2, VYSKA), 5) #vykreslení čáry uprostřed okna
        #vytvoření jedné postranní čáry vlevo a jedné postranní čáry vpravo
        pygame.draw.line(okno, BILA, (SIRKA // 50, 0), (SIRKA // 50, VYSKA), 5) #vykreslení postranní čáry vlevo
        pygame.draw.line(okno, BILA, (SIRKA - SIRKA // 50, 0), (SIRKA - SIRKA // 50, VYSKA), 5) #vykreslení postranní čáry vpravo
        #vytvoření středového kruhu
        pygame.draw.circle(okno, BILA, (SIRKA // 2, VYSKA // 2), 75, 5) #vykreslení středového kruhu s poloměrem 75 a tloušťkou čáry 5
        pygame.display.flip() #aktualizace obrazovky

        #vykreslení pozadí
        okno.fill(CERNA) #vyplnění pozadí černou barvou

    pygame.draw.rect(okno, BILA, (ctverec1_x, ctverec1_y, velikost_ctverce1, velikost_ctverce1)) #vykreslení prvního čtverce
    pygame.draw.rect(okno, BILA, (ctverec2_x, ctverec2_y, velikost_ctverce2, velikost_ctverce2)) #vykreslení druhého čtverce
    #regulace FPS
    hodiny.tick(60) #nastavení FPS na 60
pygame.quit() #ukončení pygame