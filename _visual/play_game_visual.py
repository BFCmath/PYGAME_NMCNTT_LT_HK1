import pygame
from game_setting import PlayGame, Board
import cell
from _visual.general_visual import GeneralVisual
from singleton import Singleton
class PlayGameVisual(GeneralVisual):
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(PlayGame.FONT, PlayGame.TEXT_SIZE)  
        self.text_color = PlayGame.TEXT_COLOR
        # Use the default font and a size of 32

    def print_text(self, text, color, position, alignment="left"):
        text_surface = self.font.render(text, True, color)  # Render the text
        text_rect = text_surface.get_rect()
        if alignment == "left":
            text_rect.topleft = position
        elif alignment == "right":
            text_rect.topright = position
        elif alignment == "center":
            text_rect.center = position
        self.screen.blit(text_surface, text_rect)  # Blit the text surface to the screen
    def draw_turn_text(self,turn):
        print(Singleton.turn)
        pygame.draw.rect(self.screen, PlayGame.BACKGROUND_COLOR, (0,0,Board.BOARD_WIDTH//2,40))
        text = Singleton.player_name[turn]
        text += "'s turn"
        self.print_text(text, self.text_color, PlayGame.TURN_TEXT_POSITION, alignment="left")

    def draw_all_texts(self):
        self.draw_turn_text(Singleton.turn)
        back_button =self.draw_button(self.screen,PlayGame.BACK_BUTTON_RECT, PlayGame.BACK_TEXT, PlayGame.TEXT_SIZE, PlayGame.FONT, PlayGame.BACK_BUTTON_COLOR, PlayGame.BACK_TEXT_COLOR)
        # self.print_text(back_text, self.text_color, PlayGame.BACK_TEXT_POSITION, alignment="right")
        _player1_text = Singleton.player_name[0] + ': X'
        _player2_text = Singleton.player_name[1] + ': O'
        self.print_text(_player1_text, self.text_color, PlayGame.PLAYER1_TEXT_POSITION, alignment="left")
        self.print_text(_player2_text, self.text_color, PlayGame.PLAYER2_TEXT_POSITION, alignment="right")
        pygame.display.update()
        return back_button  

    def draw_background(self):
        self.screen.fill(PlayGame.BACKGROUND_COLOR)
    def draw_caro_board(self,number_row,number_col,cell_edge,posi_list):
        cell_list = [[None for i in range(number_col)] for j in range(number_row)]
        for i in range(number_row):
            for j in range(number_col):
                cell_list[i][j] = cell.Cell(cell_edge,posi_list[i][j][0],posi_list[i][j][1])
                cell_list[i][j].draw_cell(self.screen)
        pygame.display.update()
        return cell_list
        
