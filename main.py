import pygame, sys
import numpy as np
pygame.init()
WIDTH = 600
linewidth = 15
board_rows = 3
board_columns = 3
HEIGHT = 600
Background = (20,170,156)
circle_radius = 60
circle_width = 15
circle_colour = (239,231,200)
linecolour = (23,145,135)
SQUARE_SIZE = 200
cross_width = 25
space = 55
cross_colour = (66,66,66)
game_over = False
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

def check_win(player) :
    for col in range(board_columns) :
        if board[0][col] == player and board[1][col] == player and board[2][col] == player :
            draw_vertical_winning_line(col,player)
            return True
    for row in range(board_rows) :
        if board[row][0] == player and board[row][1] == player and board[row][2] == player :
            draw_horizontal_winning_line(row,player)
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player :
        draw_des_diagnol(player)
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player :
        draw_asc_diagnol(player)
        return True
    return False
def draw_vertical_winning_line(col,player) :
    posX = col*200+100

    if player == 1 :
        colour = circle_colour
    elif player == 2 :
        colour = cross_colour
    pygame.draw.line(screen, colour, (posX,15), (posX, HEIGHT-15), 15)

def draw_horizontal_winning_line(row,player) :
        posY = row*200+100

        if player == 1 :
            colour = circle_colour
        elif player == 2 :
            colour = cross_colour
        pygame.draw.line(screen, colour, (15,posY), (WIDTH-15, posY), 15)

def draw_asc_diagnol(player) :
    if player == 1 :
        colour = circle_colour
    elif player == 2 :
        colour = cross_colour
    pygame.draw.line(screen,colour,(15,HEIGHT-15), (WIDTH-15,15),15)

def draw_des_diagnol(player) :
    if player == 1 :
        colour = circle_colour
    elif player == 2 :
        colour = cross_colour
    pygame.draw.line(screen,colour,(15,15), (WIDTH-15,HEIGHT-15),15)


def restart():
    screen.fill(Background)
    draw_lines()
    player = 1
    for row in range(board_rows) :
        for col in range(board_columns) :
            board[row][col] = 0



draw_lines()

def draw_figures() :
    for row in range(board_rows) :
        for column in range(board_columns) :
            if board[row][column] == 1 :
                pygame.draw.circle( screen, circle_colour, (int( column * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), circle_radius, circle_width )
            if board[row][column] == 2 :
                pygame.draw.line(screen, cross_colour, (column*200+space,row*200-space+200), (column*200+200-space,row*200+space), cross_width)
                pygame.draw.line(screen, cross_colour, (column*200+space, row*200+space), (column * 200 + 200 - space, row * 200 + 200 - space), cross_width )



player =1
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            rowclicked = int(mouseY // 200)
            columnclicked = int(mouseX//200)

            print(rowclicked,columnclicked)

            if available_square(rowclicked,columnclicked) :
                if player == 1 :
                    mark_square(rowclicked,columnclicked,1)
                    if check_win(player) :
                        game_over = True
                    player = 2
                elif player == 2 :
                    mark_square(rowclicked,columnclicked,2)
                    if check_win(player):
                        game_over = True
                    player = 1
                print(board)
                draw_figures()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_r :
                restart()
    pygame.display.update()
