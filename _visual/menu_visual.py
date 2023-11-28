import pygame
from game_setting import Menu, Board
from _visual.general_visual import GeneralVisual
class MenuVisual(GeneralVisual):
    def __init__(self, screen):
        self.screen = screen

    def draw_menu(self):
        self.draw_button(self.screen,Menu.TITLE_RECT, Menu.TITLE_TEXT,Menu.TITLE_TEXT_SIZE,Menu.FONT,Menu.BUTTON_COLOR,Menu.BUTTON_TEXT_COLOR)
        play_button = self.draw_button(self.screen,Menu.PLAY_BUTTON_RECT, Menu.PLAY_TEXT,Menu.PLAY_BUTTON_SIZE,Menu.FONT,Menu.BUTTON_COLOR,Menu.BUTTON_TEXT_COLOR)
        setting_button = self.draw_button(self.screen,Menu.SETTINGS_BUTTON_RECT, Menu.SETTINGS_TEXT,Menu.SETTINGS_BUTTON_SIZE,Menu.FONT,Menu.BUTTON_COLOR,Menu.BUTTON_TEXT_COLOR)
        # ve button
        pygame.display.update()
        return play_button,setting_button
        
    def draw_background(self):
        self.screen.fill(Board().BACKGROUND_COLOR)
        pygame.display.update()

