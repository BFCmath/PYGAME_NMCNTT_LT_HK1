from scene import Scene
from setting_visual import SettingVisual

class SettingScene(Scene):
    def run_first_time(self,screen):
        SettingVisual(screen).draw_background()
        SettingVisual(screen).draw_settings()
        pass

    def run_all_time(self):
        # Menu specific update code
        pass