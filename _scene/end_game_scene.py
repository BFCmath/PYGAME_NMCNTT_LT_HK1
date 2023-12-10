from scene import Scene
from _visual.end_game_visual import EndGameVisual
from _logic.end_game_logic import EndGameLogic
class EndGameScene(Scene):
    def run_first_time(self,screen):
        EndGameVisual(screen).draw_background()
        self.play_again_button,self.setting_button,self.quit_button = EndGameVisual(screen).draw_menu()
        self.end_game_logic = EndGameLogic(screen,self.play_again_button,self.setting_button,self.quit_button)
        pass
    def run_all_time(self,event):
        self.end_game_logic.handle_event(event)
        pass