
import pygame
from pygame.locals import *
import sys
from aliens import Alien
from ship import Ship
from laser import Laser

pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')

# Set the background color
bg_color = (0, 0, 0) # Black

ship = Ship(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

enemies = pygame.sprite.Group()
for i in range(8):
    for j in range(5):
        alien = Alien(10 + i * 50, 30 + j * 40)
        enemies.add(alien)

bullets = pygame.sprite.Group()

clock = pygame.time.Clock()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                laser = Laser(ship.rect.centerx, ship.rect.y)
                bullets.add(laser)

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        ship.move_left()
    if keys[K_RIGHT]:
        ship.move_right()

    # Update game objects
    enemies.update()
    bullets.update()

    # Check for collisions
    pygame.sprite.groupcollide(bullets, enemies, True, True)

    # Draw game objects
    screen.fill(bg_color)
    screen.blit(ship.image, ship.rect)
    enemies.draw(screen)
    bullets.draw(screen)

    pygame.display.flip()
    clock.tick(60)