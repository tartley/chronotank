
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
    for _ in xrange(100):
        world.add( Greenery('bush.png', green=uniform(0.6, 1)) )
        world.add( Greenery('weed.png', green=uniform(0.4, 0.7)) )
        world.add( Greenery('flower.png', rot=uniform(-35, 5), scale=0.75) )


def add_player(world):
    player = Tank(
        x=0, y=0,
        angular_velocity=20,
    )
    world.add( player )
    return player



def main():
    options = Options(sys.argv)

    world = World()
    world.background_color = Color(0.1, 0.3, 0)
    populate(world)
    player = add_player(world)

    window = pyglet.window.Window(
        fullscreen=options.fullscreen,
        vsync=options.vsync,
        visible=False,
        resizable=True,
    )
    camera = Camera((0, 0), 800)

    def make_follow_player(player):
        def follow_player(item, time, dt):
            item.x = player.x
            item.y = player.y
        return follow_player
    camera.update = make_follow_player(player)

    render = Render(world, camera, options)
    eventloop = Eventloop(window, world, render, options)
    eventloop.run(world.update)

