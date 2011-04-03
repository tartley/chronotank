from __future__ import division

import pyglet
from pyglet.event import EVENT_HANDLED
from pyglet.window import key

from .world import World
from .screenshot import screenshot



class Eventloop(object):
    '''
    .. function:: __init__()
        
        Parses the command-line options, stores results in self.options
    '''
    def __init__(self, options):
        self.options = options
        self.window = None
        self.world = None


    def init(self, draw):
        '''
        Initialise EventLoop. Must be called before calling :func:`run` to start
        the event loop. You may pass in a pyglet.window.Window instance, or
        if it is None, we will create a (non-visible) one, using self.options
        to determine its parameters.
        '''
        self.world = World()
        self.window = pyglet.window.Window(
            fullscreen=self.options.fullscreen,
            vsync=self.options.vsync,
            visible=False,
            resizable=True,
        )

        def on_draw():
            draw()
            self.window.invalid = False
            return EVENT_HANDLED

        self.window.on_draw = on_draw
        self.window.on_key_press = self.on_key_press


    def run(self, update):
        '''
        Schedules calls to self.update, makes window visible and starts the
        event loop by calling pyglet.app.run()
        '''
        pyglet.clock.schedule(self.update)
        self.window.set_visible()
        self.window.invalid = False
        try:
            pyglet.app.run()
        except:
            raise
        finally:
            if self.window:
                self.window.close()


    def update(self, dt):
        '''
        Called before every screen refresh,
        '''
        self.world.update_all(min(dt, 1 / 30.0))
        self.window.invalid = True


    def on_key_press(self, symbol, modifiers):
        '''
        Handle key presses:

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

