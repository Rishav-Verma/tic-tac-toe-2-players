import pygame, sys

pygame.init()
WIDTH = 600
linewidth = 15
HEIGHT = 600
Background = (20,170,156)
linecolour = (23,145,135)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe for 2 Players")
screen.fill(Background)

def draw_lines() :
    pygame.draw.line(screen, linecolour, (0,200), (600,200), linewidth)
    pygame.draw.line(screen, linecolour, (0,400), (600,400), linewidth)

    pygame.draw.line(screen,linecolour, (200,0), (200,600), linewidth)
    pygame.draw.line(screen, linecolour, (400,0), (400,600), linewidth)



draw_lines()
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
    pygame.display.update()
