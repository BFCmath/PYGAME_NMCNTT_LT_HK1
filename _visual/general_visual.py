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
class Button():
    def __init__(self, screen, button_rect,hover_button_rect, text, text_size, font, text_color,background_color,button_color):
        self.screen = screen
        self.button_rect = pygame.rect.Rect(button_rect)
        self.hover_button_rect = pygame.rect.Rect(hover_button_rect)
        self.text = text
        self.text_size = text_size
        self.font = pygame.font.Font(font, text_size)
        self.text_color = text_color
        self.background_color = background_color
        self.button_color = button_color
        self.hover = False
        self.draw_button()
        pass
    def draw_button(self):
        pygame.draw.rect(self.screen,self.background_color,self.hover_button_rect)
        pygame.draw.rect(self.screen,self.button_color,self.button_rect)
        self.draw_text()
        pygame.display.flip()
    def draw_hover_button(self):
        pygame.draw.rect(self.screen,self.button_color,self.hover_button_rect)
        self.draw_text()
        pygame.display.flip()
    def check_hover(self, mouse_pos):
        if(mouse_pos[0] in range(self.button_rect.left, self.button_rect.right) and mouse_pos[1] in range(self.button_rect.top, self.button_rect.bottom)):
            self.draw_hover_button()
        else:
            self.draw_button()
    def draw_text(self):
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
    def check_collide(self, mouse_pos):
        return self.button_rect.collidepoint(mouse_pos)


class InputBox:
    def __init__(self,screen,box_rect,active_border_color,passive_border_color,background_color,font,size,text_color = (255,255,255),text=''):
        self.screen = screen
        self.box_rect = pygame.rect.Rect(box_rect)
        self.active_border_color = active_border_color
        self.passive_border_color = passive_border_color
        self.background_color = background_color
        self.font = pygame.font.Font(font, size)
        self.text_color = text_color
        self.text = text
        self.active = False
        self.draw_text(text)
        pass
    def _draw_background_box(self):
        pygame.draw.rect(self.screen,self.background_color,self.box_rect)
        pygame.display.flip()


    def draw_input_box(self):
        pygame.draw.rect(self.screen,self.active_border_color,self.box_rect,2)
        pygame.display.flip()

    def draw_passive_box(self):
        pygame.draw.rect(self.screen,self.passive_border_color,self.box_rect,2)
        pygame.display.flip()

    def draw_text(self, text):
        pygame.draw.rect(self.screen, self.background_color, self.box_rect)
        pygame.draw.rect(self.screen, self.active_border_color if self.active else self.passive_border_color, self.box_rect, 2)
        
        text_surface = self.font.render(text, True, self.text_color)
        
        # Calculate the center position of the text
        text_rect = text_surface.get_rect(center=self.box_rect.center)
        
        # Blit the text surface onto the screen at the calculated position
        self.screen.blit(text_surface, text_rect)
        
        pygame.display.flip()
