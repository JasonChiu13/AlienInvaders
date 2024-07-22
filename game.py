import pygame as pg
from settings import Settings
from laser import Lasers, LaserType
from alien import Aliens, Boss
from ship import Ship
from sound import Sound
from scoreboard import Scoreboard
from vector import Vector
from barrier import Barriers
from button import Button
import sys 


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Alien Invasion")

        self.sound = Sound()
        self.scoreboard = Scoreboard(game=self)
        self.play_button = Button(game=self, msg="Play")

        self.ship_lasers = Lasers(settings=self.settings, type=LaserType.SHIP)
        self.alien_lasers = Lasers(settings=self.settings, type=LaserType.ALIEN)
        
        self.barriers = Barriers(game=self)
        self.ship = Ship(game=self)
        self.aliens = Aliens(game=self)
        self.boss = Boss(game=self)
        self.boss_exist = False
        self.boss_timer = 0
        self.settings.initialize_speed_settings()
        self.home_screen = True

    def handle_events(self):
        keys_dir = {pg.K_w: Vector(0, -1), pg.K_UP: Vector(0, -1), 
                    pg.K_s: Vector(0, 1), pg.K_DOWN: Vector(0, 1),
                    pg.K_a: Vector(-1, 0), pg.K_LEFT: Vector(-1, 0),
                    pg.K_d: Vector(1, 0), pg.K_RIGHT: Vector(1, 0)}
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if not self.home_screen:
                    self.game_over()
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                key = event.key
                if key in keys_dir:
                    self.ship.v += self.settings.ship_speed * keys_dir[key]
                elif key == pg.K_SPACE:
                    self.ship.open_fire()
            elif event.type == pg.KEYUP:
                key = event.key
                if key in keys_dir:
                    self.ship.v = Vector()
                elif key == pg.K_SPACE:
                    self.ship.cease_fire()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.check_play_button(self.play_button, mouse_x, mouse_y)

    def check_play_button(self, play_button, mouse_x, mouse_y):
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and self.home_screen:
            pg.mouse.set_visible(False)
            self.reset()
            self.scoreboard.reset()
            self.ship.ships_left = self.settings.ship_limit
            self.home_screen = False

    def reset(self):
        print('Resetting game...')
        # self.lasers.reset()    # handled by ship for ship_lasers and by aliens for alien_lasers
        self.sound.play_bg()
        self.barriers.reset()
        self.ship.reset()
        self.aliens.reset()
        self.boss.reset()

    def game_over(self):
        self.sound.play_gameover()
        f = open('high_score/high_score.txt', 'w')
        f.seek(0)
        f.write(str(self.scoreboard.high_score))
        f.truncate()
        f.close()
        self.home_screen = True
        pg.mouse.set_visible(True)

    def play(self):
        while True:
            pg.display.update()
            self.screen.fill(self.settings.bg_color)
            self.handle_events()
            self.scoreboard.update()
            if self.home_screen:
                self.play_button.update()
            if not self.home_screen:
                self.aliens.update()
                self.boss.update()
                self.barriers.update()
                self.ship.update()
            pg.display.flip()


def main():
    g = Game()
    g.play()

if __name__ == '__main__':
    main()
