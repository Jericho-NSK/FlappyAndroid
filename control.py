import pygame

from constants import WIDTH, HEIGHT, FPS
from design import Images


class Controller:
    def __init__(self):
        self.moving = False

    def control_android(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.FINGERDOWN:
                if game.main_window.elements.big_jump_bg_rect.collidepoint(event.x * WIDTH, event.y * HEIGHT):
                    game.bird.jump = 35
                elif game.main_window.elements.left_jump_bg_rect.collidepoint(event.x * WIDTH, event.y * HEIGHT) or \
                        game.main_window.elements.right_jump_bg_rect.collidepoint(event.x * WIDTH, event.y * HEIGHT):
                    game.bird.jump = 25
                elif game.main_window.elements.touchpad_bg_rect.collidepoint(event.x * WIDTH, event.y * HEIGHT):
                    self.moving = True
                    game.main_window.elements.joystick_rect.center = event.x * WIDTH, event.y * HEIGHT

            elif event.type == pygame.FINGERUP and self.moving:
                game.main_window.elements.joystick_rect.center = (game.main_window.elements.touchpad_bg_rect.x +
                                                                  game.main_window.elements.touchpad_bg_rect.width // 2,
                                                                  game.main_window.elements.touchpad_bg_rect.y)
                game.bird.image = Images.bird_images[game.bird.wings_up]
                self.moving = False
                print('FINGERUP', event, event.type)

            elif event.type == pygame.FINGERMOTION and self.moving:
                if abs(event.dx) > event.dy and event.dx < 0:
                    game.bird.rect.centerx -= 4
                elif abs(event.dx) > event.dy and event.dx > 0:
                    game.bird.rect.centerx += 4
                elif abs(event.dx) < event.dy and event.dy > 0:
                    game.bird.rect.centery += 1
                    game.bird.image = Images.bird_down

                print('FINGERMOTION', event, event.type)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_AC_BACK and not game.main_window.elements.escape_timer:
                    game.main_window.elements.escape_timer = 3 * FPS
                elif event.key == pygame.K_AC_BACK:
                    game.crash(breakdown=True)

    @staticmethod
    def control_windows(game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not game.main_window.elements.escape_timer:
                    game.main_window.elements.escape_timer = 3 * FPS
                elif event.key == pygame.K_ESCAPE:
                    game.crash(breakdown=True)
                elif event.key == pygame.K_SPACE:
                    game.bird.jump = 35
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    game.bird.jump = 25

        key = pygame.key.get_pressed()
        if any((key[pygame.K_a], key[pygame.K_LEFT])) and game.bird.rect.centerx > 0:
            game.bird.rect.centerx -= 4
        if any((key[pygame.K_d], key[pygame.K_RIGHT])) and game.bird.rect.right < WIDTH - game.bird.rect.width:
            game.bird.rect.centerx += 4
        if any((key[pygame.K_s], key[pygame.K_DOWN])) and not game.bird.jump:
            game.bird.rect.centery += 1
            game.bird.image = Images.bird_down
        if not any((key[pygame.K_s], key[pygame.K_DOWN], game.bird.jump)):
            game.bird.image = Images.bird_images[game.bird.wings_up]
