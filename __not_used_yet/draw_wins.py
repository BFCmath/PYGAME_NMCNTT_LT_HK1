import pygame, sys

width = 1200
height = 700
screen_color = (0, 0, 0)
line_color = (255, 0, 0)

wins = [[(100, 220), (1000, 500)]]
def draw_wins():
    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)
    pygame.display.flip()

    for [start, end] in wins:
        pygame.draw.line(screen, line_color, start, end, 10)
        pygame.display.update()
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
                sys.exit(0)

draw_wins()