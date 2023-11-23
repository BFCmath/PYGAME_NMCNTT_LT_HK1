import pygame
from GameSetting import Menu

class MenuVisual:
    def __init__(self, screen):
        self.screen = screen
        

    def drawButton(self, rect, text, size):
        self.font = pygame.font.Font(None, size)
        pygame.draw.rect(self.screen, Menu.BUTTON_COLOR, rect)
        textSurf = self.font.render(text, True, Menu.BUTTON_TEXT_COLOR)
        textRect = textSurf.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.screen.blit(textSurf, textRect)

    def drawMenu(self):
        self.drawButton(Menu.TITLE_RECT, Menu.TITLE_TEXT,Menu.TITLE_TEXT_SIZE)
        self.drawButton(Menu.PLAY_BUTTON_RECT, Menu.PLAY_TEXT,Menu.PLAY_BUTTON_SIZE)
        self.drawButton(Menu.SETTINGS_BUTTON_RECT, Menu.SETTINGS_TEXT,Menu.SETTINGS_BUTTON_SIZE)
        # ve button
        pygame.display.flip()