#thu vien
import pygame
from GameSetting import Board
from MenuVisual import MenuVisual as MV
#khoi tao game
pygame.init()



caroBoardSetting = Board() 
screen = pygame.display.set_mode((caroBoardSetting.BOARD_WIDTH,caroBoardSetting.BOARD_HEIGHT))
pygame.display.set_caption(Board.GAME_CAPTION)
screen.fill(caroBoardSetting.BACKGROUND_COLOR)
menuVisual = MV(screen)


running = True

#game loop
while running:
    menuVisual.drawMenu()
    #xử lý sự kiện
    for event in pygame.event.get():
    #sự kiện thoát
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Phím Esc
                running = False
        
    pygame.display.update()

#thoát chương trình
pygame.quit()