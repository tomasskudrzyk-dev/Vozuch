import pygame
import random

# inicializace pygame modulu
pygame.init()
SIRKA, VYSKA = 1000, 800 #nastavení rozměrů okna
CERNA = (0, 0, 0) #nastavení barvy pozadí
BILA = (255, 255, 255) #nastavení barvy hada a jídla
SEDA = (128, 128, 128) #nastavení barvy mřížky
CERVENA = (255, 0, 0) #nastavení barvy jídla
ZELENA = (0, 255, 0) #nastavení barvy hada
velikost_ctverce = 20 #nastavení velikosti ctverce, který bude představovat hada
had_x = SIRKA // 2 - velikost_ctverce // 2
had_y = VYSKA // 2 - velikost_ctverce // 2
rychlost = velikost_ctverce #nastavení rychlosti pohybu hada
velikost_jidla = velikost_ctverce #nastavení velikosti jídla
jidlo_x = SIRKA // 2 - velikost_jidla // 2
jidlo_y = VYSKA // 2 - velikost_jidla // 2
skore = 0 #nastavení počátečního skóre
had = [(had_x, had_y)] #vytvoření seznamu pro uložení pozic hada
smer = (1, 0)

okno = pygame.display.set_mode((SIRKA, VYSKA)) #vytvoření okna
pygame.display.set_caption("Snake game") #nastavení názvu okna
pismo = pygame.font.SysFont("Arial", 24) #nastavení fontu
bezi = True
hodiny = pygame.time.Clock() #nastavení hodin pro regulaci FPS
while bezi:
    for udalost in pygame.event.get(): #získání všch událostí
        if udalost.type == pygame.QUIT: #pokud uživatel zavře okno
            bezi = False #ukončení smyčky
        elif udalost.type == pygame.KEYDOWN: #pokud je stisknuta klávesa
            if udalost.key == pygame.K_w and smer != (0, -1): #pokud je stisknuta klávesa w had se pohybuje nahoru
                smer = (0, -1) #nastavení směru pohybu nahoru
            elif udalost.key == pygame.K_a and smer != (-1, 0): #pokud je stisknuta klávesa a had se pohybuje doleva
                smer = (-1, 0) #nastavení směru pohybu doleva
            elif udalost.key == pygame.K_s and smer != (0, 1): #pokud je stisknuta klávesa s a had se pohybuje dolů
                smer = (0, 1) #nastavení směru pohybu dolů
            elif udalost.key == pygame.K_d and smer != (1, 0): #pokud je stisknuta klávesa d a had se pohybuje doprava
                smer = (1, 0) #nastavení směru pohybu doprava

    had_x += smer[0] * rychlost #aktualizace pozice hada na x-ové ose
    had_y += smer[1] * rychlost #aktualizace pozice hada na y-ové ose
    had.insert(0, (had_x, had_y)) #přidání nové pozice hada na začátek seznamu

        #hráč se může pohybovat pouze v rámci okna
    if had_x < 0 or had_x > SIRKA - velikost_ctverce or had_y < 0 or had_y > VYSKA - velikost_ctverce:
    #pokud se had dotkne okraje okna bude na obrazovce zpráva o konečném skóre a o možnosti restartu hry pomocí klávesy R
        okno.fill(CERNA) #vyplnění pozadí černou barvou
        text = pismo.render(f"Konec hry! Skóre: {skore}. Stiskněte R pro restart.", True, BILA) #vytvoření textu pro zobrazení konečného skóre a možnosti restartu
        okno.blit(text, (SIRKA // 2 - text.get_width() // 2, VYSKA // 2 - text.get_height() // 2)) #zobrazení textu na obrazovce
        pygame.display.flip() #aktualizace obrazovky

    #po zobrazení zprávy o konci hry čeká na stisknutí klávesy R pro restart hry
        while True:
            for udalost in pygame.event.get(): #získání všech událostí
                if udalost.type == pygame.QUIT: #pokud uživatel zavře okno
                    pygame.quit() #ukončení pygame modulu
                    exit() #ukončení programu
                elif udalost.type == pygame.KEYDOWN: #pokud je stisknuta klávesa
                    if udalost.key == pygame.K_r: #pokud je stisknuta klávesa R
                        had_x = SIRKA // 2 - velikost_ctverce // 2 #nastavení pozice hada na x-ové ose pro restart hry
                        had_y = VYSKA // 2 - velikost_ctverce // 2 #nastavení pozice hada na y-ové ose pro restart hry
                        jidlo_x = SIRKA // 2 - velikost_jidla // 2 #nastavení pozice jídla na x-ové ose pro restart hry
                        jidlo_y = VYSKA // 2 - velikost_jidla // 2 #nastavení pozice jídla na y-ové ose pro restart hry
                        skore = 0 #resetování skóre pro restart hry
                        had = [(had_x, had_y)] #resetování pozic hada pro restart hry
                        smer = (1, 0) #resetování směru pohybu pro restart hry
                        break #ukončení vnitřní smyčky a pokračování v hlavní smyčce

            #když hráč stiskne klávesu R, hra se restartuje a začne znovu od začátku s původním nastavením
            if udalost.type == pygame.KEYDOWN and udalost.key == pygame.K_r:
                break #ukončení vnitřní smyčky a pokračování v hlavní smyčce

            #aktualizace obrazovky
        pygame.display.flip() #aktualizace obrazovky

    if had_y < 0: #pokud se had dostane mimo horní stranu okna
        had_y = 0 #nastavení pozice hada na horní okraj
    if had_y > VYSKA - velikost_ctverce: #pokud se had dostane mimo dolní stranu okna
        had_y = VYSKA - velikost_ctverce #nastavení pozice hada na dolní okraj

        #vytvoření kolize hada sám se sebou
    if (had_x, had_y) in had[1:]: #pokud se had dotkne sám sebe (kromě hlavy)
        okno.fill(CERNA) #vyplnění pozadí černou barvou
        text = pismo.render(f"Konec hry! Skóre: {skore}. Stiskněte R pro restart.", True, BILA) #vytvoření textu pro zobrazení konečného skóre a možnosti restartu
        okno.blit(text, (SIRKA // 2 - text.get_width() // 2, VYSKA // 2 - text.get_height() // 2)) #zobrazení textu na obrazovce
        pygame.display.flip() #aktualizace obrazovky

    #po zobrazení zprávy o konci hry čeká na stisknutí klávesy R pro restart hry
        while True:
            for udalost in pygame.event.get(): #získání všech událostí
                if udalost.type == pygame.QUIT: #pokud uživatel zavře okno
                    pygame.quit() #ukončení pygame modulu
                    exit() #ukončení programu
                elif udalost.type == pygame.KEYDOWN: #pokud je stisknuta klávesa
                    if udalost.key == pygame.K_r: #pokud je stisknuta klávesa R
                        had_x = SIRKA // 2 - velikost_ctverce // 2 #nastavení pozice hada na x-ové ose pro restart hry
                        had_y = VYSKA // 2 - velikost_ctverce // 2 #nastavení pozice hada na y-ové ose pro restart hry
                        jidlo_x = SIRKA // 2 - velikost_jidla // 2 #nastavení pozice jídla na x-ové ose pro restart hry
                        jidlo_y = VYSKA // 2 - velikost_jidla // 2 #nastavení pozice jídla na y-ové ose pro restart hry
                        skore = 0 #resetování skóre pro restart hry
                        had = [(had_x, had_y)] #resetování pozic hada pro restart hry
                        smer = (1, 0) #resetování směru pohybu pro restart hry
                        break #ukončení vnitřní smyčky a pokračování v hlavní smyčce
            #když hráč stiskne klávesu R, hra se restartuje a začne znovu od začátku s původním nastavením
            if udalost.type == pygame.KEYDOWN and udalost.key == pygame.K_r:
                break #ukončení vnitřní smyčky a pokračování v hlavní smyčce

    if had_y < 0: #pokud se had dostane mimo horní stranu okna
        had_y = 0 #nastavení pozice hada na horní okraj
    if had_y > VYSKA - velikost_ctverce: #pokud se had dostane mimo dolní stranu okna
        had_y = VYSKA - velikost_ctverce #nastavení pozice hada na dolní okraj


        #vytvoření kolize hada s jídlem
    if (had_x < jidlo_x + velikost_jidla and had_x + velikost_ctverce > jidlo_x and
        had_y < jidlo_y + velikost_jidla and
        had_y + velikost_ctverce > jidlo_y):
        jidlo_x = random.randint(0, SIRKA - velikost_jidla) #náhodné umístění jídla na x-ové ose
        jidlo_y = random.randint(0, VYSKA - velikost_jidla) #náhodné umístění jídla na y-ové ose

        skore += 1 #zvýšení skóre o 1
    else:
        had.pop() #odstranění poslední pozice hada, pokud nedošlo ke kolizi s jídlem

    pygame.display.flip() #aktualizace obrazovky

        #vykreslení pozadí
    okno.fill(CERNA) #vyplnění pozadí černou barvou


    #vykreslení skóre
    text = pismo.render(f"Skóre: {skore}", True, BILA) #vytvoření textu pro zobrazení skóre
    okno.blit(text, (10, 10)) #zobrazení textu na obrazovce

    #vykreslení hada
    for cast in had:
        pygame.draw.rect(okno, ZELENA, (cast[0], cast[1], velikost_ctverce, velikost_ctverce)) #vykreslení hada jako zelených čtverců
    #vykreslení jídla
    pygame.draw.rect(okno, CERVENA, (jidlo_x, jidlo_y, velikost_jidla, velikost_jidla)) #vykreslení jídla jako červeného čtverce

    #regulace FPS
    hodiny.tick(10) #nastavení FPS na 10
pygame.quit() #ukončení pygame modulu