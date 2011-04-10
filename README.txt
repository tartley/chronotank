Temporal Stability Breach
-------------------------

An UNFINISHED game for PyWeek 12

The game is severely not finished. Once you've seen the first
ten seconds, you've seen everything there is to see.

https://bitbucket.org/tartley/pyweek12


Drivel
------

Your tank accidentally fell into a time-machine. Ooopsie!

Emerging bleary-eyed from the resulting timestorm, you seem to have emerged in
a jungle, amongst stone ruins.

Searching for a route back to civilisation, you find that the heavy mayan stone
doors respond to pressure plates in the floor[1]. Surely there is some way to
trigger the pressure plate so that you can get through?

Your thoughts are distracted by a sound from the timestorm behind you...

[1] not yet implemented.


Reqirements
-----------

sudo apt-get install:
    libglu-dev
    libavbin0
    libavbin-dev

Then for Python2.6, 'easy_install' or 'pip install':
    pyrex
    pyglet
    rabbyt


Command-line
------------

python -O run_game.py [OPTIONS]

    --novsync   : don't use vsync
    --window    : don't start fullscreen
    --fps       : show framerate


Keyboard
--------

    WASD or arrow keys: movement

    alt-enter: toggle fullscreen
    f12: toggle framerate
    f9: screenshot


Problems
--------

The frame rate is low (~30fps) on Ubuntu, on my modest lappy, not sure why.

Sometimes segfaults on Ubuntu when playing sound. Try --silent. :-(

