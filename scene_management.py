from menu_scene import MenuScene
from setting_scene import SettingScene
# SceneManagement.py
class SceneManagement:
    def __init__(self, screen):
        self.scenes = {
            'menu': MenuScene(),
            'setting': SettingScene()
        }
        self.screen = screen
        self.current_scene = self.scenes['menu']
        self.current_scene.run_first_time(screen)

    def SwitchToScene(self, scene_name):
        self.current_scene = self.scenes[scene_name]
        self.current_scene.run_first_time(self.screen)

    def RunCurrentScene(self):
        if self.current_scene is not None:
            self.current_scene.run_all_time()
