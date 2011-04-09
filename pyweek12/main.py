
import sys

import pyglet

from .camera import Camera
from .cameraman import CameraMan
from .color import Color
from .eventloop import Eventloop
from .items.greenery import Tree, Weed, Flower, Fronds
from .items.hudmessage import LivesMessage, TimeMessage
from .items.portals import EntryPortal
from .items.tank import Tank
from .keyboard import Keyboard
from .options import Options
from .render import Render
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
        self.window = pyglet.window.Window(
            fullscreen=self.options.fullscreen,
            vsync=self.options.vsync,
            visible=False,
            resizable=True,
        )
        self.camera = Camera((0, 0), scale=16)
        self.window.on_resize = self.camera.on_resize
        self.cameraman = CameraMan(
            self.camera, lambda: self.world.entryportal)
        self.world.add(self.cameraman)
        self.render = Render(self.world, self.camera, self.options)

        self.eventloop = Eventloop(
            self.window, self.world, self.render, self.options
        )
        self.keyboard = Keyboard(self.window, self.world, self.options)

    def run(self):
        self.eventloop.run(self.world.update)


class Game(Application):

    def __init__(self):
        Application.__init__(self)
        self.lives = 9
        pyglet.clock.schedule_once( self.start, 2)

    def start(self, dt):
        self.cameraman.scale = 800
        lives_hud = LivesMessage(9)
        time_hud = TimeMessage(4, self.window.width)
        def insert_player(_):
            if self.lives > 0:
                player = Tank(x=0, y=0, speed=8)
                self.world.add(player)
                time_hud.set_time(4)
                self.lives -= 1
                lives_hud.update_lives(self.lives)
                if self.lives > 0:
                    pyglet.clock.schedule_once(insert_player, 4)
                return player

        def insert_first_player(_):
            player = insert_player(None)
            self.cameraman.get_follow = lambda: player
            self.world.add(lives_hud)
            self.world.add(time_hud)

        pyglet.clock.schedule_once(insert_first_player, 1.5)


def main():
    Game().run()
    
