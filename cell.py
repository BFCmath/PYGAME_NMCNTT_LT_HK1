import pygame 
from game_setting import CellSetting 
from singleton import Singleton
class Cell:
    def __init__(self, edge_size, position_center_x, position_center_y):
        self.edge_size = edge_size
        self.position_center_x = position_center_x+edge_size/2
        self.position_center_y = position_center_y+edge_size/2
        # Calculate the top-left corner based on the center position and edge size
        self.top_left_x = position_center_x
        self.top_left_y = position_center_y
        # Define the rectangle representing the cell
        self.rect = pygame.Rect(self.top_left_x, self.top_left_y, edge_size, edge_size)
        self.content = None  # Can be 'X', 'O', or None

    def draw_cell(self, screen):
        # Draw the cell as a rectangle
        pygame.draw.rect(screen, CellSetting().CELL_COLOR, self.rect)
        pygame.draw.rect(screen,CellSetting().EDGE_COLOR, self.rect, 1)

    def check_click(self, mouse_pos):
        if(self.rect.collidepoint(mouse_pos)):
            self.draw_sign()
            return True
        return False

    def draw_sign(self):
        if self.content is None: 
            if(Singleton.turn==0):
                _color = CellSetting.SIGN_COLOR[Singleton.turn]
                Singleton.turn =1
                self.content = 'X'
            else:
                _color = CellSetting.SIGN_COLOR[Singleton.turn]
                Singleton.turn = 0
                self.content = 'O'
           # Set the font for rendering the 'X'
            self.font = pygame.font.Font(CellSetting.SIGN_FONT, self.edge_size)  # Make sure PlayGame.FONT points to a valid font file

            # Render the 'X' text
            text_surf = self.font.render(self.content, True, _color)  # PlayGame.TEXT_COLOR should be a valid color tuple

            # Calculate the position to center the 'X' in the cell
            text_rect = text_surf.get_rect(center=(self.position_center_x, self.position_center_y))

            # Blit the text onto the screen at the calculated position
            Singleton.screen.blit(text_surf, text_rect)
            pygame.display.update(self.rect)
