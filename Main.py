#thu vien
import pygame
from game_setting import Board
from scene_management import SceneManagement

def main():
    #khoi tao game
    pygame.init()
    
    #khoi tao cac gia tri dau game
    caro_board_setting = Board() 
    screen = pygame.display.set_mode((caro_board_setting.BOARD_WIDTH,caro_board_setting.BOARD_HEIGHT))
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
                elif event.key == pygame.K_SPACE:
                    scene_manager.SwitchToScene('setting')
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()