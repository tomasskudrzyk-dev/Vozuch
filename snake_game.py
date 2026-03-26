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
rychlost = 2 #nastavení rychlosti pohybu hada
velikost_jidla = 12 #nastavení velikosti jídla
jidlo_x = SIRKA // 2 - velikost_jidla // 2
jidlo_y = VYSKA // 2 - velikost_jidla // 2
skore = 0 #nastavení počátečního skóre
had = [(had_x, had_y)] #vytvoření seznamu pro uložení pozic hada

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

    had.insert(0, (had_x, had_y)) #přidání nové pozice hada na začátek seznamu

        #hráč se může pohybovat pouze v rámci okna
    if had_x < 0 or had_x > SIRKA - velikost_ctverce or had_y < 0 or had_y > VYSKA - velikost_ctverce:
    #pokud se had dotkne okraje okna bude na obrazovce zpráva o konečném skóre a o možnosti restartu hry pomocí klávesy R
        okno.fill(CERNA) #vyplnění pozadí černou barvou
        text = pismo.render(f"Konec hry! Skóre: {skore}. Stiskněte R pro restart.", True, BILA) #vytvoření textu pro zobrazení konečného skóre a možnosti restartu
        okno.blit(text, (SIRKA // 2 - text.get_width() // 2, VYSKA // 2 - text.get_height() // 2)) #zobrazení textu na obrazovce
        pygame.display.flip() #aktualizace obrazovky

    if had_y < 0: #pokud se had dostane mimo horní stranu okna
        had_y = 0 #nastavení pozice hada na horní okraj
    if had_y > VYSKA - velikost_ctverce: #pokud se had dostane mimo dolní stranu okna
        had_y = VYSKA - velikost_ctverce #nastavení pozice hada na dolní okraj

        #had se rozpohybuje do toho směru. který byl naposledy stisknut a bude pokračovat v pohybu, dokud nebude stisknuta jiná klávesa
        if klavesy[pygame.K_w]: #pokud je stisknuta klávesa W
            had_y -= rychlost #posun hada nahoru
        if klavesy[pygame.K_s]: #pokud je stisknuta klávesa S
            had_y += rychlost #posun hada dolů
        if klavesy[pygame.K_a]: #pokud je stisknuta klávesa A
            had_x -= rychlost #posun hada doleva
        if klavesy[pygame.K_d]: #pokud je stisknuta klávesa D
            had_x += rychlost #posun hada doprava

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
    hodiny.tick(60) #nastavení FPS na 60
pygame.quit() #ukončení pygame modulu