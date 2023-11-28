# setting_logic.py
import pygame
from singleton import Singleton 
# from _scene.menu_scene import MenuScene
class SettingLogic:
    def __init__(self,back_button, rect1, rect2):
        # Initialize the values for the input boxes as empty strings
        self.back_button = back_button
        self.input_values = ['10', '10']  # Default values for the input boxes
        self.input_boxes = [rect1, rect2]  # Rectangles for the input boxes
        self.active_box = None  # The index of the active input box

    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse down")
            if self.back_button.collidepoint(event.pos):
                print("back")
                Singleton.scenes = 0
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
