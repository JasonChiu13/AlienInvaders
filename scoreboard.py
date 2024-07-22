import pygame as pg
from pygame.sprite import Group
from ship import Ship
# import pygame.font


class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.level = 0
        f = open('high_score/high_score.txt', 'r')
        self.high_score = int(f.read())
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (255, 255, 255)
        self.title_font = pg.font.SysFont(None, 150)
        self.font = pg.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        #self.prep_level()

    #def increment_score(self):
     #   self.score += self.settings.alien_points_{}
      #  self.prep_score()
       # self.prep_high_score()

    def prep_score(self): 
        score_str = f' Score: {str(self.score)}'
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score_str = f'High Score: {str(self.high_score)}'
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.bottom * 7/8

    def draw_title(self):
        for i in range(1, 5):
            point_image = self.font.render((f'=  {i}0' if i != 4 else f'=  ???'), True, self.text_color, self.settings.bg_color)
            point_rect = point_image.get_rect()
            point_rect.left = self.screen_rect.centerx
            point_rect.top = self.screen_rect.bottom * (4 + i) / 12
            self.screen.blit(point_image, point_rect)
            alien_image = pg.transform.rotozoom(pg.image.load(f'images/alien_{i}0_0.png'if i != 4 else f'images/alien_100_0.png'), 0, 2.2)
            alien_rect = alien_image.get_rect()
            alien_rect.right = self.screen_rect.centerx - 20
            alien_rect.top = self.screen_rect.bottom * (4 + 1.1 * i) / 13
            self.screen.blit(alien_image, alien_rect)

        for j in range(2):
            title_image = self.title_font.render(('   Alien' if j == 0 else 'Invaders'), True, self.text_color, self.settings.bg_color)
            title_rect = self.high_score_image.get_rect()
            title_rect.centerx = 520
            title_rect.top = self.screen_rect.bottom * (j + 1)/8
            self.screen.blit(title_image, title_rect)

    def prep_level(self):
        self.level_image = self.font.render(str(self.level), True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = 70

    def reset(self): 
        self.score = 0
        self.update()

    def update(self):
        self.prep_score()
        self.prep_high_score()
        self.draw()

    def draw(self):
        if self.game.home_screen:
            self.screen.blit(self.high_score_image, self.high_score_rect)
            self.draw_title()
        else:
            self.screen.blit(self.score_image, self.score_rect)

