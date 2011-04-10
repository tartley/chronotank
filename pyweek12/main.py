import sys

import pyglet

from .options import Options
options = Options(sys.argv)

if options.audio:
    pyglet.options['audio'] = (options.audio, 'silent')

from .application import Application
from . import audio
from .color import Color
from .items.greenery import Tree, Weed, Flower, Fronds
from .items.hudmessage import LivesMessage, TimeMessage
from .items.portals import EntryPortal
from .items.tank import Tank
from .items.wall import Wall


print "The game isn't finished - you can just drive around and that's it."


def populate(world):
    for _ in xrange(200):
        world.add( Tree() )
        world.add( Weed() )
        world.add( Flower() )
        world.add( Fronds() )

    room_size = 800

    for roomx in [-2, 0, +2]:
        for roomy in [-3, -1, +1, +3]:
            world.add(
                Wall(
                    x=roomx * room_size, y=roomy * room_size, scale_x=3, rot=0
                )
            )
            world.add(
                Wall(
                    x=roomy * room_size, y=roomx * room_size, scale_x=3, rot=90
                )
            )

    world.add( EntryPortal(0, 0) )


class Game(Application):

    def __init__(self, options):
        Application.__init__(self, options)
        self.world.background_color = Color(0.1, 0.3, 0)
        populate(self.world)
        self.lives = 9
        pyglet.clock.schedule_once( self.start, 2)
        audio.play(options.audio)

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
    Game(options).run()

