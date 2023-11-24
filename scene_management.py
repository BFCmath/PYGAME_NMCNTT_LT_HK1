from menu_scene import MenuScene
# SceneManagement.py
class SceneManagement:
    def __init__(self, screen):
        self.scenes = {
            'menu': MenuScene(),
            # ... other scenes ...
        }
        self.screen = screen
        self.current_scene = self.scenes['menu']
        self.current_scene.RunFirstRime(screen)

    def SwitchToScene(self, scene_name):
        self.current_scene = self.scenes[scene_name]
        self.current_scene.RunFirstRime()

    def RunCurrentScene(self):
        if self.current_scene is not None:
            self.current_scene.RunAllRime()
