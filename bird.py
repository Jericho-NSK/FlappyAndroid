import pygame

from constants import HEIGHT, WIDTH, FPS, BIRD_SIZE, BIRD_START
from images_and_sounds import Images


class Bird(pygame.Surface):
    timer = FPS // 2

    def __init__(self):
        super().__init__(size=BIRD_SIZE)
        self.rect = self.get_rect()
        self.rect.center = BIRD_START
        self.image = Images.bird_images[1]
        self.jump = 0
        self.wings_up = False

    def flying(self, game):
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

        if not self.timer and not self.jump:
            self.image = Images.bird_images[self.wings_up]
            self.wings_up = not self.wings_up
            self.timer = FPS // 3
        else:
            self.timer -= 1

        if game.game_starts:
            self.rect.centery += 1
            if self.rect.bottom > HEIGHT - self.rect.height // 2:
                self.rect.bottom = HEIGHT - self.rect.height // 2
            if self.rect.top < -self.rect.height // 2:
                self.rect.top = -self.rect.height // 2

            key = pygame.key.get_pressed()
            if any((key[pygame.K_a], key[pygame.K_LEFT])) and self.rect.centerx > 0:
                self.rect.centerx -= 4
            if any((key[pygame.K_d], key[pygame.K_RIGHT])) and self.rect.right < WIDTH - self.rect.width:
                self.rect.centerx += 4
            if any((key[pygame.K_s], key[pygame.K_DOWN])) and not self.jump:
                self.rect.centery += 1
                self.image = Images.bird_down
            if not any((key[pygame.K_s], key[pygame.K_DOWN], self.jump)):
                self.image = Images.bird_images[self.wings_up]
