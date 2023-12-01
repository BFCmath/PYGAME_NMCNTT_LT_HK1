import pygame
import sys

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.font = pygame.font.SysFont(None, 32)
        self.active = False
        self.limit = 10

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(self.text) < self.limit:
                    self.text += event.unicode

    def update(self):
        # Update the width of the rect based on the text length
        width = max(200, self.font.size(self.text)[0] + 10)
        self.rect.w = width

    def draw(self, screen):
        # Draw the text
        txt_surface = self.font.render(self.text, True, pygame.Color('black'))
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Draw the rect
        pygame.draw.rect(screen, self.color, self.rect, 2)

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Enter Player Names")

# Màu sắc
white = (255, 255, 255)

# Tạo hai input boxes
input_box1 = InputBox(100, 150, 140, 32)
input_box2 = InputBox(100, 250, 140, 32)
screen.fill(white)  # Vẽ nền màn hình trắng

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        input_box1.handle_event(event)
        input_box2.handle_event(event)

    input_box1.update()
    input_box2.update()

    input_box1.draw(screen)
    input_box2.draw(screen)

    pygame.display.flip()  # Cập nhật màn hình
    # Thoát Pygame
pygame.quit()
sys.exit()

