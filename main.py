import pygame, sys
import numpy as np
pygame.init()
WIDTH = 600
linewidth = 15
board_rows = 3
board_columns = 3
HEIGHT = 600
Background = (20,170,156)
linecolour = (23,145,135)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe for 2 Players")
screen.fill(Background)

board = np.zeros((board_rows,board_columns))


def mark_square(rows,columns,player) :
    board[rows][columns] = player
def available_square(rows, columns) :
    return board[rows][columns] == 0
def board_full() :
    for row in range(board_rows) :
        for col in range(board_columns) :
            if board[row][col] == 0 :
                return False
            else :
                return True


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
