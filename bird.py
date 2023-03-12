import pygame

from constants import HEIGHT, WIDTH, FPS, BIRD_SIZE, BIRD_START, SYSTEM
from design import Images


class Bird(pygame.Surface):
    """Class for Bird's mechanics"""
    timer = FPS // 2

    def __init__(self):
        super().__init__(size=BIRD_SIZE)
        self.rect = self.get_rect()
        self.rect.center = BIRD_START
        self.image = Images.bird_images[1]
        self.jump = 0
        self.wings_up = False

    def jumping(self):
        """Jumping mechanics"""
        if self.jump > 14:
            self.image = Images.bird_up
            self.rect.centery -= int((0.1 * self.jump) ** 2) - 1
            self.jump -= 1
        elif self.jump:
            self.image = Images.bird_images[self.wings_up]
            self.rect.centery -= int((0.1 * self.jump) ** 2) - 1
            self.jump -= 1
            self.timer = 0
            self.wings_up = False

    def flapping_wings(self):
        """Changes the position of the wings"""
        if not self.timer and not self.jump:
            self.image = Images.bird_images[self.wings_up]
            self.wings_up ^= 1  # is equal to self.wings_up = not self.wings_up
            if SYSTEM != 'Windows':
                self.timer = FPS // 10
            else:
                self.timer = FPS // 3

        else:
            self.timer -= 1

    def gravity(self):
        """Gravity and limits"""
        self.rect.centery += 1
        if self.rect.bottom > HEIGHT - self.rect.height // 2:
            self.rect.bottom = HEIGHT - self.rect.height // 2
        if self.rect.top < -self.rect.height // 2:
            self.rect.top = -self.rect.height // 2

    def flying(self, game):
        """Functions for flying and controls of Bird"""
        self.jumping()
        self.flapping_wings()

        if game.game_starts:
            self.gravity()
