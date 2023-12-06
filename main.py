#thu vien
import pygame
from _add.game_setting import Board
from _scene.menu_scene import MenuScene
from _scene.setting_scene import SettingScene
from _scene.play_game_scene import PlayGameScene
from _scene.intro_scene import IntroScene
from _add.singleton import Singleton
#khoi tao game
pygame.init()

#khoi tao cac gia tri dau game
screen = Singleton.screen
pygame.display.set_caption(Board.GAME_CAPTION)
scene_manager = Singleton.scene_manager
# scene_manager.SwitchToScene('menu')
running = True
#game loop
scene_manager.SwitchToScene(IntroScene())
last_scene = Singleton.scenes
while running:
    if(last_scene != Singleton.scenes):
        last_scene = Singleton.scenes
        if(Singleton.scenes == 'intro'):
            scene_manager.SwitchToScene(IntroScene())
        elif(Singleton.scenes == 'menu'): 
            scene_manager.SwitchToScene(MenuScene())
        elif(Singleton.scenes == 'setting'):
            scene_manager.SwitchToScene(SettingScene())
        elif(Singleton.scenes == 'play_game'):
            scene_manager.SwitchToScene(PlayGameScene())
        print(scene_manager.current_scene)
    scene_manager.RunImplicitScene()
    
    for event in pygame.event.get():
        scene_manager.RunCurrentScene(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.time.Clock().tick(60)
    pygame.display.flip()

pygame.quit()
