import pygame
from game_setting import PlayGame, Board

class PlayGameVisual:
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
    def draw_button(self, rect, text, size):
        font = pygame.font.Font(PlayGame.FONT, size)
        pygame.draw.rect(self.screen, PlayGame.BACK_BUTTON_COLOR, rect)
        _text_surf = font.render(text, True, PlayGame.BACK_TEXT_COLOR)
        _text_rect = _text_surf.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.screen.blit(_text_surf, _text_rect)
        
    def draw_all_texts(self):
        self.print_text(PlayGame.turn_text, self.text_color, PlayGame.TURN_TEXT_POSITION, alignment="left")
        self.draw_button(PlayGame.BACK_BUTTON_RECT, PlayGame.BACK_TEXT, PlayGame.TEXT_SIZE)
        # self.print_text(back_text, self.text_color, PlayGame.BACK_TEXT_POSITION, alignment="right")
        self.print_text(PlayGame.PLAYER1_TEXT, self.text_color, PlayGame.PLAYER1_TEXT_POSITION, alignment="left")
        self.print_text(PlayGame.PLAYER2_TEXT, self.text_color, PlayGame.PLAYER2_TEXT_POSITION, alignment="right")

        pygame.display.update()  

    def draw_background(self):
        self.screen.fill(PlayGame.BACKGROUND_COLOR)

