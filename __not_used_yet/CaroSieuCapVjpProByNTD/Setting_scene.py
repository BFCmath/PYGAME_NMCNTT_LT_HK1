import pygame, Define
from Button import Button, Box

def SetBoardSize(SCREEN):
    text = Define.get_font(50).render("BOARD SIZE", True, "#b68f40")
    rect = text.get_rect(center=(640, 250))
    Back_Button = Button(pos=(450, 500), text_input="Back", font=Define.get_font(35), font_color="black", rect_width=200, rect_height=70)
    Save_Button = Button(pos=(820, 500), text_input="Save", font=Define.get_font(35), font_color="black", rect_width=200, rect_height=70)
    Width_box = Box(pos=(540, 360), font=Define.get_font(35), font_type="number", rect_width=120, rect_height=60, text_default="09")
    Height_box = Box(pos=(740, 360), font=Define.get_font(35), font_type="number", rect_width=120, rect_height=60, text_default="09")
    running = True
    while running:
        SCREEN.blit(Define.Popup.BLUR_SURFACE, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        pygame.draw.rect(SCREEN, Define.Popup.POPUP_COLOR, (285, 155, 700, 400), 5, border_radius=30)

        SCREEN.blit(text, rect)

        for button in [Back_Button, Save_Button]:
            button.changeSize(MOUSE_POS)
            button.update(SCREEN)

        for box in [Width_box, Height_box]:
            box.changeColor(SCREEN, MOUSE_POS)
            box.update(SCREEN)

        pygame.draw.line(SCREEN, "white", (625, 345), (660, 380), 10)
        pygame.draw.line(SCREEN, "white", (625, 380), (660, 345), 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.checkForInput(MOUSE_POS):
                    running = False
                if Save_Button.checkForInput(MOUSE_POS):
                    print("Save", Width_box.text_input)
                    running = False
            Width_box.handle_event(event)
            Height_box.handle_event(event)
        pygame.display.update()

def SetPlayer(SCREEN):
    text = Define.get_font(50).render("PLAYER NAME", True, "#b68f40")
    rect = text.get_rect(center=(640, 250))

    Back_Button = Button(pos=(450, 500), text_input="Back", font=Define.get_font(35), font_color="black", rect_width=200, rect_height=70)
    Save_Button = Button(pos=(820, 500), text_input="Save", font=Define.get_font(35), font_color="black", rect_width=200, rect_height=70)
    
    player1 = Define.get_font(30).render("Player 1: ", False, "white")
    player2 = Define.get_font(30).render("Player 2: ", False, "white")
    rect1 = player1.get_rect(center=(420, 320))
    rect2 = player2.get_rect(center=(420, 400))
    
    Player1_box = Box(pos=(750, 320), font=Define.get_font(30), font_type="text", rect_width=420, rect_height=50, text_default="Player 1")
    Player2_box = Box(pos=(750, 400), font=Define.get_font(30), font_type="text", rect_width=420, rect_height=50, text_default="Player 2")
    running = True
    while running:
        SCREEN.blit(Define.Popup.BLUR_SURFACE, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        pygame.draw.rect(SCREEN, Define.Popup.POPUP_COLOR, (235, 155, 800, 400), 5, border_radius=30)

        SCREEN.blit(text, rect)
        SCREEN.blit(player1, rect1)
        SCREEN.blit(player2, rect2)

        for button in [Back_Button, Save_Button]:
            button.changeSize(MOUSE_POS)
            button.update(SCREEN)

        for box in [Player1_box, Player2_box]:
            box.changeColor(SCREEN, MOUSE_POS)
            box.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if Back_Button.checkForInput(MOUSE_POS):
                    running = False
                if Save_Button.checkForInput(MOUSE_POS):
                    print("Save", Player1_box.text_input, Player2_box.text_input)
                    running = False
            Player1_box.handle_event(event)
            Player2_box.handle_event(event)
        pygame.display.update()

def Setting_scene(SCREEN):
    running = True
    while running:
        SCREEN.blit(Define.Screen.BACKGROUND, (0, 0))
        SETTING_MOUSE_POS = pygame.mouse.get_pos()
        Setting_text = Define.get_font(100).render("SETTING", True, "#b68f40")
        Setting_rect = Setting_text.get_rect(center=(640, 100))
        SCREEN.blit(Setting_text, Setting_rect)

        BoardSize_Button = Button(pos=(640, 250), text_input="Board Size", font=Define.get_font(35), font_color="black", rect_width=450, rect_height=70)
        Player_Button = Button(pos=(640, 350), text_input="Player Name", font=Define.get_font(35), font_color="black", rect_width=450, rect_height=70)
        Sound_Button = Button(pos=(640, 450), text_input="Sound", font=Define.get_font(35), font_color="black", rect_width=450, rect_height=70)
        Back_Button = Button(pos=(640, 550), text_input="BACK", font=Define.get_font(35), font_color="black", rect_width=450, rect_height=70)

        for button in [BoardSize_Button, Sound_Button, Player_Button, Back_Button]:
            button.changeSize(SETTING_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BoardSize_Button.checkForInput(SETTING_MOUSE_POS):
                    SetBoardSize(SCREEN)
                if Sound_Button.checkForInput(SETTING_MOUSE_POS):
                    SetSound()
                if Player_Button.checkForInput(SETTING_MOUSE_POS):
                    SetPlayer(SCREEN)
                if Back_Button.checkForInput(SETTING_MOUSE_POS):
                    running = False
        pygame.display.update()