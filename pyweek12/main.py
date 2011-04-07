
import sys

import pyglet

from .camera import Camera
from .cameraman import CameraMan
from .color import Color
from .eventloop import Eventloop
from .items.greenery import Tree, Weed, Flower, Fronds
from .items.portals import EntryPortal
from .options import Options
from .render import Render
from .items.tank import Tank
from .world import World


def populate(world):
    for _ in xrange(200):
        world.add( Tree() )
        world.add( Weed() )
        world.add( Flower() )
        world.add( Fronds() )
    world.add( EntryPortal(0, 0) )
    

class Application(object):

    def __init__(self):
        self.options = Options(sys.argv)
        self.world = World()
        self.world.background_color = Color(0.1, 0.3, 0)
        populate(self.world)
        #self.world.add( Tank(x=0, y=0, speed=8) )
        self.window = pyglet.window.Window(
            fullscreen=self.options.fullscreen,
            vsync=self.options.vsync,
            visible=False,
            resizable=True,
        )
        self.camera = Camera((0, 0), 16)
        self.window.on_resize = self.camera.on_resize
        self.camera_man = CameraMan(self.camera, lambda: self.world.entryportal)
        self.world.add(self.camera_man)
        self.render = Render(self.world, self.camera, self.options)
        self.eventloop = Eventloop(
            self.window, self.world, self.render, self.options
        )

    def run(self):
        self.eventloop.run(self.world.update)


def main():
    Application().run()
    
