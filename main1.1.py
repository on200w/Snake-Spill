import pygame  # Importerer Pygame-biblioteket for spillutvikling
import time  # Importerer tidsbiblioteket
import random  # Importerer biblioteket for tilfeldige tall

# Konstanter for farger (RGB-verdi)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 128, 0)

# Skjermstørrelse og slangeparametere
WIDTH, HEIGHT = 600, 400
SNAKE_SIZE = 10
SNAKE_SPEED = 13 #tick i sekunden

# Initialiser Pygame
pygame.init()
GAME_DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))  # Setter skjermstørrelsen
pygame.display.set_caption("Snake Game")  # Setter tittel på spillet
CLOCK = pygame.time.Clock()  # Initialiserer en klokke for å kontrollere spillets hastighet
MESSAGE_FONT = pygame.font.SysFont('ubuntu', 30)  # Skrift for meldinger
SCORE_FONT = pygame.font.SysFont('ubuntu', 25)  # Skrift for poengsum

def print_score(score, font, display):
    """Viser poengsummen på skjermen."""
    text = font.render("Score: " + str(score), True, ORANGE)  # Renders poengsum tekst
    display.blit(text, [0, 0])  # Viser poengsum i øvre venstre hjørne

def draw_snake(snake_size, snake_pixels, display):
    """Tegner slangen på skjermen."""
    for pixel in snake_pixels:
        pygame.draw.rect(display, GREEN, [pixel[0], pixel[1], snake_size, snake_size])  # Tegner hver del av slangen

def run_game():
    """Hovedspillfunksjonen."""
    game_over = False  # Flag for å avslutte spillet
    game_close = False  # Flag for når spillet er over, men bruker kan velge å spille igjen

    x, y = WIDTH / 2, HEIGHT / 2  # Startposisjon for slangen
    x_speed, y_speed = 0, 0  # Startfart for slangen

    snake_pixels = []  # Liste for å holde styr på slangens posisjon
    snake_length = 1  # Startlengde for slangen

    # Initial posisjon for målet (maten)
    target_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
    target_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0

    while not game_over:
        while game_close:
            # Viser Game Over-skjerm
            GAME_DISPLAY.fill(BLACK)
            game_over_message = MESSAGE_FONT.render("Game Over!", True, RED)
            GAME_DISPLAY.blit(game_over_message, [WIDTH / 2.7, HEIGHT / 3.2])
            print_score(snake_length - 1, SCORE_FONT, GAME_DISPLAY)
            retry_message = MESSAGE_FONT.render("Trykk på C for å avslutte", True, ORANGE)
            GAME_DISPLAY.blit(retry_message, [WIDTH / 3.7, HEIGHT / 2.5])
            quit_message = MESSAGE_FONT.render("Trykk på R for å prøve igjen", True, ORANGE)
            GAME_DISPLAY.blit(quit_message, [WIDTH / 3.9, HEIGHT / 2.1])
            pygame.display.update()
            for event in pygame.event.get():  # Håndterer hendelser når spillet er over
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_over = True  # Avslutter spillet
                        game_close = False
                    if event.key == pygame.K_r:
                        run_game()  # Starter spillet på nytt
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():  # Håndterer hendelser under spillet
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    x_speed = -SNAKE_SIZE
                    y_speed = 0
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    x_speed = SNAKE_SIZE
                    y_speed = 0
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    y_speed = -SNAKE_SIZE
                    x_speed = 0
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    y_speed = SNAKE_SIZE
                    x_speed = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True  # Setter game_close til True hvis slangen går utenfor skjermen

        x += x_speed
        y += y_speed

        GAME_DISPLAY.fill(BLACK)  # Fyller skjermen med svart
        pygame.draw.rect(GAME_DISPLAY, RED, [target_x, target_y, SNAKE_SIZE, SNAKE_SIZE])  # Tegner målet (maten)

        snake_pixels.append([x, y])  # Legger til ny posisjon til slangen
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]  # Fjerner den eldste posisjonen hvis slangen har vokst

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True  # Sjekker om slangen kolliderer med seg selv

        draw_snake(SNAKE_SIZE, snake_pixels, GAME_DISPLAY)  # Tegner slangen
        print_score(snake_length - 1, SCORE_FONT, GAME_DISPLAY)  # Viser poengsummen

        pygame.display.update()  # Oppdaterer skjermen

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
            target_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0
            snake_length += 1  # Øker slangens lengde når den spiser maten

        CLOCK.tick(SNAKE_SPEED)  # Kontrollerer hastigheten på spillet

    pygame.quit()  # Avslutter Pygame
    quit()  # Avslutter programmet

run_game()  # Starter spillet
