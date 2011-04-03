
import sys
from os.path import join

import pyglet
from rabbyt.sprites import Sprite

from .eventloop import Eventloop
from .options import Options
from .path import DATA
from .render import Render
from .world import World


def main():
    options = Options(sys.argv)
    world = World()
    item = Sprite(
        join(DATA, 'images', 'car.png'),
        x=10,y=20,scale=2.0,rot=45,
    )
    world.add(item)
    window = pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        visible=False,
        resizable=True,
    )
    render = Render(world, options)
    eventloop = Eventloop(window, world, render, options)
    eventloop.run(world.update)

