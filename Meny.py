import pygame

# Setting
width_board = 1200
height_board = 800

text_color = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

# Default
pygame.init()

screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Game Caro")

font_file_path = 'font/kongtext.ttf'


# Function
def Option(screen, option, text_color, font_size, x, y, width_rect, height_rect):
    font = pygame.font.Font(font_file_path, font_size)
    text = font.render(option, False, text_color)
    pygame.draw.rect(screen, (160, 150, 100), (x, y, width_rect, height_rect), border_radius = 30)
    screen.blit(text, (x + (width_rect - text.get_width())/2, y + (height_rect - text.get_height())/2))


screen.fill(BACKGROUND_COLOR)

running = True

#game loop
while running:
    screen.fill(BACKGROUND_COLOR)

    font = pygame.font.Font(font_file_path, 80)
    text = font.render("MAIN MENU", False, text_color)
    screen.blit(text, ((width_board - text.get_width())/2, 100))    

    x = (width_board - 400)/2
    Option(screen, "Play Game", text_color, 35, x, 300, 400, 70)
    Option(screen, "Setting", text_color, 35, x, 400, 400, 70)
    Option(screen, "Help", text_color, 35,x, 500, 400, 70)
    Option(screen, "Quit", text_color, 35,x, 600, 400, 70)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if x + 400 > mouse_x > x and 300 < mouse_y < 370:
        Option(screen, "Play Game", text_color, 35,(width_board - 500)/2 , 300, 500, 85)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("Play Game")
    if x + 400 > mouse_x > x and 400 < mouse_y < 470:
        Option(screen, "Setting", text_color, 35,(width_board - 500)/2 , 400, 500, 85)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("Setting")
    if x + 400 > mouse_x > x and 500 < mouse_y < 570:
        Option(screen, "Help", text_color, 35,(width_board - 500)/2 , 500, 500, 85)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("Help")
    if x + 400 > mouse_x > x and 600 < mouse_y < 670:
        Option(screen, "Quit", text_color, 35,(width_board - 500)/2 , 600, 500, 85)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("Quit")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass
    pygame.display.flip()
pygame.quit()

    