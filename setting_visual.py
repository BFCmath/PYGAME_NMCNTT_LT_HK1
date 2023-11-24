import pygame
from game_setting import Settings


class SettingVisual:
    def __init__(self, screen):
        self.screen = screen
        
    def draw_button(self, rect, text, size):
        self.font = pygame.font.Font(None, size)
        pygame.draw.rect(self.screen, Settings.SETTINGS_BUTTON_COLOR, rect)
        _text_surf = self.font.render(text, True, Settings.SETTINGS_BUTTON_TEXT_COLOR)
        _text_rect = _text_surf.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.screen.blit(_text_surf, _text_rect)
    def draw_settings(self):
        self.draw_button(Settings.SETTINGS_TITLE_RECT, Settings.SETTINGS_TITLE_TEXT,Settings.SETTINGS_TITLE_TEXT_SIZE)
        self.draw_button(Settings.SETTINGS_BACK_BUTTON_RECT, Settings.SETTINGS_BACK_TEXT,Settings.SETTINGS_BACK_BUTTON_SIZE)
        # ve button
        pygame.display.update()
        
    def draw_background(self):
        self.screen.fill(Settings.SETTINGS_COLOR)
        pygame.display.update()