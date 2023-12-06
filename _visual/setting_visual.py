import pygame
from _visual.general_visual import GeneralVisual, InputBox
from _add.game_setting import Settings,Board
from _add.singleton import Singleton
class SettingVisual(GeneralVisual):
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(Settings.FONT, 32)  # Adjust the size as needed
        
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
        
    def draw_background(self):
        self.screen.fill(Settings.SETTINGS_COLOR)
        pygame.display.update()
    def draw_name(self):
        self.font = pygame.font.Font(Settings.FONT, Settings.NAME_SIZE)
        text_surf = self.font.render(Settings.NAME_1, True, Settings.SETTINGS_BUTTON_TEXT_COLOR)
        text_rect = text_surf.get_rect(topleft=(Settings.NAME_PLACE_1[0], Settings.NAME_PLACE_1[1]))
        self.screen.blit(text_surf, text_rect)
        text_surf = self.font.render(Settings.NAME_2, True, Settings.SETTINGS_BUTTON_TEXT_COLOR)
        text_rect = text_surf.get_rect(topleft=(Settings.NAME_PLACE_2[0], Settings.NAME_PLACE_2[1]))
        self.screen.blit(text_surf, text_rect)

    def draw_name_input_box(self):
        name_input_box_1 = InputBox(self.screen,Settings.SETTINGS_NAME_INPUT_BOX_RECT_1,Settings.ACTIVE_COLOR_INPUT_BOX,Settings.PASSIVE_COLOR_INPUT_BOX,Settings.INPUT_BOX_BACKGROUND_COLOR,Settings.FONT,Settings.SETTINGS_INPUT_BOX_TEXT_SIZE,Settings.INPUT_BOX_TEXT_COLOR,Singleton.player_name[0])
        name_input_box_1.draw_passive_box()
        name_input_box_2 = InputBox(self.screen,Settings.SETTINGS_NAME_INPUT_BOX_RECT_2,Settings.ACTIVE_COLOR_INPUT_BOX,Settings.PASSIVE_COLOR_INPUT_BOX,Settings.INPUT_BOX_BACKGROUND_COLOR,Settings.FONT,Settings.SETTINGS_INPUT_BOX_TEXT_SIZE,Settings.INPUT_BOX_TEXT_COLOR,Singleton.player_name[1])
        name_input_box_2.draw_passive_box()
        return name_input_box_1,name_input_box_2
        
    def draw_input_box_place(self):
        self.draw_x()
        size_input_box_1 = InputBox(self.screen,Settings.SETTINGS_INPUT_BOX_RECT_1,Settings.ACTIVE_COLOR_INPUT_BOX,Settings.PASSIVE_COLOR_INPUT_BOX,Settings.INPUT_BOX_BACKGROUND_COLOR,Settings.FONT,Settings.SETTINGS_INPUT_BOX_TEXT_SIZE,Settings.INPUT_BOX_TEXT_COLOR,Singleton.string_caro_board_size[0])
        size_input_box_1.draw_passive_box()
        size_input_box_2 = InputBox(self.screen,Settings.SETTINGS_INPUT_BOX_RECT_2,Settings.ACTIVE_COLOR_INPUT_BOX,Settings.PASSIVE_COLOR_INPUT_BOX,Settings.INPUT_BOX_BACKGROUND_COLOR,Settings.FONT,Settings.SETTINGS_INPUT_BOX_TEXT_SIZE,Settings.INPUT_BOX_TEXT_COLOR,Singleton.string_caro_board_size[1])
        size_input_box_2.draw_passive_box()
        return size_input_box_1,size_input_box_2
