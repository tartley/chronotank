
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

    def rotate(item, *_):
        item.rot += item.angular_velocity

    for _ in xrange(100):
        item = Sprite(
            join(DATA, 'images', 'car.png'),
            x=uniform(-100, 100),
            y=uniform(-100, 100),
            scale=uniform(0.1, 0.5),
            rot=uniform(0, 360),
        )
        item.update = rotate
        item.angular_velocity = uniform(-0.1, +0.1)
        world.add(item)

    item = Sprite(
        join(DATA, 'images', 'tank.png'),
        x=uniform(-100, 100),
        y=uniform(-100, 100),
        scale=uniform(0.1, 0.5),
        rot=uniform(0, 360),
    )
    item.update = rotate
    item.angular_velocity = uniform(-0.1, +0.1)
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

