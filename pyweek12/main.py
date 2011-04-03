
import sys
from os.path import join
from random import uniform

import pyglet
from rabbyt.sprites import Sprite

from .camera import Camera
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
        x=0, y=0,
        scale=2.0,
        rot=45,
    )
    def randomize_rot(*_):
        item.rot = uniform(0,360)
    item.update = randomize_rot
    world.add(item)
    window = pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        visible=False,
        resizable=True,
    )
    camera = Camera((0, 0), 100)
    render = Render(world, camera, options)
    eventloop = Eventloop(window, world, render, options)
    eventloop.run(world.update)

