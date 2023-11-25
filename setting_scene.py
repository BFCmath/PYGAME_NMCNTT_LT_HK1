from scene import Scene
from setting_visual import SettingVisual
from game_setting import Settings
class SettingScene(Scene):

    def run_first_time(self,screen):
        SettingVisual(screen).draw_background()
        SettingVisual(screen).draw_settings()
        SettingVisual(screen).draw_caro_board_size()
        self.input_box1,self.input_box2 = SettingVisual(screen).draw_input_box_place()
        pass

    def run_all_time(self):
        # Menu specific update code
        pass