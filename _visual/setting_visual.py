import pygame
from _visual.general_visual import GeneralVisual
from game_setting import Settings,Board

class SettingVisual(GeneralVisual):
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(Settings.FONT, 32)  # Adjust the size as needed
        self.horizontal_cells = 5  # Default value
        self.vertical_cells = 5  # Default value

    def draw_caro_board_size(self):
        self.draw_button(self.screen,Settings.SETTINGS_BOARD_SIZE_RECT, Settings.SETTINGS_BOARD_SIZE_TEXT,Settings.SETTINGS_BOARD_SIZE_TEXT_SIZE,Settings.FONT,Settings.SETTINGS_BUTTON_COLOR,Settings.SETTINGS_BUTTON_TEXT_COLOR)
    def draw_x(self):
        self.font = pygame.font.Font(Settings.FONT, Settings.SETTINGS_X_SIZE)
        _text_surf = self.font.render('X', True, Settings.SETTINGS_BUTTON_TEXT_COLOR)
        _text_rect = _text_surf.get_rect(center=(Settings.SETTINGS_X_PLACE[0]*Board.BOARD_WIDTH, Settings.SETTINGS_X_PLACE[1]*Board.BOARD_HEIGHT))
        self.screen.blit(_text_surf, _text_rect)
    def draw_settings(self):
        self.draw_button(self.screen,Settings.SETTINGS_TITLE_RECT, Settings.SETTINGS_TITLE_TEXT,Settings.SETTINGS_TITLE_TEXT_SIZE,Settings.FONT,Settings.SETTINGS_BUTTON_COLOR,Settings.SETTINGS_BUTTON_TEXT_COLOR)
        back_button = self.draw_button(self.screen,Settings.SETTINGS_BACK_BUTTON_RECT, Settings.SETTINGS_BACK_TEXT,Settings.SETTINGS_BACK_BUTTON_SIZE,Settings.FONT,Settings.SETTINGS_BUTTON_COLOR,Settings.SETTINGS_BUTTON_TEXT_COLOR)
        # ve button
        pygame.display.update()
        return back_button
    def draw_input_box_place(self):
        self.box1 = self.draw_input_box(self.screen,Settings.SETTINGS_INPUT_BOX_RECT_1,Settings.SETTINGS_INPUT_BOX_COLOR)
        self.box2= self.draw_input_box(self.screen,Settings.SETTINGS_INPUT_BOX_RECT_2,Settings.SETTINGS_INPUT_BOX_COLOR)
        self.draw_x()
        pygame.display.update()
        return self.box1,self.box2
    def draw_background(self):
        self.screen.fill(Settings.SETTINGS_COLOR)
        pygame.display.update()
    def draw_number_in_text_box(self, number, input_box_rect):
        pygame.draw.rect(self.screen, Settings.SETTINGS_COLOR, input_box_rect)
        pygame.draw.rect(self.screen, Settings.SETTINGS_INPUT_BOX_COLOR, input_box_rect, 2)
        self.font = pygame.font.Font(Settings.FONT, 15)
        text_surf = self.font.render(str(number), True, Settings.SETTINGS_BUTTON_TEXT_COLOR)
        text_rect = text_surf.get_rect(center=(input_box_rect[0] + input_box_rect[2] // 2, input_box_rect[1] + input_box_rect[3] // 2))
        self.screen.blit(text_surf, text_rect)
