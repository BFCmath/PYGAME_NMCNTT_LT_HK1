from scene_management import SceneManagement
import pygame
from game_setting import Board

class Singleton:
    screen = pygame.display.set_mode((Board().BOARD_WIDTH,Board().BOARD_HEIGHT))
    scene_manager = SceneManagement(screen)
    scenes = 0