import pygame
import random

#inicializace pygame modulu
pygame.init()
SIRKA, VYSKA = 1000, 800 #nastavení rozměrů okna
CERNA = (0, 0, 0) #nastavení barvy pozadí
BILA = (255, 255, 255) #nastavení barvy textu
SEDA = (128, 128, 128) #nastavení barvy pro hover efekt
ZELENA = (0, 255, 0) #nastavení barvy správné odpovědi
CERVENA = (255, 0, 0) #nastavení barvy špatné odpovědi
aktualni_otazka = None #proměnná pro aktuální otázku
vybrana_odpoved = None #proměnná pro vybranou odpověď
vysledek = None #proměnná pro výsledek odpovědi
odpoved_recty = [] #seznam pro ukládání obdélníků odpovědí pro detekci kliknutí

okno = pygame.display.set_mode((SIRKA, VYSKA)) #vytvoření okna
pygame.display.set_caption("Quiz") #nastavení názvu okna
pismo = pygame.font.SysFont("Arial", 24) #nastavení fontu
bezi = True
hodiny = pygame.time.Clock() #nastavení hodin pro regulaci FPS

#otázky se budou generovat náhodně z tohoto seznamu
otazky = [
        {"otazka": "Jaké je hlavní město Francie?", "odpovedi": ["a) Paříž", "b) Londýn", "c) Berlín"], "spravna": 0},
        {"otazka": "Kdo je autorem knihy 'Harry Potter'?", "odpovedi": ["a) J.K. Rowlingová", "b) Stephen King", "c) George R.R. Martin"], "spravna": 0},
        {"otazka": "Jaký je největší oceán na světě?", "odpovedi": ["a) Atlantský oceán", "b) Indický oceán", "c) Tichý oceán"], "spravna": 2},
        {"otazka": "Kdo namaloval obraz 'Mona Lisa'?", "odpovedi": ["a) Leonardo da Vinci", "b) Pablo Picasso", "c) Vincent van Gogh"], "spravna": 0},
        {"otazka": "Jaká je nejvyšší hora na světě?", "odpovedi": ["a) Mount Everest", "b) K2", "c) Kangchenjunga"], "spravna": 0},
        {"otazka": "Kdo je prezidentem Spojených států?", "odpovedi": ["a) Joe Biden", "b) Donald Trump", "c) Barack Obama"], "spravna": 0},
        {"otazka": "Jaký je největší kontinent na světě?", "odpovedi": ["a) Afrika", "b) Asie", "c) Evropa"], "spravna": 1},
        {"otazka": "Kdo je autorem teorie relativity?", "odpovedi": ["Isaac Newton", "Albert Einstein", "Nikola Tesla"], "spravna": 1},
        {"otazka": "Jaký je největší savec na světě?", "odpovedi": ["a) Slon", "b) Velryba", "c) Žirafa"], "spravna": 1},
        {"otazka": "Kdo je autorem knihy 'Pán prstenů'?", "odpovedi": ["a) J.R.R. Tolkien", "b) C.S. Lewis", "c) George R.R. Martin"], "spravna": 0},
        {"otazka": "Jaký je největší ostrov na světě?", "odpovedi": ["a) Grónsko", "b) Madagaskar", "c) Borneo"], "spravna": 0},
        {"otazka": "Kdo je nejbohatší člověk na světě?", "odpovedi": ["a) Jeff Bezos", "b) Elon Musk", "c) Bill Gates"], "spravna": 1},
        {"otazka": "Jaká je největší řeka na světě?", "odpovedi": ["a) Amazonka", "b) Nil", "c) Mississippi"], "spravna": 0},
        {"otazka": "Který sport se hraje ve Wimbledonu?", "odpovedi": ["a) Fotbal", "b) Tenis", "c) Basketbal"], "spravna": 1},
        {"otazka": "Kolik hráčů má fotbalový tým na hřišti během hry?", "odpovedi": ["a) 11", "b) 9", "c) 7"], "spravna": 0},
        {"otazka": "Kdo je autorem knihy '1984'?", "odpovedi": ["a) George Orwell", "b) Aldous Huxley", "c) Ray Bradbury"], "spravna": 0},
        {"otazka": "Kdo objevil Ameriku?", "odpovedi": ["a) Christopher Columbus", "b) Vasco da Gama", "c) Ferdinand Magellan"], "spravna": 0},
        {"otazka": "Kde se konaly zimní olympijské hry v roce 2022?", "odpovedi": ["a) Peking", "b) Soči", "c) Vancouver"], "spravna": 0},
        {"otazka": "Kolik kol má draft NHL?", "odpovedi": ["a) 7", "b) 5", "c) 3"], "spravna": 0},
        {"otazka": "Kdo vytvořil seriál 'Simpsonovi'?", "odpovedi": ["a) Matt Groening", "b) Seth MacFarlane", "c) Trey Parker"], "spravna": 0},
        ]

#hlavní herní smyčka
while bezi:
    for udalost in pygame.event.get(): #zpracování událostí
        
        if udalost.type == pygame.KEYDOWN and udalost.key == pygame.K_SPACE:
            aktualni_otazka = random.choice(otazky)
        if udalost.type == pygame.QUIT: #pokud uživatel zavře okno
            bezi = False

    #vykreslení pozadí
    okno.fill(CERNA)

    #pokud není vybrána otázka, zobrazí se úvodní text
    if aktualni_otazka is None:
        text = pismo.render("Stiskněte mezerník pro start", True, BILA)
        okno.blit(text, (SIRKA // 2 - text.get_width() // 2, VYSKA // 2 - text.get_height() // 2))
    else:
        okno.fill(CERNA)

        #vykresli otázku a možnosti odpovědí
        text = pismo.render(aktualni_otazka["otazka"], True, BILA)
        okno.blit(text, (SIRKA // 2 - text.get_width() // 2, VYSKA // 2 - 50))

        odpoved_recty = []
        for i, odpoved in enumerate(aktualni_otazka["odpovedi"]):
            text = pismo.render(odpoved, True, BILA)
            rect = text.get_rect(center=(SIRKA // 2, VYSKA // 2 + i * 30))

        #hover efekt (kdy se najedete myší na odpověď)
            if rect.collidepoint(pygame.mouse.get_pos()):
                text = pismo.render(f" {odpoved}", True, SEDA)

            okno.blit(text, rect)
            odpoved_recty.append(rect)

    #aktualizace obrazovky
    pygame.display.flip()
    #regulace FPS
    hodiny.tick(60)
    #ukončení pygame
pygame.quit()