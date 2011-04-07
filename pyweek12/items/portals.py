
from random import uniform

from .gameitem import GameItem

class EntryPortal(GameItem):
    image_name = 'explosion.png'
    layer = 3 # treetops

    def __init__(self, x, y, **kwargs):
        GameItem.__init__(self, **kwargs)
        self.x = x
        self.y = y

    def update(self, time, dt):
        self.rot = uniform(0, 360)
        self.scale = uniform(1, 2)

