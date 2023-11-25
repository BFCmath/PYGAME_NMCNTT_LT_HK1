from scene import Scene
import pygame
from setting_visual import SettingVisual
from setting_logic import SettingLogic
class SettingScene(Scene):

    def run_first_time(self,screen):
        self.setting_visual = SettingVisual(screen)
        self.setting_visual.draw_background()
        self.setting_visual.draw_settings()
        self.setting_visual.draw_caro_board_size()
        self.input_box1,self.input_box2 = self.setting_visual.draw_input_box_place()
        self.setting_logic = SettingLogic(self.input_box1,self.input_box2)
        self.setting_visual.draw_number_in_text_box(3, self.input_box1)
        self.setting_visual.draw_number_in_text_box(3, self.input_box2)

        pass

    def run_all_time(self,event):
        # print("run all time\n")
        active_box = self.setting_logic.handle_event(event)
        if(active_box!=None):
            if(active_box==1):
                self.setting_visual.draw_number_in_text_box(self.setting_logic.get_input_values()[1], self.input_box1)
            elif(active_box==2):
                self.setting_visual.draw_number_in_text_box(self.setting_logic.get_input_values()[2], self.input_box2)
        pass