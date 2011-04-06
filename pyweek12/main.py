
import sys
from random import uniform

import pyglet

from .camera import Camera
from .color import Color
from .eventloop import Eventloop
from .greenery import Tree, Weed, Flower, Fronds
from .options import Options
from .render import Render
from .tank import Tank
from .world import World


def populate(world):
    for _ in xrange(200):
        world.add( Tree() )
        world.add( Weed() )
        world.add( Flower() )
        world.add( Fronds() )


class CameraMan(object):

    def __init__(self, camera, get_follow):
        self.camera = camera
        self.get_follow = get_follow

    def update(self, _, __):
        follow = self.get_follow()
        if follow is not None:
            self.camera.x = follow.x
            self.camera.y = follow.y


class Application(object):

    def __init__(self):
        self.options = Options(sys.argv)
        self.world = World()
        self.world.background_color = Color(0.1, 0.3, 0)
        populate(self.world)
        self.player = Tank(x=0, y=0)
        self.world.add( self.player )
        self.window = pyglet.window.Window(
            fullscreen=self.options.fullscreen,
            vsync=self.options.vsync,
            visible=False,
            resizable=True,
        )
        self.camera = Camera((0, 0), 800)
        self.window.on_resize = self.camera.on_resize
        self.camera_man = CameraMan(self.camera, lambda: self.player)
        self.world.add(self.camera_man)
        self.render = Render(self.world, self.camera, self.options)
        self.eventloop = Eventloop(
            self.window, self.world, self.render, self.options
        )

    def run(self):
        self.eventloop.run(self.world.update)


def main():
    Application().run()
    
