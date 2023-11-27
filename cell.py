import pygame 
from game_setting import CellSetting 
class Cell:
    def __init__(self, edge_size, position_center_x, position_center_y):
        self.edge_size = edge_size
        self.position_center_x = position_center_x
        self.position_center_y = position_center_y
        # Calculate the top-left corner based on the center position and edge size
        top_left_x = position_center_x - edge_size // 2
        top_left_y = position_center_y - edge_size // 2
        # Define the rectangle representing the cell
        self.rect = pygame.Rect(top_left_x, top_left_y, edge_size, edge_size)
        self.content = None  # Can be 'X', 'O', or None

    def draw_cell(self, screen):
        # Draw the cell as a rectangle
        pygame.draw.rect(screen, CellSetting().CELL_COLOR, self.rect)
        pygame.draw.rect(screen,CellSetting().EDGE_COLOR, self.rect, 1)

    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

