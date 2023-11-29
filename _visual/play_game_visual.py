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
    def get_turn_text(self,turn):
        text = Singleton.player_name[turn]
        text += "'s turn"
        return  text
    def draw_all_texts(self):
        self.print_text(self.get_turn_text(Singleton.turn), self.text_color, PlayGame.TURN_TEXT_POSITION, alignment="left")
        back_button =self.draw_button(self.screen,PlayGame.BACK_BUTTON_RECT, PlayGame.BACK_TEXT, PlayGame.TEXT_SIZE, PlayGame.FONT, PlayGame.BACK_BUTTON_COLOR, PlayGame.BACK_TEXT_COLOR)
        # self.print_text(back_text, self.text_color, PlayGame.BACK_TEXT_POSITION, alignment="right")
        self.print_text(PlayGame.PLAYER1_TEXT, self.text_color, PlayGame.PLAYER1_TEXT_POSITION, alignment="left")
        self.print_text(PlayGame.PLAYER2_TEXT, self.text_color, PlayGame.PLAYER2_TEXT_POSITION, alignment="right")
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
        
