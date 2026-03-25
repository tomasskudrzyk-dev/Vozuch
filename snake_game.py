import pygame
import random

# inicializace pygame modulu
pygame.init()
SIRKA, VYSKA = 1000, 800 #nastavení rozměrů okna
CERNA = (0, 0, 0) #nastavení barvy pozadí
BILA = (255, 255, 255) #nastavení barvy hada a jídla
CERVENA = (255, 0, 0) #nastavení barvy jídla
ZELENA = (0, 255, 0) #nastavení barvy hada
velikost_ctverce = 20 #nastavení velikosti ctverce, který bude představovat hada
had_x = SIRKA // 2 - velikost_ctverce // 2
had_y = VYSKA // 2 - velikost_ctverce // 2
rychlost = 2 #nastavení rychlosti pohybu hada
velikost_jidla = 12 #nastavení velikosti jídla
jidlo_x = SIRKA // 2 - velikost_jidla // 2
jidlo_y = VYSKA // 2 - velikost_jidla // 2

okno = pygame.display.set_mode((SIRKA, VYSKA)) #vytvoření okna
pygame.display.set_caption("Snake game") #nastavení názvu okna
pismo = pygame.font.SysFont("Arial", 24) #nastavení fontu
bezi = True
hodiny = pygame.time.Clock() #nastavení hodin pro regulaci FPS
while bezi:
    for udalost in pygame.event.get(): #získání všch událostí
        if udalost.type == pygame.QUIT: #pokud uživatel zavře okno
            bezi = False #ukončení smyčky
    klavesy = pygame.key.get_pressed() #získání stisknutých kláves
    if klavesy[pygame.K_w]: #pokud je stisknuta klávesa W
        had_y -= rychlost #posun hada nahoru
    if klavesy[pygame.K_s]: #pokud je stisknuta klávesa S
        had_y += rychlost #posun hada dolů
    if klavesy[pygame.K_a]: #pokud je stisknuta klávesa A
        had_x -= rychlost #posun hada doleva
    if klavesy[pygame.K_d]: #pokud je stisknuta klávesa D
        had_x += rychlost #posun hada doprava

        #hráč se může pohybovat pouze v rámci okna
    if had_x < 0: #pokud se had dostane mimo levou stranu okna
        had_x = 0 #nastavení pozice hada na levý okraj
    if had_x > SIRKA - velikost_ctverce: #pokud se had dostane mimo pravou stranu okna
        had_x = SIRKA - velikost_ctverce #nastavení pozice hada na pravý okraj
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

    pygame.display.flip() #aktualizace obrazovky

        #vykreslení pozadí
    okno.fill(CERNA) #vyplnění pozadí černou barvou
    #vykreslení hada
    pygame.draw.rect(okno, ZELENA, (had_x, had_y, velikost_ctverce, velikost_ctverce)) #vykreslení hada jako zeleného čtverce
    #vykreslení jídla
    pygame.draw.rect(okno, CERVENA, (jidlo_x, jidlo_y, velikost_jidla, velikost_jidla)) #vykreslení jídla jako červeného čtverce

    #regulace FPS
    hodiny.tick(60) #nastavení FPS na 60
pygame.quit() #ukončení pygame modulu