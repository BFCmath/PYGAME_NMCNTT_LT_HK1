import pygame

# Setting
width_board = 1200
height_board = 800
number_width_cell = 8
number_height_cell = 8

cellLength = int(min((width_board-200)/number_width_cell, (height_board-150)/number_height_cell))
x1 = int((width_board - number_width_cell*cellLength)/2)
y1 = int((height_board - number_height_cell*cellLength)/2)
x2 = width_board - x1
y2 = height_board - y1

text_color = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

p = [[0 for j in range(number_width_cell)] for i in range(number_height_cell)]

# Default
pygame.init()

screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Game Caro")

font_file_path = 'font/kongtext.ttf'


# Function
def printText(screen, text_content, font_size, antialias, text_color, x, y, LR): #antialias: True/False, LR: True(Left)/False(Right)
    font = pygame.font.Font(font_file_path, font_size)
    text = font.render(text_content, antialias, text_color)
    pygame.draw.rect(screen, BACKGROUND_COLOR, (x, y, text.get_width(), text.get_height()))
    if(LR == True):
        screen.blit(text, (x, y))
    else:
        screen.blit(text, (x-text.get_width(), y))

def draw_caro_table(width_board,height_board, number_width_cell, number_height_cell):
    # Vung choi game (max) la HCN bat dau tu (100, 75) --> (width_board - 100, height_board - 75)
    cellLength = int(min((width_board-200)/number_width_cell, (height_board-150)/number_height_cell))
    x1 = int((width_board - number_width_cell*cellLength)/2)
    y1 = int((height_board - number_height_cell*cellLength)/2)
    x2 = width_board - x1
    y2 = height_board - y1
    for x in range(int(x1), int(x2)+1, cellLength):
        pygame.draw.line(screen, (0, 0, 0), (x, y1), (x, y2), 2)
    for y in range(int(y1), int(y2)+1, cellLength):
        pygame.draw.line(screen, (0, 0, 0), (x1, y), (x2, y), 2)

def print_caro_information(screen, text_color, width_board, height_board):
    #Thong so
    printText(screen, "Back", 30, False, text_color, width_board - 25, 25, 0)
    printText(screen, "Player 1's turn!", 30, False, text_color, 25, 25, 1)
    printText(screen, "Player 1: X", 30, False, text_color, 25 , height_board - 50, True)
    printText(screen, "Player 2: O", 30, True, text_color, width_board - 25, height_board - 50, False)

def Check_Win(turn, row, col):
    w = number_width_cell
    h = number_height_cell
    count = 0
    block = 0
    r = max(row - 1, 0)
    while (r > -1 and p[r][col] == turn):
        count = count + 1
        r = r - 1
    if r == -1 or p[r][col] == -turn:
        block = block + 1
    r = min(row + 1 , h)
    while ( r < h and p[r][col] == turn):
        count = count + 1
        r = r + 1
    if r == h or p[r][col] == -turn:
        block = block + 1
    if (count > 3 and block < 2):
        return True

    count = 0
    block = 0
    c = max(col - 1, 0)
    while (c > -1 and p[row][c] == turn):
        count = count + 1
        c = c - 1
    if c == -1 or p[row][c] == -turn:
        block = block + 1
    c = min(col + 1 , w)
    while (c < w and p[row][c] == turn):
        count = count + 1
        c = c + 1
    print(c, h)
    if c == w or p[row][c] == -turn:
        block = block + 1
    if (count > 3 and block < 2):
        return True

    count = 0
    block = 0
    i = 1
    while ( row + i < h and col + i < w and p[row + i][col + i] == turn ):
        count = count + 1
        i = i + 1
    if row + i == h or col + i == w or p[row + i][col + i] == -turn:
        block = block + 1
    i = 1
    while (row - i > -1 and col - i > -1 and p[row - i][col - i] == turn):
        count = count + 1
        i = i + 1
    if row - i == -1 or col - i == w or p[row - i][col - i] == -turn:
        block = block + 1
    if (count > 3 and block < 2):
        return True    

    count = 0
    block = 0
    i = 1
    while (row + i < h and col - i > -1 and p[row + i][col - i] == turn  ):
        count = count + 1
        i = i + 1
    if row + i == h or col - i == w or p[row + i][col - i] == -turn:
        block = block + 1
    i = 1
    while (row - i > -1 and col + i < w and p[row - i][col + i] == turn ):
        count = count + 1
        i = i + 1
    if row - i == -1 or col + i == w or p[row - i][col + i] == -turn:
        block = block + 1
    if (count > 3 and block < 2):
        return True 

    return False

def Make_Move(screen, turn, row, col):
    x0 = x1 + (x2-x1)/number_width_cell*(2*col+1)/2-int(cellLength/4)
    y0 = y1 + (y2-y1)/number_height_cell*(2*row+1)/2-int(cellLength/4)
    printText(screen, 'X' if turn == 1 else 'O', int(cellLength/1.75), True, text_color, x0, y0, 1)
    p[row][col] = turn
    return Check_Win(turn, row, col)

screen.fill(BACKGROUND_COLOR)
draw_caro_table(width_board, height_board, number_width_cell, number_height_cell)
print_caro_information(screen, text_color, width_board, height_board)
running = True
turn = 1
#game loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            cell_col = int((x - x1)*number_width_cell /(x2-x1))
            cell_row = int((y - y1)*number_height_cell/(y2-y1))

            if  x2 > x > x1 and y2 > y > y1 and p[cell_row][cell_col] == 0 :
                T = Make_Move(screen, turn, cell_row, cell_col)
                if(T == True):
                    print("Nguoi choi", 'X' if turn == 1 else 'O', "thang cuoc!")
                turn = -turn
    pygame.display.flip()
pygame.quit()

    