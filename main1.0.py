import pygame
import time
import random

# Init Pygame
pygame.init()

# Define Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
green = (0, 128, 0)

# Width and height of the game
width, height = 600, 400
game_display = pygame.display.set_mode((width, height))

# Set title
pygame.display.set_caption("Snake Game")

# Keep the game running 
clock = pygame.time.Clock()

# Snake size and speed
snake_size = 10
snake_speed = 15

# Font's
message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

# Update and draw score
def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0,0])

# Update and draw snake
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, green, [pixel[0], pixel[1], snake_size, snake_size])


# Main function to run game
def run_game():

    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0

    # Game loop
    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over!", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            print_score(snake_length -1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    y_speed = -snake_size
                    x_speed = 0
                if event.key == pygame.K_DOWN:
                    y_speed = snake_size
                    x_speed = 0
                if event.key == pygame.K_a:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_d:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_w:
                    y_speed = -snake_size
                    x_speed = 0
                if event.key == pygame.K_s:
                    y_speed = snake_size
                    x_speed = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, red, [target_x,target_y,snake_size, snake_size])

        snake_pixels.append([x,y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]
        
        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        # Plotting the snake 
        draw_snake(snake_size, snake_pixels)
        print_score(snake_length -1)

        pygame.display.update()


        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def new_func(target_x, target_y):
    pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size])

run_game()