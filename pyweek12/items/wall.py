
from random import choice, uniform

from .gameitem import GameItem


class Wall(GameItem):

    image_name = 'wall.png'
    layer = 2 # player level
    collide = True

    def __init__(self, **kwargs):
        GameItem.__init__(self, **kwargs)

