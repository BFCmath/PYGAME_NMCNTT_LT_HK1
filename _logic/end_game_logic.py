# setting_logic.py
import pygame
from singleton import Singleton
from _visual.general_visual import Button
class EndGameLogic:
    def __init__(self,screen, play_again_button,setting_button,quit_button):
        self.play_again_button = play_again_button
        self.setting_button = setting_button
        self.quit_button = quit_button
        self.screen = screen
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_again_button.check_collide(event.pos):
                Singleton.scenes = 'play_game'
            elif self.setting_button.check_collide(event.pos):
                Singleton.scenes = 'setting'
            elif self.quit_button.check_collide(event.pos):
                pygame.quit()
                quit()
        self.play_again_button.check_hover(pygame.mouse.get_pos())
        self.setting_button.check_hover(pygame.mouse.get_pos())
        self.quit_button.check_hover(pygame.mouse.get_pos())

