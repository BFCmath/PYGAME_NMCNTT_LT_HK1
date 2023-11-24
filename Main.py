#thu vien
import pygame
from game_setting import Board
from scene_management import SceneManagement

def main():
    #khoi tao game
    pygame.init()

    caroBoardSetting = Board() 
    screen = pygame.display.set_mode((caroBoardSetting.BOARD_WIDTH,caroBoardSetting.BOARD_HEIGHT))
    pygame.display.set_caption(Board.GAME_CAPTION)


    scene_manager = SceneManagement(screen)

    running = True
    #game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
    pygame.quit()

if __name__ == '__main__':
    main()