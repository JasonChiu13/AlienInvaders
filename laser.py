import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer
from random import randint
from enum import Enum


class LaserType(Enum):
    ALIEN = 1
    SHIP = 2


class Lasers:  # TODO: add laser-laser collisions AND laser-barrier collisions
    def __init__(self, settings, type):
        self.lasers = Group()
        self.settings = settings
        self.type=type

    def reset(self): self.lasers.empty()        

    def shoot(self, game, x, y):
        self.lasers.add(Laser(settings=game.settings, screen=game.screen, 
                              x=x, y=y, sound=game.sound, type=self.type))

    def update(self):
        self.lasers.update()
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0: self.lasers.remove(laser)

    def draw(self):
        for laser in self.lasers.sprites(): laser.draw()

class Laser(Sprite):   # TODO -- change to use YOUR OWN IMAGES for ship, alien lasers
                       #         and the explosion between the two types of lasers
    """A class to manage lasers fired from the ship"""
    alien_laser_images = [pg.transform.rotozoom(pg.image.load(f'images/alienlaser{n}.png'), 0, 1.2) for n in range(2)]
    ship_laser_images = [pg.transform.rotozoom(pg.image.load(f'images/laser_{n}.png'), 0, 1.5) for n in range(2)]
    laser_images = {LaserType.ALIEN: alien_laser_images, LaserType.SHIP: ship_laser_images}
    laser_explosion_images = [pg.transform.rotozoom(pg.image.load(f'images/laser_explosion_{n}.png'), 0, 2) for n in range(4)]

    def __init__(self, settings, screen, x, y, sound, type):
        super().__init__()
        self.screen = screen
        self.rect = pg.Rect(0, 0, settings.laser_width, settings.laser_height)
        self.rect.centerx = x
        self.rect.bottom = y
        self.y = float(self.rect.y)
        self.type = type
        self.color = (randint(0, 200), randint(0, 200), randint(0, 200))
        self.speed_alien = settings.alien_laser_speed
        self.speed_ship = settings.ship_laser_speed

        self.timer_normal = Timer(image_list=Laser.laser_images[type])
        self.timer_collision = Timer(image_list=Laser.laser_explosion_images, delay=150, is_loop=False)
        sound.shoot_laser(type=self.type)
        self.timer = self.timer_normal
        self.dying = False

    def hit(self):
        if not self.dying:
            self.dying = True
            self.timer = self.timer_collision

    def update(self):
        if self.timer == self.timer_collision and self.timer.is_expired():
            self.kill()
        self.y += self.speed_alien if self.type == LaserType.ALIEN else -self.speed_ship
        if not self.dying:
            self.rect.y = self.y
        self.draw()

    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.center, rect.top = self.rect.center, self.rect.top
        self.screen.blit(image, rect)

