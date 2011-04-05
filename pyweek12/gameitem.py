
from os.path import join
from math import cos, sin, radians
from random import uniform

from pyglet.window import key

from rabbyt.sprites import Sprite

from .path import DATA


class GameItem(object):

    def __init__(self, image_name, **kwargs):
        if 'x' not in kwargs:
            kwargs['x'] = uniform(-2000, 2000)
        if 'y' not in kwargs:
            kwargs['y'] = uniform(-2000, 2000)
        self.sprite = Sprite(
            join(DATA, 'images', image_name),
        )
        for name, value in kwargs.iteritems():
            setattr(self, name, value)

    # properties that delegate to storage on the sprite

    def __get_x(self):
        return self.sprite.x
    def __set_x(self, value):
        self.sprite.x = value
    x = property(__get_x, __set_x)

    def __get_y(self):
        return self.sprite.y
    def __set_y(self, value):
        self.sprite.y = value
    y = property(__get_y, __set_y)

    def __get_rot(self):
        return self.sprite.rot
    def __set_rot(self, value):
        self.sprite.rot = value
    rot = property(__get_rot, __set_rot)

    def __get_scale(self):
        return self.sprite.scale
    def __set_scale(self, value):
        self.sprite.scale = value
    scale = property(__get_scale, __set_scale)

    def __get_red(self):
        return self.sprite.red
    def __set_red(self, value):
        self.sprite.red = value
    red = property(__get_red, __set_red)

    def __get_green(self):
        return self.sprite.green
    def __set_green(self, value):
        self.sprite.green = value
    green = property(__get_green, __set_green)

    def __get_blue(self):
        return self.sprite.blue
    def __set_blue(self, value):
        self.sprite.blue = value
    blue = property(__get_blue, __set_blue)

    def __get_alpha(self):
        return self.sprite.alpha
    def __set_alpha(self, value):
        self.sprite.alpha = value
    alpha = property(__get_alpha, __set_alpha)


class Decoration(GameItem):

    def __init__(self, name, **kwargs):
        if 'scale' not in kwargs:
            kwargs['scale'] = uniform(0.5, 2)
        if 'rot' not in kwargs:
            kwargs['rot'] = uniform(0, 360)
        GameItem.__init__(self, name, **kwargs)


class Tank(GameItem):

    def __init__(self, **kwargs):
        GameItem.__init__(self, 'tank.png', **kwargs)
        self.keystate = key.KeyStateHandler()
        self.speed = 0.0

    def update(self, time, dt):
        if self.keystate[key.SPACE]:
            self.speed += 0.6
        if self.keystate[key.LEFT]:
            self.rot += 3
        elif self.keystate[key.RIGHT]:
            self.rot -= 3

        self.speed *= 0.98
        self.x -= self.speed * sin(radians(self.rot))
        self.y += self.speed * cos(radians(self.rot))

