from _scene.scene import Scene
from _add.game_setting import Board
from _visual.menu_visual import MenuVisual
from _logic.menu_logic import MenuLogic

class MenuScene(Scene):
    def run_first_time(self,screen):
        MenuVisual(screen).draw_background()
        self.play_button,self.setting_button,self.quit_button = MenuVisual(screen).draw_menu()
        self.menu_logic = MenuLogic(screen,self.play_button,self.setting_button,self.quit_button)
        pass

    def run_all_time(self,event):
        self.menu_logic.handle_event(event)
        pass