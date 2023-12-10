import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Khởi tạo âm thanh
pygame.mixer.init()

# Tạo cửa sổ trò chơi
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Sound Example")

# Tải nhạc và hiệu ứng âm thanh
background_music = pygame.mixer.Sound("Assets/MusicBackground.mp3")
explosion_sound = pygame.mixer.Sound("Assets/WriteEffect.wav")

# Điều chỉnh âm lượng của nhạc nền và hiệu ứng âm thanh
background_music.set_volume(0.2)  # Đặt âm lượng của nhạc nền là 50%
explosion_sound.set_volume(0.5)    # Đặt âm lượng của hiệu ứng âm thanh là 80%

# Chơi nhạc nền
background_music.play(-1)  # -1 để lặp vô hạn

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Chơi hiệu ứng âm thanh khi nhấn SPACE
                explosion_sound.play()

    pygame.display.flip()