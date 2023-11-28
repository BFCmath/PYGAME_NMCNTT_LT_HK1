import pygame 

class GeneralVisual:
    def draw_input_box(self,screen, input_box_rect,input_box_color):
        box_rect = pygame.Rect(input_box_rect)
        pygame.draw.rect(screen, input_box_color, box_rect, 2) 
        return box_rect
            
    def draw_button(self,screen, rect, text, size,font,button_color,text_color):
        self.font = pygame.font.Font(font, size)
        button_rect = pygame.Rect(rect)
        pygame.draw.rect(screen, button_color, button_rect)
        _text_surf = self.font.render(text, True, text_color)
        _text_rect = _text_surf.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        screen.blit(_text_surf, _text_rect)
        return button_rect

