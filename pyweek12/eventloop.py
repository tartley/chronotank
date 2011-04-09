from __future__ import division

import pyglet
from pyglet.event import EVENT_HANDLED


class Eventloop(object):
    '''
    .. function:: __init__(window, world, render, options)
    '''
    def __init__(self, window, world, render, options):
        self.window = window
        self.world = world
        self.render = render
        self.options = options


    def run(self, update):
        '''
        Schedules calls to update, makes window visible and starts the
        event loop by calling pyglet.app.run()
        '''
        def on_draw():
            self.render.draw()
            self.window.invalid = False
            return EVENT_HANDLED

        pyglet.clock.schedule(self.update)
        self.window.on_draw = on_draw
        self.window.set_visible()
        self.window.invalid = False
        try:
            pyglet.app.run()
        except:
            raise
        finally:
            self.window.close()


    def update(self, dt):
        '''
        Called before every screen refresh,
        '''
        self.world.update_all(min(dt, 1 / 30.0))
        self.window.invalid = True

