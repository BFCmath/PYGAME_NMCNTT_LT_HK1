import pygame

class SettingLogic:
    def __init__(self, rect1, rect2):
        # Initialize the values for the input boxes
        self.input_values = [5, 5]  # Default values for the input boxes
        self.input_boxes = [rect1, rect2]  # Rectangles for the input boxes
        self.active_box = None  # The index of the active input box

    # def set_input_boxes(self, rect1, rect2):
    #     # Store the rects for the input boxes for mouse collision checking
    #     self.input_boxes[0] = rect1
    #     self.input_boxes[1] = rect2

    def handle_event(self, event):
        # print("handle event\n")
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check which input box was clicked, if any
            if self.input_boxes[0].collidepoint(event.pos):
                print("input box 1\n")
                self.active_box = 0
            elif self.input_boxes[1].collidepoint(event.pos):
                print("input box 2\n")
                self.active_box = 1
            else:
                self.active_box = None

        if event.type == pygame.KEYDOWN and self.active_box is not None:
            print("key down\n")
            if event.key == pygame.K_BACKSPACE:
                # Remove the last character from the active input box's value
                self.input_values[self.active_box] = max(3, self.input_values[self.active_box] // 10)
            elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                               pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                # Add the new digit to the active input box's value
                new_value = self.input_values[self.active_box] * 10 + int(event.unicode)
                if 3 <= new_value <= 15:
                    self.input_values[self.active_box] = new_value
        return self.active_box

    def get_input_values(self):
        # Return the current values of the input boxes
        return self.input_values
