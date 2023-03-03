from webbrowser import open_new_tab

import pygame
import pygame_menu

from constants import HEIGHT, WIDTH, FPS
from walls import Wall


class Menus:
    theme = pygame_menu.themes.THEME_BLUE.copy()
    theme.set_background_color_opacity(0.5)
    # theme.widget_font = 'comicsansms'
    theme.widget_font_size = 30
    theme.widget_font_color = 'blue'
    theme.widget_selection_color = 'green'
    theme.widget_padding = 10

    main_menu = pygame_menu.Menu(title='Main Menu',
                                 width=WIDTH // 2,
                                 height=HEIGHT // 2,
                                 theme=theme,
                                 )
    # main_menu.enable()
    settings_menu = pygame_menu.Menu(title='Settings',
                                     width=WIDTH // 2,
                                     height=HEIGHT // 2,
                                     theme=theme,
                                     )

    about_menu = pygame_menu.Menu(title='About',
                                  width=WIDTH // 2,
                                  height=HEIGHT // 2,
                                  theme=theme,
                                  )

    about_menu = pygame_menu.Menu(title='About',
                                  width=WIDTH // 2,
                                  height=HEIGHT // 2,
                                  theme=theme,
                                  )

    crash_menu = pygame_menu.Menu(title='CRASH!',
                                  width=WIDTH // 2,
                                  height=HEIGHT // 1.7,
                                  theme=theme,
                                  )

    exit_menu = pygame_menu.Menu(title='Exit?',
                                 width=WIDTH // 3,
                                 height=HEIGHT // 3,
                                 theme=theme,
                                 )

    def __init__(self, game):
        self.surface = game.main_window.window
        self.create_main_menu(game)
        self.create_settings_menu()
        self.create_about_menu()
        self.create_exit_menu()

    def create_main_menu(self, game):
        self.main_menu.add.button('NEW GAME', game.new_game)
        self.main_menu.add.button('SETTINGS', self.settings_menu)
        self.main_menu.add.button('ABOUT', self.about_menu)
        self.main_menu.add.button('EXIT', self.exit_menu)

    def create_settings_menu(self):
        self.settings_menu.add.toggle_switch('FULL SCREEN',
                                             default=pygame.display.is_fullscreen(),
                                             onchange=lambda x: pygame.display.toggle_fullscreen(),
                                             )
        self.settings_menu.add.toggle_switch('MUSIC',
                                             default=pygame.display.is_fullscreen(),
                                             onchange=lambda x: pygame.display.toggle_fullscreen(),
                                             )
        self.settings_menu.add.toggle_switch('SOUNDS',
                                             default=pygame.display.is_fullscreen(),
                                             onchange=lambda x: pygame.display.toggle_fullscreen(),
                                             )
        self.settings_menu.add.button('BACK', pygame_menu.events.BACK)

    def create_about_menu(self):
        self.about_menu.add.label('NOT a flappy bird v1.0\nCreated by Jericho for Pet-project', font_color=(0, 135, 0))
        self.about_menu.add.vertical_margin(30)
        self.about_menu.add.button('LINK TO GITHUB', lambda: open_new_tab(
            'https://github.com/Jericho-NSK/PyPython/tree/main/2023-02.2%20Flappy%20Pygame%20Pet%20Project'))
        self.about_menu.add.button('BACK', pygame_menu.events.BACK)

    def create_exit_menu(self):
        question = self.exit_menu.add.label('ARE YOU SURE?')
        self.exit_menu.add.vertical_fill(self.exit_menu.get_height() - 2 * question.get_height())

        yes = self.exit_menu.add.button('YES', pygame_menu.events.EXIT)
        yes.set_float(float_status=True, origin_position=True)
        yes.translate(0.15 * self.exit_menu.get_width(), self.exit_menu.get_height() - 2.3 * yes.get_height())

        no = self.exit_menu.add.button('NO', pygame_menu.events.BACK)
        no.set_float(float_status=True, origin_position=True)
        no.translate(0.85 * self.exit_menu.get_width() - no.get_width(), self.exit_menu.get_height() - 2.3 * no.get_height())

    def create_crash_menu(self, game):
        self.crash_menu.add.label(f'YOU LOST A LIFE!\nLIVES LEFT: {game.lives} '
                                  if game.lives
                                  else f'YOU LOSE ON SPEED {Wall.speed}!\nYOUR SCORE: {game.score}',
                                  font_color=(235, 0, 0))
        self.crash_menu.add.vertical_margin(30)
        self.crash_menu.add.button('RESUME' if game.lives else 'NEW GAME',
                                   game.resume_game if game.lives else game.new_game)
        self.crash_menu.add.button('MAIN MENU', self.main_menu)
        self.crash_menu.add.button('EXIT', self.exit_menu)
        self.crash_menu.force_surface_update()

    def call_menu(self, game, crash=False, exit_=False):
        self.crash_menu.clear()
        self.create_crash_menu(game)

        while True:
            if crash:
                self.crash_menu.mainloop(self.surface,
                                         game.main_window.update_window(game),
                                         disable_loop=True,
                                         clear_surface=False,
                                         fps_limit=FPS)
            elif exit_:
                self.exit_menu.mainloop(self.surface,
                                        game.main_window.update_window(game),
                                        disable_loop=True,
                                        clear_surface=False,
                                        fps_limit=FPS)
            else:
                self.main_menu.mainloop(self.surface,
                                        game.main_window.update_window(game),
                                        disable_loop=True,
                                        clear_surface=False,
                                        fps_limit=FPS)

    def disable(self):
        self.main_menu.disable()
        self.settings_menu.disable()
        self.exit_menu.disable()
        self.crash_menu.disable()
        self.about_menu.disable()
