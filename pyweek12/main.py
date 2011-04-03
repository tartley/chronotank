
import sys

from .eventloop import Eventloop
from .options import Options
from .world import World
from .render import Render


def main():
    options = Options(sys.argv)
    world = World()
    eventloop = Eventloop(options)
    render = Render(world, options)
    eventloop.init(render.draw)
    eventloop.run(world.update)

