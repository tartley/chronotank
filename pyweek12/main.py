
import sys
from random import uniform

import pyglet

from .camera import Camera
from .color import Color
from .eventloop import Eventloop
from .gameitem import Greenery
from .options import Options
from .render import Render
from .tank import Tank
from .world import World


def populate(world):
    for _ in xrange(300):
        world.add( Greenery('bush.png', green=uniform(0.6, 1)) )
        world.add( Greenery('weed.png', green=uniform(0.4, 0.7)) )
        world.add( Greenery('flower.png', rot=uniform(-35, 5), scale=0.75) )


def add_player(world):
    player = Tank(x=0, y=0)
    world.add( player )
    return player


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
        self.player = add_player(self.world)

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
    
