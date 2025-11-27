import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Self-Driving Car Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Car properties
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 50
car_speed = 5

# Enemy car properties
enemy_width = 50
enemy_height = 100
enemy_x = random.randint(150, 150 + 300 - enemy_width)
enemy_y = -enemy_height
enemy_speed = 7

# Clock
clock = pygame.time.Clock()
FPS = 60

# Draw road
def draw_road():
    pygame.draw.rect(win, GRAY, (150, 0, 300, HEIGHT))
    for y in range(0, HEIGHT, 80):
        pygame.draw.rect(win, YELLOW, (295, y, 10, 40))

# Draw red player car
def draw_car(x, y):
    pygame.draw.rect(win, RED, (x, y, car_width, car_height))

# Draw blue enemy car
def draw_enemy(x, y):
    pygame.draw.rect(win, BLUE, (x, y, enemy_width, enemy_height))

# Collision detection
def is_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    return (
        x1 < x2 + w2 and
        x1 + w1 > x2 and
        y1 < y2 + h2 and
        y1 + h1 > y2
    )

# Main game loop
def main():
    global car_x, car_y, enemy_x, enemy_y

    run = True

    while run:
        clock.tick(FPS)
        win.fill(WHITE)
        draw_road()

        # Key controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 150:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < 150 + 300 - car_width:
            car_x += car_speed

        # Enemy movement
        enemy_y += enemy_speed
        if enemy_y > HEIGHT:
            enemy_y = -enemy_height
            enemy_x = random.randint(150, 150 + 300 - enemy_width)

        # Draw cars
        draw_car(car_x, car_y)
        draw_enemy(enemy_x, enemy_y)

        # Collision check
        if is_collision(car_x, car_y, car_width, car_height, enemy_x, enemy_y, enemy_width, enemy_height):
            font = pygame.font.SysFont("comicsans", 60)
            text = font.render("Game Over!", True, RED)
            win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False

        # Quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
    sys.exit()

# Run the game
main()