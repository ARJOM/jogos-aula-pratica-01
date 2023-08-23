import pygame
from pygame.locals import *
from sys import exit

image_bg = 'background.jpg'
mouse = 'cursor.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Jojo")

background = pygame.image.load(image_bg).convert()
mouse_cursor = pygame.image.load(mouse).convert()
mouse_cursor = pygame.transform.scale(mouse_cursor, (20, 20))

if __name__=="__main__":
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            screen.blit(background, (0, 0))

            x, y = pygame.mouse.get_pos()
            x -= mouse_cursor.get_width() / 2
            y -= mouse_cursor.get_height() / 2
            screen.blit(mouse_cursor, (x, y))

            pygame.display.update()
