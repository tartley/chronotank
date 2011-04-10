Temporal Stability Breach
-------------------------

An UNFINISHED game for PyWeek 12

The game is severely not finished. Once you've seen the first
ten seconds, you've seen everything there is to see.

https://bitbucket.org/tartley/pyweek12


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

Sometimes segfaults on Ubuntu when playing sound. :-(

