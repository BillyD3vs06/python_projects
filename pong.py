import pygame
import sys
import random
import time


HEIGHT = 600
WIDTH = 800

player_height = 70
player_width = 15
player_color = (255, 255, 255)
player_velocity = 5

p1y = HEIGHT / 2 - player_height / 2
p2y = HEIGHT / 2 - player_height / 2

ball_color = (255, 255, 255)
ball_dimension = 10

background_color = (0, 0, 0)


# Initializes the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("pong clone")

screen.fill(background_color)

pygame.display.flip()


#Starts the game loop
running = True

while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Makes the players move
    keys = pygame.key.get_pressed()


    #P1 movement controls
    if keys[pygame.K_w] and p1y > 0:
        p1y -= player_velocity
    
    if keys[pygame.K_s] and p1y < HEIGHT - player_height:
        p1y += player_velocity
    
    #p2 movement controls
    if keys[pygame.K_UP] and p2y > 0:
        p2y -= player_velocity

    if keys[pygame.K_DOWN] and p2y < HEIGHT - player_height:
        p2y += player_velocity
    
    
    #Drawing the players
    p1 = pygame.draw.rect(
        screen, 
        player_color, 
        pygame.Rect(player_width, p1y, player_width, player_height))
    
    p2 = pygame.draw.rect(
        screen, 
        player_color, 
        pygame.Rect(WIDTH - player_width * 2, p2y, player_width, player_height))
    
    
    #Drawing the net
    net_width = 6
    net_height = 20
    gap = 9

    for y in range(0, HEIGHT, net_height + gap):
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH/2 - net_width/2, y, net_width, net_height))


    pygame.display.flip()


pygame.quit()
sys.exit()
