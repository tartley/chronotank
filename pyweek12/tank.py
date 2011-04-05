from math import cos, sin, radians

from pyglet.window import key

from .gameitem import GameItem


class Tank(GameItem):

    def __init__(self, **kwargs):
        GameItem.__init__(self, 'tank.png', **kwargs)
        self.keystate = key.KeyStateHandler()
        self.speed = 0.0

    def update(self, time, dt):

        if self.keystate[key.UP] or self.keystate[key.W]:
            self.speed += 0.4
        elif self.keystate[key.DOWN] or self.keystate[key.S]:
            self.speed *= 0.8

        if self.keystate[key.LEFT] or self.keystate[key.A]:
            self.rot += 3
        elif self.keystate[key.RIGHT] or self.keystate[key.D]:
            self.rot -= 3

        self.speed *= 0.99
        self.x -= self.speed * sin(radians(self.rot))
        self.y += self.speed * cos(radians(self.rot))

