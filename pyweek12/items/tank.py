from math import cos, sin, radians

from pyglet.window import key

from .gameitem import GameItem


class Tank(GameItem):

    image_name = 'tank.png'
    layer = 2

    def __init__(self, **kwargs):
        self.keystate = None
        self.speed = 0.0
        GameItem.__init__(self, **kwargs)

    def update(self, dt):
        if self.keystate[key.UP] or self.keystate[key.W]:
            self.speed += 0.5
        elif self.keystate[key.DOWN] or self.keystate[key.S]:
            self.speed *= 0.9

        if self.keystate[key.LEFT] or self.keystate[key.A]:
            self.rot += 2
        elif self.keystate[key.RIGHT] or self.keystate[key.D]:
            self.rot -= 2

        self.speed *= 0.99
        self.x -= self.speed * sin(radians(self.rot))
        self.y += self.speed * cos(radians(self.rot))

