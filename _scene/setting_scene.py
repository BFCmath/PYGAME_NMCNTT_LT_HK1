from _scene.scene import Scene
import pygame
from _visual.setting_visual import SettingVisual
from _logic.setting_logic import SettingLogic
class SettingScene(Scene):

    def run_first_time(self,screen):
        self.setting_visual = SettingVisual(screen)

        self.setting_visual.draw_background()
        self.back_button = self.setting_visual.draw_settings()
        self.setting_visual.draw_name()
        self.setting_visual.draw_caro_board_size()
        self.size_input_box_1,self.size_input_box_2 = self.setting_visual.draw_input_box_place()
        self.name_input_box_1,self.name_input_box_2 = self.setting_visual.draw_name_input_box()

        self.setting_logic = SettingLogic(self.back_button,self.size_input_box_1,self.size_input_box_2,self.name_input_box_1,self.name_input_box_2)
        pass

    def run_all_time(self,event):
        self.setting_logic.handle_event(event)
        pass