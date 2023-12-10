# setting_logic.py
import pygame
from _add.game_setting import PlayGame,Board
from _add.singleton import Singleton
from _add.cell import Cell
from _logic.check_win_logic import *

class PlayGameLogic:
    def __init__(self,screen, back_button, cell_list):
        self.back_button = back_button
        self.screen = screen
        self.cell_list = cell_list 
        self.row_cells = Singleton.caro_board_size[0]
        self.col_cells = Singleton.caro_board_size[1]
        self.logic_caro_board = [[(0) for i in range(self.col_cells)] for j in range(self.row_cells)]
        self.cnt_p = [[[[(0) for l in range(2)] for k in range(8)] for j in range(self.col_cells)] for i in range(self.row_cells)]
        self.wins = []
    def calculate_posi_list_and_edge(row_cells,col_cells):
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

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.collidepoint(event.pos):
                Singleton.scenes = 'menu'
            turn_changed = self.handle_caro_board_logic(event)
            return turn_changed

    def handle_caro_board_logic(self, event):
        for row in range(self.row_cells):
            for col in range(self.col_cells):
                content = self.cell_list[row][col].check_click(event.pos)
                if content == None: continue
                print(row,col)
                self.logic_caro_board[row][col]=-1 if content == 'O' else 1
                self.win_logic(row,col)
                self.change_turn()
                return True
        return False        
        
    def win_logic(self, row,col):
        check_win(self.row_cells, self.col_cells, row, col, self.cnt_p, Singleton.turn, self.wins)
        if len(self.wins) > 0:
            # print(self.logic_caro_board)
            for [start, end] in self.wins:
                print(start, end, "\n")
            print(Singleton.player_name[Singleton.turn],"win")

    def change_turn(self):
        Singleton.turn = 1 if Singleton.turn == 0 else 0