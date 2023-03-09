import os

import pygame

from constants import HEIGHT
from image_converter import convert


class Text:
    font_menus = pygame.font.Font(os.path.join(os.getcwd(), 'fonts', 'comic.ttf'), 24)
    font_window = pygame.font.Font(os.path.join(os.getcwd(), 'fonts', 'comic.ttf'), 36)


class Images:
    bird_winds_up = convert('bird_wings_up', width=0.0556 * HEIGHT, height=0.0417 * HEIGHT)
    bird_winds_down = convert('bird_wings_down', width=0.0556 * HEIGHT, height=0.0417 * HEIGHT)
    bird_crash = convert('bird_crash', height=0.0417 * HEIGHT, square=False)
    bird_images = []
    for bird in [bird_winds_up, bird_winds_down, bird_crash]:
        bird_images.append(bird)
        
    bird_up = pygame.transform.rotate(bird_images[1], angle=15)
    bird_down = pygame.transform.rotate(bird_images[0], angle=-15)

    bg = convert('bg', height=HEIGHT, square=False)

    wall_image = convert('column', 0.15 * HEIGHT, 0.65 * HEIGHT)
    heart = convert('heart', 0.1 * HEIGHT)

    big_jump = convert('big_jump', 0.15 * HEIGHT)
    small_jump = convert('small_jump', 0.055 * HEIGHT)

    pygame.display.set_caption('NOT a flappy bird')
    pygame.display.set_icon(bird_images[-1])
