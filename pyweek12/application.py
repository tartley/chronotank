
import pyglet
from pyglet.event import EVENT_HANDLED

from .camera import Camera
from .cameraman import CameraMan
from .collide import Collide
from .keyboard import Keyboard
from .render import Render
from .world import World

class Application(object):

    def __init__(self, options):
        self.options = options
        self.world = World()
        self.collide = Collide(self.world)
        self.window = pyglet.window.Window(
            fullscreen=self.options.fullscreen,
            vsync=self.options.vsync,
            visible=False,
            resizable=True,
        )
        self.camera = Camera((0, 0), scale=16)
        self.window.on_resize = self.camera.on_resize
        self.cameraman = CameraMan( self.camera )
        self.render = Render(self.world, self.camera, self.options)
        self.keyboard = Keyboard(self.window, self.world, self.options)

    def on_update(self, raw_dt):
        dt = min(raw_dt, 1 / 30.0)
        self.collide.update()
        self.world.update(dt)
        self.window.invalid = True
        self.cameraman.update(dt)

    def on_draw(self):
        self.render.draw()
        self.window.invalid = False
        return EVENT_HANDLED

    def run(self):
        '''
        Schedules calls to update, makes window visible and starts the
        event loop by calling pyglet.app.run()
        '''
        pyglet.clock.schedule(self.on_update)
        self.window.on_draw = self.on_draw
        self.window.set_visible()
        self.window.invalid = False
        try:
            pyglet.app.run()
        except:
            raise
        finally:
            self.window.close()

