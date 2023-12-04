# setting_logic.py
import pygame
from singleton import Singleton 
from game_setting import Settings
# from _scene.menu_scene import MenuScene
class SettingLogic:
    def __init__(self,back_button, size_input_box_1, size_input_box_2,name_input_box_1,name_input_box_2):
        # Initialize the values for the input boxes as empty strings
        self.back_button = back_button
        self.size_input_box_1 = size_input_box_1
        self.size_input_box_2 = size_input_box_2
        self.name_input_box_1 = name_input_box_1
        self.name_input_box_2 = name_input_box_2
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse down")
            if self.back_button.collidepoint(event.pos):
                print("back")
                Singleton.scenes = 'menu'
            
        self.handle_name_input_box(event,self.name_input_box_1,player=0)
        self.handle_name_input_box(event,self.name_input_box_2,player=1)
        self.handle_size_input_box(event,self.size_input_box_1,size_id=0)
        self.handle_size_input_box(event,self.size_input_box_2,size_id=1)
        # value_change = False
        # if event.type == pygame.KEYDOWN and self.active_box is not None:
        #     print("key down")
        #     print(self.active_box)
        #     if event.key == pygame.K_BACKSPACE and self.input_values[self.active_box].__len__() >1:
        #         # Remove the last character from the active input box's value
        #         value_change = True

        #         self.input_values[self.active_box] = self.input_values[self.active_box][:-1]

        #     elif event.unicode.isdigit() and self.input_values[self.active_box].__len__() < 2:
        #         value_change = True
        #         potential_value = self.input_values[self.active_box] + event.unicode
        #         # Check if the potential value is within the desired range
        #         # if potential_value and 3 <= int(potential_value) <= 15:
        #         self.input_values[self.active_box] = potential_value            
        # return True if value_change else False

    def get_input_values(self):
        # Return the current values of the input boxes
        return self.input_values
    
    def handle_name_input_box(self,event,name_input_box,player):
        if event.type == pygame.MOUSEBUTTONDOWN:
        #If the mouse is clicked on the input_box rect
            if name_input_box.box_rect.collidepoint(event.pos):
                #Toggle the active variable
                name_input_box.active = not name_input_box.active
            else:
                name_input_box.active = False

            if(name_input_box.active):
                name_input_box.draw_input_box()
            else:
                name_input_box.draw_passive_box()
        if name_input_box.active and event.type == pygame.KEYDOWN:
            #If the key is backspace
            if event.key == pygame.K_BACKSPACE:
                #Delete the last character
                name_input_box.text = name_input_box.text[:-1]
            elif name_input_box.text.__len__() < Settings.LIMIT_OF_NAME:
                #Add the character to the text
                name_input_box.text += event.unicode
            name_input_box.draw_text(name_input_box.text)
            Singleton.player_name[player] = name_input_box.text

    def handle_size_input_box(self,event,size_input_box,size_id):
        if event.type == pygame.MOUSEBUTTONDOWN:
        #If the mouse is clicked on the input_box rect
            if size_input_box.box_rect.collidepoint(event.pos):
                #Toggle the active variable
                size_input_box.active = not size_input_box.active
            else:
                size_input_box.active = False
                if Singleton.caro_board_size[size_id] < Settings.MIN_CARO_BOARD_SIZE:
                    Singleton.caro_board_size[size_id] = Settings.MIN_CARO_BOARD_SIZE
                    Singleton.string_caro_board_size[size_id] = '0' + str(Settings.MIN_CARO_BOARD_SIZE) if Settings.MIN_CARO_BOARD_SIZE < 10 else str(Settings.MIN_CARO_BOARD_SIZE) 
                    size_input_box.draw_text(Singleton.string_caro_board_size[size_id])

            if(size_input_box.active):
                size_input_box.draw_input_box()
            else:
                size_input_box.draw_passive_box()
        if size_input_box.active and event.type == pygame.KEYDOWN:
            #If the key is backspace
            if event.key == pygame.K_BACKSPACE:
                Singleton.string_caro_board_size[size_id] = '0'+Singleton.string_caro_board_size[size_id][0] 
                Singleton.caro_board_size[size_id] = Singleton.caro_board_size[size_id]//10
            elif event.unicode.isdigit() and Singleton.string_caro_board_size[size_id][0] == '0':
                #Adding up the input
                Singleton.caro_board_size[size_id] = Singleton.caro_board_size[size_id]*10+ int(event.unicode) 
                Singleton.string_caro_board_size[size_id] = Singleton.string_caro_board_size[size_id][1]
                Singleton.string_caro_board_size[size_id] += event.unicode
                if(Singleton.caro_board_size[size_id] > Settings.MAX_CARO_BOARD_SIZE):
                    Singleton.string_caro_board_size[size_id] = str(Settings.MAX_CARO_BOARD_SIZE)
                    Singleton.caro_board_size[size_id] = Settings.MAX_CARO_BOARD_SIZE
            print(Singleton.string_caro_board_size[size_id], Singleton.caro_board_size[size_id])
        if size_input_box.active:
            size_input_box.draw_text(Singleton.string_caro_board_size[size_id])
            
        