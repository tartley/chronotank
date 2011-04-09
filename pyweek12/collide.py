
from rabbyt.collisions import aabb_collide_single

from .items.tank import Tank

class Collide(object):

    def __init__(self, world):
        self.world = world
        self.player = None
        self.items = []
        world.item_added += self.item_added
        world.item_removed += self.item_removed

    def item_added(self, item):
        if item.collide:
            self.items.append(item)
        elif isinstance(item, Tank):
            self.player = item

    def item_removed(self, item):
        if item.collide:
            self.items.remove(item)
        elif item == self.player:
            self.player = None

    def update(self):
        if self.player:
            collisions = aabb_collide_single(self.player, self.items)

