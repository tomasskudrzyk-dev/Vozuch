import pygame
import random

#inicializace pygame modulu
pygame.init()
SIRKA, VYSKA = 1000, 800 #nastavení rozměrů okna
CERNA = (0, 0, 0) #nastavení barvy pozadí
BILA = (255, 255, 255) #nastavení barvy textu
ZELENA = (0, 255, 0) #nastavení barvy správné odpovědi
CERVENA = (255, 0, 0) #nastavení barvy špatné odpovědi

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
    {"otázka": "Kdo je nejbohatší člověk na světě?", "odpovedi": ["Jeff Bezos", "Elon Musk", "Bill Gates"], "spravna": 1},
    {"otázka": "Jaká je největší řeka na světě?", "odpovedi": ["Amazonka", "Nil", "Yangtze"], "spravna": 0},
    {"otázka": "Který sport se hraje ve Wimbledonu?", "odpovedi": ["Fotbal", "Tenis", "Basketbal"], "spravna": 1},
    {"otázka": "Kolik hráčů má fotbalový tým na hřišti během hry?", "odpovedi": ["11", "9", "7"], "spravna": 0},
]

