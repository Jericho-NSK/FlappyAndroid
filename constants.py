from platform import system

import pygame

pygame.init()

SPEED = 10
SYSTEM = system()
if SYSTEM != 'Windows':
    FPS = 120
    HEIGHT = 720
    WIDTH = HEIGHT * pygame.display.Info().current_w / pygame.display.Info().current_h * 0.97
    WINDOW = pygame.display.set_mode(size=(WIDTH, HEIGHT),
                                     flags=pygame.FULLSCREEN | pygame.SCALED,
                                     depth=32,
                                     vsync=True,
                                     )

else:
    FPS = 60
    HEIGHT = 720
    WIDTH = 1455
    WINDOW = pygame.display.set_mode(size=(WIDTH, HEIGHT),
                                     flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME,
                                     depth=32,
                                     vsync=True,
                                     )


START_TRACK = HEIGHT // 2.5
BIRD_SIZE = 40, 30
BIRD_START = WIDTH // 10, HEIGHT // 3
START_LIVES = 3

DIFFICULTY_MODS = (1, 10, 20, 35, 55, 75, 100, 130, 165, 200)

GITHUB_LINK = 'https://github.com/Jericho-NSK/FlappyAndroid'

CLOCK = pygame.time.Clock()
