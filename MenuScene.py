from Scene import Scene
from GameSetting import Board
from MenuVisual import MenuVisual

class MenuScene(Scene):
    def RunFirstRime(self,screen):
        MenuVisual(screen).DrawBackGround()
        MenuVisual(screen).DrawMenu()
        pass

    def RunAllRime(self):
        # Menu specific update code
        pass