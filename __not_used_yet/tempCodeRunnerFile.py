import pygame, sys, string

#Create the screen
pygame.init()
screen = pygame.display.set_mode((1000, 700))
base_font = pygame.font.Font(None, 28)
fps = pygame.time.Clock()
#Input
user_text = '03'
user_int = 3

#Create a rectangle at (x, y)
input_rect = pygame.Rect(10, 10, 0, 28)
#Two colors for two statuses
color_active = pygame.Color(255, 255, 255)
color_passive = pygame.Color(92, 92, 61)
#Initially, the cursor is inside the rectangle
active = False
checkBoardSize = 0
color = color_active

#Repeatedly update new scenes
while True:
    #Update the text
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Check the cursor
        if event.type == pygame.MOUSEBUTTONDOWN:
            active = input_rect.collidepoint(event.pos)
        #Typing...
        if event.type == pygame.KEYDOWN:
            #The cursor is outside the box text
            if active == False:
                continue
            #Backspace
            if event.key == pygame.K_BACKSPACE:
                user_text = '0'+user_text[0]
                user_int = user_int//10
            #Digit
            elif event.unicode.isdigit() and user_text[0] == '0':
                #Adding up the input
                user_int = user_int*10+ int(event.unicode) 
                user_text= user_text[1]
                user_text += event.unicode
                if(user_int > 15):
                    user_text = '15'
                    user_int = 15
            print(user_text, user_int)

    ##Create the update sence
    #Create an empty screen
    screen.fill((0, 0, 0))
    #Set the cursor color to its status colors
    if active:
        color = color_active
    else:
        color = color_passive
        #Left empty or < 3 -> round up to 3
        if (int(user_text) < 3):
            user_text = '03'
            print(user_text, user_int)
    #Draw the rectangle (border only)
    pygame.draw.rect(screen, color, input_rect, 2)
    #Expand the rectangle to the text size
    text_surface = base_font.render(user_text, True, (255, 255, 255)) 
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = text_surface.get_width() + 10

    #Update the sence
    pygame.display.update()
    fps.tick(60)