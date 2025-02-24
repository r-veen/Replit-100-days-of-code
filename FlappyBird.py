import pygame, random

pygame.init()

# Fenstergrösse
WIDTH, HEIGHT = 700, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird mit echtem Vogel-Sprite")

# Farben
WHITE = (255, 255, 255)
BLUE_SKY = (113, 196, 206)  # Himmelblau

# Bilder laden
bg_images = [
    pygame.image.load("FBcity1.png"),
    pygame.image.load("FBcity2.png"),
    pygame.image.load("FBcity3.png"),
]

bg_images = [pygame.transform.scale(img, (WIDTH, HEIGHT - 200)) for img in bg_images] 

bird_size = (90, 90)
 
bird_images = [
    pygame.transform.scale(pygame.image.load("pngwing.com (1).png"), bird_size),
    pygame.transform.scale(pygame.image.load("pngwing.com (3).png"), bird_size)
]
 
bird_img = pygame.image.load("pngwing.com (1).png")
bird_img = pygame.transform.scale(bird_img, (50, 50)) 

pipe_img = pygame.image.load("pipe.png")  
pipe_img = pygame.transform.scale(pipe_img, (110, 500)) 


bg_index = 0
bg_timer = 0
BG_SPEED = 15


BX, BY = 100, HEIGHT // 2
Velocity = 0
Gravity = 0.5  
Flap_Force = -10 

PX = WIDTH
P_speed = 3
PIPE_WIDTH = 100 
PIPE_GAP = 200 
MIN_PIPE_HEIGHT = 100
MAX_PIPE_HEIGHT = HEIGHT - MIN_PIPE_HEIGHT - PIPE_GAP - 50  
PY1 = random.randint(MIN_PIPE_HEIGHT, MAX_PIPE_HEIGHT)  
PY2 = PY1 + PIPE_GAP  

clock = pygame.time.Clock()
FPS = 60
running = True

def create_collision_mask(image):
    """Erstellt eine Maske aus einem Bild, die nur die nicht-transparenten Bereiche berücksichtigt"""
    image = image.convert_alpha()  # Macht das Bild durchsichtiger
    return pygame.mask.from_surface(image)  

score = 0
scored = False  # Flag, das dafür sorgt, dass der Score nur einmal pro Röhre erhöht wird

font_size = 100
font = pygame.font.Font('Silkscreen-Bold.ttf', font_size)



pipe_mask = create_collision_mask(pipe_img)  # Maske für Röhre
bird_index = 0
bird_timer = 0
BIRD_ANIM_SPEED = 10  # Geschwindigkeit für Flap-Animation

while running:
    clock.tick(FPS)

    # **Berechne und rendere den Text**
    text = str(score)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH / 2, 50))  

    # Vogel-Animation und andere Logik ...
    
    # Hintergrund und Vogel zeichnen
    window.fill(BLUE_SKY)  # Himmelblau füllen (oben)
    window.blit(bg_images[bg_index], (0, 200))  # Hintergrund unter den blauen Himmel verschieben

    bird_timer += 1
    if bird_timer >= BIRD_ANIM_SPEED:
        bird_timer = 0  
        bird_index = (bird_index + 1) % len(bird_images)  # Wechsle zum nächsten Frame

    bird_img = bird_images[bird_index]  # Setze das aktuelle Bild

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Velocity = Flap_Force 

    # Hintergrund bewegung
    bg_timer += 1
    if bg_timer >= BG_SPEED:
        bg_timer = 0
        bg_index = (bg_index + 1) % len(bg_images) 
    # Schwerkraft
    Velocity += Gravity
    BY += Velocity

    # Score erhöhen, wenn der Vogel die Röhre passiert hat
    if PX + PIPE_WIDTH < BX and not scored:
        score += 1
        scored = True

    # **Kollisionen prüfen**
    if BY <= 0:  # Obere Begrenzung
        BY = 0
        Velocity = 0

    if BY >= HEIGHT - 140:  # Stirbt 100px vor dem Boden
        print("Game Over!") 
        running = False

    # Röhren bewegen
    PX -= P_speed
    if PX <= -PIPE_WIDTH:
        PX = WIDTH
        PY1 = random.randint(MIN_PIPE_HEIGHT, MAX_PIPE_HEIGHT)
        PY2 = PY1 + PIPE_GAP
        scored = False  # Zurücksetzen des Score-Flags

    # **Vogel-Sprite**: Rotation nur, wenn der Vogel sich bewegt
    rotated_image = pygame.transform.rotate(bird_img, -Velocity * 2)  # Rotation je nach Geschwindigkeit
    bird_rect = rotated_image.get_rect(center=(BX, BY))  # Position des Vogels beibehalten

    # Zeichnen der Röhren
    rotated_pipe1 = pygame.transform.rotate(pipe_img, 180)  # Um 180 Grad drehen
    rotated_pipe1_rect = rotated_pipe1.get_rect()
    rotated_pipe1_rect.topleft = (PX, PY1 - rotated_pipe1_rect.height)  # obere Röhre positionieren
    window.blit(rotated_pipe1, rotated_pipe1_rect.topleft)  # obere Röhre zeichnen

    # **Untere Röhre (pipe2)**
    pipe2_rect = pipe_img.get_rect()
    pipe2_rect.topleft = (PX, PY2)
    window.blit(pipe_img, pipe2_rect.topleft)  # untere Röhre zeichnen

    # **Kollision mit Röhren (genaue Maske)**
    bird_mask = create_collision_mask(rotated_image)  # Maske für den Vogel erstellen

    # Kollision mit der oberen Röhre
    offset = (PX - bird_rect.left, PY1 - rotated_pipe1_rect.height - bird_rect.top)
    if bird_mask.overlap(pipe_mask, offset):
        print("Game Over! Kollision mit Röhre!")
        running = False

    # Kollision mit der unteren Röhre
    offset = (PX - bird_rect.left, PY2 - bird_rect.top)
    if bird_mask.overlap(pipe_mask, offset):
        print("Game Over! Kollision mit Röhre!")
        running = False

    # Vogel zeichnen
    window.blit(rotated_image, bird_rect.topleft)  # Rotierten Vogel zeichnen

    # **Jetzt den Score hinzufügen**
    window.blit(text_surface, text_rect)  # Score wird hier hinzugefügt, nachdem alle anderen Elemente gezeichnet wurden

    # Fenster aktualisieren
    pygame.display.flip()

pygame.quit()
