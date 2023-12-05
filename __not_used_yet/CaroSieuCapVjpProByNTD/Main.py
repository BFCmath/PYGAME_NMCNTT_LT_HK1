import pygame, Define
from Button import Button
from Setting_scene import Setting_scene
from PlayGame_scene import PlayGame_scene

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = Define.get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(pos=(640, 460), text_input="BACK", font=Define.get_font(75), font_color="black", rect_width=400, rect_height=70)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def main_menu():
    SCREEN.blit(Define.Screen.BACKGROUND, (0, 0))
    while True:
        

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        Menu_text = Define.get_font(100).render("MAIN MENU", True, "#b68f40")
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
                    PlayGame_scene(SCREEN)
                if Setting_Button.checkForInput(MENU_MOUSE_POS):
                    Setting_scene(SCREEN)
                if Help_Button.checkForInput(MENU_MOUSE_POS):
                    #Help_scene()
                    pass
                if Quit_Button.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()

        pygame.display.update()

main_menu()