import pygame

from constants import WIDTH, FPS, WINDOW, CLOCK
from design import Images
from elements import Elements


class Window:
    window = WINDOW

    def __init__(self, game):
        self.bg_rect = Images.bg.get_rect()
        self.elements = Elements(game)

    def update_window(self, game):
        self.window.blit(Images.bg, (self.bg_rect.x, 0))
        self.window.blit(Images.bg, (self.bg_rect.x + self.bg_rect.width, 0))
        if self.bg_rect.x <= - self.bg_rect.width:
            self.bg_rect.x = 0

        game.walls.draw(self.window)

        self.window.blits(
            (
                (self.elements.score, (20, 20)),
                (self.elements.speed, (20, 60)),
                *((Images.heart,
                   (WIDTH - 1.15 * self.elements.heart_rect.w * (heart + 1),
                    self.elements.heart_rect.y)) for heart in range(game.lives)),
                (game.bird.image, (game.bird.rect.centerx, game.bird.rect.centery)),
            ),
            doreturn=False)

        if self.elements.escape_timer:
            self.window.blit(self.elements.escape_up, self.elements.escape_up_rect.topleft)
            self.window.blit(self.elements.escape_down, self.elements.escape_down_rect.topleft)
            self.elements.escape_timer -= 1


        if game.bird.image != Images.bird_images[-1]:
            game.bird.flying(game)
        if game.game_starts:
            self.control_buttons()
            pygame.display.update()

        CLOCK.tick(FPS)

    def control_buttons(self):
        self.window.blits(
            (
                (self.elements.big_jump_bg, self.elements.big_jump_bg_rect),
                (Images.big_jump, self.elements.big_jump.topleft),
                (self.elements.left_jump_bg, self.elements.left_jump_bg_rect),
                (Images.small_jump, self.elements.left_jump.topleft),
                (self.elements.right_jump_bg, self.elements.right_jump_bg_rect),
                (Images.small_jump, self.elements.right_jump.topleft),
            ),
            doreturn=False)
