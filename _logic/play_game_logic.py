# setting_logic.py
import pygame
from singleton import Singleton
from game_setting import PlayGame,Board
from singleton import Singleton
from cell import Cell
from check_win_logic import check_win
class PlayGameLogic:
    def __init__(self,screen, back_button, cell_list):
        self.back_button = back_button
        self.screen = screen
        self.cell_list = cell_list 
        self.row_cells =  Singleton.row_cell
        self.col_cells =  Singleton.col_cell
        self.logic_caro_board = [[(0) for i in range(self.col_cells)] for j in range(self.row_cells)]
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
                Singleton.scenes = 0
            self.handle_caro_board_logic(event)

    def handle_caro_board_logic(self,event):
        for row in range(self.row_cells):
            for col in range(self.col_cells):
                content = self.cell_list[row][col].check_click(event.pos)
                if content == 'O':
                    print(row,col)
                    self.logic_caro_board[row][col]=-1
                    self.win_logic(row,col)
                    self.change_turn()
                elif content == 'X':
                    print(row,col)
                    self.logic_caro_board[row][col]=1
                    self.win_logic(row,col)
                    self.change_turn()
    def win_logic(self,row,col):
        turn = 1 if Singleton.turn == 1 else -1
        if(check_win(turn,row,col,self.logic_caro_board,self.row_cells,self.col_cells)):
            # print(self.logic_caro_board)
            print("win")
    def change_turn(self):
        Singleton.turn = 1 if Singleton.turn == 0 else 0