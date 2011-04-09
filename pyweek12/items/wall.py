
from random import choice, uniform

from .gameitem import GameItem

class Wall(GameItem):

    image_name = 'wall.png'
    layer = 0 # ground level

    def __init__(self, **kwargs):
        GameItem.__init__(self, **kwargs)
        self.randomise_position(exclude_radius=1000)
        self.scale = uniform(0.5, 2)
        self.rot = choice([0, 90, 180, 270])

