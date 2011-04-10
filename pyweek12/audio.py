
from os.path import join

from pyglet.media import load, Player

from .path import DATA

def play(audio):
    if audio != 'silent':
        player1 = Player()
        player1.queue( load( join(DATA, 'chronotank.ogg') ) )
        player1.queue( load( join(DATA, 'imagine_a_world.ogg') ) )
        player1.play()

        player2 = Player()
        player2.eos_action = Player.EOS_LOOP
        player2.queue( load( join(DATA, 'stupidsongimadenofarting.ogg') ) )
        player2.play()

