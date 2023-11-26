from scene import Scene
# from game_setting import Board
from play_game_visual import PlayGameVisual

class PlayGameScene(Scene):
    def run_first_time(self,screen):
        play_game_visual = PlayGameVisual(screen)
        # Call draw_background once, and then draw_all_texts every frame or when the text needs to update
        play_game_visual.draw_background()
        play_game_visual.draw_all_texts()
        pass
    def run_all_time(self,event):
        # Menu specific update code
        pass