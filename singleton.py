from scene_management import SceneManagement
import pygame
from game_setting import Board

class Singleton:
    screen = pygame.display.set_mode((Board().BOARD_WIDTH,Board().BOARD_HEIGHT))
    scene_manager = SceneManagement(screen)
    scenes = 0
    row_cell = 20
    col_cell = 20
    turn = 0
    player_name = ['Player 1','Player 2']