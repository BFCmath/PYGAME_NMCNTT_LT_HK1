import pygame, Define
from Button import Button
from Setting_scene import Setting_scene
from PlayGame_scene import PlayGame_scene

def main_menu(SCREEN):
    while True:        
        SCREEN.blit(Define.Screen.BACKGROUND, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        Menu_text = Define.get_font(100).render("MAIN MENU", True, "#696969")
        Menu_rect = Menu_text.get_rect(center=(640, 100))

        PlayGame_Button = Button(pos=(640, 250), text_input="Play Game", font=Define.get_font(35), font_color="black", rect_width=400, rect_height=70)
        Setting_Button = Button(pos=(640, 350), text_input="Setting", font=Define.get_font(35),font_color="black", rect_width=400, rect_height=70)
        Help_Button = Button(pos=(640, 450), text_input="Help", font=Define.get_font(35), font_color="black", rect_width=400, rect_height=70)
        Quit_Button = Button(pos=(640, 550), text_input="QUIT", font=Define.get_font(35),font_color="black", rect_width=400, rect_height=70)
        SCREEN.blit(Menu_text, Menu_rect)

        for button in [PlayGame_Button, Setting_Button, Help_Button, Quit_Button]:
            button.changeSize(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PlayGame_Button.checkForInput(MENU_MOUSE_POS):
                    # Define.Sound.BACKGROUND_MUSIC.stop()
                    PlayGame_scene(SCREEN)
                if Setting_Button.checkForInput(MENU_MOUSE_POS):
                    Setting_scene(SCREEN)
                if Help_Button.checkForInput(MENU_MOUSE_POS):
                    #Help_scene()
                    pass
                if Quit_Button.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()

        pygame.display.update()
