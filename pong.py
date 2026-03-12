import pygame

# Initializes the game window
background_color = (0, 0, 0)

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("pong")

screen.fill(background_color)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

