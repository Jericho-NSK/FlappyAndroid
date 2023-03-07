import pygame

from constants import WIDTH, HEIGHT
from design import Images, Text
from walls import Wall


class Elements:

    def __init__(self, game, window):
        self.score = Text.font_window.render(f'SCORE: {game.score}', True, 'red')
        self.speed = Text.font_window.render(f'SPEED: {Wall.speed}', True, 'red')

        self.escape_up = Text.font_window.render('NO PAUSES! ONLY HARDCORE!', True, 'red')
        self.escape_down = Text.font_window.render('PRESS BACK AGAIN TO GIVE UP', True, 'red')
        self.escape_up_rect = self.escape_up.get_rect()
        self.escape_up_rect.center = WIDTH // 2, HEIGHT - 3 * self.escape_up_rect.h
        self.escape_down_rect = self.escape_down.get_rect()
        self.escape_down_rect.center = WIDTH // 2, HEIGHT - 2 * self.escape_down_rect.h
        self.escape_timer = 0

        self.heart_rect = Images.heart.get_rect()

        self.surf = pygame.Surface((HEIGHT // 4, HEIGHT // 4)).convert_alpha()
        self.surfr = self.surf.get_rect()
        self.surfr.center = int(WIDTH * 0.85), int(HEIGHT * 0.65)




        self.surf.fill((0, 0, 0, 0))
        pygame.draw.circle(
            self.surf,
            color=(0, 0, 0, 100),
            center=(self.surfr.height // 2, self.surfr.height // 2),
            radius=self.surfr.height // 2,
            width=20
        )
        window.window.blit(Images.big_jump, self.surfr)



        self.big_jump_surf = Images.big_jump.get_rect()
        self.big_jump_surf.center = (int(WIDTH * 0.9), int(HEIGHT * 0.75))

        self.small_jump_surf = Images.small_jump.get_rect()
        self.small_jump_surf.center = (int(WIDTH * 0.7), int(HEIGHT * 0.9))


        self.big_jump = Images.big_jump.get_rect()
        self.small_jump = Images.small_jump.get_rect()
