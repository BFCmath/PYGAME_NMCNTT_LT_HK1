# setting_logic.py
import pygame
from singleton import Singleton
class PlayGameLogic:
    def __init__(self,screen, back_button):
        self.back_button = back_button
        self.screen = screen
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.collidepoint(event.pos):
                Singleton.scenes = 0

