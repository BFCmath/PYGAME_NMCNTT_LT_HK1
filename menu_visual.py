import pygame
from game_setting import Menu, Board

class MenuVisual:
    def __init__(self, screen):
        self.screen = screen
            
    def draw_button(self, rect, text, size):
        self.font = pygame.font.Font(Menu.FONT, size)
        pygame.draw.rect(self.screen, Menu.BUTTON_COLOR, rect)
        _text_surf = self.font.render(text, True, Menu.BUTTON_TEXT_COLOR)
        _text_rect = _text_surf.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.screen.blit(_text_surf, _text_rect)

    def draw_menu(self):
        self.draw_button(Menu.TITLE_RECT, Menu.TITLE_TEXT,Menu.TITLE_TEXT_SIZE)
        self.draw_button(Menu.PLAY_BUTTON_RECT, Menu.PLAY_TEXT,Menu.PLAY_BUTTON_SIZE)
        self.draw_button(Menu.SETTINGS_BUTTON_RECT, Menu.SETTINGS_TEXT,Menu.SETTINGS_BUTTON_SIZE)
        # ve button
        pygame.display.update()
        
    def draw_background(self):
        self.screen.fill(Board().BACKGROUND_COLOR)
        pygame.display.update()

