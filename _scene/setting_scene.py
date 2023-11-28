from scene import Scene
import pygame
from _visual.setting_visual import SettingVisual
from _logic.setting_logic import SettingLogic
class SettingScene(Scene):

    def run_first_time(self,screen):
        self.setting_visual = SettingVisual(screen)

        self.setting_visual.draw_background()
        self.back_button = self.setting_visual.draw_settings()

        self.setting_visual.draw_caro_board_size()
        self.input_box1,self.input_box2 = self.setting_visual.draw_input_box_place()

        self.setting_logic = SettingLogic(self.back_button,self.input_box1,self.input_box2)
        self.setting_visual.draw_number_in_text_box(self.setting_logic.input_values[0], self.input_box1)
        self.setting_visual.draw_number_in_text_box(self.setting_logic.input_values[1], self.input_box2)
        pass

    def run_all_time(self,event):
        self.setting_logic.handle_event(event)
        pass