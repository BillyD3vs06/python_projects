import pygame
import sys
import random
import time


HEIGHT = 600
WIDTH = 800

player_height = 70
player_width = 15
player_color = (255, 255, 255)
player_velocity = 15

p1y = HEIGHT / 2 - player_height / 2
p2y = HEIGHT / 2 - player_height / 2

background_color = (0, 0, 0)

net_width = 6
net_height = 20
gap = 9

ball_color = (255, 255, 255)
ball_size = 15
ball_speed = 5

spawn_area = 100 #The ball can spawn everywhere 100 pixels from the center of the screen

spawn_x = random.randint(WIDTH // 2 - spawn_area // 2, WIDTH // 2 + spawn_area // 2)
spawn_y = random.randint(HEIGHT // 2 - spawn_area // 2, HEIGHT // 2 + spawn_area // 2)

ball = pygame.Rect(spawn_x, spawn_y, ball_size, ball_size)

ball_direction = random.choice([-1, 1]) # -1 left, 1 right

ball_vel_x = ball_direction * ball_speed
ball_vel_y = random.choice([-1, 1]) * ball_speed





# Initializes the game screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("pong clone")

pygame.display.flip()

#Draws everything on the SCREEN
def draw(player1, player2):
    SCREEN.fill(background_color)

    pygame.draw.rect(SCREEN, player_color, player1)
    pygame.draw.rect(SCREEN, player_color, player2)

    
    # Drawing the net
    for y in range(0, HEIGHT, net_height + gap):
        pygame.draw.rect(SCREEN, (255, 255, 255), (WIDTH / 2 - net_width / 2, y, net_width, net_height))

    #Drawing the ball
    pygame.draw.rect(SCREEN, ball_color, ball)


    pygame.display.flip()
    pygame.display.update()

#Starts the game loop
def main():
    running = 1

    global ball
    global ball_vel_x
    global ball_vel_y

    #Drawing the players
    p1 = pygame.Rect(player_width * 2, p1y, player_width, player_height)
    p2 = pygame.Rect(WIDTH - player_width * 3, p2y, player_width, player_height)

    clock = pygame.time.Clock()
    

    while running:
        clock.tick(60) #Sets the fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                break

        #Makes the players move
        keys = pygame.key.get_pressed()

        #P1 movement controls
        if keys[pygame.K_w] and p1.y > 0:
            p1.y -= player_velocity
        if keys[pygame.K_s] and p1.y < HEIGHT - player_height:
            p1.y += player_velocity
    
        #p2 movement controls
        if keys[pygame.K_UP] and p2.y > 0:
            p2.y -= player_velocity
        if keys[pygame.K_DOWN] and p2.y < HEIGHT - player_height:
            p2.y += player_velocity

        # Ball movement
        ball.x += ball_vel_x
        ball.y += ball_vel_y

        # Ball collision with top and bottom walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_vel_y *= -1
        
        # Ball collision with players
        if ball.colliderect(p1) or ball.colliderect(p2):
            ball_vel_x *= -1

        if ball.colliderect(p1):
            ball.left = p1.right
            ball_vel_x *= -1

        if ball.colliderect(p2):
            ball.right = p2.left
            ball_vel_x *= -1
         

        draw(p1, p2)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
