import pygame
import random

#inicializace pygame modulu
pygame.init()
SIRKA, VYSKA = 1000, 800 #nastavení rozměrů okna
CERNA = (0, 0, 0) #nastavení barvy pozadí
BILA = (255, 255, 255) #nastavení barvy textu
ZELENA = (0, 255, 0) #nastavení barvy správné odpovědi
CERVENA = (255, 0, 0) #nastavení barvy špatné odpovědi
aktualni_otazka = None #proměnná pro aktuální otázku

okno = pygame.display.set_mode((SIRKA, VYSKA)) #vytvoření okna
pygame.display.set_caption("Quiz") #nastavení názvu okna
pismo = pygame.font.SysFont("Arial", 24) #nastavení fontu
bezi = True
hodiny = pygame.time.Clock() #nastavení hodin pro regulaci FPS

#otázky se budou generovat náhodně z tohoto seznamu
otazky = [
        {"otazka": "Jaké je hlavní město Francie?", "odpovedi": ["Paříž", "Londýn", "Berlín"], "spravna": 0},
        {"otazka": "Kdo je autorem knihy 'Harry Potter'?", "odpovedi": ["J.K. Rowlingová", "Stephen King", "George R.R. Martin"], "spravna": 0},
        {"otazka": "Jaký je největší oceán na světě?", "odpovedi": ["Atlantský oceán", "Indický oceán", "Tichý oceán"], "spravna": 2},
        {"otazka": "Kdo namaloval obraz 'Mona Lisa'?", "odpovedi": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"], "spravna": 0},
        {"otazka": "Jaká je nejvyšší hora na světě?", "odpovedi": ["Mount Everest", "K2", "Kangchenjunga"], "spravna": 0},
        {"otazka": "Kdo je prezidentem Spojených států?", "odpovedi": ["Joe Biden", "Donald Trump", "Barack Obama"], "spravna": 0},
        {"otazka": "Jaký je největší kontinent na světě?", "odpovedi": ["Afrika", "Asie", "Evropa"], "spravna": 1},
        {"otazka": "Kdo je autorem teorie relativity?", "odpovedi": ["Isaac Newton", "Albert Einstein", "Nikola Tesla"], "spravna": 1},
        {"otazka": "Jaký je největší savec na světě?", "odpovedi": ["Slon", "Velryba", "Žirafa"], "spravna": 1},
        {"otazka": "Kdo je autorem knihy 'Pán prstenů'?", "odpovedi": ["J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin"], "spravna": 0},
        {"otazka": "Jaký je největší ostrov na světě?", "odpovedi": ["Grónsko", "Madagaskar", "Borneo"], "spravna": 0},
        {"otazka": "Kdo je nejbohatší člověk na světě?", "odpovedi": ["Jeff Bezos", "Elon Musk", "Bill Gates"], "spravna": 1},
        {"otazka": "Jaká je největší řeka na světě?", "odpovedi": ["Amazonka", "Nil", "Mississippi"], "spravna": 0},
        {"otazka": "Který sport se hraje ve Wimbledonu?", "odpovedi": ["Fotbal", "Tenis", "Basketbal"], "spravna": 1},
        {"otazka": "Kolik hráčů má fotbalový tým na hřišti během hry?", "odpovedi": ["11", "9", "7"], "spravna": 0},
        {"otazka": "Kdo je autorem knihy '1984'?", "odpovedi": ["George Orwell", "Aldous Huxley", "Ray Bradbury"], "spravna": 0},
        {"otazka": "Kdo objevil Ameriku?", "odpovedi": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan"], "spravna": 0},
        {"otazka": "Kde se konaly zimní olympijské hry v roce 2022?", "odpovedi": ["Peking", "Soči", "Vancouver"], "spravna": 0},
        {"otazka": "Kolik kol má draft NHL?", "odpovedi": ["7", "5", "3"], "spravna": 0},
        {"otazka": "Kdo vytvořil seriál 'Simpsonovi'?", "odpovedi": ["Matt Groening", "Seth MacFarlane", "Trey Parker"], "spravna": 0},
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

        #k otázce se vždy zobrazí 3 možnosti odpovědí, které hráč může vybrat stisknutím kláves 1, 2 nebo 3
        for i, odpoved in enumerate(aktualni_otazka["odpovedi"]):
            text = pismo.render(f"{i + 1}. {odpoved}", True, BILA)
            okno.blit(text, (SIRKA // 2 - text.get_width() // 2, VYSKA // 2 + (i + 1) * 30))

    #aktualizace obrazovky
    pygame.display.flip()
    #regulace FPS
    hodiny.tick(60)
    #ukončení pygame
pygame.quit()