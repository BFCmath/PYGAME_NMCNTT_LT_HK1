from _scene.scene import Scene
# from game_setting import Board
from _visual.play_game_visual import PlayGameVisual
from _logic.play_game_logic import PlayGameLogic
from _add.singleton import Singleton
class PlayGameScene(Scene):
    def run_first_time(self,screen):
        self.play_game_visual = PlayGameVisual(screen)
        # Call draw_background once, and then draw_all_texts every frame or when the text needs to update
        self.play_game_visual.draw_background()
        self.back_button = self.play_game_visual.draw_all_texts()

        edge_size, posi_list = PlayGameLogic.calculate_posi_list_and_edge(Singleton.caro_board_size[0],Singleton.caro_board_size[1])
        self.cell_list = self.play_game_visual.draw_caro_board(Singleton.caro_board_size[0],Singleton.caro_board_size[1],edge_size,posi_list)
        self.play_game_logic = PlayGameLogic(screen,self.back_button, self.cell_list)
        pass
    def run_all_time(self,event):
        # Menu specific update code
        turn_changed = self.play_game_logic.handle_event(event)
        if turn_changed: self.play_game_visual.draw_turn_text(Singleton.turn)
        pass