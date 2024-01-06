import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
SHIP_SPEED = 5

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galactic Groove Runner")

# Load spaceship image
ship_image = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.polygon(ship_image, (255, 0, 0), [(0, 25), (50, 25), (25, 0)])
ship_rect = ship_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_rect.left > 0:
        ship_rect.x -= SHIP_SPEED
    if keys[pygame.K_RIGHT] and ship_rect.right < WIDTH:
        ship_rect.x += SHIP_SPEED
    if keys[pygame.K_UP] and ship_rect.top > 0:
        ship_rect.y -= SHIP_SPEED
    if keys[pygame.K_DOWN] and ship_rect.bottom < HEIGHT:
        ship_rect.y += SHIP_SPEED

    # Update the display
    screen.fill(WHITE)
    screen.blit(ship_image, ship_rect)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
