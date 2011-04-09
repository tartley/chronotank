
from pyglet.window import key

from .screenshot import screenshot


class Keyboard(object):

    def __init__(self, window, world, options):
        self.window = window
        self.world = world
        self.options = options

        self.keystate = key.KeyStateHandler()
        window.push_handlers(self.keystate)

        self.window.on_key_press = self.on_key_press

        # if any items already in the world have key state handlers, then
        # bind the window key events to them
        for item in world:
            self.on_item_added(item)
        self.world.item_added += self.on_item_added
        self.world.item_removed += self.on_item_removed


    def on_item_added(self, item):
        if hasattr(item, 'keystate'):
            item.keystate = self.keystate
        #  not tested this, but expect it will be reqd:
        #if hasattr(item, 'on_key_press'):
            #window.push_handler(item.on_key_press)

    def on_item_removed(self, item):
        if hasattr(item, 'keystate'):
            item.keystate = None


    def on_key_press(self, symbol, modifiers):
        '''
        Application-wide key handler, always on.

        ========= ==================
        escape    quit
        --------- ------------------
        f12       toggle fps display
        --------- ------------------
        f9        take screenshot
        --------- ------------------
        alt-enter toggle fullscreen
        ========= ==================
        '''
        if symbol == key.ESCAPE:
            self.window.dispatch_event('on_close')
        elif symbol == key.F12:
            self.options.fps = not self.options.fps
        elif symbol == key.ENTER and (modifiers & key.MOD_ALT):
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == key.F9:
            screenshot()

