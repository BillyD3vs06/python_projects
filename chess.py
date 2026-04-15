import pygame
import sys
from pygame.locals import *

HEIGHT = 600
WIDTH = 800

ROWS = 8
COLS = 8
SQUARE_SIZE = HEIGHT // ROWS

BOARD_WHITE = (200, 180, 140) #Ljus beige
BOARD_BLACK = (100, 70, 40) #Mörk brunt


#Initialize the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                color = BOARD_WHITE
            else:
                color = BOARD_BLACK
            
            pygame.draw.rect(
                screen,
                color,
                (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            )

#Runs the game loop
def main():
    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                break

        draw_board() #Draws the chess board each frame
        pygame.display.update()

if __name__ == "__main__":
    main()