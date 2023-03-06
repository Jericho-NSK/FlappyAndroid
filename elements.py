from constants import WIDTH, HEIGHT
from design import Images, Text
from walls import Wall


class Elements:

    def __init__(self, game):
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
