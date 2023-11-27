from scene import Scene
import pygame
# from game_setting import Board
from play_game_visual import PlayGameVisual
from game_setting import Settings,PlayGame,Board
class PlayGameScene(Scene):
    def calculate_posi_list_and_edge():
        row_cells = Settings.row_cells
        col_cells = Settings.col_cells
        edge_size = min(PlayGame.CARO_BOARD_WIDTH // col_cells, PlayGame.CARO_BOARD_HEIGHT // row_cells)
        start_x = (Board.BOARD_WIDTH - (edge_size * col_cells)) / 2
        start_y = (Board.BOARD_HEIGHT - (edge_size * row_cells)) / 2

        # Generate the list of positions for each cell
        posi_list = [[(0, 0) for i in range(col_cells)] for j in range(row_cells)]
        for row in range(row_cells):
            for col in range(col_cells):
                top_left_x = start_x + col * edge_size
                top_left_y = start_y + row * edge_size
                posi_list[row][col] = [top_left_x, top_left_y]
        return edge_size, posi_list

    def run_first_time(self,screen):
        play_game_visual = PlayGameVisual(screen)
        # Call draw_background once, and then draw_all_texts every frame or when the text needs to update
        play_game_visual.draw_background()
        play_game_visual.draw_all_texts()
        edge_size, posi_list = PlayGameScene.calculate_posi_list_and_edge()
        play_game_visual.draw_caro_board(Settings.row_cells,Settings.col_cells,edge_size,posi_list)
        pass
    def run_all_time(self,event):
        # Menu specific update code
        pass