from platform import system

import pygame

pygame.init()

print(pygame.font.get_fonts())
print(pygame.font.get_default_font())
if system() != 'Windows':
    WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
else:
    WIDTH, HEIGHT = 1280, 720

START_TRACK = HEIGHT // 2.5
BIRD_SIZE = 40, 30
BIRD_START = WIDTH // 10, HEIGHT // 3
START_LIVES = 3
FPS = 60
SPEED = 2
DIFFICULTY_MODS = (1, 10, 20, 35, 55, 75, 100, 130, 165, 200)
FONT = pygame.font.SysFont('comicsanms', size=48, italic=True)

WINDOW = pygame.display.set_mode(size=(WIDTH, HEIGHT),
                                 flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME,
                                 depth=32,
                                 vsync=True,
                                 )
CLOCK = pygame.time.Clock()
