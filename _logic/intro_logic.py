# setting_logic.py
import pygame
from _add.singleton import Singleton
from _add.game_setting import Intro
class IntroLogic:
    def __init__(self):
        self.loading_time = Intro.LOADING_TIME
        self.start_time = pygame.time.get_ticks()  # Get the start time
        pass
    
    def handle_implicit_event(self):
        self.elapsed_time = pygame.time.get_ticks() - self.start_time
        return self.elapsed_time
    def check_time(self):
        if self.elapsed_time > self.loading_time:
            Singleton.scenes = 'menu'
            
