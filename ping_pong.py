from random import random

import pygame
pygame.init() #inicializace pygame modulu
SIRKA, VYSKA = 1000, 800 #nastavení rozměrů okna
CERNA = (0, 0, 0) #Nastavení barev
BILA = (255, 255, 255)
velikost_obdelniku1 = 50
obdelnik1_x = SIRKA // 2 - velikost_obdelniku1 // 2
obdelnik1_y = VYSKA // 2 - velikost_obdelniku1 // 2
rychlost = 5
velikost_obdelniku2 = 50
obdelnik2_x = SIRKA // 2 - velikost_obdelniku2 // 2
obdelnik2_y = VYSKA // 2 - velikost_obdelniku2 // 2
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
        obdelnik1_y -= rychlost #posun obdelníku nahoru
    if klavesy[pygame.K_s]: #pokud je stisknuta klavesa S
            obdelnik1_y += rychlost #posun obdelníku dolů

        #obdelník1 se bude nacházet v levé polovině okna
    if obdelnik1_x < 0: #pokud je obdelník1 vlevo od levé hranice okna
        obdelnik1_x = 0 #nastavení x souřadnice obdelníku1 na 0
    if obdelnik1_x > SIRKA // 2 - velikost_obdelniku1: #pokud je obdelník1 vpravo od středu okna
        obdelnik1_x = SIRKA // 10 - velikost_obdelniku1 #nastavení x souřadnice obdelníku1 na pravou hranici levé poloviny okna
        #obdelník se nemůže pohybovat mimo okno
    if obdelnik1_y < 0: #pokud je obdelník1 nad horní hranicí okna
        obdelnik1_y = 0 #nastavení y souřadnice obdelníku1 na 0
    if obdelnik1_y > VYSKA - 100: #pokud je obdelník1 pod dolní hranicí okna
        obdelnik1_y = VYSKA - 100 #nastavení y souřadnice obdelníku1 na dolní hranici okna

    klavesy2 = pygame.key.get_pressed() #ziskani stisknutých kláves pro druhý obdelník
    if klavesy2[pygame.K_UP]: #pokud je stisknuta klavesa UP
        obdelnik2_y -= rychlost2 #posun druhého obdelníku nahoru
    if klavesy2[pygame.K_DOWN]: #pokud je stisknuta klavesa DOWN
        obdelnik2_y += rychlost2 #posun druhého obdelníku dolů

        #obdelník se nemůže pohybovat mimo okno
    if obdelnik2_y < 0: #pokud je obdelník2 nad horní hranicí okna
        obdelnik2_y = 0 #nastavení y souřadnice obdelníku2 na 0
    if obdelnik2_y > VYSKA - 100: #pokud je obdelník2 pod dolní hranicí okna
        obdelnik2_y = VYSKA - 100 #nastavení y souřadnice obdelníku2 na dolní hranici okna

        #obdelník2 se bude nacházet v pravé polovině okna
    if obdelnik2_x < SIRKA // 1: #pokud je obdelník2 vlevo od středu okna
        obdelnik2_x = SIRKA // 1 #nastavení x souřadnice obdelníku2 na střed okna
    if obdelnik2_x > SIRKA - velikost_obdelniku2: #pokud je obdelník2 vpravo od pravé hranice okna
        obdelnik2_x = SIRKA - velikost_obdelniku2 #nastavení x souřadnice obdelníku2 na pravou hranici okna

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

            #míček se odrazí od obdelníku1 a obdelníku2
        if (obdelnik1_x < micek_x < obdelnik1_x + 20 and obdelnik1_y < micek_y < obdelnik1_y + 100) or (obdelnik2_x < micek_x < obdelnik2_x + 20 and obdelnik2_y < micek_y < obdelnik2_y + 100): #pokud je míček uvnitř obdelníku1 nebo obdelníku2
            rychlost_micek_x = -rychlost_micek_x #změna směru pohybu míčku v ose x

        #vytvoření skóre pro oba hráče s počáteční hodnotou 0
        skore1 = pismo.render(f"Hráč 1: {body_hrace1}", True, BILA) #vytvoření textu pro skóre hráče 1
        skore2 = pismo.render(f"Hráč 2: {body_hrace2}", True, BILA) #vytvoření textu pro skóre hráče 2
        okno.blit(skore1, (140, 10)) #vykreslení skóre hráče 1 na obrazovku
        okno.blit(skore2, (SIRKA - 240, 10)) #vykreslení skóre hráče 2 na obrazovku

        #po získání 20 bodů jedním z hráčů se zobrazí zpráva o vítězství a hra poté napíše "Stiskněte klávesu R pro restartování hry"
        if body_hrace1 >= 20: #pokud hráč 1 získá 20 nebo více bodů
            vyhra1 = pismo.render("Hráč 1 vyhrál! Gratulujeme!", True, BILA) #vytvoření textu pro vítězství hráče 1
            restart = pismo.render("Stiskněte klávesu R pro restartování hry", True, BILA) #vytvoření textu pro restartování hry
        if body_hrace2 >= 20: #pokud hráč 2 získá 20 nebo více bodů
            vyhra2 = pismo.render("Hráč 2 vyhrál! Gratulujeme!", True, BILA) #vytvoření textu pro vítězství hráče 2
            restart = pismo.render("Stiskněte klávesu R pro restartování hry", True, BILA) #vytvoření textu pro restartování hry
        if body_hrace1 >= 20: #pokud hráč 1 získá 20 nebo více bodů
            okno.blit(vyhra1, (SIRKA // 2 - vyhra1.get_width() // 2, VYSKA // 4 - vyhra1.get_height() // 2 - 20)) #vykreslení zprávy o vítězství hráče 1 na obrazovku
            okno.blit(restart, (SIRKA // 2 - restart.get_width() // 2, VYSKA // 4 - restart.get_height() // 2 + 20)) #vykreslení zprávy o restartování hry na obrazovku
        if body_hrace2 >= 20: #pokud hráč 2 získá 20 nebo více bodů
            okno.blit(vyhra2, (SIRKA // 2 - vyhra2.get_width() // 2, VYSKA // 4 - vyhra2.get_height() // 2 - 20)) #vykreslení zprávy o vítězství hráče 2 na obrazovku
            okno.blit(restart, (SIRKA // 2 - restart.get_width() // 2, VYSKA // 4 - restart.get_height() // 2 + 20)) #vykreslení zprávy o restartování hry na obrazovku
            #pokud je po ukázání zprávy o vítězství stisknuta klávesa R, hra se restartuje a skóre se resetuje na 0
        if (body_hrace1 >= 20 and klavesy[pygame.K_r]) or (body_hrace2 >= 20 and klavesy[pygame.K_r]): #pokud je stisknuta klavesa R
            body_hrace1 = 0 #reset skóre hráče 1 na 0
            body_hrace2 = 0 #reset skóre hráče 2 na 0
            micek_x = SIRKA // 2 #reset pozice míčku v ose x
            micek_y = VYSKA // 2 #reset pozice míčku v ose y
            rychlost_micek_x = 0 #reset rychlosti míčku v ose x
            rychlost_micek_y = 0 #reset rychlosti míčku v ose y
            #když jeden z hráčů zvítězí, nebude možné pohybovat obdelníkem a ani míčkem ale objeví se zpráva o vítězství a zpráva o restartování hry, dokud není stisknuta klávesa R pro restartování hry
        if body_hrace1 >= 20 or body_hrace2 >= 20: #pokud jeden z hráčů získá 20 nebo více bodů
            obdelnik1_x = SIRKA // 2 - velikost_obdelniku1 // 2 #nastavení x souřadnice obdelníku1 na střed okna
            obdelnik1_y = VYSKA // 2 - velikost_obdelniku1 // 2 #nastavení y souřadnice obdelníku1 na střed okna
            obdelnik2_x = SIRKA // 2 - velikost_obdelniku2 // 2 #nastavení x souřadnice obdelníku2 na střed okna
            obdelnik2_y = VYSKA // 2 - velikost_obdelniku2 // 2 #nastavení y souřadnice obdelníku2 na střed okna
            #po vítězství jednoho z hráčů nebude možné pohybovat míčkem, po stisknutí klávesy R pro restartování hry se míček vrátí do středu okna a nebude se pohybovat, dokud není stisknut mezerník pro rozpohybování míčku
            rychlost_micek_x = 0 #nastavení rychlosti míčku v ose x na 0
            rychlost_micek_y = 0 #nastavení rychlosti míčku v ose y na 0

                #po získání 10 bodů jedním z hráčů se zobrazí zpráva "Hráč 1 získal 10 bodů!" nebo "Hráč 2 získal 10 bodů!" v závislosti na tom, který hráč získal 10 bodů
        if body_hrace1 == 10: #pokud hráč 1 získá 10 bodů
            deset_bodu1 = pismo.render("Hráč 1 získal 10 bodů!", True, BILA) #vytvoření textu pro zprávu o získání 10 bodů hráčem 1
            okno.blit(deset_bodu1, (SIRKA // 2 - deset_bodu1.get_width() // 2, VYSKA // 4 - deset_bodu1.get_height() // 2)) #vykreslení zprávy o získání 10 bodů hráčem 1 na obrazovku
        if body_hrace2 == 10: #pokud hráč 2 získá 10 bodů
            deset_bodu2 = pismo.render("Hráč 2 získal 10 bodů!", True, BILA) #vytvoření textu pro zprávu o získání 10 bodů hráčem 2
            okno.blit(deset_bodu2, (SIRKA // 2 - deset_bodu2.get_width() // 2, VYSKA // 4 - deset_bodu2.get_height() // 2)) #vykreslení zprávy o získání 10 bodů hráčem 2 na obrazovku

            #po odrazu míčku od obdelníku se míček zrychlí +1 v ose x a +1 v ose y
        if (obdelnik1_x < micek_x < obdelnik1_x + 20 and obdelnik1_y < micek_y < obdelnik1_y + 100) or (obdelnik2_x < micek_x < obdelnik2_x + 20 and obdelnik2_y < micek_y < obdelnik2_y + 100): #pokud je míček uvnitř obdelníku1 nebo obdelníku2
            if rychlost_micek_x > 0: #pokud se míček pohybuje vpravo
                rychlost_micek_x += 1 #zvýšení rychlosti míčku v ose x o 1
            else: #pokud se míček pohybuje vlevo
                rychlost_micek_x -= 1 #snížení rychlosti míčku v ose x o 1
            if rychlost_micek_y > 0: #pokud se míček pohybuje dolů
                rychlost_micek_y += 1 #zvýšení rychlosti míčku v ose y o 1
            else: #pokud se míček pohybuje nahoru
                rychlost_micek_y -= 1 #snížení rychlosti míčku v ose y o 1

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

    pygame.draw.rect(okno, BILA, (obdelnik1_x, obdelnik1_y, 20, 100)) #vykreslení prvního čtverce
    pygame.draw.rect(okno, BILA, (obdelnik2_x, obdelnik2_y, 20, 100)) #vykreslení druhého čtverce
    #regulace FPS
    hodiny.tick(60) #nastavení FPS na 60
pygame.quit() #ukončení pygame