import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Loading")

# Load logo image
logo_image = pygame.image.load('__others/logo_caro.jpg')
logo_image = pygame.transform.scale(logo_image, (400, 400))  # Scale the logo to the desired size

# Loading bar settings
loading_bar_length = 300
loading_bar_height = 25
loading_bar_color = (0, 128, 0)
loading_bar_background_color = (128, 128, 128)
loading_bar_position = (screen_width // 2 - loading_bar_length // 2, screen_height - 50)
loading_bar_rect = pygame.Rect(loading_bar_position[0], loading_bar_position[1], 0, loading_bar_height)

# Intro loop
intro = True
start_time = pygame.time.get_ticks()  # Get the start time
loading_time = 5000  # Time in milliseconds to display the intro

while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate elapsed time
    elapsed_time = pygame.time.get_ticks() - start_time
    # Calculate the width of the loading bar based on elapsed time
    loading_bar_rect.width = (elapsed_time / loading_time) * loading_bar_length

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw the logo image
    screen.blit(logo_image, (screen_width // 2 - logo_image.get_width() // 2, screen_height // 2 - logo_image.get_height() // 2))

    # Draw loading bar background
    pygame.draw.rect(screen, loading_bar_background_color, (loading_bar_position[0], loading_bar_position[1], loading_bar_length, loading_bar_height))

    # Draw loading bar
    pygame.draw.rect(screen, loading_bar_color, loading_bar_rect)

    # Update the display
    pygame.display.update()

    # Check if the loading time has passed
    if elapsed_time > loading_time:
        intro = False  # End the intro loop

# Transition to MenuScene
# menu_scene = MenuScene(screen)
# menu_scene.run()  # Or however you've set up to run the menu scene

# Clean up Pygame before exiting
pygame.quit()
