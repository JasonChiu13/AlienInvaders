import pygame as pg
import pygame.font


class Button:
    def __init__(self, game, msg):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.msg = msg

        self.width, self.height = 140, 60
        self.button_color = self.settings.button_color
        self.bg_color = self.settings.bg_color
        self.text_color = self.settings.text_color
        self.font = pygame.font.SysFont(None, 100)

        self.rect = pg.Rect(self.screen_rect.centerx - self.width / 2, self.screen_rect.centery - self.height / 2,
                            self.width, self.height)

        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.bottom * 4/5

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.button_color,
                                          self.bg_color)
        self.msg_image_rect = self.rect
        self.msg_image_rect.centerx = self.rect.x
        self.msg_image_rect.centery = self.rect.y

    def draw(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def update(self):
        if self.game.home_screen:
            self.draw()