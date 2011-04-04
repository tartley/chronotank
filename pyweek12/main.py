
import sys
from os.path import join
from random import uniform

import pyglet
from rabbyt.sprites import Sprite

from .camera import Camera
from .color import Color
from .eventloop import Eventloop
from .options import Options
from .path import DATA
from .render import Render
from .world import World


def main():
    options = Options(sys.argv)
    world = World()
    world.background_color = Color(0.1, 0.3, 0)

    def rotate(item, _, dt):
        item.rot += item.angular_velocity * dt

    for _ in xrange(100):
        for image in ['bush.png', 'flower.png', 'weed.png']:
            item = Sprite(
                join(DATA, 'images', image),
                x=uniform(-2000, 2000),
                y=uniform(-2000, 2000),
                scale=uniform(0.5, 1),
                rot=uniform(0, 360),
                green=uniform(0.6, 1),
            )
            world.add(item)

    item = Sprite(
        join(DATA, 'images', 'tank.png'),
        x=0, y=0,
        scale=1,
    )
    item.update = rotate
    item.angular_velocity = 20
    world.add(item)

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

