
import sys
from random import uniform

import pyglet

from .camera import Camera
from .color import Color
from .eventloop import Eventloop
from .gameitem import Decoration, Tank
from .options import Options
from .render import Render
from .world import World


def populate(world):
    for _ in xrange(100):
        world.add( Decoration('bush.png', green=uniform(0.6, 1)) )
        world.add( Decoration('weed.png', green=uniform(0.4, 0.7)) )
        world.add( Decoration('flower.png', rot=uniform(-35, 5), scale=0.75) )


def add_player(world):
    player = Tank(
        x=0, y=0,
        angular_velocity=20,
    )
    world.add( player )


def main():
    options = Options(sys.argv)

    world = World()
    world.background_color = Color(0.1, 0.3, 0)
    populate(world)
    add_player(world)

    window = pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        visible=False,
        resizable=True,
    )
    camera = Camera((0, 0), 800)
    render = Render(world, camera, options)

    eventloop = Eventloop(window, world, render, options)
    eventloop.run(world.update)

