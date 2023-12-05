import pygame, Define
from Button import Button
from BoardGame import Game_logic

def Draw_Board(Screen, number_width_cell, number_height_cell):
    # Vung choi game (max) la HCN bat dau tu (100, 100) --> (width_board - 100, height_board - 100)
    cellLength = min(Define.BoardGame.BOARD_WIDTH // number_width_cell, Define.BoardGame.BOARD_HEIGHT // number_height_cell)
    
    x1 = (Define.Screen.SCREEN_WIDTH - number_width_cell*cellLength)//2
    y1 = (Define.Screen.SCREEN_HEIGHT - number_height_cell*cellLength)//2
    x2 = x1 + cellLength*number_width_cell
    y2 = y1 + cellLength*number_height_cell

    for x in range(x1, x2 + 1, cellLength):
        pygame.draw.line(Screen, (255, 255, 255), (x, y1), (x, y2), 2)
    for y in range(y1, y2 + 1, cellLength):
        pygame.draw.line(Screen, (255, 255, 255), (x1, y), (x2, y), 2)
            
    # O thu (i, j) xac dinh nhu sau:
    # chia vung choi game thanh cac o nhu sau:
        # theo chieu Ox: chia [x1, x2] thanh number_width_cell thanh phan [x1, a1], [a1, a2],..., [a_number_width_cell - 1; x2] -> cot thu j co toa do: x = x1 + (x2-x1)/number_width_cell*(2*j+1)/2
        # theo chieu )y: chia [y1, y2] thanh number_height_cell thanh phan [y1, b1], [b1, b2],..., [b_number_width_cell - 1; y2] -> hang thu i co toa do: x = y1 + (y2-y1)/number_height_cell*(2*i+1)/2
    #gioi han cua o (i, j) la: (x1 + (x2-x1)/number_width_cell*i, y1 + (y2-y1)/number_height_cell*j) --> (x1 + (x2-x1)/number_width_cell*(i+1), y1 + (y2-y1)/number_height_cell*(j+1))
    #Do kich thuoc chu = font_size x font_size nen de in ra ngay trung tam o can xac dinh:
    # i, j = 1, 2
    # xo = x1 + (x2-x1)/number_width_cell*(2*j+1)/2-int(cellLength/4)
    # yo = y1 + (y2-y1)/number_height_cell*(2*i+1)/2-int(cellLength/4)
    # printText(screen, "O", int(cellLength/2), True, text_color, xo, yo, 1)

def PlayGame_scene(SCREEN):
    running = True
    p = [[0 for j in range(5)] for i in range(5)]
    Back_Button = Button(pos=(1120, 670), text_input="Back", font=Define.get_font(35), font_color="black", rect_width=200, rect_height=70)
    Board = Game_logic(5, 5, p, "TrongDoanh", "Hehe")
    while running:
        SCREEN.blit(Define.Screen.BACKGROUND, (0, 0))
        # Draw_Board(SCREEN, 99, 50)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        for button in [Back_Button]:
            button.changeSize(PLAY_MOUSE_POS)
            button.update(SCREEN)
        
        Board.PrintInfor(SCREEN)
        Board.DrawBoard(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.checkForInput(PLAY_MOUSE_POS):
                    running = False
                Board.checkForInput(PLAY_MOUSE_POS)
        pygame.display.update()