import pygame
from _scene.scene_management import SceneManagement
from _add.game_setting import Board

class Singleton:
    screen = pygame.display.set_mode((Board().BOARD_WIDTH,Board().BOARD_HEIGHT))
    scene_manager = SceneManagement(screen)
    scenes = 'intro' #intro,menu,setting,play_game
    caro_board_size = [10,10]
    string_caro_board_size = [str(caro_board_size[0]), str(caro_board_size[1])]
    turn = 0
    player_name = ['Player 1','Player 2']