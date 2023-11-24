from scene import Scene
from game_setting import Board
from menu_visual import MenuVisual

class MenuScene(Scene):
    def RunFirstRime(self,screen):
        MenuVisual(screen).DrawBackGround()
        MenuVisual(screen).DrawMenu()
        pass

    def RunAllRime(self):
        # Menu specific update code
        pass