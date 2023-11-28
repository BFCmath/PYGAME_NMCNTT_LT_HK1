#thu vien
import pygame
from game_setting import Board
from _scene.menu_scene import MenuScene
from _scene.setting_scene import SettingScene
from _scene.play_game_scene import PlayGameScene
from singleton import Singleton
#khoi tao game
pygame.init()

#khoi tao cac gia tri dau game
screen = Singleton.screen
pygame.display.set_caption(Board.GAME_CAPTION)
scene_manager = Singleton.scene_manager
# scene_manager.SwitchToScene('menu')
running = True
#game loop
scene_manager.SwitchToScene(MenuScene())
last_scene = Singleton.scenes
while running:
    for event in pygame.event.get():
        if(last_scene != Singleton.scenes):
            last_scene = Singleton.scenes
            if(Singleton.scenes == 0): 
                scene_manager.SwitchToScene(MenuScene())
            elif(Singleton.scenes == 1):
                scene_manager.SwitchToScene(SettingScene())
            elif(Singleton.scenes == 2):
                scene_manager.SwitchToScene(PlayGameScene())
            print(scene_manager.current_scene)
        scene_manager.RunCurrentScene(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.time.Clock().tick(60)
    pygame.display.flip()

pygame.quit()
