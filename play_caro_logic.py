import pygame

width_board = 1200
height_board = 800
number_width_cell = 10
number_height_cell = 5

pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Game Caro")

font_file_path = 'font/kongtext.ttf'
font_size = 30
font = pygame.font.Font(font_file_path, font_size)

text_color = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

def printText(screen, text_content, font_size, antialias, text_color, x, y, LR): #antialias: True/False, LR: True(Left)/False(Right)
    font = pygame.font.Font(font_file_path, font_size)
    text = font.render(text_content, antialias, text_color)
    pygame.draw.rect(screen, BACKGROUND_COLOR, (x, y, text.get_width(), text.get_height()))
    if(LR == True):
        screen.blit(text, (x, y))
    else:
        screen.blit(text, (x-text.get_width(), y))

def draw_caro_table(width_board,lenght_board, number_width_cell, number_height_cell):
    # Vung choi game (max) la HCN bat dau tu (100, 75) --> (width_board - 100, height_board - 75)
    cellLength = min((width_board-200)/number_width_cell, (height_board-150)/number_height_cell)
    x1 = (width_board - number_width_cell*cellLength)/2
    y1 = (height_board - number_height_cell*cellLength)/2
    x2 = width_board - x1
    y2 = height_board - y1
    for x in range(int(x1), int(x2)+1, int(cellLength)):
        pygame.draw.line(screen, (0, 0, 0), (x, y1), (x, y2), 2)
    for y in range(int(y1), int(y2)+1, int(cellLength)):
        pygame.draw.line(screen, (0, 0, 0), (x1, y), (x2, y), 2)

    # O thu (i, j) xac dinh nhu sau:
    # chia vung choi game thanh cac o nhu sau:
        # theo chieu Ox: chia [x1, x2] thanh number_width_cell thanh phan [x1, a1], [a1, a2],..., [a_number_width_cell - 1; x2] -> cot thu j co toa do: x = x1 + (x2-x1)/number_width_cell*(2*j+1)/2
        # theo chieu )y: chia [y1, y2] thanh number_height_cell thanh phan [y1, b1], [b1, b2],..., [b_number_width_cell - 1; y2] -> hang thu i co toa do: x = y1 + (y2-y1)/number_height_cell*(2*i+1)/2
    #gioi han cua o (i, j) la: (x1 + (x2-x1)/number_width_cell*i, y1 + (y2-y1)/number_height_cell*j) --> (x1 + (x2-x1)/number_width_cell*(i+1), y1 + (y2-y1)/number_height_cell*(j+1))
    #Do kich thuoc chu = font_size x font_size nen de in ra ngay trung tam o can xac dinh:
    i, j = 1, 2
    xo = x1 + (x2-x1)/number_width_cell*(2*j+1)/2-int(cellLength/4)
    yo = y1 + (y2-y1)/number_height_cell*(2*i+1)/2-int(cellLength/4)
    printText(screen, "O", int(cellLength/2), True, text_color, xo, yo, 1)
def print_caro_information(screen, text_color, width_board, height_board):
    #Thong so
    printText(screen, "Back", 30, False, text_color, width_board - 25, 25, 0)
    printText(screen, "Player 1's turn!", 30, False, text_color, 25, 25, 1)
    printText(screen, "Player 1: X", 30, False, text_color, 25 , height_board - 50, True)
    printText(screen, "Player 2: O", 30, True, text_color, width_board - 25, height_board - 50, False)
running = 1
while running:
    #khai báo màu nền cho giao diện

    screen.fill(BACKGROUND_COLOR)


    draw_caro_table(width_board, height_board, number_width_cell, number_height_cell)
    print_caro_information(screen, text_color, width_board, height_board)

        #xử lý sự kiện
    for event in pygame.event.get():
        #sự kiện thoát
        if event.type == pygame.QUIT:
            running = False
        #sự kiện chuột
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #nhấn chuột trái
                print(event.pos) #in tọa độ chuột
    pygame.display.update()
pygame.quit()