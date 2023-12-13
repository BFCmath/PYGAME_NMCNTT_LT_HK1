import pygame, Intro, Define

pygame.init()
pygame.mixer.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

Define.Sound.BACKGROUND_MUSIC.play(-1)

Intro.intro(SCREEN)