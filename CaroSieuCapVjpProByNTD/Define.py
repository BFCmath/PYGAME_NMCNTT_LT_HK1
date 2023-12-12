import pygame, time
pygame.mixer.init()

class Screen:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    SCREEN_TITLE = "CARO SIEU CAP VJP PRO BY TRONG DOANH"
    BACKGROUND = pygame.image.load("Assets/ChillChill.jpg")
    ENDGAME_SCENE = pygame.image.load("Assets/EndGame.png")

class Font:
    FONT_FILE_PATH = "FontText/KongText.ttf"
    FONT_COLOR = (0, 0, 0)

def get_font(size):
    return pygame.font.Font(Font.FONT_FILE_PATH, size)

def Find_in(a, p):
    for row in p:
        if a in row:
            return True
    return False

class Popup:
    POPUP_COLOR = ("#c8c8c8")
    
    BLUR_SURFACE = pygame.Surface((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT), pygame.SRCALPHA)
    BLUR_SURFACE.fill((0, 0, 0, 100))

class BoardGame:
    BOARD_WIDTH = 1080
    BOARD_HEIGHT = 520
    NUMBER_WIDTH_CELL = "09"
    NUMBER_HEIGHT_CELL = "09"
    PLAYER_X = "Player 1"
    PLAYER_O = "Player 2"

class Sound:
    BACKGROUND_MUSIC = pygame.mixer.Sound("Assets/MusicBackground.mp3")
    BACKGROUND_MUSIC.set_volume(1)
    
    SOUND_EFFECT = pygame.mixer.Sound("Assets/WriteEffect.wav")
    SOUND_EFFECT.set_volume(100)

