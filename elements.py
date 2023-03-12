import pygame

from constants import WIDTH, HEIGHT, SYSTEM
from design import Images, Text
from walls import Wall


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class Elements:

    def __init__(self, game):
        self.score = Text.font_window.render(f'SCORE: {game.score}', True, 'red')
        self.speed = Text.font_window.render(f'SPEED: {Wall.speed}', True, 'red')
        self.heart_rect = Images.heart.get_rect()
        self.escape_elements()
        self.big_jump_button(pos_width=0.8, pos_height=0.7, element_color=(10, 90, 90, 90), outer_color=(0, 0, 0, 100))
        self.right_jump_button(pos_width=0.74, pos_height=0.9, element_color=(90, 90, 10, 90), outer_color=(0, 0, 0, 100))
        self.left_jump_button(pos_width=0.13, pos_height=0.63, element_color=(90, 10, 90, 20), outer_color=(0, 0, 0, 50))
        self.touchpad_creator(pos_width=0.2, pos_height=0.86, element_color=(90, 90, 10, 90), outer_color=(0, 0, 0, 100))
        self.joyctick_creator(element_color=(255, 255, 255, 130), outer_color=(0, 0, 0, 120))

    def escape_elements(self):
        self.escape_up = Text.font_window.render('NO PAUSES! ONLY HARDCORE!', True, 'red')
        self.escape_down = Text.font_window.render('PRESS BACK AGAIN TO GIVE UP' if SYSTEM != 'Windows'
                                                   else 'PRESS ESCAPE AGAIN TO GIVE UP', True, 'red')
        self.escape_up_rect = self.escape_up.get_rect()
        self.escape_up_rect.center = WIDTH // 2, HEIGHT - 3 * self.escape_up_rect.h
        self.escape_down_rect = self.escape_down.get_rect()
        self.escape_down_rect.center = WIDTH // 2, HEIGHT - 2 * self.escape_down_rect.h
        self.escape_timer = 0

    def big_jump_button(self, pos_width, pos_height, element_color, outer_color):
        self.big_jump = Images.big_jump.get_rect()

        self.big_jump_bg = pygame.Surface((self.big_jump.width * 1.6, self.big_jump.height * 1.6)).convert_alpha()
        self.big_jump_bg_rect = self.big_jump_bg.get_rect()
        self.big_jump_bg_rect.center = int(WIDTH * pos_width), int(HEIGHT * pos_height)
        self.big_jump_bg.fill((0, 0, 0, 0))

        pygame.draw.circle(
            surface=self.big_jump_bg,
            color=element_color,
            center=(self.big_jump_bg_rect.width // 2, self.big_jump_bg_rect.height // 2),
            radius=self.big_jump_bg_rect.height // 2,
        )

        pygame.draw.circle(
            surface=self.big_jump_bg,
            color=outer_color,
            center=(self.big_jump_bg_rect.width // 2, self.big_jump_bg_rect.height // 2),
            radius=self.big_jump_bg_rect.height // 2,
            width=20,
        )

        self.big_jump.topleft = (self.big_jump_bg_rect.centerx - self.big_jump.width // 2,
                                 self.big_jump_bg_rect.centery - self.big_jump.height // 2)

    def right_jump_button(self, pos_width, pos_height, element_color, outer_color):
        self.right_jump = Images.small_jump.get_rect()

        self.right_jump_bg = pygame.Surface((self.right_jump.width * 1.6, self.right_jump.height * 1.6)).convert_alpha()
        self.right_jump_bg_rect = self.right_jump_bg.get_rect()
        self.right_jump_bg_rect.center = int(WIDTH * pos_width), int(HEIGHT * pos_height)
        self.right_jump_bg.fill((0, 0, 0, 0))

        pygame.draw.circle(
            surface=self.right_jump_bg,
            color=element_color,
            center=(self.right_jump_bg_rect.width // 2, self.right_jump_bg_rect.height // 2),
            radius=self.right_jump_bg_rect.height // 2,
        )

        pygame.draw.circle(
            surface=self.right_jump_bg,
            color=outer_color,
            center=(self.right_jump_bg_rect.width // 2, self.right_jump_bg_rect.height // 2),
            radius=self.right_jump_bg_rect.height // 2,
            width=13,
        )

        self.right_jump.topleft = (self.right_jump_bg_rect.centerx - self.right_jump.width // 2,
                                   self.right_jump_bg_rect.centery - self.right_jump.height // 2)

    def left_jump_button(self, pos_width, pos_height, element_color, outer_color):
        self.left_jump = Images.small_jump.get_rect()

        self.left_jump_bg = pygame.Surface((self.left_jump.width * 1.6, self.left_jump.height * 1.6)).convert_alpha()
        self.left_jump_bg_rect = self.left_jump_bg.get_rect()
        self.left_jump_bg_rect.center = int(WIDTH * pos_width), int(HEIGHT * pos_height)
        self.left_jump_bg.fill((0, 0, 0, 0))

        pygame.draw.circle(
            surface=self.left_jump_bg,
            color=element_color,
            center=(self.left_jump_bg_rect.width // 2, self.left_jump_bg_rect.height // 2),
            radius=self.left_jump_bg_rect.height // 2,
        )

        pygame.draw.circle(
            surface=self.left_jump_bg,
            color=outer_color,
            center=(self.left_jump_bg_rect.width // 2, self.left_jump_bg_rect.height // 2),
            radius=self.left_jump_bg_rect.height // 2,
            width=13,
        )

        self.left_jump.topleft = (self.left_jump_bg_rect.centerx - self.left_jump.width // 2,
                                  self.left_jump_bg_rect.centery - self.left_jump.height // 2)

    def touchpad_creator(self, pos_width, pos_height, element_color, outer_color):
        self.touchpad = pygame.Surface((HEIGHT * 0.4, HEIGHT * 0.2)).convert_alpha()
        self.touchpad_rect = self.touchpad.get_rect()
        self.touchpad_rect.center = int(WIDTH * pos_width), int(HEIGHT * pos_height)
        self.touchpad.fill((0, 0, 0, 0))

        self.touch_left = pygame.Surface((self.touchpad_rect.width * 0.45, self.touchpad_rect.height * 0.5)).convert_alpha()
        self.touch_left_rect = self.touch_left.get_rect()
        self.touch_left_rect.topleft = self.touchpad_rect.topleft
        self.touch_left.fill((200, 0, 0, 200))

        self.touch_right = pygame.Surface((self.touch_left_rect.width, self.touch_left_rect.height)).convert_alpha()
        self.touch_right_rect = self.touch_left.get_rect()
        self.touch_right_rect.topleft = self.touchpad_rect.topright[0] - self.touch_right_rect.width, self.touchpad_rect.y
        self.touch_right.fill((0, 200, 0, 200))

        self.touch_down = pygame.Surface((self.touchpad_rect.width, self.touchpad_rect.height * 0.65)).convert_alpha()
        self.touch_down_rect = self.touch_down.get_rect()
        self.touch_down_rect.topleft = self.touchpad_rect.x, self.touchpad_rect.y + self.touchpad_rect.height - self.touch_down_rect.height
        self.touch_down.fill((0, 0, 200, 200))

        self.touch_down_left = pygame.Surface((self.touchpad_rect.width * 0.35, self.touch_left_rect.height)).convert_alpha()
        self.touch_down_left_rect = self.touch_down_left.get_rect()
        self.touch_down_left_rect.topleft = self.touchpad_rect.x, self.touchpad_rect.y + self.touch_left_rect.height
        self.touch_down_left.fill((0, 200, 200, 200))

        self.touch_down_right = pygame.Surface((self.touch_down_left_rect.width, self.touch_left_rect.height)).convert_alpha()
        self.touch_down_right_rect = self.touch_down_right.get_rect()
        self.touch_down_right_rect.topleft = (self.touchpad_rect.topright[0] - self.touch_down_right_rect.width,
                                              self.touchpad_rect.y + self.touch_right_rect.height)
        self.touch_down_right.fill((200, 200, 0, 200))

        pygame.draw.circle(
            surface=self.touchpad,
            color=element_color,
            center=(self.touchpad_rect.width // 2, 0),
            radius=self.touchpad_rect.height,
        )

        pygame.draw.circle(
            surface=self.touchpad,
            color=outer_color,
            center=(self.touchpad_rect.width // 2, 0),
            radius=self.touchpad_rect.height,
            width=14,
        )

    def joyctick_creator(self, element_color, outer_color):
        self.joystick = pygame.Surface((HEIGHT * 0.08, HEIGHT * 0.08)).convert_alpha()
        self.joystick_rect = self.joystick.get_rect()
        self.joystick_rect.midtop = self.touchpad_rect.x + self.touchpad_rect.width // 2, self.touchpad_rect.y
        self.joystick.fill((0, 0, 0, 0))

        pygame.draw.circle(
            surface=self.joystick,
            color=element_color,
            center=(self.joystick_rect.width // 2, self.joystick_rect.height // 2),
            radius=self.joystick_rect.height // 2,
        )

        pygame.draw.circle(
            surface=self.joystick,
            color=outer_color,
            center=(self.joystick_rect.width // 2, self.joystick_rect.height // 2),
            radius=self.joystick_rect.height // 2,
            width=4,
        )
