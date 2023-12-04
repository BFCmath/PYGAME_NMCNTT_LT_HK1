# import pygame

# #khởi tạo pygame
# pygame.init()

# #tạo cửa sổ giao diện trong pygame
# screen = pygame.display.set_mode((1280,720))
# pygame.display.set_caption("Game Caro")

# #khai báo màu nền cho giao diện
# BACKGROUND_COLOR = (100, 100, 100)

# #biến vòng lặp game
# running = True

# #game loop
# while running:

#     #vẽ màu nền
#     screen.fill(BACKGROUND_COLOR)

#     #xử lý sự kiện
#     for event in pygame.event.get():
#         #sự kiện thoát
#         if event.type == pygame.QUIT:
#             running = False
#         #sự kiện chuột
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1: #nhấn chuột trái
#                 print(event.pos) #in tọa độ chuột
#     r = 255
#     g = 0
#     b = 0
#     x = 10
#     y = 10
#     width = 100
#     height = 200

#     #hàm vẽ hình chữ nhật có điểm trái trên tọa độ (x,y) kích thước (width, height) với màu (r,g,b)
#     # pygame.draw.rect(screen, (r, g, b), (x, y, width, height))

#     x1 = 203
#     y1 = 232
#     x2 = 432
#     y2 = 324
#     thickness = 5
#     #hàm vẽ đoạn thẳng nối 2 điểm (x1, y1) và (x2, y2) có độ dày thickness
#     # pygame.draw.line(screen, (r, g, b), (x1, y1), (x2, y2), thickness)
#     #vẽ tất cả lên màn hình
#     pygame.draw.rect(screen, (225, 225, 225), (335, 205, 600, 300), 5, border_radius=30)
#     pygame.display.update()


# #thoát chương trình
# pygame.quit()

# import pygame
# import sys

# class NumberBox:
#     def __init__(self):
#         self.value = 9  # Giá trị mặc định là 09

#     def set_value(self, new_value):
#         # Chỉ chấp nhận giá trị từ 9 đến 30
#         if 9 <= new_value <= 30:
#             self.value = new_value
#         else:
#             print("Giá trị không hợp lệ. Box chỉ chấp nhận giá trị từ 9 đến 30.")

#     def display_value(self):
#         # Hiển thị số với đúng định dạng (2 chữ số)
#         print(f"{self.value:02d}")

# # Khởi tạo Pygame
# pygame.init()

# # Cấu hình màn hình
# width, height = 400, 200
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Menu with Number Box")

# # Khởi tạo NumberBox
# box = NumberBox()

# # Vòng lặp chính
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             # Xử lý sự kiện khi người dùng nhấn phím
#             if pygame.K_0 <= event.key <= pygame.K_9:
#                 new_value = int(chr(event.key))
#                 box.set_value(new_value)

#     # Hiển thị giá trị hiện tại của box và menu
#     screen.fill((255, 255, 255))
    
#     # Hiển thị giá trị box
#     font = pygame.font.Font(None, 36)
#     text = font.render(f"Giá trị hiện tại: {box.value:02d}", True, (0, 0, 0))
#     screen.blit(text, (20, 20))

#     # Hiển thị menu
#     menu_text = font.render("Menu:", True, (0, 0, 0))
#     screen.blit(menu_text, (20, 70))
#     menu_options = [
#         "1. Option 1",
#         "2. Option 2",
#         "3. Option 3"
#     ]
#     for i, option in enumerate(menu_options):
#         option_text = font.render(option, True, (0, 0, 0))
#         screen.blit(option_text, (20, 100 + i * 30))

#     # Cập nhật màn hình
#     pygame.display.flip()



# import pygame
# import sys

# # Khởi tạo Pygame
# pygame.init()

# # Kích thước cửa sổ
# width, height = 800, 600

# # Màu sắc
# white = (255, 255, 255)
# blue = (0, 0, 255)

# # Tạo cửa sổ
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Chuyển Cảnh Pygame")

# # Biến trạng thái cảnh
# current_scene = 1

# # Vòng lặp chính
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Xử lý logic cảnh hiện tại
#     if current_scene == 1:
#         # Logic cho cảnh 1
#         screen.fill(white)
#         pygame.draw.rect(screen, blue, (100, 100, 200, 200))

#         # Kiểm tra điều kiện chuyển cảnh
#         # Ví dụ: Khi nhấn phím space, chuyển sang cảnh 2
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE]:
#             current_scene = 2

#     elif current_scene == 2:
#         # Logic cho cảnh 2
#         screen.fill(white)
#         pygame.draw.circle(screen, blue, (400, 300), 100)

#         # Kiểm tra điều kiện chuyển cảnh
#         # Ví dụ: Khi nhấn phím space, chuyển lại cảnh 1
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE]:
#             current_scene = 1

#     # Cập nhật cửa sổ
#     pygame.display.flip()

#     # Đặt độ trễ để giảm tải CPU
#     pygame.time.Clock().tick(60)

# import pygame
# import sys

# # Khởi tạo Pygame
# pygame.init()

# # Kích thước cửa sổ
# width, height = 400, 300
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Thông báo từng Button")

# # Màu sắc
# white = (255, 255, 255)
# black = (0, 0, 0)
# button_color = (0, 128, 255)
# overlay_color = (0, 0, 0, 128)  # Màu sắc overlay có alpha để làm mờ

# # Kích thước button
# button_width, button_height = 200, 50

# # Tọa độ button
# button1_x, button1_y = (width - button_width) // 2, (height - button_height) // 3
# button2_x, button2_y = (width - button_width) // 2, (height - button_height) // 1.5

# # Tạo font
# font = pygame.font.Font(None, 36)

# # Text trên button
# button1_text = font.render("Show Popup 1", True, white)
# button2_text = font.render("Show Popup 2", True, white)

# # Trạng thái hiển thị bảng thông báo cho mỗi button
# show_popup1 = False
# show_popup2 = False

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             # Kiểm tra xem chuột có nằm trong button1 hay không
#             if button1_x < mouse_x < button1_x + button_width and button1_y < mouse_y < button1_y + button_height:
#                 show_popup1 = True
#             # Kiểm tra xem chuột có nằm trong button2 hay không
#             elif button2_x < mouse_x < button2_x + button_width and button2_y < mouse_y < button2_y + button_height:
#                 show_popup2 = True

#     # Xóa màn hình
#     screen.fill(white)

#     # Vẽ button1
#     pygame.draw.rect(screen, button_color, (button1_x, button1_y, button_width, button_height))
#     # Vẽ text trên button1
#     text_rect1 = button1_text.get_rect(center=(button1_x + button_width // 2, button1_y + button_height // 2))
#     screen.blit(button1_text, text_rect1)

#     # Vẽ button2
#     pygame.draw.rect(screen, button_color, (button2_x, button2_y, button_width, button_height))
#     # Vẽ text trên button2
#     text_rect2 = button2_text.get_rect(center=(button2_x + button_width // 2, button2_y + button_height // 2))
#     screen.blit(button2_text, text_rect2)

#     # Nếu đang hiển thị bảng thông báo cho button1
#     if show_popup1:
#         # Tạo overlay làm mờ
#         overlay = pygame.Surface((width, height), pygame.SRCALPHA)
#         overlay.fill(overlay_color)
#         screen.blit(overlay, (0, 0))

#         # Vẽ bảng thông báo cho button1
#         popup_rect = pygame.Rect(50, 50, 300, 200)
#         pygame.draw.rect(screen, black, popup_rect)
#         pygame.draw.rect(screen, white, popup_rect.inflate(-10, -10))

#         # Hiển thị nội dung bảng thông báo cho button1
#         popup_text = font.render("Đây là bảng thông báo cho Button 1", True, black)
#         screen.blit(popup_text, (popup_rect.x + 10, popup_rect.y + 10))

#     # Nếu đang hiển thị bảng thông báo cho button2
#     elif show_popup2:
#         # Tạo overlay làm mờ
#         overlay = pygame.Surface((width, height), pygame.SRCALPHA)
#         overlay.fill(overlay_color)
#         screen.blit(overlay, (0, 0))

#         # Vẽ bảng thông báo cho button2
#         popup_rect = pygame.Rect(50, 50, 10, 10)
#         pygame.draw.rect(screen, black, popup_rect)
#         pygame.draw.rect(screen, white, popup_rect.inflate(-10, -10))

#         # Hiển thị nội dung bảng thông báo cho button2
#         popup_text = font.render("Đây là bảng thông báo cho Button 2", True, black)
#         screen.blit(popup_text, (popup_rect.x + 10, popup_rect.y + 10))

#     # Cập nhật màn hình
#     pygame.display.flip()

import pygame
import sys

pygame.init()

class TextInputBox:
    def __init__(self, x, y, width, height, font_size=32):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = '09'
        self.font = pygame.font.Font(None, font_size)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:
            print(self.active)
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def update(self):
        text_surface = self.font.render(self.text, True, self.color)
        return text_surface

# Tạo cửa sổ
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Text Input Box")

# Tạo ô nhập văn bản
input_box = TextInputBox(150, 100, 140, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Xử lý sự kiện cho ô nhập văn bản
        input_box.handle_event(event)

    screen.fill((255, 255, 255))
    
    # Cập nhật và vẽ ô nhập văn bản
    text_surface = input_box.update()
    pygame.draw.rect(screen, input_box.color, input_box.rect, 2)
    screen.blit(text_surface, (input_box.rect.x + 5, input_box.rect.y + 5))

    pygame.display.flip()