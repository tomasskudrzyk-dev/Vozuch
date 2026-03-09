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
            
    klavesy2 = pygame.key.get_pressed() #ziskani stisknutých kláves pro druhý čtverec
    if klavesy2[pygame.K_UP]: #pokud je stisknuta klavesa UP
        ctverec2_y -= rychlost2 #posun druhého čtverce nahoru
    if klavesy2[pygame.K_DOWN]: #pokud je stisknuta klavesa DOWN
        ctverec2_y += rychlost2 #posun druhého čtverce dolů

        #čtverec2 se bude nacházet v pravé polovině okna
    if ctverec2_x < SIRKA // 1: #pokud je čtverec2 vlevo od středu okna
        ctverec2_x = SIRKA // 1 #nastavení x souřadnice čtverce2 na střed okna
    if ctverec2_x > SIRKA - velikost_ctverce2: #pokud je čtverec2 vpravo od pravé hranice okna
        ctverec2_x = SIRKA - velikost_ctverce2 #nastavení x souřadnice čtverce2 na pravou hranici okna


        #vykreslení pozadí
        okno.fill(CERNA) #vyplnění pozadí černou barvou

    pygame.draw.rect(okno, BILA, (ctverec1_x, ctverec1_y, velikost_ctverce1, velikost_ctverce1)) #vykreslení prvního čtverce
    pygame.draw.rect(okno, BILA, (ctverec2_x, ctverec2_y, velikost_ctverce2, velikost_ctverce2)) #vykreslení druhého čtverce
    #regulace FPS
    hodiny.tick(60) #nastavení FPS na 60
    pygame.display.flip() #aktualizace obrazovky
    #vykrerslení okna
pygame.quit() #ukončení pygame
