
from random import uniform

from .gameitem import GameItem

class Greenery(GameItem):
    layer = 0 # ground level
    def __init__(self, **kwargs):
        GameItem.__init__(self, **kwargs)
        self.randomise_position()
        self.scale = uniform(0.5, 2)
        self.rot = uniform(0, 360)

    def randomise_position(self):
        self.x = uniform(-4000, 4000)
        self.y = uniform(-4000, 4000)

class Tree(Greenery):
    image_name = 'bush.png'
    layer = 3 # tree level
    def __init__(self, **kwargs):
        Greenery.__init__(self, **kwargs)
        self.green = uniform(0.6, 1)
        while (self.x*self.x + self.y*self.y) < 1000**2:
            self.randomise_position()

class Fronds(Tree):
    image_name = 'fronds.png'
    layer = 3 # tree level
    def __init__(self, **kwargs):
        Tree.__init__(self, **kwargs)
        self.green = uniform(0.5, 1)
        
class Flower(Greenery):
    image_name = 'flower.png'
    def __init__(self, **kwargs):
        Greenery.__init__(self, **kwargs)
        self.scale = uniform(0.5, 1)
        self.rot = uniform(-20, 20)

class Weed(Greenery):
    image_name = 'weed.png'
    def __init__(self, **kwargs):
        Greenery.__init__(self, **kwargs)
        self.green = uniform(0.4, 0.7)

