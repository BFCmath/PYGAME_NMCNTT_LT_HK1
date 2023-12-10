import pygame, Define
from Button import Button
from BoardGame import Game_logic

def PlayGame_scene(SCREEN):
    running = True
    p = [[0 for j in range(15)] for i in range(7)]
    Back_Button = Button(pos=(1120, 670), text_input="Back", font=Define.get_font(35), font_color="black", rect_width=200, rect_height=70)
    Board = Game_logic(15, 7, p, "TrongDoanh", "Hehe")
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