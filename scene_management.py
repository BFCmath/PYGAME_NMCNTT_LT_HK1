# from _scene.menu_scene import MenuScene
# from _scene.setting_scene import SettingScene
# from _scene.play_game_scene import PlayGameScene
# from singleton import Singleton 
class SceneManagement:
    def __init__(self, screen):
        # self.scenes = {
        #     'menu': MenuScene(),
        #     'setting': SettingScene(),
        #     'play_game': PlayGameScene()
        # }
        self.screen = screen
        self.current_scene = None

    def SwitchToScene(self, scene):
        self.current_scene = scene
        self.current_scene.run_first_time(self.screen)
        # Singleton.change = True

    def RunCurrentScene(self,event):
        self.current_scene.run_all_time(event)
