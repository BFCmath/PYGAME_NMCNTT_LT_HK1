from scene import Scene
from game_setting import Board
from menu_visual import MenuVisual

class MenuScene(Scene):
    def run_first_time(self,screen):
        MenuVisual(screen).draw_background()
        MenuVisual(screen).draw_menu()
        pass

    def run_all_time(self):
        # Menu specific update code
        pass