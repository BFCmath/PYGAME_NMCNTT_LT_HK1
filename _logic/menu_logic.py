# setting_logic.py
import pygame
from _scene.setting_scene import SettingScene
from _scene.play_game_scene import PlayGameScene
from singleton import Singleton
class MenuLogic:
    def __init__(self,screen, play_button,setting_button):
        self.play_button = play_button
        self.setting_button = setting_button
        self.screen = screen
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button.collidepoint(event.pos):
                Singleton.scenes = 2
            elif self.setting_button.collidepoint(event.pos):
                Singleton.scenes = 1

