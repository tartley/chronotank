
from rabbyt.collisions import aabb_collide_single

from .items.tank import Tank

class Collide(object):

    def __init__(self, world):
        self.world = world
        self.tanks = []
        self.items_to_check = []
        world.item_added += self.item_added
        world.item_removed += self.item_removed

    def item_added(self, item):
        if item.collide:
            self.items_to_check.append(item)
        elif isinstance(item, Tank):
            self.tanks.append(item)

    def item_removed(self, item):
        if item.collide:
            self.items_to_check.remove(item)
        elif isinstance(item, Tank):
            self.tanks.remove(item)

    def update(self):
        for tank in self.tanks:
            collisions = aabb_collide_single(tank, self.items_to_check)
            if collisions:
                tank.speed = 0

