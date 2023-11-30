import pygame
from game_setting import Intro, Board
from _visual.general_visual import GeneralVisual
class IntroVisual(GeneralVisual):
    def __init__(self, screen):
        self.screen = screen

    def draw_logo(self):
        print("logo")
        self.logo_image = pygame.image.load(Intro.LOGO_IMAGE)
        self.logo_image = pygame.transform.scale(self.logo_image, Intro.LOGO_IMAGE_SIZE)
        self.screen.blit(self.logo_image, ((Board.BOARD_WIDTH-self.logo_image.get_width())//2, (Board.BOARD_HEIGHT-self.logo_image.get_height())//2))
        
        pygame.display.update()
        
    def draw_loading_bar_background(self):
        print("loading bar")
        self.loading_bar_color = Intro.LOADING_BAR_COLOR
        self.loading_bar_background_color = Intro.LOADING_BAR_BACKGROUND_COLOR
        self.loading_bar_rect = pygame.Rect(Intro.LOADING_BAR_RECT)
        pygame.draw.rect(self.screen, Intro.LOADING_BAR_BACKGROUND_COLOR, Intro.LOADING_BAR_RECT)
        pygame.display.update()
    def draw_loading_bar(self,elapsed_time):
        self.loading_bar_length = Intro.LOADING_BAR_RECT[2]
        self.loading_bar_rect.width = (elapsed_time / Intro.LOADING_TIME) * self.loading_bar_length
        pygame.draw.rect(self.screen, self.loading_bar_color, self.loading_bar_rect)
        pygame.display.update()
    def draw_background(self):
        self.screen.fill(Board().BACKGROUND_COLOR)
        pygame.display.update()

