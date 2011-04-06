
from os.path import join
from random import uniform

from rabbyt.sprites import Sprite

from .path import DATA


class GameItem(object):

    image_name = None # needs overriding in derived classes
    layer = 0

    def __init__(self, **kwargs):
        if 'x' not in kwargs:
            kwargs['x'] = uniform(-4000, 4000)
        if 'y' not in kwargs:
            kwargs['y'] = uniform(-4000, 4000)
        self.sprite = Sprite(
            join(DATA, 'images', self.image_name),
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

