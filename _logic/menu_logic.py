# setting_logic.py
import pygame
from _add.singleton import Singleton
class MenuLogic:
    def __init__(self,screen, play_button,setting_button,quit_button):
        self.play_button = play_button
        self.setting_button = setting_button
        self.quit_button = quit_button
        self.screen = screen
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button.collidepoint(event.pos):
                Singleton.scenes = 'play_game'
            elif self.setting_button.collidepoint(event.pos):
                Singleton.scenes = 'setting'
            elif self.quit_button.collidepoint(event.pos):
                pygame.quit()
                quit()

