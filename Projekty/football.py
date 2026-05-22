import pygame
import sys
import random

pygame.init()  # Inicializace pygame modulu
hodiny = pygame.time.Clock()
# Nastavení rozměrů okna
SIRKA, VYSKA = 1000, 800
# Vytvoření okna
okno = pygame.display.set_mode((SIRKA, VYSKA))
# Nastavení názvu okna
pygame.display.set_caption("Fotbal")
pismo = pygame.font.SysFont("Arial", 24)
pismo_maly = pygame.font.SysFont("Arial", 18)
# Nastavení barev
BILA = (255, 255, 255)
SEDA = (128, 128, 128)
CERNA = (0, 0, 0)
CERVENA = (255, 0, 0)
MODRA = (0, 0, 255)
ZELENA = (0, 255, 0)
TMAVE_ZELENA = (0, 100, 0)

# Pozadí (tráva)
pozadi = pygame.Surface((SIRKA, VYSKA))
pozadi.fill(TMAVE_ZELENA)

def draw_goal(surface, x, y, width, height, frame_color, net_color):
    pygame.draw.rect(surface, frame_color, (x, y, width, height), 5)
    # síť v brance
    for i in range(1, 6):
        x_offset = i * (width // 6)
        y_offset = i * (height // 6)
        pygame.draw.line(surface, net_color, (x + x_offset, y), (x + x_offset, y + height), 1)
        pygame.draw.line(surface, net_color, (x, y + y_offset), (x + width, y + y_offset), 1)

def draw_field(surface):
    surface.blit(pozadi, (0, 0))
    pygame.draw.rect(surface, BILA, (50, 50, 900, 700), 5)  # Hřiště
    pygame.draw.line(surface, BILA, (SIRKA // 2, 50), (SIRKA // 2, 750), 5)  # Středová čára
    pygame.draw.circle(surface, BILA, (SIRKA // 2, VYSKA // 2), 50, 5)  # Středový kruh
    # Vápna
    pygame.draw.rect(surface, BILA, (50, 250, 150, 300), 5)
    pygame.draw.rect(surface, BILA, (800, 250, 150, 300), 5)
    pygame.draw.rect(surface, BILA, (50, 325, 75, 150), 5)
    pygame.draw.rect(surface, BILA, (875, 325, 75, 150), 5)
    # Branky
    draw_goal(surface, 50, 300, 50, 200, BILA, SEDA)
    draw_goal(surface, 900, 300, 50, 200, BILA, SEDA)

# Vytvoření hráčů (červení vlevo, bílí vpravo)
hraci_cerveni = []
for i in range(6):
    hrac_cerveni_x = random.randint(50 + 20, SIRKA // 2 - 50)
    hrac_cerveni_y = random.randint(100, VYSKA - 100)
    hrac = {
        "cislo": i + 1,
        "x": hrac_cerveni_x,
        "y": hrac_cerveni_y,
        "dres": random.randint(1, 99)
    }
    hraci_cerveni.append(hrac)

hraci_bili = []
for i in range(6):
    hrac_bili_x = random.randint(SIRKA // 2 + 50, SIRKA - 50 - 20)
    hrac_bili_y = random.randint(100, VYSKA - 100)
    hrac = {
        "cislo": i + 1,
        "x": hrac_bili_x,
        "y": hrac_bili_y,
        "dres": random.randint(1, 99)
    }
    hraci_bili.append(hrac)

# Scoreboard / míč (statické pro teď)
score = (0, 0)
ball_pos = [SIRKA // 2, VYSKA // 2]

# Hráč, kterého ovládáme v červeném týmu (index 0)
ovladany_cerveny_idx = 0
# Hráč, kterého ovládáme v bílém týmu (index 0)
ovladany_bily_idx = 0
rychlost = 5

# Hlavní herní smyčka
bezi = True
while bezi:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False
        elif udalost.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            # Tab cycles controlled red players
            if udalost.key == pygame.K_TAB:
                ovladany_cerveny_idx = (ovladany_cerveny_idx + 1) % len(hraci_cerveni)
            # Pressing Shift alone cycles white players (either shift key)
            elif udalost.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                ovladany_bily_idx = (ovladany_bily_idx + 1) % len(hraci_bili)
            # Number keys 1-6 to select specific player: Shift + number selects white, otherwise red
            elif udalost.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6):
                idx = udalost.key - pygame.K_1
                if mods & pygame.KMOD_SHIFT:
                    if 0 <= idx < len(hraci_bili):
                        ovladany_bily_idx = idx
                else:
                    if 0 <= idx < len(hraci_cerveni):
                        ovladany_cerveny_idx = idx

    klavesy = pygame.key.get_pressed()
    # WASD pro červený tým (ovládá hrac s indexem ovladany_cerveny_idx)
    player = hraci_cerveni[ovladany_cerveny_idx]
    if klavesy[pygame.K_w]:
        player["y"] -= rychlost
    if klavesy[pygame.K_s]:
        player["y"] += rychlost
    if klavesy[pygame.K_a]:
        player["x"] -= rychlost
    if klavesy[pygame.K_d]:
        player["x"] += rychlost

    # Šipky pro bílý tým (ovládá vybraného bílého hráče)
    player_b = hraci_bili[ovladany_bily_idx]
    if klavesy[pygame.K_UP]:
        player_b["y"] -= rychlost
    if klavesy[pygame.K_DOWN]:
        player_b["y"] += rychlost
    if klavesy[pygame.K_LEFT]:
        player_b["x"] -= rychlost
    if klavesy[pygame.K_RIGHT]:
        player_b["x"] += rychlost

    # Ošetření hranic hřiště (aby hráči nevytékali)
    min_x = 50 + 20
    max_x = SIRKA - 50 - 20
    min_y = 50 + 20
    max_y = VYSKA - 50 - 20
    for t in (hraci_cerveni, hraci_bili):
        for h in t:
            h["x"] = max(min_x, min(max_x, h["x"]))
            h["y"] = max(min_y, min(max_y, h["y"]))

    # Překreslení scény
    draw_field(okno)

    # Vykreslení hráčů
    for idx, hrac in enumerate(hraci_cerveni):
        pygame.draw.circle(okno, CERVENA, (hrac["x"], hrac["y"]), 20)
        pygame.draw.circle(okno, CERNA, (hrac["x"], hrac["y"]), 20, 2)
        # zvýraznění ovládaného hráče
        if idx == ovladany_cerveny_idx:
            pygame.draw.circle(okno, ZELENA, (hrac["x"], hrac["y"]), 24, 3)
        cislo_text = pismo_maly.render(str(hrac["dres"]), True, BILA)
        cislo_rect = cislo_text.get_rect(center=(hrac["x"], hrac["y"]))
        okno.blit(cislo_text, cislo_rect)
        text = pismo_maly.render(f"Hráč {hrac['cislo']}", True, BILA)
        text_rect = text.get_rect(center=(hrac["x"], hrac["y"] + 30))
        okno.blit(text, text_rect)

    for idx, hrac in enumerate(hraci_bili):
        pygame.draw.circle(okno, BILA, (hrac["x"], hrac["y"]), 20)
        pygame.draw.circle(okno, CERNA, (hrac["x"], hrac["y"]), 20, 2)
        # zvýraznění ovládaného bílého hráče
        if idx == ovladany_bily_idx:
            pygame.draw.circle(okno, MODRA, (hrac["x"], hrac["y"]), 24, 3)
        cislo_text = pismo_maly.render(str(hrac["dres"]), True, CERNA)
        cislo_rect = cislo_text.get_rect(center=(hrac["x"], hrac["y"]))
        okno.blit(cislo_text, cislo_rect)
        text = pismo_maly.render(f"Hráč {hrac['cislo']}", True, CERNA)
        text_rect = text.get_rect(center=(hrac["x"], hrac["y"] + 30))
        okno.blit(text, text_rect)

    # Vykreslení míče a scoreboard
    pygame.draw.circle(okno, BILA, (ball_pos[0], ball_pos[1]), 15)
    pygame.draw.circle(okno, CERNA, (ball_pos[0], ball_pos[1]), 15, 2)
    scoreboard_text = pismo.render(f"Skóre: {score[0]} - {score[1]}", True, BILA)
    scoreboard_rect = scoreboard_text.get_rect(center=(SIRKA // 2, 30))
    okno.blit(scoreboard_text, scoreboard_rect)

    pygame.display.flip()
    hodiny.tick(60)

pygame.quit()
