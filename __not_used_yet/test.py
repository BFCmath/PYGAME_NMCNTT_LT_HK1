import pygame
import sys

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
        return mouse_pos[0] in range(self.button_rect.left, self.button_rect.right) and mouse_pos[1] in range(self.button_rect.top, self.button_rect.bottom)
    def draw_text(self):
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Button Example")

    # Button configuration
    button_rect = (350, 250, 100, 50)  # x, y, width, height
    hover_button_rect = (345, 245, 110, 60)  # Slightly larger for hover effect
    text = "Click Me"
    text_size = 24
    font = None  # None will use the default system font
    text_color = (255, 255, 255)  # White text
    background_color = (100, 100, 100)  # Black background
    button_color = (0, 128, 0)  # Green button

    # Create a Button instance
    my_button = Button(screen, button_rect, hover_button_rect, text, text_size, font, text_color, background_color, button_color)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check for mouse hover on the button
        mouse_pos = pygame.mouse.get_pos()
        if my_button.check_hover(mouse_pos):
            my_button.draw_hover_button()
        else:
            my_button.draw_button()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
