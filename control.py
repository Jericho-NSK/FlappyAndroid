import pygame

from constants import WIDTH, HEIGHT, FPS
from design import Images


class Controller:

    @staticmethod
    def control_android(game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.FINGERDOWN:
                event.finger_id = 0
                if game.main_window.elements.big_jump_bg_rect.collidepoint(event.x * WIDTH, event.y * HEIGHT):
                    game.bird.jump = 37
                elif game.main_window.elements.left_jump_bg_rect.collidepoint(event.x * WIDTH, event.y * HEIGHT) or \
                        game.main_window.elements.right_jump_bg_rect.collidepoint(event.x * WIDTH, event.y * HEIGHT):
                    game.bird.jump = 30

            elif event.type == pygame.FINGERMOTION:
                event.finger_id = 1
                if game.main_window.elements.touchpad_bg_rect.collidepoint(event.x * WIDTH, event.y * HEIGHT):
                    game.main_window.elements.joystick_rect.center = event.x * WIDTH, event.y * HEIGHT
                    game.bird.moving = True
                    if abs(event.dx) > event.dy and event.dx < 0:
                        game.bird.move_left = True
                        game.bird.move_right = False
                        game.bird.move_down = False
                    elif abs(event.dx) > event.dy and event.dx > 0:
                        game.bird.move_left = False
                        game.bird.move_right = True
                        game.bird.move_down = False
                    elif abs(event.dx) < event.dy and event.dy > 0.003:
                        game.bird.move_left = False
                        game.bird.move_right = False
                        game.bird.move_down = True

                print('FINGERMOTION', event)

            elif event.type == pygame.FINGERUP and game.bird.moving:
                game.main_window.elements.joystick_rect.midtop = (game.main_window.elements.touchpad_bg_rect.x +
                                                                  game.main_window.elements.touchpad_bg_rect.width // 2,
                                                                  game.main_window.elements.touchpad_bg_rect.y)
                game.bird.image = Images.bird_images[game.bird.wings_up]
                game.bird.moving = False
                game.bird.move_left = False
                game.bird.move_right = False
                game.bird.move_down = False
                print('FINGERUP', event, type(event.finger_id), event.finger_id, type(event.touch_id), event.touch_id)

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
                    game.bird.jump = 37
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    game.bird.jump = 30

        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            game.bird.move_left = True
        elif not key[pygame.K_a] and not key[pygame.K_LEFT]:
            game.bird.move_left = False
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            game.bird.move_right = True
        elif not key[pygame.K_d] and not key[pygame.K_RIGHT]:
            game.bird.move_right = False
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            game.bird.move_down = True
        elif not key[pygame.K_s] and not key[pygame.K_DOWN]:
            game.bird.move_down = False

        if not key[pygame.K_s] and not key[pygame.K_DOWN] and not game.bird.jump:
            game.bird.image = Images.bird_images[game.bird.wings_up]
