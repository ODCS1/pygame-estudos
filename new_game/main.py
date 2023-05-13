import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.time.Clock()

SKY_SURFACE = pygame.image.load('grafics/Sky.png').convert()
ground_surface = pygame.image.load('grafics/ground.png').convert()
TEXT_SURFACE = TEXT_SURFACE = test

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # Draw all our elements
    # update everythinh
    pygame.display.update()
    clock.tick(60)