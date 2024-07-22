
import pygame as pg
from laser import LaserType
import time


class Sound:
    def __init__(self):
        pg.mixer.music.load('sounds/startrek.wav')
        pg.mixer.music.set_volume(0.3)
        self.alienlaser = pg.mixer.Sound('sounds/alienlaser.wav')
        self.photontorpedo = pg.mixer.Sound('sounds/photon_torpedo.wav')
        self.explosion = pg.mixer.Sound('sounds/explosion.wav')
        self.pop = pg.mixer.Sound('sounds/pop.wav')
        self.gameover = pg.mixer.Sound('sounds/gameover.wav')

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def shoot_laser(self, type):
        pg.mixer.Sound.play(self.alienlaser if type == LaserType.ALIEN else self.photontorpedo)

    def play_explosion(self):
        pg.mixer.Sound.play(self.explosion)

    def play_pop(self):
        pg.mixer.Sound.play(self.pop)

    def play_gameover(self):
        self.stop_bg()
        pg.mixer.Sound.play(self.gameover)
        time.sleep(3)