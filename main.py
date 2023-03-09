__version__ = '0.1'

from inspect import getouterframes, currentframe
from sys import exit, getrecursionlimit, setrecursionlimit
from time import perf_counter

import pygame

from bird import Bird
from constants import START_LIVES, START_TRACK, BIRD_START, SPEED, FPS, WIDTH, HEIGHT
from design import Images, Text
from menus import Menus
from walls import Wall
from window import Window


class Game:
    walls = pygame.sprite.Group()
    lives = START_LIVES
    score = 0

    def __init__(self):
        self.breakdown = False
        self.game_starts = False
        self.track = START_TRACK
        self.main_window = Window(self)
        self.bird = Bird()
        self.menu = Menus(self)
        self.menu.call_menu(self)

    def crash(self):
        for wall in self.walls:
            if wall.rect.collidepoint(self.bird.rect.midright) or wall.rect.collidepoint(self.bird.rect.bottomright) or self.breakdown:
                self.game_starts = False
                self.track = START_TRACK
                self.bird.timer = 0
                self.bird.jump = 0
                self.bird.image = Images.bird_images[-1]
                self.main_window.elements.escape_timer = 0
                self.lives -= 1
                self.menu.crash_menu.enable()
                break
            # self.sound_catch.play()

    def new_game(self):
        self.lives = START_LIVES
        self.score = 0
        Wall.speed = SPEED
        self.main_window = Window(self)
        self.resume_game()

    def resume_game(self):
        self.breakdown = False
        self.menu.disable()
        self.game_starts = True
        self.bird.rect.center = BIRD_START
        self.bird.image = Images.bird_images[0]
        for wall in self.walls:
            wall.kill()
        self.mainloop()

    def mainloop(self):

        if len(getouterframes(currentframe())) > getrecursionlimit() - 100:
            setrecursionlimit(getrecursionlimit() + 100)

        self.start = perf_counter()  #temp

        while True:
            self.game_starts = True

            if not self.walls.sprites() or self.walls.sprites()[-1].rect.right < WIDTH * 0.85 - 2 * Wall.speed ** 2:
                Wall.create_wall(game=self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.FINGERDOWN:
                    self.bird.jump = 35
                elif event.type == pygame.FINGERMOTION:
                    print(event, event.type)
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE or event.key == pygame.K_AC_BACK) and not self.main_window.elements.escape_timer:
                        self.main_window.elements.escape_timer = 3 * FPS
                    elif event.key == pygame.K_ESCAPE or event.key == pygame.K_AC_BACK:
                        self.breakdown = True
                    elif event.key == pygame.K_SPACE:
                        self.bird.jump = 35
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.bird.jump = 25




            self.walls.update(self, self.main_window)

            # self.crash()
            if not self.game_starts:
                self.menu.call_menu(self, crash=True)

            self.main_window.bg_rect.x -= 1
            self.main_window.update_window(self)


if __name__ == '__main__':
    Game()
