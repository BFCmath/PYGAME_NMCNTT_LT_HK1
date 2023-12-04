import pygame, sys, string
class InputBox:
    def __init__(self,screen,box_rect,active_border_color,passive_border_color,background_color,text=''):
        self.screen = screen
        self.box_rect = pygame.rect.Rect(box_rect)
        self.active_border_color = active_border_color
        self.passive_border_color = passive_border_color
        self.background_color = background_color
        self.text = text
        pass
    def draw_background_box(self):
        pygame.draw.rect(self.screen,self.background_color,self.box_rect)
        pygame.display.flip()


    def draw_input_box(self):
        self.draw_background_box()
        pygame.draw.rect(self.screen,self.active_border_color,self.box_rect,2)
        pygame.display.flip()

    def draw_passive_box(self):
        self.draw_background_box()
        pygame.draw.rect(self.screen,self.passive_border_color,self.box_rect,2)
        pygame.display.flip()


    def draw_text(self,text):
        # self.draw_input_box()
        
        # self.draw_background_box()
        pygame.draw.rect(self.screen,self.background_color,self.box_rect)

        pygame.draw.rect(self.screen,self.active_border_color,self.box_rect,2)
        font = pygame.font.Font(None, 28)
        text_surface = font.render(text, True, (255,255,255))
        self.screen.blit(text_surface, (self.box_rect[0] + 5, self.box_rect[1] + 5))
        pygame.display.flip()


#Create the screen
pygame.init()
screen = pygame.display.set_mode((1000, 700))
base_font = pygame.font.Font(None, 28)
<<<<<<< HEAD
fps = pygame.time.Clock()
#Input
user_text = ''

#Create a rectangle at (x, y)
input_rect = pygame.Rect(10, 10, 0, 28)
#Two colors for two statuses
color_active = pygame.Color(255, 255, 255)
color_passive = pygame.Color(92, 92, 61)
#Initially, the cursor is inside the rectangle
active = True
checkBoardSize = 0
color = color_active
=======
#Board size
user_text = ''

#Create a rectangle at (x, y)
>>>>>>> d7aa9ac1168bb7beb5fe3749287454c5dad3e498

#Two colors for two statuses
color_background = pygame.Color(255,10,10)
color_active = pygame.Color(180, 180, 180)
color_passive = pygame.Color(92, 92, 61)
input_box = InputBox(screen,(100,100,140,32),color_active,color_passive,color_background)
input_box.draw_background_box()
#Initially, the cursor is inside the rectangle
screen.fill((0,0,0))
active = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #If the user press a key
        if event.type == pygame.MOUSEBUTTONDOWN:
            #If the mouse is clicked on the input_box rect
            if input_box.box_rect.collidepoint(event.pos):
                #Toggle the active variable
                active = not active
            else:
                active = False
            if(active):
                input_box.draw_input_box()
            else:
                input_box.draw_passive_box()
        if active and event.type == pygame.KEYDOWN:
            #If the key is backspace
            if event.key == pygame.K_BACKSPACE:
                #Delete the last character
                user_text = user_text[:-1]
<<<<<<< HEAD
            #Digit
            elif event.unicode.isdigit():
                checkBoardSize = 0
                #Adding up the input
                if user_text != '':
                    checkBoardSize += int(user_text)
                checkBoardSize = checkBoardSize * 10 + int(event.unicode)
                #Valid range = [3; 15]
                if checkBoardSize != 0:
                    #Exceed -> minimize to 15
                    if (checkBoardSize > 15):
                        user_text = '15'
                    #Inclusive -> valid
                    else:
                        user_text += event.unicode
                else:
                    user_text = '3'

    ##Create the update sence
    #Create an empty screen
    screen.fill((0, 0, 0))
    #Set the cursor color to its status colors
    if active:
        color = color_active
    else:
        color = color_passive
        #Left empty or < 3 -> round up to 3
        if (user_text == '' or int(user_text) < 3):
            user_text = '3'
    #Draw the rectangle (border only)
    pygame.draw.rect(screen, color, input_rect, 2)
    #Expand the rectangle to the text size
    text_surface = base_font.render(user_text, True, (255, 255, 255)) 
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = text_surface.get_width() + 10

    #Update the sence
    pygame.display.update()
    fps.tick(60)
=======
            elif user_text.__len__() < 10:
                #Add the character to the text
                user_text += event.unicode
            input_box.draw_text(user_text)
    
>>>>>>> d7aa9ac1168bb7beb5fe3749287454c5dad3e498
