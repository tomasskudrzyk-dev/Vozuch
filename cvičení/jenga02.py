import pygame

WIDTH, HEIGHT = 800, 600
BACKGROUND = (30, 30, 40)

# Barvy pro jednotlivé strany krychle
COLOR_TOP = (200, 200, 200)
COLOR_LEFT = (150, 150, 150)
COLOR_RIGHT = (100, 100, 100)
#Vytvoření barev
BILA = (255, 255, 255)
SEDA = (128, 128, 128)
CERNA = (0, 0, 0)
CERVENA = (255, 0, 0)
MODRA = (0, 0, 255)
ZELENA = (0, 255, 0)

# Velikost hrany krychle
SIZE = 150

# Nastavení izometrické projekce
ISO_COS = 0.866
ISO_SIN = 0.5

def project(x, y, z):
    """Převede 3D souřadnice na 2D souřadnice obrazovky."""
    screen_x = WIDTH // 2 + (x - y) * ISO_COS
    # Použijeme střed obrazovky jako výchozí bod (0,0,0)
    screen_y = HEIGHT // 2 + (x + y) * ISO_SIN - z
    return int(screen_x), int(screen_y)

def draw_cube(surface):
    """Vykreslí izometrickou krychli."""
    s = SIZE / 2
    # 8 rohů krychle ve 3D prostoru (x, y, z)
    corners_3d = [
        (-s, -s, -s), (s, -s, -s), (s, s, -s), (-s, s, -s), # Spodní rohy
        (-s, -s, s),  (s, -s, s),  (s, s, s),  (-s, s, s)   # Horní rohy
    ]
    
    # Převedení všech rohů do 2D obrazovky
    c = [project(x, y, z) for x, y, z in corners_3d]
    
    # Definice 6 stěn (pomocí indexů rohů) a jejich barvy
    faces = [
        ([4, 5, 6, 7], BILA),   # Horní stěna (+z)
        ([5, 1, 2, 6], BILA), # Pravá stěna (+x)
        ([6, 2, 3, 7], MODRA),  # Levá stěna (+y)
        ([7, 3, 0, 4], COLOR_RIGHT), # Zadní pravá (-x)
        ([4, 0, 1, 5], COLOR_LEFT),  # Zadní levá (-y)
        ([1, 0, 3, 2], COLOR_TOP),   # Spodní stěna (-z)
    ]
    
    for idxs, color in faces:
        face = [c[i] for i in idxs]
        
        # Algoritmus Backface culling: zjistí, zda je stěna natočená k nám
        area = 0
        for i in range(len(face)):
            p1 = face[i]
            p2 = face[(i+1) % len(face)]
            area += (p1[0] * p2[1] - p2[0] * p1[1])
            
        # Vykreslí stěnu pouze pokud je viditelná (obsah > 0)
        if area > 0:
            pygame.draw.polygon(surface, color, face)       # Vyplnění barvou
            pygame.draw.polygon(surface, (0, 0, 0), face, 2) # Černý obrys

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Izometrická krychle")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill(BACKGROUND)
        draw_cube(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
