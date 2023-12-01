# setting_logic.py
import pygame
from singleton import Singleton 
from game_setting import Settings
# from _scene.menu_scene import MenuScene
class SettingLogic:
    def __init__(self,back_button, rect1, rect2):
        # Initialize the values for the input boxes as empty strings
        self.back_button = back_button
        self.input_values = ['10', '10']  # Default values for the input boxes
        self.input_boxes = [rect1, rect2]  # Rectangles for the input boxes
        self.active_box = None  # The index of the active input box
        self.active_name_button_1 = False
        self.active_name_button_2 = False
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse down")
            if self.back_button.collidepoint(event.pos):
                print("back")
                Singleton.scenes = 'menu'
            # Check which input box was clicked, if any
            if self.input_boxes[0].collidepoint(event.pos):
                self.active_box = 0
            elif self.input_boxes[1].collidepoint(event.pos):
                self.active_box = 1
            else:
                self.active_box = None

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
    
    def handle_name_input_box(self,event,name_input_box_1,name_input_box_2):
        if event.type == pygame.MOUSEBUTTONDOWN:
        #If the mouse is clicked on the input_box rect
            if name_input_box_1.box_rect.collidepoint(event.pos):
                #Toggle the active variable
                self.active_name_button_1 = not self.active_name_button_1
            else:
                self.active_name_button_1 = False

            if(self.active_name_button_1):
                name_input_box_1.draw_input_box()
            else:
                name_input_box_1.draw_passive_box()
            
            if name_input_box_2.box_rect.collidepoint(event.pos):
                #Toggle the active variable
                self.active_name_button_2 = not self.active_name_button_2
            else:
                self.active_name_button_2 = False

            if(self.active_name_button_2):
                name_input_box_2.draw_input_box()
            else:
                name_input_box_2.draw_passive_box()

        if self.active_name_button_1 and event.type == pygame.KEYDOWN:
            #If the key is backspace
            if event.key == pygame.K_BACKSPACE:
                #Delete the last character
                name_input_box_1.text = name_input_box_1.text[:-1]
            elif name_input_box_1.text.__len__() < Settings.LIMIT_OF_NAME:
                #Add the character to the text
                name_input_box_1.text += event.unicode
            name_input_box_1.draw_text(name_input_box_1.text)
            Singleton.player_name[0] = name_input_box_1.text


        if self.active_name_button_2 and event.type == pygame.KEYDOWN:
            #If the key is backspace
            if event.key == pygame.K_BACKSPACE:
                #Delete the last character
                name_input_box_2.text = name_input_box_2.text[:-1]
            elif name_input_box_2.text.__len__() < Settings.LIMIT_OF_NAME:
                #Add the character to the text
                name_input_box_2.text += event.unicode
            name_input_box_2.draw_text(name_input_box_2.text)
            Singleton.player_name[1] = name_input_box_2.text
        