import pygame
from game_setting import Settings,Board

class SettingVisual:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(Settings.FONT, 32)  # Adjust the size as needed
        self.horizontal_cells = 5  # Default value
        self.vertical_cells = 5  # Default value

    def draw_caro_board_size(self):
        self.draw_button(Settings.SETTINGS_BOARD_SIZE_RECT, Settings.SETTINGS_BOARD_SIZE_TEXT,Settings.SETTINGS_BOARD_SIZE_TEXT_SIZE)


    def draw_input_box(self, input_box_rect):
        box_rect = pygame.Rect(input_box_rect)
        pygame.draw.rect(self.screen, Settings.SETTINGS_INPUT_BOX_COLOR, box_rect, 2) 
        return box_rect
            
    def draw_button(self, rect, text, size):
        self.font = pygame.font.Font(Settings.FONT, size)
        pygame.draw.rect(self.screen, Settings.SETTINGS_BUTTON_COLOR, rect)
        _text_surf = self.font.render(text, True, Settings.SETTINGS_BUTTON_TEXT_COLOR)
        _text_rect = _text_surf.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.screen.blit(_text_surf, _text_rect)
    def draw_x(self):
        self.font = pygame.font.Font(Settings.FONT, Settings.SETTINGS_X_SIZE)
        _text_surf = self.font.render('X', True, Settings.SETTINGS_BUTTON_TEXT_COLOR)
        _text_rect = _text_surf.get_rect(center=(Settings.SETTINGS_X_PLACE[0]*Board.BOARD_WIDTH, Settings.SETTINGS_X_PLACE[1]*Board.BOARD_HEIGHT))
        self.screen.blit(_text_surf, _text_rect)
    def draw_settings(self):
        self.draw_button(Settings.SETTINGS_TITLE_RECT, Settings.SETTINGS_TITLE_TEXT,Settings.SETTINGS_TITLE_TEXT_SIZE)
        self.draw_button(Settings.SETTINGS_BACK_BUTTON_RECT, Settings.SETTINGS_BACK_TEXT,Settings.SETTINGS_BACK_BUTTON_SIZE)
        # ve button
        pygame.display.update()
    def draw_input_box_place(self):
        box1 = self.draw_input_box(Settings.SETTINGS_INPUT_BOX_RECT_1)
        box2= self.draw_input_box(Settings.SETTINGS_INPUT_BOX_RECT_2)
        self.draw_x()
        pygame.display.update()
        return box1,box2
    def draw_background(self):
        self.screen.fill(Settings.SETTINGS_COLOR)
        pygame.display.update()