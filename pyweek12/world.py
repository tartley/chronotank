
from .color import Color
from .event import Event

class World(object):
    '''
    A collection of all the GameItems to be updated and rendered.
    Supports iteration through all added items, and indexing by item.id
    to get a particular item.
    
    Attributes:
    
    ``self.items``: a dict of all items that have been added, keyed by their
        shape.id attribute.

    ``self.item_added``: event which is fired after an item is added.

    ``self.item_removed``: event which is fired after an item is removed.

    ``self.background_color``: color used to clear the screen before render
    '''
    def __init__(self):
        self.items = {}
        self.item_added = Event()
        self.item_removed = Event()
        self.background_color = Color.Orange

    def __iter__(self):
        return self.items.itervalues()

    def __getitem__(self, itemid):
        return self.items[itemid]

    def add(self, item, position=None):
        '''
        add given item to the world. If position is not given, the item's
        existing position attribute is used.

        if item is one of a few special types (e.g. Tank, EntryPortal) then
        populate attributes to remember which item it is (e.g. self.player,
        self.entryportal)

        Fires the self.item_added event.
        '''
        self.items[id(item)] = item
        self.item_added.fire(item)

    def remove(self, item):
        '''
        remove the given item from the world.

        if item is one of our special item attributes (e.g. item.player,
        item.entryportal) then set that attribute to None.

        Fires the self.item_removed event.
        '''
        del self.items[id(item)]
        if item is self.player:
            self.player = None
        if item is self.entryportal:
            self.entryportal = None
        self.item_removed.fire(item)
        item.position = None

    def update(self, dt):
        '''
        Calls item.update() on each item that has a populated update attribute.
        Fires the self.update event.
        '''
        for item in self:
            if hasattr(item, 'update'):
                item.update(dt)

