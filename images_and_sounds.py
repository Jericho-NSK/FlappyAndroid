import pygame
import os

abspath = os.getcwd() + "/"
class Images:

    images = 'bird_up.png', 'bird_down.png', 'bird_crash.png'
    bird_images = [pygame.image.load(abspath + 'images/' + bird).convert_alpha() for bird in images]
    bird_up = pygame.transform.rotate(bird_images[1], angle=15)
    bird_down = pygame.transform.rotate(bird_images[0], angle=-15)

    bg = pygame.image.load(abspath + 'images/bg.png').convert()

    pygame.display.set_caption('NOT a flappy bird')
    pygame.display.set_icon(bird_images[-1])

    wall_image = pygame.image.load(abspath + 'images/column.png').convert_alpha()
    heart = pygame.image.load(abspath + 'images/heart.png').convert_alpha()
