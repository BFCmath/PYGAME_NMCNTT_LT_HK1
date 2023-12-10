import pygame
from game_setting import EndGame, Board
from _visual.general_visual import GeneralVisual,Button
class EndGameVisual(GeneralVisual):
    def __init__(self, screen):
        self.screen = screen
        self.background_color = EndGame().END_GAME_BACKGROUND_COLOR

    def draw_menu(self):
        play_again_button = Button(self.screen,EndGame.PLAY_AGAIN_BUTTON_RECT,EndGame.PLAY_AGAIN_HOVER_BUTTON_RECT,EndGame.PLAY_AGAIN_TEXT,EndGame.PLAY_AGAIN_BUTTON_SIZE,EndGame.FONT,EndGame.BUTTON_TEXT_COLOR,self.background_color,EndGame.BUTTON_COLOR)
        setting_button = Button(self.screen,EndGame.SETTINGS_BUTTON_RECT,EndGame.SETTINGS_HOVER_BUTTON_RECT,EndGame.SETTINGS_TEXT,EndGame.SETTINGS_BUTTON_SIZE,EndGame.FONT,EndGame.BUTTON_TEXT_COLOR,self.background_color,EndGame.BUTTON_COLOR)
        quit_button = Button(self.screen,EndGame.QUIT_BUTTON_RECT,EndGame.QUIT_HOVER_BUTTON_RECT,EndGame.QUIT_TEXT,EndGame.QUIT_BUTTON_SIZE,EndGame.FONT,EndGame.BUTTON_TEXT_COLOR,self.background_color,EndGame.BUTTON_COLOR)
        # ve button
        pygame.display.update()
        return play_again_button,setting_button,quit_button
        
    def draw_background(self):
        self.screen.fill(self.background_color)
        pygame.display.update()

