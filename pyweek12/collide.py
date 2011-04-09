
class Collide(object):

    def __init__(self, world):
        self.items = []
        world.item_added += self.item_added
        world.item_removed += self.item_removed

    def item_added(self, item):
        if item.collide:
            self.items.append(item)

    def item_removed(self, item):
        if item.collide:
            self.items.remove(item)

    def update(self):
        pass

