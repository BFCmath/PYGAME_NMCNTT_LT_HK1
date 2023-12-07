import pygame
from game_setting import Menu, Board
from _visual.general_visual import GeneralVisual,Button
class MenuVisual(GeneralVisual):
    def __init__(self, screen):
        self.screen = screen
        self.background_color = Board().BACKGROUND_COLOR

    def draw_menu(self):
        self.draw_button(self.screen,Menu.TITLE_RECT, Menu.TITLE_TEXT,Menu.TITLE_TEXT_SIZE,Menu.FONT,Menu.BUTTON_COLOR,Menu.BUTTON_TEXT_COLOR)
        play_button = Button(self.screen,Menu.PLAY_BUTTON_RECT,Menu.PLAY_HOVER_BUTTON_RECT,Menu.PLAY_TEXT,Menu.PLAY_BUTTON_SIZE,Menu.FONT,Menu.BUTTON_TEXT_COLOR,self.background_color,Menu.BUTTON_COLOR)
        setting_button = Button(self.screen,Menu.SETTINGS_BUTTON_RECT,Menu.SETTINGS_HOVER_BUTTON_RECT,Menu.SETTINGS_TEXT,Menu.SETTINGS_BUTTON_SIZE,Menu.FONT,Menu.BUTTON_TEXT_COLOR,self.background_color,Menu.BUTTON_COLOR)
        quit_button = Button(self.screen,Menu.QUIT_BUTTON_RECT,Menu.QUIT_HOVER_BUTTON_RECT,Menu.QUIT_TEXT,Menu.QUIT_BUTTON_SIZE,Menu.FONT,Menu.BUTTON_TEXT_COLOR,self.background_color,Menu.BUTTON_COLOR)
        # ve button
        pygame.display.update()
        return play_button,setting_button,quit_button
        
    def draw_background(self):
        self.screen.fill(self.background_color)
        pygame.display.update()

